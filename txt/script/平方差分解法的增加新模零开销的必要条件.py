
r'''
e script/平方差分解法的增加新模零开销的必要条件.py
[M%2=!=0][len(all_ok_x_mod N M)==1]:
  [{0} == {(u+inv_u*N)*inv_2%M | [@u.[gcd(u,M)==1]]}] #平方差分解法的增加新模零开销的必要条件囗过时

平方差分解法的增加新模大数零开销的充要条件 = [M=3][N%M==2]
    #平方差分解法的增加新模零开销的必要条件
!![y**2-x**2=[%M]=(-N)]
平方差分解法的增加新模小数零开销的充要条件 = [M=3][(-N)%M==2]

求 min(len(all_ok_x_mod N M)/M)

py script/平方差分解法的增加新模零开销的必要条件.py -L 2 -M 100
py script/平方差分解法的增加新模零开销的必要条件.py -L 2 -M 100 -o ~/my_tmp/out4py/平方差分解法的增加新模零开销的必要条件.py.out.2-100.txt
view /sdcard/0my_files/tmp/out4py/平方差分解法的增加新模零开销的必要条件.py.out.2-100.txt

py script/平方差分解法的增加新模零开销的必要条件.py -L 2 -M 1000 -o ~/my_tmp/out4py/平方差分解法的增加新模零开销的必要条件.py.out.2-1000.txt
view /sdcard/0my_files/tmp/out4py/平方差分解法的增加新模零开销的必要条件.py.out.2-1000.txt
[(0.05, 720), (0.066, 900), (0.081, 880), (0.083, 144), (0.083, 288), (0.083, 432), (0.083, 576), (0.083, 864), (0.085, 560), (0.086, 828), (0.087, 684), (0.087, 912), (0.088, 612), (0.088, 816), (0.089, 468), (0.089, 624), (0.089, 936), (0.09, 396), (0.09, 528), (0.09, 792), (0.095, 252), (0.095, 336), (0.095, 504), (0.095, 672), (0.095, 756), (0.1, 180), (0.1, 240), (0.1, 360), (0.1, 400), (0.1, 480), (0.1, 540), (0.1, 800), (0.1, 960), (0.102, 819), (0.103, 693), (0.103, 924), (0.105, 855), (0.105, 765), (0.107, 784), (0.107, 585), (0.107, 780), (0.109, 495), (0.109, 660), (0.109, 990), (0.114, 315), (0.114, 420), (0.114, 630), (0.114, 700), (0.114, 840), (0.114, 945), (0.127, 976), (0.127, ...) ...]
(0.05, 720)
    2|3|5
(0.083, 144)
    2|3
    !!! 2**i * 3**j: limit worst_efficiency -> ??
(0.1, 180)
    2|3|5


py script/平方差分解法的增加新模零开销的必要条件.py -L 2 -M 10000 -o ~/my_tmp/out4py/平方差分解法的增加新模零开销的必要条件.py.out.2-10000.txt
#'''



from math import gcd, floor
from nn_ns.math_nn.prime2 import sorted_primes_endby_ge
from nn_ns.math_nn.integer.mod import invmod
from itertools import count, combinations
from seed.mapping_tools.dict_op import inv__k2v_to_v2ks#, inv__k2v_to_v2k, inv__k2vs_to_v2k, inv__k2vs_to_v2ks

def _search_N_per_M(UPPER_BOUND_OF_M, /, *, fout):
    primes, i = sorted_primes_endby_ge(UPPER_BOUND_OF_M)
    #print(primes)
    it = iter(primes)
    next(it)
    #for M in it:
    for M in primes[1:i]:
        inv_ = [None]*M
        inv_[1] = 1
        inv_[M-1] = M-1
        for i in range(2, M-1):
            if inv_[i] is None:
                j = invmod(i, M)
                inv_[i] = j
                inv_[j] = i
        for i in range(1, M):
            assert i*inv_[i]%M == 1
        inv_2 = inv_[2]
        _Ns = [N for N in range(M) if all((u+inv_u*N)*inv_2%M==0 for u, inv_u in enumerate(inv_) if u)] #if u and gcd(u,M)==1 #but since M is prime...
        if not _Ns: continue
        print(f'候选:{_Ns}%{M}', file=fout)

        all_quadratic_residues = {pow(u,2,M) for u in range(M)}
        sorted_all_quadratic_residues = sorted(all_quadratic_residues)
        Ns_ok = []
        for N in _Ns:
            xx_ls = []
            for xx in sorted_all_quadratic_residues:
                yy = (xx-N)%M
                if yy in all_quadratic_residues:
                    xx_ls.append(xx)
            if not xx_ls: raise logic-err
            if len(xx_ls) >=2:
                print(f'无效候选:{N}%{M}:{xx_ls}', file=fout)
            else:
                Ns_ok.append(N)


        print(f'有效:{Ns_ok}%{M}', file=fout)


#_search_N_per_M(1000, fout=None)

def _search_N_for_M_eq_3_power(UPPER_BOUND_OF_M, /, *, fout):
    M = 1
    for e in count(1):
        M *= 3
        if M > UPPER_BOUND_OF_M: break
        inv_ = [None]*M
        for i in range(M):
            if i%3 and inv_[i] is None:
                j = invmod(i, M)
                inv_[i] = j
                inv_[j] = i
        for i in range(M):
            if i%3:
                assert i*inv_[i]%M == 1
        _Ns = range(2, M, 3)
        _Ns = [N for N in range(2, M, 3) if all((u**2+N)%M==0 for u in range(M) if u%3)]
        if not _Ns: continue
        print(f'候选:{_Ns}%{M}', file=fout)

        all_quadratic_residues = {pow(u,2,M) for u in range(M)}
        sorted_all_quadratic_residues = sorted(all_quadratic_residues)
        Ns_ok = []
        for N in _Ns:
            xx_ls = []
            for xx in sorted_all_quadratic_residues:
                yy = (xx-N)%M
                if yy in all_quadratic_residues:
                    xx_ls.append(xx)
            if not xx_ls: raise logic-err
            if len(xx_ls) >=2:
                print(f'无效候选:{N}%{M}:{xx_ls}', file=fout)
            else:
                Ns_ok.append(N)


        print(f'有效:{Ns_ok}%{M}', file=fout)

def _tabu_M_N_efficiency__per_M(LOWER_BOUND_OF_M, UPPER_BOUND_OF_M, /, *, fout):
    Ms_ok = []
    M__most_inefficient_N__sz__triples = []
    #bug:for M in range(3, UPPER_BOUND_OF_M+1, 2):
    #   之前『零开销』==>>[M%2=!=0]
    #   此处 不要求 某个N『零开销』，M可为 偶数
    for M in range(max(2, LOWER_BOUND_OF_M), UPPER_BOUND_OF_M+1):
        N2xs_ok = _search_all_ok_x_mod__per_N(M)
        M_N_efficiency__triples = _tabu_M_N_efficiency(N2xs_ok)
        most_inefficient_N = max(range(1,M), key=lambda N,/: -1 if not gcd(N,M) == 1 else len(N2xs_ok[N]))
            #目标是 分解N
            #   这里假设 [gcd(N,M)==1]
            #   所以 无视 N2xs_ok[0]
            #   注意:len(N2xs_ok[0])==M
        M__most_inefficient_N__sz__triples.append((M, most_inefficient_N, len(N2xs_ok[most_inefficient_N])))
            #？奇素数 在 [N=1]时 效率最低？sz = (M+1)//2 = M//2+1
            #x**2-y**2=[%M]=1
            #(x-y)(x+y)=[%M]=1
            #x+y=u
            #x-y=inv[%M] u
            #x==(u+inv_u)*inv_2
        M_ok = False
        for t in M_N_efficiency__triples:
            _M, N, efficiency = t
            xs_ok = N2xs_ok[N]
            if len(xs_ok)*9 < M:
                M_ok = True
                print(t, sorted(xs_ok), file=fout)
        if M_ok:
            Ms_ok.append(M)
    print(Ms_ok, file=fout)
    print(M__most_inefficient_N__sz__triples, file=fout)
    worst_efficiency__M__pairs = [(sz/M, M) for M, _, sz in M__most_inefficient_N__sz__triples]
    worst_efficiency__M__pairs.sort()
    worst_efficiency__M__pairs = [(truncate(3, worst_efficiency), M) for worst_efficiency, M in worst_efficiency__M__pairs]
    print(worst_efficiency__M__pairs, file=fout)

        #_tabu_M_N_efficiency__per_M(2, 100):
        ###if len(xs_ok)*9 < M:
        # Ms_ok := [24, 40, 45, 48, 56, 60, 63, 72, 75, 80, 81, 84, 90, 96, 99]
        # M__most_inefficient_N__sz__triples := [(2, 1, 2), (3, 1, 2), (4, 1, 2), (5, 1, 3), (6, 1, 4), (7, 1, 4), (8, 1, 4), (9, 2, 3), (10, 1, 6), (11, 1, 6), (12, 1, 4), (13, 1, 7), (14, 1, 8), (15, 1, 6), (16, 1, 4), (17, 1, 9), (18, 5, 6), (19, 1, 10), (20, 1, 6), (21, 1, 8), (22, 1, 12), (23, 1, 12), (24, 1, 8), (25, 2, 10), (26, 1, 14), (27, 2, 9), (28, 1, 8), (29, 1, 15), (30, 1, 12), (31, 1, 16), (32, 1, 8), (33, 1, 12), (34, 1, 18), (35, 1, 12), (36, 5, 6), (37, 1, 19), (38, 1, 20), (39, 1, 14), (40, 1, 12), (41, 1, 21), (42, 1, 16), (43, 1, 22), (44, 1, 12), (45, 11, 9), (46, 1, 24), (47, 1, 24), (48, 1, 8), (49, 3, 21), (50, 3, 20), (51, 1, 18), (52, 1, 14), (53, 1, 27), (54, 5, 18), (55, 1, 18), (56, 1, 16), (57, 1, 20), (58, 1, 30), (59, 1, 30), (60, 1, 12), (61, 1, 31), (62, 1, 32), (63, 2, 12), (64, 3, 16), (65, 1, 21), (66, 1, 24), (67, 1, 34), (68, 1, 18), (69, 1, 24), (70, 1, 24), (71, 1, 36), (72, 5, 12), (73, 1, 37), (74, 1, 38), (75, 7, 20), (76, 1, 20), (77, 1, 24), (78, 1, 28), (79, 1, 40), (80, 1, 12), (81, 2, 27), (82, 1, 42), (83, 1, 42), (84, 1, 16), (85, 1, 27), (86, 1, 44), (87, 1, 30), (88, 1, 24), (89, 1, 45), (90, 11, 18), (91, 1, 28), (92, 1, 24), (93, 1, 32), (94, 1, 48), (95, 1, 30), (96, 1, 16), (97, 1, 49), (98, 3, 42), (99, 5, 18), (100, 3, 20)]
        #worst_efficiency__M__pairs := [(0.15, 80), (0.166, 36), (0.166, 48), (0.166, 72), (0.166, 96), (0.181, 99), (0.19, 63), (0.19, 84), (0.2, 45), (0.2, 60), (0.2, 90), (0.2, 100), (0.25, 16), (0.25, 32), (0.25, 64), (0.26, 92), (0.263, 76), (0.264, 68), (0.266, 75), (0.269, 52), (0.272, 44), (0.272, 88), (0.285, 28), (0.285, 56), (0.3, 20), (0.3, 40), (0.307, 91), (0.311, 77), (0.315, 95), (0.317, 85), (0.323, 65), (0.327, 55), (0.333, 9), (0.333, 12), (0.333, 18), (0.333, 24), (0.333, 27), (0.333, 54), (0.333, 81), (0.342, 35), (0.342, 70), (0.344, 93), (0.344, 87), (0.347, 69), (0.35, 57), (0.352, 51), (0.358, 39), (0.358, 78), (0.363, 33), (0.363, 66), (0.38, 21), (0.38, 42), (0.4, 15), (0.4, 25), (0.4, 30), (0.4, 50), (0.428, 49), (0.428, 98), (0.5, 4), (0.5, 8), (0.505, 97), (0.505, 89), (0.506, 83), (0.506, 79), (0.506, 73), (0.507, 71), (0.507, 67), (0.508, 61), (0.508, 59), (0.509, 53), (0.51, 47), (0.51, 94), (0.511, 43), (0.511, 86), (0.512, 41), (0.512, 82), (0.513, 37), (0.513, 74), (0.516, 31), (0.516, 62), (0.517, 29), (0.517, 58), (0.521, 23), (0.521, 46), (0.526, 19), (0.526, 38), (0.529, 17), (0.529, 34), (0.538, 13), (0.538, 26), (0.545, 11), (0.545, 22), (0.571, 7), (0.571, 14), (0.6, 5), (0.6, 10), (0.666, 3), (0.666, 6), (1.0, 2)]
        #


def _tabu_M_N_efficiency(N2xs_ok, /):
    M = len(N2xs_ok)
    M_N_efficiency__triples = [(M,N, sz/M) for N, sz in enumerate(map(len, N2xs_ok)) if gcd(N,M)==1]
    return M_N_efficiency__triples

def max_height_of_2_power_(M, /):
    assert M >= 1
    e = (M^(M-1)).bit_length()-1
    assert M%2**e == 0
    assert (M//2**e)%2 == 1
    Mo = M>>e
    assert Mo & 1 == 1
    assert (Mo << e) == M
    return e
assert max_height_of_2_power_(1)==0
def truncate(d, x, /):
    return floor(x*10**d)/10**d

def _search_all_ok_x_mod__per_N(M, /):
    N2xs_ok = [set() for N in range(M)]
    for x, y in combinations(range(M), 2):
        assert x < y
        xx = pow(x, 2, M)
        yy = pow(y, 2, M)
        N = (xx-yy)%M
        N2xs_ok[N].add(x)
        #if x: N2xs_ok[N].add(M-x)
        neg_N = -N if N==0 else M-N
        N2xs_ok[neg_N].add(y)
    N2xs_ok[0].add(0)
    if M%2==0:
        N2xs_ok[0].add(M//2)

    if M%2:
        assert all(N2xs_ok)
    else:
        e = max_height_of_2_power_(M)
        #if e%2:
        if e < 2:
            assert all(N2xs_ok), (e,M,N2xs_ok)
        else:
            assert all(xs_ok if N == 0 else (not xs_ok) == bool(max_height_of_2_power_(N)==1) for N, xs_ok in enumerate(N2xs_ok)), (e,M,N2xs_ok)
    assert len(N2xs_ok[0]) == M, (M,N2xs_ok[0])
    return N2xs_ok

    #old:
    quadratic_residue2sqrts = inv__k2v_to_v2ks({u:pow(u,2,M) for u in range(M)})
    N2xs_ok = [_search_all_ok_x_mod(N, M, quadratic_residue2sqrts) for N in range(M)]
    return N2xs_ok
def _search_all_ok_x_mod(N, M, quadratic_residue2sqrts, /):
    xs_ok = {*[]}
    for xx, _xs in quadratic_residue2sqrts.items():
        yy = (xx-N)%M
        if yy in quadratic_residue2sqrts:
            xs_ok |= _xs
    if not xs_ok: raise logic-err
    return xs_ok


def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='平方差分解法的增加新模零开销的必要条件'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-L', '--LOWER_BOUND_OF_M', type=int, required=True
                        , help='LOWER_BOUND_OF_M')
    parser.add_argument('-M', '--UPPER_BOUND_OF_M', type=int, required=True
                        , help='UPPER_BOUND_OF_M')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'

    UPPER_BOUND_OF_M = args.UPPER_BOUND_OF_M
    LOWER_BOUND_OF_M = args.LOWER_BOUND_OF_M

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        #_search_N_per_M(UPPER_BOUND_OF_M, fout=fout)
        #_search_N_for_M_eq_3_power(UPPER_BOUND_OF_M, fout=fout)
        _tabu_M_N_efficiency__per_M(LOWER_BOUND_OF_M, UPPER_BOUND_OF_M, fout=fout)
if __name__ == "__main__":
    main()


