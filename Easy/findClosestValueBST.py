# Avg O(log(n)) Time | Space O(log(n))
# Worst O(n) time | Space O(n)
# Recursive
def findClosestValueBST (tree,target):
  return findClosestValueBSTHelper(tree, target, float("inf"))

def findClosestValueBSTHelper(tree, target, closest):
  if tree is None:
    return closest
  
  if abs(target - closest) > abs(target - tree.value):
    closest = tree.value
  if target > tree.value:
    return findClosestValueBSTHelper(tree.left, target, closest)
  elif target < tree.value:
    return  findClosestValueBSTHelper(tree.right, target, closest)
  else:
    return closest


#Iterative
#Avg O(log(n)) Time | Space O(1)
#Worst O(n) Time | Space O(1)
def findClosestValueBST(tree, target):
  return findClosestValueBSTHelper(tree,target, float("inf"))

def findClosestValueBSTHelper(tree, target, closest):
  currentNode = tree
  while currentNode is not None:
    if abs(target - closest) > abs(target - currentNode.value):
      closest = currentNode.value
    if target < currentNode.value:
      currentNode = currentNode.left
    elif target > currentNode.value:
      currentNode = currentNode.right
    else:
      break
  return closest 