'''
Write a function is_anagram(s, t)  that takes take stwo strings s and t amd returns True of t is an anagram of s, and False otherwise.
An anagram is a word or phrase formed rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

"""
def is_anagram(s: str, t: str) -> bool:
    if len(s) == len(t):
        for char in s:
            for letter in t:
                if char in t:
                    return True
                else:
                    return False
"""
                
def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
                    
                
# Test cases
if __name__ == "__main__": 
    print(is_anagram("anagram", "nagaram")) # True
    print(is_anagram("rat", "cat"))         # False
   