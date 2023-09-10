r'''[[[
e script/discrete_logarithm.py

离散对数:
  既然能开平方，那不就能检测出 离散对数的所有比特位？
p-1 = 2**e2 * p**ep * q**eq * ...
两个毛病
第一，x**2 最终循环，但不一定是1。所以开平方时，要保证最低的『1』比特确实下降，这个容易检测，发现没有，只要 sqrt*g**((p-1)///2)就行
    x**2 %7:
        6 --> 1 --> 1 # loop
        2 --> 4 --> 2 # loop
        3 --> 2 # join
        5 --> 4 # join

第二，sqrt 低位块的最高比特 混淆: sqrts_mod_(p; g**(2*k)) --> {g**k, g**(k +(p-1)///2)} ；不可区分！！

其实，只能 识别 最低e2比特
g**k == g**(k%(p-1))
解k 本就 %(p-1)
转换到 k%2**(e2+?)，只有最低e2比特保持，其余比特 等效混同，不可区分



discrete logarithm == generalized multiplicative order == index
MultiplicativeOrder
discrete logarithm problem (DLP)
[discrete_logarithm__(M;g;u) =[def]= min {k :<- [1..] | [g**k =[%M]= u]}]
  [[eg == order_mod_(M;g) == discrete_logarithm__(M;g;1)][u == g**k %M][k == discrete_logarithm__(M;g;u)][p2e4eg == factorization(eg)][M,g,eg,p2e4eg,u known][k unknown]]:
      #neednot:[is_primitive_root_mod_(M;g)]
      #有以下操作:
      [mul_pow_(M,g;a,b;u) := u**a *g**b %M]
      [gcd_exp_(M,g,p2e4eg;u) := gcd(eg,discrete_logarithm__(M;g;u))]
      [add_pow_(M,g;c,u) := u + g**c]

    若只使用以下操作:
      [mul_pow_(M,g;a,b;u) := u**a *g**b %M == g**(a*k+b) %M]
      [gcd_exp_(M,g,p2e4eg;u) := gcd(eg,k)]
    则 [[max p2e4eg.keys() <= B] -> [存在B的多项式时间算法求k]]
      通过 不断 加一 [u' := lntf_(M,g;1,1;u)] 直到 [gcd := gcd_exp_(M,g,p2e4eg;u)][gcd > 1]
        更新g,eg,p2e4eg:
          [g' := g**gcd]
          [eg' := eg///gcd]
          [p2e4eg[gcd] -= 1]
    也就是说[2**(2**k) +1 型的费马素数M，其离散对数最好求]
      #[u == g**k %M]
      #2可以替换成其他素数p，只不过 要确定余数需要O(p)操作
      let e,odd :=> [2**e*odd == eg]
      let bs := bin(k%2**e) via gcd_exp_ <<==:
        u_ := u
        es_ = []
        loop:
          let e_,odd_ :=> [2**e_*odd_ == gcd_exp_(M,g,p2e4eg;u_) == gcd(eg,k_)][odd_%2==1]
          if e_ == e:
            break
          u_ := mul_pow_(M,g;1,-e_;u_)
          es_.append(e_)
        [k%2** e == sum 2**e_ {e_ <- es_}]



#]]]'''#'''



from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers
from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power_,  iter_sqrts_mod_prime_
if 0:
    def iter_sqrts_mod_prime_(p, xx, /, *, _may_output4debug_=None, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
        'p/prime -> xx/int -> Iter x{x**2 =[%p]= xx} #output is strict sorted # [[upperbound4apply_floor_sqrt == Ellipsis] <-> [upperbound4apply_floor_sqrt == +oo]]'
    def iter_sqrts_mod_prime_power_(p, k, xx, /, *, _may_output4debug_=None, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
        'p/prime -> k/int{>=1} -> xx/int -> Iter x{x**2 =[%p**k]= xx} # output is strict sorted # [[upperbound4apply_floor_sqrt == Ellipsis] <-> [upperbound4apply_floor_sqrt == +oo]]'


def detect_(p, odd, e_, x_, /):
    y = pow(x_, odd<<e_, p)
    while not y == 1:
        y = pow(y, 2, p)
        e_ += 1
    return e_

def discrete_logarithm_mod_prime_(p, g, x, /):
    if not p >= 3: raise 000
    if not p & 1: raise 000
    x0 = x
    x_p = x%p
    if x_p == 0: raise 000
    e2, odd = factor_pint_out_2_powers(p-1)
    assert e2 >= 1

    x_ = x_p
    e_ = detect_(p, odd, 0, x_)
    ls = [(x_,e_)]
    while not x_ == 1:
        if e_ == 0:
            x_ *= g
            e_ = detect_(p, odd, 0, x_)
            ls.append((x_,e_))
        assert 0 < e_

        rs = [*iter_sqrts_mod_prime_(p, x_)]
        if not rs:
            raise 000

        x_1, x_2 = rs
        e_1 = detect_(p, odd, 0, x_1)
        e_2 = detect_(p, odd, 0, x_2)
        if e_ == e2:
            assert not e_1 == e_2
            assert {e_1, e_2} == {e2, e2-1}
            e_ = e2-1
            if e_1 == e_:
                x_ = x_1
            elif e_2 == e_:
                x_ = x_2
            else:
                raise 000
        else:
            assert 0 < e_ < e2
            x_1, x_2 = rs
            e_1 = detect_(p, odd, 0, x_1)
            e_2 = detect_(p, odd, 0, x_2)
            assert e_1 == e_2 == e_-1
            x_ = x_1
            e_ = e_1
        ls.append((x_,e_))


