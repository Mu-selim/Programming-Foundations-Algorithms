def countdown(n):
    if n == 0:
        print(n)
        return 
    else:
        print(n," ", end="")
        return countdown(n-1)

countdown(5)
countdown(20)