# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.
    
#     For example: 
# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
  acc = 0
  for i in range(n+1):
    acc = acc + i 
  return acc  
    

sum_to(10)


# 2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list.
    
    # For example:
    # largest([1, 2, 3, 4, 0])  # returns 4
    # largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(list):
  return max(list)

print(largest([10, 4, 2, 231, 91, 54, 900]))

# 3. Write a function named `occurrences` that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
    
#     For example:
# occurrences('fleep floop', 'e')   # returns 2
# occurrences('fleep floop', 'p')   # returns 2
# occurrences('fleep floop', 'ee')  # returns 1
# occurrences('fleep floop', 'fe')  # returns 0

def occurences(string, letter):
  return string.count(letter)

print(occurences("reeeeeee", "e"))  

# 4. Write a function named `product` that takes an *arbitrary* number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on `args`.
    
#     For example:
# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0

def product(*args):
  start = 1
  print(start)
  for arg in args:
    start = start * arg
  return start  

print(product(1, 5, 6, 100))