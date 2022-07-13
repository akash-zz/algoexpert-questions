# O(n) Time | O(1) Space:
def validSubsequence (array, sequence):
  arrIdx = 0
  seqIdx = 0
  while arrIdx < len(array) and seqIdx < len(sequence):
    if array[arrIdx] == sequence[seqIdx]:
      seqIdx += 1
    arrIdx += 1
  return seqIdx == len(sequence)

#Using For Loop:
# Same space and time complexity:
def validSubsequence (array, sequence):
  seqIdx = 0
  for num in array:
    if seqIdx == len(sequence):
      break
    if sequence[seqIdx] == num:
      seqIdx += 1
  return seqIdx == len(sequence)