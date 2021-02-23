r'''
py script/欧路词典.py search -t '计算机词汇' -i  /sdcard/0my_files/unzip/eudb_en/1922908499.eudb    -v 1
py script/欧路词典.py search -t '计算机词汇' -i  /sdcard/0my_files/unzip/eudb_en/1922908499.eudb    -v 2
py script/欧路词典.py search -t '计算机词汇' -i  /sdcard/0my_files/unzip/eudb_en/1922908499.eudb    -v 3
==>> 1046


py script/欧路词典.py search -t '中华成语大词典' -i  /sdcard/0my_files/unzip/eudb_en/315772229.eudb    -v 3
==>> 1046


py script/欧路词典.py readline  -i  /sdcard/0my_files/unzip/eudb_en/1922908499.eudb    -b 1046   -n '"\r"'
'计算机词汇@这是一本计算机词汇，包含了6130多 个词条。'
py script/欧路词典.py readline  -i  /sdcard/0my_files/unzip/eudb_en/1922908499.eudb    -b 1046   -n '"@"'
'计算机词汇'


py script/欧路词典.py readline    -b 1046   -n '"@"'    -i  /sdcard/0my_files/unzip/eudb_en/1522017926.eudb
'新世纪汉英科技大词典'

for i in ${ls}; do echo $i ; done

cd /sdcard/0my_files/unzip/eudb_en/
for i in $(ls) ; do py $my_txt/script/欧路词典.py readline    -b 1046   -n '"@"'    -i  $i ; done
'汉语大辞典'
'新世纪汉英科技大词典'
'计算机词汇'
'r'
'中华成语大词典'
'现代汉语词典'
'新世纪英汉科技大词典'




中华成语大词典
计算机词汇


====
欧路词典 @com.eusoft.eudic

目标:
    本地词库 -> 名称

view /sdcard/0my_files/unzip/eudb_en/1922908499.eudb

$ grep 计算机 -r
Binary file 1522017926.eudb matches
Binary file 1922908499.eudb matches
Binary file 20017.eudb matches
Binary file 375916128.eudb matches
Binary file 99569493.eudb matches
$ grep 计算机词 1922908499.eudb
Binary file 1922908499.eudb matches

$ grep 计算机词汇 1922908499.eudb
Binary file 1922908499.eudb matches


>>> '计算机词汇'.encode('u8')
b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe8\xaf\x8d\xe6\xb1\x87'



see:
    seed.iters.find
        #search subseq
        #using failure_func
    nn_ns.bin.stream_search
        #search subseq
        #using polynomial hash
    seed.seq_tools.seq_index_if
        #search value
        #using predicator



#'''

import codecs
import ast
from io import TextIOWrapper
from pathlib import Path
from seed.iters.find import iter_search_subseq_on_stream
from nn_ns.bin.stream_search import iter_search_all




r'''
def iter_search_subseq_on_stream(istream, subseq, *, overlap:bool, last_pos2restart_pos=None, _ver=None, offset=0):
def iter_search_all(key, file_obj):
'''

def iter_search_1(fin, bs):
    return iter_search_all(bs, fin)
def _iter_search_2_3(_ver, fin, bs):
    return iter_search_subseq_on_stream(fin, bs, overlap=False, _ver=_ver)
def iter_search_2(fin, bs):
    return _iter_search_2_3(2, fin, bs)
def iter_search_3(fin, bs):
    return _iter_search_2_3(3, fin, bs)

  e /storage/emulated/0/0my_files/git_repos/python3_src/seed/text/StepDecoder.py
def iter_read_lines_ex(bin_fin, pos, *, encoding, newline, **kwargs):
    '-> Iter (pos, line_without_NL)'
    # line donot contains newline at end
    assert len(newline) == 1
    bin_fin.seek(pos)
    Decoder = codecs.getincrementaldecoder(encoding)
    decoder = Decoder()
    ls = []
    err = 0
    ch = ''
    #def push(err, ls):

    while 1:
        assert ch == ''
        while 1: #skip err
            if err:
                next_line_begin_pos = bin_fin.tell()
            elif not ls:
                #no err then start a new line
                curr_line_begin_pos = bin_fin.tell()
            bs = bin_fin.read(1)
            assert ch == ''
            try:
                ch = decoder.decode(bs, final=not len(bs))
                #if ch: print(f'{ch!r}')
            except UnicodeDecodeError:
                err = 1
                decoder.reset()
                if not bs:
                    break
            else:
                break
        if not bs or err or ch == newline:
            #not bs <=> eof
            #err => eof or recovery from failure with new ch
            # bs and not err => new ch
            yield (curr_line_begin_pos, ''.join(ls))
            ? = next_line_begin_pos = ?
            ls.clear()
        else:
            if ch:
                ls.append(ch)
        ch = ''
        err = 0
        if not bs:
            break
    return

    return
    fin = TextIOWrapper(bin_fin, encoding=encoding, newline=None, **kwargs)
    ls = []
    while 1:
        try:
            ch = fin.read(1)
        except:
            yield ''.join(ls)
            raise
        print(f'{ch!r}')
        if not ch or ch == newline:
            yield ''.join(ls)
            ls = []
        else:
            ls.append(ch)
        if not ch:
            break
    return
    try:
        for line in fin:
            yield line
            begin = bin_fin.tell()
    except:
        print(bin_fin.tell())
        print(fin.tell())
        raise
    #return iter(fin)



if 0:
    ifname = '/sdcard/0my_files/unzip/eudb_en/1922908499.eudb'
    ifname = Path(ifname)
    idir = ifname.dir()


def main(args=None):
    import argparse
    from seed.for_libs.for_argparse.subcmd import ArgParserPrepare, mk_group
    from seed.helper.get_args_kwargs import mk_GetArgsKwargs as G, xcall

    parser = argparse.ArgumentParser(
        description='search encoded bytes of text in binary file, output offset'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )

    定位词库名的位置 = ArgParserPrepare([], [


    G('-v', '--method_version', type=int, required=True
                        , choices=(1,2,3)
                        , help='input file path')
    ,G('-i', '--input', type=str, required=True
                        , help='input file path')
    ,G('-t', '--text', type=str, required=True
                        , help='input text to search')
    ,G('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input text encoding')
        ], {})
    读取词库名 = ArgParserPrepare([], [
    G('-i', '--input', type=str, required=True
                        , help='input file path')
    ,G('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input text encoding')
    ,G('-b', '--byte_offset', type=int, required=True
                        , help='line begin at offset in bytes')
    ,G('-n', '--newline', type=str, required=True
                        , help='line sep')
    ,G('-sz', '--num_lines', type=int
                        , default=1
                        , help='num_lines to show; default 1; num_lines < 0 => all ')
        ], {})
    顶级设置 = ArgParserPrepare([], [
        ], {mk_group('subcmd'):dict(search=定位词库名的位置, readline=读取词库名)})
    #parser.add_subparsers('a')
    顶级设置.fill_to(parser)
    #raise


    args = parser.parse_args(args)
    subcmd = args.subcmd
    nm = f'_main_subcmd_{subcmd}'
    f = globals()[nm]
    f(args)

def _main_subcmd_search(args):
    ifname = args.input
    encoding = args.encoding
    text = args.text
    _ver = args.method_version

    bs = text.encode(encoding)
    f = [iter_search_1, iter_search_2, iter_search_3][_ver-1]
    with open(ifname, 'rb') as fin:
        for location in f(fin, bs):
            print(location)
            break
        else:
            pass

def _main_subcmd_readline(args):
    ifname = args.input
    encoding = args.encoding
    byte_offset = args.byte_offset
    newline = args.newline
    newline = ast.literal_eval(newline)
    num_lines = args.num_lines


    with open(ifname, 'rb') as fin:
        it = iter_read_lines_ex(fin, byte_offset, encoding=encoding, newline=newline)
        if num_lines >= 0:
            it = islice(it, num_lines)
        for pos, line in it:
            print(f"{pos} {line!r}")
            break
        else:
            pass


if __name__ == "__main__":
    main()





