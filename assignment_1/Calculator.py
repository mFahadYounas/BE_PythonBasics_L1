def calculator(num1, num2, operator):
    match(operator):
        case '+':
            print(num1 + num2)
        case '-':
            print( num1 - num2)
        case '*':
            print(num1 * num2)
        case '/':
            print(num1 / num2)
        case _:
            print("Invalid operator")      