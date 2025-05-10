#__all__:goto
r'''[[[
e script/制表冫间歇性素数数量.py

script.制表冫间歇性素数数量
py -m nn_ns.app.debug_cmd   script.制表冫间歇性素数数量 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.制表冫间歇性素数数量:__doc__ -ht # -ff -df

[[
  /sdcard/0my_files/book/math/factorint/snd/The new book of prime number records(3ed)(1996)(Ribenboim).djvu
  ===
  #@page214[239/567]
  [?[x0 :: real] -> @[f,h :: real{>x0} -> real{>0}] -> [[f(x) /~/ h(x)] <-> [lim{f(x)/h(x) | x-->+oo} == 1]]]
  [?[x0 :: real] -> @[f,h :: real{>x0} -> real{>0}] -> [[have_the_same_order_of_magnitude_(f,h)] <-> [?[C4inferior,C4superior :: real{>0}] -> ?[x1 :: real{>x0}] -> @[x :: real{>x1}] -> [C4inferior <= f(x)/h(x) <= C4superior]]]]
  [?[x0 :: real] -> @[f,g :: real -> real] -> @[h :: real{>x0} -> real{>0}] -> [[f(x) == g(x) +O(h(x))] <-> [have_the_same_order_of_magnitude_((\x->h(x)+abs(f(x)-g(x))),h)]]]
    # big_O_notation
  [?[x0 :: real] -> @[f,g :: real -> real] -> @[h :: real{>x0} -> real{>0}] -> [[f(x) == g(x) +o(h(x))] <-> [lim{(f(x)-g(x))/h(x) | x-->+oo} == 0]]]
    # ???small_O_notation
  ===
  [n :<- [1..]]:
    [PRIMES_S1[n] =[def]= PRIMES[n-1]]
      @page3[28/567]
  [PRIMES_S1[1] == PRIMES[0] == 2]
  ===
  II. The nth Prime and Gaps
  page249[274/567]
  [[sufficiently large n] => [PRIMES_S1[n] == n*ln(n) + n*(lnln(n)-1) + o(n*lnln(n)/ln(n))]]
  [[n>=1] -> [1/4*n*ln(n) < PRIMES_S1[n] < 36*n*ln(n)]]
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-10) < PRIMES_S1[n] < n*ln(n) + n*(lnln(n)+8)]]
    # [[n>=2] -> [-10 < (PRIMES_S1[n]/n -ln(n) -lnln(n)) < 8]]
    # [[n>=2] -> [abs(PRIMES_S1[n]/n -ln(n) -lnln(n) +1) < 9]]
  [[n>=1] -> [PRIMES_S1[n] > n*ln(n)]]
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-1.0072629) <= PRIMES_S1[n]]]
  [[n>=2] -> [PRIMES_S1[n] <= 10**11] -> [n*ln(n) + n*(lnln(n)-1) <= PRIMES_S1[n]]]
  [[n>=7022] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.9385)]]
    #[不太对,缩放方向错误:当为『-0.9384』]: [n==7022] => -0.93844... <<== -0.9384449719153132
  [PRIMES_S1[7022] == PRIMES[7021] == 70919]
  ==>>:
  #cancel:注意下面数据:多了减一个1
    #old:[n>=2] => (PRIMES_S1[n]/n -ln(n) -lnln(n) +1)
    #new:[n>=2] => (PRIMES_S1[n]/n -ln(n) -lnln(n) +0)
  [[n>=2194] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.9)]]
    #(2193, 19381, -1.900217878683324)
    #(2193, 19381, -0.9002178786833239)
  [PRIMES_S1[2194] == PRIMES[2193] == 19381]

  [[n>=227] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.8)]]
    #(226, 1433, -1.8031833731015237)
  [PRIMES_S1[227] == PRIMES[226] == 1433]

  [[n>=103] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.7)]]
    #(102, 563, -1.7022872973458798)
  [PRIMES_S1[103] == PRIMES[102] == 563]

  [[n>=49] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.6)]]
    #(48, 227, -1.6180442280243583)
  [PRIMES_S1[49] == PRIMES[48] == 227]

  [[n>=25] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.5)]]
    #(24, 97, -1.5079080007552566)
  [PRIMES_S1[25] == PRIMES[24] == 97]

  [[n>=17] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.4)]]
    #(16, 59, -1.404036633536879)
  [PRIMES_S1[17] == PRIMES[16] == 59]

  [[n>=12] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.3)]]
    #(11, 37, -0.3118084098199928)
  [PRIMES_S1[12] == PRIMES[11] == 37]

  [[n>=10] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.2)]]
    #(9, 29, -0.23661753824200193)
  [PRIMES_S1[10] == PRIMES[9] == 29]

  [[n>=7] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.1)]]
    #(6, 17, -0.18306853106216125)
  [PRIMES_S1[7] == PRIMES[6] == 17]

  [[n>=5] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +0.1147)]]
    #(4, 11, 0.11467709223878936)
  [PRIMES_S1[5] == PRIMES[4] == 11]

  [[n>=3] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +0.4741)]]
    #(2, 5, 0.47400655038185785)
  [PRIMES_S1[3] == PRIMES[2] == 5]

  [[n>=2] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +1.1734)]]
    #(1, 3, 1.173365740021719)
  [PRIMES_S1[2] == PRIMES[1] == 3]


  !! [[n>=2] -> [n*ln(n) + n*(lnln(n)-1.0072629) <= PRIMES_S1[n]]]
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-1.0072629) <= PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +1.1734)]]
    => [[n>=2] -> [n*ln(n) + n*(lnln(n)-1.0073) <= PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +1.1734)]]
  !!:
    # 1.0072629 ~ '0x1.01dbfb3df95fdp+0'
    # 1.173365740021719 ~ '0x1.2c61b277a3df0p+0'
  !! [1.0072629 < float.fromhex('0x1.02') == 1.0078125 == 258/256 == 129/128]
  !! [1.173365740021719 < float.fromhex('0x1.2d') == 1.17578125 == 301/256]
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-258/256) <= PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +301/256)]]

  !! [1.0072629 < float.fromhex('0x1.01dc') == 1.00726318359375 == 66012/65536 == 16503/16384 == 33006/32768 == 1+238/2**15]
  !! [1.173365740021719 < float.fromhex('0x1.2c62') == 1.173370361328125 == 76898/65536 == 38449/32768 == 1+5681/2**15]
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-1-238/2**15) <= PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +1+5681/2**15)]]

  !! [1+3/413 == 416/413 == 1.0072639225181599 > 1.0072629]
  !! [1+69/398 == 467/398 == 1.1733668341708543 > 1.173365740021719]
    # [:why__416over413__467over398]:goto
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-416/413) <= PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +467/398)]]
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-1-3/413) <= PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +1+69/398)]]



  [[n>=2] -> [n*ln(n) + n*(lnln(n)-1.0072629) <= PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) +(head [err | [(j,p,err) :<- [(7021, 70919, -0.9384) ,(2193, 19381, -0.9002) ,(226, 1433, -0.8031) ,(102, 563, -0.7022) ,(48, 227, -0.6180) ,(24, 97, -0.5079) ,(16, 59, -0.4040) ,(11, 37, -0.3118) ,(9, 29, -0.2366) ,(6, 17, -0.1830) ,(1, 3, 1.1734)]][n>=j+1]])]]
    #(7021, 70919, -0.9384449719153132)
    #(2193, 19381, -0.9002178786833239)
    #(226, 1433, -0.8031833731015237)
    #(102, 563, -0.7022872973458798)
    #(48, 227, -0.6180442280243583)
    #(24, 97, -0.5079080007552566)
    #(16, 59, -0.404036633536879)
    #(11, 37, -0.3118084098199928)
    #(9, 29, -0.23661753824200193)
    #(6, 17, -0.18306853106216125)
    #(4, 11, 0.11467709223878936)
    #(2, 5, 0.47400655038185785)
    #(1, 3, 1.173365740021719)
]]
[[
[:why__416over413__467over398]:here
===

1.0072629
py_adhoc_call   seed.math.continued_fraction.continued_fraction5ND   @list.iter_continued_fraction_digits5ND_  =10072629 =10000000
[1, 137, 1, 2, 5, 2, 1, 1, 76, 5, 2]

1.173365740021719
py_adhoc_call   seed.math.continued_fraction.continued_fraction5ND   @list.iter_continued_fraction_digits5ND_  =1173365740021719 =1000000000000000
[1, 5, 1, 3, 3, 5, 5, 1, 1, 2, 1, 1, 2, 1, 5, 1, 3, 1, 3, 3, 4, 1, 1, 33, 1, 2, 3, 1, 1, 2, 1, 1, 5, 1, 3, 2, 9]

py_adhoc_call   seed.math.continued_fraction.continued_fraction5ND   @list.iter_continued_fraction_digits5ND_  =416 =413
[1, 137, 1, 2]
py_adhoc_call   seed.math.continued_fraction.continued_fraction5ND   @list.iter_continued_fraction_digits5ND_  =467 =398
[1, 5, 1, 3, 3, 5]

1.0072629
py_adhoc_call   seed.math.continued_fraction.continued_fraction_fold   ,iter_approximate_fraction_NDs5continued_fraction_  ='[1, 137, 1, 2, 5, 2, 1, 1, 76, 5, 2]'
(1, 1)
(138, 137)
(139, 138)
(416, 413)
(2219, 2203)
(4854, 4819)
(7073, 7022)
(11927, 11841)
(913525, 906938)
(4579552, 4546531)
(10072629, 10000000)

1.173365740021719
py_adhoc_call   seed.math.continued_fraction.continued_fraction_fold   ,iter_approximate_fraction_NDs5continued_fraction_  ='[1, 5, 1, 3, 3, 5, 5, 1, 1, 2, 1, 1, 2, 1, 5, 1, 3, 1, 3, 3, 4, 1, 1, 33, 1, 2, 3, 1, 1, 2, 1, 1, 5, 1, 3, 2, 9]'
(1, 1)
(6, 5)
(7, 6)
(27, 23)
(88, 75)
(467, 398)
(2423, 2065)
(2890, 2463)
(5313, 4528)
(13516, 11519)
(18829, 16047)
(32345, 27566)
(83519, 71179)
(115864, 98745)
(662839, 564904)
(778703, 663649)
(2998948, 2555851)
(3777651, 3219500)
(14331901, 12214351)
(46773354, 39862553)
(201425317, 171664563)
(248198671, 211527116)
(449623988, 383191679)
(15085790275, 12856852523)
(15535414263, 13240044202)
(46156618801, 39336940927)
(154005270666, 131250866983)
(200161889467, 170587807910)
(354167160133, 301838674893)
(908496209733, 774265157696)
(1262663369866, 1076103832589)
(2171159579599, 1850368990285)
(12118461267861, 10327948784014)
(14289620847460, 12178317774299)
(54987323810241, 46862902106911)
(124264268467942, 105904121988121)
(1173365740021719, 1000000000000000)

138/137
416/413
4854/4819

6/5
27/23
467/398
2890/2463

[1+3/413 == 416/413 == 1.0072639225181599 > 1.0072629]
[1+69/398 == 467/398 == 1.1733668341708543 > 1.173365740021719]

1.0072629
>>> 138/137
1.0072992700729928
>>> 416/413
1.0072639225181599
>>> 4854/4819
1.007262917617763

1.173365740021719
>>> 6/5
1.2
>>> 27/23
1.173913043478261
>>> 467/398
1.1733668341708543
>>> 2890/2463
1.173365814047909

]]

>>> from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import raw_iter_cf_digits4e_the_natural_logarithm_base_
>>> from seed.math.continued_fraction.continued_fraction_fold import approximate_fraction_boundaries5continued_fraction__by_limit_denominator_
>>> approximate_fraction_boundaries5continued_fraction__by_limit_denominator_(10000, raw_iter_cf_digits4e_the_natural_logarithm_base_())
(Fraction(25946, 9545), Fraction(23225, 8544))



py -m nn_ns.math_nn.numbers.prime_number
    => 『deprecated, use INumberList/INumberTable instead』
view ../../python3_src/nn_ns/math_nn/numbers/prime_number.py
view ../../python3_src/nn_ns/math_nn/numbers/least_positive_primitive_root_of_prime.py
from nn_ns.math_nn.numbers.least_positive_primitive_root_of_prime import j2prime, j2min_primitive_root, j2min_prime_primitive_root__head_eq_1, j2min_prime_primitive_root__head_eq_3
    j2prime = PRIMES[:10**4]


py_adhoc_call   script.制表冫间歇性素数数量   @_ge_PRIME_1__le_PRIME_7020_  =1
new:((2687, 24137, -0.9834403085234653), (1, 3, 1.173365740021719), (7021, 70919, -0.9384449719153132))
old:((2687, 24137, -1.9834403085234653), (1, 3, 0.173365740021719), (7021, 70919, -1.9384449719153132))

[[
===
py_adhoc_call   script.制表冫间歇性素数数量   ,_ge_PRIME_1__le_PRIME_7020_  =2
    #80行:
(7021, 70919, -0.9384449719153132)
(7020, 70913, -0.9377025743220013)
(7018, 70891, -0.9376419158677063)
(7016, 70877, -0.9364412238277446)
(7015, 70867, -0.9362682486928078)
(7013, 70849, -0.9356370735294424)
(7012, 70843, -0.9348936075086125)
(7011, 70841, -0.9335795011489432)
(6946, 70117, -0.9329042128341585)
(6945, 70111, -0.932154702447725)
(6935, 70001, -0.9318577343705394)
(6934, 69997, -0.9308187434659634)
(6933, 69991, -0.9300679095666702)
(4271, 40813, -0.9296714865570368)
(4265, 40751, -0.9291945322409516)
(3470, 32359, -0.9278120208505638)
(3469, 32353, -0.926530989059132)
(3466, 32323, -0.9261452179386338)
(3465, 32321, -0.9237085272972991)
(3463, 32303, -0.9228727726498964)
(3462, 32299, -0.9210108369833252)
(3461, 32297, -0.9185702173133148)
(3438, 32059, -0.917900132481229)
(3437, 32057, -0.9154438115268335)
(3436, 32051, -0.914149960621705)
(3427, 31957, -0.9141441788231908)
(2226, 19681, -0.9132732108362478)
(2200, 19427, -0.9110119440014959)
(2199, 19423, -0.9083046185444554)
(2198, 19421, -0.9046855565169118)
(2197, 19417, -0.9019733498310298)
(2193, 19381, -0.9002178786833239)
(2192, 19379, -0.8965866139086285)
(2191, 19373, -0.8947770850079806)
(1414, 11807, -0.8923902076647017)
(1413, 11801, -0.8899279641489413)
(1411, 11783, -0.8892439876702656)
(1410, 11779, -0.8853585283825292)
(1409, 11777, -0.8800496804773725)
(946, 7481, -0.8783460388247402)
(945, 7477, -0.8730130532626932)
(942, 7451, -0.8718000375088748)
(712, 5407, -0.8684661079730926)
(711, 5399, -0.8674339772258646)
(710, 5393, -0.8635882339792418)
(709, 5387, -0.8597338943243826)
(708, 5381, -0.8558709250869898)
(491, 3527, -0.854083423136063)
(489, 3511, -0.8527457970647963)
(482, 3457, -0.8439877234039983)
(481, 3449, -0.8433280027936585)
(463, 3301, -0.8404663537084873)
(462, 3299, -0.8269115626766652)
(383, 2657, -0.8148709250127633)
(228, 1447, -0.807569061960451)
(226, 1433, -0.8031833731015237)
(225, 1429, -0.7877206686477907)
(224, 1427, -0.7632542534935378)
(223, 1423, -0.7475207879782326)
(108, 599, -0.7416549742922087)
(107, 593, -0.7351438830654486)
(106, 587, -0.7286121604788136)
(103, 569, -0.7088972862225538)
(102, 563, -0.7022872973458798)
(101, 557, -0.6956589922970857)
(68, 347, -0.6482933243521112)
(48, 227, -0.6180442280243583)
(47, 223, -0.5789324752070328)
(34, 149, -0.566658170401084)
(25, 101, -0.5546242942155544)
(24, 97, -0.5079080007552566)
(18, 67, -0.4980414892148384)
(16, 59, -0.404036633536879)
(12, 41, -0.35304193836349407)
(11, 37, -0.3118084098199928)
(9, 29, -0.23661753824200193)
(6, 17, -0.18306853106216125)
(4, 11, 0.11467709223878936)
(2, 5, 0.47400655038185785)
(1, 3, 1.173365740021719)
===
]]



from script.制表冫间歇性素数数量 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

def _ge_PRIME_1__le_PRIME_7020_(ver=1):
    from math import log as ln
    from nn_ns.math_nn.numbers.least_positive_primitive_root_of_prime import j2prime, j2min_primitive_root, j2min_prime_primitive_root__head_eq_1, j2min_prime_primitive_root__head_eq_3
    ps = j2prime[:7021]
        #PRIMES[:7021]
    def f(n, b_tail=False):
        #new:[n>=2] => (PRIMES_S1[n]/n -ln(n) -lnln(n) +0)
        #old:[n>=2] => (PRIMES_S1[n]/n -ln(n) -lnln(n) +1)
        assert n >= 2
        if 0:
            assert n < 7022
            p = ps[n-1]
        else:
            assert n < 7022+b_tail
            p = j2prime[n-1]
        p
        lnN = ln(n)
        lnlnN = ln(lnN)
        #new:
        return p/n -lnN -lnlnN
        #old:
        #bug:return p/n -lnN -lnlnN -1
        return p/n -lnN -lnlnN +1
    n4min = min(range(2, 7022), key=f)
    n4max = max(range(2, 7022), key=f)
    j4min = -1+n4min
    j4max = -1+n4max
    p4min = ps[j4min]
    p4max = ps[j4max]
    err4min = f(n4min)
    err4max = f(n4max)
    n4tail = 7022
    j4tail = -1+n4tail
    p4tail = j2prime[j4tail]
    err4tail = f(n4tail, b_tail=True)
    if ver==1:
        return ((j4min, p4min, err4min), (j4max, p4max, err4max), (j4tail, p4tail, err4tail))
            # new:((2687, 24137, -0.9834403085234653), (1, 3, 1.173365740021719), (7021, 70919, -0.9384449719153132))
            # old:((2687, 24137, -1.9834403085234653), (1, 3, 0.173365740021719), (7021, 70919, -1.9384449719153132))

    ls = [(n-1, f(n, b_tail=True)) for n in range(2, 7023)]
    max_err = -2
    assert all(err > max_err for j, err in reversed(ls))
    outs = []
    for j, err in reversed(ls):
        if err >= max_err:
            max_err = err
            outs.append((j, j2prime[j], err))
    if ver==2:
        return outs

#def 列表冫素数牜极简素数筛扌():
#def 列表冫素数牜极简素数筛牜轮空型扌():

__all__
from script.制表冫间歇性素数数量 import *
