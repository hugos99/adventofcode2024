from pathlib import Path
from scipy.signal import convolve2d
import numpy as np


# get the path of the file
path = Path(__file__).parent.absolute()

#magic number to check for
MAGIC_NUMBER = 42

# function to parse the file into matrix
def read_file(file_name: str)-> list:
    matrix = []
    with open(file_name, "r") as file:
        for line in file:
            local_array = []
            for char in line.strip():
                if char == 'X':
                    local_array.append(0)
                elif char == 'M':
                    local_array.append(2)
                elif char == 'A':
                    local_array.append(3)
                elif char == 'S':
                    local_array.append(4)
            matrix.append(local_array)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def process_matrix(matrix):
    matrix_np = np.array(matrix)
    filter = np.array([
        [1, 0, 1],
        [0, 10, 0],
        [1, 0, 1]])
    return convolve2d(matrix_np, filter, mode='same')

def get_input_file_path():
    return path.as_posix() + "/input.txt"


def count_matches(matrix, result):
    matches = np.argwhere(result == MAGIC_NUMBER)
    count = 0
    for x, y in matches:
        if matrix[x][y] != 3:
            continue
        if matrix[x + 1][y + 1] + matrix[x - 1][y - 1] != 6:
            continue
        if matrix[x + 1][y - 1] + matrix[x - 1][y + 1] != 6:
            continue
        # check if diagonals are either the number 4 or 2
        if matrix[x + 1][y + 1] == 3 or matrix[x - 1][y - 1] == 3:
            continue
        if matrix[x + 1][y - 1] == 3 or matrix[x - 1][y + 1] == 3:
            continue

        count += 1
    return count

def run():
    matrix = read_file(get_input_file_path())
    result = process_matrix(matrix)
    print(count_matches(matrix, result))

if __name__ == '__main__':
    run()