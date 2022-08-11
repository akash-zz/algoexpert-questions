# O(n) Time | O(log(n)) Space
def maxPathSum(tree):
  _, maxSum = maxPathHelper(tree)
  return maxSum

def maxPathHelper(tree):
  if tree is None:
    return (0,0)

  leftMaxSumAsBranch, leftMaxPathSum = maxPathHelper(tree.left)
  rightMaxSumAsBranch, rightMaxPathSum = maxPathHelper(tree.right)
  maxChildSumBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

  value = tree.value
  maxSumAsBranch = max(maxChildSumBranch + value, value)
  maxSumAsRootNode = max(maxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
  maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

  return (maxSumAsBranch, maxPathSum)
