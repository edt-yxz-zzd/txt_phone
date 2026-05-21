#__all__:goto
#?bug?:不止四个候选
#TODO:最小化(s**2+t**2)，不考虑zz
r'''[[[
e script/整数分解牜平方根环.py

script.整数分解牜平方根环
py -m nn_ns.app.debug_cmd   script.整数分解牜平方根环 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.整数分解牜平方根环:__doc__ -ht # -ff -df
#######

[[
[z := (_z**2%N-N)][(g+z*h) == gcd(_z+z*1, (N+z*0))]:
    [p*q == N == (g+z*h)*(u+z*v)]
    [g*v+h*u == 0]
    [p*q == N == (g-z*h)*(u-z*v)]
    [p**2*q**2 == N**2 == (g+z*h)*(u+z*v)*(g-z*h)*(u-z*v)]
    [p**2*q**2 == N**2 == (g+z*h)*(g-z*h) * (u+z*v)*(u-z*v)]
    [p**2*q**2 == N**2 == (g**2-zz*h**2) * (u**2-zz*v**2)]
    [(g**2-zz*h**2) <- {1,p,q,N}]

]]

[[
整数分解:平方根环
view ../../python3_src/seed/math/GaussInteger.py
e script/整数分解牜平方根环.py
[x**2%N==y]
[x**2-y==u*N]
[(x-sqrtY)*(x+sqrtY) == u*N]
[gcd((x+sqrtY),N) == ??]
[z:=sqrtY]
[z**2==y]
divmod:
  (a+b*z)/%(c+d*z)
  (a+b*z)*(c-d*z)/%((c+d*z)*(c-d*z))
  (a+b*z)*(c-d*z)/%((c+d*z)*(c-d*z))
  (a+b*z)*(c-d*z)/%((c**2-d**2*y))
  ((a*c-b*d*y)+(c*b-a*d)*z)/%((c**2-d**2*y))
  ((a*c-b*d*y)/%((c**2-d**2*y)) +(c*b-a*d)/%((c**2-d**2*y))*z)
  但是，是否绝对值下降？
  以最小化余数绝对值为目标进行除法:
  [(s+t*z) == (a+b*z) -(c+d*z)*(p+q*z)]
  [s == a -(c*p+d*q*zz)]
  [t == b -(c*q+d*p)]
  [abs(R)**2 == (s+t*z)*(s-t*z) == (s**2-t**2*zz)]
  找出(p+q*z)使得(s**2-t**2*zz)最小
    要求: [zz < 0]
  最小化余数<==>最小化(s**2-t**2*zz)
  不如直接让s,t为零，然后比较?bug?!四个候选值
    ?bug? !! 不止四个候选
  [0 == s0 == a -(c*p0+d*q0*zz)]
  [0 == t0 == b -(c*q0+d*p0)]

  [d*p0 == (b -c*q0)]

  [a == (c*p0+d*q0*zz)]
  [d*a == (c*d*p0 +d**2*q0*zz)]
  !! [d*p0 == (b -c*q0)]
  [d*a == (c*(b -c*q0) +d**2*q0*zz)]
  [d*a == (c*b -c**2*q0 +d**2*q0*zz)]
  [d*a -c*b == (-c**2 +d**2*zz)*q0]
  [q0 == (c*b -d*a)/(c**2 -zz*d**2)]

  [d*p0 == (b -c*q0)
  == b -c*(c*b -d*a)/(c**2 -zz*d**2)
  == ((b*c**2 -zz*b*d**2) -(c**2*b -c*d*a))/(c**2 -zz*d**2)
  == d*(c*a -zz*b*d)/(c**2 -zz*d**2)
  ]
  [p0 == (c*a -zz*b*d)/(c**2 -zz*d**2)]

  ==>>:
  [p0 == (c*a -zz*b*d)/(c**2 -zz*d**2)]
  [q0 == (c*b -d*a)/(c**2 -zz*d**2)]
  [(p0 +z*q0)*(c**2 -zz*d**2) == (c*a -zz*b*d) +z*(c*b -d*a)]
  [(p0 +z*q0)*(c +z*d)*(c -z*d) == (a +z*b)*(c -z*d)]
不止四个候选，到底有多少？
  [0 == s0 == a -(c*p0+d*q0*zz)]
  [0 == t0 == b -(c*q0+d*p0)]
  [p0 == (c*a -zz*b*d)/(c**2 -zz*d**2)]
  [q0 == (c*b -d*a)/(c**2 -zz*d**2)]
  #p0,q0不是整数，微调p0,q0:
  [qy := (q0+dy)]
  [px := (p0+dx)]
  [sw == a -(c*(p0+dx)+d*(q0+dy)*zz)]
  [tw == b -(c*(q0+dy)+d*(p0+dx))]

  [sw == -(c*dx+d*dy*zz)]
  [tw == -(c*dy+d*dx)]

  [dx:=-(d/c)*zz*dy]:
    [tw == -(c*dy+d*-(d/c)*zz*dy)]
    [tw == -c*dy*(1-(d/c)**2*zz)]

  [(sw**2 -zz*tw**2)
  == (c*dx+d*dy*zz)**2 -zz*(c*dy+d*dx)**2
  == (c**2*dx**2 +d**2*dy**2*zz**2 +(2*c*dx*d*dy*zz))
  -  (zz*c**2*dy**2 +zz*d**2*dx**2 +(zz*2*c*dy*d*dx))
  == (c**2*dx**2 +d**2*dy**2*zz**2)
  -  (zz*c**2*dy**2 +zz*d**2*dx**2)
  == (c**2 -zz*d**2)*(dx**2 -zz*dy**2)
  ]
  最小化(sw**2 -zz*tw**2)
    <==> 最小化(dx**2 -zz*dy**2)
    !! [zz < 0]
    <==> 分别最小化(dx**2),(dy**2)
    这么说，『四个候选值』没毛病？

[(a+z*b)/(c+z*d) == (p0+z*q0)]:
    [(a+z*b) == (c+z*d) * (p0+z*q0)]
    [(a+z*b) == (c+z*d) * (px+z*qy) +(sw+z*tw)]
    [0 == (c+z*d) * (dx+z*dy) +(sw+z*tw)]
    [(sw+z*tw) == -(c+z*d) * (dx+z*dy)]
    [len (sw+z*tw) == len (c+z*d) * len (dx+z*dy)]
    最小化(sw**2 -zz*tw**2)
        <==> 最小化(dx**2 -zz*dy**2)
        !! [zz < 0]
        <==> 分别最小化(dx**2),(dy**2)



TODO:最小化(abs(sw)+abs(tw))，不考虑zz
TODO:最小化(sw**2 +tw**2)，不考虑zz
TODO:最小化(sw**2 -ww*tw**2)，[ww < 0]，不考虑zz
    [(sw+z*tw) == -(c+z*d) * (dx+z*dy)]
    [sw == -(c*dx+zz*d*dy)]
    [tw == -(c*dy+d*dx)]
    [sw**2 -ww*tw**2
    == (c*dx+zz*d*dy)**2 -ww*(c*dy+d*dx)**2
    == (c**2*dx**2 +zz**2*d**2*dy**2) +(2*c*dx*zz*d*dy)
    +  -ww*(c**2*dy**2 +d**2*dx**2) -ww*(2*c*dy*d*dx)
    == (2*c*d*dx*dy)*(zz-ww)
    +  dx**2*(c**2 -ww*d**2)
    +  dy**2*(-ww*c**2 +zz**2*d**2)
    ]
    [dx == -(c*d*dy)*(zz-ww)/(c**2 -ww*d**2)]
    [dy == -(c*d*dx)*(zz-ww)/(-ww*c**2 +zz**2*d**2)]
===
]]
[[
死循环:
    zz=-27
    ab=(-37, -44)
    cd=(175, 1)

cd
    (175, 1)
z*ab
    (1188, -37)
z*cd
    (-27, 175)
ab
    (-37, -44)

ab+cd
    (138, -43)
ab-cd
    (-212, -45)
ab+z*cd
    (-64, 131)
ab-z*cd
    (-10, -219)

x*(1,1) +y*(-27,1)
(x-27*y, x+y)


(a+z*b)的生成点阵有多稀疏？
(a+z*b)*(1+z*0)
    (a,b)
(a+z*b)*(0+z*1)
    (zz*b,a)

要求:
    @ab. [len ab > 1/2 * len (ab + z*ab)]
    @ab. [len ab > 1/2 * len (ab * (1,1))]
    @ab. [len ab > 1/2 * len (a+zz*b, a+b)]
    @ab. [(a**2 -zz*b**2) > 1/4 * ((a+zz*b)**2 -zz*(a+b)**2)]
    @ab. [(4*a**2 -4*zz*b**2) > ((a**2+zz**2*b**2) +(2*a*zz*b) -zz*(a**2+b**2) -(zz*2*a*b))]
    @ab. [(3*a**2 -3*zz*b**2) > (-zz*a**2 +zz**2*b**2)]
    [3 > -zz][-3*zz > zz**2]
    [-3 < zz < 0]
    [zz <- {-2, -1}]
    可否考虑分数？
    可否考虑其他多项式？
        ZZ%(X**2-zz) --> ZZ%(X**2-u*X+v)
        ZZ%(X**2-zz) --> ZZ%(X**3-u*X+v)
]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   script.整数分解牜平方根环   @try1_
    using:_ver1__divmod4sqrt_ring_:未最小化余数
    try1_使用 [zz > 0]
N=7663
zz=648
ab=(233, 1)
cd=(7663, 0)
zz=648
ab=(233, 1)
cd=(7663, 0)
######### 0 #########
ab=(233, 1)
cd=(7663, 0)
Q=(0, 0)
R=(233, 1)
######### 1 #########
ab=(7663, 0)
cd=(233, 1)
Q=(33, -1)
R=(622, 200)
######### 2 #########
ab=(233, 1)
cd=(622, 200)
Q=(-1, 0)
R=(855, 201)
######### 3 #########
ab=(622, 200)
cd=(855, 201)
Q=(1, -1)
R=(130015, 854)
######### 4 #########
ab=(855, 201)
cd=(130015, 854)
Q=(-1, 0)
R=(130870, 1055)

]]
[[
py_adhoc_call   script.整数分解牜平方根环   @try2_
    using:_ver1__divmod4sqrt_ring_:未最小化余数
    try2_使用 [zz < 0]
N=7663
zz=-7015
ab=(233, 1)
cd=(7663, 0)
zz=-7015
ab=(233, 1)
cd=(7663, 0)
######### 0 #########
ab=(233, 1)
cd=(7663, 0)
Q=(0, 0)
R=(233, 1)
######### 1 #########
ab=(7663, 0)
cd=(233, 1)
Q=(29, -1)
R=(-6109, 204)
######### 2 #########
ab=(233, 1)
cd=(-6109, 204)
Q=(0, -1)
R=(-1430827, -6108)
######### 3 #########
ab=(-6109, 204)
cd=(-1430827, -6108)
Q=(0, -1)
R=(42841511, -1430623)
######### 4 #########
ab=(-1430827, -6108)
cd=(42841511, -1430623)
Q=(0, -1)
R=(10034389518, 42835403)
]]
[[
py_adhoc_call   script.整数分解牜平方根环   @try3_  -big_remainder_ok
    using:_ver2__divmod4sqrt_ring_:最小化余数
    try3_使用 [zz < 0]
N=7663
zz=-7015
ab=(233, 1)
cd=(7663, 0)
zz=-7015
ab=(233, 1)
cd=(7663, 0)
######### 0 #########
ab=(233, 1)
cd=(7663, 0)
Q=(0, 0)
R=(233, 1)
raise Exception(sf.zz, ab, cd, QRs, sign)
Exception: (-7015, (7663, 0), (233, 1), [((29, 0), (906, -29))], 1)
]]
[[
+big_remainder_ok
py_adhoc_call   script.整数分解牜平方根环   @try3_  +big_remainder_ok
    using:_ver2__divmod4sqrt_ring_:最小化余数
    try3_使用 [zz < 0]
    最终:死循环
N=7663
zz=-7015
ab=(233, 1)
cd=(7663, 0)
zz=-7015
ab=(233, 1)
cd=(7663, 0)
######### 0 #########
ab=(233, 1)
cd=(7663, 0)
Q=(0, 0)
R=(233, 1)
######### 1 #########
ab=(7663, 0)
cd=(233, 1)
Q=(29, 0)
R=(906, -29)
######### 2 #########
ab=(233, 1)
cd=(906, -29)
Q=(0, 0)
R=(233, 1)
######### 3 #########
ab=(906, -29)
cd=(233, 1)
Q=(0, 0)
R=(906, -29)
### dead_loop ###
]]
[[
+big_remainder_ok
try4_
py_adhoc_call   script.整数分解牜平方根环   @try4_  +big_remainder_ok
    using:_ver2__divmod4sqrt_ring_:最小化余数
    [-zz > _z == floor_sqrt(N)] 导致 gcd超大
        希望:[-zz < floor_sqrt(N)]
N=7663
_z=87
zz=-94
ab=(87, 1)
cd=(7663, 0)
zz=-94
ab=(87, 1)
cd=(7663, 0)
######### 0 #########
ab=(87, 1)
cd=(7663, 0)
Q=(0, 0)
R=(87, 1)
######### 1 #########
ab=(7663, 0)
cd=(87, 1)
Q=(87, -1)
R=(0, 0)
### found_gcd ###
_gcd=(87, 1)
_gcdXgcd=7663
N=7663
_z=87
zz=-94
ab=(87, 1)
cd=(7663, 0)
_gcd=(87, 1)
_gcdXgcd=7663
g=7663
]]
[[
+big_remainder_ok
try5_
py_adhoc_call   script.整数分解牜平方根环   @try5_  +big_remainder_ok
    using:_ver2__divmod4sqrt_ring_:最小化余数
    [-zz < floor_sqrt(N) == h]
    最终:死循环
N=7663
h=87
_z=175
zz=-27
ab=(175, 1)
cd=(7663, 0)
zz=-27
ab=(175, 1)
cd=(7663, 0)
######### 0 #########
ab=(175, 1)
cd=(7663, 0)
Q=(0, 0)
R=(175, 1)
######### 1 #########
ab=(7663, 0)
cd=(175, 1)
Q=(44, 0)
R=(-37, -44)
######### 2 #########
ab=(175, 1)
cd=(-37, -44)
Q=(0, 0)
R=(175, 1)
######### 3 #########
ab=(-37, -44)
cd=(175, 1)
Q=(0, 0)
R=(-37, -44)
### dead_loop ###
N=7663
h=87
_z=175
zz=-27
ab=(175, 1)
cd=(7663, 0)
_ab=(175, 1)
_cd=(-37, -44)
_abXab=30652
_cdXcd=53641
g0=7663
g1=7663
]]
[[
]]
[[
]]










from script.整数分解牜平方根环 import *
]]]'''#'''
__all__ = r'''
IOps4sqrt_ring
    Ops4sqrt_ring
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from abc import ABC, abstractmethod
from seed.debug.print_local_variables import print_eqs, print_eq
    #print_eqs(locals(), 'd0 c0 d1 c1')
from seed.math.sign_of import sign_of
from itertools import product
from math import isqrt as floor_sqrt, gcd
___end_mark_of_excluded_global_names__0___ = ...


def __():
    def conjugate4sqrt_ring_(zz, ab, /):
        (a, b) = ab
        return (a, -b)
    def neg4sqrt_ring_(zz, ab, /):
        (a, b) = ab
        return (-a, -b)

    def add4sqrt_ring_(zz, ab, cd, /):
        (a, b) = ab
        (c, d) = cd
        return (a+c, b+d)
    def sub4sqrt_ring_(zz, ab, cd, /):
        return add4sqrt_ring_(zz, ab, neg4sqrt_ring_(zz, cd))
    def mul4sqrt_ring_(zz, ab, cd, /):
        (a, b) = ab
        (c, d) = cd
        r'''[[[
        (a+b*z)*(c+d*z)
        (a*c+b*d*zz) +(a*d+c*b)*z
        #]]]'''#'''
        return ((a*c+b*d*zz), (a*d+c*b))
    def square_len4sqrt_ring_(zz, ab, /):
        match mul4sqrt_ring_(zz, ab, conjugate4sqrt_ring_(zz, ab)):
            case (ss, 0):
                return ss
        raise 000

    def _ver1__divmod4sqrt_ring_(zz, ab, cd, /):
        (a, b) = ab
        (c, d) = cd
        r'''[[[
        (a+b*z)/%(c+d*z)
        (a+b*z)*(c-d*z)/%((c+d*z)*(c-d*z))
        (a+b*z)*(c-d*z)/%((c+d*z)*(c-d*z))
        (a+b*z)*(c-d*z)/%((c**2-d**2*y))
        ((a*c-b*d*y)+(c*b-a*d)*z)/%((c**2-d**2*y))
        ((a*c-b*d*y)/%((c**2-d**2*y)) +(c*b-a*d)/%((c**2-d**2*y))*z)
        #]]]'''#'''
        ss = square_len4sqrt_ring_(zz, cd)
        mn = mul4sqrt_ring_(zz, ab, conjugate4sqrt_ring_(zz, cd))
        (m, n) = mn
        (q_, r_) = divmod(m, ss)
        (_q, _r) = divmod(n, ss)
        Q = (q_, _q)
        #bug:R = (r_, _r) # !! 放大了 conj_(cd)
        R = sub4sqrt_ring_(zz, ab, mul4sqrt_ring_(zz, Q, cd))
        if not ab == add4sqrt_ring_(zz, R, mul4sqrt_ring_(zz, Q, cd)):
            print_eqs(locals(), 'zz ab cd ss mn Q R')
            assert ab == add4sqrt_ring_(zz, R, mul4sqrt_ring_(zz, Q, cd))
            raise 000
        return (Q, R)
    divmod4sqrt_ring_ = _ver1__divmod4sqrt_ring_
    def try1_():
        N = 97*79
        _z = 233
        zz = pow(_z, 2, N)
        ab = (_z, 1)
        cd = (N, 0)
        print_eqs(locals(), 'N zz ab cd')
        tries_ver1_(zz, ab, cd, k:=5)
    def try2_():
        N = 97*79
        _z = 233
        zz = pow(_z, 2, N) -N
        ab = (_z, 1)
        cd = (N, 0)
        print_eqs(locals(), 'N zz ab cd')
        tries_ver1_(zz, ab, cd, k:=5)


    def tries_ver1_(zz, ab, cd, k, /):
        print_eqs(locals(), 'zz ab cd')
        for j in range(k):
            (Q, R) = _ver1__divmod4sqrt_ring_(zz, ab, cd)
            print('#########', j, '#########')
            print_eqs(locals(), 'ab cd Q R')
            ab, cd = cd, R
    conjugate4sqrt_ring_
    neg4sqrt_ring_
    add4sqrt_ring_
    sub4sqrt_ring_
    mul4sqrt_ring_
    square_len4sqrt_ring_
    divmod4sqrt_ring_

class IOps4sqrt_ring(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def big_remainder_ok(sf, /):
        '-> bool#see:divmod_'
        raise 000
    @property
    @abstractmethod
    def zz(sf, /):
        '-> zz/int{<0} # [zz == z*z < 0] # cmp_len_ => [zz < 0]'
        raise 000
    def neg_(sf, ab, /):
        (a, b) = ab
        return (-a, -b)
    def conj_(sf, ab, /):
        (a, b) = ab
        return (a, -b)
    def add_(sf, ab, cd, /):
        (a, b) = ab
        (c, d) = cd
        return (a+c, b+d)
    def sub_(sf, ab, cd, /):
        return sf.add_(ab, sf.neg_(cd))
    def mul_(sf, ab, cd, /):
        (a, b) = ab
        (c, d) = cd
        r'''[[[
        (a+b*z)*(c+d*z)
        (a*c+b*d*zz) +(a*d+c*b)*z
        #]]]'''#'''
        return ((a*c+b*d*sf.zz), (a*d+c*b))
    def square_len_(sf, ab, /):
        match sf.mul_(ab, sf.conj_(ab)):
            case (ss, 0):
                return ss
        raise 000
    def cmp_len_(sf, ab, cd, /):
        return sign_of(sf.square_len_(ab) -sf.square_len_(cd))

    def divmod_(sf, ab, cd, /):
        '-> (Q, R)'
        #as:_ver2__divmod4sqrt_ring_
        #vs:_ver1__divmod4sqrt_ring_
        ss = sf.square_len_(cd)
        mn = sf.mul_(ab, sf.conj_(cd))
        (m, n) = mn
        (q_, r_) = divmod(m, ss)
        (_q, _r) = divmod(n, ss)
        if 0:
            Q = (q_, _q)
            #bug:R = (r_, _r) # !! 放大了 conj_(cd)
        qs_ = [q_, 1+q_] if r_ else [q_]
        _qs = [_q, 1+_q] if _r else [_q]
            #?bug?:不止四个候选
        QRs = []
        for Q in product(qs_, _qs):
            R = sf.sub_(ab, sf.mul_(Q, cd))
            QR = (Q, R)
            if not QRs:
                QRs = [QR]
                continue
            match sf.cmp_len_(R, QRs[0][1]):
                case -1:
                    #min
                    QRs = [QR]
                case 0:
                    QRs.append(QR)
                case 1:
                    pass
                case _:
                    raise 000
                #case
            #match
        #for
        QRs
        if not sf.big_remainder_ok:
            (Q, R) = QRs[0]
            match sf.cmp_len_(R, cd):
                case -1:
                    #ok
                    pass
                case (0 | 1) as sign:
                    #bad
                    raise Exception(sf.zz, ab, cd, QRs, sign)
                case _:
                    raise 000
                #case
            #match

        return QRs[0]

class Ops4sqrt_ring(IOps4sqrt_ring):
    def __init__(sf, big_remainder_ok, zz, /):
        assert zz < 0 # cmp_len_ => [zz < 0]
        sf._zz = zz
        sf._b = big_remainder_ok
    @property
    #@override
    def zz(sf, /):
        return sf._zz
    @property
    #@override
    def big_remainder_ok(sf, /):
        return sf._b
def tries_ver2_(big_remainder_ok, zz, ab, cd, k, /):
    print_eqs(locals(), 'zz ab cd')
    ops = Ops4sqrt_ring(big_remainder_ok, zz)
    abcd_set = {(ab, cd)}
    for j in range(k):
        if cd == (0, 0):
            print('### found_gcd ###')
            _gcd = ab
            _gcdXgcd = ops.square_len_(_gcd)
            print_eqs(locals(), '_gcd _gcdXgcd')
            return (True, (_gcd, _gcdXgcd))
            break
        (Q, R) = ops.divmod_(ab, cd)
        print('#########', j, '#########')
        print_eqs(locals(), 'ab cd Q R')
        ab, cd = cd, R
        abcd = (ab, cd)
        if abcd in abcd_set:
            print('### dead_loop ###')
            _abXab = ops.square_len_(ab)
            _cdXcd = ops.square_len_(cd)
            return (False, (ab, cd, _abXab, _cdXcd))
            break
        else:
            abcd_set.add(abcd)
    return None


def try3_(big_remainder_ok):
    N = 97*79
    _z = 233
    zz = pow(_z, 2, N) -N
    ab = (_z, 1)
    cd = (N, 0)
    print_eqs(locals(), 'N zz ab cd')
    tries_ver2_(big_remainder_ok, zz, ab, cd, k:=5)



def try4_(big_remainder_ok):
    N = 97*79
    _z = floor_sqrt(N)
    zz = pow(_z, 2, N) -N
    ab = (_z, 1)
    cd = (N, 0)
    print_eqs(locals(), nms:='N _z zz ab cd')
    m = tries_ver2_(big_remainder_ok, zz, ab, cd, k:=5)
    _post4try5_(locals(), nms, m)
    return
    if m:
        (_gcd, _gcdXgcd) = m
        g = gcd(N, _gcdXgcd)
        print_eqs(locals(), 'N _z zz ab cd _gcd _gcdXgcd g')

def try5_(big_remainder_ok):
    N = 97*79
    h = floor_sqrt(N)
    #_z=897,1138,2496,2582,3414:found_gcd:useless
    for _z in range(1+3907 or 3756 or 3716 or 3662 or 3519 or 3507 or 3414 or 3323 or 3233 or 3111 or 2902 or 2846 or 2793 or 2691 or 2671 or 2582 or 2496 or 2370 or 2344 or 2321 or 2276 or 2254 or 2000 or 1973 or 1811 or 1794 or 1766 or 1633 or 1470 or 1449 or 1425 or 1158 or 1138 or 897 or 753 or 574 or 339 or 175 or h, N):
        zz = pow(_z, 2, N) -N
        if -zz < h:break
    else:
        raise 000
    ab = (_z, 1)
    cd = (N, 0)
    print_eqs(locals(), nms:='N h _z zz ab cd')
    m = tries_ver2_(big_remainder_ok, zz, ab, cd, k:=50)
    _post4try5_(locals(), nms, m)
def _post4try5_(nm2v, nms, m, /):
    if m:print_eqs(nm2v, nms)
    N = nm2v['N']
    match m:
        case None:
            pass
        case (True, (_gcd, _gcdXgcd)):
            g = gcd(N, _gcdXgcd)
            print_eqs(locals(), '_gcd _gcdXgcd g')
        case (False, (_ab, _cd, _abXab, _cdXcd)):
            g0 = gcd(N, _abXab)
            g1 = gcd(N, _cdXcd)
            print_eqs(locals(), '_ab _cd _abXab _cdXcd g0 g1')
            pass
        case _:
            raise 000





__all__
from script.整数分解牜平方根环 import *
