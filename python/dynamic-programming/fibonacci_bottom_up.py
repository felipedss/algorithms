
# Time complexity = O(n) 
# Spacial complexity = O(n) 
def fibonacci(number):


    if (number == 0):
        return 0
    
    if (number == 1):
        return 1

    # Instantiate an array in order to store the results of the subproblems
    fib = [0] * (number+1)
        
    fib[0] = 0
    fib[1] = 1

    for i in range(2, number + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[number]

print(fibonacci(10))    

