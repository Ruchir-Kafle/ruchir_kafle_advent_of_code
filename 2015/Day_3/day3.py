input_file = open("input.txt").read()
directions: list[str] = [direction for direction in input_file]

def calculate_houses(part: int = 1):
    
    current_coordinates: dict[str: list[list[int]]] = {
        "actual_santa": [0, 0],
        "robot_santa": [0, 0]
    }

    all_coordinates: list[list[int]] = [[0, 0]]

    santa = "actual_santa"

    total_houses: int = 1

    for move in directions:

        if move == "^":
            current_coordinates[santa] = [current_coordinates[santa][0], current_coordinates[santa][1] + 1]
        if move == ">":
            current_coordinates[santa] = [current_coordinates[santa][0] + 1, current_coordinates[santa][1]]
        if move == "v":
            current_coordinates[santa] = [current_coordinates[santa][0], current_coordinates[santa][1] - 1]
        if move == "<":
            current_coordinates[santa] = [current_coordinates[santa][0] - 1, current_coordinates[santa][1]]
        
        if not (current_coordinates[santa] in all_coordinates):
            all_coordinates.append(current_coordinates[santa])
            total_houses += 1

        if part == 2:
            if santa == "actual_santa":
                santa = "robot_santa"
            elif santa == "robot_santa":
                santa = "actual_santa"

    return(total_houses)

print(calculate_houses(1))
print(calculate_houses(2))