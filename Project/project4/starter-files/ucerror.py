"""
ucerror.py

This file defines the error-handling function used by the uC compiler.
"""

disabled = False
num_errors = 0

def error(phase, position, message):
    """If error checking is enabled, prints an error message for the
    given phase at the given source position, with the given message
    content. Increments the number of errors encountered. If error
    checking is disabled, does nothing"""
    global num_errors
    if not disabled:
        print('Error ({}) at line {}: {}'.format(phase, position,
                                                 message))
        num_errors += 1

def error_count():
    """Returns the number of errors detected in static analysis."""
    return num_errors

def disable_errors():
    """Disables error checking."""
    global disabled
    disabled = True
