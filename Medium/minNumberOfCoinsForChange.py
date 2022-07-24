# O(nd) Time | O(n) Space
def minNumberOfCoinsForChange(n, denominators):
  numOfCoins = [float("inf") for amount in range(n + 1)]
  for denominator in denominators:
    for amount in range(len(numOfCoins)):
      if denominator <= amount:
        numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denominator])
  return numOfCoins[n] if numOfCoins[n] != float("inf") else -1
