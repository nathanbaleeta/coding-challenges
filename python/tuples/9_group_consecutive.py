"""
Goal: Write a function that takes a tuple of elements and groups consecutive identical elements into a list of tuples.
"""

def group_consecutive(tup: tuple):
    result = []
    
    # initialize first group with first element
    current_group = [tup[0]]
    
    for item in tup[1:]:
        if item == current_group[0]:
            current_group.append(item)
        else:
            result.append(tuple(current_group))
            current_group = [item]
    
    # Don't forget to append the final group
    result.append(tuple(current_group))
    return result

## Test cases
if __name__ == "__main__":
    print(group_consecutive( (1, 1, 2, 3, 3, 3, 1, 1) )) # return   [(1, 1), (2,), (3, 3, 3), (1, 1)]
    print(group_consecutive( ('a', 'a', 'b', 'c', 'c', 'a'))) # return   [('a', 'a'), ('b',), ('c', 'c'), ('a',)]