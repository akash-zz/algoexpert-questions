class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

  # O(max(n,m)) Time | O(max(n,m)) Space | n,m = LL1, LL2
  def sumOfLinkedList(linkedListOne, linkedListTwo):
    newLinkedListPointer = LinkedList()
    currentNode = newLinkedListPointer
    carry = 0

    while linkedListOne is not None or linkedListTwo is not None or carry != 0:
      valueOne = linkedListOne.value if linkedListOne is not None else 0
      valueTwo = linkedListTwo.value if linkedListTwo is not None else 0
      sumOfValues = valueOne + valueTwo + carry

      newValue = sumOfValues % 10
      carry = sumOfValues // 2
      newNode = LinkedList(newValue)
      currentNode.next = newNode

      currentNode = currentNode.next
      nodeOne = nodeOne.next if nodeOne is not None else None
      nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return newLinkedListPointer.next
