def temp_converter(temperature: float, unit: str) -> float:
    unit = unit.lower()

    match unit:
        case "celsius":
            return temperature * 9 / 5 + 32
        case "fahrenheit":
            return ((temperature - 32) * 5) / 9
        case _:
            raise ValueError("Invalid unit: enter either celsius or fahrenheit!")


print(temp_converter(1, "celsius"))
