"""
uccontext.py

This file defines the PhaseContext type that is used by both the
frontend and backend.
"""

import sys
import copy

class PhaseContext:
    """A class that contains contextual information required in a
    compiler phase. Instance attributes may be added dynamically as
    needed."""
    def __init__(self, phase=0, global_env=None, out=sys.stdout,
                 indent=''):
        """Initializes this context with the given phase number,
        global environment, output file, and output indentation."""
        self.phase = phase
        self.global_env = global_env
        self.out=out
        self.indent = indent
    def clone(self):
        """Return a copy of this context."""
        return copy.copy(self)
    def print_noln(self, *args, **kwargs):
        """Print to this context's output file, without a trailing
        newline."""
        print(*args, file=self.out, end='', **kwargs)
    def print(self, *args, **kwargs):
        """Print to this context's output file, with a trailing
        newline."""
        print(*args, file=self.out, **kwargs)
    def print_in_noln(self, *args, **kwargs):
        """Print to this context's output file, beginning with this
        context's indentation, without a trailing newline."""
        print(self.indent, file=self.out, end='')
        print(*args, file=self.out, end='', **kwargs)
    def print_in(self, *args, **kwargs):
        """Print to this context's output file, beginning with this
        context's indentation, with a trailing newline."""
        print(self.indent, file=self.out, end='')
        print(*args, file=self.out, **kwargs)
