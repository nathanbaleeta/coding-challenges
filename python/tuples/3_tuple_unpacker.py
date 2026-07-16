'''
Goal: You are given a tuple containing a user's first name, last name, age, and city. 
Write a function that unpacks these values and returns a formatted string: "First Last is Age years old and lives in City."
'''

def profile_string(user_data: tuple) -> str:
    # unpack values into variables
    first, last, age, city = user_data

    # use string formatting to embed variables in str output
    return f"{first} {last} is {age} years old and lives in {city}"

    

        
# Test cases
if __name__ == "__main__": 
    print(profile_string(("Jane", "Doe", 28, "Paris")))       # "First Last is Age years old and lives in City."