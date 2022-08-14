# O(n) Time | O(n) Space
def waterArea(heights):
  maxes = [0 for x in heights]
  leftMax = 0
  for i in range(len(heights)):
    height = heights[i]
    maxes[i] = leftMax
    leftMax = max(leftMax, height)

  rightMax = 0
  for i in reversed(range(len(heights))):
    height = heights[i]
    minHeight = min(maxes[i], rightMax)
    if height < minHeight:
      maxes[i] = minHeight - height
    else:
      maxes[i] = 0
    rightMax = max(rightMax, height)

  return sum(maxes)
