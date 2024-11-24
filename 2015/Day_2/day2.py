input_file = open("input.txt").read()
present_dimensions: list[str] = input_file.split("\n")

def calculate_material(day: int = 1):
    total_material: int = 0

    for measurement in present_dimensions:
        
        measurement = measurement.split("x")

        if len(measurement) > 1 and measurement[0]:

            sides: dict[str: int] = {
                "length": int(measurement[0]),
                "width": int(measurement[1]),
                "height": int(measurement[2])
            }

            if day == 1:

                side_1_area: int = sides["length"] * sides["width"]
                side_2_area: int = sides["width"] * sides["height"]
                side_3_area: int = sides["height"] * sides["length"]

                present_square_footage: int = (2 * side_1_area) + (2 * side_2_area) + (2 * side_3_area)

                smallest_side: int = min(side_1_area, side_2_area, side_3_area)

                total_material += present_square_footage + smallest_side
            
            elif day == 2:

                least_side: int = 100000000
                second_least_side: int = 100000000

                for i in [sides["length"], sides["width"], sides["height"]]:

                    if i < least_side:

                        second_least_side = least_side
                        least_side = i

                    else:

                        if i < second_least_side:
                            second_least_side = i

                present_ribbon_perimeter: int = (2 * least_side) + (2 * second_least_side)

                present_cubic_volume: int = sides["length"] * sides["width"] * sides["height"]

                total_material += present_ribbon_perimeter + present_cubic_volume

    print(total_material)

calculate_material(1)
calculate_material(2)