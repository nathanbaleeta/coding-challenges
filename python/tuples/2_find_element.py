'''
Goal: You are given a tuple containing a user's first name, last name, age, and city. 
Write a function that unpacks these values and returns a formatted string: "First Last is Age years old and lives in City."
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
    