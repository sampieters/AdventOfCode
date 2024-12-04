PATH = "./2024/Day 2/input.txt"

def is_sorted(numbers):
    # Check for strictly increasing or decreasing sequences with a difference greater than 0 adn less than 4
    increasing = all(0 < j - i < 4 for i, j in zip(numbers, numbers[1:]))
    decreasing = all(0 < i - j < 4 for i, j in zip(numbers, numbers[1:]))
    return increasing or decreasing

with open(PATH, "r") as file:
    result = 0
    for line in file:
        # Convert the line into a list of integers
        numbers = list(map(int, line.strip().split()))

        # Check all possible lists by removing one element
        for i in range(len(numbers)):
            if is_sorted(numbers[:i] + numbers[i + 1:]):
                result += 1
                break

    print(result)

