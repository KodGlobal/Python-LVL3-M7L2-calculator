def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Unknown operation."


def main():
    print("Simple Calculator. Enter two numbers and choose an operation.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    result = calculate(num1, num2, operation)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()