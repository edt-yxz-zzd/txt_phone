#__all__:goto
r'''[[[
e script/解读冫二进制文件冃靶值讠最小显链长.py
view others/数学/最短加链/最短加链-www-wwwhomes.uni-bielefeld.de.txt

script.解读冫二进制文件冃靶值讠最小显链长
py -m nn_ns.app.debug_cmd   script.解读冫二进制文件冃靶值讠最小显链长 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.解读冫二进制文件冃靶值讠最小显链长:__doc__ -ht # -ff -df
#######

[[
『The uncompressed values are coded as ℓ(n)-λ(n)-ceil(log2(v(n))) into 2 bits each which the exception of ℓ(2135101487) #.』
  view others/数学/最短加链/最短加链--py_doc-www-杂录.txt
>>> (2135101487).bit_length()
31
>>> 2**30 < 2135101487 < 2**31
True

hexdump -n 0x100 -s 0x0 -C /sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat

]]
[[
文件格式牜不带表格:
view /sdcard/0my_files/tmp/wget_/new/wwwhomes.uni-bielefeld.de/achim/ddt.c
         /* only exception below 2^31 */
         m = lb+k + (no!=2135101487U ? c&(1<<TWO)-1 : 4);

  # [靶值<2**31] => 唯一例外{not 0<=编码值<=3}:2135101487{编码值==4}
  文件格式{add31.bits}:
  [文件牜不带表格==(负载区)]
  [负载区==bytes{len==最大靶值///4}]
  [靶值 <= 2**31]
  [编码值{靶值} == if 靶值 == 2135101487 then 4 else let [(q,r):=(靶值-1)/%4] in (负载区[q] >> (2*r))&0b011]
    #例外:2135101487
  [最小显链长{靶值} == 首爻位{靶值} +ceil_log2(阳爻数{靶值}) +编码值{靶值}]
]]
]]
[[
文件格式牜带表格:
view /sdcard/0my_files/tmp/wget_/new/wwwhomes.uni-bielefeld.de/achim/ddt4ln.c
  #使用表格后无需例外:2135101487
  # [靶值<2**31] => 唯一例外{not 0<=编码值<=3}:2135101487{编码值==4}
  文件格式{addXX.4ln}:
  [文件牜带表格==(表格区,负载区)]
  [表格区==(表格规模::uint32le{<256},表格::[bytes{len==4}]{len==表格规模})]
  [负载区==bytes{len==最大靶值///4}]
  [编码值{靶值} == let [(q,r):=(靶值-1)/%4] in 表格[负载区[q]][r]]
    #使用表格后无需例外:2135101487
  [最小显链长{靶值} == 首爻位{靶值} +ceil_log2(阳爻数{靶值}) +编码值{靶值}]
]]



'#'; __doc__ = r'#'
>>>


[[
最大靶值纟中断文件
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @求取冫最大靶值巛二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat'
    7320000
>>> (7320000).bit_length()
23
>>> 2**22 < 7320000 < 2**23
True
>>> 7320000 - 2**22
3125696
>>> 7320000 - 2**23
-1068608

===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @求取冫最大靶值巛二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add32.4ln-靶值首爻位小于三十二牜不完整.dat'
    131157856
>>> (131157856).bit_length()
27
>>> 2**26 < 131157856 < 2**27
True
>>> 131157856 -2**26
64048992
>>> 131157856 -2**27
-3059872
>>> 131157856/7320000
17.917739890710383

===
]]


[[
校验中断文件
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举解读冫二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat'  ='range(1,100)'
xxx:py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @内置校验冫二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat' =None
    IndexError: tuple index out of range
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @内置校验冫二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat' ='range(1,100001)'
    ok
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @内置校验冫二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add32.4ln-靶值首爻位小于三十二牜不完整.dat' ='range(1,100001)'
    ok
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @对照校验冫二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat'  :'/sdcard/0my_files/unzip/addition_chain/add32.4ln-靶值首爻位小于三十二牜不完整.dat' ='None'
    ok
]]


copy_to:view others/数学/最短加链/最短加链-www-wwwhomes.uni-bielefeld.de.txt
[[
转换格式丶打包存档:add31.bits不完整
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat' =100
...py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat' =-1 >>  /sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt
du -h /sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt
    14M
view /sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt

tar -cJvf /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz   -C $my_tmp/out4py/   script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt
du -h /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz
    712K # < 820K #看来压缩程序对二进制文件不友好
tar -tvf /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz
tar -xvf /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz -O | more
cp -iv /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz ../../python3_src/nn_ns/math_nn/numbers/
du -h ../../python3_src/nn_ns/math_nn/numbers/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz
    712K
du -h ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py
    912K
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver2.py
    #解码加载:耗时8秒！
        DONE:_ignore__tmp/解包后缓存
    du -h ../../python3_src/nn_ns/math_nn/numbers/_ignore__tmp/靶值讠最小显链长.le7320000.pickle
        14M

]]
[[
转换格式丶打包存档:add32.4ln不完整
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add32.4ln-靶值首爻位小于三十二牜不完整.dat' =100
...py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add32.4ln-靶值首爻位小于三十二牜不完整.dat' =-1 >>  /sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le131157856.out.txt
    耗时十几分钟
du -h /sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le131157856.out.txt
    251M
wc -l -c /sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le131157856.out.txt
    =>『131157856 262315712』
    #num_lines,num_bytes

tar -cJvf /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le131157856.txt.txz   -C $my_tmp/out4py/   script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le131157856.out.txt
du -h /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le131157856.txt.txz
    14M # > 13M #二进制文件压缩率更高:这里不同上面
tar -tvf /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le131157856.txt.txz
tar -xvf /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le131157856.txt.txz -O | more
#no:cp -iv /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le131157856.txt.txz ../../python3_src/nn_ns/math_nn/numbers/
#no:du -h ../../python3_src/nn_ns/math_nn/numbers/偏移值文本冃靶值讠最小显链长.le131157856.txt.txz

]]
[[
view /sdcard/0my_files/tmp/wget_/new/wwwhomes.uni-bielefeld.de/achim/correct_ln.txt
    『correct is:   l(2597275) = l(2964271) = l(3187103) = l(3731944) = 26』

ns='[2597275,2964271,3187103,3731944]'
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举解读冫二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat'  ="$ns"
    26
    26
    26
    26

]]



[[
偏移值丶首发靶值
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举冫偏移值辻首发靶值巛二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat'  =100
    (0, 1)
    (1, 29)
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举冫偏移值辻首发靶值巛二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add32.4ln-靶值首爻位小于三十二牜不完整.dat'  =100
    (0, 1)
    (1, 29)
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举冫偏移值字符辻首发靶值巛偏移值文本文件扌 :'/sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt'  =100 -is_tarfile
    ('0', 1)
    ('1', 29)
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举冫偏移值字符辻首发靶值巛偏移值文本文件扌 :'/sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz'  =100 +is_tarfile
    ('0', 1)
    ('1', 29)
===
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举冫偏移值字符辻首发靶值巛偏移值文本文件扌 :'/sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz'  =-1 +is_tarfile
    ('0', 1)
    ('1', 29)
    ('2', 3691)
    ('3', 919627)
===
...py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举冫偏移值字符辻首发靶值巛偏移值文本文件扌 :'/sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le131157856.out.txt'  =-1 -is_tarfile
        #费时:251M
    ('0', 1)
    ('1', 29)
    ('2', 3691)
    ('3', 919627)
        !! 中断先于:131157856<2135101487首发例外
===
7z a -t7z    /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le131157856.txt.7z    '/sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le131157856.out.txt'
du -h /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le131157856.txt.7z
    16M
    #7z:16M > txz:14M > 下载中断:13M

rm -iv /sdcard/0my_files/zip/addition_chain/偏移值文本冃靶值讠最小显链长.le131157856.txt.7z
rm -iv '/sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le131157856.out.txt'

===
]]
[[
count_each_chars -ie ascii -i /sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt
    ,'\n':7320000
    ,'0':672651
    ,'1':5349930
    ,'2':1297218
    ,'3':201
1:最多
2:次多
0:次少
3:最少
    能否有更佳的下界估值公式以消除上面的偏移值一？

首发靶值{偏移值}:
    ('0', 1)
    ('1', 29)
    ('2', 3691)
    ('3', 919627)
>>> (29).bit_count()
4
>>> (3691).bit_count()
8
>>> (919627).bit_count()
8
>>> bin(29)
'0b11101'
>>> bin(3691)
'0b111001101011'
>>> bin(919627)
'0b11100000100001001011'

py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举冫偏移值字符辻首发靶值巛偏移值文本文件扌 :'/sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt'  =100 -is_tarfile --至多几个=2
    ('0', 1)
    ('0', 2)
    ('1', 29)
    ('1', 53)

py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   ,枚举冫偏移值字符辻首发靶值巛偏移值文本文件扌 :'/sdcard/0my_files/tmp/out4py/script.解读冫二进制文件冃靶值讠最小显链长..转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌.le7320000.out.txt'  =10000 -is_tarfile --至多几个=10
    ('0', 1)
    ('0', 2)
    ('0', 3)
    ('0', 4)
    ('0', 5)
    ('0', 6)
    ('0', 7)
    ('0', 8)
    ('0', 9)
    ('0', 10)
    ('1', 29)
    ('1', 53)
    ('1', 57)
    ('1', 58)
    ('1', 71)
    ('1', 89)
    ('1', 101)
    ('1', 105)
    ('1', 106)
    ('1', 113)
    ('2', 3691)
    ('2', 3755)
    ('2', 3763)
    ('2', 3787)
    ('2', 6319)
    ('2', 6331)
    ('2', 6491)
    ('2', 6703)
    ('2', 7243)
    ('2', 7247)

>>> ns=[29,53,57,58,71,89,101,105,106,113,   3691,3755,3763,3787,6319,6331,6491,6703,7243,7247]
>>> [n.bit_count() for n in ns] #未必是二幂
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 7, 8]



]]


[[
py_adhoc_call   seed.io.decompress_truncated_file   @count_uncompression_bytes4truncated_compression_file_ :bz2 :ipath :'../../python3_src/nn_ns/math_nn/numbers/偏移值二爻冃靶值讠最小显链长.le7320000.le7322932[add31.bits-中断].bz2'
    =>:1830733

#no:cp -iv /sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat '../../python3_src/nn_ns/math_nn/numbers/偏移值二爻冃靶值讠最小显链长.le7320000[add31.bits-中断].dat'
stat /sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat
    =>:1830000 bytes
py.bz2解压实测:
    =>:1830733 bytes
du -h /sdcard/0my_files/tmp/wget_/wwwhomes.uni-bielefeld.de/achim/add31.bits.bz2
  820K#中断
cp -iv /sdcard/0my_files/tmp/wget_/wwwhomes.uni-bielefeld.de/achim/add31.bits.bz2  '../../python3_src/nn_ns/math_nn/numbers/偏移值二爻冃靶值讠最小显链长.le7320000.le7322932[add31.bits-中断].bz2'

e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver3.py
测试:
    ++kw:ver@内置校验冫二进制文件冃靶值讠最小显链长扌
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @内置校验冫二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add32.4ln-靶值首爻位小于三十二牜不完整.dat' ='range(1,1+7322932)' --ver=3
    ok
py_adhoc_call   script.解读冫二进制文件冃靶值讠最小显链长   @内置校验冫二进制文件冃靶值讠最小显链长扌 :'/sdcard/0my_files/unzip/addition_chain/add32.4ln-靶值首爻位小于三十二牜不完整.dat' ='range(7320000,1+7322932)' --ver=3
    ok

]]

factor -h 7320000
    7320000: 2^6 3 5^4 61


from script.解读冫二进制文件冃靶值讠最小显链长 import *
]]]'''#'''
__all__ = r'''

转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌
枚举解读冫二进制文件冃靶值讠最小显链长扌
    求取冫最大靶值巛二进制文件冃靶值讠最小显链长扌
内置校验冫二进制文件冃靶值讠最小显链长扌
对照校验冫二进制文件冃靶值讠最小显链长扌


枚举冫偏移值辻首发靶值巛二进制文件冃靶值讠最小显链长扌
    枚举冫靶值辻偏移值巛二进制文件冃靶值讠最小显链长扌
枚举冫偏移值字符辻首发靶值巛偏移值文本文件扌
    枚举冫靶值辻偏移值字符巛偏移值文本文件扌


枚举冫特征值辻前几个键值巛序列纟键值辻特征值扌
    枚举冫特征值辻首发键值巛序列纟键值辻特征值扌

鬽序列纟靶值巛毝最大靶值扌
解读冫编码值讠最小显链长纟靶值扌
ibfile2num_bytes_
read_eq_
read_uint32le_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
from io import SEEK_END
___end_mark_of_excluded_global_names__0___ = ...




def _work_on_ifile_or_ipath_(ipath_or_ifile, f, /, *, encoding):
    assert encoding
    return _work_on_ixfile_or_ipath_(ipath_or_ifile, f, xencoding=encoding)
def _work_on_ibfile_or_ipath_(ipath_or_ibfile, f, /):
    return _work_on_ixfile_or_ipath_(ipath_or_ibfile, f, xencoding=None)
def _work_on_ixfile_or_ipath_(ipath_or_ixfile, f, /, *, xencoding):
    if hasattr(ipath_or_ixfile, 'seek'):
        ixfile = ipath_or_ixfile
        yield from f(ixfile)
    else:
        ipath = ipath_or_ixfile
        _mode = 'rt' if xencoding else 'rb'
        with open(ipath, _mode) as ixfile:
            yield from f(ixfile)
    return


def 解读冫编码值讠最小显链长纟靶值扌(靶值, 编码值, /):
    check_int_ge(1, 靶值)
    首爻位纟靶值 = -1+靶值.bit_length()
    阳爻数纟靶值 = 靶值.bit_count()

    首爻位纟阳爻数纟靶值 = -1+阳爻数纟靶值.bit_length()
    阳爻数纟阳爻数纟靶值 = 阳爻数纟靶值.bit_count()

    欤阳爻数是二幂 = (阳爻数纟阳爻数纟靶值 == 1)
    ceil_log2_阳爻数纟靶值 = 首爻位纟阳爻数纟靶值 +(1-欤阳爻数是二幂)
    最小显链长纟靶值 = 首爻位纟靶值 +ceil_log2_阳爻数纟靶值 +编码值
    return 最小显链长纟靶值

#_例外靶值讠编码值 = {2135101487:4}
assert 0x80_00_00_00 == 2**31
def _解读冫二进制文件冃靶值讠编码值扌(鬽表格辻偏移纟负载区, ibfile, 靶值, /):
    check_int_ge(1, 靶值)
    def f(偏移纟负载区, 靶值, /):
        u = 靶值-1
        #(offset7bytes, offset7bits) = divmod(u*2, 8)
        (offset7bytes, half_offset7bits) = divmod(u, 4)
        ibfile.seek(偏移纟负载区+offset7bytes)
        bs = ibfile.read(1)
        if not bs:
            raise OverflowError(靶值)#EOFError#Exception()
        [uint8] = bs
        return (half_offset7bits, uint8)
    def 乊无表格乊非例外扌(偏移纟负载区, 靶值, /):
        (half_offset7bits, uint8) = f(偏移纟负载区, 靶值)
        offset7bits = 2*half_offset7bits
        v = uint8 >> offset7bits
        编码值 = v&0b011
        assert 0 <= 编码值 <= 3
        return 编码值
    def 乊带表格扌(表格, 偏移纟负载区, 靶值, /):
        (half_offset7bits, uint8) = f(偏移纟负载区, 靶值)
        try:
            编码值 = 表格[uint8][half_offset7bits]
        except:
            print(len(表格), uint8, half_offset7bits, 靶值)
            raise
        #不受限制:assert 0 <= 编码值 <= 4
        return 编码值

    (鬽表格, 偏移纟负载区) = 鬽表格辻偏移纟负载区
    if 鬽表格 is None:
        if not 靶值 <= 0x80_00_00_00:raise OverflowError(靶值)
        elif 靶值 == 2135101487:
            #if 靶值 in _例外靶值讠编码值:
            #   编码值 = _例外靶值讠编码值[靶值]
            编码值 = 4
        else:
            编码值 = 乊无表格乊非例外扌(偏移纟负载区, 靶值)
            assert 0 <= 编码值 <= 3
        编码值
        assert 0 <= 编码值 <= 4
    else:
        表格 = 鬽表格
        编码值 = 乊带表格扌(表格, 偏移纟负载区, 靶值)
        #不受限制:assert 0 <= 编码值 <= 4
    编码值
    return 编码值
def _解读冫二进制文件冃靶值讠最小显链长扌(鬽表格辻偏移纟负载区, ibfile, 靶值, /, *, 欤带靶值, 欤带编码值, 欤不带最小显链长):
    if 欤带编码值 or not 欤不带最小显链长:
        编码值 = _解读冫二进制文件冃靶值讠编码值扌(鬽表格辻偏移纟负载区, ibfile, 靶值)

    rs = []
    ######
    if 欤带靶值:
        rs.append(靶值)
    ######
    if 欤带编码值:
        rs.append(编码值)
    ######
    if not 欤不带最小显链长:
        最小显链长纟靶值 = 解读冫编码值讠最小显链长纟靶值扌(靶值, 编码值)
        rs.append(最小显链长纟靶值)
    ######

    #rs.reverse()
    return 最小显链长纟靶值 if len(rs) == 1 and not 欤不带最小显链长 else tuple(rs)
def ibfile2num_bytes_(ibfile, /):
    ibfile.seek(0, SEEK_END)
    num_bytes = ibfile.tell()
    return num_bytes
def _求取冫最大靶值巛二进制文件冃靶值讠最小显链长扌(偏移纟负载区, ibfile, /):
    num_bytes = ibfile2num_bytes_(ibfile)
    最大靶值 = (num_bytes-偏移纟负载区)*4
    return 最大靶值
def _枚举解读冫二进制文件冃靶值讠最小显链长扌(鬽表格辻偏移纟负载区, ibfile, 鬽序列纟靶值, /, *, 欤带靶值, 欤带编码值, 欤不带最小显链长):
    (鬽表格, 偏移纟负载区) = 鬽表格辻偏移纟负载区
    if 鬽序列纟靶值 is None:
        最大靶值 = _求取冫最大靶值巛二进制文件冃靶值讠最小显链长扌(偏移纟负载区, ibfile)
        序列纟靶值 = range(1, 1+最大靶值)
    else:
        序列纟靶值 = 鬽序列纟靶值
    序列纟靶值
    for 靶值 in 序列纟靶值:
        yield _解读冫二进制文件冃靶值讠最小显链长扌(鬽表格辻偏移纟负载区, ibfile, 靶值, 欤带靶值=欤带靶值, 欤带编码值=欤带编码值, 欤不带最小显链长=欤不带最小显链长)
def 枚举解读冫二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 鬽序列纟靶值, /, *, 欤带靶值=False, 欤带编码值=False, 欤不带最小显链长=False):
    check_type_is(bool, 欤带靶值)
    check_type_is(bool, 欤带编码值)
    check_type_is(bool, 欤不带最小显链长)
    def f(ibfile, /):
        鬽表格辻偏移纟负载区 = _读冫鬽表格辻偏移纟负载区巛二进制文件冃靶值讠最小显链长扌(ibfile)
        return _枚举解读冫二进制文件冃靶值讠最小显链长扌(鬽表格辻偏移纟负载区, ibfile, 鬽序列纟靶值, 欤带靶值=欤带靶值, 欤带编码值=欤带编码值, 欤不带最小显链长=欤不带最小显链长)
    return _work_on_ibfile_or_ipath_(ipath_or_ibfile, f)

def 求取冫最大靶值巛二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, /):
    def f(ibfile, /):
        (鬽表格, 偏移纟负载区) = 鬽表格辻偏移纟负载区 = _读冫鬽表格辻偏移纟负载区巛二进制文件冃靶值讠最小显链长扌(ibfile)
        yield _求取冫最大靶值巛二进制文件冃靶值讠最小显链长扌(偏移纟负载区, ibfile)
    [最大靶值] = _work_on_ibfile_or_ipath_(ipath_or_ibfile, f)
    return 最大靶值
def read_eq_(num_bytes, ibfile, /):
    if not num_bytes >= 0:raise TypeError
    bs = ibfile.read(num_bytes)
    if not len(bs) == num_bytes:raise EOFError
    return bs
def read_uint32le_(num_words, ibfile, /):
    bs = read_eq_(num_words*4, ibfile)
    us = tuple(int.from_bytes(bs[j:j+4], byteorder='little', signed=False) for j in range(0, len(bs), 4))
    return us
def _读冫鬽表格辻偏移纟负载区巛二进制文件冃靶值讠最小显链长扌(ibfile, /):
    '-> (鬽表格, 偏移纟负载区)'
    ibfile.seek(0)
    bs = ibfile.read(1)
    if bs and bs[0]:
        [num_words] = bs
        assert 0 < num_words < 256
        if any(read_eq_(3, ibfile)):raise Exception('too big:表格规模')
        bs = read_eq_(num_words*4, ibfile)
        bss = tuple(bs[j:j+4] for j in range(0, len(bs), 4))
        鬽表格 = 表格 = bss
        偏移纟负载区 = ibfile.tell()
    else:
        鬽表格 = None
        偏移纟负载区 = 0
    鬽表格
    偏移纟负载区
    return (鬽表格, 偏移纟负载区) #鬽表格辻偏移纟负载区

def _靶值讠最小显链长_(ver=0):
    match ver:
        case 0:
            from seed.math.power.addition_chain.data.target_uint2may_len_optimal_addition_chain import 靶值讠最小显链长
        case 3:
            from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3 import 取冫靶值讠最小显链长扌
            靶值讠最小显链长 = 取冫靶值讠最小显链长扌()
    return 靶值讠最小显链长


def 内置校验冫二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 鬽序列纟靶值, /, *, ver=0):
    ts = 枚举解读冫二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 鬽序列纟靶值, 欤带靶值=True, 欤带编码值=True)
    靶值讠最小显链长 = _靶值讠最小显链长_(ver=ver)
    L = len(靶值讠最小显链长)
    ordered = 鬽序列纟靶值 is None
    #for 靶值 in range(1, L):
    for (靶值, 编码值, 最小显链长) in ts:
        if ordered and not 靶值 < L:
            break
        assert 最小显链长 == 靶值讠最小显链长[靶值], ((靶值, 编码值, 最小显链长), 靶值讠最小显链长[靶值])
def 对照校验冫二进制文件冃靶值讠最小显链长扌(lhs_ipath_or_ibfile, rhs_ipath_or_ibfile, 鬽序列纟靶值, /):
    if 鬽序列纟靶值 is None:
        x = (None, None)
    else:
        from itertools import tee
        x = tee(鬽序列纟靶值)
    (lhs_鬽序列纟靶值, rhs_鬽序列纟靶值) = x
    lhs_ts = 枚举解读冫二进制文件冃靶值讠最小显链长扌(lhs_ipath_or_ibfile, lhs_鬽序列纟靶值, 欤带靶值=True, 欤带编码值=True)
    rhs_ts = 枚举解读冫二进制文件冃靶值讠最小显链长扌(rhs_ipath_or_ibfile, rhs_鬽序列纟靶值, 欤带靶值=True, 欤带编码值=True)
    for lhs_tpl, rhs_tpl in zip(lhs_ts, rhs_ts):
        assert lhs_tpl == rhs_tpl, (lhs_tpl, rhs_tpl)


def 鬽序列纟靶值巛毝最大靶值扌(毝最大靶值, /):
    check_int_ge(-1, 毝最大靶值)
    if 毝最大靶值 > 0:
        最大靶值 = 毝最大靶值
        鬽序列纟靶值 = 序列纟靶值 = range(1, 1+最大靶值)
    else:
        鬽序列纟靶值 = None
    鬽序列纟靶值
    return 鬽序列纟靶值

def 枚举冫靶值辻偏移值巛二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 毝最大靶值=-1, /):
    鬽序列纟靶值 = 鬽序列纟靶值巛毝最大靶值扌(毝最大靶值)
    ts = 枚举解读冫二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 鬽序列纟靶值, 欤带靶值=True, 欤带编码值=True, 欤不带最小显链长=True)
    for (靶值, 编码值) in ts:
        yield (靶值, 编码值)

def 转存冫偏移值文本巛二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 毝最大靶值=-1, /):
    from seed.text.mk_char_pt_ranges5predicator import alnum_ascii_sorted_chars
    def _print(ch, /):
        #print(ch, end='')
        print(ch)
    #_print('-')
    ts = 枚举冫靶值辻偏移值巛二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 毝最大靶值)
    for (靶值, 编码值) in ts:
        ch = alnum_ascii_sorted_chars[编码值]
        _print(ch)


def 枚举冫特征值辻首发键值巛序列纟键值辻特征值扌(序列纟键值辻特征值, /):
    s = set()
    for (键值, 特征值) in 序列纟键值辻特征值:
        if not 特征值 in s:
            s.add(特征值)
            yield (特征值, 键值)
def 枚举冫特征值辻前几个键值巛序列纟键值辻特征值扌(序列纟键值辻特征值, 至多几个, /):
    if 至多几个 == 1:
        return 枚举冫特征值辻首发键值巛序列纟键值辻特征值扌(序列纟键值辻特征值)
    return _枚举冫特征值辻前几个键值巛序列纟键值辻特征值扌(序列纟键值辻特征值, 至多几个)
def _枚举冫特征值辻前几个键值巛序列纟键值辻特征值扌(序列纟键值辻特征值, 至多几个, /):
    check_int_ge(1, 至多几个)
    d = {}
    for (键值, 特征值) in 序列纟键值辻特征值:
        ok = True
        #d.setdefault()
        if not 特征值 in d:
            d[特征值] = 1
        else:
            n = d[特征值]
            if n == 至多几个:
                ok = False
            else:
                ok
                d[特征值] = 1+n
            ok
        ok
        if ok:
            yield (特征值, 键值)

def 枚举冫偏移值辻首发靶值巛二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 毝最大靶值=-1, /, *, 至多几个=1):
    '-> (偏移值, 首发靶值{偏移值})'
    ts = 枚举冫靶值辻偏移值巛二进制文件冃靶值讠最小显链长扌(ipath_or_ibfile, 毝最大靶值)
    #for (靶值, 偏移值) in ts:
    #.return 枚举冫特征值辻首发键值巛序列纟键值辻特征值扌(ts)
    return _枚举冫特征值辻前几个键值巛序列纟键值辻特征值扌(ts, 至多几个)

def 枚举冫偏移值字符辻首发靶值巛偏移值文本文件扌(ipath_or_ifile, 毝最大靶值=-1, /, *, 至多几个=1, is_tarfile=False):
    '-> (偏移值字符, 首发靶值{偏移值字符})'
    ts = 枚举冫靶值辻偏移值字符巛偏移值文本文件扌(ipath_or_ifile, 毝最大靶值, is_tarfile=is_tarfile)
    #for (靶值, 偏移值字符) in ts:
    #.return 枚举冫特征值辻首发键值巛序列纟键值辻特征值扌(ts)
    return _枚举冫特征值辻前几个键值巛序列纟键值辻特征值扌(ts, 至多几个)

def 枚举冫靶值辻偏移值字符巛偏移值文本文件扌(ipath_or_ifile, 毝最大靶值=-1, /, *, is_tarfile=False):
    check_int_ge(-1, 毝最大靶值)
    check_type_is(bool, is_tarfile)


    def f(lines, /):
        it = map(str.strip, lines)
        if not 毝最大靶值 == -1:
            最大靶值 = 毝最大靶值
            from itertools import islice
            it = islice(it, 0, 最大靶值)
        it
        for 靶值, 偏移值字符 in enumerate(it, 1):
            yield (靶值, 偏移值字符)
    #end-def f(lines, /):


    if is_tarfile:
        from seed.for_libs.for_tarfile import iter_read_solo_tarfile_
        #def iter_read_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}):
        iter_lines = iter_read_solo_tarfile_(ipath_or_ifile, xencoding4data='ascii')
        it = f(iter_lines)
    else:
        it = _work_on_ifile_or_ipath_(ipath_or_ifile, f, encoding='ascii')
    it
    return it

__all__
from script.解读冫二进制文件冃靶值讠最小显链长 import *
