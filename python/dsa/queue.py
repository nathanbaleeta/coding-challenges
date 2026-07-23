"""A Object-Oriented Queue implementation using a Python list."""

class Queue:
    
    def __init__(self):
        """Initialize an empty queue."""
        self._items = []

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self._items) == 0

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")

        return self._items.pop(0)

    def peek(self):
        """Return the front item of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue.")
        return self._items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)

    def __str__(self):
        """Return a string representation of the queue."""
        return f"Queue({self._items})"

if __name__ == "__main__":
    
    # Create an instance of the Queue
    my_queue = Queue()

    # Enqueue elements
    my_queue.enqueue("Task 1")
    my_queue.enqueue("Task 2")
    my_queue.enqueue("Task 3")
    print(my_queue)  # Output: Queue(['Task 1', 'Task 2', 'Task 3'])

    # Peek at the front element
    print(my_queue.peek())  # Output: Task 1

    # Dequeue elements (FIFO)
    print(my_queue.dequeue())  # Output: Task 1
    print(my_queue)  # Output: Queue(['Task 2', 'Task 3'])

    # Check current size
    print(my_queue.size())  # Output: 2


