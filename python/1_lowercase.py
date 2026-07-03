'''
Write a function called lowercase that, given a string, returns the entire sting as lowercase
'''

# convert string to lowercase
def lowercase(string) -> str:
    return string.lower()

if __name__ == "__main__":
    result = lowercase("ARG")
    result2 = lowercase("TRINKET")

    #print(result, result2, sep='\n')
    print(f"{result}\n{result2}")
