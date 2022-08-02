# O(n) Time | O(1) Space
def threeNumberSort(order, array):
  valueCounts = [0,0,0]

  for element in array:
    orderIdx = order.index(element)
    valueCounts[orderIdx] += 1

  for i in range(3):
    value = order[i]
    count = valueCounts[i]

    numElementsBefore = sum(valueCounts[:i])
    for n in range(count):
      currentIdx = numElementsBefore + n
      array[currentIdx] = value

  return array

# O(n) Time | O(1) Space
def threeNumberSum(array, order):
  firstValue = order[0]
  lastValue = order[2]

  firstIdx = 0
  for idx in range(len(array)):
    if array[idx] == firstValue:
      array[idx], array[firstIdx] = array[firstIdx], array[idx]
      firstIdx += 1

  lastIdx = len(array) - 1
  for idx in range(len(array) -1, -1, -1):
    if array[idx] == lastValue:
      array[idx], array[lastIdx] = array[lastIdx], array[idx]
      lastIdx -= 1

  return array

# O(n) Time | O(1) Space
def threeNumberSort(array, order):
  firstValue = order[0]
  secondValue = order[1]
  firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1

  while secondIdx <= thirdIdx:
    value = array[secondIdx]

    if value == firstValue:
      array[firstIdx], array[secondIdx] = array[secondIdx], array[firstIdx]
      firstIdx += 1
      secondIdx += 1

    elif value == secondValue:
      secondIdx += 1

    else:
      array[secondIdx], array[thirdIdx] = array[thirdIdx], array[secondIdx]
      thirdIdx -= 1

  return array
