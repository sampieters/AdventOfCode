import re

PATH = "./2024/Python/Day 3/input.txt"

pattern = r"mul\((\d+),(\d+)\)"
with open(PATH, "r") as file:
    result = 0
    all_text = "do()" + file.read()
    all_lines = all_text.split("don't()")
    for line in all_lines:
        # Find the first occurrence of "do()"
        index = line.find("do()")
        cleaned_line = line[index:] if index != -1 else ""

        # Find all matches
        matches = re.findall(pattern, cleaned_line)
        # If there are no matches the result will just be 0
        for (x, y) in matches:
            result += (int(x) * int(y))
        
    print(result)


