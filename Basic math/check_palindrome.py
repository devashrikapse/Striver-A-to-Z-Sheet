def check_palindrome(n):

    new_n = 0
    original = n

    while n > 0:
        digit = n % 10
        new_n = new_n * 10 + digit
        n //= 10

    return original == new_n

result = check_palindrome(121)
print(result)