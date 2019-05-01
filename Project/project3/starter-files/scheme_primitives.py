"""This file implements built-in Scheme procedures."""

from scheme_core import *
import functools
import operator
import sys

_PRIMITIVES = []

def primitive(*names):
    """Returns a decorator that creates a primitive procedure from its
    argument for each name in names and adds it to the _PRIMITIVES
    list. See examples of using primitive() as a decorator below."""
    def decorate(fn):
        for name in names:
            pass # fill in with your solution
        return fn
    return decorate

def add_primitives(env):
    """Adds the set of primitive variables and procedures to the given
    environment."""
    # Primitive procedures
    for procedure in _PRIMITIVES:
        pass # fill in with your solution

def check_type(val, predicate, k, name):
    """Raises a SchemeError if not PREDICATE(VAL) using "argument K of
    NAME" to describe the offending value."""
    if not predicate(val):
        msg = "argument {0} of {1} has wrong type ({2})"
        raise SchemeError(msg.format(k, name, type(val).__name__))
    return val

# Basic predicates

@primitive('boolean?')
def scheme_booleanp(x):
    return x is True or x is False

@primitive('not')
def scheme_not(x):
    return not is_scheme_true(x)

@primitive('eq?')
def scheme_eqp(x, y):
    return x == y

@primitive('pair?')
def scheme_pairp(x):
    return isinstance(x, Pair)

@primitive('null?')
def scheme_nullp(x):
    return x is nil

@primitive('list?')
def scheme_listp(x):
    """Return whether x is a well-formed list. Assumes no cycles."""
    return is_scheme_list(x)

# Pair/list operations

@primitive('length')
def scheme_length(x):
    if x is nil:
        return 0
    check_type(x, scheme_listp, 0, 'length')
    return len(x)

@primitive('cons')
def scheme_cons(x, y):
    return Pair(x, y)

@primitive('car')
def scheme_car(x):
    check_type(x, scheme_pairp, 0, 'car')
    return x.first

@primitive('cdr')
def scheme_cdr(x):
    check_type(x, scheme_pairp, 0, 'cdr')
    return x.second

@primitive('list')
def scheme_list(*vals):
    result = nil
    for i in range(len(vals)-1, -1, -1):
        result = Pair(vals[i], result)
    return result

@primitive('append')
def scheme_append(*vals):
    if len(vals) == 0:
        return nil
    result = vals[-1]
    for i in range(len(vals)-2, -1, -1):
        v = vals[i]
        if v is not nil:
            check_type(v, scheme_pairp, i, 'append')
            r = p = Pair(v.first, result)
            v = v.second
            while scheme_pairp(v):
                p.second = Pair(v.first, result)
                p = p.second
                v = v.second
            result = r
    return result

# Type predicates

@primitive('string?')
def scheme_stringp(x):
    return is_scheme_string(x)

@primitive('symbol?')
def scheme_symbolp(x):
    return is_scheme_symbol(x)

@primitive('number?')
def scheme_numberp(x):
    return isinstance(x, int) or isinstance(x, float)

@primitive('integer?')
def scheme_integerp(x):
    return isinstance(x, int) or (scheme_numberp(x) and round(x) == x)

@primitive('procedure?')
def scheme_procedurep(x):
    return is_scheme_procedure(x)

# Arithmetic operations

def _check_nums(*vals):
    """Check that all arguments in VALS are numbers."""
    for i, v in enumerate(vals):
        if not scheme_numberp(v):
            msg = 'operand {0} ({1}) is not a number'
            raise SchemeError(msg.format(i, v))

def _convert_integral(val):
    """Converts the given value to an int if it is representable as an
    int."""
    return round(val) if round(val) == val else val

@primitive('+')
def plus(arg0, *args):
    _check_nums(arg0, *args)
    return _convert_integral(sum((arg0,) + args))

# define - and * according to the Scheme specification
# define / to produce a float rather than a rational, but
#   otherwise match the Scheme specification
# implement all three forms of - and / in the Scheme spec
# convert the result to an int if it is integral, using the
#   _convert_integral() function above

@primitive('quotient')
def scheme_quo(val0, val1):
    try:
        _check_nums(val0, val1)
        return operator.floordiv(val0, val1)
    except ZeroDivisionError as err:
        raise SchemeError(err)

@primitive('modulo', 'remainder')
def scheme_modulo(val0, val1):
    try:
        _check_nums(val0, val1)
        return operator.mod(val0, val1)
    except ZeroDivisionError as err:
        raise SchemeError(err)

@primitive('floor')
def scheme_floor(val):
    _check_nums(val)
    return math.floor(val)

@primitive('ceiling')
def scheme_ceiling(val):
    _check_nums(val)
    return math.ceil(val)

# Numerical comparisons and predicates

@primitive('=')
def scheme_eq(arg0, arg1, *args):
    _check_nums(arg0, arg1, *args)
    args = (arg1,) + args
    for i in range(len(args)):
        if arg0 != args[i]:
            return False
    return True

# define <, <=, >, and >= as well

# Numerical predicates

@primitive('even?')
def scheme_evenp(x):
    _check_nums(x)
    return x % 2 == 0

@primitive('odd?')
def scheme_oddp(x):
    _check_nums(x)
    return x % 2 == 1

@primitive('zero?')
def scheme_zerop(x):
    _check_nums(x)
    return x == 0

@primitive('positive?')
def scheme_positivep(x):
    _check_nums(x)
    return x > 0

@primitive('negative?')
def scheme_negativep(x):
    _check_nums(x)
    return x < 0

# Apply

# define apply to take in a procedure and an argument list
# example: (apply + (list 1 2 3)) should result in 6

# Other operations

@primitive('display')
def scheme_display(val):
    if scheme_stringp(val):
        val = eval(val)
    print(scheme_to_string(val), end='', flush=True)
    return okay

@primitive('newline')
def scheme_newline():
    print()
    sys.stdout.flush()
    return okay

@primitive('exit')
def scheme_exit():
    raise EOFError
