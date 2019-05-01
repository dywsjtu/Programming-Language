def memoize(fn):
    """Return a function that computes the same result as fn, but
    if a given set of arguments has already been seen before,
    returns the previously computed result instead of repeating
    the computation. Assumes fn is a pure function (i.e. has no
    side affects), and that all arguments to fn are hashable.

    >>> @memoize
    ... def sum_to_n(n):
    ...     return 1 if n == 1 else n + sum_to_n(n - 1)
    >>> try:
    ...     sum_to_n(300)
    ...     sum_to_n(600)
    ...     sum_to_n(900)
    ...     sum_to_n(1200)
    ... except RecursionError:
    ...     print('recursion limit exceeded')
    45150
    180300
    405450
    720600
    >>> @memoize
    ... def sum_k_to_n(k, n):
    ...     return k if n == k else n + sum_k_to_n(k, n - 1)
    >>> try:
    ...     sum_k_to_n(2, 300)
    ...     sum_k_to_n(2, 600)
    ...     sum_k_to_n(2, 900)
    ...     sum_k_to_n(2, 1200)
    ... except RecursionError:
    ...     print('recursion limit exceeded')
    45149
    180299
    405449
    720599
    """
    pass # replace with your solution

def chain(*funcs):
    """Returns a function that is the compositional chain of funcs. If
    funcs is empty, returns the identity function.

    >>> chain()(3)
    3
    >>> chain(lambda x: 3 * x)(3)
    9
    >>> chain(lambda x: x + 1, lambda x: 3 * x)(3)
    10
    >>> chain(lambda x: x // 2, lambda x: x + 1, lambda x: 3 * x)(3)
    5
    """
    pass # replace with your solution

def scale(items, factor):
    """Produces a new iterable that contains the elements from items
    scaled by factor. Consumes the elements from items.

    >>> def naturals():
    ...     num = 0
    ...     while True:
    ...         yield num
    ...         num += 1
    >>> values = scale(naturals(), 3)
    >>> [next(values) for i in range(5)]
    [0, 3, 6, 9, 12]
    """
    pass # replace with your solution

def merge(items1, items2):
    """Produces a new iterable that contains the elements in
    increasing order from items1 and items2, without duplicates.
    Requires each of items1 and items2 to be infinite iterables in
    monotonically increasing order. Consumes the elements from items1
    and items2.

    >>> def naturals():
    ...     num = 0
    ...     while True:
    ...         yield num
    ...         num += 1
    >>> values = merge(naturals(), naturals())
    >>> [next(values) for i in range(5)]
    [0, 1, 2, 3, 4]
    >>> values2 = merge(scale(naturals(), 2), scale(naturals(), 3))
    >>> [next(values2) for i in range(10)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14]
    """
    pass # replace with your solution

def make_s():
    """Produces an iterable over all positive integers that only have
    2, 3, or 5 as factors.

    >>> values = make_s()
    >>> [next(values) for i in range(18)]
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30]
    """
    pass # replace with your solution
