from email_validator import validate_email, EmailNotValidError

def data_type_verifier(val, intype):
    type_map = {
        'integer': int,
        'string': str,
        'float': float,
    }
    if intype != 'email':
        return isinstance(val, type_map[intype])
    else:
        try:
            v = validate_email(val, check_deliverability=False)
            return True
        except EmailNotValidError:
            return False

print(data_type_verifier("your@gmail.com", 'email'))