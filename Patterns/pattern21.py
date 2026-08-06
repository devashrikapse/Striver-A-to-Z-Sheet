def pattern21(n):
    for i in range(n):

        if i == 0 or i == n-1:
            for j in range(n):
                print("*", end="")
        else:
            for j in range(1):
                print("*",end="")
            for j in range(n-2):
                print(" ", end="")
            for j in range(1):
                print("*",end="")

        print()
pattern21(4)

