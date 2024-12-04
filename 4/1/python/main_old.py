from pathlib import Path
import numpy as np
from scipy.signal import convolve2d

# get the path of the file
path = Path(__file__).parent.absolute()

# function to parse the file into matrix
def read_file(file_name: str) -> np.ndarray:
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
    return np.array(matrix)
    
def find_matches(matrix: np.ndarray) -> int:
    # Define filters for [1, 2, 3, 4] and [4, 3, 2, 1]
    filter_forward = np.array([[1, 2, 3, 4]])
    filter_backward = np.array([[4, 3, 2, 1]])

    # Define the expected sum for matches
    target_sum = 10

    results = []

    # Horizontal detection
    conv_hor_forward = convolve2d(matrix, filter_forward, mode='same')
    conv_hor_backward = convolve2d(matrix, filter_backward, mode='same')

    # Vertical detection
    conv_ver_forward = convolve2d(matrix, filter_forward.T, mode='same')
    conv_ver_backward = convolve2d(matrix, filter_backward.T, mode='same')

    # Diagonal detection
    filter_diag_forward = np.eye(4)
    filter_diag_backward = np.fliplr(np.eye(4))

    conv_diag_forward = convolve2d(matrix, filter_diag_forward, mode='same')
    conv_diag_backward = convolve2d(matrix, filter_diag_backward, mode='same')

    # Check for matches
    results.extend(np.argwhere(conv_hor_forward == target_sum))
    results.extend(np.argwhere(conv_hor_backward == target_sum))
    results.extend(np.argwhere(conv_ver_forward == target_sum))
    results.extend(np.argwhere(conv_ver_backward == target_sum))
    results.extend(np.argwhere(conv_diag_forward == target_sum))
    results.extend(np.argwhere(conv_diag_backward == target_sum))

    return results.__len__()

def detect_sequences_with_correlate(matrix, sequence):
    rows, cols = matrix.shape
    results = 0

    # Convert sequence to a NumPy array
    sequence = np.array(sequence)
    sequence_sum = np.sum(sequence)

    # Horizontal detection
    for i in range(rows):
        row = matrix[i, :]
        correlation = np.correlate(row, sequence, mode='valid')
        matches = np.where(correlation == sequence_sum)[0]
        for match in matches:
            results =+ 1

    # Vertical detection
    for j in range(cols):
        col = matrix[:, j]
        correlation = np.correlate(col, sequence, mode='valid')
        matches = np.where(correlation == sequence_sum)[0]
        for match in matches:
            results =+ 1

    # Diagonal detection
    for offset in range(-rows + 1, cols):  # Diagonals from TL-BR
        diag = matrix.diagonal(offset)
        if len(diag) >= len(sequence):
            correlation = np.correlate(diag, sequence, mode='valid')
            matches = np.where(correlation == sequence_sum)[0]
            for match in matches:
                results =+ 1

    for offset in range(-rows + 1, cols):  # Diagonals from TR-BL
        diag = np.fliplr(matrix).diagonal(offset)
        if len(diag) >= len(sequence):
            correlation = np.correlate(diag, sequence, mode='valid')
            matches = np.where(correlation == sequence_sum)[0]
            for match in matches:
                results =+ 1

    return results

def run():
    matrix = read_file(path.as_posix()+"/input-t.txt")
    matches = detect_sequences_with_correlate(matrix,[1,2,3,4])
    print("Matches found at positions:", matches)

if __name__ == '__main__':
    run()
    # correct answer is