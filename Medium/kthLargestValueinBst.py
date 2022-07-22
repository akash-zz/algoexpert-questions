class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# O(n) Time | O(n) Space
def kthLargestValueInBst(Node, target):
    array = []
    if Node is not None:
      kthLargestValueInBst(Node.left, array)
      array.append(Node.value)
      kthLargestValueInBst(Node.right, array)
    return array[len(array) - target]

class TreeInfo:
  def __init__(self, numOfNodesVisited, latestVisitedNodeValue):
    self.numOfNodesVisited = numOfNodesVisited
    self.latestVisitedNodeValue = latestVisitedNodeValue

# O(h + k) Time | O(h) Space
def kthLargestValueInBst(tree, k):
  treeInfo = TreeInfo(0, -1)
  reverseInOrderTraverse(tree, k, treeInfo)
  return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
  if node == None or treeInfo.numOfNodesVisited >= k:
    return

  reverseInOrderTraverse(node.right, k, treeInfo)
  if treeInfo.numOfNodesVisited < k:
    treeInfo.numOfNodesVisited += 1
    treeInfo.latestNodeVisitedValue = node.value
    reverseInOrderTraverse(node.left, k, treeInfo)
