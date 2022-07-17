# O(n^2) Time | O(n) Space
def isPalindrome(string):
  reversedString = ""
  for i in reversed(range(string)):
    reversedString += string[i]
  return string == reversedString

# O(n) Time | O(1) Space
def isPalindrome(string):
  reverseChars = []
  for i in reversed(range(string)):
    reverseChars.append(string[i])
  return string == "".join(reverseChars)

#O(n) Time | O(n) Space
def isPalindrome(string, i = 0):
  j = len(string) - 1 - i
  return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

# Tail Recursion
# O(n) Time | O(n) Space
def isPalindrome(string, i = 0):
  j  = len(string) - 1 - i
  if i >= j :
    return True
  if string[i] != string[j]:
    return False
  return isPalindrome(string, i + 1) 

# O(n) Time | O(1) Space
def isPalindrome(string):
  leftIdx = 0
  rightIdx = len(string) - 1
  while leftIdx < rightIdx:
    if string[leftIdx] != string[rightIdx]:
      return False
    leftIdx += 1
    rightIdx -= 1
  return True