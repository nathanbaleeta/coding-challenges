'''
Write a function called reverse_string that, given a string returns returns in reverse.
'''

# reverse string using in-built slicing techniques  
def reverse_string(string) -> str:
    return string[::-1]
    
if __name__ == "__main__": 
    print(reverse_string("arg"))
    print(reverse_string("Hi!"))
    