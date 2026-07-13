'''
Write a function called lookup_state that, given a US state abbreviation, returns the state's name
'''

from utilities.US import states

def lookup_state(abbreviation) -> str:    
    return states[abbreviation]
       

if __name__ == "__main__": 
    print(lookup_state("NY"))
    print(lookup_state("CA"))