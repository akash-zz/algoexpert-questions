class Node:
  def __init__(self, value, parent = None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = parent

# O(n) Time | O(n) Space
def findSuccessor(tree, node):
  inOrderTraversalOrder = getInOrderTraversalOrder(tree)

  for idx, currentNode in enumerate(inOrderTraversalOrder):
    if currentNode != node:
      continue

    if idx == len(inOrderTraversalOrder) - 1:
      return None

    return inOrderTraversalOrder[idx + 1]

def getInOrderTraversalOrder(node, order = []):
  if node is None:
    return order

  getInOrderTraversalOrder(node.left, order)
  order.append(node)
  getInOrderTraversalOrder(node.right, order)
  return order

# O(h) Time | O(1) Space
def findSuccessor(tree, node):
  if tree.right is not None:
    return getLeftMostChild(node.right)

  return getRightMostParent(node)

def getLeftMostChild(node):
  current = node
  while current.left is not None:
    current = node.left
  return current

def getRightMostParent(node):
  current = node
  while current.parent is not None and current.parent.right == current:
    current = current.parent
  return current.parent
