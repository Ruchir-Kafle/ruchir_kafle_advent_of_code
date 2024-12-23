input_file: str = open("input.txt").read()
reports: list[str] = list(map(lambda report: report.split(" "), input_file.split("\n")))

def filter_through(difference):
    increasing = (difference > 0)
    if abs(difference) > 0 and abs(difference) < 4:
        if increasing:
            return 1
        else:
            return -1
                    
    return 0

def find_safe_reports(part: int = 1):
    safe_reports: int = 0

    for report in reports:
        difference_list: list[int] = []

        previous_level: int = 0
        for level in report:
            if level:
                if previous_level:
                    difference_list.append(int(level) - previous_level)
                
                previous_level = int(level)
    
        if difference_list:
            filtered_list: list[bool] = list(map(filter_through, difference_list))

            if len(set(filtered_list)) == 1:
                safe_reports += 1
            else:
                if part == 2:
                    count_increasing: int = 0
                    count_decreasing: int = 0
                    count_invalid: int = 0

                    for element in filtered_list:
                        if element == 1:
                            count_increasing += 1
                        elif element == -1:
                            count_decreasing += 1
                        else:
                            count_invalid += 1

                    invalid_differences: int = 0
                    valid_differences: int = 0

                    for index, difference in list(enumerate(difference_list)):
                        if abs(difference) <= 0 or abs(difference) >= 4:
                            invalid_differences += 1

                            increasing: bool | None = None

                            if difference > 0:
                                increasing = True
                            elif difference < 0:
                                increasing = False
                            
                            if increasing != (difference_list[index + 1] > 0):
                                if index != 0:
                                    something = abs(abs(difference_list[index - 1]) - abs(difference_list[index + 1]))
                                    if something > 0 and something < 4:
                                        if (count_decreasing == 1 or count_increasing == 1):
                                            safe_reports += 1

    return safe_reports

print(find_safe_reports(1))
print(find_safe_reports(2))