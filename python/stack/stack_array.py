
class Stack:

    def __init__(self):
        self.array = []

    # Add to top
    def push(self, element):
        self.array.append(element)

    # Get number of elements
    def get_number_of_elements(self):
        return len(self.array)

    # Remove to top
    def pop(self):
        return self.array.pop(len(self.array) - 1)

    # Return the item from the top
    def top(self):
        return self.array[len(self.array) - 1]

    # Return if the stack is empty or not
    def is_empty(self):
        return len(self.array) == 0


stack =  Stack()        
stack.push(10)

assert stack.top() == 10, "Element should be 10"

stack.push(20)
stack.push(30)

assert stack.get_number_of_elements() == 3, "Number of elements should be one"

# Remove 30
stack.pop()

assert stack.top() == 20, "Element should be 20"
assert stack.get_number_of_elements() == 2, "Number of elements should be 2"








