# searching for an item in an ordered list this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binary_search(n, list):
    list_len = len(list)-1
    l = 0
    r = list_len

    while l <= r:
        mid = (l+r) // 2

        if list[mid] == n:
            return f"{n} was found at index {mid+1}"

        if list[mid] < n:
            l = mid + 1
        else:
            r = mid - 1
    return f"{n} was not found at the list"


print(binary_search(23, items))
print(binary_search(87, items))
print(binary_search(250, items))