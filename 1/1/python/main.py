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


#function to sort list from smallest to largest
def sort_list(list):
    list.sort()
    return list

#function to calculate the distance between the two lists
def calculate_distance(list1, list2):
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    return distance
    
# read file into the two lists
rigth_side,left_side = parse_file(path.as_posix()+"/input.txt")

# sort the lists
rigth_side = sort_list(rigth_side)
left_side = sort_list(left_side)

#calculate the distance between the two lists
distance = calculate_distance(rigth_side, left_side)
print(distance)

# correct answer is 1970720