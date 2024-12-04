PATH = "./2024/Python/Day 2/input.txt"

with open(PATH, "r") as file:
    result = 0
    for line in file:
        # Convert the line into a list of integers
        numbers = list(map(int, line.strip().split()))
        
        # Check for strictly increasing or decreasing sequences with a difference greater than 0 adn less than 4
        increasing = all(0 < j - i < 4 for i, j in zip(numbers, numbers[1:]))
        decreasing = all(0 < i - j < 4 for i, j in zip(numbers, numbers[1:]))
        
        # Convert the boolean result to int (0 or 1) and count it
        result += int(increasing or decreasing)

    print(result)