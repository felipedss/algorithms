def binary_search(array, value):
    return binary_search_recursive(array, value, 0, len(array) - 1)


def binary_search_recursive(array, value, left, right):

    if left > right:
        return False

    mid = find_middle_point(left, right)

    if array[mid] == value:
        return True
    elif value < array[mid]:
        return binary_search_recursive(array, value, left, mid - 1)
    else:
        return binary_search_recursive(array, value, mid + 1, right)


def find_middle_point(left, right):
    return left + int((right - left) / 2)


print(binary_search([1, 2, 3, 4], 2))  # True
print(binary_search([1, 2, 3, 4], 4))  # True
print(binary_search([1, 2, 3, 4], 5))  # False
