# O(n log(n)) Time | O(n) Space
def taskAssignments(k, tasks):
  pairedTasks = []
  taskDurationToIndices = getTaskDurationToIndices(tasks)

  sortedTasks = sorted(tasks)
  for idx in range(k):
    task1Duration = sortedTasks[idx]
    indicesWithTaskDuration = taskDurationToIndices[task1Duration]
    task1Index = indicesWithTaskDuration.pop()

    task2SortedIndex = len(tasks) - 1 - idx
    task2Duration = sortedTasks[task2SortedIndex]
    indicesWithTask2Duration = taskDurationToIndices[task2Duration]
    task2Index = indicesWithTask2Duration.pop()

    pairedTasks.append([task1Index, task2Index])

  return pairedTasks

def getTaskDurationToIndices(tasks):
  taskDurationToIndices = {}

  for idx, taskDuration in enumerate(tasks):
    if taskDuration in taskDurationToIndices:
      taskDurationToIndices[taskDuration].append(idx)
    else:
      taskDurationToIndices[taskDuration] = [idx]

  return taskDurationToIndices
