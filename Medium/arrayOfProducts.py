# O(n^2) Time | O(n) Space
def arrayOfProducts(array):
  productArray = [1 for _ in range(len(array))]
  for i in range(len(array)):
    product = 1
    for j in range(len(array)):
      if i  != j:
        product *= array[j]
      productArray[i] = product
  return productArray

# O(n) Time | O(n) Space
def arrayOfProducts(array):
  product = 1
  productArray = []
  for i in range(len(array)):
    product *= array[i]
  for i in range(len(array)):
    productArray.append(product // array[i])
  return productArray
