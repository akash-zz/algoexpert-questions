# O(m * (m +n)) Time | O(1) Space
def generateDocument(characters, document):
  for character in document:
    charFreq = countCharFreq(character, characters)
    docFreq = countCharFreq(character, document)

    if docFreq > charFreq:
      return False
    
  return True

# O(c * (m+n)) Time | O(c) Space
def generateDocument(characters, document):
  alreadyCounted = set()

  for character in characters:
    if character in alreadyCounted:
      continue

    charFreq = countCharFreq(character, characters)
    docFreq = countCharFreq(character, document)

    if charFreq > docFreq:
      return False
  
    alreadyCounted.add(character)
  return True


def countCharFreq(character, target):
  frequency = 0
  for char in target:
    if char == character:
      frequency += 1
  
  return frequency

# O(n + m) Time | O(c) Space
def generateDocument(characters, document):
  characterCounts = {}

  for character in characters:
    if character not in characterCounts:
      characterCounts[character] = 0
    
    characterCounts += 1

  for character in document:
    if character not in characterCounts or characterCounts[character] == 0:
      return False
    
    characterCounts[character] -= 1
  
  return True