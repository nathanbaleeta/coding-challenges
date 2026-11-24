'''
Given a list of integers nums, flatten a list nested to any depth.
'''

def flatten_nested_list(nums: list[int]):
    for num in nums:
        if isinstance(num, list):
            yield from flatten_nested_list(num)
        else:
            yield num


# Test cases
if __name__ == "__main__":
    print(list(flatten_nested_list([1, [2, [3, [4]], 5]]))) # returns [1, 2, 3, 4, 5]
    print(list(flatten_nested_list([1, 2, [3, 4], 5, [6, 7, 8]]))) # returns [1, 2, 3, 4, 5, 6, 7, 8]
