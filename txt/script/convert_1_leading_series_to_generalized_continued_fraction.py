#__all__:goto
r'''[[[
e ./script/convert_1_leading_series_to_generalized_continued_fraction.py
view others/数学/continued-fraction/generalized_continued_fraction.txt
    # [:分式转化为连分式]:goto


script.convert_1_leading_series_to_generalized_continued_fraction
py -m nn_ns.app.debug_cmd   script.convert_1_leading_series_to_generalized_continued_fraction -x
py -m nn_ns.app.doctest_cmd script.convert_1_leading_series_to_generalized_continued_fraction:__doc__ -ff -v
from script.convert_1_leading_series_to_generalized_continued_fraction import *



[arctan(x) == sum (-1)**k /(2*k+1) *x**(2*k+1) {k :<- [0..]}]
[e**z == 1 + z + z**2/factorial(2) +... +z**k/factorial(k) +...]
    [e**z == gcf[1; z$1, -z$2, z$3, -z$2, z$5, -z$2, z$7, ..., ((-1)**(k+1)*z)$(k if k%2 else 2), ...]]

[arcsin(x) == x + 1/2*x**3/3 + 1/2*3/4*x**5/5 + 1/2*3/4*5/6*x**7/7 +...]
[arcsin(x) == sum choose(2*k;k)/2**(2*k) *x**(2*k+1)/(2*k+1) {k :<- [0..]}]


py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4arcsin_to_generalized_continued_fraction_ =6 +factor_as_p2e


py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4arcsin_to_generalized_continued_fraction_ =10
Fraction(0, 1)
(Fraction(1, 1), 1)
(Fraction(-1, 6), 2)
(Fraction(-17, 60), 2)
(Fraction(-549, 2380), 2)
(Fraction(-69049, 261324), 2)
(Fraction(-399121325, 1667947644), 2)
(Fraction(-9600903541557, 37091075359052), 2)
(Fraction(-3109112782183806769, 12810036504055156860), 2)
(Fraction(-4201832398286608520252509, 16391659978047051834461340), 2)

$ py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4arcsin_to_generalized_continued_fraction_ =10 +factor_as_p2e
Fraction(0, 1)
(((), ()), 1)
((((-1, 1),), ((2, 1), (3, 1))), 2)
((((-1, 1), (17, 1)), ((2, 2), (3, 1), (5, 1))), 2)
((((-1, 1), (3, 2), (61, 1)), ((2, 2), (5, 1), (7, 1), (17, 1))), 2)
((((-1, 1), (29, 1), (2381, 1)), ((2, 2), (3, 2), (7, 1), (17, 1), (61, 1))), 2)
((((-1, 1), (5, 2), (17, 1), (939109, 1)), ((2, 2), (3, 2), (11, 1), (29, 1), (61, 1), (2381, 1))), 2)
((((-1, 1), (3, 2), (61, 1), (8447, 1), (2070319, 1)), ((2, 2), (11, 1), (13, 1), (29, 1), (2381, 1), (939109, 1))), 2)
((((-1, 1), (7, 2), (29, 1), (59, 1), (419, 1), (2381, 1), (37172089, 1)), ((2, 2), (3, 1), (5, 1), (13, 1), (8447, 1), (939109, 1), (2070319, 1))), 2)
^C
KeyboardInterrupt
==>>:
    ++kw:list_p2e
    ++_factor_() resue prev factors

py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4arcsin_to_generalized_continued_fraction_ =10 +factor_as_p2e +list_p2e
Fraction(0, 1)
(([], []), 1)
(([-1], [2, 3]), 2)
(([-1, 17], [2, 2, 3, 5]), 2)
(([-1, 3, 3, 61], [2, 2, 5, 7, 17]), 2)
(([-1, 29, 2381], [2, 2, 3, 3, 7, 17, 61]), 2)
(([-1, 5, 5, 17, 939109], [2, 2, 3, 3, 11, 29, 61, 2381]), 2)
(([-1, 3, 3, 61, 8447, 2070319], [2, 2, 11, 13, 29, 2381, 939109]), 2)
(([-1, 7, 7, 29, 59, 419, 2381, 37172089], [2, 2, 3, 5, 13, 8447, 939109, 2070319]), 2)
(([-1, 19, 19, 370871, 939109, 33418938071], [2, 2, 3, 5, 17, 59, 419, 8447, 2070319, 37172089]), 2)



py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :arcsin  =10
py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :arctan  =10
Fraction(0, 1)
(Fraction(1, 1), 1)
(Fraction(1, 3), 2)
(Fraction(4, 15), 2)
(Fraction(9, 35), 2)
(Fraction(16, 63), 2)
(Fraction(25, 99), 2)
(Fraction(36, 143), 2)
(Fraction(49, 195), 2)
(Fraction(64, 255), 2)



py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  =20
Fraction(0, 1)
(Fraction(1, 1), 0)
(Fraction(-1, 1), 1)
(Fraction(1, 2), 1)
(Fraction(-1, 6), 1)
(Fraction(1, 6), 1)
(Fraction(-1, 10), 1)
(Fraction(1, 10), 1)
(Fraction(-1, 14), 1)
(Fraction(1, 14), 1)
(Fraction(-1, 18), 1)
(Fraction(1, 18), 1)
(Fraction(-1, 22), 1)
(Fraction(1, 22), 1)
(Fraction(-1, 26), 1)
(Fraction(1, 26), 1)
(Fraction(-1, 30), 1)
(Fraction(1, 30), 1)
(Fraction(-1, 34), 1)
(Fraction(1, 34), 1)
==>>:
    [e**z == gcf[0; 1$1, (-z)$1, (z/2)$1, (-z/6)$1, (z/6)$1, (-z/10)$1, (z/10)$1, (-z/14)$1, (z/14)$1, ...]
    [e**z == gcf[0; 1$1, (-z)$1, (z/2)$1, (-z/2)$3, (z/2)$1, (-z/2)$5, (z/2)$1, (-z/2)$7, (z/2)$1, ...]
    [e**z == gcf[0; 1$1, (-z)$1, z$2, (-z)$3, z$2, (-z)$5, z$2, (-z)$7, z$2, ...]

    vs: [e**z == gcf[1; z$1, -z$2, z$3, -z$2, z$5, -z$2, z$7, ..., ((-1)**(k+1)*z)$(k if k%2 else 2), ...]]

py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  =20 --args4iter_power_series4xxx_=[-1]
Fraction(0, 1)
(Fraction(1, 1), 1)
(Fraction(-1, 2), 1)
(Fraction(1, 6), 1)
(Fraction(-1, 6), 1)
...

py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  =20 --args4iter_power_series4xxx_=[1]
Fraction(0, 1)
(Fraction(2, 1), 0)
(Fraction(-1, 2), 1)
(Fraction(1, 12), 2)
(Fraction(1, 60), 2)
(Fraction(1, 140), 2)
(Fraction(1, 252), 2)
(Fraction(1, 396), 2)
(Fraction(1, 572), 2)
(Fraction(1, 780), 2)
(Fraction(1, 1020), 2)
(Fraction(1, 1292), 2)
(Fraction(1, 1596), 2)
(Fraction(1, 1932), 2)
(Fraction(1, 2300), 2)
(Fraction(1, 2700), 2)
(Fraction(1, 3132), 2)
(Fraction(1, 3596), 2)
(Fraction(1, 4092), 2)
(Fraction(1, 4620), 2)

py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  =20 --args4iter_power_series4xxx_=[-2]
xxx Fraction(0, 1)
xxx (Fraction(-1, 1), 0)
xxx (Fraction(1, 1), 1)
xxx (Fraction(-3, 2), 1)
xxx (Fraction(1, 18), 1)
xxx (Fraction(-1, 18), 1)
xxx (Fraction(3, 10), 1)
xxx (Fraction(-2, 63), 2)
xxx (Fraction(2, 63), 2)
xxx ^C
xxx KeyboardInterrupt
    怎么回事？
==>>:
    ++kw:sz4cut_power_series
    发现重大bug: _diff_(): e4N <?> e4D 方向错误！！
        这里的数据是错的
        但是 arcsin/arctan/(e**z+(0|-1|+1|-1/2|+1/2)) 能正常运行，并且数据不出错 真是狗屎运


py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  --args4iter_power_series4xxx_=[-2]  =10 --sz4cut_power_series=20
Fraction(0, 1)
(Fraction(-1, 1), 0)
(Fraction(1, 1), 1)
(Fraction(-3, 2), 1)
(Fraction(1, 18), 1)
(Fraction(-1, 18), 1)
(Fraction(3, 10), 1)
(Fraction(-3, 10), 1)
(Fraction(1, 42), 1)
(Fraction(-1, 42), 1)

py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  --args4iter_power_series4xxx_=[-2]  =100 --sz4cut_power_series=20
Fraction(0, 1)
(Fraction(-1, 1), 0)
(Fraction(1, 1), 1)
(Fraction(-3, 2), 1)
(Fraction(1, 18), 1)
(Fraction(-1, 18), 1)
(Fraction(3, 10), 1)
(Fraction(-3, 10), 1)
(Fraction(1, 42), 1)
(Fraction(-1, 42), 1)
(Fraction(1, 6), 1)
(Fraction(-1, 6), 1)
(Fraction(1, 66), 1)
(Fraction(-1, 66), 1)
(Fraction(3, 26), 1)
(Fraction(-3, 26), 1)
(Fraction(1, 90), 1)
(Fraction(-1, 90), 1)
(Fraction(3, 34), 1)
(Fraction(-3, 34), 1)
(Fraction(1, 114), 1)
xxx (Fraction(-277135, 114), 1)
xxx (Fraction(9435673677, 3879890), 1)
xxx (Fraction(104749994202767, 12203125314218510), 1)
xxx ... ...
    只有20项部分分子是正确的(见下面)




[[[
py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  =25 --args4iter_power_series4xxx_=[-2]
Fraction(0, 1)
(Fraction(-1, 1), 0)
(Fraction(1, 1), 1)
(Fraction(-3, 2), 1)
(Fraction(1, 18), 1)
(Fraction(-1, 18), 1)
(Fraction(3, 10), 1)
(Fraction(-3, 10), 1)
(Fraction(1, 42), 1)
(Fraction(-1, 42), 1)
(Fraction(1, 6), 1)
(Fraction(-1, 6), 1)
(Fraction(1, 66), 1)
(Fraction(-1, 66), 1)
(Fraction(3, 26), 1)
(Fraction(-3, 26), 1)
(Fraction(1, 90), 1)
(Fraction(-1, 90), 1)
(Fraction(3, 34), 1)
(Fraction(-3, 34), 1)
(Fraction(1, 114), 1)
(Fraction(-1, 114), 1)
(Fraction(1, 14), 1)
(Fraction(-1, 14), 1)
(Fraction(1, 138), 1)
看起来 很接近e的简单连分数，有必要折叠起来好好瞧瞧
]]]






py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  =20 --args4iter_power_series4xxx_=['1/2']
Fraction(0, 1)
(Fraction(3, 2), 0)
(Fraction(-2, 3), 1)
(Fraction(1, 6), 1)
(Fraction(-1, 2), 1)
(Fraction(1, 2), 1)
(Fraction(-1, 30), 1)
(Fraction(1, 30), 1)
(Fraction(-3, 14), 1)
(Fraction(3, 14), 1)
(Fraction(-1, 54), 1)
(Fraction(1, 54), 1)
(Fraction(-3, 22), 1)
(Fraction(3, 22), 1)
(Fraction(-1, 78), 1)
(Fraction(1, 78), 1)
(Fraction(-1, 10), 1)
(Fraction(1, 10), 1)
(Fraction(-1, 102), 1)
(Fraction(1, 102), 1)

py_adhoc_call   script.convert_1_leading_series_to_generalized_continued_fraction   ,convert_power_series4xxx_to_generalized_continued_fraction_  :natural_exponential_function  =20 --args4iter_power_series4xxx_=['-1/2']
Fraction(0, 1)
(Fraction(1, 2), 0)
(Fraction(-2, 1), 1)
(Fraction(3, 2), 1)
(Fraction(-1, 18), 1)
(Fraction(1, 18), 1)
(Fraction(-3, 10), 1)
(Fraction(3, 10), 1)
(Fraction(-1, 42), 1)
(Fraction(1, 42), 1)
(Fraction(-1, 6), 1)
(Fraction(1, 6), 1)
(Fraction(-1, 66), 1)
(Fraction(1, 66), 1)
(Fraction(-3, 26), 1)
(Fraction(3, 26), 1)
(Fraction(-1, 90), 1)
(Fraction(1, 90), 1)
(Fraction(-3, 34), 1)
(Fraction(3, 34), 1)


#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_
from seed.types.LazyList import ToConcatLazyList, decorator4protocol4ToConcatLazyList_
from seed.types.LazyList import LazyList, LazyListError
from fractions import Fraction
from operator import __index__
from itertools import count as count_
from itertools import islice



class BaseError(Exception):pass
class Error__exp4power_series__diff_self_not_eq_zero(BaseError):pass
class Error__one_leading_series__not_startswith_one(BaseError):pass
class Error__coeff4power_series__div_self_not_eq_one(BaseError):pass
class Error__one_leading_series__empty(BaseError):pass
class Error__exp4power_series__lt_zero(BaseError):pass
class Error__exp4power_series__not_strict_increasing(BaseError):pass
class Error__coeff4power_series__eq_zero(BaseError):pass





def convert_power_series4xxx_to_generalized_continued_fraction_(nm, sz, /, *, factor_as_p2e=False, list_p2e=False, args4iter_power_series4xxx_=(), sz4cut_power_series=None):
    iter_power_series4xxx_ = globals()[f'iter_power_series4{nm}_']
    power_series = iter_power_series4xxx_(*args4iter_power_series4xxx_)
    if not sz4cut_power_series is None:
        power_series = islice(power_series, sz4cut_power_series)
    it = convert_power_series_to_generalized_continued_fraction__coeff_is_Fraction_(power_series, factor_as_p2e=factor_as_p2e, list_p2e=list_p2e)
    it = islice(it, sz)
    return it
def convert_power_series4arcsin_to_generalized_continued_fraction_(sz, /, *, factor_as_p2e=False, list_p2e=False):
    power_series = iter_power_series4arcsin_()
    it = convert_power_series_to_generalized_continued_fraction__coeff_is_Fraction_(power_series, factor_as_p2e=factor_as_p2e, list_p2e=list_p2e)
    it = islice(it, sz)
    return it
def iter_power_series4arcsin_():
    '[arcsin(x) == x + 1/2*x**3/3 + 1/2*3/4*x**5/5 + 1/2*3/4*5/6*x**7/7 +...]'
    acc = Fraction(1)
    for k in count_(1, 2):
        yield (acc/k, k)
        acc = (acc*k) /(k+1)
def iter_power_series4arctan_():
    '[arctan(x) == sum (-1)**k /(2*k+1) *x**(2*k+1) {k :<- [0..]}]'
    _1 = Fraction(1)
    for k in count_(0):
        kk = 2*k+1
        yield (_1*(-1)**k /kk, kk)
def iter_power_series4natural_exponential_function_(offset=0, /):
    '[e**z == 1 + z + z**2/factorial(2) +... +z**k/factorial(k) +...]'
    offset = Fraction(offset) # 5str
    acc = Fraction(1)
    if 1:
        k = 0
        if acc+offset:
            yield (acc+offset, k)
    for k in count_(1):
        acc /= k
        yield (acc, k)

def _factor_(ps, n, /):
    p2e_, u = semi_factor_pint_via_trial_division(ps, n)
    _p2e = factor_pint_by_trial_division_(u)
    p2e = {**p2e_, **_p2e}
    assert len(p2e_) + len(_p2e) == len(p2e)
    ps.update(_p2e)
    return p2e

def convert_power_series_to_generalized_continued_fraction__coeff_is_Fraction_(power_series, /, *, factor_as_p2e=False, list_p2e=False):
    power_series = iter(power_series)
    def _main_(power_series, /):
        power_series = _std_(power_series)
        one = Fraction(1)
        zero = Fraction(0)
        it = convert_power_series_to_generalized_continued_fraction_(zero, one, power_series)
        if factor_as_p2e:
            it = f(it)
        return it
    def f(it, /):
        # impl:kw:factor_as_p2e
        it = iter(it)
        #bug:for d0 in it: yield d0
        for d0 in it:
            break
        else:
            raise 000
        yield d0
        ps = {2}
        for nk,e in it:
            N,D = nk.as_integer_ratio()
            absN = abs(N)
            p2e4N = _factor_(ps, absN)
            p2e4D = _factor_(ps, D)
            if N < 0:
                p2e4N[-1] = 1
            ps8N = _f__ls(p2e4N)
            ps8D = _f__ls(p2e4D)
            yield ((ps8N, ps8D), e)
    def _f__ls(p2e, /):
        ps = (*sorted(p2e.items()),)
        if list_p2e:
            ps = [p for p, e in ps for _ in range(e)]
        return ps
    def _std_(power_series, /):
        power_series = iter(power_series)
        for c, e in power_series:
            yield Fraction(c), __index__(e)
    return _main_(power_series)
#def convert_1_leading_series_to_generalized_continued_fraction_():
def convert_power_series_to_generalized_continued_fraction_(zero, one, power_series, /):
    r'''[[[
    'power_series/(Iter (coeff4PS/real{=!=0}, exp4PS/uint){exp[k] < exp[k+1]}) -> gcf/([d0/real] ++ Iter (coeff4N/real{=!=0}, exp4N/pint{except first may be 0})) # gcf[d0; n1$d1, ...]; [n0 == ...]; [d1 == d2 == ... == 1]'

    [power_series<z> == sum coeff4PS[i]*z**exp4PS[i] {i :<- [0..]}]

    [gcf == gcf[d0; (coeff4N[1]*z**exp4N[1])$1, (coeff4N[2]*z**exp4N[2])$1, ..., (coeff4N[k]*z**exp4N[k])$1, ...]]
        [d0 == 0]
        [d1 == d2 == ... == 1]

    #]]]'''#'''
    power_series = iter(power_series)
    def _main_(power_series, /):
        power_series = _std_(power_series)
        d0 = zero
        for c0, e0 in power_series:
            break
        else:
            yield d0
            return
        one_leading_series = power_series
        000;    power_series = None
        # [power_series == c0*z**e0 * one_leading_series]
        # [one_leading_series == 1 + c1/c0 *z**(e1-e0) + ...]

        ...
        # [power_series == c0*z**e0 / (1/one_leading_series)]
        it = convert_one_leading_series_fraction_to_generalized_continued_fraction_(iter([(one, 0)]), one_leading_series)
        yield d0
        yield (c0, e0)
        yield from it
        return
    def convert_one_leading_series_fraction_to_generalized_continued_fraction_(one_leading_series8N, one_leading_series8D, /):
        if 0:
            yield one
        while 1:
            if 0b00:print(f'convert_one_leading_series_fraction_to_generalized_continued_fraction_')
            #bug:one_leading_series8N = iter(one_leading_series8N)
            one_leading_series8N = LazyList(one_leading_series8N)
            one_leading_series8D = LazyList(one_leading_series8D)
            if 0:
                ls = one_leading_series8D.iter__le(2)
                if not len(ls) >= 2:
                    if not ls: raise Error__one_leading_series__empty
                    if not ls == (one,): raise Error__one_leading_series__not_startswith_one
                    return

            it = _std_(_diff_(one_leading_series8N, one_leading_series8D))
            000; one_leading_series8N = None

            for c0, e0 in it:
                break
            else:
                # [N==D]
                # [N/D==1]
                return
            yield (c0, e0)
            one_leading_series8N = one_leading_series8D
            one_leading_series8D = it
        #end-while 1:
        return
    def _diff_(one_leading_series8N, one_leading_series8D, /):
        series8N = _drop_1_(one_leading_series8N)
        series8D = _drop_1_(one_leading_series8D)
        000; one_leading_series8N = None
        000; one_leading_series8D = None
        while 1:
            if 0b00:print(f'_diff_: {id(series8N):X} : {id(series8D):X}')
            if series8N.is_empty_(relax=False):
                break
            if series8D.is_empty_(relax=False):
                break
            ...
            c4N, e4N = series8N.extract_head_or_raise()
            c4D, e4D = series8D.extract_head_or_raise()
            if 0b000:print(f'_diff_: ({c4N!s}*z**{e4N!s}) <?> ({c4D!s}*z**{e4D!s})')

            to_drop4N = to_drop4D = False
            #bug:if e4N > e4D:
            if e4N < e4D:
                to_drop4N = True
                yield (c4N, e4N)
            #bug:elif e4N < e4D:
            elif e4N > e4D:
                to_drop4D = True
                yield (-c4D, e4D)
            else:
                if 0b00:print(f'_diff_: (?*z**{e4N!s}) <?> (?*z**{e4D!s})')
                to_drop4N = to_drop4D = True
                c = c4N-c4D
                if not c == zero:
                    yield (c, e4N)
            if to_drop4N:
                series8N = series8N.extract_tail_or_raise()
            if to_drop4D:
                series8D = series8D.extract_tail_or_raise()
        #end-while 1:
        series8N = iter(series8N)
        series8D = iter(series8D)
        yield from series8N
        for c4D, e4D in series8D:
            yield (-c4D, e4D)
    def _drop_1_(one_leading_series, /):
        #one_leading_series = LazyList(one_leading_series)
        for _1 in one_leading_series:
            break
        else:
            raise Error__one_leading_series__empty
        if not _1 == (one, 0): raise Error__one_leading_series__not_startswith_one(_1)
        _1, series = one_leading_series.unpack_or_raise()
        return series
    def _std_(power_series, /):
        power_series = iter(power_series)
        for (c0, e0) in power_series:
            break
        else:
            return
        e0 = __index__(e0)
        if c0 == zero:
            raise Error__coeff4power_series__eq_zero
        if e0 < 0:
            raise Error__exp4power_series__lt_zero

        c0_0 = c0/c0
        e0_0 = e0-e0
        if not c0_0 == one: raise Error__coeff4power_series__div_self_not_eq_one
        if not e0_0 == 0: raise Error__exp4power_series__diff_self_not_eq_zero
        yield c0, e0
        yield c0_0, e0_0 #(one, 0)
        e_prev = e0
        for (c1, e1) in power_series:
            e1 = __index__(e1)
            if c1 == zero:
                raise Error__coeff4power_series__eq_zero
            if not e_prev < e1:
                raise Error__exp4power_series__not_strict_increasing
            c1_0 = c1/c0
            e1_0 = e1-e0
            yield c1_0, e1_0
            ######
            e_prev = e1
    __ = _main_(power_series)
    000; power_series = None
    return __


def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__


from script.convert_1_leading_series_to_generalized_continued_fraction import *
