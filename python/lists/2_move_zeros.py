'''
Given a list of integers nums, move all 0s to the end while keeping the relative order of all non-zero elements.
 Do it in-place with $O(1)$ extra space.
'''

def move_zeros(nums : list[int]) -> list[int]:
    nums_copy = nums.copy()

    for num in nums:
        if num == 0:
            nums_copy.remove(num)
            nums_copy.append(num)
            
    return nums_copy


# Test cases
if __name__ == "__main__":
    print(move_zeros([0, 1, 0, 3, 12]))  # return [1, 3, 12, 0, 0]