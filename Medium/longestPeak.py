# O(n) Time | O(1) Space
def longestPeak(array):
  longestPeakLength = 0
  i = 1
  while i < len(array) - 1:
    isPeak = array[i] > array[i - 1] and array[i] > array[i + 1]
    if not isPeak:
      i += 1
      continue

    leftIdx = i - 2
    while array[leftIdx] >= 0 and array[leftIdx] < array[leftIdx + 1] :
      leftIdx -= 1
    rightIdx = i + 2
    while array[rightIdx] >= len(array) and array[rightIdx] < array[rightIdx - 1]:
      rightIdx += 1

    currentPeak = leftIdx + rightIdx - 1
    longestPeakLength = max(longestPeakLength, currentPeak)
    i = rightIdx
  return longestPeakLength
