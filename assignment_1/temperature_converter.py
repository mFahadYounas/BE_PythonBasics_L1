def temp_converter(temp, unit: str):
    if unit.lower() == "celsius":
        print(f"{temp * 9 / 5 + 32} Fahrenheit")
    elif unit.lower() == "fahrenheit":
        print(f"{((temp - 32) * 5) / 9} Celsius")
    else:
        print("Invalid unit")


temp_converter(32, "fahrenheit")
