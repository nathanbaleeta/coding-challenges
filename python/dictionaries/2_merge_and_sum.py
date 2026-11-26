"""
Goal: Combine two dictionaries into a single dictionary and sum the values of common keys. 
If a key exists in both, sum their values.
"""

def merge_and_sum(dict1: dict, dict2: dict) -> dict:

    result = dict1.copy()  # Start with a copy of the first dictionary so as not to modify it

    for key, value in dict2.items():
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value
    return result


# Test cases
if __name__ == "__main__":
    d1 = {"a": 100, "b": 200, "c": 300, "e": 500}
    d2 = {"a": 300, "b": 200, "d": 400}
    print(merge_and_sum(d1, d2)) # # Expected Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}

