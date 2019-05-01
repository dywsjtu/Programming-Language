"""
range.py

A simplified version of Python's range type.
"""

from math import ceil

class Range:
    """Represents a fixed sequence of integers, with an inclusive
    start, an exclusive end, and a step value between adjacent
    integers in the sequence."""

    def __init__(self, start, stop, step=1):
        """Constructs this range to have the given start, stop, and
        step. Requires start, stop, and step to be integers, and step
        to be positive."""
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """Returns an iterator object over this sequence."""
        return RangeIter(self.start, self.stop, self.step)

    def __len__(self):
        """Returns the length of this sequence."""
        pass # replace with your code

    def __contains__(self, i):
        """Returns whether or not the given integer is a member of
        this range."""
        pass # replace with your code

class RangeIter:
    """An iterator over a range of integers."""
    def __init__(self, start, stop, step):
        """Constructs this iterator with the given start, stop, and
        step. Requires start, stop, and step to be integers, and step
        to be positive."""
        pass # replace with your code

    def __iter__(self):
        """Returns this object."""
        return self

    def __next__(self):
        """Returns the next item in the sequence. Raises a
        StopIteration if there are no more items."""
        pass # replace with your code

def test():
    """Basic test cases for Range."""
    r = Range(1, 1)
    assert len(r) == 0
    r = Range(1, 5)
    assert len(r) == 4
    r = Range(1, 5, 3)
    assert len(r) == 2
    assert 1 in r
    assert 4 in r
    assert 3 not in r
    assert 7 not in r
    items = []
    for i in Range(-3, 11, 3):
        items.append(i)
    assert items == [-3, 0, 3, 6, 9]

if __name__ == '__main__':
    test()
