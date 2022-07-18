# O(n) Time | O(n) Space
def runLengthEncoding(string):
  outputString = []
  length = 1
  
  for i in range(1, len(string)):
    currentCharacter = string[1]
    previousCharacter = string[i - 1]

    if currentCharacter != previousCharacter or length == 9:
      outputString.append(str(length))
      outputString.append(previousCharacter)
      length = 0
    
    length += 1
  
  outputString.append(str(length))
  outputString.append(string[len(string) -1])

  return "".join(outputString)
