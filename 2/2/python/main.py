from pathlib import Path
import operator

# get the path of the file
path = Path(__file__).parent.absolute()


def read_file(file_name: str) -> dict:
    dict_of_reports = {}
    i = 0
    with open(file_name, "r") as file:
        for line in file:
            # split line by the equal sign
            dict_of_reports[i] = [int(text) for text in line.split(" ")]
            i += 1

    return dict_of_reports

def find_safe_reports(dict_of_reports: dict) -> dict:
    safe_reports = 0
    for i in range(len(dict_of_reports)):
        safe= is_safe(dict_of_reports[i])
        if safe:
            safe_reports += 1
            continue
        # else:
        #     del dict_of_reports[i][possible_infractor]
        #     safe , _ = is_safe(dict_of_reports[i])
        #     if safe:
        #         safe_reports += 1
        for j in range(len(dict_of_reports[i])):
            temp = dict_of_reports[i].copy()
            del temp[j]
            safe = is_safe(temp)
            if safe:
                safe_reports += 1
                break
                      
    return safe_reports

def is_safe(report: list):
    compare_operator = operator.le if report[0] - report[-1] > 0 else operator.ge
    for i in range(len(report)):
        if i == 0:
            continue
        if compare_operator(report[i-1], report[i]):
            return False 
        if abs(report[i-1] - report[i]) > 3:
            return False 

    return True

def run():
    results = read_file(path.as_posix()+"/input.txt")
    safe_reports = find_safe_reports(results)
    return safe_reports

if __name__ == '__main__':
    print(run())
    #correct answer is 612