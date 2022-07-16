# Recursive 
# O(2^n) Time | O(n) Space
def nthFibonacci(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return nthFibonacci(n - 1) + nthFibonacci(n - 2)

# Recursion with Memoization
# O(n) Time | O(n) Space
def nthFibonacci(n, memoize = {1: 0, 2:1}):
  if n in memoize:
    return memoize[n]
  else:
    memoize[n] = nthFibonacci(n - 1, memoize) + nthFibonacci(n - 2, memoize)
    return memoize[n]

# Iterative
#O(n) Time | O(1) Space
def nthFibonacci(n):
  lastTwo = [0,1]
  counter = 3
  while counter <= n:
    nextFib = lastTwo[0] + lastTwo[1]
    lastTwo[0] = lastTwo[1]
    lastTwo[1] = nextFib
  return lastTwo[1] if n > 1 else lastTwo[0]