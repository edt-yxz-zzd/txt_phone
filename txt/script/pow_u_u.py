#__all__:goto
r'''[[[
e script/pow_u_u.py

script.pow_u_u
py -m nn_ns.app.debug_cmd   script.pow_u_u -x # -off_defs
py -m nn_ns.app.doctest_cmd script.pow_u_u:__doc__ -ht # -ff -df
#######

[[
view others/数学/the_function-pow_u_u.txt
[(1+x)**(1+x) == sum[Q[j]/j!*x**j | [j:<-[0..]]]]
    [j:<-[1..]]:
        [Q[j] == Q[j-1] - sum[Q[j-1-k]*(-1)**k*(k-1)!*C(j-1;k) | [k:<-[1..<j]]]]
        [Q[j] == Q[j-1] + sum[Q[i]*(-1)**(j-i)*(j-2-i)!*C(j-1;i) | [i:<-[0..<j-1]]]]
    [Q[0] == 0!*c[0] == 1]
    [Q[1] == 1!*c[1] == 1]
    [Q[2] == 2!*c[2] == 2]
]]


'#'; __doc__ = r'#'
>>>



DONE:oeis:
    1,1,2,3,8,10,54,-42,944,-5112,47160,-419760
    @20260117
    view others/数学/the_function-pow_u_u.txt
        view ../../python3_src/nn_ns/math_nn/numbers/b005727-Lehmer_Comtet_numbers-Nth_derivative_of_pow_u_u_at_u_EQ_1__fst_401.txt
[[
py_adhoc_call   script.pow_u_u   ,22:枚举冫阶乘后泰勒系数纟自幂方函数扌
1
1
2
3
8
10
54
-42
944
-5112
47160
-419760
4297512
-47607144
575023344
-7500202920
105180931200
-1578296510400
25238664189504
-428528786243904
7700297625889920
-146004847062359040

]]
[[
py_adhoc_call   script.pow_u_u   @eval_powUU_ =11 =0.5 +ex
    (1.5, (1.8371173070873836, 1.8371209038628473), 3.5967754636878624e-06)
    #
    1.8371209038628473
    ^^^^^^zyyyxxxxxxx
py_adhoc_call   script.pow_u_u   @eval_powUU_ =12 =0.5
    1.8371157691592261
    ^^^^^^^yyyxxxxxxx
py_adhoc_call   script.pow_u_u   @eval_powUU_ =22 =0.5
    1.837117306662609
    ^^^^^^^^^^xxxxxxx

<<==:
py_adhoc_call   script.pow_u_u   ,22:iter_eval_powUU_  =0.5
(1, -0.8371173070873836)
(2, -0.33711730708738363)
(3, -0.08711730708738363)
(4, -0.024617307087383633)
(5, -0.0037839737540503737)
(6, -0.001179807087383633)
(7, -7.932087383588637e-06)
(8, -7.303625405041814e-05)
(9, 1.8419599124186448e-05)
(10, -9.094661788333624e-06)
(11, 3.5967754636878624e-06)
(12, -1.5379281574912085e-06)
(13, 6.524554772013857e-07)
(14, -2.808028387590866e-07)
(15, 1.2178178598887257e-07)
(16, -5.325263696676075e-08)
(17, 2.345480254462018e-08)
(18, -1.0399210381706325e-08)
(19, 4.638628592346095e-09)
(20, -2.08053885231152e-09)
(21, 9.379039767054564e-10)
(22, -4.2477465989065877e-10)

]]


from script.pow_u_u import *
]]]'''#'''
__all__ = r'''
枚举冫阶乘后泰勒系数纟自幂方函数扌
    截取冫阶乘后泰勒系数纟自幂方函数扌
eval_powUU_
    iter_eval_powUU_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice, count
from seed.tiny_.check import check_type_is, check_int_ge
from math import comb as C, factorial
___end_mark_of_excluded_global_names__0___ = ...


assert C(4, 2) == 6, C(4, 2)
def 枚举冫阶乘后泰勒系数纟自幂方函数扌(Qs=[1], /):
    yield from Qs
    while 1:
        j = len(Qs)
        # [Q[j] == Q[j-1] + sum[Q[i]*(-1)**(j-i)*(j-2-i)!*C(j-1;i) | [i:<-[0..<j-1]]]]
        Qj = Qs[j-1] +sum(Qs[i]*(-1)**(j-i) * factorial(j-2-i) * C(j-1,i) for i in range(j-1))
        Qs.append(Qj)
        yield Qj

def 截取冫阶乘后泰勒系数纟自幂方函数扌(L, /):
    return tuple(islice(枚举冫阶乘后泰勒系数纟自幂方函数扌(), 0, L))

def eval_powUU_(L, x, /, *, ex=False):
    'eval("(1+x)**(1+x)") as sum[Q[j]/j!*x**j | [j:<-[0..<L]]]'
    check_int_ge(1, L)
    assert 0 < x < 1
    Qs = 截取冫阶乘后泰勒系数纟自幂方函数扌(L)
    v = 0.0
    for j in reversed(range(1, L)):
        #bug:v = Qs[j]/factorial(j) *x *(1.0 +v)
        v = (Qs[j] +v) *x/j
    j = 0
    777;v = (Qs[j] +v)/factorial(j)
    if ex:
        u = (1.0+x)
        y = u**u
        return (u, (y, v), v-y)
    return v
def iter_eval_powUU_(x, /):
    (u, (y, v), diff_v_y) = eval_powUU_(L:=1, x, ex=True)
    777;yield (L, diff_v_y)
    for L in count(2):
        v = eval_powUU_(L, x)
        yield (L, v-y)



__all__
from script.pow_u_u import *
