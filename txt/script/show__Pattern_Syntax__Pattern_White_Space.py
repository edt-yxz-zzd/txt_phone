r'''
py script/show__Pattern_Syntax__Pattern_White_Space.py
py script/show__Pattern_Syntax__Pattern_White_Space.py > /sdcard/0my_files/tmp/_.txt
view /sdcard/0my_files/tmp/_.txt

e script/show__Pattern_Syntax__Pattern_White_Space.py

view ../lots/NOTE/unicode/note4UnicodeStandard_14_0_annex/unicode_ver14_0_UAX31_UAX38摘要.txt
  分类:
  #字集不再变:
    Pattern_Syntax Characters
    Pattern_White_Space Characters
    #还有:Noncharacter_Code_Point=True也是不再变
  #字集可变:
    ID_Start Characters
      ++ from {ID_Nonstart Characters, Other Assigned Code Points, Unassigned Code Points}
    ID_Nonstart Characters
      ++ from {Other Assigned Code Points, Unassigned Code Points}
    Other Assigned Code Points
      ++ from {Unassigned Code Points}
    Unassigned Code Points
view /storage/emulated/0/0my_files/unzip/e_book/unicode_13__UCD/PropList.txt
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__PropList_txt__of_ver13_0.py
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__PropList_txt.py.out.ver13_0.hex.txt
# Total code points: 2760
    ,'Pattern_Syntax'
    : [(0x21, 0x30), (0x3a, 0x41), (0x5b, 0x5f), (0x60, 0x61), (0x7b, 0x7f), (0xa1, 0xa8), (0xa9, 0xaa), (0xab, 0xad), (0xae, 0xaf), (0xb0, 0xb2), (0xb6, 0xb7), (0xbb, 0xbc), (0xbf, 0xc0), (0xd7, 0xd8), (0xf7, 0xf8), (0x2010, 0x2028), (0x2030, 0x203f), (0x2041, 0x2054), (0x2055, 0x205f), (0x2190, 0x2460), (0x2500, 0x2776), (0x2794, 0x2c00), (0x2e00, 0x2e80), (0x3001, 0x3004), (0x3008, 0x3021), (0x3030, 0x3031), (0xfd3e, 0xfd40), (0xfe45, 0xfe47)]
# Total code points: 11
    ,'Pattern_White_Space'
    : [(0x9, 0xe), (0x20, 0x21), (0x85, 0x86), (0x200e, 0x2010), (0x2028, 0x202a)]
e




version of the Unicode database: 12.1.0

unicodedata.normalize(form, unistr)
unicodedata.is_normalized(form, unistr)
    form <- {'NFC', 'NFKC', 'NFD', 'NFKD'}

view ../lots/NOTE/unicode/note4UnicodeStandard_13_0_pdf/unicode_ver13_0__Normalization.txt



#'''

import unicodedata as U
from nn_ns.CJK.unicode.ucd_unihan.ucd.parsed_result__of__PropList_txt__of_ver13_0 import readonly_parsed_result4ver13_0
readonly_parsed_result4ver13_0['Pattern_Syntax']
readonly_parsed_result4ver13_0['Pattern_White_Space']
readonly_parsed_result4ver13_0['Noncharacter_Code_Point']


forms = ['NFC', 'NFKC', 'NFD', 'NFKD']
class Tmp:
    def __init__(sf, prop2rngs, /):
        sf._d = prop2rngs
    def __getitem__(sf, nm4prop, /):
        return sf._d[nm4prop]
    def on_names4prop(sf, nms4prop, /):
        it = map(sf.on_name4prop, nms4prop)
        for _ in it:pass
    def on_name4prop(sf, nm4prop, /):
        rngs = sf[nm4prop]
        sz = rngs.len_ints()
        print(f'{nm4prop}: total: {sz}')
        s = ''.join(map(chr, rngs.iter_ints()))
        print(f'{nm4prop}: chars: {s!r}')
        for ch in s:
            pt = hex(ord(ch))#f'{}'
            nm4ch = U.name(ch, '--__None__--')
            nfs = [(form, U.normalize(form, ch)) for form in forms if not U.is_normalized(form, ch)]
            print(f'{ch!r}:{pt: >8}:{nm4ch}:{nfs}')
            ...

print(f'version of the Unicode database: {U.unidata_version}')
tmp = Tmp(readonly_parsed_result4ver13_0)
tmp.on_names4prop(['Pattern_Syntax', 'Pattern_White_Space', 'Noncharacter_Code_Point'])
    #盲文？、中文标点符号、重卦 都包含在 Pattern_Syntax中
    #但『　』0x3000不在Pattern_White_Space中


