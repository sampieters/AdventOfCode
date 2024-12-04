PATH = "./2024/Day 1/input.txt"

with open(PATH, "r") as file:
    list1 = []
    list2 = []

    for line in file:
        numbers = line.strip().split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

    distance = 0
    for elem in list1:
        appearance = list2.count(elem)
        sim_score = elem * appearance
        distance += sim_score

    print(distance)