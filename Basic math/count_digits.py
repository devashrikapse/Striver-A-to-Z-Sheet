def count_digit(n):

    if n == 0:
        return 1
    
    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count

result = count_digit(14)
print(result)
        
