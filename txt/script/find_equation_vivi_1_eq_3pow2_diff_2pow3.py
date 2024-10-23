#__all__:goto
r'''[[[
e script/find_equation_vivi_1_eq_3pow2_diff_2pow3.py
九宫八卦基本关系式:[1 == 3**2 - 2**3]

script.find_equation_vivi_1_eq_3pow2_diff_2pow3
py -m nn_ns.app.debug_cmd   script.find_equation_vivi_1_eq_3pow2_diff_2pow3 -x
py -m nn_ns.app.doctest_cmd script.find_equation_vivi_1_eq_3pow2_diff_2pow3:__doc__ -ht
py_adhoc_call   script.find_equation_vivi_1_eq_3pow2_diff_2pow3   ,find_equation_vivi_1_eq_3pow2_diff_2pow3   -to_exclude_Pythagorean_triples +to_exclude_double_cases =10 =10
(1, 8, 9)
(9, 16, 25)
(4, 32, 36)
(9, 27, 36)
(32, 49, 81)
(36, 64, 100)
(25, 100, 125)
(27, 216, 243)
(100, 243, 343)

py_adhoc_call   script.find_equation_vivi_1_eq_3pow2_diff_2pow3   ,find_equation_vivi_1_eq_3pow2_diff_2pow3   +to_exclude_Pythagorean_triples +to_exclude_double_cases =10 =10
(1, 8, 9)
(4, 32, 36)
(9, 27, 36)
(32, 49, 81)
(25, 100, 125)
(27, 216, 243)
(100, 243, 343)


#]]]'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from math import isqrt
__gt__ = int.__gt__
__ge__ = int.__ge__
___end_mark_of_excluded_global_names__0___ = ...


def uniqued_sorted_seq5iterable_or_max(min_u, iterable_or_max_u, /):
    if type(iterable_or_max_u) is int:
        max_u = iterable_or_max_u
        return range(min_u, 1+max_u)
    it = iterable_or_max_u
    return tuple(sorted(set(it)))
def is_square_(u, /):
    return isqrt(u)**2 == u
def find_equation_vivi_1_eq_3pow2_diff_2pow3(iterable_or_max_exp, iterable_or_max_base, /, *, to_exclude_double_cases, to_exclude_Pythagorean_triples):
    '-> Iter (a, b, c){[a+b==c]}'
    gx = __ge__ if to_exclude_double_cases else __gt__
    x222 = bool(to_exclude_Pythagorean_triples)

    es = uniqued_sorted_seq5iterable_or_max(2, iterable_or_max_exp)
    us = uniqued_sorted_seq5iterable_or_max(1, iterable_or_max_base)
    assert not es or es[0] >= 2
    assert not us or us[0] >= 1

    s = {u**e for e in es for u in us}
    j2u = sorted(s)
    if x222:
        j2is_square = [*map(is_square_, j2u)]
        u2j = {u:j for j,u in enumerate(j2u)}

    L = len(j2u)
    for i in range(L):
        c = j2u[i]
        for j in reversed(range(i)):
            b = j2u[j]
            a = c - b
            assert a > 0
            if gx(a, b): break
            if a in s:
                if x222 and j2is_square[i] and j2is_square[j] and j2is_square[u2j[a]]:
                    continue
                yield (a, b, c)

__all__
from script.find_equation_vivi_1_eq_3pow2_diff_2pow3 import *
