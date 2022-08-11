class BinaryTree:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

# O(n) Time | O(1) Space
def findNodeDistance(tree, target, k):
  nodeToParents = {}
  populateNodeToParents(tree, nodeToParents)
  targetNode = getNodeFromValue(target, tree, nodeToParents)

  return bfsFromNodeDistance(targetNode, nodeToParents, k)

def bfsFromNodeDistance(targetNode, nodeToParents, k):
  queue = [(targetNode, 0)]
  seen = {targetNode.value}
  while len(queue) > 0:
    currentNode, distanceFromTarget = queue.pop(0)

    if distanceFromTarget == k:
      nodeDistanceK = [node.value for node, _ in queue]
      nodeDistanceK.append(currentNode.value)
      return nodeDistanceK

    connectedNodes = [currentNode.left, currentNode.right, nodeToParents[currentNode.value]]
    for node in connectedNodes:
      if node is None:
        continue

      if node.value in seen:
        continue

      seen.add(node.value)
      queue.append(node, distanceFromTarget - 1)

  return []

def getNodeFromValue(value, tree, nodeToParents):
  if tree.value = value:
    return tree

  nodeParent = nodeToParents[value]
  if nodeParent.left and nodeParent.right.value == value:
    return nodeParent.left

  return nodeParent.right

def populateNodeToParents(node, nodeToParents, parent = None):
  if node:
    nodeToParents[node.value] = parent
    populateNodeToParents(node.left, nodeToParents, parent)
    populateNodeToParents(node.right, nodeToParents, parent)
