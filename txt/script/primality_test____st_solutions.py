#__all__:goto
r'''[[[
e script/primality_test____st_solutions.py
view others/数学/prime/primality_test.txt


script.primality_test____st_solutions
py -m nn_ns.app.debug_cmd   script.primality_test____st_solutions -x
py -m nn_ns.app.doctest_cmd script.primality_test____st_solutions:__doc__ -ff -v
from script.primality_test____st_solutions import *

[eR == s*t*eF + (s+t)][0 <= s <= t > 0][gcd(eR,eF) == 1][eF%2 == 0][gcd(eR,W) == 1][r := eR%W][f := eF%W][gcd(W,r) == 1][[W%2 == 0] -> [f%2 == 0]]:
    [s*t%W == ???]
    [gcd(W,s*t)%??? == 0]
    ===
    [r =[%W]= s*t*f + (s+t)]
    [r-s =[%W]= (s*f+1)*t]
    [g := gcd(W, (s*f+1))]
    [(r-s)%g == 0]:
        [(r-s)///g *s =[%W///g]= (s*f+1)///g *(s*t)]
        [(r-s)///g*s*inv_mod_(W///g;(s*f+1)///g) =[%W///g]= (s*t)]

    [-r*f+s*f =[%W]= -f*(1+s*f)*t]
    [-r*f =[%W]= 1]:
        <==> [-eF*eR =[%W]= 1]
        <==> [0 =[%W]= 1+eF*eR == m]
    !! [m%W =!= 0]
    [(1+r*f) %W =!= 0]
    [t%W == _5s(s)]
        #depends on s, not constant
    ===
    !! [gcd(eR,eF) == 1][eF%2 == 0]
    [eR%2 == 1]
    !! [eR == s*t*eF + (s+t)]
    [(s+t)%2 == 1]
    [s%2 == 1 -t%2]

    [W == 2**k][r == 1]:
        [g == 1]
        [f%W == 0]:
            [(s+t)%W == r == 1]
            [s*t
            =[%W]= t*(1-t)
            =[%W]= t -t**2
            =[%W]= s -s**2
            ]
            [k <= 3][gcd(W,t) == 1]:
                [t**2 %W == 1]


py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_powers_  ='[(2,3)]' +with_sts
    [g==2]
py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_  =15
    [g==3]
py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_  =5
    no g
py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_  =7
    no g
py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_  =11
    no g
py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_  =13
    no g

py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_  +with_st_mod_W =5
    no output
py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_  +with_st_mod_W =10
    [g==2][may_imay_st_mod_W is None]

[[[
py_adhoc_call   script.primality_test____st_solutions   ,iter_st_solutions_mod_powers_  ='[(2,[1,2]), (3,[1,2]), (5,1)]'
===
((2, 1), (1, 0), 2)
((2, 2), (1, 0), 2)
((2, 2), (1, 2), 2)
((2, 2), (3, 0), 2)
((2, 2), (3, 2), 2)
((3, 1), (1, 1), 3)
((3, 1), (2, 2), 3)
((3, 2), (1, 1), 3)
((3, 2), (1, 4), 3)
((3, 2), (1, 7), 3)
((3, 2), (2, 2), 3)
((3, 2), (2, 5), 3)
((3, 2), (2, 8), 3)
((3, 2), (4, 1), 3)
((3, 2), (4, 4), 3)
((3, 2), (4, 7), 3)
((3, 2), (5, 2), 3)
((3, 2), (5, 5), 3)
((3, 2), (5, 8), 3)
((3, 2), (7, 1), 3)
((3, 2), (7, 4), 3)
((3, 2), (7, 7), 3)
((3, 2), (8, 2), 3)
((3, 2), (8, 5), 3)
((3, 2), (8, 8), 3)
]]]


#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from math import gcd

def iter_st_solutions_mod_powers_(pks, /, **kwds):
    for p, k_or_ks in pks:
        if type(k_or_ks) is int:
            k = k_or_ks
            ks = [k]
        else:
            ks = k_or_ks
        for k in ks:
            yield from iter_st_solutions_mod_power_(p, k, **kwds)

def iter_st_solutions_mod_power_(p, k, /, **kwds):
    assert p >= 2
    assert k >= 1
    for (W, (r, f), g, *ls) in iter_st_solutions_mod_(p**k, **kwds):
        yield ((p, k), (r, f), g, *ls)

def _iter_rfs4iter_st_solutions_mod_(W, /):
    assert W >= 2
    even_W = (W&1) == 0
    for r in range(1, W):
        if not gcd(W, r) == 1:continue
        #f2sts = [[] for f in range(0, W)]
        for f in range(0, W, 1+even_W):
            yield r, f
def _iter_sts4iter_st_solutions_mod_(W, r, f, /):
    for s in range(0, W):
        for t in range(0, W):
            if (r - (s*t*f + (s+t))) %W == 0:
                yield s, t
def iter_st_solutions_mod_(W, /, *, with_sts=False, with_st_mod_W=False):
    for r, f in _iter_rfs4iter_st_solutions_mod_(W):
        if with_st_mod_W:
            may_imay_st_mod_W = ...
        if with_sts:
            sts = []
        g = 0
        for s, t in _iter_sts4iter_st_solutions_mod_(W, r, f):
            if with_st_mod_W:
                st_mod_W = (s*t %W)
                if may_imay_st_mod_W is ...:
                    may_imay_st_mod_W = st_mod_W
                elif may_imay_st_mod_W is None:
                    pass
                elif not may_imay_st_mod_W == st_mod_W:
                    may_imay_st_mod_W = None
                else:
                    pass

            if with_sts:
                sts.append((s,t))
            g = gcd(g,gcd(W,s*t))

            if with_st_mod_W:
                if g == 1 and may_imay_st_mod_W is None:break
            else:
                if g == 1:break
        else:
            if with_st_mod_W:
                assert not (g == 1 and may_imay_st_mod_W is None)
            else:
                assert not g == 1
            if with_sts:
                ls = [sts]
            else:
                ls = []
            if with_st_mod_W:
                ls.append(may_imay_st_mod_W)
            yield (W, (r, f), g, *ls)

if __name__ == "__main__":
    pass
__all__


from script.primality_test____st_solutions import *
