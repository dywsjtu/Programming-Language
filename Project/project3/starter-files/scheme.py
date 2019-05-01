"""This file implements the Scheme REPL and top-level driver."""

from scheme_core import *
from scheme_reader import *
from scheme_primitives import *
import readline
import sys

def read_eval_print_loop(next_line, env, quiet=False, startup=False,
                         interactive=False, load_files=()):
    """Read and evaluate input until an end of file or keyboard
    interrupt."""
    if startup:
        for filename in load_files:
            scheme_load(filename, env)

    while True:
        try:
            src = next_line()
            while src.more_on_line:
                expression = scheme_read(src)
                result = scheme_eval(expression, env)
                handle_eval_result(result, expression, quiet)
        except KeyboardInterrupt:  # <Control>-C
            if not startup:
                raise
            print('\nKeyboardInterrupt')
            if not interactive:
                return
        except EOFError:  # <Control>-D, etc.
            return
        except BaseException as err:
            if (isinstance(err, RuntimeError) and
                'maximum recursion depth exceeded' not in err.args[0]):
                # signifies some internal error in the intepreter
                raise
            print('Error:', err)

def handle_eval_result(result, expression, quiet):
    """Print the result if not quiet."""
    assert result is not None, ('scheme_eval returned None: ' +
                                str(expression))
    if not quiet:
        print(scheme_to_string(result))

def scheme_load(filename, env, quiet=True):
    """Load a Scheme source file.."""
    with scheme_open(filename) as infile:
        lines = infile.readlines()
    args = (lines, None) if quiet else (lines,)
    def next_line():
        return buffer_lines(*args)
    try:
        read_eval_print_loop(next_line, env, quiet=quiet)
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt')
        return

def scheme_open(filename):
    """If either FILENAME or FILENAME.scm is the name of a valid file,
    return a Python file opened to it. Otherwise, raise an error."""
    try:
        return open(filename)
    except IOError as exc:
        if filename.endswith('.scm'):
            raise SchemeError(str(exc))
    try:
        return open(filename + '.scm')
    except IOError as exc:
        raise SchemeError(str(exc))

def create_global_environment():
    """Initialize and return a single-frame environment with built-in
    names."""
    global_env = create_environment()
    add_primitives(global_env)
    add_special_forms(global_env)
    return global_env

if __name__ == '__main__':
    argv = sys.argv[1:]
    next_line = buffer_input
    interactive = True
    load_files = ()
    if argv:
        try:
            filename = argv[0]
            if filename == '-load':
                load_files = argv[1:]
            else:
                input_file = open(argv[0])
                lines = input_file.readlines()
                def next_line():
                    return buffer_lines(lines)
                interactive = False
        except IOError as err:
            print(err)
            sys.exit(1)
    read_eval_print_loop(next_line, create_global_environment(),
                         startup=True, interactive=interactive,
                         load_files=load_files)
    print('Bye.')
