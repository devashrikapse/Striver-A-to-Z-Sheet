def print_numbers(n, count, total):
        
    if count == n+1:
        return total
    
    total += count

    return print_numbers(n, count+1, total) 


result = print_numbers(4, 1, 0)
print(result)