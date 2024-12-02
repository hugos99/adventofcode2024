from pathlib import Path

# get the path of the file
path = Path(__file__).parent.absolute()

# function to parse the file
def parse_file(file_name: str):
    rigth_side = []
    left_side = []
    with open(file_name, "r") as file:
        for line in file:
            # split line by the equal sign
            left, right = line.split("   ")
            # remove the leading and trailing whitespaces
            rigth_side.append(int(right.strip()))
            left_side.append(int(left.strip()))
    return rigth_side, left_side

def calculate_similarity(rigth_list, left_list):
    similarity = 0
    similarity_map = create_similarity_map(rigth_list)
    for i in range(len(left_list)):
        if left_list[i] in similarity_map:
            similarity += similarity_map[left_list[i]] * left_list[i]
    return similarity

def create_similarity_map(unmapped_list):
    similarity_map = {}
    for i in range(len(unmapped_list)):
        if unmapped_list[i] not in similarity_map:
            similarity_map[unmapped_list[i]] = 1
        else:
            similarity_map[unmapped_list[i]] += 1
    return similarity_map

def run():
    # read file into the two lists
    rigth_side,left_side = parse_file(path.as_posix()+"/input.txt")

    # calculate the similarity between the two lists
    similarity = calculate_similarity(rigth_side, left_side)
    return similarity

if __name__ == '__main__':
    print(run())
    # correct answer is 17191599