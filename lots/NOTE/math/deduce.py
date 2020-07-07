
'''
EvalBool ~=~ BoolPair


'''

# deduce
DeduceBool = 'DT DF'.split()
evalbools = EvalBool = 'TF TU UU UF'.split()
bools = (False, True)
boolpairs = BoolPair = tuple((f, s) for f in bools for s in bools)


def is_boolpair(x):
    return type(x) == tuple and len(x) == 2 and all(type(b) is bool for b in x)\
           and x in boolpairs
def is_evalbool(x):
    return type(x) == str and len(x) == 2 and x in evalbools


def evalbool2boolpair(evalbool):
    assert is_evalbool(evalbool)
    x, y = evalbool
    return x == 'T', y == 'F'
def boolpair2evalbool(boolpair):
    assert is_boolpair(boolpair)
    fst, snd = boolpair
    return 'UT'[fst] + 'UF'[snd] # bug: 'UT'[fst], 'UF'[snd] // tuple not str

def check_evalbool2boolpair():
    try:
        for xy in evalbools:
            fs = evalbool2boolpair(xy)
            assert fs in boolpairs
            assert xy == boolpair2evalbool(fs)
    except:
        print(fs, xy)
        print(boolpair2evalbool(fs))
        raise
def check_boolpair2evalbool():
    for fs in boolpairs:
        xy = boolpair2evalbool(fs)
        assert xy in evalbools
        assert fs == evalbool2boolpair(xy)
        
check_evalbool2boolpair()
check_boolpair2evalbool()
def boolpair_not(fs):
    assert is_boolpair(fs)
    fst, snd = fs
    return snd, fst
def boolpair_or(fs, ht):
    assert is_boolpair(fs)
    assert is_boolpair(ht)
    f, s = fs
    h, t = ht
    return f or h, s and t
def boolpair_and(fs, ht):
    assert is_boolpair(fs)
    assert is_boolpair(ht)
    f, s = fs
    h, t = ht
    return f and h, s or t

def check_boolpair_not():
    for fs in boolpairs:
        xy = boolpair2evalbool(fs)

        _fs = boolpair_not(fs)
        _xy = evalbool_not(xy)
        
        assert _fs == evalbool2boolpair(_xy)

def check_boolpair_or():
    for fs in boolpairs:
        for ht in boolpairs:
            xy = boolpair2evalbool(fs)
            ab = boolpair2evalbool(ht)

            fs_or_ht = boolpair_or(fs, ht)
            xy_or_ab = evalbool_or(xy, ab)
            
            assert fs_or_ht == evalbool2boolpair(xy_or_ab)
def check_boolpair_and():
    for fs in boolpairs:
        for ht in boolpairs:
            xy = boolpair2evalbool(fs)
            ab = boolpair2evalbool(ht)

            fs_and_ht = boolpair_and(fs, ht)
            xy_and_ab = evalbool_and(xy, ab)
            
            assert fs_and_ht == evalbool2boolpair(xy_and_ab)



def evalbool_not_fst2snd(x):
    assert x in 'TU'
    return 'U' if x == 'U' else 'F'
def evalbool_not_snd2fst(y):
    assert y in 'UF'
    return 'U' if y == 'U' else 'T'

def evalbool_not(xy):
    '''
    -- not _F = T?
    -- not _U = U?
    -- not T_ = ?F
    -- not U_ = ?U
    '''
    assert is_evalbool(xy)
    x, y = xy
    return evalbool_not_snd2fst(y) + evalbool_not_fst2snd(x)

def check_xy_notxy(xy, not_xy):
    assert bool(xy[1] == 'F') == bool(not_xy[0] == 'T')
    assert bool(xy[1] == 'U') == bool(not_xy[0] == 'U')
    assert bool(xy[0] == 'U') == bool(not_xy[1] == 'U')
    assert bool(xy[0] == 'T') == bool(not_xy[1] == 'F')

def check_evalbool_not():
    for xy in evalbools:
        _xy = evalbool_not(xy)
        assert _xy in evalbools
        assert xy == evalbool_not(_xy)
        check_xy_notxy(xy, _xy)
        
check_evalbool_not()


def evalbool_or(ab, xy):
    '''
    -- U_ or x_ = x?
    -- _F or _y = ?y
    -- T_ or __ = T?
    -- _U or __ = ?U
    '''
    assert is_evalbool(ab)
    assert is_evalbool(xy)
    a, b = ab
    x, y = xy
    fst = x if a == 'U' else a
    snd = b if b == 'U' else y
    return fst + snd

def check_ab_xy_aborxy(ab, xy, ab_or_xy):
    assert ab[0] != 'U' or ab_or_xy[0] == xy[0]
    assert ab[0] != 'T' or ab_or_xy[0] == 'T'
    assert ab[1] != 'U' or ab_or_xy[1] == 'U'
    assert ab[1] != 'F' or ab_or_xy[1] == xy[1]
    


def check_evalbool_or():
    try:
        for ab in evalbools:
            for xy in evalbools:
                ab_or_xy = evalbool_or(ab, xy)
                assert ab_or_xy in evalbools
                assert ab_or_xy == evalbool_or(xy, ab)
                check_ab_xy_aborxy(ab, xy, ab_or_xy)
                check_ab_xy_aborxy(xy, ab, ab_or_xy)
    except:
        print(ab, xy, ab_or_xy)
        raise
    try:
        for ab in evalbools:
            for xy in evalbools:
                for zw in evalbools:
                    ab_or_xy = evalbool_or(ab, xy)
                    xy_or_zw = evalbool_or(xy, zw)
                    assert evalbool_or(ab_or_xy, zw) == evalbool_or(ab, xy_or_zw)
    except:
        print(ab, xy, zw)
        raise
check_evalbool_or()




def evalbool_and(ab, xy):
    '''
    -- T_ and x_ = x?
    -- U_ and __ = U?
    -- _U and _y = ?y
    -- _F and __ = ?F
    '''

    assert is_evalbool(ab)
    assert is_evalbool(xy)
    a, b = ab
    x, y = xy
    fst = a if a == 'U' else x
    snd = y if b == 'U' else b
    return fst + snd

def check_ab_xy_abandxy(ab, xy, ab_and_xy):
    assert ab[0] != 'U' or ab_and_xy[0] == 'U'
    assert ab[0] != 'T' or ab_and_xy[0] == xy[0]
    assert ab[1] != 'U' or ab_and_xy[1] == xy[1]
    assert ab[1] != 'F' or ab_and_xy[1] == 'F'
    


def check_evalbool_and():
    try:
        for ab in evalbools:
            for xy in evalbools:
                ab_and_xy = evalbool_and(ab, xy)
                assert ab_and_xy in evalbools
                assert ab_and_xy == evalbool_and(xy, ab)
                check_ab_xy_abandxy(ab, xy, ab_and_xy)
                check_ab_xy_abandxy(xy, ab, ab_and_xy)
    except:
        print(ab, xy, ab_and_xy)
        raise
    try:
        for ab in evalbools:
            for xy in evalbools:
                for zw in evalbools:
                    ab_and_xy = evalbool_and(ab, xy)
                    xy_and_zw = evalbool_and(xy, zw)
                    assert evalbool_and(ab_and_xy, zw) == evalbool_and(ab, xy_and_zw)
    except:
        print(ab, xy, zw)
        raise
check_evalbool_and()

def check_evalbool_not_and_or():
        for ab in evalbools:
            for xy in evalbools:
                not_ab = evalbool_not(ab)
                not_xy = evalbool_not(xy)
                assert evalbool_not(evalbool_or(ab, xy)) == evalbool_and(not_ab, not_xy)
                assert evalbool_not(evalbool_and(ab, xy)) == evalbool_or(not_ab, not_xy)
    

check_evalbool_not_and_or()


check_boolpair_not()
check_boolpair_or()
check_boolpair_and()


