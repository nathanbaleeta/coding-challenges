'''
Goal: Given a list of integers nums, write a function that returns the second largest distinct number. 
Return None if fewer than two distinct numbers exist. 
'''

def second_largest(nums: list[int]) -> int | None:
    unique = set(nums)

    if len(unique) < 2:
        return None
    return sorted(unique)[-2]

# Test cases
if __name__ == "__main__":
    print(second_largest([10, 5, 20, 20, 8])) # return 10
    print(second_largest([7, 7, 7])) # return None