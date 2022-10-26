r'''[[[
e script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py
view ../../python3_src/seed/math/floor_ceil.py
直接检查:[not$ [(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) >= (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]]
    [lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)]
    [upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))]
    [E == 2**e]
    求:max_E(flbQ), max_e(flbN)

py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__k__fKrtQ =0 =0
-1
py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__k__fKrtQ =1 =0
KeyboardInterrupt
py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__k__fKrtQ =1 =4
KeyboardInterrupt
py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__fKrtQ_lt__k_eq_ =2 =0
0


py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__fKrtQ_lt__k_eq_ =2 =17
[((2, 0), 0), ((2, 1), 1), ((2, 2), 2), ((2, 3), 2), ((2, 4), 3), ((2, 5), 3), ((2, 6), 3), ((2, 7), 3), ((2, 8), 4), ((2, 9), 4), ((2, 10), 4), ((2, 11), 4), ((2, 12), 4), ((2, 13), 4), ((2, 14), 4), ((2, 15), 4), ((2, 16), 5)]
py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__floor_log2_fKrtQ_lt__k_eq_ =2 =17
[((2, 0), 1), ((2, 1), 2), ((2, 2), 3), ((2, 3), 4), ((2, 4), 5), ((2, 5), 6), ((2, 6), 7), ((2, 7), 8), ((2, 8), 9), ((2, 9), 10), ((2, 10), 11), ((2, 11), 12), ((2, 12), 13), ((2, 13), 14), ((2, 14), 15), ((2, 15), 16), ((2, 16), 17)]
py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__floor_log2_fKrtQ_lt__k_eq_ =3 =17
[((3, 0), 1), ((3, 1), 1), ((3, 2), 2), ((3, 3), 3), ((3, 4), 4), ((3, 5), 5), ((3, 6), 6), ((3, 7), 7), ((3, 8), 8), ((3, 9), 9), ((3, 10), 10), ((3, 11), 11), ((3, 12), 12), ((3, 13), 13), ((3, 14), 14), ((3, 15), 15), ((3, 16), 16)]


py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py ,iter_max_e__floor_log2_fKrtQ_lt__k_ge2_lt_ =6 =17
[[
py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py ,iter_max_e__floor_log2_fKrtQ_lt__k_ge2_lt_ =17 =17
((2, 0), 1)
((2, 1), 2)
((2, 2), 3)
((2, 3), 4)
((2, 4), 5)
((2, 5), 6)
((2, 6), 7)
((2, 7), 8)
((2, 8), 9)
((2, 9), 10)
((2, 10), 11)
((2, 11), 12)
((2, 12), 13)
((2, 13), 14)
((2, 14), 15)
((2, 15), 16)
((2, 16), 17)
((3, 0), 1)
((3, 1), 1)
((3, 2), 2)
((3, 3), 3)
((3, 4), 4)
((3, 5), 5)
((3, 6), 6)
((3, 7), 7)
((3, 8), 8)
((3, 9), 9)
((3, 10), 10)
((3, 11), 11)
((3, 12), 12)
((3, 13), 13)
((3, 14), 14)
((3, 15), 15)
((3, 16), 16)
((4, 0), 0)
((4, 1), 1)
((4, 2), 1)
((4, 3), 2)
((4, 4), 3)
((4, 5), 4)
((4, 6), 5)
((4, 7), 6)
((4, 8), 7)
((4, 9), 8)
((4, 10), 9)
((4, 11), 10)
((4, 12), 11)
((4, 13), 12)
((4, 14), 13)
((4, 15), 14)
((4, 16), 15)
((5, 0), 0)
((5, 1), 0)
((5, 2), 1)
((5, 3), 2)
((5, 4), 3)
((5, 5), 4)
((5, 6), 5)
((5, 7), 6)
((5, 8), 7)
((5, 9), 8)
((5, 10), 9)
((5, 11), 10)
((5, 12), 11)
((5, 13), 12)
((5, 14), 13)
((5, 15), 14)
((5, 16), 15)
((6, 0), 0)
((6, 1), 0)
((6, 2), 1)
((6, 3), 1)
((6, 4), 2)
((6, 5), 3)
((6, 6), 4)
((6, 7), 5)
((6, 8), 6)
((6, 9), 7)
((6, 10), 8)
((6, 11), 9)
((6, 12), 10)
((6, 13), 11)
((6, 14), 12)
((6, 15), 13)
((6, 16), 14)
((7, 0), 0)
((7, 1), 0)
((7, 2), 1)
((7, 3), 1)
((7, 4), 2)
((7, 5), 3)
((7, 6), 4)
((7, 7), 5)
((7, 8), 6)
((7, 9), 7)
((7, 10), 8)
((7, 11), 9)
((7, 12), 10)
((7, 13), 11)
((7, 14), 12)
((7, 15), 13)
((7, 16), 14)
((8, 0), 0)
((8, 1), 0)
((8, 2), 0)
((8, 3), 1)
((8, 4), 2)
((8, 5), 3)
((8, 6), 4)
((8, 7), 5)
((8, 8), 6)
((8, 9), 7)
((8, 10), 8)
((8, 11), 9)
((8, 12), 10)
((8, 13), 11)
((8, 14), 12)
((8, 15), 13)
((8, 16), 14)
((9, 0), 0)
((9, 1), 0)
((9, 2), 0)
((9, 3), 1)
((9, 4), 2)
((9, 5), 3)
((9, 6), 4)
((9, 7), 5)
((9, 8), 6)
((9, 9), 7)
((9, 10), 8)
((9, 11), 9)
((9, 12), 10)
((9, 13), 11)
((9, 14), 12)
((9, 15), 13)
((9, 16), 14)
((10, 0), 0)
((10, 1), 0)
((10, 2), 0)
((10, 3), 1)
((10, 4), 2)
((10, 5), 2)
((10, 6), 3)
((10, 7), 4)
((10, 8), 5)
((10, 9), 6)
((10, 10), 7)
((10, 11), 8)
((10, 12), 9)
((10, 13), 10)
((10, 14), 11)
((10, 15), 12)
((10, 16), 13)
((11, 0), 0)
((11, 1), 0)
((11, 2), 0)
((11, 3), 1)
((11, 4), 1)
((11, 5), 2)
((11, 6), 3)
((11, 7), 4)
((11, 8), 5)
((11, 9), 6)
((11, 10), 7)
((11, 11), 8)
((11, 12), 9)
((11, 13), 10)
((11, 14), 11)
((11, 15), 12)
((11, 16), 13)
((12, 0), 0)
((12, 1), 0)
((12, 2), 0)
((12, 3), 1)
((12, 4), 1)
((12, 5), 2)
((12, 6), 3)
((12, 7), 4)
((12, 8), 5)
((12, 9), 6)
((12, 10), 7)
((12, 11), 8)
((12, 12), 9)
((12, 13), 10)
((12, 14), 11)
((12, 15), 12)
((12, 16), 13)
((13, 0), 0)
((13, 1), 0)
((13, 2), 0)
((13, 3), 0)
((13, 4), 1)
((13, 5), 2)
((13, 6), 3)
((13, 7), 4)
((13, 8), 5)
((13, 9), 6)
((13, 10), 7)
((13, 11), 8)
((13, 12), 9)
((13, 13), 10)
((13, 14), 11)
((13, 15), 12)
((13, 16), 13)
((14, 0), 0)
((14, 1), 0)
((14, 2), 0)
((14, 3), 0)
((14, 4), 1)
((14, 5), 2)
((14, 6), 3)
((14, 7), 4)
((14, 8), 5)
((14, 9), 6)
((14, 10), 7)
((14, 11), 8)
((14, 12), 9)
((14, 13), 10)
((14, 14), 11)
((14, 15), 12)
((14, 16), 13)
((15, 0), 0)
((15, 1), 0)
((15, 2), 0)
((15, 3), 0)
((15, 4), 1)
((15, 5), 2)
((15, 6), 3)
((15, 7), 4)
((15, 8), 5)
((15, 9), 6)
((15, 10), 7)
((15, 11), 8)
((15, 12), 9)
((15, 13), 10)
((15, 14), 11)
((15, 15), 12)
((15, 16), 13)
((16, 0), 0)
((16, 1), 0)
((16, 2), 0)
((16, 3), 0)
((16, 4), 1)
((16, 5), 2)
((16, 6), 3)
((16, 7), 4)
((16, 8), 5)
((16, 9), 6)
((16, 10), 7)
((16, 11), 8)
((16, 12), 9)
((16, 13), 10)
((16, 14), 11)
((16, 15), 12)
((16, 16), 13)

]]

猜想:
    [k==2]:[max_e==floor_log2_fKrtQ+1]
    [k==3]:[max_e==max(1,floor_log2_fKrtQ)]
    [k==4]:[max_e==floor_log2_fKrtQ]
    [k==5]:[max_e==max(0,floor_log2_fKrtQ-1)]
    [k==6]or[k==7]:[max_e==max(0,floor_log2_fKrtQ-2+[floor_log2_fKrtQ<=2])]
    [k==8]or[k==9]:[max_e==max(0,floor_log2_fKrtQ-2+[floor_log2_fKrtQ<=1])]
    [k==10]:[max_e==max(0,floor_log2_fKrtQ-3+[floor_log2_fKrtQ<=4])]
    [k==11]or[k==12]:[max_e==max(0,floor_log2_fKrtQ-3+[floor_log2_fKrtQ<=3])]
    [k<-[13..=16]]:[max_e==max(0,floor_log2_fKrtQ-3+[floor_log2_fKrtQ<=2])]


py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py ,iter_max_e__floor_log2_fKrtQ_ge_lt__k_ge_lt_ =17 =18 =17 =101
((17, 17), 14)
((17, 18), 15)
((17, 19), 16)
... ...
((17, 98), 95)
((17, 99), 96)
((17, 100), 97)



py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py ,iter_max_e__floor_log2_fKrtQ_ge_lt__k_ge_lt_ =100 =101 =0 =17
((100, 0), 0)
((100, 1), 0)
((100, 2), 0)
((100, 3), 0)
((100, 4), 0)
((100, 5), 0)
((100, 6), 0)
((100, 7), 1)
((100, 8), 2)
((100, 9), 3)
((100, 10), 4)
((100, 11), 5)
((100, 12), 6)
((100, 13), 7)
((100, 14), 8)
((100, 15), 9)
((100, 16), 10)




py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__floor_log2_fKrtQ_lt__k_eq_ ... ...
py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py @find_max_e__floor_log2_fKrtQ_lt__k_eq_ =66 =17
[((66, 0), 0), ((66, 1), 0), ((66, 2), 0), ((66, 3), 0), ((66, 4), 0), ((66, 5), 0), ((66, 6), 1), ((66, 7), 2), ((66, 8), 3), ((66, 9), 4), ((66, 10), 4), ((66, 11), 5), ((66, 12), 6), ((66, 13), 7), ((66, 14), 8), ((66, 15), 9), ((66, 16), 10)]
[((65, 0), 0), ((65, 1), 0), ((65, 2), 0), ((65, 3), 0), ((65, 4), 0), ((65, 5), 0), ((65, 6), 1), ((65, 7), 2), ((65, 8), 3), ((65, 9), 4), ((65, 10), 5), ((65, 11), 6), ((65, 12), 7), ((65, 13), 8), ((65, 14), 9), ((65, 15), 10), ((65, 16), 11)]
[((34, 0), 0), ((34, 1), 0), ((34, 2), 0), ((34, 3), 0), ((34, 4), 0), ((34, 5), 1), ((34, 6), 2), ((34, 7), 3), ((34, 8), 3), ((34, 9), 4), ((34, 10), 5), ((34, 11), 6), ((34, 12), 7), ((34, 13), 8), ((34, 14), 9), ((34, 15), 10), ((34, 16), 11)]
[((33, 0), 0), ((33, 1), 0), ((33, 2), 0), ((33, 3), 0), ((33, 4), 0), ((33, 5), 1), ((33, 6), 2), ((33, 7), 3), ((33, 8), 4), ((33, 9), 5), ((33, 10), 6), ((33, 11), 7), ((33, 12), 8), ((33, 13), 9), ((33, 14), 10), ((33, 15), 11), ((33, 16), 12)]
[((18, 0), 0), ((18, 1), 0), ((18, 2), 0), ((18, 3), 0), ((18, 4), 1), ((18, 5), 2), ((18, 6), 2), ((18, 7), 3), ((18, 8), 4), ((18, 9), 5), ((18, 10), 6), ((18, 11), 7), ((18, 12), 8), ((18, 13), 9), ((18, 14), 10), ((18, 15), 11), ((18, 16), 12)]
[((17, 0), 0), ((17, 1), 0), ((17, 2), 0), ((17, 3), 0), ((17, 4), 1), ((17, 5), 2), ((17, 6), 3), ((17, 7), 4), ((17, 8), 5), ((17, 9), 6), ((17, 10), 7), ((17, 11), 8), ((17, 12), 9), ((17, 13), 10), ((17, 14), 11), ((17, 15), 12), ((17, 16), 13)]
[((10, 0), 0), ((10, 1), 0), ((10, 2), 0), ((10, 3), 1), ((10, 4), 2), ((10, 5), 2), ((10, 6), 3), ((10, 7), 4), ((10, 8), 5), ((10, 9), 6), ((10, 10), 7), ((10, 11), 8), ((10, 12), 9), ((10, 13), 10), ((10, 14), 11), ((10, 15), 12), ((10, 16), 13)]
[((9, 0), 0), ((9, 1), 0), ((9, 2), 0), ((9, 3), 1), ((9, 4), 2), ((9, 5), 3), ((9, 6), 4), ((9, 7), 5), ((9, 8), 6), ((9, 9), 7), ((9, 10), 8), ((9, 11), 9), ((9, 12), 10), ((9, 13), 11), ((9, 14), 12), ((9, 15), 13), ((9, 16), 14)]
[((6, 0), 0), ((6, 1), 0), ((6, 2), 1), ((6, 3), 1), ((6, 4), 2), ((6, 5), 3), ((6, 6), 4), ((6, 7), 5), ((6, 8), 6), ((6, 9), 7), ((6, 10), 8), ((6, 11), 9), ((6, 12), 10), ((6, 13), 11), ((6, 14), 12), ((6, 15), 13), ((6, 16), 14)]
[((5, 0), 0), ((5, 1), 0), ((5, 2), 1), ((5, 3), 2), ((5, 4), 3), ((5, 5), 4), ((5, 6), 5), ((5, 7), 6), ((5, 8), 7), ((5, 9), 8), ((5, 10), 9), ((5, 11), 10), ((5, 12), 11), ((5, 13), 12), ((5, 14), 13), ((5, 15), 14), ((5, 16), 15)]
[((4, 0), 0), ((4, 1), 1), ((4, 2), 1), ((4, 3), 2), ((4, 4), 3), ((4, 5), 4), ((4, 6), 5), ((4, 7), 6), ((4, 8), 7), ((4, 9), 8), ((4, 10), 9), ((4, 11), 10), ((4, 12), 11), ((4, 13), 12), ((4, 14), 13), ((4, 15), 14), ((4, 16), 15)]
[((3, 0), 1), ((3, 1), 1), ((3, 2), 2), ((3, 3), 3), ((3, 4), 4), ((3, 5), 5), ((3, 6), 6), ((3, 7), 7), ((3, 8), 8), ((3, 9), 9), ((3, 10), 10), ((3, 11), 11), ((3, 12), 12), ((3, 13), 13), ((3, 14), 14), ((3, 15), 15), ((3, 16), 16)]
[((2, 0), 1), ((2, 1), 2), ((2, 2), 3), ((2, 3), 4), ((2, 4), 5), ((2, 5), 6), ((2, 6), 7), ((2, 7), 8), ((2, 8), 9), ((2, 9), 10), ((2, 10), 11), ((2, 11), 12), ((2, 12), 13), ((2, 13), 14), ((2, 14), 15), ((2, 15), 16), ((2, 16), 17)]

[[定义 序列Up #保持(floor_log2_fKrtQ-e)差值不变的k取值范围的上界所构成的序列
[Up :: [uint]]
[Up[0] := 2]
[@[i>=1] -> [Up[i] := Up[i-1]*2 -1]]
[Up == [2,3,5,9,17,33,65,129,257,...]]

[@[i>=1] -> [Up[i]-1 == (Up[i-1]-1)*2 == 2**i]]
[@[i>=1] -> [Up[i] == 2**i+1]]
[@[i>=0] -> [Up[i] == 2**i+1]]
猜想:
    [@[i>=-1] -> @[k<-[floor(2**i+2)..=2**(i+1)+1]] -> [[max(0, floor_log2_fKrtQ-i)<=find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ)<=max(0, 1+floor_log2_fKrtQ-i)][?[threshold>=i] -> [floor_log2_fKrtQ >= threshold] -> [find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ)==floor_log2_fKrtQ-i]]]]
    即:
    [@[k>=2] -> [i:=ceil_log2(k-1)-1] -> [[max(0, floor_log2_fKrtQ-i)<=find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ)<=max(0, 1+floor_log2_fKrtQ-i)][?[threshold>=i] -> [floor_log2_fKrtQ >= threshold] -> [find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ)==floor_log2_fKrtQ-i]]]]

]]

##验证后续:
[((129, 0), 0), ((129, 1), 0), ((129, 2), 0), ((129, 3), 0), ((129, 4), 0), ((129, 5), 0), ((129, 6), 0), ((129, 7), 1), ((129, 8), 2), ((129, 9), 3), ((129, 10), 4), ((129, 11), 5), ((129, 12), 6), ((129, 13), 7), ((129, 14), 8), ((129, 15), 9), ((129, 16), 10)]
[((130, 0), 0), ((130, 1), 0), ((130, 2), 0), ((130, 3), 0), ((130, 4), 0), ((130, 5), 0), ((130, 6), 0), ((130, 7), 1), ((130, 8), 2), ((130, 9), 3), ((130, 10), 4), ((130, 11), 5), ((130, 12), 5), ((130, 13), 6), ((130, 14), 7), ((130, 15), 8), ((130, 16), 9)]

[((257, 0), 0), ((257, 1), 0), ((257, 2), 0), ((257, 3), 0), ((257, 4), 0), ((257, 5), 0), ((257, 6), 0), ((257, 7), 0), ((257, 8), 1), ((257, 9), 2), ((257, 10), 3), ((257, 11), 4), ((257, 12), 5), ((257, 13), 6), ((257, 14), 7), ((257, 15), 8), ((257, 16), 9)]
[((258, 0), 0), ((258, 1), 0), ((258, 2), 0), ((258, 3), 0), ((258, 4), 0), ((258, 5), 0), ((258, 6), 0), ((258, 7), 0), ((258, 8), 1), ((258, 9), 2), ((258, 10), 3), ((258, 11), 4), ((258, 12), 5), ((258, 13), 6), ((258, 14), 6), ((258, 15), 7), ((258, 16), 8)]


[is_e_ok__k__fKrtQ(k, fKrtQ, e) =[def]= [[k>=2][fKrtQ>=1][E:=2**e][lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)][upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))][(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) < (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]]]
[is_e_ok__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ, e) =[def]= [[k>=2][floor_log2_fKrtQ>=0][@[fKrtQ :<- [2**floor_log2_fKrtQ..<2**(1+floor_log2_fKrtQ)]] -> [is_e_ok__k__fKrtQ(k, fKrtQ, e)]]]]
[find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ) =[def]= (-1+min({0}\-/{bad_e <- [1..] | [not$ [is_e_ok__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ, bad_e)]]}))]
    # [find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ) =[def]= (max({-1}\-/{max_e <- [0..] | [@[e <- [0..=max_e]] -> [is_e_ok__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ, e)]]}))]
[第一猜想:= [@[k>=2] -> [i:=ceil_log2(k-1)-1] -> @[floor_log2_fKrtQ>=0] -> [[max(0, floor_log2_fKrtQ-i)<=find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ)<=max(0, 1+floor_log2_fKrtQ-i)][?[threshold>=i] -> [floor_log2_fKrtQ >= threshold] -> [find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ)==floor_log2_fKrtQ-i]]]]] #候选的粗略定义:[max_e<k{>=2},floor_log2_fKrtQ{>=0}> =[def]= max(0, 1+floor_log2_fKrtQ-ceil_log2(k-1))]



bug:q0定义有误:
[[bug:q0,fKrtQ0定义有误，应当改为[q0 := n//2**((flbN-min_flbQ)//k *k)]
  [第一猜想]: # ==>> fKrtQ0取值范围
    [max_e(k;floor_log2_fKrtQ) =[def]= floor_log2_fKrtQ-ceil_log2(k-1)+1]
    #floor_log2_fKrtQ初始值
    !![e >= 1]
    [max_e(k;floor_log2_fKrtQ) >= e >= 1]
    [floor_log2_fKrtQ-ceil_log2(k-1)+1 >= 1]
    [floor_log2_fKrtQ >= ceil_log2(k-1)]
    [min_floor_log2_fKrtQ == ceil_log2(k-1)]
    !![2**floor_log2_fKrtQ <= fKrtQ < 2**(floor_log2_fKrtQ+1)]
    !![fKrtQ**k <= q < (fKrtQ+1)**k]
    [2**(floor_log2_fKrtQ*k) <= q < (2**floor_log2_fKrtQ+1)**k]
    [min_flbQ == k*min_floor_log2_fKrtQ == k*ceil_log2(k-1)]
    [min_q == 2**min_flbQ == 2**(k*ceil_log2(k-1))]
    [2**(ceil_log2(k-1)-1) < k-1 <= 2**ceil_log2(k-1)]
    [k-1 <= min_fKrtQ ==2**ceil_log2(k-1) < 2*(k-1)]
    [k-1 <= min_fKrtQ < 2*(k-1)]
    [(k-1)**k <= min_q == min_fKrtQ**k == 2**(k*ceil_log2(k-1)) < 2**k*(k-1)**k]
    [n >= min_q][q0 := n//2**(flbN-min_flbQ)][fKrtQ0 := floor_kth_root_(k,q0)]:
        [q0 <= n/2**(flbN-min_flbQ) < (q0+1)]
        [n/2**(flbN-min_flbQ) -1 < q0 <= n/2**(flbN-min_flbQ)]
        !![1 <= n/2**flbN < 2]
        !![min_q == 2**min_flbQ]
        [min_q <= n/2**(flbN-min_flbQ) == min_q*n/2**flbN < 2*min_q]
        [min_q-1 <= n/2**(flbN-min_flbQ) -1 < q0 <= n/2**(flbN-min_flbQ) < 2*min_q]

        [min_q <= q0 < 2*min_q]
        [k-1 <= min_fKrtQ == 2**ceil_log2(k-1) == 2**floor_log2_fKrtQ == 2**(min_flbQ///k) == floor_kth_root_(k,min_q) <= fKrtQ0 <= floor_kth_root_(k,2*min_q-1)]
            #最后是『<=』不是『<』
        [1 <= k-1 <= 2**ceil_log2(k-1) <= fKrtQ0 <= floor_kth_root_(k,-1+2**(1+k*ceil_log2(k-1))) < 2*(k-1)]
            证明:[-1+2**(1+k*ceil_log2(k-1)) < (2*(k-1))**k]
                <==> [2**(1+k*ceil_log2(k-1)) <= (2*(k-1))**k]
                <==> [2*2**(k*ceil_log2(k-1)) <= 2**k * (k-1)**k]
                <==> [2**(k*ceil_log2(k-1)) <= 2**(k-1) * 2**(k*log2(k-1))]
                <==> [(k*ceil_log2(k-1)) <= (k-1) + (k*log2(k-1))]
                <==> [k*ceil_log2(k-1) < k + k*log2(k-1)]
                <==> [ceil_log2(k-1) < 1 + log2(k-1)]
                证毕！

        view: k2rng4fKrtQ0
[[第一猜想] -> @[k>=2] -> [[min_floor_log2_fKrtQ := ceil_log2(k-1)][min_flbQ := k*min_floor_log2_fKrtQ][min_q := 2**min_flbQ]] -> @[n >= min_q] -> [[flbN := floor_log2(n)][q0 := n//2**(flbN-min_flbQ)][fKrtQ0 := floor_kth_root_(k,q0)]] -> [1 <= k-1 <= 2**ceil_log2(k-1) <= fKrtQ0 <= floor_kth_root_(k,-1+2**(1+k*ceil_log2(k-1))) < 2*(k-1)]] # [第一猜想 ==>> fKrtQ0取值范围]
]] #bug


py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py ,iter_rng4fKrtQ0__5k_ge_lt =2 =21
(2, (1, 2))
(3, (2, 3))
(4, (4, 5))
(5, (4, 5))
(6, (8, 9))
(7, (8, 9))
(8, (8, 9))
(9, (8, 9))
(10, (16, 18))
(11, (16, 18))
(12, (16, 17))
(13, (16, 17))
(14, (16, 17))
(15, (16, 17))
(16, (16, 17))
(17, (16, 17))
(18, (32, 34))
(19, (32, 34))
(20, (32, 34))


py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py ,iter_rng4k_of_same_len_rng4fKrtQ0__5k_ge_lt =2 =21
AssertionError: ((10, 21), (18, 21))

py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py ,iter_rng4k_with_same_len_rng4fKrtQ0__5k_ge_lt =2 =1025
((2, 10), 1)
((10, 12), 2)
((12, 18), 1)
((18, 23), 2)
((23, 34), 1)
((34, 45), 2)
((45, 66), 1)
((66, 90), 2)
((90, 130), 1)
((130, 178), 2)
((178, 258), 1)
((258, 356), 2)
((356, 514), 1)
((514, 711), 2)
((711, 1025), 1)
py script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py ,iter_rng4k_with_same_len_rng4fKrtQ0__5k_ge_lt =1025 =2049
((1025, 1026), 1)
((1026, 1420), 2)
((1420, 2049), 1)


[[bug:q0,fKrtQ0定义有误，应当改为[q0 := n//2**((flbN-min_flbQ)//k *k)]
    [第二猜想:= [@[k>=2] -> [2**(1+k*ceil_log2(k-1)) <= (2+2**ceil_log2(k-1))**k]]] #初始值fKrtQ0<k>最多只有两种不同取值
    [[[第一猜想][第二猜想]] -> @[k>=2] -> [[min_floor_log2_fKrtQ := ceil_log2(k-1)][min_flbQ := k*min_floor_log2_fKrtQ][min_q := 2**min_flbQ]] -> @[n >= min_q] -> [[flbN := floor_log2(n)][q0 := n//2**(flbN-min_flbQ)][fKrtQ0 := floor_kth_root_(k,q0)]] -> [1 <= k-1 <= 2**ceil_log2(k-1) <= fKrtQ0 <= floor_kth_root_(k,-1+2**(1+k*ceil_log2(k-1))) < min((2+2**ceil_log2(k-1)), 2*(k-1))]] # [第一猜想&&第二猜想 ==>> fKrtQ0最多只有两种不同取值]
]] #bug

[[尝试证明[第一猜想]


分解为多个证明:

1:证明:[@[k>=2] -> @[floor_log2_fKrtQ>=0] -> [is_e_ok__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ, e) == is_e_ok__k__fKrtQ(k, 2**floor_log2_fKrtQ, e)]]
    # [fKrtQ :<- [2**floor_log2_fKrtQ..<2**(1+floor_log2_fKrtQ)]] 变 [fKrtQ := 2**floor_log2_fKrtQ]
    #   即 max_e(k;fKrtQ) 关于fKrtQ单调递增
    #   即 max_E(k;fKrtQ) 关于fKrtQ单调递增
    <<== [@[k>=2] -> @[fKrtQ>=1] -> @[e>=0] -> [is_e_ok__k__fKrtQ(k, fKrtQ, e)] -> [is_e_ok__k__fKrtQ(k, fKrtQ+1, e)]]
    待证明

2:证明:[@[k>=2] -> @[fKrtQ>=1] -> @[e>=0] -> [is_e_ok__k__fKrtQ(k+1, fKrtQ, e)] -> [is_e_ok__k__fKrtQ(k, fKrtQ, e)]]
    待证明

3:证明:[@[i>=0] -> [k:=1+2**i] -> @[floor_log2_fKrtQ>=0] -> [fKrtQ:=2**floor_log2_fKrtQ] -> [e:=max(0, 1+floor_log2_fKrtQ-ceil_log2(k-1))] -> [is_e_ok__k__fKrtQ(k, fKrtQ, e)]]
    <==> [@[i>=0] -> @[floor_log2_fKrtQ>=0] -> [is_e_ok__k__fKrtQ(1+2**i, 2**floor_log2_fKrtQ, max(0, 1+floor_log2_fKrtQ-i))]]
    <==> [[@[i>=0] -> @[floor_log2_fKrtQ>=i] -> [is_e_ok__k__fKrtQ(1+2**i, 2**floor_log2_fKrtQ, max(0, 1+floor_log2_fKrtQ-i))]][@[k>=2] -> @[floor_log2_fKrtQ>=0] -> [is_e_ok__k__fKrtQ(k, 2**floor_log2_fKrtQ, 0)]]]
    <==> [[@[i>=0] -> @[floor_log2_fKrtQ>=i] -> [is_e_ok__k__fKrtQ(1+2**i, 2**floor_log2_fKrtQ, (1+floor_log2_fKrtQ-i))]][@[k>=2] -> @[fKrtQ>=1] -> [is_e_ok__k__fKrtQ(k, fKrtQ, 0)]]]
    再分解:
3-1:证明:[@[i>=0] -> @[floor_log2_fKrtQ>=i] -> [is_e_ok__k__fKrtQ(1+2**i, 2**floor_log2_fKrtQ, (1+floor_log2_fKrtQ-i))]]
    !![is_e_ok__k__fKrtQ(k, fKrtQ, e) =[def]= [[k>=2][fKrtQ>=1][E:=2**e][lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)][upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))][(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) < (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]]]
    [j:=floor_log2_fKrtQ-i]
    [e:=(1+floor_log2_fKrtQ-i)]
    [fKrtQ:=2**floor_log2_fKrtQ]
    [k:=1+2**i]
    [floor_log2_fKrtQ == i+j]
    [e == 1+j]
    [fKrtQ==2**(i+j)]

    [E==2**e==2**(1+j)]
    [lower_D_dd == ((fKrtQ*E+1)**k - (fKrtQ*E)**k)
    == ((1+2**(1+i+2*j))**k - (2**(1+i+2*j))**k)
    == ((1+2**(1+i+2*j))**(1+2**i) - (2**(1+i+2*j))**(1+2**i))
    == ((1+2**(1+i+2*j))**(1+2**i) - 2**((1+i+2*j)*(1+2**i)))
    ]
    [upper_D1_dd1 == (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))
    == (((1+2**(i+j))**k - (2**(i+j))**k)*(2**(1+j))**(2**i))
    == (((1+2**(i+j))**k - 2**((i+j)*k))*2**((1+j)*2**i))
    == ((1+2**(i+j))**k*2**((1+j)*2**i) - 2**((i+j)*k)*2**((1+j)*2**i))
    == ((1+2**(i+j))*((1+2**(i+j))*2**(1+j))**(2**i) - 2**((i+j)*(1+2**i)+(1+j)*2**i))
    == ((1+2**(i+j))*(2**(1+j)+2**(1+i+2*j))**(2**i) - 2**((i+j)+(1+i+2*j)*2**i))
    ]
    [upper_D1_dd1 -lower_D_dd
    == ((1+2**(i+j))*(2**(1+j)+2**(1+i+2*j))**(2**i) - 2**((i+j)+(1+i+2*j)*2**i)) -((1+2**(1+i+2*j))**(1+2**i) - 2**((1+i+2*j)*(1+2**i)))
    == ???
    ]

    [(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) < (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]
        <==> ???
    待证明

3-2:证明:[@[k>=2] -> @[fKrtQ>=1] -> [is_e_ok__k__fKrtQ(k, fKrtQ, 0)]]
    [e==0]:
        [E==2**e==1]
        [lower_D_dd == ((fKrtQ*E+1)**k - (fKrtQ*E)**k) == ((fKrtQ+1)**k - fKrtQ**k)]
        [upper_D1_dd1 == (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1)) == (((fKrtQ+1)**k - fKrtQ**k))]
        [lower_D_dd == upper_D1_dd1]
        !![k>=2][fKrtQ>=1]
        [(fKrtQ+1)**k > fKrtQ**k]
        [upper_D1_dd1 > 0]
        [upper_D1_dd1 >= 1]
    [is_e_ok__k__fKrtQ(k, fKrtQ, 0)
    == [(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) < (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]
    !![lower_D_dd == upper_D1_dd1]
    == [(upper_D1_dd1*E)*(upper_D1_dd1-upper_D1_dd1) < (upper_D1_dd1*upper_D1_dd1 +2*upper_D1_dd1 -upper_D1_dd1-1)]
    == [0 < (upper_D1_dd1*upper_D1_dd1 +upper_D1_dd1 -1)]
    !![upper_D1_dd1 >= 1]
    == 1
    ]
    证毕！

]]


#]]]'''
__all__ = '''

    '''.split()

from seed.seq_tools.bisearch import bisearch
from itertools import count, pairwise, chain


def find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ, /):
    min_fKrtQ = 1<<floor_log2_fKrtQ
    max_fKrtQ = (min_fKrtQ<<1) -1
    if floor_log2_fKrtQ >= 2:
        mid_fKrtQ = min_fKrtQ//2 *3
        assert min_fKrtQ < mid_fKrtQ < max_fKrtQ
        ls = [min_fKrtQ, mid_fKrtQ, max_fKrtQ]
    else:
        ls = [min_fKrtQ, max_fKrtQ]
    es = [find_max_e__k__fKrtQ(k, fKrtQ) for fKrtQ in ls]
    assert all(e0 <= e1 for e0, e1 in pairwise(ls))
    max_e = min(es) # min max
    assert max_e == es[0]
    return max_e

def find_max_e__k__fKrtQ(k, fKrtQ, /):
    for e in count(0):
        E = 1<<e
        lower_D_dd = ((fKrtQ*E+1)**k - (fKrtQ*E)**k)
        upper_D1_dd1 = (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))
        if (upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) >= (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1):
            break
    max_e = e-1
    return max_e

def iter_max_e__floor_log2_fKrtQ_ge_lt__k_ge_lt_(lower4k, upper4k, lower4floor_log2_fKrtQ, upper4floor_log2_fKrtQ, /):
    if not lower4k >= 2: raise ValueError(lower4k)
    return chain.from_iterable((iter_max_e__floor_log2_fKrtQ_ge_lt__k_eq_(k, lower4floor_log2_fKrtQ, upper4floor_log2_fKrtQ)) for k in range(lower4k,upper4k))
def iter_max_e__floor_log2_fKrtQ_lt__k_ge2_lt_(upper4k, upper4floor_log2_fKrtQ, /):
    return iter_max_e__floor_log2_fKrtQ_lt__k_ge_lt_(2, upper4k, 0, upper4floor_log2_fKrtQ)
def iter_max_e__floor_log2_fKrtQ_ge_lt__k_eq_(k, lower4floor_log2_fKrtQ, upper4floor_log2_fKrtQ, /):
    if not lower4floor_log2_fKrtQ >= 0: raise ValueError(lower4k)
    return (((k,floor_log2_fKrtQ), find_max_e__k__floor_log2_fKrtQ(k,floor_log2_fKrtQ)) for floor_log2_fKrtQ in range(lower4floor_log2_fKrtQ, upper4floor_log2_fKrtQ))


def find_max_e__floor_log2_fKrtQ_lt__k_lt_(upper4k, upper4floor_log2_fKrtQ, /):
    return [(find_max_e__floor_log2_fKrtQ_lt__k_eq_(k,upper4floor_log2_fKrtQ)) for k in range(upper4k)]
def find_max_e__floor_log2_fKrtQ_lt__k_eq_(k, upper4floor_log2_fKrtQ, /):
    return [((k,floor_log2_fKrtQ), find_max_e__k__floor_log2_fKrtQ(k,floor_log2_fKrtQ)) for floor_log2_fKrtQ in range(upper4floor_log2_fKrtQ)]
def find_max_e__fKrtQ_lt__k_eq_(k, upper4fKrtQ, /):
    return [((k,fKrtQ), find_max_e__k__fKrtQ(k,fKrtQ)) for fKrtQ in range(upper4fKrtQ)]


def ceil_log2(pint, /):
    e = floor_log2(pint)
    if not pint == (1<<e):
        e += 1
    return e

def floor_log2(pint, /):
    assert pint > 0
    return pint.bit_length()-1


def iter_rng4k_with_same_len_rng4fKrtQ0__5k_ge_lt(lower4k, upper4k, /):
    #[第一猜想] ==>> [1 <= k-1 <= 2**ceil_log2(k-1) <= fKrtQ0 <= floor_kth_root_(k,-1+2**(1+k*ceil_log2(k-1))) < 2*(k-1)]
    prev_k = lower4k
    if 2 <= lower4k < upper4k:
        prev_L = k2len_rng4fKrtQ0(prev_k)

    k = None
    for k in range(lower4k, upper4k):
        L = k2len_rng4fKrtQ0(k)
        if not L == prev_L:
            yield ((prev_k, k), prev_L)
            prev_k = k
            prev_L = L
    else:
        if not k is None:
            assert k+1 == upper4k
            yield ((prev_k, k+1), prev_L)

if 0:
  def iter_rng4k_of_same_len_rng4fKrtQ0__5k_ge_lt(lower4k, upper4k, /):
    #####ver1:bug:k2len_rng4fKrtQ0 并非 单调递增
    if not 2 <= lower4k <= upper4k: raise ValueError((lower4k, upper4k))
    ks = range(0, upper4k)
    while lower4k < upper4k:
        L = k2len_rng4fKrtQ0(lower4k)
        (middle_begin, middle_end) = bisearch(L, ks, begin=lower4k, key=k2len_rng4fKrtQ0)
        assert middle_begin == lower4k, ((lower4k, upper4k), (middle_begin, middle_end))
            #((10,21), (18,21))
            #k2len_rng4fKrtQ0 并非 单调递增:[[k<-[10,11]]->[k2len_rng4fKrtQ0)==2]][[k<-[12..=17]]->[k2len_rng4fKrtQ0)==1]]
        yield (middle_begin, middle_end)
        lower4k = middle_end

def k2len_rng4fKrtQ0(k, /):
    #[第一猜想] ==>> [1 <= k-1 <= 2**ceil_log2(k-1) <= fKrtQ0 <= floor_kth_root_(k,-1+2**(1+k*ceil_log2(k-1))) < 2*(k-1)]
    (begin4fKrtQ0, end4fKrtQ0) = k2rng4fKrtQ0(k)
    return end4fKrtQ0 -begin4fKrtQ0

def iter_rng4fKrtQ0__5k_ge_lt(lower4k, upper4k, /):
    #[第一猜想] ==>> [1 <= k-1 <= 2**ceil_log2(k-1) <= fKrtQ0 <= floor_kth_root_(k,-1+2**(1+k*ceil_log2(k-1))) < 2*(k-1)]
    if not lower4k >= 2: raise ValueError(lower4k)
    return ((k, k2rng4fKrtQ0(k)) for k in range(lower4k,upper4k))
def k2rng4fKrtQ0(k, /):
    #[第一猜想] ==>> [1 <= k-1 <= 2**ceil_log2(k-1) <= fKrtQ0 <= floor_kth_root_(k,-1+2**(1+k*ceil_log2(k-1))) < 2*(k-1)]
    assert k >= 2
    ceil_log2_Kneg1 = ceil_log2(k-1)
    min_fKrtQ0 = 1<<ceil_log2_Kneg1
    max_q0 = -1+(1<<(1+k*ceil_log2_Kneg1))
    (middle_begin, middle_end) = bisearch(max_q0, range(2*(k-1)), begin=min_fKrtQ0, key=lambda fKrtQ:fKrtQ**k)
    assert middle_begin <= middle_end <= middle_begin+1
    max_fKrtQ0 = middle_end-1
    assert k-1 <= min_fKrtQ0 <= max_fKrtQ0 < 2*(k-1) <= 2*min_fKrtQ0 == (1<<(1+ceil_log2_Kneg1))
    assert max_fKrtQ0**k <= max_q0 < (max_fKrtQ0+1)**k
    begin4fKrtQ0 = min_fKrtQ0
    end4fKrtQ0 = max_fKrtQ0+1
    return (begin4fKrtQ0, end4fKrtQ0)




if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call(globals(), None)
        #main()






