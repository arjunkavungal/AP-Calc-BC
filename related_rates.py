"""A Circle's radius is 5 cm. It increases at 3 cm/sec.
How much does the area increase per second."""

#Area of a circle: pi*r**2
from scipy.misc import derivative
import math
dr = 3
def A(r):
  return math.pi * r ** 2
print(derivative(A, 5, dx = 1e-6) * dr)
