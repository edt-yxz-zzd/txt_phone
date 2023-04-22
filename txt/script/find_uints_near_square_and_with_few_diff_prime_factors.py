#__all__:goto
r'''[[[
e script/find_uints_near_square_and_with_few_diff_prime_factors.py
TODO:靠近平方数且素因子很少的数
  例:x**2+-1==2**y * 3**z
    * [x**2+1 == ???]:
    * [x**2-1 == (x-1)*(x+1)]:
      * [x奇]:
        [2==gcd(x-1,x+1)]
        [d :<- {-1,+1}]
        [x+d==2**(y-1)]
        [x-d==2*3**z]
        [x-d==x+d-2*d==2**(y-1)-2*d]
        [2*3**z==2**(y-1)-2*d]
        [3**z==2**(y-2)-d]
        * [9==8+1]:
          [z==2][y==5][d==-1]
          [x==17]
          [17**2-1==288==2**5*3**2]
  ===方法:
  * 指定偏移量:-1/+1
  * 指定允许的素因子:[2,3]
  * 指定素因子数目的最大值:2



=====
py -m nn_ns.app.adhoc_argparser__main__call8module   script.find_uints_near_square_and_with_few_diff_prime_factors   ,stable_repr.main__using_hints_lt  --max_num_prime_factors=-1 --legal_prime_factors_lt=10 --square_roots='range(1000)' --offset6square=-1
(2, -1, 3, 1, {3: 1})
(3, -1, 8, 1, {2: 3})
(4, -1, 15, 2, {3: 1, 5: 1})
(5, -1, 24, 2, {2: 3, 3: 1})
(6, -1, 35, 2, {5: 1, 7: 1})
(7, -1, 48, 2, {2: 4, 3: 1})
(8, -1, 63, 2, {3: 2, 7: 1})
(9, -1, 80, 2, {2: 4, 5: 1})
(11, -1, 120, 3, {2: 3, 3: 1, 5: 1})
(13, -1, 168, 3, {2: 3, 3: 1, 7: 1})
(15, -1, 224, 2, {2: 5, 7: 1})
(17, -1, 288, 2, {2: 5, 3: 2})
(19, -1, 360, 3, {2: 3, 3: 2, 5: 1})
(26, -1, 675, 2, {3: 3, 5: 2})
(29, -1, 840, 4, {2: 3, 3: 1, 5: 1, 7: 1})
(31, -1, 960, 3, {2: 6, 3: 1, 5: 1})
(41, -1, 1680, 4, {2: 4, 3: 1, 5: 1, 7: 1})
(49, -1, 2400, 3, {2: 5, 3: 1, 5: 2})
(55, -1, 3024, 3, {2: 4, 3: 3, 7: 1})
(71, -1, 5040, 4, {2: 4, 3: 2, 5: 1, 7: 1})
(97, -1, 9408, 3, {2: 6, 3: 1, 7: 2})
(99, -1, 9800, 3, {2: 3, 5: 2, 7: 2})
(127, -1, 16128, 3, {2: 8, 3: 2, 7: 1})
(161, -1, 25920, 3, {2: 6, 3: 4, 5: 1})
(244, -1, 59535, 3, {3: 5, 5: 1, 7: 2})
(251, -1, 63000, 4, {2: 3, 3: 2, 5: 3, 7: 1})
(449, -1, 201600, 4, {2: 7, 3: 2, 5: 2, 7: 1})

=====
py -m nn_ns.app.adhoc_argparser__main__call8module   script.find_uints_near_square_and_with_few_diff_prime_factors   ,stable_repr.main__using_hints_lt  --max_num_prime_factors=-1 --legal_prime_factors_lt=6 --square_roots='range(1000)' --offset6square=-1
(2, -1, 3, 1, {3: 1})
(3, -1, 8, 1, {2: 3})
(4, -1, 15, 2, {3: 1, 5: 1})
(5, -1, 24, 2, {2: 3, 3: 1})
(7, -1, 48, 2, {2: 4, 3: 1})
(9, -1, 80, 2, {2: 4, 5: 1})
(11, -1, 120, 3, {2: 3, 3: 1, 5: 1})
(17, -1, 288, 2, {2: 5, 3: 2})
(19, -1, 360, 3, {2: 3, 3: 2, 5: 1})
(26, -1, 675, 2, {3: 3, 5: 2})
(31, -1, 960, 3, {2: 6, 3: 1, 5: 1})
(49, -1, 2400, 3, {2: 5, 3: 1, 5: 2})
(161, -1, 25920, 3, {2: 6, 3: 4, 5: 1})
=====
(11, -1, 120, 3, {2: 3, 3: 1, 5: 1})
(17, -1, 288, 2, {2: 5, 3: 2})
(19, -1, 360, 3, {2: 3, 3: 2, 5: 1})
(31, -1, 960, 3, {2: 6, 3: 1, 5: 1})
(49, -1, 2400, 3, {2: 5, 3: 1, 5: 2})




=====
py -m nn_ns.app.adhoc_argparser__main__call8module   script.find_uints_near_square_and_with_few_diff_prime_factors   ,stable_repr.main__using_hints_lt  --max_num_prime_factors=-1 --legal_prime_factors_lt=10 --square_roots='range(10**5)' --offset6square=1
    『10**5』与下面『1000』结果相同
py -m nn_ns.app.adhoc_argparser__main__call8module   script.find_uints_near_square_and_with_few_diff_prime_factors   ,stable_repr.main__using_hints_lt  --max_num_prime_factors=-1 --legal_prime_factors_lt=10 --square_roots='range(10**3)' --offset6square=1
(0, 1, 1, 0, {})
(1, 1, 2, 1, {2: 1})
(2, 1, 5, 1, {5: 1})
(3, 1, 10, 2, {2: 1, 5: 1})
(7, 1, 50, 2, {2: 1, 5: 2})


=====
py -m nn_ns.app.adhoc_argparser__main__call8module   script.find_uints_near_square_and_with_few_diff_prime_factors   ,stable_repr.main__using_hints_lt  --max_num_prime_factors=4 --legal_prime_factors_lt=50 --square_roots='range(1000)' --offset6square=1
(0, 1, 1, 0, {})
(1, 1, 2, 1, {2: 1})
(2, 1, 5, 1, {5: 1})
(3, 1, 10, 2, {2: 1, 5: 1})
(4, 1, 17, 1, {17: 1})
(5, 1, 26, 2, {2: 1, 13: 1})
(6, 1, 37, 1, {37: 1})
(7, 1, 50, 2, {2: 1, 5: 2})
(8, 1, 65, 2, {5: 1, 13: 1})
(9, 1, 82, 2, {2: 1, 41: 1})
(12, 1, 145, 2, {5: 1, 29: 1})
(13, 1, 170, 3, {2: 1, 5: 1, 17: 1})
(17, 1, 290, 3, {2: 1, 5: 1, 29: 1})
(18, 1, 325, 2, {5: 2, 13: 1})
(21, 1, 442, 3, {2: 1, 13: 1, 17: 1})
(31, 1, 962, 3, {2: 1, 13: 1, 37: 1})
(32, 1, 1025, 2, {5: 2, 41: 1})
(38, 1, 1445, 2, {5: 1, 17: 2})
(41, 1, 1682, 2, {2: 1, 29: 2})
(43, 1, 1850, 3, {2: 1, 5: 2, 37: 1})
(47, 1, 2210, 4, {2: 1, 5: 1, 13: 1, 17: 1})
(57, 1, 3250, 3, {2: 1, 5: 3, 13: 1})
(68, 1, 4625, 2, {5: 3, 37: 1})
(70, 1, 4901, 2, {13: 2, 29: 1})
(73, 1, 5330, 4, {2: 1, 5: 1, 13: 1, 41: 1})
(99, 1, 9802, 3, {2: 1, 13: 2, 29: 1})
(117, 1, 13690, 3, {2: 1, 5: 1, 37: 2})
(132, 1, 17425, 3, {5: 2, 17: 1, 41: 1})
(157, 1, 24650, 4, {2: 1, 5: 2, 17: 1, 29: 1})
(191, 1, 36482, 4, {2: 1, 17: 1, 29: 1, 37: 1})
(239, 1, 57122, 2, {2: 1, 13: 4})
(268, 1, 71825, 3, {5: 2, 13: 2, 17: 1})
(278, 1, 77285, 4, {5: 1, 13: 1, 29: 1, 41: 1})
(302, 1, 91205, 4, {5: 1, 17: 1, 29: 1, 37: 1})
(307, 1, 94250, 4, {2: 1, 5: 3, 13: 1, 29: 1})
(327, 1, 106930, 4, {2: 1, 5: 1, 17: 2, 37: 1})
(378, 1, 142885, 3, {5: 1, 17: 1, 41: 2})
(829, 1, 687242, 4, {2: 1, 17: 2, 29: 1, 41: 1})
(882, 1, 777925, 3, {5: 2, 29: 2, 37: 1})

=====
py -m nn_ns.app.adhoc_argparser__main__call8module   script.find_uints_near_square_and_with_few_diff_prime_factors   ,stable_repr.main__using_hints_lt  --max_num_prime_factors=-1 --legal_prime_factors_lt=20 --square_roots='range(1000)' --offset6square=1
(0, 1, 1, 0, {})
(1, 1, 2, 1, {2: 1})
(2, 1, 5, 1, {5: 1})
(3, 1, 10, 2, {2: 1, 5: 1})
(4, 1, 17, 1, {17: 1})
(5, 1, 26, 2, {2: 1, 13: 1})
(7, 1, 50, 2, {2: 1, 5: 2})
(8, 1, 65, 2, {5: 1, 13: 1})
(13, 1, 170, 3, {2: 1, 5: 1, 17: 1})
(18, 1, 325, 2, {5: 2, 13: 1})
(21, 1, 442, 3, {2: 1, 13: 1, 17: 1})
(38, 1, 1445, 2, {5: 1, 17: 2})
(47, 1, 2210, 4, {2: 1, 5: 1, 13: 1, 17: 1})
(57, 1, 3250, 3, {2: 1, 5: 3, 13: 1})
(239, 1, 57122, 2, {2: 1, 13: 4})
(268, 1, 71825, 3, {5: 2, 13: 2, 17: 1})

=====
py -m nn_ns.app.adhoc_argparser__main__call8module   script.find_uints_near_square_and_with_few_diff_prime_factors   ,stable_repr.main__using_hints_lt  --max_num_prime_factors=-1 --legal_prime_factors_lt=20 --square_roots='range(1000)' --offset6square=1 --factor_ge2max_num_factors_ge='{6:1}'
(0, 1, 1, 0, {})
(1, 1, 2, 1, {2: 1})
(2, 1, 5, 1, {5: 1})
(3, 1, 10, 2, {2: 1, 5: 1})
(4, 1, 17, 1, {17: 1})
(5, 1, 26, 2, {2: 1, 13: 1})
(7, 1, 50, 2, {2: 1, 5: 2})
(8, 1, 65, 2, {5: 1, 13: 1})
(13, 1, 170, 3, {2: 1, 5: 1, 17: 1})
(18, 1, 325, 2, {5: 2, 13: 1})
(57, 1, 3250, 3, {2: 1, 5: 3, 13: 1})

=====
(13, 1, 170, 3, {2: 1, 5: 1, 17: 1})
(18, 1, 325, 2, {5: 2, 13: 1})
(57, 1, 3250, 3, {2: 1, 5: 3, 13: 1})
=====
(11, -1, 120, 3, {2: 3, 3: 1, 5: 1})
(17, -1, 288, 2, {2: 5, 3: 2})
(19, -1, 360, 3, {2: 3, 3: 2, 5: 1})
(31, -1, 960, 3, {2: 6, 3: 1, 5: 1})
(49, -1, 2400, 3, {2: 5, 3: 1, 5: 2})
=====







script.find_uints_near_square_and_with_few_diff_prime_factors
py -m nn_ns.app.debug_cmd   script.find_uints_near_square_and_with_few_diff_prime_factors
py -m nn_ns.app.doctest_cmd script.find_uints_near_square_and_with_few_diff_prime_factors:f -v
from script.find_uints_near_square_and_with_few_diff_prime_factors import f
#]]]'''
__all__ = r'''
'''.split()#'''
__all__


from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
from nn_ns.math_nn.prime2 import primes_lt

def is_square_root_ok4uint_near_square_and_with_few_diff_prime_factors(offset6square, max_num_prime_factors, legal_prime_factors, square_root, /):
    u = square_root**2 +offset6square
    (f2e, unfactored_part) = semi_factor_pint_via_trial_division(legal_prime_factors, u)
    return unfactored_part==1










def iter_uints_near_square_and_with_few_diff_prime_factors_ex(offset6square, legal_prime_factors, factor_ge2max_num_factors_ge, min_num_prime_factors, max_num_prime_factors, square_roots, /):
    '-> (square_root, offset6square, square_root**2 +offset6square, len(factor2exp), factor2exp)'
    if max_num_prime_factors < 0:
        max_num_prime_factors = len(legal_prime_factors)
    for square_root in square_roots:
        u = square_root**2 +offset6square
        if u < 1:continue
        (f2e, unfactored_part) = semi_factor_pint_via_trial_division(legal_prime_factors, u)
        if unfactored_part==1 and (min_num_prime_factors <= len(f2e) <= max_num_prime_factors):
            if factor_ge2max_num_factors_ge and not all(sum(e for factor, e in f2e.items() if factor_ge <= factor) <= max_num_factors_ge for factor_ge, max_num_factors_ge in factor_ge2max_num_factors_ge.items()):
                continue
            yield (square_root, offset6square, u, len(f2e), f2e)
def main__using_hints(*, offset6square, legal_prime_factors, square_roots, min_num_prime_factors=-1, max_num_prime_factors=-1, factor_ge2max_num_factors_ge=None):
    return iter_uints_near_square_and_with_few_diff_prime_factors_ex(offset6square, legal_prime_factors, factor_ge2max_num_factors_ge, min_num_prime_factors, max_num_prime_factors, square_roots)
def main__using_hints_lt(*, offset6square, legal_prime_factors_lt, square_roots, min_num_prime_factors=-1, max_num_prime_factors=-1, factor_ge2max_num_factors_ge=None):
    legal_prime_factors = primes_lt(legal_prime_factors_lt)
    return iter_uints_near_square_and_with_few_diff_prime_factors_ex(offset6square, legal_prime_factors, factor_ge2max_num_factors_ge, min_num_prime_factors, max_num_prime_factors, square_roots)

if __name__ == "__main__":
    pass
