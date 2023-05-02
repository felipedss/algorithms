
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # Add to front
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Return front item
    def top_front(self):
        if self.head == None:
            raise Exception("The head is empty!")
        return self.head.data

    # Remove front item
    def pop_front(self):
        if self.head == None:
            raise Exception("The head is empty!")
        self.head = self.head.next    

    # Add to back
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_head = self.head
            while new_head.next != None:
                new_head = new_head.next
            new_head.next = new_node       

    # Return back item
    def top_back(self):
        new_head = self.head
        while new_head.next != None:
            new_head = new_head.next
        return new_head.data  
        
        

linked_list = LinkedList()
linked_list.push_front(10)
linked_list.push_front(20)
linked_list.push_front(30)

assert linked_list.top_front() == 30, "Top front should be 30"

# Remove 30 at the beggining
linked_list.pop_front()

assert linked_list.top_front() == 20, "Top front should be 20"

# Add 40 at the end
linked_list.push_back(40)

# Add 50 at the end
linked_list.push_back(50)

assert linked_list.top_back() == 50, "Pop front should be 20"