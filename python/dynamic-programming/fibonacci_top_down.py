
# Time complexity = O(n) - with memoization
# Spacial complexity = O(n) 

memo = {}

def fibonacci(number):

    if number in memo:
        return memo[number]

    if (number == 0):
        result =  0
    elif (number == 1):
        result = 1
    else:
        result = fibonacci(number - 1) + fibonacci(number - 2)

    memo[number] = result

    return result

print(fibonacci(10))    

