#__all__:goto
r'''[[[
e script/辅助冫构造非平方判别式.py

script.辅助冫构造非平方判别式
py -m nn_ns.app.debug_cmd   script.辅助冫构造非平方判别式 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.辅助冫构造非平方判别式:__doc__ -ht # -ff -df

[[
源起:
/storage/emulated/0/0my_files/book/math/factorint/202308/Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance)/Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf
Grantham’s Frobenius test
    Frobenius pseudoprime
    stronger than Lucas test
nonsquare discriminant:(a**2-4*b)
    x**2-a*x+b
    x**2-P*x+Q
        Lucas pseudoprime with respect to (x**2-P*x+Q*x)

若是[Jacobi_symbol(p; a**2-4*b) == -1]，则 (x**2-(a+ka*p)*x+(b+kb*p))无整数解
    #若p是奇素数，则Jacobi_symbol是Legendre_symbol


view ../lots/NOTE/math-book/prime/The_new_book_of_prime_number_records-note.txt
[V(m+n) == Vm*Vn - Q**n*V(m-n)]
  特例:[V(2*n) == Vn**2 - Q**n*2]
  特例:[V(2*n+1) == Vnpp*Vn - Q**n*P]
  特例:[V(2*(n+1)) == Vnpp**2 - Q**(n+1)*2]
  (n,n+1) --> (2*n,2*n+1)
  (n,n+1) --> (2*n+1,2*n+2)
  最好是[Q==+/-1]
]]

[[[
py_adhoc_call   script.辅助冫构造非平方判别式   ,枚举冫素模辻相应参数纟非平方判别式扌 =3 =9
===34:
>>> for t in 枚举冫素模辻相应参数纟非平方判别式扌(3, 9):t
(3, 0, 2)
(3, 1, 2)
(3, 2, 2)
(5, 0, 1)
(5, 0, 2)
(5, 1, 1)
(5, 1, 2)
(5, 2, 1)
(5, 2, 2)
(5, 3, 1)
(5, 3, 2)
(5, 4, 1)
(5, 4, 2)
(7, 0, 3)
(7, 0, 4)
(7, 0, 6)
(7, 1, 3)
(7, 1, 4)
(7, 1, 6)
(7, 2, 3)
(7, 2, 4)
(7, 2, 6)
(7, 3, 3)
(7, 3, 4)
(7, 3, 6)
(7, 4, 3)
(7, 4, 4)
(7, 4, 6)
(7, 5, 3)
(7, 5, 4)
(7, 5, 6)
(7, 6, 3)
(7, 6, 4)
(7, 6, 6)

===
]]]
[[[
py_adhoc_call   script.辅助冫构造非平方判别式   ,枚举冫非平方判别式辻相应参数扌 =0 =66
===
(-3, 1, 1) # 避免使用(x**2+/-x+1)即 分圆多项式 某个(x**n-1)的因子 # 使用不可约二次函数就是为了构造GF(q**2);两根{x,a-x}必然在GF(q)之外，order_mod_(x**2-a*x+b;x)是重点，若是 分圆多项式，ZZ%[n;x**2-a*x+b]，即使是合数n，结果也十分好预测
>>> for t in 枚举冫非平方判别式辻相应参数扌(0, 66):t
(-3, 1, 1)
(-4, 0, 1)
(5, 1, -1)
(-7, 1, 2)
(-8, 0, 2)
(8, 2, -1)
(-11, 1, 3)
(-12, 0, 3)
(12, 4, 1)
(13, 3, -1)
(-15, 1, 4)
(-16, 0, 4)
(17, 1, -4)
(-19, 1, 5)
(-20, 0, 5)
(20, 4, -1)
(21, 5, 1)
(-23, 1, 6)
(-24, 0, 6)
(24, 0, -6)
(-27, 1, 7)
(-28, 0, 7)
(28, 0, -7)
(29, 5, -1)
(-31, 1, 8)
(-32, 0, 8)
(32, 6, 1)
(33, 1, -8)
(-35, 1, 9)
(-36, 0, 9)
(37, 1, -9)
(-39, 1, 10)
(-40, 0, 10)
(40, 6, -1)
(41, 1, -10)
(-43, 1, 11)
(-44, 0, 11)
(44, 0, -11)
(45, 7, 1)
(-47, 1, 12)
(-48, 0, 12)
(48, 0, -12)
(-51, 1, 13)
(-52, 0, 13)
(52, 0, -13)
(53, 7, -1)
(-55, 1, 14)
(-56, 0, 14)
(56, 0, -14)
(57, 1, -14)
(-59, 1, 15)
(-60, 0, 15)
(60, 8, 1)
(61, 1, -15)
(-63, 1, 16)
(-64, 0, 16)
(65, 1, -16)

===
]]]
[[[
===
[b==+/-1]
>>> for t in 枚举冫非平方判别式辻相应参数牜次参为正负一扌(0, 20):t
(-4, 0, 1)
(-4, 0, 1)
(5, -1, -1)
(-3, -1, 1)
(5, 1, -1)
(-3, 1, 1)
(8, -2, -1)
(8, 2, -1)
(13, -3, -1)
(5, -3, 1)
(13, 3, -1)
(5, 3, 1)
(20, -4, -1)
(12, -4, 1)
(20, 4, -1)
(12, 4, 1)
(29, -5, -1)
(21, -5, 1)
(29, 5, -1)
(21, 5, 1)
(40, -6, -1)
(32, -6, 1)
(40, 6, -1)
(32, 6, 1)
(53, -7, -1)
(45, -7, 1)
(53, 7, -1)
(45, 7, 1)
(68, -8, -1)
(60, -8, 1)
(68, 8, -1)
(60, 8, 1)
(85, -9, -1)
(77, -9, 1)
(85, 9, -1)
(77, 9, 1)
(104, -10, -1)
(96, -10, 1)
(104, 10, -1)
(96, 10, 1)
(125, -11, -1)
(117, -11, 1)
(125, 11, -1)
(117, 11, 1)
(148, -12, -1)
(140, -12, 1)
(148, 12, -1)
(140, 12, 1)
(173, -13, -1)
(165, -13, 1)
(173, 13, -1)
(165, 13, 1)
(200, -14, -1)
(192, -14, 1)
(200, 14, -1)
(192, 14, 1)
(229, -15, -1)
(221, -15, 1)
(229, 15, -1)
(221, 15, 1)
(260, -16, -1)
(252, -16, 1)
(260, 16, -1)
(252, 16, 1)
(293, -17, -1)
(285, -17, 1)
(293, 17, -1)
(285, 17, 1)
(328, -18, -1)
(320, -18, 1)
(328, 18, -1)
(320, 18, 1)
(365, -19, -1)
(357, -19, 1)
(365, 19, -1)
(357, 19, 1)
(404, -20, -1)
(396, -20, 1)
(404, 20, -1)
(396, 20, 1)


===
]]]


]]]'''#'''
__all__ = r'''
枚举冫素模辻相应参数纟非平方判别式扌
枚举冫非平方判别式辻相应参数扌
枚举冫非平方判别式辻相应参数牜次参为正负一扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.math.prime_gens import iter_primes__between_, prime_gen
#from seed.math.factor_pint_as_pefect_power_ import is_kth_power_, is_square_, is_cube_
from math import isqrt
from itertools import count# islice
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...


def 枚举冫素模辻相应参数纟非平方判别式扌(begin, may_end, /, *, reverse=False):
    '-> Iter (p, a, b){[odd_prime p][Jacobi_symbol(p; a**2-4*b) == -1]}'
    for p in iter_primes__between_(begin, may_end, reverse=reverse):
        if p == 2:continue
        a2aa = [pow(a,2,p) for a in range(p)]
        x2b_sq = [False]*p
        for aa in a2aa:
            x2b_sq[aa] = True
        for a in range(p):
            aa = a2aa[aa]
            for b in range(p):
                D = (aa-4*b)%p
                if not x2b_sq[D]:
                    yield (p, a, b)


def 枚举冫非平方判别式辻相应参数牜次参为正负一扌(min_absA, may_max_absA, /, *, reverse=False):
    '-> Iter (D, a, b){[nonsquare D][D==a**2-4*b][abs(b)==1]} # => [D%4 <- {0,1}]'
    check_int_ge(0, min_absA)
    if may_max_absA is None:
        if reverse:raise TypeError
        it = count(min_absA)
    else:
        max_absA = may_max_absA
        check_int_ge(0, max_absA)
        it = range(min_absA, 1+max_absA)
        if reverse:
            it = reversed(it)
    it = iter(it)
    for x in it:
      for a in [-x, +x]:
        for b in [-1, +1]:
            D = a**2 -4*b
            if 0 <= D == isqrt(D)**2:continue
            #if is_square_(D):continue
            yield (D, a, b)

def 枚举冫非平方判别式辻相应参数扌(min_absD, may_max_absD, /, *, reverse=False):
    '-> Iter (D, a, b){[nonsquare D][D==a**2-4*b]} # => [D%4 <- {0,1}]'
    check_int_ge(0, min_absD)
    if may_max_absD is None:
        if reverse:raise TypeError
        it = count(min_absD)
    else:
        max_absD = may_max_absD
        check_int_ge(0, max_absD)
        it = range(min_absD, 1+max_absD)
        if reverse:
            it = reversed(it)
    it = iter(it)
    for x in it:
      for x in [-x, +x]:
        if not x % 4 <= 1:continue
        if 0 <= x == isqrt(x)**2:continue
        #if is_square_(x):continue

        D = x
        done = False
        #try:b==+/-1
          #最好是[Q==+/-1] <<== 翻倍公式:含Q**n
        if D >= -4:
            for b in [-1, +1]:
                aa = D+4*b
                #if not is_square_(aa):continue
                if 0 <= aa == (a:=isqrt(aa))**2:
                    done = True
                    break

        if done:
            a
        elif D%4 == 1:
            a = 1
        else:
            a = 0
        a
        b = (a**2-D)//4
        assert D == a**2 -4*b
            # => [D%4 <- {0,1}]
        yield (D, a, b)

__all__
from script.辅助冫构造非平方判别式 import 枚举冫素模辻相应参数纟非平方判别式扌
from script.辅助冫构造非平方判别式 import *
