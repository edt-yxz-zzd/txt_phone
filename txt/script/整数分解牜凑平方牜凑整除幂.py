#__all__:goto
r'''[[[
e script/整数分解牜凑平方牜凑整除幂.py
view ../../python3_src/seed/math/search_smooth_around_interval.py

script.整数分解牜凑平方牜凑整除幂
py -m nn_ns.app.debug_cmd   script.整数分解牜凑平方牜凑整除幂 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.整数分解牜凑平方牜凑整除幂:__doc__ -ht # -ff -df
#######

[[
失败...只能减少至:O(N/**2)
===
QS:
    [(ideal{qs}*x**2 +k*N) <- ideal{ps\-\qs}]
    [(Q*x**2+k*N) %p == 0]:
        [k%p == (-Q*x**2 * N**-1) %p]
        CRT?
        [k%P == (-Q*x**2 * N**-1) %P]

    凑偶除二！负一！
    [x,N::odd][xx:=x**2%N]:
        [(xx-N)///-2 < N/2]
        [f(xx,N,W,z):=(xx*N**-1%z**W)]
        [(xx-N*f(xx,N,W,2))///-2**W < ???]
        [(xx-N*f(xx,N,W,2))///-2**W < N*f(xx,N,W,2)/2**W]
        how[f(xx,N,W,p)很小]?
        [Jacobi_symbol(p;N) == 1][(p**W)**2 < N]:
            [xp**2 == N%p]
            [xpW**2 == N%p**W]
            [xpW**2 < (p**W)**2 < N]
            [xpW**2 %N == xpW**2]
_
]]


'#'; __doc__ = r'#'
>>>


[[
py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @凑整除幂扌  =999 =5
    (68, -194)

py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @凑整除幂扌 --ver=1  ='-1+2**67' =3
    ver1:floor_log_(p,N):
        (45010737213839606863, 129058277379971399789, [(-1, 1), (3, 42)])
        (45010737213839606863, -18515675209705013138, [(-1, 1), (3, 42)])

py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @凑整除幂扌 --ver=2  ='-1+2**67' =3
    ver2:floor_log_(p,fsqrt4N):
        (2018499299, 13718429042, [(-1, 1), (3, 21), (1, -1)])

py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @凑整除幂扌 --ver=2  ='-1+2**67' =3 =4
    (4220926952, 7295074437, [(-1, 1), (3, 21), (4, -1)])
py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @凑整除幂扌 --ver=3  ='-1+2**67' =3 =4
    (734142551, 41705501323, [(-1, 1), (3, 20), (4, -1)])
py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @凑整除幂扌 --ver=2  ='-1+2**67' =3 ='737**2'
    (3446197190, -616678687195591, [(-1, 1), (3, 21), (543169, -1)])
py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @凑整除幂扌 --ver=3  ='-1+2**67' =3 ='737**2'
    (2459510, 10055694166161, [(-1, 1), (3, 15), (543169, -1)])

py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @凑整除幂扌 --ver=4  ='-1+2**67' =3
    (2018499299, 13718429042, [(-1, 1), (3, 21), (1, -1)])


]]
[[
py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   ,凑整除幂牜尝试扌  ='-1+2**67' =3 =1
    (22939205705, 12065660322, [(3, 22)])
    (2018499299, 13718429042, [(-1, 1), (3, 21)])
py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   ,凑整除幂牜尝试扌  ='-1+2**67' =3 =7
    (31677672440, 73045659299, [(3, 23), (7, -1)])
    (296612831, 4683019000, [(-1, 1), (3, 22), (7, -1)])

]]



py_adhoc_call   script.整数分解牜凑平方牜凑整除幂   @f
from script.整数分解牜凑平方牜凑整除幂 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.sqrts_mod_ import list_sqrts_mod_prime_power_
    #def list_sqrts_mod_prime_power_(p, k, xx, /, *, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
    from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt, ceil_sqrt# floor_kth_root_, ceil_kth_root_
    from seed.math.floor_ceil_tools.fc_log import ceil_log_, floor_log_
    from seed.math.Jacobi_symbol import Jacobi_symbol
    from seed.math.floor_ceil_tools.fc_perfect import perfect_div
    from seed.tiny_.check import check_type_is, check_int_ge

    from seed.math.search_smooth_around_interval import search_smooth_integer_around_interval_, search_max_smooth_integer_le_, search_min_smooth_integer_ge_
    #def search_smooth_integer_around_interval_(min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
    from seed.math.search_smooth_around_interval import sorted_search_smooth_integer_inside_interval_, disordered_search_smooth_integer_inside_interval_, disordered_iter_search_smooth_integer_inside_interval_
    #def sorted_search_smooth_integer_inside_interval_(min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def 凑整除幂扌(N, p, g=1, /, *, ver):
    check_int_ge(1, g)
    check_int_ge(2, p)
    check_int_ge(p, N)
    if N%p == 0:raise ValueError(N, p)
    match ver:
        case 1:
            W = floor_log_(p, N)
        case 2:
            fsqrt4N = floor_sqrt(N)
            W = floor_log_(p, fsqrt4N)
        case 3:
            fsqrt4Ng = floor_sqrt(N//g)
            W = floor_log_(p, fsqrt4Ng)
        case 4:
            csqrt4N = ceil_sqrt(N)
            W = floor_log_(p, csqrt4N)
        case _:
            raise Exception(ver)
    W
    pW = p**W
    inv4N6pW = pow(N, -1, pW)
    inv4g6pW = pow(g, -1, pW)
    xs = list_sqrts_mod_prime_power_(p, W, inv4g6pW*N)
    if not xs:raise ValueError('[Jacobi_symbol(p;N/g) == -1]', N, p, g)
    x = min(xs)
    xx = x**2
    xx6N = xx%N
    assert not ver==2 or xx6N == xx < N
    #xx6pW = xx%pW
    if 0:
        k = (inv4N6pW*xx6N %pW)
        assert not ver==2 or k == 1, k
        y = perfect_div(k*N -xx6N, pW)
    else:
        #k = (inv4N6pW*xx %pW)
        #assert k == 1, k
        #y = perfect_div(k*N -xx, pW)
        y = perfect_div(N -g*xx, pW)
    assert (y*-pW) %N == xx6N*g%N
    return (x, y, [(-1,1), (p,W), (g,-1)])

def 凑整除幂牜尝试扌(N, p, g, /):
    check_int_ge(1, g)
    check_int_ge(2, p)
    check_int_ge(p, N)
    if N%p == 0:raise ValueError(N, p)
    W = ceil_log_(p, N)
    pW = p**W
    #inv4N6pW = pow(N, -1, pW)
    inv4g6pW = pow(g, -1, pW)
    xs = list_sqrts_mod_prime_power_(p, W, inv4g6pW*N)
    if not xs:raise ValueError('[Jacobi_symbol(p;N/g) == -1]', N, p, g)
    x0 = min(xs)
    tmg = [] if g==1 else [(g,-1)]
    ls = []
    for _W in range(W, 0, -1):
        _pW = p**_W
        x = x0%_pW
        xx = x**2
        y = perfect_div(g*xx -N, _pW)
        assert (y*_pW) %N == xx*g%N
        if y < 0:
            record = (x, -y, [(-1,1), (p,_W), *tmg])
        else:
            record = (x, +y, [(p,_W), *tmg])
        ls.append(record)
        if y < 0:
            break
    ls
    del ls[:-2]
    return ls

__all__
from script.整数分解牜凑平方牜凑整除幂 import *
