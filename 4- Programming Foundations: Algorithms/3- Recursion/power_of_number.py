def power_of_number(n, power):
    if power == 0:
        return 1
    else:
        return n * power_of_number(n, power-1)

print(f"5 power 3 = {power_of_number(5, 3)}")
print(f"100 power 5 = {power_of_number(100, 5)}")
