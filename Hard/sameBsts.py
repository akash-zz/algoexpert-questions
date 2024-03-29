# O(n^2) Time | O(n^2) Space
def sameBst(arrayOne, arrayTwo):
  if len(arrayOne) != len(arrayTwo):
    return False

  if len(arrayOne) == 0 and len(arrayTwo) == 0:
    return True

  if arrayOne[0] != arrayTwo[0]:
    return False

  leftOne = getSmaller(arrayOne)
  leftTwo = getSmaller(arrayTwo)
  rightOne = getBigger(arrayOne)
  rightTwo = getBigger(arrayTwo)

  return sameBst(leftOne, leftTwo) and sameBst(rightOne, rightTwo)

def getSmaller(array):
  result = []
  for i in range(1, len(array)):
    if array[i] < array[0]:
      result.append(array[i])
  return result

def getBigger(array):
  result = []
  for i in range(1, len(array)):
    if array[i] >= array[0]:
      result.append(array[i])
  return result

# O(n^2) Time | O(n) Space
def sameBst(arrayOne, arrayTwo):
  return areSameBst(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))

def areSameBst(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
  if rootIdxOne == -1 or rootIdxTwo == -1:
    return rootIdxOne == rootIdxTwo

  if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
    return False

  leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
  leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
  rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
  rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

  currentValue = arrayOne[rootIdxOne]
  leftAreSame = areSameBst(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
  rightAreSame = areSameBst(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

  return leftAreSame and rightAreSame

def getIdxOfFirstSmaller(array, startingIdx, minVal):
  for i in range(startingIdx + 1, len(array)):
    if array[i] < array[startingIdx] and array[i] >= minVal:
      return i
  return -1

def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
  for i in range(startingIdx + 1, len(array)):
    if array[i] >= array[startingIdx] and array[i] < maxVal:
      return i
  return -1
