# O(2^(n + m)) Time | O(n + m) Space
def numberOfWaysToTraverseGraph(width, height):
  if width == 1 or height == 1:
    return 1

  return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)

# O(n * m )Time | O(n * m) Space
def numberOfWaysToTraverseGraph(width, height):
  numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

  for widthIdx in range(1, width + 1):
    for heightIdx in range(1, height + 1):
      if widthIdx == 1 or heightIdx == 1:
        numberOfWays[heightIdx][widthIdx] = 1
      else:
        waysLeft = numberOfWays[heightIdx][widthIdx - 1]
        waysUp = numberOfWays[heightIdx - 1][widthIdx]
        numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp

  return numberOfWays[heightIdx][width]

# O(n * m) Time | O(1) Space
def numberOfWaysToTraverseGraph(width, height):
  xDistanceToCorner = width - 1
  yDistanceToCorner = height - 1

  numerator = factorial(xDistanceToCorner + yDistanceToCorner)
  denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner)
  return numerator // denominator

def factorial(num):
  result = 1
  for n in range(2, num + 1):
    result *= n
  return result
