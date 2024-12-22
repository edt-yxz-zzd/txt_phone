#__all__:goto
r'''[[[
e script/搜索冫最短加链长度.py
    蛮力搜索@20241220
optimal addition chain
see:
    view script/搜索冫最短加链长度.py..statistics.out.txt
    view ../../python3_src/seed/for_libs/for_tarfile.py
        py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii
see:
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py
    view others/数学/最小加法链.txt
see:
    view ../../python3_src/seed/io/continue_io.py
    view ../../python3_src/seed/for_libs/for_signal.py

script.搜索冫最短加链长度
py -m nn_ns.app.debug_cmd   script.搜索冫最短加链长度 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.搜索冫最短加链长度:__doc__ -ht # -ff -df



[[
最大化冫次极大值纟加链:
===
[1, ..., a, ..., z; n]
[1, ..., b, ..., c, ..., y, z; n]
[1 <= a <= z < n]
[1 <= b <= c <= y < z < n]
[n >= 3]
[z >= 2]
[2*y >= z]
[2*z >= n]

below assume: [n >= 3][n > 2**floor_log2_(n)]
[?(a,b,c) :=> [n == z + a][z == b + c][b <= c]]
    # to adjust to [a' <= b' <= c']
[n == (b+c) + a]
[len{a,b,c}==3]:
    只要能分解成三个不同整数，就可依加法交换律调整:最大化z(最小化a)
[len{a,b,c}==2]:
    ...最糟况态
[len{a,b,c}==1]:
    乘法分解:或可调整乘法因子的相乘次序
[y <- {a,b,c}]
!! [b <= c < z]
[y <- {a,c}]

!! [a <= z]
* [a == z]:
    [y < z == a]
    !! [y <- {a,c}]
    [c == y]
    [n == 2*z]
    [1, ..., b, ..., c==y, z; n]
    -->:
    [1, 2*1, ..., 2*b, ..., 2*c==2*y; 2*z==n]
    !! [2*y >= z]
    * [2*y == z]:
        [n == 2*z == 4*y]
        -->: [1, 2, 4*1, ...; 4*y=n]
        ... ...
        unless [n == 2**e]
        otherwise eventually fall into case [2*y > z]
        !! [n > 2**floor_log2_(n)]
    * [2*y > z]:
        ... got a addition_chain with  bigger z
* [a < z]:

]]


>>> def show_(xs, /):
...     for x in xs:
...         print(x)
>>> show_(搜索冫最短加链长度牜批量扌(range(1,13), brief=False))
(1, True, 0)
(1,)
(2, True, 1)
(1, 2)
(3, True, 2)
(1, 2, 3)
(4, True, 2)
(1, 2, 4)
(5, True, 3)
(1, 2, 4, 5)
(1, 2, 3, 5)
(6, True, 3)
(1, 2, 4, 6)
(1, 2, 3, 6)
(7, True, 4)
(1, 2, 4, 6, 7)
(1, 2, 4, 5, 7)
(1, 2, 3, 6, 7)
(1, 2, 3, 5, 7)
(1, 2, 3, 4, 7)
(8, True, 3)
(1, 2, 4, 8)
(9, True, 4)
(1, 2, 4, 8, 9)
(1, 2, 4, 5, 9)
(1, 2, 3, 6, 9)
(10, True, 4)
(1, 2, 4, 8, 10)
(1, 2, 4, 6, 10)
(1, 2, 4, 5, 10)
(1, 2, 3, 5, 10)
(11, True, 5)
(1, 2, 4, 8, 10, 11)
(1, 2, 4, 8, 9, 11)
(1, 2, 4, 6, 10, 11)
(1, 2, 4, 6, 7, 11)
(1, 2, 4, 5, 10, 11)
(1, 2, 4, 5, 9, 11)
(1, 2, 4, 5, 7, 11)
(1, 2, 4, 5, 6, 11)
(1, 2, 3, 6, 9, 11)
(1, 2, 3, 6, 8, 11)
(1, 2, 3, 5, 10, 11)
(1, 2, 3, 5, 8, 11)
(1, 2, 3, 5, 6, 11)
(1, 2, 3, 4, 8, 11)
(1, 2, 3, 4, 7, 11)
(12, True, 4)
(1, 2, 4, 8, 12)
(1, 2, 4, 6, 12)
(1, 2, 3, 6, 12)

>>> show_(搜索冫最短加链长度牜批量扌(range(1,51), brief=True))
(1, 0, (1,))
(2, 1, (1, 2))
(3, 2, (1, 2, 3))
(4, 2, (1, 2, 4))
(5, 3, (1, 2, 4, 5))
(6, 3, (1, 2, 4, 6))
(7, 4, (1, 2, 4, 6, 7))
(8, 3, (1, 2, 4, 8))
(9, 4, (1, 2, 4, 8, 9))
(10, 4, (1, 2, 4, 8, 10))
(11, 5, (1, 2, 4, 8, 10, 11))
(12, 4, (1, 2, 4, 8, 12))
(13, 5, (1, 2, 4, 8, 12, 13))
(14, 5, (1, 2, 4, 8, 12, 14))
(15, 5, (1, 2, 4, 5, 10, 15))
(16, 4, (1, 2, 4, 8, 16))
(17, 5, (1, 2, 4, 8, 16, 17))
(18, 5, (1, 2, 4, 8, 16, 18))
(19, 6, (1, 2, 4, 8, 16, 18, 19))
(20, 5, (1, 2, 4, 8, 16, 20))
(21, 6, (1, 2, 4, 8, 16, 20, 21))
(22, 6, (1, 2, 4, 8, 16, 20, 22))
(23, 6, (1, 2, 4, 5, 9, 18, 23))
(24, 5, (1, 2, 4, 8, 16, 24))
(25, 6, (1, 2, 4, 8, 16, 24, 25))
(26, 6, (1, 2, 4, 8, 16, 24, 26))
(27, 6, (1, 2, 4, 8, 9, 18, 27))
(28, 6, (1, 2, 4, 8, 16, 24, 28))
(29, 7, (1, 2, 4, 8, 16, 24, 28, 29))
(30, 6, (1, 2, 4, 8, 10, 20, 30))
(31, 7, (1, 2, 4, 8, 10, 20, 30, 31))
(32, 5, (1, 2, 4, 8, 16, 32))
(33, 6, (1, 2, 4, 8, 16, 32, 33))
(34, 6, (1, 2, 4, 8, 16, 32, 34))
(35, 7, (1, 2, 4, 8, 16, 32, 34, 35))
(36, 6, (1, 2, 4, 8, 16, 32, 36))
(37, 7, (1, 2, 4, 8, 16, 32, 36, 37))
(38, 7, (1, 2, 4, 8, 16, 32, 36, 38))
(39, 7, (1, 2, 4, 8, 12, 13, 26, 39))
(40, 6, (1, 2, 4, 8, 16, 32, 40))
(41, 7, (1, 2, 4, 8, 16, 32, 40, 41))
(42, 7, (1, 2, 4, 8, 16, 32, 40, 42))
(43, 7, (1, 2, 4, 8, 9, 17, 34, 43))
(44, 7, (1, 2, 4, 8, 16, 32, 40, 44))
(45, 7, (1, 2, 4, 8, 9, 18, 36, 45))
(46, 7, (1, 2, 4, 8, 10, 18, 36, 46))
(47, 8, (1, 2, 4, 8, 12, 13, 26, 39, 47))
(48, 6, (1, 2, 4, 8, 16, 32, 48))
(49, 7, (1, 2, 4, 8, 16, 32, 48, 49))
(50, 7, (1, 2, 4, 8, 16, 32, 48, 50))

++kw:with_statistical_information
++_find_may_max_k4j__new_ver()
    verify compatibility here:
>>> show_(搜索冫最短加链长度牜批量扌(range(1,51), brief=True, with_statistical_information=True))
(1, 0, ((1,), (1, 0, 0)))
(2, 1, ((1, 2), (1, 0, 1)))
(3, 2, ((1, 2, 3), (1, 0, 4)))
(4, 2, ((1, 2, 4), (1, 0, 2)))
(5, 3, ((1, 2, 4, 5), (1, 0, 6)))
(6, 3, ((1, 2, 4, 6), (1, 0, 5)))
(7, 4, ((1, 2, 4, 6, 7), (1, 0, 12)))
(8, 3, ((1, 2, 4, 8), (1, 0, 3)))
(9, 4, ((1, 2, 4, 8, 9), (1, 0, 8)))
(10, 4, ((1, 2, 4, 8, 10), (1, 0, 7)))
(11, 5, ((1, 2, 4, 8, 10, 11), (1, 0, 16)))
(12, 4, ((1, 2, 4, 8, 12), (1, 0, 6)))
(13, 5, ((1, 2, 4, 8, 12, 13), (1, 0, 14)))
(14, 5, ((1, 2, 4, 8, 12, 14), (1, 0, 13)))
(15, 5, ((1, 2, 4, 5, 10, 15), (1, 8, 53)))
(16, 4, ((1, 2, 4, 8, 16), (1, 0, 4)))
(17, 5, ((1, 2, 4, 8, 16, 17), (1, 0, 10)))
(18, 5, ((1, 2, 4, 8, 16, 18), (1, 0, 9)))
(19, 6, ((1, 2, 4, 8, 16, 18, 19), (1, 0, 20)))
(20, 5, ((1, 2, 4, 8, 16, 20), (1, 0, 8)))
(21, 6, ((1, 2, 4, 8, 16, 20, 21), (1, 0, 18)))
(22, 6, ((1, 2, 4, 8, 16, 20, 22), (1, 0, 17)))
(23, 6, ((1, 2, 4, 5, 9, 18, 23), (1, 46, 264)))
(24, 5, ((1, 2, 4, 8, 16, 24), (1, 0, 7)))
(25, 6, ((1, 2, 4, 8, 16, 24, 25), (1, 0, 16)))
(26, 6, ((1, 2, 4, 8, 16, 24, 26), (1, 0, 15)))
(27, 6, ((1, 2, 4, 8, 9, 18, 27), (1, 15, 93)))
(28, 6, ((1, 2, 4, 8, 16, 24, 28), (1, 0, 14)))
(29, 7, ((1, 2, 4, 8, 16, 24, 28, 29), (1, 0, 28)))
(30, 6, ((1, 2, 4, 8, 10, 20, 30), (1, 9, 61)))
(31, 7, ((1, 2, 4, 8, 10, 20, 30, 31), (1, 55, 494)))
(32, 5, ((1, 2, 4, 8, 16, 32), (1, 0, 5)))
(33, 6, ((1, 2, 4, 8, 16, 32, 33), (1, 0, 12)))
(34, 6, ((1, 2, 4, 8, 16, 32, 34), (1, 0, 11)))
(35, 7, ((1, 2, 4, 8, 16, 32, 34, 35), (1, 0, 24)))
(36, 6, ((1, 2, 4, 8, 16, 32, 36), (1, 0, 10)))
(37, 7, ((1, 2, 4, 8, 16, 32, 36, 37), (1, 0, 22)))
(38, 7, ((1, 2, 4, 8, 16, 32, 36, 38), (1, 0, 21)))
(39, 7, ((1, 2, 4, 8, 12, 13, 26, 39), (1, 56, 386)))
(40, 6, ((1, 2, 4, 8, 16, 32, 40), (1, 0, 9)))
(41, 7, ((1, 2, 4, 8, 16, 32, 40, 41), (1, 0, 20)))
(42, 7, ((1, 2, 4, 8, 16, 32, 40, 42), (1, 0, 19)))
(43, 7, ((1, 2, 4, 8, 9, 17, 34, 43), (1, 88, 474)))
(44, 7, ((1, 2, 4, 8, 16, 32, 40, 44), (1, 0, 18)))
(45, 7, ((1, 2, 4, 8, 9, 18, 36, 45), (1, 73, 390)))
(46, 7, ((1, 2, 4, 8, 10, 18, 36, 46), (1, 59, 334)))
(47, 8, ((1, 2, 4, 8, 12, 13, 26, 39, 47), (1, 426, 3576)))
(48, 6, ((1, 2, 4, 8, 16, 32, 48), (1, 0, 8)))
(49, 7, ((1, 2, 4, 8, 16, 32, 48, 49), (1, 0, 18)))
(50, 7, ((1, 2, 4, 8, 16, 32, 48, 50), (1, 0, 17)))





view others/数学/最小加法链.txt
    不成立:最小加法链囗偶数猜想=[def]=???[@[k>=1] -> @[i>=0] -> [最少加法(k*2**i) == 最少加法(k)+i]]
    [存在反例382==191*2,最少加法(382)==11==最少加法(191)]
    #其他:
    [?[n>=1] -> [最少加法(2*n) < 最少加法(n)]]
      [[n==191] -> [最少加法(2*n) == 最少加法(n)]]
      [[n==30958077] -> [最少加法(4*n) == 最少加法(2*n) == 最少加法(n)]]
      [[n==375494703] -> [34 == 最少加法(2*n) < 最少加法(n) == 35]]
      [[n <- [1..<5784689]] -> [最少加法(2**n-1) <= 最少加法(n)+n-1]]
      [[n <- [1..=64]] -> [最少加法(2**n-1) == 最少加法(n)+n-1]]

>>> from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length__first_100000_terms as _n2sz
>>> for n in range(1, 233): #doctest: +SKIP
...     assert 最短加链长度扌(n) == _n2sz[n], (最短加链长度扌(n), _n2sz[n])
>>> 191*2
382
>>> 找出冫某一最短加链扌(191) #doctest: +SKIP
(191, 11, (1, 2, 4, 8, 16, 32, 48, 52, 53, 106, 159, 191))
>>> 找出冫某一最短加链扌(191*2) #doctest: +SKIP
(382, 11, (1, 2, 4, 8, 16, 17, 33, 50, 83, 166, 332, 382))
























py_adhoc_call   script.搜索冫最短加链长度   ,搜索冫最短加链长度牜批量扌 ='range(1,5)' -brief

#.py_adhoc_call   script.搜索冫最短加链长度   @可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py.out.patch-1-2104.statistics.txt  +with_statistical_information --may_max1_N=2104
#.py_adhoc_call   script.搜索冫最短加链长度   @可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py.out.txt  +with_statistical_information
#.view script/搜索冫最短加链长度.py.out.txt
#.du -h script/搜索冫最短加链长度.py.out.txt
#.py_adhoc_call   script.搜索冫最短加链长度   @校验冫输出文件纟可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py.out.txt
#.py_adhoc_call   script.搜索冫最短加链长度   @校验冫输出文件纟可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py.out.txt -allow_without_statistical_information
#.py_adhoc_call   script.搜索冫最短加链长度   @校验冫输出文件纟可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py.out.patch-1-2104.statistics.txt -allow_without_statistical_information
#.py_adhoc_call   script.搜索冫最短加链长度   ,排序冫输出文件纟可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py.out.patch-1-2104.statistics.txt

xxx:view /sdcard/0my_files/tmp/out4py/script.搜索冫最短加链长度.py.out.txt
cp -iv script/搜索冫最短加链长度.py.out.txt script/搜索冫最短加链长度.py..statistics.out.txt
e script/搜索冫最短加链长度.py..statistics.out.txt
    patch script/搜索冫最短加链长度.py..statistics.out.txt by script/搜索冫最短加链长度.py.out.patch-1-2104.statistics.txt

py_adhoc_call   script.搜索冫最短加链长度   @校验冫输出文件纟可重启运算纟任一最短加链扌 -allow_without_statistical_information  :script/搜索冫最短加链长度.py..statistics.out.txt
py_adhoc_call   script.搜索冫最短加链长度   ,排序冫输出文件纟可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py..statistics.out.txt
py_adhoc_call   script.搜索冫最短加链长度   @可重启运算纟任一最短加链扌  +with_statistical_information :script/搜索冫最短加链长度.py..statistics.out.txt

view script/搜索冫最短加链长度.py..statistics.out.txt
rm script/搜索冫最短加链长度.py.out.patch-1-2104.statistics.txt
rm script/搜索冫最短加链长度.py.out.txt

tar --create --verbose --file=script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --lzma script/搜索冫最短加链长度.py..statistics.out.txt
tar -cvf script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --lzma script/搜索冫最短加链长度.py..statistics.out.txt
view script/搜索冫最短加链长度.py..statistics.out.txt
    (1, 0, ((1,), (1, 0, 0)))
    ... ...
    (2173, 15, ((1, 2, 4, 8, 16, 32, 64, 128, 256, 272, 280, 281, 537, 818, 1636, 2173), (1, 2108288, 15261095)))
du -h script/搜索冫最短加链长度.py..statistics.out.txt
    188K
du -h script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma
    28K

tar --extract --verbose --file=script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma --to-stdout | more
tar -xvf script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma -O | more
    -C, --directory=DIR
tar -xf script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma -O | diff - script/搜索冫最短加链长度.py..statistics.out.txt -s
    Files - and script/搜索冫最短加链长度.py..statistics.out.txt are identical
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii  | diff - script/搜索冫最短加链长度.py..statistics.out.txt -s


py_adhoc_call   script.搜索冫最短加链长度   ,排序冫输出文件纟可重启运算纟任一最短加链扌 :script/搜索冫最短加链长度.py..statistics.out.txt
2173
(0, (1, 0, ((1,), (1, 0, 0))))
... ...
(16353919, (2047, 15, ((1, 2, 4, 8, 16, 32, 64, 128, 256, 288, 292, 584, 585, 1170, 1755, 2047), (1, 2038760, 16353919))))
30
(0, (1, 0, ((1,), (1, 0, 0))))
(1, (2, 1, ((1, 2), (1, 0, 1))))
(4, (3, 2, ((1, 2, 3), (1, 0, 4))))
(6, (5, 3, ((1, 2, 4, 5), (1, 0, 6))))
(12, (7, 4, ((1, 2, 4, 6, 7), (1, 0, 12))))
(16, (11, 5, ((1, 2, 4, 8, 10, 11), (1, 0, 16))))
(53, (15, 5, ((1, 2, 4, 5, 10, 15), (1, 8, 53))))
(264, (23, 6, ((1, 2, 4, 5, 9, 18, 23), (1, 46, 264))))
(494, (31, 7, ((1, 2, 4, 8, 10, 20, 30, 31), (1, 55, 494))))
(3576, (47, 8, ((1, 2, 4, 8, 12, 13, 26, 39, 47), (1, 426, 3576))))
(6288, (79, 9, ((1, 2, 4, 8, 16, 24, 26, 52, 78, 79), (1, 626, 6288))))
(6686, (93, 9, ((1, 2, 4, 8, 16, 20, 36, 72, 92, 93), (1, 868, 6686))))
(8228, (95, 9, ((1, 2, 4, 8, 16, 20, 21, 37, 74, 95), (1, 1147, 8228))))
(17697, (127, 10, ((1, 2, 4, 8, 16, 32, 40, 42, 84, 126, 127), (1, 1515, 17697))))
(23433, (143, 10, ((1, 2, 4, 8, 16, 32, 36, 37, 74, 111, 143), (1, 2732, 23433))))
(145864, (191, 11, ((1, 2, 4, 8, 16, 32, 48, 52, 53, 106, 159, 191), (1, 13355, 145864))))
(165328, (319, 11, ((1, 2, 4, 8, 16, 24, 25, 49, 98, 196, 294, 319), (1, 31206, 165328))))
(222142, (367, 11, ((1, 2, 4, 8, 9, 17, 34, 68, 77, 145, 290, 367), (1, 50257, 222142))))
(230645, (379, 12, ((1, 2, 4, 8, 16, 32, 64, 96, 104, 105, 210, 315, 379), (1, 21470, 230645))))
(357480, (383, 12, ((1, 2, 4, 8, 16, 32, 64, 80, 84, 85, 149, 298, 383), (1, 38578, 357480))))
(484038, (543, 12, ((1, 2, 4, 8, 16, 32, 36, 72, 144, 180, 181, 362, 543), (1, 89898, 484038))))
(543471, (559, 12, ((1, 2, 4, 8, 16, 32, 33, 66, 132, 165, 197, 394, 559), (1, 106512, 543471))))
(979041, (671, 13, ((1, 2, 4, 8, 16, 32, 64, 128, 136, 138, 266, 532, 670, 671), (1, 112057, 979041))))
(2611347, (767, 13, ((1, 2, 4, 8, 16, 32, 64, 72, 73, 137, 274, 347, 694, 767), (1, 415364, 2611347))))
(5189360, (1111, 14, ((1, 2, 4, 8, 16, 32, 64, 128, 192, 196, 197, 393, 786, 983, 1111), (1, 618902, 5189360))))
(6569756, (1151, 14, ((1, 2, 4, 8, 16, 32, 64, 128, 160, 164, 328, 329, 658, 987, 1151), (1, 842193, 6569756))))
(7052762, (1279, 14, ((1, 2, 4, 8, 16, 32, 64, 128, 136, 137, 201, 402, 539, 1078, 1279), (1, 1057913, 7052762))))
(7624790, (1519, 14, ((1, 2, 4, 8, 16, 32, 64, 96, 97, 194, 388, 485, 970, 1455, 1519), (1, 1376244, 7624790))))
(8938786, (1533, 14, ((1, 2, 4, 8, 16, 32, 64, 80, 81, 162, 242, 484, 968, 1452, 1533), (1, 1658265, 8938786))))
(16353919, (2047, 15, ((1, 2, 4, 8, 16, 32, 64, 128, 256, 288, 292, 584, 585, 1170, 1755, 2047), (1, 2038760, 16353919))))



cp -iv script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma script/搜索冫最短加链长度.py..statistics.le2173.out.txt.tar.lzma
tar -cvf script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --lzma script/搜索冫最短加链长度.py..statistics.out.txt
    2173,2862
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii

py_adhoc_call   script.搜索冫最短加链长度   @可重启运算纟任一最短加链扌  +with_statistical_information :script/搜索冫最短加链长度.py..statistics.out.txt

]]]'''#'''
__all__ = r'''
可重启运算纟任一最短加链扌
    校验冫输出文件纟可重启运算纟任一最短加链扌
    排序冫输出文件纟可重启运算纟任一最短加链扌

check_addition_chain_
找出冫某一最短加链扌
最短加链长度扌
搜索冫最短加链长度牜批量扌
    搜索冫最短加链长度扌
        搜索冫最短加链牜指定长度扌

'''.split()#'''
    # 罒乸可重启运算纟任一最短加链
    # _n2sz
__all__
___begin_mark_of_excluded_global_names__0___ = ...
if 0:
    #see:check_addition_chain_()
    from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length__first_100000_terms as _n2sz
from seed.tiny import print_err
from seed.tiny_.check import check_type_is, check_int_ge
from seed.for_libs.for_heapq import merge_ex
#def merge_ex(*sorted_iterable_exs, key4stable:[False,callable]=False, key4le=None, __le__=None, reverse=False, unique=False, obj2value_:[None,callable]=None):

from seed.io.continue_io import LineContinueIO, IValidatableLineContinueIO
from itertools import count as count_
from seed.for_libs.for_signal import PostponeKeyboardInterrupt
from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)

timer = timer__print_err__thread_wide

___end_mark_of_excluded_global_names__0___ = ...
(None
,0#1
,1#2
,2#3
,2#4
,3#5
,3#6
,4#7
,3#8
,4#9
,4#10
,5#11
,...
)

def 排序冫输出文件纟可重启运算纟任一最短加链扌(path, /, *, may_setting=None, key6statistics=-1, reverse=False, to_output_all_rows=True, to_output_max_rows=True):
    with_statistical_information = True
    校验冫输出文件纟可重启运算纟任一最短加链扌(path, may_setting=may_setting, allow_without_statistical_information=False)
        # !! with_statistical_information = True
    sf = 罒乸可重启运算纟任一最短加链.from_path_(may_setting, path, allow_create=False)
    max_k4sort = -1
    max_rows = []
    ls = []
    for line_value in sf.iter_read_line_values_():
        addition_chain = line_value
        (n, sz, us_ex) = addition_chain
        (us, statistics) = us_ex
            # !! with_statistical_information = True
        (num_fulfilled_uss, num_pops, num_checked_items) = statistics
        k4sort = statistics[key6statistics]
        row = (k4sort, addition_chain)
        ls.append(row)
        if max_k4sort < k4sort:
            max_k4sort = k4sort
            max_rows.append(row)
    ls.sort(reverse=reverse)
    if to_output_all_rows:
        total = len(ls)
        yield total
        yield from ls

    if to_output_max_rows:
        total4max_rows = len(max_rows)
        yield total4max_rows
        yield from max_rows

def 校验冫输出文件纟可重启运算纟任一最短加链扌(path, /, *, may_setting=None, to_validate_continuity:bool=True, to_validate_payload:bool=True, allow_with_statistical_information=True, allow_without_statistical_information=True):
    sf = 罒乸可重启运算纟任一最短加链.from_path_(may_setting, path, allow_create=False)
    sf.allow_with_statistical_information=allow_with_statistical_information
    sf.allow_without_statistical_information=allow_without_statistical_information
    sf.validate_whole_file_(to_validate_continuity=to_validate_continuity, to_validate_payload=to_validate_payload)
def 可重启运算纟任一最短加链扌(path, /, *, may_setting=None, may_prompt_string='\n\n    postpone_KeyboardInterrupt_until_subtask_switchover\n\n', to_postpone_KeyboardInterrupt_until_subtask_switchover:bool=True, allow_create:bool=True, verbose:bool=True, with_statistical_information=True, may_max1_N=None, to_check_optimal_if_known=True):
    罒乸可重启运算纟任一最短加链.run_or_resume_(may_setting, path
            , may_prompt_string=may_prompt_string
            , to_postpone_KeyboardInterrupt_until_subtask_switchover=to_postpone_KeyboardInterrupt_until_subtask_switchover
            , allow_create=allow_create
            , verbose=verbose
            , with_statistical_information=with_statistical_information
            , may_max1_N=may_max1_N
            , to_check_optimal_if_known=to_check_optimal_if_known
            )

class 罒乸可重启运算纟任一最短加链(IValidatableLineContinueIO):
    '[line_value == addition_chain == (n, sz, us_ex)] # [addition_chain :: (n/pint, sz/最短加链长度/uint, us_ex)] # [us_ex == (us if not with_statistical_information else (us,statistics)] # [us==最短加链 :: strict_sorted[pint]{len=sz+1}] # [statistics == (num_fulfilled_uss, num_pops, num_checked_items/num_ijks) :: (uint, uint, uint)]'
    #@override
    #@optional
    def iter_generate_continuity_infos(sf, /):
        return count_(1)
    #@override
    #@optional
    def line_value2may_iter_regenerate_continuity_infos_(sf, line_value, /):
        return None
    #@override
    #@optional
    def validate_line_value_payload_(sf, line_value, /):
        addition_chain = line_value
        check_addition_chain_(addition_chain, non_shortest_ok=None, allow_without_statistical_information=sf.allow_without_statistical_information, allow_with_statistical_information=sf.allow_with_statistical_information)
    #@override
    #@optional
    def validate_line_value_continuity_info_(sf, line_value, continuity_info, /):
        addition_chain = line_value
        (n, sz, us_ex) = addition_chain
        _n = continuity_info
        assert n == _n, ValueError(n, _n)
    #def validate_whole_file_(sf, /, *, to_validate_continuity, to_validate_payload):
    @classmethod
    def run_or_resume_(cls, may_setting, path, /, *, may_prompt_string, to_postpone_KeyboardInterrupt_until_subtask_switchover:bool, allow_create:bool, verbose=False, with_statistical_information=False, may_max1_N=None, to_check_optimal_if_known:bool):
        if not may_max1_N is None:
            max1_N = may_max1_N
            check_int_ge(0, max1_N)
        check_type_is(bool, to_postpone_KeyboardInterrupt_until_subtask_switchover)
        check_type_is(bool, allow_create)
        check_type_is(bool, verbose)
        check_type_is(bool, with_statistical_information)
        postpone = PostponeKeyboardInterrupt(xhandler_or_whether_turnoff:=not to_postpone_KeyboardInterrupt_until_subtask_switchover, may_prompt_string=may_prompt_string)

        sf = cls.from_path_(may_setting, path, allow_create=allow_create)
        tmay_result = sf.read_last_line_then_tmay_safe_eval_()
            # ^IncompleteLastLineError
            # will be at eof
        if tmay_result:
            [line_value] = tmay_result
            addition_chain = line_value
            (n, sz, us_ex) = addition_chain
        else:
            n = 0
        n += 1
        ns = count_(n) if may_max1_N is None else range(n, max1_N)
        ns = iter(ns)

        _to_show_ = verbose
        with sf.get_text_iofile_wrapper() as ofile:
            for n in ns:
                #if verbose: print_err(n)
                with postpone, timer(prefix=f'{n}', _to_show_=_to_show_, _show_hint_on_enter_=True):
                    addition_chain = 找出冫某一最短加链扌(n, with_statistical_information=with_statistical_information, to_check_optimal_if_known=to_check_optimal_if_known)
                    print(addition_chain, flush=True, file=ofile)
                    if verbose:
                        print_err(addition_chain)


def _get_n2optimal_sz():
    global _n2sz
    try:
        return _n2sz
    except NameError:
        from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length__first_100000_terms as _n2sz
        return _get_n2optimal_sz()
def check_addition_chain_(addition_chain, /, *, non_shortest_ok:[None, bool], may__i2may_jk=None, to_output__i2may_jk=False, allow_without_statistical_information=True, allow_with_statistical_information=False):
    '[allow non-shortest]:addition_chain/(n/pint, sz/加链长度/uint, us_ex) -> ((None if not to_output__i2may_jk else i2may_jk/[may (j/pint,k/pint)])|^Exception)'
    ######################
    check_type_is(tuple, addition_chain)
    assert len(addition_chain) == 3, TypeError(len(addition_chain))
    (n, sz, us_ex) = addition_chain
    check_int_ge(1, n)
    check_int_ge(0, sz)
    ######################
    if not non_shortest_ok is None:
        check_type_is(bool, non_shortest_ok)
    if non_shortest_ok is False:raise NotImplementedError
    ######################
    if non_shortest_ok is None:
        _n2sz = _get_n2optimal_sz()
    ######################
    if not (non_shortest_ok is True or non_shortest_ok is None and n < len(_n2sz)):raise NotImplementedError
    if non_shortest_ok is None:
        # optimal addition chain
        _n2sz
        assert sz == _n2sz[n], ValueError(n, sz, _n2sz[n])
        #if 0b0001:print_err('ok:', n, sz)
    elif non_shortest_ok is True:
        # non_optimal addition chain
        pass
    else:
        raise 000
    ######################
    # check us_ex
    check_type_is(tuple, us_ex)
    assert us_ex, TypeError
    if not type(us_ex[-1]) is int:
        # [us_ex == (us, statistics)]
        # [with_statistical_information]
        if not allow_with_statistical_information:raise TypeError
        check_type_is(tuple, us_ex[-1])
        assert len(us_ex) == 2, TypeError(len(us_ex))
        (us, statistics) = us_ex
        #########
        # check statistics
        check_type_is(tuple, statistics)
        assert len(statistics) == 3, TypeError(len(statistics))
        (num_fulfilled_uss, num_pops, num_checked_items) = statistics
        check_int_ge(0, num_fulfilled_uss)
        check_int_ge(0, num_pops)
        check_int_ge(0, num_checked_items)
        assert num_fulfilled_uss-1 <= num_pops <= num_checked_items, statistics
        #########
        us
    else:
        # [us_ex == us]
        # [not with_statistical_information]
        if not allow_without_statistical_information:raise TypeError
        us = us_ex
    us
    ######################
    # check us
    check_type_is(tuple, us)
    assert len(us) == sz+1, TypeError(sz, len(us))
    u_ = 0
    for u in us:
        #strict_sorted
        check_int_ge(u_+1, u)
        u_ = u
    assert us, ValueError(us)
    assert us[0] == 1, ValueError(us)
    assert us[-1] == n, ValueError(n, us)

    ######################
    # mk i2may_jk
    if may__i2may_jk:
        i2may_jk = may__i2may_jk
    else:
        i2u = us
        u2i = {u:i for i, u in enumerate(us)}
        i2may_jk = [None]
        for i, ui in enumerate(us):
            if i == 0:continue
            assert len(i2may_jk) == i, 000
            for j in reversed(range(i)):
                uj = us[j]
                uk = ui -uj
                if uk > uj:
                    # fail
                    break
                if not None is (k := u2i.get(uk)):
                    i2may_jk.append((j,k))
                    break
            else:
                #fail
                pass
            if len(i2may_jk) == i:
                #fail
                raise ValueError(addition_chain, i, ui)
            assert len(i2may_jk) == i+1, 000
        assert len(i2may_jk) == len(us), 000
    i2may_jk
    ######################
    # check using i2may_jk
    assert len(i2may_jk) == len(us), TypeError(len(us), len(i2may_jk))
    for i, ui in enumerate(us):
        if i == 0:
            assert i2may_jk[i] is None, TypeError
            assert ui == 1, 000
            continue

        j, k = i2may_jk[i]
        assert i >= j >= k >= 0, TypeError
        assert ui == us[j] + us[k], (addition_chain, i2may_jk, (i, j, k), (ui, us[j], us[k]))
    ######################
    if to_output__i2may_jk:
        return i2may_jk
    return None
    ######################

def 搜索冫最短加链长度牜批量扌(ns, /, *, brief=False, with_statistical_information=False, to_check_optimal_if_known=False):
    'Iter n/pint -> ((Iter addition_chain) if brief else Iter [[(n, trusty, sz), us_ex, ...], ...])  # [addition_chain :: (n/pint, sz/最短加链长度/uint, us_ex)] # [us_ex == (us if not with_statistical_information else (us,statistics)] # [us==最短加链 :: strict_sorted[pint]{len=sz+1}]'
    for n in ns:
        it = 搜索冫最短加链长度扌(n, with_statistical_information=with_statistical_information, to_check_optimal_if_known=to_check_optimal_if_known)
        if brief:
            for (n, trusty, sz) in it:
                assert trusty is True, (n, sz)
                us_ex = next(it)
                yield (n, sz, us_ex)
                break
            else:
                print_err('fail:', n)
        else:
            yield from it
def 找出冫某一最短加链扌(n, /, *, may_min0=None, may_max1=None, with_statistical_information=False, to_check_optimal_if_known=False):
    'n/pint -> addition_chain/(n/pint, sz/最短加链长度/uint, us_ex) # [us_ex == (us if not with_statistical_information else (us,statistics)] # [us==最短加链 :: strict_sorted[pint]{len=sz+1}]'
    it = 搜索冫最短加链长度扌(n, may_min0=may_min0, may_max1=may_max1, with_statistical_information=with_statistical_information, to_check_optimal_if_known=to_check_optimal_if_known)
    for (n, trusty, sz) in it:
        us_ex = next(it)
        return (n, sz, us_ex)
    raise Exception('fail:', n, may_min0, may_max1)



def _mk_reversed_shortest_lows(n, /):
    rv_lows = []
    i = n
    while 1:
        rv_lows.append(i)
        if i == 1:
            break
        i = (i+1) >> 1
    return rv_lows
def 搜索冫最短加链牜指定长度扌(sz, n, /, *, with_statistical_information=False):
    'sz/uint -> n/pint -> Iter (us if not with_statistical_information else (us, statistics)) # [us :: strict_sorted[pint]{len=sz+1}{us[0]==1;us[-1]==n}] # [statistics == (num_fulfilled_uss, num_pops, num_checked_items/num_ijks) :: (uint, uint, uint)]'
    check_type_is(bool, with_statistical_information)
    check_int_ge(1, n)
    check_int_ge(0, sz)
    L = sz+1
    us = []
        # finally:[len(us) == sz+1 == L]
    #i2jk = []
        # [(j,k)]
        # [us[i+1] == us[j]+us[k]]
        # [0 <= k <= j <= i]
    i2may_iter_jks = []
        # [may Iter (j,k,k4le)]
        # [[may_jks is None] <==> [i==sz==L-1]]
        # see:_mk_may_iter_jks()
    j2may_max_k = []
        # [may max_k] where [us[j]+us[max_k] <= up]
        # see:_find_may_max_k4j_()
        # see:_mk_may_iter_jks()
        # see:pushs_()
    ######################
    if with_statistical_information:
        def mk_output_():
            '-> us_ex'
            #statistics = (num_pops, num_checked_items:=num_ijks)
            statistics = (num_fulfilled_uss, num_pops, num_ijks)
            return (tuple(us), statistics)
    else:
        def mk_output_():
            '-> us_ex'
            return tuple(us)
    mk_output_
    ######################
    num_ijks = 0
        # number of processed (i,j,k)@us[:i+1]
        # --> num_checked_items
    def _4mk_iter_jks(st, j, /):
        nonlocal num_ijks
        k = j
        (us, i, up, low) = st
        k4le = us[j] + us[k] #key4le(obj)
        777; num_ijks += 1

        obj = (st, j, k, k4le)
        if k4le < low: return
        may_branches = None if j == 0 else iter([_4mk_iter_jks(st, j-1)])

        if 1: #xxx:if not k4le > up:
            yield (obj, may_branches)
                # even when [k4le > up]
                # !! required:[k4le{obj} >= all k4le{may_branches}]
        may_branches = None

        def _find_may_max_k4j__old_ver():
            nonlocal num_ijks
            max_k4le = up
            uj = us[j]
            max_uk = max_k4le -uj
            ks = reversed(range(j))
                # !! [(j,k:=j) is handled]
            for k in ks:
                if not us[k] > max_uk:break
                777; num_ijks += 1
            else:
                # no k:
                # updated:num_ijks += j
                return None
            k, ks
            max_k = k
                # updated:num_ijks += (j-1-max_k)
            return max_k
        def _find_may_max_k4j__new_ver():
            #see:_find_may_max_k4j_
            nonlocal num_ijks
            may_max_k4j = j2may_max_k[j]
            if may_max_k4j is None:
                777; num_ijks += j #vivi:old_ver
                return None
            max_k = may_max_k4j
            if max_k == j:
                # !! [(j,k:=j) is handled]
                if not max_k:
                    # [max_k == j == 0]
                    #777; num_ijks += j #vivi:old_ver
                    return None
                max_k -= 1
            assert 0 <= max_k < j
            777; num_ijks += (j-1-max_k) #vivi:old_ver
            return max_k
        #may_max_k4j = _find_may_max_k4j__old_ver()
        may_max_k4j = _find_may_max_k4j__new_ver()
        if may_max_k4j is None:
            return
        max_k = may_max_k4j
        ks = reversed(range(max_k+1))
            # !! [(j,max_k) is not handled]
        for k in ks:
            k4le = us[j] + us[k] #key4le(obj)
            777; num_ijks += 1
            if k4le < low: break
            assert not k4le > up
            obj = (st, j, k, k4le)
            yield (obj, None)
        return

    def key4le(obj, /):
        return obj[-1]
        (st, j, k, k4le) = obj
        return us[j] + us[k]
    #.def obj2value_(obj, /):
    #.    (st, j, k, k4le) = obj
    #.    return (us[j] + us[k], (j, k))
    #.obj2value_ = key4le
    def obj2value_(obj, /):
        (st, j, k, k4le) = obj
        return (j, k, k4le)
    def _mk_may_iter_jks(n, us, i, /):
        if i == sz:
            return None
        up = n
        low = max(lows[i+1], us[i]+1)
        st = (us, i, up, low)
        j = i
        #def merge_ex(*sorted_iterable_exs, key4stable:[False,callable]=False, key4le=None, __le__=None, reverse=False, unique=False, obj2value_:[None,callable]=None):
        return merge_ex(_4mk_iter_jks(st, j), key4stable=False, key4le=key4le, __le__=int.__ge__, unique=True, obj2value_=obj2value_)
    num_pops = 0
        # number of called pops_()
    def pops_():
        nonlocal num_pops
        777; num_pops += 1
        prev_u = us.pop()
        #i2jk.pop()
        i2may_iter_jks.pop()
        j2may_max_k.pop()
        return prev_u
    #.def push(j, k, /):
    #.    assert 0 <= k <= j <= len(us)-1 # == i
    #.    u = us[j]+us[k]
    #.def pushs_(u, /):
    #.    for i in range(len(us), L):
    #.        if u > n:break
    #.        us.append(u)
    #.        #i2jk.append((i,i))
    #.        may_jks = _mk_may_iter_jks(n, us, i)
    #.        if may_jks is None:next(may_jks)
    #.        i2may_iter_jks.append(may_jks)
    #.        u <<= 1
    def pushs_(u, /):
        if u > n:return
        i = len(us)
        us.append(u)
        may_jks = _mk_may_iter_jks(n, us, i)
        i2may_iter_jks.append(may_jks)
        may_max_k4j = _find_may_max_k4j_(j:=i)
        j2may_max_k.append(may_max_k4j)
    _half_up = n >> 1
    def _find_may_max_k4j_(j, /):
        'j -> may max_k # [us[j]+us[max_k] <= up]'
        up = n
        if j == sz:
            return None
        assert up > 1
        # [up > 1]
        uj = us[j]
        if uj <= _half_up:
            #if (uj << 1) <= up:
            max_k = j
            return max_k
        # [uj > up/2]
        # [2*uj > up]
        assert j > 0
            # !! [up == n >= 1]
            # !! [[j==0] -> [uj==1]]
            # [[[j==0][uj > up/2]] -> [[1 <= up < 2*uj == 2][up==1]]]

        # [j > 0]
        if not uj < up:
            return None
        # [up/2 < uj < up]
        # [us[j] + us[0] == uj+1 <= up]
        # [0 is a possible k]
        # [may_max_k4j is not None]

        j1 = j-1
        #assert j1 >= 0
            # !! [j > 0]
        max0_k = j2may_max_k[j1]
        assert max0_k <= j1
        ks = reversed(range(max0_k+1))
        max_k4le = up
        max_uk = max_k4le -uj
        for k in ks:
            if not us[k] > max_uk:break
            #777; num_ijks += 1
        else:
            # no k:
            raise 000
                # impossible
                # !! [may_max_k4j is not None]
            return None
        k
        max_k = k
        return max_k
    ######################


    ######################
    def _mk_lows():
        rv_lows = _mk_reversed_shortest_lows(n)
        if not len(rv_lows) <= L:
            assert not sz >= n.bit_length()-1, (sz, n, n.bit_length()-1)
            raise ValueError(sz)

        rv_lows += [1]*(L-len(rv_lows))
        assert len(rv_lows) == L
        lows = rv_lows; lows.reverse(); del rv_lows
        # [[k :<- [0..<L]] -> [lows[k] <= us[k]]]

        if not lows[0] <= 1:# == us[0]:
            assert not sz >= n.bit_length()-1, (sz, n, n.bit_length()-1)
            raise ValueError(sz)
        return lows
    lows = _mk_lows()
    ######################


    ######################
    num_fulfilled_uss = 0
    def main():
        nonlocal num_fulfilled_uss
        n1 = n+1
        pushs_(1)
        777; prev_u = n1
        while us:
            # us, i2may_iter_jks
            # [0 < len(us) == len(i2may_iter_jks)]
            if len(us) == L:
                777; num_fulfilled_uss += 1
                assert us[-1] == n, (n, sz, us)
                    # !! [up == n]
                    # !! [lows[L-1] == n]
                if us[-1] == n:
                    yield mk_output_() #tuple(us)
                prev_u = pops_()
                continue
            # [0 < len(us) < L]
            if not us[-1] < n:
                if us[-1] == n:raise ValueError('too big:', sz)
                raise 000
            # [0 < len(us) < L]
            # [us[-1] < n]
            jks = i2may_iter_jks[-1]
                # [[may_jks is None] <==> [i==sz==L-1]]
                # [[len(us) < L] -> [may_jks is not None]]
            for j, k, k4le in jks:
                #if 0b0001:print_err(n, us, j, k)
                if k4le > n: continue
                #if 0b0001:print_err(n, us, j, k)

                assert len(us)-1 >= j >= k
                next_u = k4le # = us[j] + us[k]
                assert prev_u > next_u, (us, prev_u, next_u)
                assert us[-1] < next_u
                assert lows[len(us)] <= next_u <= n # [low..=up]
                pushs_(next_u)
                777; prev_u = n1
                break
            else:
                prev_u = pops_()
            #continue
    ######################
    return main()


def 最短加链长度扌(n, /, *, may_min0=None, may_max1=None, to_check_optimal_if_known=False):
    'n/pint -> sz/最短加链长度/uint'
    it = 搜索冫最短加链长度扌(n, may_min0=may_min0, may_max1=may_max1, to_check_optimal_if_known=to_check_optimal_if_known)
    for (n, trusty, sz) in it:
        return sz
    raise Exception('fail:', n, may_min0, may_max1)

def 搜索冫最短加链长度扌(n, /, *, may_min0=None, may_max1=None, with_statistical_information=False, to_check_optimal_if_known=False):
    r'''
    :: n/pint -> Iter [(n, trusty, sz); us_ex, us_ex...]

    # [(n, trusty, sz/最短加链长度)/(pint,bool,uint)]
    # [us_ex == (us if not with_statistical_information else (us,statistics)]
    # [statistics == (num_fulfilled_uss, num_pops, num_checked_items/num_ijks) :: (uint, uint, uint)]
    # [us :: strict_sorted[pint]{len=sz+1}{us[0]==1;us[-1]==n}]
        # [1=>0[;1]; 2=>1[1;2]; 3=>2[1,2;3]; 4=>2[1,2;4]]'

    '''#'''
    #if 0b0001: n = 1
    check_type_is(bool, with_statistical_information)
    check_type_is(bool, to_check_optimal_if_known)
    if to_check_optimal_if_known:
        _n2sz = _get_n2optimal_sz()
    check_int_ge(1, n)

    bit_sz = n.bit_length()
    num_bit1s = n.bit_count()
    _min0__ver1 = bit_sz -1
    rv_lows = _mk_reversed_shortest_lows(n)
    _min0__ver2 = len(rv_lows)-1
    assert _min0__ver2 >= _min0__ver1
    _min0 = _min0__ver2

    _max0 = (bit_sz -1) +(num_bit1s -1)
    _max1 = _max0 +1
    min0 = _min0 if may_min0 is None else may_min0
    max1 = _max1 if may_max1 is None else may_max1


    min0 = max(min0, _min0)
    max1 = min(max1, _max1)



    for sz in range(min0, max1):
        it = 搜索冫最短加链牜指定长度扌(sz, n, with_statistical_information=with_statistical_information)
        for us_ex in it:
            break#done
        else:
            continue
        break#done
    else:
        raise Exception('fail:', n, min0, max1)
    #done
    us_ex
    if with_statistical_information:
        (us, statistics) = us_ex
    else:
        us = us_ex
    n, min0, sz, us, it # ?statistics?
    trusty = sz == _min0 or sz > min0
    n, trusty, sz, us, it


    #if 0b0001: (n, trusty, sz) = (1, False, 1)
    if to_check_optimal_if_known:
        if n < len(_n2sz):
            if not sz == _n2sz[n]:raise Exception(n, sz, _n2sz[n])
    #if 0b0001: raise 000

    yield (n, trusty, sz)
    yield us_ex # (us, ?statistics?)
    yield from it



__all__
from script.搜索冫最短加链长度 import (
可重启运算纟任一最短加链扌
,   校验冫输出文件纟可重启运算纟任一最短加链扌
,   排序冫输出文件纟可重启运算纟任一最短加链扌
)

from script.搜索冫最短加链长度 import check_addition_chain_

from script.搜索冫最短加链长度 import (
找出冫某一最短加链扌
,最短加链长度扌
,搜索冫最短加链长度牜批量扌
,   搜索冫最短加链长度扌
,       搜索冫最短加链牜指定长度扌
)

from script.搜索冫最短加链长度 import *
