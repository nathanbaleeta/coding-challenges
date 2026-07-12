'''
Write a function gerund_infinitive that, given a string ending in "ing", returns the rest of the string prefixed with "to".
If the string doesn't end in "ing", return "That's not a gerund!"
'''

def gerund_infinitive(string) -> str:
    gerund = ""
    if string[-3:] == 'ing':
        return "to " + string[:-3]
    else:
        return "That's not a gerund!"

if __name__ == "__main__": 
    print(gerund_infinitive("building"))
    print(gerund_infinitive("build"))
    print(gerund_infinitive("picking"))
    print(gerund_infinitive("pick"))
    