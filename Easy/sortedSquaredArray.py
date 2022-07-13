# O(n log(n)) Time | O(n) Space:
def sortedSquaredArray (array):
  squaredArray = [];
  for num in array:
    squaredArray.append(num* num)

  squaredArray.sort()
  return squaredArray

# O(n) Time | O(n) Space
def sortedSquaredArray (array):
  squaredArray = [0 for _ in array]
  smallValueIdx = 0
  largeValueIdx = len(array) -1
  
  for idx in reversed(range(len(array))):
    largerValue = array[largeValueIdx]
    smallerValue = array[smallValueIdx]

    if abs(smallValueIdx) < abs(largeValueIdx):
      squaredArray[idx] = largerValue * largerValue
      largeValueIdx -= 1
    else:
        squaredArray[idx] = smallerValue * smallerValue
        smallValueIdx += 1
  
  return squaredArray

