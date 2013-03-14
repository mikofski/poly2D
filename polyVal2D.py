import numpy as np

def polyVal2D(p, x, y, n, m):
  """
  polyVal2D(p, x, y, n, m)
  
  Evaluate a 2-D polynomial using Horner's method.
  
  Evaluates the 2-D polynomial p at the points specified by X
  and Y, which must be the same dimensions. The output F will
  be the same dimensions as X and Y. N and M specify the order
  of X and Y respectively.
  
  Parameters
  ----------
  p : array_like
      Polynomial coefficients in order specified by polyVal2D.html.
  x : array_like
      Values of 1st independent variable.
  y : array_like
      Values of 2nd independent variable.
  n : int
      Order of the 1st independent variable, `x`.
  m : int
      Order of the 2nd independent variable, `y`.
  
  Returns
  -------
  f : ndarray
      Values of the evaluated 2-D polynomial.
  
  See Also
  --------
  numpy.polyval : Evaluate a polynomial at specific values.
  
  Example
  --------
  >>> polyVal2D(np.array([1,2,3,4,5,6,7,8,9]),5,6,2,2)
  2802
  """
  # TODO: check input args
  x = np.array(x)
  y = np.array(y)
  f = p[1]
  for ni in range(n):
      f = f * x + p[1 + ni]
  npp = n + 1
  for mi in range(m):
      g = p[npp * mi + 1]
      for ni in range(n):
          g = g * x + p[npp * mi + 1 + ni]
      f = f * y + g
  return f
