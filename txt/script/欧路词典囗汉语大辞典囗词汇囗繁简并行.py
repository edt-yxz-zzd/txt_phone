#__all__:goto
r'''[[[
e script/欧路词典囗汉语大辞典囗词汇囗繁简并行.py


script.欧路词典囗汉语大辞典囗词汇囗繁简并行
py -m nn_ns.app.debug_cmd   script.欧路词典囗汉语大辞典囗词汇囗繁简并行 -x
py -m nn_ns.app.doctest_cmd script.欧路词典囗汉语大辞典囗词汇囗繁简并行:__doc__ -v
py -m nn_ns.app.doctest_cmd script.欧路词典囗汉语大辞典囗词汇囗繁简并行!
from script.欧路词典囗汉语大辞典囗词汇囗繁简并行 import *

py_adhoc_call   script.欧路词典囗汉语大辞典囗词汇囗繁简并行   @提取词义中的繁简对照项囗   --ipath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt   --opath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照.txt

py_adhoc_call   script.欧路词典囗汉语大辞典囗词汇囗繁简并行   @提取词义中的繁简对照项囗   --ipath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt   --opath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt +to_export_smay_wordS


view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照.txt
    205422行，
    205422/348430=0.5895646184312487
    不足59%
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt
    348430行
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt
    696860行/2
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照.txt
3.2M
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt
4.3M


#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from seed.tiny import mk_fprint, check_type_is
from seed.io.may_open import open4w, open4w_err, open4r
#def open4w(may_opath, /, *, force, xencoding):
#def open4r(may_opath, /, *, xencoding):
from itertools import chain
import re
_cs = '（(，,)）'
_fcs = '[^（(，,)）]'
pattern4TS = fr'[（(](?P<T>{_fcs}+)[，,](?P<S>{_fcs}+)[)）]'
regex4TS = re.compile(pattern4TS)

_data4test = r'''
,物價
:<B>物價</B><DIV><DIV>(物價,物价)<BR>貨物的價格。<BR>&nbsp;《南齊書‧王敬則傳》：“永初中，官布一匹直錢一千，而民間所輸聽為九百，漸及元嘉，物價轉賤。”<BR>&nbsp;唐柳宗元《非國語上‧大錢》：“幣輕則物價騰踊。”<BR>&nbsp;元劉致《端正好‧上高監司》套曲：“一日日物價高漲，十分料鈔加三倒，一斗粗糧折四量。”<BR>&nbsp;清昭槤《嘯亭雜錄‧關稅》：“乃使物價昂貴，於民生大有虧損。”<BR>&nbsp;周而復《上海的早晨》第一部六：“發了工資，不要說遲一天買東西了，就是遲一小時半小時物價也要上漲。”</DIV></DIV>
,物件
:<B>物件</B><DIV><DIV>1.東西，物品。<BR>&nbsp;金董解元《西廂記諸宮調》卷七：“寄來的物件，斑管、瑤琴、簪是玉，竅包兒裏一套衣服，怎不教人痛苦？”<BR>&nbsp;《紅樓夢》第一○五回：“一進屋門，只見箱開櫃破，物件搶得半空。此時急得兩眼直豎，淌淚發呆。”<BR>&nbsp;楊朔《滇池邊上的報春花》：“曇花本來是稀罕物件，這兒的曇花都長成大樹。”<BR>2.貶稱人。<BR>&nbsp;魯迅《書信集‧致曹聚仁》：“古人告訴我們唐如何盛，明如何佳，其實唐室大有胡氣，明則無賴兒郎，此種物件，都須褫其華袞，示人真相。”</DIV></DIV>
,物盡其用
:<B>物盡其用</B><DIV><DIV>(物盡其用,物尽其用)<BR>充分發揮各種東西的功用。<BR>&nbsp;耿可貴《孫中山與宋慶齡》：“為了使我們苦難的祖國掙脫專制枷鎖，做到人盡其才，物盡其用，地盡其利，貨盡其通，為了實現天下為公的願望，總要有一些人付出生命的代價。”<BR>&nbsp;馬烽《典型事例》三：“這倒是人盡其才，物盡其用，兩全其美。”</DIV></DIV>
,物景
:<B>物景</B><DIV><DIV>景物。<BR>&nbsp;五代王周《過武寧縣》詩：“行過武寧縣，初晴物景和。”<BR>&nbsp;宋梅堯臣《答水丘》詩：“時雨乍晴，物景鮮麗。”<BR>&nbsp;宋樓鑰《王成之給事囿山堂》詩：“主人意軒豁，物景供曠快。”</DIV></DIV>
'''.split()#'''
assert len(_data4test)==8

def 提取词义中的繁简对照项囗(*, ipath, opath=None, force=False, to_export_smay_wordS=False):
    check_type_is(bool, to_export_smay_wordS)
    check_type_is(bool, force)
    with open4r(ipath, xencoding='u8') as ifile, open4w(opath, force=force, xencoding='u8') as ofile:
        fprint = mk_fprint(ofile)
        it = 迭代提取词义中的繁简对照项囗多行词条词义囗(iter(ifile))
        for (wordT, smay_wordS) in it:
            if to_export_smay_wordS or smay_wordS:
                fprint(f'{wordT}:{smay_wordS}')
            else:
                pass

def 迭代提取词义中的繁简对照项囗词典路径囗(ipath, /):
    '-> Iter (wordT, smay_wordS)'
    with open(ipath, 'rt', encoding='u8') as ifile:
        yield from 迭代提取词义中的繁简对照项囗多行词条词义囗(iter(ifile))

def 迭代提取词义中的繁简对照项囗多行词条词义囗(xlines, /):
    '-> Iter (wordT, smay_wordS)'
    #return chain.from_iterable(map(迭代提取词义中的繁简对照项囗单行词义囗, iter_lines))
    it = iter(xlines)
    f = 迭代提取词义中的繁简对照项囗单行词义囗
    for i, word_or_body in enumerate(it):
        word_or_body = word_or_body.strip()
        if i&1:
            body = word_or_body
            word
            assert body.startswith(':')
            body = body[1:]
            yield from f(word, body)
            del word
        else:
            word = word_or_body
            assert word.startswith(',')
            word = word[1:]
def 迭代提取词义中的繁简对照项囗单行词义囗(wordT, body, /):
    '-> Iter (wordT, smay_wordS)'
    wordT = wordT.strip()
    for m in regex4TS.finditer(body):
        if m is None:continue
        t, s = map(str.strip, (m['T'], m['S']))
        if wordT == t:
            yield t, s
            break #at most one
    else:
        yield wordT, ''

#assert [('物價', '物价'), ('物盡其用', '物尽其用')] == [*迭代提取词义中的繁简对照项囗多行词条词义囗(_data4test)], [*迭代提取词义中的繁简对照项囗多行词条词义囗(_data4test)]
assert [('物價', '物价'), ('物件', ''), ('物盡其用', '物尽其用'), ('物景', '')] == [*迭代提取词义中的繁简对照项囗多行词条词义囗(_data4test)], [*迭代提取词义中的繁简对照项囗多行词条词义囗(_data4test)]


