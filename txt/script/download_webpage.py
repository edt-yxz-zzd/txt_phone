
r'''
py script/download_webpage.py > /sdcard/0my_files/tmp/wget_/cmd.txt
bash /sdcard/0my_files/tmp/wget_/cmd.txt
======
    http://www.dmxs.bid/45691/
      耽美肉文网
      http://www.dmxs.bid/45691/66.html
      http://www.dmxs.bid/45691/66-2.html
      1-17
      84-4
      85-11
      86-6
      87-7
      88-10
      89-11
      90-4
      91-5
      92-5
      93-6
      94-7
        wget -k -r -l1 http://www.dmxs.bid/45691/
        wget -k -r -l1 http://m.dmxs.bid/45691/

e /storage/emulated/0/0my_files/tmp/wget_/novel/m.dmxs.bid/45691/1.html
view ++enc=gbk
<h2 class="headline">【】（1-3）(1/17)</h2>

<div id="content">勾住了她腰间罗裙的衣带，轻声道：「我来为陆姐姐宽</p><p>衣。」</p><p>喜欢琼明神女录请大家收藏：(m.dmxs.bid),耽美肉文网更新速度最快。</p></div>



mv -t /sdcard/0my_files/novel/2/  '/storage/emulated/0/0my_files/tmp/wget_/novel/m.dmxs.bid/45691/琼明神女录[dmxs.bid].txt'
#'''

class G:
    prefix = r'http://m.dmxs.bid/45691/'
    fmt_1 = '{}.html'
    fmt_ge2 = '{}-{}.html'
    chapter_idc = range(1,94+1)
    page_idc = range(1, 20)
    ####
    idir = r'/storage/emulated/0/0my_files/tmp/wget_/novel/m.dmxs.bid/45691/' #'1.html'
    iencoding = 'gb18030'
    ofname = idir + '琼明神女录[dmxs.bid].txt'
    omode = 'wt'
    oencoding = iencoding = 'gb18030'
    chapter_idx_num_pages_pairs = [(1, 17), (2, 6), (3, 8), (4, 7), (5, 5), (6, 6), (7, 6), (8, 6), (9, 6), (10, 12), (11, 5), (12, 5), (13, 7), (14, 6), (15, 4), (16, 9), (17, 4), (18, 4), (19, 4), (20, 6), (21, 6), (22, 8), (23, 8), (24, 6), (25, 7), (26, 8), (27, 4), (28, 5), (29, 4), (30, 5), (31, 4), (32, 5), (33, 4), (34, 4), (35, 5), (36, 5), (37, 5), (38, 6), (39, 6), (40, 5), (41, 7), (42, 14), (43, 12), (44, 5), (45, 5), (46, 4), (47, 6), (48, 5), (49, 6), (50, 5), (51, 5), (52, 7), (53, 8), (54, 6), (55, 5), (56, 6), (57, 6), (58, 5), (59, 8), (60, 3), (61, 6), (62, 6), (63, 5), (64, 5), (65, 5), (66, 5), (67, 5), (68, 4), (69, 4), (70, 5), (71, 6), (72, 6), (73, 8), (74, 4), (75, 5), (76, 4), (77, 4), (78, 4), (79, 4), (80, 4), (81, 4), (82, 5), (83, 4), (84, 4), (85, 11), (86, 6), (87, 7), (88, 10), (89, 11), (90, 4), (91, 5), (92, 5), (93, 6), (94, 7)]


def mk_iter_hrefs(prefix, fmt_1, fmt_ge2, chapter_idc, page_idc):
    for pg in page_idc:
        fmt = prefix + (fmt_1 if pg == 1 else fmt_ge2)
        for ch in chapter_idc:
            yield fmt.format(ch, pg)

def mk_cmd(iter_hrefs):
    return 'wget -k ' + ' '.join(iter_hrefs)
    return 'wget -k -r -l0 ' + ' '.join(iter_hrefs)



if 0:
    print(mk_cmd(mk_iter_hrefs(G.prefix, G.fmt_1, G.fmt_ge2, G.chapter_idc, G.page_idc)))


import bs4
import re
from pathlib import Path
from seed.internet.html_ast import HtmlAstOps, MarkupLang
def mk_num_pages():
    rex = re.compile(r'\((\d+)/(\d+)\)')
    ops = HtmlAstOps()
    paths = mk_iter_hrefs(G.idir, G.fmt_1, G.fmt_ge2, G.chapter_idc, [1])
    ls = []
    for ch, path in enumerate(paths, 1):
        html_fname = Path(path)
        html_doc = html_fname.read_text(encoding=G.iencoding)
        obj = ops.建(html_doc, markup_lang=MarkupLang.HTML)
        #it = ops.搜索后代(obj, 'h2', )
        h2 = ops.搜得唯一后代(obj, 'h2', 属性过滤={'class':'headline'}, 文本过滤=rex)
        headline = ops.得文本(h2)
        m = rex.search(headline)
        i = int(m[1])
        total = int(m[2])
        assert i == 1
        ls.append((ch, total))
    return ls

if 0:
    ls = mk_num_pages()
    print(ls)
    assert ls == G.chapter_idx_num_pages_pairs


def mk_ch_pg_html_paths(idir, fmt_1, fmt_ge2, chapter_idx_num_pages_pairs):
    fmt_1 = idir + fmt_1
    fmt_ge2 = idir + fmt_ge2
    for ch, total in chapter_idx_num_pages_pairs:
        for pg in range(1, total+1):
            fmt = (fmt_1 if pg == 1 else fmt_ge2)
            yield ch, pg, fmt.format(ch, pg)


def merge_pages(ofname, ch_pg_html_paths, *, omode, iencoding, oencoding):
    def oprint(*args, **kw):
        return print(*args, **kw, file=fout)
    ops = HtmlAstOps()
    with open(ofname, omode, encoding=oencoding) as fout:
        for ch, pg, path in ch_pg_html_paths:
            #if not (ch,pg) == (66,4): continue
            html_fname = Path(path)
            html_doc = html_fname.read_text(encoding=iencoding)
            obj = ops.建(html_doc, markup_lang=MarkupLang.HTML)
            oprint(f'\n\n第{ch}章 第{pg}页【【【【{ch}-{pg}】】】】\n\n')
            div = ops.搜得唯一后代(obj, 'div', 属性过滤={'id':'content'})
            begin_str = '朗读'
            end_str = '喜欢琼明神女录请大家收藏'
            if 1:
                #it = ops.枚举序后文本(div)
                it = ops.枚举此后文本(div)
                for txt in it:
                    if end_str in txt: break
                    oprint(txt)
            elif 0:
                it = ops.枚举文本(div)
                for txt in it:
                    oprint(txt)
            elif 0:
                it = ops.搜索后代(div, 'p')
                for p in it:
                    txt = ops.得文本(p)
                    oprint(txt)
                    #print(p.name)
            else:
                raise logic-err
            #break

if 1:
    ch_pg_html_paths = mk_ch_pg_html_paths(G.idir, G.fmt_1, G.fmt_ge2, G.chapter_idx_num_pages_pairs)
    merge_pages(G.ofname, ch_pg_html_paths, omode=G.omode, iencoding=G.iencoding, oencoding=G.oencoding)
