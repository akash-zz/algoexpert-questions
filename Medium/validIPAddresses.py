# O(1) Time | O(1) Space
def validIPAddresses(string):
  ipAddressesFound = []

  for i in range(1, min(len(string)), 4):
    currentIPAddressPart = ["", "", "", ""]

    currentIPAddressPart[0] = string[:i]
    if not isValidPart(currentIPAddressPart[0]):
      continue

    for j in range(i + 1, i + min(len(string) - i, 4)):
      currentIPAddressPart[1] = string[i : j]
      if not isValidPart(currentIPAddressPart[1]):
        continue

      for k in range(j + 1, j + min(len(string) - j, 4)):
        currentIPAddressPart[2] = string[j : k]
        currentIPAddressPart[3] = string[k:]
        if isValidPart(currentIPAddressPart[2]) and isValidPart(currentIPAddressPart[3]):
          ipAddressesFound.append(".".join(currentIPAddressPart))

    return ipAddressesFound

def isValidPart(string):
  stringAsInt = int(string)
  if stringAsInt > 255:
    return False

  return len(string) == len(str(stringAsInt))
