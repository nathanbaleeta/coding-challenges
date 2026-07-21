"""
Goal: Write a recursive function that flattens a deeply nested tuple of arbitrary depth into a single, flat tuple.
"""

def flatten_tuple(tup: tuple) -> tuple:
    flat = []
    for i in tup:
        if isinstance(i, tuple):
            flat.extend(flatten_tuple(i))
        else:
            flat.append(i)
    return tuple(flat)
        

## Test cases
if __name__ == "__main__":
    print(flatten_tuple( (1, (2, 3), (4, (5, 6))) )  )              # return    (1, 2, 3, 4, 5, 6)
    print(flatten_tuple((1, (2, 3, (4, (5, 6))), 7, (8,))))         # return    (1, 2, 3, 4, 5, 6, 7, 8)