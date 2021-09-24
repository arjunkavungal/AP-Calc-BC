from sympy import *
 
x = symbols('x')
expr = 1 / x ** 2;
   
print(limit(expr, x, 0) )
