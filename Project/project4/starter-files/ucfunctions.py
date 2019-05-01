"""
ucfunctions.py

This file contains definitions of classes that represent uC functions,
as well as utility functions that operate on functions.
"""

from ucerror import *
from uctypes import *

class Function:
    """A class that represents a uC function."""
    def __init__(self, name):
        """Initializes this function with the given name, a return
        type set to None, and an empty set of parameter types."""
        self.name = name
        self.rettype = None
        self.param_types = []
    def __str__(self):
        """Returns the name of this function."""
        return self.name
    def mangle(self):
        """Returns the name of this function that should be used in
        code generation."""
        return '_UC_FUNCTION({0})'.format(self.name)
    def check_args(self, phase, position, args):
        """Checks if the given arguments are compatible with the
        parameter types of this function. The arguments must have
        already have their types computed. phase is the current
        compiler phase, position is the source position where this
        check occurs. Reports an error if the arguments are
        incompatible with this function."""
        return False # replace with your solution

class PrimitiveFunction(Function):
    """A class that represents a primitive uC functions."""
    def __init__(self, name, rettype, param_types, type_env):
        """Initializes this function with the given name. rettype is
        the name of the return type, param_types is a sequence of
        names of the parameter types, and type_env is the dictionary
        in which to look up type names."""
        super().__init__(name)
        self.rettype = type_env[rettype]
        for p in param_types:
            self.param_types.append(type_env[p])

class UserFunction(Function):
    def __init__(self, name, decl):
        """Initializes this function with the given name, a return
        type set to None, and an empty set of parameter types. decl is
        the AST node that defines this function."""
        super().__init__(name)
        self.decl = decl
    def add_param_types(self, param_types):
        """Add the given parameter types to this functions list of
        parameter types. param_types must be a sequence of items, each
        of which must be of type uctypes.Type."""
        self.param_types += param_types

def make_conversion(target, source, type_env):
    """Creates a primitive function to convert the type named by
    source to that named by target. type_env is the dictionary in
    which to look up type names."""
    return PrimitiveFunction('{0}_to_{1}'.format(source, target),
                             target, (source,), type_env)

def add_conversions(func_env, type_env):
    """Creates all the primitive conversion functions. func_env is the
    dictionary in which to insert the conversion functions. type_env
    is the dictionary to use to look up type names."""
    types = ('int', 'long', 'float', 'string')
    for t1 in types:
        for t2 in types:
            if t1 != t2:
                func = make_conversion(t1, t2, type_env)
                func_env[func.name] = func
    func = make_conversion('boolean', 'string', type_env)
    func_env[func.name] = func
    func = make_conversion('string', 'boolean', type_env)
    func_env[func.name] = func

def add_builtin_functions(func_env, type_env):
    """Creates all the primitive uC functions. func_env is the
    dictionary in which to insert the conversion functions. type_env
    is the dictionary to use to look up type names."""
    add_conversions(func_env, type_env)
    # string functions
    func_env['length'] = PrimitiveFunction('length', 'int',
                                           ('string',), type_env)
    func_env['substr'] = PrimitiveFunction('substr', 'string',
                                           ('string', 'int', 'int'),
                                           type_env)
    func_env['ordinal'] = PrimitiveFunction('ordinal', 'int',
                                            ('string',), type_env)
    func_env['character'] = PrimitiveFunction('character', 'string',
                                              ('int',), type_env)
    # numerical functions
    func_env['pow'] = PrimitiveFunction('pow', 'float',
                                        ('float', 'float'),
                                        type_env)
    func_env['sqrt'] = PrimitiveFunction('sqrt', 'float',
                                         ('float',), type_env)
    func_env['ceil'] = PrimitiveFunction('ceil', 'float',
                                         ('float',), type_env)
    func_env['floor'] = PrimitiveFunction('floor', 'float',
                                          ('float',), type_env)
    # print functions
    func_env['print'] = PrimitiveFunction('print', 'void',
                                          ('string',), type_env)
    func_env['println'] = PrimitiveFunction('println', 'void',
                                            ('string',), type_env)

    # input functions
    func_env['peekchar'] = PrimitiveFunction('peekchar', 'string', (),
                                             type_env)
    func_env['readchar'] = PrimitiveFunction('readchar', 'string', (),
                                             type_env)
    func_env['readline'] = PrimitiveFunction('readline', 'string', (),
                                             type_env)
