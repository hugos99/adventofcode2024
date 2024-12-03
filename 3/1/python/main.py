from pathlib import Path
import re

# get the path of the file
path = Path(__file__).parent.absolute()

def read_file(file_name: str) -> dict:
    #read all file lines and return a single string with all the lines
    with open(file_name, "r") as file:
        #return a string of all the lines in the file
        return file.read()

def get_all_instructions(file: str) -> list:
    # apply regex mul\([0-9]{1,3},[0-9]{1,3}\) to the file string and return a list of all the matches
    return re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", file)

def calculate_result(instructions: list) -> int:
    final_result = 0
    for instruction in instructions:
        # apply regex mul\(([0-9]{1,3}),([0-9]{1,3})\) to the instruction string and multiply group 1 and group 2
        match = re.search(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', instruction)
        if match:
            final_result += int(match.group(1)) * int(match.group(2))   
    return final_result

def run():
    file = read_file(path.as_posix()+"/input.txt")
    instructions = get_all_instructions(file)
    result = calculate_result(instructions)
    return result

if __name__ == '__main__':
    print(run())
    #correct answer is 612