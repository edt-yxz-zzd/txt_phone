
r'''
py script/extract_html_text.py

read_htmls_then_write_text

view-source:file:///sdcard/0my_files/tmp/wget_/novel/m.biqugelu.com/164535/1.html


#'''


import bs4
from pathlib import Path
from seed.internet.html_ast import HtmlAstOps, MarkupLang

def iter_idx_html_fname_pairs(idir):
    for i in range(1, 94+1):
        yield (i, idir / f'{i}.html')
class Globals:
    idir = r'/sdcard/0my_files/tmp/wget_/novel/m.biqugelu.com/164535/'
    idir = Path(idir)
    ofname = idir / '琼明神女录.txt'
    omode = 'wt'
    oencoding = iencoding = 'gb18030'
    idx_html_fname_pairs = iter_idx_html_fname_pairs(idir)



def read_htmls_then_write_text(idx_html_fname_pairs, ofname, omode, *, iencoding, oencoding):
    ops = HtmlAstOps()
    def oprint(*args, **kw):
        return print(*args, **kw, file=fout)
    with open(ofname, omode, encoding=oencoding) as fout:
        for idx, html_fname in idx_html_fname_pairs:
            html_doc = html_fname.read_text(encoding=iencoding)
            obj = ops.建(html_doc, markup_lang=MarkupLang.HTML)

            oprint(f'\n\n第{idx}章【【【【{idx}】】】】\n\n')
            if 1:
                it = ops.搜索后代(obj, 'p')
                for p in it:
                    txt = ops.得文本(p)
                    oprint(txt)
                    #print(p.name)
                    #input()
            elif 0:
                print(obj.string) #None
                break
            elif 0:
                txt = ops.得文本(obj) #without \n
                print(txt)
            elif 0:
                txts = ops.枚举文本(obj)
                for txt in txts:
                    print(txt)
            else:
                raise logic-err



if 1:
    G = Globals
    read_htmls_then_write_text(G.idx_html_fname_pairs, G.ofname, G.omode, iencoding=G.iencoding, oencoding=G.oencoding)





