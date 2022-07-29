# O(n) Time | O(1) Space
def removeNodeFromEnd(head, n):
  counter = 1
  first = head
  second = head
  while counter <= n:
    second = second.next
    counter += 1

  if second is None:
    head.value = head.next.value
    head.next = head.next.next

  while second.next is not None:
    first = first.next
    second = second.next
  first.next = first.next.next
