#__all__:goto
r'''[[[
e script/整数分解牜两位数乘法.py

py -m script.整数分解牜两位数乘法
py -m nn_ns.app.debug_cmd   script.整数分解牜两位数乘法 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.整数分解牜两位数乘法:__doc__ -ht # -ff -df
#######

[[
]]

[[
@20260518
整数分解:
感觉很有希望:但最终证明无用:始终不能分割((a+b)+a*b/z)
[N/k**2
== (z/k+a/k)*(z/k+b/k)
== (z/k)**2 +(a/k+b/k)*(z/k) +(a/k)*(b/k)
== (z/k)**2 +((a+b)/k)*(z/k) +(a*b/k**2)
== (z/k)**2 +(((a+b)//k*k+(a+b)%k)/k)*(z/k) +(a*b/k**2)
== (z/k)**2 +(((a+b)//k+(a+b)%k/k))*(z/k) +(a*b/k**2)
== (z/k)**2 +((a+b)//k)*(z/k) +((((a+b)%k) +a*b/z)/k)*(z/k)
== (z/k)**2 +((a+b)//k)*(z/k) +(((((a+b)%k) +a*b/z)//k) +((((a+b)%k) +a*b/z)%k/k))*(z/k)
== (z/k)**2 +((a+b)//k +((((a+b)%k) +a*b/z)//k))*(z/k) +((((a+b)%k) +a*b/z)%k/k)*(z/k)
== (z/k)**2 +(Q1 +((R1 +Q0*k+R0)//k))*(z/k) +((R1 +R0)%k/k)*(z/k)
== (z/k)**2 +(Q1+Q0 +((R1+R0)//k))*(z/k) +((R1+R0)%k/k)*(z/k)
  # => ((R1+R0)%k)
== (z/k)**2 +((a+b+a*b/z)//k)*(z/k) +((R1+R0)%k/k)*(z/k)
k++:
== (z/(k+1))**2 +((a+b)//(k+1) +((((a+b)%(k+1)) +a*b/z)//(k+1)))*(z/(k+1)) +((((a+b)%(k+1)) +a*b/z)%(k+1)/(k+1))*(z/(k+1))

]
假设:
  假设:[N/k**2 == (z/k)**2 +d0*(z/k) +c0]
  假设:[N/(k+1)**2 == (z/(k+1))**2 +d1*(z/(k+1)) +c1]
  假设:[d==d0==d1]
  假设:[(a+b)//k == (a+b)//(k+1) +p01][p01 :<- {0,1}]
  假设:[(a*b/z)//k == (a*b/z)//(k+1) +q01][q01 :<- {0,1}]
  假设:[(((a+b)%k) +a*b/z)%k +s01*k == (a+b)%k +(a*b/z)%k][s01 :<- {0,1}]
  假设:[(((a+b)%(k+1)) +a*b/z)%(k+1) +t01*(k+1) == (a+b)%(k+1) +(a*b/z)%(k+1)][t01 :<- {0,1}]
  ==>>:
  [[p01==0] -> [(a+b)%(k+1) == (a+b)%k -(a+b)//k]] # !! f001
  [[p01==1] -> [(a+b)%(k+1) == (a+b)%k -(a+b)//k +(k+1)]] # !! f002
  ==>>:
  [(a+b)%(k+1) == (a+b)%k -(a+b)//k +p01*(k+1)]
  [(a*b/z)%(k+1) == (a*b/z)%k -(a*b/z)//k +q01*(k+1)]

  [d == ((a+b)//k +((((a+b)%k) +a*b/z)//k))]
  [c0*k**2/z == (((a+b)%k) +a*b/z)%k]
  [c1*(k+1)**2/z == (((a+b)%(k+1)) +a*b/z)%(k+1)]

  [c1*(k+1)**2/z
  == (((a+b)%(k+1)) +a*b/z)%(k+1)
  !! 假设
  == (a+b)%(k+1) +(a*b/z)%(k+1) -t01*(k+1)
  !! 假设
  == (a+b)%k -(a+b)//k +p01*(k+1) +(a*b/z)%k -(a*b/z)//k +q01*(k+1) -t01*(k+1)
  == (a+b)%k -(a+b)//k +(a*b/z)%k -(a*b/z)//k +(p01+q01-t01)*(k+1) +q01*(k+1)
  ]
  [c1*(k+1)**2/z == (a+b)%k -(a+b)//k +(a*b/z)%k -(a*b/z)//k +(p01+q01-t01)*(k+1)]

  [c0*k**2/z
  == (((a+b)%k) +a*b/z)%k
  !! 假设
  == (a+b)%k +(a*b/z)%k -s01*k
  ]
  [c0*k**2/z == (a+b)%k +(a*b/z)%k -s01*k]

  [c0*k**2/z -c1*(k+1)**2/z
  == (a+b)%k +(a*b/z)%k -s01*k
  - ((a+b)%k -(a+b)//k +(a*b/z)%k -(a*b/z)//k +(p01+q01-t01)*(k+1))
  == (a+b)//k +(a*b/z)//k +(s01 -(p01+q01+s01-t01)*(k+1))
  ]
  [c0*k**2/z -c1*(k+1)**2/z == (a+b)//k +(a*b/z)//k +(s01 -(p01+q01+s01-t01)*(k+1))]



  !! [c0*k**2/z -c1*(k+1)**2/z == (a+b)//k +(a*b/z)//k +(s01 -(p01+q01+s01-t01)*(k+1))]
  !! [c0*k**2/z == (a+b)%k +(a*b/z)%k -s01*k]
  ==>>:
  [Q1:=(a+b)//k]
  [R1:=(a+b)%k]
  [Q0:=(a*b/z)//k]
  [R0:=(a*b/z)%k]
  [K1:=c0*k**2/z -c1*(k+1)**2/z]
  [K0:=c0*k**2/z]
  [G1:=-(s01 -(p01+q01+s01-t01)*(k+1))]
  [G0:=+s01*k]

  [K1+G1 == Q1+Q0]
  [K0+G0 == R1+R0]
  [a+b == Q1*k+R1]
  [a*b/z == Q0*k+R0]
    这里k足够大，则[Q0==0]
    [k ~ z]???

  !! [N == (z+a)*(z+b)]
  [N/z-z == (a+b) +a*b/z]
  [X1:=a+b]
  [X0:=a*b/z]
  [M:=N/z-z]
  ==>>:
  [M == X1+X0]
  [X1 == Q1*k+R1]
  [X0 == Q0*k+R0]

  已知:M,k,K0,K1;枚举:G1,G0,?Q0?
    六个未知变量:Q1,Q0,R1,R0,X1,X0#a,b
    bug:六个等式！感觉可以！
    实际上只有4.5个等式:
    [K1+G1 == Q1+Q0]
    [K0+G0 == R1+R0]
    [X1 == Q1*k+R1]
    [X0 == Q0*k+R0]
    #冗余:[M == X1+X0]
      # << [X1+X0 == (Q1+Q0)*k+(R1+R0) == (a+b) +a*b/z == M]
    ++假设:[Q0 == 0]#或枚举{-1,0,+1}
      #<<==k足够大

    ==>>:
    [Q1 == K1+G1-Q0]
    []

[q == u//k][q-1 == u//(k+1)]:
  [u == q*k +r]
  [u == (q-1)*(k+1) +(r-q+k+1)] #f002
  要求:[k+1>=q]
    即:[u < (k+1)**2]
    即:[k >= floor_sqrt(u)]
  希望:
    [(a+b)//k - (a+b)//(k+1) <= 1]
    [(a*b/z)//k - (a*b/z)//(k+1) <= 1]
      要求:[k >= floor_sqrt(a*b/z)]
        <<== [k>=floor_sqrt(z)]
        [z ~ N**/2]
        [k ~>~ N**/4]
[q == u//k == u//(k+1)]:
  [u == q*k +r]
  [u == q*(k+1) +(r-q)] #f001
  [u%(k+1) == u%k -u//k]
  [r >= q]
    当q远小于k时高概率成立
    即 当u远小于k**2时高概率成立
  希望:
    [(a+b)//k == (a+b)//(k+1)]
    [(a*b/z)//k == (a*b/z)//(k+1)]
      这里要求:(a*b/z)远小于k**2
      [z ~ N**/2]
      [a*b ~ N]
      [a*b/z ~ N**/2]
      [k**2 ~>>~ N**/2]
      [k ~>>~ N**/4]
      只需k远大于N**/4

[k:=N][a+b < N==k]:
  [1/N
  == N/N**2
  == N/k**2
  == (z/k)**2 +((a+b)//k)*(z/k) +((((a+b)%k) +a*b/z)/k)*(z/k)
  == (z/k)**2 +(a+b +a*b/z)*(z/k**2)
    还原，无用
  ]

[(abs(a)+1)*(abs(b)+1) < k**2]:
e script/整数分解牜两位数乘法.py
===
]]
]

'#'; __doc__ = r'#'
>>>



py_adhoc_call   script.整数分解牜两位数乘法   @f
from script.整数分解牜两位数乘法 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from fractions import Fraction
from math import isqrt
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


def print_eq(*args, sep='=', **kwds):
    print(*args, sep='=', **kwds)
def print_eqs(nm2v, nms, /):
    for nm in nms.split():
        print_eq(nm, nm2v[nm])


def rational2two_digits_(radix, fr, /):
    (d1, d0) = divmod(fr-radix**2, radix)
    return (d1, d0)
def __():
    xxx = False
    z = 35678987467
    a = -746778567
    b = +999746778567
    N = (z+a)*(z+b)
    r2 = isqrt(N)
    r4 = isqrt(r2)
    k = 13*r4
    k = z+10*r4
    k=z+1#35678551368
    print_eqs(locals(), 'N z a b r2 r4 k')
    z = Fraction(z)
    k0 = Fraction(k)
    k1 = 1+k0
    (d0, c0) = rational2two_digits_(z/k0, N/(k0**2))
    (d1, c1) = rational2two_digits_(z/k1, N/(k1**2))
    print_eqs(locals(), 'd0 c0 d1 c1')
    assert d0 == d1
    777;d = d0 = d1
    assert (a+b)//k0 == (a+b)//k1
    assert (a*b/z)//k0 == (a*b/z)//k1
    assert (_0:=((((a+b)%k0) +a*b/z)%k0)) == (_1:=((a+b)%k0 +(a*b/z)%k0)) or _0 == _1-k0, (_0, _1, _1-_0, (_1-_0)%1)
        # ^AssertionError: (Fraction(100490085207827511, 35678987467), Fraction(256086149551414511, 35678987467), Fraction(4361000, 1), Fraction(0, 1))
    if xxx:assert _0 == _1
    assert (_0:=((((a+b)%k1) +a*b/z)%k1)) == (_1:=((a+b)%k1 +(a*b/z)%k1)) or _0 == _1-k1, (_0, _1, _1-_0, (_1-_0)%1)
    if xxx:assert _0 == _1

    if xxx:
        assert d == ((a+b)//k +((((a+b)%k) +a*b/z)//k))
        assert c0*k**2/z == (((a+b)%k) +a*b/z)%k
        assert c1*(k+1)**2/z == (((a+b)%(k+1)) +a*b/z)%(k+1)


        assert c0*k**2/z -c1*(k+1)**2/z == (a+b)//k +(a*b/z)//k
        assert c0*k**2/z == (a+b)%k +(a*b/z)%k


    Q1 = (a+b)//k
    R1 = (a+b)%k
    Q0 = (a*b/z)//k
    R0 = (a*b/z)%k
    K1 = c0*k**2/z -c1*(k+1)**2/z
    K0 = c0*k**2/z

    if xxx:
        #已知:N,z,k,d,K0,K1
        #六个未知变量:Q1,Q0,R1,R0,a,b
        assert K1 == Q1 +Q0
        assert K0 == R1 +R0
        assert a+b == Q1*k+R1
        assert a*b/z == Q0*k+R0
        assert d == Q1+Q0
        assert N == (z+a)*(z+b)


    X1 = a+b
    X0 = a*b/z
    M = N/z-z
    if xxx:
        #已知:M,z,k,d,K0,K1
        #六个未知变量:Q1,Q0,R1,R0,X1,X0#a,b
        assert K1 == Q1 +Q0
        assert K0 == R1 +R0
        assert X1 == Q1*k +R1
        assert X0 == Q0*k +R0
        assert d  == Q1 +Q0
        assert M  == X1 +X0 #冗余！！

        assert K1 == d #冗余！！
    print_eqs(locals(), 'M z k d K1 K0')
    print_eqs(locals(), 'Q1 Q0 R1 R0 X1 X0')
    assert Q0 == 0
__()

__all__
from script.整数分解牜两位数乘法 import *
