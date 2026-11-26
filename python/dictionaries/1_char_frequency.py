"""
Goal: Write a function that takes a string and returns a dictionary counting the occurrence of each character.
"""

def char_frequency(text: str) -> dict:
    char_counts = {}

    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts


# Test cases
if __name__ == "__main__":
    print(char_frequency("testing"))
    print(char_frequency("w3resource"))