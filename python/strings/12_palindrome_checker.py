'''
Write a function is_palindrome(s) that takes a string and returns True 
if the string is a palindrome (reads the same forward and backward) 
and False otherwise. You should ignore capitalization, spaces, and punctuation.
'''

def is_palindrome(string: str) -> bool:
    # clean the string: keep only alphanumeric and lowercase them - use generator
    cleaned = "".join((char.lower() for char in string if char.isalnum()))

    """ if cleaned == cleaned[::-1]:
        return True
    else:
        return False
    """
    
    return cleaned == cleaned[::-1]
   
        
# Test cases
if __name__ == "__main__": 
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("hello"))
    print(is_palindrome("racecar"))
    