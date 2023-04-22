#__all__:goto
r'''[[[
e script/汉语辞海囗.py
主要输出:
    view /sdcard/0my_files/tmp/out4py/汉语辞海囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt


script.汉语辞海囗
py -m nn_ns.app.debug_cmd   script.汉语辞海囗 -x
py -m nn_ns.app.doctest_cmd script.汉语辞海囗:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd script.汉语辞海囗!
py_adhoc_call   script.汉语辞海囗   @f
from script.汉语辞海囗 import *


[[
/sdcard/zidian/cihai/cihai.dat
hanyu(ciyu,content,pinyin,id)
pinyin:无法解码，放弃
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd \
 '%!may2smay=lambda m:(str(m) if m else "")' \
 '%!std4NL_=lambda s:(s.replace("\r\n", "\n").replace("\r", "\n"))' \
 '%!strips=lambda s:("\n".join(map(str.strip,s.split("\n"))))' \
 '%!s_=lambda s:(strips(std4NL_(may2smay(s))).replace("\n", "\n/"))' \
 '%!d_=lambda hexs:(bytes.fromhex(hexs).decode("u8"))' \
 --ipath:/sdcard/zidian/cihai/cihai.dat \
 --nm4table:hanyu \
 --nms4columns:ciyu,content \
 --fmtr4row='(lambda ciyu,content:f",{d_(ciyu)}\n:{s_(content)}")' \
 --opath:/sdcard/0my_files/tmp/out4py/汉语辞海囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt


du -h /sdcard/0my_files/tmp/out4py/汉语辞海囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
27M
view /sdcard/0my_files/tmp/out4py/汉语辞海囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
]]


py_adhoc_call   script.汉语辞海囗   @dump_to_file --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf/cihai.dat --opath:/sdcard/0my_files/tmp/out4py/script.汉语辞海囗._dump.out.txt --ofmt:echo
du -h /sdcard/0my_files/tmp/out4py/script.汉语辞海囗._dump.out.txt
57M
view /sdcard/0my_files/tmp/out4py/script.汉语辞海囗._dump.out.txt

py_adhoc_call   script.汉语辞海囗   @dump_to_file --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf/cihai.dat --opath:/sdcard/0my_files/tmp/out4py/script.汉语辞海囗.dump8dic.out.txt --ofmt:word___hex4pinyin__body___3lines
du -h /sdcard/0my_files/tmp/out4py/script.汉语辞海囗.dump8dic.out.txt
41M


view /sdcard/0my_files/tmp/out4py/script.汉语辞海囗.dump8dic.out.txt

发现已解包:
/sdcard/zidian/cihai/cihai.dat
du -b /sdcard/zidian/cihai/cihai.dat
53126144

cd /sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf
rm /sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf/cihai.dat
cd /sdcard/0my_files/unzip/apk/dictionary/
rm -rf ./han_yu_ci_hai
rm /sdcard/0my_files/tmp/out4py/script.汉语辞海囗._dump.out.txt
view /sdcard/0my_files/tmp/out4py/script.汉语辞海囗.dump8dic.out.txt








view /sdcard/0my_files/tmp/out4py/script.汉语辞海囗.dump8dic.out.txt
,吖吖
:C2D48E8DACE76693
,阿Q
:DE6A96482D5A4260
,阿Q正传
:115A0614E9371B6A
,阿爸
:2F2F8EDC5740D90F
,阿傍
:13EEFE7EBB0B6F3AF21693EFB10085A0
,阿保
:4576EE3848BC72BCA1B27B6398A3DECE
,阿堵
:E0538C8D0D0976CA
:1.六朝人口语。犹这﹐这个。 2.指钱。
,阿堵物
:B8761842D2EC99DEEC79F75032205EEE
:西晋的一些士族阶层人士自命清高，耻于言钱，钱被称为“阿堵物”。后人指为钱的别称，有讽刺意义。
,阿堵物(ē-)
:115A0614E9371B6A
:六朝王夷甫为人清高，从不说及“钱”字。妻子想试试他，把铜钱串起来绕床一周。王夷甫醒来，无法下床，便大声呼叫婢女：“快拿开阿堵物!”阿堵，六朝人的口语，意思是“这个”。后因用“阿堵物”指钱。见《世说新语·规箴》。

,居诸
:C2F53A979E86D0CD049D3CF1CF9B52B4
:1.《诗．邶风．柏舟》:"日居月诸，胡迭而微。"孔颖达疏:"居﹑诸者，语助也。"后用以借指日月﹑光阴。 2.指来往。
,日就月将
:CD5EFCBB6E8DD04C6281E93B1E15058A318C9B6720502D6B
:就：成就；将：进步。每天有成就，每月有进步。形容精进不止。也日积月累。
,日居衡茅
:DB0D597241CC31B7B0EF0941590A4C90AD1340991E40E40E
:晶：每天；衡茅：用衡木做门的茅草屋。每天居住在简陋的茅草屋中，不知天下大事。
,日居月诸
:DB0D597241CC31B77C28F2D73C3D3DD15A266CBA23D10037
:居：音“积”，语助词，同“乎”；诸：语助词。指光阴的流逝。
,日君
:5F428C519C4CFBBFD2A09B97793AC873
:1.指太阳。喻君主。




>>> '意义'.encode('u8').hex().upper()
'E6848FE4B989'

『意义』『yì yì』？16字节，感觉不太像 pinyin
INSERT INTO "hanyu" VALUES('E6848FE4B989','1.谓事物所包含的思想和道理。 2.内容。 3.美名，声誉。 4.作用，价值。','C359B5F74815488602A0CA37C6011812',329578);

[[[
汉语辞海:
mkdir ../../../unzip/apk/dictionary/han_yu_ci_hai/
cd ../../../unzip/apk/dictionary/han_yu_ci_hai/
du -h /sdcard/0my_files/apk/学习查询/com.xiaobin.chinach_0.1.5.apk_
25M
7z l /sdcard/0my_files/apk/学习查询/com.xiaobin.chinach_0.1.5.apk_
7z x /sdcard/0my_files/apk/学习查询/com.xiaobin.chinach_0.1.5.apk_
view ++enc=utf16le ../../../unzip/apk/dictionary/han_yu_ci_hai/resources.arsc
du -h ../../../unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf
24M
du -b ../../../unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf
25098454
25098454==0x17ef8d6
hexdump ../../../unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf  -C  -n 0x200 -s 0x0
hexdump ../../../unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf  -C  -n 0x200 -s 0x17ef700
PK    cihai.dat


search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
  [[
213603=0x34263
319065=0x4DE59
337347=0x525C3
339356=0x52D9C
... 许多
  ]]
0x19bf6==(0x4DE59-0x34263)
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '63 42 03 00'
  无
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    'f6 9b 01 00'
  无
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '00 03 42 63'
  无
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '00 01 9b f6 '
  无


补偿: [[[

搜 压缩包:
>>> hex(ord(']'))
'0x5d'
>>> chr(0x5d)
']'

header<lzma,FORMAT_ALONE=2> = b']\x00\x00\x80\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00'
header<lzma,FORMAT_XZ=7zXZ' -e4bs 'ascii'
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '5d 00 00 80'
  无
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '5d 00 00'
3466405=0x34E4A5
5598130=0x556BB2
9415028=0x8FA974
24072172=0x16F4FEC
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '7zXZ' -e4bs 'ascii'
  无

bz2
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    'BZh' -e4bs 'ascii'
  无

zlib
py_adhoc_call   nn_ns.bin.find_zlib_objs_in_file   ,hex.iter_find_zlib_objs_in_file__ipath   :'/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf'
  无
gzip
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '1f 8b'
[
200714=0x3100A
476963=0x74723
483704=0x76178
...许多
25001388=0x17D7DAC
25009277=0x17D9C7D
25091610=0x17EDE1A
]


hexdump ../../../unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf  -C  -n 0x200 -s 0x0
00000000  50 4b 03 04 14 00 00 00  08 00 74 bd f7 42 ef d3  |PK........t..B..|
00000010  1e 9b 3e f8 7e 01 00 a4  2a 03 09 00 00 00 63 69  |..>.~...*.....ci|
00000020  68 61 69 2e 64 61 74 ec  5d 07 70 1c 57 19 be 82  |hai.dat.].p.W...|
hexdump ../../../unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf  -C  -n 0x200 -s 0x17ef700
017ef880  03 09 00 24 00 00 00 00  00 00 00 20 00 00 00 00  |...$....... ....|
017ef890  00 00 00 63 69 68 61 69  2e 64 61 74 0a 00 20 00  |...cihai.dat.. .|
017ef8a0  00 00 00 00 01 00 18 00  00 9e 2d 67 bb 87 ce 01  |..........-g....|
017ef8b0  12 5d e5 73 bb 87 ce 01  80 7d f2 e8 33 05 ce 01  |.].s.....}..3...|
017ef8c0  50 4b 05 06 00 00 00 00  01 00 01 00 5b 00 00 00  |PK..........[...|
017ef8d0  65 f8 7e 01 00 00                                 |e.~...|
017ef8d6
    补偿: ]
==>>:
PK    cihai.dat

grep PK -r ../../python3_src/nn_ns/fileformat/
../../python3_src/nn_ns/fileformat/zip/get_last_zip_begin.py:            # [b'PK\x05\x06', 0, 0, 2, 2, 183, 32592, 0, b'', 65296]

scihai.ttf is zip???
/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf
mkdir /sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf
cd /sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf
7z l /sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf
7z x /sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf
$ ls
cihai.dat
$ du -h cihai.dat
51M     cihai.dat
hexdump  /sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf/cihai.dat   -C  -n 0x200 -s 0x0
00000000  53 51 4c 69 74 65 20 66  6f 72 6d 61 74 20 33 00  |SQLite format 3.|
00000010  04 00 01 01 00 40 20 20  00 05 fd 97 00 00 00 00  |.....@  ........|
SQLite
import sqlparse
iterdump
from itertools import islice
import sqlite3
cx = sqlite3.connect("/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf/cihai.dat")
it = cx.iterdump()
ls = [*islice(it, 12)]
>>> for x in ls:x
'BEGIN TRANSACTION;'
'CREATE TABLE android_metadata (locale TEXT);'
'INSERT INTO "android_metadata" VALUES(\'zh_CN\');'
'CREATE TABLE hanyu (ciyu TEXT(255,0) NOT NULL,content TEXT(255,0) NOT NULL,pinyin TEXT(255,0) NOT NULL,id integer NOT NULL PRIMARY KEY AUTOINCREMENT DEFAULT 1);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E5AEB6E68CA8E688B7\',\'每家每户，户户不漏。挨，依次，顺次。\',\'E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA\',1);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E5AEB6E6AF94E688B7\',\'1.犹挨户。\',\'E7208696463BB2AF5FEA58937BC1FF84398233309C0EFAAD\',2);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9\',\'1.接连。\',\'E7208696463BB2AF5A5AD409958A3BFA\',3);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E5B9B6E8B6B3\',\'形容人群拥挤。\',\'E7208696463BB2AF4CDD6CF5D0DC5FD52D0FE46E78109FDA\',4);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E693A6E88680\',\'指身体相贴近。也形容人群拥挤。\',\'E7208696463BB2AF9C8FDB92BCA9C7EB7C6130F180EE6BAD\',5);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E693A6E8838C\',\'肩挨肩，背擦背。形容人多拥挤。\',\'E7208696463BB2AF5CBF4620AE1859182A7C47D825F34D2B\',6);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E693A6E884B8\',\'挨：靠近。擦，接触。形容狎昵之状。\',\'E7208696463BB2AF70B188DDC5A5BDB42C914B16426F1BFC\',7);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E690ADE8838C\',\'挨肩：肩和肩相靠。搭背：手搭在别人背上。形容极其亲昵的样子 。\',\'E7208696463BB2AF2C209CC907DB0200DD6E091BB17561CD\',8);'


for x in it:
  if not x.startswith('INSERT INTO'):
    print(x)

BEGIN TRANSACTION;
CREATE TABLE android_metadata (locale TEXT);
CREATE TABLE hanyu (ciyu TEXT(255,0) NOT NULL,content TEXT(255,0) NOT NULL,pinyin TEXT(255,0) NOT NULL,id integer NOT NULL PRIMARY KEY AUTOINCREMENT DEFAULT 1);
DELETE FROM "sqlite_sequence";
COMMIT;

from itertools import islice
import sqlite3
cx = sqlite3.connect("/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf/cihai.dat")
it = cx.iterdump()
ls = [*islice(it, 12)]

from ast import literal_eval
literal_eval(ls[-1][26:-1])

it = cx.iterdump()
for x in it:
  if x.startswith('INSERT INTO'):
    (ciyu, content, pinyin, _id) = literal_eval(x[26:-1])
    print(f'{ciyu}:{pinyin}:{content}')


hanyu (ciyu, content, pinyin, id)

bytes.fromhex('E68CA8E5AEB6E68CA8E688B7').decode('u8')
'挨家挨户'
bytes.fromhex('E68CA8E5AEB6E6AF94E688B7').decode('u8')
'挨家比户'


bytes.fromhex('E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA').decode('u8')
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 0: invalid continuation byte

bytes.fromhex('E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA').decode('gb18030')
UnicodeDecodeError: 'gb18030' codec can't decode byte 0xe7 in position 0: illegal multibyte sequence

bytes.fromhex('E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA').decode('ascii')
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)


『āi jiā āi hù』
>>> 'āi jiā āi hù'.encode('u8').hex(' ')
'c4 81 69 20 6a 69 c4 81 20 c4 81 69 20 68 c3 b9'
>>>
'āi jiā āi hù'.encode('u8').hex(' ')
E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA
E7208696463BB2AF5FEA58937BC1FF84398233309C0EFAAD
----------------xxxxxxxxxxxx-xxxxxxx-xxxxxxxx-xx

E7 8696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA
bytes.fromhex('8696463BB2AFDBF1E744398AF54B').decode('gb18030')

cx.close();quit()

help(sqlparse)

echo "INSERT INTO 'hanyu' VALUES('E68CA8E5AEB6E68CA8E688B7','每家每户，户户不漏。挨，依次，顺次。','E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA',1);" | py -m sqlparse -
p.parse_args("INSERT INTO 'hanyu' VALUES('E68CA8E5AEB6E68CA8E688B7','每家每户，户户不漏。挨，依次，顺次。','E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA',1);".split())

view /data/data/com.termux/files/usr/lib/python3.10/site-packages/sqlparse/cli.py
ls /data/data/com.termux/files/usr/lib/python3.10/site-packages/sqlparse/filters/
from seed.text.encodings import all_encodings
bs=bytes.fromhex('E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA')
for e in all_encodings:
  try:
    bs.decode(e)
  except(ValueError,LookupError):
    pass
  else:
    print(e)

not-found encoding


]]]

[[
base64:
>>> import base64 as b
>>> b.__all__
['encode', 'decode', 'encodebytes', 'decodebytes', 'b64encode', 'b64decode', 'b32encode', 'b32decode', 'b32hexencode', 'b32hexdecode', 'b16encode', 'b16decode', 'b85encode', 'b85decode', 'a85encode', 'a85decode', 'standard_b64encode', 'standard_b64decode', 'urlsafe_b64encode', 'urlsafe_b64decode']
>>> s = 'C2D48E8DACE76693' #吖吖
>>> bs=bytes.fromhex('C2D48E8DACE76693')
>>> b.b32decode(s)
Traceback (most recent call last):
    ...
binascii.Error: Non-base32 digit found
>>> b.b32hexdecode(s)
b'`\x9aD9\rS\x1cs\x19#'
>>> b.b64decode(s)
b'\x0b`\xf8\xf0O\x03\x00!;\xeb\xafw'
>>> b.b16decode(s)
b'\xc2\xd4\x8e\x8d\xac\xe7f\x93'
>>> bs
b'\xc2\xd4\x8e\x8d\xac\xe7f\x93'
>>> b.b85decode(s)
b'%jfg+\xdb\xabY+\xd1\x85\x86'
>>> b.a85decode(s)
b'jl\xcfpp\xde\x16\xbcp\xd3)\x00'

>>> u = int.from_bytes(bs,'big')
>>> bin(u)
'0b1100001011010100100011101000110110101100111001110110011010010011'

>>> [*filter(bool, map(len, bin(u)[2:].split('0')))]
[2, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 2, 3, 3, 2, 2, 1, 1, 2]
>>> [*filter(bool, map(len, bin(u)[2:].split('1')))]
[4, 1, 1, 1, 2, 3, 1, 3, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2]
>>> L0s = [*filter(bool, map(len, bin(u)[2:].split('1')))]
>>> L1s = [*filter(bool, map(len, bin(u)[2:].split('0')))]
>>> Ls = L0s+L1s
>>> Ls[0::2] = L1s
>>> Ls[1::2] = map(int.__neg__, L0s)
>>> Ls
[2, -4, 1, -1, 2, -1, 1, -1, 1, -2, 1, -3, 3, -1, 1, -3, 2, -1, 2, -1, 1, -1, 2, -2, 3, -2, 3, -1, 2, -2, 2, -1, 1, -2, 1, -2, 2]

1100001011010100100011101000110110101100111001110110011010010011

]]

[[fail...
猜测:可能是音频数据
,吖吖
:C2D48E8DACE76693
,阿Q
:DE6A96482D5A4260
,阿Q正传
:115A0614E9371B6A
,阿爸
:2F2F8EDC5740D90F

import audioop
audioop.adpcm2lin
audioop.alaw2lin
audioop.ulaw2lin
bs = bytes.fromhex('C2D48E8DACE76693')
audioop.ulaw2lin(bs, 1)
audioop.alaw2lin(bs, 1)

>>> len(bs)
8

>>> audioop.ulaw2lin(bs, 1)
b'\x06\x02EI\x12\x01\xfe8'
>>> audioop.ulaw2lin(bs, 2)
b'\xdc\x06\xec\x02|E|I\xfc\x12\x04\x01\xec\xfe|8'
>>> audioop.ulaw2lin(bs, 3)
b'\x00\xdc\x06\x00\xec\x02\x00|E\x00|I\x00\xfc\x12\x00\x04\x01\x00\xec\xfe\x00|8'
>>> audioop.ulaw2lin(bs, 4)
b'\x00\x00\xdc\x06\x00\x00\xec\x02\x00\x00|E\x00\x00|I\x00\x00\xfc\x12\x00\x00\x04\x01\x00\x00\xec\xfe\x00\x00|8'
>>> audioop.ulaw2lin(bs, 5)
Traceback (most recent call last):
  ...
audioop.error: Size should be 1, 2, 3 or 4


>>> audioop.alaw2lin(bs, 1)
b'\x01\x00\x1b\x18f\x04\xfb\x0b'
>>> audioop.alaw2lin(bs, 2)
b'x\x01\x18\x00\x80\x1b\x80\x18\x00f\xa0\x04 \xfb@\x0b'
>>> audioop.alaw2lin(bs, 3)
b'\x00x\x01\x00\x18\x00\x00\x80\x1b\x00\x80\x18\x00\x00f\x00\xa0\x04\x00 \xfb\x00@\x0b'
>>> audioop.alaw2lin(bs, 4)
b'\x00\x00x\x01\x00\x00\x18\x00\x00\x00\x80\x1b\x00\x00\x80\x18\x00\x00\x00f\x00\x00\xa0\x04\x00\x00 \xfb\x00\x00@\x0b'
>>> audioop.alaw2lin(bs, 5)
Traceback (most recent call last):
  ...
audioop.error: Size should be 1, 2, 3 or 4
>>> len(_)
32

ns = 0xC2D4, 0x8E8D, 0xACE7, 0x6693
us = 0xD4C2, 0x8D8E, 0xE7AC, 0x9366
audioop.adpcm2lin(bs[4:], 1, us[:2])
ValueError: bad state

>>> i = int.from_bytes(bs, 'big')
>>> hex(i)
'0xc2d48e8dace76693'
>>> bin(i)
'0b1100001011010100100011101000110110101100111001110110011010010011'

import wave

py.sound?
    ossaudiodev — Access to OSS-compatible audio devices
    wave — Read and write WAV files
    audioop — Manipulate raw audio data

audioop
This module provides support for a-LAW, u-LAW and Intel/DVI ADPCM encodings.

A few of the more complicated operations only take 16-bit samples, otherwise the sample size (in bytes) is always a parameter of the operation.


audioop.adpcm2lin(adpcmfragment, width, state)¶
Decode an Intel/DVI ADPCM coded fragment to a linear fragment. See the description of lin2adpcm() for details on ADPCM coding. Return a tuple (sample, newstate) where the sample has the width specified in width.

audioop.alaw2lin(fragment, width)¶
Convert sound fragments in a-LAW encoding to linearly encoded sound fragments. a-LAW encoding always uses 8 bits samples, so width refers only to the sample width of the output fragment here.

audioop.ulaw2lin(fragment, width)¶
Convert sound fragments in u-LAW encoding to linearly encoded sound fragments. u-LAW encoding always uses 8 bits samples, so width refers only to the sample width of the output fragment here.





audioop.lin2adpcm(fragment, width, state)¶
Convert samples to 4 bit Intel/DVI ADPCM encoding. ADPCM coding is an adaptive coding scheme, whereby each 4 bit number is the difference between one sample and the next, divided by a (varying) step. The Intel/DVI ADPCM algorithm has been selected for use by the IMA, so it may well become a standard.

state is a tuple containing the state of the coder. The coder returns a tuple (adpcmfrag, newstate), and the newstate should be passed to the next call of lin2adpcm(). In the initial call, None can be passed as the state. adpcmfrag is the ADPCM coded fragment packed 2 4-bit values per byte.

audioop.lin2alaw(fragment, width)¶
Convert samples in the audio fragment to a-LAW encoding and return this as a bytes object. a-LAW is an audio encoding format whereby you get a dynamic range of about 13 bits using only 8 bit samples. It is used by the Sun audio hardware, among others.

audioop.lin2lin(fragment, width, newwidth)¶
Convert samples between 1-, 2-, 3- and 4-byte formats.

Note

In some audio formats, such as .WAV files, 16, 24 and 32 bit samples are signed, but 8 bit samples are unsigned. So when converting to 8 bit wide samples for these formats, you need to also add 128 to the result:

new_frames = audioop.lin2lin(frames, old_width, 1)
new_frames = audioop.bias(new_frames, 1, 128)
The same, in reverse, has to be applied when converting from 8 to 16, 24 or 32 bit width samples.

audioop.lin2ulaw(fragment, width)¶
Convert samples in the audio fragment to u-LAW encoding and return this as a bytes object. u-LAW is an audio encoding format whereby you get a dynamic range of about 14 bits using only 8 bit samples. It is used by the Sun audio hardware, among others.
]]

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from seed.io.may_open import open4w, open4w_err, open4r
from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
from ast import literal_eval
from itertools import islice
import sqlite3

def _first_try():
  if 0:
    cx = sqlite3.connect("/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf/cihai.dat")
    it = cx.iterdump()
    ls = [*islice(it, 12)]
  if 0:
    for x in ls:
        print(repr(x))
    r'''
'BEGIN TRANSACTION;'
'CREATE TABLE android_metadata (locale TEXT);'
'INSERT INTO "android_metadata" VALUES(\'zh_CN\');'
'CREATE TABLE hanyu (ciyu TEXT(255,0) NOT NULL,content TEXT(255,0) NOT NULL,pinyin TEXT(255,0) NOT NULL,id integer NOT NULL PRIMARY KEY AUTOINCREMENT DEFAULT 1);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E5AEB6E68CA8E688B7\',\'每家每户，户户不漏。挨，依次，顺次。\',\'E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA\',1);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E5AEB6E6AF94E688B7\',\'1.犹挨户。\',\'E7208696463BB2AF5FEA58937BC1FF84398233309C0EFAAD\',2);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9\',\'1.接连。\',\'E7208696463BB2AF5A5AD409958A3BFA\',3);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E5B9B6E8B6B3\',\'形容人群拥挤。\',\'E7208696463BB2AF4CDD6CF5D0DC5FD52D0FE46E78109FDA\',4);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E693A6E88680\',\'指身体相贴近。也形容人群拥挤。\',\'E7208696463BB2AF9C8FDB92BCA9C7EB7C6130F180EE6BAD\',5);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E693A6E8838C\',\'肩挨肩，背擦背。形容人多拥挤。\',\'E7208696463BB2AF5CBF4620AE1859182A7C47D825F34D2B\',6);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E693A6E884B8\',\'挨：靠近。擦，接触。形容狎昵之状。\',\'E7208696463BB2AF70B188DDC5A5BDB42C914B16426F1BFC\',7);'
'INSERT INTO "hanyu" VALUES(\'E68CA8E882A9E690ADE8838C\',\'挨肩：肩和肩相靠。搭背：手搭在别人背上。形容极其亲昵的样子 。\',\'E7208696463BB2AF2C209CC907DB0200DD6E091BB17561CD\',8);'
    '''#'''

  if 0:
    it = cx.iterdump()
    for x in it:
      if not x.startswith('INSERT INTO'):
        print(x)
    r'''
BEGIN TRANSACTION;
CREATE TABLE android_metadata (locale TEXT);
CREATE TABLE hanyu (ciyu TEXT(255,0) NOT NULL,content TEXT(255,0) NOT NULL,pinyin TEXT(255,0) NOT NULL,id integer NOT NULL PRIMARY KEY AUTOINCREMENT DEFAULT 1);
DELETE FROM "sqlite_sequence";
COMMIT;
    '''#'''
  if 0:
    print(literal_eval(ls[-1][26:-1]))
    ('E68CA8E882A9E690ADE8838C', '挨肩：肩和肩相靠。搭背：手搭 在别人背上。形容极其亲昵的样子。', 'E7208696463BB2AF2C209CC907DB0200DD6E091BB17561CD', 8)
  cx.close()
































def decode_hex__u8(hex_str, /):
    return bytes.fromhex(hex_str).decode('u8')
class FormatError(Exception):pass
_echo = echo
omitted_sql_stmts = r'''
BEGIN TRANSACTION;
CREATE TABLE android_metadata (locale TEXT);
INSERT INTO "android_metadata" VALUES('zh_CN');
CREATE TABLE hanyu (ciyu TEXT(255,0) NOT NULL,content TEXT(255,0) NOT NULL,pinyin TEXT(255,0) NOT NULL,id integer NOT NULL PRIMARY KEY AUTOINCREMENT DEFAULT 1);

DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('hanyu',371824);
COMMIT;
        '''.split('\n')#'''
prefix4data_sql_stmt = 'INSERT INTO "hanyu" VALUES'
r'''
BEGIN TRANSACTION;
CREATE TABLE android_metadata (locale TEXT);
INSERT INTO "android_metadata" VALUES('zh_CN');
CREATE TABLE hanyu (ciyu TEXT(255,0) NOT NULL,content TEXT(255,0) NOT NULL,pinyin TEXT(255,0) NOT NULL,id integer NOT NULL PRIMARY KEY AUTOINCREMENT DEFAULT 1);
INSERT INTO "hanyu" VALUES('E68CA8E5AEB6E68CA8E688B7','每家每户，户户不漏。挨，依次，顺次。','E7208696463BB2AFDBF1E744398AF54BC20F3A646AE4AAEA',1);
...INSERT INTO "hanyu" VALUES...
    /^\(INSERT INTO "hanyu" VALUES\)\@!
        skip this section
        NOTE:
            2th line:『INSERT INTO "android_metadata" VALUES』
            -2th line:『INSERT INTO "sqlite_sequence" VALUES』
INSERT INTO "hanyu" VALUES('E5819AE6898BE8849A','1.施展手段。 2.指暗中耍花样。','99269B98B4F0B9C028787A13CD2A0073DE05DE2E423C2046',371824);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('hanyu',371824);
COMMIT;
'''#'''


assert len(prefix4data_sql_stmt) == 26


def mk_nm2fmtr__():
    '-> nm2fmtr_/{nm4fmtr_:fmtr_/(sql_stmt -> Iter line)}'
    #echo = _echo
    def echo(sql_stmt, /):
        '-> Iter line'
        yield sql_stmt
    def word___hex4pinyin__body___3lines(sql_stmt, /):
        '-> Iter line'
        if not sql_stmt.startswith(prefix4data_sql_stmt):
            assert sql_stmt in omitted_sql_stmts
            return
        s = sql_stmt[len(prefix4data_sql_stmt):-1]
        if 1:
            raise DeprecationWarning('see: ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py::using SELECT FROM')
            #bug:s = s.replace("''", "'")
            s = s.replace("\\", r"\\")
                #『\』-->『\\』--->『\』
            s = s.replace("''", r"\'")
                #『''』-->『\'』--->『'』
        (hex4word, content, hex4pinyin, _id8PK) = literal_eval(s)
            # <<== CREATE TABLE hanyu (ciyu, content, pinyin, _id
            #
            #('E69F8FE4BABA','1.古地名。在今河北省唐山市西。春秋晋地，战国属赵，汉置县。 2.《史记．张耳陈馀列传》:"汉八年，上从东垣还，过赵，贯高等乃壁人柏人，要之置厕。上过欲宿，心动， 问曰:''县名为何?''曰:''柏人。''''柏人者，迫于人也!''不宿而去。"后遂用为皇帝行止戒备的典故。','EDBC4EA9750BA8FBE9B3E46DFB75B46F',10044)
            #SyntaxError: unterminated triple-quoted string literal (detected at line 1)
            #decode_hex__u8('E69F8FE4BABA') == '柏人'
            #汉语辞海['柏人'] --> 『1.古地名。在今河北省唐山市西。春秋晋地，战国属赵，汉置县。 2.《史记．张耳陈馀列传》:"汉八年，上从东垣还，过赵，贯高等乃壁人柏人，要之置厕。上过欲宿，心动，问曰:'县名为何?'曰:'柏人。''柏人者，迫于人也!'不宿而去。"后遂用为皇帝行止戒备的典故。』
            #『''』--> 『'』


        word = decode_hex__u8(hex4word)
        hex4pinyin
        body = (content)
        try:
            bs4pinyin = bytes.fromhex(hex4pinyin) # check hex and no "\n"
        except ValueError as e:
            raise ValueError(fr'not hex:hex4pinyin={hex4pinyin!r}') from e
        if '\n' in word: raise FormatError(fr'contains "\n":word={word!r}')
        if '\n' in body: raise FormatError(fr'contains "\n":body={body!r}')
        yield f',{word}'
        yield f':{hex4pinyin}'
        yield f':{body}'
        return
    return {**locals()}




_nm2fmtr__ = mk_nm2fmtr__()



def dump_to_file(*, ipath, opath, ofmt, force=False):
    raise DeprecationWarning('see: ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py::using SELECT FROM')
    assert ofmt in _nm2fmtr__, sorted(_nm2fmtr__)
    fmtr_ = _nm2fmtr__[ofmt]

    #def open4w(may_opath, /, *, force, xencoding):
    with sqlite3.connect(ipath) as cx, open4w(opath, xencoding='u8', force=force) as fout:
        it = cx.iterdump()
        fprint = mk_fprint(fout)
        for sql_stmt in it:
            for line in fmtr_(sql_stmt):
                fprint(line)



from script.汉语辞海囗 import *
