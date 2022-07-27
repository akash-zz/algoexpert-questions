# # O(v + e) Time | O(v) Space -> v,e = Vertices, Edges
def cycleInGraph(edges):
  numberOfNodes = len(edges)
  visited = [False for _ in range(numberOfNodes)]
  currentlyInStack = [False for _ in range(numberOfNodes)]

  for node in range(numberOfNodes):
    if visited[node]:
      continue
    containsCycle = isNodeInCycle(edges, node, visited, currentlyInStack)
    if containsCycle:
      return True
  return False

def isNodeInCycle(edges, node, visited, currentlyInStack):
  visited[node] = True
  currentlyInStack[node] = True

  neighbors = edges[node]
  for neighbor in neighbors:
    if not visited[neighbor]:
      containsCycle = isNodeInCycle(edges, neighbor, visited, currentlyInStack)
      if containsCycle:
        return True
    elif currentlyInStack[neighbor]:
      return True

  currentlyInStack[node] = False
  return False

# WHITE = Not Visited
# GREY = Currently in Stack
# BLACK = Finished processing all its nodes
# O(v + e) Time | O(v) Space
WHITE, GREY, BLACK = 0,1,2

def cycleInGraph(edges):
  numberOfNodes = len(edges)
  colors = [WHITE for _ in range(len(numberOfNodes))]

  for node in range(numberOfNodes):
    if colors[node] != WHITE:
      continue
    containsCycle = traverseAndColorNodes(node, edges, colors)
    if containsCycle:
      return True
  return False

def traverseAndColorNodes(node, edges, colors):
  colors[node] = GREY

  neighbors = edges[node]
  for neighbor in neighbors:
    neighborColor = colors[neighbor]
    if neighborColor == GREY:
      return True
    if neighborColor != WHITE:
      continue

    containsCycle = traverseAndColorNodes(neighbor, edges, colors)
    if containsCycle:
      return True

  colors[node] = BLACK
  return False
