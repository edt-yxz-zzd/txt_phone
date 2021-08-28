
r'''
py -m nn_ns.app.show_factor_uint
cp -T /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py /sdcard/0my_files/git_repos/python3_src/nn_ns/app/show_factor_uint.py
=================================
=================================
=================================
e script/factor_uint.py
    list {factor:exp} of uint coprime to given primes

py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 5 --uint_le 100 > /sdcard/0my_files/tmp/out4py/factor_uint.py.100_5.out.txt
    #result see below
    #8/30: 8 coprimes per 30 uint
    #   8/30 = (1-1/2)*(1-1/3)*(1-1/5) = 4/15
py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 0 --uint_le 10000 > /sdcard/0my_files/tmp/out4py/factor_uint.py.10000_0.out.txt
du -h /sdcard/0my_files/tmp/out4py/factor_uint.py.10000_0.out.txt
    duM /sdcard/0my_files/tmp/out4py/factor_uint.py.10000_0.out.txt
    duM /sdcard/0my_files/unzip/e_book/素数表/primes1.txt
$ du -h /sdcard/0my_files/tmp/out4py/factor_uint.py.10000_0.out.txt
184K    /sdcard/0my_files/tmp/out4py/factor_uint.py.10000_0.out.txt
$
65536=2**16
py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 0 --uint_le 65536 > /sdcard/0my_files/tmp/out4py/factor_uint.py.65536_0.out.txt
du -h /sdcard/0my_files/tmp/out4py/factor_uint.py.65536_0.out.txt
$ du -h /sdcard/0my_files/tmp/out4py/factor_uint.py.65536_0.out.txt
1.4M    /sdcard/0my_files/tmp/out4py/factor_uint.py.65536_0.out.txt
$

py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 0 --uint_le 100000 > /sdcard/0my_files/tmp/out4py/factor_uint.py.100000_0.out.txt
du -h /sdcard/0my_files/tmp/out4py/factor_uint.py.100000_0.out.txt
$ du -h /sdcard/0my_files/tmp/out4py/factor_uint.py.100000_0.out.txt
2.1M    /sdcard/0my_files/tmp/out4py/factor_uint.py.100000_0.out.txt
$

cp -t /sdcard/0my_files/git_repos/txt_phone/txt/script/   /sdcard/0my_files/tmp/out4py/factor_uint.py.100000_0.out.txt.rar
    #524KB


view others/app/termux/tar_7zip.txt
cd /sdcard/0my_files/tmp/out4py/
7z a factor_uint.py.100000_0.out.txt.7z factor_uint.py.100000_0.out.txt
    Archive size: 432638 bytes (423 KiB)
    #422KB
mkdir /sdcard/0my_files/tmp/out4py/unzip/
cd /sdcard/0my_files/tmp/out4py/unzip/
7z e ../factor_uint.py.100000_0.out.txt.7z factor_uint.py.100000_0.out.txt






===========================
===========================
===========================
list {factor:exp} of uint coprime to given primes
view ../../python3_src/nn_ns/math_nn/numbers/min_factor.py
view ../../python3_src/nn_ns/math_nn/numbers/prime_number.py
view ../../python3_src/seed/iters/product.py
view ../../python3_src/seed/tiny.py


view ../../python3_src/nn_ns/math_nn/numbers/INumberList.py
view ../../python3_src/nn_ns/math_nn/numbers/numberss.py


e ../../python3_src/nn_ns/math_nn/numbers/numberss.py
    class NumberList(INumberList__nums__concrete_mixins):
        add:
            def _calc_pos(self, n, nums):
e ../../python3_src/nn_ns/math_nn/numbers/min_factor.py
    class MinFactor(NumberList):
        add:
            def _lookup_neg(self, n, nums):
        fixed:
            def _calc_neg(self, n, nums):


grep:
    deprecated, use INumberList/INumberTable instead
    ===
    grep 'use INumberList/INumberTable instead' --directories=recurse  /sdcard/0my_files/git_repos/python3_src/nn_ns/math_nn/numbers/
        /sdcard/0my_files/git_repos/python3_src/nn_ns/math_nn/numbers/numberss.py:warnings.warn("deprecated, use INumberList/INumberTable instead"
                #)


#'''

from nn_ns.math_nn.numbers.min_factor import min_factor
from nn_ns.math_nn.numbers.prime_number import PRIMES
from seed.iters.product import product
from seed.tiny import mk_fprint

def iter_factor_uint(*, uint_lt, coprime_lt):
    assert coprime_lt >= 1
    assert uint_lt >= 1
    min_factor(uint_lt)
        #prepare cache
    for u in range(1, uint_lt):
    #for u in range(max(1, coprime_lt), max(1, uint_lt)):
        i = u
        x = min_factor(i)
            #x is 1 or prime
        exp = 0
        if 2 <= x < coprime_lt: continue
        pairs = []
        while i != 1:
            i //= x
            exp += 1
            y = min_factor(i)
            if y != x:
                pairs.append((x, exp))
                x = y
                exp = 0
        else:
            assert i == 1 == x
            assert exp == 0
            assert u == product(1, (p**exp for p, exp in pairs))
        yield u, pairs
#def list_factor_uint(*, uint_lt, coprime_lt):
def show_factor_uint(*, fout, uint_le, coprime_le):
    assert coprime_le >= 0
    assert uint_le >= 0
    fprint = mk_fprint(fout)

    avoiding_factors = list(PRIMES.get_le(coprime_le))
    fprint(f'#uint_le={uint_le}, coprime_le={coprime_le}#avoiding_factors={avoiding_factors}')

    for u, pairs in iter_factor_uint(uint_lt=uint_le+1, coprime_lt=coprime_le+1):
        fprint('{', end='')
        sep = ''
        for p, exp in pairs:
            fprint(f'{sep}{p}:{exp}', end='')
            sep = ','
        fprint('}', end='')
        fprint(f'#{u}')


def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='factor_uint'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--uint_le', type=int, required=True
                        , help='factor uint in [1..uint_le] only which coprime to [2..coprime_le]')
    parser.add_argument('--coprime_le', type=int, required=True
            , help='factor uint in [1..uint_le] only which coprime to [2..coprime_le]')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        show_factor_uint(fout=fout, uint_le=args.uint_le, coprime_le=args.coprime_le)

if __name__ == "__main__":
    main()



r'''
===
py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 0 --uint_le 11 > /sdcard/0my_files/tmp/out4py/factor_uint.py.11_0.out.txt
view /sdcard/0my_files/tmp/out4py/factor_uint.py.11_0.out.txt
===
#uint_le=11, coprime_le=0#avoiding_factors=[]
{}#1
{2:1}#2
{3:1}#3
{2:2}#4
{5:1}#5
{2:1,3:1}#6
{7:1}#7
{2:3}#8
{3:2}#9
{2:1,5:1}#10
{11:1}#11
===



===
py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 5 --uint_le 0 > /sdcard/0my_files/tmp/out4py/factor_uint.py.0_5.out.txt
view /sdcard/0my_files/tmp/out4py/factor_uint.py.0_5.out.txt
===
#uint_le=0, coprime_le=5#avoiding_factors=[2, 3, 5]
===




===
py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 5 --uint_le 1 > /sdcard/0my_files/tmp/out4py/factor_uint.py.1_5.out.txt
view /sdcard/0my_files/tmp/out4py/factor_uint.py.1_5.out.txt
===
#uint_le=1, coprime_le=5#avoiding_factors=[2, 3, 5]
{}#1
===



===
py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 5 --uint_le 7 > /sdcard/0my_files/tmp/out4py/factor_uint.py.7_5.out.txt
view /sdcard/0my_files/tmp/out4py/factor_uint.py.7_5.out.txt
===
#uint_le=7, coprime_le=5#avoiding_factors=[2, 3, 5]
{}#1
{7:1}#7
===


===
py /sdcard/0my_files/git_repos/txt_phone/txt/script/factor_uint.py --coprime_le 5 --uint_le 100 > /sdcard/0my_files/tmp/out4py/factor_uint.py.100_5.out.txt
view /sdcard/0my_files/tmp/out4py/factor_uint.py.100_5.out.txt
===
#uint_le=100, coprime_le=5#avoiding_factors=[2, 3, 5]
{}#1
{7:1}#7
{11:1}#11
{13:1}#13
{17:1}#17
{19:1}#19
{23:1}#23
{29:1}#29
{31:1}#31
{37:1}#37
{41:1}#41
{43:1}#43
{47:1}#47
{7:2}#49
{53:1}#53
{59:1}#59
{61:1}#61
{67:1}#67
{71:1}#71
{73:1}#73
{7:1,11:1}#77
{79:1}#79
{83:1}#83
{89:1}#89
{7:1,13:1}#91
{97:1}#97
===

#'''
