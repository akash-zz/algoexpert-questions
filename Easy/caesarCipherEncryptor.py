# O(n) Time | O(n) Space
def caesarCipherEncryptor(string, key):
  newLetter = []
  newKey = key % 26
  for letter in string:
    newLetter.append(getNewLetter(letter, newKey))
  return "".join(newLetter)

def getNewLetter(letter, key):
  newLetterCode = ord(letter) + key
  return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

# O(n) Time | O(n) Space
def caesarCipherEncryptor(string, key):
  newLetter = []
  newKey = key % 26
  alphabet = list("abcdefghijklmnopqrstuvwxyz")
  for letter in string:
    newLetter.append(getNewLetter(letter, newKey, alphabet))
  return "".join(newLetter)

def getNewLetter(letter, key, alphabet):
  newLetterCode = ord(letter) + key
  return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]