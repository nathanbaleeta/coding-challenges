'''
Write a function called uppercase that, given a string, returns the entire sting as uppercase
'''

# convert string to uppercase
def uppercase(string) -> str:
    return string.upper()
    
if __name__ == "__main__": 
    print(uppercase("arg"))
    print(uppercase("trinket"))
