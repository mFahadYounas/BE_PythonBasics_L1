def data_type_verifier(val, intype):
    type_map = {
        'integer': int,
        'string': str,
        'float': float,
    }
    return isinstance(val, type_map[intype])

print(data_type_verifier(3, 'float'))