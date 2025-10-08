def fib_seq(n):
    output = [0, 1]
    i = 2
    while i < n:
        output.append(output[i - 1] + output[i - 2])
        i += 1
    return output

print(fib_seq(10))