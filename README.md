Py # PolynomialSolver_simplified
#installing sympy
import sympy as sp
from sympy import symbols,Eq,expand,simplify
x=sp.Symbol('x')
#example of a polynomial equation
equation= sp.Eq(x*(x+8),4-3*x)
#put everything to the left side of the equation, so the right side will be equal to the 0
left_side= sp.expand(x*(x+8)-(4-3*x))
#simplyfying
simplified= sp.simplify(left_side)
print("The simplified equation :")
print(simplified,"=0")
#finding the sum and the product of the roots
roots=sp.solve(simplified,x)
print("Roots:", roots)
if len(roots)==2: #if whe have 2 roots
    discr_roots= roots[0] * roots[1]
    sum_roots= roots[0] + roots[1]
    product_roots= roots[0]*roots[1]
    print("The sum of the roots:", sum_roots)
    print("The discriminant of the roots:",discr_roots)#finding discriminant
    print("The product of the roots:",float(product_roots))
else:
    print("Equation does not have exactly 2 roots:")
