from pathlib import Path
import re

# get the path of the file
path = Path(__file__).parent.absolute()

def read_file(file_name: str) -> dict:
    #read all file lines and return a single string with all the lines
    with open(file_name, "r") as file:
        #return a string of all the lines in the file
        return file.read()

def get_instructions_iterator(search_area: str) -> iter:
    # apply regex mul\([0-9]{1,3},[0-9]{1,3}\) to the file string and return a list of all the matches
    return re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", search_area)

def get_do_donts_iterator(search_area: str) -> iter:
    return re.finditer(r"(do|don't)\(\)", search_area)

def calculate_result_area(instructions: iter) -> int:
    final_result = 0
    for instruction in instructions:
        final_result += int(instruction.group(1)) * int(instruction.group(2))   
    return final_result

def calculate_result(do_donts_instructions: list, search_area: str) -> int:
    final_result = 0
    #make dict with current instruction and index location
    current_instruction = {"instruction": "do", "index": 0}
    for instruction in do_donts_instructions:
        # switch the do and don't instructions
        if (instruction.group(1) == "do" and current_instruction["instruction"] == "don't"):
            current_instruction = {"instruction": "do", "index": instruction.end()}
        elif (instruction.group(1) == "don't" and current_instruction["instruction"] == "do"):
            final_result += calculate_result_area(get_instructions_iterator(search_area[current_instruction["index"]:instruction.start()]))
            current_instruction = {"instruction": "don't", "index": instruction.end()}
            
    #clean up the last instruction if it is a do
    if current_instruction["instruction"] == "do":
        final_result += calculate_result_area(get_instructions_iterator(search_area[current_instruction["index"]:-1]))
        
    return final_result

def run():
    file = read_file(path.as_posix()+"/input.txt")
    do_donts_instructions = get_do_donts_iterator(file)
    result = calculate_result(do_donts_instructions,file)
    return result

if __name__ == '__main__':
    print(run())
    #correct answer is 108830766