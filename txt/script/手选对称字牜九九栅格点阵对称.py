#__all__:goto
r'''[[[
e script/手选对称字牜九九栅格点阵对称.py

script.手选对称字牜九九栅格点阵对称
py -m nn_ns.app.debug_cmd   script.手选对称字牜九九栅格点阵对称 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.手选对称字牜九九栅格点阵对称:__doc__ -ht # -ff -df

[[
考虑到类似『留/桀/怨/兜/韋』等不规则对称，不如设计一套对称点阵图
九宫各宫内嵌小九宫:2**81种字形

对称形式:
    翻转对称:
        水平轴对称/上下对称
        竖直轴对称/左右对称
        左倾轴对称
        右倾轴对称
    旋转对称:
        顺旋对称/顺时针旋转90度
        逆旋对称/顺时针旋转270度
        中心对称/顺时针旋转180度
    周期晶格对称:
        平移对称
        偏心对称

===
计数:
    A:所有编码数量
    H:水平轴对称/上下对称
    V:竖直轴对称/左右对称
    L:左倾轴对称
    R:右倾轴对称
    C:顺旋对称
    E:逆旋对称
    O:中心对称
    ... ...
大九宫巛小九宫:
    A=_A**9
    H=_A**3*_H**3
    V=_A**3*_V**3
    L=_A**3*_L**3
    R=_A**3*_R**3
    C=_A**2*_C**1
    E=_A**2*_E**1
    O=_A**4*_O**1
    [[_C==_E] -> [C==E]]
    [[_H==_V==_L==_R] -> [H==V==L==R]]
单格:2:口田
    A=2
    H=2
    V=2
    L=2
    R=2
    C=2
    E=2
    O=2
小九宫:
    A=2**9
    H=2**6
    V=2**6
    L=2**6
    R=2**6
    C=2**3
    E=2**3
    O=2**5
大九宫:
    A=2**81
    H=2**45
    V=2**45
    L=2**45
    R=2**45
    C=2**21
    E=2**21
    O=2**41

===
小九宫牜横竖八卦:
    A=14==8+8-2
    H=10==8+4-2
    V=10
    L=2
    R=2
    C=2
    E=2
    O=6==4+4-2
大九宫牜横竖八卦小九宫:
    A=14**9==206_6104_6784
    H=140**3==2744000
    V=140**3==2744000
    L=28**3==21952
    R=28**3==21952
    C=14**2*2==392
    E=14**2*2==392
    O=14**4*6==230496
]]

py_adhoc_call   script.手选对称字牜九九栅格点阵对称   @f
from script.手选对称字牜九九栅格点阵对称 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge, check_uint_lt, check_pair
#from seed.iters.iter_unique_by_hash import iter_unique_by_hash
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

[_0, _1] = b'01'
class BitSquareMatrix:
    def __init__(sf, sz_or_bs, /):
        if not type(sz_or_bs) is int:
            bs = sz_or_bs
            bs = bytearray(bs)
            L = len(bs)
            sz = isqrt(L)
            if not sz**2 == L:raise TypeError
        else:
            sz = sz_or_bs
            check_int_ge(0, sz)
            L = sz**2
            bs = bytearray(b'0'*L)
        sz
        bs
        sf._bs = bs
        sf._sz = sz
    def to_bytes(sf, /):
        return bytes(sf._bs)
    def _idx5kk(sf, kk, /):
        check_pair(kk)
        r, c = kk
        sz = sf._sz
        check_uint_lt(sz, r)
        check_uint_lt(sz, c)
        j = r*sz+c
        return j
    def __getitem__(sf, kk, /):
        j = sf._idx5kk(kk)
        bs = sf._bs
        return bs[j] == _1
    def __setitem__(sf, kk, b, /):
        if not type(b) is bool:
            check_uint_lt(2, b)
        #check_type_is(bool, b)
        j = sf._idx5kk(kk)
        bs = sf._bs
        bs[j] = b'01'[b]
        return



def 列表冫小九宫牜横竖八卦扌():
    '-> Iter bytes{len==9}'
    it0 = _枚举冫小九宫牜竖八卦扌()
    it1 = _枚举冫小九宫牜横八卦扌()
    #iter_unique_by_hash(chain(it0, it1))
    ls = sorted({*it0, *it1})
    return ls
    return iter(ls)
def _枚举冫小九宫牜竖八卦扌():
    '-> Iter bytes{len==9}'
    mx = BitSquareMatrix(3)
    for r in range(3):
        mx[r,0] = True
        mx[r,2] = True
    for j in range(8):
        bs = bf'{j:0>3B}'
        assert len(bs) == 3
        for r in range(3):
            mx[r,1] = (bs[r] == _1)
        yield mx.to_bytes()
def _枚举冫小九宫牜横八卦扌():
    '-> Iter bytes{len==9}'
    mx = BitSquareMatrix(3)
    for c in range(3):
        mx[0,c] = True
        mx[2,c] = True
    for j in range(8):
        bs = bf'{j:0>3B}'
        assert len(bs) == 3
        for c in range(3):
            mx[1,c] = (bs[c] == _1)
        yield mx.to_bytes()

def 枚举冫大九宫牜横竖八卦小九宫扌():
    '-> Iter bytes{len==81}'
    ls = 列表冫小九宫牜横竖八卦扌()
    ... ...
__all__
from script.手选对称字牜九九栅格点阵对称 import *
