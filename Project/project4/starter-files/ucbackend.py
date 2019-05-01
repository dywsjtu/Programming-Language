"""
ucbackend.py

This file implements entry points into the backend of the compiler.
"""

# NOTE: This file is for the backend project. Ignore it for the
#       frontend.

import ucbase
import ucerror
import uccontext

###################
# Code Generation #
###################

def gen_header(tree, global_env, out):
    """Generates the header for a uC program, writing it to out. The
    header includes library code written in C++."""
    ctx = uccontext.PhaseContext(0, global_env, out, '  ')
    ctx.print('#include "defs.h"')
    ctx.print('#include "ref.h"')
    ctx.print('#include "array.h"')
    ctx.print('#include "library.h"')
    ctx.print('#include "expr.h"')
    ctx.print()
    ctx.print('namespace _uc {\n')

def gen_footer(tree, global_env, out):
    """Generates the footer for a uC program, writing it to out. The
    footer bootstraps execution of a uC program."""
    ctx = uccontext.PhaseContext(0, global_env, out, '  ')
    ctx.print('} // namespace _uc\n')
    ctx.print('int main(int argc, char **argv) {')
    ctx.print('  _uc::_UC_ARRAY(_uc::_UC_PRIMITIVE(string)) args = ' +
              '_uc::_uc_make_array<_uc::_UC_PRIMITIVE(string)>();')
    ctx.print('  for (int i = 1; i < argc; i++) {')
    ctx.print('    _uc::_uc_array_push(args, ' +
              '_uc::_UC_PRIMITIVE(string)(argv[i]));')
    ctx.print('  }')
    ctx.print('  _uc::_UC_FUNCTION(main)(args);')
    ctx.print('  return 0;')
    ctx.print('}')

def gen_type_decls(tree, global_env, out):
    """Generates forward type declarations, writing them to out."""
    ctx = uccontext.PhaseContext(1, global_env, out, '  ')
    ctx.print_in('// Forward type declarations\n')
    # add your code here

def gen_function_decls(tree, global_env, out):
    """Generates forward function declarations, writing them to
    out."""
    ctx = uccontext.PhaseContext(2, global_env, out, '  ')
    ctx.print_in('// Forward function declarations\n')
    # add your code here

def gen_type_defs(tree, global_env, out):
    """Generates full type definitions, writing them to out."""
    ctx = uccontext.PhaseContext(3, global_env, out, '  ')
    ctx.print_in('// Full type definitions\n')
    # add your code here

def gen_function_defs(tree, global_env, out):
    """Generates full function definitions, writing them to out."""
    ctx = uccontext.PhaseContext(4, global_env, out, '  ')
    ctx.print_in('// Full function definitions\n')
    # add your code here
