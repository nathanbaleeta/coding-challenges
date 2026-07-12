'''
Write a function called aardvark, given a string returns 'aardvark' if the string starts with 'a'. Otherwise returns zebra.
'''

def aardvark(string) -> str:
    if string[0] == 'a':
        return aardvark
    else:
        return 'zebra'
    

if __name__ == "__main__": 
    print(aardvark("arg"))
    print(aardvark("trinket"))
    