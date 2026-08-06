def find_GDC(n,m):

    small = min(n, m)

    GDC = 0

    for i in range(1, small+1):
        if n % i == 0 and m % i == 0:
            GDC = i
    return GDC

result = find_GDC(25,50)
print(result)
