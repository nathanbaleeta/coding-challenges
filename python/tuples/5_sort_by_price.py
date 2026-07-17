"""
Goal: You are given a list of tuples representing items and their prices. Write a function that sorts this list in ascending order based on the price (the second element of each tuple).
"""

def sort_by_price(prices: list[tuple]) -> list[tuple]:
    return sorted(prices, key=lambda x: x[1])

# Sorting in descending order
def sort_by_price_descending(prices: list[tuple]) -> list[tuple]:
    return sorted(prices, key=lambda x: x[1], reverse=True)
    

## Test cases
if __name__ == "__main__":
    print(sort_by_price([("apple", 1.2), ("banana", 0.5), ("cherry", 2.0)]))       # return [('banana', 0.5), ('apple', 1.2), ('cherry', 2.0)]