import os
import strutils
import tables
import sequtils

proc buildDictOfRules(listOfRules: seq[string]): Table[int, seq[int]] =
  var dictOfRulesBack = initTable[int, seq[int]]()
  for rule in listOfRules:
    let parts = rule.split("|")
    let ruleKey = parseInt(parts[0])
    let ruleValue = parseInt(parts[1])
    
    if not dictOfRulesBack.hasKey(ruleValue):
      dictOfRulesBack[ruleValue] = @[ruleKey]
    else:
      dictOfRulesBack[ruleValue].add(ruleKey)
  
  return dictOfRulesBack

proc readFile(fileName: string): tuple[prints: seq[seq[int]], rules: Table[int, seq[int]]] =
  var
    listOfRules: seq[string] = @[]
    listOfPrints: seq[seq[int]] = @[]
    isRules = true
    
  for line in lines(fileName):
    if line == "":
      isRules = false
      continue
    if isRules:
      listOfRules.add(line.strip())
    else:
      listOfPrints.add(line.split(",").map(parseInt))
  result = (listOfPrints, buildDictOfRules(listOfRules))

proc validateSequence(dictOfRulesBack: Table[int, seq[int]], sequence: seq[int]): bool =
  for i in 1..<sequence.len:
    for j in 0..<i:
      if dictOfRulesBack.hasKey(sequence[j]) and sequence[i] in dictOfRulesBack[sequence[j]]:
        return false
  return true

proc reorderSequence(dictOfRulesBack: Table[int, seq[int]],  sequence: seq[int]): seq[int] =
  var 
    newSequence = sequence
    tmp = 0
  for i in 1..<sequence.len:
    for j in 0..<i:
      if dictOfRulesBack.hasKey(sequence[j]) and sequence[i] in dictOfRulesBack[sequence[j]]:
        tmp = newSequence[j]
        newSequence[j] = newSequence[i]
        newSequence[i] = tmp
  return newSequence

proc run(): int =
  let currentDir = getCurrentDir()
  let (listOfPrints, dictOfRulesBack) = readFile(currentDir & "/input-t.txt")
  var wrongList: seq[seq[int]] = @[]
  
  for prints in listOfPrints:
    if not validateSequence(dictOfRulesBack, prints):
      wrongList.add(prints)
  
  
  result = 0
  for sequence in wrongList:
    var sequenceTmp = reorderSequence(dictOfRulesBack, sequence)
    result += sequenceTmp[sequenceTmp.len div 2]

when isMainModule:
  echo run()
