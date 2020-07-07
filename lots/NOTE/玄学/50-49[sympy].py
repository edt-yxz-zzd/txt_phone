'''
class sympy.polys.domains.quotientring.QuotientRing(ring, ideal)
Class representing (commutative) quotient rings.
You should not usually instantiate this by hand, instead use the constructor from the
base ring in the construction.
>>> from sympy.abc import x
>>> from sympy import QQ
>>> I = QQ.old_poly_ring(x).ideal(x**3 + 1)
>>> QQ.old_poly_ring(x).quotient_ring(I)
QQ[x]/<x**3 + 1>
Shorter versions are possible:
>>> QQ.old_poly_ring(x)/I
QQ[x]/<x**3 + 1>
>>> QQ.old_poly_ring(x)/[x**3 + 1]
QQ[x]/<x**3 + 1
'''

from sympy.abc import x
import sympy as s
from sympy import Poly


def f1():
    F = s.FiniteField(7)
    p = s.poly('x**2 + x + 3', domain=F)
    r = s.poly('x', domain=F)
    (r**48) % p # == 1
    (r**24) % p # == -1
    (r**16) % p # == 2
    assert (r**48) % p == 1
    assert (r**24) % p == -1
    assert (r**16) % p == 2
    p1 = p

    p = s.poly('x**2 + 1', domain=F)
    p2 = p
    if 1:
        r = s.poly('x+2', domain=F)
        (r**48) % p # == 1
        (r**24) % p # == -1
        (r**16) % p # == -3
        assert (r**48) % p == 1
        assert (r**24) % p == -1
        assert (r**16) % p == -3
    if 1:
        r = s.poly('x+3', domain=F)
        (r**48) % p # == 1
        (r**24) % p # == -1
        (r**16) % p # == 2
        assert (r**48) % p == 1
        assert (r**24) % p == -1
        assert (r**16) % p == 2


    ct = F.convert
    one = ct(1)
    p1 = s.poly(one*(x**2 + x + 3), domain=F)
    p2 = s.poly(one*(x**2 + 1), domain=F)
    def mk(poly):
        return s.poly(one*poly, domain=F)

p1 = x**2 + x + 3
p2 = x**2 + 1

def show_primitive_elements_and_roots(*
    , eqn_poly, modulus_poly, prime, order, var
    ):
    if order != 2: raise NotImplementedError
    assert order == 2
    assert prime & 1
    x = var
    p = prime
    n = order
    q = p**n
    F = s.FiniteField(prime)
    F = s.FiniteField(prime, symmetric=False)
    F = s.FiniteField(prime, symmetric=True)
    ct = F.convert
    one = ct(1)
    print(f'GF({p}); GF({p}**{n})')
    print(f'eqn_poly = {eqn_poly}')
    print(f'modulus_poly = {modulus_poly}')

    def power(base, exp, modulus):
        #r = pow(base, exp, modulus)
        r = s.rem(base**exp, modulus, domain=F)
        #r = s.poly(r, x, domain=F)
        #print(r)
        return r

    ith = 0
    for i in range(1,p):
        for j in range(p):
            #r = s.poly(f'{i}*x+{j}', domain=F)
            #r = s.poly(one*(i*x+j), domain=F)
            r = i*x+j
            rr = s.poly(one*r, domain=F).as_expr()
            #assert r == 0 or (r**48) % modulus_poly == 1
            assert r == 0 or power(r, 48, modulus_poly) == 1
            #if (r**24) % modulus_poly == -1 and (r**16) % modulus_poly in (2,-3):
            if power(r, 24, modulus_poly) == -1 and power(r, 16, modulus_poly) in (2,-3):
                ith += 1
                print(f'{ith}-th primitive element: {rr}')
            #elif (r**24) % modulus_poly != 1 != (r**16) % modulus_poly:
            elif power(r, 24, modulus_poly) != 1 != power(r, 16, modulus_poly):
                print(f'!!!!!!!!!!primitive element: {rr}!!!!!!!!!!!!')

            ff = eqn_poly.subs(x, i*x+j);
            ff = ff.expand();
            ff = s.rem(ff, modulus_poly, domain=F)
            #ff = s.poly(ff, x, domain=F); #print(ff)
            if ff.is_zero:
                print(f'root of {eqn_poly} == {rr}')

f1()
show_primitive_elements_and_roots(eqn_poly=p1, modulus_poly=p1, prime=7, order=2, var=x)
show_primitive_elements_and_roots(eqn_poly=p1, modulus_poly=p2, prime=7, order=2, var=x)

