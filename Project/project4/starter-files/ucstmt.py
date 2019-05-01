"""
ucstmt.py

This file contains definitions of AST nodes that represent uC
statements.
"""

from ucbase import *
from ucerror import *
from uctypes import *

@astnode('statements')
class BlockNode(ASTNode):
    """An AST node representing a block of statements. statements is a
    list of statement nodes."""
    pass # replace if necessary with your code

@astnode()
class StatementNode(ASTNode):
    """The base class for all statement nodes."""
    pass # replace if necessary with your code

@astnode('test', 'then_block', 'else_block')
class IfNode(StatementNode):
    """An AST node representing an if statement. test is the
    condition, then_block is a block representing the then case, and
    else_block is a block representing the else case."""
    pass # replace with your code

@astnode('test', 'body')
class WhileNode(StatementNode):
    """An AST node representing a while statement. test is the
    condition and body is a block representing the body."""
    pass # replace with your code

@astnode()
class BreakNode(StatementNode):
    """An AST node representing a break statement."""
    pass # replace with your code

@astnode()
class ContinueNode(StatementNode):
    """An AST node representing a continue statement."""
    pass # replace with your code

@astnode('expr')
class ReturnNode(StatementNode):
    """An AST node representing a return statement. expr is the return
    expression if there is one, None otherwise."""
    pass # replace with your code

@astnode('expr')
class ExpressionStatementNode(StatementNode):
    """An AST node representing a statement consisting of just an
    expression. expr is the expression."""
    pass # replace if necessary with your code
