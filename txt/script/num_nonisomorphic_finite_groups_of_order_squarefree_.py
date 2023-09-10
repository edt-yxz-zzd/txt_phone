r'''[[[
e script/num_nonisomorphic_finite_groups_of_order_squarefree_.py
will copy to:
    e ../../python3_src/nn_ns/math_nn/numbers/num_nonisomorphic_finite_groups_per_order.py
e ../../python3_src/nn_ns/math_nn/numbers/num_nonisomorphic_finite_groups_per_order.py

num_nonisomorphic_finite_groups_of_order_squarefree_

[[[
view  others/数学/algebra/order.txt
===
grep A000001 -r .
./others/数学/algebra/order.txt:https://oeis.org/A000001/b000001.txt
view  others/数学/algebra/order.txt
30,42,105,66,78
30 4
42 6
66 4
78 6
105 2
]]]

[[[
view others/数学/algebra/group.txt

===
FiniteGroup.html
  A convenient way to visualize groups is using so-called cycle graphs, which show the cycle structure of a given abstract group.
  Frucht's theorem states that every finite group is the graph automorphism group of a finite undirected graph.
  ...
  [p<q][素数p,q]:
    #the number of nonisomorphic finite groups of order p*q
    g(pq) = 1+[(q-1)%p==0]*1
    g(p^2) = 2
    g(p^3) = 5
  [squarefree n]:
    #the number of nonisomorphic finite groups of order squarefree n
    g(n)=sum_(d|n)product_(p|d; d!=1)(p^(o_p(n/d))-1)/(p-1)
      where o_p(m) is the number of primes q such that q|m and p|(q-1) (Dennis).

  [squarefree n]:
    #the number of nonisomorphic finite groups of order squarefree n
    [o_(p;m) =[def]= len{q :<- all_prime_factors_of(m) | [(q-1)%p == 0]}]
    [g(n) =[def]= sum~ II~ ((p^(o_(p;n/d))-1)/(p-1)) ~{p :<- all_prime_factors_of_(d) | [d =!= 1]} ~{d :<- all_factors_of_(n)}]
    ===
    [d :<- all_factors_of_(n) | [d =!= 1]]:
      [p :<- all_prime_factors_of_(d)]:
        [d == n]:
          [o_(p;n/d) == o_(p;1) == len{q :<- all_prime_factors_of(1) | [(q-1)%p == 0]} == 0]
          [(p^(o_(p;n/d))-1) == 0]
          [II~ ((p^(o_(p;n/d))-1)/(p-1)) ~{p :<- all_prime_factors_of_(d)} == [n==1]]
        [d == 1]:
          [II~ ((p^(o_(p;n/d))-1)/(p-1)) ~{p :<- all_prime_factors_of_(d)} == 1]
    ==>>:
    [g(n) == 1+sum~ II~ ((p^(o_(p;n/d))-1)/(p-1)) ~{p :<- all_prime_factors_of_(d)} ~{d :<- all_factors_of_(n) | [1 < d < n]}]
      :def____num_nonisomorphic_finite_groups_of_order_squarefree_:here
      #num_nonisomorphic_finite_groups_of_order_squarefree_(n)

    let [ps :|<=| all_primes][n == II(ps)][strict_sorted(ps)]
    [i2js :: [[uint]]]
    [i2js := [[j | [j :<- [i+1..<len(ps)]][q := ps[j]][(q-1)%p==0]] | [i :<- [0..<len(ps)]][p := ps[i]]]]
    [g(n) == 1+sum~ II~ [d := ...][p := ...]:Q_(es;i) ~{i :<- [0..<len(ps)] | [es[i] == 1]} ~{es :: [bit]{len(ps)} | [0 <- es][1 <- es]}]
      [es :<- ...][i :<- ...]:
        [d := II([p**e | [(p,e) :<- zip(ps,es)]])]
        [p := ps[i]]
        [o_(p;n/d) == len{j :<- i2js[i] | [es[j] == 0]}]
        [Q_(es;i) =[def]= ((p^(o_(p;n/d))-1)/(p-1))]
        [Q_(es;i) =[def]= ((p^(len{j :<- i2js[i] | [es[j] == 0]})-1)/(p-1))]


    #the number of nonisomorphic finite groups of order squarefree n
    [o_(p;m) =[def]= len{q :<- all_prime_factors_of(m) | [(q-1)%p == 0]}]
    [g(n) =[def]= sum~ II~ ((p^(o_(p;n/d))-1)/(p-1)) ~{p :<- all_prime_factors_of_(d) | [d =!= 1]} ~{d :<- all_factors_of_(n)}]
    [g(n) == 1+sum~ II~ ((p^(o_(p;n/d))-1)/(p-1)) ~{p :<- all_prime_factors_of_(d)} ~{d :<- all_factors_of_(n) | [1 < d < n]}]

    g(pq) = 1*? + p*? + q*? + pq*?
      = 1 + ((p^(o_(p;n/p))-1)/(p-1)) + ((q^(o_(q;n/q))-1)/(q-1)) + ((p^(o_(p;n/pq))-1)/(p-1))*((q^(o_(q;n/pq))-1)/(q-1))
      = 1 + ((p^(o_(p;q))-1)/(p-1)) + ((q^(o_(q;p))-1)/(q-1)) + ((p^(o_(p;1))-1)/(p-1))*((q^(o_(q;1))-1)/(q-1))
      !! [p<q]
      = 1 + ((p^(o_(p;q))-1)/(p-1)) + ((q^0-1)/(q-1)) + ((p^0-1)/(p-1))*((q^0-1)/(q-1))
      = 1 + ((p^(o_(p;q))-1)/(p-1))
      = 1+[(q-1)%p==0]*1
      #ok!

]]]

script.num_nonisomorphic_finite_groups_of_order_squarefree_
py -m nn_ns.app.adhoc_argparser__main__call8module    @num_nonisomorphic_finite_groups_of_order_squarefree_ =2 =3 =5
py script/num_nonisomorphic_finite_groups_of_order_squarefree_.py

#]]]'''#'''

being pseudoprimes.

e ../../python3_src/seed/math/all_primes.py
    LazySeq
from seed.types.LazySeq import LazySeq
            factor_pint
e ../../python3_src/nn_ns/math_nn/numbers/num_nonisomorphic_finite_groups_per_order.py
e others/数学/prime/primality_test.txt
e ../../python3_src/seed/math/prime_gens.py
A014233
primality_test_of_Miller_Rabin
from seed.math.is_prime__le_pow2_64 import is_prime__le_pow2_64
from seed.math.II import II
from seed.math.prime_gens import prime_gen, prime_filter__using_primality_test_, raw_iter_all_strict_sorted_primes__using_primality_test__lt_

def num_nonisomorphic_finite_groups_of_order_squarefree_N_(n, primes=None, is_prime_=is_prime__le_pow2_64):
def num_nonisomorphic_finite_groups_of_order_squarefree_(*primes, is_prime_=is_prime__le_pow2_64):
    if not all(type(p) is int for p in primes): raise TypeError
    ps = sorted({*primes})
    if not len(ps) == len(primes): raise ValueError(f'dup:{primes}')
    if not (not ps or ps[0] > 0): raise ValueError
    if not all(map(is_prime_, ps)): raise ValueError
    n = II(ps)
    L = len(ps)
    i2js = [[j for j in range(i+1, L) if (ps[j]-1)%ps[i] == 0] for i in range(L)]
    def Q_(es, i, /):
        count = sum(es[j] == 0 for j in i2js[i])
        p = ps[i]
        return ((p**count-1)//(p-1))
    def bits5u(u, /):
        return (*map(int, bin(u)[3:]),)
    u8bits = 1 << L
    return 1 + sum(II(Q_(es, i) for i in range(L) if es[i]==1) for es in map(bits5u, range(u8bits+1, (u8bits << 1)-1)))

def __():
    ts = (
    [((2,3,5), 30, 4)
    ,((2,3,7), 42, 6)
    ,((2,3,11), 66, 4)
    ,((2,3,13), 78, 6)
    ,((3,5,7), 105, 2)
    ])
    for (ps, n, ans) in ts:
        r = num_nonisomorphic_finite_groups_of_order_squarefree_(*ps)
        assert r == ans, (ps, n, ans, r)
__()
def __():
    from nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order import num_nonisomorphic_finite_groups5order_lt2048
    from nn_ns.math_nn.numbers.num_nonisomorphic_finite_groups_per_order import num_nonisomorphic_finite_groups5order
    for (group_order, num_nonisomorphic_finite_groups) in enumerate(num_nonisomorphic_finite_groups5order):
        if group_order > 0:
            factor_pint

    for 
__()
