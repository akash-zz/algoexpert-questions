# O(d) Time -> d is the depth of the lowerAncestor | O(1) Time
def youngestCommonAncestor(topAncestor, descendentOne, descendentTwo):
  depthOne = getDescendentDepth(descendentOne, topAncestor)
  depthTwo = getDescendentDepth(descendentTwo, topAncestor)
  if depthTwo > depthOne:
    return backtrackAncestralTree(descendentOne, descendentTwo, depthTwo - depthOne)
  else:
    return backtrackAncestralTree(descendentTwo, descendentOne, depthOne - depthTwo)

def getDescendentDepth(descendant, ancestor):
  depth = 0
  while descendant != ancestor:
    depth += 1
    descendant = descendant.ancestor
  return depth

def backtrackAncestralTree(lowerDescendent, higherDescendent, diff):
  while diff > 0:
    lowerDescendent = lowerDescendent.ancestor
    diff -= 1
  while lowerDescendent != higherDescendent:
    lowerDescendent = lowerDescendent.ancestor
    higherDescendent = higherDescendent.ancestor
  return lowerDescendent
