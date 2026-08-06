def pattern5(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
pattern5(4)