'''
Write a function called how_many that, given a list of a number and a thing name, returns a grammatically correct sentence describing the number of things
'''

def how_many(the_list) -> str:
    count = the_list[0]
    object = the_list[-1]
    
    if count > 1:
        return f"There are {count} {object}s."
    else:
        return f"There is {count} {object}."
        

if __name__ == "__main__": 
    print(how_many([5, "trinket"]))
    print(how_many([1, "king"]))