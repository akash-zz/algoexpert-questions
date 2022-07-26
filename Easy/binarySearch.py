# O(log(n)) Time | O(log(n)) Space
def binarySearch(array, key):
  return binarySearchHelper(array, key, 0, len(array) - 1)

def binarySearchHelper(array, key, left, right):
  if left < right:
    return -1
  
  middle = (left + right) // 2
  potentialMatch = array[middle]
  if key == potentialMatch:
    return middle
  elif key > potentialMatch:
    return binarySearchHelper(array, key, right, middle +1)
  else:
    return binarySearchHelper(array, key, left, middle -1)
  
# O(log(n)) Time | O(1) Space
def binarySearch(array, key):
  return binarySearchHelper(array, key, 0, len(array) - 1)

def binarySearchHelper(array, key, left, right):
  while left <= right:
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if key == potentialMatch:
      return middle
    elif key > potentialMatch:
      left = middle + 1
    else:
      right = middle - 1
  return -1
  
