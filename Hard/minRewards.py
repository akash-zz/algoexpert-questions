# O(n^2) Time | O(n) Space
def minRewards(scores):
  rewards = [1 for _ in scores]

  for i in range(1, len(scores)):
    j = i - 1
    if scores[i] > scores[j]:
      rewards[i] += rewards[j] + 1
    else:
      while j >= 0 and scores[j] > scores[j + 1]:
        rewards[j] = max(rewards[j], rewards[j + 1] + 1)
        j -= 1

  return sum(rewards)

# O(n) Time | O(n) Space
def minRewards(scores):
  rewards = [1 for _ in scores]
  for i in range(1, len(scores)):
    if scores[i] > scores[i - 1]:
      rewards[i] = scores[i - 1] + 1

  for i in reversed(range(len(scores) - 1)):
    if scores[i] > scores[i + 1]:
      rewards[i] = max(scores[i], scores[i + 1] + 1)

  return sum(rewards)
