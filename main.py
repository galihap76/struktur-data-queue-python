class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue size:", queue.size())  # Output: 3
print("Front item:", queue.front())  # Output: 10

dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)  # Output: 10

print("Is queue empty?", queue.is_empty())  # Output: False
