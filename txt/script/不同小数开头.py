#__all__:goto
r'''[[[
e script/不同小数开头.py
TODO:整系数一元二次方程，对应不同小数开头，极小化系数

[x/1 == (1-x)/x]:
    [x**2+x-1==0]
    [(x+1)*x==1]
    [x0+x1 == -1]
    [x0*x1 == -1]
    [x0 < 0 < x1]
    [x1==1/(1+x1) == cf[0;1,1,...]]
    [-2 < x0 < -1 < 0 < x1 < 1]
    [(x0+2)*(x1+2) == x0*x1 +2*(x0+x1) + 4 == -1 -2 +4 == 1]
    [x0==-2+1/(2+x1) == cf[-2;2,1,1,...]]

script.不同小数开头
py -m nn_ns.app.debug_cmd   script.不同小数开头 -x
py -m nn_ns.app.doctest_cmd script.不同小数开头:__doc__ -ht
from script.不同小数开头 import *


py_adhoc_call   script.不同小数开头   ,整系数一元二次方程讠实数根扌 =1 =1 =-1 --precision=60
Decimal('-1.61803398874989484820458683436563811772030917980576286213545')
Decimal('0.61803398874989484820458683436563811772030917980576286213545')

[[[
py_adhoc_call   script.不同小数开头   ,枚举冫整系数一元二次方程辻实数根扌 =5 =5 =5  --precision=6
===
((1, -1, -1), (Decimal('-0.618035'), Decimal('1.61804')))
((1, 1, -1), (Decimal('-1.61804'), Decimal('0.618035')))
((1, 0, -2), (Decimal('-1.41422'), Decimal('1.41422')))
((2, 0, -1), (Decimal('-0.707108'), Decimal('0.707108')))
((1, -2, -1), (Decimal('-0.414215'), Decimal('2.41422')))
((1, 2, -1), (Decimal('-2.41422'), Decimal('0.414215')))
((1, -2, -2), (Decimal('-0.73205'), Decimal('2.73205')))
((1, 2, -2), (Decimal('-2.73205'), Decimal('0.73205')))
((2, -2, -1), (Decimal('-0.366025'), Decimal('1.36602')))
((2, -1, -2), (Decimal('-0.780778'), Decimal('1.28078')))
((2, 1, -2), (Decimal('-1.28078'), Decimal('0.780778')))
((2, 2, -1), (Decimal('-1.36602'), Decimal('0.366025')))
((1, 0, -3), (Decimal('-1.73205'), Decimal('1.73205')))
((3, 0, -1), (Decimal('-0.57735'), Decimal('0.57735')))
((1, -3, -1), (Decimal('-0.302775'), Decimal('3.30278')))
((1, -3, 1), (Decimal('0.381965'), Decimal('2.61804')))
((1, -1, -3), (Decimal('-1.30278'), Decimal('2.30278')))
((1, 1, -3), (Decimal('-2.30278'), Decimal('1.30278')))
((1, 3, -1), (Decimal('-3.30278'), Decimal('0.302775')))
((1, 3, 1), (Decimal('-2.61804'), Decimal('-0.381965')))
((3, -1, -1), (Decimal('-0.434258'), Decimal('0.767592')))
((3, 1, -1), (Decimal('-0.767592'), Decimal('0.434258')))
((2, 0, -3), (Decimal('-1.22474'), Decimal('1.22474')))
((3, 0, -2), (Decimal('-0.816497'), Decimal('0.816497')))
((1, -3, -2), (Decimal('-0.561555'), Decimal('3.56156')))
((1, 3, -2), (Decimal('-3.56156'), Decimal('0.561555')))
((2, -3, -1), (Decimal('-0.280778'), Decimal('1.78078')))
((2, 3, -1), (Decimal('-1.78078'), Decimal('0.280778')))
((2, -2, -3), (Decimal('-0.822875'), Decimal('1.82288')))
((2, 2, -3), (Decimal('-1.82288'), Decimal('0.822875')))
((3, -2, -2), (Decimal('-0.548583'), Decimal('1.21525')))
((3, 2, -2), (Decimal('-1.21525'), Decimal('0.548583')))
((1, -4, -1), (Decimal('-0.23607'), Decimal('4.23607')))
((1, -4, 1), (Decimal('0.26795'), Decimal('3.73205')))
((1, -1, -4), (Decimal('-1.56156'), Decimal('2.56156')))
((1, 1, -4), (Decimal('-2.56156'), Decimal('1.56156')))
((1, 4, -1), (Decimal('-4.23607'), Decimal('0.23607')))
((1, 4, 1), (Decimal('-3.73205'), Decimal('-0.26795')))
((4, -1, -1), (Decimal('-0.390389'), Decimal('0.640389')))
((4, 1, -1), (Decimal('-0.640389'), Decimal('0.390389')))
((1, -3, -3), (Decimal('-0.79129'), Decimal('3.79129')))
((1, 3, -3), (Decimal('-3.79129'), Decimal('0.79129')))
((3, -3, -1), (Decimal('-0.263763'), Decimal('1.26376')))
((3, -1, -3), (Decimal('-0.847127'), Decimal('1.18046')))
((3, 1, -3), (Decimal('-1.18046'), Decimal('0.847127')))
((3, 3, -1), (Decimal('-1.26376'), Decimal('0.263763')))
((1, -4, -2), (Decimal('-0.44949'), Decimal('4.44949')))
((1, -4, 2), (Decimal('0.585785'), Decimal('3.41422')))
((1, -2, -4), (Decimal('-1.23607'), Decimal('3.23607')))
((1, 2, -4), (Decimal('-3.23607'), Decimal('1.23607')))
((1, 4, -2), (Decimal('-4.44949'), Decimal('0.44949')))
((1, 4, 2), (Decimal('-3.41422'), Decimal('-0.585785')))
((2, -4, -1), (Decimal('-0.224745'), Decimal('2.22474')))
((2, -4, 1), (Decimal('0.292892'), Decimal('1.70711')))
((2, -1, -4), (Decimal('-1.18614'), Decimal('1.68614')))
((2, 1, -4), (Decimal('-1.68614'), Decimal('1.18614')))
((2, 4, -1), (Decimal('-2.22474'), Decimal('0.224745')))
((2, 4, 1), (Decimal('-1.70711'), Decimal('-0.292892')))
((4, -2, -1), (Decimal('-0.309018'), Decimal('0.809018')))
((4, -1, -2), (Decimal('-0.59307'), Decimal('0.84307')))
((4, 1, -2), (Decimal('-0.84307'), Decimal('0.59307')))
((4, 2, -1), (Decimal('-0.809018'), Decimal('0.309018')))
((2, -3, -3), (Decimal('-0.68614'), Decimal('2.18614')))
((2, 3, -3), (Decimal('-2.18614'), Decimal('0.68614')))
((3, -3, -2), (Decimal('-0.457427'), Decimal('1.45743')))
((3, -2, -3), (Decimal('-0.72076'), Decimal('1.38743')))
((3, 2, -3), (Decimal('-1.38743'), Decimal('0.72076')))
((3, 3, -2), (Decimal('-1.45743'), Decimal('0.457427')))
((3, 0, -4), (Decimal('-1.15470'), Decimal('1.15470')))
((4, 0, -3), (Decimal('-0.866025'), Decimal('0.866025')))
((1, -4, -3), (Decimal('-0.64575'), Decimal('4.64575')))
((1, 0, -5), (Decimal('-2.23607'), Decimal('2.23607')))
((1, 4, -3), (Decimal('-4.64575'), Decimal('0.64575')))
((3, -4, -1), (Decimal('-0.21525'), Decimal('1.54858')))
((3, 4, -1), (Decimal('-1.54858'), Decimal('0.21525')))
((5, 0, -1), (Decimal('-0.447214'), Decimal('0.447214')))
((1, -5, -1), (Decimal('-0.19258'), Decimal('5.1926')))
((1, -5, 1), (Decimal('0.20871'), Decimal('4.79129')))
((1, -1, -5), (Decimal('-1.79129'), Decimal('2.79129')))
((1, 1, -5), (Decimal('-2.79129'), Decimal('1.79129')))
((1, 5, -1), (Decimal('-5.1926'), Decimal('0.19258')))
((1, 5, 1), (Decimal('-4.79129'), Decimal('-0.20871')))
((5, -1, -1), (Decimal('-0.358258'), Decimal('0.558258')))
((5, 1, -1), (Decimal('-0.558258'), Decimal('0.358258')))
((2, -4, -3), (Decimal('-0.58114'), Decimal('2.58115')))
((2, -3, -4), (Decimal('-0.85078'), Decimal('2.35078')))
((2, 0, -5), (Decimal('-1.58114'), Decimal('1.58114')))
((2, 3, -4), (Decimal('-2.35078'), Decimal('0.85078')))
((2, 4, -3), (Decimal('-2.58115'), Decimal('0.58114')))
((3, -4, -2), (Decimal('-0.387427'), Decimal('1.72077')))
((3, -2, -4), (Decimal('-0.868517'), Decimal('1.53518')))
((3, 2, -4), (Decimal('-1.53518'), Decimal('0.868517')))
((3, 4, -2), (Decimal('-1.72077'), Decimal('0.387427')))
((4, -3, -2), (Decimal('-0.42539'), Decimal('1.17539')))
((4, -2, -3), (Decimal('-0.651388'), Decimal('1.15139')))
((4, 2, -3), (Decimal('-1.15139'), Decimal('0.651388')))
((4, 3, -2), (Decimal('-1.17539'), Decimal('0.42539')))
((5, 0, -2), (Decimal('-0.632456'), Decimal('0.632456')))
((1, -5, -2), (Decimal('-0.37228'), Decimal('5.3723')))
((1, -5, 2), (Decimal('0.438445'), Decimal('4.56156')))
((1, -2, -5), (Decimal('-1.44949'), Decimal('3.44949')))
((1, 2, -5), (Decimal('-3.44949'), Decimal('1.44949')))
((1, 5, -2), (Decimal('-5.3723'), Decimal('0.37228')))
((1, 5, 2), (Decimal('-4.56156'), Decimal('-0.438445')))
((2, -5, -1), (Decimal('-0.18614'), Decimal('2.68615')))
((2, -5, 1), (Decimal('0.219222'), Decimal('2.28078')))
((2, -1, -5), (Decimal('-1.35078'), Decimal('1.85078')))
((2, 1, -5), (Decimal('-1.85078'), Decimal('1.35078')))
((2, 5, -1), (Decimal('-2.68615'), Decimal('0.18614')))
((2, 5, 1), (Decimal('-2.28078'), Decimal('-0.219222')))
((5, -2, -1), (Decimal('-0.289898'), Decimal('0.689898')))
((5, -1, -2), (Decimal('-0.540312'), Decimal('0.740312')))
((5, 1, -2), (Decimal('-0.740312'), Decimal('0.540312')))
((5, 2, -1), (Decimal('-0.689898'), Decimal('0.289898')))
((1, -4, -4), (Decimal('-0.828425'), Decimal('4.82842')))
((1, 4, -4), (Decimal('-4.82842'), Decimal('0.828425')))
((2, -5, -2), (Decimal('-0.35078'), Decimal('2.85078')))
((2, -2, -5), (Decimal('-1.15831'), Decimal('2.15831')))
((2, 2, -5), (Decimal('-2.15831'), Decimal('1.15831')))
((2, 5, -2), (Decimal('-2.85078'), Decimal('0.35078')))
((4, -4, -1), (Decimal('-0.207106'), Decimal('1.20711')))
((4, -1, -4), (Decimal('-0.882782'), Decimal('1.13278')))
((4, 1, -4), (Decimal('-1.13278'), Decimal('0.882782')))
((4, 4, -1), (Decimal('-1.20711'), Decimal('0.207106')))
((5, -2, -2), (Decimal('-0.463325'), Decimal('0.863325')))
((5, 2, -2), (Decimal('-0.863325'), Decimal('0.463325')))
((3, -4, -3), (Decimal('-0.535183'), Decimal('1.86852')))
((3, -3, -4), (Decimal('-0.758305'), Decimal('1.7583')))
((3, 0, -5), (Decimal('-1.29100'), Decimal('1.29100')))
((3, 3, -4), (Decimal('-1.7583'), Decimal('0.758305')))
((3, 4, -3), (Decimal('-1.86852'), Decimal('0.535183')))
((4, -3, -3), (Decimal('-0.568729'), Decimal('1.31872')))
((4, 3, -3), (Decimal('-1.31872'), Decimal('0.568729')))
((5, 0, -3), (Decimal('-0.774597'), Decimal('0.774597')))
((1, -5, -3), (Decimal('-0.54138'), Decimal('5.5414')))
((1, -5, 3), (Decimal('0.697225'), Decimal('4.30278')))
((1, -3, -5), (Decimal('-1.19258'), Decimal('4.19258')))
((1, 3, -5), (Decimal('-4.19258'), Decimal('1.19258')))
((1, 5, -3), (Decimal('-5.5414'), Decimal('0.54138')))
((1, 5, 3), (Decimal('-4.30278'), Decimal('-0.697225')))
((3, -5, -1), (Decimal('-0.18046'), Decimal('1.84713')))
((3, -5, 1), (Decimal('0.232408'), Decimal('1.43426')))
((3, -1, -5), (Decimal('-1.13504'), Decimal('1.46838')))
((3, 1, -5), (Decimal('-1.46838'), Decimal('1.13504')))
((3, 5, -1), (Decimal('-1.84713'), Decimal('0.18046')))
((3, 5, 1), (Decimal('-1.43426'), Decimal('-0.232408')))
((5, -3, -1), (Decimal('-0.238516'), Decimal('0.838516')))
((5, -1, -3), (Decimal('-0.681025'), Decimal('0.881025')))
((5, 1, -3), (Decimal('-0.881025'), Decimal('0.681025')))
((5, 3, -1), (Decimal('-0.838516'), Decimal('0.238516')))
((4, -3, -4), (Decimal('-0.69300'), Decimal('1.4430')))
((4, 0, -5), (Decimal('-1.11803'), Decimal('1.11803')))
((4, 3, -4), (Decimal('-1.4430'), Decimal('0.69300')))
((5, 0, -4), (Decimal('-0.894427'), Decimal('0.894427')))
((1, -5, -4), (Decimal('-0.70156'), Decimal('5.70155')))
((1, 5, -4), (Decimal('-5.70155'), Decimal('0.70156')))
((4, -5, -1), (Decimal('-0.17539'), Decimal('1.42539')))
((4, 5, -1), (Decimal('-1.42539'), Decimal('0.17539')))
((3, -5, -3), (Decimal('-0.468375'), Decimal('2.13503')))
((3, -3, -5), (Decimal('-0.884437'), Decimal('1.88443')))
((3, 3, -5), (Decimal('-1.88443'), Decimal('0.884437')))
((3, 5, -3), (Decimal('-2.13503'), Decimal('0.468375')))
((5, -3, -3), (Decimal('-0.530662'), Decimal('1.13066')))
((5, 3, -3), (Decimal('-1.13066'), Decimal('0.530662')))
((2, -5, -4), (Decimal('-0.637458'), Decimal('3.13745')))
((2, -4, -5), (Decimal('-0.870828'), Decimal('2.87082')))
((2, 4, -5), (Decimal('-2.87082'), Decimal('0.870828')))
((2, 5, -4), (Decimal('-3.13745'), Decimal('0.637458')))
((4, -5, -2), (Decimal('-0.318729'), Decimal('1.56872')))
((4, -2, -5), (Decimal('-0.895644'), Decimal('1.39565')))
((4, 2, -5), (Decimal('-1.39565'), Decimal('0.895644')))
((4, 5, -2), (Decimal('-1.56872'), Decimal('0.318729')))
((5, -4, -2), (Decimal('-0.348331'), Decimal('1.14833')))
((5, -2, -4), (Decimal('-0.716515'), Decimal('1.11652')))
((5, 2, -4), (Decimal('-1.11652'), Decimal('0.716515')))
((5, 4, -2), (Decimal('-1.14833'), Decimal('0.348331')))
((3, -5, -4), (Decimal('-0.590667'), Decimal('2.25733')))
((3, -4, -5), (Decimal('-0.78630'), Decimal('2.11963')))
((3, 4, -5), (Decimal('-2.11963'), Decimal('0.78630')))
((3, 5, -4), (Decimal('-2.25733'), Decimal('0.590667')))
((4, -5, -3), (Decimal('-0.44300'), Decimal('1.6930')))
((4, -3, -5), (Decimal('-0.804248'), Decimal('1.55425')))
((4, 3, -5), (Decimal('-1.55425'), Decimal('0.804248')))
((4, 5, -3), (Decimal('-1.6930'), Decimal('0.44300')))
((5, -4, -3), (Decimal('-0.47178'), Decimal('1.27178')))
((5, -3, -4), (Decimal('-0.643398'), Decimal('1.2434')))
((5, 3, -4), (Decimal('-1.2434'), Decimal('0.643398')))
((5, 4, -3), (Decimal('-1.27178'), Decimal('0.47178')))
((1, -5, -5), (Decimal('-0.85410'), Decimal('5.8541')))
((1, -5, 5), (Decimal('1.38196'), Decimal('3.61804')))
((1, 5, -5), (Decimal('-5.8541'), Decimal('0.85410')))
((1, 5, 5), (Decimal('-3.61804'), Decimal('-1.38196')))
((5, -5, -1), (Decimal('-0.17082'), Decimal('1.17082')))
((5, -5, 1), (Decimal('0.276393'), Decimal('0.723607')))
((5, -1, -5), (Decimal('-0.90499'), Decimal('1.10499')))
((5, 1, -5), (Decimal('-1.10499'), Decimal('0.90499')))
((5, 5, -1), (Decimal('-1.17082'), Decimal('0.17082')))
((5, 5, 1), (Decimal('-0.723607'), Decimal('-0.276393')))
((2, -5, -5), (Decimal('-0.765565'), Decimal('3.26558')))
((2, 5, -5), (Decimal('-3.26558'), Decimal('0.765565')))
((5, -5, -2), (Decimal('-0.306226'), Decimal('1.30623')))
((5, -2, -5), (Decimal('-0.8198'), Decimal('1.2198')))
((5, 2, -5), (Decimal('-1.2198'), Decimal('0.8198')))
((5, 5, -2), (Decimal('-1.30623'), Decimal('0.306226')))
((4, -5, -4), (Decimal('-0.554248'), Decimal('1.80425')))
((4, -4, -5), (Decimal('-0.724745'), Decimal('1.72475')))
((4, 4, -5), (Decimal('-1.72475'), Decimal('0.724745')))
((4, 5, -4), (Decimal('-1.80425'), Decimal('0.554248')))
((5, -4, -4), (Decimal('-0.579796'), Decimal('1.3798')))
((5, 4, -4), (Decimal('-1.3798'), Decimal('0.579796')))
((3, -5, -5), (Decimal('-0.703257'), Decimal('2.36992')))
((3, 5, -5), (Decimal('-2.36992'), Decimal('0.703257')))
((5, -5, -3), (Decimal('-0.421954'), Decimal('1.42195')))
((5, -3, -5), (Decimal('-0.74403'), Decimal('1.34403')))
((5, 3, -5), (Decimal('-1.34403'), Decimal('0.74403')))
((5, 5, -3), (Decimal('-1.42195'), Decimal('0.421954')))
((4, -5, -5), (Decimal('-0.655875'), Decimal('1.90588')))
((4, 5, -5), (Decimal('-1.90588'), Decimal('0.655875')))
((5, -5, -4), (Decimal('-0.5247'), Decimal('1.5247')))
((5, -4, -5), (Decimal('-0.67703'), Decimal('1.47703')))
((5, 4, -5), (Decimal('-1.47703'), Decimal('0.67703')))
((5, 5, -4), (Decimal('-1.5247'), Decimal('0.5247')))
===
]]]


#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from seed.tiny_.check import check_type_is, check_int_ge
from seed.math.gcd import gcd

import math
from decimal import Decimal
from decimal import DefaultContext, Context, localcontext
#[DefaultContext===Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])]



class 错误(Exception):pass
class 错误牜非一元二次方程牜首项系数为零(错误):pass
class 错误牜一元二次方程无实根(错误):pass
def mk_may_context(*, precision=None, context=None):
    #may_context = ...
    if context is not None is not precision: raise 000
    elif context is None is not precision:
        context = Context(prec=precision)
        may_context = context
    elif context is not None is precision:
        context
        may_context = context
    elif context is None is precision:
        may_context = None
    else:
        raise 000
    may_context
    return may_context

def 整系数一元二次方程讠实数根扌(a, b, c, /, *, precision=None, context=None, to_detect_rational=False):
    '[a*x**2+b*x+c==0][a,b,c :: int][a=!=0][b**2 - 4*a*c >= 0]'
    coeffs = (c, b, a)
    for k in coeffs:
        check_type_is(int, k)
    if coeffs[-1] == 0:raise 错误牜非一元二次方程牜首项系数为零
    if (D := b**2 - 4*a*c) < 0: raise 错误牜一元二次方程无实根
    #(-b+/-sqrt(D))/(2*a)

    may_context = mk_may_context(precision=precision, context=context)

    with localcontext(may_context):
        sqrt_D = Decimal(D).sqrt()
        A = Decimal(a)
        B = Decimal(b)
        C = Decimal(c)
        x0 = (-B-sqrt_D)/(2*A)
        x1 = (-B+sqrt_D)/(2*A)
        if to_detect_rational:
            isqrt_D = math.floor(sqrt_D)
            are_roots_rational = isqrt_D**2 == D
    if to_detect_rational:
        return (are_roots_rational, x0, x1)
    return (x0, x1)



def iter_ABCs(max4a, max4b, max4c, /):
    for a in range(1, 1+max4a):
        for b in range(-max4b, 1+max4b):
            for c in range(-max4c, 1+max4b):
                yield (a,b,c)
def sum_abs_(ns, /):
    return sum(map(abs, ns))
def sum_square_(ns, /):
    return sum(n**2 for n in ns)
def iter_sorted_ABCs(max4a, max4b, max4c, /, *, key=None):
    if key is None:
        key = sum_square_
    it = iter_ABCs(max4a, max4b, max4c)
    return sorted(it, key=key)
def 枚举冫整系数一元二次方程辻实数根扌(max4a, max4b, max4c, /, *, precision=None, context=None, to_show=False):
    may_context = mk_may_context(precision=precision, context=context)
    for a,b,c in iter_sorted_ABCs(max4a, max4b, max4c):
        may_xs = _impl1(a, b, c, may_context, to_show=to_show)
        if not may_xs is None:
            (x0,x1) = xs = may_xs
            yield ((a,b,c), (x0,x1))

def _impl1(a, b, c, may_context, /, *, to_show, _f=整系数一元二次方程讠实数根扌):
    '-> may (x0,x1)'
    if not gcd(a, b, c) == 1:
        #skip
        return
    try:
        are_roots_rational, x0, x1 = _f(a, b, c, context=may_context, to_detect_rational=True)
    except 错误牜一元二次方程无实根:
        #skip
        return
    if are_roots_rational:
        #skip
        return
    if to_show:
        print((a,b,c))
        print(x0)
        print(x1)
    return (x0, x1)

def _split_cf5quadratic_surd__ABC(a, b, c, /, *, sub_vs_add):
    D = b**2 -4*a*c
    B = -b
    C = 2*a
    if sub_vs_add is False:
        #sub
        PNQ = -B, D, -C
    elif sub_vs_add is True:
        #add
        PNQ = B, D, C
    else:
        raise 000
    return _split_cf5quadratic_surd__PNQ(*PNQ)

def _split_cf5quadratic_surd__PNQ(P, N, Q):
    # (P+sqrt(N))/Q
    kwds = dict(locals())
    ######################
    (non_periodic_digits, periodic_digits) = list_split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ(**kwds)
    ######################
    return (non_periodic_digits, periodic_digits)


def _iter_cf_digits_(non_periodic_digits, periodic_digits, /):
    yield from non_periodic_digits
    if len(periodic_digits) == 0:
        return
    while 1:
        yield from periodic_digits
    raise 000
def _mk_cf_(non_periodic_digits, periodic_digits, /):
    cf_digits = _iter_cf_digits_(non_periodic_digits, periodic_digits)
    cf = ContinuedFraction(cf_digits)
    return cf
    cf.iter_approximate_fractions_

if 1:
    #for:_split_cf5quadratic_surd__PNQ
    from nn_ns.math_nn.continued_fraction.continued_fraction_digits_of_quadratic_surd import list_split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ# split_periodic_continued_fraction_digits_of_quadratic_surd__PNQ
    #view ../../python3_src/nn_ns/math_nn/continued_fraction/continued_fraction_digits_of_quadratic_surd.py
    ######################

if 1:
    #for:_mk_cf_
    from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import ContinuedFraction
    #view ../../python3_src/seed/math/continued_fraction/continued_fraction_ops____using_LazyList.py
    ######################



__all__
from script.不同小数开头 import *
