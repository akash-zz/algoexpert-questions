class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# o(n^2) Time | O(n) Space
def reconstructBst(array):
  if len(array) == 0:
    return
  currentValue = array[0]
  rightSubTreeIdx = len(array)

  for idx in range(1, len(array)):
    value = array[idx]
    if value > currentValue:
      rightSubTreeIdx = idx
      break

  leftSubTree = reconstructBst(array[1:rightSubTreeIdx])
  rightSubTree = reconstructBst(array[rightSubTree:])
  return BST(currentValue, leftSubTree, rightSubTree)


class TreeInfo:
  def __init__(self, rootIdx):
    self.rootIdx = rootIdx

# O(n) Time | O(n) Space
def reconstructBst(array):
  treeInfo = TreeInfo(0)
  return reconstructBstFromRange(float("-inf"), float("inf"), array, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, array, currentSubTreeInfo):
  if currentSubTreeInfo.rootIdx == len(array):
    return None

  rootValue = array[currentSubTreeInfo.rootIdx]
  if rootValue < lowerBound or rootValue >= upperBound:
    return None

  currentSubTreeInfo.rootIdx += 1
  leftSubTree = reconstructBstFromRange(lowerBound, rootValue, array, currentSubTreeInfo)
  rightSubTree = reconstructBstFromRange(rootValue, upperBound, array, currentSubTreeInfo)
  return BST(rootValue, leftSubTree, rightSubTree)
