r'''[[[
e script/tmp_search__q_pn__mod__F1F2_2.py
py script/tmp_search__q_pn__mod__F1F2_2.py

#]]]'''
__all__ = '''

    '''.split()
from seed.math.gcd import gcd
from nn_ns.math_nn.integer.mod import invmod

def f(F1_2, F2_2, /):
    #assert gcd(F1_2, F2_2) ==1
    assert F1_2 > 0
    assert F2_2 > 0
    s = invmod(F1_2, F2_2)
    t = (1-s*F1_2)//F2_2
    assert s*F1_2 + t*F2_2 ==1
    F1F2_4 = F1_2 * F2_2
    q_pn0 = (s*F1_2*(F2_2*2-1) + t*F2_2*1) %F1F2_4
    q_pns = {q_pn0, q_pn0+F1F2_4}
    q_pns = {q_pn for q_pn in q_pns if q_pn%(F1_2*2)==1 and q_pn%(F2_2*2)==(F2_2*2-1)}
    return q_pns

def search(N, /):
    Ls = {}
    for F1_2 in range(2, N):
        for F2_2 in range(2, N):
            if gcd(F1_2, F2_2) ==1:
                q_pns = f(F1_2, F2_2)
                L = len(q_pns)
                if L not in Ls:
                    Ls[L] = ((F1_2, F2_2), q_pns)
                    print(Ls[L])

search(1000)

