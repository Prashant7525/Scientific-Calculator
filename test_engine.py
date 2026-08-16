from calculator_engine import evaluate
import math


assert evaluate("2 + 3", "DEG") == 5
assert evaluate("2 * 3", "DEG") == 6
assert evaluate("2 ** 3", "DEG") == 8
assert evaluate("10 / 2", "DEG") == 5
assert evaluate("sqrt(25)", "DEG") == 5
assert evaluate("log(100)", "DEG") == 2
assert evaluate("ln(e)", "DEG") == 1

assert math.isclose(
    evaluate("sin(90)", "DEG"),
    1.0
)

assert math.isclose(
    evaluate("cos(0)", "DEG"),
    1.0
)

assert math.isclose(
    evaluate("tan(45)", "DEG"),
    1.0
)

assert math.isclose(
    evaluate("sin(pi / 2)", "RAD"),
    1.0
)

assert math.isclose(
    evaluate("cos(0)", "RAD"),
    1.0
)

assert math.isclose(
    evaluate("tan(pi / 4)", "RAD"),
    1.0
)

try:
    evaluate("10 / 0", "DEG")
    assert False
except ZeroDivisionError:
    pass


print("All calculator engine tests passed.")