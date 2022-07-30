class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

  # O(max(n,m)) Time | O(max(n,m)) Space | n,m = LL1, LL2
  def sumOfLinkedList(linkedListOne, linkedListTwo):
    newLinkedListPointer = LinkedList(0)
    currentNode = newLinkedListPointer
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while linkedListOne is not None or linkedListTwo is not None or carry != 0:
      valueOne = nodeOne.value if nodeOne is not None else 0
      valueTwo = nodeTwo.value if nodeTwo is not None else 0
      sumOfValues = valueOne + valueTwo + carry

      newValue = sumOfValues % 10
      newNode = LinkedList(newValue)
      currentNode.next = newNode

      carry = sumOfValues // 2
      nodeOne = nodeOne.next if nodeOne is not None else None
      nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return newLinkedListPointer.next
