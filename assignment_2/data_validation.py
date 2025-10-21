from email_validator import validate_email, EmailNotValidError


def data_type_verifier(val, input_type: str) -> bool:
    type_map = {
        "integer": int,
        "string": str,
        "float": float,
    }
    if input_type != "email":
        return isinstance(val, type_map[input_type])
    try:
        _ = validate_email(val, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


print(data_type_verifier("your@gmail.com", "email"))
