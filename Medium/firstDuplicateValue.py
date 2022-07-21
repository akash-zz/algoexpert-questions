# O(n log(n)) Time | O(1) Space
def firstDuplicateValue(array):
  array.sort()
  for i in range(len(array)):
    if array[i] == array[i + 1]:
      return array[i]
    else:
       return -1

# O(n) Time | O(n) Space
def firstDuplicateValue(array):
  allNums = set()
  for i in range(len(array)):
    if array[i] not in allNums:
      allNums.add(array[i])
      i += 1
    if array[i] in allNums:
      return array[i]
    else:
      return -1

# O(n^2) Time | O(1) Space
def firstDuplicateValue(array):
  minimumSecondIndex = len(array)
  for i in range(len(array)):
    value = array[i]
    for j in range(i+1, len(array)):
      valueToCompare = array[j]
      if value == valueToCompare:
        minimumSecondIndex = min(minimumSecondIndex, j)

  if minimumSecondIndex == len(array):
    return -1

  return array[minimumSecondIndex]
