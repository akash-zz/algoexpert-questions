# O(nd) Time | O(n) Space
def numberOfWaysToMakeChange(n, denominators):
  ways = [0 for amount in range(n + 1)]
  ways[0] = 1
  for denominator in denominators:
    for amount in range(2, n + 1):
      if denominator <= amount:
        ways[amount] += ways[amount - denominator]
  return ways[n]
