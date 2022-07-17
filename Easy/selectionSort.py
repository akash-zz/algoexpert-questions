# O(n^2) Time | O(1) Space
def selectionSort(array):
  currentIdx = 0
  while currentIdx < len(array) - 1:
    smallestIdx = currentIdx
    for i in range(currentIdx + 1, len(array)):
      if array[smallestIdx] > array[i]:
        smallestIdx = i
    swap(currentIdx, smallestIdx, array)

def swap(i, j, array):
  array[i], array[j] = array[j], array[i]
