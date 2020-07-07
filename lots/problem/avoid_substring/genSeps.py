

__all__ = '''
    iter_minSeps
    iter_minSeps__native
    '''.split()
from itertools import product, permutations
def iter_minSeps(numSepChar, SepLen):
    '''
0 < numSepChar <= SepLen
split SepLen into L nonempty_ranges, where numSepChar <= L <= SepLen
    # C(SepLen-1, L-1)
group these L ranges into numSepChar partitions
    # choose numSepChar ranges as the min range in each class firstly.
    # the first 2 range must be selected
    # two adjection ranges cannot be grouped together
color these L ranges by order
'''
    assert 0 < numSepChar <= SepLen
    for L in range(numSepChar, SepLen+1):
        n = SepLen - L

def is_minSep(numSepChar, Sep):
    # [UInt] -> Bool
    next_new_uint = 0
    for u in Sep:
        if 0 <= u < next_new_uint: continue
        elif u == next_new_uint:
            next_new_uint += 1
        else:
            return False
    return next_new_uint == numSepChar
def iter_minSeps__native(numSepChar, SepLen):
    return (Sep for Sep in product(range(numSepChar), repeat=SepLen)
            if is_minSep(numSepChar, Sep)
            )

