
'''
see:
    "[A001203]pi.txt"

"Pi Unleashed (2001).djvu"
    [page 77] 6. spigot algorithm
http://www.cut-the-knot.org/Curriculum/Algorithms/SpigotForPi.shtml
    Rabinowitz and Wagon's spigot algorithm
    # Each term shrinks the range by a factor of about a half, so more than three terms are required on average for every digit of the output.
    #
    pi = SUM 2^(k+1) * (k!)^2 / (2*k+1)! {k <- 0..}
        ==>>
            pi/2 = SUM k! / (2*k+1)!! {k <- 0..}
                = 1 + 1/3 + (1*2)/(3*5) + (1*2*3)/(3*5*7) + ...
                = 1 + 1/3 + 1/3*2/5 + 1/3*2/5*3/7 + ...
                = 1 + 1/3*(1 + 2/5*(1 + 3/7*(1 + ...)))
            pi = 2 + 1/3*(2 + 2/5*(2 + 3/7*(2 + ...)))
                ^^^      ^^^      ^^^      ^^^
        vs:
            pi = 3.14159...
                = 3 + 1/10*(1 + 1/10*(4 + 1/10*(1 + 1/10*(5 + 1/10*(9 + ...)))))
                 ^^^       ^^^       ^^^       ^^^       ^^^       ^^^
                = [3; 1,4,1,5,9...] of fixed-radix base [; 1/10, 1/10, 1/10, 1/10, 1/10...]
                = [2; 2,2,2,2...] of mixed-radix base [; 1/3,2/5,3/7...]
                # NOTE: 1 === [0; 9,9,9,9,9...] of fixed-radix base [; 1/10, 1/10, 1/10, 1/10, 1/10...]


'''

import sys
import traceback
import itertools

def Rabinowitz_and_Wagon_spigot_algorithm(
    num_decimal_digits_of_pi, *
    , verbose=False
    , raise_Exception=True
    ):
    it = _Rabinowitz_and_Wagon_spigot_algorithm(
        num_decimal_digits_of_pi
        ,verbose=verbose
        ,raise_Exception=raise_Exception
        )
    return itertools.islice(it, num_decimal_digits_of_pi)

def Rabinowitz_and_Wagon_spigot_algorithm(
    num_decimal_digits_of_pi, *
    , verbose=False
    , raise_Exception=True
    ):
    '''
time(Rabinowitz_and_Wagon_spigot_algorithm(n))
    = O(100/9*n*n*(div_ops<log2(400*n)>))
    = O(n^2*log(n)^2)
'''
    verbose = bool(verbose)
    raise_Exception = bool(raise_Exception)

    n = num_decimal_digits_of_pi
    L = 1 + 10*n//3
    A = [2] * L
        # for n decimal digits # n = 3 = len(3.14)
        # NOTE: not all correct digits of pi
        #   but: abs(result<n> - pi) <= 5*10^(-n)
        #
    head_digit = None # p
    num_nines_after_head_digit = None # nines
    new_base = 10
    num_output_digits = 0

    #Iteration: repeat until n decimal places have been output.
    while num_output_digits < n:
    #* Multiply with the new base.
        for i in range(L):
            A[i] *= 10
    #* Normalise.
        #for i in range(L, 0, -1):
        for i in reversed(range(1, L)):
            # A[i] == 10*r[i] + (q[i+1])*(i+1)
            # r[i] == (old A[i])%(2*i+1) <= 2*i
            # q[i] == (old A[i])//(2*i+1)
            # A[i] <= 10*2*i + q[i+1]*(i+1)
            # q[i] <= (10*2*i + q[i+1]*(i+1))//(2*i+1) <= 20
            # A[i] <= 20*(2*i+1) < 40*L <= 40 + 400*n/3 <= O(400*n)
            q, r = divmod(A[i], 2*i+1)
            A[i] = r
            A[i-1] += q*i

    #* Calculation of the next provisional digit of pi.
        q, r = divmod(A[0], 10)
        A[0] = r
    #* Correct the old provisional digits.
        assert 0 <= q <= 11
        if q < 9:
            #output
            if head_digit is None:
                assert num_nines_after_head_digit is None
            else:
                position = num_output_digits + 1 + num_nines_after_head_digit
                if position > n:
                    num_nines_after_head_digit = n - (num_output_digits+1)
                del position

                yield head_digit
                yield from [9]*num_nines_after_head_digit
                num_output_digits += 1 + num_nines_after_head_digit
            head_digit = q
            num_nines_after_head_digit = 0
        elif q == 9:
            if __debug__ and verbose:
                position = num_output_digits + 1 + num_nines_after_head_digit
                print(f'position={position}; pseudo 9', file=sys.stderr)
            num_nines_after_head_digit += 1
            if raise_Exception and num_nines_after_head_digit + num_output_digits >= n:
                raise Exception(f'too many 9s at num_decimal_digits_of_pi={n}!')
        elif q == 10:
            position = num_output_digits + 1 + num_nines_after_head_digit
            if __debug__ and verbose:
                print(f'position={position}; pseudo 10', file=sys.stderr)
            if position > n:
                num_nines_after_head_digit = n - (num_output_digits+1)
            del position

            head_digit += 1
            yield head_digit
            yield from [0]*num_nines_after_head_digit # 0 not 9
            num_output_digits += 1 + num_nines_after_head_digit
            head_digit = 0
            num_nines_after_head_digit = 0
        else:
            raise logic-error

############################################################
# from https://oeis.org/A000796
pi_decimal_digits__from_A000796 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3, 0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7, 0, 6, 7, 9, 8, 2, 1, 4]
############################################################
############################################################
pi_decimal_digits__len400 = list(Rabinowitz_and_Wagon_spigot_algorithm(400))
assert len(pi_decimal_digits__len400) == 400 >= len(pi_decimal_digits__from_A000796)
assert pi_decimal_digits__len400[:len(pi_decimal_digits__from_A000796)] == pi_decimal_digits__from_A000796

def _t1():
    ls = list(Rabinowitz_and_Wagon_spigot_algorithm(len(pi_decimal_digits__from_A000796)))
    assert ls == pi_decimal_digits__from_A000796


def _calc_and_show(n, *, verbose, **kwargs):
    print(f'_calc_and_show({n})', file=sys.stderr)
    it = Rabinowitz_and_Wagon_spigot_algorithm(n, verbose=verbose, **kwargs)
    ls = []
    for i, digit in enumerate(it):
        if verbose: print(i, digit)
        ls.append(digit)
    print(ls)
    return ls


def _t2(*, verbose, **kwargs):
    rngs = [range(6), range(29, 36), range(41, 49), range(359, 365)]
    for rng in rngs:
      for n in rng:
        assert n <= 400
        try:
            ls = _calc_and_show(n, verbose=False, **kwargs)
        except Exception:
            traceback.print_exc()
            input(f'>>> n=={n}... to be continue')
            continue
        try:
            assert ls == pi_decimal_digits__len400[:n]
        except AssertionError:
            traceback.print_exc()
            input(f'>>> n=={n}... to be continue')
            continue

    '''
?:
    ...
    position=30; pseudo 9
    position=32; pseudo 10
    ...
    position=42; pseudo 9
    position=44; pseudo 9
    position=45; pseudo 9
    ...
    position=360; pseudo 9
    position=361; pseudo 10

    ########################
    # _t2() ==>> 'xA' | 'yA':
    #   turn off Exception('too many 9s at ...')
    #       i.e. raise_Exception=False
    #   if AssertionError, then mark "xA", else "yA"
    # _t2() ==>> 'xE' | 'yE':
    #   turn on Exception('too many 9s at ...')
    #       i.e. raise_Exception=True
    #   if Exception, then mark "xE", else "yE"
    0 3
    1 1
    2 4
    3 1
    4 5
    ...
    28 2
    29 7
    30 9 # yA xE
    31 5
    32 0 # yA yE
    33 2
    ...
    40 1
    41 6
    42 9 # yA xE
    43 3
    44 9 # yA xE
    45 9 # yA xE
    46 3
    47 7
    ...
    357 0
    358 3
    359 6
    360 0 # yA xE
    361 0 # yA yE
    362 1
    363 1
    ...

Rabinowitz_and_Wagon_spigot_algorithm(400)
position=4; pseudo 9
position=11; pseudo 9
position=13; pseudo 9
position=29; pseudo 9
position=31; pseudo 10
position=37; pseudo 9
position=41; pseudo 9
position=43; pseudo 9
position=44; pseudo 9
position=54; pseudo 9
position=57; pseudo 9
position=61; pseudo 9
position=78; pseudo 9
position=79; pseudo 9
position=84; pseudo 10
position=99; pseudo 9
position=121; pseudo 9
position=128; pseudo 9
position=143; pseudo 9
position=166; pseudo 10
position=168; pseudo 9
position=179; pseudo 9
position=186; pseudo 9
position=189; pseudo 9
position=192; pseudo 9
position=198; pseudo 9
position=207; pseudo 9
position=213; pseudo 9
position=244; pseudo 10
position=246; pseudo 9
position=248; pseudo 9
position=258; pseudo 9
position=283; pseudo 9
position=290; pseudo 10
position=293; pseudo 9
position=306; pseudo 10
position=327; pseudo 9
position=330; pseudo 9
position=335; pseudo 9
position=340; pseudo 9
position=352; pseudo 9
position=356; pseudo 10
position=359; pseudo 9
position=360; pseudo 10
position=387; pseudo 9
position=390; pseudo 9
position=398; pseudo 9
'''
if __name__ == '__main__':
    import sys
    _, n = sys.argv
    n = int(n)
    _calc_and_show(n, verbose=True)

    ans = input('>>> ... to be continue (Yes/No)?')
    ans = ans.upper()
    if ans in ('Y', 'YES'):
        _t1()
        _t2(verbose=False, raise_Exception=False)
        _t2(verbose=False, raise_Exception=True)

