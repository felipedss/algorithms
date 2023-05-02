# Quadratic Time: O(n^2)
def quadratic_function(lst, size):
    for i in range(size):
        for j in range(size):
            print("Iteration : ", i, "Element of list at ", j, " is ", lst[j])

quadratic_function([1, 2, 3, 4], 4)