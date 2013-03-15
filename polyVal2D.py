import numpy as np

def polyVal2D(p, x, y, n, m):
  """
  polyVal2D(p, x, y, n, m)
  
  Evaluate a 2-D polynomial using Horner's method.
  
  Evaluates the 2-D polynomial `p` at the points specified by `x`
  and `y`, which must be the same dimensions. The output `f` will
  have the same dimensions as `x` and `y`. The order of `x` and `y`
  are specified by `n` and `m`, respectively.
  
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
  >>> (5**2 * 6**2 + 2 * 5 * 6**2 + 3 * 6**2 + 4 * 5**2 * 6 +
  ...  5 * 5 * 6 + 6 * 6 + 7 * 5**2 + 8 * 5 + 9)
  2378
  >>> polyVal2D(np.array([1,2,3,4,5,6,7,8,9]),5,6,2,2)
  2378
  >>> 5 * 6 + 2 * 6 + 3 * 5 + 4
  61
  >>> polyVal2D(np.array([1,2,3,4]),5,6,1,1)
  61
  """
  # TODO: check input args
  x = np.array(x)
  y = np.array(y)
  f = p[0]
  for ni in range(n):
    f = f * x + p[1 + ni]
  for mi in range(m):
    mpp = (n + 1) * (mi + 1)
    g = p[mpp]
    for ni in range(n):
      g = g * x + p[mpp + 1 + ni]
    f = f * y + g
  return f
