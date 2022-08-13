# O(n^2) Time | O(n) Space
def maxSumIncreasingSubsequence(array):
  sequences = [None for x in array]
  sums =array[:]
  maxIdx = 0

  for i in range(len(array)):
    currentNum = array[i]
    for j in range(0, i):
      otherNum = array[i]
      if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
        sums[i] = sums[j] + currentNum
        sequences[i] = j
      if sums[i] > sums[maxIdx]:
        maxIdx = i

  return [sums[maxIdx], buildSequence(array, sequences, maxIdx)]

def buildSequence(array, sequences, currentIdx):
  sequence = []
  while currentIdx is not None:
    sequence.append(array[currentIdx])
    currentIdx = sequences[currentIdx]
  return list(reversed(sequence))
