
'''
rationalizing radical denominator
    TODO
    it seems sympy radsimp/max_terms <= 4
rationalizing sqrt denominator
    f<n>(a2,b2,...)/sum(a,b,...)
    f<n> = ??
        see:
            eval_sqrt_rational_product_at__ver2
            is_sqrt_rational_product
        f(xs^2...) = II(x0[+-]x1[+-]x2...)
            # sign(xi) in (1,-1)
            # only sign(x0)===1
            # total number of product terms == 2**(n-1) == sum of exp



sqrt:
n=1
product=x0**2
n=2
product=x0**2 - x1**2
    (x0 - x1)(x0 + x1)
n=3
product=x0**4 - 2*x0**2*x1**2 - 2*x0**2*x2**2 + x1**4 - 2*x1**2*x2**2 + x2**4
    (x0 - x1 - x2)*(x0 - x1 + x2)*(x0 + x1 - x2)*(x0 + x1 + x2)
n=4
product=x0**8 - 4*x0**6*x1**2 - 4*x0**6*x2**2 - 4*x0**6*x3**2 + 6*x0**4*x1**4 + 4*x0**4*x1**2*x2**2 + 4*x0**4*x1**2*x3**2 + 6*x0**4*x2**4 + 4*x0**4*x2**2*x3**2 + 6*x0**4*x3**4 - 4*x0**2*x1**6 + 4*x0**2*x1**4*x2**2 + 4*x0**2*x1**4*x3**2 + 4*x0**2*x1**2*x2**4 - 40*x0**2*x1**2*x2**2*x3**2 + 4*x0**2*x1**2*x3**4 - 4*x0**2*x2**6 + 4*x0**2*x2**4*x3**2 + 4*x0**2*x2**2*x3**4 - 4*x0**2*x3**6 + x1**8 - 4*x1**6*x2**2 - 4*x1**6*x3**2 + 6*x1**4*x2**4 + 4*x1**4*x2**2*x3**2 + 6*x1**4*x3**4 - 4*x1**2*x2**6 + 4*x1**2*x2**4*x3**2 + 4*x1**2*x2**2*x3**4 - 4*x1**2*x3**6 + x2**8 - 4*x2**6*x3**2 + 6*x2**4*x3**4 - 4*x2**2*x3**6 + x3**8
    (x0 - x1 - x2 - x3)*(x0 - x1 - x2 + x3)*(x0 - x1 + x2 - x3)*(x0 - x1 + x2 + x3)*(x0 + x1 - x2 - x3)*(x0 + x1 - x2 + x3)*(x0 + x1 + x2 - x3)*(x0 + x1 + x2 + x3)


product<n=4>=
x0**8
+ x1**8
+ x2**8
+ x3**8
- 40*x0**2*x1**2*x2**2*x3**2

- 4*x0**6*x1**2
- 4*x0**6*x2**2
- 4*x0**6*x3**2
- 4*x0**2*x1**6
- 4*x0**2*x2**6
- 4*x0**2*x3**6
- 4*x1**6*x2**2
- 4*x1**6*x3**2
- 4*x1**2*x2**6
- 4*x1**2*x3**6
- 4*x2**6*x3**2
- 4*x2**2*x3**6

+ 4*x0**4*x1**2*x2**2
+ 4*x0**4*x1**2*x3**2
+ 4*x0**4*x2**2*x3**2
+ 4*x0**2*x1**4*x2**2
+ 4*x0**2*x1**4*x3**2
+ 4*x0**2*x1**2*x2**4
+ 4*x0**2*x1**2*x3**4
+ 4*x0**2*x2**4*x3**2
+ 4*x0**2*x2**2*x3**4
+ 4*x1**4*x2**2*x3**2
+ 4*x1**2*x2**4*x3**2
+ 4*x1**2*x2**2*x3**4

+ 6*x0**4*x1**4
+ 6*x0**4*x2**4
+ 6*x0**4*x3**4
+ 6*x1**4*x2**4
+ 6*x1**4*x3**4
+ 6*x2**4*x3**4
<end of product>

'''

'''
sympy.simplify.simplify.radsimp(expr, symbolic=True, max_terms=4)
Rationalize the denominator by removing square roots.
Note: the expression returned from radsimp must be used with caution since if the denominator contains symbols, it will be possible to make substitutions that violate the assumptions of the simplification process: that for a denominator matching a + b*sqrt(c), a != +/-b*sqrt(c). (If there are no symbols, this assumptions is made valid by collecting terms of sqrt(c) so the match variable a does not contain sqrt(c).) If you do not want the simplification to occur for symbolic denominators, set symbolic to False.
If there are more than max_terms radical terms do not simplify.
Examples
>>> from sympy import radsimp, sqrt, Symbol, denom, pprint, I
>>> from sympy.abc import a, b, c
>>> radsimp(1/(I + 1))
(1 - I)/2
>>> radsimp(1/(2 + sqrt(2)))
'''

import sympy
from sympy.abc import a,b,c
from sympy import sqrt, radsimp, fraction, symbols
from pprint import pprint
def pdir(x): pprint(dir(x))

def is_denominator_1(x):
    numerator, denominator = fraction(x)
    return denominator == 1

def is_polynomial(expr):
    return expr.is_polynomial()
def rationalizing_radical_denominator(radical_denominator):
    #denominator = sqrt(a)+sqrt(b)+sqrt(c)
    assert is_denominator_1(radical_denominator)
    assert not radical_denominator.is_polynomial()
    num_terms = radical_denominator.as_poly().length()
    x = radsimp(1/radical_denominator, max_terms=num_terms)
        # max_terms cannot >= 5?????????
    #numerator, denominator
    rationalizor, product = fraction(x)
    try:
        assert not rationalizor.is_polynomial()
        assert product.is_polynomial()
    except:
        print(f'rationalizor={rationalizor}')
        print(f'product={product}')
        print(f'num_terms={num_terms}')
        raise
    return rationalizor, product
def eval_rationalizor_at(n:int):
    # n=3: denominator = sqrt(a)+sqrt(b)+sqrt(c)
    assert n >= 1
    xs = symbols(f'x:{n}')
    denominator = sum(map(sqrt, xs))
    rationalizor, product = rationalizing_radical_denominator(denominator)
    return rationalizor



# fail at n >= 5
def main1(n, begin=1):
    #pprint(list(map(eval_rationalizor_at, range(begin, n))))
    for i in range(begin, n):
        print(i)
        print(eval_rationalizor_at(i))
#main1(6, 1)

from sympy import solve, linsolve
def rationalizing_sqrt_denominator(sqrt_denominator):
    #denominator = sqrt(a)+sqrt(b)+sqrt(c)
    assert is_denominator_1(radical_denominator)
    assert not radical_denominator.is_polynomial()

def is_sqrt_rational_product(xs, product):
    xs = tuple(xs)
    n = len(xs)
    assert n > 0
    L = 1+max(len(str(x)) for x in xs)
    y = symbols('x'*L)
    assert y not in xs

    product = product
    denominator = sum(xs).as_poly()
    rationalizor = product/denominator
    rationalizor = rationalizor.simplify()
    if not rationalizor.is_polynomial():
        print('why False: rationalizor is not poly', rationalizor)
        return False
    r = product.subs((x, sqrt(x)) for x in xs)
    r = r.expand().simplify()
    #return r.is_polynomial()
    if not r.is_polynomial():
        print('why False: product != f(x^2...)', r)
        return False
    return True
    for x in xs:
        r_ = r.replace(sqrt(x), y)
        if y in r_.free_symbols:
            print(r)
            print(r_)
            print(r_.free_symbols)
            raise
    return all(y not in r.replace(sqrt(x), y).free_symbols for x in xs)

    #r = r.as_poly(xs)
    return r.is_polynomial()
assert not is_sqrt_rational_product([a], a)
assert is_sqrt_rational_product([a], a**2)
assert not is_sqrt_rational_product([a], a**3)
assert is_sqrt_rational_product([a], a**4)
assert not is_sqrt_rational_product([a,b], a**2+b**2)
assert is_sqrt_rational_product([a,b], a**2-b**2)

def eval_sqrt_rational_product_at(n):
    return eval_sqrt_rational_product_at__ver2(n)
def eval_sqrt_rational_product_at__ver2(n):
    assert n > 0
    total_factors = 2**(n-1)
    x_str = 'x'
    xs = symbols(f'{x_str}:{n}')
    if n==1:
        return xs[0]**2
    n_1 = n-1
    fmt = f'{{:0>{n_1}b}}'
    terms = []
    for i in range(total_factors):
        str01 = fmt.format(i)
        assert len(str01) == n_1
        signs = [1]
        signs.extend((1 if bit=='1' else -1) for bit in str01)
        assert len(signs) == len(xs)
        term = sum(sign*x for x, sign in zip(xs, signs))
        terms.append(term)
    product = py_product(terms)
    return product
def eval_sqrt_rational_product_at__ver1(n):
    ###### version1
    denominator, rationalizor, product = eval_sqrt_rationalizor_at_ex3(n)
    return product
def eval_sqrt_rationalizor_at(n):
    denominator, rationalizor, product = eval_sqrt_rationalizor_at_ex3(n)
    return rationalizor
def eval_sqrt_rationalizor_at_ex3(n):
    assert n > 0
    e = 2; x_str = 'x'; k_str = 'k'
    xs = symbols(f'{x_str}:{n}')
    denominator = sum(xs).as_poly() # x0+x1+...
    for s in count(max(1, n-1)):
        #print(s)
        rationalizor, ks_less = make_complete_polynomial_from_symbols(xs, 1, s*e-1, k_str)
        product, ks_more = make_complete_polynomial_from_symbols(xs, e, s, k_str)
        MSB = product.coeff(xs[0]**(e*s))
        assert not MSB.is_zero
        product = product.subs({MSB:1})

        # set coeffs to make "rationalizor*denominator == product"
        poly = (product - rationalizor*denominator).as_poly(xs)
        cs = poly.coeffs()
        ks = (*ks_less, *ks_more,)
        if 0:
            solve_results = solve(cs, *ks, dict=True)
            assert type(solve_results) is list
        else:
            solve_results = linsolve(cs, *ks)
            #solve_results :: set<tuple>
            solve_results = [dict(zip(ks, r)) for r in solve_results]
        if solve_results:
            solve_result, = solve_results
            assert type(solve_result) is dict
            #print(s, solve_results)
            #print(f'rationalizor={rationalizor}')
            #print(f'product={product}')
            rationalizorT = rationalizor.subs(solve_result)
            productT = product.subs(solve_result)
            assert (productT - rationalizorT*denominator).is_zero
            break
    return denominator, rationalizorT, productT

from sympy import sympify
from itertools import combinations_with_replacement, count
from collections import Counter
from seed.iters.product import py_product
def make_complete_polynomial(n, e, s, x_str, k_str):
    # this 2 1 3 'x' 'k' = (k0_1_1_2*x0*x1**2 + k0_2_1_1*x0**2*x1 + k0_3*x0**3 + k1_3*x1**3, (x0, x1), {k0_3, k0_2_1_1, k0_1_1_2, k1_3})
    # this 3 1 3 'x' 'k' = k0_3*x0^3+k1_3*x1^3+k2_3*x2^3+ k0_1_1_1_2_1*x0*x1*x2 + k0_1_1_2*x0*x1^2 + ...
    # n - size of {x[i]}
    # e - basic exp of every x
    # s*e - sum of exp in every term
    assert n > 0
    assert e > 0
    assert s > 0
    xs = symbols(f'{x_str}:{n}')
    poly, ks = make_complete_polynomial_from_symbols(xs, e, s, k_str)
    return poly, xs, ks
def make_complete_polynomial_from_symbols(xs, e, s, k_str):
    #xs = tuple(x**e for x in xs)
    xs = tuple(xs)
    n = len(xs)
    assert n > 0
    assert e > 0
    assert s > 0

    terms = []
    ks = []
    it = combinations_with_replacement(range(n), s)
    for idc in it:
        d = Counter(idc)
        pairs = sorted(d.items())
        pairs = [(idx, exp*e) for idx, exp in pairs]
        pairs_str = '_'.join(f'{idx}_{exp}' for idx, exp in pairs)
        coeff = f'{k_str}{pairs_str}'
        coeff = symbols(coeff)
        ks.append(coeff)
        term = coeff * py_product(xs[idx]**exp for idx, exp in pairs)
        terms.append(term)
    poly = sum(terms)
    ks = frozenset(ks)
    return poly, ks

def _t1():
    r = make_complete_polynomial(2, 1, 3, 'x', 'k')
    print(r)
def _t2():
    for n in range(1, 6):
        #n = 1 2 3 4 5
        #s = 1 1 2 4 ... = max(1, 2^(n-2))
        product = eval_sqrt_rational_product_at(n)
        print(f'n={n}')
        print(f'product={product}')
        xs = tuple(product.free_symbols)
        assert is_sqrt_rational_product(xs, product)
#_t2()


def _t3():
    n_product_pairs = \
        [(3, 'x0**4 - 2*x0**2*x1**2 - 2*x0**2*x2**2 + x1**4 - 2*x1**2*x2**2 + x2**4')
        ,(4, 'x0**8 - 4*x0**6*x1**2 - 4*x0**6*x2**2 - 4*x0**6*x3**2 + 6*x0**4*x1**4 + 4*x0**4*x1**2*x2**2 + 4*x0**4*x1**2*x3**2 + 6*x0**4*x2**4 + 4*x0**4*x2**2*x3**2 + 6*x0**4*x3**4 - 4*x0**2*x1**6 + 4*x0**2*x1**4*x2**2 + 4*x0**2*x1**4*x3**2 + 4*x0**2*x1**2*x2**4 - 40*x0**2*x1**2*x2**2*x3**2 + 4*x0**2*x1**2*x3**4 - 4*x0**2*x2**6 + 4*x0**2*x2**4*x3**2 + 4*x0**2*x2**2*x3**4 - 4*x0**2*x3**6 + x1**8 - 4*x1**6*x2**2 - 4*x1**6*x3**2 + 6*x1**4*x2**4 + 4*x1**4*x2**2*x3**2 + 6*x1**4*x3**4 - 4*x1**2*x2**6 + 4*x1**2*x2**4*x3**2 + 4*x1**2*x2**2*x3**4 - 4*x1**2*x3**6 + x2**8 - 4*x2**6*x3**2 + 6*x2**4*x3**4 - 4*x2**2*x3**6 + x3**8')
        ]

    for n, product in n_product_pairs:
        product = sympify(product).as_poly()
        fs = product.factor()
        print(fs)
_t2()





