def check_armstrong(n):

    original = n
    temp = n
    num = 0
    sum1 = 0

    while temp > 0:
        num += 1
        temp //= 10

    temp = n

    while temp > 0:
        digit = temp % 10

        new_n = 1

        for i in range (num):
            new_n *= digit

        sum1 += new_n
        temp //= 10

    
    return original  == sum1

result = check_armstrong(153)
print(result)

"""def check_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    return total == original"""