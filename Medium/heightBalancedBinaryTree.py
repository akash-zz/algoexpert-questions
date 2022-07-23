class Tree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class TreeInfo:
  def __init__(self, isBalanced, height):
    self.isBalanced = isBalanced
    self.height = height

# O(n) Space | O(h) Space -> h is height of the tree
def heightBalancedBinaryTree(tree):
  treeInfo = getTreeInfo(tree)
  return treeInfo.isBalanced

def getTreeInfo(node):
  if node == None:
    return TreeInfo(True, -1)

  leftSubTreeInfo = getTreeInfo(node.left)
  rightSubTreeInfo = getTreeInfo(node.right)

  isBalanced = leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
  height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1
  return TreeInfo(isBalanced, height)
