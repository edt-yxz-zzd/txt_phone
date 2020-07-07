

r'''
see CombinatorSKIBC


    size_L :: LambdaTerm -> Nat
    -- size_L t = numSub_L t + sum (numFVs_L t)
    size_L x = 2
    size_L (t1 t2) = 1 + size FV(t1 t2) + size_L t1 + size_L t2
    size_L (\x. t) = 1 + size FV(\x. t) + size_L t

    -- to find out min numSub_L, max size_L when size FV is 0
    size_L3 t = (numSub_L t, size FV(t), size_L t)
    size_L3 x = (1, 1, 2)
    size_L3 (\x.t) =
        let (n, f, s) = size_L3 t in
        if x in FV(t)
        then (n+1, f-1, f+s)
        else (n+1, f, 1+f+s)
    size_L3 (t1 t2) =
        let (n1, f1, s1) = size_L3 t1 in
        let (n2, f2, s2) = size_L3 t2 in
        let m = size (FV(t1) /-\ FV(t2)) in
        (n1+n2+1, f1+f2-m, 1+f1+f2-m+s1+s2) -- 0 <= m <= min(f1, f2)

    size_LX :: LambdaTerm -> (Nat, [Nat])
    size_LX t = (numSub_L t, numFVs_L t)
    -- numSub_L t = number of subterms of t
    -- numFVs_L t = all FVs of subterms of t
    numSub_L x = 1
    numSub_L (t1 t2) = 1 + numSub_L t1 + numSub_L t2
    numSub_L (\x. t) = 1 + numSub_L t
    numFVs_L x = [1] -- [size FV(x)]
    numFVs_L (t1 t2) = size FV(t1 t2) : numFVs_L t1 ++ numFVs_L t2
    numFVs_L (\x. t) = size FV(\x.t) : numFVs_L t


    Combinator  = I
                | K Combinator
                | S Combinator Combinator
                | B Combinator Combinator
                | C Combinator Combinator
                | A Combinator Combinator -- application
    -- size_C = node of CombinatorTerm
    size_C I = 1
    size_C (K c) = 1 + size_C c
    size_C (S/B/C/A c1 c2) = 1 + size_C c1 + size_C c2

    remove_abs
    f
        x -> x
            1 -> 1
        t1 t2 -> (f t1) `A` (f t2)
            1 A -> 1 A
        \x.t -> sub x (f t)
            1 x -> 0
            each LambdaTerm map into a CombinatorTerm
            except this one, the abstraction!!!
            CombinatorTerm has one lesser term
    sub x c
        x not in FV(c) -> K c
            0 -> 1 K
            each sub preserve numTerm
            except this one!
            CombinatorTerm has one more K!
            if this 'sub' call was the one in "\x.t -> sub x (f t)"
            then the removed x in LambdaTerm meet this K
            else this 'sub' call was from below "c1 c2 -> ..." where
                each 'sub' meet one FV
            ==>> size_C (remove_abs t) <= size_L t
        case c of
            x -> I
                1 x -> 1 I
            c1 c2 -> case (x in FV(c1), x in FV(c2)) of
                T, T -> S (sub x c1) (sub x c2)
                    1 A -> 1 S
                    -2 x in FVs
                F, T -> B         c1 (sub x c2)
                    1 A -> 1 B
                    -1 x in FVs
                T, F -> C (sub x c1) c2
                    1 A -> 1 C
                    -1 x in FVs

    ? [FV(t) == {}] ==>> [numSub_L t ~ size_L t]
    ? numSub_L t ~ size_L t
    1 ->
        x
        [1] -> 2
    2 ->
        \x. x
        [0,1] -> 3
        \x. y
        [1,1] -> 4
    3 ->
        x x
        [1, ...] -> 6
        x y
        [2, ...] -> 7
    \x. t


'''

from collections import defaultdict
# calc the max size_L for each numSub_L, sizeFV
# max size_L = sub2fv2max[numSub_L][sizeFV]
sub2fv2max = {1:{1:2}}
sub2fv2max = defaultdict(lambda:defaultdict(int))
sub2fv2max[1][1] += 2
def insert(sub2fv2max, n_f_s):
    numSub_L, sizeFV, size_L = n_f_s
    if sub2fv2max[numSub_L][sizeFV] < size_L:
        sub2fv2max[numSub_L][sizeFV] = size_L
def calc_between(sub2fv2max, from_numSub_L, to_numSub_L):
    # sub2fv2max :: defaultdict(defaultdict(int))
    # from_numSub_L = 2; any numSub_L < from_numSub_L has given
    # [from_numSub_L..to_numSub_L] inclusive
    assert sub2fv2max
    assert 2 <= from_numSub_L <= to_numSub_L
    def update(n, f, s):
        insert(sub2fv2max, (n, f, s))
    for n in range(from_numSub_L, to_numSub_L+1):
        # sub2fv2max.setdefault(from_numSub_L, {})
        # abs: \x.t
        p1 = sub2fv2max[1]
        n1 = sub2fv2max[n-1]
        for f_p1 in p1.keys():
            for f_n1, s_n1 in n1.items():
                # x not in FV(t)
                f = f_n1
                s = 1 + f + s_n1
                update(n, f, s)

                # x in FV(t)
                if f > 0:
                    f -= 1
                    s -= 1
                    update(n, f, s)

        # app: t1 t2
        for i in range(1, n-1):
            j = n-1 - i
            assert j >= 1
            #bug: if j > i: break
            if j < i: break
            d1 = sub2fv2max[i]
            d2 = sub2fv2max[j]
            # (n1+n2+1, f1+f2-m, 1+f1+f2-m+s1+s2) -- 0 <= m <= min(f1, f2)
            for f1, s1 in d1.items():
                for f2, s2 in d2.items():
                    f12 = f1+f2
                    s12 = 1+f12+s1+s2
                    for common_fv in range(min(f1,f2)+1):
                        assert common_fv <= f12
                        #rint(common_fv, f12, f1, f2)
                        f = f12 - common_fv
                        s = s12 - common_fv
                        update(n, f, s)

def to_dict(sub2fv2max):
    return {k:dict(d) for k,d in sub2fv2max.items()}

def main():
    from pprint import pprint
    import sys
    args = sys.argv
    if len(args) != 2:
        raise ValueError('*.py <to_numSub_L>')
    _, to_numSub_L = args
    to_numSub_L = int(to_numSub_L)
    calc_between(sub2fv2max, 2, to_numSub_L)
    pprint(to_dict(sub2fv2max))

if __name__ == '__main__':
    main()










