class Queue:
    def __init__(self):
        self.array = []

    # Add at the end
    def queue(self, element):
        self.array.append(element)

    # Remove the oldest element
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.array.pop(0)

    # Return if the queue is empty or not
    def is_empty(self):
        return len(self.array) == 0


queue = Queue()
queue.queue(10)
queue.queue(20)
queue.queue(30)

assert queue.dequeue() == 10, "Element should be 10"

queue.queue(40)

assert queue.dequeue() == 20, "Element should be 20"

queue.dequeue()
queue.dequeue()

assert queue.is_empty(), "Queue should be empty"
