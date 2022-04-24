
r'''[[[
e script/download_zxcs_novel/collect_links_from_zxcs_sort_pages.py
py /sdcard/0my_files/git_repos/txt_phone/txt/script/download_zxcs_novel/collect_links_from_zxcs_sort_pages.py -sort 37 -od /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/
    ###
    mkdir -p /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/
    mkdir -p script/download_zxcs_novel/zxcs_pages/via_py_download/20210919


idx:
    sort_idx_str
    sort_page_idx
    novel_page_idx
    collectlist_idx
    ===
    sort_link:
        http://www.zxcs.me/sort/37/page/1
        http://www.zxcs.me/sort/{sort_idx_str}/page/{sort_page_idx}
    novel_link:
        http://www.zxcs.me/post/12842
        http://www.zxcs.me/post/{novel_page_idx}
    download_page_link
        http://www.zxcs.me/download.php?id=12842
        http://www.zxcs.me/download.php?id={novel_page_idx}
    html_file_basename:
        001.html
        {outdir}/{sort_idx_str}/{sort_page_idx:0>max(3,...)}.html

view ../../python3_src/nn_ns/internet/webpage/fetch_webpage.py
from nn_ns.internet.webpage.fetch_webpage import fetch_webpage__str

fixed:
    20220418
        『<br>』之前加『\n』
        『点击下载』由属性值 移作文本
        移除『www.』，否则进入小说页面无法显示评分
            # 以前 小说页面&下载页面 都有
            #   现在 都没有


####################################
####################################
####################################
####################################
####################################
#用python直接下载的页面 与 手机上看到的 不同！！
#这里用手机firefox复制源文件
    mkdir -p script/download_zxcs_novel/zxcs_pages/via_py_download/20210919
view script/download_zxcs_novel/zxcs_pages/zxcs-37-1@20210829.html
<!-- @20210829 view-source:http://www.zxcs.me/sort/37/page/1 -->
37-1 ~ 37-???
按时间倒序，我收集时 从后往前

<div id="m">
<ul>
<li>
<div class="info">
  <h2><a href="http://www.zxcs.me/post/12630">《道长去哪了》（校对版全本）作者：八宝饭</a> <span>大约 3 天前</span></h2>
  <p>

【TXT大小】：4.10 MB
【内容简介】：　　顾佐举着宗门的牌匾，热情如火，眉毛笑成了弯月：“劳驾，这位兄台，你愿意加入怀仙馆么？”
　　这世道，修仙难，招人更难！
优质订阅书源，收集于网络！
文本由河洛校对！</p>
</div>
</li>
<li>
<div class="info">
  <h2><a href="http://www.zxcs.me/post/13156">《大奉打更人》（校对版全本）作者：卖报小郎君</a> <span>大约 4 天前</span></h2>
  <p>

【TXT大小】：7.92 MB
【内容简介】：　　这个世界，有儒；有道；有佛；有妖；有术士。
　　警校毕业的许七安幽幽醒来，发现自己身处牢狱之中，三日后流放边陲……
　　他起初的目的只是自保，顺便在这个没有人权的社会里当个富家翁悠闲度日。
　　……
　　多年后，许七安回首前尘，身后是早已逝去的敌人，以及累累白骨。
　　滚滚长江东逝水，浪花淘尽英雄，是非成败转头空。
　　青山依旧在，几度夕阳红。
　　PS：本书不悲剧！
优质订阅书源，收集于网络！
文本由河洛校对！</p>
</div>
</li>
<li>
... ...
... ...
</ul>
</div><div class="clear"></div>
<div id="diypage"> <a class="down_pagenavi" href="http://www.zxcs.me/sort/37/page/2">下一页</a> </div><div class="clear"></div>






####################################
####################################
####################################
####################################
####################################
#用python直接下载的页面 与 手机上看到的 不同！！
#这里用python直接下载
# script/download_zxcs_novel/zxcs_pages/via_py_download/20210919/
view script/download_zxcs_novel/zxcs_pages/via_py_download/20210919/zxcs.me@20210919-sort-37-page-1.html
view script/download_zxcs_novel/zxcs_pages/via_py_download/20210919/zxcs.me@20210919-sort-37-page-47.html
view script/download_zxcs_novel/zxcs_pages/via_py_download/20210919/zxcs.me@20210919-sort-37-page-48.html
view script/download_zxcs_novel/zxcs_pages/via_py_download/20210919/zxcs.me@20210919-sort-37-page-199.html


view script/download_zxcs_novel/zxcs_pages/via_py_download/20210919/zxcs.me@20210919-sort-37-page-1.html
    	<dl id="plist">
			<dt><a href="http://www.zxcs.me/post/12859">《心魔种道》（校对版全本）作者：废纸桥</a></dt>
            <dd class="des">

【TXT大小】：3.88 MB
【内容简介】：　　诸位同道，诸位大师、道长、师太、仙子、魔尊、教主们，欢迎来到我的世界，享受穿梭诸界带来的至高愉悦与无上享受（滑稽笑）。
优质订阅书源，收集于网络！
文本由河洛校对！</dd>
			<dd>
分类：	<a href="http://www.zxcs.me/sort/37">精校仙侠</a>
	&nbsp; <a href="http://www.zxcs.me/tag/%E4%BF%AE%E7%9C%9F%E6%96%87%E6%98%8E">修真文明</a> &nbsp;&nbsp;&nbsp;发布者：<a href="http://www.zxcs.me/author/2955" >花小雪</a>&nbsp;&nbsp;&nbsp;时间：大约 0 天前<div align="right"><a href="http://www.zxcs.me/post/12859" class="vw">查看全文</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><br />

			</dd>
		</dl>
    	<dl id="plist">
			<dt><a href="http://www.zxcs.me/post/13210">《大周仙吏》（校对版全本）作者：荣小荣</a></dt>
            <dd class="des">

【TXT大小】：4.19 MB
【内容简介】：　　穿越妖魅横生，群魔乱舞的仙侠世界，李慕开始真的只想苟活，可他无意中救了的小狐狸忽然口吐人言，说要以身相许……
　　这是一个现代青年穿越仙侠世界，斩妖除魔，匡扶正义的故事。
优质订阅书源，收集于网络！
文本由河洛校对！</dd>
			<dd>
分类：	<a href="http://www.zxcs.me/sort/37">精校仙侠</a>
	&nbsp; <a href="http://www.zxcs.me/tag/%E4%BF%AE%E7%9C%9F%E6%96%87%E6%98%8E">修真文明</a> &nbsp;&nbsp;&nbsp;发布者：<a href="http://www.zxcs.me/author/20470" >Ray</a>&nbsp;&nbsp;&nbsp;时间：大约 4 天前<div align="right"><a href="http://www.zxcs.me/post/13210" class="vw">查看全文</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><br />

			</dd>
		</dl>
		<div id="pagenavi"> <span>1</span>  <a href="http://www.zxcs.me/sort/37/page/2">2</a>  <a href="http://www.zxcs.me/sort/37/page/3">3</a>  <a href="http://www.zxcs.me/sort/37/page/4">4</a>  <a href="http://www.zxcs.me/sort/37/page/5">5</a>  <a href="http://www.zxcs.me/sort/37/page/6">6</a> <em>...</em> <a href="http://www.zxcs.me/sort/37/page/48" title="尾页">&raquo;</a></div>


view script/download_zxcs_novel/zxcs_pages/via_py_download/20210919/zxcs.me@20210919-sort-37-page-47.html
		<div id="pagenavi"><a href="http://www.zxcs.me/sort/37" title="首页">&laquo;</a><em>...</em> <a href="http://www.zxcs.me/sort/37/page/42">42</a>  <a href="http://www.zxcs.me/sort/37/page/43">43</a>  <a href="http://www.zxcs.me/sort/37/page/44">44</a>  <a href="http://www.zxcs.me/sort/37/page/45">45</a>  <a href="http://www.zxcs.me/sort/37/page/46">46</a>  <span>47</span>  <a href="http://www.zxcs.me/sort/37/page/48">48</a> </div>

view script/download_zxcs_novel/zxcs_pages/via_py_download/20210919/zxcs.me@20210919-sort-37-page-48.html
		<div id="pagenavi"><a href="http://www.zxcs.me/sort/37" title="首页">&laquo;</a><em>...</em> <a href="http://www.zxcs.me/sort/37/page/43">43</a>  <a href="http://www.zxcs.me/sort/37/page/44">44</a>  <a href="http://www.zxcs.me/sort/37/page/45">45</a>  <a href="http://www.zxcs.me/sort/37/page/46">46</a>  <a href="http://www.zxcs.me/sort/37/page/47">47</a>  <span>48</span> </div>


#]]]'''



import bs4
#from bs4 import BeautifulSoup
from pathlib import Path
from itertools import chain
from nn_ns.internet.webpage.fetch_webpage import fetch_webpage__str
import os#makedirs


class G:
    working_path = Path(__file__).parent
    sort_page_path = working_path/'zxcs_pages/zxcs-37-1@20210829.html'
    output_dir_path = working_path/'output'
    output_collect_infoss_path = output_dir_path/'collect-from-zxcs-37-1@20210829.html'
    #####
    prev_page_link_label = '上一页'
    next_page_link_label = '下一页'

def rpartition_last_uint_from_link(url):
    #rpartition
    _, _, idx_str = url.rpartition('/')
    return int(idx_str)
class Main4mk_collectlist_webpage:
    r'''
view script/download_zxcs_novel/zxcs_pages/zxcs-37-12842.html
<!-- view-source:http://www.zxcs.me/post/12842 -->
    <a href="http://www.zxcs.me/download.php?id=12842" rel="external nofollow" target="_blank" title="点击下载"></a>
    #'''

    def __init__(sf, /, *, to_remove_www_in_URL):
        sf.mk_tag = bs4.BeautifulSoup(features="lxml").new_tag
        sf.to_remove_www_in_URL = to_remove_www_in_URL
    def mk_page_from_link_infoss(sf, link_infoss, /,*, reverse:bool):
        if reverse:
            def f(it):
                return reversed((*it,))
            link_infoss = f(map(f, link_infoss))
        link_infos = chain.from_iterable(link_infoss)

        soup = sf.mk_tag('html')
        body_soup = sf.mk_tag('body')
        soup.append(body_soup)
        list_soup = sf.mk_tag('ol')
        body_soup.append(list_soup)
        for collectlist_idx, link_info in enumerate(link_infos, 1):
            (novel_link, target_label, description) = link_info
            link_info_tag = sf.mk_link_info_tag(collectlist_idx, novel_link, target_label, description)
            list_item_soup = sf.mk_tag('li')
            list_item_soup.append(link_info_tag)
            list_soup.append(list_item_soup)
        return soup
    def mk_link_info_tag(sf, collectlist_idx, novel_link, target_label, description, /):
        if sf.to_remove_www_in_URL:
            novel_link = novel_link.replace('www.', '')
        description = description.strip()
        novel_page_idx = rpartition_last_uint_from_link(novel_link)
            #12842 <- http://www.zxcs.me/post/12842
        download_page_link = sf.mk_zxcs_download_page_link(novel_page_idx)
            # 12842 -> http://www.zxcs.me/download.php?id=12842

        div_soup = sf.mk_tag('div')
        link_soup = sf.mk_tag('a', href=novel_link, target='_blank')
        link_soup.append(target_label)
        div_soup.append(link_soup)
        p_soup = sf.mk_tag('p')
        div_soup.append(p_soup)
        #bug:p_soup.append(description.replace('\n', '\n<br/>'))
        def add_EOL(p_soup, /):
            #too ugly:p_soup.append(sf.mk_tag('br'))
            p_soup.append('\n')
            p_soup.append(sf.mk_tag('br'))
        if 1:
            p_soup.append(f'{collectlist_idx}:{novel_page_idx}:{target_label}')
            add_EOL(p_soup)
            add_EOL(p_soup)
        for s in description.split('\n'):
            p_soup.append(s)
            add_EOL(p_soup)
        if 1:
            #bug:p_soup.append(sf.mk_tag('a', href=download_page_link, rel="external nofollow", target="_blank", title="点击下载"))
            #无法显示，因为没有『内容』
            #??为何？原页面可以？<a href="http://www.zxcs.me/download.php?id=12842" rel="external nofollow" target="_blank" title="点击下载"></a>
            a4download = sf.mk_tag('a', href=download_page_link, rel="external nofollow", target="_blank")
            a4download.append("点击下载")
            p_soup.append(a4download)

        add_EOL(p_soup)
        add_EOL(p_soup)
        return div_soup
    def mk_zxcs_download_page_link(sf, novel_page_idx, /):
        download_page_link = f'http://www.zxcs.me/download.php?id={novel_page_idx}'
        if sf.to_remove_www_in_URL:
            download_page_link = download_page_link.replace('www.', '')
        return download_page_link
class Extract_novel_link_infos_from_zxcs_me_sort_page__webpage_via_python_fetch:
    def __init__(sf, page_txt_or_html_file):
        sf.soup = bs4.BeautifulSoup(page_txt_or_html_file, 'lxml')
    def get_last_page_link(sf):
        [navigation_pages_soup] = sf.soup.find_all('div', attrs={'id':'pagenavi'})
        last_link_soup = navigation_pages_soup.find_all('a')[-1]
        last_page_link = last_link_soup['href']
        return last_page_link
    def iter_extract_novel_link_infos(sf):
        it = sf.soup.find_all('dl', attrs={'id':'plist'})
        for info_soup in it:
            yield sf.extract_novel_link_info(info_soup)
    def extract_novel_link_info(sf, info_soup):
        link_soup = info_soup.dt.a
        novel_link = link_soup['href']
        novel_title_author = str(link_soup.string)
        it = info_soup.find_all('dd')
        novel_info = ''.join(str(dd_soup.string) for dd_soup in it)
        return (novel_link, novel_title_author, novel_info)


class Extract_novel_link_infos_from_zxcs_me_sort_page__webpage_via_phone_firefox:
    def __init__(sf, page_txt_or_html_file):
        sf.soup = bs4.BeautifulSoup(page_txt_or_html_file, 'lxml')
    def may_get_prev_page_link(sf):
        d = sf.get_navigation_page_link_dict()
        return d.get(G.prev_page_link_label)
    def may_get_next_page_link(sf):
        d = sf.get_navigation_page_link_dict()
        return d.get(G.next_page_link_label)
    def get_navigation_page_link_dict(sf):
        navigation_pages_soup = sf.soup.find('div', id='diypage')
        it = navigation_pages_soup.find_all('a', attrs={'class':'down_pagenavi'})
        d = {}
        for navigation_page_link_soup in it:
            description, sort_link = sf.extract_navigation_page_info(navigation_page_link_soup)
            if description in d: raise ValueError('unknown format or logic error')
            d[description] = sort_link
        return d
    def extract_navigation_page_info(sf, navigation_page_link_soup):
        description = str(navigation_page_link_soup.string)
        sort_link = navigation_page_link_soup['href']
        return (description, sort_link)
    def iter_extract_novel_link_infos(sf):
        m_soup = sf.soup.find('div', id='m')
        if m_soup is None: raise ValueError('unknown zxcs.me/sort/??/page/?? page format')
        it = m_soup.ul.find_all('div', attrs={'class':'info'})
        for info_soup in it:
            yield sf.extract_novel_link_info(info_soup)
    def extract_novel_link_info(sf, info_soup):
        link_soup = info_soup.a
        novel_link = link_soup['href']
        novel_title_author = str(link_soup.string)
        novel_info = str(info_soup.p.string)
        return (novel_link, novel_title_author, novel_info)



def _t(*, to_remove_www_in_URL):
    sort_page_path = G.sort_page_path
    with open(sort_page_path, 'rb') as fin:
        x = Extract_novel_link_infos_from_zxcs_me_sort_page__webpage_via_phone_firefox(fin)
        [*infos] = x.iter_extract_novel_link_infos()
    #print(infos)
    assert len(infos)==15
    main4mk_collectlist_webpage = Main4mk_collectlist_webpage(to_remove_www_in_URL=to_remove_www_in_URL)
    html_soup = main4mk_collectlist_webpage.mk_page_from_link_infoss([infos], reverse=True)
    #print(str(html_soup))

    output_collect_infoss_path = G.output_collect_infoss_path
    with open(output_collect_infoss_path, 'xt', encoding='utf8') as fout:
        print(str(html_soup), file=fout)
#_t(to_remove_www_in_URL=False)



def total2stem_len(*, total, min_len):
    L = max(min_len, len(str(total)))
    return L
class MkHtmlFileBaseName:
    def __init__(sf, /,*, total, min_len=3, prefix='', suffix='.html'):
        sf.stem_len = total2stem_len(total=total, min_len=min_len)
        sf.suffix = suffix
        sf.prefix = prefix
    def mk_html_file_basename(sf, sort_page_idx, /):
        L = sf.stem_len
        _name_ = str(sort_page_idx)
        pad_0s = '0'*(L-len(_name_))
        name = f'{sf.prefix}{pad_0s}{_name_}{sf.suffix}'
        return name

class Main:
    def main(sf, /,*, may_ofname, outdir, sort_idx_str, may_total, timeout, to_remove_www_in_URL):
        main4download = Main4download(timeout=timeout, to_remove_www_in_URL=to_remove_www_in_URL)
        if may_total is None:
            total = main4download.detect_total_pages_of_zxcs_sort(sort_idx_str=sort_idx_str)
        else:
            total = may_total
        assert total >= 1


        int(sort_idx_str)
        outdir = Path(outdir)
        if may_ofname is None:
            ofname = outdir/f'{sort_idx_str}.html'
        else:
            ofname = Path(ofname)

        main4download.download_zxcs_sort_pages_to(sort_idx_str=sort_idx_str, total=total, outdir=outdir)

        main4extract = Main4extract(via_phone=False)
        main4extract.mk_zxcs_novel_info_collectlist_page_from_sort_pages_from(ofname=ofname, indir=outdir, sort_idx_str=sort_idx_str, may_total=total, to_remove_www_in_URL=to_remove_www_in_URL)

class Main4extract:
    r'''
    def extract_zxcs_novel_infoss_of_sort_pages_from(sf, /,*, indir, sort_idx_str, may_total):
    def mk_zxcs_novel_info_collectlist_page_from_sort_pages_from(sf, /,*, ofname, indir, sort_idx_str, may_total, to_remove_www_in_URL):
    #'''
    def __init__(sf, /,*, via_phone:bool):
        sf.Extract_novel_link_infos_from_zxcs_me_sort_page = Extract_novel_link_infos_from_zxcs_me_sort_page__webpage_via_phone_firefox if via_phone else Extract_novel_link_infos_from_zxcs_me_sort_page__webpage_via_python_fetch
    def mk_zxcs_novel_info_collectlist_page_from_sort_pages_from(sf, /,*, ofname, indir, sort_idx_str, may_total, to_remove_www_in_URL):
        html_soup = sf._mk_zxcs_novel_info_collectlist_page_from_sort_pages_from__soup(indir=indir, sort_idx_str=sort_idx_str, may_total=may_total, to_remove_www_in_URL=to_remove_www_in_URL)
        with open(ofname, 'xt', encoding='utf8') as fout:
            print(str(html_soup), file=fout)
    def _mk_zxcs_novel_info_collectlist_page_from_sort_pages_from__soup(sf, /,*, indir, sort_idx_str, may_total, to_remove_www_in_URL):
        infoss = sf.extract_zxcs_novel_infoss_of_sort_pages_from(indir=indir, sort_idx_str=sort_idx_str, may_total=may_total)
        main4mk_collectlist_webpage = Main4mk_collectlist_webpage(to_remove_www_in_URL=to_remove_www_in_URL)
        html_soup = main4mk_collectlist_webpage.mk_page_from_link_infoss(infoss, reverse=True)
        return html_soup
    def extract_zxcs_novel_infoss_of_sort_pages_from(sf, /,*, indir, sort_idx_str, may_total):
        indir_sort_dir = indir/sort_idx_str
        if may_total is None:
            ifnames = indir_sort_dir.iter_dir()
            ifnames = sorted(ifnames)
        else:
            total = may_total
            mk_basename = MkHtmlFileBaseName(total=total).mk_html_file_basename
            def f():
                for sort_page_idx in range(1, total+1):
                    name = mk_basename(sort_page_idx)
                    yield indir_sort_dir/name
            ifnames = f()
        infoss = sf.iter_extract_zxcs_sort_page_infoss(ifnames)
        return infoss
    def iter_extract_zxcs_sort_page_infoss(sf, ifnames, /):
        return map(sf.iter_extract_zxcs_sort_page_infos, ifnames)
    def iter_extract_zxcs_sort_page_infos(sf, ifname, /):
        x = sf.Extract_novel_link_infos_from_zxcs_me_sort_page(ifname.read_text('utf8'))
        infos = x.iter_extract_novel_link_infos()
        return infos





class Main4download:
    r'''
    def download_zxcs_sort_pages_to(sf, /,*, sort_idx_str, total, outdir):
    def detect_total_pages_of_zxcs_sort(sf, /,*, sort_idx_str):
    #'''

    def __init__(sf, /,*, timeout, to_remove_www_in_URL):
        sf.timeout = timeout
        sf.to_remove_www_in_URL = to_remove_www_in_URL
    def download_webpage(sf, link, /):
        return fetch_webpage__str(link, timeout=sf.timeout)
    def download_webpage_to(sf, link, /,*, ofname):
        with open(ofname, 'xt', encoding='utf8') as fout:
            txt = sf.download_webpage(link)
            fout.write(txt)
    def download_webpages_to(sf, name_link_pairs, /,*, outdir):
        for name, link in name_link_pairs:
            ofname = outdir/name
            sf.download_webpage_to(link, ofname=ofname)
    def download_zxcs_sort_pages_to(sf, /,*, sort_idx_str, total, outdir):
        idx_link_pairs = sf.iter_zxcs_sort_page_links_with_page_idx(sort_idx_str=sort_idx_str, total=total)
        mk_basename = MkHtmlFileBaseName(total=total).mk_html_file_basename
        def f(idx_link_pair):
            sort_page_idx, sort_link = idx_link_pair
            name = mk_basename(sort_page_idx)
            return name, sort_link
        sf.download_webpages_to(map(f, idx_link_pairs), outdir=outdir/sort_idx_str)
    def iter_zxcs_sort_page_links_with_page_idx(sf, /,*, sort_idx_str, total):
        for sort_page_idx in range(1, total+1):
            sort_link = sf.mk_zxcs_sort_page_link(sort_idx_str=sort_idx_str, sort_page_idx=sort_page_idx)
            yield sort_page_idx, sort_link
    def mk_zxcs_sort_page_link(sf, /,*, sort_idx_str, sort_page_idx):
        sort_link = f'http://www.zxcs.me/sort/{sort_idx_str}/page/{sort_page_idx}'
        if sf.to_remove_www_in_URL:
            sort_link = sort_link.replace('www.', '')
        return sort_link



    def detect_total_pages_of_zxcs_sort(sf, /,*, sort_idx_str):
        total = sf.detect_total_pages_of_zxcs_sort__webpage_via_python_fetch(sort_idx_str=sort_idx_str)
        assert total >= 1
        return total
    def detect_total_pages_of_zxcs_sort__webpage_via_python_fetch(sf, /,*, sort_idx_str):
        sort_link = sf.mk_zxcs_sort_page_link(sort_idx_str=sort_idx_str, sort_page_idx=1)
        txt = sf.download_webpage(sort_link)
        x = Extract_novel_link_infos_from_zxcs_me_sort_page__webpage_via_python_fetch(txt)
        last_page_link = x.get_last_page_link()
        last_page_idx = rpartition_last_uint_from_link(last_page_link)
        total = last_page_idx
        assert total >= 1
        return total
    def detect_total_pages_of_zxcs_sort__webpage_via_phone_firefox(sf, /,*, sort_idx_str):
        sort_page_idx = 19
        while 1:
            sort_page_idx = sort_page_idx*10+9
            sort_link = sf.mk_zxcs_sort_page_link(sort_idx_str=sort_idx_str, sort_page_idx=sort_page_idx)
            #print(sort_link)
            txt = sf.download_webpage(sort_link)
            #print(txt)
            x = Extract_novel_link_infos_from_zxcs_me_sort_page__webpage_via_phone_firefox(txt)
            d = x.get_navigation_page_link_dict()
            n = len(d)
            if not n <= 2: raise logic-err
            if n==1:
                #may_get_prev_page_link
                may_prev_page_link = d.get(G.prev_page_link_label)
                if may_prev_page_link is None: raise logic-err
                prev_page_link = may_prev_page_link
                prev_page_idx = rpartition_last_uint_from_link(prev_page_link)
                last_page_idx = 1+prev_page_idx
                break
            elif n==0:
                last_page_idx = 1
                break
            elif n==2:
                continue
            else:
                raise logic-err
        ...
        total = last_page_idx
        assert total >= 1
        return total


def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='collect novel infos per sort at www.zxcs.me then merge as a list webpage'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-sort', '--sort_idx_str', type=str
                        , required=True
                        , help='download:"http://www.zxcs.me/sort/{sort_idx_str}/page/{sort_page_idx}"')
    parser.add_argument('-N', '--total', type=int, default=None
                        , help='total subpages of {sort_idx_str}')
    parser.add_argument('-od', '--outdir', type=Path
                        , required=True
                        , help='top outdir path; pages of each sort are stored inside "{outdir}/{sort_idx_str}"')
    parser.add_argument('-o', '--output', type=str
                        , default=None
                        #, required=True
                        , help='output file path')
    parser.add_argument('--timeout', type=int, default=60
                        , help='timeout for fetch_webpage')
    r'''
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    #'''
    parser.add_argument('--remove_www_in_URL', action='store_true'
                        , default = False
                        , help='202204 found change: http://www.zxcs.me -->> http://zxcs.me; 小说页面 带『www.』时出错不显示评分')

    args = parser.parse_args(args)
    r'''
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
    #'''
    outdir = args.outdir
    sort_idx_str = args.sort_idx_str
    may_total = args.total
    may_ofname = args.output
    timeout = args.timeout
    to_remove_www_in_URL = args.remove_www_in_URL


    os.makedirs(outdir/sort_idx_str, exist_ok=True)
    Main().main(may_ofname=may_ofname, outdir=outdir, sort_idx_str=sort_idx_str, may_total=may_total, timeout=timeout, to_remove_www_in_URL=to_remove_www_in_URL)

def _main4download_example_page_to_programming():
    #用python直接下载的页面 与 手机上看到的 不同！！
    #这里用python直接下载
    sort_links = r'''
        http://www.zxcs.me/sort/37/page/199
        http://www.zxcs.me/sort/37/page/48
        http://www.zxcs.me/sort/37/page/47
        http://www.zxcs.me/sort/37/page/2
        http://www.zxcs.me/sort/37/page/1
        http://www.zxcs.me/sort/37/page/0
        http://www.zxcs.me/sort/37/page/
        '''.split()
        #0~=1
        #199~=48
    date = '20210919'
    outdir = Path(fr'script/download_zxcs_novel/zxcs_pages/via_py_download/{date}/')
    main4download = Main4download(timeout=60, to_remove_www_in_URL=False)
    sort_idx_str = '37'
    sort_page_idc = [199, 48, 47, 2, 1, 0]
    for sort_page_idx in sort_page_idc:
        sort_link = main4download.mk_zxcs_sort_page_link(sort_idx_str=sort_idx_str, sort_page_idx=sort_page_idx)
        ofname = outdir/f'zxcs.me@{date}-sort-{sort_idx_str}-page-{sort_page_idx}.html'
        main4download.download_webpage_to(sort_link, ofname=ofname)
if __name__ == "__main__":
    #_main4download_example_page_to_programming()
    main()


