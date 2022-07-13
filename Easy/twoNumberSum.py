# O(n^2) Time | O(1) Space:
def twoNumberSum (array, targetSum):
  for i in range(len(array) -1):
    firstNum = array[i]
    for j in range(i+1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetSum:
        return [firstNum, secondNum]
  return []

# O(n) Time | O(n) Space: 
def twoNumberSum(array, targetSum):
  nums = {}
  for num in array:
    potentialSum = targetSum - num
    if potentialSum in nums:
      return [potentialSum, num]
    else:
      nums[num] = True
  return []

# O(nlog(n)) Time | O(1) Space :
def twoNumberSum (array, targetSum):
  left = 0
  right = len(array) - 1
  while left < right:
    currentSum = array[left] + array[right]
    if currentSum == targetSum:
      return [array[left], array[right]]
    elif currentSum < targetSum:
      left += 1
    elif currentSum > targetSum:
      right -= 1
  return [] 

print(twoNumberSum([2,4,6,8,-1,-4],7))