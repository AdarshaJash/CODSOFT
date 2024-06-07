def calculator():
    print(" WELCOME to the Simple Calculator Python Program. ")
    num1 = float(input(" Enter the first number: "))
    num2 = float(input(" Enter the second number: "))
    print(" Select an operation: ")
    print(" 1. Addition (+) ")
    print(" 2. Subtraction (-) ")
    print(" 3. Multiplication (*) ")
    print(" 4. Division (/) ")
    operation = input(" Enter the number corresponding to the operation (1/2/3/4): ")
    if operation == '1':
        result = num1 + num2
        operation_symbol = '+'
    elif operation == '2':
        result = num1 - num2
        operation_symbol = '-'
    elif operation == '3':
        result = num1 * num2
        operation_symbol = '*'
    elif operation == '4':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
        operation_symbol = '/'
    else:
        return "Invalid operation choice."
    return f"The result of {num1} {operation_symbol} {num2} is {result}."
print(calculator())
print("\n Thank You for using the Python Simple Calculator. ")
print(" Designed by ADARSHA JASH. ")