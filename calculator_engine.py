import ast
import math
import operator


# Allowed binary operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


# Allowed mathematical functions
FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "log": math.log10,
    "ln": math.log,
}


# Allowed mathematical constants
CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}


def evaluate(expression):
    """
    Safely evaluate a mathematical expression.

    Supported operators:
    +, -, *, /, **, %

    Supported functions:
    sqrt(), sin(), cos(), tan(), log(), ln()

    Supported constants:
    pi, e
    """

    tree = ast.parse(expression, mode="eval")
    return evaluate_node(tree.body)


def evaluate_node(node):

    # Numbers
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Invalid value")

    # Constants such as pi and e
    if isinstance(node, ast.Name):

        if node.id in CONSTANTS:
            return CONSTANTS[node.id]

        raise ValueError("Unknown constant")

    # Binary operations
    if isinstance(node, ast.BinOp):

        if type(node.op) not in OPERATORS:
            raise ValueError("Operator not allowed")

        left = evaluate_node(node.left)
        right = evaluate_node(node.right)

        if isinstance(node.op, ast.Div) and right == 0:
            raise ZeroDivisionError

        return OPERATORS[type(node.op)](left, right)

    # Positive and negative numbers
    if isinstance(node, ast.UnaryOp):

        if isinstance(node.op, ast.UAdd):
            return +evaluate_node(node.operand)

        if isinstance(node.op, ast.USub):
            return -evaluate_node(node.operand)

        raise ValueError("Operator not allowed")

    # Mathematical functions
    if isinstance(node, ast.Call):

        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function")

        function_name = node.func.id

        if function_name not in FUNCTIONS:
            raise ValueError("Function not allowed")

        if len(node.args) != 1:
            raise ValueError("Function requires one argument")

        argument = evaluate_node(node.args[0])

        try:
            return FUNCTIONS[function_name](argument)

        except ValueError:
            raise ValueError("Invalid mathematical value")

    raise ValueError("Invalid expression")