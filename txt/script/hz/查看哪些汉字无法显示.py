#__all__:goto
r'''[[[
e script/hz/查看哪些汉字无法显示.py
!mv script/查看哪些汉字无法显示.py script/hz/

py -m nn_ns.app.adhoc_argparser__main__call8module   script.hz.查看哪些汉字无法显示   @main1 :../../../tmp/out4py/script.hz.查看哪些汉字无法显示.py.out.html
view ../../../tmp/out4py/script.hz.查看哪些汉字无法显示.py.out.html
<p>#(0xE400, 0xE5E9)</p>
<p>#(0xE600, 0xE6D0)</p>
<p>#(0xE815, 0xE870)</p>
    部首-特化
...剩下的，高位面，部分汉字有字体，离散严重，也不知 字体文件 是怎么设计的。
e others/app/gvim/set_font.txt




script.hz.查看哪些汉字无法显示
py -m nn_ns.app.debug_cmd   script.hz.查看哪些汉字无法显示
py -m nn_ns.app.doctest_cmd script.hz.查看哪些汉字无法显示:f -v
from script.hz.查看哪些汉字无法显示 import f
#]]]'''
__all__ = r'''
'''.split()#'''
__all__

def _():
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper

from nn_ns.CJK.CJK_data.raw.汉字相关字符范围 import union_ranges
from seed.tiny import fprint
from seed.io.may_open import open4w, open4w_err, open4r

def show_hzs(prefix, begin, end, /, *, fout, prefix_per_line, suffix_per_line):
    hzs = ''.join(map(chr, range(begin, end)))
    fprint(f"{prefix_per_line!s}{prefix!s}{hzs!s}{suffix_per_line!s}", file=fout)
def show_hex_uint_pairs(prefix, uint_pairs, /, *, fout, prefix_per_line, suffix_per_line):
    for a, b in uint_pairs:
        assert a >= 0
        assert b >= 0
        fprint(f"{prefix_per_line!s}{prefix!s}(0x{a:X}, 0x{b:X}){suffix_per_line!s}", file=fout)

def 查看哪些汉字无法显示(fout, sz_per_line, prefix_per_line, suffix_per_line, prefix4hzs_line, prefix4block_header, /):
    kwargs = dict(fout=fout, prefix_per_line=prefix_per_line, suffix_per_line=suffix_per_line)
    for (begin, end) in union_ranges:
        show_hex_uint_pairs(prefix4block_header, [(begin, end)], **kwargs)
        r = end % sz_per_line
        end_ = end -r
        for i in range(begin, end_, sz_per_line):
            show_hzs(prefix4hzs_line, i, i+sz_per_line, **kwargs)
        if r:
            show_hzs(prefix4hzs_line, end_, end_+r, **kwargs)
        fprint(file=fout)

def main1(may_opath=None, /, *, force=False, sz_per_line=16, prefix_per_line='<p>', suffix_per_line='</p>', prefix4hzs_line='+', prefix4block_header='#'):
    with open4w(may_opath, force=force, xencoding='utf8') as fout:
        查看哪些汉字无法显示(fout, sz_per_line, prefix_per_line, suffix_per_line, prefix4hzs_line, prefix4block_header)

if __name__ == "__main__":
    pass
