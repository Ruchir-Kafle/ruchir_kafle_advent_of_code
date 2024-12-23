input_file: str = open("input.txt").read()
row_list: list[str] = input_file.split(sep="\n")

def location_probability(part: int = 1):

    left_list: list[int] = []
    right_list: list[int] = []

    for row in row_list:
        if row:
            locations = row.split("   ")
            left_list.append(int(locations[0]))
            right_list.append(int(locations[1]))

    left_list.sort()
    right_list.sort()

    if part == 1:
        total_distance: int = 0

        for index, _ in list(enumerate(left_list)):
            distance: int = abs(left_list[index] - right_list[index])
            total_distance += distance

        return(total_distance)

    elif part == 2:
        similarity_score: int = 0

        for location_id in left_list:
            right_list_appearances: int = right_list.count(location_id)            
            similarity_score += location_id * right_list_appearances

        return(similarity_score)

print(location_probability(1))
print(location_probability(2))