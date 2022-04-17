r'''
py script/remove_unicode_reports__non_curr_version.py  '/sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/'
    仍需手动改名: pdf: tr25,tr54
cp script/remove_unicode_reports__non_curr_version.py  '/sdcard/0my_files/unicode/unicode14_0/'
[[

/sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25/index.html
py -m nn_ns.txt.encoding_cmd /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25/index.html -e utf8 gb18030 utf_16_be utf_16_le utf_32_be utf_32_le

#tr25:UTR 25 Unicode Support for Mathematics
snippet /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25/index.html
[b'%PDF-1.7\r\n%\xb5\xb5\xb5\xb5\r']

mv /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25/index.html /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25/index.html.pdf


#tr54: UTR 54 Unicode Mongolian 12.1 Snapshot
snippet /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr54/index.html
[b'%PDF-1.7\r%\xe2\xe3\xcf\xd3\r\n']

mv /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr54/index.html /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr54/index.html.pdf


#tr8: UTR 8 The Unicode Standard, Version 2.1
snippet /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr8/index.html
[b'<!DOCTYPE HTML P']

]]
[[
$ py script/remove_unicode_reports__non_curr_version.py  '/sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/'
skip: gname='tr11-h2'
skip: gname='tr45-sourcedata-6'
skip: gname='tr45-glyphs-6'
skip: gname='tr45-sourcedata-4'
skip: gname='tr45-glyphs-4'
skip: gname='tr45-sourcedata-3'
skip: gname='tr45-glyphs-3'
skip: gname='tr45-sourcedata-2'
skip: gname='tr45-glyphs-1'
skip: gname='tr45-sourcedata-1'
skip: gname='tr35-collation'
skip: gname='tr35-general'
skip: gname='tr35-numbers'
skip: gname='tr35-dates'
skip: gname='tr35-info'
skip: gname='tr35-keyboards'
skip: gname='tr51-5-archive'
skip: gname='tr51-3-archive'
skip: 'tr25' #pdf not html
skip: gname='tr36-spoofing-examples'
skip: 'tr54' #pdf not html
skip: 'tr6' #stabilized
skip: 'tr16' #stabilized
skip: 'tr22' #stabilized
skip: 'tr26' #stabilized
skip: 'tr8' #superseded
skip: 'tr27' #superseded
skip: 'tr28' #superseded
delete: 'tr20' #superseded
skip: 'tr13' #superseded








du -h '/sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/' | grep '[GM]'
1.4M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr31/print-images
1.9M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr31
2.5M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr45
1.5M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr50
4.8M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr10
1.7M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr35/tr35-66
4.5M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr35
3.1M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr39/data
3.8M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr39
9.2M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr51/images/other
11M     /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr51/images
11M     /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr51
1.8M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25
1.5M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr36/data
4.3M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr36
45M     /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/
$

#150M -> 45M
]]

9.2M    /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr51/images/other
    UTS 51 Unicode Emoji
    The word emoji comes from Japanese:
    絵 (e ≅ picture) 文字 (moji ≅ written character).


e script/remove_unicode_reports__non_curr_version.py
view /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr10/index.html
    <tr>
      <td>This Version</td>
      <td>
      <a href="tr10-45.html">https://www.unicode.org/reports/tr10/tr10-45.html</a></td>
    </tr>


view ../../python3_src/seed/internet/html_ast.py
view script/extract_html_text.py

[[[[[[[
TODO:打包？删除 旧版？
  43M  /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr35
    zip -> 10.8M
file:///storage/emulated/0/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr35
file:///storage/emulated/0/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr31/tr31-35.html
file:///storage/emulated/0/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr35/index.html
file:///storage/emulated/0/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr10/index.html
e script/remove_unicode_reports__non_curr_version.py

手动复制:
  e /sdcard/0my_files/tmp/wget_/unicode/README4www.unicode.org.txt
  手动复制:
    /sdcard/0my_files/tmp/wget_/unicode/*
    到:
    /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/
  手动移动:
    /sdcard/0my_files/tmp/wget_/unicode/*
    到:
    /sdcard/0my_files/unicode/unicode14_0/
    [[
du -h -d 3 /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/ | grep '[GM]' > /sdcard/0my_files/tmp/_.txt
view  /sdcard/0my_files/tmp/_.txt
/\d\dM
=====
11M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr10
43M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr35
21M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr51
150M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/reports
14M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/Public/zipped
28M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/Public/14.0.0
42M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/Public
14M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/versions/Unicode14.0.0
14M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org/versions
206M  /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/www.unicode.org
]]

view /mnt/m_external_sd/000edt/0my_files/unicode/unicode14_0/

]]]]]]]

#'''

import shutil
from pathlib import Path
import re
from seed.internet.html_ast import HtmlAstOps, MarkupLang
from seed.tiny import print_err



文本过滤 = re.compile('This Version')
gname4trDD__rex = re.compile(r'tr\d+[-]\d+')
basename4trDD__rex = re.compile(r'tr\d+[-]\d+(?:[.]Orientation)?[.]html')
trDD__rex = re.compile(r'tr\d+')
def check_dirname4trDD(dirname4trDD4curr_version, /):
    check_basename4trDD(f'{dirname4trDD4curr_version}.html')
def check_basename4trDD(s, /):
    if not is_basename4trDD(s): raise ValueError(f'not basename of trDD-DD.html: {s!r}')
def is_gname(s, /):
    return not None is gname4trDD__rex.fullmatch(s)
def is_basename4trDD(s, /):
    return not None is basename4trDD__rex.fullmatch(s)
def is_trDD(s, /):
    return not None is trDD__rex.fullmatch(s)
def check_trDD(s, /):
    if not is_trDD(s): raise ValueError(f'not dir trDD: {s!r}')

ops = HtmlAstOps()
def trDD_index_html2basename4trDD4curr_version__doc(doc4trDD_index_html, /):
    '-> (dirORbasename4trDD4curr_version, rpath_basename4trDD4curr_version)'
    obj = ops.建(doc4trDD_index_html, markup_lang=MarkupLang.HTML)
    td = ops.搜得唯一后代(obj, ['td'], 属性过滤={}, 文本过滤=文本过滤)
    r'''
      <td>This Version</td>
      <td>
      <a href="tr10-45.html">https://www.unicode.org/reports/tr10/tr10-45.html</a></td>

['\n', <td>
<a href="tr10-45.html">https://www.unicode.org/reports/tr10/tr10-45.html</a></td>, '\n']
3
    #'''
    if 0:
        [*xx] = ops.枚举弟妹(td)
        print_err((xx))
        print_err(len(xx))
        xx = ops.举得唯一弟妹(td)
        assert 'td' == ops.得件名(xx)
    #xx = ops.搜得唯一弟妹(td, ['td'])
    xx = ops.搜得唯一弟妹(td, True)
    a = ops.搜得唯一后代(xx, ['a'])
    try:
        rpath_basename4trDD4curr_version = a['href']
    except:
        print_err(a)
        #<span><a href="tr38-31.html">https://www.unicode.org/reports/tr38/tr38-31.html</a></span>
        raise

    #path = Path(rpath_basename4trDD4curr_version)
    if '/' in rpath_basename4trDD4curr_version:
        # tr35-66/tr35.html
        dirname4trDD4curr_version, _, _ = rpath_basename4trDD4curr_version.partition('/')
        check_dirname4trDD(dirname4trDD4curr_version)
        dirORbasename4trDD4curr_version = dirname4trDD4curr_version
    else:
        basename4trDD4curr_version = rpath_basename4trDD4curr_version
        check_basename4trDD(basename4trDD4curr_version)
        dirORbasename4trDD4curr_version = basename4trDD4curr_version
    return (dirORbasename4trDD4curr_version, rpath_basename4trDD4curr_version)




def trDD_index_html2basename4trDD4curr_version__path(path4trDD_index_html, /):
    '-> (dirORbasename4trDD4curr_version, rpath_basename4trDD4curr_version)'
    path4trDD_index_html = Path(path4trDD_index_html)
    try:
        doc = path4trDD_index_html.read_text(encoding='utf8')
    except:
        print_err(path4trDD_index_html)
        # /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25/index.html
        #   UTR 25 Unicode Support for Mathematics
        # py -m nn_ns.txt.encoding_cmd /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25/index.html -e utf8 gb18030 utf_16_be utf_16_le utf_32_be utf_32_le
        # snippet /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr25/index.html
        #   [b'%PDF-1.7\r\n%\xb5\xb5\xb5\xb5\r']
        raise
    try:
        return trDD_index_html2basename4trDD4curr_version__doc(doc)
    except:
        print_err(path4trDD_index_html)
        r'''
        # /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr6/index.html
Stabilized Technical Report

UTS #6, "A Standard Compression Scheme for Unicode" has been stabilized: There are no plans to ever publish another update for it. The last version can be found at https://www.unicode.org/reports/tr6/tr6-4.html.
        #'''
        r'''
        # /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr8/index.html

    Unicode 2.1.0

        Version 2.1.0 has been superseded by the latest version of the Unicode Standard.
        #'''
        # /sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr20/index.html
        raise


def _t1():
    path = '/sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/tr10/index.html'
    print(trDD_index_html2basename4trDD4curr_version__path(path))
    'tr10-45.html'

#_t1()


_exceptions = {*'''
    tr50-9.Orientation.html
    tr18-5.1.html
    tr35-66/tr35.html
    '''.split()
    }
def xname2gname(xname, /):
    return xname.partition('.')[0]
def remove_unicode_reports__non_curr_version_html___dir4trDD(dir4trDD, /):
    dir4trDD = Path(dir4trDD)
    check_trDD(dir4trDD.name)
    r'''
手动删:tr20
====
Stabilized Reports
UTS 	6 	A Standard Compression Scheme for Unicode
UTR 	16 	UTF-EBCDIC
UTS 	22 	Unicode Character Mapping Markup Language
UTR 	26 	Compatibility Encoding Scheme for UTF-16: 8-Bit (CESU-8)


Old Versions of the Unicode Standard (Superseded)
UTR 	4 	The Unicode Standard, Version 1.1
UTR 	8 	The Unicode Standard, Version 2.1
UAX 	27 	Unicode 3.1
UAX 	28 	Unicode 3.2


Other Superseded Reports
UTR 	1 	Proposals for Burmese (Myanmar), Khmer, and Ethiopian
UTR 	2 	Proposals for Sinhala, Mongolian, and Tibetan
UTR 	3 	Proposals for Less Common Scripts
UTR 	5 	Handling Non-Spacing Marks
UTR 	7 	Plane 14 Characters for Language Tags
UAX 	13 	Unicode Newline Guidelines
UAX 	19 	UTF-32
UAX 	21 	Case Mappings


Withdrawn or Suspended Reports
UTR 	12 	Support for Interlinear Annotations
UTR 	20 	Unicode in XML and other Markup Languages
UTR 	30 	Unicode Character Foldings
UTR 	32 	Assessing Unicode Support
UTS 	40 	BOCU-1: MIME-Compatible Unicode Compression
UTR 	49 	Unicode Character Categories
UTS 	52 	Unicode Emoji Mechanisms

    #'''
    if dir4trDD.name in ['tr54', 'tr25']:
        print_err(f'skip: {dir4trDD.name!r} #pdf not html')
        return
    if dir4trDD.name in ['tr6', 'tr16', 'tr22', 'tr26']:
        print_err(f'skip: {dir4trDD.name!r} #stabilized')
        return
    if dir4trDD.name in ['tr4', 'tr8', 'tr27', 'tr28', 'tr1', 'tr2', 'tr3', 'tr5', 'tr7', 'tr13', 'tr19', 'tr21', 'tr12', 'tr20', 'tr30', 'tr32', 'tr40', 'tr49', 'tr52']:
        if dir4trDD.name == 'tr20':
            print_err(f'delete: {dir4trDD.name!r} #superseded')
        else:
            print_err(f'skip: {dir4trDD.name!r} #superseded')
            return









    path4trDD_index_html = dir4trDD / 'index.html'
    if dir4trDD.name == 'tr20':
        _ = 'tr20-9.html'
        (dirORbasename4trDD4curr_version, rpath_basename4trDD4curr_version) = (_, _)
    else:
        (dirORbasename4trDD4curr_version, rpath_basename4trDD4curr_version) = trDD_index_html2basename4trDD4curr_version__path(path4trDD_index_html)
    is_html = dirORbasename4trDD4curr_version == rpath_basename4trDD4curr_version
    if is_html:
        basename4trDD4curr_version = dirORbasename4trDD4curr_version
    else:
        dirname4trDD4curr_version = dirORbasename4trDD4curr_version
    gname4trDD4curr_version = xname2gname(dirORbasename4trDD4curr_version)

    path4curr_version_html = dir4trDD/rpath_basename4trDD4curr_version
    assert path4curr_version_html.exists()

    xpaths = dir4trDD.glob('tr*-*')
    xpaths = [*xpaths]
    xnames = [xpath.name for xpath in xpaths]
    gnames = [xname2gname(xname) for xname in xnames]
    if not gname4trDD4curr_version in gnames: raise logic-err

    for gname, xpath in zip(gnames, xpaths):
        if not is_gname(gname):
            # tr11-h2
            print_err(f'skip: gname={gname!r}')
            continue
            raise ValueError(f'unknown howto handle: gname={gname!r}')
        if gname4trDD4curr_version == gname:
            continue

        if xpath.is_dir():
            shutil.rmtree(xpath)
        else:
            xpath.unlink()
    return
    r'''
    if is_html:
        html_paths = dir4trDD.glob('tr*-*.html')
        html_paths = [*html_paths]
        i = html_paths.index(path4curr_version_html)
        del html_paths[i]
        for html_path in html_paths:
            if 1 and html_path.name in _exceptions:
                pass
            else:
                check_basename4trDD(html_path.name)
            assert html_path.is_file()
            html_path.unlink()
    else:
        path4curr_version_dir = dir4trDD/dirname4trDD4curr_version
        assert path4curr_version_dir.exists()
        assert path4curr_version_dir.is_dir()

        dir_paths = dir4trDD.glob('tr*-*')
        dir_paths = [*dir_paths]
        i = dir_paths.index(path4curr_version_dir)
        del dir_paths[i]
        for dir_path in dir_paths:
            check_dirname4trDD(dir_path.name)
            assert dir_path.is_dir()
            dir_path.unlink()
    return
    #'''
def remove_unicode_reports__non_curr_version_html___dir4reports(dir4reports, /):
    dir4reports = Path(dir4reports)
    assert dir4reports.name == 'reports'
    trDD_paths = dir4reports.glob('tr*')
    for trDD_path in trDD_paths:
        check_trDD(trDD_path.name)
        remove_unicode_reports__non_curr_version_html___dir4trDD(trDD_path)

def _t2():
    path = '/sdcard/0my_files/unicode/unicode14_0/www.unicode.org/reports/'
    remove_unicode_reports__non_curr_version_html___dir4reports(path)

#_t2()

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='删除旧版本的UAX，以节省存储空间'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('dir4reports', type=str
                        , help='path to www.unicode.org/reports/')
    args = parser.parse_args(args)
    remove_unicode_reports__non_curr_version_html___dir4reports(args.dir4reports)

if __name__ == "__main__":
    main()


