# O(2^n * n) Time | O(2^n * n) Space
def powerSet(array):
  subsets = [[]]
  for element in array:
    for i in range(len(subsets)):
      currentSubset = subsets[i]
      subsets.append(currentSubset + [element])
  return subsets

# O(n^2 * n) Time | O(n^2 * n) Space
def powerSet(array, idx = None):
  if idx is None:
    idx = len(array) - 1
  elif idx < 0:
    return [[]]
  ele = array[idx]
  subsets = powerSet(array, idx - 1)

  for i in range(len(subsets)):
    currentSubset = subsets[i]
    subsets.append(currentSubset + [ele])
  return subsets
