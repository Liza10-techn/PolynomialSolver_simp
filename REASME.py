#GeneralPolynomialSolver
#installing sympy
import sympy as sp
#example of a polynomial equation
x=sp.Symbol ('x')
eq=2*x**2-3*x+1
#asking for a solution
from sympy import symbols, Eq, solve
x=symbols('x')
roots=sp.solve (eq,x)
#finding the sum and the product of the roots
sum_roots= sum(roots)
product_roots=sp.prod(roots)
print("Roots:", roots)
print("The sum of the roots:", sum_roots)
print("The product of the roots:", product_roots)
