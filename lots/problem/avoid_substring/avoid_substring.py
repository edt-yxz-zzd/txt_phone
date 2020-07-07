
# import sympy
from sympy.matrices import Matrix
import sympy as S
from sympy import collect, expand
from sympy import simplify # not sympify
from sympy.simplify import combsimp
from sympy.assumptions.refine import refine
# how to express 'Size >= 2' and pass it to Symbol??
Size = sympy.Symbol('Size', positive=True, integer=True)
def mkStateTF__aaa(SepLen, Size = Size):
    assert SepLen > 0
    mx = [[Size - 1] * SepLen]
    for row in range(1, SepLen):
        col = row - 1
        ls = [0] * SepLen
        ls[col] = 1
        mx.append(ls)
    return Matrix(mx)

mx = mkStateTF__aaa(4)
print(mx)
#mx.jordan_form()
mx.subs(Size,2).jordan_form()
if 0:
    mx4 = mx**4
    mx4 = simplify(mx4)
    mx4 = combsimp(mx4)
    Matrix([
        [Size**3*(Size - 1), (Size - 1)**2*(Size**2 + Size + 1), Size*(Size - 1)**2*(Size + 1), Size**2*(Size - 1)**2],
        [Size**2*(Size - 1),                 Size**2*(Size - 1),      (Size - 1)**2*(Size + 1),    Size*(Size - 1)**2],
        [   Size*(Size - 1),                    Size*(Size - 1),               Size*(Size - 1),         (Size - 1)**2],
        [          Size - 1,                           Size - 1,                      Size - 1,              Size - 1]])

def simp_power(mx, n):
    mx = mx**n
    mx = simplify(mx)
    mx = combsimp(mx)
    return mx
simp_power(mx, 8)


