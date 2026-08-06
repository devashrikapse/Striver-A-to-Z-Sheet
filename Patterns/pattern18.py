def pattern18(n):
    char=n
    for i in range(1, n+1):
        for j in range(i):
            print(chr(65+n-i+j), end="")
        print()
       

pattern18(4)