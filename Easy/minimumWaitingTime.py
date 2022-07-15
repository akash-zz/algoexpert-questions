# O(n(log(n))) Time | O(1) Space
def minimumWaitingTime(array):
  array.sort()

  totalWaitingTime = 0
  for idx, duration in enumerate(array):
    queriesLeft = len(array) - (idx + 1)
    totalWaitingTime += duration * queriesLeft
    
  return totalWaitingTime
