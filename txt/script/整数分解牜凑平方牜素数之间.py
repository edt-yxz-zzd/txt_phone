#__all__:goto
r'''[[[
e script/整数分解牜凑平方牜素数之间.py

script.整数分解牜凑平方牜素数之间
py -m nn_ns.app.debug_cmd   script.整数分解牜凑平方牜素数之间 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.整数分解牜凑平方牜素数之间:__doc__ -ht # -ff -df
#######

[[
整数分解:凑平方
大合数N，寻找c满足[c**2%N 足够小]
素数p,q, [p...<N**eN<q...]
  #??? [p%4==1][q%4==1]
[eN:=2*eH]
[eN:=1]
for c in range(2,max1_c):
    if is_perfect_square_(c):continue
    if Jacobi_symbol(p;c) == -1:continue
    if Jacobi_symbol(q;c) == -1:continue
    (ap,bp) = sqrts_mod_(p;c)
    (aq,bq) = sqrts_mod_(q;c)
    # [ap**2 == c+kp*p]
    # [aq**2 == c+kq*q]
    kp = (ap**2-c)///p
    kq = (aq**2-c)///q
    if not kp == kq:continue
    # [kp == kq]
    # [aq**2 -ap**2 == kp*(q-p)]
    # [@[ax:<-[ap..=aq]] -> [ap**2 <= ax**2 <= aq**2]]
    # [@[ax:<-[ap..=aq]] -> [kp == ap**2//N <= ax**2//N <= aq**2//N == kq == kp]]
    # [@[ax:<-[ap..=aq]] -> [ax**2//N == kp]]
    # [@[ax:<-[ap..=aq]] -> [ax**2 -kp*N <= aq**2 -kp*N == aq**2 -kp*q +kp*(q-N) == c+kp*(q-N)]]
    # [@[ax:<-[ap..=aq]] -> [ax**2 -kp*N >= ap**2 -kp*N == ap**2 -kp*p +kp*(p-N) == c-kp*(N-p)]]
    # [@[ax:<-[ap..=aq]] -> [c-kp*(N-p) <= ax**2 <= c+kp*(q-N)]]

]]
[[
[N >= 9][eN >= 1][len_primes >= 1][max1_c >= 3]:
    [M := N**eN]
    # [... < p1 < p0 < M < q==q0 < q1 < ...]
    ?ps,qs :=> [ps,qs::[prime]{len>=len_primes}][sorted(ps) == ps[::-1]][sorted(qs) == qs][ps[0] < M < qs[0]]
    [c:<-[2..<max1_c]][not$is_square_(c)][ps4c:=[p | [p:<-ps][Jacobi_symbol(p;c) == 1]]][qs4c:=[q | [q:<-qs][Jacobi_symbol(q;c) == 1]]][len(ps4c) > 0][len(qs4c) > 0]:
        [p:<-ps4c][q:<-qs4c][Jacobi_symbol(p;c) == 1][Jacobi_symbol(q;c) == 1][rp:<-[ceil_sqrt(p)..=p//2]][rq:<-[ceil_sqrt(q)..=q//2]][rp**2%p == c][rq**2%q == c][(rp**2-c)//p == (rq**2-c)//q]:
            [k:=(rp**2-c)//p]
            [rp**2 == c +k*p]
            [rq**2 == c +k*q]
            [rm:<-[rp..=rq]]:
                [rm**2 -k*M <= rq**2 -k*q +k*(q-M) == c +k*(q-M)]
                [rm**2 -k*M >= rp**2 -k*p +k*(p-M) == c -k*(M-p)]
                [-k*(M-p) <= rm**2 -c -k*M <= k*(q-M)]
                失败分析二:
                    [k ~ O(M)]
                    [k*(q-M) 通常非常大，范围大]
            失败分析一:
            !! [rp**2 == c +k*p]
            !! [rq**2 == c +k*q]
            [rq**2 -rp**2 == k*(q-p)]
                #...可能比较罕见
]]
[[

[N >= 9][eN,eNN >= 1][NH:=(2*N)**eN][NN:=NH**2][MH:=NH**eNN][M:=(NN**eNN-1)]:
    [c::uint%M][p::prime][M%p==0][ep:=gde_(p;M)][xp::uint%p**ep][xp**2 =[%p**ep]= c]:
        [(xp**2 -c)%p**ep == 0]
    [c,F::uint%M][M%F==0][R:=M///F][gcd(F,R) == 1][xF::uint%F][xF**2 =[%F]= c]:
        [(xF**2 -c)%F == 0]

    ?????????how?????????
    无法得到xM
    [c,xM::uint%M][xM**2 =[%M]= c]:
        [(xM**2 -c)%M == 0]
        [(xM**2 -c)%(NN**eNN-1) == 0]
        [(xM**2 -c)%(NH**(2**eNN)-1) == 0]
        [(xM**2 -c)%(MH**2-1) == 0]

        [(xM**2 -c)%(MH-1) == 0]
        [(xM**2 -c)%(MH+1) == 0]

        !! [MH%2 == 0]
        [gcd((MH-1),(MH+1)) == gcd((MH-1),2) == 1]
        [k:=(xM**2 -c)///M]
        [(xM**2 -c) == k*(MH-1)*(MH+1)]
        [kmm:=k*(MH+1)]
        [kpp:=k*(MH-1)]
        [(-kmm+kpp)///2 == -k]
        [(kmm+kpp)///2 == k*MH]

        [(xM**2 -c) == kmm*(MH-1)]
        [(xM**2 -c) == kpp*(MH+1)]

        [(xM**2 -c) == (-kmm+kpp)/2 +(kmm+kpp)/2*MH]
        !! [MH%2 == 0]
        [(-kmm+kpp)/2 %1.0 == 0]
        [(-kmm+kpp)%2 == 0]
        [(kmm+kpp)%2 == 0]
        [(xM**2 -c) == (-kmm+kpp)///2 +(kmm+kpp)///2*MH]

        !! [MH%N == 0]
        [(xM**2 -c) =[%N]= (-kmm+kpp)///2]
        [xM**2 =[%N]= c +(-kmm+kpp)///2]
        [xM**2 =[%N]= c -k]
            k很大,感觉无用...



[N >= 9][Q::prime][g:<-primitive_roots_mod_(Q)]:
    [M:=N*Q]
    [c::uint%N][Jacobi_symbol(Q;c) == 1][rdN::uint%N][d:=rdN**2%N][Jacobi_symbol(Q;d) == 1][c,d < Q]:
        [rdQ:=list_sqrts_mod_prime_(Q;d)[0]]
        [d==rdN**2%N]
        [d==rdQ**2%Q]
        ?rdM :=> [d==rdM**2%M]
        [t := c*d**-1%M]
        [c == d*t%M]
        [c == d*t%Q]
        [rtQ:=list_sqrts_mod_prime_(Q;t)[0]]
        [c == (rdQ*rtQ)**2%Q]
        [t%N == 1]:
            [rtN := 1]
            [rtM%M :=CRT{%M}(rtN%N, rtQ%Q)]
            [c == (rdM*rtM)**2%M]
            [c == (rdM*rtM)**2%N]
            [c == (rdM*rtN)**2%N]
            [c == (rdM*1)**2%N]
            [c == rdM**2%N]
            [c == rdM**2%M %N]
            [c == d %N]
            [c == d]
            无用...


]]



'#'; __doc__ = r'#'
next_probable_prime ='2**60+567'
1152921504606847601
next_probable_prime ='2**70+56789'
1180591620717411360257
>>> N = 1152921504606847601*1180591620717411360257



py_adhoc_call   script.整数分解牜凑平方牜素数之间   ,_try1_ ='1152921504606847601*1180591620717411360257' =1 =1 ='2**16' | more
    <NONE>
    失败！


from script.整数分解牜凑平方牜素数之间 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.sqrts_mod_ import list_sqrts_mod_prime_, find_arbitrary_one_square_nonresidual_mod_odd_prime_
    #def list_sqrts_mod_prime_(p, xx, /, *, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
    from seed.math.prime_gens import iter_probable_primes__ge_, reversed_iter_probable_primes__lt_, iter_primes__le_pow2_81__ge_, reversed_iter_primes__le_pow2_81__lt_
    from seed.iters.apply_may_args4islice_ import list_islice_
    from seed.math.perfect_kth_root import is_square_
    from seed.math.Jacobi_symbol import Jacobi_symbol
    from seed.math.perfect_div import perfect_div
    from seed.tiny_.check import check_type_is, check_int_ge
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def _try1_(N, eN, len_primes, cs_or_max1_c):
    check_int_ge(9, N)
    check_int_ge(1, eN)
    check_int_ge(1, len_primes)
    if type(cs_or_max1_c) is int:
        max1_c = cs_or_max1_c
        check_int_ge(3, max1_c)
        # [N >= 9][eN >= 1][max1_c >= 3][len_primes >= 1]
        cs = range(2, max1_c)
    else:
        cs = cs_or_max1_c
        iter(cs)
    cs
    M = N**eN
    ps = list_islice_(len_primes, reversed_iter_probable_primes__lt_(M))
    #777;ps.reverse()
    qs = list_islice_(len_primes, iter_probable_primes__ge_(1+M))
    if not ps:raise 000
    if ps[-1] == 2:
        ps.pop()
        # all ps, qs are old prime
        if not ps:raise 000

    p2x = {p:find_arbitrary_one_square_nonresidual_mod_odd_prime_(p) for p in ps}
        # !! old prime
    q2x = {q:find_arbitrary_one_square_nonresidual_mod_odd_prime_(q) for q in qs}
    for c in cs:
        if is_square_(c):continue
        ps4c = [p for p in ps if Jacobi_symbol(p,c) == 1]
        if not ps4c:continue
        qs4c = [q for q in qs if Jacobi_symbol(q,c) == 1]
        if not qs4c:continue

        rs4p = [list_sqrts_mod_prime_(p, c, may_arbitrary_one_square_nonresidual_mod_odd_prime=p2x[p])[0] for p in ps4c]
        rs4q = [list_sqrts_mod_prime_(q, c, may_arbitrary_one_square_nonresidual_mod_odd_prime=q2x[q])[0] for q in qs4c]
        ks4p = [perfect_div(r**2-c, p) for p, r in zip(ps4c, rs4p)]
        ks4q = [perfect_div(r**2-c, q) for q, r in zip(qs4c, rs4q)]
        #########
        common_ks = set(ks4p) & set(ks4q)
        if not common_ks:continue
        k2jps_jqs = {k:([], []) for k in common_ks}
        for b, (ds4c, ks4d) in enumerate([(ps4c, ks4p), (qs4c, ks4q)]):
            for j4d, (d, k) in enumerate(zip(ds4c, ks4d)):
                if k in common_ks:
                    k2jps_jqs[k][b].append(j4d)

        #########
        min_r = M
        max_r = 0
        for k, (jps6k, jqs6k) in sorted(k2jps_jqs.items()):
            _min_r = rs4p[jps6k[-1]]
            _max_r = rs4q[jqs6k[-1]]
            assert _min_r <= _max_r
            min_r = min(min_r, _min_r)
            max_r = max(max_r, _max_r)
        assert min_r <= max_r
        for rm in range(min_r, 1+max_r):
            _c = rm**2%M
            yield (c, _c, rm)




__all__
from script.整数分解牜凑平方牜素数之间 import *
