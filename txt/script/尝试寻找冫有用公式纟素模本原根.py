#__all__:goto
r'''[[[
e script/尝试寻找冫有用公式纟素模本原根.py

script.尝试寻找冫有用公式纟素模本原根
py -m nn_ns.app.debug_cmd   script.尝试寻找冫有用公式纟素模本原根 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.尝试寻找冫有用公式纟素模本原根:__doc__ -ht # -ff -df
#######

[[
比如:ceil_sqrt
]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   script.尝试寻找冫有用公式纟素模本原根   @测试冫如计算器纟素模本原根扌 :ceil_sqrt --素数集牜忽略='[2]' =100
    ^TestFail: (11, 4)

py_adhoc_call   script.尝试寻找冫有用公式纟素模本原根   @测试冫如计算器纟素模本原根扌 :floor_ceil_sqrt_  =100
    ^TestFail: (11, [3, 4])
]]


from script.尝试寻找冫有用公式纟素模本原根 import *
]]]'''#'''
__all__ = r'''
测试冫如计算器纟素模本原根扌
    解名冫如计算器纟素模本原根扌
分解冫素数减一扌
    上限纟素数

TooBig
NotPrime
TestFail
UnknownFuncName

floor_ceil_sqrt_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import is_kth_primitive_root_mod_N__via_complete_factorization_k_
    #def is_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, /, *, _ver=2):
    #   'may k/int{>=1} -> factorization{k} -> N/int{>=2} -> r/uint%N -> bool/[k==min_order_mod_(N;r)]'
    from seed.math.prime_gens import prime_gen
    from seed.math.prime_gens import all_prime_factors_gen, tabulate_may_all_prime_factors4uint_lt_
    from seed.math.prime_gens import hold_all_weakrefs4caches_
    from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
    #def complete_factor_pint_via_trial_division(candidate_factors, pint, /):
    #    'Iter factor{>=2} -> pint -> (factor2exp/{factor:exp{>=1}})'
    from seed.math.floor_ceil import floor_sqrt, ceil_sqrt
    from seed.tiny_.check import check_type_is, check_int_ge

    from itertools import islice

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

class TooBig(Exception):pass
class NotPrime(Exception):pass
class TestFail(Exception):pass
class UnknownFuncName(Exception):pass
上限纟素数 = 2**16
def 分解冫素数减一扌(p, /):
    check_int_ge(2, p)
    if not p <= 上限纟素数:raise TooBig(p, 上限纟素数)
    if not (p,) == all_prime_factors_gen[p]:raise NotPrime(p, all_prime_factors_gen[p])
    pmm = p-1
    p2e4pmm = complete_factor_pint_via_trial_division(all_prime_factors_gen[pmm], pmm)
    return p2e4pmm
def 测试冫如计算器纟素模本原根扌(素数讠如本原根扌, 趃素数丨素数数量, /, *, 素数集牜忽略=()):
    素数集牜忽略 = set(素数集牜忽略)
    素数讠如本原根扌 = 解名冫如计算器纟素模本原根扌(素数讠如本原根扌)
    if type(趃素数丨素数数量) is int:
        素数数量 = 趃素数丨素数数量
        it = iter(prime_gen)
        it = (p for p in it if not p in 素数集牜忽略)
        趃素数 = islice(it, 素数数量)
    else:
        趃素数 = 趃素数丨素数数量
        it = iter(趃素数)
        it = (p for p in it if not p in 素数集牜忽略)
        趃素数 = it
    趃素数
    000;    __ws = hold_all_weakrefs4caches_()
    for p in 趃素数:
        r_or_rs = 素数讠如本原根扌(p)
        if type(r_or_rs) is int:
            r = r_or_rs
            rs = (r,)
        else:
            rs = r_or_rs
        rs = sorted(set(rs))

        p2e4pmm = 分解冫素数减一扌(p)
        pmm = p-1
        rs7bad = []
        for r in rs:
            if is_kth_primitive_root_mod_N__via_complete_factorization_k_(pmm, p2e4pmm, p, r):
                break
        else:
            raise TestFail(p, rs)

def 解名冫如计算器纟素模本原根扌(素数讠如本原根扌, /):
    if not callable(素数讠如本原根扌):
        check_type_is(str, 素数讠如本原根扌)
        名 = 素数讠如本原根扌
        if not 名 in _oks: raise UnknownFuncName(名)
        素数讠如本原根扌 = globals()[名]
    素数讠如本原根扌
    return 素数讠如本原根扌
_oks = set('ceil_sqrt floor_ceil_sqrt_'.split())
def floor_ceil_sqrt_(u, /):
    x = floor_sqrt(u)
    y = x + (not x**2 == u)
    return (x,y)

__all__
from script.尝试寻找冫有用公式纟素模本原根 import *
