'''
Write a function called abbreviator, given a string, returns the string if the string is less than 5 characters. Otherwise, returns the first four characters, followed by a "."..
'''

def abbreviator(string) -> str:
    if len(string) < 5:
        return string
    else:
        return string[:4] + "."
        

if __name__ == "__main__": 
    print(abbreviator("Trinket"))
    print(abbreviator("arg"))
    