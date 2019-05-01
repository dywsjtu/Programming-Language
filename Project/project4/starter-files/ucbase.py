"""
ucbase.py

This file contains definitions of the base AST node, declaration
nodes, global and local environments, and utility functions.
"""

from ucerror import *
from uctypes import *
from ucfunctions import *
import sys

#################
# AST Functions #
#################

def astnode(*children, **attrs):
    """Produces a decorator that takes in a definition of an AST node
    and modifies it to have the given children and attributes. A child
    is another AST node or a terminal and must be passed in upon
    initialization of a node. An attribute has an initial default
    value that is replaced during static analysis."""
    def decorate(cls):
        def __init__(self, position, *_children):
            assert(len(children) == len(_children))
            super(cls, self).__init__(position)
            self.child_names += children
            self.children += _children
            for i in range(len(children)):
                self.__dict__[children[i]] = _children[i]
            for key in attrs.keys():
                self.__dict__[key] = attrs[key]
        def __str__(self):
            result = '{' + type(self).__name__ + ':'
            for name in children:
                result += ' ' + child_str(self.__dict__[name])
            return result + '}'
        cls.__init__ = __init__
        cls.__str__ = __str__
        return cls
    return decorate

def ast_map(fn, item, terminal_fn=None):
    """Maps the given function on an AST item. If the item is a list,
    then the function is mapped across its elements. If the item is a
    terminal rather than an AST node, then terminal_fn is applied if
    given."""
    if isinstance(item, list):
        for i in item:
            ast_map(fn, i, terminal_fn)
    elif isinstance(item, ASTNode):
        fn(item)
    elif terminal_fn:
        terminal_fn(item)


################################
# Environments in the Compiler #
################################

class GlobalEnv:
    """A class that represents the global environment of a uC program.
    Maps names to types and to functions."""
    def __init__(self):
        """Initializes this environment to contain built-in types and
        functions."""
        self.types = {}
        self.functions = {}
        add_builtin_types(self.types)
        add_builtin_functions(self.functions, self.types)
    def add_type(self, phase, position, name, defnode):
        """Adds the given type to this environment. phase is the
        current compiler phase, position is the source position of the
        type definition, name is the name of the type, and defnode is
        the AST node corresponding to the definition. Reports an error
        if a type of the given name is already defined."""
        if name in self.types:
            error(phase, position, 'redefinition of type ' + name)
        else:
            self.types[name] = UserType(name, defnode)
            return self.types[name]
    def add_function(self, phase, position, name, defnode):
        """Adds the given function to this environment. phase is the
        current compiler phase, position is the source position of the
        function definition, name is the name of the function, and
        defnode is the AST node corresponding to the definition.
        Reports an error if a function of the given name is already
        defined."""
        if name in self.functions:
            error(phase, position, 'redefinition of function ' + name)
        else:
            self.functions[name] = UserFunction(name, defnode)
            return self.functions[name]
    def lookup_type(self, phase, position, name, strict=True):
        """Returns the type represented by the given name. phase is
        the current compiler phase, position is the source position
        that resulted in this lookup, name is the name of the type to
        look up. If strict is True, then an error is reported if the
        name is not found, and the int type is returned. Otherwise, if
        the name is not found, None is returned."""
        if name not in self.types:
            if strict:
                error(phase, position, 'undefined type ' + name)
                return self.types['int'] # treat it as int by default
            else:
                return None
        return self.types[name]
    def lookup_function(self, phase, position, name, strict=True):
        """Returns the function represented by the given name.
        phase is the current compiler phase, position is the source
        position that resulted in this lookup, name is the name of the
        function to look up. If strict is True, then an error is
        reported if the name is not found, and string_to_int function
        is returned. Otherwise, if the name is not found, None is
        returned."""
        if name not in self.functions:
            if strict:
                error(phase, position, 'undefined function ' + name)
                return self.functions['string_to_int'] # default
            else:
                return None
        return self.functions[name]
    def get_type_names(self):
        """Returns a sequence of all the type names in this
        environment."""
        return self.types.keys()
    def get_function_names(self):
        """Returns a sequence of all the function names in this
        environment."""
        return self.functions.keys()

class VarEnv:
    """A class that represents a local environment in a uC program.
    Maps names to types of fields, parameters, and variables."""
    def __init__(self, global_env):
        """Initializes this to an empty local environment, with the
        given global environment."""
        self.global_env = global_env
        self.var_types = {}
    def add_variable(self, phase, position, name, var_type, kind_str):
        """Inserts a variable into this environment. phase is the
        current compiler phase, position is the source position of the
        field, parameter, or variable declaration, name is the name of
        the field, variable, or parameter, var_type is its type, and
        kind_str is one of 'field, 'variable', or 'parameter'. Reports
        an error if a field, variable, or parameter of the given name
        already exists in this environment."""
        if name in self.var_types:
            error(phase, position,
                  'redeclaration of {0} {1}'.format(kind_str, name))
        else:
            self.var_types[name] = var_type
    def contains(self, name):
        """Returns whether or not the name is defined in this local
        environment."""
        return name in self.var_types
    def get_type(self, phase, position, name):
        """Looks up the given name and returns the type of the entity
        it names. phase is the current compiler phase, position is the
        source position where the name appears, and name is the name.
        Reports an error if the given name is not defined and returns
        the int type."""
        if name not in self.var_types:
            error(phase, position, 'undefined variable ' + name)
            # default to int
            return self.global_env.lookup_type(phase, position, 'int')
        return self.var_types[name]

#################
# Base AST Node #
#################

class ASTNode:
    """The base class for all AST nodes. Implements default
    functionality for an AST node."""
    next_id = 0 # used for giving each node a unique id
    def __init__(self, position):
        """Initializes this node, recording the given source position.
        Initializes the set of children to be empty."""
        self.position = position
        self.children = []
        self.child_names = []
        self.node_id = ASTNode.next_id
        ASTNode.next_id += 1
    def find_decls(self, ctx):
        """Searching this AST node for type and function declarations.
        Adds the types and functions that are found to ctx.global_env.
        Reports an error if a type or function is multiply defined."""
        ast_map(lambda n: n.find_decls(ctx), self.children)
    def resolve_types(self, ctx):
        """Matches all occurrences of a type name to the actual type
        it names. Uses ctx.global_env to look up a type name. Reports
        an error if an unknown type is named."""
        ast_map(lambda n: n.resolve_types(ctx), self.children)
    def resolve_calls(self, ctx):
        """Matches function calls to the actual function it names.
        Uses ctx.global_env to look up a function name. Reports an
        error if an unknown function is named."""
        ast_map(lambda n: n.resolve_calls(ctx), self.children)
    def check_names(self, ctx):
        """Checks the names introduced within a type or function to
        ensure they are unique in the scope of the type or
        function."""
        ast_map(lambda n: n.check_names(ctx), self.children)
    def type_check(self, ctx):
        """Computes the type of each expression. Uses ctx.local_env to
        compute the type of a local name. Checks that the type of an
        expression is compatible with the context in which it is
        used."""
        ast_map(lambda n: n.type_check(ctx), self.children)
    def basic_control(self, ctx):
        """Checks basic control flow within this AST node."""
        ast_map(lambda n: n.basic_control(ctx), self.children)
    def advanced_control(self, ctx):
        """Checks advanced control flow within this AST node."""
        ast_map(lambda n: n.advanced_control(ctx), self.children)
    def write_types(self, ctx):
        """Writes out a representation of this AST, with type
        annotations for each node that has a type, using
        ctx.print*."""
        ctx.print_in_noln(type(self).__name__)
        if 'type' in dir(self):
            ctx.print_noln(': {0}'.format(self.type.name if
                                          self.type else self.type))
        ctx.print(' {')
        new_ctx = ctx.clone()
        new_ctx.indent += '  '
        ast_map(lambda n: n.write_types(new_ctx), self.children,
                lambda c: new_ctx.print_in(c))
        ctx.print_in('}')
    def emit(self, ctx):
        """Generates code for this AST node, writing it out with
        ctx.print*. This function is specific to the backend."""
        ast_map(lambda n: n.emit(ctx), self.children)

##############
# Start Node #
##############

@astnode('decls')
class ProgramNode(ASTNode):
    """Represents a uC program."""
    pass

##########################
# Names and Declarations #
##########################

@astnode()
class DeclNode(ASTNode):
    """The base node for type and function declarations."""
    pass

@astnode('name', 'vardecls', type=None)
class StructDeclNode(DeclNode):
    """An AST node representing a type declaration. name is the name
    of the type and vardecls is a list of field declarations. type is
    the instance of uctypes.Type that is associated with this
    declaration."""
    # pass # replace with your code

@astnode('rettype', 'name', 'parameters', 'vardecls', 'body',
         func=None)
class FunctionDeclNode(DeclNode):
    """An AST node representing a function declaration. rettype is a
    node representing the return type, name is the name of the
    function, parameters is a list of parameter declarations, vardecls
    is a list of local variable declarations, and body is the body of
    the function."""
    # pass # replace with your code

@astnode('vartype', 'name')
class VarDeclNode(ASTNode):
    """An AST node representing a variable or field declaration.
    vartype is a node representing the type and name is a node
    representing the name."""
    pass # replace if necessary with your code

@astnode('name', type=None)
class TypeNameNode(ASTNode):
    """An AST node representing a type. name is a node representing
    the name of the type. type is the instance of uctypes.Type
    associated with the type named by this node."""
    pass # replace if necessary with your code

@astnode('elem_type', type=None)
class ArrayTypeNameNode(ASTNode):
    """An AST node representing an array type. elem_type is a node
    representing the element type. type is the instance of
    uctypes.Type associated with the type named by this node."""
    pass # replace if necessary with your code

@astnode('id')
class NameNode(ASTNode):
    """An AST node representing a name. id is the actual string
    containing the name."""
    pass # replace if necessary with your code

@astnode('vartype', 'name')
class ParameterNode(ASTNode):
    """An AST node representing a parameter declaration. vartype is a
    node representing the type and name is a node representing the
    name."""
    pass # replace if necessary with your code

######################
# Printing Functions #
######################

def child_str(child):
    """Converts an AST item into a string. Converts list elements to
    strings using str() rather than repr()."""
    if isinstance(child, list):
        result = '['
        if child:
            result += child_str(child[0])
        for i in range(1, len(child)):
            result += ', ' + child_str(child[i])
        return result + ']'
    return str(child)

def graph_gen(item, parent_id=None, child_num=None, child_name=None,
              out=sys.stdout):
    """Prints a graph representation of the given AST node to out, in
    a format compatible with Graphviz."""
    if isinstance(item, ASTNode):
        if parent_id:
            edge = '  {0} -> {{N{1} [label="{2}{4}"]}} [label="{3}"]'
            print(edge.format(parent_id, item.node_id,
                              type(item).__name__, child_name,
                              ' ({})'.format(item.type.name)
                              if 'type' in item.__dict__  and item.type
                              else ''),
                  file=out)
            new_parent_id = 'N{0}'.format(item.node_id)
        else:
            print('digraph {', file=out)
            new_parent_id = type(item).__name__
        for i, child in enumerate(item.children):
            graph_gen(child, new_parent_id, i, item.child_names[i],
                      out)
        if not parent_id:
            print('}', file=out)
    elif isinstance(item, list):
        edge = '  {0} -> {{{0}L{1} [label="[list]"]}} [label="{2}"]'
        print(edge.format(parent_id, child_num, child_name), file=out)
        for i, child in enumerate(item):
            graph_gen(child, '{0}L{1}'.format(parent_id, child_num),
                      i, i, out)
    else:
        edge = '  {0} -> {{{0}T{1} [label="{2}"]}} [label="{3}"]'
        print(edge.format(parent_id, child_num,
                          str(item).replace('\\', '\\\\').replace('"', '\\"'),
                          child_name),
              file=out)
