# O(n log(n)) Time | O(n) Space
def minHeightBst(array):
  return minHeightBstMaker(array, None, 0, len(array) -1)

def minHeightBstMaker(array, bst, startIdx, endIdx):
  if endIdx < startIdx:
    return
  midIdx = (startIdx + endIdx) // 2
  valueToAdd = array[midIdx]
  if bst is None:
    bst = BST(valueToAdd)
  else:
    bst.insert(valueToAdd)
  minHeightBst(array, bst, startIdx, startIdx)
  minHeightBst(array, bst, midIdx + 1, endIdx)
  return bst

# O(n) Time | O(n) Space
def minHeightBst(array):
  return minHeightBstMaker(array, 0, len(array) -1)

def minHeightBstMaker(array, bst, startIdx, endIdx):
  if startIdx > endIdx:
    return
  midIdx = (startIdx + endIdx) // 2
  bst = BST(array[midIdx])
  bst.left = minHeightBstMaker(array, startIdx, midIdx - 1)
  bst.right = minHeightBstMaker(array, midIdx + 1, endIdx)
  return bst

class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if self.left is None:
        self.left = BST(value)
      else:
        self.left.insert(value)

    else:
      if self.right is None:
        self.right = BST(value)
      else:
        self.right.insert(value)
