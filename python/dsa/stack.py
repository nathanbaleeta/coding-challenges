"""A class representing a Last-In, First-Out (LIFO) stack data structure."""
    

class Stack:

    def __init__(self):
        """Initialize list to act as internal stack storage"""
        self._items = []

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self._items) == 0
    
    def push(self, item):
        """Add item on top of the stack"""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item i.e from tail of stack
        
        Raises IndexError is stack is empty
        """
        if self.is_empty():
            return IndexError("Cannot pop from an empty stack")
        return self._items.pop(-1)
    
    def peek(self):
        """Return item at top of stack

        Raises IndexError is stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack")
        return self._items[-1]

    def size(self):
        """Return the total number of items currently in the stack."""
        return len(self._items)
    
    def __str__(self):
        """Return a user-friendly string representation of the stack."""
        return f"Stack({self._items})"


## Test cases
if __name__ == "__main__":

    # Instantiate a new stack instance
    my_stack = Stack()

    # Push elements into the stack
    my_stack.push("Webpage 1")
    my_stack.push("Webpage 2")
    my_stack.push("Webpage 3")
    print(my_stack)  # Output: Stack: ['Webpage 1', 'Webpage 2', 'Webpage 3']

    # Check the top item and total size
    print("Top item:", my_stack.peek())  # Output: Top item: Webpage 3
    print("Total size:", my_stack.size()) # Output: Total size: 3

    # Remove elements in LIFO order
    print("Popped item:", my_stack.pop())  # Output: Popped item: Webpage 3
    print(my_stack)  # Output: Stack: ['Webpage 1', 'Webpage 2']
