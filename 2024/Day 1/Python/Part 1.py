PATH = "./2024/Day 1/input.txt"

with open(PATH, "r") as file:
    left = []
    right = []

    for line in file:
        numbers = line.strip().split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

    left.sort()
    right.sort()             

    distances = 0
    for index in range(len(left)):
        distances += abs(right[index] - left[index])
    print(distances)