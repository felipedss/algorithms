# Linear Time: O(n)
def linear_function(lst, size):
    for i in range(size):
        print("Element at index", i, " has value: ", lst[i])

linear_function([1, 2, 3, 4], 4)