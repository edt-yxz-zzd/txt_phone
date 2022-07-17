
r'''
e script/parse_integer_factor_result_at_factordb_com.py
py script/parse_integer_factor_result_at_factordb_com.py

py script/parse_integer_factor_result_at_factordb_com.py 'FF	65 (show)	2^214-1<65> = 3 · 643 · 84115747449047881488635567801<29> · 162259276829213363391578010288127<33>'
py script/parse_integer_factor_result_at_factordb_com.py 'FF	77 (show)	2^253-1<77> = 23^2 · 47 · 89 · 178481 · 4103188409<10> · 199957736328435366769577<24> · 44667711762797798403039426178361<32>'
py script/parse_integer_factor_result_at_factordb_com.py ''

http://factordb.com/index.php?query=%282%5E211-1%29

http://factordb.com/index.php?query=%282%5E213-1%29
2^213-1<65> = 7 · 66457 · 228479 · 48544121 · 212885833 · 2849881972114740679<19> · 4205268574191396793<19>

http://factordb.com/index.php?query=%282%5E214-1%29
    (2^214-1)
http://factordb.com/index.php?query=2%5E214-1
    2^214-1
    # %5E == '^'
FF	65 (show)	2^214-1<65> = 3 · 643 · 84115747449047881488635567801<29> · 162259276829213363391578010288127<33>
    # FF 完全分解
    # P  素数
    # 其他 状态 不予考虑


#'''


import re
#from itertools import reduce
from seed.math.II import II
from seed.helper.stable_repr import stable_repr

example0 = r'FF	65 (show)	2^214-1<65> = 3 · 643 · 84115747449047881488635567801<29> · 162259276829213363391578010288127<33>'
example1 = r'FF	77 (show)	2^253-1<77> = 23^2 · 47 · 89 · 178481 · 4103188409<10> · 199957736328435366769577<24> · 44667711762797798403039426178361<32>'
factor_ptn = fr'(?:(\d+)(?:\^(\d+))?(?:<\d+>)?)'
pattern = fr'^(FF|P)\t\d+ [(]show[)]\t2\^(\d+)-1<\d+> = ({factor_ptn}(?: · {factor_ptn})*)$'
regex = re.compile(pattern)
factor_rex = re.compile(factor_ptn)


examples = [example0, example1]
assert all(regex.fullmatch(example) for example in examples)
def s_parse(s, /):
    e, p2e = parse(s)
    return f',2**{e}-1: {stable_repr(p2e)}'
def parse(s, /):
    m = regex.fullmatch(s)
    if not m: raise ValueError
    status = m[1]
    exp = int(m[2])
    ls = m[3].split(' · ')
    ls = [(int(m[1]), int(m[2]) if m[2] else 1) for m in map(factor_rex.fullmatch, ls)]

    n = 2**exp-1
    assert II(p**e for p,e in ls) == n
    if status == 'P':
        assert ls == [n]
        return exp, {n:1}
    elif status == 'FF':
        return exp, dict(ls) #{p:1 for p in ls}
    else:
        raise logic-err

#print(s_parse(example0))
#print(s_parse(example1))
assert s_parse(example0) == ',2**214-1: {3: 1, 643: 1, 84115747449047881488635567801: 1, 162259276829213363391578010288127: 1}'
assert s_parse(example1) == ',2**253-1: {23: 2, 47: 1, 89: 1, 178481: 1, 4103188409: 1, 199957736328435366769577: 1, 44667711762797798403039426178361: 1}'


def main(args=None, /):
    import argparse

    parser = argparse.ArgumentParser(
        description='parse search result of (2**m-1) at factordb.com'
        , epilog='http://factordb.com/index.php?query=2%5E214-1'
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('input', type=str#, required=True
                        , help='factor info line')
    args = parser.parse_args(args)

    line = args.input
    print(s_parse(line))
if __name__ == "__main__":
    main()


