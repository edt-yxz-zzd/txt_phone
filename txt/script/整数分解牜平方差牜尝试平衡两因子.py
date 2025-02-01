#__all__:goto
r'''[[[
e script/整数分解牜平方差牜尝试平衡两因子.py

script.整数分解牜平方差牜尝试平衡两因子
py -m nn_ns.app.debug_cmd   script.整数分解牜平方差牜尝试平衡两因子 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.整数分解牜平方差牜尝试平衡两因子:__doc__ -ht # -ff -df

[[
源起:
    '/sdcard/0my_files/book/math/factorint/202308/Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
        Squares:page227:Lehman method (Algorithm 5.1.2)

是否可以乘上一个含有许多不同素因子的系数，已将两个未知因子提升到十分接近?
k = 2**e2 * 3**e3 ...
detect is_perfect_square(k*N)?
[N == p*q][k == u*v]:
    ???how [abs(u*p-q*v) < B]

]]
[[
Lehman method
    '/sdcard/0my_files/book/math/factorint/202308/Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
        Squares:page227:Lehman method (Algorithm 5.1.2)

[TIME{Lehman_method(n)} = O(n**/3 * TIME{sqrt(n)})]

[21 < n==p*q][floor(n**/3) < p <= q]:
    [floor(n**/3) < p <= q < ceil(n**(2/3))]
    [k :<- [1..=ceil(n**/3)]]
    [a :<- [ceil((4*k*n)**/2)..=ceil((4*k*n)**/2)+floor((n/(4*k)**3)**/6)]]
    [b := sqrt(a**2-4*k*n)]
    [b%1 == 0] => [gcd(a+b,n) is factor of n]
        # !! [(a+b) < n]

已知:[@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    [abs(u*q - p*v) < q/B]

证明:算法中(k,a)的范围合理
    # let [(u,v) :=> [k==u*v]]
    # [4*k*n == (2*u*q)*(2*p*v) == a**2-b**2 == (a+b)*(a-b)][a>=b]
    # [(2*b) == (a+b)-(a-b) == 2*abs(u*q - p*v) SHOULD_BE small enough]
    # [a**2 == 4*k*n + b**2 >= 4*k*n]
    # [a >= sqrt(4*k*n) == min_A]
    !! [@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    # [b == abs(u*q - p*v) < q/B < (n**(2/3))/B < (n**(2/3))]
    # [4*k*n <= min_A**2 <= a**2 == (min_A+dA)**2 == 4*k*n + b**2]
    # [2*min_A*dA+dA**2 == b**2 <= q**2/B**2]
    # [dA <= q**2/B**2/2/min_A == q**2/B**2/2/sqrt(4*k*n) == max_dA]
    ####bug:let [max_dA <= n**/3]
    #       !! max_dA(B) #see below:『let [max_k(B) <= n**/3]』
    #
    #
    # [k == u*v == (u/v)*v**2 < (p/q+1/(v*B))*v**2 == (p/q*v**2+v/B) <= (v**2*p/q+1) <= (B**2*p/q+1) == max_k]
    # [max_k(B) == ceil(B**2*p/q)]
    # 太大:[max_b(B) == floor(q/B)]
    # [max_dA(B,k) == q**2/B**2/2/sqrt(4*k*n)]
    # [最小化循环步骤]<->[最小化:sum[1+ max_b(B) | [k :<- [1..=max_k(B)]]]]<->[最小化:sum[1+ max_dA(B;k) | [k :<- [1..=max_k(B)]]]]
    #       『+1』 <<== 最外层循环 数量，因为[max_dA==0]时仍旧要加1每循环
    # [SUM <= sum[1+ q**2/B**2/2/sqrt(4*k*n) | [k :<- [1..<=(B**2*p/q)]]]]
    # let [max_k(B) <= n**/3]
    # [(B**2*p/q) <= n**/3]
    # [B <= n**/6 * sqrt(q/p)]
    # let [B := n**/6 * sqrt(q/p)]
    # [max_k(B) <= n**/3]
    # [max_dA == q**2/B**2/2/sqrt(4*k*n) == (n**/6)/4/sqrt(k)]
    # [SUM <= sum[1+ (n**/6)/4/sqrt(k) | [k :<- [1..<=n**/3]]] ~= (n**/3)+ (n**/6)/4 * Integral[1/sqrt(k) | [k :<- [1..<=n**/3]]] ~= (n**/3)+ (n**/6)/4 * 2*sqrt(k:=n**/3) ~= O(n**/3)]
    # DONE
    # ??? [(a+b)<n] <<== [n>=21]
    ##################
    ##################
    ##################
    ##################
    # 尝试 let [max_k(B) <= n**/4]
    #   虽然 前提试除 已经 O(n**/3)，但仍可以强行假设，试图分解
    # [(B**2*p/q) <= n**/4]
    # [B <= n**/8 * sqrt(q/p)]
    # let [B := n**/8 * sqrt(q/p)]
    # [max_k(B) == (B**2*p/q) == n**/4]
    # [max_dA(B,k) == q**2/B**2/2/sqrt(4*k*n) == (n**/4)/4/sqrt(k)]
    # [SUM <= sum[1+ (n**/4)/4/sqrt(k) | [k :<- [1..<=n**/4]]] ~= (n**/4)+ (n**/4)/4 * Integral[1/sqrt(k) | [k :<- [1..<=n**/4]]] ~= (n**/4)+ (n**/4)/4 * 2*sqrt(k:=n**/4) ~= O(n**(3/8)) > O(n**/3)]
    ##################
    ##################
    ##################
    # 尝试 let [max_k(B) <= n**/2]
    #   虽然 这样一来 外层循环 已经 O(n**/2)，但可以看看是否大量max_dA(B,k)小于1 # 其实[k:=n]直接就有[a==2*n][b==0][dA==0]
    # [(B**2*p/q) <= n**/2]
    # [B <= n**/4 * sqrt(q/p)]
    # let [B := n**/4 * sqrt(q/p)]
    # [max_k(B) == (B**2*p/q) == n**/2]
    # [max_dA(B,k) == q**2/B**2/2/sqrt(4*k*n) == 1/4/sqrt(k)] # ===0???
    # [SUM <= sum[1+ 1/4/sqrt(k) | [k :<- [1..<=n**/2]]] ~= (n**/2)+ 1/4 * Integral[1/sqrt(k) | [k :<- [1..<=n**/2]]] ~= (n**/2)+ 1/4 * 2*sqrt(k:=n**/2) ~= O(n**/2) > O(n**/3)] # >_<
    ##################
    ##################
    ##################
    ##################
    ##################
    ######################
    重头再来:
    [k == u*v]
    [a+b == 2*u*q]
    [a-b == 2*v*p > 0]
    [a > b >= 0]
    [4*k*n == (2*u*q)*(2*v*p) == (a+b)*(a-b)]
    [a >= (4*k*n)**/2]
    [b < (a+b)/2 == u*q < k*n**/2]
    !! [@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    [b == abs(u*q - p*v) < q/B]
    [4*k*n <= min_A**2 <= a**2 == (min_A+dA)**2 == 4*k*n + b**2]
    [2*min_A*dA+dA**2 == b**2 <= (q/B)**2]
    [dA <= (q/B)**2/2/min_A == (q/B)**2/2/sqrt(4*k*n) == max_dA]
    [max_dA == (q/B)**2/2/sqrt(4*k*n)]
    [k == u*v == (u/v)*v**2 < (p/q+1/(v*B))*v**2 == (p/q*v**2+v/B) <= (v**2*p/q+1) <= (B**2*p/q+1) == max_k]
    [max_k(B) == (1+B**2*p/q)]
    [max_dA(B,k) == (q/B)**2/2/sqrt(4*k*n)]
    [最小化循环步骤]<->[最小化:sum[1+ max_b(B) | [k :<- [1..=max_k(B)]]]]<->[最小化:sum[1+ max_dA(B;k) | [k :<- [1..=max_k(B)]]]]
        # 『+1』 <<== 最外层循环 数量，因为[max_dA==0]时仍旧要加1每循环
    [SUM <= sum[1+ (q/B)**2/2/sqrt(4*k*n) | [k :<- [1..<=(1+B**2*p/q)]]]]
    [max_k(B) <= 1+n**z]:
        [(1+B**2*p/q) <= 1+n**z]
        [B <= n**(z/2) * sqrt(q/p)]
    let [B := n**(z/2) * sqrt(q/p)]
    [max_k(B) == 1+n**z]
    [max_dA == (q/B)**2/2/sqrt(4*k*n) == n**(1/2-z)/4/sqrt(k)]
    [SUM <= sum[1+ n**(1/2-z)/4/sqrt(k) | [k :<- [1..<=1+n**z]]] ~= (n**z)+ n**(1/2-z)/4 * Integral[1/sqrt(k) | [k :<- [1..<=1+n**z]]] ~= (n**z)+ n**(1/2-z)/4 * 2*sqrt(k:=1+n**z) ~= O(n**z + n**(1/2-z/2))]
    [z == 1/2-z/2]:
        [z == 1/3]
    #######
    [gcd(a+b,n) < n]
        <<== [(a+b) < n]
    [a+b
    <= a + q/B
    == a + q / (n**(z/2) * sqrt(q/p))
    == a + n**(1/2-z/2)
    <= sqrt(4*k*n)+max_dA + n**(1/2-z/2)
    == sqrt(4*k*n) + n**(1/2-z)/4/sqrt(k) + n**(1/2-z/2)
    <= sqrt(4*max_k*n) + n**(1/2-z)/4/min_k + n**(1/2-z/2)
    == sqrt(4*(1+n**z)*n) + n**(1/2-z)/4/1 + n**(1/2-z/2)
    <= 2*n**/2 +2*n**(z/2+1/2) + n**(1/2-z)/4 + n**(1/2-z/2)
    == n**/2 *(2 +2*n**(z/2) + n**(-z)/4 + n**(-z/2))
    <= n**/2 *(2 +2*n**(z/2) +2)
    == 2*n**/2 *(2 +n**(z/2))
    ]
    [a+b <= 2*n**/2 *(2 +n**(z/2))]
    [a+b < n] <<==:
        [2*n**/2 *(2 +n**(z/2)) < n]
        [2*(2 +n**(z/2)) < n**/2]
        * [z==1/3]:
            [2*(2 +n**/6) < n**/2]
            [x := n**/6]
            [4 +2*x < x**3]
            [x==2]:
                [4 +2*x == x**3]
            [x > 2]
            [n**/6 > 2]
            [n > 2**6]
            [n > 64] #21???
    [a+b < n] <<== [2*(2 +n**(z/2)) < n**/2]
    # DONE
    ######################
    ######################


]]
[[[
上面是 [n==p*q][n**/3 < p <= q]
下面假设 [n==p*q][p <= q < sqrt2*p]
    #此可以通过不断乘2达到
    #   连续尝试试分解(n*2**ez) for ez in [0..log2(n)]
    # 而且不同因子 (n*R**e) 可以减小 sqrt2
===
失败:上面已是在调整k，这里预先调整并无用处....
<<==:
===
[n==p*q][p <= q < sqrt2*p]:
    [n==p*q < sqrt2*p**2]
    [p > n**/2 / sqrt_sqrt2]
    [n**/2 / sqrt_sqrt2 < p <= q < n**/2 * sqrt_sqrt2]
    [1 <= q/p < sqrt2]
    ######################
    [b == abs(u*q - p*v) < q/B]
    [max_k(B) == (1+B**2*p/q)]
    [max_dA(B,k) == (q/B)**2/2/sqrt(4*k*n)]
    [B := q]:
    ######################
    #下面部分 暂不考虑 [1 <= q/p < sqrt2]
    #   感觉似乎无法改进？

===
]]]
[[[
改进搜索次序，一层一层搜索
    =>每一层结束，可以中断；不必非得一次性O(n**/3)
    ######################
    # 以下内容，是复制上面的
    #   再尝试『偷懒』或者说调整为更有高效的搜索次序:
    #       窜改公式『1/(v*B)』-->『1/v/B**t』
    #       或者说:窜改公式『v<=B』-->『v**t<=B』
    ######################
    [k == u*v]
    [a+b == 2*u*q]
    [a-b == 2*v*p > 0]
    [a > b >= 0]
    [4*k*n == (2*u*q)*(2*v*p) == (a+b)*(a-b)]
    [a >= (4*k*n)**/2]
    [b < (a+b)/2 == u*q < k*n**/2]
    原:!! [@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    窜改: [t>=1][@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v**t <= B][abs(u/v - p/q) < 1/(v*B)]]]
    [b == abs(u*q - p*v) < q/B]
    [4*k*n <= min_A**2 <= a**2 == (min_A+dA)**2 == 4*k*n + b**2]
    [2*min_A*dA+dA**2 == b**2 <= (q/B)**2]
    [dA <= (q/B)**2/2/min_A == (q/B)**2/2/sqrt(4*k*n) == max_dA]
    [max_dA == (q/B)**2/2/sqrt(4*k*n)]
    原:[k == u*v == (u/v)*v**2 < (p/q+1/(v*B))*v**2 == (p/q*v**2+v/B) <= (v**2*p/q+1) <= (B**2*p/q+1) == max_k]
    窜改:[k == u*v == (u/v)*v**2 < (p/q+1/(v*B))*v**2 == (p/q*v**2+v/B) <= (v**2*p/q+1) <= (B**(2/t)*p/q+1) == max_k]
    [max_k(B) == (1+B**(2/t)*p/q)]
    [max_dA(B,k) == (q/B)**2/2/sqrt(4*k*n)]
    [最小化循环步骤]<->[最小化:sum[1+ max_b(B) | [k :<- [1..=max_k(B)]]]]<->[最小化:sum[1+ max_dA(B;k) | [k :<- [1..=max_k(B)]]]]
        # 『+1』 <<== 最外层循环 数量，因为[max_dA==0]时仍旧要加1每循环
    [SUM <= sum[1+ (q/B)**2/2/sqrt(4*k*n) | [k :<- [1..<=(1+B**(2/t)*p/q)]]]]
    [max_k(B) <= 1+n**z]:
        [(1+B**(2/t)*p/q) <= 1+n**z]
        [B <= n**(t*z/2) * sqrt(q/p)**t]
    let [B := n**(t*z/2) * sqrt(q/p)**t]
    [max_k(B) == 1+n**z]
    [max_dA == (q/B)**2/2/sqrt(4*k*n)
    == (q/n**(t*z/2) / sqrt(q/p)**t)**2/2/sqrt(4*k*n)
    == (q**2/n**(t*z) / (q/p)**t)/4/sqrt(k*n)
    == (q**(2-t) * p**t/n**(t*z))/4/sqrt(k*n)
    == (n**(t-t*z-1/2))/q**(2*t-2)/4/sqrt(k)
    <= (n**(t-t*z-1/2))/n**(t-1)/4/sqrt(k)
    == (n**(1/2-t*z))/4/sqrt(k)
    ]
    [max_dA == (n**(1/2-t*z))/4/sqrt(k)]
    [SUM <= sum[1+ n**(1/2-t*z)/4/sqrt(k) | [k :<- [1..<=1+n**z]]] ~= (n**z)+ n**(1/2-t*z)/4 * Integral[1/sqrt(k) | [k :<- [1..<=1+n**z]]] ~= (n**z)+ n**(1/2-t*z)/4 * 2*sqrt(k:=1+n**z) ~= O(n**z + n**(1/2+z/2-t*z))]
    [z == 1/2+z/2-t*z]:
        [z == 1/(1+2*t)]
        !! [t >= 1]
        [z <= 1/3]
        计算量:O(n**z)
        计算量:O(n**/(1+2*t))
        计算量翻倍:
            ?_t :=> [n**/(1+2*_t) == ZZZ*n**/(1+2*t)]
            [1/(1+2*_t) == log(n;ZZZ) + 1/(1+2*t)]
            [(1+2*_t) == (1+2*t)/(log(n;ZZZ)*(1+2*t) + 1)]
            [_t == (1/2+t)/(log(n;ZZZ)*(1+2*t) + 1) -1/2]
            [_t - t
            == (1/2+t)/(log(n;ZZZ)*(1+2*t) + 1) -1/2 -t
            == (1/2+t)*log(ZZZ;n)/((1+2*t) + log(ZZZ;n)) -1/2 -t
            == ((log(ZZZ;n)/2+t*log(ZZZ;n)) -((1+2*t)*t + t*log(ZZZ;n)))/((1+2*t) + log(ZZZ;n)) -1/2
            == (log(ZZZ;n)/2 -(1+2*t)*t)/((1+2*t) + log(ZZZ;n)) -1/2
            == (-2*(1+2*t)*t -(1+2*t))/2/((1+2*t) + log(ZZZ;n))
            == -(1+2*t)**2/2/((1+2*t) + log(ZZZ;n))
            ]
        计算量翻倍公式: [_t -t == -(1+2*t)**2/2/((1+2*t) + log(ZZZ;n))]
    #######
    [gcd(a+b,n) < n]
        <<== [(a+b) < n]
    [a+b
    <= a + q/B
    == a + q / (n**(t*z/2) * sqrt(q/p)**t)
    == a + n**(t/2*(1-z)) /q**(t-1)
    <= sqrt(4*k*n)+max_dA + n**(t/2*(1-z)) /q**(t-1)
    == sqrt(4*k*n) + (n**(1/2-t*z))/4/sqrt(k) + n**(t/2*(1-z)) /q**(t-1)
    <= sqrt(4*max_k*n) + n**(1/2-t*z)/4/min_k + n**(t/2*(1-z)) /q**(t-1)
    == sqrt(4*(1+n**z)*n) + n**(1/2-t*z)/4/1 + n**(t/2*(1-z)) /q**(t-1)
    <= 2*n**/2 +2*n**(z/2+1/2) + n**(1/2-t*z)/4 + n**(t/2*(1-z)) /q**(t-1)
    == n**/2 *(2 +2*n**(z/2) + n**(-t*z)/4 + n**(((t-1)-t*z)/2) /q**(t-1))
    # t消失，归同
    <= n**/2 *(2 +2*n**(z/2) +2)
    == 2*n**/2 *(2 +n**(z/2))
    ]
    [a+b <= 2*n**/2 *(2 +n**(z/2))]
    [a+b < n] <<==:
        [2*n**/2 *(2 +n**(z/2)) < n]
        [2*(2 +n**(z/2)) < n**/2]
        * [z==1/3]:
            [2*(2 +n**/6) < n**/2]
            [x := n**/6]
            [4 +2*x < x**3]
            [x==2]:
                [4 +2*x == x**3]
            [x > 2]
            [n**/6 > 2]
            [n > 2**6]
            [n > 64] #21???
    [a+b < n] <<== [2*(2 +n**(z/2)) < n**/2]
    # DONE
    ######################
    上面的[t>=1]可以从大值开始尝试，直至1:
    [t :<- [100,99..=1]]:
        # 也不必非得整数t，可按计算量翻倍逐次降低t
        # 计算量翻倍公式: [_t -t == -(1+2*t)**2/2/((1+2*t) + log(ZZZ;n))]
        [z == 1/(1+2*t)]
        [max_k(B) == 1+n**z]
        [max_dA(B,k) == (n**(1/2-t*z))/4/sqrt(k)]
    ######################

===
]]]



py_adhoc_call   script.整数分解牜平方差牜尝试平衡两因子   @_尝试一下 ='2**20'
'fail'
    p = 2**521-1
    q = 2**607-1
    N = p*q
    ps = iter_prime_basis4II_prime_basis_gtN_(N)
    k = 2**500 * 3**100 * 5**50 * 7**20 * II(ps)
    kN = k*N
    R = isqrt(kN)



from script.整数分解牜平方差牜尝试平衡两因子 import *
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

from math import isqrt, gcd

def is_perfect_square(n, /):
    return isqrt(n)**2 == n
def _尝试一下(B=2**16, /):
    from seed.math.prime_gens import iter_prime_basis4II_prime_basis_gtN_
    from seed.math.II import II
    #2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667
    p = 2**521-1
    q = 2**607-1
    N = p*q
    ps = iter_prime_basis4II_prime_basis_gtN_(N)
    k = 2**500 * 3**100 * 5**50 * 7**20 * II(ps)
    kN = k*N
    R = isqrt(kN)
    a = (R+1)
    d = a**2-kN
    assert d > 0
    for _ in range(B):
        if is_perfect_square(d):
            ok = True
            break
        d += (a<<1)|1
        a += 1
    else:
        ok = False
    ok
    if not ok:
        return 'fail'
    b = isqrt(d)
    # [k*N == a**2-b**2]
    ft = gcd(a-b, N)
    assert ft in (p,q), (a, d, ft)
    return 'ok'

__all__
from script.整数分解牜平方差牜尝试平衡两因子 import *
