from math import floor, sqrt

def is_prime(num):
  if num <= 1:
      return False
  for i in range(2, floor(sqrt(num)+1)):
      if num % i == 0:
          return False
  return True