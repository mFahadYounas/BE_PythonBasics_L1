def calculator(num1: int, num2: int, operator: str) -> float:
    operator = operator.strip()
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            try:
                out = num1 / num2
            except ZeroDivisionError:
                out = num1 / 0.000000001  # Used approximate zero value
            return out
        case _:
            raise ValueError("Invalid operator!")


print(calculator(3, 0, "/"))
