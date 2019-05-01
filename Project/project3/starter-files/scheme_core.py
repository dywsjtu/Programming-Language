"""This file implements the core of the Scheme interpreter, including
internal data types, special forms, and scheme_eval()."""

class SchemeError(Exception):
    """Exception indicating an error in a Scheme program."""

# Scheme representations

class SchemeExpr(object):
    """Base class for all non-primitive Scheme expressions."""
    pass # add whatever you need here

class okay(SchemeExpr):
    """Signifies an undefined value."""
    def __repr__(self):
        return "okay"

okay = okay() # Assignment hides the okay class; there is only one instance

def scheme_to_string(x):
    """Convert a Scheme object to a string."""
    if isinstance(x, bool):
        return '#t' if x else '#f'
    return str(x)


def is_scheme_true(val):
    """All values in Scheme are true except False."""
    return val is not False

def is_scheme_false(val):
    """Only False is false in Scheme."""
    return val is False

def is_scheme_string(x):
    """Scheme strings are Python strings that begin and end with
    quotes."""
    return isinstance(x, str) and x.startswith('"')

def is_scheme_symbol(x):
    """Any Python string that is not quoted is a symbol."""
    return isinstance(x, str) and not is_scheme_string(x)

def is_scheme_list(x):
    """Return whether x is a well-formed list. Assumes no cycles."""
    return x is nil or (isinstance(x, Pair) and x.is_list())

def is_scheme_procedure(x):
    """Return true if x is a primitive or user-defined Scheme
    procedure."""
    pass # replace with your solution

def is_special_form(x):
    """Return true if x is a special form."""
    pass # replace with your solution

def is_scheme_value(expr):
    """Return true if expr is a Scheme value that evaluates to
    itself."""
    return (isinstance(expr, int) or isinstance(expr, float) or
            isinstance(expr, bool) or is_scheme_string(expr) or
            is_special_form(expr) or
            is_scheme_procedure(expr))

# Evaluation

def scheme_eval(expr, env):
    """Evaluates the expr, which must represent a Scheme expression,
    in the given environment and returns the result."""
    if is_scheme_value(expr):
        return expr # values evaluate to themselves
    # fill in your solution

# Environments

def create_environment():
    """Return a new environment consisting of a single empty frame."""
    pass # fill in with your solution

# Special Forms

def add_special_forms(env):
    """Adds the set of special forms to the given environment."""
    pass # fill in with your solution

# Pairs and Scheme lists

def python_to_scheme_list(plist):
    """Construct a Scheme list from a Python sequence."""
    slist = nil
    for i in range(len(plist)):
        slist = Pair(plist[-1 - i], slist)
    return slist

class Pair(SchemeExpr):
    """A pair has two instance attributes: first and second.  For a Pair to be
    a well-formed list, second is either a well-formed list or nil.  Some
    methods only apply to well-formed lists.

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return 'Pair({0}, {1})'.format(repr(self.first), repr(self.second))

    def __str__(self):
        s = '(' + str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += ' ' + str(second.first)
            second = second.second
        if second is not nil:
            s += ' . ' + str(second)
        return s + ')'

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError('length attempted on improper list')
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError('negative index into list')
        y = self
        for _ in range(k):
            if y.second is nil:
                raise IndexError('list index out of bounds')
            elif not isinstance(y.second, Pair):
                raise TypeError('ill-formed list')
            y = y.second
        return y.first

    def __eq__(self, p):
        if not isinstance(p, Pair):
            return False
        return self.first == p.first and self.second == p.second

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError('ill-formed list')

    def is_list(self):
        """Return whether this is a well-formed list. Assumes no cycles."""
        x = self
        while x is not nil:
            if not isinstance(x, Pair):
                return False
            x = x.second
        return True


class nil(SchemeExpr):
    """The empty list"""

    def __repr__(self):
        return 'nil'

    def __str__(self):
        return '()'

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError('negative index into list')
        raise IndexError('list index out of bounds')

    def map(self, fn):
        return self


nil = nil() # Assignment hides the nil class; there is only one instance
