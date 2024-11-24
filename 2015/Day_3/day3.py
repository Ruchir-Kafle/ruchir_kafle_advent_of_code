input_file = open("input.txt").read()
directions: list[str] = input_file.split("")

all_coordinates: list[list[int]] = [[0, 0]]
coordinate: list[int] = [0, 0]

total_houses: int = 1

for move in directions:
    if move == "^":
        coordinate = [coordinate[0], coordinate[1] + 1]
    if move == ">":
        coordinate = [coordinate[0] + 1, coordinate[1]]
    if move == "v":
        coordinate = [coordinate[0], coordinate[1] - 1]
    if move == "<":
        coordinate = [coordinate[0] - 1, coordinate[1]]
    
    if not (coordinate in all_coordinates):
        all_coordinates.append(coordinate)
        total_houses += 1

print(total_houses)