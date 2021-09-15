# Using HashTable
# key --> value

item1 = dict({"key1": "One", "key2": "Two", "key3": "Three"})
print(item1)

item2 = {}
item2["key1"] = 1
item2["key3"] = 3
item2["key2"] = 2
item2["key4"] = 4
print(item2)

item2["key2"] = 20
print(item2)
print()

for key, value in item2.items():
    print(f"Key: {key}, value: {value}")