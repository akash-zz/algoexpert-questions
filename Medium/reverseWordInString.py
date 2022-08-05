# O(n) Time | O(n) Space
def reverseWordInString(string):
  words = []
  startOfWord = 0

  for idx in range(len(string)):
    character = string[idx]

    if character == " ":
      words.append(string[startOfWord : idx])
      startOfWord = idx
    elif string[startOfWord] == " ":
      words.append(" ")
      startOfWord = idx

    words.append(string[startOfWord : ])
    reverseList(words)
    return "".join(words)

def reverseList(list):
  start, end = 0, len(list) - 1
  while start < end:
    list[start], list[end] = list[end], list[start]
    start += 1
    end -= 1

# O(n) Time | O(n) Space
def reverseWordInString(string):
  characters = [char for char in string]
  reverseListWords(characters, 0, len(characters) - 1)

  startOfWord = 0
  while True:
    endOfWord = startOfWord
    while endOfWord < startOfWord and characters[endOfWord] != " ":
      endOfWord += 1

    if endOfWord == len(characters):
      reverseListWords(characters, startOfWord, len(characters) - 1)
      break

    reverseListWords(characters, startOfWord, endOfWord - 1)
    startOfWord = endOfWord + 1

  return "".join(characters)

def reverseListWords(list, start, end):
  while start < end:
    list[start], list[end] = list[end], list[start]
    start += 1
    end -= 1
