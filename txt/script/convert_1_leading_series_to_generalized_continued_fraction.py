#__all__:goto
r'''[[[
e ./script/convert_1_leading_series_to_generalized_continued_fraction.py
view others/数学/continued-fraction/generalized_continued_fraction.txt
    # [:分式转化为连分式]:goto


script.convert_1_leading_series_to_generalized_continued_fraction
py -m nn_ns.app.debug_cmd   script.convert_1_leading_series_to_generalized_continued_fraction -x
py -m nn_ns.app.doctest_cmd script.convert_1_leading_series_to_generalized_continued_fraction:__doc__ -ff -v
from script.convert_1_leading_series_to_generalized_continued_fraction import *



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

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_, factor_pint_by_trial_division_ex_
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





#def convert_1_leading_series_to_generalized_continued_fraction_():
def convert_power_series4arcsin_to_generalized_continued_fraction_(sz, /, *, factor_as_p2e=False):
    power_series = iter_power_series4arcsin_()
    it = convert_power_series_to_generalized_continued_fraction__coeff_is_Fraction_(power_series, factor_as_p2e=factor_as_p2e)
    it = islice(it, sz)
    return it

def convert_power_series_to_generalized_continued_fraction__coeff_is_Fraction_(power_series, /, *, factor_as_p2e=False):
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
        for nk,e in it:
            N,D = nk.as_integer_ratio()
            absN = abs(N)
            p2e4N = factor_pint_by_trial_division_(absN)
            p2e4D = factor_pint_by_trial_division_(D)
            if N < 0:
                p2e4N[-1] = 1
            ps8N = (*sorted(p2e4N.items()),)
            ps8D = (*sorted(p2e4D.items()),)
            yield ((ps8N, ps8D), e)
    def _std_(power_series, /):
        for c, e in power_series:
            yield Fraction(c), __index__(e)
    return _main_(power_series)
def iter_power_series4arcsin_():
    '[arcsin(x) == x + 1/2*x**3/3 + 1/2*3/4*x**5/5 + 1/2*3/4*5/6*x**7/7 +...]'
    acc = Fraction(1)
    for k in count_(1, 2):
        yield (acc/k, k)
        acc = (acc*k) /(k+1)
def convert_power_series_to_generalized_continued_fraction_(zero, one, power_series, /):
    r'''[[[
    'power_series/(Iter (coeff4PS/real{=!=0}, exp4PS/uint){exp[k] < exp[k+1]}) -> gcf/([d0/real] ++ Iter (coeff4N/real{=!=0}, exp4N/pint)) # gcf[d0; n1$d1, ...]; [n0 == ...]; [d1 == d2 == ... == 1]'

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
        it = convert_one_leading_series_fraction_to_generalized_continued_fraction_([(one, 0)], one_leading_series)
        yield d0
        yield (c0, e0)
        yield from it
        return
    def convert_one_leading_series_fraction_to_generalized_continued_fraction_(one_leading_series8N, one_leading_series8D, /):
        if 0:
            yield one
        while 1:
            one_leading_series8N = iter(one_leading_series8N)
            one_leading_series8D = LazyList(one_leading_series8D)
            if 0:
                ls = one_leading_series8D.iter__le(2)
                if not len(ls) >= 2:
                    if not ls: raise Error__one_leading_series__empty
                    if not ls == (one,): raise Error__one_leading_series__not_startswith_one
                    return

            it = _std_(_diff_(one_leading_series8N, one_leading_series8D))
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
            if series8N.is_empty_(relax=False):
                break
            if series8D.is_empty_(relax=False):
                break
            ...
            c4N, e4N = series8N.extract_head_or_raise()
            c4D, e4D = series8D.extract_head_or_raise()

            to_drop4N = to_drop4D = False
            if e4N > e4D:
                to_drop4N = True
                yield (c4N, e4N)
            elif e4N < e4D:
                to_drop4D = True
                yield (-c4D, e4D)
            else:
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
        one_leading_series = LazyList(one_leading_series)
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
        yield c0_0, e0_0
        e_prev = e0
        for (c1, e1) in power_series:
            e1 = __index__(e1)
            if c1 == 0:
                raise Error__coeff4power_series__eq_zero
            if not e_prev < e1:
                raise Error__exp4power_series__not_strict_increasing
            c1_0 = c1/c0
            e1_0 = e1-e0
            yield c1_0, e1_0
            ######
            e_prev = e1
    return _main_(power_series)


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
