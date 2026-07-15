'''
Goal: Write a function that takes a tuple and an element. If the element exists in the tuple, return its index. If it doesn't, return -1. Do not let the code throw a ValueError.
'''

"""
def find_element(tup: tuple, element) -> int:
    for key, value in enumerate(tup):
        if value == element:
            return key
    return -1
"""

def find_element(tup: tuple, element) -> int:
    if element in tup:
        return tup.index(element) 
    else:
        return -1

        
# Test cases
if __name__ == "__main__": 
    print(find_element(("Alice", 28, "Engineer"), 28))
    print(find_element(("Apple", ), "Pie"))
    