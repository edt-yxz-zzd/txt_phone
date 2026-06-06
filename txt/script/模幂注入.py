#__all__:goto
r'''[[[
e script/模幂注入.py

script.模幂注入
py -m nn_ns.app.debug_cmd   script.模幂注入 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.模幂注入:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/algo/rho_method__7iter.py
view script/整数分解牜尸方法牜吸引子.py
]]
[[
幂方注入:
  x**x%p == x**(x%(p-1))%p
  x**x%(p*q) == x**(x%((p-1)*(q-1)))%(p*q)
  x==a*p+b
  x**x%p == b**((a+b)%(p-1))%p =!= b**b%p
  x**x%p =!= b**b%p
    这就无用了...
    环状根 肯定更大
  x==a*p+b==(c*(p-1)+d)*p +b == c*(p-1)*p +d*p+b
  0 <= b <= p-1
  0 <= d <= p-2
  0 <= b <= d+b <= p-2+b <= 2*p-3 < 2*(p-1)
  x**x%p == b**((d+b)%(p-1))%p
  [x**x%p =!= b**b%p] ==>> [d=!=0]
  x%(p*(p-1)) == d*p+b
    得考察 x**x%p 在 [x<-[0..<p*(p-1)]] 上面的表现
    环状根 平均规模 O(p)
  x**x%(p*(p-1))
    phi(p*(p-1)) = (p-1)*phi(p-1)
    然而 x**x%(p*q)导致输出的(d,b)里d不可预测

]]


'#'; __doc__ = r'#'
>>>


[[
py_adhoc_call { -lineno }  script.模幂注入   ,枚举冫模幂注入扌 +both =3
    0:(0, 1)
    1:(1, 1)
    2:(2, 4)
    3:(3, 3)
    4:(4, 4)
    5:(5, 5)
py_adhoc_call { -lineno }  script.模幂注入   ,枚举冫模幂注入扌 +both +as_digits =3
    0:((0, 0), (0, 1))
    1:((0, 1), (0, 1))
    2:((0, 2), (1, 1))
    3:((1, 0), (1, 0))
    4:((1, 1), (1, 1))
    5:((1, 2), (1, 2))

py_adhoc_call { -lineno }  script.模幂注入   ,枚举冫模幂注入扌 +both +as_digits =5
    0:((0, 0), (0, 1))
    1:((0, 1), (0, 1))
    2:((0, 2), (0, 4))
    3:((0, 3), (1, 2))
    4:((0, 4), (3, 1))
    5:((1, 0), (1, 0))
    6:((1, 1), (3, 1))
    7:((1, 2), (0, 3))
    8:((1, 3), (3, 1))
    9:((1, 4), (1, 4))
    10:((2, 0), (0, 0))
    11:((2, 1), (2, 1))
    12:((2, 2), (3, 1))
    13:((2, 3), (2, 3))
    14:((2, 4), (3, 1))
    15:((3, 0), (3, 0))
    16:((3, 1), (3, 1))
    17:((3, 2), (3, 2))
    18:((3, 3), (0, 4))
    19:((3, 4), (3, 4))

py_adhoc_call { -lineno }  script.模幂注入   ,枚举冫模幂注入扌 +both +as_digits =7
    0:((0, 0), (0, 1))
    1:((0, 1), (0, 1))
    2:((0, 2), (0, 4))
    3:((0, 3), (3, 6))
    4:((0, 4), (0, 4))
    5:((0, 5), (2, 3))
    6:((0, 6), (5, 1))
    7:((1, 0), (1, 0))
    8:((1, 1), (3, 1))
    9:((1, 2), (2, 1))
    10:((1, 3), (0, 4))
    11:((1, 4), (3, 2))
    12:((1, 5), (5, 1))
    13:((1, 6), (1, 6))
    14:((2, 0), (4, 0))
    15:((2, 1), (2, 1))
    16:((2, 2), (2, 2))
    17:((2, 3), (0, 5))
    18:((2, 4), (5, 1))
    19:((2, 5), (2, 5))
    20:((2, 6), (3, 1))
    21:((3, 0), (3, 0))
    22:((3, 1), (3, 1))
    23:((3, 2), (1, 4))
    24:((3, 3), (5, 1))
    25:((3, 4), (3, 4))
    26:((3, 5), (0, 4))
    27:((3, 6), (3, 6))
    28:((4, 0), (4, 0))
    29:((4, 1), (4, 1))
    30:((4, 2), (5, 1))
    31:((4, 3), (4, 3))
    32:((4, 4), (2, 2))
    33:((4, 5), (3, 6))
    34:((4, 6), (3, 1))
    35:((5, 0), (5, 0))
    36:((5, 1), (5, 1))
    37:((5, 2), (5, 2))
    38:((5, 3), (2, 2))
    39:((5, 4), (2, 1))
    40:((5, 5), (2, 2))
    41:((5, 6), (5, 6))

py_adhoc_call { -lineno }  script.模幂注入   ,枚举冫模幂注入扌 +both +as_digits +out1  =7
    0:((0, 0), 1)
    1:((0, 1), 1)
    2:((0, 2), 4)
    3:((0, 3), 6)
    4:((0, 4), 4)
    5:((0, 5), 3)
    6:((0, 6), 1)
    7:((1, 0), 0)
    8:((1, 1), 1)
    9:((1, 2), 1)
    10:((1, 3), 4)
    11:((1, 4), 2)
    12:((1, 5), 1)
    13:((1, 6), 6)
    14:((2, 0), 0)
    15:((2, 1), 1)
    16:((2, 2), 2)
    17:((2, 3), 5)
    18:((2, 4), 1)
    19:((2, 5), 5)
    20:((2, 6), 1)
    21:((3, 0), 0)
    22:((3, 1), 1)
    23:((3, 2), 4)
    24:((3, 3), 1)
    25:((3, 4), 4)
    26:((3, 5), 4)
    27:((3, 6), 6)
    28:((4, 0), 0)
    29:((4, 1), 1)
    30:((4, 2), 1)
    31:((4, 3), 3)
    32:((4, 4), 2)
    33:((4, 5), 6)
    34:((4, 6), 1)
    35:((5, 0), 0)
    36:((5, 1), 1)
    37:((5, 2), 2)
    38:((5, 3), 2)
    39:((5, 4), 1)
    40:((5, 5), 2)
    41:((5, 6), 6)

]]
[[
py_adhoc_call   script.模幂注入   ,成尸冫模幂注入扌  =35 =8
    (0, 8)
    (1, 1)
    (1, 2, 1, 1)
]]
[[
py_adhoc_call   script.模幂注入   ,批量成尸冫模幂注入扌  =35
    [[1], [0, 6, 8, 12, 24, 34], [17]]
    [[13], [27, 33], [3]]
    [[15], [20, 30]]
    [[16], [11, 32], [4, 23, 26], [2]]
    [[19]]
    [[21], [14, 28], [7]]
    [[25], [10], [5]]
    [[29], [9, 18, 22]]
    [[31]]


py_adhoc_call   script.模幂注入   ,批量成尸冫模幂注入扌  ='7*13'
    [[1], [0, 8, 9, 12, 24, 30, 36, 48, 60, 64, 66, 72, 81, 90], [6, 10, 15, 18, 34, 51, 54, 58, 69, 75, 80, 82, 88], [11, 17, 33, 41, 59, 83], [19, 45, 67, 89]]
    [[13]]
    [[14], [42, 84], [7, 28, 35, 56]]
    [[16], [32, 74], [4, 68], [2, 23, 46]]
    [[21]]
    [[22], [29, 62], [20, 76]]
    [[25], [86]]
    [[27], [3, 87]]
    [[37]]
    [[43], [50], [71]]
    [[49]]
    [[55]]
    [[57]]
    [[61]]
    [[73], [31], [5, 47]]
    [[77], [70], [63]]
    [[78], [39], [26, 52, 65]]
    [[79], [38, 40, 53], [44]]
    [[85]]

py_adhoc_call   script.模幂注入   ,批量成尸冫模幂注入扌  ='5'
    [[1], [0, 4], [2], [3]]

py_adhoc_call   script.模幂注入   ,批量成尸冫模幂注入扌  ='7'
    [[1], [0, 6], [3], [5]]
    [[4], [2]]

py_adhoc_call   script.模幂注入   ,批量成尸冫模幂注入扌  ='13'
    [[1], [0, 3, 8, 9, 12], [4, 6, 10], [2, 7, 11]]
    [[5]]


py_adhoc_call   script.模幂注入   ,len.批量成尸冫模幂注入扌  ='233'
    14
    5
    6
    2
    2
    2
    8
    14
py_adhoc_call   script.模幂注入   ,len.批量成尸冫模幂注入扌  ='377'
    8
    3
    3
    9
    1
    1
    4
    1
    1
    2
    2
    9
    6
    2
    1
    6
    1
    1
    5
    3
    2
    1
    2

is_prime =233
    True
is_prime =377
    False

py_adhoc_call   script.模幂注入   ,len.批量成尸冫模幂注入扌  ='257'
    11
    4
    4
    1
    4
    5
    3
    11

py_adhoc_call   script.模幂注入   ,len.批量成尸冫模幂注入扌  ='7'
    4
    2
py_adhoc_call   script.模幂注入   ,len.批量成尸冫模幂注入扌  ='11'
    5
py_adhoc_call   script.模幂注入   ,len.批量成尸冫模幂注入扌  ='13'
    4
    1
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only ='7*11'
    (6, [4, 1, 4, 2, 2, 3, 2, 2, 1, 2, 4, 1, 5, 6], (14, 2, 5))
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only ='7*13'
    (5, [5, 1, 3, 4, 1, 3, 2, 2, 1, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1], (19, 1, 4))
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only ='11*13'
    (8, [8, 6, 4, 1, 1, 1, 1, 2, 4, 1, 1, 4, 1, 6, 1, 3, 1, 1, 3, 5], (20, 3, 7))
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only ='233*257'
    (33, [33, 3, 3, 1, 5, 2, 5, 4, 15, 13, 1, 13, 6, 2, 1, 6, 22, 5, 1, 2, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 2, 2, 3, 3, 12, 2, 1, 3, 3, 9, 1, 3, 11, 1, 4, 8, 5, 10, 2, 2, 1, 21, 2, 1, 4, 1, 1, 6, 1, 19, 1, 1, 12, 2, 7, 4, 1, 3, 6, 14, 1, 3, 17, 6, 8, 1, 2, 4, 5, 1, 2, 1, 19, 9, 1], (85, 7, 32))
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only ='233'
    (14, [14, 5, 6, 2, 2, 2, 8, 14], (8, 4, 13))
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only ='257'
    (11, [11, 4, 4, 1, 4, 5, 3, 11], (8, 2, 10))



]]
[[
++kw:average
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only +average  ='233*257'
    (33, [33, 7, 6, 4, 11, 3, 5, 6, 17, 10, 3, 11, 5, 3, 3, 6, 17, 6, 3, 3, 3, 3, 3, 5, 5, 5, 3, 3, 4, 3, 3, 3, 5, 5, 9, 3, 3, 5, 5, 9, 3, 5, 12, 3, 7, 9, 5, 9, 3, 6, 4, 18, 3, 3, 5, 3, 3, 5, 3, 17, 4, 3, 9, 3, 9, 5, 3, 5, 5, 9, 3, 6, 17, 5, 9, 3, 3, 5, 5, 3, 3, 3, 17, 9, 3], (85, 7, 32))
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only +average  ='233'
    (9, [9, 8, 6, 3, 3, 3, 9, 9], (8, 4, 13))
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only +average  ='257'
    (9, [9, 6, 6, 3, 6, 5, 5, 9], (8, 2, 10))
py_adhoc_call   script.模幂注入   @批量成尸冫模幂注入扌 +size_only +average  ='2**16-13'
    (21, [17, 5, 18, 3, 5, 5, 6, 10, 6, 10, 7, 5, 9, 7, 5, 9, 10, 6, 5, 10, 5, 21, 3, 5, 10, 9, 9, 5, 5, 5, 5, 9, 10, 9, 5, 9, 19, 5, 9, 7, 5, 17, 9, 17, 10, 4, 5, 17, 18, 18, 4, 18, 5, 9, 18, 17, 18, 17, 9, 9, 17, 9, 6, 17, 3, 5, 3, 18, 5, 9, 17, 5, 5, 5, 5, 6, 4, 9, 9, 9, 9, 17, 10, 3, 9, 6, 9, 17, 6, 4, 5, 5, 5, 9, 9, 17, 17, 9, 5, 5, 9, 10, 3, 10, 17, 6, 9, 3, 5, 3, 5, 9, 9, 17, 9, 9, 9, 3, 9, 5, 9, 5, 9, 6, 5, 17, 4, 5, 4, 9, 5, 5, 9, 5, 5, 5], (136, 6, 25))

]]




py_adhoc_call   script.模幂注入   @f
from script.模幂注入 import *
]]]'''#'''
__all__ = r'''
枚举冫模幂注入扌
成尸冫模幂注入扌
制表冫模幂注入扌
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
    from seed.helper.forest_tabulation5modular_func import group_, tab_, show4tab_
        # (x2y, y2num_xs, y2xs, x2min_root, x2height, min_root2len_period, min_root2minmax_height, (num_trees, max_len_period, max_height)) = tab_(f, M, *args, max_M=max_M)
        # (x2y, y2num_xs, y2xs, x2min_root, x2height, min_root2len_period, min_root2minmax_height, (num_trees, max_len_period, max_height), min_root2root2tree, min_root2layers) = tab_(f, M, *args, max_M=max_M, more=1)

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


def 枚举冫模幂注入扌(p, /, *, as_digits=False, both=False, out1=False):
    # [p::prime]
    M = p*(p-1)
    N = M if not out1 else p
    for x in range(M):
        y = pow(x,x,N)
        if as_digits:
            if not out1:
                y = divmod(y, p)
            if both:
                x = divmod(x, p)
        yield y if not both else (x, y)
    return


def 成尸冫模幂注入扌(pq, u, /):
    us = []
    u2j = {}
    u %= pq
    for j in range(1+pq):
        if u in u2j:
            break
        u2j[u] = j
        us.append(u)
        yield (j, u)
        u = pow(u,u,pq)
    else:
        raise 000
    i = u2j[u]
    yield (i,j,j-i,u,us)

def 制表冫模幂注入扌(pq, /):
    x2y = [pow(x,x,pq) for x in range(pq)]
    return x2y
def 单算冫模幂注入扌(pq, x, /):
    return pow(x,x,pq)
def 批量成尸冫模幂注入扌(pq, /, *, size_only=False, average=False):
    #x2y = 制表冫模幂注入扌(pq)
    (x2y, y2num_xs, y2xs, x2min_root, x2height, min_root2len_period, min_root2minmax_height, (num_trees, max_len_period, max_height), min_root2root2tree, min_root2layers) = tab_(单算冫模幂注入扌, pq, more=1)
    ps = sorted(min_root2layers.items())
    layerss = [layers for _, layers in ps]
    if size_only:
        if average:
            #szs = [(len(layers)+1)//2 +len(layers[0]) for layers in layerss]
            szs = [(1<<((len(layers)+1)//2).bit_length()) +len(layers[0]) for layers in layerss]
        else:
            szs = [*map(len, layerss)]
        szs
        max_sz = max(szs)
        return (max_sz, szs, (num_trees, max_len_period, max_height))
    return layerss


__all__
from script.模幂注入 import *
