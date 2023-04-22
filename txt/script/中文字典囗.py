#__all__:goto
r'''[[[
e script/中文字典囗.py

主要输出:
    view /sdcard/0my_files/tmp/out4py/script.中文字典囗..格式化囗新华字典囗..新华字典.out.txt


script.中文字典囗
py -m nn_ns.app.debug_cmd   script.中文字典囗 -x
py -m nn_ns.app.doctest_cmd script.中文字典囗:__doc__ -ff -v

py_adhoc_call   script.中文字典囗   @not_show.格式化囗新华字典囗  --ipath:/sdcard/0my_files/unzip/e_book/字词典/中文字典.utf_16_le   --iencoding:utf_16_le   --may_opath=None  --oencoding:u8  =4

py_adhoc_call   script.中文字典囗   @not_show.格式化囗新华字典囗  --ipath:/sdcard/0my_files/unzip/e_book/字词典/中文字典.utf_16_le   --iencoding:utf_16_le   --may_opath:/sdcard/0my_files/tmp/out4py/script.中文字典囗..格式化囗新华字典囗..新华字典.out.txt  --oencoding:u8

view /sdcard/0my_files/tmp/out4py/script.中文字典囗..格式化囗新华字典囗..新华字典.out.txt

from script.中文字典囗 import *


/sdcard/0my_files/unzip/e_book/字词典/中文字典.utf_16_le
[[[
TODO: 中文字典.utf_16_le -> 中文字典.u8
view ++enc=utf16le ../../../unzip/e_book/字词典/中文字典.utf_16_le
!du -h ../../../unzip/e_book/字词典/中文字典.utf_16_le
15M

===


*\S pin,yin,笔划：\d+部首：\S五笔输入法：\w*
基本解释：...
笔画数：\d+；
部首：\S；
详细解释：...


[[
*厂 ān,chǎng,笔划：2部首：厂五笔输入法：dgt
基本解释：厂
（厰）
chǎng
指用机械制造生产资料或生活资料的工场。
有空地方可以存货或进行加工的地方：煤厂。
棚舍：“枳篱茅厂共桑麻。”
中国明代为加强专制统治而设的特务机关。
厂
ān
ㄢˉ
同“庵”，多用于人名。
厂
hàn
ㄏㄢˋ
山边岩石突出覆盖处，人可居住的地方。
笔画数：2；
部首：厂；
详细解释：厂
ān
【名】
同“庵”。多用于人名
另见chǎng
厂
廠、厰
chǎng
【名】
(形声。从广(yǎn),敞声。从“广”,表示与房屋有关。本义:棚舍)
没有墙壁的简易房屋
又如:厂屋(棚舍;无隔墙的房屋)
马屋;牲口棚子
架北墙为厂。——《齐民要术》
工厂
正德十四年,广州置铁厂。——《明史·食货志》
又如:纱厂;钢厂;面粉厂;纺织厂;造纸厂;木器厂
明代的一种特务机构。如:厂臣(明东厂、西厂的主官);厂狱(指明代东厂、西厂囚禁犯人的牢狱)
另见ān
厂房
chǎngfáng
工厂的房屋,指车间
厂规
chǎngguī
工厂的规章制度
厂家
chǎngjiā
∶工厂
∶办工厂的人
厂矿
chǎngkuàng
工厂和矿山
厂商
chǎngshāng
∶工厂和商店(多指私营的)
∶开工厂的人
厂史
chǎngshǐ
工厂的发展史
厂休
chǎngxiū
工厂规定的职工休息日
我厂是每星期四厂休
厂狱
chǎngyù
指明朝东厂(由太监掌管的特务机构)的监狱
及左公下厂狱。——清·方苞《左忠毅公逸事》
厂长
chǎngzhǎng
负责全厂生产、生活和其他一切事务的领导人
厂子
chǎngzi
∶工厂
我们厂子新分来一个大学生
]]
]]]



#]]]'''
__all__ = r'''
格式化囗新华字典囗
    读取囗新华字典囗
        icut_if_startswith_
        iter_blocks5line_contents_
    parse_block_
        parse_block_string_
            FormatError
            regex4block
            column_nms

'''.split()#'''
__all__


from seed.io.savefile__str_tuple import SaveStrTupleAsMultiLine, std_saver4str_tuple
from seed.io.may_open import open4w, open4w_err, open4r
#def open4w(may_opath, /, *, force, xencoding):

from seed.io.iter_line_contents__ver2 import default_may_smay_newline, default_may_newlines
from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__path__human, iter_line_contents__path
#def iter_line_contents__path(ipath, /, *, encoding, newline=default_may_smay_newline, kwargs4open=None, may_newlines=default_may_newlines, without_last_line_if_empty=False):
#from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__file__human, iter_line_contents__file
from seed.iters.isplit_if import iter_split_if_starts_, iter_split_if_ends_, iter_split_with_sep_if_, iter_split_without_sep_if_

from seed.tiny import check_type_is

import re
from itertools import islice

class _G:
    ipath = '/sdcard/0my_files/unzip/e_book/字词典/中文字典.utf_16_le'

def icut_if_startswith_(prefix, strs, /):
    f = lambda s:s.startswith(prefix)
    return iter_split_if_starts_(f, strs)

def __():
  def icut_if_startswith_(prefix, strs, /):
    ls = []
    for s in strs:
        if s.startswith(prefix):
            yield ls
            ls = []
        ls.append(s)
    yield ls

def iter_blocks5line_contents_(header, prefix, line_contents, /):
    line_contentss = icut_if_startswith_(prefix, line_contents)
    for _header in line_contentss:
        assert _header == [*header], (_header, header)
        #discard header
        break
    blocks = line_contentss
    return blocks

def 读取囗新华字典囗(ipath, /, *, encoding, newline=default_may_smay_newline, kwargs4open=None, may_newlines=default_may_newlines, without_last_line_if_empty=False):
    line_contents = iter_line_contents__path(ipath, encoding=encoding, newline=newline, kwargs4open=kwargs4open, may_newlines=may_newlines, without_last_line_if_empty=without_last_line_if_empty)
    blocks = iter_blocks5line_contents_(['\ufeff新华字典'], '*', line_contents)
        #utf_16_le.BOM == '\ufeff'
    return blocks

r'''[[[

*\S pin,yin,笔划：\d+部首：\S五笔输入法：\w*
基本解释：...
笔画数：\d+；
部首：\S；
详细解释：...

#]]]'''


regex4block = re.compile(r'[*](?P<汉字>\S) (?P<拼音序列>.*?),?笔划：(?P<笔画数>\d+)部首：(?P<部首序列>难检字|\S(,\S)*|)五笔输入法：(?P<五笔编码序列>[,\w]*?),*[|]*\n基本解释：(?P<基本解释>.*?)\n(笔画数：(?P<笔画数二>\d+)；\n)?(部首：(?P<部首序列二>难检字|\S(,\S)*)；\n)?详细解释：(?P<详细解释>.*)', re.DOTALL)
    #拼音序列 允空:『么』
    #赓.部首序列:贝,广
    #羸.部首:亠  .部首二:羊
    #部首序列 允空:『裛』
    #蔻.五笔编码序列:apfl,apfc

column_nms = r'''
汉字
拼音序列
笔画数
部首序列
五笔编码序列
基本解释
详细解释
'''.split()#'''
column_nms = (*column_nms,)
assert len(column_nms) == 7


class FormatError(Exception):pass

def parse_block_(block, /):
    assert block
    line_contents = block
    #head = line_contents[0]
    s = '\n'.join(line_contents)
    return parse_block_string_(lambda:line_contents, s)
def parse_block_string_(lazy_err_msg, s, /):
    m = regex4block.fullmatch(s)
    if m is None:raise FormatError(lazy_err_msg())
    d = {nm:m[nm] for nm in column_nms}
    if not (m['部首序列二'] is None or m['部首序列二'] == m['部首序列']):
        bks = {*m['部首序列'].split(','), *m['部首序列二'].split(',')}
        bks.discard('')
        d['部首序列'] = ','.join(sorted(bks))
            # 羸.部首:亠  .部首二:羊
            #部首序列 允空:『裛』
    try:
        #assert m['部首序列二'] is None or m['部首序列二'] == m['部首序列']
        assert m['笔画数二'] is None or m['笔画数二'] == m['笔画数']
    except AssertionError as e:
        if 0:
          if d['汉字'] == '题':
            d['笔画数'] = m['笔画数二']
            assert m['笔画数二'] == '15' != '12' == m['笔画数']
        elif 1:
            print(d['汉字'], m['笔画数'], m['笔画数二'])
            d['笔画数'] = m['笔画数二']
            r'''[[[
            题 12 15
            颂 12 10
            袅 9 10
            #]]]'''
        else:
            raise Exception(lazy_err_msg()) from e
    t = tuple(d[nm] for nm in column_nms)
    if 0b0:
        if d['汉字'] == '羸':
            print(t)
        if d['汉字'] == '题':
            print(t)
    else:
        pass
    #for s in t: check_type_is(str, s)
    return t
_strings4test = (
'''\
*乃 nǎi,笔划：2部首：丿五笔输入法：etn||
基本解释：
乃
nǎi
◎才：今～得之。“断其喉，尽其肉，～去”。
◎是，为：～大丈夫也。
◎竟：～至如此。
◎于是，就：“因山势高峻，～在山腰休息片时”。
◎你，你的：～父。～兄。“家祭无忘告～翁”。
详细解释：乃
廼、迺
nǎi
【代】
你,你的
余嘉乃勋。——《左传·僖公十二年》
几败乃公事。——《汉书·高帝纪上》
谁谓乃公勇者?——《史记·淮南衡山传》
王师北定中原日,家祭无忘告乃翁(父亲)。——陆游《示儿》
又如:乃父(乃翁。你的父亲);乃祖(你的祖父;先祖);乃公(你的父亲);乃兄
他的
乃心在咸阳。——曹操《蒿里行》
又如:乃眷(他的妻子);乃尊(尊称别人的父亲);乃老(他的父亲);乃堂(他的母亲)
此,这个
吾闻之,五子不满隅,一子可满朝,非乃子耶?——《晏子春秋》
又如:乃今(如今;从今);乃者(往日;从前)
这样,如此
子无乃称。——《庄子·德充符》
又如:因山势高峻,乃在山腰休息片刻;乃尔(如此;这样);乃若(至于)
乃
nǎi
【动】
是,就是
以其乃华山之阳名之。——宋·王安石《游褒禅山记》
吾乃与而君言,汝何为者也?——《史记·平原君虞卿列传》
又如:真乃英雄好汉;失败乃成功之母;乃是(却是)
乃
nǎi
【副】
刚刚,才,表示事情发生得晚或结束得晚
九月…丁巳,葬我君定公,雨,不克葬,戊午日下昃乃克葬。——《春秋经·定公十五年》
乃悟前狼假寐,盖以诱敌。——《聊斋志异·狼三则》
只,仅仅。如:唯虚心乃能进步
竟,竟然
今其智乃反不能及,其何怪也!——唐·韩愈《师说》
却
乃日视便利田宅可买者。(却每天寻找可买的合适的土地房屋。)——汉·刘向《列女传》
于是;就
屠乃奔倚其下。——《聊斋志异·狼三则》
乃令张仪佯去秦,厚币委质事楚。——《史记·屈原贾生列传》
婉贞挥刀奋斫…敌乃纷退。——清·徐珂《清稗类钞·战事类》
又如:乃遂(就,于是);乃其(于是,就)
乃
nǎi
【连】
可是,然而
时夫仆具阻险行后,余亦停弗上。乃一路奇景,不觉引余独往。——《徐霞客游记》
乃是
nǎishì
是,就是
人民群众乃是真正的英雄
乃至
nǎizhì
甚至
全城军民乃至老弱妇孺都参加了抢险护堤
也说“乃至于”
'''#'''
, '''\
*么 笔划：3部首：丿五笔输入法：tcu
基本解释：么
（麽）
me
词尾：怎么。这么。多么。什么。
助词，表示含蓄语气，用在前半句末了：不让你去么，你又要去。
么
yāo
同“幺”。
么
mɑ
同“吗3”。
笔画数：3；
部首：丿；
详细解释：么
麽
me
【后缀】
用作某些词的后缀。如:什么;怎么;多么
么
麽
me
【助】
用作歌词中的衬字。如:五月的花儿,红呀么红似火
另见yāo;mó;ma
'''#'''
, '''\
*蔻 kòu,笔划：14部首：艹五笔输入法：apfl,apfc
基本解释：蔻
kòu
〔豆蔻〕见“
〔蔻蔻〕即“可可”。
〔蔻丹〕染指甲的油。
豆”。
笔画数：14；
部首：艹；
详细解释：蔻
kòu
【名】
(形声。本义:豆蔻:植物名。比喻处女。因称女子十三四岁为“豆蔻年华。”)小豆蔻。东印度一种草本植物的芳香蒴果,用作调味品和用作芳香剂和健胃剂
'''#'''
, '''\
*赓 gēng,笔划：12部首：贝,广五笔输入法：yvwm
基本解释：賡
gēng
【动】
(形声。从贝,庚声。本义:连续,继续)
同本义
乃赓载歌曰:“元首明哉,股肱良哉,庶事康哉。——《书·益稷》
又如:赓扬(继续);赓载(相续而成);赓咏(相继咏和);赓衍(延续演变);赓飏(飞扬轻举连续而歌)
酬答、应和
赖有西邻好诗句,赓酬终日自忘饥。——宋·张耒《张右史集·屋东》
又如:赓和(唱和;酬谢、赠答之意);赓歌(作歌唱和;连续不断的歌声,表示欢乐);赓酬(作诗相唱和、赠答)
通“庚”。赔偿
智者有什倍人之功,愚者有不赓本之事。——《管子·国蓄》
又如:赓本(抵偿成本)
详细解释：赓
賡
gēng
【动】
(形声。从贝,庚声。本义:连续,继续)
同本义
乃赓载歌曰:“元首明哉,股肱良哉,庶事康哉。——《书·益稷》
又如:赓扬(继续);赓载(相续而成);赓咏(相继咏和);赓衍(延续演变);赓飏(飞扬轻举连续而歌)
酬答、应和
赖有西邻好诗句,赓酬终日自忘饥。——宋·张耒《张右史集·屋东》
又如:赓和(唱和;酬谢、赠答之意);赓歌(作歌唱和;连续不断的歌声,表示欢乐);赓酬(作诗相唱和、赠答)
通“庚”。赔偿
智者有什倍人之功,愚者有不赓本之事。——《管子·国蓄》
又如:赓本(抵偿成本)

'''#'''
, '''\
*羸 léi,笔划：19部首：亠五笔输入法：ynky
基本解释：羸
léi
瘦弱：羸瘦。羸困（瘦弱困顿）。羸顿。羸弱。羸惫。
笔画数：19；
部首：羊；
详细解释：羸
léi
【形】
(形声。从羊,本义:瘦弱)
同本义
羸,瘦也。——《说文》。按,本训当为瘦羊,转而言人耳。
羸老易子。——汉·贾谊《论积贮疏》
皆羸老之卒。——《资治通鉴·唐纪》
悉使羸兵负草。——《资治通鉴》
又
羸兵为人马所蹈藉。
又如:羸骖(瘦弱的马);羸蹇(驽弱瘦瘠的驴);羸驷(瘦弱的马);羸骀(瘦弱驽钝的马。喻才能低下);羸饿(瘦瘠饥饿。亦指瘦瘠饥饿的人)
疲困
身病体羸。——《礼记·问丧》。释文:“疲也。”
又如:羸北(困败);羸色(疲惫的神色);羸师(谓藏其精锐而出示疲弱的军队以麻痹敌人)
衰弱
请羸师以张之。——《左传·桓公元年》
此羸者阳也。——《国语·周语》。注:“弱也。”
又如:羸老(衰弱的老人);羸病(衰弱生病);羸疾(衰弱生病)
贫弱。如:羸民(贫弱之民)
低劣
小子无谓我老而羸我。——《淮南子·缪称》。注:“劣人也。”
又如:羸钝(低劣迟钝)
羸
léi
【动】
通“累”。缠绕,困住
羝羊触藩,羸其角。——《易·大壮》
有攸往见凶,羸豕孚蹢躅。——《易·姤》
羸惫
léibèi
瘦弱疲惫
羸顿
léidùn
瘦弱困顿
羸劣
léiliè
瘦弱
羸弱
léiruò
瘦弱
羸瘦
léishòu
瘦弱
面容赢瘦
'''#'''
, '''\
*题 tí,笔划：12部首：页五笔输入法：jghm
基本解释：题
（題）
tí
写作或讲演内容的总名目：题目。主题。话题。题材。题旨。
练习或考试时要求解答的问题：试题。问答题。
写上，签署：题名。题字。题壁。题诗。题辞。题跋。
姓。
笔画数：15；
部首：页；
详细解释：题
題
tí
【名】
(形声。从页(xié),是声。页,头。本义:额头)
同本义
题,额也。——《说文》
雕题交趾。——《礼记·王制》
赤眉圆题。——《汉书·司马相如传》
夫加之以衡扼,齐之以月题。——《庄子·马蹄》。释文引司马崔云:“月题,马额上当颅如月形者也。”
文题白身,名曰孟极。——《山海经·北山经》
雕题黑齿。——《楚辞·招魂》
连缓耳,琐雕题。——《后汉书·杜笃传》
《雕题交阯》——《后汉书·南蛮西南夷传》
又如:题注(以头额撞击);黑牛白题(黑牛白额)
物品的前端或顶端堂高数仞,榱题数尺。——《孟子》
又如:榱题(屋檐的椽头。榱,椽子)
题目;标题
臣尝私习此赋,请试他题。——脱脱等《宋史》
又如:试题(考试时让应考者作答的问题);题头(标题,篇目);题意(题目的旨意);题号(标题名称);题位(题目的要求,作文的规则)
书签;标签
委之在深箧,蠹鱼坏其题。——唐·李白《感兴八首》
标志
欲垦荒田,先立表题。——《晋书》
奏章。明、清两代公文用语之一。又指上奏。
如:题参(参奏;奏本弹劾);题本(上奏章);题估(清代公文用语);题奏(题本用奏本);题留(清代公文用语);题补(清代公文用语);题销(上奏报销);题请(上奏呈请)
题
題
tí
【动】
书写;题署
题名其上。——明·魏学洢《核舟记》
又如:题赞(在书画上题写几句有关的话或留作纪念的话);题款(署名或题字在书画上);题诗(作诗。题在书画,器物或墙壁之上);题叶(在叶上题诗);题署(签署,书写文书封筒;题壁(在壁上题诗写字))
谈及
且把闲话休题。——《水浒传》
又如:休题旧事;题说(说起)
品评;评论
一经品题,便作佳士。——李白《与韩荆州书》
又如:题拂(评论,标榜);题品(品评。也作题评);题评(品评。同题品)
鸣;叫
遍青山,题经子杜鹃。——明·汤显祖《牡丹亭》
题跋
tíbá
写在书籍,碑帖,字画等前面的文字叫做题,写在后面的,叫做跋,总称题跋
题壁
tíbì
∶在墙壁上题诗、写字
∶写在墙上的文字或诗句
题材
tícái
作品内容主题所用的材料
农村题材
题词,题辞
tící,tící
∶为勉励或留作纪念而写下的一段话
∶所题的词。冠于一部著作之前,以一种较正式或不甚正式的样式或方式,题写给予某人的姓名及祝贺词
∶序文
题解
tíjiě
∶书本中用来注解题目或简介作品的时代特征的文字
∶关于中学数、理、化练习题的详细解答,也指汇集成册的
题名
tímíng
∶题目名称,写作、印刷品、讲述或影印作品名称
∶写上姓名作为标记
对联、题名。——明·魏学洢《核舟记》
请题名留念
题目
tímù
∶诗歌或文章的主题、意旨;书籍的标目
让我们别再谈这个题目了吧
∶提出来要求解答的问题
练习题目
∶借口;名义
∶评论;品题
题签
tíqiān
∶书面上的标签
∶写在书皮上的标签
∶签名题字
题外
tíwài
在划定或公认的范围以外的
不大可能对已由该构成假说组织好了的事实加以证实的题外证据
题旨
tízhǐ
∶文章题目的意义、主旨
∶文艺作品主题的意义
题旨深远
题注
tízhù
附加在新闻、文章、电视节目等条目上的关于其来源或作者的说明
题字
tízì
∶为留纪念而写上的字
书上有作者亲笔题字
∶留作纪念而写字
'''#'''
, '''\
*裛 yì,笔划：13部首：五笔输入法：
基本解释：裛
yì
书套。
缠绕：“裛以藻绣，络以纶连。”
用香熏：“麝裛战袍香。”
古同“浥”，沾湿。
笔画数：13；
部首：衣；
详细解释：裛
yì
【动】
缠裹。如:裛衣(裹衣,以衣裹身)
香气熏染侵袭。如:裛裛(香气袭人的样子)
通“浥”。沾湿。如:裛妆(泪妆);裛艓(云气缭绕貌);裛烂(潮湿霉烂)
'''#'''

)

def __():
    for _string4test in _strings4test:
        parse_block_string_(lambda:_string4test.partition('\n')[0], _string4test)
__()

def 格式化囗新华字典囗(*args4islice, ipath, iencoding, may_opath, oencoding, force=False, turnoff_may_smay_newline=True, newline=default_may_smay_newline, kwargs4open=None, may_newlines=default_may_newlines, without_last_line_if_empty=False):
    if not iencoding: raise TypeError
    if not oencoding: raise TypeError

    blocks = 读取囗新华字典囗(ipath, encoding=iencoding, newline=newline, kwargs4open=kwargs4open, may_newlines=may_newlines, without_last_line_if_empty=without_last_line_if_empty)

    if args4islice:
        blocks = islice(blocks, *args4islice)

    it = map(parse_block_, blocks)
    #kw = dict(flush=True, turnoff_may_smay_newline=turnoff_may_smay_newline)
    kw = dict(flush=False, turnoff_may_smay_newline=turnoff_may_smay_newline)
    with open4w(may_opath, force=force, xencoding=oencoding) as ofile:
        std_saver4str_tuple.save_header_to_ofile_(ofile, **kw)
        std_saver4str_tuple.save_empty_line_to_ofile_(ofile, **kw)

        std_saver4str_tuple.save_comment_to_ofile_(ofile, repr('新华字典'), **kw)
        std_saver4str_tuple.save_comment_to_ofile_(ofile, repr(column_nms), **kw)
        std_saver4str_tuple.save_empty_line_to_ofile_(ofile, **kw)
        for t in it:
            std_saver4str_tuple.save_str_tuple_to_ofile_(ofile, t, **kw)
            std_saver4str_tuple.save_empty_line_to_ofile_(ofile, **kw)





from script.中文字典囗 import *
