def check_prime(n):

    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        return True

result = check_prime(80)
print(result)


