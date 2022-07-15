from audioop import reverse
from tkinter.tix import Tree


# Time O(n(log(n))) | Space O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
  redShirtHeights.sort(reverse = True)
  blueShirtHeights.sort(reverse = True)

  shirtColorInFront = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
  for idx in range(len(redShirtHeights)):
    redShirtHeight = redShirtHeights[idx]
    blueShirtHeight = blueShirtHeights[idx]

    if shirtColorInFront == 'RED':
      if redShirtHeight >= blueShirtHeight:
        return False
      else:
        if blueShirtHeight >= redShirtHeight:
          return False

  return True