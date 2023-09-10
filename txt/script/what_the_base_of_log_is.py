
r'''[[[
e script/what_the_base_of_log_is.py
py script/what_the_base_of_log_is.py

pseudoprime
strong pseudoprime

probable-prime (PRP)
strong probable-prime (SPRP)
  b-SPRP
Extended Riemann Hypothesis (ERH)

[n :: int]:
    [is_strong_pseudoprime_(b;n) =[def]= [[n > 0][n%2==1][(e,t) :=> [[e,t :: pint][t%2==1][t*2**e == n-1]]][[b**t %n == +1]or[?[s :<- [0..<e]] -> [(b**t)**(2**s) %n == -1]]]]]
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(n, 2*(log n)**2)]] -> [is_strong_pseudoprime_(b;n)]]]]

[log n === log_(b;n)] which 'b'? 2,e,10
    py.math.log(x, [base=math.e])

[[x >= 120] -> [x**(1 - log log x/log 37) < (log x)**3/(log 3 * log 4)]]
==>> [log =!= log10]
[e ~= 2.718281828459045]
[log2(e) ~= 1.4426950408889634]
[ln(2) ~= 0.6931471805599453]
[e > 2]
[log2(e) > 1]
[[x > 1] -> [ln(x) == log2(x)/log2(e) < log2(x)]]

[[x > 1] -> [ln(x) < log2(x)]]
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(n, 2*(log n)**2)]] -> [is_strong_pseudoprime_(b;n)]]]]
==>>:
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(n, 2*(log2 n)**2)]] -> [is_strong_pseudoprime_(b;n)]]]]
==>>:
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(n, 2*(ceil_log2 n)**2)]] -> [is_strong_pseudoprime_(b;n)]]]]

#]]]'''#'''

from math import log as ln, log2 as lb, log10 as lg
import math
import itertools

def find_min_n_satisfy_(f, n0, /):
    for n in itertools.count(n0):
        if f(n):
            return n
def find_ns_satisfy_(f, n0, nt, /):
    return [n for n in range(n0, nt) if f(n)]

def _mk_f(logX_, /):
    def f(x, /):
        #[x**(1 - log log x/log 37) < (log x)**3/(log 3 * log 4)]
        return math.pow(x, 1.0-logX_(logX_(x))/logX_(37)) < math.pow(logX_(x), 3)/(logX_(3)*logX_(4))
    return f


def __():
    for logX_ in [ln, lb, lg]:
        f = _mk_f(logX_)
        n = find_min_n_satisfy_(f, 2)
        print(logX_, ns)
def __():
    for logX_ in [ln, lb, lg]:
        f = _mk_f(logX_)
        ns = find_ns_satisfy_(f, 100, 123)
        print(logX_, ns)
        r'''[[[
<built-in function log> [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
<built-in function log2> [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
<built-in function log10> []
不是10

        #]]]'''#'''
__()
