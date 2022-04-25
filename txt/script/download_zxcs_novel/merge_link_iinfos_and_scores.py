r'''[[[

e script/download_zxcs_novel/merge_link_iinfos_and_scores.py
[[
  合并 两个输出文件:
    view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.html.iinfos.txt
    view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.html.iinfos.scores.txt
  为：
    view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.scored.html
]]


#37 39 42
[[
py script/download_zxcs_novel/merge_link_iinfos_and_scores.py  --remove_www_in_URL    -ii /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.txt    -id2sc /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.scores.txt    -o /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.scored.html
file:///sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.scored.html
]]
[[
py script/download_zxcs_novel/merge_link_iinfos_and_scores.py  --remove_www_in_URL    -ii /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/39.html.iinfos.txt    -id2sc /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/39.html.iinfos.scores.txt    -o /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/39.scored.html
file:///sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/39.scored.html
]]
[[
py script/download_zxcs_novel/merge_link_iinfos_and_scores.py  --remove_www_in_URL    -ii /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.html.iinfos.txt    -id2sc /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.html.iinfos.scores.txt    -o /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.scored.html
file:///sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.scored.html
]]

#]]]'''


from pathlib import Path
from ast import literal_eval
import bs4


def ipath2obj__read_then_eval(ipath, /, *, encoding):
    txt = ipath.read_text(encoding)
    obj = literal_eval(txt)
    return obj

def merge_link_iinfos_and_scores__read_in(ipath4iinfos, ipath4ID2scores, /, encoding):
    link_iinfos = ipath2obj__read_then_eval(ipath4iinfos, encoding=encoding)
    (date__str, novel_page_idx2scores) = ipath2obj__read_then_eval(ipath4ID2scores, encoding=encoding)

    link_scored_iinfos = tuple(
        (collectlist_idx, novel_page_idx, target_label, description, novel_page_idx2scores[novel_page_idx])
        for (collectlist_idx, novel_page_idx, target_label, description) in link_iinfos
        )
    hash(link_scored_iinfos)
    return (date__str, link_scored_iinfos)

def merge_link_iinfos_and_scores__to_html_doc(date__str, link_scored_iinfos, /, to_remove_www_in_URL):
    '->soup   #scored-variant-of:collect_links_from_zxcs_sort_pages.py::Main4mk_collectlist_webpage<to_remove_www_in_URL>::def mk_page_from_link_iinfos(sf, link_iinfos, /):'
    #sf.xxx: to_remove_www_in_URL, mk_tag, mk_link_info_tag, mk_zxcs_novel_link, mk_zxcs_download_page_link
    if 1:
        to_remove_www_in_URL
        mk_tag = bs4.BeautifulSoup(features="lxml").new_tag


    #def mk_page_from_link_iinfos(sf, link_iinfos, /):
    def main():
        soup = mk_tag('html')
        if 1:
            date__str
            title = f'【评分快照日期：{date__str}】'

            head_soup = mk_tag('head')
            soup.append(head_soup)

            title_soup = mk_tag('title')
            head_soup.append(title_soup)

            title_soup.append(title)

        body_soup = mk_tag('body')
        soup.append(body_soup)

        if 1:
            title
            p_soup = mk_tag('p')
            body_soup.append(p_soup)

            p_soup.append('\n')
            p_soup.append(mk_tag('br'))
            p_soup.append(title)

        list_soup = mk_tag('ol')
        body_soup.append(list_soup)
        for (collectlist_idx, novel_page_idx, target_label, description, scores) in link_scored_iinfos:
            link_info_tag = mk_link_info_tag(collectlist_idx, novel_page_idx, target_label, description, scores)
            list_item_soup = mk_tag('li')
            list_item_soup.append(link_info_tag)
            list_soup.append(list_item_soup)
        return soup

    #def mk_link_info_tag(sf, collectlist_idx, novel_page_idx, target_label, description, /):
    def mk_link_info_tag(collectlist_idx, novel_page_idx, target_label, description, scores, /):
        novel_link = mk_zxcs_novel_link(novel_page_idx)
        download_page_link = mk_zxcs_download_page_link(novel_page_idx)
            # 12842 -> http://www.zxcs.me/download.php?id=12842

        div_soup = mk_tag('div')
        link_soup = mk_tag('a', href=novel_link, target='_blank')
        link_soup.append(target_label)
        div_soup.append(link_soup)
        p_soup = mk_tag('p')
        div_soup.append(p_soup)
        #bug:p_soup.append(description.replace('\n', '\n<br/>'))
        def add_EOL(p_soup, /):
            #too ugly:p_soup.append(mk_tag('br'))
            p_soup.append('\n')
            p_soup.append(mk_tag('br'))
        if 1:
            p_soup.append(f'{collectlist_idx}:{novel_page_idx}:{target_label}')
            add_EOL(p_soup)
            add_EOL(p_soup)
        for s in description.split('\n'):
            p_soup.append(s)
            add_EOL(p_soup)
        if 1:
            #bug:p_soup.append(mk_tag('a', href=download_page_link, rel="external nofollow", target="_blank", title="点击下载"))
            #无法显示，因为没有『内容』
            #??为何？原页面可以？<a href="http://www.zxcs.me/download.php?id=12842" rel="external nofollow" target="_blank" title="点击下载"></a>
            a4download = mk_tag('a', href=download_page_link, rel="external nofollow", target="_blank")
            a4download.append("点击下载")
            p_soup.append(a4download)

        add_EOL(p_soup)
        if 1:
            scores
            #92人:仙草; 8人:粮草; 5人:干草; 7人:枯草; 30人:毒草;
            #〖92人:仙草〗〖8人:粮草〗〖5人:干草〗〖7人:枯草〗〖30人:毒草〗
            a, b, c, d, e = scores

            p_soup.append(f'〖{a}人:仙草〗〖{b}人:粮草〗〖{c}人:干草〗〖{d}人:枯草〗〖{e}人:毒草〗')

        add_EOL(p_soup)
        add_EOL(p_soup)
        return div_soup
    #def mk_zxcs_novel_link(sf, novel_page_idx, /):
    def mk_zxcs_novel_link(novel_page_idx, /):
        novel_link = f'http://www.zxcs.me/post/{novel_page_idx}'
        if to_remove_www_in_URL:
            novel_link = novel_link.replace('www.', '')
        return novel_link
    #def mk_zxcs_download_page_link(sf, novel_page_idx, /):
    def mk_zxcs_download_page_link(novel_page_idx, /):
        download_page_link = f'http://www.zxcs.me/download.php?id={novel_page_idx}'
        if to_remove_www_in_URL:
            download_page_link = download_page_link.replace('www.', '')
        return download_page_link


    return main()



def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='merge (xxx.html.iinfos.txt, xxx.html.iinfos.scores.txt) -> xxx.scored.html'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--remove_www_in_URL', action='store_true'
                        , default = False
                        , help='202204 found change: http://www.zxcs.me -->> http://zxcs.me; 小说页面 带『www.』时出错不显示评分')
    parser.add_argument('-ii', '--link_iinfos_txtfile', type=Path, required=True
                        , help='input file path for "xxx.html.iinfos.txt"')
    parser.add_argument('-id2sc', '--link_info_ID2scores_txtfile', type=Path, required=True
                        , help='input file path for "xxx.html.iinfos.scores.txt"')

    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path for "xxx.scored.html"')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    ipath4iinfos = args.link_iinfos_txtfile
    ipath4ID2scores = args.link_info_ID2scores_txtfile

    (date__str, link_scored_iinfos) = merge_link_iinfos_and_scores__read_in(ipath4iinfos, ipath4ID2scores, encoding=encoding)
    html_soup = merge_link_iinfos_and_scores__to_html_doc(date__str, link_scored_iinfos, to_remove_www_in_URL=args.remove_www_in_URL)
    html_soup__str = str(html_soup)


    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        print(html_soup__str, file=fout)
if __name__ == "__main__":
    main()



