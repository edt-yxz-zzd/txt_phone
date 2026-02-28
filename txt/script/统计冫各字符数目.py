#__all__:goto
r'''[[[
e script/统计冫各字符数目.py

script.统计冫各字符数目
py -m nn_ns.app.debug_cmd   script.统计冫各字符数目 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.统计冫各字符数目:__doc__ -ht # -ff -df
#######

[[
源起:
    找出一个字符，用于替代转义符『\』『&』『%』『&』
    感觉『~』『!』『`』不错:
        『!』用作 我的『因为』『!!』
        『?』用作 我的特称量词
        『@』用作 我的全称量词、蟒语函数的修饰词标记
        『^』用作 TeX上标符、正则表达式的行首锚
        『|』???怎么那么多？ ！用作 纵线乊制表！
        『`』用作 Haskell中介算子双端标识、注释中函数参数标记

===
e others/数学/编程/设计/单字符冃转义符.txt
之前，设想过，使用 双字符转义符『?!』(!?是)，但是 不能满足需求:『转义后字符串的串联依然是转义后字符串』并且『转义后字符串唯一』
    还是得考虑 单字符转义符
        不过 注意 避免使用『\\』这种模式，以免数据爆炸

#『?!』:view ../lots/NOTE/char/问叹号.txt
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   script.统计冫各字符数目   ,count_each_ascii_chars_ :TODO_www.txt +printable_only +to_separate
' etaoinsrhl1dc.2mpu/,03gf4y65b8w97-=v:x()SA_kTEP\\I]C[+ORMND>^"BF<LjHzWqG{}\'*U%JK?;Y#VX$Z@Q&|!~`'
[16480, 7581, 6049, 4708, 4653, 4539, 4482, 4187, 3900, 2886, 2833, 2636, 2438, 2407, 2145, 2098, 2026, 2022, 1882, 1780, 1721, 1690, 1469, 1393, 1391, 1353, 1200, 1195, 1130, 1127, 1104, 1091, 1023, 981, 856, 759, 746, 626, 616, 556, 556, 463, 456, 429, 409, 393, 336, 324, 324, 290, 271, 270, 269, 265, 216, 211, 194, 191, 189, 173, 169, 164, 161, 161, 152, 143, 130, 127, 126, 121, 109, 106, 96, 96, 92, 84, 82, 80, 79, 76, 72, 70, 67, 52, 46, 40, 30, 28, 21, 18, 11, 10, 9, 5, 0]


du -h script/
py_adhoc_call   script.统计冫各字符数目   ,count_each_ascii_chars_ :script/png/site-packages/png +printable_only +to_separate
' ertaisnoldhpcfum).|gybw,_(`":=\'kx/v-NRz}#0PTG]jS1[EI*ABZC2FD3<W%L8MH>q4!O6+5;$VY\\U@7&XJ9K?{Q^~'
[49668, 13974, 10679, 10593, 7852, 7612, 7171, 6224, 6156, 5518, 5268, 3696, 3646, 3344, 3315, 2700, 2551, 2094, 2069, 1977, 1859, 1800, 1655, 1632, 1591, 1590, 1589, 1187, 1165, 1109, 1027, 956, 914, 895, 793, 775, 657, 640, 607, 581, 576, 544, 537, 518, 516, 493, 490, 470, 464, 455, 435, 424, 424, 419, 416, 379, 377, 312, 268, 264, 262, 249, 236, 210, 207, 205, 190, 180, 173, 166, 166, 154, 152, 149, 140, 135, 129, 104, 100, 92, 88, 81, 76, 55, 54, 45, 45, 43, 38, 35, 26, 26, 23, 18, 10]



du -h /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/
    13M
py_adhoc_call   script.统计冫各字符数目   ,count_each_ascii_chars_ +printable_only +to_separate :/sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/
' etaonisr-lcdhupm"f.bgy*=w,_v)(TPxk\':SIAEC1>320NORFL|j4DM+5U689zq7BW/HG[]~;VY#XK<{}\\%ZJQ?!^@$&`'
[2279162, 1008575, 747205, 584638, 576213, 571927, 557959, 537653, 511865, 360390, 338648, 299605, 298681, 275910, 228616, 214618, 198841, 180342, 174117, 169300, 145359, 142278, 134852, 105376, 103334, 90397, 83399, 74722, 71446, 70558, 70533, 49890, 49081, 47364, 45299, 42226, 40605, 33788, 33368, 31710, 31272, 30200, 29591, 27695, 27568, 25966, 24935, 22197, 21563, 21171, 19761, 19682, 19059, 18392, 16276, 15705, 15283, 13849, 13054, 12781, 12365, 11724, 11364, 11052, 10810, 10058, 9863, 9309, 9169, 8294, 7433, 7128, 7111, 5194, 4859, 4265, 3928, 3646, 3400, 3178, 2543, 2405, 2385, 2266, 1853, 1473, 1456, 1336, 1075, 820, 742, 663, 565, 482, 214]



' etaoinsrhl1dc.2mpu/,03gf4y65b8w97-=v:x()SA_kTEP\\I]C[+ORMND>^"BF<LjHzWqG{}\'*U%JK?;Y#VX$Z@Q&|!~`'
' ertaisnoldhpcfum).|gybw,_(`":=\'kx/v-NRz}#0PTG]jS1[EI*ABZC2FD3<W%L8MH>q4!O6+5;$VY\\U@7&XJ9K?{Q^~'
' etaonisr-lcdhupm"f.bgy*=w,_v)(TPxk\':SIAEC1>320NORFL|j4DM+5U689zq7BW/HG[]~;VY#XK<{}\\%ZJQ?!^@$&`'


]]]'''#'''
__all__ = r'''
count_each_ascii_chars_
count_each_bytes_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from pathlib import Path
import os
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_len_eq
from seed.iters.unzip import unzip
___end_mark_of_excluded_global_names__0___ = ...


def count_each_ascii_chars_(*ipaths, may_jbyte2count=None, printable_only=False, to_separate=False):
    j2n = count_each_bytes_(*ipaths, may_jbyte2count=may_jbyte2count)
    j2n = j2n[:0x80]
    c_n_pairs = [(chr(j), n) for j, n in enumerate(j2n)]
    c_n_pairs.sort(reverse=True, key=lambda p:p[1])
    if printable_only:
        c_n_pairs = [(c, n) for c, n in c_n_pairs if c.isprintable()]
    if to_separate:
        (cs, ns) = unzip(2, c_n_pairs)
        s = ''.join(cs)
        return (s, ns)
    return c_n_pairs
def count_each_bytes_(*ipaths, may_jbyte2count=None):
    j2n = [0]*256 if may_jbyte2count is None else may_jbyte2count
    check_type_is(list, j2n)
    check_len_eq(256, j2n)
    for ipath in map(Path, ipaths):
        if ipath.is_dir():
            ipath7dir = ipath
            #for parent, children7dir, children7file in ipath7dir.walk():
            for parent, children7dir, children7file in os.walk(ipath7dir):
                parent = Path(parent)
                for fnm in children7file:
                    ipath4file = parent/fnm
                    _acc_(j2n, ipath4file)
                j2n
            j2n
        else:
            ipath7file = ipath
            _acc_(j2n, ipath7file)
            j2n
        j2n
    j2n
    return j2n
BLOCK_SIZE = 2**20 # == 1MB
def _acc_(j2n, ifname, /):
    #if 0b0001:print(ifname)
    with open(ifname, 'rb') as ibfile:
        while (bs:=ibfile.read(BLOCK_SIZE)):
            for u in bs:
                j2n[u] += 1
    return


__all__
from script.统计冫各字符数目 import count_each_ascii_chars_, count_each_bytes_
from script.统计冫各字符数目 import *
