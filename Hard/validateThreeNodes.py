class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# O(h) Time | O(h) Space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
  if isDescendant(nodeTwo, nodeOne):
    return isDescendant(nodeThree, nodeTwo)

  if isDescendant(nodeTwo, nodeThree):
    return isDescendant(nodeOne, nodeTwo)

  return False

def isDescendant(node, target):
  if node is None:
    return False

  if node is target:
    return True

  return isDescendant(node.left, target) if target.value < node.value else isDescendant(node.right, target)

# # O(h) Time | O(1) Space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
  if isDescendent(nodeTwo, nodeOne):
    return isDescendent(nodeThree, nodeTwo)

  if isDescendent(nodeTwo, nodeThree):
    return isDescendent(nodeOne, nodeTwo)

  return False

def isDescendent(node, target):
  while node is not node and node is not target:
    node = node.left if node.value > target.value else node.right

  return node is target

# O(d) Avg Time and O(h) Worst Time | O(1) Space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
  searchOne = nodeOne
  searchTwo = nodeTwo

  while True:
    foundThreeFromOne = searchOne is nodeThree
    foundThreeFromTwo = searchTwo is nodeThree
    foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
    finishedSearching = searchOne is None or searchTwo is None
    if foundThreeFromOne or foundThreeFromTwo or foundNodeTwo or finishedSearching:
      break

    if searchOne is not None:
      searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right

    if searchTwo is not None:
      searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right

  foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeThree
  foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
  if not foundNodeFromOther or foundNodeTwo:
    return False

  return searchForTarget(nodeTwo, nodeThree if searchOne is nodeTwo else nodeOne)

def searchForTarget(node, target):
  while node is not None and node is not target:
    node = node.left if node.value > target.value else node.right

  return node is target
