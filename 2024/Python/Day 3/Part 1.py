import re

PATH = "./2024/Python/Day 3/input.txt"

pattern = r"mul\((\d+),(\d+)\)"
with open(PATH, "r") as file:
    result = 0
    for line in file:
        # Find all matches
        matches = re.findall(pattern, line)
        # If there are no matches the result will just be 0
        for (x, y) in matches:
            result += (int(x) * int(y))
    print(result)
