#__all__:goto
r'''[[[
e script/unicode/unicode_char_class4word.py
view ../lots/NOTE/unicode/char_class/word-vs-graphical.txt
view others/app/termux/help/perluniprops.man.txt

script.unicode.unicode_char_class4word
py -m nn_ns.app.debug_cmd   script.unicode.unicode_char_class4word -x
py -m nn_ns.app.doctest_cmd script.unicode.unicode_char_class4word:__doc__ -ht


[[[
view ../lots/NOTE/unicode/char_class/word-vs-graphical.txt
===
#NOTE:below counts are from (Unicode_ver15@perl(v5.38.2)  |  py3_11_9__re2_2_1)
  #vs:ucd_ver14_0_0:view script/unicode/unicode_char_class4word.py.out.txt
===
py.\w (133_548)
perl.\w (139_612)
\p{Graph} (286_635)
    (\p{Graph}-\p{Co}-\p{Cf}) (148_997)
\p{Print} (286_652)
    \p{Print}-\p{Co}-\p{Cf} (149_014)
Letter (136_104)
Alphabetic (137_765)
Ideographic (105_854)
  Unified_Ideograph (97_058)
Emoji (1424)
Emoji_Presentation (1205)
Extended_Pictographic (3537)
Grapheme_Base (146_986)
Grapheme_Extend (2125)
Unicode_Graphic_character+Co (286_482)
Unicode_Base_character+Co (284_032)
Unicode_Graphic_character-Co (149_014)
Unicode_Base_character-Co (146_564)
XID_Start (136_322)
XID_Continue (139_463)
ID_Start (136_345)
ID_Continue (139_482)
===
]]]
[[[
view ../lots/NOTE/unicode/char_class/word-vs-graphical.txt
===
[Unicode_Graphic_character =[def]= gc.L|N|P|S|Zs|M|?Co? === -(gc.Zl|Zp|Cn|Cs|Cc|Cf|?Co?)]
  『isolated combining character => as if it were a base character』
  ~= [[:print:]] == [[:graph:][:space:]]
[Unicode_Base_character =[def]= Unicode_Graphic_character-gc.M === gc.L|N|P|S|Zs|?Co? === -(gc.M|Zl|Zp|Cn|Cs|Cc|Cf|?Co?)]


===
Unicode_Graphic_character+Co (286_482) === \p{General_Category=Letter} (136_104) +\p{General_Category=Number} (1831) +\p{General_Category=Punctuation} (842) +\p{General_Category=Symbol} (7770) +\p{General_Category=Space_Separator} (17) +\p{General_Category=Mark} (2450) +\p{General_Category=Private_Use} (137_468)
  286_482 === (136_104) + (1831) + (842) + (7770) + (17) + (2450) + (137_468)
Unicode_Graphic_character-Co (149_014) === \p{General_Category=Letter} (136_104) +\p{General_Category=Number} (1831) +\p{General_Category=Punctuation} (842) +\p{General_Category=Symbol} (7770) +\p{General_Category=Space_Separator} (17) +\p{General_Category=Mark} (2450)
  149_014 === (136_104) + (1831) + (842) + (7770) + (17) + (2450)
===
Unicode_Base_character+Co (284_032) === \p{General_Category=Letter} (136_104) +\p{General_Category=Number} (1831) +\p{General_Category=Punctuation} (842) +\p{General_Category=Symbol} (7770) +\p{General_Category=Space_Separator} (17) +\p{General_Category=Private_Use} (137_468)
  284_032 === (136_104) + (1831) + (842) + (7770) + (17) + (137_468)
Unicode_Base_character-Co (146_564) === \p{General_Category=Letter} (136_104) +\p{General_Category=Number} (1831) +\p{General_Category=Punctuation} (842) +\p{General_Category=Symbol} (7770) +\p{General_Category=Space_Separator} (17)
  146_564 === (136_104) + (1831) + (842) + (7770) + (17)
===
===
\p{General_Category=Space_Separator} (Short=\p{Gc=Zs}, \p{Zs}) (17: [\x20\xa0], U+1680, U+2000..200A, U+202F, U+205F, U+3000)
===
\p{Print}===\p{XPosixPrint} (286_652)===\p{XPosixGraph} (286_635) +\p{General_Category=Space_Separator} (17)
===
]]]





























[[
py_adhoc_call   script.unicode.unicode_char_class4word   @stable_repr__expand_top_layer.list_pairwise_cmp_all_available_char_classes :ver14_0_0     +to_output_version   --to_add_chars_if_sz_le=20   >   script/unicode/unicode_char_class4word.py.out.txt
view script/unicode/unicode_char_class4word.py.out.txt
,(('ucd__gc__Punctuation', 'py__re__w'), '___', (819, 133548), (818, 1, 133547), ('', '_', ''))
,(('ucd__gc__Number', 'py__re__w'), '__lt__', (1791, 133548))
,(('ucd__Unified_Ideograph__Y', 'py__re__w'), '__lt__', (92865, 133548))
,(('ucd__Ideographic__Y', 'py__re__w'), '___', (101661, 133548), (1, 101660, 31888), ('𖿤', '', ''))
    '0x16FE4'
    'KHITAN SMALL SCRIPT FILLER'
        'Ideographic_Symbols' : {0x16FE0: 32}
        Khitan Small Script: U+18B00–U+18CFF・契丹小字
,(('ucd__gc__Letter', 'py__re__w'), '__lt__', (131756, 133548))
    1+1791+131756==133548
,(('py__re__w', 'py__re__w__5__gc_L_N_underscore'), '__eq__', (133548, 133548))

]]



[[
import script.unicode.unicode_char_class4word as x
import importlib
x = importlib.reload(x)
ver = 'ver14_0_0'
ucc14 = x.UnicodeCharClass4Word4ver(ver)
ucc14.all_names4available_char_class
len(ucc14.all_names4available_char_class) #38

selected_nms = (
('pl__XPosixAlnum'
#, 'pl__XPosixAlpha' #ucd__Alphabetic__Y
#, 'pl__XPosixDigit'
, 'pl__XPosixGraph'
, 'pl__XPosixGraph__exclude__Co_Cf'
, 'pl__XPosixPrint'
, 'pl__XPosixPrint__exclude__Co_Cf'
, 'pl__XPosixWord'
#, 'py__re__w' #new
#, 'py__re__w__5__gc_L_N_underscore' #new
, 'std__Unicode_Base_character__exclude__Co'
, 'std__Unicode_Base_character__include__Co'
, 'std__Unicode_Graphic_character__exclude__Co'
, 'std__Unicode_Graphic_character__include__Co'
, 'ucd__Alphabetic__Y'
, 'ucd__Emoji_Presentation__Y'
, 'ucd__Emoji__Y'
, 'ucd__Extended_Pictographic__Y'
, 'ucd__Grapheme_Base__Y'
, 'ucd__Grapheme_Extend__Y'
, 'ucd__ID_Continue__Y'
, 'ucd__ID_Start__Y'
, 'ucd__Ideographic__Y'
#, 'ucd__Join_Control__Y'
#, 'ucd__Unified_Ideograph__Y' #new
, 'ucd__XID_Continue__Y'
, 'ucd__XID_Start__Y'
#, 'ucd__gc__Connector_Punctuation'
#, 'ucd__gc__Decimal_Number'
#, 'ucd__gc__Format'
, 'ucd__gc__Letter'
#, 'ucd__gc__Mark'
#, 'ucd__gc__Number'
#, 'ucd__gc__Private_Use'
#, 'ucd__gc__Punctuation'
#, 'ucd__gc__Space_Separator'
#, 'ucd__gc__Spacing_Mark'
, 'ucd__gc__Symbol'
))

len(selected_nms) #23 #23*22//2 == 253

import contextlib
with open('/sdcard/0my_files/tmp/0tmp', 'wt', encoding='u8') as ofile, contextlib.redirect_stdout(ofile):
    for t in ucc14.iter_pairwise_cmp_all_available_char_classes(selected_nms):print(t)

view /sdcard/0my_files/tmp/0tmp
,(('ucd__Ideographic__Y', 'ucd__Alphabetic__Y'), '___', (101661, 133396), (1, 101660, 31736))
    ???难道是:〇???
,(('ucd__ID_Start__Y', 'std__Unicode_Base_character__include__Co'), '___', (131997, 279592), (2, 131995, 147597))



with open('/sdcard/0my_files/tmp/0tmp', 'wt', encoding='u8') as ofile, contextlib.redirect_stdout(ofile):
    for t in ucc14.iter_pairwise_cmp_all_available_char_classes(selected_nms, to_add_chars_if_sz_le=20):print(t)

view /sdcard/0my_files/tmp/0tmp
  view ../lots/NOTE/unicode/统合码冫汉化.txt
,(('ucd__Ideographic__Y', 'ucd__Alphabetic__Y'), '___', (101661, 133396), (1, 101660, 31736), ('𖿤', '', ''))
    '0x16FE4'
    'KHITAN SMALL SCRIPT FILLER'
        'Ideographic_Symbols' : {0x16FE0: 32}
        Khitan Small Script: U+18B00–U+18CFF・契丹小字
,(('ucd__ID_Start__Y', 'std__Unicode_Base_character__include__Co'), '___', (131997, 279592), (2, 131995, 147597), ('ᢅᢆ', '', ''))
    '0x1885'
    'MONGOLIAN LETTER ALI GALI BALUDA'
    +
    '0x1886'
    'MONGOLIAN LETTER ALI GALI THREE BALUDA'
        Mongolian: U+1800–U+18AF・蒙文Mongolian Supplement: U+11660–U+1167F・蒙文增补

]]




#]]]'''
__all__ = r'''
UnicodeCharClass4Word4ver
    cmp_result_ver14
    list_pairwise_cmp_all_available_char_classes
    iter_pairwise_cmp_all_available_char_classes
'''.split()#'''
__all__


from script.unicode.unicode_common import chars2Ranges, chars5Ranges, print_names5chars, print_repr
from script.unicode.unicode_common import UnicodeCommonOps4ver, list_methods6UnicodeCommonOps4ver
    #(ops_v14, pa2vas, pa__Z__ichr2va, pa_va2Ranges, list_gc__vas, gc2Ranges, show_info_of_chars5pa_va) = list_methods6UnicodeCommonOps4ver('ver14_0_0')
from functools import cached_property, cache
import sys
#sys.version_info(major=3, minor=11, micro=9, releaselevel='final', serial=0)
import re
re.__version__ # '2.2.1'

py_ver = f'py{sys.version_info.major}_{sys.version_info.minor}_{sys.version_info.micro}'
re_ver = 're' +re.__version__.replace('.', '_')
py_re_ver = f'{py_ver}__{re_ver}'


_word_regex = re.compile(r'\w')
_nonword_regex = re.compile(r'\W')
assert 'abc' == _nonword_regex.sub('', 'a+b c')
if 1:
    ranges4underscore = chars2Ranges('_')
    @cache
    def py__re__w(max1=0x11_00_00, /):
        #bug:def py__re__w(max1=0x1_00_00, /):
        r'-> IRanges/NonTouchRanges # ' \
        r"[re.compile(r'\w')==\pL|\pN|'_']"
        s = ''.join(map(chr, range(max1)))
        s = _nonword_regex.sub('', s)
        return chars2Ranges(s)
if 1:
    def list_pairwise_cmp_all_available_char_classes(ver, /, *args, **kwds):
        sf = UnicodeCharClass4Word4ver(ver)
        return sf.list_pairwise_cmp_all_available_char_classes(*args, **kwds)
    def iter_pairwise_cmp_all_available_char_classes(ver, /, *args, **kwds):
        sf = UnicodeCharClass4Word4ver(ver)
        return sf.iter_pairwise_cmp_all_available_char_classes(*args, **kwds)


class UnicodeCharClass4Word4ver:
    def __init__(sf, ver:'ver14_0_0', /):
        sf._ver = ver
        sf._opsX = UnicodeCommonOps4ver(ver)
    @property
    def ver(sf, /):
        return sf._ver
    @property
    def opsX(sf, /):
        return sf._opsX

    ######################
    ######################
    ######################
    @cached_property
    def all_names4available_char_class(sf, /):
        '-> [nm]'
        return tuple(nm for nm in sorted({*dir(sf)}) if any(map(nm.startswith, 'pl__ ucd__ std__ py__'.split())))

    def list_pairwise_cmp_all_available_char_classes(sf, /, *args, **kwds):
        return [*sf.iter_pairwise_cmp_all_available_char_classes(*args, **kwds)]
    def iter_pairwise_cmp_all_available_char_classes(sf, nms=None, /, *, to_add_chars_if_sz_le=None, to_output_version=False):
        if to_output_version:
            ucd_ver = f'ucd_{sf.ver}'
            yield ucd_ver
            yield py_re_ver
        ######################
        if nms is None:
            nms = sf.all_names4available_char_class
        nms = sorted({*nms})
        ts = [(rs.len_ints(), nm, rs) for nm in nms for rs in [getattr(sf, nm)]]
        ts.sort()
        if not to_add_chars_if_sz_le is None and to_add_chars_if_sz_le > 0:
            max0 = to_add_chars_if_sz_le
            def iter_sss5szs(rss, szs, /):
                '-> Iter [smay_str]'
                if not min(szs) <= max0:
                    return
                yield tuple(chars5Ranges(rs) if sz <= max0 else '' for rs, sz in zip(rss, szs))
                return
        else:
            def iter_sss5szs(rss, szs, /):
                '-> Iter [smay_str]'
                return;yield

        def f(i, j, /):
            (sz4i, nm4i, rs4i) = ts[i]
            (sz4j, nm4j, rs4j) = ts[j]
            assert sz4i <= sz4j
            assert not nm4i == nm4j
            rs4IsubJ = rs4i - rs4j
            #if rs4i <= rs4j:
            if not rs4IsubJ:
                op = '__eq__' if rs4i == rs4j else '__lt__'
                yield ((nm4i, nm4j), op, (sz4i, sz4j))
                return
            rs4IandJ = rs4i & rs4j
            if not rs4IandJ:
                yield ((nm4i, nm4j), 'disjoint', (sz4i, sz4j))
                return
            rs4JsubI = rs4j - rs4i
            rss = (rs4IsubJ, rs4IandJ, rs4JsubI)
            szs = tuple(rs.len_ints() for rs in rss)
            yield ((nm4i, nm4j), '___', (sz4i, sz4j), szs, *iter_sss5szs(rss, szs))
            return
        #end-def f(i, j, /):

        L = len(ts)
        for i in range(L):
            for j in range(i+1, L):
                yield from f(i, j)
    #end-def iter_pairwise_cmp_all_available_char_classes(sf, nms=None, /, *, to_add_chars_if_sz_le=None):


    ######################
    ######################
    ######################
    @cached_property
    def py__re__w(sf, /):
        #vs: py__re__w__5__gc_L_N_underscore()
        r'-> IRanges/NonTouchRanges # ' \
        r"[re.compile(r'\w')==\pL|\pN|'_']"
        return py__re__w()
    @cached_property
    def py__re__w__5__gc_L_N_underscore(sf, /):
        #vs: py__re__w()
        r'-> IRanges/NonTouchRanges # ' \
        r"[re.compile(r'\w')==\pL|\pN|'_']"
        # py.re.\w===(gc.L | gc.N | '_')
        return sf.ucd__gc__Letter | sf.ucd__gc__Number | ranges4underscore

    ######################
    ######################
    ######################
    @cached_property
    def pl__XPosixGraph(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Graph}===\p{XPosixGraph} (286_635) === \pL+\pN+\pP+\pS+\pM+\p{Co}+\p{Cf}]'
        #\p{Graph}=== \p{General_Category=Letter} (136_104) +\p{General_Category=Number} (1831) +\p{General_Category=Punctuation} (842) +\p{General_Category=Symbol} (7770) +\p{General_Category=Mark} (2450) +\p{General_Category=Private_Use} (137_468) +\p{General_Category=Format} (170)
        return sf.ucd__gc__Letter | sf.ucd__gc__Number | sf.ucd__gc__Punctuation | sf.ucd__gc__Symbol | sf.ucd__gc__Mark | sf.ucd__gc__Private_Use | sf.ucd__gc__Format

    @cached_property
    def pl__XPosixGraph__exclude__Co_Cf(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Graph}-\p{Co}-\p{Cf}===(\p{XPosixGraph}-\p{Co}-\p{Cf}) (148_997) === \pL+\pN+\pP+\pS+\pM]'
        return sf.ucd__gc__Letter | sf.ucd__gc__Number | sf.ucd__gc__Punctuation | sf.ucd__gc__Symbol | sf.ucd__gc__Mark


    @cached_property
    def pl__XPosixWord(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\w===\p{Word}===\p{XPosixWord} (139_612)===\p{Alnum} + \pM + \p{Pc} + \p{Join_Control}]'
        # \w (139_612)===\p{Alphabetic=Y} (137_765)+ \p{General_Category=Decimal_Number} (680) + \p{General_Category=Mark} (2450) + \p{General_Category=Connector_Punctuation} (10) + \p{Join_Control=Y} (2)  -(?1295?)(count of [\p{Alphabetic=Y}&\p{General_Category=Mark}])
        return sf.pl__XPosixAlnum | sf.ucd__gc__Mark | sf.ucd__gc__Connector_Punctuation | sf.ucd__Join_Control__Y

    @cached_property
    def pl__XPosixAlnum(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Alnum}===\p{XPosixAlnum} (138_445)===\p{XPosixAlpha} (137_765)+ \p{XPosixDigit} (680)===\p{Alphabetic=Y} (137_765)+ \p{General_Category=Decimal_Number} (680)]'
        return sf.pl__XPosixAlpha | sf.pl__XPosixDigit


    @cached_property
    def pl__XPosixAlpha(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{XPosixAlpha}===\p{Alphabetic=Y} (Short: \p{Alpha}) (137_765)]'
        return sf.ucd__Alphabetic__Y


    @cached_property
    def pl__XPosixDigit(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{XPosixDigit}===\p{General_Category=Decimal_Number} [0-9] + all other decimal digits (Short: \p{Nd}) (680)]'
        return sf.ucd__gc__Decimal_Number

    @cached_property
    def pl__XPosixPrint(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Print}===\p{XPosixPrint} (286_652)===\p{XPosixGraph} (286_635) +\p{General_Category=Space_Separator} (17)]'
        return sf.pl__XPosixGraph | sf.ucd__gc__Space_Separator

    @cached_property
    def pl__XPosixPrint__exclude__Co_Cf(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Print}-\p{Co}-\p{Cf}===(\p{XPosixPrint}-\p{Co}-\p{Cf}) (149_014)===(\p{XPosixGraph}-\p{Co}-\p{Cf}) (148_997) +\p{General_Category=Space_Separator} (17)]'
        return sf.pl__XPosixGraph__exclude__Co_Cf | sf.ucd__gc__Space_Separator

    ######################
    ######################
    ######################
    @cached_property
    def ucd__Join_Control__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Join_Control=Y} (2)]'
        return sf.opsX.pa_va2Ranges('Join_C', 'Y')
    @cached_property
    def ucd__Alphabetic__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'\p{XPosixAlpha}===\p{Alphabetic=Y} (Short: \p{Alpha}) (137_765)'
        return sf.opsX.pa_va2Ranges('Alpha', 'Y')
    @cached_property
    def ucd__Ideographic__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Ideo}===\p{Ideographic} (= \p{Ideographic=Y}) (105_854)]'
        return sf.opsX.pa_va2Ranges('Ideo', 'Y')
    @cached_property
    def ucd__Unified_Ideograph__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{UIdeo}===\p{Unified_Ideograph} (=\p{Unified_Ideograph=Y}) (97_058)]'
        return sf.opsX.pa_va2Ranges('UIdeo', 'Y')



    ######################
    @cached_property
    def ucd__XID_Start__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{XIDS}===\p{XID_Start} (= \p{XID_Start=Y}) (136_322)]'
        return sf.opsX.pa_va2Ranges('XIDS', 'Y')
    @cached_property
    def ucd__XID_Continue__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{XIDC}===\p{XID_Continue} (= \p{XID_Continue=Y}) (139_463)]'
        return sf.opsX.pa_va2Ranges('XIDC', 'Y')
    @cached_property
    def ucd__ID_Start__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{IDS}===\p{ID_Start} (= \p{ID_Start=Y}) (136_345)]'
        return sf.opsX.pa_va2Ranges('IDS', 'Y')
    @cached_property
    def ucd__ID_Continue__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{IDC}===\p{ID_Continue} (= \p{ID_Continue=Y}) (NOT \p{Ideographic_Description_Characters}) (139_482)]'
        return sf.opsX.pa_va2Ranges('IDC', 'Y')




    ######################
    @cached_property
    def ucd__Emoji__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Emoji}===\p{Emoji=Y} (1424)]'
        return sf.opsX.pa_va2Ranges('Emoji', 'Y')
    @cached_property
    def ucd__Emoji_Presentation__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Emoji_Presentation}===\p{Emoji_Presentation=Y} (Short: \p{EPres}) (1205)]'
        return sf.opsX.pa_va2Ranges('EPres', 'Y')
    @cached_property
    def ucd__Extended_Pictographic__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Extended_Pictographic} \p{Extended_Pictographic=Y} (Short: \p{ExtPict}) (3537)]'
        return sf.opsX.pa_va2Ranges('ExtPict', 'Y')



    ######################
    @cached_property
    def ucd__Grapheme_Base__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Gr_Base}===\p{Grapheme_Base} (= \p{Grapheme_Base=Y}) (146_986)]'
        # \p{Gr_Base}===\p{Grapheme_Base} (= \p{Grapheme_Base=Y}) (146_986) ~= Unicode_Base_character-Co (146_564) -{U+FF9E,U+FF9F} +\p{General_Category=Spacing_Mark} (452) -??? (?28?)
        return sf.opsX.pa_va2Ranges('Gr_Base', 'Y')
    @cached_property
    def ucd__Grapheme_Extend__Y(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Gr_Ext}===\p{Grapheme_Extend} (= \p{Grapheme_Extend=Y}) (2125)]'
        return sf.opsX.pa_va2Ranges('Gr_Ext', 'Y')

    ######################
    ######################
    ######################
    @cached_property
    def ucd__gc__Space_Separator(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Space_Separator} (Short=\p{Gc=Zs}, \p{Zs}) (17: [\x20\xa0], U+1680, U+2000..200A, U+202F, U+205F, U+3000)]'
        return sf.opsX.pa_va2Ranges('gc', 'Zs')
    @cached_property
    def ucd__gc__Spacing_Mark(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{Mc}===\p{Spacing_Mark} (= \p{General_Category=Spacing_Mark}) (452)]'
        return sf.opsX.pa_va2Ranges('gc', 'Mc')
    @cached_property
    def ucd__gc__Decimal_Number(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{XPosixDigit}===\p{General_Category=Decimal_Number} [0-9] + all other decimal digits (Short: \p{Nd}) (680)]'
        return sf.opsX.pa_va2Ranges('gc', 'Nd')
    @cached_property
    def ucd__gc__Connector_Punctuation(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Connector_Punctuation} (10)]'
        return sf.opsX.pa_va2Ranges('gc', 'Pc')
    @cached_property
    def ucd__gc__Letter(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Letter}]'
        return sf.opsX.pa_va2Ranges('gc', 'L')
    @cached_property
    def ucd__gc__Number(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Number}]'
        return sf.opsX.pa_va2Ranges('gc', 'N')
    @cached_property
    def ucd__gc__Punctuation(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Punctuation}]'
        return sf.opsX.pa_va2Ranges('gc', 'P')
    @cached_property
    def ucd__gc__Symbol(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Symbol}]'
        return sf.opsX.pa_va2Ranges('gc', 'S')
    @cached_property
    def ucd__gc__Mark(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Mark}]'
        return sf.opsX.pa_va2Ranges('gc', 'M')
    @cached_property
    def ucd__gc__Private_Use(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Private_Use}]'
        return sf.opsX.pa_va2Ranges('gc', 'Co')
    @cached_property
    def ucd__gc__Format(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[\p{General_Category=Format}]'
        return sf.opsX.pa_va2Ranges('gc', 'Cf')
    ######################
    ######################
    ######################


    @cached_property
    def std__Unicode_Graphic_character__include__Co(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[Unicode_Graphic_character =[def]= gc.L|N|P|S|Zs|M|?Co? === -(gc.Zl|Zp|Cn|Cs|Cc|Cf|?Co?)]'
        return sf.std__Unicode_Graphic_character__exclude__Co | sf.ucd__gc__Private_Use
        return sf.std__Unicode_Base_character__include__Co | sf.ucd__gc__Mark
        return sf.ucd__gc__Letter | sf.ucd__gc__Number | sf.ucd__gc__Punctuation | sf.ucd__gc__Symbol | sf.ucd__gc__Space_Separator | sf.ucd__gc__Mark | sf.ucd__gc__Private_Use
    @cached_property
    def std__Unicode_Base_character__include__Co(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[Unicode_Base_character =[def]= Unicode_Graphic_character-gc.M === gc.L|N|P|S|Zs|?Co? === -(gc.M|Zl|Zp|Cn|Cs|Cc|Cf|?Co?)]'
        return sf.std__Unicode_Base_character__exclude__Co | sf.ucd__gc__Private_Use
        return sf.ucd__gc__Letter | sf.ucd__gc__Number | sf.ucd__gc__Punctuation | sf.ucd__gc__Symbol | sf.ucd__gc__Space_Separator | sf.ucd__gc__Private_Use

    @cached_property
    def std__Unicode_Graphic_character__exclude__Co(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[Unicode_Graphic_character =[def]= gc.L|N|P|S|Zs|M|?Co? === -(gc.Zl|Zp|Cn|Cs|Cc|Cf|?Co?)]'
        return sf.std__Unicode_Base_character__exclude__Co | sf.ucd__gc__Mark
    @cached_property
    def std__Unicode_Base_character__exclude__Co(sf, /):
        r'-> IRanges/NonTouchRanges # ' \
        r'[Unicode_Base_character =[def]= Unicode_Graphic_character-gc.M === gc.L|N|P|S|Zs|?Co? === -(gc.M|Zl|Zp|Cn|Cs|Cc|Cf|?Co?)]'
        return sf.ucd__gc__Letter | sf.ucd__gc__Number | sf.ucd__gc__Punctuation | sf.ucd__gc__Symbol | sf.ucd__gc__Space_Separator

    ######################
    ######################
    ######################
#end:class UnicodeCharClass4Word4ver:

#253
#output:UnicodeCharClass4Word4ver<ver14_0_0>.iter_pairwise_cmp_all_available_char_classes(selected_nms, to_add_chars_if_sz_le=20)
cmp_result_ver14 = (
((('ucd__Emoji_Presentation__Y', 'ucd__Emoji__Y'), '__lt__', (1185, 1404))
,(('ucd__Emoji_Presentation__Y', 'ucd__Grapheme_Extend__Y'), 'disjoint', (1185, 2090))
,(('ucd__Emoji_Presentation__Y', 'ucd__Extended_Pictographic__Y'), '___', (1185, 3537), (31, 1154, 2383))
,(('ucd__Emoji_Presentation__Y', 'ucd__gc__Symbol'), '__lt__', (1185, 7741))
,(('ucd__Emoji_Presentation__Y', 'ucd__Ideographic__Y'), 'disjoint', (1185, 101661))
,(('ucd__Emoji_Presentation__Y', 'ucd__gc__Letter'), 'disjoint', (1185, 131756))
,(('ucd__Emoji_Presentation__Y', 'ucd__XID_Start__Y'), 'disjoint', (1185, 131974))
,(('ucd__Emoji_Presentation__Y', 'ucd__ID_Start__Y'), 'disjoint', (1185, 131997))
,(('ucd__Emoji_Presentation__Y', 'ucd__Alphabetic__Y'), 'disjoint', (1185, 133396))
,(('ucd__Emoji_Presentation__Y', 'pl__XPosixAlnum'), 'disjoint', (1185, 134056))
,(('ucd__Emoji_Presentation__Y', 'ucd__XID_Continue__Y'), 'disjoint', (1185, 135053))
,(('ucd__Emoji_Presentation__Y', 'ucd__ID_Continue__Y'), 'disjoint', (1185, 135072))
,(('ucd__Emoji_Presentation__Y', 'pl__XPosixWord'), 'disjoint', (1185, 135202))
,(('ucd__Emoji_Presentation__Y', 'std__Unicode_Base_character__exclude__Co'), '__lt__', (1185, 142124))
,(('ucd__Emoji_Presentation__Y', 'ucd__Grapheme_Base__Y'), '__lt__', (1185, 142539))
,(('ucd__Emoji_Presentation__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (1185, 144515))
,(('ucd__Emoji_Presentation__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (1185, 144532))
,(('ucd__Emoji_Presentation__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (1185, 144532))
,(('ucd__Emoji_Presentation__Y', 'std__Unicode_Base_character__include__Co'), '__lt__', (1185, 279592))
,(('ucd__Emoji_Presentation__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (1185, 282000))
,(('ucd__Emoji_Presentation__Y', 'pl__XPosixGraph'), '__lt__', (1185, 282146))
,(('ucd__Emoji_Presentation__Y', 'pl__XPosixPrint'), '__lt__', (1185, 282163))
,(('ucd__Emoji__Y', 'ucd__Grapheme_Extend__Y'), 'disjoint', (1404, 2090))
,(('ucd__Emoji__Y', 'ucd__Extended_Pictographic__Y'), '___', (1404, 3537), (43, 1361, 2176))
,(('ucd__Emoji__Y', 'ucd__gc__Symbol'), '___', (1404, 7741), (17, 1387, 6354), ('#*0123456789‼⁉ℹ〰〽', '', ''))
,(('ucd__Emoji__Y', 'ucd__Ideographic__Y'), 'disjoint', (1404, 101661))
,(('ucd__Emoji__Y', 'ucd__gc__Letter'), '___', (1404, 131756), (1403, 1, 131755), ('', 'ℹ', ''))
,(('ucd__Emoji__Y', 'ucd__XID_Start__Y'), '___', (1404, 131974), (1403, 1, 131973), ('', 'ℹ', ''))
,(('ucd__Emoji__Y', 'ucd__ID_Start__Y'), '___', (1404, 131997), (1403, 1, 131996), ('', 'ℹ', ''))
,(('ucd__Emoji__Y', 'ucd__Alphabetic__Y'), '___', (1404, 133396), (1398, 6, 133390), ('', 'ℹⓂ🅰🅱🅾🅿', ''))
,(('ucd__Emoji__Y', 'pl__XPosixAlnum'), '___', (1404, 134056), (1388, 16, 134040), ('', '0123456789ℹⓂ🅰🅱🅾🅿', ''))
,(('ucd__Emoji__Y', 'ucd__XID_Continue__Y'), '___', (1404, 135053), (1393, 11, 135042), ('', '0123456789ℹ', ''))
,(('ucd__Emoji__Y', 'ucd__ID_Continue__Y'), '___', (1404, 135072), (1393, 11, 135061), ('', '0123456789ℹ', ''))
,(('ucd__Emoji__Y', 'pl__XPosixWord'), '___', (1404, 135202), (1388, 16, 135186), ('', '0123456789ℹⓂ🅰🅱🅾🅿', ''))
,(('ucd__Emoji__Y', 'std__Unicode_Base_character__exclude__Co'), '__lt__', (1404, 142124))
,(('ucd__Emoji__Y', 'ucd__Grapheme_Base__Y'), '__lt__', (1404, 142539))
,(('ucd__Emoji__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (1404, 144515))
,(('ucd__Emoji__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (1404, 144532))
,(('ucd__Emoji__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (1404, 144532))
,(('ucd__Emoji__Y', 'std__Unicode_Base_character__include__Co'), '__lt__', (1404, 279592))
,(('ucd__Emoji__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (1404, 282000))
,(('ucd__Emoji__Y', 'pl__XPosixGraph'), '__lt__', (1404, 282146))
,(('ucd__Emoji__Y', 'pl__XPosixPrint'), '__lt__', (1404, 282163))
,(('ucd__Grapheme_Extend__Y', 'ucd__Extended_Pictographic__Y'), 'disjoint', (2090, 3537))
,(('ucd__Grapheme_Extend__Y', 'ucd__gc__Symbol'), 'disjoint', (2090, 7741))
,(('ucd__Grapheme_Extend__Y', 'ucd__Ideographic__Y'), '___', (2090, 101661), (2089, 1, 101660), ('', '𖿤', ''))
,(('ucd__Grapheme_Extend__Y', 'ucd__gc__Letter'), '___', (2090, 131756), (2088, 2, 131754), ('', 'ﾞﾟ', ''))
,(('ucd__Grapheme_Extend__Y', 'ucd__XID_Start__Y'), '___', (2090, 131974), (2088, 2, 131972), ('', 'ᢅᢆ', ''))
,(('ucd__Grapheme_Extend__Y', 'ucd__ID_Start__Y'), '___', (2090, 131997), (2086, 4, 131993), ('', 'ᢅᢆﾞﾟ', ''))
,(('ucd__Grapheme_Extend__Y', 'ucd__Alphabetic__Y'), '___', (2090, 133396), (1211, 879, 132517))
,(('ucd__Grapheme_Extend__Y', 'pl__XPosixAlnum'), '___', (2090, 134056), (1211, 879, 133177))
,(('ucd__Grapheme_Extend__Y', 'ucd__XID_Continue__Y'), '___', (2090, 135053), (110, 1980, 133073))
,(('ucd__Grapheme_Extend__Y', 'ucd__ID_Continue__Y'), '___', (2090, 135072), (110, 1980, 133092))
,(('ucd__Grapheme_Extend__Y', 'pl__XPosixWord'), '___', (2090, 135202), (96, 1994, 133208))
,(('ucd__Grapheme_Extend__Y', 'std__Unicode_Base_character__exclude__Co'), '___', (2090, 142124), (2088, 2, 142122), ('', 'ﾞﾟ', ''))
,(('ucd__Grapheme_Extend__Y', 'ucd__Grapheme_Base__Y'), 'disjoint', (2090, 142539))
,(('ucd__Grapheme_Extend__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '___', (2090, 144515), (97, 1993, 142522))
,(('ucd__Grapheme_Extend__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '___', (2090, 144532), (97, 1993, 142539))
,(('ucd__Grapheme_Extend__Y', 'std__Unicode_Graphic_character__exclude__Co'), '___', (2090, 144532), (97, 1993, 142539))
,(('ucd__Grapheme_Extend__Y', 'std__Unicode_Base_character__include__Co'), '___', (2090, 279592), (2088, 2, 279590), ('', 'ﾞﾟ', ''))
,(('ucd__Grapheme_Extend__Y', 'std__Unicode_Graphic_character__include__Co'), '___', (2090, 282000), (97, 1993, 280007))
,(('ucd__Grapheme_Extend__Y', 'pl__XPosixGraph'), '__lt__', (2090, 282146))
,(('ucd__Grapheme_Extend__Y', 'pl__XPosixPrint'), '__lt__', (2090, 282163))
,(('ucd__Extended_Pictographic__Y', 'ucd__gc__Symbol'), '___', (3537, 7741), (1530, 2007, 5734))
,(('ucd__Extended_Pictographic__Y', 'ucd__Ideographic__Y'), 'disjoint', (3537, 101661))
,(('ucd__Extended_Pictographic__Y', 'ucd__gc__Letter'), '___', (3537, 131756), (3536, 1, 131755), ('', 'ℹ', ''))
,(('ucd__Extended_Pictographic__Y', 'ucd__XID_Start__Y'), '___', (3537, 131974), (3536, 1, 131973), ('', 'ℹ', ''))
,(('ucd__Extended_Pictographic__Y', 'ucd__ID_Start__Y'), '___', (3537, 131997), (3536, 1, 131996), ('', 'ℹ', ''))
,(('ucd__Extended_Pictographic__Y', 'ucd__Alphabetic__Y'), '___', (3537, 133396), (3531, 6, 133390), ('', 'ℹⓂ🅰🅱🅾🅿', ''))
,(('ucd__Extended_Pictographic__Y', 'pl__XPosixAlnum'), '___', (3537, 134056), (3531, 6, 134050), ('', 'ℹⓂ🅰🅱🅾🅿', ''))
,(('ucd__Extended_Pictographic__Y', 'ucd__XID_Continue__Y'), '___', (3537, 135053), (3536, 1, 135052), ('', 'ℹ', ''))
,(('ucd__Extended_Pictographic__Y', 'ucd__ID_Continue__Y'), '___', (3537, 135072), (3536, 1, 135071), ('', 'ℹ', ''))
,(('ucd__Extended_Pictographic__Y', 'pl__XPosixWord'), '___', (3537, 135202), (3531, 6, 135196), ('', 'ℹⓂ🅰🅱🅾🅿', ''))
,(('ucd__Extended_Pictographic__Y', 'std__Unicode_Base_character__exclude__Co'), '___', (3537, 142124), (1525, 2012, 140112))
,(('ucd__Extended_Pictographic__Y', 'ucd__Grapheme_Base__Y'), '___', (3537, 142539), (1525, 2012, 140527))
,(('ucd__Extended_Pictographic__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '___', (3537, 144515), (1525, 2012, 142503))
,(('ucd__Extended_Pictographic__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '___', (3537, 144532), (1525, 2012, 142520))
,(('ucd__Extended_Pictographic__Y', 'std__Unicode_Graphic_character__exclude__Co'), '___', (3537, 144532), (1525, 2012, 142520))
,(('ucd__Extended_Pictographic__Y', 'std__Unicode_Base_character__include__Co'), '___', (3537, 279592), (1525, 2012, 277580))
,(('ucd__Extended_Pictographic__Y', 'std__Unicode_Graphic_character__include__Co'), '___', (3537, 282000), (1525, 2012, 279988))
,(('ucd__Extended_Pictographic__Y', 'pl__XPosixGraph'), '___', (3537, 282146), (1525, 2012, 280134))
,(('ucd__Extended_Pictographic__Y', 'pl__XPosixPrint'), '___', (3537, 282163), (1525, 2012, 280151))
,(('ucd__gc__Symbol', 'ucd__Ideographic__Y'), 'disjoint', (7741, 101661))
,(('ucd__gc__Symbol', 'ucd__gc__Letter'), 'disjoint', (7741, 131756))
,(('ucd__gc__Symbol', 'ucd__XID_Start__Y'), '___', (7741, 131974), (7739, 2, 131972), ('', '℘℮', ''))
,(('ucd__gc__Symbol', 'ucd__ID_Start__Y'), '___', (7741, 131997), (7737, 4, 131993), ('', '℘℮゛゜', ''))
,(('ucd__gc__Symbol', 'ucd__Alphabetic__Y'), '___', (7741, 133396), (7611, 130, 133266))
,(('ucd__gc__Symbol', 'pl__XPosixAlnum'), '___', (7741, 134056), (7611, 130, 133926))
,(('ucd__gc__Symbol', 'ucd__XID_Continue__Y'), '___', (7741, 135053), (7739, 2, 135051), ('', '℘℮', ''))
,(('ucd__gc__Symbol', 'ucd__ID_Continue__Y'), '___', (7741, 135072), (7737, 4, 135068), ('', '℘℮゛゜', ''))
,(('ucd__gc__Symbol', 'pl__XPosixWord'), '___', (7741, 135202), (7611, 130, 135072))
,(('ucd__gc__Symbol', 'std__Unicode_Base_character__exclude__Co'), '__lt__', (7741, 142124))
,(('ucd__gc__Symbol', 'ucd__Grapheme_Base__Y'), '__lt__', (7741, 142539))
,(('ucd__gc__Symbol', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (7741, 144515))
,(('ucd__gc__Symbol', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (7741, 144532))
,(('ucd__gc__Symbol', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (7741, 144532))
,(('ucd__gc__Symbol', 'std__Unicode_Base_character__include__Co'), '__lt__', (7741, 279592))
,(('ucd__gc__Symbol', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (7741, 282000))
,(('ucd__gc__Symbol', 'pl__XPosixGraph'), '__lt__', (7741, 282146))
,(('ucd__gc__Symbol', 'pl__XPosixPrint'), '__lt__', (7741, 282163))
,(('ucd__Ideographic__Y', 'ucd__gc__Letter'), '___', (101661, 131756), (14, 101647, 30109), ('〇〡〢〣〤〥〦〧〨〩〸〹〺𖿤', '', ''))
,(('ucd__Ideographic__Y', 'ucd__XID_Start__Y'), '___', (101661, 131974), (1, 101660, 30314), ('𖿤', '', ''))
,(('ucd__Ideographic__Y', 'ucd__ID_Start__Y'), '___', (101661, 131997), (1, 101660, 30337), ('𖿤', '', ''))
,(('ucd__Ideographic__Y', 'ucd__Alphabetic__Y'), '___', (101661, 133396), (1, 101660, 31736), ('𖿤', '', ''))
,(('ucd__Ideographic__Y', 'pl__XPosixAlnum'), '___', (101661, 134056), (1, 101660, 32396), ('𖿤', '', ''))
,(('ucd__Ideographic__Y', 'ucd__XID_Continue__Y'), '__lt__', (101661, 135053))
,(('ucd__Ideographic__Y', 'ucd__ID_Continue__Y'), '__lt__', (101661, 135072))
,(('ucd__Ideographic__Y', 'pl__XPosixWord'), '__lt__', (101661, 135202))
,(('ucd__Ideographic__Y', 'std__Unicode_Base_character__exclude__Co'), '___', (101661, 142124), (1, 101660, 40464), ('𖿤', '', ''))
,(('ucd__Ideographic__Y', 'ucd__Grapheme_Base__Y'), '___', (101661, 142539), (1, 101660, 40879), ('𖿤', '', ''))
,(('ucd__Ideographic__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (101661, 144515))
,(('ucd__Ideographic__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (101661, 144532))
,(('ucd__Ideographic__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (101661, 144532))
,(('ucd__Ideographic__Y', 'std__Unicode_Base_character__include__Co'), '___', (101661, 279592), (1, 101660, 177932), ('𖿤', '', ''))
,(('ucd__Ideographic__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (101661, 282000))
,(('ucd__Ideographic__Y', 'pl__XPosixGraph'), '__lt__', (101661, 282146))
,(('ucd__Ideographic__Y', 'pl__XPosixPrint'), '__lt__', (101661, 282163))
,(('ucd__gc__Letter', 'ucd__XID_Start__Y'), '___', (131756, 131974), (22, 131734, 240))
,(('ucd__gc__Letter', 'ucd__ID_Start__Y'), '___', (131756, 131997), (1, 131755, 242), ('ⸯ', '', ''))
,(('ucd__gc__Letter', 'ucd__Alphabetic__Y'), '__lt__', (131756, 133396))
,(('ucd__gc__Letter', 'pl__XPosixAlnum'), '__lt__', (131756, 134056))
,(('ucd__gc__Letter', 'ucd__XID_Continue__Y'), '___', (131756, 135053), (18, 131738, 3315), ('ͺⸯﱞﱟﱠﱡﱢﱣﷺﷻﹰﹲﹴﹶﹸﹺﹼﹾ', '', ''))
,(('ucd__gc__Letter', 'ucd__ID_Continue__Y'), '___', (131756, 135072), (1, 131755, 3317), ('ⸯ', '', ''))
,(('ucd__gc__Letter', 'pl__XPosixWord'), '__lt__', (131756, 135202))
,(('ucd__gc__Letter', 'std__Unicode_Base_character__exclude__Co'), '__lt__', (131756, 142124))
,(('ucd__gc__Letter', 'ucd__Grapheme_Base__Y'), '___', (131756, 142539), (2, 131754, 10785), ('ﾞﾟ', '', ''))
,(('ucd__gc__Letter', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (131756, 144515))
,(('ucd__gc__Letter', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (131756, 144532))
,(('ucd__gc__Letter', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (131756, 144532))
,(('ucd__gc__Letter', 'std__Unicode_Base_character__include__Co'), '__lt__', (131756, 279592))
,(('ucd__gc__Letter', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (131756, 282000))
,(('ucd__gc__Letter', 'pl__XPosixGraph'), '__lt__', (131756, 282146))
,(('ucd__gc__Letter', 'pl__XPosixPrint'), '__lt__', (131756, 282163))
,(('ucd__XID_Start__Y', 'ucd__ID_Start__Y'), '__lt__', (131974, 131997))
,(('ucd__XID_Start__Y', 'ucd__Alphabetic__Y'), '___', (131974, 133396), (2, 131972, 1424), ('℘℮', '', ''))
,(('ucd__XID_Start__Y', 'pl__XPosixAlnum'), '___', (131974, 134056), (2, 131972, 2084), ('℘℮', '', ''))
,(('ucd__XID_Start__Y', 'ucd__XID_Continue__Y'), '__lt__', (131974, 135053))
,(('ucd__XID_Start__Y', 'ucd__ID_Continue__Y'), '__lt__', (131974, 135072))
,(('ucd__XID_Start__Y', 'pl__XPosixWord'), '___', (131974, 135202), (2, 131972, 3230), ('℘℮', '', ''))
,(('ucd__XID_Start__Y', 'std__Unicode_Base_character__exclude__Co'), '___', (131974, 142124), (2, 131972, 10152), ('ᢅᢆ', '', ''))
,(('ucd__XID_Start__Y', 'ucd__Grapheme_Base__Y'), '___', (131974, 142539), (2, 131972, 10567), ('ᢅᢆ', '', ''))
,(('ucd__XID_Start__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (131974, 144515))
,(('ucd__XID_Start__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (131974, 144532))
,(('ucd__XID_Start__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (131974, 144532))
,(('ucd__XID_Start__Y', 'std__Unicode_Base_character__include__Co'), '___', (131974, 279592), (2, 131972, 147620), ('ᢅᢆ', '', ''))
,(('ucd__XID_Start__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (131974, 282000))
,(('ucd__XID_Start__Y', 'pl__XPosixGraph'), '__lt__', (131974, 282146))
,(('ucd__XID_Start__Y', 'pl__XPosixPrint'), '__lt__', (131974, 282163))
,(('ucd__ID_Start__Y', 'ucd__Alphabetic__Y'), '___', (131997, 133396), (4, 131993, 1403), ('℘℮゛゜', '', ''))
,(('ucd__ID_Start__Y', 'pl__XPosixAlnum'), '___', (131997, 134056), (4, 131993, 2063), ('℘℮゛゜', '', ''))
,(('ucd__ID_Start__Y', 'ucd__XID_Continue__Y'), '___', (131997, 135053), (19, 131978, 3075), ('ͺ゛゜ﱞﱟﱠﱡﱢﱣﷺﷻﹰﹲﹴﹶﹸﹺﹼﹾ', '', ''))
,(('ucd__ID_Start__Y', 'ucd__ID_Continue__Y'), '__lt__', (131997, 135072))
,(('ucd__ID_Start__Y', 'pl__XPosixWord'), '___', (131997, 135202), (4, 131993, 3209), ('℘℮゛゜', '', ''))
,(('ucd__ID_Start__Y', 'std__Unicode_Base_character__exclude__Co'), '___', (131997, 142124), (2, 131995, 10129), ('ᢅᢆ', '', ''))
,(('ucd__ID_Start__Y', 'ucd__Grapheme_Base__Y'), '___', (131997, 142539), (4, 131993, 10546), ('ᢅᢆﾞﾟ', '', ''))
,(('ucd__ID_Start__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (131997, 144515))
,(('ucd__ID_Start__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (131997, 144532))
,(('ucd__ID_Start__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (131997, 144532))
,(('ucd__ID_Start__Y', 'std__Unicode_Base_character__include__Co'), '___', (131997, 279592), (2, 131995, 147597), ('ᢅᢆ', '', ''))
,(('ucd__ID_Start__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (131997, 282000))
,(('ucd__ID_Start__Y', 'pl__XPosixGraph'), '__lt__', (131997, 282146))
,(('ucd__ID_Start__Y', 'pl__XPosixPrint'), '__lt__', (131997, 282163))
,(('ucd__Alphabetic__Y', 'pl__XPosixAlnum'), '__lt__', (133396, 134056))
,(('ucd__Alphabetic__Y', 'ucd__XID_Continue__Y'), '___', (133396, 135053), (148, 133248, 1805))
,(('ucd__Alphabetic__Y', 'ucd__ID_Continue__Y'), '___', (133396, 135072), (131, 133265, 1807))
,(('ucd__Alphabetic__Y', 'pl__XPosixWord'), '__lt__', (133396, 135202))
,(('ucd__Alphabetic__Y', 'std__Unicode_Base_character__exclude__Co'), '___', (133396, 142124), (1274, 132122, 10002))
,(('ucd__Alphabetic__Y', 'ucd__Grapheme_Base__Y'), '___', (133396, 142539), (879, 132517, 10022))
,(('ucd__Alphabetic__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (133396, 144515))
,(('ucd__Alphabetic__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (133396, 144532))
,(('ucd__Alphabetic__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (133396, 144532))
,(('ucd__Alphabetic__Y', 'std__Unicode_Base_character__include__Co'), '___', (133396, 279592), (1274, 132122, 147470))
,(('ucd__Alphabetic__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (133396, 282000))
,(('ucd__Alphabetic__Y', 'pl__XPosixGraph'), '__lt__', (133396, 282146))
,(('ucd__Alphabetic__Y', 'pl__XPosixPrint'), '__lt__', (133396, 282163))
,(('pl__XPosixAlnum', 'ucd__XID_Continue__Y'), '___', (134056, 135053), (148, 133908, 1145))
,(('pl__XPosixAlnum', 'ucd__ID_Continue__Y'), '___', (134056, 135072), (131, 133925, 1147))
,(('pl__XPosixAlnum', 'pl__XPosixWord'), '__lt__', (134056, 135202))
,(('pl__XPosixAlnum', 'std__Unicode_Base_character__exclude__Co'), '___', (134056, 142124), (1274, 132782, 9342))
,(('pl__XPosixAlnum', 'ucd__Grapheme_Base__Y'), '___', (134056, 142539), (879, 133177, 9362))
,(('pl__XPosixAlnum', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (134056, 144515))
,(('pl__XPosixAlnum', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (134056, 144532))
,(('pl__XPosixAlnum', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (134056, 144532))
,(('pl__XPosixAlnum', 'std__Unicode_Base_character__include__Co'), '___', (134056, 279592), (1274, 132782, 146810))
,(('pl__XPosixAlnum', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (134056, 282000))
,(('pl__XPosixAlnum', 'pl__XPosixGraph'), '__lt__', (134056, 282146))
,(('pl__XPosixAlnum', 'pl__XPosixPrint'), '__lt__', (134056, 282163))
,(('ucd__XID_Continue__Y', 'ucd__ID_Continue__Y'), '__lt__', (135053, 135072))
,(('ucd__XID_Continue__Y', 'pl__XPosixWord'), '___', (135053, 135202), (14, 135039, 163), ('··፩፪፫፬፭፮፯፰፱᧚℘℮', '', ''))
,(('ucd__XID_Continue__Y', 'std__Unicode_Base_character__exclude__Co'), '___', (135053, 142124), (2395, 132658, 9466))
,(('ucd__XID_Continue__Y', 'ucd__Grapheme_Base__Y'), '___', (135053, 142539), (1980, 133073, 9466))
,(('ucd__XID_Continue__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (135053, 144515))
,(('ucd__XID_Continue__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (135053, 144532))
,(('ucd__XID_Continue__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (135053, 144532))
,(('ucd__XID_Continue__Y', 'std__Unicode_Base_character__include__Co'), '___', (135053, 279592), (2395, 132658, 146934))
,(('ucd__XID_Continue__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (135053, 282000))
,(('ucd__XID_Continue__Y', 'pl__XPosixGraph'), '__lt__', (135053, 282146))
,(('ucd__XID_Continue__Y', 'pl__XPosixPrint'), '__lt__', (135053, 282163))
,(('ucd__ID_Continue__Y', 'pl__XPosixWord'), '___', (135072, 135202), (16, 135056, 146), ('··፩፪፫፬፭፮፯፰፱᧚℘℮゛゜', '', ''))
,(('ucd__ID_Continue__Y', 'std__Unicode_Base_character__exclude__Co'), '___', (135072, 142124), (2395, 132677, 9447))
,(('ucd__ID_Continue__Y', 'ucd__Grapheme_Base__Y'), '___', (135072, 142539), (1980, 133092, 9447))
,(('ucd__ID_Continue__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '__lt__', (135072, 144515))
,(('ucd__ID_Continue__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (135072, 144532))
,(('ucd__ID_Continue__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (135072, 144532))
,(('ucd__ID_Continue__Y', 'std__Unicode_Base_character__include__Co'), '___', (135072, 279592), (2395, 132677, 146915))
,(('ucd__ID_Continue__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (135072, 282000))
,(('ucd__ID_Continue__Y', 'pl__XPosixGraph'), '__lt__', (135072, 282146))
,(('ucd__ID_Continue__Y', 'pl__XPosixPrint'), '__lt__', (135072, 282163))
,(('pl__XPosixWord', 'std__Unicode_Base_character__exclude__Co'), '___', (135202, 142124), (2410, 132792, 9332))
,(('pl__XPosixWord', 'ucd__Grapheme_Base__Y'), '___', (135202, 142539), (1995, 133207, 9332))
,(('pl__XPosixWord', 'pl__XPosixGraph__exclude__Co_Cf'), '___', (135202, 144515), (2, 135200, 9315), ('\u200c\u200d', '', ''))
,(('pl__XPosixWord', 'pl__XPosixPrint__exclude__Co_Cf'), '___', (135202, 144532), (2, 135200, 9332), ('\u200c\u200d', '', ''))
,(('pl__XPosixWord', 'std__Unicode_Graphic_character__exclude__Co'), '___', (135202, 144532), (2, 135200, 9332), ('\u200c\u200d', '', ''))
,(('pl__XPosixWord', 'std__Unicode_Base_character__include__Co'), '___', (135202, 279592), (2410, 132792, 146800))
,(('pl__XPosixWord', 'std__Unicode_Graphic_character__include__Co'), '___', (135202, 282000), (2, 135200, 146800), ('\u200c\u200d', '', ''))
,(('pl__XPosixWord', 'pl__XPosixGraph'), '__lt__', (135202, 282146))
,(('pl__XPosixWord', 'pl__XPosixPrint'), '__lt__', (135202, 282163))
,(('std__Unicode_Base_character__exclude__Co', 'ucd__Grapheme_Base__Y'), '___', (142124, 142539), (2, 142122, 417), ('ﾞﾟ', '', ''))
,(('std__Unicode_Base_character__exclude__Co', 'pl__XPosixGraph__exclude__Co_Cf'), '___', (142124, 144515), (17, 142107, 2408), (' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000', '', ''))
,(('std__Unicode_Base_character__exclude__Co', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (142124, 144532))
,(('std__Unicode_Base_character__exclude__Co', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (142124, 144532))
,(('std__Unicode_Base_character__exclude__Co', 'std__Unicode_Base_character__include__Co'), '__lt__', (142124, 279592))
,(('std__Unicode_Base_character__exclude__Co', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (142124, 282000))
,(('std__Unicode_Base_character__exclude__Co', 'pl__XPosixGraph'), '___', (142124, 282146), (17, 142107, 140039), (' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000', '', ''))
,(('std__Unicode_Base_character__exclude__Co', 'pl__XPosixPrint'), '__lt__', (142124, 282163))
,(('ucd__Grapheme_Base__Y', 'pl__XPosixGraph__exclude__Co_Cf'), '___', (142539, 144515), (17, 142522, 1993), (' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000', '', ''))
,(('ucd__Grapheme_Base__Y', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (142539, 144532))
,(('ucd__Grapheme_Base__Y', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (142539, 144532))
,(('ucd__Grapheme_Base__Y', 'std__Unicode_Base_character__include__Co'), '___', (142539, 279592), (417, 142122, 137470))
,(('ucd__Grapheme_Base__Y', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (142539, 282000))
,(('ucd__Grapheme_Base__Y', 'pl__XPosixGraph'), '___', (142539, 282146), (17, 142522, 139624), (' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000', '', ''))
,(('ucd__Grapheme_Base__Y', 'pl__XPosixPrint'), '__lt__', (142539, 282163))
,(('pl__XPosixGraph__exclude__Co_Cf', 'pl__XPosixPrint__exclude__Co_Cf'), '__lt__', (144515, 144532))
,(('pl__XPosixGraph__exclude__Co_Cf', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (144515, 144532))
,(('pl__XPosixGraph__exclude__Co_Cf', 'std__Unicode_Base_character__include__Co'), '___', (144515, 279592), (2408, 142107, 137485))
,(('pl__XPosixGraph__exclude__Co_Cf', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (144515, 282000))
,(('pl__XPosixGraph__exclude__Co_Cf', 'pl__XPosixGraph'), '__lt__', (144515, 282146))
,(('pl__XPosixGraph__exclude__Co_Cf', 'pl__XPosixPrint'), '__lt__', (144515, 282163))
,(('pl__XPosixPrint__exclude__Co_Cf', 'std__Unicode_Graphic_character__exclude__Co'), '__lt__', (144532, 144532))
,(('pl__XPosixPrint__exclude__Co_Cf', 'std__Unicode_Base_character__include__Co'), '___', (144532, 279592), (2408, 142124, 137468))
,(('pl__XPosixPrint__exclude__Co_Cf', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (144532, 282000))
,(('pl__XPosixPrint__exclude__Co_Cf', 'pl__XPosixGraph'), '___', (144532, 282146), (17, 144515, 137631), (' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000', '', ''))
,(('pl__XPosixPrint__exclude__Co_Cf', 'pl__XPosixPrint'), '__lt__', (144532, 282163))
,(('std__Unicode_Graphic_character__exclude__Co', 'std__Unicode_Base_character__include__Co'), '___', (144532, 279592), (2408, 142124, 137468))
,(('std__Unicode_Graphic_character__exclude__Co', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (144532, 282000))
,(('std__Unicode_Graphic_character__exclude__Co', 'pl__XPosixGraph'), '___', (144532, 282146), (17, 144515, 137631), (' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000', '', ''))
,(('std__Unicode_Graphic_character__exclude__Co', 'pl__XPosixPrint'), '__lt__', (144532, 282163))
,(('std__Unicode_Base_character__include__Co', 'std__Unicode_Graphic_character__include__Co'), '__lt__', (279592, 282000))
,(('std__Unicode_Base_character__include__Co', 'pl__XPosixGraph'), '___', (279592, 282146), (17, 279575, 2571), (' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000', '', ''))
,(('std__Unicode_Base_character__include__Co', 'pl__XPosixPrint'), '__lt__', (279592, 282163))
,(('std__Unicode_Graphic_character__include__Co', 'pl__XPosixGraph'), '___', (282000, 282146), (17, 281983, 163), (' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000', '', ''))
,(('std__Unicode_Graphic_character__include__Co', 'pl__XPosixPrint'), '__lt__', (282000, 282163))
,(('pl__XPosixGraph', 'pl__XPosixPrint'), '__lt__', (282146, 282163))
))
#253
__all__
from script.unicode.unicode_char_class4word import UnicodeCharClass4Word4ver
from script.unicode.unicode_char_class4word import *
