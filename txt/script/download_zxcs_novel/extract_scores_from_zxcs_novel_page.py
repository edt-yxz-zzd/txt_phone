r'''
e script/download_zxcs_novel/extract_scores_from_zxcs_novel_page.py



[[4test
py script/download_zxcs_novel/extract_scores_from_zxcs_novel_page.py -i /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.4test.txt -o /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.scores.4test.txt
view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.4test.txt
view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.scores.4test.txt
]]


#37 39 42
[[sort-37
py /sdcard/0my_files/git_repos/txt_phone/txt/script/download_zxcs_novel/collect_links_from_zxcs_sort_pages.py -sort 37 -od /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/ --turnoff__download --remove_www_in_URL
view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.txt

py script/download_zxcs_novel/extract_scores_from_zxcs_novel_page.py -i /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.txt -o /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.scores.txt
view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/37.html.iinfos.scores.txt
]]
[[sort-39
py /sdcard/0my_files/git_repos/txt_phone/txt/script/download_zxcs_novel/collect_links_from_zxcs_sort_pages.py -sort 39 -od /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/ --turnoff__download --remove_www_in_URL
view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/39.html.iinfos.txt

py script/download_zxcs_novel/extract_scores_from_zxcs_novel_page.py -i /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/39.html.iinfos.txt -o /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/39.html.iinfos.scores.txt
view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/39.html.iinfos.scores.txt
]]
[[sort-42
py /sdcard/0my_files/git_repos/txt_phone/txt/script/download_zxcs_novel/collect_links_from_zxcs_sort_pages.py -sort 42 -od /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/ --turnoff__download --remove_www_in_URL
view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.html.iinfos.txt

py script/download_zxcs_novel/extract_scores_from_zxcs_novel_page.py -i /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.html.iinfos.txt -o /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.html.iinfos.scores.txt
view /sdcard/0my_files/tmp/out4py/download_zxcs_novel/collect_links_from_zxcs_sort_pages/sorts/42.html.iinfos.scores.txt
]]


[[[
[[
view-source:http://zxcs.me/post/9999
<div........>
... ...
... ...
<div class="filecont">
  <p class="filetit"><a href="http://zxcs.me/download.php?id=9999" rel="external nofollow" target="_blank" title="">《唐朝小官人》（校对版全本）作者：上山打老虎额</a></p>
  <p class="fileinfo"><span>格式：TXT</span>|&nbsp;&nbsp;&nbsp;<span>大小：3.54 MB</span></p>
</div>

<div class="down_2">
  <a href="http://zxcs.me/download.php?id=9999" rel="external nofollow" target="_blank" title="点击下载"></a>
</div>
... ...
... ...
</div>

<div id="vote">
<script language="javascript">
    var pluginpath = "http://zxcs.me/content/plugins/cgz_xinqing/";
    var infoid = "9999";
</script>
<script language = "javascript" src ="http://zxcs.me/content/plugins/cgz_xinqing/cgz_xinqing.js">
</script>
</div>
]]
==>>下载『cgz_xinqing.js』
[[
!mkdir /sdcard/0my_files/tmp/wget_/zxcs.me/
cd /sdcard/0my_files/tmp/wget_/zxcs.me/
wget http://zxcs.me/content/plugins/cgz_xinqing/cgz_xinqing.js
]]
[[
view /sdcard/0my_files/tmp/wget_/zxcs.me/cgz_xinqing.js

document.writeln("<div><a onclick=\"get_mood(\'mood1\')\" ><img src=\""+pluginpath+"images\/1.png\" \><\/a><\/div>");
document.writeln("<div style=\"font-size:16px;height:26px;light-height:26px;\">仙草<\/div>");

function get_mood(mood_id)
{
  ... ...
  url = ""+pluginpath+"cgz_xinqing_action.php?action=mood&id="+infoid+"&typee="+mood_id+"&m=" + Math.random();
  makeRequest(url,'return_review1','GET','');
  ... ...
}
function return_review1(ajax)
{
  if (http_request.status == 200) {
    var str_error_num = http_request.responseText;
    ... ...
      moodinner(str_error_num);
    ... ...
  }
}

# moodinner() ==>> moodarr/moodtext 是 评分
#   mood 心情/情绪
function moodinner(moodtext)
{
  ... ...
  var moodarr = moodtext.split(",");
  var moodzs = 0;
  for(k=0;k<8;k++) {
    moodarr[k] = parseInt(moodarr[k]);
    moodzs += moodarr[k];
  }
  for(i=0;i<8;i++) {
    heightarr[i]= Math.round(moodarr[i]/moodzs*heightz);
    if(heightarr[i]<1) heightarr[i]=1;
    if(moodarr[i]>hmaxpx) {
    hmaxpx = moodarr[i];
    }
  }
  for(j=0;j<8;j++)
  {
    if(moodarr[j]==hmaxpx && moodarr[j]!=0) {
      vote("moodinfo"+j).innerHTML = "<span style='color: "+color2+";'>"+moodarr[j]+"</span>";
    } else {
      vote("moodinfo"+j).innerHTML = "<span style='color: "+color1+";'>"+moodarr[j]+"</span>";
    }
  }
}

function makeRequest(url, functionName, httpType, sendData) {
  http_request = false;
  if (!httpType) httpType = "GET";

  ... ...
  var changefunc="http_request.onreadystatechange = "+functionName;
  eval (changefunc);
  http_request.open(httpType, url, true);
  http_request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  http_request.send(sendData);
}
]]

[[摘要:
======================
view-source:http://zxcs.me/post/9999
var pluginpath = "http://zxcs.me/content/plugins/cgz_xinqing/";
var infoid = "9999";
======================
view /sdcard/0my_files/tmp/wget_/zxcs.me/cgz_xinqing.js
onclick=\"get_mood(\'mood1\')\"
var moodarr = moodtext.split(",");
url = ""+pluginpath+"cgz_xinqing_action.php?action=mood&id="+infoid+"&typee="+mood_id+"&m=" + Math.random();
makeRequest(url,'return_review1','GET','');

]]
[[py模拟:
import random as Rm
pluginpath = "http://zxcs.me/content/plugins/cgz_xinqing/"
infoid = "9999"
  #info_ID
  #来自于网址:小说页面:http://zxcs.me/post/9999
  #
mood_id = "mood1"
  #mood[1-5]
  #按理来说，mood1 只代表 仙草
  #但，结果是 全部！
  #
url = ""+pluginpath+"cgz_xinqing_action.php?action=mood&id="+infoid+"&typee="+mood_id+"&m=" + str(Rm.random());
  #JavaScript Math.random()->float
  #与py::random.random()一样！
  #
'http://zxcs.me/content/plugins/cgz_xinqing/cgz_xinqing_action.php?action=mood&id=9999&typee=mood1&m=0.7204524125627698'

import requests as R
r = R.get(url)
r.status_code
200
r.content
b'93,8,5,7,30'
  #92人:仙草; 8人:粮草; 5人:干草; 7人:枯草; 30人:毒草;
]]
]]]
#'''

r'''[[[deprecated extract_scores_from_zxcs_novel_page by fetch_scores_from_internet:

e script/download_zxcs_novel/extract_scores_from_zxcs_novel_page.py

用的是 js，无法提取

view script/download_zxcs_novel/zxcs_pages/zxcs-37-12842.html
<!-- view-source:http://www.zxcs.me/post/12842 -->
    ##################
    <div class="posttitle">《修仙从沙漠开始》（校对版全本）作者：中天紫薇大帝</div>
    <a href="http://www.zxcs.me/download.php?id=12842" rel="external nofollow" target="_blank" title="点击下载"></a>
    <div id="vote">



	<div class="posttitle">《修仙从沙漠开始》（校对版全本）作者：中天紫薇大帝</div>


	<div class="postcont"><img src="http://tu.zxcs.me/content/uploadfile/27/1rrc5u54zajidip.jpg" alt="《修仙从沙漠开始》（校对版全本）作者：中天紫薇大帝" border="0" width="180" height="240"/>
<br/><p><br/></p>
<p>【TXT大小】：6.85 MB
<br/>【内容简介】：<br/>　　一个普普通通的办公室小职员，意外重生到了一个神秘浩瀚的仙侠世界中，成为了一个小修仙家族的一员。
<br/>　　故事，从无边沙海中一个名为玉泉湖绿洲的绿洲开始。
<br/><br/></p><p class="yinyong"><span style="font-size:14px;color:#E56600;">优质订阅书源，收集于网络！</span></p>
<p class="yinyong"><span style="font-size:14px;color:#E56600;">文本由河洛校对！</span></p><br/><link href="http://www.zxcs.me/content/plugins/cpdown/images/logid.css" type=text/css rel=stylesheet><div class="pagefujian"><div class="fileico "></div><div class="filecont"><p class="filetit"><a href="http://www.zxcs.me/download.php?id=12842" rel="external nofollow" target="_blank" title="">《修仙从沙漠开始》（校对版全本）作者：中天紫薇大帝</a></p>
  <p class="fileinfo"><span>格式：TXT</span>|&nbsp;&nbsp;&nbsp;<span>大小：6.85 MB</span></p>
</div>
	<div class="down_2">
		<a href="http://www.zxcs.me/download.php?id=12842" rel="external nofollow" target="_blank" title="点击下载"></a> 
	</div>
</div><div id="vote">
<script language="javascript">
    var pluginpath = "http://www.zxcs.me/content/plugins/cgz_xinqing/";
    var infoid = "12842"; 
</script>
<script language = "javascript" src ="http://www.zxcs.me/content/plugins/cgz_xinqing/cgz_xinqing.js"></script>
</div></div><div class="clear"></div>
#]]]'''



__all__ = '''
    fetch_scores_from_internet
    batch_fetch_scoress_from_internet
    '''.split()



import random
import requests
import datetime
import time
from seed.tiny import print_err



def extract_scores_from_zxcs_novel_page():
    'ID -> (日期, [此刻评分]{len=5})'
    raise NotImplementedError('use instead: fetch_scores_from_internet()')

class Glabols:
    pluginpath = "http://zxcs.me/content/plugins/cgz_xinqing/"
    #url = ""+pluginpath+"cgz_xinqing_action.php?action=mood&id="+infoid+"&typee="+mood_id+"&m=" + str(random.random());
    fmt4url = '{pluginpath!s}cgz_xinqing_action.php?action=mood&id={infoid!s}&typee={mood_id!s}&m={random_!s}'

def fetch_scores_from_internet(novel_page_idx, /):
    r'''
    ID -> [此刻评分]{len=5}
    #xxx ID -> (今天日期, [此刻评分]{len=5})

    小说页面-网址格式:http://www.zxcs.me/post/{novel_page_idx}

    别名:info_ID=infoid=novel_page_idx
    #'''
    assert novel_page_idx >= 0

    infoid = "9999"
      #info_ID
      #来自于网址:小说页面:http://zxcs.me/post/9999
      #
    infoid = novel_page_idx
    mood_id = "mood1"
      #mood[1-5]
      #按理来说，mood1 只代表 仙草
      #但，结果是 全部！
      #
    url = Glabols.fmt4url.format(pluginpath=Glabols.pluginpath, infoid=infoid, mood_id=mood_id, random_=random.random())
      #JavaScript Math.random()->float
      #与py::random.random()一样！
      #
    'http://zxcs.me/content/plugins/cgz_xinqing/cgz_xinqing_action.php?action=mood&id=9999&typee=mood1&m=0.7204524125627698'

    r = requests.get(url)
    if not r.status_code == 200: raise RuntimeError(f'{r.status_code}: {r!r}')
    bs = r.content
    b'93,8,5,7,30'
      #92人:仙草; 8人:粮草; 5人:干草; 7人:枯草; 30人:毒草;
    s = bs.decode('ascii')
    scores = (*map(int, s.split(',')),)
    assert len(scores) == 5
    assert all(u >= 0 for u in scores)
    return scores

def get_today__str():
    today__str = datetime.date.today().strftime("%Y%m%d")
    return today__str

def batch_fetch_scoress_from_internet(novel_page_idc, /, seconds4sleep, interactive):
    'Iter ID -> (今天日期, {ID:[此刻评分]{len=5}})'

    today__str = get_today__str()
    assert len(today__str) == 8

    novel_page_idx2scores = {}
    for novel_page_idx in novel_page_idc:
        if not novel_page_idx in novel_page_idx2scores:
            while 1:
                try:
                    scores = fetch_scores_from_internet(novel_page_idx)
                    break
                except Exception as e:
                    print_err(e)
                    print_err(type(e))
                    print_err('num_success =', len(novel_page_idx2scores))
                    print_err('fail ID =', novel_page_idx)
                    if not interactive:
                        raise
                    while 1:
                        ans = input('continue? (Y/N)')
                        ans = ans.upper()
                        if ans in ('Y', 'N'):
                            break
                    #end-while
                    if ans == 'N':
                        raise
                    elif ans == 'Y':
                        continue
                    else:
                        raise logic-err
                #end-try-except
            #end-while

            novel_page_idx2scores[novel_page_idx] = scores
            #time.sleep(0.2)#seconds
            time.sleep(seconds4sleep)
    today__str
    novel_page_idx2scores
    return (today__str, novel_page_idx2scores)


if __name__ == "__main__":
    if 0b00:
        print(get_today__str())
        print(fetch_scores_from_internet('9999'))

#def link_iinfos2iter_IDs(link_iinfos, /):
def link_iinfos_to_ID2cidx(link_iinfos, /):
    novel_page_idx2collectlist_idx = {}
    for (collectlist_idx, novel_page_idx, target_label, description) in link_iinfos:
        ID = infoid = info_ID = novel_page_idx
        novel_page_idx2collectlist_idx[novel_page_idx] = cidx = collectlist_idx
    return novel_page_idx2collectlist_idx

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    from ast import literal_eval
    #from seed.tiny_.pprint4container__depth1 import pprintT4tuple__depth1, pprint4container__depth1
    from seed.tiny_.pprint4container__depth1 import pprintT4dict_items__depth1

    parser = argparse.ArgumentParser(
        description='fetch_scores_from_internet @zxcs.me'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('--turnoff__interactive', action='store_true'
                        , default = False
                        , help='interactive mode will ask user whether to retry when fetch fail')
    parser.add_argument('--seconds4sleep', type=float, default=float("0.2")
                        , help='how long to wait to start next fetch; [default=0.2]')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path of xx.html.iinfos.txt #see: collect_links_from_zxcs_sort_pages.py::--turnoff__download/--turnoff__extract/ofname4html__to__ofname4iinfos()')
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
    seconds4sleep = args.seconds4sleep
    time.sleep(seconds4sleep)

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        txt = fin.read()
    link_iinfos = literal_eval(txt)
    #iter_IDs = link_iinfos2iter_IDs(link_iinfos)
    novel_page_idx2collectlist_idx = link_iinfos_to_ID2cidx(link_iinfos)
    iter_IDs = iter(novel_page_idx2collectlist_idx)

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        #pprint4dict_items__depth1 = pprintT4dict_items__depth1(indent='', fout=fout, two_lines_per_item=False, sort_by_=('keyfunc', echo))
        pprint4dict_items__depth1 = pprintT4dict_items__depth1(indent='', fout=fout, two_lines_per_item=False, sort_by_=('sortfunc4elements', iter))#no_sort
        (today__str, novel_page_idx2scores) = batch_fetch_scoress_from_internet(iter_IDs, seconds4sleep=seconds4sleep, interactive=not args.turnoff__interactive)
        items = sorted(novel_page_idx2scores.items(), key=lambda kv: novel_page_idx2collectlist_idx[kv[0]])

        print(f'({today__str!r},', file=fout)
        pprint4dict_items__depth1(items)
        print(f')', file=fout)
    if not len(novel_page_idx2scores) == len(link_iinfos): raise logic-err #ValueError
if __name__ == "__main__":
    main()


