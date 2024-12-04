PATH = "./2024/Python/Day 4/input.txt"

with open(PATH, "r") as file:
    matrix = [list(line.strip()) for line in file]

    target = "XMAS"

    rows, cols = len(matrix), len(matrix[0])
    target_length = len(target)
    count = 0

    for row in range(rows):
        for col in range(cols):
            # Right
            if col <= cols - target_length:
                if ''.join(matrix[row][col:col + target_length]) == target:
                    count += 1

            # Left
            if col >= target_length - 1:
                if ''.join(matrix[row][col - target_length + 1:col + 1][::-1]) == target:
                    count += 1

            # Down
            if row <= rows - target_length:
                if ''.join(matrix[row + i][col] for i in range(target_length)) == target:
                    count += 1

            # Up
            if row >= target_length - 1:
                if ''.join(matrix[row - i][col] for i in range(target_length)) == target:
                    count += 1

            # Diagonal Down-Right
            if row <= rows - target_length and col <= cols - target_length:
                if ''.join(matrix[row + i][col + i] for i in range(target_length)) == target:
                    count += 1

            # Diagonal Down-Left
            if row <= rows - target_length and col >= target_length - 1:
                if ''.join(matrix[row + i][col - i] for i in range(target_length)) == target:
                    count += 1

            # Diagonal Up-Right
            if row >= target_length - 1 and col <= cols - target_length:
                if ''.join(matrix[row - i][col + i] for i in range(target_length)) == target:
                    count += 1

            # Diagonal Up-Left
            if row >= target_length - 1 and col >= target_length - 1:
                if ''.join(matrix[row - i][col - i] for i in range(target_length)) == target:
                    count += 1

print(count)
