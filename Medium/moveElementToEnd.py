# O(n) Time | O(1) Space
def moveElementToEnd(array, target):
  i = 0
  j = len(array) -1
  while i < j:
    while i < j and array[j] == target:
      j -= 1
    if array[i] == target:
      array[i], array[j] = array[j], array[i]
    i += 1
  return array
