# searching for an item in an unordered list sometimes called a Linear search

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    for i in itemlist:
        if i == item:
            return f"{item} was found in the list"
    return f"{item} was not found in the lsit"

print(find_item(87, items))
print(find_item(250, items))