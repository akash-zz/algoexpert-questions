# O(n * l) Time | O(c) Space
def minimumCharacterForWords(words):
  maxCharacterFreq = {}
  for word in words:
    characterFreq = countCharacterFreq(word)
    updateMaxFreq(characterFreq, maxCharacterFreq)

  return makeArray(maxCharacterFreq)

def countCharacterFreq(string):
  characterFreq = {}
  for char in string:
    if char not in characterFreq:
      characterFreq[char] = 0

    characterFreq[char] += 1

  return characterFreq

def updateMaxFreq(frequencies, maxCharacterFreq):
  for character in frequencies:
    frequency = frequencies[character]

    if character in maxCharacterFreq:
      maxCharacterFreq[character] = max(frequency, maxCharacterFreq)
    else:
      maxCharacterFreq[character] = frequency

def makeArray(dictionary):
  characters = []
  for character in dictionary:
    frequency = dictionary[character]

    for _ in range(frequency):
      characters.append(character)

  return characters
