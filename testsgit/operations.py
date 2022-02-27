# Module for implementation of basic operations

from audioop import add


def addition(a,b,c):
  """
  Function returning addition of 3 numbers
  """
  return a+b+c

def custom_operation(a,b,c):
  """
  Our super useful operation
  """

  return multiplication(a,b, addition(a,b,c))

def multiplication(a, b):
  """
  Function returning multiplication of  numbers
  """
  return a*b
