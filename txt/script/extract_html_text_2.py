
r'''
e script/extract_html_text_2.py
py script/extract_html_text_2.py

view ++enc=gbk /storage/emulated/0/0my_files/tmp/wget_/novel/www.dzwx520.com/book_9871/index.html
view ++enc=gbk /storage/emulated/0/0my_files/tmp/wget_/novel/www.dzwx520.com/book_9871/4193399.html
<div id="htmlContent" class="contentbox">


mv -t /sdcard/0my_files/novel/2/  '/storage/emulated/0/0my_files/tmp/wget_/novel/www.dzwx520.com/book_9871/琼明神女录[dzwx520.com].txt'

#'''

href_title_pairs = \
[("4193399.html"
,"【琼明神女录】（1-3）"
)

,("4194046.html"
,"【琼明神女录】（4）"
)

,("4195196.html"
,"【琼明神女录】（5）"
)

,("4195666.html"
,"【琼明神女录】（6）"
)

,("4195667.html"
,"【琼明神女录】（7）"
)

,("4196508.html"
,"【琼明神女录】（8）"
)

,("4196803.html"
,"【琼明神女录】（9）"
)

,("4197315.html"
,"【琼明神女录】（10）"
)

,("4197823.html"
,"【琼明神女录】（11）"
)

,("4198512.html"
,"【琼明神女录】（12）"
)

,("4199483.html"
,"【琼明神女录】（13）"
)

,("4200258.html"
,"【琼明神女录】（14）"
)

,("4201778.html"
,"【琼明神女录】（15）"
)

,("4203510.html"
,"【琼明神女录】（16）"
)

,("4204699.html"
,"【琼明神女录】（17）"
)

,("4205448.html"
,"【琼明神女录】（特别篇）浅斟低唱 三万年大梦"
)

,("4207763.html"
,"【琼明神女录】（19）"
)

,("4208706.html"
,"【琼明神女录】（20）"
)

,("4209541.html"
,"【琼明神女录】同人（陆嘉静篇）"
)

,("4209542.html"
,"【琼明神女录】（21）"
)

,("4210505.html"
,"【琼明神女录】（22）"
)

,("4211010.html"
,"【琼明神女录】（23）"
)

,("4217956.html"
,"【琼明神女录】（24）"
)

,("4222527.html"
,"【琼明神女录】（25）"
)

,("4224123.html"
,"【琼明神女录】（26）"
)

,("4225773.html"
,"【琼明神女录】（27）"
)

,("4230701.html"
,"【琼明神女录】（28）"
)

,("4230702.html"
,"【琼明神女录】（29）"
)

,("4234582.html"
,"【琼明神女录】（30）"
)

,("4234863.html"
,"【琼明神女录】（31）"
)

,("4242861.html"
,"【琼明神女录】（32）"
)

,("4250737.html"
,"【琼明神女录】（33）"
)

,("4250738.html"
,"【琼明神女录】（34）"
)

,("4253337.html"
,"【琼明神女录】（35）"
)

,("4253338.html"
,"【琼明神女录】（36）"
)

,("4253339.html"
,"【琼明神女录】（37）"
)

,("4253340.html"
,"【琼明神女录】（38）"
)

,("4254500.html"
,"【琼明神女录】（39）"
)

,("4255999.html"
,"【琼明神女录】（40）"
)

,("4256216.html"
,"【琼明神女录】（41）"
)

,("4256755.html"
,"【琼明神女录】（42）"
)

,("4257414.html"
,"【琼明神女录】（43）"
)

,("4605750.html"
,"【琼明神女录】（44）"
)

,("4889690.html"
,"【琼明神女录】（45）"
)

,("4920284.html"
,"【琼明神女录】（46）"
)

,("4931041.html"
,"【琼明神女录】（静静篇）"
)

,("4961255.html"
,"【琼明神女录】（47）"
)

,("4971872.html"
,"【琼明神女录】（48）"
)

,("4971880.html"
,"【琼明神女录】（49）"
)

,("5017562.html"
,"【琼明神女录】（50）"
)

,("5038844.html"
,"【琼明神女录】（51）"
)

,("5052910.html"
,"【琼明神女录】（52）"
)

,("5102564.html"
,"【琼明神女录】（53）"
)

,("5117743.html"
,"【琼明神女录】（54）"
)

,("5140306.html"
,"【琼明神女录】（55）"
)

,("5140307.html"
,"【琼明神女录】（56）"
)

,("5152050.html"
,"【琼明神女录】（57）"
)

,("5167051.html"
,"【琼明神女录】（58）"
)

,("5219084.html"
,"【琼明神女录】（59）"
)

,("5219085.html"
,"【琼明神女录】（60）"
)

,("5219086.html"
,"【琼明神女录】（61）"
)

,("5234673.html"
,"【琼明神女录】（62）"
)

,("5321079.html"
,"【琼明神女录】（63）"
)

,("5321080.html"
,"【琼明神女录】（64）"
)

,("5321081.html"
,"【琼明神女录】（65）"
)

,("5400262.html"
,"【琼明神女录】（66）"
)

,("5400265.html"
,"【琼明神女录】（67）"
)

,("5400267.html"
,"【琼明神女录】（68）"
)

,("5400270.html"
,"【琼明神女录】（69）"
)

,("5400273.html"
,"【琼明神女录】（70）"
)

,("5400278.html"
,"【琼明神女录】（71）"
)

,("5400281.html"
,"【琼明神女录】（72）"
)

,("5400284.html"
,"【琼明神女录】（73）"
)

,("5400288.html"
,"【琼明神女录】（74）"
)

,("5400291.html"
,"【琼明神女录】（75）"
)

,("5400295.html"
,"【琼明神女录】（76）"
)

,("5445747.html"
,"【琼明神女录】（77）"
)

,("5445748.html"
,"【琼明神女录】（78）"
)

,("5445749.html"
,"【琼明神女录】（79）"
)

,("5445750.html"
,"【琼明神女录】（80）"
)

,("5445751.html"
,"【琼明神女录】（81）"
)

,("5445752.html"
,"【琼明神女录】（82）"
)

,("5445753.html"
,"【琼明神女录】（83）"
)
]



from nn_ns.txt.MergeContentOfWebpages import MergeContentOfWebpages__枚举此后文本
class MergeContentOfWebpages_for_dzwx520_com_book_9871(MergeContentOfWebpages__枚举此后文本):
    'wget -k -r -l1 http://www.dzwx520.com/book_9871/'
    def iter_usrdata_htmlpath_pairs(sf):
        '-> Iter (usrdata, html_fname)'
        for href, title in href_title_pairs:
            yield title, idir + href
    def 是否除去文本的空白前后缀(sf):
        '-> bool'
        return True
    def 构造可选的结束文本(sf):
        '-> may_end_str'
        return '温馨提示：按 回车[Enter]键 返回书目'
    def 构造搜索参数(sf):
        '-> (args, kwargs) #for bs4_ops.搜得第一后代()'
        #<div id="htmlContent" class="contentbox">
        return ['div'], dict(属性过滤={'class':'contentbox', 'id':'htmlContent'})

    r'''
    def output(sf, bs4_ops, bs4_obj, idx, usrdata, html_fname):
        'bs4_ops::HtmlAstOps -> bs4_obj::BeautifulSoup -> idx -> usrdata -> html_fname::Path -> IO ()'
    def skip(sf, idx, usrdata, html_fname):
        'idx -> usrdata -> html_fname::Path -> bool'
        return idx
    #'''
    def __init__(sf, idir, may_ofname, *, force, iencoding, oencoding):
        sf.idir = idir
        super().__init__(may_ofname, force=force, iencoding=iencoding, oencoding=oencoding)

if __name__ == "__main__":
    iencoding='gb18030'
    oencoding='gb18030'
    idir = '/storage/emulated/0/0my_files/tmp/wget_/novel/www.dzwx520.com/book_9871/'
    may_ofname = idir + '琼明神女录[dzwx520.com].txt'
    sf = MergeContentOfWebpages_for_dzwx520_com_book_9871(idir, may_ofname, force=True, iencoding=iencoding, oencoding=oencoding)
    sf.main()


