"""
Quick sort algorithm

-> Divide and conquer algorithm
-> Also uses recursion to perform sorting
-> Generally performs better than merge sort, O(n log n)
-> Operate in place of data
-> Worst case is O(n^2) when data is already or mostly sorted
-> No more memeory needed
"""

""" 
This Function handles sorting part of quick sort start and end
points to first and last element of an array respectively
"""
def partition(start, end, array):
      
    # Initializing pivot's index to start
    pivot_index = start 
    pivot = array[pivot_index]


    """
    This loop runs till start pointer crosses end pointer, 
    and when it does we swap the pivot with element on end pointer
    """ 
    while start < end:
          
        """
        Increment the start pointer till it finds an element greater
        than  pivot 
        """
        while start < len(array) and array[start] <= pivot:
            start += 1
              
        """
        Decrement the end pointer till it finds an element less than pivot
        """
        while array[end] > pivot:
            end -= 1
          
        """
        If start and end have not crossed each other, swap the 
        numbers on start and end
        """
        if(start < end):
            array[start], array[end] = array[end], array[start]
      
    """
    Swap pivot element with element on end pointer.
    This puts pivot on its correct sorted place.
    """
    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    """ Returning end pointer to divide the array into 2 """
    return end
      
""" The main function that implements QuickSort """
def quick_sort(start, end, array):
      
    if (start < end):
          
        """ p is partitioning index, array[p] is at right place """
        p = partition(start, end, array)
          
        """ Sort elements before partition and after partition """
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)



def main():
    array1 = [10, 7, 8, 9, 1, 5]
    array2 = [-7, 51, 42, 84, 29, -56, 10, 2, -4, -3, 54]
    print(f"Fisrt list before sorting: {array1}")
    quick_sort(0, len(array1) - 1, array1)
    print(f"Fisrt list after sorting: {array1}")
    print()
    print(f"Second list before sorting: {array2}")
    quick_sort(0, len(array2) - 1, array2)
    print(f"Fisrt list after sorting: {array2}")

if __name__ == "__main__":
    main()