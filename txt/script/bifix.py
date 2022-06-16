r'''
bifix 双缀

e script/bifix.py

py script/bifix.py -s '_find(True)'
py script/bifix.py -s '_find(False)'

py script/bifix.py -s '枚举所有非空真子双缀长度的可行配置(3)'
1
[([], [], [])]
2
[([], [], [(0, 1)]), ([1], [[0, 1]], [])]
3
[([], [], [(0, 1), (0, 2)]), ([], [[0, 1]], [(0, 2)]), ([1], [[0, 2]], [(0, 1)]), ([1, 2], [[0, 1, 2]], [])]

py script/bifix.py -s '枚举所有非空真子双缀长度的可行配置(9)' > ~/my_tmp/_.txt
py script/bifix.py -s '枚举所有非空真子双缀长度的可行配置(16)' > ~/my_tmp/_.txt
2 2
3 3
4 4
5 6
6 8
7 10
8 13
9 17
10 21
11 27
12 30
13 37
14 47
15 57
16 62
view /sdcard/0my_files/tmp/_.txt
len_str: 1
flatten: 1
grouped: 1
len_str: 2
flatten: 2
grouped: 2
len_str: 3
flatten: 4
grouped: 3
len_str: 4
flatten: 9
grouped: 4
len_str: 5
flatten: 20
grouped: 6
len_str: 6
flatten: 47
grouped: 8
len_str: 7
flatten: 110
grouped: 10
len_str: 8
flatten: 263
grouped: 13
len_str: 9
flatten: 630
grouped: 17
len_str: 10
flatten: 1525
grouped: 21
len_str: 11
flatten: 3701
grouped: 27
len_str: 12
flatten: 9039
grouped: 30
len_str: 13
flatten: 22140
grouped: 37
len_str: 14
flatten: 54460
grouped: 47
len_str: 15
flatten: 134339
grouped: 57


py script/bifix.py -s '枚举所有非空真子双缀长度的可行配置囗简单版(3)'
py script/bifix.py -s '枚举所有非空真子双缀长度的可行配置囗简单版(9)' > ~/my_tmp/_.txt
py script/bifix.py -s '枚举所有非空真子双缀长度的可行配置囗简单版(16)' > ~/my_tmp/_.txt
1 1
2 2
3 3
4 4
5 6
6 8
7 10
8 13
9 17
10 21
11 27
12 30
13 37
14 47
15 57
16 62


view /sdcard/0my_files/tmp/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt
view script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt.7z

OEIS 在线揭秘整数序列
    1 2 3 4 6 8 10 13 17 21 27 30 37 47 57 62
    https://oeis.org/A005434
    [[[
The OEIS is supported by the many generous donors to the OEIS Foundation.
 

(Greetings from The On-Line Encyclopedia of Integer Sequences!)
A005434		Number of distinct autocorrelations of binary words of length n.
(Formerly M0555)		8
1, 2, 3, 4, 6, 8, 10, 13, 17, 21, 27, 30, 37, 47, 57, 62, 75, 87, 102, 116, 135, 155, 180, 194, 220, 254, 289, 312, 359, 392, 438, 479, 538, 595, 664, 701, 772, 863, 956, 1005, 1115, 1205, 1317, 1414, 1552, 1677, 1836, 1920, 2074, 2249, 2444 (list; graph; refs; listen; history; text; internal format)
OFFSET	
1,2

COMMENTS	
Conjecture: a(n + 1) - a(n) < a(n + 13) - a(n + 12) for all n >= 1. - Eric Rowland, Nov 24 2021

REFERENCES	
R. L. Graham, D. E. Knuth and O. Patashnik, Concrete Mathematics, Addison-Wesley Publ., 2nd Ed., 1994. Section 8.4: Flipping Coins

N. J. A. Sloane and Simon Plouffe, The Encyclopedia of Integer Sequences, Academic Press, 1995 (includes this sequence).

LINKS	
E-Hern Lee, Table of n, a(n) for n = 1..654

L. J. Guibas, Periodicities in Strings, Combinatorial Algorithms on Words 1985, NATO ASI Vol. F12, 257-269

L. J. Guibas and A. M. Odlyzko, Periods in Strings, Journal of Combinatorial Theory A 30:1 (1981) 19-42.

Leo J. Guibas and Andrew M. Odlyzko, String overlaps, pattern matching and nontransitive games, Journal of Combinatorial Theory Series A, 30 (March 1981), 183-208.

H. Harborth, Endliche 0-1-Folgen mit gleichen Teilblöcken, Journal für Mathematik, 271 (1974) 139-154.

A. Kaseorg, Rust program used to compute values for n up to 500

E. H. Rivals and S. Rahmann, Combinatorics of Periods in Strings, Journal of Combinatorial Theory - Series A, Vol. 104(1) (2003), pp. 95-113.

E. H. Rivals, Autocorrelation of Strings.

E. H. Rivals and S. Rahmann Combinatorics of Periods in Strings

T. Sillke, Autocorrelation Range

T. Sillke, kappa sequence for words of length n

T. Sillke, The autocorrelation function

EXAMPLE	
From Eric Rowland, Nov 22 2021: (Start)

For n = 5 there are a(5) = 6 distinct autocorrelations of length-5 binary words:

  00000 can overlap itself in 1, 2, 3, 4, or 5 letters. Its autocorrelation is 11111.

  00100 can overlap itself in 1, 2, or 5 letters. Its autocorrelation is 10011.

  01010 can overlap itself in 1, 3, or 5 letters. Its autocorrelation is 10101.

  00010 can overlap itself in 1 or 5 letters. Its autocorrelation is 10001.

  01001 can overlap itself in 2 or 5 letters. Its autocorrelation is 10010.

  00001 can only overlap itself in 5 letters. Its autocorrelation is 10000.

(End)

MAPLE	
A005434 := proc( n :: posint )

    local    S := table();

    for local c in Iterator:-BinaryGrayCode( n ) do

        c := convert( c, 'list' );

        S[ [seq]( evalb( c[ 1 .. i + 1 ] = c[ n - i .. n ] ), i = 0 .. n - 1 ) ] := 0

    end do;

    numelems( S )

end proc: # James McCarron, Jun 21 2017

MATHEMATICA	
Table[Length[Union[Map[Flatten[Position[Table[Take[#, n-i]==Drop[#, i], {i, 0, n-1}], True]-1]&, Tuples[{0, 1}, n]]]], {n, 1, 15}] (* Geoffrey Critzer, Nov 29 2013 *)

CROSSREFS	
Cf. A018819 (related to a lower bound for autocorrelations), A045690 (the number of binary strings sharing the same autocorrelation).

Sequence in context: A325350 A027585 A123015 * A027589 A039851 A239100

Adjacent sequences:  A005431 A005432 A005433 * A005435 A005436 A005437

KEYWORD	
nonn,nice

AUTHOR	
Simon Plouffe, N. J. A. Sloane

EXTENSIONS	
More terms and additional references from torsten.sillke(at)lhsystems.com

Definition clarified by Eric Rowland, Nov 22 2021

STATUS	
approved

Lookup | Welcome | Wiki | Register | Music | Plot 2 | Demos | Index | Browse | More | WebCam
Contribute new seq. or comment | Format | Style Sheet | Transforms | Superseeker | Recents
The OEIS Community | Maintained by The OEIS Foundation Inc.
License Agreements, Terms of Use, Privacy Policy. .
Last modified June 16 08:57 EDT 2022. Contains 354568 sequences. (Running on oeis4.)
    ]]]

#'''



def _find(slack, /):
    i = 0
    Nothing = ()
    ls = [Nothing]
        #最长非空真子双缀长度
    while 1:
        i += 1
        s = f'{i:b}'
        n = len(s)
        for L in reversed(range(1, n)):
            if s[:L] == s[-L:]:
                j = int(s[:L], base=2)
                rj = ls[j]
                r = (rj, L)
                n = len(s)
                T = n-L
                print(i, s, n, T, L, j, r)
                if slack:
                  if 2*T < n and rj and not rj[-1] == L-T:
                    #443 110111011 9 4 5 27 ((((), 1), 2), 5)
                    #1 1011 1011
                    #11 011
                    return
                else:
                  if 2*T < n and rj and not rj[-1] == L-T and rj[-1] >= T:
                    #no i found: n <= 20
                    return
                break
        else:
            print(i)
            r = Nothing
        ls.append(r)

#_find()


r'''
from seed.types.union_find_algo.DisjointSet import UnionFindCtxOps__opaque_state4DisjointSet__ctx_is_element2opaque_state_mapping__union_by_rank__path_compression as UnionFindCtxOps4dict
view ../../python3_src/seed/abc/ICtxOps.py
view ../../python3_src/seed/types/union_find_algo/DisjointSet.py
mk_ctxops__via_ireplace_mutable_context
union_find_algo__init_raw_element
#'''
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
import sys
from seed.tiny import group4dict_value, fst, fmap4dict_value, snd
from seed.tiny import print_err
#from seed.iters.group_by import group_by
#def group_by(iterable, *, key=None, container=tuple):

def eq_lsls__to__idx2min_eq_idx(sz, eq_lsls, /):
    i2g = [*range(sz)]
    i2g = [None]*sz
    if not sorted(eq_lsls) == eq_lsls: raise ValueError
    for eq_ls in eq_lsls:
        if not sorted(eq_ls) == eq_ls: raise ValueError
        g = eq_ls[0]
        for i in eq_ls:
            if not 0 <= i < sz: raise ValueError
            #if not i2g[i] == i: raise ValueError
            if not i2g[i] is None: raise ValueError
            #if not g <= i: raise ValueError
            i2g[i] = g
    i2g = [i if g is None else g for i, g in enumerate(i2g)]
    return i2g


def 枚举所有非空真子双缀长度的可行配置(until, /):
    def 反双缀(sorted_bifix_lens, eq_lsls, i2g, ne_pairs, /):
        ilast = len(i2g)
        sorted_bifix_lens_ = []
        eq_lsls_ = eq_lsls
        ne_pairs_ = ((i2g[i], ilast) for i in [0, *sorted_bifix_lens])
        ne_pairs_ = sorted({*ne_pairs, *ne_pairs_})
        config = (sorted_bifix_lens_, eq_lsls_, ne_pairs_)
        yield config
    def 双缀增长(sorted_bifix_lens, eq_lsls, i2g, ne_pairs, /):
        ilast = len(i2g)
        pre_sz = len(i2g)
        if not pre_sz >= 1: raise logic-err
            #要求 结果 为 非空真子双缀。因为 使用了 0长 双缀，加一后 非空，但 真子 要求 curr_sz >= 2, pre_sz >= 1
        idc = [0, *sorted_bifix_lens]
        assert len({*idc}) == len(idc)
        assert sorted(idc) == idc
        gs = [i2g[i] for i in idc]
        g2bifix_lens = {g:[] for g in gs}
        for i, g in zip(idc, gs):
            g2bifix_lens[g].append(i+1)
        g2i4eq_lsls = {eq_ls[0]:i for i, eq_ls in enumerate(eq_lsls)}
        for g, bifix_lens in sorted(g2bifix_lens.items()):
            sorted_bifix_lens_ = bifix_lens
            if g in g2i4eq_lsls:
                i4eq_lsls = g2i4eq_lsls[g]
                    #KeyError: 0
                eq_ls_ = [*eq_lsls[i4eq_lsls], ilast]
                eq_lsls_ = [*eq_lsls]
                eq_lsls_[i4eq_lsls] = eq_ls_
            else:
                eq_ls_ = [g, ilast]
                eq_lsls_ = [eq_ls_, *eq_lsls]
                eq_lsls_.sort()
            ne_pairs_ = ne_pairs
            config = (sorted_bifix_lens_, eq_lsls_, ne_pairs_)
            yield config


    def show(sz, configs, /):
        #ps = (((*sorted_bifix_lens,), (eq_lsls, ne_pairs)) for (sorted_bifix_lens, eq_lsls, ne_pairs) in configs)
        i2pair = {i: ((*sorted_bifix_lens,), (eq_lsls, ne_pairs)) for i, (sorted_bifix_lens, eq_lsls, ne_pairs) in enumerate(configs)}
        lens2i2pair = group4dict_value(fst, i2pair)
        def i2pair_to_sorted_pairs(i2pair, /):
            return sorted(map(snd, i2pair.values()))
        lens2pairs = fmap4dict_value(i2pair_to_sorted_pairs, lens2i2pair)
        print_err(sz, len(lens2pairs))
        print('len_str:', sz)
        print('flatten:', len(configs))
        print('grouped:', len(lens2pairs))
        stable_repr_print__expand_top_layer(sys.stdout, lens2pairs)
        print()

    def main():
        sz2configs = [[], [([], [], [])]]
            # S -> [(sorted[uint], eq_lsls, ne_pairs)]
        S = len(sz2configs)-1
        while 1:
            sz2configs[-1].sort()
            show(S, sz2configs[-1])
            if S == until: break
            ##next round
            S = sz = len(sz2configs)
            ilast = S-1
            configs = []
            for config in sz2configs[-1]:
                (sorted_bifix_lens, eq_lsls, ne_pairs) = config
                i2g = eq_lsls__to__idx2min_eq_idx(ilast, eq_lsls)
                configs_ = 反双缀(sorted_bifix_lens, eq_lsls, i2g, ne_pairs)
                configs.extend(configs_)
                configs_ = 双缀增长(sorted_bifix_lens, eq_lsls, i2g, ne_pairs)
                configs.extend(configs_)
            sz2configs.append(configs)

            #
    main()
#枚举所有非空真子双缀长度的可行配置()

#[[[枚举所有非空真子双缀长度的可行配置囗简单版
# copy from: view script/bifix.py
# copy to: view others/数学/编程/永恒代码/原貌字符串.txt
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
from seed.tiny import print_err
def 枚举所有非空真子双缀长度的可行配置囗简单版(until, /):
    def show(sz, config2instance, /):
        bifix_lens2seq = config2instance
        print_err(sz, len(bifix_lens2seq))
        print('len_seq:', sz)
        print('grouped:', len(bifix_lens2seq))
        stable_repr_print__expand_top_layer(sys.stdout, bifix_lens2seq)
        print()


    def instance2sorted_bifix_lens(instance, /):
        return tuple(i for i in range(1, len(instance)) if instance[:i] == instance[-i:])

    def main():
        sz2config2instance = [{}, {():[0]}]
            # S -> {sorted_bifix_lens/sorted[uint%S]:instance/[uint%S]{len=S}}
        S = len(sz2config2instance)-1
        while 1:
            show(S, sz2config2instance[S])
            if S == until: break
            ##next round
            S = sz = len(sz2config2instance)
            ilast = S-1
            config2instance = {}
            def add(sorted_bifix_lens, instance, /):
                assert len(instance) == S
                assert sorted_bifix_lens not in config2instance
                assert sorted_bifix_lens == instance2sorted_bifix_lens(instance)
                config2instance[sorted_bifix_lens] = instance
            #def add(sorted_bifix_lens, instance, /):

            for pseudo_period in range(1, S+1):
                q, r = divmod(S, pseudo_period)
                assert q >= 1
                if q > 1:
                    assert 1 <= pseudo_period <= S//2
                    sz__small = r+pseudo_period
                    assert 0 < sz__small < S
                    config2instance__small = sz2config2instance[sz__small]
                    if r == 0:
                        def pred(sorted_bifix_lens__small, /):
                            assert sz__small == pseudo_period
                            if sorted_bifix_lens__small:
                                min_pseudo_period__small = sz__small - sorted_bifix_lens__small[-1]
                                return not pseudo_period%min_pseudo_period__small==0
                            return True
                    else:
                        def pred(sorted_bifix_lens__small, /):
                            if not r in sorted_bifix_lens__small:
                                return False
                            min_pseudo_period__small = sz__small - sorted_bifix_lens__small[-1]

                            return min_pseudo_period__small == pseudo_period or not pseudo_period%min_pseudo_period__small==0
                    ##end-def-pred()
                    ex = (*range(sz__small, S, pseudo_period),)
                    for sorted_bifix_lens__small, instance__small in config2instance__small.items():
                        if not pred(sorted_bifix_lens__small):continue
                        sorted_bifix_lens = sorted_bifix_lens__small + ex
                        instance = instance__small + instance__small[r:]*(q-1)
                        add(sorted_bifix_lens, instance)
                #if q > 1:
                else:
                    assert q==1
                    assert pseudo_period > S//2
                    if r == 0:
                        assert pseudo_period == S
                        sorted_bifix_lens = ()
                        instance = [0]*S
                        instance[-1] = 1
                        add(sorted_bifix_lens, instance)
                    else:
                        assert 1 <= r < pseudo_period
                        assert r+pseudo_period == S
                        assert 2*r < S
                        sz__small = r
                        config2instance__small = sz2config2instance[sz__small]
                        for sorted_bifix_lens__small, instance__small in config2instance__small.items():
                            sorted_bifix_lens = sorted_bifix_lens__small + (sz__small,)
                            instance = instance__small + [sz__small]*(S-2*sz__small) + instance__small
                            add(sorted_bifix_lens, instance)
            sz2config2instance.append(config2instance)
        #end-while 1:
        sz2config2instance
        sz2num_configs = [*map(len, sz2config2instance)]
        print_err(sz2num_configs)
    #end-def main():



    main()
#end-def 枚举所有非空真子双缀长度的可行配置囗简单版(until, /):
    r'''[[[
py script/bifix.py -s '枚举所有非空真子双缀长度的可行配置囗简单版(50)' > ~/my_tmp/_.txt
.../txt_phone/txt $ py script/bifix.py -s '枚举所 有非空真子双缀长度的可行配置囗简单版(50)' > ~/my_tmp/_.txt
1 1
2 2
3 3
4 4
5 6
6 8
7 10
8 13
9 17
10 21
11 27
12 30
13 37
14 47
15 57
16 62
17 75
18 87
19 102
20 116
21 135
22 155
23 180
24 194
25 220
26 254
27 289
28 312
29 359
30 392
31 438
32 479
33 538
34 595
35 664
36 701
37 772
38 863
39 956
40 1005
41 1115
42 1205
43 1317
44 1414
45 1552
46 1677
47 1836
48 1920
49 2074
50 2249
[0, 1, 2, 3, 4, 6, 8, 10, 13, 17, 21, 27, 30, 37, 47, 57, 62, 75, 87, 102, 116, 135, 155, 180, 194, 220, 254, 289, 312, 359, 392, 438, 479, 538, 595, 664, 701, 772, 863, 956, 1005, 1115, 1205, 1317, 1414, 1552, 1677, 1836, 1920, 2074, 2249]
.../txt_phone/txt $

cp ~/my_tmp/_.txt ~/my_txt/'script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt'
view script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt
!du -h 'script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt'
    3.7MB !!!
7z a  ~/my_txt/'script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt'.7z  ~/my_txt/'script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt'
!du -h 'script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt'.7z
    164KB

mv ~/my_txt/'script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt' ~/my_tmp/
view /sdcard/0my_files/tmp/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt
view script/bifix.py.out.枚举所有非空真子双缀长度的可行配置囗简单版(50).txt.7z



py script/bifix.py -s '枚举所有非空真子双缀长度的可行配置囗简单版(16)' > ~/my_tmp/_.txt
1 1
2 2
3 3
4 4
5 6
6 8
7 10
8 13
9 17
10 21
11 27
12 30
13 37
14 47
15 57
16 62


view /sdcard/0my_files/tmp/_.txt
len_seq: 1
grouped: 1
{()
: [0]
}
len_seq: 2
grouped: 2
{()
: [0, 1]
,(1,)
: [0, 0]
}
len_seq: 3
grouped: 3
{()
: [0, 0, 1]
,(1,)
: [0, 1, 0]
,(1, 2)
: [0, 0, 0]
}
len_seq: 4
grouped: 4
{()
: [0, 0, 0, 1]
,(1,)
: [0, 1, 1, 0]
,(2,)
: [0, 1, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 0]
}
len_seq: 5
grouped: 6
{()
: [0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 0, 1]
,(1, 2)
: [0, 0, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 1, 0]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 0]
}
len_seq: 6
grouped: 8
{()
: [0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 0, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 0, 1]
,(1, 2, 3, 4, 5)
: [0, 0, 0, 0, 0, 0]
}
len_seq: 7
grouped: 10
{()
: [0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 1, 1, 0]
,(1, 2, 3)
: [0, 0, 0, 3, 0, 0, 0]
,(1, 3, 5)
: [0, 1, 0, 1, 0, 1, 0]
,(1, 2, 3, 4, 5, 6)
: [0, 0, 0, 0, 0, 0, 0]
}
len_seq: 8
grouped: 13
{()
: [0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 0, 1, 1, 0]
,(2, 5)
: [0, 1, 2, 0, 1, 2, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 2, 0, 0]
,(2, 4, 6)
: [0, 1, 0, 1, 0, 1, 0, 1]
,(1, 2, 3, 4, 5, 6, 7)
: [0, 0, 0, 0, 0, 0, 0, 0]
}
len_seq: 9
grouped: 17
{()
: [0, 0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 4, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 4, 0, 1, 1, 0]
,(1, 5)
: [0, 1, 1, 1, 0, 1, 1, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 4, 0, 1, 0, 1]
,(3, 6)
: [0, 0, 1, 0, 0, 1, 0, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 0, 2, 0, 0]
,(1, 3, 6)
: [0, 1, 0, 0, 1, 0, 0, 1, 0]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 4, 0, 0, 0, 0]
,(1, 3, 5, 7)
: [0, 1, 0, 1, 0, 1, 0, 1, 0]
,(1, 2, 3, 4, 5, 6, 7, 8)
: [0, 0, 0, 0, 0, 0, 0, 0, 0]
}
len_seq: 10
grouped: 21
{()
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 4, 4, 0, 0, 0, 1]
,(5,)
: [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 4, 4, 0, 1, 1, 0]
,(1, 5)
: [0, 1, 1, 1, 0, 0, 1, 1, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 4, 4, 0, 1, 0, 1]
,(2, 5)
: [0, 1, 2, 0, 1, 0, 1, 2, 0, 1]
,(2, 6)
: [0, 1, 2, 2, 0, 1, 2, 2, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 0, 0, 2, 0, 0]
,(1, 2, 6)
: [0, 0, 2, 2, 0, 0, 2, 2, 0, 0]
,(1, 3, 5)
: [0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
,(1, 4, 7)
: [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 4, 4, 0, 0, 0, 0]
,(2, 4, 6, 8)
: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
,(1, 2, 3, 4, 5, 6, 7, 8, 9)
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
len_seq: 11
grouped: 27
{()
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 3, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 4, 4, 4, 0, 0, 0, 1]
,(5,)
: [0, 0, 0, 0, 1, 5, 0, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 3, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 4, 4, 4, 0, 1, 1, 0]
,(1, 5)
: [0, 1, 1, 1, 0, 5, 0, 1, 1, 1, 0]
,(1, 6)
: [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 4, 4, 4, 0, 1, 0, 1]
,(2, 5)
: [0, 1, 2, 0, 1, 5, 0, 1, 2, 0, 1]
,(3, 7)
: [0, 0, 1, 3, 0, 0, 1, 3, 0, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 5, 0, 0, 2, 0, 0]
,(1, 2, 6)
: [0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0]
,(1, 3, 5)
: [0, 1, 0, 1, 0, 5, 0, 1, 0, 1, 0]
,(1, 3, 6)
: [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
,(1, 3, 7)
: [0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0]
,(2, 5, 8)
: [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0]
,(1, 2, 3, 7)
: [0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0]
,(1, 2, 5, 8)
: [0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0]
,(1, 2, 3, 4, 5)
: [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0]
,(1, 3, 5, 7, 9)
: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
len_seq: 12
grouped: 30
{()
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 3, 3, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 4, 4, 4, 4, 0, 0, 0, 1]
,(5,)
: [0, 0, 0, 0, 1, 5, 5, 0, 0, 0, 0, 1]
,(6,)
: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 3, 3, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 4, 4, 4, 4, 0, 1, 1, 0]
,(1, 5)
: [0, 1, 1, 1, 0, 5, 5, 0, 1, 1, 1, 0]
,(1, 6)
: [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 4, 4, 4, 4, 0, 1, 0, 1]
,(2, 5)
: [0, 1, 2, 0, 1, 5, 5, 0, 1, 2, 0, 1]
,(2, 6)
: [0, 1, 2, 2, 0, 1, 0, 1, 2, 2, 0, 1]
,(2, 7)
: [0, 1, 2, 2, 2, 0, 1, 2, 2, 2, 0, 1]
,(4, 8)
: [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 5, 5, 0, 0, 2, 0, 0]
,(1, 2, 6)
: [0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0]
,(1, 2, 7)
: [0, 0, 2, 2, 2, 0, 0, 2, 2, 2, 0, 0]
,(1, 3, 5)
: [0, 1, 0, 1, 0, 5, 5, 0, 1, 0, 1, 0]
,(1, 4, 8)
: [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
,(3, 6, 9)
: [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0, 0]
,(1, 2, 3, 7)
: [0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0]
,(1, 3, 6, 9)
: [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
,(1, 2, 3, 4, 5)
: [0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0]
,(2, 4, 6, 8, 10)
: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
len_seq: 13
grouped: 37
{()
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 4, 4, 4, 4, 4, 0, 0, 0, 1]
,(5,)
: [0, 0, 0, 0, 1, 5, 5, 5, 0, 0, 0, 0, 1]
,(6,)
: [0, 0, 0, 0, 0, 1, 6, 0, 0, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 3, 3, 3, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 4, 4, 4, 4, 4, 0, 1, 1, 0]
,(1, 5)
: [0, 1, 1, 1, 0, 5, 5, 5, 0, 1, 1, 1, 0]
,(1, 6)
: [0, 1, 1, 1, 1, 0, 6, 0, 1, 1, 1, 1, 0]
,(1, 7)
: [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 4, 4, 4, 4, 4, 0, 1, 0, 1]
,(2, 5)
: [0, 1, 2, 0, 1, 5, 5, 5, 0, 1, 2, 0, 1]
,(2, 6)
: [0, 1, 2, 2, 0, 1, 6, 0, 1, 2, 2, 0, 1]
,(3, 6)
: [0, 0, 1, 0, 0, 1, 6, 0, 0, 1, 0, 0, 1]
,(3, 8)
: [0, 0, 1, 3, 3, 0, 0, 1, 3, 3, 0, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 5, 5, 5, 0, 0, 2, 0, 0]
,(1, 2, 6)
: [0, 0, 2, 2, 0, 0, 6, 0, 0, 2, 2, 0, 0]
,(1, 2, 7)
: [0, 0, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 0]
,(1, 3, 5)
: [0, 1, 0, 1, 0, 5, 5, 5, 0, 1, 0, 1, 0]
,(1, 3, 6)
: [0, 1, 0, 0, 1, 0, 6, 0, 1, 0, 0, 1, 0]
,(1, 3, 7)
: [0, 1, 0, 3, 0, 1, 0, 1, 0, 3, 0, 1, 0]
,(1, 3, 8)
: [0, 1, 0, 3, 3, 0, 1, 0, 3, 3, 0, 1, 0]
,(1, 5, 9)
: [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]
,(2, 4, 6)
: [0, 1, 0, 1, 0, 1, 6, 0, 1, 0, 1, 0, 1]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0]
,(1, 2, 3, 7)
: [0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0]
,(1, 2, 3, 8)
: [0, 0, 0, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0]
,(1, 2, 5, 9)
: [0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0]
,(1, 4, 7, 10)
: [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
,(1, 2, 3, 4, 5)
: [0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0]
,(1, 2, 3, 4, 5, 6)
: [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0]
,(1, 3, 5, 7, 9, 11)
: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
len_seq: 14
grouped: 47
{()
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 0, 0, 0, 1]
,(5,)
: [0, 0, 0, 0, 1, 5, 5, 5, 5, 0, 0, 0, 0, 1]
,(6,)
: [0, 0, 0, 0, 0, 1, 6, 6, 0, 0, 0, 0, 0, 1]
,(7,)
: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 4, 4, 4, 4, 4, 4, 0, 1, 1, 0]
,(1, 5)
: [0, 1, 1, 1, 0, 5, 5, 5, 5, 0, 1, 1, 1, 0]
,(1, 6)
: [0, 1, 1, 1, 1, 0, 6, 6, 0, 1, 1, 1, 1, 0]
,(1, 7)
: [0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 4, 4, 4, 4, 4, 4, 0, 1, 0, 1]
,(2, 5)
: [0, 1, 2, 0, 1, 5, 5, 5, 5, 0, 1, 2, 0, 1]
,(2, 6)
: [0, 1, 2, 2, 0, 1, 6, 6, 0, 1, 2, 2, 0, 1]
,(2, 7)
: [0, 1, 2, 2, 2, 0, 1, 0, 1, 2, 2, 2, 0, 1]
,(2, 8)
: [0, 1, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2, 0, 1]
,(3, 6)
: [0, 0, 1, 0, 0, 1, 6, 6, 0, 0, 1, 0, 0, 1]
,(3, 7)
: [0, 0, 1, 3, 0, 0, 1, 0, 0, 1, 3, 0, 0, 1]
,(4, 9)
: [0, 0, 0, 1, 4, 0, 0, 0, 1, 4, 0, 0, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 5, 5, 5, 5, 0, 0, 2, 0, 0]
,(1, 2, 6)
: [0, 0, 2, 2, 0, 0, 6, 6, 0, 0, 2, 2, 0, 0]
,(1, 2, 7)
: [0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 0, 0]
,(1, 2, 8)
: [0, 0, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 0]
,(1, 3, 5)
: [0, 1, 0, 1, 0, 5, 5, 5, 5, 0, 1, 0, 1, 0]
,(1, 3, 6)
: [0, 1, 0, 0, 1, 0, 6, 6, 0, 1, 0, 0, 1, 0]
,(1, 3, 7)
: [0, 1, 0, 3, 0, 1, 0, 0, 1, 0, 3, 0, 1, 0]
,(1, 4, 7)
: [0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]
,(1, 4, 9)
: [0, 1, 1, 0, 4, 0, 1, 1, 0, 4, 0, 1, 1, 0]
,(2, 4, 6)
: [0, 1, 0, 1, 0, 1, 6, 6, 0, 1, 0, 1, 0, 1]
,(2, 4, 9)
: [0, 1, 0, 1, 4, 0, 1, 0, 1, 4, 0, 1, 0, 1]
,(2, 6, 10)
: [0, 1, 2, 2, 0, 1, 2, 2, 0, 1, 2, 2, 0, 1]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0]
,(1, 2, 3, 7)
: [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0]
,(1, 2, 3, 8)
: [0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0]
,(1, 2, 6, 10)
: [0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0]
,(1, 3, 5, 7)
: [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
,(2, 5, 8, 11)
: [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1]
,(1, 2, 3, 4, 5)
: [0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 0, 0]
,(1, 2, 3, 4, 9)
: [0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0]
,(1, 2, 5, 8, 11)
: [0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0]
,(1, 2, 3, 4, 5, 6)
: [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0]
,(2, 4, 6, 8, 10, 12)
: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
len_seq: 15
grouped: 57
{()
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 1]
,(5,)
: [0, 0, 0, 0, 1, 5, 5, 5, 5, 5, 0, 0, 0, 0, 1]
,(6,)
: [0, 0, 0, 0, 0, 1, 6, 6, 6, 0, 0, 0, 0, 0, 1]
,(7,)
: [0, 0, 0, 0, 0, 0, 1, 7, 0, 0, 0, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 4, 4, 4, 4, 4, 4, 4, 0, 1, 1, 0]
,(1, 5)
: [0, 1, 1, 1, 0, 5, 5, 5, 5, 5, 0, 1, 1, 1, 0]
,(1, 6)
: [0, 1, 1, 1, 1, 0, 6, 6, 6, 0, 1, 1, 1, 1, 0]
,(1, 7)
: [0, 1, 1, 1, 1, 1, 0, 7, 0, 1, 1, 1, 1, 1, 0]
,(1, 8)
: [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 4, 4, 4, 4, 4, 4, 4, 0, 1, 0, 1]
,(2, 5)
: [0, 1, 2, 0, 1, 5, 5, 5, 5, 5, 0, 1, 2, 0, 1]
,(2, 6)
: [0, 1, 2, 2, 0, 1, 6, 6, 6, 0, 1, 2, 2, 0, 1]
,(2, 7)
: [0, 1, 2, 2, 2, 0, 1, 7, 0, 1, 2, 2, 2, 0, 1]
,(3, 6)
: [0, 0, 1, 0, 0, 1, 6, 6, 6, 0, 0, 1, 0, 0, 1]
,(3, 7)
: [0, 0, 1, 3, 0, 0, 1, 7, 0, 0, 1, 3, 0, 0, 1]
,(3, 9)
: [0, 0, 1, 3, 3, 3, 0, 0, 1, 3, 3, 3, 0, 0, 1]
,(5, 10)
: [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 5, 5, 5, 5, 5, 0, 0, 2, 0, 0]
,(1, 2, 6)
: [0, 0, 2, 2, 0, 0, 6, 6, 6, 0, 0, 2, 2, 0, 0]
,(1, 2, 7)
: [0, 0, 2, 2, 2, 0, 0, 7, 0, 0, 2, 2, 2, 0, 0]
,(1, 2, 8)
: [0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0]
,(1, 3, 5)
: [0, 1, 0, 1, 0, 5, 5, 5, 5, 5, 0, 1, 0, 1, 0]
,(1, 3, 6)
: [0, 1, 0, 0, 1, 0, 6, 6, 6, 0, 1, 0, 0, 1, 0]
,(1, 3, 7)
: [0, 1, 0, 3, 0, 1, 0, 7, 0, 1, 0, 3, 0, 1, 0]
,(1, 3, 8)
: [0, 1, 0, 3, 3, 0, 1, 0, 1, 0, 3, 3, 0, 1, 0]
,(1, 3, 9)
: [0, 1, 0, 3, 3, 3, 0, 1, 0, 3, 3, 3, 0, 1, 0]
,(1, 4, 7)
: [0, 1, 1, 0, 1, 1, 0, 7, 0, 1, 1, 0, 1, 1, 0]
,(1, 4, 8)
: [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0]
,(1, 5, 10)
: [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0]
,(2, 4, 6)
: [0, 1, 0, 1, 0, 1, 6, 6, 6, 0, 1, 0, 1, 0, 1]
,(2, 5, 10)
: [0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1]
,(3, 7, 11)
: [0, 0, 1, 3, 0, 0, 1, 3, 0, 0, 1, 3, 0, 0, 1]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0]
,(1, 2, 3, 7)
: [0, 0, 0, 3, 0, 0, 0, 7, 0, 0, 0, 3, 0, 0, 0]
,(1, 2, 3, 8)
: [0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0]
,(1, 2, 3, 9)
: [0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 3, 0, 0, 0]
,(1, 2, 5, 8)
: [0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0]
,(1, 2, 5, 10)
: [0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0]
,(1, 3, 5, 7)
: [0, 1, 0, 1, 0, 1, 0, 7, 0, 1, 0, 1, 0, 1, 0]
,(1, 3, 5, 10)
: [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
,(1, 3, 7, 11)
: [0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0, 3, 0, 1, 0]
,(3, 6, 9, 12)
: [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
,(1, 2, 3, 4, 5)
: [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0]
,(1, 2, 3, 4, 9)
: [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0]
,(1, 2, 3, 7, 11)
: [0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0]
,(1, 3, 6, 9, 12)
: [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
,(1, 2, 3, 4, 5, 6)
: [0, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 0]
,(1, 2, 3, 4, 5, 6, 7)
: [0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0]
,(1, 3, 5, 7, 9, 11, 13)
: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
len_seq: 16
grouped: 62
{()
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
,(1,)
: [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
,(2,)
: [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1]
,(3,)
: [0, 0, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 1]
,(4,)
: [0, 0, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 1]
,(5,)
: [0, 0, 0, 0, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 1]
,(6,)
: [0, 0, 0, 0, 0, 1, 6, 6, 6, 6, 0, 0, 0, 0, 0, 1]
,(7,)
: [0, 0, 0, 0, 0, 0, 1, 7, 7, 0, 0, 0, 0, 0, 0, 1]
,(8,)
: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
,(1, 2)
: [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
,(1, 3)
: [0, 1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 1, 0]
,(1, 4)
: [0, 1, 1, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 1, 1, 0]
,(1, 5)
: [0, 1, 1, 1, 0, 5, 5, 5, 5, 5, 5, 0, 1, 1, 1, 0]
,(1, 6)
: [0, 1, 1, 1, 1, 0, 6, 6, 6, 6, 0, 1, 1, 1, 1, 0]
,(1, 7)
: [0, 1, 1, 1, 1, 1, 0, 7, 7, 0, 1, 1, 1, 1, 1, 0]
,(1, 8)
: [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0]
,(2, 4)
: [0, 1, 0, 1, 4, 4, 4, 4, 4, 4, 4, 4, 0, 1, 0, 1]
,(2, 5)
: [0, 1, 2, 0, 1, 5, 5, 5, 5, 5, 5, 0, 1, 2, 0, 1]
,(2, 6)
: [0, 1, 2, 2, 0, 1, 6, 6, 6, 6, 0, 1, 2, 2, 0, 1]
,(2, 7)
: [0, 1, 2, 2, 2, 0, 1, 7, 7, 0, 1, 2, 2, 2, 0, 1]
,(2, 8)
: [0, 1, 2, 2, 2, 2, 0, 1, 0, 1, 2, 2, 2, 2, 0, 1]
,(2, 9)
: [0, 1, 2, 2, 2, 2, 2, 0, 1, 2, 2, 2, 2, 2, 0, 1]
,(3, 6)
: [0, 0, 1, 0, 0, 1, 6, 6, 6, 6, 0, 0, 1, 0, 0, 1]
,(3, 7)
: [0, 0, 1, 3, 0, 0, 1, 7, 7, 0, 0, 1, 3, 0, 0, 1]
,(3, 8)
: [0, 0, 1, 3, 3, 0, 0, 1, 0, 0, 1, 3, 3, 0, 0, 1]
,(4, 10)
: [0, 0, 0, 1, 4, 4, 0, 0, 0, 1, 4, 4, 0, 0, 0, 1]
,(1, 2, 3)
: [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0]
,(1, 2, 5)
: [0, 0, 2, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 2, 0, 0]
,(1, 2, 6)
: [0, 0, 2, 2, 0, 0, 6, 6, 6, 6, 0, 0, 2, 2, 0, 0]
,(1, 2, 7)
: [0, 0, 2, 2, 2, 0, 0, 7, 7, 0, 0, 2, 2, 2, 0, 0]
,(1, 2, 8)
: [0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0]
,(1, 2, 9)
: [0, 0, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0]
,(1, 3, 5)
: [0, 1, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 1, 0, 1, 0]
,(1, 3, 6)
: [0, 1, 0, 0, 1, 0, 6, 6, 6, 6, 0, 1, 0, 0, 1, 0]
,(1, 3, 7)
: [0, 1, 0, 3, 0, 1, 0, 7, 7, 0, 1, 0, 3, 0, 1, 0]
,(1, 3, 8)
: [0, 1, 0, 3, 3, 0, 1, 0, 0, 1, 0, 3, 3, 0, 1, 0]
,(1, 4, 7)
: [0, 1, 1, 0, 1, 1, 0, 7, 7, 0, 1, 1, 0, 1, 1, 0]
,(1, 4, 10)
: [0, 1, 1, 0, 4, 4, 0, 1, 1, 0, 4, 4, 0, 1, 1, 0]
,(1, 6, 11)
: [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]
,(2, 4, 6)
: [0, 1, 0, 1, 0, 1, 6, 6, 6, 6, 0, 1, 0, 1, 0, 1]
,(2, 4, 9)
: [0, 1, 0, 1, 4, 0, 1, 0, 1, 0, 1, 4, 0, 1, 0, 1]
,(2, 4, 10)
: [0, 1, 0, 1, 4, 4, 0, 1, 0, 1, 4, 4, 0, 1, 0, 1]
,(2, 5, 8)
: [0, 1, 2, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1]
,(4, 8, 12)
: [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
,(1, 2, 3, 4)
: [0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0]
,(1, 2, 3, 7)
: [0, 0, 0, 3, 0, 0, 0, 7, 7, 0, 0, 0, 3, 0, 0, 0]
,(1, 2, 3, 8)
: [0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0]
,(1, 2, 3, 9)
: [0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0]
,(1, 2, 5, 8)
: [0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0]
,(1, 2, 5, 9)
: [0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0]
,(1, 2, 6, 11)
: [0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0]
,(1, 3, 5, 7)
: [0, 1, 0, 1, 0, 1, 0, 7, 7, 0, 1, 0, 1, 0, 1, 0]
,(1, 3, 6, 11)
: [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
,(1, 4, 8, 12)
: [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
,(1, 2, 3, 4, 5)
: [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0]
,(1, 2, 3, 4, 9)
: [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0]
,(1, 2, 3, 4, 10)
: [0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0]
,(1, 4, 7, 10, 13)
: [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
,(1, 2, 3, 4, 5, 6)
: [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0]
,(1, 2, 3, 4, 5, 6, 7)
: [0, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0]
,(2, 4, 6, 8, 10, 12, 14)
: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
,(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
    #]]]'''
#]]]枚举所有非空真子双缀长度的可行配置囗简单版


def main(args=None, /):
    import argparse

    parser = argparse.ArgumentParser(
        description='字串 双缀/拟周期 相关'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-s', '--stmt4py', type=str, default=None
                        , help='input exec stmt for python')

    args = parser.parse_args(args)
    exec(args.stmt4py)

if __name__ == "__main__":
    main()



