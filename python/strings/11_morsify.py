'''
Write a function called morsify that, given an uppercase string, returns a string in morse code. Morse.py contains a dictionary 
mapping capital letters to morse code.
'''

from utilities.morse import morse_code

def morsify(string):
    final_string = ""

    if len(string) == 1:
        return morse_code[string]
    else:
        for ietter in list(string):
            final_string += morse_code[ietter]
    return final_string
        
if __name__ == "__main__": 
    print(morsify("TRINKET"))
    print(morsify("Z"))