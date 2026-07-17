"""
Goal: Tuples can hold mixed data types. Write a function that takes a tuple and returns the sum of only the numerical elements (integers and floats).
"""

def sum_numbers(tup: tuple) -> float:
    # Note: Python treats True as 1, so filter carefully!
    ######################################
    # Solution 1:
    ######################################
    """
    sum = 0
    for i in tup:
        if type(i) in (int, float):
            sum += i
    return sum
    """

    ######################################
    # Solution 2:
    ######################################
    """
    sum = 0
    for i in tup:
        if not isinstance(i, (str, bool)):
            sum += i 
    return sum
    """

    ######################################
    # Solution 3:
    ######################################
    sum = 0
    for i in tup:
        if isinstance(i, (int, float)) and not isinstance(i, bool):
            sum += i 
    return sum

    
# Test cases
if __name__ == "__main__": 
    print(sum_numbers((1, "apple", 2.5, True, 3))) # should return 6.5