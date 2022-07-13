# O(nlogn) Time bcz of Sorting | O(1) Space

def nonDestructibleChange (coins):
  coins.sort()

  currentChangeCreated = 0
  for coin in coins:
    if coin > currentChangeCreated + 1:
      return currentChangeCreated + 1
    
    currentChangeCreated += coin
  
  return currentChangeCreated +1