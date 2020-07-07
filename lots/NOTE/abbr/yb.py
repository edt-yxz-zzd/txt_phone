
import unicodedata as u
s = 'æ'
i = ord(s)
print(s, i, hex(i))
s = ''.join(map(chr, range(0x100)))
s = 'æ@əŒœuƱ@ǝ@ə'
s = 'æɪəʊθɔʌ'
'''
æɪəʊθɔʌ
[230, 618, 601, 650, 952, 596, 652]
['0xe6', '0x26a', '0x259', '0x28 a', '0x3b8', '0x254', '0x28c']
'''
def to_ords(s):
    return list(map(ord, s))
def to_hexs(s):
    return list(map(hex, to_ords(s)))
print(s, to_ords(s), to_hexs(s))



