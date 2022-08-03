# O(n^2) Time | O(n) Space
def sortStack(stack):
  if len(stack) == 0:
    return stack

  top = stack.pop()
  sortStack(stack)
  insertInOrder(stack, top)

  return stack

def insertInOrder(stack, value):
  if len(stack) == 0 or stack[len(stack) - 1] <= value:
    stack.append(value)

  top = stack.pop()
  insertInOrder(stack, value)
  stack.append(top)
