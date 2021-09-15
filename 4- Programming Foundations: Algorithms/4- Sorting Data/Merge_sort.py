"""
Merge Sort Algorithm

-> Divide and conquer algorithm
-> Breaks a dataset into individual pieces and merge them
-> Uses recursion to operate on dataset
-> Perform well on large sets of data
-> In general has a performance of O(n log n) time complexity "Log Linear"
"""

def merge_sort(dataset):
    if len(dataset) > 1:
        # Finding the mid of the arrays
        mid = len(dataset) // 2

        # Divide array into left and right
        left_array = dataset[:mid]
        right_array = dataset[mid:] 

        # sorting left half
        merge_sort(left_array)
        # sorting right half
        merge_sort(right_array)

        right = 0 # Initial index of right subarray
        left = 0 # Initial index of left subarray
        merged = 0 # Initial index of merged subarray
        
        len_right = len(right_array)
        len_left = len(left_array)

        # Copy data to temp arrays right_array and left_array
        while right < len_right and left < len_left:
            if right_array[right] < left_array[left]:
                dataset[merged] = right_array[right]
                right += 1
            else:
                dataset[merged] = left_array[left]
                left += 1
            merged += 1

        # Checking if any element was left
        while left < len_left:
            dataset[merged] = left_array[left]
            left += 1
            merged += 1

        while right < len_right:
            dataset[merged] = right_array[right]
            right += 1
            merged += 1


def main():
    list1 = [80, -15, 14, -50, 14, 7, -8, 44, 100, 46, -67, 15, 20]
    list2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(f"Fisrt list before sorting: {list1}")
    merge_sort(list1)
    print(f"Fisrt list after sorting: {list1}")
    print()
    print(f"Second list before sorting: {list2}")
    merge_sort(list2)
    print(f"Second list after sorting: {list2}")

if __name__ == "__main__":
    main()