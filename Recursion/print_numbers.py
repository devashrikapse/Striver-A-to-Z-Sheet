def print_numbers(n, count):
    
    if count == n+1:
        return

    print(count)

    print_numbers(n,count+1) 

print_numbers(10, 1)