#__all__:goto
r'''[[[
e script/尝试冫整数分解牜阶乘差.py

script.尝试冫整数分解牜阶乘差
py -m nn_ns.app.debug_cmd   script.尝试冫整数分解牜阶乘差 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.尝试冫整数分解牜阶乘差:__doc__ -ht # -ff -df

[[
整数分解牜阶乘差
  [i,j:<-[1..<4*ln(p)]]:
    (i!%p)
    ((i!-j!)%p)

[4*N.bit_length()**2 <= sqrt(N)]
    <==> [(4*N.bit_length()**2)**2 <= N]
    <==> [(4*(1+floor_log2(N)**2))**2 <= N]
    <==> [N >= 4477456]
]]

>>> from bisect import bisect_right
>>> f = lambda N:(4*N.bit_length()**2)**2 <= N
>>> bisect_right(range(1<<31), False, key=f)
4477456
>>> f(4477456-1)
False
>>> f(4477456)
True
>>> g = lambda N:N - (4*N.bit_length()**2)**2
>>> g(4477456-1)
-1
>>> g(4477456)
0
>>> bin(4477456)
'0b10001000101001000010000'
>>> hex(4477456)
'0x445210'
>>> (4477456).bit_length()
23
>>> 4*(4477456).bit_length()**2
2116
>>> (4*23**2)**2 == 2116**2 == 4477456
True

$ next_pseudoprime =4477456
4477457
$ next_pseudoprime =4477458
4477463
$ next_pseudoprime ='2**28'
268435459
$ next_pseudoprime ='2**32'
4294967311

[[[
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   ,枚举冫阶乘模扌 =7
===
1:1
2:2
3:6
4:3
5:1
6:6
7:0
===
]]]
[[[
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   ,枚举冫阶乘模扌 =41
===
1:1
2:2
3:6
4:24
5:38
6:23
7:38
8:17
9:30
10:13
11:20
12:35
13:4
14:15
15:20
16:33
17:28
18:12
19:23
20:9
21:25
22:17
23:22
24:36
25:39
26:30
27:31
28:7
29:39
30:22
31:26
32:12
33:27
34:16
35:27
36:29
37:7
38:20
39:1
40:40
41:0
===
]]]
[[[
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   ,枚举冫阶乘模牜直到出现重复项扌 =97
===
1:1
2:2
3:6
4:24
5:23
6:41
7:93
8:65
9:3
10:30
11:39
12:80
13:70
14:10
15:53
16:72
17:60
18:13
19:53
===
]]]
[[[
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   ,枚举冫阶乘模牜直到出现重复项扌 =4477457 > /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp
===
1:1
2:2
3:6
... ...
... ...
1170:2298553
... ...
... ...
3298:2298553
===
[3298-1170==2128 > sqrt_(4477457) > 2116]
===
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   @求冫序号辻重复项纟第一对牜阶乘模扌 =4477457
(1170, 3298, -2128, 2298553)
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   @求冫序号辻重复项纟第一对牜阶乘模扌 =4477457 +with_log_diff_N
(1170, 3298, -2128, 2298553, 1.9985240789046823)
===
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   @求冫序号辻重复项纟第一对牜阶乘模扌 =4477463 +with_log_diff_N
(1102, 2313, -1211, 678682, 2.157223826361937)
===
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   @求冫序号辻重复项纟第一对牜阶乘模扌 =268435459 +with_log_diff_N
(382, 26250, -25868, 50427731, 1.9101048856725784)
===
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   @求冫序号辻重复项纟第一对牜阶乘模扌 =4294967311 +with_log_diff_N
(1769, 70660, -68891, 4287748910, 1.9910368626323691)
===
综上:类似于:尸方法(rho_method):随机行走O(sqrt_(N))
===
]]]
[[[
++may_start5N_
===
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   @求冫序号辻重复项纟第一对牜阶乘模扌 --may_start5N_:isqrt +with_log_diff_N  =4477457
(854, 1418, -564, 1301557, 2.4174324640828466)
===
py_adhoc_call { +lineno }  script.尝试冫整数分解牜阶乘差   ,枚举冫序号辻重复项纟第一对牜阶乘模扌 --may_start5N_:isqrt +with_log_diff_N  ='[4477457,4477463,268435459,4294967311]'
1:(4477457, (854, 1418, -564, 1301557, 2.4174324640828466))
2:(4477463, (100, 3673, -3573, 2340365, 1.8719308194904483))
3:(268435459, (6520, 17203, -10683, 118349172, 2.092201963663871))
4:(4294967311, (71484, 111902, -40418, 925570096, 2.0911328351520035))
===
综上:类似于:尸方法(rho_method):随机行走O(sqrt_(N))
===
]]]



from script.尝试冫整数分解牜阶乘差 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from math import log2, log, isqrt
#.from itertools import islice
___end_mark_of_excluded_global_names__0___ = ...


def 枚举冫序号辻重复项纟第一对牜阶乘模扌(Ns, /, *, with_log_diff_N=False, **kwds0):
    'Iter N/int{>=2} -> Iter (N, (serial_number0{>=1}, serial_number1{>serial_number0}, neg_diff{==serial_number0-serial_number1}, factorial_residue{==(serial_number0!%N)==(serial_number1!%N)})/(pint, pint, neg_int, uint%N))'
    check_type_is(bool, with_log_diff_N)
    for N in Ns:
        t = 求冫序号辻重复项纟第一对牜阶乘模扌(N, with_log_diff_N=with_log_diff_N, **kwds0)
        yield (N, t)
    return

def 求冫序号辻重复项纟第一对牜阶乘模扌(N, /, *, with_log_diff_N=False, **kwds0):
    'N/int{>=2} -> (serial_number0{>=1}, serial_number1{>serial_number0}, neg_diff{==serial_number0-serial_number1}, factorial_residue{==(serial_number0!%N)==(serial_number1!%N)})/(pint, pint, neg_int, uint%N)'
    check_type_is(bool, with_log_diff_N)
    check_int_ge(2, N)
    r2j = {}
    for j, r in 枚举冫阶乘模牜直到出现重复项扌(N, with_serial_number=True, **kwds0):
        r2j.setdefault(r, j)
    j0 = 1+r2j[r]
    j1 = 1+j
    assert 1 <= j0 < j1
    neg_diff = j0-j1
    if with_log_diff_N:
        log_diff_N = log(N,-neg_diff) # == log_(diff; N)
        return (j0, j1, neg_diff, r, log_diff_N)
    return (j0, j1, neg_diff, r)
def 枚举冫阶乘模牜直到出现重复项扌(N, /, *, with_serial_number=False, **kwds0):
    'N/int{>=2} -> (Iter uint%N)'
    check_int_ge(2, N)
    check_type_is(bool, with_serial_number)
    b = bool(with_serial_number)
    it = 枚举冫阶乘模扌(N, may_sz:=N+1, **kwds0)
    rs = set()
    for j, r in enumerate(it):
        assert len(rs) == j
        if b:
            yield (j, r)
        else:
            yield r
        rs.add(r)
        if len(rs) == j:
            break
    else:
        raise 000

_d4start = dict(isqrt=isqrt)
def _start5N_kwds0(N, /, *, may_start=None, may_start5N_=None):
    if not may_start is None:
        start = may_start
    elif not may_start5N_ is None:
        if type(may_start5N_) is str:
            nm = may_start5N_
            start5N_ = _d4start[nm]
        else:
            start5N_ = may_start5N_
            assert callable(start5N_)
        start5N_
        start = start5N_(N)
    else:
        start = 1
    start
    check_int_ge(1, start)
    check_int_ge(start, N)
    return start
#def 枚举冫阶乘模扌(N, may_sz=None, /, *, may_start=None, may_start5N_=None):
def 枚举冫阶乘模扌(N, may_sz=None, /, **kwds0):
    'N/int{>=2} -> may sz/pint{default:=min(N, 4*N.bit_length()**2)} -> (Iter uint%N){len=sz}'
    check_int_ge(2, N)
    start = _start5N_kwds0(N, **kwds0)
    sz = min(N+1-start, 4*N.bit_length()**2) if may_sz is None else may_sz
    check_int_ge(1, sz)
    r = 1
    for j in range(start, start+sz):
        r *= j
        r %= N
        yield r

__all__
from script.尝试冫整数分解牜阶乘差 import *
