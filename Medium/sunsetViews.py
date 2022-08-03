# O(n) Time | O(n) Space
def sunsetViews(buildings, direction):
  buildingsWithSunsetViews = []

  startIdx = 0 if direction == "WEST" else len(buildings) - 1
  step = 1 if direction == "WEST" else - 1

  idx = startIdx
  runningMaxHeight = 0

  while idx >= 0 and idx < len(buildings):
    buildingsHeight =  buildings[idx]

    if buildingsHeight > runningMaxHeight:
      buildingsWithSunsetViews.append(idx)

    runningMaxHeight = max(runningMaxHeight, buildingsHeight)
    idx += step

  if direction == "EAST":
    return buildingsWithSunsetViews[::-1]

  return buildingsWithSunsetViews

# O(n) Time | O(n) Space
def sunsetViews(buildings, direction):
  candidateBuildings = []

  startIdx = 0 if direction == "EAST" else len(buildings) - 1
  step = 1 if direction == "EAST" else -1

  idx = startIdx

  while idx >= 0 and idx < len(buildings):
    buildingsHeight = buildings[idx]

    while len(candidateBuildings) > 0 and buildingsHeight[candidateBuildings[-1]] <= buildingsHeight:
      candidateBuildings.pop()

    candidateBuildings.append(idx)
    idx += step

  if direction == "WEST":
    return candidateBuildings[::-1]

  return candidateBuildings
