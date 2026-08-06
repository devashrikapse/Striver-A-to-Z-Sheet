def reverse_number(n):

    if n == 0:
        return 1

    new_n = 0

    while n > 0:
        digit = n % 10
        new_n = new_n * 10 + digit 
        n //= 10


    return new_n

result = reverse_number(123)
print(result)


