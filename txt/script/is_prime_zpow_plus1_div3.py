#__all__:goto
r'''[[[
e script/is_prime_zpow_plus1_div3.py

script.is_prime_zpow_plus1_div3
py -m nn_ns.app.debug_cmd   script.is_prime_zpow_plus1_div3 -x
py -m nn_ns.app.doctest_cmd script.is_prime_zpow_plus1_div3:__doc__ -ht

py_adhoc_call   script.is_prime_zpow_plus1_div3   ,10:iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_
(1, 3)
(1, 5)
(1, 7)
(1, 11)
(1, 13)
(1, 17)
(1, 19)
(1, 23)
(1, 31)
(1, 43)

py_adhoc_call  { +lineno } script.is_prime_zpow_plus1_div3   ,100:iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_
1:(1, 3)
2:(1, 5)
3:(1, 7)
4:(1, 11)
5:(1, 13)
6:(1, 17)
7:(1, 19)
8:(1, 23)
9:(1, 31)
10:(1, 43)
11:(1, 61)
12:(1, 79)
13:(-1, 101)
14:(-1, 127)
15:(-1, 167)
16:(-1, 191)
17:(-1, 199)
18:(-1, 313)
19:(-1, 347)
20:(-1, 701)
21:(-1, 1709)
22:(-1, 2617)
... ^C KeyboardInterrupt

23:(-1, 3539) #1分钟强
24:(-1, 5807) #7分钟强





3, 5, 7, 13, 17, 19, 31, 61, 127, ...
    <<==交集
vs: (2**e+1)///3 vs (2**e-1)
    view ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
A000043
    Mersenne exponents: primes p such that 2^p - 1 is prime. Then 2^p - 1 is called a Mersenne prime.
    (Formerly M0672 N0248)
    2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667



py_adhoc_call  { +lineno } script.is_prime_zpow_plus1_div3   ,100:iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_ +mersenne
1:(1, 3)
2:(1, 5)
3:(1, 7)
4:(1, 13)
5:(1, 17)
6:(1, 19)
7:(1, 31)
8:(1, 61)
9:(-1, 127)
... ^C KeyboardInterrupt

py_adhoc_call  { +lineno } script.is_prime_zpow_plus1_div3   ,100:iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_ +mersenne +verbose
    before: ++timer
# 3
1:(1, 3)
# 5
2:(1, 5)
# 7
3:(1, 7)
# 13
4:(1, 13)
# 17
5:(1, 17)
# 19
6:(1, 19)
# 31
7:(1, 31)
# 61
8:(1, 61)
# 89
# 107
# 127
9:(-1, 127)
# 521
# 607
# 1279
# 2203
# 2281
# 3217
# 4253
# 4423
# 9689
# 9941
# 11213
# 19937
# 21701
# 23209
# 44497
# 86243
... ^C KeyboardInterrupt: 86243




py_adhoc_call  { --lineno=10 } script.is_prime_zpow_plus1_div3   ,100:iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_ +mersenne +verbose --begin_exp=86243
    after: ++timer
    53分钟强
# 86243
[SPRP:(2**e-1)][SPRP:(2**e+1)/3]:86243: ... ...
[SPRP:(2**e-1)][SPRP:(2**e+1)/3]:86243:duration: 3187.933666715 *(unit: 0:00:01)
# 110503
[SPRP:(2**e-1)][SPRP:(2**e+1)/3]:110503: ... ...
^C[SPRP:(2**e-1)][SPRP:(2**e+1)/3]:110503:duration: 75.69456918500009 *(unit: 0:00:01)
Traceback (most recent call last):
    ...
KeyboardInterrupt: 110503




py_adhoc_call  { --lineno=22+1 } script.is_prime_zpow_plus1_div3   ,1:iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_ -mersenne +to_show_timeit --begin_exp=2617+1 --_low_duration_threshold4show_=10
    1分钟强
[SPRP:(2**e+1)/3]:3539:duration: 71.09771070800001 *(unit: 0:00:01)
23:(-1, 3539)

py_adhoc_call  { --lineno=23+1 } script.is_prime_zpow_plus1_div3   ,1:iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_ -mersenne +to_show_timeit --begin_exp=3539+1 --_low_duration_threshold4show_=10
    7分钟强
[SPRP:(2**e+1)/3]:5807:duration: 434.878573848 *(unit: 0:00:01)
24:(-1, 5807)


#]]]'''
__all__ = r'''
iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_
    is_old_exponent_of_strong_pseudoprime_of_form_zpow_plus1_div3__imay_bool_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny import print_err
from seed.tiny_.check import check_type_is, check_int_ge
#from seed.math.is_prime__le_pow2_64 import is_prime__le_pow2_64
from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_
from seed.math.prime_gens import is_prime__le_pow2_81_
from seed.math.prime_gens import iter_primes__le_pow2_81__ge_, iter_pseudoprimes__ge_
#from itertools import count
from nn_ns.math_nn.numbers.Mersenne_exponents import Mersenne_exponents, Mersenne_exponents__stable, Mersenne_exponents__unstable

from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)



___end_mark_of_excluded_global_names__0___ = ...

def is_old_exponent_of_strong_pseudoprime_of_form_zpow_plus1_div3__imay_bool_(odd_exp, /):
    '[odd_exp%2==1] => odd_exp/uint -> imay_bool/{0|1|-1}/[is_strong_pseudoprime((2**odd_exp+1)/3)]'
    check_int_ge(0, odd_exp)
    if not (odd_exp&1 == 1):
        raise ValueError('not odd', odd_exp)
    zpow = 1 << odd_exp
    (q, r) = divmod(zpow+1, 3)
    assert r == 0, (odd_exp, r)
    if odd_exp <= 82:
        return int(is_prime__le_pow2_81_(q))
    return detect_strong_pseudoprime__not_waste_too_much_time_(q)

#def is_minus1_half_of_exponent_of_strong_pseudoprime_of_form_zpow_plus1_div3__imay_bool_(emm_half, /):
#    'emm_half/uint -> imay_bool/{0|1|-1}/is_strong_pseudoprime((2**(2*emm_half+1)+1)/3)'
#    check_int_ge(0, emm_half)

def iter_cased_old_exponents_of_strong_pseudoprime_of_form_zpow_plus1_div3_(*, mersenne=False, verbose=False, to_show_each_trial=False, to_show_timeit=False, begin_exp=3, _low_duration_threshold4show_=0):
    '-> Iter ({1|-1}, odd_exp)'
    check_type_is(bool, mersenne)
    check_type_is(bool, verbose)
    check_type_is(bool, to_show_each_trial)
    check_type_is(bool, to_show_timeit)
    check_int_ge(0, begin_exp)

    begin_exp = max(3, begin_exp)
    to_show_each_trial = verbose or to_show_each_trial
    to_show_timeit = verbose or to_show_timeit

    f = is_old_exponent_of_strong_pseudoprime_of_form_zpow_plus1_div3__imay_bool_
    ls = Mersenne_exponents__stable
    it = iter(ls[ls.index(begin_exp):]) if mersenne else iter_primes__le_pow2_81__ge_(begin_exp)
    timer = timer__print_err__thread_wide
    _to_show_ = to_show_timeit
    fmt4prefix = '[SPRP:(2**e-1)][SPRP:(2**e+1)/3]:{}' if mersenne else '[SPRP:(2**e+1)/3]:{}'
    kwds = dict(_to_show_=_to_show_, _show_hint_on_enter_=False and _to_show_, _low_duration_threshold4show_=_low_duration_threshold4show_)
    try:
        #for odd_exp in count(1, 2):
        for odd_exp in it:
            if to_show_each_trial:
                print_err('#', odd_exp)
            t = timer(prefix=fmt4prefix.format(odd_exp), **kwds)
            with t:
                imay_bool = f(odd_exp)

            if imay_bool:
                yield (imay_bool, odd_exp)
    except KeyboardInterrupt:
        raise KeyboardInterrupt(odd_exp)


__all__
from script.is_prime_zpow_plus1_div3 import *
