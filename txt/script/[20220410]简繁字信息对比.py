r'''
显示我搜集到的繁简字信息与统一码标准数据库ver13_0的异同
显示消除非平凡繁简属性字后的1869与2513

py script/简繁字信息对比.py 显示消除非平凡繁简属性字后的1869与2513 -o script/简繁字信息对比.py.显示消除非平凡繁简属性字后的1869与2513.out.txt
view script/简繁字信息对比.py.显示消除非平凡繁简属性字后的1869与2513.out.txt
!du -h script/简繁字信息对比.py.显示消除非平凡繁简属性字后的1869与2513.out.txt
    16K

py script/简繁字信息对比.py 显示我搜集到的繁简字信息与统一码标准数据库ver13_0的异同 -o script/简繁字信息对比.py.显示我搜集到的繁简字信息与统一码标准数据库ver13_0的异同.out.txt
view script/简繁字信息对比.py.显示我搜集到的繁简字信息与统一码标准数据库ver13_0的异同.out.txt
!du -h script/简繁字信息对比.py.显示我搜集到的繁简字信息与统一码标准数据库ver13_0的异同.out.txt
    200K
    184K





py script/简繁字信息对比.py > script/简繁字信息对比.py.out.txt
view script/简繁字信息对比.py.out.txt


[[
  from nn_ns.CJK.cjk_subsets.hanzi import cjk_common_subset_1869
  对比一下:
    nn_ns.CJK.CJK_data.汉字繁简
    nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0

e script/简繁字信息对比.py
  from nn_ns.CJK.CJK_data.汉字繁简 import (
    简繁字对集
        ,繁体字到简体字串
        ,简体字到繁体字串
    )
  view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字繁简.py
    简繁字对集
        繁体字到简体字串
        简体字到繁体字串
        ====上面是读取已打包好的数据，下面是解析生成
        view ../../python3_src/nn_ns/CJK/CJK_data/raw/parse_繁简.py
          从网上搜集的繁简字信息，但不含UCD::Unihan::Unihan_Variants.txt
  from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0 import readonly_parsed_result4ver13_0, readonly_simplified_result4ver13_0
      view /storage/emulated/0/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_Variants.txt
.readonly_simplified_result
    :: {kind: {hz: sorted_hz_str}}
.readonly_parsed_result
    :: {kind: [((hz, hex), [((hz, hex), [src])])]}
[('kSimplifiedVariant', 'kTraditionalVariant')]

]]
#'''

from pprint import pprint
from seed.tiny import echo, print_err, mk_fprint
from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0 import readonly_parsed_result4ver13_0, readonly_simplified_result4ver13_0
from nn_ns.CJK.CJK_data.汉字繁简 import (
    简繁字对集
        ,繁体字到简体字串
        ,简体字到繁体字串
    )
from seed.mapping_tools.dict_op import mapping_grouped_zipped_symmetric_partition__immutable
from nn_ns.CJK.cjk_subsets.hanzi import cjk_common_subset_1869, cjk_common_subset_2513


def 清理无效(forward__hz2hzs, backward__hz2hzs, /):
    return {hz:hzs for hz, hzs in forward__hz2hzs.items() if not (hz == hzs and backward__hz2hzs[hzs] == hz)}
def _cmp(lhs, rhs, /):
    'lhs, rhs :: {hz: sorted_hz_str}'
    (lonly_dict, grouped_zipped_common_dict, ronly_dict) = mapping_grouped_zipped_symmetric_partition__immutable(None, lhs, rhs)
    diff_zipped_common_dict = grouped_zipped_common_dict[False]
    same_zipped_common_dict = grouped_zipped_common_dict[True]
    #return (lonly_dict, diff_zipped_common_dict, ronly_dict)
    ls = (lonly_dict, diff_zipped_common_dict, same_zipped_common_dict, ronly_dict)
    nms = 'lonly_dict diff_zipped_common_dict same_zipped_common_dict ronly_dict'.split()
    return ({nm:len(d) for nm, d in zip(nms, ls)}, *[x for nm_d in zip(nms, ls) for x in nm_d])


def _pack_hzs(hzs, /):
    hzs = ''.join(sorted(hzs))
    return hzs
def _merge_hzss(*hzss):
    s = set()
    s.update(*hzss)
    hzs = _pack_hzs(s)
    return hzs
def _subtract__hzs(lhs, rhs, /):
    s = set(lhs) - set(rhs)
    hzs = _pack_hzs(s)
    return hzs
def _remove_spaces(hzs, /):
    hzs = _pack_hzs(hzs.split())
    #more! to sorted hz instead of word
    hzs = _pack_hzs(hzs)
    return hzs


cjk_common_subset_1869 = _remove_spaces(cjk_common_subset_1869)
cjk_common_subset_2513 = _remove_spaces(cjk_common_subset_2513)

统一码囗繁体字到简体字串 = readonly_simplified_result4ver13_0['kSimplifiedVariant']
统一码囗简体字到繁体字串 = readonly_simplified_result4ver13_0['kTraditionalVariant']

我搜集囗繁体字到简体字串 = 清理无效(繁体字到简体字串, 简体字到繁体字串)
我搜集囗简体字到繁体字串 = 清理无效(简体字到繁体字串, 繁体字到简体字串)



_hzss = [
统一码囗繁体字到简体字串
,统一码囗简体字到繁体字串
,我搜集囗繁体字到简体字串
,我搜集囗简体字到繁体字串
]
非平凡繁简属性字串 = _merge_hzss(*_hzss)
cjk_common_subset_1869__removed_TS_hz = _subtract__hzs(cjk_common_subset_1869, 非平凡繁简属性字串)
cjk_common_subset_2513__removed_TS_hz = _subtract__hzs(cjk_common_subset_2513, 非平凡繁简属性字串)
def _show_len(**kw):
    for nm, xs in sorted(kw.items()):
        print(f'len({nm!s}) = {len(xs)!r}')

def _removed_TS_hz__then__show_len(fout, all_TS_hzs, TS='TS', /, **kw):
    print = mk_fprint(fout)
    for nm, hzs in sorted(kw.items()):
        nALL = len(hzs)
        print(f'len({nm!s}) = {nALL!r}')
        hzs__removed_TS_hz = _subtract__hzs(hzs, all_TS_hzs)
        nRes = len(hzs__removed_TS_hz)
        nTS = nALL - nRes
        print(f'len({nm!s}__removed_{TS}_hz) = {nRes!r} = {nALL!r} - {nTS!r}')
        print(f'({nm!s}__removed_{TS}_hz{nTS}__{nRes!r} = "{hzs__removed_TS_hz!s}")')
        hzs__TS_hz = _subtract__hzs(hzs, hzs__removed_TS_hz)
        assert len(hzs__TS_hz) == nTS
        print(f'({nm!s}__{TS}_hz{nTS} = "{hzs__TS_hz!s}")')
        print()
        print()
def 显示消除非平凡繁简属性字后的1869与2513(fout, /):
    _removed_TS_hz__then__show_len(fout
        ,非平凡繁简属性字串
        ,cjk_common_subset_1869=cjk_common_subset_1869
        ,cjk_common_subset_2513=cjk_common_subset_2513
        )
    r'''
cjk_common_subset_1869__removed_TS_hz238__1631 = cjk_common_subset_1869 - cjk_common_subset_1869__TS_hz238

cjk_common_subset_2513__removed_TS_hz286__2227 = cjk_common_subset_2513 - cjk_common_subset_2513__TS_hz286




len(cjk_common_subset_1869) = 1869
len(cjk_common_subset_1869__removed_TS_hz) = 1631 = 1869 - 238
len(cjk_common_subset_2513) = 2513
len(cjk_common_subset_2513__removed_TS_hz) = 2227 = 2513 - 286


    #'''

if 0:
    _show_len(
        cjk_common_subset_1869__removed_TS_hz=cjk_common_subset_1869__removed_TS_hz
        ,cjk_common_subset_2513__removed_TS_hz=cjk_common_subset_2513__removed_TS_hz
        )


def _tT(hz, /):
    head = ' '*4
    print(hz)
    print(head, 统一码囗繁体字到简体字串[hz])
    print(head, 繁体字到简体字串[hz])
    print(head, 我搜集囗繁体字到简体字串[hz])
def _tS(hz, /):
    head = ' '*4
    print(hz)
    print(head, 统一码囗简体字到繁体字串[hz])
    print(head, 简体字到繁体字串[hz])
    print(head, 我搜集囗简体字到繁体字串[hz])

def 显示我搜集到的繁简字信息与统一码标准数据库ver13_0的异同(fout, /):
    异同囗我搜集囗统一码 = _cmp(我搜集囗繁体字到简体字串, 统一码囗繁体字到简体字串)
#pprint([[[[]]]], indent=0, compact=True)
    pprint(异同囗我搜集囗统一码, stream=fout, compact=True, indent=0)
    r'''[[[
    same_zipped_common_dict:
  '徵': ('征徵', '征徵'),
  '瀋': ('沈渖', '沈渖'),
  '線': ('线缐', '线缐'),
  '鍾': ('钟锺', '钟锺'),
  ...
#]]]'''

if 0:
    _tT('鳥')
    _tS('鸟')
    r'''[[[

_tT('萬')
_tS('万')
萬
     万
     万
     万
万
     萬
     万萬
     万萬

_tT('鳥')
_tS('鸟')
鳥
     鸟
     鸟
     鸟
鸟
     鳥
     鳥
     鳥
#]]]'''

main_routines = [
显示我搜集到的繁简字信息与统一码标准数据库ver13_0的异同
,显示消除非平凡繁简属性字后的1869与2513
]



main_routines = {f.__name__:f for f in main_routines}
def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='繁简字信息相关'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('case', type=str, choices=sorted(main_routines.keys())
                        , help='choose one main_routine')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'


    main_routine = main_routines[args.case]
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        main_routine(fout)
if __name__ == "__main__":
    main()


