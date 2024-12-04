import tables, strutils, sequtils, sugar

# define a function for reading the line from the file
proc readFile(file: File): Table[int,seq[int]] =
  var 
    array: Table[int,seq[int]]
    i: int = 0
  for line in file.lines:
    array[i] = line.items.toSeq().mapIt(
        case it
            of 'X': 1
            of 'M': 2
            of 'A': 3
            of 'S': 4
            else: 0
    )
    inc i
  return array

#fucntion to echo the matrix in order to debug
proc echoMatrix(matrix: Table[int,seq[int]]): void =
    for i in 0 .. matrix.keys.toSeq().high :
        echo matrix[i]

echoMatrix(readFile(open("./input.txt", fmRead)))