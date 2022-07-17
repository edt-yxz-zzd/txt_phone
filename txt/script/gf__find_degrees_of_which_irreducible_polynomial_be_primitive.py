
r'''
e script/gf__find_degrees_of_which_irreducible_polynomial_be_primitive.py
-> {m <- [1..]| [sum_mu_mul m (p**) == phi(p**m-1)]}
    还有哪些？<<==除了 [p=2]时 的 梅森素数的比特数:[2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,2203,2281,3217,4253,4423,9689,9941,11213,19937,21701,23209,44497,86243,110503,132049,216091,756839,859433,1257787,1398269,2976221,3021377,6972593,13466917,20996011,24036583,25964951,30402457,32582657,37156667,42643801,43112609,57885161        ,74207281,77232917,82589933]

py script/gf__find_degrees_of_which_irreducible_polynomial_be_primitive.py --turnon_print_STDERR_degree --turnon_print_bad_degree -p 2 -m 1 -M 8 >> ~/my_tmp/out4py/gf__find_degrees_of_which_irreducible_polynomial_be_primitive.out.txt
view /sdcard/0my_files/tmp/out4py/gf__find_degrees_of_which_irreducible_polynomial_be_primitive.out.txt
py script/gf__find_degrees_of_which_irreducible_polynomial_be_primitive.py --turnon_print_STDERR_degree --turnon_print_bad_degree -o ~/my_tmp/out4py/gf__find_degrees_of_which_irreducible_polynomial_be_primitive.out.txt -f -p 2 -m 9 -M 100
py script/gf__find_degrees_of_which_irreducible_polynomial_be_primitive.py --turnon_print_STDERR_degree --turnon_print_bad_degree -o ~/my_tmp/out4py/gf__find_degrees_of_which_irreducible_polynomial_be_primitive.out.txt -f -p 2 -m 101 -M -1
#'''

from nn_ns.math_nn.Mobius import Mobius, Mu, Euler_totient_function, phi, iter_Mu#, II, phi
from nn_ns.math_nn.numbers.Mersenne_exponents import is_known_Mersenne_exponent

def _is_degree_ok(p, m, /):
    assert m > 0
    if 0:
        if p == 2 and is_known_Mersenne_exponent(m):
            return True
    return sum(mu_d* p**(m//d) for mu_d, d in iter_Mu(m)) == phi(p**m-1)
    #(p**m-1) 分解因子 很慢
    #2**m-1 先检查 梅森素数 比特数
    #    若是 比较 [sum_mu_mul m (p**) == phi(p**m-1)] 则 有 hint = gcd(p**m-1, sum_mu_mul m (p**)) 含因子:(p**m-1)/II all_prime_factors_of(p**m-1)
    #   若m是合数，则 [d<-all_divisors_of m] -> [hint=2**d-1]
    #cached... from file??
    #
    # 费马小定理:先随机检测 [a**(sum_mu_mul m (p**)) %(p**m-1) == 1] 若有反例，则 必然不相等
    #


def main(args=None, /):
    import argparse
    from itertools import count
    from seed.tiny import print_err, mk_fprint
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='find_degrees_of_which_irreducible_polynomial_be_primitive ~ GF(p**m)'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--turnon_print_STDERR_degree', action='store_true'
                        , default = False
                        , help='print degrees to stderr')
    parser.add_argument('--turnon_print_bad_degree', action='store_true'
                        , default = False
                        , help='print bad degrees to output file')
    parser.add_argument('-m', '--min_polynomial_degree', type=int, default=1
                        , help='min_polynomial_degree to start search; >=1')
    parser.add_argument('-M', '--max_polynomial_degree', type=int, default=1
                        , help='max_polynomial_degree to stop search; >=-1; -1 means +oo')
    parser.add_argument('-p', '--field_characteristic_prime', type=int, default=2
                        , help='field characteristic prime')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file #force to append instead of overwrite')

    args = parser.parse_args(args)
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'
    omode = 'at' if args.force else 'xt'

    p = args.field_characteristic_prime
    min_d = args.min_polynomial_degree
    max_d = args.max_polynomial_degree
    if not min_d >= 1: raise TypeError(min_d)
    if not max_d >= -1: raise TypeError(max_d)
    it = count(min_d) if max_d == -1 else iter(range(min_d, max_d+1))

    turnon_print_STDERR_degree = args.turnon_print_STDERR_degree
    turnon_print_bad_degree = args.turnon_print_bad_degree

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        fprint = mk_fprint(fout)

        for m in it:
            b = _is_degree_ok(p, m)
            ch = '-+'[b]
            s = f':{p}^{ch}{m}'
            if turnon_print_STDERR_degree:
                print_err(s)
            if b or turnon_print_bad_degree:
                fprint(s)
if __name__ == "__main__":
    main()



