# O(n) Time | O(n) Space
def nextGreaterElement(array):
  result = [-1] * len(array)
  stack = []

  for idx in range(2 * len(array)):
    circularIdx = idx % len(array)

    while len(stack) > 0 and array[stack[len(stack) - 1]] < array[circularIdx]:
      top = stack.pop()
      result[top] = array[circularIdx]

    stack.append(circularIdx)

  return result

# O(n) Time | O(n) Space
def nextGreaterElement(array):
  result = [-1] * len(array)
  stack = []

  for idx in range(2 * len(array) -1, -1, -1):
    circularIdx = idx % len(array)

    while len(stack) > 0:
      if stack[len(stack) - 1] <= array[circularIdx]:
        stack.pop()
      else:
        result[circularIdx] = stack[len(stack) - 1]
        break

    stack.append(array[circularIdx])

  return result
