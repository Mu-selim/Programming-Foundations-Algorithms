"""
Bubble sort algorithm

-> Very simple to undersatnd and implement
-> Performance: O(n^2)
-> Other sorting algorithms are generally much better
-> Not considered to be a practical solution unless the dataset is very small
"""

def bubble_sort(dataset):
    temp = len(dataset)-1
    for i in range(temp, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                (dataset[j], dataset[j+1]) = (dataset[j+1], dataset[j])
    
        print("Current sortig state:", dataset)

def main():
    list = [6, 100, 4, -5, 20, 12, 3]
    bubble_sort(list)
    print(f"Sorted list: {list}")

if __name__ == "__main__":
    main()