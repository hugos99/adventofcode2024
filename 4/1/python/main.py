from pathlib import Path


# get the path of the file
path = Path(__file__).parent.absolute()

# function to parse the file into matrix
def read_file(file_name: str)-> list:
    matrix = []
    with open(file_name, "r") as file:
        for line in file:
            local_array = []
            for char in line.strip():
                if char == 'X':
                    local_array.append(1)
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


def count_sequences(matrix,sequence):
    rows, cols = len(matrix), len(matrix[0])
    sequence_length = len(sequence)
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # Top, Bottom, Left, Right
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
    ]

    def dfs(x, y, index, direction=None):
        if index == sequence_length -1 and matrix[x][y] == sequence[index]:
            return 1
        if matrix[x][y] != sequence[index]:
            return 0

        count = 0
        if direction is not None:
            dx, dy = direction
            if 0 <= x + dx < rows and 0 <= y + dy < cols:
                count += dfs(x + dx, y + dy, index + 1, direction)
        else:
            for dx, dy in directions:
                if 0 <= x + dx < rows and 0 <= y + dy < cols:
                    count += dfs(x + dx, y + dy, index + 1, (dx, dy))
        return count

    total_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == sequence[0]:
                total_count += dfs(i, j, 0)
    return total_count

def run():
    matrix = read_file(path.as_posix() + "/input.txt")
    print_matrix(matrix)
    print("count_sequences:", count_sequences(matrix, [4,3,2,1]))

if __name__ == '__main__':
    run()