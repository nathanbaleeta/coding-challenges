"""
Goal: Write a function that takes a tuple with duplicate elements and returns a new tuple containing only the unique elements while keeping their original order.
"""

def unique_elements(tup: tuple) -> tuple:
    temp_set = set(tup) 
    ordered_tuple = tuple(temp_set)
    return ordered_tuple 
    

## Test cases
if __name__ == "__main__":
    print(unique_elements((1, 2, 2, 3, 1)) )                # return    (1, 2, 3)