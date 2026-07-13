'''
Write a function called commafy that, given a list of three or things, returns a list with commas
'''

def commafy(list) -> str:
    new_string = ""
    for i in list:
        if i != list[-1]:
            new_string += i + ', '
    return new_string + "and " + list[-1]

def commafy_v2(list) -> str:
    list[-1] = "and " + list[-1]
    
    return ", ".join(list)
        

if __name__ == "__main__": 
    print(commafy(["trinket", "learning", "fun"]))
    print(commafy(["lions", "tigers", "bears"]))