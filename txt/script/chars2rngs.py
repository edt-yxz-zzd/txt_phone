#__all__:goto
r'''[[[
e script/chars2rngs.py


script.chars2rngs
py -m nn_ns.app.debug_cmd   script.chars2rngs -x
py -m nn_ns.app.doctest_cmd script.chars2rngs:__doc__ -ff -v
#from script.chars2rngs import chars2rngs_, chars2NonTouchRanges, chars2hexXhexszpair_list, chars2len_rng2hexbegins

py_adhoc_call   script.chars2rngs   @stable_repr.chars2len_rng2hexbegins   :5783afvyjngjitedguuy5677g
{1: [0x33, 0x61, 0x6e, 0x79], 2: [0x69], 3: [0x74], 4: [0x35, 0x64]}

py_adhoc_call   script.chars2rngs   @stable_repr.chars2hexXhexszpair_list   :5783afvyjngjitedguuy5677g
[0x33, (0x35, 4), 0x61, (0x64, 4), (0x69, 2), 0x6e, (0x74, 3), 0x79]


py_adhoc_call   script.chars2rngs   @stable_repr.main --name4func:chars2hexXhexszpair_list   --qname4module:nn_ns.CJK.cjk_subsets.hanzi  --qname4chars:cjk_common_subset_2513
py_adhoc_call   script.chars2rngs   @stable_repr.main --name4func:chars2len_rng2hexbegins   --qname4module:nn_ns.CJK.cjk_subsets.hanzi  --qname4chars:cjk_common_subset_2513
{..., 4: [0x4eab, 0x4f59, 0x5143, 0x516b, 0x5175, 0x5347, 0x53c8, 0x5bb3, 0x5bc4, 0x5de5, 0x5df1, 0x5eb5, 0x5fd6, 0x62ec, 0x63a7, 0x672a, 0x674e, 0x6840, 0x6c5d, 0x7433, 0x7459, 0x7530, 0x7b4f, 0x8302, 0x8e47, 0x91cc, 0x96c4], 5: [0x4e07, 0x4f0d, 0x4f4d, 0x53e9, 0x53ef, 0x5ba2, 0x5c38, 0x6cbb, 0x9b41], 6: [0x4ed4, 0x540c, 0x5b97, 0x901d, 0x9149]}
    大部分相邻长度是1、2，少量3

py_adhoc_call   script.chars2rngs   @stable_repr.main --name4func:chars2len_rng2hexbegins   --qname4module:nn_ns.CJK.cjk_subsets.hanzi  --qname4chars:cjk_common_subset_2513 --name4obj4IChars2Rngs:chars2rngs__using_gb2312
{..., 4: [0x5a4, 0x5db, 0x5e0, 0x605, 0x645, 0x64a, 0x6a5, 0x6ee, 0x71c, 0x72f, 0x774, 0x783, 0x78c, 0x863, 0x8b6, 0x8cc, 0x8f6, 0x8fb, 0x903, 0x92d, 0x953, 0x9ad, 0x9c0, 0x9e4, 0xa22, 0xac8, 0xacf, 0xada, 0xaef, 0xb17, 0xb38, 0xb51, 0xb5e, 0xc15, 0xc31, 0xc78, 0xcbc, 0xceb, 0xd06, 0xd17, 0xd7a, 0xd97, 0xd9e, 0xdc8, 0xe23, 0xe7a, 0xe8b, 0xebc, 0xed4, 0xeee, 0xf09, 0xf24, 0xf2f, 0xf3c, 0xf42, 0xf52, 0xf86, 0xfa2, 0x10cc, 0x10d9, 0x10ed, 0x1126, 0x1142, 0x1168, 0x11c1, 0x1226, 0x1233, 0x1372, 0x13b0, 0x13be, 0x13cc, 0x13d3, 0x13ef, 0x1429, 0x1a89, 0x1bf0, 0x1fdd], 5: [0x593, 0x5be, 0x619, 0x666, 0x6d9, 0x755, 0x886, 0x8bf, 0x8f0, 0x9c5, 0xa05, 0xa5c, 0xa82, 0xad4, 0xb11, 0xc0d, 0xc89, 0xc9b, 0xe69, 0xe85, 0xf29, 0xffa, 0x1099, 0x1132, 0x1192, 0x122d, 0x12ab, 0x12c3, 0x12d0, 0x139a, 0x1415, 0x18b6], 6: [0x5eb, 0x6c2, 0x6ce, 0x712, 0x73d, 0x7ce, 0x89a, 0x8d1, 0x958, 0x9f7, 0xb02, 0xb3f, 0xba4, 0xbed, 0xc7d, 0xd82, 0xd8f, 0xdba, 0xe2b, 0xee5, 0xef9, 0x1214, 0x134e, 0x137e, 0x138c], 7: [0x5c6, 0x939, 0xa94, 0xd41, 0xe42, 0xf8b, 0x1147, 0x117c, 0x11d6], 8: [0x65b, 0x82d, 0x97d, 0x986, 0xadf, 0xe96, 0x1077, 0x10e4, 0x1288], 9: [0x9b3, 0xa89, 0xd5a, 0xf58, 0x1028, 0x1080, 0x1238], 10: [0x87a, 0xdcd, 0x1171, 0x141e], 13: [0xcf0], 14: [0xcdc]}
    还是分裂成很多部分

#]]]'''
__all__ = r'''
main
IChars2Rngs
    Chars2Rngs__using_unicode
        chars2rngs__using_unicode
    Chars2Rngs__using_gb2312
        chars2rngs__using_gb2312
'''.split()#'''
    #chars2rngs_
    #chars2NonTouchRanges
    #chars2hexXhexszpair_list
    #chars2len_rng2hexbegins
__all__
from nn_ns.CJK.cjk_subsets.hanzi import cjk_common_subset_2513 #共享汉字字集
import nn_ns.CJK.cjk_subsets.hanzi
from seed.data_funcs.rngs import sorted_ints_to_iter_nontouch_ranges, make_NonTouchRanges  # make_Ranges
from seed.data_funcs.rngs import ranges2hexXhexszpair_list, ranges5hexXhexszpair_list
from seed.data_funcs.rngs import ranges2len_rng2hexbegins, ranges5len_rng2hexbegins
from seed.pkg_tools.import_object import import4qobject
#def import4qobject(may_qname4module, may_qname4obj, /):

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

r'''[[[
def hzs2rngs(hzs, /):
    rngs = chars2rngs_(hzs)
    assert not rngs or rngs[0][0] >= 0x3400
    return rngs
#]]]'''#'''
class IChars2Rngs(ABC):
    __slots__ = ()
    @abstractmethod
    def _char2uint_(sf, ch, /):
        raise NotImplementedError
    def chars2rngs_(sf, s, /):
        return tuple(sorted_ints_to_iter_nontouch_ranges(sorted(map(sf._char2uint_, s))))
    def chars2NonTouchRanges(sf, s, /):
        return make_NonTouchRanges(sf.chars2rngs_(s))
    def chars2hexXhexszpair_list(sf, s, /):
        return ranges2hexXhexszpair_list(sf.chars2NonTouchRanges(s))
    def chars2len_rng2hexbegins(sf, s, /):
        return ranges2len_rng2hexbegins(sf.chars2NonTouchRanges(s))
class Chars2Rngs__using_unicode(IChars2Rngs):
    __slots__ = ()
    @override
    def _char2uint_(sf, ch, /):
        return ord(ch)
chars2rngs__using_unicode = Chars2Rngs__using_unicode()

class Chars2Rngs__using_gb2312(IChars2Rngs):
    __slots__ = ()
    #view ../../python3_src/nn_ns/CJK/iter_gb2312_hanzi.py
    @override
    def _char2uint_(sf, ch, /):
        bs = ch.encode('gb2312')
        if not len(bs) == 2: raise Exception(f'not hz: {ch!r}')
        i,j = bs
        i -= 0xA0
        j -= 0xA0
        assert 1 <= i <= 94
        assert 1 <= j <= 94
        u = (i-1)*94+(j-1)
        return u
        return ord(ch)
chars2rngs__using_gb2312 = Chars2Rngs__using_gb2312()

#def main(*, qname4module, qname4chars, name4func):
    #f = globals()[name4func]
def main(*, qname4module, qname4chars, name4func, name4obj4IChars2Rngs='chars2rngs__using_unicode'):
    sf = globals()[name4obj4IChars2Rngs]
    f = getattr(sf, name4func)
    s = import4qobject(qname4module, qname4chars)
    return f(s)

if __name__ == "__main__":
    pass
__all__


from script.chars2rngs import *
#from script.chars2rngs import chars2rngs_, chars2NonTouchRanges, chars2hexXhexszpair_list, chars2len_rng2hexbegins
