from email_validator import validate_email, EmailNotValidError


def data_type_verifier(val, input_type: str) -> bool:
    input_type = input_type.strip()
    input_type = input_type.lower()

    type_map = {
        "integer": int,
        "string": str,
        "float": float,
    }

    if input_type != "email":
        try:
            return isinstance(val, type_map[input_type])
        except KeyError:
            raise ValueError(
                "Invalid input_type: Input type can only be: integer, string, float or email!"
            )

    try:
        _ = validate_email(val, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


print(data_type_verifier("your@gmail.com", "email"))
