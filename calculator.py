import math

print("===== Scientific Calculator v1.1 =====")

print("""
Choose an operation:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Square Root
7. Sine
8. Cosine
9. Tangent
10. Logarithm (base 10)
11. Natural Logarithm
12. Factorial
13. Show π
14. Show e
""")

choice = int(input("Enter your choice (1-14): "))

if choice in [1, 2, 3, 4, 5]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        result = num1 + num2

    elif choice == 2:
        result = num1 - num2

    elif choice == 3:
        result = num1 * num2

    elif choice == 4:
        if num2 == 0:
            result = "Error: Cannot divide by zero"
        else:
            result = num1 / num2

    elif choice == 5:
        result = num1 ** num2

elif choice == 6:
    num = float(input("Enter a number: "))

    if num < 0:
        result = "Error: Cannot find square root of a negative number"
    else:
        result = math.sqrt(num)

elif choice in [7, 8, 9]:
    angle = float(input("Enter angle in degrees: "))
    radians = math.radians(angle)

    if choice == 7:
        result = math.sin(radians)

    elif choice == 8:
        result = math.cos(radians)

    elif choice == 9:
        result = math.tan(radians)

elif choice == 10:
    num = float(input("Enter a number: "))

    if num <= 0:
        result = "Error: Logarithm is only defined for positive numbers"
    else:
        result = math.log10(num)

elif choice == 11:
    num = float(input("Enter a number: "))

    if num <= 0:
        result = "Error: Natural logarithm is only defined for positive numbers"
    else:
        result = math.log(num)

elif choice == 12:
    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        result = "Error: Factorial is not defined for negative numbers"
    else:
        result = math.factorial(num)

elif choice == 13:
    result = math.pi

elif choice == 14:
    result = math.e

else:
    result = "Invalid choice"

print("Result:", result)