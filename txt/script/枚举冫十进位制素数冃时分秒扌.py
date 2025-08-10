#__all__:goto
r'''[[[
e script/枚举冫十进位制素数冃时分秒扌.py

script.枚举冫十进位制素数冃时分秒扌
py -m nn_ns.app.debug_cmd   script.枚举冫十进位制素数冃时分秒扌 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.枚举冫十进位制素数冃时分秒扌:__doc__ -ht # -ff -df

[[
]]

[[
py_adhoc_call   script.枚举冫十进位制素数冃时分秒扌   ,枚举冫变进位制数扌 +dec_repr =4 =3
0
1
2
10
11
12
20
21
22
30
31
32
]]

[[
py_adhoc_call   script.枚举冫十进位制素数冃时分秒扌   ,10:枚举冫十进位制素数冃时分扌 +padding
py_adhoc_call   script.枚举冫十进位制素数冃时分秒扌   ,str.10:枚举冫十进位制素数冃时分扌 +padding
py_adhoc_call   script.枚举冫十进位制素数冃时分秒扌   ,str.枚举冫十进位制素数冃时分扌 +padding > /sdcard/0my_files/tmp/0tmp
    211行
view /sdcard/0my_files/tmp/0tmp

!mkdir script/枚举冫十进位制素数冃时分秒扌.py.out/
py_adhoc_call   script.枚举冫十进位制素数冃时分秒扌   ,str.枚举冫十进位制素数冃时分扌 +padding > script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分.txt
grep . -n script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分.txt > script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分牜带编号.txt
view script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分牜带编号.txt
view script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分.txt
0002
0003
0005
0007
0011
0013
0017
0019
0023
0029
0031
0037
0041
0043
0047
0053
0059
0101
0103
0107
0109
0113
0127
0131
0137
0139
0149
0151
0157
0211
0223
0227
0229
0233
0239
0241
0251
0257
0307
0311
0313
0317
0331
0337
0347
0349
0353
0359
0401
0409
0419
0421
0431
0433
0439
0443
0449
0457
0503
0509
0521
0523
0541
0547
0557
0601
0607
0613
0617
0619
0631
0641
0643
0647
0653
0659
0701
0709
0719
0727
0733
0739
0743
0751
0757
0809
0811
0821
0823
0827
0829
0839
0853
0857
0859
0907
0911
0919
0929
0937
0941
0947
0953
1009
1013
1019
1021
1031
1033
1039
1049
1051
1103
1109
1117
1123
1129
1151
1153
1201
1213
1217
1223
1229
1231
1237
1249
1259
1301
1303
1307
1319
1321
1327
1409
1423
1427
1429
1433
1439
1447
1451
1453
1459
1511
1523
1531
1543
1549
1553
1559
1601
1607
1609
1613
1619
1621
1627
1637
1657
1709
1721
1723
1733
1741
1747
1753
1759
1801
1811
1823
1831
1847
1901
1907
1913
1931
1933
1949
1951
2003
2011
2017
2027
2029
2039
2053
2111
2113
2129
2131
2137
2141
2143
2153
2203
2207
2213
2221
2237
2239
2243
2251
2309
2311
2333
2339
2341
2347
2351
2357

]]
[[
py_adhoc_call   script.枚举冫十进位制素数冃时分秒扌   ,str.枚举冫十进位制素数冃时分秒扌 +padding > /sdcard/0my_files/tmp/0tmp
    7669行
view /sdcard/0my_files/tmp/0tmp
grep . -n /sdcard/0my_files/tmp/0tmp > /sdcard/0my_files/tmp/1tmp
1:000002
... ...
3543:100003
... ...
6526:200003
... ...
7669:235951
cp -iv /sdcard/0my_files/tmp/0tmp script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分秒.txt
grep . -n script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分秒.txt > script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分秒牜带编号.txt
view script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分秒.txt
view script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分秒牜带编号.txt
du -h script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分秒.txt
    56K
du -h script/枚举冫十进位制素数冃时分秒扌.py.out/十进位制素数冃时分秒牜带编号.txt
    92K
]]


]]]'''#'''
__all__ = r'''
枚举冫十进位制素数冃时分秒扌
    枚举冫十进位制素数冃时分扌



枚举冫变进位制数扌
    枚举冫十进位制数冃时分扌
    枚举冫十进位制数冃时分秒扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import product
___end_mark_of_excluded_global_names__0___ = ...



def 枚举冫变进位制数扌(*bases, dec_repr:bool):
    if dec_repr:
        from seed.math.floor_ceil import ceil_log_
    weights = [1]
    for base in reversed(bases[1:]):
        if dec_repr:
            base = 10**ceil_log_(10, base)
        weights.append(weights[-1]*base)
    weights.reverse()
    L = len(bases)
    assert len(weights) == L
    #if 0b0001:print(bases, weights)
    for ds in product(*map(range, bases)):
        #if 0b0001:print(ds)
        assert len(ds) == L
        yield sum(map(int.__mul__, weights, ds))
def 枚举冫十进位制数冃时分扌():
    return 枚举冫变进位制数扌(24,60, dec_repr=True)
def 枚举冫十进位制数冃时分秒扌():
    return 枚举冫变进位制数扌(24,60,60, dec_repr=True)
def 枚举冫十进位制素数冃时分扌(**kwds):
    return 枚举冫十进位制素数冃时分秒扌(without_second=True, **kwds)
def 枚举冫十进位制素数冃时分秒扌(*, without_second=False, padding=False):
    it = 枚举冫十进位制数冃时分秒扌() if not without_second else 枚举冫十进位制数冃时分扌()
    from seed.math.prime_gens import is_prime__le_pow2_81_
    ns = filter(is_prime__le_pow2_81_, it)
    def pad_(n, /):
        return f'{n:0>{num4padding}}'
    if padding:
        num4padding = (6 if not without_second else 4)
        rs = map(pad_, ns)
    else:
        rs = ns
    rs
    return rs

__all__
from script.枚举冫十进位制素数冃时分秒扌 import 枚举冫变进位制数扌,枚举冫十进位制素数冃时分秒扌,枚举冫十进位制素数冃时分扌
from script.枚举冫十进位制素数冃时分秒扌 import *
