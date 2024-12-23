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
            filtered_list: list[bool] = map(filter_through, difference_list)

            if len(set(list(filtered_list))) == 1:
                safe_reports += 1

    print(safe_reports)

find_safe_reports(1)