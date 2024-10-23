#__all__:goto
r'''[[[
e script/unicode/unicode_common.py


script.unicode.unicode_common
py -m nn_ns.app.debug_cmd   script.unicode.unicode_common -x
py -m nn_ns.app.doctest_cmd script.unicode.unicode_common:__doc__ -ht
py_adhoc_call   script.unicode.unicode_common   @f

>>> list_gc_vas()
['Cc', 'Cf', 'Cn', 'Co', 'Cs', 'Ll', 'Lm', 'Lo', 'Lt', 'Lu', 'Mc', 'Me', 'Mn', 'Nd', 'Nl', 'No', 'Pc', 'Pd', 'Pe', 'Pf', 'Pi', 'Po', 'Ps', 'Sc', 'Sk', 'Sm', 'So', 'Zl', 'Zp', 'Zs']

#]]]'''
__all__ = r'''
chars2Ranges
chars5Ranges
print_names5chars
print_repr

UnicodeCommonOps4ver
list_methods6UnicodeCommonOps4ver
    pa2vas
    pa__Z__ichr2va
    pa_va2Ranges
    list_gc_vas
    gc2Ranges
    show_info_of_chars5pa_va

'''.split()#'''
__all__



from seed.iters.is_sorted import is_sorted
from seed.data_funcs.rngs import IRanges, make_Ranges, sorted_ints_to_iter_nontouch_ranges
from nn_ns.CJK.unicode.ucd_unihan.xml.resource_loader import data_loader4depth2__literal_eval__u8 as _load
#from functools import cached_property, cache
import unicodedata as U

_v14 = _load.ver14_0_0


def chars2Ranges(chars, /):
    us = map(ord, chars)
    if not is_sorted(chars):
        us = sorted({*us})
    return make_Ranges(sorted_ints_to_iter_nontouch_ranges(us))
def chars5Ranges(ranges, /):
    chars = ''.join(map(chr, ranges.iter_ints_(reverse=False)))
    return chars

def print_names5chars(cs, /):
    for ch in cs:
        print_repr(U.name(ch, '<None>'))

def print_repr(x, /):
    print(repr(x))


class UnicodeCommonOps4ver:
    def __init__(sf, ver:'ver14_0_0', /):
        sf._ver = ver
        sf._loadX = getattr(_load, ver)
    @property
    def ver(sf, /):
        return sf._ver
    @property
    def loaderX(sf, /):
        return sf._loadX

    #@cache
    def pa2vas(sf, pa, /):
        (va2hx2sz, ichr2va) = getattr(_v14, pa)
        vas = tuple(sorted(va2hx2sz))
        return vas

    def pa__Z__ichr2va(sf, pa, /):
        (va2hx2sz, ichr2va) = getattr(_v14, pa)
        return ichr2va
    #@cache
    def pa_va2Ranges(sf, pa, va, /):
        if pa == 'gc' and len(va) == 1:
            prefix4va = va
            vas = sf.pa2vas(pa)
            recur = sf.pa_va2Ranges
            ranges_ls = [recur(pa, va) for va in vas if va[0] == prefix4va]
            rs = ranges_ls.pop()
            for _rs in ranges_ls:
                rs |= _rs
            return rs
        ######################
        assert not pa == 'gc' or len(va) >= 2
        (va2hx2sz, ichr2va) = getattr(_v14, pa)
        hx2sz = va2hx2sz[va]
        ranges = IRanges.from_hex2sz(hx2sz)
        return ranges
        #ranges.to_hexXhexszpair_list()


    def list_gc_vas(sf, /):
        return sf.pa2vas('gc')

    def gc2Ranges(sf, gc, /):
        return sf.pa_va2Ranges('gc', gc)

    def show_info_of_chars5pa_va(sf, pa, va, /):
        'show:(sz;cs;nms)'
        ranges = sf.pa_va2Ranges(pa, va)
        cs4pa_va = chars5Ranges(ranges)
        print(len(cs4pa_va))
        print_repr(cs4pa_va)
        print_names5chars(cs4pa_va)
#end-class UnicodeCommonOps4ver:

def list_methods6UnicodeCommonOps4ver(ver:'ver14_0_0', /):
    ops_vXX = UnicodeCommonOps4ver(ver)
    pa2vas = ops_vXX.pa2vas
    pa__Z__ichr2va = ops_vXX.pa__Z__ichr2va
    pa_va2Ranges = ops_vXX.pa_va2Ranges
    list_gc_vas = ops_vXX.list_gc_vas
    gc2Ranges = ops_vXX.gc2Ranges
    show_info_of_chars5pa_va = ops_vXX.show_info_of_chars5pa_va
    return (ops_vXX, pa2vas, pa__Z__ichr2va, pa_va2Ranges, list_gc_vas, gc2Ranges, show_info_of_chars5pa_va)
if 1:
    (ops_v14, pa2vas, pa__Z__ichr2va, pa_va2Ranges, list_gc_vas, gc2Ranges, show_info_of_chars5pa_va) = list_methods6UnicodeCommonOps4ver('ver14_0_0')



__all__
from script.unicode.unicode_common import chars2Ranges, chars5Ranges, print_names5chars, print_repr
from script.unicode.unicode_common import UnicodeCommonOps4ver, list_methods6UnicodeCommonOps4ver
    #(ops_v14, pa2vas, pa__Z__ichr2va, pa_va2Ranges, list_gc_vas, gc2Ranges, show_info_of_chars5pa_va) = list_methods6UnicodeCommonOps4ver('ver14_0_0')
from script.unicode.unicode_common import pa2vas, pa__Z__ichr2va, pa_va2Ranges, list_gc_vas, gc2Ranges, show_info_of_chars5pa_va
from script.unicode.unicode_common import *
