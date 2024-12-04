PATH = "./2024/Python/Day 4/input.txt"

with open(PATH, "r") as file:
    matrix = [list(line.strip()) for line in file]

    target = "MAS"

    rows, cols = len(matrix), len(matrix[0])
    target_length = len(target)
    count = 0

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if matrix[row][col] == "A":
                # Diagonal Left-Right
                diag1 = ''.join(matrix[row - 1 + i][col - 1 + i] for i in range(target_length))
                # Diagonal Right-Left
                diag2 = ''.join(matrix[row - 1 + i][col + 1 - i] for i in range(target_length))

                count += int((diag1 == target or diag1[::-1] == target) and (diag2 == target or diag2[::-1] == target))

print(count)