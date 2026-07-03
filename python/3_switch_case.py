'''
Write a function called switch_case, given a string, returns the string with uppercase letters
in lower case and vice-versa. Include punctuation and non-cased characters unchanged.
'''

# convert strings to uppercase
def switch_case_general(string) -> str:
    if string.isupper():
        return string.lower()
    elif string.islower():
        return string.upper()
    else:
        return "".join([letter.lower() if letter.isupper() else letter.upper() for letter in list(string)])
    
def switch_case_modified(string) -> str:
    new_string = ''
    for letter in string:
        if letter.isupper():
            new_string += letter.lower()
        else:
            new_string += letter.upper()
    return new_string

if __name__ == "__main__": 
    print(switch_case_modified("ARG"))
    print(switch_case_modified("trinket"))
    print(switch_case_modified("Arg"))
    print(switch_case_modified("TrInKet"))
