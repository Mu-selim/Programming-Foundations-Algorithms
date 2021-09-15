# determine if a list is sorted


list1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
list2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(l):
    temp = len(l)-1
    for i in range(1, temp):
        if (l[i] < l[i-1]):
            return "List is not sorted"
    return "List is sorted"

print(is_sorted(list1))
print(is_sorted(list2))
