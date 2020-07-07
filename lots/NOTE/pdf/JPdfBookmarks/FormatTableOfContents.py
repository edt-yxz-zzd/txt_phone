
r'''
0. remove empty line:
    rex"^\s*$" => ""
1. format to JPdfBookmarks_cli.exe
    "3.3.3 Title and I  234 " => "3.3.3 Title and I/234"
    rex"^(?P<title>.*?)\s*(?P<page_num>\d+)\s*$" => rex"^\g<title>/\g<page_num>$"
2. indent
    "3.3.3 Title/444" => "\t\t3.3.3 Title/444"
3. offset
    +7 "...333" => "...340"
    rex"^(?P<prefix>.*?)(?P<page_num>\d+)\s*$" => rex"^\g<prefix>{page_num+offset})$"


'''


import re

old_bookmark_rex = re.compile(r"^(?P<title>.*?)\s*(?P<page_num>\d+)\s*$")
new_bookmark_rex = re.compile(r"\g<title>/\g<page_num>")
def reformat_bookmarks(bookmarks:"Iter bookmark"):
    for bookmark in bookmarks:
        if not bookmark or bookmark.isspace():
            continue
        yield reformat_bookmark(bookmark)
def reformat_bookmark(bookmark):
    r'"title \d+ " => "title/\d+"'
    return old_bookmark_rex.sub(new_bookmark_rex.pattern, bookmark)

assert reformat_bookmark("  t 3 ") == "  t/3"


def step1(fname, encoding='utf-8'):
    lines = read_lines(fname, encoding=encoding)
    return list(reformat_bookmarks(lines))
def read_lines(fname, encoding='utf-8'):
    with open(fname, encoding=encoding) as fin:
        return list(fin)

# print(step1("算法的乐趣(2015)(王晓华)[目录].u8"))


indent_bookmark_rex = re.compile(r"^(?P<ignored>\s*)(?P<levels>(?:\d+(?:\.\d+)*)?).*$")
def indent_bookmark(bookmark):
    r'"3.3 ..." => "\t3.3 ..."'
    m = indent_bookmark_rex.match(bookmark)
    assert m
    if not m:
        raise logic-error
    ignored = m.group('ignored')
    levels = m.group('levels')
    indent_count = levels.count('.')
    return '\t'*indent_count + bookmark[len(ignored):]
def indent_bookmarks(bookmarks):
    return list(map(indent_bookmark, bookmarks))
assert indent_bookmark('afaf') == 'afaf'
assert indent_bookmark(' 3.3. 3 afaf') == '\t3.3. 3 afaf'

# print(indent_bookmarks(step1("算法的乐趣(2015)(王晓华)[目录].u8")))

def step2(bookmarks, fname, encoding='utf-8'):
    lines = indent_bookmarks(bookmarks)
    output_lines(lines, fname, encoding=encoding)
def output_lines(lines, fname, encoding='utf-8'):
    bs = '\n'.join(lines).encode(encoding)
    with open(fname, 'xb') as fout:
        fout.write(bs)


# step2(step1("算法的乐趣(2015)(王晓华)[目录].u8"), "算法的乐趣(2015)(王晓华)[目录]2.u8")


offset_bookmark_rex = re.compile(r"^(?P<prefix>.*?)(?P<page_num>\d+)\s*$")
def offset_bookmark(bookmark, offset):
    m = offset_bookmark_rex.match(bookmark)
    if not m:
        raise Exception("not a bookmark: {!r}".format(bookmark))
    prefix = m.group('prefix')
    page_num = m.group('page_num')
    return '{!s}{!r}'.format(prefix, int(page_num)+offset)

def offset_bookmarks(bookmarks, offset):
    return [offset_bookmark(bookmark, offset) for bookmark in bookmarks]
assert offset_bookmark('...3', 2) == '...5'


def tranforms(bookmarks, offset):
    bookmarks = reformat_bookmarks(bookmarks)
    bookmarks = indent_bookmarks(bookmarks)
    bookmarks = offset_bookmarks(bookmarks, offset)
    return bookmarks
def steps(in_fname, out_fname, offset=0, iencoding='utf-8', oencoding='utf-8'):
    lines = read_lines(in_fname, encoding=iencoding)
    bookmarks = tranforms(lines, offset)
    output_lines(bookmarks, out_fname, encoding=oencoding)


# steps("算法的乐趣(2015)(王晓华)[目录].u8", "算法的乐趣(2015)(王晓华)[bookmarks].u8", offset=144-126)





