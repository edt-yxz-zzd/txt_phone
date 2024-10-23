#__all__:goto
r'''[[[
e script/unicode/unicode_space.py

vs:Pattern_White_Space,White_Space,gc.Zs

view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/originals/ucd_ver14_0/PropertyAliases.txt
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyValueAliases_txt.py.out.ver14_0_0.txt
Pat_WS                   ; Pattern_White_Space
WSpace                   ; White_Space                 ; space


script.unicode.unicode_space
py -m nn_ns.app.debug_cmd   script.unicode.unicode_space -x
py -m nn_ns.app.doctest_cmd script.unicode.unicode_space:__doc__ -ht
py_adhoc_call   script.unicode.unicode_space   @f
from script.unicode.unicode_space import *


_gc_Zs_() ==17==25-6-2== _WSpace_() excludes:
    6 '<None>'
    'LINE SEPARATOR'
    'PARAGRAPH SEPARATOR'

>>> _Pat_WS_()
11
'\t\n\x0b\x0c\r \x85\u200e\u200f\u2028\u2029'
'<None>'
'<None>'
'<None>'
'<None>'
'<None>'
'SPACE'
'<None>'
'LEFT-TO-RIGHT MARK'
'RIGHT-TO-LEFT MARK'
'LINE SEPARATOR'
'PARAGRAPH SEPARATOR'

>>> _WSpace_()
25
'\t\n\x0b\x0c\r \x85\xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u2028\u2029\u202f\u205f\u3000'
'<None>'
'<None>'
'<None>'
'<None>'
'<None>'
'SPACE'
'<None>'
'NO-BREAK SPACE'
'OGHAM SPACE MARK'
'EN QUAD'
'EM QUAD'
'EN SPACE'
'EM SPACE'
'THREE-PER-EM SPACE'
'FOUR-PER-EM SPACE'
'SIX-PER-EM SPACE'
'FIGURE SPACE'
'PUNCTUATION SPACE'
'THIN SPACE'
'HAIR SPACE'
'LINE SEPARATOR'
'PARAGRAPH SEPARATOR'
'NARROW NO-BREAK SPACE'
'MEDIUM MATHEMATICAL SPACE'
'IDEOGRAPHIC SPACE'

>>> _gc_Zs_()
17
' \xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f\u205f\u3000'
'SPACE'
'NO-BREAK SPACE'
'OGHAM SPACE MARK'
'EN QUAD'
'EM QUAD'
'EN SPACE'
'EM SPACE'
'THREE-PER-EM SPACE'
'FOUR-PER-EM SPACE'
'SIX-PER-EM SPACE'
'FIGURE SPACE'
'PUNCTUATION SPACE'
'THIN SPACE'
'HAIR SPACE'
'NARROW NO-BREAK SPACE'
'MEDIUM MATHEMATICAL SPACE'
'IDEOGRAPHIC SPACE'


#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from script.unicode.unicode_common import pa_va2Ranges, chars5Ranges, print_names5chars, print_repr, gc2Ranges, show_info_of_chars5pa_va

def _Pat_WS_():
    'Pat_WS:Pattern_White_Space'
    show_info_of_chars5pa_va('Pat_WS', 'Y')
    return

def _WSpace_():
    'WSpace:White_Space'
    show_info_of_chars5pa_va('WSpace', 'Y')
    return

def _gc_Zs_():
    'gc.Zs'
    show_info_of_chars5pa_va('gc', 'Zs')
    return

if 0:_Pat_WS_()
if 0:_WSpace_()
if 0:_gc_Zs_()

__all__
from script.unicode.unicode_space import *
