def pattern19(n):
    for i in range (n):

        for j in range(n-i):
            print("*", end="")
        for j in range(i*2):
            print(" ", end="")
        for j in range(n-i):
            print("*", end="")
        print()

    for i in range (1, n+1):
    
            for j in range(i):
                print("*", end="")
            for j in range(2*(n-i)):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            print()

pattern19(4)
    


