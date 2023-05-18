def binary_search_iterative(array, value):

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = find_middle_point(left, right)
        if array[mid] == value:
            return True
        else:
            if value < array[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return False


def find_middle_point(left, right):
    return left + int((right - left) / 2)


print(binary_search_iterative([1, 2, 3, 4], 2))  # True
print(binary_search_iterative([1, 2, 3, 4], 4))  # True
print(binary_search_iterative([1, 2, 3, 4], 5))  # False
