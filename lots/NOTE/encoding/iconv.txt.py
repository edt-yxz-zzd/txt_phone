r'''[[[
e ../lots/NOTE/encoding/iconv.txt.py
view ../lots/NOTE/encoding/iconv.txt
view ../../python3_src/seed/exec/cmd_call.py
view '../lots/NOTE/encoding/rngs4cjk_encodings5iconv.out.txt.7z'



py ../lots/NOTE/encoding/iconv.txt.py  ,list_all_encodings6iconv_
py ../lots/NOTE/encoding/iconv.txt.py  @show_rngs_info4all_encodings6iconv_    --chars7included:'一' --regex4excluded_encoding_names:'(?i)^(?:UTF|UCS).*$'   >  /sdcard/0my_files/tmp/0tmp      2>&1
view /sdcard/0my_files/tmp/0tmp
    262529行:『buggy』混淆
    ++『, flush=True』
    仍是262529行:『buggy』不混淆
du -h /sdcard/0my_files/tmp/0tmp
    1.6M
cp -iv /sdcard/0my_files/tmp/0tmp  /sdcard/0my_files/tmp/rngs4cjk_encodings5iconv.out.txt
[[[
7z a -t7z /sdcard/0my_files/tmp/rngs4cjk_encodings5iconv.out.txt.7z /sdcard/0my_files/tmp/rngs4cjk_encodings5iconv.out.txt
    1.6M-->84K
    1/20
du -h /sdcard/0my_files/tmp/rngs4cjk_encodings5iconv.out.txt.7z
cp -iv /sdcard/0my_files/tmp/rngs4cjk_encodings5iconv.out.txt.7z   ../lots/NOTE/encoding/
7z l /sdcard/0my_files/tmp/rngs4cjk_encodings5iconv.out.txt.7z   >  /sdcard/0my_files/tmp/0tmp
7z l '../lots/NOTE/encoding/rngs4cjk_encodings5iconv.out.txt.7z'
===

7-Zip [64] 17.05 : Copyright (c) 1999-2021 Igor Pavlov : 2017-08-28
p7zip Version 17.05 (locale=utf8,Utf16=on,HugeFiles=on,64 bits,8 CPUs LE)

Scanning the drive for archives:
1 file, 82454 bytes (81 KiB)

Listing archive: /sdcard/0my_files/tmp/rngs4cjk_encodings5iconv.out.txt.7z

--
Path = /sdcard/0my_files/tmp/rngs4cjk_encodings5iconv.out.txt.7z
Type = 7z
Physical Size = 82454
Headers Size = 170
Method = LZMA2:21
Solid = -
Blocks = 1

   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2024-07-16 00:17:42 ....A      1601262        82284  rngs4cjk_encodings5iconv.out.txt
------------------- ----- ------------ ------------  ------------------------
2024-07-16 00:17:42            1601262        82284  1 files
]]]


######################
'CP932'
'CP932'
∠‖
2220:2016
，−
FF0C:2212
｝〜
FF5D:301C
ﾟ¢
FF9F:A2
skip:CP932
######################
    应当是『兼容区』-->『归并区』


[[[
#init:script
    py ../lots/NOTE/encoding/iconv.txt.py    >  /sdcard/0my_files/tmp/0tmp
    py ../lots/NOTE/encoding/iconv.txt.py
#now:adhoc_argparser__main__call
py ../lots/NOTE/encoding/iconv.txt.py  @show_rngs_info4all_encodings6iconv_ --encodingss="[['gbk'], ['ascii'], ['utf-8']]"  --utf8_bytes="'a一'.encode('u8')"   --chars7included:'一' --regex4excluded_encoding_names:'(?i)^(?:UTF|UCS).*$'
===
######################
'gbk'
######################
######################
'gbk'
'gbk'
2
2
gbk_8hx2sz = (
{0x61
: 1
,0x4E00
: 1
}
)
######################
===
]]]



>>> hex(65042)
'0xfe12'
>>> hex(65041)
'0xfe11'
>>> '\ufe12'
'︒'
>>> '\ufe11'
'︑'




Surrogates Area: U+D800..U+DFFF
    total 2**(3+8) == 2**11

Private Use Area (PUA): U+E000..U+F8FF
    total of 6400 private-use characters
Supplementary Private Use Areas
    Supplementary Private Use Area-A : U+F 0000..U+F FFFD
        Plane 15
    Supplementary Private Use Area-B: U+10 0000..U+10 FFFD
        Plane 16

    131068 == (2**16 - 2) * 2

total requires 17 bits # see Private-Use Surrogate pair which provide 17 bits


#]]]'''#'''


from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer

from seed.data_funcs.rngs import make_Ranges, sorted_ints_to_iter_nontouch_ranges

from pathlib import Path
from functools import cache

from seed.exec.cmd_call import cmd_call
from seed.tiny import print_err, mk_tuple

def _try_call_iconv():
    r = cmd_call('iconv -f utf-8 -t gbk'.split(), input='一'.encode('u8'))
    assert r == (b'\xd2\xbb', b'', 0, False), r
        # (outs, errs, returncode, is_timeout)
    #print(r)

if 0b000:
    _try_call_iconv()
    quit(0)
@cache
def list_all_encodings6iconv_():
    '-> encodingss/[aliases]/[[encoding]]'
    r = cmd_call(cmd:='iconv -l'.split())
    (outs, errs, returncode, is_timeout) = r
    if not returncode == 0 or errs:
        raise Exception(encoding, cmd, r)
    s = outs.decode('ascii')
    ss = s.split('\n')
    encodingss = [encodings for nms__str in ss for encodings in [nms__str.split()] if encodings]
    assert all(map(all, encodingss)), (ss, encodingss)
    encodingss = tuple(map(tuple, encodingss))
    return encodingss
if 0b000:
    print(list_all_encodings6iconv_())
    quit(0)
def show_rngs_info4all_encodings6iconv_(*, encodingss=None, utf8_bytes=None, chars7included='', regex4excluded_encoding_names=None):
    if encodingss is None:
        encodingss = list_all_encodings6iconv_()
    if utf8_bytes is None:
        utf8_bytes = mk_utf8_bytes4all_chars_of_unicode()
    ######################
    for encodings in encodingss:
        encoding = _pick_one5aliases_(encodings)
    ######################
    if regex4excluded_encoding_names:
        import re
        rex4exclude = re.compile(regex4excluded_encoding_names)
        encodingss = [encodings for encodings in encodingss if all(rex4exclude.fullmatch(encoding) is None for encoding in encodings)]
    ######################
    if chars7included:
        _utf8_bytes7included = chars7included.encode('u8')
        def is_ok_(encodings, /):
            [encoding, *aliases] = encodings
            r = cmd_call(cmd:=[*'iconv  -c  -f utf-8 -t'.split(), encoding], input=_utf8_bytes7included)
            (outs, errs, returncode, is_timeout) = r
            r = cmd_call(cmd:=[*'iconv  -c  -t utf-8 -f'.split(), encoding], input=outs)
            (outs, errs, returncode, is_timeout) = r
            return outs == _utf8_bytes7included
        encodingss = [*filter(is_ok_, encodingss)]

    ######################
    print('#'*22)
    for encodings in encodingss:
        nms__str = ' '.join(encodings)
        print(repr(nms__str))
    print('#'*22)
    ######################
    for encodings in encodingss:
        print('#'*22)
        encoding = _pick_one5aliases_(encodings)

        nms__str = ' '.join(encodings)
        print(repr(nms__str), flush=True)
        show_rngs_info4encoding6iconv_(encoding, utf8_bytes=utf8_bytes)
    print('#'*22)
    ######################
    return

def _pick_one5aliases_(encodings, /):
    '-> encoding'
    if 0:
        [encoding, *aliases] = encodings
    else:
        # !! 'ANSI_X3.4-1968 ANSI_X3.4-1986 ASCII CP367 IBM367 ISO-IR-6 ISO646-US ISO_646.IRV:1991 US US-ASCII CSASCII'
        # => '.-:_'
        for nm in encodings:
            nm4id = nm.replace('-', '_')
            if nm4id.isidentifier():
                break
        else:
            #raise Exception(encodings)
                #Exception: ('BIG5-HKSCS:1999',)
            nm = encodings[0]
            _nm2id_(nm)
                #^Exception
        encoding = nm
    return encoding
#end-def _pick_one5aliases_(encodings, /):


def mk_txt4all_chars_of_unicode(rngs=None, /):
    '-> txt4all_chars_of_unicode :: sorted [char]'
    if not rngs is None:
        rngs = mk_tuple(rngs)
    return _mk_txt4all_chars_of_unicode(rngs)
@cache
def _mk_txt4all_chars_of_unicode(rngs=None, /):
    '-> txt4all_chars_of_unicode :: sorted [char]'
    from seed.data_funcs.rngs import make_Ranges, sorted_ints_to_iter_nontouch_ranges
    if rngs is None:
        skips = make_Ranges([(0xD800,0xDFFF+1), (0xE000,0xF8FF+1), (0xF_00_00,0xF_FF_FD+1), (0x10_00_00,0x10_FF_FD+1)])
        all_code_points = make_Ranges([(0, 0x11_00_00)])
        us = all_code_points -skips
    else:
        us = make_Ranges(rngs)
    us
    txt = ''.join(chr(cp) for cp in us.iter_ints_(reverse=False))
    if rngs is None:
        #print(len(txt)) #974596 #0xedf04
        assert len(txt) == 974596 == 0xEDF04
    return txt
def mk_utf8_bytes4all_chars_of_unicode(rngs=None, /):
    '-> bytes#utf8'
    if not rngs is None:
        rngs = mk_tuple(rngs)
    return _mk_utf8_bytes4all_chars_of_unicode(rngs)
@cache
def _mk_utf8_bytes4all_chars_of_unicode(rngs=None, /):
    '-> bytes#utf8'
    txt = mk_txt4all_chars_of_unicode(rngs)
    utf8_bytes = txt.encode('u8')
    if rngs is None:
        assert len(utf8_bytes) == 3839120
    return utf8_bytes
def show_rngs_info4encoding6iconv_(encoding, /, *, utf8_bytes=None):
    if utf8_bytes is None:
        utf8_bytes = mk_utf8_bytes4all_chars_of_unicode()
    #from utf8 to the_encoding
    r = cmd_call(cmd:=[*'iconv  -c  -f utf-8 -t'.split(), encoding], input=utf8_bytes)
    (outs, errs, returncode, is_timeout) = r
    if 0:
        #[returncode may be 1] <<== since 『-c』 turnon
        if not returncode == 0:
            raise Exception(encoding, cmd, r)
    if errs:
        raise Exception(encoding, cmd, r)
    bs6the_encoding = outs

    #from the_encoding back to utf8
    r = cmd_call(cmd:=[*'iconv  -t utf-8 -f'.split(), encoding], input=bs6the_encoding)
    (outs, errs, returncode, is_timeout) = r
    if not returncode == 0 or errs:
        'ISO-2022-JP-2 ISO-2022-CN ISO-2022-CN-EXT HZ'
        print_err(f'buggy@52utf8:{encoding}')
        print_err(errs)
        # ++『-c』
        r = cmd_call(cmd:=[*'iconv  -c  -t utf-8 -f'.split(), encoding], input=bs6the_encoding)
        (outs, errs, returncode, is_timeout) = r

    #『-c』:if not returncode == 0: raise Exception(encoding, cmd, r)
    if errs:
        raise Exception(encoding, cmd, r)
    bs6utf84charset_of_the_encoding = outs
    txt = bs6utf84charset_of_the_encoding.decode('u8')
    print(repr(encoding))
    show_rngs_info4chars_file___txt_(encoding, txt)

def show_rngs_info4chars_files6dir_(idir='/sdcard/0my_files/tmp/1tmp.all.uncode.chars.u8...odir..back_to_u8/', /):
    d = Path(idir)
    #for ipath in sorted(d.glob('GB18030.u8')):
    for ipath in sorted(d.glob('*.u8')):
        show_rngs_info4chars_file_____path_(ipath)
def _nm2id_(nm, /):
    nm4id = (nm.replace('-', '_')
    .replace('.', '_')
    .replace(':', '_')
    )
    assert nm4id.isidentifier(), nm
    return nm4id
def show_rngs_info4chars_file___path_(ipath, /):
    nm = ipath.stem
    print(repr(nm))
    nm4id = _nm2id_(nm)
    if 0:
        with open(ipath, 'rt', encoding='u8') as ifile:
            txt = ifile.read()
    else:
        bs = ipath.read_bytes()
        txt = bs.decode('u8')
    txt
    show_rngs_info4chars_file___txt_(nm, txt)

def show_rngs_info4chars_file___txt_(encoding, txt, /):
    'txt :: sorted [char]'
    nm = encoding
    #print(repr(nm))
    nm4id = _nm2id_(nm)
    bad = False
    if 0b001:
        c_ = txt[0]
        for c in txt:
            if not c_ <= c:
                bad = True
                print(c_+c)
                print(f'{ord(c_):X}:{ord(c):X}')
            c_ = c
        r'''[[[
===ver2:不含PUA:跳过5个:
FFFF:FFFD
skip:ISO-10646-UCS-2

FFFF:FFFD
skip:UCS-2-INTERNAL

FFFF:FFFD
skip:UCS-2-SWAPPED

FFFF:FFFD
skip:UCS-2BE

FFFF:FFFD
skip:UCS-2LE
'



===ver1:含PUA
'GB18030'
毛病出在私用区...PUA
︒︑
FE12:FE11
︙
FE19:E797
𠃌
200CC:E819
龴
E81D:9FB4
龵
E825:9FB5
龶
E82A:9FB6
𡗗龸
215D7:9FB8
𢦏
2298F:E83C
龹
E842:9FB9
龺
E853:9FBA
𤇾
241FE:E856
龻
E863:9FBB
        #]]]'''#'''
    if bad:
        print(f'skip:{nm}')
        return#continue
    if 1:
        rngs = sorted_ints_to_iter_nontouch_ranges(map(ord, txt))
            #C99
            #raise TypeError('not sorted_unique_ints: {} {}'.format(end-1, last))
            #TypeError: not sorted_unique_ints: 12 10
            #
            #'\r'出毛病:
            #snippet -c 8 -n 3 -b 0 /sdcard/0my_files/tmp/1tmp.all.uncode.chars.u8
            #  没毛病
            #毛病出在:universal newlines mode
            #
            #
            #'GB18030'
            #
            #TypeError: not sorted_unique_ints: 65042 65041
            #
    else:
        rngs = sorted_ints_to_iter_nontouch_ranges(sorted(map(ord, txt)))
    rngs = make_Ranges(rngs)
    print(rngs.len_ints())
    print(rngs.len_rngs())
    if 0:
        #print(f'{nm4id}4hxXhxsz_ls = (') #)
        print(f'{nm4id}_8hxXhxsz_ls = (') #)
        print(stable_repr__expand_top_layer(rngs.to_hexXhexszpair_list()))
        #(
        print(')')
    if 1:
        #print(f'{nm4id}4hx2sz = (') #)
        print(f'{nm4id}_8hx2sz = (') #)
        print(stable_repr__expand_top_layer(rngs.to_hex2sz()))
        #(
        print(')')
#end-def show_rngs_info4chars_file___txt_(encoding, txt, /):


if 0b000:
    show_rngs_info4encoding6iconv_('ascii', utf8_bytes=''.join(map(chr, range(0x100))).encode('u8'))
    quit(0)
if 0b000:
    show_rngs_info4all_encodings6iconv_(encodingss=[['gbk'], ['ascii'], ['utf-8']], utf8_bytes='a一'.encode('u8'), chars7included='一', regex4excluded_encoding_names='(?i)^(?:UTF|UCS).*$')
    quit(0)
if 0b000:
    show_rngs_info4all_encodings6iconv_(encodingss=[['hz']], utf8_bytes=mk_utf8_bytes4all_chars_of_unicode([(0,0xD800), (0xF900,0x1_0000)]))
    quit(0)
    r'''[[[
>>> b'\x7e'.decode('hz')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'hz' codec can't decode byte 0x7e in position 0: incomplete multibyte sequence
>>> b'\x7e'.decode('ascii')
'~'
>>> b'\x7e'.decode('gb2312')
'~'
>>> '~'.encode('hz')
b'~~'
>>> b'\x7e\x7e'.decode('hz')
'~'



$ py ../lots/NOTE/encoding/iconv.txt.py | more
buggy@52utf8:hz
b'\niconv: (stdin):2:94: cannot convert\n'
######################
'hz'
######################
######################
'hz'
'hz'
7572
3632
hz_8hx2sz = (
{0x0
: 126
,0x7F
: 1
... ...
... ...
... ...
,0xFFE3
: 1
,0xFFE5
: 1
}
)
######################
    #]]]'''#'''

if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call(globals(), None)
        #main()

