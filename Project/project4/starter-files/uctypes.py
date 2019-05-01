"""
uctypes.py

This file contains definitions of classes that represent uC types, as
well as utility functions that operate on types.
"""

from ucerror import *

class Type:
    """Parent class for all uC types."""
    def __init__(self, name):
        """Initialize this type to have the given name."""
        self.name = name
        self._array_type = None # cache for the array type
    def __str__(self):
        """Returns the name of this type."""
        return self.name
    @property
    def array_type(self):
        """Return the array type corresponding to this type."""
        if not self._array_type:
            self._array_type = ArrayType(self)
        return self._array_type
    def lookup_field(self, phase, position, name, global_env):
        """Lookup up a field in this type. phase is the current
        compiler phase, position is the source position from where
        this lookup occurs, name is the name of the field, and
        global_env is the global environment. Reports an error if the
        field is not found. Returns the type of the field if it is
        found, int otherwise."""
        error(phase, position,
              'type {0} has no field {1}'.format(self.name, name))
        return global_env.lookup_type(phase, position, 'int')
    def mangle(self):
        """Returns the name of this type that should be used in code
        generation."""
        return '_UC_TYPE({0})'.format(self.name)

class ArrayType(Type):
    """A class representing an array type. The instance attribute
    elem_type refers to the element type of the array."""
    def __init__(self, elem_type):
        """Initialize this type to have the given name and element
        type."""
        super().__init__(elem_type.name + '[]')
        self.elem_type = elem_type
    def mangle(self):
        """Returns the name of this type that should be used in code
        generation."""
        return '_UC_ARRAY({0})'.format(self.elem_type.mangle())
    def check_args(self, phase, position, args):
        """Checks if the given arguments are compatible with the
        element type of this array. The arguments must have already
        have their types computed. phase is the current compiler
        phase, position is the source position where this check
        occurs. Reports an error if an argument is incompatible."""
        return False # replace with your solution
    def lookup_field(self, phase, position, name, global_env):
        """Lookup up a field in this type. phase is the current
        compiler phase, position is the source position from where
        this lookup occurs, name is the name of the field, and
        global_env is the global environment. Reports an error if the
        field is not found. Returns the type of the field if it is
        found, int otherwise."""
        # fill in your solution here
        return global_env.lookup_type(phase, position, 'int')

class PrimitiveType(Type):
    """A class representing a primitive type."""
    def __init__(self, name):
        """Initialize this type to have the given name."""
        super().__init__(name)
    def mangle(self):
        """Returns the name of this type that should be used in code
        generation."""
        return '_UC_PRIMITIVE({0})'.format(self.name)

class UserType(Type):
    """A class representing a user-defined type."""
    def __init__(self, name, decl):
        """Initialize this type. name is the name of the type and decl
        is the AST node for the declaration of this type."""
        super().__init__(name)
        self.decl = decl
        self.fields = decl.vardecls
    def check_args(self, phase, position, args):
        """Checks if the given arguments are compatible with the field
        types of this type. The arguments must have already have their
        types computed. phase is the current compiler phase, position
        is the source position where this check occurs. Reports an
        error if an argument is incompatible."""
        return False # replace with your solution
    def lookup_field(self, phase, position, name, global_env):
        """Lookup up a field in this type. phase is the current
        compiler phase, position is the source position from where
        this lookup occurs, name is the name of the field, and
        global_env is the global environment. Reports an error if the
        field is not found. Returns the type of the field if it is
        found, int otherwise."""
        # fill in your solution here
        return global_env.lookup_type(phase, position, 'int')

def is_compatible(source, target):
    """Returns whether or not the source type can be assigned to the
    target type."""
    return ((source is target) or
            (source.name == 'int' and
             target.name in ('long', 'float')) or
            (source.name == 'long' and target.name == 'float') or
            (source.name == 'null' and
             not isinstance(target, PrimitiveType)))

def is_numeric_type(type_):
    """Returns whether or not the given type is a primitive numeric
    type."""
    return type_.name in ('int', 'long', 'float')

def is_integral_type(type_):
    """Returns whether or not the given type is a primitive integral
    type."""
    return type_.name in ('int', 'long')

def join_types(phase, position, type1, type2, global_env):
    """Computes the type of a binary operation given the types of the
    two operands."""
    if type1.name == 'string' or type2.name == 'string':
        return global_env.lookup_type(phase, position, 'string')
    elif type1.name == 'float' or type2.name == 'float':
        return global_env.lookup_type(phase, position, 'float')
    elif type1.name == 'long' or type2.name == 'long':
        return global_env.lookup_type(phase, position, 'long')
    else: # default to int
        return global_env.lookup_type(phase, position, 'int')

def add_builtin_types(types):
    for name in ('int', 'long', 'float', 'boolean', 'string', 'void',
                 'null'):
        types[name] = PrimitiveType(name)
