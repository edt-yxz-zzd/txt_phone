#__all__:goto
r'''[[[
e script/汇编冫牛津英汉双解.py

script.汇编冫牛津英汉双解
py -m nn_ns.app.debug_cmd   script.汇编冫牛津英汉双解 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.汇编冫牛津英汉双解:__doc__ -ht # -ff -df

[[
view ++enc=gbk /sdcard/0my_files/unzip/e_book/字词典/牛津英汉双解(第4版)TXT/0012L/L-j,k,l,m,n,o.txt
du -h '/sdcard/0my_files/unzip/e_book/字词典/牛津英汉双解(第4版)TXT/'
  14M
$ ls '/sdcard/0my_files/unzip/e_book/字词典/牛津英汉双解(第4版)TXT/'
0001A  0005E  0009I  0013M  0017Q  0021U  0025Y
0002B  0006F  0010J  0014N  0018R  0022V  0026Z
0003C  0007G  0011K  0015O  0019S  0023W
0004D  0008H  0012L  0016P  0020T  0024X

$ ls '/sdcard/0my_files/unzip/e_book/字词典/牛津英汉双解(第4版)TXT/0012L'
L-a.txt        L-f,g,h,i.txt      L-p~z.txt
L-b,c,d,e.txt  L-j,k,l,m,n,o.txt

ls '/sdcard/0my_files/unzip/e_book/字词典/牛津英汉双解(第4版)TXT/'00[0-9][0-9][A-Z]/[A-Z]*.{txt,TXT}
ls '/sdcard/0my_files/unzip/e_book/字词典/牛津英汉双解(第4版)TXT/'00[0-9][0-9][A-Z]/[A-Z]*.[tT][xX][tT]


errors:
help(codecs.Codec)
    |   'surrogateescape' - replace with private code points U+DCnn.
    |   'xmlcharrefreplace' - Replace with the appropriate XML
    |                         character reference (only for encoding).
]]

py_adhoc_call   script.汇编冫牛津英汉双解   @汇编冫牛津英汉双解扌  --ipath4dir:'/sdcard/0my_files/unzip/e_book/字词典/牛津英汉双解(第4版)TXT/'  --iencoding:gb18030   --oencoding:utf8 --may_opath4txt:/sdcard/0my_files/tmp/out4py/script.汇编冫牛津英汉双解..牛津英汉双解.4ed.out.词典.txt  +force --ierrors:surrogateescape  --oerrors:xmlcharrefreplace
view /sdcard/0my_files/tmp/out4py/script.汇编冫牛津英汉双解..牛津英汉双解.4ed.out.词典.txt
grep '&#[0-9]*;' -o /sdcard/0my_files/tmp/out4py/script.汇编冫牛津英汉双解..牛津英汉双解.4ed.out.词典.txt | sort -u
    &#56575;
        #只有一个
>>> hex(56575)
'0xdcff'

U+DCff ==>> b'\xff'
du -h /sdcard/0my_files/tmp/out4py/script.汇编冫牛津英汉双解..牛津英汉双解.4ed.out.词典.txt
    15M
tar -cvf /sdcard/0my_files/tmp/out4tar/script.汇编冫牛津英汉双解..牛津英汉双解.4ed.out.词典.txt.tar.lzma --lzma -C  /sdcard/0my_files/tmp/out4py/   script.汇编冫牛津英汉双解..牛津英汉双解.4ed.out.词典.txt
du -h /sdcard/0my_files/tmp/out4tar/script.汇编冫牛津英汉双解..牛津英汉双解.4ed.out.词典.txt.tar.lzma
    4.6M


from script.汇编冫牛津英汉双解 import *
]]]'''#'''
__all__ = r'''
汇编冫牛津英汉双解扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError



def 汇编冫牛津英汉双解扌(*, ipath4dir, may_opath4txt, iencoding, oencoding='utf8', force=False, ierrors=None, oerrors=None):
    from seed.tiny_.check import check_type_is
    check_type_is(bool, force)
    check_type_is(str, iencoding)
    check_type_is(str, oencoding)
    if not iencoding:raise TypeError
    if not oencoding:raise TypeError
    from seed.io.may_open import open4w, open4w_err, open4r
    from pathlib import Path
    ipath4dir = Path(ipath4dir)
    if not ipath4dir.is_dir():raise NotADirectoryError(ipath4dir)
    #omode = 'wt' if force else 'xt'
    with open4w(may_opath4txt, force=force, xencoding=oencoding, errors=oerrors) as ofile:
        for line in _iter_lines(ipath4dir, iencoding, ierrors):
            line = line.strip() # remove '\n'
            if not line:continue
            print(line, file=ofile)
def _iter_lines(ipath4dir, iencoding, ierrors, /):
    mid_dirs = sorted(ipath4dir.iterdir())
    #for j in range(26):
    for j, mid_dir in enumerate(mid_dirs):
        if not mid_dir.is_dir():raise NotADirectoryError(mid_dir)
        n = 1+j
        ch = chr(ord('A')+j)
        mid_nm = f'{n:0>4}{ch}'
        #mid_dir = ipath4dir/mid
        #if not mid_dir.samefile(_mid_dir):raise Exception(mid_dir, _mid_dir)
        if not mid_dir.name == mid_nm:raise Exception(mid_dir, mid_nm)
        for ipath4txt in sorted(mid_dir.iterdir()):
            nm = ipath4txt.name
            if not nm.startswith(ch):raise Exception(ipath4txt)
            if not nm.lower().endswith('.txt'):raise Exception(ipath4txt)
            with open(ipath4txt, 'rt', encoding=iencoding, errors=ierrors) as ifile:
                try:
                    yield from ifile
                except UnicodeError:
                    from seed.tiny import print_err
                    print_err(ipath4txt)
                        #/sdcard/0my_files/unzip/e_book/字词典/牛津英汉双解(第4版)TXT/0001A/A-c.txt
                        #   ^UnicodeDecodeError: 'gbk' codec can't decode byte 0xff in position 882: illegal multibyte sequence
                        #   ^UnicodeDecodeError: 'gb18030' codec can't decode byte 0xff in position 882: illegal multibyte sequence
                    raise
#end-def _iter_lines(ipath4dir, /)

__all__
from script.汇编冫牛津英汉双解 import *
