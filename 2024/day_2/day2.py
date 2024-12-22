input_file: str = open("input.txt").read()
reports: list[str] = input_file.split("\n")

def map_into(report):
    return report.split(" ")

reports = list(map(map_into, reports))

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
            increasing = (difference_list[0] > 0)
            for difference in difference_list:
                if abs(difference) > 0 and abs(difference) < 4:
                    if (difference > 0) == increasing:
                        pass

    print(safe_reports)

find_safe_reports(1)