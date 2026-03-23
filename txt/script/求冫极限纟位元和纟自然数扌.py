#__all__:goto
r'''[[[
e script/求冫极限纟位元和纟自然数扌.py

script.求冫极限纟位元和纟自然数扌
py -m nn_ns.app.debug_cmd   script.求冫极限纟位元和纟自然数扌 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.求冫极限纟位元和纟自然数扌:__doc__ -ht # -ff -df
#######

[[
[radix:<-[2..]][u:<-[0..]]:
    [digit_sum4uint9_(radix;u) =[def]= sum(uint2radix_repr_(radix, u, is_big_endian=True))]
    [limit4digit_sum4uint9_(radix;u) =[def]= if u < radix then u else limit4digit_sum4uint9_(1+radix;digit_sum4uint9_(radix;u))]

[u:<-[0..]]:
    [limit4digit_sum4uint_(u) =[def]= limit4digit_sum4uint9_(2;u)]


]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   @求冫极限纟位元和纟自然数扌  =567788532224766777
    3
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   @求冫极限纟位元和纟自然数扌  =567788532224766777  +ex
    (3, 4, [567788532224766777, 29], [59, 4], [(1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1), (1, 0, 0, 2)])
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   @求冫极限纟位元和纟自然数扌  =567788532224766777  +ex +bijective
    (3, 4, [567788532224766777, 28], [58, 3], [(1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0), (1, 2, 0)])
]]
[[
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   ,200:求冫极限纟位元和纟趃自然数扌  ='count(0)'
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   @list.200:求冫极限纟位元和纟趃自然数扌  ='count(0)'
printf %s $(py_adhoc_call   script.求冫极限纟位元和纟自然数扌   ,200:求冫极限纟位元和纟趃自然数扌  ='count(0)' )
    01121221122121121221211221121223122121122112122321121223122323321221211221121223211212231223233221121223122323321223233223323223122121122112122321121223122323322112122312232332122323322332322321121223
]]
[[
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   ,极限纟位元和讠趃丮最小自然数辻基数辻位元串厈扌  =4
    (4, 5, (4,))
    (4, 4, (1, 3))
    (7, 3, (1, 2, 2, 2))
    (53, 2, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
    (9007199254740991, 1, ())
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   @求冫极限纟位元和纟自然数扌  =9007199254740991
    4
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   @求冫极限纟位元和纟自然数扌  =9007199254740991 +ex
    (4, 5, [9007199254740991, 53, 7], [53, 4, 2], [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 2, 2, 2), (1, 3)])
]]
[[
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   ,极限纟位元和讠趃丮最小自然数辻基数辻位元串厈扌  =4 +bijective
    很大
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   ,极限纟位元和讠趃丮最小自然数辻基数辻位元串厈扌  =3 +bijective
    (3, 4, (3,))
    (4, 3, (2, 2))
    (12, 2, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
    (8190, 1, ())
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   @求冫极限纟位元和纟自然数扌  =8190 +bijective +ex
    (3, 5, [8190, 12, 4], [12, 2, 1], [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (2, 2), (3,)])
]]
[[
py_adhoc_call   script.求冫极限纟位元和纟自然数扌   ,极限纟位元和讠趃丮最小自然数辻基数辻位元串厈扌  =5
    (5, 6, (5,))
    (5, 5, (1, 4))
    (9, 4, (3, 3, 3))
    (63, 3, (1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2))
    ^OverflowError: 1235346792567893

py_adhoc_call   script.求冫极限纟位元和纟自然数扌   ,极限纟位元和讠趃丮最小自然数辻基数辻位元串厈扌  =5 +bijective
    (5, 6, (5,))
    (6, 5, (2, 4))
    (20, 4, (2, 3, 3, 3, 3, 3, 3))
    (17748, 3, (2, 2, 2, 2, ...))
    ^OverflowError: 141288118359573126018437571367215643563...45208853666936185043828834273596606652
]]

]]]'''#'''
__all__ = r'''
求冫极限纟位元和纟自然数扌
    求冫极限纟位元和纟趃自然数扌

极限纟位元和讠趃丮最小自然数辻基数辻位元串厈扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
    from seed._lazy_ import mk_tuple
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'uint2radix_repr:uint2radix_repr_'):
    from seed.tiny_.check import check_type_is, check_int_ge
    #.from seed.int_tools.digits.uint2radix_repr import uint2radix_repr as uint2radix_repr_
    from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_, uint5radix_repr_
        #.u = uint5radix_repr_(radix, digits, is_big_endian=is_big_endian, **kwds)
        #.digits = uint2radix_repr_(radix, u, is_big_endian=is_big_endian, **kwds)
    from seed.int_tools.digits.uint25bijective_numeration import uint5bijective_numeration_, uint2bijective_numeration_
        #.def uint2bijective_numeration_(radix, u, /, *, is_big_endian, offset4digit):
        #.def uint5bijective_numeration_(radix, offsetted_digits, /, *, is_big_endian, offset4digit):

    from itertools import repeat#count#islice
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
#.    from seed.func_tools.dot2 import dot
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def 求冫极限纟位元和纟趃自然数扌(us, /, *, radix=2, ex=False, bijective=False):
    check_type_is(bool, ex)
    check_int_ge(2, radix)
    for u in us:
        yield 求冫极限纟位元和纟自然数扌(u, radix=radix, ex=ex, bijective=bijective)
def 求冫极限纟位元和纟自然数扌(u, /, *, radix=2, ex=False, bijective=False):
    check_type_is(bool, bijective)
    check_type_is(bool, ex)
    check_int_ge(2, radix)
    check_int_ge(0, u)
    (u2digits_, kwds) = _mk_u2digits_ex_(bijective)
    #.for radix in count(radix):
    if ex:
        us = []
        lens4digitss = []
        digitss = []
    while not u < radix:
        digits = u2digits_(radix, u, **kwds)
        if ex:
            digits = mk_tuple(digits)
            us.append(u)
            lens4digitss.append(len(digits))
            digitss.append(digits)
        digit_sum = sum(digits)
        u = digit_sum
        radix += 1
    if ex:
        return (u, radix, us, lens4digitss, digitss)
    return u
def _mk_u2digits_ex_(bijective, /):
    if bijective:
        u2digits_ = uint2bijective_numeration_
        kwds = dict(is_big_endian=True, offset4digit=0)
    else:
        u2digits_ = uint2radix_repr_
        kwds = dict(is_big_endian=True)
    return (u2digits_, kwds)
def _mk_u5digits_ex_(bijective, /):
    if bijective:
        u5digits_ = uint5bijective_numeration_
        kwds = dict(is_big_endian=True, offset4digit=0)
    else:
        u5digits_ = uint5radix_repr_
        kwds = dict(is_big_endian=True)
    return (u5digits_, kwds)
def 极限纟位元和讠趃丮最小自然数辻基数辻位元串厈扌(digit_sum, /, *, bijective=False, MAX_NUM_DIGITS=2**16):
    '#反函数{求冫极限纟位元和纟自然数扌}'
    check_type_is(bool, bijective)
    check_int_ge(0, digit_sum)
    (u5digits_, kwds) = _mk_u5digits_ex_(bijective)
    radix = max(2, 1+digit_sum)
    while 1:
        max_digit = -1+radix
        (q, r) = divmod(digit_sum, max_digit)
        num_digits = q+bool(r)
        if num_digits > MAX_NUM_DIGITS:raise OverflowError(num_digits)#Exception
        tmay_head = (r,) if r else ()
        digits = (*tmay_head, *repeat(max_digit, q))
        yield (digit_sum, radix, digits)
        u = u5digits_(radix, digits, **kwds)
        if radix == 2:
            break
        digit_sum = u
        radix -= 1
    yield (u, 1, ())



__all__
from script.求冫极限纟位元和纟自然数扌 import 求冫极限纟位元和纟自然数扌, 求冫极限纟位元和纟趃自然数扌, 极限纟位元和讠趃丮最小自然数辻基数辻位元串厈扌
from script.求冫极限纟位元和纟自然数扌 import *
