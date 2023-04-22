#__all__:goto
r'''[[[
e script/pairwise_parallel_schedule.py
py -m nn_ns.app.debug_cmd    script.pairwise_parallel_schedule
py -m nn_ns.app.adhoc_argparser__main__call8module   script.pairwise_parallel_schedule  ,pairwise_parallel_schedule__pow_2_  =4
py -m nn_ns.app.adhoc_argparser__main__call8module   script.pairwise_parallel_schedule  ,pairwise_parallel_schedule  =6


[[
pairwise parallel schedule
两两比赛，并行最短解是？X(n),n>=2
  [X(n) >= n-1]
  [X(n) >= X(n-1)]
  [X(m+n) <= max{X(m),X(n)}+max{m,n} == X(max{m,n})+max{m,n}]
  [[m>=n] -> [X(m+n) <= X(m)+m]]
  [X(2*n) <= X(n)+n]
  [X(2*n+1) <= X(n+1)+n+1]
  [X(n) >= ceil(C(n;2)/(n//2)) >= n-1]
    [X(2*n) >= (2*n-1)]
    [X(2*n+1) >= (2*n+1)]
      ...每轮必有一队轮空...
      ???==>>[X(2*n+2) == X(2*n+1)]
  [2**n-1 <= X(2**n) <= X(2**(n-1))+2**(n-1) <= X(2)+2+...+2**(n-1) == 2**n-1]
  [X(2**n) == 2**n-1]
  [(2**n+1) <= X(2**n+1) <= X(2**(n-1)+1)+2**(n-1)+1 <= X(2+1)+2+1+...+2**(n-1)+1 == 3+(n-1)+2**n-2 == 2**n+n]
  [(2**n+1) <= X(2**n+1) <= 2**n+n]
  [5 <= X(5) <= 6]
  [X(m*n) <= X(n)+X(m)*n]
    [m==2]:
      [X(2*n) <= X(n)+X(2)*n == X(n)+n]
    [n==2]:
      [X(m*2) <= X(2)+X(m)*2 == 1+X(m)*2 >= X(m)+m]
    [m==2**i]:
      [X(2**i*n) <= X(n)+X(2**i)*n == X(n)+(2**i-1)*n]
    [n==2**i]:
      [X(m*2**i) <= X(2**i)+X(m)*2**i == (2**i-1)+X(m)*2**i == X(m)+(1+X(m))*(2**i-1) >= X(m)+(2**i-1)*m]
  [X(2**i*n) <= X(n)+(2**i-1)*n]
  ===
  n-C(n;2)-X(n)
  2-1-1
  3-3-3
  4-6-3
    ab,cd;ac,bd;ad,bc
  5-10-5
  6-15-5
    ab,cd,ef
    ac,de,bf
    ad,be,cf
    ae,bc,df
    af,ce,bd
    [X(5) == X(6) == 5]


bigraph (bipartite graph) 二部图
]]




py -m nn_ns.app.adhoc_argparser__main__call8module   script.pairwise_parallel_schedule  ,pairwise_parallel_schedule__pow_2_  =3
((0, 1), (2, 3), (4, 5), (6, 7))
((0, 2), (1, 3), (4, 6), (5, 7))
((0, 3), (1, 2), (4, 7), (5, 6))
((0, 4), (1, 5), (2, 6), (3, 7))
((0, 5), (1, 6), (2, 7), (3, 4))
((0, 6), (1, 7), (2, 4), (3, 5))
((0, 7), (1, 4), (2, 5), (3, 6))


.../txt_phone/txt $ py -m nn_ns.app.adhoc_argparser__main__call8module   script.pairwise_parallel_schedule  ,pairwise_parallel_schedule  =8
((0, 1), (2, 3), (4, 5), (6, 7))
((0, 2), (1, 3), (4, 6), (5, 7))
((0, 3), (1, 2), (4, 7), (5, 6))
((0, 4), (1, 5), (2, 6), (3, 7))
((0, 5), (1, 6), (2, 7), (3, 4))
((0, 6), (1, 7), (2, 4), (3, 5))
((0, 7), (1, 4), (2, 5), (3, 6))
.../txt_phone/txt $ py -m nn_ns.app.adhoc_argparser__main__call8module   script.pairwise_parallel_schedule  ,pairwise_parallel_schedule  =7
((0, 1), (2, 3), (4, 5))
((0, 2), (1, 3), (4, 6))
((0, 3), (1, 2), (5, 6))
((0, 4), (1, 5), (2, 6))
((0, 5), (1, 6), (3, 4))
((0, 6), (2, 4), (3, 5))
((1, 4), (2, 5), (3, 6))
.../txt_phone/txt $ py -m nn_ns.app.adhoc_argparser__main__call8module   script.pairwise_parallel_schedule  ,pairwise_parallel_schedule  =6
((0, 2), (1, 3), (4, 5))
((0, 4), (1, 5), (2, 3))
((0, 5), (3, 4), (1, 2))
((2, 4), (3, 5), (0, 1))
((1, 4), (2, 5), (0, 3))
.../txt_phone/txt $ py -m nn_ns.app.adhoc_argparser__main__call8module   script.pairwise_parallel_schedule  ,pairwise_parallel_schedule  =5
((0, 2), (1, 3))
((0, 4), (2, 3))
((3, 4), (1, 2))
((2, 4), (0, 1))
((1, 4), (0, 3))






.../txt_phone/txt $ py -m nn_ns.app.adhoc_argparser__main__call8module   script.pairwise_parallel_schedule  ,pairwise_parallel_schedule  =9
assert sum(len_dups) == len(s)+2, (m,k,1<<k,i, may_new_pairs, dups, len_dups, len(s))
AssertionError: (9, 4, 16, 14, [None, (12, 13), (12, 13), (10, 11), (9, 10), (8, 9), (8, 11), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1), (0, 7)], [{(0, 1), (10, 11), (12, 13), (2, 3), (6, 7), (4, 5), (8, 9)}, {(12, 13)}, {(9, 10), (1, 2), (12, 13), (5, 6), (8, 11)}], [7, 1, 5], 13)

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from seed.math.floor_ceil import ceil_log2
from seed.func_tools.fmapT.checkT__tiny import (dot
,checkT__pattern_tuple
,checkT__pattern_list
,checkT__AND
,checkT__type_is
,checkT__type_is__AND
,checkT__lt
,checkT__ge_lt
,checkT__len_eq
,check_int
,check_uint
,check_tuple
,check_list
,checkT__tuple
,checkT__list
)


def check_std_schedule_(n, std_schedule, /):
    check_uint(n)
    assert n >= 1
    check_uint_mod = checkT__AND(check_uint, checkT__lt(n))
    check_uint_mod_pair = checkT__type_is__AND(tuple, checkT__len_eq(2), checkT__pattern_list(check_uint_mod))
    check_uint_mod_pairs = checkT__type_is__AND(tuple, checkT__pattern_list(check_uint_mod_pair))
    check_uint_mod_pairss = checkT__type_is__AND(tuple, checkT__pattern_list(check_uint_mod_pairs))
    check_uint_mod_pairss(std_schedule)
    ls = [0]*n
    for row in std_schedule:
        for i,j in row:
            ls[i] += 1
            ls[j] += 1
            if not ls[i]==1==ls[j]: raise ValueError
        for i,j in row:
            ls[i] -= 1
            ls[j] -= 1
    ls = [[0]*k for k in range(n)]
    for row in std_schedule:
        for i,j in row:
            if not 0 <= i < j < n: raise ValueError
            ls[j][i] += 1
            if not ls[j][i]==1: raise ValueError
    if not all(map(all, ls)): raise ValueError

def std2nonstd(nonstd_ls, std_schedule, /):
    return tuple(tuple((nonstd_ls[i], nonstd_ls[j]) for i,j in row) for row in std_schedule)
def parallel_merge(lhs_schedule, rhs_schedule, /):
    assert len(lhs_schedule) == len(rhs_schedule)
    return tuple(xs+ys for xs, ys in zip(lhs_schedule, rhs_schedule))
def bipartite_pairwise_parallel_schedule(xs, ys, /):
    assert 1 <= len(xs) <= len(ys)
    m = len(xs)
    n = len(ys)
    assert len(range(-n,0)) == n
    return tuple(tuple((xs[i], ys[j+i]) for i in range(m)) for j in range(-n, 0))



def pairwise_parallel_schedule__pow_2_(k, /):
    '[X(2**k) == 2**k-1]'
    assert k >= 0
    i = 0
    std_schedule = () #k==i==0
    for i in range(k):
        check_std_schedule_(1<<i, std_schedule)
        nonstd_ls = range(1<<i,1<<(i+1))
        nonstd_schedule = std2nonstd(nonstd_ls, std_schedule)
        inits = parallel_merge(std_schedule, nonstd_schedule)
        std_ls = range(1<<i)
        tails = bipartite_pairwise_parallel_schedule(std_ls, nonstd_ls)
        std_schedule = inits + tails
    check_std_schedule_(1<<k, std_schedule)
    return std_schedule
def pairwise_parallel_schedule(n, /):
    assert n >= 0
    m = max(1,n)
    k = ceil_log2(m)
    assert (1<<k)//2 < m <= (1<<k)
    i = (1<<k)
    std_schedule = pairwise_parallel_schedule__pow_2_(k)
    if 0:
        print(f'm = {m}')
        print(f'k = {k}')
        print(f'i = {i}')
    for i in range(i-2, m-1, -2):
        if 0:
            print(f'i = {i}')
        pairss = []
        may_new_pairs = []
        for row in std_schedule:
            pairs = []
            new_pair = []
            for a,b in row:
                assert 0 <= a < b
                if a==i:
                    assert b==i+1
                    new_pair = None
                elif not b < i:
                    new_pair.append(a)
                else:
                    assert 0 <= a < b < i
                    pairs.append((a,b))
            if not new_pair is None:
                new_pair = tuple(sorted(new_pair))
                pairs.append(new_pair)
            assert len(pairs)==len(row)-1
            pairs = (*pairs,)
            pairss.append(pairs)
            may_new_pairs.append(new_pair)
        if 0:
            print(may_new_pairs)
            print(pairss)
            raise ...
        if 1:
            may_new_pair2idc = {mp:[] for mp in may_new_pairs}
            for idx, may_new_pair in enumerate(may_new_pairs):
                may_new_pair2idc[may_new_pair].append(idx)
            [((a,b), [iA,iB])] = [(mp,idc) for mp, idc in may_new_pair2idc.items() if len(idc)==2]
            if 0:
                #bug:
                del pairss[iB]
                del pairss[iA]
            ab = (a,b)
            idc = [idx for idx, pairs in enumerate(pairss) if ab in pairs]
            assert len(idc)==3
            s = {*may_new_pair2idc}
            s.remove(None)
            dups = [s&{*pairss[idx]} for idx in idc]
            len_dups = [*map(len, dups)]
            if 0:
                print(f'i = {i}')
                print(may_new_pairs)
                print(dups)
                print(len_dups)
            assert sum(len_dups) == len(s)+2, (m,k,1<<k,i, may_new_pairs, dups, len_dups, len(s))
            del idc[len_dups.index(1)]
            [iA,iB] = idc
            del pairss[iB]
            del pairss[iA]
        if 0:
            print(may_new_pairs)
            print(pairss)
            raise ...
        pairss = (*pairss,)
        std_schedule = pairss
        check_std_schedule_(i, std_schedule)

    assert m <= i <= m+1
    assert m+(m&1) == i
    if not i == m:
        i -= 1
        assert i==m
        std_schedule = tuple(tuple(pair for pair in row if not pair[1]==i) for row in std_schedule)
        check_std_schedule_(i, std_schedule)
    check_std_schedule_(m, std_schedule)
    check_std_schedule_(n, std_schedule)
    return std_schedule




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL


