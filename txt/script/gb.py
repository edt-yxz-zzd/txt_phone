e = 'gb2312'
'gb2312' # 6763+682; [a1..a9, b0..f7] * [a1..fe]

'gbk' # 20902+984; +gb2312 = [81..fe] * [40..7e, 80..fe]

'gb18030' # 4bytes; -gbk = [81..82, 95..98] * [30..39] * ? * ?

r"""
GB 18030 defines a one (ASCII), two (extended GBK), or four-byte (UTF) encoding. The two-byte codes are defined in a lookup table, while the four-byte codes are defined sequentially (hence algorithmically) to fill otherwise unencoded parts in UCS. GB 18030 inherits the bad aspects of GBK, most notably needing special code to safely find ASCII characters in a GB18030 sequence.

GB 18030 encoding[3]:3[5]:252[9]
GB 18030	code points[c]	Unicode
byte 1 (MSB)	byte 2	byte 3	byte 4
00 – 7F		128	0000 – 007F
80		—	invalid[d]
81 – FE	40 – FE except 7F[e]		23940	0080 – FFFF except D800 – DFFF[f]
81 – 84	30 – 39	81 – FE	30 – 39	39420
85	— (12600)	reserved for future character extension
86 – 8F	— (126000)	reserved for future ideographic extension
unassigned	—	D800 – DFFF[g]
90 – E3	30 – 39	81 – FE	30 – 39	1048576	10000 – 10FFFF
E4 – FC	— (315000)	reserved for future standard extension
FD – FE	— (25200)	user-defined
FF		—	invalid
Total	1112064	
The one- and two-byte code points are essentially GBK with the euro sign, PUA mappings for unassigned/user-defined points, and vertical punctuations. The four byte scheme can be thought of as consisting of two units, each of two bytes. Each unit has a similar format to a GBK two byte character but with a range of values for the second byte of 0x30–0x39 (the ASCII codes for decimal digits). The first byte has the range 0x81 to 0xFE, as before. This means that a string search routine that is safe for GBK should also be reasonably safe for GB18030 (in much the same way that a basic byte-oriented search routine is reasonably safe for EUC).

This gives a total of 1,587,600 (126×10×126×10) possible 4 byte sequences, which is easily sufficient to cover Unicode's 1,112,064 (17×65536 − 2048 surrogates) assigned, reserved, and noncharacter code points.

Unfortunately, to further complicate matters there are no simple rules to translate between a 4 byte sequence and its corresponding code point. Instead, codes are allocated sequentially (with the first byte containing the most significant part and the last the least significant part) only to Unicode code points that are not mapped in any other manner. For example:

U+00DE (Þ) → 81 30 89 37
U+00DF (ß) → 81 30 89 38
U+00E0 (à) → A8 A4
U+00E1 (á) → A8 A2
U+00E2 (â) → 81 30 89 39
U+00E3 (ã) → 81 30 8A 30
An offset table is used in the WHATWG and W3C version of GB 18030 to efficiently translate code points.[10] ICU[9] and glibc use similar range definitions to avoid wasting space on large sequential blocks.

"""

rg = range
pr=print
def sw(a):
	pr(a, end='')
