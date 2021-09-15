# use a hashtable to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

unique_list = {}
for item in items:
    unique_list[item] = 0

print(items)
print(unique_list)
answer = set(unique_list.keys())
print(answer)