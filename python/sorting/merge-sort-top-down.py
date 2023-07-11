
# Time Complexity: O(n log n)
# Space complexity: O(n) - Merge sort requires additional memory to store the merged sub-arrays during the sorting process. 
def merge_sort(array):

    if len(array) == 1:
        return
    
    # Finding the mid of the array
    mid = len(array)//2

    # Dividing the array elements
    left = array[:mid]

    # Into 2 halves
    right = array[mid:]

    # Sorting the first half
    merge_sort(left)

    # Sorting the second half
    merge_sort(right)

    i = j = k = 0

    # Copy data to temp arrays left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]  
            i += 1
        else:
            array[k] = right[j]      
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# Code to print the list
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()    

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("\nSorted array is ")
print_list(arr)    