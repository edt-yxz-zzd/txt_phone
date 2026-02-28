#__all__:goto
r'''[[[
e script/搜索冫首个特例纟最短加链牜查表.py

script.搜索冫首个特例纟最短加链牜查表
py -m nn_ns.app.debug_cmd   script.搜索冫首个特例纟最短加链牜查表 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.搜索冫首个特例纟最短加链牜查表:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   script.搜索冫首个特例纟最短加链牜查表   ,搜索冫首个特例纟最短加链牜查表牜倍数而链长不增扌 '=range(2,17)'
(2, (191, 11), (382, 11))
(3, (171, 10), (513, 10))
(4, None, range(1, 100001))
(5, (3277, 15), (16385, 15))
(6, (2731, 15), (16386, 15))
(7, None, range(1, 100001))
(8, None, range(1, 100001))
(9, None, range(1, 100001))
(10, None, range(1, 100001))
(11, None, range(1, 100001))
(12, None, range(1, 100001))
(13, None, range(1, 100001))
(14, None, range(1, 100001))
(15, None, range(1, 100001))
(16, None, range(1, 100001))

e others/数学/最短加链/最短加链--py_doc-www-杂录.txt
    [191==min{u | [u:<-[1..]][ℓ(2*u) == ℓ(u)]}]
    [171==min{u | [u:<-[1..]][ℓ(3*u) == ℓ(u)]}]
    [3277==min{u | [u:<-[1..]][ℓ(5*u) == ℓ(u)]}]
    [2731==min{u | [u:<-[1..]][ℓ(6*u) == ℓ(u)]}]
    [12509 == min{n | [n:<-[1..]][ℓ(n) < ℓ*(n)]}]
    [375_494_703==375494703==3_7549_4703==min{u | [u:<-[1..]][ℓ(2*u) < ℓ(u)]}]
    [30_958_077==30958077==3095_8077==min{u | [u:<-[1..]][ℓ(4*u) == ℓ(2*u) == ℓ(u)]}]
]]


from script.搜索冫首个特例纟最短加链牜查表 import *
]]]'''#'''
__all__ = r'''
搜索冫首个特例纟最短加链牜查表牜倍数而链长不增扌

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
___end_mark_of_excluded_global_names__0___ = ...

def 搜索冫首个特例纟最短加链牜查表牜倍数而链长不增扌(scales, /):
    from seed.tiny_.check import check_type_is, check_int_ge
    from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length
    u2szmm = pint2shortest_addition_chain_length
    max1_u = len(u2szmm)
    s = set()
    for scale in scales:
        check_int_ge(2, scale)
        if scale in s:continue
        s.add(scale)
        #for u in range(1, ceil_div(max1_u,scale)):
        for u, w in zip(range(1, max1_u), range(scale, max1_u, scale)):
            if not u2szmm[u] < u2szmm[w]:
                yield (scale, (u, u2szmm[u]), (w, u2szmm[w]))
                break
        else:
                yield (scale, None, range(1, max1_u))


__all__
from script.搜索冫首个特例纟最短加链牜查表 import *
