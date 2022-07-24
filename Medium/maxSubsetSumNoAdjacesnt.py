# O(n) Time | O(n) Space
def maxSubsetSumNoAdjacent(array):
  if not len(array):
    return
  elif len(array) == 1:
    return array[0]
  maxSums = array[:]
  maxSums[1] = max(array[0], array[1])
  for i in range(2, len(array)):
    maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
  return array[-1]

# O(n) Time | O(1) Space
def maxSubsetNoAdjacent(array):
  if not len(array):
    return
  elif len(array) == 1:
    return array[0]
  first = array[0]
  second = max(array[0], array[1])
  for i in range(2, len(array)):
    current = max(first, second + array[i])
    second = first
    first = current
  return first
