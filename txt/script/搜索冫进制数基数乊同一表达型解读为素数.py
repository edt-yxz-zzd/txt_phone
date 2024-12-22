#__all__:goto
r'''[[[
e script/搜索冫进制数基数乊同一表达型解读为素数.py
view script/搜索冫某进制表达数乊多种进制解读皆为素数.py

script.搜索冫进制数基数乊同一表达型解读为素数
py -m nn_ns.app.debug_cmd   script.搜索冫进制数基数乊同一表达型解读为素数 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.搜索冫进制数基数乊同一表达型解读为素数:__doc__ -ht # -ff -df




py_adhoc_call   script.搜索冫进制数基数乊同一表达型解读为素数   ,200:枚举冫进制数基数乊同一表达型解读为素数扌 :17401
py_adhoc_call   script.搜索冫进制数基数乊同一表达型解读为素数   @list.100:枚举冫进制数基数乊同一表达型解读为素数扌 :17401
[2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 16, 17, 18, 19, 22, 23, 25, 29, 31, 33, 35, 36, 37, 41, 43, 49, 50, 51, 57, 58, 59, 60, 61, 62, 69, 76, 81, 84, 86, 87, 96, 97, 98, 101, 109, 111, 112, 115, 126, 140, 141, 148, 149, 150, 151, 154, 158, 167, 171, 172, 175, 177, 181, 184, 185, 186, 191, 197, 201, 215, 219, 224, 227, 229, 236, 239, 241, 249, 253, 254, 258, 264, 265, 266, 268, 271, 284, 289, 301, 302, 314, 315, 317, 327, 328, 331, 336, 344, 350]

py_adhoc_call   script.搜索冫进制数基数乊同一表达型解读为素数   @list.100:枚举冫进制数基数乊同一表达型解读为素数扌 :17401 +invert
[9, 14, 15, 20, 21, 24, 26, 27, 28, 30, 32, 34, 38, 39, 40, 42, 44, 45, 46, 47, 48, 52, 53, 54, 55, 56, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 83, 85, 88, 89, 90, 91, 92, 93, 94, 95, 99, 100, 102, 103, 104, 105, 106, 107, 108, 110, 113, 114, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 142, 143, 144, 145, 146, 147, 152, 153, 155, 156, 157, 159]

]]]'''#'''
__all__ = r'''
枚举冫进制数基数乊同一表达型解读为素数扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.int_tools.digits.radix_repr2uint import radix_repr2uint__big_endian
from seed.int_tools.digits.generic_base85 import b85_alphabet
_tbl_85 = b85_alphabet.decode('ascii')
from seed.tiny_.check import check_type_is, check_int_ge

from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_
_max1 = is_prime__using_A014233_.upperbound

from itertools import count as count_
___end_mark_of_excluded_global_names__0___ = ...

def 枚举冫进制数基数乊同一表达型解读为素数扌(digits4show, digit_table4show=_tbl_85, *, begin4radix4read=2, invert=False):
    '-> radixes4read/(Iter radix4read)'
    ######################
    check_type_is(bool, invert)
    ######################
    check_type_is(str, digit_table4show)
    digit2char = digit_table4show
    char2digit = {char:digit for digit, char in enumerate(digit2char)}
    if not len(char2digit) == len(digit2char): raise ValueError('digit_table4show contains duplicate digits')


    ######################
    if type(digits4show) is str:
        s = digits4show
        #digits4show = (digit_table4show.index(ch) for ch in s)
        digits4show = (char2digit[ch] for ch in s)
    digits4show
    digits4show = tuple(digits4show)
    for digit in digits4show:
        #check_int_ge(digit)
        check_type_is(int, digit)
            # !! allow negative digit
            # !! allow digit overflow


    ######################
    check_int_ge(2, begin4radix4read)
    ######################
    is_prime_ = is_prime__using_A014233_
    max1_4u = _max1
    for radix4read in count_(begin4radix4read):
        u = radix_repr2uint__big_endian(radix4read, digits4show)
            # allow negative digit
            # allow digit overflow
        if not u < max1_4u: raise NotImplementedError
        if is_prime_(u) ^ invert:
            yield radix4read



__all__
from script.搜索冫进制数基数乊同一表达型解读为素数 import 枚举冫进制数基数乊同一表达型解读为素数扌
from script.搜索冫进制数基数乊同一表达型解读为素数 import *
