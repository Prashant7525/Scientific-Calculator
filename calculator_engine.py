import ast
import math
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}


CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}


def evaluate(expression, angle_mode="DEG"):
    """
    Safely evaluate a mathematical expression.

    angle_mode:
        DEG - degrees
        RAD - radians
    """

    tree = ast.parse(expression, mode="eval")

    return evaluate_node(
        tree.body,
        angle_mode
    )


def evaluate_node(node, angle_mode):

    # Numbers
    if isinstance(node, ast.Constant):

        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Invalid value")

    # Constants
    if isinstance(node, ast.Name):

        if node.id in CONSTANTS:
            return CONSTANTS[node.id]

        raise ValueError("Unknown constant")

    # Binary operations
    if isinstance(node, ast.BinOp):

        if type(node.op) not in OPERATORS:
            raise ValueError("Operator not allowed")

        left = evaluate_node(
            node.left,
            angle_mode
        )

        right = evaluate_node(
            node.right,
            angle_mode
        )

        if isinstance(node.op, ast.Div) and right == 0:
            raise ZeroDivisionError

        return OPERATORS[type(node.op)](
            left,
            right
        )

    # Positive / negative values
    if isinstance(node, ast.UnaryOp):

        if isinstance(node.op, ast.UAdd):
            return +evaluate_node(
                node.operand,
                angle_mode
            )

        if isinstance(node.op, ast.USub):
            return -evaluate_node(
                node.operand,
                angle_mode
            )

        raise ValueError("Operator not allowed")

    # Functions
    if isinstance(node, ast.Call):

        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function")

        function_name = node.func.id

        allowed_functions = {
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
        }

        if function_name in allowed_functions:

            if len(node.args) != 1:
                raise ValueError(
                    "Function requires one argument"
                )

            argument = evaluate_node(
                node.args[0],
                angle_mode
            )

            return allowed_functions[
                function_name
            ](argument)

        # Trigonometric functions
        if function_name in ["sin", "cos", "tan"]:

            if len(node.args) != 1:
                raise ValueError(
                    "Function requires one argument"
                )

            argument = evaluate_node(
                node.args[0],
                angle_mode
            )

            if angle_mode == "DEG":
                argument = math.radians(argument)

            elif angle_mode != "RAD":
                raise ValueError(
                    "Invalid angle mode"
                )

            if function_name == "sin":
                return math.sin(argument)

            if function_name == "cos":
                return math.cos(argument)

            return math.tan(argument)

        raise ValueError("Function not allowed")

    raise ValueError("Invalid expression")