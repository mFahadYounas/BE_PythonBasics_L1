def fib_seq(seq_len: int) -> list[int]:
    if seq_len == 1:
        return [0]
    if seq_len <= 0:
        return []

    output = [0, 1]
    i = 2
    while i < seq_len:
        output.append(output[i - 1] + output[i - 2])
        i += 1

    return output
