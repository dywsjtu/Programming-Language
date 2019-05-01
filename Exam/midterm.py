# Run with python3 -m doctest midterm.py

###################
# Q3a

def make_add_nums(n):
    """Returns a list of n functions, each of which takes in an
    argument and returns i added to the argument, for i in [0, n).

    >>> funcs = make_add_nums(5)
    >>> funcs[0](3)
    7
    >>> funcs[1](3)
    7
    >>> funcs[2](3)
    7
    >>> funcs[4](3)
    7
    """
    funcs = []
    for i in range(n):
        funcs.append(lambda x: x + i)
    return funcs

###################
# Q4a

def print_arg(x):
    """Prints the value of x on its own line.

    >>> one = lambda f: lambda x: f(x)
    >>> two = lambda f: lambda x: f(f(x))
    >>> _ = one(print_arg)(3)    # assignment to suppress return value
    3
    >>> _ = two(print_arg)(3)    # assignment to suppress return value
    3
    3
    """
    print(x)
    return x

###################
# Q4b

def incr(n):
    """Returns the Church numeral that represents one more than the
    Church numeral n.

    >>> one = lambda f: lambda x: f(x)
    >>> _ = incr(one)(print_arg)(3)
    3
    3
    >>> _ = incr(incr(one))(print_arg)(3)
    3
    3
    3
    """
    return lambda f: lambda x: f(n(f)(x))

###################
# Q4c

def deep_iterate(nested_items):
    """Produces a generator that iterates over the items contained in
    the given nested-list structure, in left-to-right order. If an
    item is a list, its elements are themselves iterated over.
    Otherwise, the item is yielded by the generator.

    >>> nested_lists = [[3, [4]], [2], [], 'a']
    >>> iter = deep_iterate(nested_lists)
    >>> next(iter)
    3
    >>> next(iter)
    4
    >>> next(iter)
    2
    >>> next(iter)
    'a'
    >>> nested_lists = [[3, [0, 4, 5, [6]]], [[], 2], None, 'a']
    >>> list(deep_iterate(nested_lists))
    [3, 0, 4, 5, 6, 2, None, 'a']
    """
    for item in nested_items:
        if isinstance(item, list):
            for nitem in deep_iterate(item):
                yield nitem
        else:
            yield item
