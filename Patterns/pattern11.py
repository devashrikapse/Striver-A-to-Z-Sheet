def pattern11(n):
    for i in range(n):
        if i % 2 == 0:
            num = 1
        else:
            num = 0

        for j in range(i+1):
            print(num, end="")
            num = 1 - num
        print()
pattern11(4)
