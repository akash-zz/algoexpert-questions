# O(n) Time | O(n) Space
def invertBinaryTree(tree):
  queue = [tree]
  while len(queue) > 0:
    current = queue.pop(0)
    if current is None:
      continue
    swapLeftAndRight(current)
    queue.append(current.left)
    queue.append(current.right)

def swapLeftAndRight(tree):
  tree.left, tree.right = tree.right, tree.left

# O(n) Time | O(d) Space -> d is depth of the tree
def invertBinaryTree(tree):
  if tree is None:
    return
  swapLeftAndRight(tree)
  invertBinaryTree(tree.left)
  invertBinaryTree(tree.right)

def swapLeftAndRight(tree):
  tree.left, tree.right = tree.right, tree.left
