#__all__:goto
r'''[[[
e script/整数分解牜平方根附近牜平方筛.py

script.整数分解牜平方根附近牜平方筛
py -m nn_ns.app.debug_cmd   script.整数分解牜平方根附近牜平方筛 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.整数分解牜平方根附近牜平方筛:__doc__ -ht # -ff -df
#######

[[
]]

[[
整数分解:平方根附近:平方筛{k值}
[N==(z-a)*(z+b)
== zz+(b-a)*z-a*b
== zz+(b-a-k)*z +(k*z-a*b)
== zz +u*z +v
== (_z-dz)**2 +u*(_z-dz) +v
== (_z**2 -2*dz*_z +dz**2) +(u*_z -u*dz) +v
== _z**2 +(u -2*dz)*_z +(v +dz**2 -u*dz)
bug:== _z**2 +_u*_z +_v
    not:[_v == (v +dz**2 -u*dz)]
    but:[_v == (v +dz**2 -u*dz)%z]
]
[b-a == u+k]
[-a*b == v-k*z]
[(b+a)**2 == (u+k)**2 -4*(v-k*z)
== kk+2uk+uu-4v+4kz
== kk+(2u+4z)*k+(uu-4v)
== kk+s*k+t
== f(k)
== (k+s///2)**2 +(t -s**2///4)
]
[(t -s**2///4) == (uu-4v) -(2u+4z)**2///4 == (uu-4v) -(u+2z)**2 == -4v -4uz -4zz == -4N]

如何找到p，使得len[k | [k:<-[0..<p]][Jacobi_symbol(p;f(k)%p) == 1]]数量最少？
e script/整数分解牜平方根附近牜平方筛.py

bug:
    not:[_v == (v +dz**2 -u*dz)]
    but:[_v == (v +dz**2 -u*dz)%z]
    ... ...
    [_s == (2*_u+4*_z) == (2*(u -2*dz) +4*(z+dz)) == (2u+4z) == s]
    [_t == (_u**2 -4*_v) == ((u -2*dz)**2 -4*(v +dz**2 -u*dz)) == (uu-4v) == t]
    (s,t)与z无关
[z:=1]:
    [v == 0]
    [u == (N-1)]
    [s == (2u+4z) == 2N+2 == 2*(1+N)]
    [t == (uu-4v) == (N-1)**2]
    [(t -s**2///4) == (N-1)**2 -(1+N)**2 == -4N]
]]
[[
凑平方 由于[phi(m)%2==0] 所以麻烦
哪能不能 凑立方？
[(k**2+s*k+t)*(c*k+d)
== c*k**3 + (s*c+d)*k**2 +(t*c+s*d)*k +t*d
]
[(s+d/c)**2 == 3*(t+s*d/c)]
[(s+e)**2 == 3*(t+s*e)]
[(s**2+e**2-s*e) == (3*t)]
[(e**2-s*e+1/4*s**2) == 3*(t-1/4*s**2)]
[(e**2-s*e+1/4*s**2) == -12*N]
]]


'#'; __doc__ = r'#'
>>>



[[
view ../../python3_src/seed/math/factor_pint/factor_pint__near_sqrtN.py
>>> 193707721*761838257287==-1+2**67
True
>>> N = -1+2**67
147573952589676412927
>>> 2*(1+N)
295147905179352825856
>>> (N-1)**2
21778071482940061661065679065274459881476

py_adhoc_call   script.整数分解牜平方根附近牜平方筛   @n2zst_ ='-1+2**67'
    (12148001999, 48592007998, -39281659707)
py_adhoc_call   script.整数分解牜平方根附近牜平方筛   @n2zst_ ='-1+2**67' =999
    (12148002998, 48592007998, -39281659707)
py_adhoc_call   script.整数分解牜平方根附近牜平方筛   @n2zst_ ='-1+2**67' =1-12148001999
    (1, 295147905179352825856, 21778071482940061661065679065274459881476)
py_adhoc_call   script.整数分解牜平方根附近牜平方筛   @n2zst_ ='-1+2**67' =193707721-12148001999
    (193707721, 1524063930016, 580102419883595030788356)
py_adhoc_call   script.整数分解牜平方根附近牜平方筛   @n2zst_ ='-1+2**67' =1+193707721-12148001999
    (193707722, 1524063922152, 580102413890975673426068)
py_adhoc_call   script.整数分解牜平方根附近牜平方筛   @n2zst_ ='-1+2**67' =761838257287-12148001999
    (761838257287, 1524063930016, 580102419883595030788356)
py_adhoc_call   script.整数分解牜平方根附近牜平方筛   @n2zst_ ='-1+2**67' =-1+761838257287-12148001999
    (761838257286, 1524063930014, 580102419882070966858341)








py_adhoc_call   script.整数分解牜平方根附近牜平方筛   @n2zst_ ='-1+2**67' +ex
    (12148001999, 48592007998, -39281659707, -590295810358705651708)

py_adhoc_call   script.整数分解牜平方根附近牜平方筛   ,50:list_prime_infos4st_ =48592007998 =-39281659707
    ...没好处...
    (3, 2, 0.6666666666666666)
    (5, 2, 0.4)
    (7, 4, 0.5714285714285714)
    (11, 5, 0.45454545454545453)
    (13, 7, 0.5384615384615384)
    (17, 8, 0.47058823529411764)
    (19, 9, 0.47368421052631576)
    (23, 12, 0.5217391304347826)
    (29, 14, 0.4827586206896552)
    (31, 15, 0.4838709677419355)
    (37, 19, 0.5135135135135135)
    (41, 21, 0.5121951219512195)
    (43, 21, 0.4883720930232558)
    (47, 23, 0.48936170212765956)
    (53, 27, 0.5094339622641509)
    (59, 29, 0.4915254237288136)
    (61, 31, 0.5081967213114754)
    (67, 34, 0.5074626865671642)
    (71, 36, 0.5070422535211268)
    (73, 36, 0.4931506849315068)
    (79, 39, 0.4936708860759494)
    (83, 42, 0.5060240963855421)
    (89, 45, 0.5056179775280899)
    (97, 49, 0.5051546391752577)
    (101, 51, 0.504950495049505)
    (103, 51, 0.49514563106796117)
    (107, 53, 0.4953271028037383)
    (109, 54, 0.4954128440366973)
    (113, 57, 0.504424778761062)
    (127, 64, 0.5039370078740157)
    (131, 65, 0.4961832061068702)
    (137, 69, 0.5036496350364964)
    (139, 69, 0.49640287769784175)
    (149, 74, 0.4966442953020134)
    (151, 76, 0.5033112582781457)
    (157, 79, 0.5031847133757962)
    (163, 81, 0.49693251533742333)
    (167, 84, 0.5029940119760479)
    (173, 87, 0.5028901734104047)
    (179, 89, 0.4972067039106145)
    (181, 91, 0.5027624309392266)
    (191, 96, 0.5026178010471204)
    (193, 97, 0.5025906735751295)
    (197, 99, 0.5025380710659898)
    (199, 99, 0.49748743718592964)
    (211, 105, 0.4976303317535545)
    (223, 111, 0.4977578475336323)
    (227, 113, 0.4977973568281938)
    (229, 114, 0.4978165938864629)
    (233, 116, 0.4978540772532189)

]]

from script.整数分解牜平方根附近牜平方筛 import *
]]]'''#'''
__all__ = r'''
n2zst_
list_prime_infos4st_
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
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.prime_sieve.sieve_ge_le import iter_primes_
    from seed.math.Jacobi_symbol import Jacobi_symbol
#.    from itertools import islice
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

def n2zst_(N, dz=0, /, *, ex=False):
    check_int_ge(4, N)
    z = dz+floor_sqrt(N)
    (u, v) = divmod(N-z**2, z)
    # [N == zz +uz +v]
    s = 2*u +4*z
    t = u**2 -4*v
    # [N == (z-a)*(z+b)]
    # [(a+b)**2 == kk+sk+t == (k+s///2)**2 +(t -s**2///4)]
    _neg_4N_ = (t -s**2//4)
    assert _neg_4N_ == -4*N
    if 1:
        a = z-1
        b = N-z
        assert N == (z-a)*(z+b)
        k = b-a-u
        assert k*z-a*b == v
        assert (a+b)**2 == k**2 +s*k +t
    return (z, s, t) if not ex else (z, s, t, _neg_4N_)

def list_prime_infos4st_(s, t, /):
    ps = iter_primes_()
    next(ps) # Jacobi_symbol only for odd
    for p in ps:
        j2bsquare = [False]*p
        for i in range(p):
            j = pow(i, 2, p)
            j2bsquare[j] = True

        num_squares = 0
        for k in range(p):
            cc = (k**2 +s*k +t)%p
            #if not -1 == Jacobi_symbol(p, cc):
            if j2bsquare[cc]:
                num_squares += 1
        yield (p, num_squares, num_squares/p)


__all__
from script.整数分解牜平方根附近牜平方筛 import *
