#__all__:goto
r'''[[[
e script/p_adic_digit_distribution_mod_uint_power.py

script.p_adic_digit_distribution_mod_uint_power
py -m nn_ns.app.debug_cmd   script.p_adic_digit_distribution_mod_uint_power -x # -off_defs
py -m nn_ns.app.doctest_cmd script.p_adic_digit_distribution_mod_uint_power:__doc__ -ht # -ff -df
#######

[[
f(k,n;u) := uint2radix_repr_(n, u**(n-1) % n**k, is_big_endian=False)
view ../../python3_src/seed/int_tools/digits/uint25radix_repr.py
from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_, uint5radix_repr_
    decimal_digits = uint2radix_repr_(radix, u, is_big_endian=is_big_endian, **kwds)
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   script.p_adic_digit_distribution_mod_uint_power   @f
from script.p_adic_digit_distribution_mod_uint_power import *
]]]'''#'''
__all__ = r'''
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
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__):
#.    from itertools import islice
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
#.    from seed.func_tools.dot2 import dot
#.    from seed.tiny_.check import check_type_is, check_int_ge
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.#################################
___end_mark_of_excluded_global_names__0___ = ...



__all__
from script.p_adic_digit_distribution_mod_uint_power import *
