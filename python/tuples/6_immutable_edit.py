"""
Goal: Because tuples are immutable, you can't change them directly. Write a function that takes a tuple, an index, and a new value.
 It should return a new tuple with the value at that index updated. If the index is out of bounds, return the original tuple.
"""

def update_tuple(tup: tuple, index: int, value) -> tuple:
    if 0 <= index < len(tup):
        temp_list = list(tup)
        temp_list[index] = value
        return tuple(temp_list)
    return tup

## Test cases
if __name__ == "__main__":
    print(update_tuple(("apple", "banana", "cherry"), 2, "avocado" ))           # return    ('apple', 'banana', 'avocado')
    print(update_tuple(("soccer", "basketball", "tennis"), 10, "golf" ))        # return    ('soccer', 'basketball', 'tennis')
    print(update_tuple(("toyota", "honda", "nissan"), -5, "mercedes" ))         # return    ('toyota', 'honda', 'nissan')