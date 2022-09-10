r'''[[[
tabulate_best_u2eu__lt另一种方案:
    PRIMES[:k]
        某一指数+=1
    t := II (p**e[p])
        t由小到大排序
        ??保持 [[p<q]->[e[p]>=e[q]]]
            论文中的数据的指数:
                [1]
                [2,1]
                [2,1,1]
                [2,2,1]
                [3,1,1,1]
                [2,2,1,1]
                [4,1,1,1]
                [3,2,1,1]
                [4,2,1,1]
                [4,3,1,1]
                [4,2,1,1,1]
                [5,2,1,1,1]
                [4,2,1,1,1,1]
                [5,2,1,1,1,1]
                [5,3,1,1,1,1]
                [5,2,1,1,1,1,1]
                [5,3,1,1,1,1,1]
                [5,3,2,1,1,1,1]
                [5,3,1,1,1,1,1,1]
                [5,3,2,1,1,1,1,1]

    #找出所有 素数q, 满足[t%(q-1)==0]
    pseudo_q := 1+II (p**e_ where e_ < e[p])
    is_prime(pseudo_q)
        正好 (pseudo_q-1)的分解完全知晓...素性证明...
        后面要用到q的 本原根
            #甚至制表 求离散对数
            #q太大也不好



e script/primality_test.py
see also:
    view script/primality_test.py
    view ../../python3_src/nn_ns/math_nn/inv_phi.py

py script/primality_test.py --tabulate_best_u2eu__lt 100
py script/primality_test.py --tabulate_best_u2eu__lt 10000 -o script/primality_test.py.out.tabulate_best_u2eu__lt.10000.txt
view  script/primality_test.py.out.tabulate_best_u2eu__lt.10000.txt
py script/primality_test.py --tabulate_best_u2eu__lt 1000000 -o script/primality_test.py.out.tabulate_best_u2eu__lt.1000000.txt
view  script/primality_test.py.out.tabulate_best_u2eu__lt.1000000.txt


view others/数学/整数分解/factorint.txt
    wget 'https://www.ams.org/journals/mcom/1987-48-177/S0025-5718-1987-0866102-2/S0025-5718-1987-0866102-2.pdf' -O 'Implementation of a New Primality Test(1987)(Cohen).pdf'
        强调实现步骤
    wget 'https://www.ams.org/journals/mcom/1984-42-165/S0025-5718-1984-0726006-X/S0025-5718-1984-0726006-X.pdf' -O 'Primality Testing and Jacobi Sums(1984)(Cohen).pdf'
        数据表格


primality_test(i) for i <- [2..=N<e(t)**2], find t, s.t. e(t)**2 > N
(1.1) Preparation of Tables, (a) Select an even positive integer t with e(t) > N**(1/2) (cf. (1.5)), where:
    e(t) = 2 * II q**(1+max_power_of_base_as_factor_of_(q,t)) {q<-all_primes | [t%(q-1)==0]}
    and tabulate the primes dividing e(t);
6983776800 == 2**5 * 3**3 * 5**2 *7*11*13*17*19
e(6983776800) == 7.471e3010

primitive_pkth_root_of_unity(p,k)
    单位根
    [primitive_pkth_root_of_unity(p,k)**(p**k) ==1]

for odd prime q, [e(t)%q==0]: # [t%(q-1)==0]:
    g[q] := primitive root of q
    tabulate: f(q,g[q],x) := log<g[q]%p>(1-g[q]**x)
    for prime p, [(q-1)%p==0]: #[t%p==0]
        k := max_power_of_base_as_factor_of_(p, q-1)
        if not p**k ==2:
            tabulate: j(p,q,g[q]) := sum primitive_pkth_root_of_unity(p,k)**(x+f(q,g[q],x)) {x=1..=q-2}




view ../../python3_src/nn_ns/math_nn/numbers/min_factor.py
view ../../python3_src/nn_ns/math_nn/numbers/prime_number.py
view ../../python3_src/nn_ns/math_nn/prime2.py



#]]]'''
__all__ = '''

    '''.split()
if 0:
    from nn_ns.math_nn.numbers.min_factor import min_factor
    assert min_factor.get_first(4) == [0,1,2,3]
    from nn_ns.math_nn.numbers.prime_number import prime_number as PRIMES
    assert PRIMES.get_first(4) == [2,3,5,7]
from nn_ns.math_nn.prime2 import primes_lt
assert primes_lt(10) == (2,3,5,7)
from seed.math.max_power_of_base_as_factor_of_ import max_power_of_base_as_factor_of_
from seed.math.II import II
from seed.helper.stable_repr import stable_repr
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer

def mk_uint2primes__p_divs__lt(N, /):
    u2ps = [set() for i in range(N)]
    for i in range(2, N):
        if u2ps[i]: continue
        # i is prime
        p = i
        for j in range(p, N, p):
            u2ps[j].add(p)
    return u2ps

def mk_uint2primes__p1_divs__lt(N, /, *, _ps_=None):
    ps = primes_lt(N) if _ps_ is None else _ps_
    u2ps = [[] for i in range(N)]
    for p in ps:
        p1 = p-1
        for j in range(p1, N, p1):
            u2ps[j].append(p)
    return u2ps

#print(mk_uint2primes__p1_divs__lt(100))
assert (mk_uint2primes__p1_divs__lt(100)) == (
[[], [2], [2, 3], [2], [2, 3, 5], [2], [2, 3, 7], [2], [2, 3, 5], [2]
, [2, 3, 11], [2], [2, 3, 5, 7, 13], [2], [2, 3], [2], [2, 3, 5, 17], [2], [2, 3, 7, 19], [2]
, [2, 3, 5, 11], [2], [2, 3, 23], [2], [2, 3, 5, 7, 13], [2], [2, 3], [2], [2, 3, 5, 29], [2]
, [2, 3, 7, 11, 31], [2], [2, 3, 5, 17], [2], [2, 3], [2], [2, 3, 5, 7, 13, 19, 37], [2], [2, 3], [2]
, [2, 3, 5, 11, 41], [2], [2, 3, 7, 43], [2], [2, 3, 5, 23], [2], [2, 3, 47], [2], [2, 3, 5, 7, 13, 17], [2]
, [2, 3, 11], [2], [2, 3, 5, 53], [2], [2, 3, 7, 19], [2], [2, 3, 5, 29], [2], [2, 3, 59], [2]
, [2, 3, 5, 7, 11, 13, 31, 61], [2], [2, 3], [2], [2, 3, 5, 17], [2], [2, 3, 7, 23, 67], [2], [2, 3, 5], [2]
, [2, 3, 11, 71], [2], [2, 3, 5, 7, 13, 19, 37, 73], [2], [2, 3], [2], [2, 3, 5], [2], [2, 3, 7, 79], [2]
, [2, 3, 5, 11, 17, 41], [2], [2, 3, 83], [2], [2, 3, 5, 7, 13, 29, 43], [2], [2, 3], [2], [2, 3, 5, 23, 89], [2]
, [2, 3, 7, 11, 19, 31], [2], [2, 3, 5, 47], [2], [2, 3], [2], [2, 3, 5, 7, 13, 17, 97], [2], [2, 3], [2]
])

def calc_eu__u_ps(u, ps, /):
    '->e(t)'
    eu = 2*II(p**(1+max_power_of_base_as_factor_of_(p, u)) for p in ps)
    return eu

def u2ps_to_u2eu(u2ps, /):
    u2eu = [calc_eu__u_ps(u,ps) for u, ps in enumerate(u2ps)]
    return u2eu
#print(u2ps_to_u2eu(mk_uint2primes__p1_divs__lt(100)))
assert (u2ps_to_u2eu(mk_uint2primes__p1_divs__lt(100))) == (
[2, 4, 24, 4, 240, 4, 504, 4, 480, 4, 264, 4, 65520, 4, 24, 4, 16320, 4, 28728, 4, 13200, 4, 552, 4, 131040, 4, 24, 4, 6960, 4, 171864, 4, 32640, 4, 24, 4, 138181680, 4, 24, 4, 1082400, 4, 151704, 4, 5520, 4, 1128, 4, 4455360, 4, 264, 4, 12720, 4, 86184, 4, 13920, 4, 1416, 4, 6814407600, 4, 24, 4, 65280, 4, 776664, 4, 240, 4, 18744, 4, 20174525280, 4, 24, 4, 240, 4, 39816, 4, 36801600, 4, 1992, 4, 571924080, 4, 24, 4, 982560, 4, 9796248, 4, 11280, 4, 24, 4, 864339840, 4, 24, 4])

def u2eu_to_best_u2eu(u2eu, /):
    'seq -> mapping'
    max_eu = -1
    d = {}
    for u, eu in enumerate(u2eu):
        if eu > max_eu:
            max_eu = eu
            d[u] = eu
    best_u2eu = d
    return best_u2eu

#print(stable_repr(u2eu_to_best_u2eu(u2ps_to_u2eu(mk_uint2primes__p1_divs__lt(100)))))
assert (u2eu_to_best_u2eu(u2ps_to_u2eu(mk_uint2primes__p1_divs__lt(100)))) == (
{0: 2, 1: 4, 2: 24, 4: 240, 6: 504, 12: 65520, 24: 131040, 30: 171864, 36: 138181680, 60: 6814407600, 72: 20174525280})

def tabulate_best_u2eu__lt(N, /):
    u2ps = mk_uint2primes__p1_divs__lt(N)
    u2eu = u2ps_to_u2eu(u2ps)
    best_u2eu = u2eu_to_best_u2eu(u2eu)
    best_u2ps = {u:u2ps[u] for u in best_u2eu}
    return (best_u2eu, best_u2ps)
    stable_repr(best_u2eu)
    stable_repr(best_u2ps)

#print(stable_repr(tabulate_best_u2eu__lt(100)))
assert (tabulate_best_u2eu__lt(100)) == (
({0: 2, 1: 4, 2: 24, 4: 240, 6: 504, 12: 65520, 24: 131040, 30: 171864, 36: 138181680, 60: 6814407600, 72: 20174525280}
,{0: [], 1: [2], 2: [2, 3], 4: [2, 3, 5], 6: [2, 3, 7], 12: [2, 3, 5, 7, 13], 24: [2, 3, 5, 7, 13], 30: [2, 3, 7, 11, 31], 36: [2, 3, 5, 7, 13, 19, 37], 60: [2, 3, 5, 7, 11, 13, 31, 61], 72: [2, 3, 5, 7, 13, 19, 37, 73]}
))



def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='show tabulate_best_u2eu__lt'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--tabulate_best_u2eu__lt', type=int, default=None
                        , help='upper bound')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    iencoding = args.iencoding
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'

    #may_ifname = args.input
    #with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:

    N = args.tabulate_best_u2eu__lt
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        (best_u2eu, best_u2ps) = tabulate_best_u2eu__lt(N)
        stable_repr_print__expand_top_layer(fout, (N, len(best_u2eu), best_u2eu, best_u2ps))
        print(file=fout)
if __name__ == "__main__":
    main()









