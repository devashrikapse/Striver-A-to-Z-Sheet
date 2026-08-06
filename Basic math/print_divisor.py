def print_divisor(n):

    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")

print_divisor(27)

