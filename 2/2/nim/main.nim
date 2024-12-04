import tables, strutils, sequtils, sugar

# define a function for reading the line from the file
proc readFile(file: File): Table[int,seq[int]] =
  var
    map: Table[int,seq[int]]
    i: int = 0
  for line in file.lines:
    map[i] = line.split(" ").mapIt(it.parseInt)
    inc i
  return map

proc is_safe(report: seq[int]): bool =
  var comparator_operator: (x: int,y: int) -> bool
  comparator_operator = if report[0] - report[report.high] > 0: (x: int, y: int) => x <= y else: (x: int, y: int) => x >= y
  for i in 1 .. report.high:
    if comparator_operator(report[i-1], report[i]):
      return false
    if abs(report[i-1] - report[i]) > 3:
      return false
  return true

proc kinda_safe(report: seq[int], index: int=0): bool =
  return index == report.high or (is_safe(report) or is_safe(report.delete(index)) or kinda_safe(report, index + 1))

proc find_safe_reports(report_map: Table[int,seq[int]], index: int = 0): int =  
  if report_map.len() == index:
    return 0
  if is_safe(report_map[index]):
    return 1 + find_safe_reports(report_map, index + 1)
  else:
    return find_safe_reports(report_map, index + 1)


# print file content
echo find_safe_reports(readFile(open("./input.txt", fmRead)))
# result was 572