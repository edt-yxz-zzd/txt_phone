#__all__:goto
r'''[[[
e script/unicode/unicode_paired.py


script.unicode.unicode_paired
py -m nn_ns.app.debug_cmd   script.unicode.unicode_paired -x
py -m nn_ns.app.doctest_cmd script.unicode.unicode_paired:__doc__ -ht



[[
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/xml/ver14_0_0/gc.General_Category.ver14_0_0.xml.out.txt
Ps = Punctuation, open
Pe = Punctuation, close
Pi = Punctuation, initial quote (may behave like Ps or Pe depending on usage)
Pf = Punctuation, final quote (may behave like Ps or Pe depending on usage)

,'Ps'

,'Pe'

,'Pf'

,'Pi'



]]

[[
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ucd_ver14_0/PropertyAliases.txt
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyValueAliases_txt.py.out.ver14_0_0.txt

# Miscellaneous Properties
bmg                      ; Bidi_Mirroring_Glyph
{''
: ...
,'0028'
: {0x29: 1}
,'0029'
: {0x28: 1}
... ...
,'FF63'
: {0xFF62: 1}
}
bpb                      ; Bidi_Paired_Bracket
c/close:
o/open:


# Enumerated Properties
bpt                      ; Bidi_Paired_Bracket_Type
   ,'bpt' : ['c' ,'n' ,'o' ]
bc                       ; Bidi_Class
   ,'bc' : ['AL' ,'AN' ,'B' ,'BN' ,'CS' ,'EN' ,'ES' ,'ET' ,'FSI' ,'L' ,'LRE' ,'LRI' ,'LRO' ,'NSM' ,'ON' ,'PDF' ,'PDI' ,'R' ,'RLE' ,'RLI' ,'RLO' ,'S' ,'WS' ]

# Binary Properties
Bidi_C                   ; Bidi_Control
:
Bidi_M                   ; Bidi_Mirrored
:
]]

[[
]]



[[
weird:
Ps:
'SINGLE LOW-9 QUOTATION MARK'
'DOUBLE LOW-9 QUOTATION MARK'
'DOUBLE LOW-REVERSED-9 QUOTATION MARK'
Pi:
'SINGLE HIGH-REVERSED-9 QUOTATION MARK'
'DOUBLE HIGH-REVERSED-9 QUOTATION MARK'
===
===
py_adhoc_call   script.unicode.unicode_paired   @_gc__Ps_Pe_Pi_Pf_
===
... ...
'([{༺༼᚛‚„⁅⁽₍⌈⌊〈❨❪❬❮❰❲❴⟅⟦⟨⟪⟬⟮⦃⦅⦇⦉⦋⦍⦏⦑⦓⦕⦗⧘⧚⧼⸢⸤⸦⸨⹂����〈《「『【〔〖〘〚〝﴿︗︵︷︹︻︽︿﹁﹃﹇﹙﹛﹝（［｛｟｢'
'LEFT PARENTHESIS'
'LEFT SQUARE BRACKET'
'LEFT CURLY BRACKET'
'TIBETAN MARK GUG RTAGS GYON'
'TIBETAN MARK ANG KHANG GYON'
'OGHAM FEATHER MARK'
'SINGLE LOW-9 QUOTATION MARK'
'DOUBLE LOW-9 QUOTATION MARK'
'LEFT SQUARE BRACKET WITH QUILL'
'SUPERSCRIPT LEFT PARENTHESIS'
'SUBSCRIPT LEFT PARENTHESIS'
'LEFT CEILING'
'LEFT FLOOR'
'LEFT-POINTING ANGLE BRACKET'
'MEDIUM LEFT PARENTHESIS ORNAMENT'
'MEDIUM FLATTENED LEFT PARENTHESIS ORNAMENT'
'MEDIUM LEFT-POINTING ANGLE BRACKET ORNAMENT'
'HEAVY LEFT-POINTING ANGLE QUOTATION MARK ORNAMENT'
'HEAVY LEFT-POINTING ANGLE BRACKET ORNAMENT'
'LIGHT LEFT TORTOISE SHELL BRACKET ORNAMENT'
'MEDIUM LEFT CURLY BRACKET ORNAMENT'
'LEFT S-SHAPED BAG DELIMITER'
'MATHEMATICAL LEFT WHITE SQUARE BRACKET'
'MATHEMATICAL LEFT ANGLE BRACKET'
'MATHEMATICAL LEFT DOUBLE ANGLE BRACKET'
'MATHEMATICAL LEFT WHITE TORTOISE SHELL BRACKET'
'MATHEMATICAL LEFT FLATTENED PARENTHESIS'
'LEFT WHITE CURLY BRACKET'
'LEFT WHITE PARENTHESIS'
'Z NOTATION LEFT IMAGE BRACKET'
'Z NOTATION LEFT BINDING BRACKET'
'LEFT SQUARE BRACKET WITH UNDERBAR'
'LEFT SQUARE BRACKET WITH TICK IN TOP CORNER'
'LEFT SQUARE BRACKET WITH TICK IN BOTTOM CORNER'
'LEFT ANGLE BRACKET WITH DOT'
'LEFT ARC LESS-THAN BRACKET'
'DOUBLE LEFT ARC GREATER-THAN BRACKET'
'LEFT BLACK TORTOISE SHELL BRACKET'
'LEFT WIGGLY FENCE'
'LEFT DOUBLE WIGGLY FENCE'
'LEFT-POINTING CURVED ANGLE BRACKET'
'TOP LEFT HALF BRACKET'
'BOTTOM LEFT HALF BRACKET'
'LEFT SIDEWAYS U BRACKET'
'LEFT DOUBLE PARENTHESIS'
'DOUBLE LOW-REVERSED-9 QUOTATION MARK'
'LEFT SQUARE BRACKET WITH STROKE'
'LEFT SQUARE BRACKET WITH DOUBLE STROKE'
'TOP HALF LEFT PARENTHESIS'
'BOTTOM HALF LEFT PARENTHESIS'
'LEFT ANGLE BRACKET'
'LEFT DOUBLE ANGLE BRACKET'
'LEFT CORNER BRACKET'
'LEFT WHITE CORNER BRACKET'
'LEFT BLACK LENTICULAR BRACKET'
'LEFT TORTOISE SHELL BRACKET'
'LEFT WHITE LENTICULAR BRACKET'
'LEFT WHITE TORTOISE SHELL BRACKET'
'LEFT WHITE SQUARE BRACKET'
'REVERSED DOUBLE PRIME QUOTATION MARK'
'ORNATE RIGHT PARENTHESIS'
'PRESENTATION FORM FOR VERTICAL LEFT WHITE LENTICULAR BRACKET'
'PRESENTATION FORM FOR VERTICAL LEFT PARENTHESIS'
'PRESENTATION FORM FOR VERTICAL LEFT CURLY BRACKET'
'PRESENTATION FORM FOR VERTICAL LEFT TORTOISE SHELL BRACKET'
'PRESENTATION FORM FOR VERTICAL LEFT BLACK LENTICULAR BRACKET'
'PRESENTATION FORM FOR VERTICAL LEFT DOUBLE ANGLE BRACKET'
'PRESENTATION FORM FOR VERTICAL LEFT ANGLE BRACKET'
'PRESENTATION FORM FOR VERTICAL LEFT CORNER BRACKET'
'PRESENTATION FORM FOR VERTICAL LEFT WHITE CORNER BRACKET'
'PRESENTATION FORM FOR VERTICAL LEFT SQUARE BRACKET'
'SMALL LEFT PARENTHESIS'
'SMALL LEFT CURLY BRACKET'
'SMALL LEFT TORTOISE SHELL BRACKET'
'FULLWIDTH LEFT PARENTHESIS'
'FULLWIDTH LEFT SQUARE BRACKET'
'FULLWIDTH LEFT CURLY BRACKET'
'FULLWIDTH LEFT WHITE PARENTHESIS'
'HALFWIDTH LEFT CORNER BRACKET'
')]}༻༽᚜⁆⁾₎⌉⌋〉❩❫❭❯❱❳❵⟆⟧⟩⟫⟭⟯⦄⦆⦈⦊⦌⦎⦐⦒⦔⦖⦘⧙⧛⧽⸣⸥⸧⸩����〉》 」』】〕〗〙〛〞〟﴾︘︶︸︺︼︾﹀﹂﹄﹈﹚﹜﹞）］｝｠｣'
'RIGHT PARENTHESIS'
'RIGHT SQUARE BRACKET'
'RIGHT CURLY BRACKET'
'TIBETAN MARK GUG RTAGS GYAS'
'TIBETAN MARK ANG KHANG GYAS'
'OGHAM REVERSED FEATHER MARK'
'RIGHT SQUARE BRACKET WITH QUILL'
'SUPERSCRIPT RIGHT PARENTHESIS'
'SUBSCRIPT RIGHT PARENTHESIS'
'RIGHT CEILING'
'RIGHT FLOOR'
'RIGHT-POINTING ANGLE BRACKET'
'MEDIUM RIGHT PARENTHESIS ORNAMENT'
'MEDIUM FLATTENED RIGHT PARENTHESIS ORNAMENT'
'MEDIUM RIGHT-POINTING ANGLE BRACKET ORNAMENT'
'HEAVY RIGHT-POINTING ANGLE QUOTATION MARK ORNAMENT'
'HEAVY RIGHT-POINTING ANGLE BRACKET ORNAMENT'
'LIGHT RIGHT TORTOISE SHELL BRACKET ORNAMENT'
'MEDIUM RIGHT CURLY BRACKET ORNAMENT'
'RIGHT S-SHAPED BAG DELIMITER'
'MATHEMATICAL RIGHT WHITE SQUARE BRACKET'
'MATHEMATICAL RIGHT ANGLE BRACKET'
'MATHEMATICAL RIGHT DOUBLE ANGLE BRACKET'
'MATHEMATICAL RIGHT WHITE TORTOISE SHELL BRACKET'
'MATHEMATICAL RIGHT FLATTENED PARENTHESIS'
'RIGHT WHITE CURLY BRACKET'
'RIGHT WHITE PARENTHESIS'
'Z NOTATION RIGHT IMAGE BRACKET'
'Z NOTATION RIGHT BINDING BRACKET'
'RIGHT SQUARE BRACKET WITH UNDERBAR'
'RIGHT SQUARE BRACKET WITH TICK IN BOTTOM CORNER'
'RIGHT SQUARE BRACKET WITH TICK IN TOP CORNER'
'RIGHT ANGLE BRACKET WITH DOT'
'RIGHT ARC GREATER-THAN BRACKET'
'DOUBLE RIGHT ARC LESS-THAN BRACKET'
'RIGHT BLACK TORTOISE SHELL BRACKET'
'RIGHT WIGGLY FENCE'
'RIGHT DOUBLE WIGGLY FENCE'
'RIGHT-POINTING CURVED ANGLE BRACKET'
'TOP RIGHT HALF BRACKET'
'BOTTOM RIGHT HALF BRACKET'
'RIGHT SIDEWAYS U BRACKET'
'RIGHT DOUBLE PARENTHESIS'
'RIGHT SQUARE BRACKET WITH STROKE'
'RIGHT SQUARE BRACKET WITH DOUBLE STROKE'
'TOP HALF RIGHT PARENTHESIS'
'BOTTOM HALF RIGHT PARENTHESIS'
'RIGHT ANGLE BRACKET'
'RIGHT DOUBLE ANGLE BRACKET'
'RIGHT CORNER BRACKET'
'RIGHT WHITE CORNER BRACKET'
'RIGHT BLACK LENTICULAR BRACKET'
'RIGHT TORTOISE SHELL BRACKET'
'RIGHT WHITE LENTICULAR BRACKET'
'RIGHT WHITE TORTOISE SHELL BRACKET'
'RIGHT WHITE SQUARE BRACKET'
'DOUBLE PRIME QUOTATION MARK'
'LOW DOUBLE PRIME QUOTATION MARK'
'ORNATE LEFT PARENTHESIS'
'PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET'
'PRESENTATION FORM FOR VERTICAL RIGHT PARENTHESIS'
'PRESENTATION FORM FOR VERTICAL RIGHT CURLY BRACKET'
'PRESENTATION FORM FOR VERTICAL RIGHT TORTOISE SHELL BRACKET'
'PRESENTATION FORM FOR VERTICAL RIGHT BLACK LENTICULAR BRACKET'
'PRESENTATION FORM FOR VERTICAL RIGHT DOUBLE ANGLE BRACKET'
'PRESENTATION FORM FOR VERTICAL RIGHT ANGLE BRACKET'
'PRESENTATION FORM FOR VERTICAL RIGHT CORNER BRACKET' 'PRESENTATION FORM FOR VERTICAL RIGHT WHITE CORNER BRACKET'
'PRESENTATION FORM FOR VERTICAL RIGHT SQUARE BRACKET' 'SMALL RIGHT PARENTHESIS'
'SMALL RIGHT CURLY BRACKET'
'SMALL RIGHT TORTOISE SHELL BRACKET'
'FULLWIDTH RIGHT PARENTHESIS'
'FULLWIDTH RIGHT SQUARE BRACKET'
'FULLWIDTH RIGHT CURLY BRACKET'
'FULLWIDTH RIGHT WHITE PARENTHESIS'
'HALFWIDTH RIGHT CORNER BRACKET'
'«‘‛“‟‹⸂⸄⸉⸌⸜⸠'
'LEFT-POINTING DOUBLE ANGLE QUOTATION MARK'
'LEFT SINGLE QUOTATION MARK'
'SINGLE HIGH-REVERSED-9 QUOTATION MARK'
'LEFT DOUBLE QUOTATION MARK'
'DOUBLE HIGH-REVERSED-9 QUOTATION MARK'
'SINGLE LEFT-POINTING ANGLE QUOTATION MARK'
'LEFT SUBSTITUTION BRACKET'
'LEFT DOTTED SUBSTITUTION BRACKET'
'LEFT TRANSPOSITION BRACKET'
'LEFT RAISED OMISSION BRACKET'
'LEFT LOW PARAPHRASE BRACKET'
'LEFT VERTICAL BAR WITH QUILL'
'»’”›⸃⸅⸊⸍⸝⸡'
'RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK'
'RIGHT SINGLE QUOTATION MARK'
'RIGHT DOUBLE QUOTATION MARK'
'SINGLE RIGHT-POINTING ANGLE QUOTATION MARK'
'RIGHT SUBSTITUTION BRACKET'
'RIGHT DOTTED SUBSTITUTION BRACKET'
'RIGHT TRANSPOSITION BRACKET'
'RIGHT RAISED OMISSION BRACKET'
'RIGHT LOW PARAPHRASE BRACKET'
'RIGHT VERTICAL BAR WITH QUILL'

]]



from script.unicode.unicode_paired import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__
#from seed.data_funcs.rngs import make_Ranges, sorted_rngs_to_iter_nontouch_ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
    #TouchRangeBasedIntMapping.from_value2begin2sz/.from_rng_value_pairs/.from_clone_of_rngs_with_default
from seed.data_funcs.rngs import IRanges
    #for:.from_hexXhexszpair_list/.from_hex_repr_pair_list/.from_len_rng2hexbegins/.from_len_rng2begin_chars/.from_char_pairs__str/.from_hex_sz_pair_list/.from_hex2sz
#from seed.data_funcs.rngs import NonTouchRanges, TouchRanges, make_NonTouchRanges, make_TouchRanges
#from seed.data_funcs.rngs import len_of__rng, len_of__rng__neg_as0

from nn_ns.CJK.unicode.ucd_unihan.xml.resource_loader import data_loader4depth2__literal_eval__u8 as _load
import unicodedata as U

_v14 = _load.ver14_0_0

def pa_va2Ranges(pa, va, /):
    (va2hx2sz, ichr2va) = getattr(_v14, pa)
    hx2sz = va2hx2sz[va]
    ranges = IRanges.from_hex2sz(hx2sz)
    return ranges
    #ranges.to_hexXhexszpair_list()

def chars5Ranges(ranges, /):
    chars = ''.join(map(chr, ranges.iter_ints_(reverse=False)))
    return chars

def print_names5chars(cs, /):
    for ch in cs:
        print_repr(U.name(ch))

def print_repr(x, /):
    print(repr(x))

def gc2Ranges(gc, /):
    return pa_va2Ranges('gc', gc)

def _gc__Ps_Pe_Pi_Pf_():
    cs4Ps = chars5Ranges(gc2Ranges('Ps'))
    '([{༺༼᚛‚„⁅⁽₍⌈⌊〈❨❪❬❮❰❲❴⟅⟦⟨⟪⟬⟮⦃⦅⦇⦉⦋⦍⦏⦑⦓⦕⦗⧘⧚⧼⸢⸤⸦⸨⹂����〈《「『【〔〖〘〚〝﴿︗︵︷︹︻︽︿﹁﹃﹇﹙﹛﹝（［｛｟｢'
    cs4Pe = chars5Ranges(gc2Ranges('Pe'))
    ')]}༻༽᚜⁆⁾₎⌉⌋〉❩❫❭❯❱❳❵⟆⟧⟩⟫⟭⟯⦄⦆⦈⦊⦌⦎⦐⦒⦔⦖⦘⧙⧛⧽⸣⸥⸧⸩����〉》 」』】〕〗〙〛〞〟﴾︘︶︸︺︼︾﹀﹂﹄﹈﹚﹜﹞）］｝｠｣'
    cs4Pi = chars5Ranges(gc2Ranges('Pi'))
    '«‘‛“‟‹⸂⸄⸉⸌⸜⸠'
    cs4Pf = chars5Ranges(gc2Ranges('Pf'))
    '»’”›⸃⸅⸊⸍⸝⸡'
    print_repr(cs4Ps)
    print_repr(cs4Pe)
    print_repr(cs4Pi)
    print_repr(cs4Pf)
    assert len(cs4Ps) == 79
    assert len(cs4Pe) == 77
    assert len(cs4Pi) == 12
    assert len(cs4Pf) == 10
    print_repr(cs4Ps)
    print_names5chars(cs4Ps)
    print_repr(cs4Pe)
    print_names5chars(cs4Pe)
    print_repr(cs4Pi)
    print_names5chars(cs4Pi)
    print_repr(cs4Pf)
    print_names5chars(cs4Pf)


def _bmg_():
    'bmg:Bidi_Mirroring_Glyph'
    (bmg2hx2sz, ichr2bmg) = _v14.bmg
    for bmg, hx2sz in bmg2hx2sz.items():
        if bmg == '':
            continue
        assert len(hx2sz) == 1
        [hx] = hx2sz
        assert hx2sz[hx] == 1
        ch = chr(hx)
        ch8bmg = chr(int(bmg,16))
        print_repr(ch+ch8bmg)


def _bpt_():
    'bpt:Bidi_Paired_Bracket_Type'
    (bpt2hx2sz, ichr2bpt) = _v14.bpt
    assert sorted(bpt2hx2sz) == 'c n o'.split(), sorted(bpt2hx2sz)
    cs4open_bracket = chars5Ranges(pa_va2Ranges('bpt', 'o'))
    cs4close_bracket = chars5Ranges(pa_va2Ranges('bpt', 'c'))
    print_repr(cs4open_bracket)
    '([{༺༼᚛⁅⁽₍⌈⌊〈❨❪❬❮❰❲❴⟅⟦⟨⟪⟬⟮⦃⦅⦇⦉⦋⦍⦏⦑⦓⦕⦗⧘⧚⧼⸢⸤⸦⸨����〈《「『【〔〖〘〚﹙﹛﹝（［｛｟｢'
    print_repr(cs4close_bracket)
    ')]}༻༽᚜⁆⁾₎⌉⌋〉❩❫❭❯❱❳❵⟆⟧⟩⟫⟭⟯⦄⦆⦈⦊⦌⦎⦐⦒⦔⦖⦘⧙⧛⧽⸣⸥⸧⸩����〉》」』】〕〗〙〛﹚﹜﹞）］｝｠｣'
    assert len(cs4open_bracket) == 64, (len(cs4open_bracket), len(cs4close_bracket))
    assert len(cs4close_bracket) == 64

def _bpb_():
    'bpb:Bidi_Paired_Bracket'
    (bpb2hx2sz, ichr2bpb) = _v14.bpb
    (bpt2hx2sz, ichr2bpt) = _v14.bpt
    set4cc = set()
    set4cc__oc5co = set()
    for bpb, hx2sz in bpb2hx2sz.items():
        if bpb == '#':
            continue
        assert len(hx2sz) == 1
        [hx] = hx2sz
        assert hx2sz[hx] == 1
        bpt = ichr2bpt[hx]
        assert bpt in 'o c', bpt
        ch = chr(hx)
        ch8bpb = chr(int(bpb,16))
        if bpt == 'o':
            cc = ch+ch8bpb
            #print_repr(cc)
            set4cc.add(cc)
        else:
            cc = ch8bpb+ch
            set4cc__oc5co.add(cc)
    assert set4cc__oc5co == set4cc, (set4cc__oc5co ^ set4cc)
    assert len(set4cc) == 64, len(set4cc)
    cs = ''.join(sorted(set4cc))
    print_repr(cs)
    '()[]{}༺༻༼༽᚛᚜⁅⁆⁽⁾₍₎⌈⌉⌊⌋〈〉❨❩❪❫❬❭❮❯❰❱❲❳❴❵⟅⟆⟦⟧⟨⟩⟪⟫⟬⟭⟮⟯⦃⦄⦅⦆⦇⦈⦉⦊⦋⦌⦍⦐⦏⦎⦑⦒⦓⦔⦕⦖⦗⦘⧘⧙⧚⧛⧼⧽⸢⸣⸤⸥⸦⸧⸨⸩��������〈〉《》「」『』【】〔〕〖〗〘〙〚〛﹙﹚﹛﹜﹝﹞（）［］｛｝｟｠｢｣'
    assert [*map(ord,'⦍⦐⦏⦎')] == [10637, 10640, 10639, 10638]
    hxs__str = ','.join(f'{ord(ch):X}' for ch in cs)
    print_repr(hxs__str)
    '28,29,5B,5D,7B,7D,F3A,F3B,F3C,F3D,169B,169C,2045,2046,207D,207E,208D,208E,2308,2309,230A,230B,2329,232A,2768,2769,276A,276B,276C,276D,276E,276F,2770,2771,2772,2773,2774,2775,27C5,27C6,27E6,27E7,27E8,27E9,27EA,27EB,27EC,27ED,27EE,27EF,2983,2984,2985,2986,2987,2988,2989,298A,298B,298C,298D,2990,298F,298E,2991,2992,2993,2994,2995,2996,2997,2998,29D8,29D9,29DA,29DB,29FC,29FD,2E22,2E23,2E24,2E25,2E26,2E27,2E28,2E29,2E55,2E56,2E57,2E58,2E59,2E5A,2E5B,2E5C,3008,3009,300A,300B,300C,300D,300E,300F,3010,3011,3014,3015,3016,3017,3018,3019,301A,301B,FE59,FE5A,FE5B,FE5C,FE5D,FE5E,FF08,FF09,FF3B,FF3D,FF5B,FF5D,FF5F,FF60,FF62,FF63'
    assert '⸩〈' == '\u2E29\u3008'
    #
    i = 1+cs.index('⸩')
    j = cs.index('〈')
    too_new_cs = cs[i:j]
    too_new_hxs__str = ','.join(f'{ord(ch):X}' for ch in too_new_cs)
    print_repr(too_new_hxs__str)
    '2E55,2E56,2E57,2E58,2E59,2E5A,2E5B,2E5C'
    print_names5chars(too_new_cs)
    'LEFT SQUARE BRACKET WITH STROKE'
    'RIGHT SQUARE BRACKET WITH STROKE'
    'LEFT SQUARE BRACKET WITH DOUBLE STROKE'
    'RIGHT SQUARE BRACKET WITH DOUBLE STROKE'
    'TOP HALF LEFT PARENTHESIS'
    'TOP HALF RIGHT PARENTHESIS'
    'BOTTOM HALF LEFT PARENTHESIS'
    'BOTTOM HALF RIGHT PARENTHESIS'


if 0:_gc__Ps_Pe_Pi_Pf_()
if 0:_bmg_()
if 0:_bpt_()
if 0:_bpb_()

__all__
from script.unicode.unicode_paired import *
