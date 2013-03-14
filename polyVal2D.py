import numpy as np

def polyVal2D(p, x, y, n, m):
  """
  POLYVAL2D Evaluate a 2-D polynomial using Horner's method.
  F = POLYVAL2D(P,X,Y) evaluates the 2-D polynomial P at the
  points specified by X and Y, which must be the same
  dimensions. The output F will be the same dimensions as X and 
  Y. N and M specify the order of X and Y respectively.
  """
  # TODO: check input args
  x = np.array(x)
  y = np.array(y)
  f = p[1]
  for ni in range(1, n + 1):
      f = f * x + p[1 + ni]
  npp = n + 1
  for mi in range(1, m + 1):
      g = p[npp * mi + 1]
      for ni in range(1, n + 1):
          g = g * x + p[npp * mi + 1 + ni]
      f = f * y + g
  return f
