# O(nlog(n) + mlog(n)) Time | O(1) Space
def smallestDifference(array1, array2):
    array1.sort()
    array2.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while idxOne < len(array1) and idxTwo < len(array2):
        firstNum = array1[idxOne]
        secondNum = array2[idxTwo]
        if firstNum < secondNum:
            current =  firstNum - secondNum
            idxOne += 1
        elif secondNum > firstNum:
            current = secondNum - firstNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
