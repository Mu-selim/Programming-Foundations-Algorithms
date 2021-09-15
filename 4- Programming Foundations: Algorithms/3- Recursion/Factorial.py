def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"5! = {factorial(5)}")
print(f"6! = {factorial(6)}")
print(f"7! = {factorial(7)}")