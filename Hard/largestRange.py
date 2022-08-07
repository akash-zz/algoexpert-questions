# O(n) Time | O(n) Space
def largestRange(array):
  nums = {}
  longestRange = 0
  bestRange = []

  for num in array:
    nums[num] = True

  for num in array:
    if not nums[num]:
      continue
    nums[num] = False
    currentLength = 0
    left = num - 1
    right = num + 1

    while left in nums:
      currentLength += 1
      left -= 1
    while right in nums:
      currentLength += 1
      right += 1

    if currentLength > longestRange:
      longestRange = currentLength
      bestRange = [left + 1, right - 1]

    return bestRange
