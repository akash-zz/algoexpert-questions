# UpperBound: O(n^2 * n!) Time | O(n * n!) Space
def getPermutations(array):
  permutations = []
  permutationsHelper(array, [], permutations)
  return permutations

def permutationsHelper(array, currentPermutations, permutations):
  if not len(array) or len(currentPermutations):
    permutations.append(currentPermutations)
  else:
    for i in range(len(array)):
      newArray = array[:i] + array[i + 1:]
      newPermutation = currentPermutations + array[i]
      permutationsHelper(newArray, newPermutation, permutations)

# O(n * n!) Time | O(n * n!) Space
def getPermutations(array):
  permutations = []
  permutationHelper(0, array, permutations)
  return permutations

def permutationHelper(i, array, permutations):
  if i == len(array) - 1:
    permutations.append(array[:])
  else:
    for j in range(i, len(array)):
      swap(array, i, j)
      permutationHelper(i + 1, j, permutations)
      swap(array, i, j)

def swap(array, i, j):
  array[i], array[j] = array[j], array[i]
