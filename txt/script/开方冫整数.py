#__all__:goto
r'''[[[
e script/开方冫整数.py
view /storage/emulated/0/0my_files/book/math/fxtbook[Matters Computational][Algorithms for Programmers].pdf


script.开方冫整数
py -m nn_ns.app.debug_cmd   script.开方冫整数 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.开方冫整数:__doc__ -ht # -ff -df

[[
[x := sqrt(xx)]
牛顿迭代 需要 一次长除法每次迭代:
    [x[k+1] := (x[k] + xx/x[k])/2]

改用 零除法迭代 [x := xx*sqrt_inv(xx)] 无需长除法
    divisionless iteration
[z := sqrt_inv(xx)]
    [z == xx**(-1/2)]
    [xx*z == xx**(1/2)]
[x := xx*z]

second order correction:
[z[k+1] := z[k] + 1/2*z[k]*(1-xx*z[k]**2)]
    [t:=(1-xx*z[k]**2)][z[k+1] := z[k] + 1/2*z[k]*t]
[?err :=> [z[k] == z*(1+err)]]:
    [z[k+1]
    == z*(1+err) + z*(1+err)*(1-xx*(z*(1+err))**2)/2
    == z*(1+err) + z*(1+err)*(1-(1+err)**2)/2
    == z*(1+err)*(1-err-err**2/2)
    == z*(1-err**2 -(1+err)*err**2/2)
    == z*(1-3/2*err**2 -1/2*err**3)
    ]
    [abs(3/2*err**2) < abs(err)]
        <<== [abs(3/2*err) < 1]
        <<== [abs(err) < 2/3]

third order correction:
[z[k+1] := z[k] + 1/2*z[k]*(1-xx*z[k]**2) + 3/8*z[k]*(1-xx*z[k]**2)**2]
    [t:=(1-xx*z[k]**2)][z[k+1] := z[k] + 1/2*z[k]*t + 3/8*z[k]*t**2]

general form of the third order divisionless iteration for the e-th root of D is:
    [d := D*(D**(e-1))**(-1/e)]
        [d == D**(1/e)]
    [z := D**(-1/e)]
    [t:=(1-D*z[k]**e)][z[k+1] := z[k]*(1 + 1/e*t + (1+e)/(2*e**2)*t**2)]
[e==1]:
    !! [z := D**(-1/e)]
    [z == D**(-1) == 1/D]
    [t:=(1-D*z[k])][z[k+1] := z[k]*(1 + t + t**2)]
[?err :=> [z[k] == z*(1+err)]]:
    [t==(1-D*z*(1+err)) == -err]
    [z[k+1]
    * second order:
        == z*(1+err)*(1 + t)
        == z*(1+err)*(1 - err)
        == z*(1 - err**2)
    * third order:
        == z*(1+err)*(1 + t + t**2)
        == z*(1+err)*(1 - err + err**2)
        == z*(1 + err**3)
    ]

]]
[[
(a+2**e4a)*(b+2**e4b)
== a*b + b*2**e4a + a*2**e4b + 2**(e4a+e4b)
* [a==2**lbA][b==2**lbB][ez == lbB+e4a == lbA+e4b]:
    ... == a*b + 2**ez + 2**ez + 2**(e4a+e4b)
    == a*b + 2**(ez+1) + 2**(e4a+e4b)
    < a*b + 2**(ez+2)
[e4ab == 2+ez]
[e4ab == 2+max(lbB+e4a, lbA+e4b)]
[e4ab
== 2+max(ceil_log2(b)+e4a, ceil_log2(a)+e4b)
== 2 +(e4a+e4b) +max(ceil_log2(b)-e4b, ceil_log2(a)-e4a)
]
[ceil_log2(a*b) == (0|-1)+ceil_log2(a)+ceil_log2(b)]
    [a==b==7]:
        [6 == ceil_log2(49) == ceil_log2(7)*2 == 3*2 == 6]
    [a==b==5]:
        [5 == ceil_log2(25) < ceil_log2(5)*2 == 3*2 == 6]
[ceil_log2(a*b)-e4ab
== (0|-1)+ceil_log2(a)+ceil_log2(b)
    -(2 +(e4a+e4b) +max(ceil_log2(b)-e4b, ceil_log2(a)-e4a))
== -(2|3)
    +ceil_log2(a)+ceil_log2(b) -(e4a+e4b)
    -max(ceil_log2(b)-e4b, ceil_log2(a)-e4a)
== -(2|3) +min(ceil_log2(b)-e4b, ceil_log2(a)-e4a)
]
==>> (a*b)的精度 比 a,b两者最小精度还要小 3爻元
]]


py_adhoc_call   script.开方冫整数   @f
from script.开方冫整数 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
from seed.math.max_power_of_base_as_factor_of_ import factor_nonzero_int_out_sign_and_2_powers

from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#_exact = float('-inf')
#_exact = None
#class Interval8Float:
class Integer8Float:
    '[(i-1)*2**e <= float_value <= (i+1)*2**e]'
    '[abs(float_value-i*2**e) <= 2**e]'
    '[abs(float_value/2**e - i) <= 1]'
    '[float_value ~= i*2**e]'
    def __new__(cls, i, e, b_exact:bool, /):
        check_type_is(bool, b_exact)
        check_type_is(int, i)
        check_type_is(int, e)
        if i == 0 and b_exact:
            try:
                return _zero
            except NameError:
                pass
            e = 0
        if b_exact and i and (i&1)==0:
            # nonzero&even --> odd
            (sign, ez, odd) = factor_nonzero_int_out_sign_and_2_powers(i)
            i = -odd if sign else odd
            e += ez
        else:
            # cannot shift if inexact:
            #   since LSB repr err(+/-ulp)
            pass
        assert not b_exact or (e==0 if i==0 else (i&1)==1)
            # [exact => 0 or odd]

        sf = super(__class__, cls).__new__(cls)
        sf._ieb = i, e, b_exact
        return sf
        #.sf._i = i
        #.sf._e = e
        #.sf._b = b_exact
        #bug:sf._e = e if i else 0
            # 2**e is not related to i
    @classmethod
    def mk5triple(cls, i, e, b_exact:bool, /):
        return cls(i, e, b_exact)
    @classmethod
    def mk5int(cls, i, /):
        return cls.mk5triple(i, 0, True)
    @classmethod
    def mk_exact_binary_float(cls, i, e, /):
        return cls.mk5triple(i, e, True)
    @classmethod
    def mk_inexact_binary_float(cls, i, e, /):
        return cls.mk5triple(i, e, False)
    def __str__(sf, /):
        i, e, b = sf._ieb
        shift = 'pq'[e < 0]
            # p - pad 0s "<<"
        delta = 'mw'[b]
            # w - whole/complete/exact
        return f'{bin(i)}{delta}{shift}{abs(e)}'
    def __repr__(sf, /):
        #i = sf._i
        #e = sf._e
        #args = [i, e] if not e is _exact else [i]
        args = sf._ieb
        return repr_helper(sf, *args)
    def never_lt(sf, ot, /):
        #def any_lt(sf, ot, /):
        return _unpack(_never_lt, sf, ot)
    def always_lt(sf, ot, /):
        #def all_lt(sf, ot, /):
        return _unpack(_always_lt, sf, ot)
    def never_le(sf, ot, /):
        return _unpack(_never_le, sf, ot)
    def always_le(sf, ot, /):
        return _unpack(_always_le, sf, ot)
    def never_eq(sf, ot, /):
        return _unpack(_never_eq, sf, ot)
    def always_eq(sf, ot, /):
        return _unpack(_always_eq, sf, ot)


    def __rmul__(sf, ot, /):
        return _unpack(_mul, sf, ot)
        return type(sf).__mul__(sf, ot)
    def __mul__(sf, ot, /):
        return _unpack(_mul, sf, ot)
#middle-class Integer8Float:

class _Boundary:
    def __init__(sf, lowerL, upperL, lowerR, upperR, /):
        (lowerL, upperL, lowerR, upperR) = rename_boundaries_as_ranks__lulu_(lowerL, upperL, lowerR, upperR)
        
        sf._ns = ns = (lowerL, upperL, lowerR, upperR)
        for n in ns:
            check_int_ge_lt(0, 4, n)
        assert lowerL <= upperL
        assert lowerR <= upperR
        assert min(ns) == 0
        assert [*range(1+max(ns))] == sorted(set(ns))
    @cached_property
    def never_le(sf, /):
        (lowerL, upperL, lowerR, upperR) = sf._ns
        return (upperR < lowerL)
    @cached_property
    def always_le(sf, /):
        (lowerL, upperL, lowerR, upperR) = sf._ns
        return (upperL <= lowerR)
    @cached_property
    def never_lt(sf, /):
        (lowerL, upperL, lowerR, upperR) = sf._ns
        return (upperR <= lowerL)
    @cached_property
    def always_lt(sf, /):
        (lowerL, upperL, lowerR, upperR) = sf._ns
        return (upperL < lowerR)
    @cached_property
    def never_eq(sf, /):
        (lowerL, upperL, lowerR, upperR) = sf._ns
        return (upperL < lowerR or upperR < lowerL)
    @cached_property
    def always_eq(sf, /):
        (lowerL, upperL, lowerR, upperR) = sf._ns
        return (lowerL == upperL == lowerR == upperR)
    never_ne = always_eq
    always_ne = never_eq
    never_ge = always_lt
    always_ge = never_lt
    never_gt = always_le
    always_gt = never_le
def rename_boundaries_as_ranks__lulu_(lowerL, upperL, lowerR, upperR, /):
    '-> renamed(lowerL, upperL, lowerR, upperR)/[uint%4]{len==4}'
    ns = (lowerL, upperL, lowerR, upperR)
    js = sorted(range(4), key=ns.__getitem__)
    rs = [None]*4
    j0 = js[0]
    rs[j0] = 0
    j_ = j0
    for j in js[1:]:
        rs[j] = rs[j_] + not ns[j] == ns[j_]
        j_ = j
    return tuple(rs)
def rename_boundaries_as_ranks__iebieb_(iL, eL, bL, iR, eR, bR, /):
    '-> renamed(lowerL, upperL, lowerR, upperR)/[uint%4]{len==4}'
    ez = min(eL, eR)
    eL -= ez
    eR -= ez
    lowerL = iL if bL else iL-1
    upperL = iL if bL else iL+1
    lowerR = iR if bR else iR-1
    upperR = iR if bR else iR+1
    lowerL <<= eL
    upperL <<= eL
    lowerR <<= eR
    upperR <<= eR
    return rename_boundaries_as_ranks__lulu_(lowerL, upperL, lowerR, upperR)
    #######
    #######
    #######
rc4ab = -1,0
rc4cd = -1,0
rc4ad = -1,0,+1
rc4bc = -1,0,+1
rc4ac = -1,0,+1
rc4bd = -1,0,+1
def _rename_boundaries_as_ranks_(iL, eL, bL, iR, eR, bR, /):
    '-> renamed(lowerL, upperL, lowerR, upperR)/[uint%4]{len==4}'
    j = bL+2*bR
    #######
    (upperL, lowerR, rc) = ex_cmp_upperL_lowerR(iL, eL, bL, iR, eR, bR)
    if rc == -1:
        # [upperL < lowerR]
        return _0123_0012_0122_0011[j]
    if rc == 0:
        # [upperL == lowerR]
        return _0112_0001_0111_0000[j]
    assert rc == +1
    # [upperL > lowerR]
    #######
    (upperR, lowerL, rc) = ex_cmp_upperL_lowerR(iR, eR, bR, iL, eL, bL)
    if rc == -1:
        # [upperR < lowerL]
        return _2301_2201_1200_1100[j]
    if rc == 0:
        # [upperR == lowerL]
        return _1201_1101_0100_0000[j]
    assert rc == +1
    # [upperR > lowerL]
    #######
    # [upperL > lowerR]
    # [upperR > lowerL]
    #######
    rc = sign_of(lowerL-lowerR)
    #######
    lowerL = lowerR = min_lowerX = 0
    if rc == -1:
        # [lowerL < lowerR]
        lowerR += 1
        # [lowerL < lowerR < upperL]
        assert not bL
        if bR:
            # [lowerR == upperR]
            # [lowerL < lowerR == upperR < upperL]
            return _0211
    elif rc == 0:
        # [lowerL == lowerR]
        pass
        # [lowerL == lowerR < {upperL,upperR}]
        assert not bL
        assert not bR
    else:
        # [lowerL > lowerR]
        assert rc == +1
        lowerL += 1
        # [upperR > lowerL > lowerR]
        assert not bR
        if bL:
            # [lowerL == upperL]
            # [lowerR < lowerL == upperL < upperR]
            return _1102
    assert not bL
    assert not bR
    #######
    max_lowerX = max(lowerL, lowerR)
    min_upperX = max(lowerL, lowerR)
    #######
    rc = sign_of(upperL-upperR)
    #######
    upperL = upperR = min_upperX
    if rc == -1:
        # [upperL < upperR]
        upperR += 1
    elif rc == 0:
        # [upperL == upperR]
        pass
    else:
        # [upperL > upperR]
        assert rc == +1
        upperL += 1
    return (lowerL, upperL, lowerR, upperR) # renamed
    #######
    #######
    #######
def cmp_boundaries_(iL, eL, bL, iR, eR, bR, /):
def ex_cmp_upperL_lowerR(iL, eL, bL, iR, eR, bR, /):
    upperL = iL if bL else iL+1
    lowerR = iR if bR else iR-1
    _eL = eL-eR
    if _eL < 0:
        # [eL < eR]
        _eR = -_eL # == eR-eL
        _eL = 0
    else:
        # [eL >= eR]
        _eR = 0
    # cmp (upperL*2**_eL) (lowerR*2**_eR)
    upperL <<= _eL
    lowerR <<= _eR
    # cmp (upperL) (lowerR)
    return (upperL, lowerR, sign_of(upperL-lowerR))

def _never_lt(cls, iL, eL, bL, iR, eR, bR, /):
def _always_lt(cls, iL, eL, bL, iR, eR, bR, /):

def _never_le(cls, iL, eL, bL, iR, eR, bR, /):
def _always_le(cls, iL, eL, bL, iR, eR, bR, /):

def _never_eq(cls, iL, eL, bL, iR, eR, bR, /):
    (lowerL, upperL, lowerR, upperR) = rename_boundaries_as_ranks_(iL, eL, bL, iR, eR, bR)
    rc = ex_cmp_upperL_lowerR(iL, eL, bL, iR, eR, bR)
    if rc == -1:
        return True
    if rc == 0:
        return False
    assert rc == +1
    if iL < 0 and iR > 0:
    return bL and bR and eL == eR and iL == iR
def _always_eq(cls, iL, eL, bL, iR, eR, bR, /):
    # !! factor_nonzero_int_out_sign_and_2_powers
    # [exact => 0 or odd]
    return bL and bR and eL == eR and iL == iR
def _mul(cls, iL, eL, bL, iR, eR, bR, /):
    if bL and not bR:
        #swap
        (iL,eL,bL), (iR,eR,bR) = (iR,eR,bR), (iL,eL,bL)

    ii = iL*iR
    if bL and bR:
        return cls.mk5triple(ii, eL+eR, True)
    elif not bL and bR:
        if iR == 0:
            # return since below require [b-a >= 2]
            return _zero
        # [iR =!= 0]
        _r = abs(iR)
        # [_r >= 1]
        a = ii-_r
        b = ii+_r
        # [a == min (iL+/-1)*iR]
        # [b == max (iL+/-1)*iR]
        # [b-a == 2*_r >= 2]
        # [b-a >= 2]
        # [a <= sf/2**eL * ot/2**eR <= b]
    elif bL and not bR:
        raise 000
    elif not bL and not bR:
        s = iL+iR
        d = iL-iR
        _s = abs(s)
        _d = abs(d)
        a = ii+min(1-_s, -1-_d)
        b = ii+max(1+_s, -1+_d)
        # [a == min (iL+/-1)*(iR+/-1)]
        # [b == max (iL+/-1)*(iR+/-1)]
        # [b-a >= 2]
        # [a <= sf/2**eL * ot/2**eR <= b]
    a, b
    # [a <= sf/2**eL * ot/2**eR <= b]
    # [b-a >= 2]

    # [product_value := sf*ot]
    # [v := product_value/2**(eL+eR)]
    # [a <= v <= b]
    assert b-a >= 2
    k0 = -1+ceil_log2(b-a)
    assert k0 >= 0
    # [ceil_log2(b-a) == 1+k0]
    # [log2(b-a) <= (1+k0)]
    # [(b-a) <= 2**(1+k0)]
    # let [k >= k0]
    # [(b-a) <= 2**(1+k)]
    err0 = 1 << k0
    # [(b-a) <= 2*err0]
    # [b <= a+2*err0]
    a_k0 = (((a >> k0) + 1) << k0)
        # clear low bits lower than 2**k0 and add 2**k0
    # [a_k0-err0 == a-low_bits <= a < a-low_bits+err0 == a_k0]
    # [a_k0-err0 <= a < a_k0]
    a_2k0 = a_k0+err0
    a_3k0 = a_2k0+err0
    # [b <= a+2*err0 < a_k0+2*err0 == a_3k0]
    assert a < a_k0 <= b < a_3k0
    # [a_k0-err0 <= a < a_k0 <= {b,a_2k0} < a_3k0]
    if a_2k0 < b:
        # [a_k0-err0 <= a < a_k0 < a_2k0 < b < a_3k0]
        # [neither a_k0 nor a_2k0 can be output]
        # [k0 is not ok]
        k = 1+k0
        # [k >= 1]
        # [k >= 0]
        err = 1<<k
        # [err == 2**k]
        # [err == 2*err0]

        #c = a_k0 if a_2k0&err0 else a_2k0
        u = a_2k0 >> k
        # choose larger one since ">>" is floor div
        c = u << k
        assert 0 == (c&err0)
        assert c in (a_k0, a_2k0)
        # [c == u*2**k]
        # [c <- [a_k0, a_2k0]]
        # [a_k0 <= c <= a_2k0]
        # [c-err <= a_2k0-2*err0 == a_k0-err0 <= a < a_k0 <= c <= a_2k0 < b < a_3k0 == a_k0+2*err0 <= c+err]
        # [c-err <= a <= c <= b <= c+err]
        # [err == 2**k]
        # [c == u*2**k]
        # [k >= 0]
    else:
        # [a_k0-err0 <= a < a_k0 <= b <= a_2k0 < a_3k0]
        # [a_k0 can be output]
        # [k0 is ok]
        k = k0
        # [k >= 0]
        c = a_k0
        err = err0
        # [err == 2**k]
        # [c-err == a_k0-err0 <= a < c == a_k0 <= b <= a_2k0 == c+err < a_3k0]
        # [c-err <= a <= c <= b <= c+err]
        u = c >> k
        assert c == (u<<k)
        # [c == u*2**k]
        # [err == 2**k]
        # [c-err <= a <= c <= b <= c+err]
        # [k >= 0]
    k, err, c
    # [k >= 0]
    # [err == 2**k]
    # [c == u*2**k]
    # [c-err <= a <= c <= b <= c+err]
    assert k >= 0
    assert err == (1<<k)
    assert c == (u<<k)
    assert c-err <= a <= c <= b <= c+err
    # [(u-1)*2**k <= a <= u*2**k <= b <= (u+1)*2**k]
    # [(u-1) <= a/2**k <= u <= b/2**k <= (u+1)]
    # !! [a <= v <= b]
    # [(u-1) <= a/2**k <= v/2**k <= b/2**k <= (u+1)]
    # [(u-1) <= v/2**k <= (u+1)]
    # !! [v := product_value/2**(eL+eR)]
    # [(u-1) <= product_value/2**(eL+eR)/2**k <= (u+1)]
    # [product_value ~= u*2**(eL+eR+k)]
    eO = (eL+eR+k)
    iO = u
    return cls.mk5triple(iO, eO, False)
def _unpack(f, sf, ot, /):
    if type(ot) is int:
        #iR, eR, bR = ot, 0, True
        ieb4ot = ot, 0, True
    elif type(ot) is type(sf):
        #iR, eR, bR = ot._ieb
        ieb4ot = ot._ieb
    else:
        return NotImplemented
        #return None
    #(iL, eL, bL) = sf._ieb
    #return (iL, eL, bL), (iR, eR, bR)
    cls = type(sf)
    #return cls, sf._ieb, ieb4ot
    return f(cls, *sf._ieb, *ieb4ot)

#end-class Integer8Float:
_zero = Integer8Float(0, 0, True)
assert _zero is Integer8Float(0, 0, True)
assert _zero is Integer8Float(0, 999, True)
assert _zero is Integer8Float(0, -999, True)




__all__
from script.开方冫整数 import *
