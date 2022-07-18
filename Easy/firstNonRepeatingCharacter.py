# O(n^2) Time | O(1) Space
def firstNonRepeatingCharacter(string):
  for idx in range(len(string)):
    foundDuplicate = False
    for idx2 in range(len(string)):
      if string[idx] == string[idx2] and idx != idx2:
        foundDuplicate = True
      
      if not foundDuplicate:
        return idx
  
  return -1

# O(n) Time | O(1) Space
def firstNonRepeatingCharacter(string):
  charFreq = {}

  for character in string:
    charFreq[character] = charFreq.get(character, 0) + 1
  
  for idx in range(len(string)):
    character = string[idx]
    if charFreq[character] == 1:
      return idx
  
  return -1
