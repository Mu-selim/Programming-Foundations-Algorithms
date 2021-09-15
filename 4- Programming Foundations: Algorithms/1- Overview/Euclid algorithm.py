# Using Euclid's Algorithm

def greater_common_divisior(a, b):
    if a < b:
        (a, b) = (b, a)
    divisor = a / b
    remainder = a % b
    while remainder != 0:
        a = b
        b = remainder
        remainder = a % b
    return b

print(greater_common_divisior(8, 20))
print(greater_common_divisior(60, 96))
