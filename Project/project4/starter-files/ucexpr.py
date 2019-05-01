"""
ucstmt.py

This file contains definitions of AST nodes that represent uC
expressions.
"""

from ucbase import *
from ucerror import *
from uctypes import *

#############################
# Base Node for Expressions #
#############################

@astnode(type=None)
class ExpressionNode(ASTNode):
    """The base class for all nodes representing expressions. type is
    a reference to the computed uctypes.Type of this expression."""
    pass

############
# Literals #
############

@astnode(text=None)
class LiteralNode(ExpressionNode):
    """The base class for all nodes representing literals. text is the
    textual representation of the literal in generated code."""
    pass # replace if necessary with your code

@astnode('text')
class IntegerNode(LiteralNode):
    """An AST node representing an integer (int or long) literal. text
    is the literal text."""
    pass # replace with your code

@astnode('text')
class FloatNode(LiteralNode):
    """An AST node representing a float literal. text is the literal
    text."""
    pass # replace with your code

@astnode('text')
class StringNode(LiteralNode):
    """An AST node representing a string literal. text is the literal
    text."""
    pass # replace with your code

@astnode('text')
class BooleanNode(LiteralNode):
    """An AST node representing a boolean literal. text is the literal
    text."""
    pass # replace with your code

@astnode(text='nullptr')
class NullNode(LiteralNode):
    """An AST node representing the null literal, which is generated
    as nullptr."""
    pass # replace with your code

###################
# Name Expression #
###################

@astnode('name')
class NameExpressionNode(ExpressionNode):
    """An AST node representing a name expression. name is a node
    denoting the actual name."""
    pass # replace with your code

#######################
# Calls and Accessors #
#######################

@astnode('name', 'args', func=None)
class CallNode(ExpressionNode):
    """An AST node representing a function-call expression. name is a
    node representing the name of the function and args is a list of
    argument expressions to the function. func is a reference to the
    ucfunctions.Function named by this call."""
    pass # replace with your code

@astnode('name', 'args')
class NewNode(ExpressionNode):
    """An AST node representing a new expression for a simple object.
    name is a node representing the type of the object and args is a
    list of argument expressions to the constructor."""
    pass # replace with your code

@astnode('elem_type', 'args')
class NewArrayNode(ExpressionNode):
    """An AST node representing a new expression for an array.
    elem_type is a node representing the element type and args is a
    list of argument expressions representing the initial elements of
    the array."""
    pass # replace with your code

@astnode('receiver', 'field')
class FieldAccessNode(ExpressionNode):
    """An AST node representing access to a field of an object.
    receiver is an expression representing the object whose field is
    being accessed and field is is a node representing the name of the
    field."""
    pass # replace with your code

@astnode('receiver', 'index')
class ArrayIndexNode(ExpressionNode):
    """An AST node representing indexing into an array. receiver is an
    expression representing the array and index the index
    expression."""
    pass # replace with your code

#####################
# Unary Expressions #
#####################

@astnode(expr=None, op_name=None)
class UnaryPrefixNode(ExpressionNode):
    """A base AST node that represents a unary prefix operation. expr
    is the expression to which the operation is being applied and
    op_name is the string representation of the operator."""
    pass # replace if necessary with your code

@astnode()
class PrefixSignNode(UnaryPrefixNode):
    """A base AST node representing a prefix sign operation."""
    pass # replace if necessary with your code

@astnode('expr', op_name='+')
class PrefixPlusNode(PrefixSignNode):
    """An AST node representing a prefix plus operation. expr is the
    operand expression."""
    pass # replace if necessary with your code

@astnode('expr', op_name='-')
class PrefixMinusNode(PrefixSignNode):
    """An AST node representing a prefix minus operation. expr is the
    operand expression."""
    pass # replace if necessary with your code

@astnode('expr', op_name='!')
class NotNode(UnaryPrefixNode):
    """An AST node representing a not operation. expr is the operand
    expression."""
    pass # replace if necessary with your code

@astnode()
class PrefixIncrDecrNode(UnaryPrefixNode):
    """A base AST node representing a prefix increment or decrement
    operation."""
    pass # replace if necessary with your code

@astnode('expr', op_name='++')
class PrefixIncrNode(PrefixIncrDecrNode):
    """An AST node representing a prefix increment operation. expr is
    the operand expression."""
    pass # replace if necessary with your code

@astnode('expr', op_name='--')
class PrefixDecrNode(PrefixIncrDecrNode):
    """An AST node representing a prefix decrement operation. expr is
    the operand expression."""
    pass # replace if necessary with your code

######################
# Binary Expressions #
######################

# Base classes

@astnode(lhs=None, rhs=None, op_name=None)
class BinaryOpNode(ExpressionNode):
    """A base AST node that represents a binary infix operation. lhs
    is the left-hand side expression, rhs is the right-hand side
    expression, and op_name is the name of the operator."""
    pass # replace if necessary with your code

@astnode()
class BinaryArithNode(BinaryOpNode):
    """A base AST node representing a binary arithmetic operation."""
    pass # replace if necessary with your code

@astnode()
class BinaryLogicNode(BinaryOpNode):
    """A base AST node representing a binary logic operation."""
    pass # replace if necessary with your code

@astnode()
class BinaryCompNode(BinaryOpNode):
    """A base AST node representing binary comparison operation."""
    pass # replace if necessary with your code

@astnode()
class EqualityTestNode(BinaryOpNode):
    """A base AST node representing an equality comparison."""
    pass # replace if necessary with your code

# Arithmetic operations

@astnode('lhs', 'rhs', op_name='+')
class PlusNode(BinaryArithNode):
    """An AST node representing a binary plus operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace with your code

@astnode('lhs', 'rhs', op_name='-')
class MinusNode(BinaryArithNode):
    """An AST node representing a binary minus operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

@astnode('lhs', 'rhs', op_name='*')
class TimesNode(BinaryArithNode):
    """An AST node representing a binary times operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

@astnode('lhs', 'rhs', op_name='/')
class DivideNode(BinaryArithNode):
    """An AST node representing a binary divide operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

@astnode('lhs', 'rhs', op_name='%')
class ModuloNode(BinaryArithNode):
    """An AST node representing a binary modulo operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

# Logical operations

@astnode('lhs', 'rhs', op_name='||')
class LogicalOrNode(BinaryLogicNode):
    """An AST node representing a logical or operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

@astnode('lhs', 'rhs', op_name='&&')
class LogicalAndNode(BinaryLogicNode):
    """An AST node representing a logical and operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

# Arithmetic comparisons

@astnode('lhs', 'rhs', op_name='<')
class LessNode(BinaryCompNode):
    """An AST node representing a less than operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

@astnode('lhs', 'rhs', op_name='<=')
class LessEqualNode(BinaryCompNode):
    """An AST node representing a less than or equal operation. lhs is
    the left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

@astnode('lhs', 'rhs', op_name='>')
class GreaterNode(BinaryCompNode):
    """An AST node representing a greater than operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

@astnode('lhs', 'rhs', op_name='>=')
class GreaterEqualNode(BinaryCompNode):
    """An AST node representing a greater than or equal operation. lhs
    is the left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

# Equality comparisons

@astnode('lhs', 'rhs', op_name='==')
class EqualNode(EqualityTestNode):
    """An AST node representing an equality comparison. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

@astnode('lhs', 'rhs', op_name='!=')
class NotEqualNode(EqualityTestNode):
    """An AST node representing an inequality comparison. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace if necessary with your code

# Other binary operations

@astnode('lhs', 'rhs', op_name='=')
class AssignNode(BinaryOpNode):
    """An AST node representing an assignment operation. lhs is the
    left-hand operand and rhs is the right-hand operand."""
    pass # replace with your code

@astnode('lhs', 'rhs', op_name='<<')
class PushNode(BinaryOpNode):
    """An AST node representing an array insertion operation. lhs is
    the left-hand operand and rhs is the right-hand operand."""
    pass # replace with your code

@astnode('lhs', 'rhs', op_name='>>')
class PopNode(BinaryOpNode):
    """An AST node representing an array extraction operation. lhs is
    the left-hand operand and rhs is the right-hand operand."""
    pass # replace with your code

#############
# Utilities #
#############

def is_lvalue(node):
    """Returns whether or not the given node produces an l-value."""
    return false # replace with your solution
