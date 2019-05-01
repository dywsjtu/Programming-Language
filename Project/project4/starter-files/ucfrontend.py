"""
ucfrontend.py

This file implements entry points into the frontend phases of the
compiler.
"""

import ucbase
import ucerror
import uccontext

#############
# Utilities #
#############

def make_global_env():
    """Returns an empty global environment."""
    return ucbase.GlobalEnv()

###################
# Frontend Phases #
###################

def find_decls(tree, global_env):
    """Searching the given AST node for type and function
    declarations. Adds the types and functions that are found to
    global_env. Reports an error if a type or function is multiply
    defined."""
    ctx = uccontext.PhaseContext(1, global_env)
    tree.find_decls(ctx)

def resolve_types(tree, global_env):
    """Matches all occurrences of a type name to the actual type it
    names in the given AST node. Uses global_env to look up a type
    name. Reports an error if an unknown type is named."""
    ctx = uccontext.PhaseContext(2, global_env)
    ctx.is_return = False # whether or not the current node is the
                          # node specifying the return type of a
                          # function
    tree.resolve_types(ctx)

def resolve_calls(tree, global_env):
    """Matches function calls to the actual function it names. Uses
    global_env to look up a function name. Reports an error if an
    unknown function is named."""
    ctx = uccontext.PhaseContext(3, global_env)
    tree.resolve_calls(ctx)

def check_names(tree, global_env):
    """Checks the names introduced within a type or function to ensure
    they are unique in the scope of the type or function."""
    ctx = uccontext.PhaseContext(4, global_env)
    tree.check_names(ctx)

def type_check(tree, global_env):
    """Computes the type of each expression. Checks that the type of
    an expression is compatible with the context in which it is used.
    Checks that a valid main function exists."""
    ctx = uccontext.PhaseContext(5, global_env)
    ctx.local_env = None # used to look up local names
    ctx.rettype = None # used to check types of return expressions
    tree.type_check(ctx)
    # check for main
    func = global_env.lookup_function(ctx.phase, tree.position,
                                      'main', False)
    if func is None:
        ucerror.error(ctx.phase, tree.position,
                      'no definition for function main')
    elif (len(func.param_types) != 1 or
          func.param_types[0] is not
          global_env.lookup_type(ctx.phase, tree.position,
                                 'string').array_type or
          func.decl.rettype.type.name != 'void'):
        ucerror.error(ctx.phase, func.decl.position,
                      'signature for main must be ' +
                      'void main(string[] <name>)')

def basic_control(tree, global_env):
    """Checks basic control flow within the given AST node."""
    ctx = uccontext.PhaseContext(6, global_env)
    ctx.in_loop = False # whether or not the current node is within a loop
    tree.basic_control(ctx)

def advanced_control(tree, global_env):
    """Checks advanced control flow within the given AST node."""
    ctx = uccontext.PhaseContext(7, global_env)
    tree.advanced_control(ctx)

def write_types(tree, global_env, out):
    """Writes out a representation of the given AST node, with type
    annotations for each node that has a type, to the given output
    file."""
    ctx = uccontext.PhaseContext(0, global_env, out)
    tree.write_types(ctx)
