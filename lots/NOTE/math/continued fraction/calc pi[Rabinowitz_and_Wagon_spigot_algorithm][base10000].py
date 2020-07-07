'''
calc pi[Rabinowitz_and_Wagon_spigot_algorithm][base10000]
"Pi Unleashed (2001).djvu"
    [page 77] 6. spigot algorithm

    pi = SUM 2^(k+1) * (k!)^2 / (2*k+1)! {k <- 0..}
        ==>>
            pi/2 = SUM k! / (2*k+1)!! {k <- 0..}
                = 1 + 1/3 + (1*2)/(3*5) + (1*2*3)/(3*5*7) + ...
                = 1 + 1/3 + 1/3*2/5 + 1/3*2/5*3/7 + ...
                = 1 + 1/3*(1 + 2/5*(1 + 3/7*(1 + ...)))
            pi = 2 + 1/3*(2 + 2/5*(2 + 3/7*(2 + ...)))
                ^^^      ^^^      ^^^      ^^^
            1000*pi = 2000 + 1/3*(2000 + 2/5*(2000 + 3/7*(2000 + ...)))
                      ^^^^        ^^^^        ^^^^        ^^^^
        vs:
            pi = 3.14159...
                = 3 + 1/10*(1 + 1/10*(4 + 1/10*(1 + 1/10*(5 + 1/10*(9 + ...)))))
                 ^^^       ^^^       ^^^       ^^^       ^^^       ^^^
                = [3; 1,4,1,5,9...] of fixed-radix base [; 1/10, 1/10, 1/10, 1/10, 1/10...]
                = [2; 2,2,2,2...] of mixed-radix base [; 1/3,2/5,3/7...]
                # NOTE: 1 === [0; 9,9,9,9,9...] of fixed-radix base [; 1/10, 1/10, 1/10, 1/10, 1/10...]
            1000*pi = [2000; 2000,2000,2000,2000...] of mixed-radix base [; 1/3,2/5,3/7...]




/*
* Spigot program for pi to NDIGITS decimals
* 4 digits per loop
* Expanded version
* Thanks to Dik T. Winter and Achim Flammenkamp.
*/
#include <stdio.h>
#include <stdlib.h>
#define NDIGITS 15000           /* max. digits to compute */
#define LEN (NDIGITS/4+l)*14    /* nec. array length */
long a[LEN];                    /* array of 4 digit-decimals*/
long b;                         /* nominator prev. base */
long c = LEN;                   /* index */
long d;                         /* accumulator and carry */
long e = 0;                     /* save prev. 4 digits */
long f = 10000;                 /* new base, 4 dec. digits */
long g;                         /* denom prev. base */
long h = 0;                     /* init switch */

int main(void)
{
    for ( ; (b=c-=14) > 0; )    /* outer loop:4 digits/loop*/
    {
        for (; --b > 0; )       /* inner loop: radix conv */
        {
            d *= b;                     /* acc *= nom. prev base */
            if (h == 0) d += 2000 * f;  /* first outer loop */
            else        d += a[b] * f;  /* non-first outer loop */

            g=b+b-l;                    /* denom prev. base */
            a[b] = d % g;
            d /= g;                     /* save carry */
        }
        h = printf ("%04ld", e+d/f);    /* print prev 4 digits */
        d = e = d%f;                    /* save current 4 digits */
                                        /* assure a small enough d */
    }
    return 0;
}

'''


import sys


def str_Rabinowitz_and_Wagon_spigot_algorithm__base10000(
    num_decimal_digits_of_pi, *, verbose=False):
    for _4digit in Rabinowitz_and_Wagon_spigot_algorithm__base10000(num_decimal_digits_of_pi, verbose=verbose):
        yield f'{_4digit:0>4}'
def Rabinowitz_and_Wagon_spigot_algorithm__base10000(
    num_decimal_digits_of_pi, *, verbose=False):
    '''
time(Rabinowitz_and_Wagon_spigot_algorithm(n))
    = O((n/4 * n*7/2) * div_ops<log2(160000*max(250,n))>)
    = O(n^2 * div_ops<log2(n)>)
    = O(n^2 * log(n)^2)
'''
    verbose = bool(verbose)
    n = num_decimal_digits_of_pi
    if n % 4 != 0: raise ValueError

    L = (n//4+1)*14
    A = [0]*L
    accumulator = 0
    prev_4_digits = 0
    new_base = 10000
    is_first_outer_loop = True

    #for c in range(L-14, 0, -14):
    for c in reversed(range(14, L, 14)):
        for b in reversed(range(1, c)):
            accumulator *= b
            tmp = 2000 if is_first_outer_loop else A[b]
            accumulator += tmp * new_base

            # accumulator[b] = accumulator[b+1]/(2*b+1) * b + 10000 * (2000|A[b])
            #   < accumulator[b+1]/2 + 10000 * max(2000, A[b])
            # ACC = ACC/2 + MAX ==>> ACC = 2*MAX
            # accumulator < 20000 * max(2000, *A)
            # A[b] <= 2*b-1 < 2*c <= 2*(L-14) = 7*n
            # accumulator < 20000 * max(2000, 7*n) < 160000 * max(250, n)
            carry, A[b] = divmod(accumulator, (2*b-1))
            accumulator = carry
        is_first_outer_loop = False
        q, r = divmod(accumulator, new_base)
        yield prev_4_digits + q                 # output prev 4 digits
        accumulator = prev_4_digits = r         # save current 4 digits

############################################################
# from https://oeis.org/A000796
pi_decimal_digits__from_A000796 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9, 8, 2, 1, 4]
assert len(pi_decimal_digits__from_A000796) == 105
str_pi_decimal_digits__from_A000796 = ''.join(map(str, pi_decimal_digits__from_A000796))
assert len(str_pi_decimal_digits__from_A000796) == len(pi_decimal_digits__from_A000796)
str104_pi_decimal_digits__from_A000796 = str_pi_decimal_digits__from_A000796[:104]
assert len(str104_pi_decimal_digits__from_A000796) == 104
assert len(str104_pi_decimal_digits__from_A000796)%4 == 0
############################################################
############################################################

def _calc_and_show(n, *, verbose, **kwargs):
    print(f'_calc_and_show({n})', file=sys.stderr)
    it = str_Rabinowitz_and_Wagon_spigot_algorithm__base10000(n, verbose=verbose, **kwargs)
    ls = []
    for i, _4digit in enumerate(it):
        if verbose: print(i, _4digit)
        ls.append(_4digit)
    print(ls)
    assert all(len(_4digit) == 4 for _4digit in ls)

    s = ''.join(ls)
    print(s)
    try:
        assert len(s) == n
    except AssertionError:
        print(f'n={n} != {len(s)}=len(s)')
        raise

    L = min(n, len(str_pi_decimal_digits__from_A000796))
    assert s[:L] == str_pi_decimal_digits__from_A000796[:L]
    return s

assert _calc_and_show(104, verbose=False) == str104_pi_decimal_digits__from_A000796

if __name__ == '__main__':
    _, n = sys.argv
    n = int(n)
    _calc_and_show(n, verbose=True)

    ans = input('>>> ... to be continue (Yes/No)?')
    ans = ans.upper()
    if ans in ('Y', 'YES'):
        prev_s = ''
        for i in range(1000):
            n = 4*i
            s = _calc_and_show(n, verbose=False)
            assert prev_s == s[:len(prev_s)]
            prev_s = s


