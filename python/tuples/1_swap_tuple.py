'''
Goal: Write a function that takes a tuple of two elements and returns a new tuple with the elements swapped. Do this in a single line of code inside the function.
'''

def swap_tuple(tup: tuple) -> tuple:
    # Your code here
    return tup[::-1]
        
# Test cases
if __name__ == "__main__": 
    print(swap_tuple(("first", "last")))
    print(swap_tuple(("one", "two", "three")))  
    print(swap_tuple(("small", "medium", "large", "Extra large")))  
