"""This module implements a parser for Scheme expressions.

Pairs and lists are defined in scheme_core.py, as well as a
representation for an unspecified value. Other data types in Scheme
are represented by their corresponding type in Python:
    number:       int or float
    symbol:       string
    string:       quoted string
    boolean:      bool
"""

from scheme_tokens import tokenize_lines, DELIMITERS
from scheme_core import *
from buffer import Buffer, InputReader, LineReader

# Scheme list parser

# Quotation markers
QUOTES = {"'":  "quote",
          "`":  "quasiquote",
          ",":  "unquote",
          ",@": "unquote-splicing"}

def scheme_read(src):
    """Read the next expression from SRC, a Buffer of tokens.

    >>> lines = ["(+ 1 ", "(+ 23 4)) ("]
    >>> src = Buffer(tokenize_lines(lines))
    >>> print(scheme_read(src))
    (+ 1 (+ 23 4))
    >>> read_line("'hello")
    Pair('quote', Pair('hello', nil))
    >>> print(read_line("(car '(1 2))"))
    (car (quote (1 2)))
    """
    if src.current() is None:
        raise EOFError
    val = src.pop()
    if val not in DELIMITERS:
        return val
    elif val in QUOTES:
        pass # fill in your solution here
    elif val == "(":
        return read_tail(src)
    else:
        raise SyntaxError("unexpected token: {0}".format(val))

def read_tail(src):
    """Return the remainder of a list in SRC, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([")"])))
    nil
    >>> read_tail(Buffer(tokenize_lines(["2 3)"])))
    Pair(2, Pair(3, nil))
    >>> read_tail(Buffer(tokenize_lines(["2 (3 4))"])))
    Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
    >>> read_line("(1 . 2)")
    Pair(1, 2)
    >>> read_line("(1 2 . 3)")
    Pair(1, Pair(2, 3))
    >>> read_line("(1 . 2 3)")
    Traceback (most recent call last):
        ...
    SyntaxError: Expected one element after .
    >>> scheme_read(Buffer(tokenize_lines(["(1", "2 .", "'(3 4))", "4"])))
    Pair(1, Pair(2, Pair('quote', Pair(Pair(3, Pair(4, nil)), nil))))
    >>> print(read_line("(car `(1 2 , x ,@ '(4)))"))
    (car (quasiquote (1 2 (unquote x) (unquote-splicing (quote (4))))))
    """
    try:
        if src.current() is None:
            raise SyntaxError("unexpected end of file")
        if src.current() == ")":
            src.pop()
            return nil
        # fill in your solution here

        first = scheme_read(src)
        rest = read_tail(src)
        return Pair(first, rest)
    except EOFError:
        raise SyntaxError("unexpected end of file")

# Convenience functions

def buffer_input(prompt="scm> "):
    """Return a Buffer instance containing interactive input."""
    return Buffer(tokenize_lines(InputReader(prompt)))

def buffer_lines(lines, prompt="scm> "):
    """Return a Buffer instance iterating through LINES."""
    return Buffer(tokenize_lines(LineReader(lines, prompt)))

def read_line(line):
    """Read a single string LINE as a Scheme expression."""
    return scheme_read(Buffer(tokenize_lines([line])))

# Interactive loop

if __name__ == "__main__":
    """Run a read-print loop for Scheme expressions."""
    while True:
        try:
            src = buffer_input("read> ")
            while src.more_on_line:
                expression = scheme_read(src)
                print(expression)
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ":", err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            break
