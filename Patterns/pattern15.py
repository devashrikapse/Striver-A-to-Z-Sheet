def pattern15(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65+j),end="")
        print()
pattern15(4)