#__all__:goto
# [:公式纟拆分纟幂方纟奇数]:goto
r'''[[[
e script/拆分冫幂方纟奇数.py
view script/拆分冫幂方纟奇数.py.test.txt

script.拆分冫幂方纟奇数
py -m nn_ns.app.debug_cmd   script.拆分冫幂方纟奇数 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.拆分冫幂方纟奇数:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd script.拆分冫幂方纟奇数:_doc4doctest -ht # -ff -df
    view script/拆分冫幂方纟奇数.py.test.txt

[[
泛化:3**3==27==1+6+12+8#魔方
===
@20250507
3**3==27==1+6+12+8#魔方
  泛化此类拆分
  m**n==sum ???
(2*k+1)**n==sum ???
(2*k)**n==sum ???
3**1==1+2==1+(2*1 * 1/1)
3**2==1+4+4==1+(2*2 * 1/1)+(2*2 * 2/2)
3**3==1+6+12+8==1+(2*3 * 1/1)+(2*3 * 4/2)+2**3{==(2*3 * 4/3)}
3**4==1+8+24+32+16==1+(2*4 * 1/1)+(2*4 * 6/2)+(2*4 * 12/3)+2**4{==(2*4 * 8/4)}
5**1==1+2*2
5**2==1+4*2+4*4
5**3==1+6*2+12*4+8*8
5**4==1+8*2+24*4+32*8+16*16

(2*k+1)**n:
  分类:中心,对称轴刺穿面,普通点
  [n==1]:kind=3
  [n==2]:kind=4
  [n==3]:kind=5
  kind{n}=n+2
  [n==1]:一隅之地=(k+1)==C(k+1;1)
  [n==2]:一隅之地=sum[(j+1) | [j:<-[0..=k]]]==(k+1)*(k+2)/2==C(k+2;2)
  [n==3]:一隅之地=sum[(j+1)*(j+2)/2 | [j:<-[0..=k]]]==C(k+3;3)
  一隅之地{n;k}=sum[一隅之地{n-1;j} | [j:<-[0..=k]]]==C(k+n;n)
  一隅之地{n;k}==C(k+n;n)
  [C(k+1+n;n)-C(k+n;n)==C(k+1+n-1;n-1)]
    proof:
    [C(k+1+n;n)-C(k+n;n)
    ==C(k+n;n)*(k+1+n)/(k+1)-C(k+n;n)
    ==C(k+n;n)*n/(k+1)
    ==C(k+n;n-1)
    ==C(k+1+n-1;n-1)
    =!=C(k+n-1;n-1)
    ]
  xxx普通点纟一隅之地{n;k}==一隅之地{n;k}-中心-k*(kind{n}-2{中心,普通})==C(k+n;n)-1-k*n
  xxx普通点纟一隅之地{n;k}==C(k+n;n)-1-k*n
  普通点纟一隅之地{n;k}==一隅之地{n;k-2}==C(k-2+n;n)
  普通点纟一隅之地{n;k}==C(k-2+n;n)
  [n==2]:普通点重复度==2*4
  [n==3]:普通点重复度==2*4*6
  普通点重复度{n}==n!*2**n
  普通点{n;k}==普通点纟一隅之地{n;k}*普通点重复度{n}
  xxx普通点{n;k}==(C(k+n;n)-1-k*n)*n!*2**n
  普通点{n;k}==C(k-2+n;n)*n!*2**n
  表皮纟一隅之地{n;k}==一隅之地{n;k}-一隅之地{n;k-2}==C(k+n;n)-C(k-2+n;n)==C(k+n;n)*(1-k*(k-1)/(k+n)/(k-1+n))
    [(k+n)*(k-1+n)-k*(k-1)==n*(n-1)+k*(2*n)==n*(2*k+n-1)]
  表皮纟一隅之地{n;k}==C(k+n;n)*n*(2*k+n-1)/(k+n)/(k-1+n)==C(k+n-1;n-1)*(2*k+n-1)/(k-1+n)==C(k+n-2;n-2)*(2*k+n-1)/(n-1)
  [n==1]:表皮纟一隅之地==2
  [n==2]:表皮纟一隅之地==2*k+1
  [n==3]:表皮纟一隅之地==(k+1)**2
  ...
  对称轴纟一隅之地{n;k}==
拆分冫幂方纟奇数:坐标对称性
  (2*k+1)**n
  n维[-k..=+k]
  [num_zeros==0][整数拆分(n-num_zeros)===[1]*n]:重复度==1/(n!*2**n)
    # 立方体内所有点表达为n维坐标系中各分量值取值范围为[-k..=+k]的坐标点。
    #   对称性:首先区分零与非零(同轴对称度==2)
    #   对称性:其次同一非零值的出现次数(异轴对称度==阶乘扌(同一非零值的出现次数))
  整数拆分(n-num_zeros)
    ==>>??? [总型数{n}==2**n==sum[数量纟整数拆分(n-num_zeros) | [num_zeros:<-[0..=n]]]] ???不太对:见下面:
view ../../python3_src/seed/math/uint_partition.py
from seed.math.uint_partition import uint2num_uint_partitions_
f=lambda n, cache=[]:2**n-sum(uint2num_uint_partitions_(n-num_zeros, cache=cache) for num_zeros in range(n+1))
[cache] = f.__defaults__
#>>> cache
[[1], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 3, 4, 5], [0, 1, 3, 5, 6, 7], [0, 1, 4, 7, 9, 10, 11], [0, 1, 4, 8, 11, 13, 14, 15], [0, 1, 5, 10, 15, 18, 20, 21, 22], [0, 1, 5, 12, 18, 23, 26, 28, 29, 30]]

#??? [总型数{n}==2**n==sum[数量纟整数拆分(n-num_zeros) | [num_zeros:<-[0..=n]]]] ???不太对
for n in range(10):f(n)
0
0
0
1 # 普通点 膨化 无分裂 ==>> 比2**3少+1
4
13
34
83
189
415

13-2*4==5
34-2*13==8
83-2*34==15
189-2*83==23
415-2*189==37
e script/拆分冫幂方纟奇数.py


@20250510
# [:公式纟拆分纟幂方纟奇数]:here
[(2*k+1)**n==sum[len_orbit*num_std_points4same_kind | [u:<-[0..=n]][parts4u:<-uint2iter_uint_partitions_(u)][counted_parts4u:=tuple(iter_counted_parts5expanded_uint_partition_(parts4u))][v:=len(parts4u)][parts4v:=sorted((count for part, count in counted_parts4u), reverse=True)][num_std_coordinate_choices:=num_ordered_choices5uint_partition_(parts4v)][num_std_points4same_kind:=C(k,v)*num_std_coordinate_choices][len_orbit:=C(n,u)*num_ordered_choices5uint_partition_(parts4u)*2**u]]]
    [num_zeros:=n-u]
        即:隐变量num_zeros
    [v==sum(parts4v)]
        即:parts4v命名的由来
    [len_orbit{n,parts4u}*num_std_points4same_kind{n,parts4u,k} == (len_orbit{n,parts4u}*num_std_coordinate_choices{n,parts4u})*C(k,v)]#[v:=len(parts4u)]
        即:求和公式的各部分 可再分离出 k无关部 与 k相关部
            =>抽取出:骨架:拆分冫幂方纟奇数牜冗长详尽牜骨架扌()
]]


>>> 拆分冫幂方纟奇数牜冗长详尽扌(3, 0)
(3, 0, 1, [(3, 0, (), 1, 1)])

>>> 拆分冫幂方纟奇数牜冗长详尽扌(3, 1)
(3, 1, 27, [(0, 3, (3,), 8, 1), (1, 2, (2,), 12, 1), (2, 1, (1,), 6, 1), (3, 0, (), 1, 1)])

>>> 拆分冫幂方纟奇数牜冗长详尽扌(3, 2)
(3, 2, 125, [(0, 3, (3,), 8, 2), (0, 3, (2, 1), 24, 2), (1, 2, (2,), 12, 2), (1, 2, (1, 1), 24, 1), (2, 1, (1,), 6, 2), (3, 0, (), 1, 1)])

>>> 拆分冫幂方纟奇数牜冗长详尽扌(3, 3)
(3, 3, 343, [(0, 3, (3,), 8, 3), (0, 3, (2, 1), 24, 6), (0, 3, (1, 1, 1), 48, 1), (1, 2, (2,), 12, 3), (1, 2, (1, 1), 24, 3), (2, 1, (1,), 6, 3), (3, 0, (), 1, 1)])

view script/拆分冫幂方纟奇数.py.test.txt
    _doc4doctest:goto
>>> for n in range(10): #doctest: +SKIP
...     for k in range(10):
...         拆分冫幂方纟奇数牜冗长详尽扌(n, k)
>>> for n in range(10): #doctest: +SKIP
...     for k in range(10):
...         print('#', (n, k))
...         拆分冫幂方纟奇数牜简略扌(n, k)
>>> for n in range(10): #doctest: +SKIP
...     for k in range(10):
...         print('#', (n, k))
...         拆分冫幂方纟奇数牜极简扌(n, k)





>>> max_n = 5
>>> max_k = 5

>>> for n in range(1+max_n):
...     for k in range(1+max_k):
...         拆分冫幂方纟奇数牜冗长详尽扌(n, k)
(0, 0, 1, [(0, 0, (), 1, 1)])
(0, 1, 1, [(0, 0, (), 1, 1)])
(0, 2, 1, [(0, 0, (), 1, 1)])
(0, 3, 1, [(0, 0, (), 1, 1)])
(0, 4, 1, [(0, 0, (), 1, 1)])
(0, 5, 1, [(0, 0, (), 1, 1)])
(1, 0, 1, [(1, 0, (), 1, 1)])
(1, 1, 3, [(0, 1, (1,), 2, 1), (1, 0, (), 1, 1)])
(1, 2, 5, [(0, 1, (1,), 2, 2), (1, 0, (), 1, 1)])
(1, 3, 7, [(0, 1, (1,), 2, 3), (1, 0, (), 1, 1)])
(1, 4, 9, [(0, 1, (1,), 2, 4), (1, 0, (), 1, 1)])
(1, 5, 11, [(0, 1, (1,), 2, 5), (1, 0, (), 1, 1)])
(2, 0, 1, [(2, 0, (), 1, 1)])
(2, 1, 9, [(0, 2, (2,), 4, 1), (1, 1, (1,), 4, 1), (2, 0, (), 1, 1)])
(2, 2, 25, [(0, 2, (2,), 4, 2), (0, 2, (1, 1), 8, 1), (1, 1, (1,), 4, 2), (2, 0, (), 1, 1)])
(2, 3, 49, [(0, 2, (2,), 4, 3), (0, 2, (1, 1), 8, 3), (1, 1, (1,), 4, 3), (2, 0, (), 1, 1)])
(2, 4, 81, [(0, 2, (2,), 4, 4), (0, 2, (1, 1), 8, 6), (1, 1, (1,), 4, 4), (2, 0, (), 1, 1)])
(2, 5, 121, [(0, 2, (2,), 4, 5), (0, 2, (1, 1), 8, 10), (1, 1, (1,), 4, 5), (2, 0, (), 1, 1)])
(3, 0, 1, [(3, 0, (), 1, 1)])
(3, 1, 27, [(0, 3, (3,), 8, 1), (1, 2, (2,), 12, 1), (2, 1, (1,), 6, 1), (3, 0, (), 1, 1)])
(3, 2, 125, [(0, 3, (3,), 8, 2), (0, 3, (2, 1), 24, 2), (1, 2, (2,), 12, 2), (1, 2, (1, 1), 24, 1), (2, 1, (1,), 6, 2), (3, 0, (), 1, 1)])
(3, 3, 343, [(0, 3, (3,), 8, 3), (0, 3, (2, 1), 24, 6), (0, 3, (1, 1, 1), 48, 1), (1, 2, (2,), 12, 3), (1, 2, (1, 1), 24, 3), (2, 1, (1,), 6, 3), (3, 0, (), 1, 1)])
(3, 4, 729, [(0, 3, (3,), 8, 4), (0, 3, (2, 1), 24, 12), (0, 3, (1, 1, 1), 48, 4), (1, 2, (2,), 12, 4), (1, 2, (1, 1), 24, 6), (2, 1, (1,), 6, 4), (3, 0, (), 1, 1)])
(3, 5, 1331, [(0, 3, (3,), 8, 5), (0, 3, (2, 1), 24, 20), (0, 3, (1, 1, 1), 48, 10), (1, 2, (2,), 12, 5), (1, 2, (1, 1), 24, 10), (2, 1, (1,), 6, 5), (3, 0, (), 1, 1)])
(4, 0, 1, [(4, 0, (), 1, 1)])
(4, 1, 81, [(0, 4, (4,), 16, 1), (1, 3, (3,), 32, 1), (2, 2, (2,), 24, 1), (3, 1, (1,), 8, 1), (4, 0, (), 1, 1)])
(4, 2, 625, [(0, 4, (4,), 16, 2), (0, 4, (3, 1), 64, 2), (0, 4, (2, 2), 96, 1), (1, 3, (3,), 32, 2), (1, 3, (2, 1), 96, 2), (2, 2, (2,), 24, 2), (2, 2, (1, 1), 48, 1), (3, 1, (1,), 8, 2), (4, 0, (), 1, 1)])
(4, 3, 2401, [(0, 4, (4,), 16, 3), (0, 4, (3, 1), 64, 6), (0, 4, (2, 2), 96, 3), (0, 4, (2, 1, 1), 192, 3), (1, 3, (3,), 32, 3), (1, 3, (2, 1), 96, 6), (1, 3, (1, 1, 1), 192, 1), (2, 2, (2,), 24, 3), (2, 2, (1, 1), 48, 3), (3, 1, (1,), 8, 3), (4, 0, (), 1, 1)])
(4, 4, 6561, [(0, 4, (4,), 16, 4), (0, 4, (3, 1), 64, 12), (0, 4, (2, 2), 96, 6), (0, 4, (2, 1, 1), 192, 12), (0, 4, (1, 1, 1, 1), 384, 1), (1, 3, (3,), 32, 4), (1, 3, (2, 1), 96, 12), (1, 3, (1, 1, 1), 192, 4), (2, 2, (2,), 24, 4), (2, 2, (1, 1), 48, 6), (3, 1, (1,), 8, 4), (4, 0, (), 1, 1)])
(4, 5, 14641, [(0, 4, (4,), 16, 5), (0, 4, (3, 1), 64, 20), (0, 4, (2, 2), 96, 10), (0, 4, (2, 1, 1), 192, 30), (0, 4, (1, 1, 1, 1), 384, 5), (1, 3, (3,), 32, 5), (1, 3, (2, 1), 96, 20), (1, 3, (1, 1, 1), 192, 10), (2, 2, (2,), 24, 5), (2, 2, (1, 1), 48, 10), (3, 1, (1,), 8, 5), (4, 0, (), 1, 1)])
(5, 0, 1, [(5, 0, (), 1, 1)])
(5, 1, 243, [(0, 5, (5,), 32, 1), (1, 4, (4,), 80, 1), (2, 3, (3,), 80, 1), (3, 2, (2,), 40, 1), (4, 1, (1,), 10, 1), (5, 0, (), 1, 1)])
(5, 2, 3125, [(0, 5, (5,), 32, 2), (0, 5, (4, 1), 160, 2), (0, 5, (3, 2), 320, 2), (1, 4, (4,), 80, 2), (1, 4, (3, 1), 320, 2), (1, 4, (2, 2), 480, 1), (2, 3, (3,), 80, 2), (2, 3, (2, 1), 240, 2), (3, 2, (2,), 40, 2), (3, 2, (1, 1), 80, 1), (4, 1, (1,), 10, 2), (5, 0, (), 1, 1)])
(5, 3, 16807, [(0, 5, (5,), 32, 3), (0, 5, (4, 1), 160, 6), (0, 5, (3, 2), 320, 6), (0, 5, (3, 1, 1), 640, 3), (0, 5, (2, 2, 1), 960, 3), (1, 4, (4,), 80, 3), (1, 4, (3, 1), 320, 6), (1, 4, (2, 2), 480, 3), (1, 4, (2, 1, 1), 960, 3), (2, 3, (3,), 80, 3), (2, 3, (2, 1), 240, 6), (2, 3, (1, 1, 1), 480, 1), (3, 2, (2,), 40, 3), (3, 2, (1, 1), 80, 3), (4, 1, (1,), 10, 3), (5, 0, (), 1, 1)])
(5, 4, 59049, [(0, 5, (5,), 32, 4), (0, 5, (4, 1), 160, 12), (0, 5, (3, 2), 320, 12), (0, 5, (3, 1, 1), 640, 12), (0, 5, (2, 2, 1), 960, 12), (0, 5, (2, 1, 1, 1), 1920, 4), (1, 4, (4,), 80, 4), (1, 4, (3, 1), 320, 12), (1, 4, (2, 2), 480, 6), (1, 4, (2, 1, 1), 960, 12), (1, 4, (1, 1, 1, 1), 1920, 1), (2, 3, (3,), 80, 4), (2, 3, (2, 1), 240, 12), (2, 3, (1, 1, 1), 480, 4), (3, 2, (2,), 40, 4), (3, 2, (1, 1), 80, 6), (4, 1, (1,), 10, 4), (5, 0, (), 1, 1)])
(5, 5, 161051, [(0, 5, (5,), 32, 5), (0, 5, (4, 1), 160, 20), (0, 5, (3, 2), 320, 20), (0, 5, (3, 1, 1), 640, 30), (0, 5, (2, 2, 1), 960, 30), (0, 5, (2, 1, 1, 1), 1920, 20), (0, 5, (1, 1, 1, 1, 1), 3840, 1), (1, 4, (4,), 80, 5), (1, 4, (3, 1), 320, 20), (1, 4, (2, 2), 480, 10), (1, 4, (2, 1, 1), 960, 30), (1, 4, (1, 1, 1, 1), 1920, 5), (2, 3, (3,), 80, 5), (2, 3, (2, 1), 240, 20), (2, 3, (1, 1, 1), 480, 10), (3, 2, (2,), 40, 5), (3, 2, (1, 1), 80, 10), (4, 1, (1,), 10, 5), (5, 0, (), 1, 1)])

>>> for n in range(1+max_n):
...     for k in range(1+max_k):
...         print('#', (n, k))
...         拆分冫幂方纟奇数牜简略扌(n, k)
# (0, 0)
[(1, 1)]
# (0, 1)
[(1, 1)]
# (0, 2)
[(1, 1)]
# (0, 3)
[(1, 1)]
# (0, 4)
[(1, 1)]
# (0, 5)
[(1, 1)]
# (1, 0)
[(1, 1)]
# (1, 1)
[(2, 1), (1, 1)]
# (1, 2)
[(2, 2), (1, 1)]
# (1, 3)
[(2, 3), (1, 1)]
# (1, 4)
[(2, 4), (1, 1)]
# (1, 5)
[(2, 5), (1, 1)]
# (2, 0)
[(1, 1)]
# (2, 1)
[(4, 1), (4, 1), (1, 1)]
# (2, 2)
[(4, 2), (8, 1), (4, 2), (1, 1)]
# (2, 3)
[(4, 3), (8, 3), (4, 3), (1, 1)]
# (2, 4)
[(4, 4), (8, 6), (4, 4), (1, 1)]
# (2, 5)
[(4, 5), (8, 10), (4, 5), (1, 1)]
# (3, 0)
[(1, 1)]
# (3, 1)
[(8, 1), (12, 1), (6, 1), (1, 1)]
# (3, 2)
[(8, 2), (24, 2), (12, 2), (24, 1), (6, 2), (1, 1)]
# (3, 3)
[(8, 3), (24, 6), (48, 1), (12, 3), (24, 3), (6, 3), (1, 1)]
# (3, 4)
[(8, 4), (24, 12), (48, 4), (12, 4), (24, 6), (6, 4), (1, 1)]
# (3, 5)
[(8, 5), (24, 20), (48, 10), (12, 5), (24, 10), (6, 5), (1, 1)]
# (4, 0)
[(1, 1)]
# (4, 1)
[(16, 1), (32, 1), (24, 1), (8, 1), (1, 1)]
# (4, 2)
[(16, 2), (64, 2), (96, 1), (32, 2), (96, 2), (24, 2), (48, 1), (8, 2), (1, 1)]
# (4, 3)
[(16, 3), (64, 6), (96, 3), (192, 3), (32, 3), (96, 6), (192, 1), (24, 3), (48, 3), (8, 3), (1, 1)]
# (4, 4)
[(16, 4), (64, 12), (96, 6), (192, 12), (384, 1), (32, 4), (96, 12), (192, 4), (24, 4), (48, 6), (8, 4), (1, 1)]
# (4, 5)
[(16, 5), (64, 20), (96, 10), (192, 30), (384, 5), (32, 5), (96, 20), (192, 10), (24, 5), (48, 10), (8, 5), (1, 1)]
# (5, 0)
[(1, 1)]
# (5, 1)
[(32, 1), (80, 1), (80, 1), (40, 1), (10, 1), (1, 1)]
# (5, 2)
[(32, 2), (160, 2), (320, 2), (80, 2), (320, 2), (480, 1), (80, 2), (240, 2), (40, 2), (80, 1), (10, 2), (1, 1)]
# (5, 3)
[(32, 3), (160, 6), (320, 6), (640, 3), (960, 3), (80, 3), (320, 6), (480, 3), (960, 3), (80, 3), (240, 6), (480, 1), (40, 3), (80, 3), (10, 3), (1, 1)]
# (5, 4)
[(32, 4), (160, 12), (320, 12), (640, 12), (960, 12), (1920, 4), (80, 4), (320, 12), (480, 6), (960, 12), (1920, 1), (80, 4), (240, 12), (480, 4), (40, 4), (80, 6), (10, 4), (1, 1)]
# (5, 5)
[(32, 5), (160, 20), (320, 20), (640, 30), (960, 30), (1920, 20), (3840, 1), (80, 5), (320, 20), (480, 10), (960, 30), (1920, 5), (80, 5), (240, 20), (480, 10), (40, 5), (80, 10), (10, 5), (1, 1)]

>>> for n in range(1+max_n):
...     for k in range(1+max_k):
...         print('#', (n, k))
...         拆分冫幂方纟奇数牜极简扌(n, k)
# (0, 0)
[1]
# (0, 1)
[1]
# (0, 2)
[1]
# (0, 3)
[1]
# (0, 4)
[1]
# (0, 5)
[1]
# (1, 0)
[1]
# (1, 1)
[2, 1]
# (1, 2)
[4, 1]
# (1, 3)
[6, 1]
# (1, 4)
[8, 1]
# (1, 5)
[10, 1]
# (2, 0)
[1]
# (2, 1)
[4, 4, 1]
# (2, 2)
[8, 8, 8, 1]
# (2, 3)
[12, 24, 12, 1]
# (2, 4)
[16, 48, 16, 1]
# (2, 5)
[20, 80, 20, 1]
# (3, 0)
[1]
# (3, 1)
[8, 12, 6, 1]
# (3, 2)
[16, 48, 24, 24, 12, 1]
# (3, 3)
[24, 144, 48, 36, 72, 18, 1]
# (3, 4)
[32, 288, 192, 48, 144, 24, 1]
# (3, 5)
[40, 480, 480, 60, 240, 30, 1]
# (4, 0)
[1]
# (4, 1)
[16, 32, 24, 8, 1]
# (4, 2)
[32, 128, 96, 64, 192, 48, 48, 16, 1]
# (4, 3)
[48, 384, 288, 576, 96, 576, 192, 72, 144, 24, 1]
# (4, 4)
[64, 768, 576, 2304, 384, 128, 1152, 768, 96, 288, 32, 1]
# (4, 5)
[80, 1280, 960, 5760, 1920, 160, 1920, 1920, 120, 480, 40, 1]
# (5, 0)
[1]
# (5, 1)
[32, 80, 80, 40, 10, 1]
# (5, 2)
[64, 320, 640, 160, 640, 480, 160, 480, 80, 80, 20, 1]
# (5, 3)
[96, 960, 1920, 1920, 2880, 240, 1920, 1440, 2880, 240, 1440, 480, 120, 240, 30, 1]
# (5, 4)
[128, 1920, 3840, 7680, 11520, 7680, 320, 3840, 2880, 11520, 1920, 320, 2880, 1920, 160, 480, 40, 1]
# (5, 5)
[160, 3200, 6400, 19200, 28800, 38400, 3840, 400, 6400, 4800, 28800, 9600, 400, 4800, 4800, 200, 800, 50, 1]









>>> for n in range(1+max_n):
...     for k in range(1+max_k):
...         print('#', (n, k))
...         拆分冫幂方纟奇数牜简略扌(n, k, to_allow_zero_num_std_points4same_kind=True)
# (0, 0)
[(1, 1)]
# (0, 1)
[(1, 1)]
# (0, 2)
[(1, 1)]
# (0, 3)
[(1, 1)]
# (0, 4)
[(1, 1)]
# (0, 5)
[(1, 1)]
# (1, 0)
[(2, 0), (1, 1)]
# (1, 1)
[(2, 1), (1, 1)]
# (1, 2)
[(2, 2), (1, 1)]
# (1, 3)
[(2, 3), (1, 1)]
# (1, 4)
[(2, 4), (1, 1)]
# (1, 5)
[(2, 5), (1, 1)]
# (2, 0)
[(4, 0), (8, 0), (4, 0), (1, 1)]
# (2, 1)
[(4, 1), (8, 0), (4, 1), (1, 1)]
# (2, 2)
[(4, 2), (8, 1), (4, 2), (1, 1)]
# (2, 3)
[(4, 3), (8, 3), (4, 3), (1, 1)]
# (2, 4)
[(4, 4), (8, 6), (4, 4), (1, 1)]
# (2, 5)
[(4, 5), (8, 10), (4, 5), (1, 1)]
# (3, 0)
[(8, 0), (24, 0), (48, 0), (12, 0), (24, 0), (6, 0), (1, 1)]
# (3, 1)
[(8, 1), (24, 0), (48, 0), (12, 1), (24, 0), (6, 1), (1, 1)]
# (3, 2)
[(8, 2), (24, 2), (48, 0), (12, 2), (24, 1), (6, 2), (1, 1)]
# (3, 3)
[(8, 3), (24, 6), (48, 1), (12, 3), (24, 3), (6, 3), (1, 1)]
# (3, 4)
[(8, 4), (24, 12), (48, 4), (12, 4), (24, 6), (6, 4), (1, 1)]
# (3, 5)
[(8, 5), (24, 20), (48, 10), (12, 5), (24, 10), (6, 5), (1, 1)]
# (4, 0)
[(16, 0), (64, 0), (96, 0), (192, 0), (384, 0), (32, 0), (96, 0), (192, 0), (24, 0), (48, 0), (8, 0), (1, 1)]
# (4, 1)
[(16, 1), (64, 0), (96, 0), (192, 0), (384, 0), (32, 1), (96, 0), (192, 0), (24, 1), (48, 0), (8, 1), (1, 1)]
# (4, 2)
[(16, 2), (64, 2), (96, 1), (192, 0), (384, 0), (32, 2), (96, 2), (192, 0), (24, 2), (48, 1), (8, 2), (1, 1)]
# (4, 3)
[(16, 3), (64, 6), (96, 3), (192, 3), (384, 0), (32, 3), (96, 6), (192, 1), (24, 3), (48, 3), (8, 3), (1, 1)]
# (4, 4)
[(16, 4), (64, 12), (96, 6), (192, 12), (384, 1), (32, 4), (96, 12), (192, 4), (24, 4), (48, 6), (8, 4), (1, 1)]
# (4, 5)
[(16, 5), (64, 20), (96, 10), (192, 30), (384, 5), (32, 5), (96, 20), (192, 10), (24, 5), (48, 10), (8, 5), (1, 1)]
# (5, 0)
[(32, 0), (160, 0), (320, 0), (640, 0), (960, 0), (1920, 0), (3840, 0), (80, 0), (320, 0), (480, 0), (960, 0), (1920, 0), (80, 0), (240, 0), (480, 0), (40, 0), (80, 0), (10, 0), (1, 1)]
# (5, 1)
[(32, 1), (160, 0), (320, 0), (640, 0), (960, 0), (1920, 0), (3840, 0), (80, 1), (320, 0), (480, 0), (960, 0), (1920, 0), (80, 1), (240, 0), (480, 0), (40, 1), (80, 0), (10, 1), (1, 1)]
# (5, 2)
[(32, 2), (160, 2), (320, 2), (640, 0), (960, 0), (1920, 0), (3840, 0), (80, 2), (320, 2), (480, 1), (960, 0), (1920, 0), (80, 2), (240, 2), (480, 0), (40, 2), (80, 1), (10, 2), (1, 1)]
# (5, 3)
[(32, 3), (160, 6), (320, 6), (640, 3), (960, 3), (1920, 0), (3840, 0), (80, 3), (320, 6), (480, 3), (960, 3), (1920, 0), (80, 3), (240, 6), (480, 1), (40, 3), (80, 3), (10, 3), (1, 1)]
# (5, 4)
[(32, 4), (160, 12), (320, 12), (640, 12), (960, 12), (1920, 4), (3840, 0), (80, 4), (320, 12), (480, 6), (960, 12), (1920, 1), (80, 4), (240, 12), (480, 4), (40, 4), (80, 6), (10, 4), (1, 1)]
# (5, 5)
[(32, 5), (160, 20), (320, 20), (640, 30), (960, 30), (1920, 20), (3840, 1), (80, 5), (320, 20), (480, 10), (960, 30), (1920, 5), (80, 5), (240, 20), (480, 10), (40, 5), (80, 10), (10, 5), (1, 1)]




>>> for n in range(1+max_n):
...     for k in range(1+max_k):
...         print('#', (n, k))
...         拆分冫幂方纟奇数牜极简扌(n, k, to_allow_zero_num_std_points4same_kind=True)
# (0, 0)
[1]
# (0, 1)
[1]
# (0, 2)
[1]
# (0, 3)
[1]
# (0, 4)
[1]
# (0, 5)
[1]
# (1, 0)
[0, 1]
# (1, 1)
[2, 1]
# (1, 2)
[4, 1]
# (1, 3)
[6, 1]
# (1, 4)
[8, 1]
# (1, 5)
[10, 1]
# (2, 0)
[0, 0, 0, 1]
# (2, 1)
[4, 0, 4, 1]
# (2, 2)
[8, 8, 8, 1]
# (2, 3)
[12, 24, 12, 1]
# (2, 4)
[16, 48, 16, 1]
# (2, 5)
[20, 80, 20, 1]
# (3, 0)
[0, 0, 0, 0, 0, 0, 1]
# (3, 1)
[8, 0, 0, 12, 0, 6, 1]
# (3, 2)
[16, 48, 0, 24, 24, 12, 1]
# (3, 3)
[24, 144, 48, 36, 72, 18, 1]
# (3, 4)
[32, 288, 192, 48, 144, 24, 1]
# (3, 5)
[40, 480, 480, 60, 240, 30, 1]
# (4, 0)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# (4, 1)
[16, 0, 0, 0, 0, 32, 0, 0, 24, 0, 8, 1]
# (4, 2)
[32, 128, 96, 0, 0, 64, 192, 0, 48, 48, 16, 1]
# (4, 3)
[48, 384, 288, 576, 0, 96, 576, 192, 72, 144, 24, 1]
# (4, 4)
[64, 768, 576, 2304, 384, 128, 1152, 768, 96, 288, 32, 1]
# (4, 5)
[80, 1280, 960, 5760, 1920, 160, 1920, 1920, 120, 480, 40, 1]
# (5, 0)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# (5, 1)
[32, 0, 0, 0, 0, 0, 0, 80, 0, 0, 0, 0, 80, 0, 0, 40, 0, 10, 1]
# (5, 2)
[64, 320, 640, 0, 0, 0, 0, 160, 640, 480, 0, 0, 160, 480, 0, 80, 80, 20, 1]
# (5, 3)
[96, 960, 1920, 1920, 2880, 0, 0, 240, 1920, 1440, 2880, 0, 240, 1440, 480, 120, 240, 30, 1]
# (5, 4)
[128, 1920, 3840, 7680, 11520, 7680, 0, 320, 3840, 2880, 11520, 1920, 320, 2880, 1920, 160, 480, 40, 1]
# (5, 5)
[160, 3200, 6400, 19200, 28800, 38400, 3840, 400, 6400, 4800, 28800, 9600, 400, 4800, 4800, 200, 800, 50, 1]

















>>> for n in range(1+max_n):
...     拆分冫幂方纟奇数牜冗长详尽牜骨架扌(n)
(0, [(0, 0, (), 1, 1)])
(1, [(0, 1, (1,), 2, 1), (1, 0, (), 1, 1)])
(2, [(0, 2, (2,), 4, 1), (0, 2, (1, 1), 8, 1), (1, 1, (1,), 4, 1), (2, 0, (), 1, 1)])
(3, [(0, 3, (3,), 8, 1), (0, 3, (2, 1), 24, 2), (0, 3, (1, 1, 1), 48, 1), (1, 2, (2,), 12, 1), (1, 2, (1, 1), 24, 1), (2, 1, (1,), 6, 1), (3, 0, (), 1, 1)])
(4, [(0, 4, (4,), 16, 1), (0, 4, (3, 1), 64, 2), (0, 4, (2, 2), 96, 1), (0, 4, (2, 1, 1), 192, 3), (0, 4, (1, 1, 1, 1), 384, 1), (1, 3, (3,), 32, 1), (1, 3, (2, 1), 96, 2), (1, 3, (1, 1, 1), 192, 1), (2, 2, (2,), 24, 1), (2, 2, (1, 1), 48, 1), (3, 1, (1,), 8, 1), (4, 0, (), 1, 1)])
(5, [(0, 5, (5,), 32, 1), (0, 5, (4, 1), 160, 2), (0, 5, (3, 2), 320, 2), (0, 5, (3, 1, 1), 640, 3), (0, 5, (2, 2, 1), 960, 3), (0, 5, (2, 1, 1, 1), 1920, 4), (0, 5, (1, 1, 1, 1, 1), 3840, 1), (1, 4, (4,), 80, 1), (1, 4, (3, 1), 320, 2), (1, 4, (2, 2), 480, 1), (1, 4, (2, 1, 1), 960, 3), (1, 4, (1, 1, 1, 1), 1920, 1), (2, 3, (3,), 80, 1), (2, 3, (2, 1), 240, 2), (2, 3, (1, 1, 1), 480, 1), (3, 2, (2,), 40, 1), (3, 2, (1, 1), 80, 1), (4, 1, (1,), 10, 1), (5, 0, (), 1, 1)])







>>> for n in range(1+max_n):
...     print('#', n)
...     拆分冫幂方纟奇数牜简略牜骨架扌(n)
# 0
[(0, 1, 1)]
# 1
[(1, 2, 1), (0, 1, 1)]
# 2
[(1, 4, 1), (2, 8, 1), (1, 4, 1), (0, 1, 1)]
# 3
[(1, 8, 1), (2, 24, 2), (3, 48, 1), (1, 12, 1), (2, 24, 1), (1, 6, 1), (0, 1, 1)]
# 4
[(1, 16, 1), (2, 64, 2), (2, 96, 1), (3, 192, 3), (4, 384, 1), (1, 32, 1), (2, 96, 2), (3, 192, 1), (1, 24, 1), (2, 48, 1), (1, 8, 1), (0, 1, 1)]
# 5
[(1, 32, 1), (2, 160, 2), (2, 320, 2), (3, 640, 3), (3, 960, 3), (4, 1920, 4), (5, 3840, 1), (1, 80, 1), (2, 320, 2), (2, 480, 1), (3, 960, 3), (4, 1920, 1), (1, 80, 1), (2, 240, 2), (3, 480, 1), (1, 40, 1), (2, 80, 1), (1, 10, 1), (0, 1, 1)]










py_adhoc_call   script.拆分冫幂方纟奇数   @拆分冫幂方纟奇数牜冗长详尽扌  =3 =1
py_adhoc_call   script.拆分冫幂方纟奇数   @拆分冫幂方纟奇数牜冗长详尽扌  =3 =2
py_adhoc_call  { -lineno }  script.拆分冫幂方纟奇数   ,20:枚举冫规模纟拆分纟幂方纟奇数扌 --cache='...' --cache2='...'
0:1
1:2
2:4
3:7
4:12
5:19
6:30
7:45
8:67
9:97
10:139
11:195
12:272
13:373
14:508
15:684
16:915
17:1212
18:1597
19:2087

py_adhoc_call  { -lineno }  script.拆分冫幂方纟奇数   ,20:枚举冫规模纟拆分纟幂方纟奇数扌 --cache='...' --cache2='...' --may_max4num_parts=1
0:1
1:2
2:3
3:4
4:5
5:6
6:7
7:8
8:9
9:10
10:11
11:12
12:13
13:14
14:15
15:16
16:17
17:18
18:19
19:20

[[
py_adhoc_call  { -lineno }  script.拆分冫幂方纟奇数   ,20:枚举冫规模纟拆分纟幂方纟奇数扌 --cache='...' --cache2='...' --may_max4num_parts=2
0:1
1:2
2:4
3:6 #?? why not 7 ?? [k==2==max4num_parts] ?? 见下面
4:9
5:12
6:16
7:20
8:25
9:30
10:36
11:42
12:49
13:56
14:64
15:72
16:81
17:90
18:100
19:110
==>>:
    [[
    输出:『3:6』 #?? why not 7 ?? [k==2==max4num_parts] ??
        [(0,0,0):1, (0,0,x):2, (0,x,x):2, (0,1,2):1, (x,x,x):2, {a,a,b}/{(1,1,2), (1,2,2)}:2]
            [num_std_points4same_kind==1] => 2项
            [num_std_points4same_kind==2] => 4项
        # (3, 2)
        [(8, 2), (24, 2), (12, 2), (24, 1), (6, 2), (1, 1)]
        # (3, 2)
        [(8, 2), (24, 2), (48, 0), (12, 2), (24, 1), (6, 2), (1, 1)]
    ]]
]]


py_adhoc_call  { -lineno }  script.拆分冫幂方纟奇数   ,20:枚举冫规模纟拆分纟幂方纟奇数扌 --cache='...' --cache2='...' --may_max4num_parts=3
0:1
1:2
2:4
3:7
4:11
5:16
6:23
7:31
8:41
9:53
10:67
11:83
12:102
13:123
14:147
15:174
16:204
17:237
18:274
19:314

from script.拆分冫幂方纟奇数 import *
]]]'''#'''
__all__ = r'''
拆分冫幂方纟奇数牜极简扌
拆分冫幂方纟奇数牜简略扌
拆分冫幂方纟奇数牜冗长详尽扌
    拆分冫幂方纟奇数牜冗长详尽牜骨架扌
        拆分冫幂方纟奇数牜简略牜骨架扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from math import factorial, comb, perm, prod
from seed.math.uint_partition import uint2num_uint_partitions__len_le_, uint2num_uint_partitions_, uint2iter_uint_partitions_, num_permutations5uint_partition_, num_set_partitions5uint_partition_, num_ordered_choices5uint_partition_, iter_counted_parts5expanded_uint_partition_
def _API():
    def uint2num_uint_partitions__len_le_(max4num_parts, u, /, *, cache2, max4part=None):
        '[O(u**2)] => max4num_parts/uint -> u/uint -> (kw:max4part/uint) -> (kw:cache2/(None=>local|...=>global|[[[uint]]])) -> num_uint_partitions{all parts <= max4part}/uint{==cache2[u][max4num_parts][offsetted_max4part]} # [cache2==u2max4num_parts2offsetted_max4part2num_uint_partitions :: [[[uint]]] / list{list{list{uint}}}]'
    def uint2num_uint_partitions_(u, /, *, cache, max4part=None):
        '[O(u**2)] => u/uint -> (kw:max4part/uint) -> (kw:cache/(None=>local|...=>global|[[uint]])) -> num_uint_partitions{all parts <= max4part}/uint{==cache[u][max4part]}'
    def uint2iter_uint_partitions_(u, /, *, to_expand=True, max4part=None, max4num_parts=None):
        'u/uint -> (kw:to_expand/bool) -> Iter ([part] if to_expand else [(part, count)]) # in decreasing order'
    def num_permutations5uint_partition_(uint_partition, /, *, zipped_vs_expanded=True):
        '([part] if zipped_vs_expanded else [(part, count)]) -> num_permutations/uint'
    def num_set_partitions5uint_partition_(uint_partition, /, *, zipped_vs_expanded=True):
        '([part] if zipped_vs_expanded else [(part, count)]) -> num_set_partitions/uint'
    def num_ordered_choices5uint_partition_(uint_partition, /, *, zipped_vs_expanded=True):
        '([part] if zipped_vs_expanded else [(part, count)]) -> num_ordered_choices/uint'
    def iter_counted_parts5expanded_uint_partition_(expanded_uint_partition, /):
        '[part] -> Iter (part, count)'
from seed.tiny_.check import check_type_is, check_int_ge
from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
#.from itertools import islice
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

_doc4doctest = read_under_pkg_(__package__, '拆分冫幂方纟奇数.py.test.txt', xencoding='u8')
    #view script/拆分冫幂方纟奇数.py.test.txt

def 拆分冫幂方纟奇数牜极简扌(n, k, /, *, to_allow_zero_num_std_points4same_kind=False):
    'n/uint -> k/uint -> [uint]/拆分牜极简{((2*k+1)**n)} # [((2*k+1)**n) == sum result]'
    _ls = 拆分冫幂方纟奇数牜简略扌(n, k, to_allow_zero_num_std_points4same_kind=to_allow_zero_num_std_points4same_kind)
    us = [(len_orbit * num_std_points4same_kind) for (len_orbit, num_std_points4same_kind) in _ls]
    return us
def 拆分冫幂方纟奇数牜简略扌(n, k, /, *, to_allow_zero_num_std_points4same_kind=False):
    'n/uint -> k/uint -> [(len_orbit/uint,num_std_points4same_kind/uint)]/拆分牜简略{((2*k+1)**n)} # [len_orbit==num_symmetry_points==num_isomorphic_points==num_conjugate_points] # [((2*k+1)**n) == sum [len_orbit*num_std_points4same_kind | [(len_orbit,num_std_points4same_kind) :<- result]]]'
    (n, k, pow_2k1_n, ls) = 拆分冫幂方纟奇数牜冗长详尽扌(n, k, to_allow_zero_num_std_points4same_kind=to_allow_zero_num_std_points4same_kind)
    _ls = [(len_orbit, num_std_points4same_kind) for (num_zeros, u, parts4u, len_orbit, num_std_points4same_kind) in ls]
    return _ls
def 拆分冫幂方纟奇数牜冗长详尽扌(n, k, /, *, to_allow_zero_num_std_points4same_kind=False):
    r'''[[[
    'n/uint -> k/uint -> (n,k,pow_2k1_n{[pow_2k1_n==((2*k+1)**n)]},[(num_zeros/uint, u/uint{[u+num_zeros==n]}, parts4u/uint_partition{u}, len_orbit/uint,num_std_points4same_kind/uint)]/拆分牜冗长详尽{pow_2k1_n}) # [len_orbit==num_symmetry_points==num_isomorphic_points==num_conjugate_points] # [((2*k+1)**n) == sum [len_orbit*num_std_points4same_kind | [(len_orbit,num_std_points4same_kind) :<- ...]]]'

    # [:公式纟拆分纟幂方纟奇数]:goto
        [(2*k+1)**n==sum[len_orbit*num_std_points4same_kind | [u:<-[0..=n]][parts4u:<-uint2iter_uint_partitions_(u)][counted_parts4u:=tuple(iter_counted_parts5expanded_uint_partition_(parts4u))][v:=len(parts4u)][parts4v:=sorted((count for part, count in counted_parts4u), reverse=True)][num_std_coordinate_choices:=num_ordered_choices5uint_partition_(parts4v)][num_std_points4same_kind:=C(k,v)*num_std_coordinate_choices][len_orbit:=C(n,u)*num_ordered_choices5uint_partition_(parts4u)*2**u]]]

    #]]]'''#'''
    ######################common:
    check_type_is(bool, to_allow_zero_num_std_points4same_kind)
    check_int_ge(0, n)
    check_int_ge(0, k)
    pow_2k1_n = ((2*k+1)**n)
    # 立方体内所有点表达为n维坐标系中各分量值取值范围为[-k..=+k]的坐标点。
    #   对称性:首先区分零与非零(同轴对称度==2)
    #   对称性:其次同一非零值的出现次数(异轴对称度==阶乘扌(同一非零值的出现次数))
    #max4num_parts4std_pt = k+1
        # 标准点坐标各分量值取值范围为[0..=+k]
    max4num_nonzero_parts4std_pt = k
        # 标准点坐标各非零分量值取值范围为[1..=+k]
    may_max4num_parts = max4num_nonzero_parts4std_pt if not to_allow_zero_num_std_points4same_kind else None
    ######################
    ######################
    ######################
    ######################

    ######################new:
    ls = []
    acc = 0
    if 1:
        (_n, _ls) = 拆分冫幂方纟奇数牜冗长详尽牜骨架扌(n, may_max4num_parts=may_max4num_parts)
        for (num_zeros, u, parts4u, len_orbit, num_std_coordinate_choices) in _ls:
            P3 = num_std_coordinate_choices
            v = len(parts4u)
            C1 = comb(k, v)
            assert C1 > 0 or may_max4num_parts is None
            num_std_points4same_kind = C1*P3 # = comb(k, v)*num_ordered_choices5uint_partition_(parts4v)
            assert num_std_points4same_kind > 0 or may_max4num_parts is None
            ls.append((num_zeros, u, parts4u, len_orbit, num_std_points4same_kind))
            acc += len_orbit*num_std_points4same_kind
    ls
    acc
    assert acc == pow_2k1_n, (acc, (n, k, pow_2k1_n, ls))
    return (n, k, pow_2k1_n, ls)
    ######################
    ######################
    ######################
    ######################
    ######################old:
    ls = []
    acc = 0
    for num_zeros in range(n+1):
        # [0 <= num_zeros <= n]
        u = n - num_zeros
        # [0 <= u <= n]
        C0 = comb(n, num_zeros)
        #for parts4u in uint2iter_uint_partitions_(u, max4num_parts=max4num_nonzero_parts4std_pt):
        for parts4u in uint2iter_uint_partitions_(u, max4num_parts=may_max4num_parts):
            assert len(parts4u) <= max4num_nonzero_parts4std_pt == k or may_max4num_parts is None
            counted_parts4u = tuple(iter_counted_parts5expanded_uint_partition_(parts4u))
            counts = sorted((count for part, count in counted_parts4u), reverse=True)
            v = sum(counts)
            parts4v = counts
            assert v == len(parts4u)
            # [len_orbit==num_symmetry_points==num_isomorphic_points==num_conjugate_points]
            C1 = comb(k, len(parts4u))
            assert C1 > 0 or may_max4num_parts is None
            #P1 = perm(k, len(parts4u))
            #P2 = num_set_partitions5uint_partition_(parts4v)
            P3 = num_ordered_choices5uint_partition_(parts4v)
                # num_std_coordinate_choices
            P4u = num_ordered_choices5uint_partition_(parts4u) # = (factorial(u)//prod(factorial(part) for part in parts4u))
            len_orbit = (C0*P4u)<<u
                #len_orbit = comb(n, num_zeros) * (factorial(u)//prod(factorial(part) for part in parts4u)) * 2**u
            #bug:num_std_points4same_kind = C1 # = comb(k, len(parts4u))
            #bug:num_std_points4same_kind = P1 # = perm(k, len(parts4u))
            #bug:num_std_points4same_kind = C1*P2 # = comb(k, len(parts4u))*num_set_partitions5uint_partition_(parts4v)
            num_std_points4same_kind = C1*P3 # = comb(k, len(parts4u))*num_ordered_choices5uint_partition_(parts4v)
            assert num_std_points4same_kind > 0 or may_max4num_parts is None
            ls.append((num_zeros, u, parts4u, len_orbit, num_std_points4same_kind))
            acc += len_orbit*num_std_points4same_kind
    ls
    acc
    assert acc == pow_2k1_n, (acc, (n, k, pow_2k1_n, ls))
    return (n, k, pow_2k1_n, ls)
    ######################
    ######################
    ######################
def 拆分冫幂方纟奇数牜冗长详尽牜骨架扌(n, /, *, may_max4num_parts=None):
    'n/uint -> (n,[(num_zeros/uint, u/uint{[u+num_zeros==n]}, parts4u/uint_partition{u}, len_orbit/uint, num_std_coordinate_choices/uint)]/拆分牜冗长详尽牜骨架) # [len_orbit==num_symmetry_points==num_isomorphic_points==num_conjugate_points] # [num_std_points4same_kind{k} == == comb(k, v)*num_std_coordinate_choices][num_std_coordinate_choices==num_ordered_choices5uint_partition_(parts4v)][parts4v==sorted((count for part, count in counted_parts4u), reverse=True)][counted_parts4u==tuple(iter_counted_parts5expanded_uint_partition_(parts4u))][v == len(parts4u)]'
    check_int_ge(0, n)
    # 立方体内所有点表达为n维坐标系中各分量值取值范围为[-k..=+k]的坐标点。
    #   对称性:首先区分零与非零(同轴对称度==2)
    #   对称性:其次同一非零值的出现次数(异轴对称度==阶乘扌(同一非零值的出现次数))
    may_max4num_parts
    ls = []
    #.for num_zeros in range(n+1):
    #.    # [0 <= num_zeros <= n]
    #.    u = n - num_zeros
    #.    # [0 <= u <= n]
    #.    C0 = comb(n, num_zeros)
    for u in range(n+1):
        # [0 <= u <= n]
        C0 = comb(n, u)
        # [0 <= num_zeros <= n]
        num_zeros = n - u
        for parts4u in uint2iter_uint_partitions_(u, max4num_parts=may_max4num_parts):
            v = len(parts4u)
            counted_parts4u = tuple(iter_counted_parts5expanded_uint_partition_(parts4u))
            counts = sorted((count for part, count in counted_parts4u), reverse=True)
            parts4v = counts
            assert v == sum(parts4v)
            #assert v == len(parts4u)
            # [len_orbit==num_symmetry_points==num_isomorphic_points==num_conjugate_points]
            num_std_coordinate_choices = P3 = num_ordered_choices5uint_partition_(parts4v)
            P4u = num_ordered_choices5uint_partition_(parts4u) # = (factorial(u)//prod(factorial(part) for part in parts4u))
            len_orbit = (C0*P4u)<<u
                #len_orbit = comb(n, num_zeros) * (factorial(u)//prod(factorial(part) for part in parts4u)) * 2**u
                #len_orbit = comb(n, u) * num_ordered_choices5uint_partition_(parts4u) * 2**u
            #num_std_points4same_kind = C1*P3 # = comb(k, v)*num_ordered_choices5uint_partition_(parts4v)
            ls.append((num_zeros, u, parts4u, len_orbit, num_std_coordinate_choices))
    ls
    return (n, ls)
def 拆分冫幂方纟奇数牜简略牜骨架扌(n, /, *, may_max4num_parts=None):
    'n/uint -> [(len_parts4u/uint/len(uint_partition{u}), len_orbit/uint, num_std_coordinate_choices/uint)]/拆分牜简略牜骨架 # [len_orbit==num_symmetry_points==num_isomorphic_points==num_conjugate_points]'
    (_n, _ls) = 拆分冫幂方纟奇数牜冗长详尽牜骨架扌(n, may_max4num_parts=may_max4num_parts)
    _3s = [(len(parts4u), len_orbit, num_std_coordinate_choices) for (num_zeros, u, parts4u, len_orbit, num_std_coordinate_choices) in _ls]
    return _3s

def _预备冫规模纟拆分纟幂方纟奇数扌(*, cache, cache2, may_max4part, may_max4num_parts):
    if cache is None:
        cache = []
    if cache2 is None:
        cache2 = []
    if not may_max4num_parts is None:
        max4num_parts = may_max4num_parts
        check_int_ge(0, max4num_parts)
        _uint2num_uint_partitions_ = lambda u:uint2num_uint_partitions__len_le_(max4num_parts, u, cache2=cache2, max4part=may_max4part)
    else:
        _uint2num_uint_partitions_ = lambda u:uint2num_uint_partitions_(u, cache=cache, max4part=may_max4part)
    _uint2num_uint_partitions_
    return (cache, cache2, _uint2num_uint_partitions_)
def 求冫规模纟拆分纟幂方纟奇数扌(n, /, *, cache, cache2, may_max4part=None, may_max4num_parts=None):
    'n/uint -> num_kinds/uint'
    check_int_ge(0, n)
    (cache, cache2, _uint2num_uint_partitions_) = _预备冫规模纟拆分纟幂方纟奇数扌(cache=cache, cache2=cache2, may_max4part=may_max4part, may_max4num_parts=may_max4num_parts)
    #num_kinds = sum(_uint2num_uint_partitions_(u) for u in range(n+1))
    num_kinds = sum(map(_uint2num_uint_partitions_, range(n+1)))
    return num_kinds
def 枚举冫规模纟拆分纟幂方纟奇数扌(may_max1_n=None, /, *, cache, cache2, may_max4part=None, may_max4num_parts=None):
    (cache, cache2, _uint2num_uint_partitions_) = _预备冫规模纟拆分纟幂方纟奇数扌(cache=cache, cache2=cache2, may_max4part=may_max4part, may_max4num_parts=may_max4num_parts)
    from seed.iters.count_ import count_
    num_kinds = 0
    for n in count_(0, may_max1_n):
        # num_kinds = sum(uint2num_uint_partitions_(u, cache=cache, max4part=may_max4part) for u in range(n+1))
        #num_kinds += uint2num_uint_partitions_(n, cache=cache, max4part=may_max4part)
        num_kinds += _uint2num_uint_partitions_(n)
        yield num_kinds

    return

__all__
from script.拆分冫幂方纟奇数 import *
