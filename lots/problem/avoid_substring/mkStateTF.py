


from pprint import pprint
# see "avoid_substring.txt" for the named definitions
def mkMatrix(nRow, nCol, default=None):
    return [[default]*nCol for row in range(nRow)]
def is_suffix_of(sub, seq):
    if len(sub) > len(seq):
        return False
    return sub == seq[len(seq)-len(sub):]
def mkStateTF__native(Size, Sep):
    # Sep = list(Sep) # for "+ [char]"; see below
    SepLen = len(Sep)
    assert SepLen > 0
    using_chars = set(Sep)
    # Size may be a symbol
    assert type(Size) is not int or Size >= len(using_chars)


    def is_there_a_shift(row, col):
        # 0 < row <= col < SepLen
        # from col to row?
        # ?char. Sep[:row] `is_suffix_of` (Sep[:col] + [char])
        # let char = Sep[row-1]
        # Sep[:row-1] `is_suffix_of` Sep[:col]
        # not ?r>row. Sep[:r] `is_suffix_of` (Sep[:col] + [char])
        char = Sep[row-1]
        ls = Sep[:col]
        if not is_suffix_of(Sep[:row-1], ls):
            return False
        for i in range(row, col+1):
            if Sep[i] != char: continue
            if is_suffix_of(Sep[:i], ls): return False
        return True


    StateTF = mkMatrix(SepLen, SepLen)
    for row in range(1, SepLen):
        col = row-1
        StateTF[row][col] = 1
    for row in range(1, SepLen):
        for col in range(row-1):
            StateTF[row][col] = 0
    for row in range(1, SepLen):
        for col in range(row, SepLen):
            StateTF[row][col] = int(bool(is_there_a_shift(row, col)))
    for row in [0]:
        for col in range(SepLen):
            n = Size-1 - sum(StateTF[r][col] for r in range(1,col+1))
            StateTF[row][col] = n
    return StateTF

if 0:
    mx = mkStateTF__native(30, 'aaaa')
    mx = mkStateTF__native(30, 'aabbb')
    mx = mkStateTF__native(30, 'aabbbaa')
    mx = mkStateTF__native(30, 'aabbbaaa')
    pprint(mx)

def show_StateTF_of(Sep, Size=10):
    mx = mkStateTF__native(Size, Sep)
    print(Sep)
    pprint(mx)
    return mx

seps = '''
    aaa
    aaabbb
    aaabbbaaa
    aaabbbaaaaaa
    abbb
    aaab
    abab
    ababa
'''.split()

def test():
    for sep in seps:
        show_StateTF_of(sep)

from collections import defaultdict
from genSeps import iter_minSeps__native
def count_below1s_in_StateTF(Size, StateTF):
    # sum sum mx[row][i] {i}{row=1->len(mx)}
    return Size*len(StateTF)-1 - sum(StateTF[0])

def order_StateTF_by_num_of_1s(numSepChar=2, SepLen=6, Size=10):
    # -> [(count, (Sep, StateTF))]
    d = defaultdict(list)
    for Sep in iter_minSeps__native(numSepChar, SepLen):
        # StateTF = show_StateTF_of(Sep)
        StateTF = mkStateTF__native(Size, Sep)
        complex = count_below1s_in_StateTF(Size, StateTF)
        d[complex].append((Sep, StateTF))
    pairs = sorted(d.items(), reverse = True)
    return pairs

for numSepChar, SepLen in [(3,8),(2,6), (3, 6)]:
    pairs = order_StateTF_by_num_of_1s(numSepChar, SepLen)
    pprint(pairs)


