class MinMaxStack:
  def __init__(self):
    self.minMaxStack = []
    self.stack = []

  # O(1) Time | O(1) Space
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # O(1) Time | O(1) Space
  def pop(self):
    self.minMaxStack.pop()
    return self.stack.pop()

  # O(1) Time | O(1) Space
  def push(self,number):
    newMinMax = {"min": number, "max": number}

    if len(self.minMaxStack):
      lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
      newMinMax["min"] = min(lastMinMax["min"], number)
      newMinMax["max"] = max(lastMinMax["max"], number)

    self.minMaxStack.append(newMinMax)
    self.stack.append(number)

  # O(1) Time | O(1) Space
  def getMin(self):
    return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

  # O(1) Time | O(1) Space
  def getMax(self):
    return self.minMaxStack[len(self.minMaxStack) - 1]["max"]
