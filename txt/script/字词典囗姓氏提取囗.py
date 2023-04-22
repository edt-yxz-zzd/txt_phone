#__all__:goto
r'''[[[
e script/字词典囗姓氏提取囗.py


script.字词典囗姓氏提取囗
py -m nn_ns.app.debug_cmd   script.字词典囗姓氏提取囗 -x
py -m nn_ns.app.doctest_cmd script.字词典囗姓氏提取囗:__doc__ -ff -v
from script.字词典囗姓氏提取囗 import *

[[[
view script/字词典囗用字统计囗.py
===

view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词典.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-初步清理.txt
view /sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
view /sdcard/0my_files/tmp/out4py/古汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
view /sdcard/0my_files/tmp/out4py/汉语辞海囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
view /sdcard/0my_files/tmp/out4py/script.中文字典囗..格式化囗新华字典囗..新华字典.out.txt
view ++enc=utf16le /sdcard/0my_files/unzip/e_book/字词典/现代汉语词典（第五版）全文_更新.txt
]]]
[[
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.过滤出候选姓氏囗格式化囗字词典囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/古汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt --may_opath=None =4
===

py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.过滤出候选姓氏囗格式化囗字词典囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/古汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.古汉语字典囗.dump.out.txt
e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.古汉语字典囗.dump.out.txt

py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..APP.古汉语字典囗.dump.out.txt  --may_opath=None
丁
万俟
冯
党
区
郑
仇
任
佼
莘
菅
萧
太师
庾
员
姬
彪
澹台
缪
孩
贾
爨
梓
敖
肖
翟
翦
解
隽

/^[冯党仇任佼莘菅庾员彪缪梓隽]

py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..APP.古汉语字典囗.dump.out.txt  --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.古汉语字典囗.dump.out.txt
view  /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.古汉语字典囗.dump.out.txt




===
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.过滤出候选姓氏囗格式化囗字词典囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.汉语字典囗.dump.out.txt
e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.汉语字典囗.dump.out.txt
mv /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.汉语字典囗.dump.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..APP.汉语字典囗.dump.out.txt
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..APP.汉语字典囗.dump.out.txt  --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语字典囗.dump.out.txt
view  /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语字典囗.dump.out.txt
    1056个姓氏#有重复





===
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.过滤出候选姓氏囗格式化囗字词典囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/汉语辞海囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.汉语辞海囗.dump.out.txt

py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.再过滤囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.汉语辞海囗.dump.out.txt  --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤..APP.汉语辞海囗.dump.out.txt

e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤..APP.汉语辞海囗.dump.out.txt
mv /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤..APP.汉语辞海囗.dump.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤+人工编辑..APP.汉语辞海囗.dump.out.txt
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤+人工编辑..APP.汉语辞海囗.dump.out.txt

py_adhoc_call   nn_ns.CJK.CJK_data.raw.姓氏   @show_diff  :姓氏囗囗欧路词典囗汉语大辞典囗囗简体版   :姓氏囗囗应用程序囗汉语辞海
    35
京城
公晳
公甫
养由
匹娄
叱吕引
司鸿
园
如人
娵觜
库傉官
库褥官
彡姐
扶馀
旗号
术甲
术虎
淡台
淳于
滚
滾
矍相
耨盌温敦
蔿
角里
豕韦
赤
边韶寝
逢蒙
释迦
钟
钟离
销声
陶唐
鬔


\(^\|,\)\(京城\|公晳\|公甫\|养由\|匹娄\|叱吕引\|司鸿\|园\|如人\|娵觜\|库傉官\|库褥官\|彡姐\|扶馀\|旗号\|术甲\|术虎\|淡台\|淳于\|滚\|滾\|矍相\|耨盌温敦\|蔿\|角里\|豕韦\|赤\|边韶寝\|逢蒙\|释迦\|钟\|钟离\|销声\|陶唐\|鬔\)


py_adhoc_call   nn_ns.CJK.CJK_data.raw.姓氏   @show_diff  :姓氏囗囗欧路词典囗汉语大辞典囗囗简体版   :姓氏囗囗应用程序囗汉语辞海
    23=35+1-13
    +1:
    +公析
    -13:
    -匹娄
    -园
    -娵觜
    -旗号
    -淡台
    -滾
    -豕韦
    -赤
    -边韶寝
    -逢蒙
    -销声
    -陶唐
    -鬔
京城
公晳
公析
公甫
养由
叱吕引
司鸿
如人
库傉官
库褥官
彡姐
扶馀
术甲
术虎
淳于
滚
矍相
耨盌温敦
蔿
角里
释迦
钟
钟离

\(^\|,\)\(京城\|公晳\|公析\|公甫\|养由\|叱吕引\|司鸿\|如人\|库傉官\|库褥官\|彡姐\|扶馀\|术甲\|术虎\|淳于\|滚\|矍相\|耨盌温敦\|蔿\|角里\|释迦\|钟\|钟离\)


view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt
bug:发现2个误删:『矍相』『司鴻』
===
矍相
2025:('<B>矍相</B><DIV><DIV>1.古地名。在山東省曲阜市城內闕里西。後借指學宮中習射的場所。<NB>《禮記‧射義》：“孔子射於矍相之圃，蓋觀者如堵牆。”<NB>鄭玄注：“矍相，地名。”<NB>《北史‧張普惠傳》：“乞至九月，備飾盡行，然後奏《狸首》之章，宣矍相之命。”<NB>宋王禹偁《射宮選士賦》：“煥乎得矍相之義，洋然有闕里之儀。”<BR>2.複姓。見《通志‧氏族三》。</DIV></DIV>',)
===
司鴻
3455:('<B>司鴻</B><DIV><DIV>(司鴻,司鸿)<BR>複姓。<NB>漢有中大夫司鴻儀。見《通志‧氏族四》。</DIV></DIV>',)
更新:
    e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt






py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤+人工编辑..APP.汉语辞海囗.dump.out.txt  --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语辞海囗.dump.out.txt
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语辞海囗.dump.out.txt
    979个#有重复
    969个#有重复
    961个#有重复

=====
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.过滤出候选姓氏囗格式化囗字词典囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.中文字典囗..格式化囗新华字典囗..新华字典.out.txt  --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..TXT.中文字典囗.新华字典.格式化.out.txt
e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..TXT.中文字典囗.新华字典.格式化.out.txt
mv /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..TXT.中文字典囗.新华字典.格式化.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..TXT.中文字典囗.新华字典.格式化.out.txt

py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..TXT.中文字典囗.新华字典.格式化.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..TXT.中文字典囗.新华字典.格式化.out.txt
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..TXT.中文字典囗.新华字典.格式化.out.txt
    1497个#有重复

=====
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.过滤出候选姓氏囗格式化囗字词典囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词典.txt   --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.现代汉语词典.词典.out.txt

e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.现代汉语词典.词典.out.txt
mv /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.现代汉语词典.词典.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.现代汉语词典.词典.out.txt

view  /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.现代汉语词典.词典.out.txt
[[检验:
/^x.*\n.*）姓
    确认:<无>

%s/^===\n[^x].*\n\d.*\(\([0-9\u2460-\u24ff\u25b2-\u2609]\|（[A-Z][\0-\u2000]*）\|'[\0-\u2000]*\)\(([^()]*)\|（[^（）]*）\|\[[^\[\]]*\]\|<br \/>\)*姓\(（[^（）]*）\)\?。\).*\n//
    临时性修改，不保存
/^[^x=0-9]
    只剩2个非『x』:
        兒,倪
        万俟#万


^===\nx.*\n\d.*\([0-9\u2460-\u24ff\u25b2-\u2609]\|（[A-Z][\0-\u2000]*）\|'[\0-\u2000]*\)\(([^()]*)\|（[^（）]*）\|\[[^\[\]]*\]\|<br \/>\)*姓
    只有4个『x』:
        x氏
        x姓
        x姓名
        x张冠李戴
]]

py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.现代汉语词典.词典.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.现代汉语词典.词典.out.txt

view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.现代汉语词典.词典.out.txt
    941#有重复
    乐
    乐le4
    乐yue4


+再过滤+只保留关键义项:
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.再过滤囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.现代汉语词典.词典.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.现代汉语词典.词典.out.txt
view  /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.现代汉语词典.词典.out.txt
%s/^\(\d*:\).*\(\([0-9\u2460-\u24ff\u25b2-\u2609]\|（[A-Z][\0-\u2000]*）\|'[\0-\u2000]*\)\(([^()]*)\|（[^（）]*）\|\[[^\[\]]*\]\|<br \/>\)*姓\(（[^（）]*）\)\?。\).*/\1    \2/
    临时性修改，不保存，但另存为:
    w /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.现代汉语词典.词典.out.txt
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.现代汉语词典.词典.out.txt
/:\S
    确认:
    只剩2个(+2个 使用了 私用区字符):
        兒,倪
        房#房  ###bug:'\ue7a1'是多余的
        焦#焦  ###bug:'\ue7a1'是多余的
        万俟#万
    ===
    确认『乐』:
    乐,乐le4,乐yue4
    365:    （Yuè）姓（与Lè不同姓）。




=====
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.过滤出候选姓氏囗格式化囗字词典囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt   --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.汉语大辞典.词典.out.txt
    有误:缺『-初步清理』
    view script/欧路词典囗清理超文本标记.py

py_adhoc_call   script.欧路词典囗清理超文本标记   @初步清理囗超文本标记囗囗欧路词典囗超链接囗囗文件囗 --encoding:u8   --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.汉语大辞典.词典.out.txt   --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.汉语大辞典.词典-初步清理.out.txt

du -h /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
    8.5M
    !!!
    过滤算法不行，繁体字
e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
mv /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..欧路词典.汉语大辞典.词典-初步清理.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt

view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt


py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.再过滤囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt
du -h /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt
    6M !!!
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
diff /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
< 普六茹
< 普陋茹
< 有呂
    --賜姓
    ++if '氏曰' in s or '姓曰' in s:
< 孫
< 賈
< 毛
< 趙
< 許
< 鄭
< 周

^[孫賈毛趙許鄭周]
孫#伯樂
賈#賈 ###???无『姓』项？
毛#毛 ###???无『姓』项？
趙#尉佗
許#許 ###???无『姓』项？
鄭#鄭 ###???无『姓』项？
周#周 ###???无『姓』项？

e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt
    复制粘贴附后

mv /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+复制粘贴附后以补全..欧路词典.汉语大辞典.词典-初步清理.out.txt

py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+复制粘贴附后以补全..欧路词典.汉语大辞典.词典-初步清理.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+复制粘贴附后以补全+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt

diff /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+复制粘贴附后以补全+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
< 孫
< 賈
< 毛
< 趙
< 許
< 鄭
< 周
> 孫
> 賈
> 毛
> 趙
> 許
> 鄭
> 周


:%s/\d\+[.]姓.\{-}>\([I0-9]\|<\/DIV>\)\@=/XXXXX\rYYYYY\0ZZZZZ\rWWWWW/g

e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+复制粘贴附后以补全..欧路词典.汉语大辞典.词典-初步清理.out.txt
    1429 处 少了7处
e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt
    1436处/1433行
    w /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt.tmp
grep YYYYY /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt.tmp > /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt.tmp.grep
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt.tmp.grep

grep YYYYY /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+复制粘贴附后以补全..欧路词典.汉语大辞典.词典-初步清理.out.txt >  /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+复制粘贴附后以补全..欧路词典.汉语大辞典.词典-初步清理.out.txt.grep
[
diff    /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt.tmp.grep    /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+复制粘贴附后以补全..欧路词典.汉语大辞典.词典-初步清理.out.txt.grep

134d133
< YYYYY9.姓。<NB>明有春又邰。見明顧起元《客座贅語‧僻姓》。<BR>ZZZZZ
524d522
< YYYYY17.姓。<NB>宋有句中正。見《宋史‧文苑傳三》。<BR>ZZZZZ
681d678
< YYYYY1.姓名埋沒，不為人知。<NB>《漢書‧翟方進傳》：“設令時命不成，死國埋名，猶可以不慚於先帝。”<NB>明李東陽《擬古出塞》詩之一：“征南競投籍，征北多埋名。”<BR>ZZZZZ
1152,1154d1148
< YYYYY1.姓氏。<NB>《史記‧平準書》：“守閭閻者食粱肉，為吏者長子孫，居官者以為姓號。”<NB>裴駰集解引如淳曰：“倉氏、庾氏 是也。”<BR>ZZZZZ
< YYYYY1.姓和氏。姓、氏本有分別，姓起於女系，氏起於男系。<NB>秦漢以後，姓、氏不合一，通稱姓，或兼稱姓氏。<NB>《通志‧氏族略序》：“三代之前，姓氏分而為二，男子稱氏，婦人稱姓……三代之後，姓氏合而為一。”<NB>宋洪邁《容齋三筆‧漢人希姓》：“兩《漢書》所載人姓氏，有後世不著見者甚多，漫紀于此，以助氏族書 之遺脫。”<NB>清顧炎武《日知錄‧氏族》：“姓氏之稱，自太史公始混而為一。”<BR>ZZZZZ
< YYYYY2.姓氏家族。<NB>南朝梁沈約《奏彈王源》：“竊尋璋之姓 族，士庶莫辨。”<NB>北齊顏之推《顏氏家訓‧勉學》：“夫學者，貴能博聞也。郡國山川、官位姓族、衣服飲食、器四制度，皆欲根尋 ，得其原本。”</DIV>ZZZZZ
1430d1423
< YYYYY2.姓氏。表明家族、宗族系統的稱號。<NB>《左傳‧隱公八 年》：“無駭卒，羽父請謚與族。公問族於眾仲，眾仲對曰：‘天子 建德，因生以賜姓，胙之土而命之氏；諸侯以字為謚，因以為族； 官有世功，則有官族，邑亦如之。’”<NB>《戰國策‧秦策二》：“費 人有與曾子同名族者而殺人。”<NB>高誘注：“族，姓。”<NB>ZZZZZ
===>:
x春
x句
x埋名
x姓號
x姓氏
x姓族
x族
===>:
春,句:漏！
]


刷新:
    ++bug:发现2个误删:『春』『句』
    ++逆转被过滤『孫賈毛趙許鄭周』<<==附『#姓氏』于解释后，使7个 被 再过滤 跳过的词 保留
    --bug:发现1个非姓:『麼』
    ++pinyin多音姓『樂那朴相余俞』
    ++bug:发现2个误删:『矍相』『司鴻』
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
    确认有『春』『句』
    确认:逆转被过滤『孫賈毛趙許鄭周』
    确认无『麼』
    确认:多音姓
        /^[樂那朴相余俞]
        xxx /^[安樂那朴仵相余俞]
    确认有『矍相』『司鴻』
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.再过滤囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt
view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt
    确认『普六茹』『有呂#養物』
    确认『^[孫賈毛趙許鄭周]』
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
diff /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
    这次相同了
cp /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt    /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
    :%s/\d\+[.]姓.\{-}>\([I0-9]\|<\/DIV>\)\@=/XXXXX\rYYYYY\0ZZZZZ\rWWWWW/g
    1431处/1428行
        少了无关的五处，ok
===加『複』
:%s/\d\+[.]複\?姓.\{-}>\([I0-9]\|<\/DIV>\)\@=/XXXXX\rYYYYY\0ZZZZZ\rWWWWW/g
    1650处/1647行
        #全文件一共才2262词条#被提取出来
%s/.*XXXXX\n//
    1650
%s/\nWWWWW.*//
    1647 少了3处:安樂相
        <<== WWWWW.*XXXXX 同行，先删XXXXX
/YYYYY.*\nYYYYY
    安
    樂
    相
合并 安樂相 义项 使同行
du -h /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤..欧路词典.汉语大辞典.词典-初步清理.out.txt
    6M
du -h /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
    556K

^.\{5000}
    齊,任
^.\{4000}
    名,脩,則
^.\{3000}
    強,沈,遂,周
^.\{2000}
    不,紀,毛,釋,提,許,序,壯
    以上手动删
^.\{1000}
    賁,但,黨,蕃,鬲,賈,繆,淖,頗,朴,無,絮,苑
        未处理

bug: :%s/[DIVX]\@<![IVX]\+[^IVX0-9]\{-}複\?姓.\{-}>\([I0-9]\|<\/DIV>\)\@=/XXXXX\rYYYYY\0ZZZZZ\rWWWWW/g
    50多?处/?行
    取消 有bug
    I\+ --> <DIV>, IV IX XII...


<B>賁</B><DIV><DIV>(賁,贲)<BR>

:%s/\C>\@<=\(\([IVX]\+[^IVX0-9]\{-}\|\d\+[.]\)複\?姓.\{-}>\)\([IVX0-9]\|<\/DIV>\)\@=/RRRRR\rSSSSS\1TTTTT\rUUUUU/g
    58处/56行
    #下面更新: 通/亦作

^UUU.*姓
    <无>
%s/\nUUUUU.*//
    全删

姓.*RRR$
    蕃,逢
        手动删
%s/>I.*RRR$/>/
    42处/42行
56-2-42=12
    人工确认，剩余12个 头部已不含义项

%s/('\(.*\)\nSSSSS/    \1    SSSSS
    54处/54行

/^S
    酈:删 义项
    朴:保留 2义项
        54+2=56 完成
du -h /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
    340K
/^.\{1000}
    鬲,賈,無
        郾#鬲
        賈#賈 ###???无『姓』项？
        無,鄦
    手动删

/???
    /###???无『姓』项？
    /姓
    鄧,江,孟,宋,蕭,徐,鄭
        手动删
/^.\{500}
    10个
        bug『麼』:删除
    6.通“[^班]”。姓
    2.(又讀é)姓
    5.通“[^蓋]”。姓
    5.亦作“[^銅鍉]”。複姓

:%s/\C>\@<=\(\([IVX]\+[^IVX0-9]\{-}\|\d\+[.]\)\(\(通\|亦作\)“\[\^[^\]]\+\]”。\)\?\(([^()]\+)\)\?複\?姓.\{-}>\)\([IVX0-9]\|<\/DIV>\)\@=/RRRRR\rSSSSS\1TTTTT\rUUUUU/g
    7处/7行
^UUU.*姓
    <无>
%s/\nUUUUU.*//
    全删
    7处/7行

姓.*RRR$
    <无>
%s/>[I1].*RRR$/>/
    全去尾
    7处/7行
%s/('\(.*\)\nSSSSS/    \1    SSSSS
    合并
    7处/7行

/.\{300}
    /姓
        部分选择性删减
du -h /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
    300K


注意:多音姓
^[余俞相朴那樂]

:%s/\C>\@<=\(\([IVX]\+[^IVX0-9]\{-}\|\d\+[.]\)\(\(通\|亦作\)“\[\^[^\]]\+\]”。\)\?\(([^()]\+)\)\?複\?姓.\{-}>\)\([IVX0-9]\|<\/DIV>\)\@=/RRRRR\rSSSSS\1TTTTT\rUUUUU/g
    1729处/1716行
取消，加『“”』:
:%s/\C>\@<=\(\([IVX]\+[^IVX0-9“”]\{-}\|\d\+[.]\)\(\(通\|亦作\)“\[\^[^\]]\+\]”。\)\?\(([^()]\+)\)\?複\?姓.\{-}>\)\([IVX0-9]\|<\/DIV>\)\@=/RRRRR\rSSSSS\1TTTTT\rUUUUU/g
    1722处/1714行
    /^S.*\nU.*\nS
        安樂那朴仵相余俞
    多了『安』『仵』，但都 非多音姓
    [[
23.姓。漢有安成。見《廣韻》卷一引漢應劭《風俗通》。
24.姓。古代安息人或安國人來華，常以安為姓，如漢有安世高(安息人)，唐有九姓商胡安門物(安國人)。
---
6.姓。唐有仵士政。見《資治通鑒‧唐高祖武德元年》。
9.通“[^伍]”。姓。《敦煌變文‧伍子胥變文》：“楚之上相，姓仵名奢……伍奢乃有二子，見事於君，小者子胥，大者子尚。”《敦煌變文‧伍子胥變文》：“下官身是仵子胥，避楚逃逝入南吳。”
    ]]


[[打补丁:
更新所有副本:
===
?script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt
    ++pinyin@词目
===
?script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
    ++pinyin@词目
    ++pinyin@义项
===
?script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
===
^[安樂那朴仵相余俞]
===
安
8:  <B>安</B><DIV><DIV>ān<BR>ㄢ<BR>〔《廣韻》烏寒切，平寒，影。〕<BR>亦作“[^侒]”。<BR>    SSSSS23.姓。<NB>漢有安成。見《廣韻》卷一引漢應劭《風俗通》。<BR>TTTTT    SSSSS24.姓。古代安息人或安國人來華，常以安為姓，如漢有安世高(安息人)，唐有九姓商胡安門物(安國人)。</DIV>TTTTT
===
樂,樂yue4,樂le4
937:    <B>樂</B><DIV><DIV>(樂,乐)<BR>    SSSSSI<NB>yuè<NB>ㄩㄝˋ<NB>〔《廣韻》五角切，入覺，疑。〕<NB>7.姓。<NB>戰國時有燕將樂毅。<BR>TTTTT    SSSSSII<NB>lè<NB>ㄌㄜˋ<NB>〔《廣韻》盧各切，入鐸，來。〕<NB>9.姓(與樂yuè不同姓)。<BR>TTTTT
===
那,那nuo2,那na1,葉赫那拉
1143:   <B>那</B><DIV><DIV>    SSSSSI<NB>nuó<NB>ㄋㄨㄛˊ<NB>〔《廣韻》諾何切，平歌，泥。〕<NB>8.姓。<NB>明有那嵩。見明陳士元《姓觿》卷三、《明史》本傳。<BR>TTTTT    SSSSSVII<NB>nā<NB>ㄋㄚ<NB>姓。<NB>《清史稿‧那桐傳》：“那桐，字琴軒，葉赫那拉氏，內務府滿洲鑲黃旗人。”<NB>夏仁虎《舊京瑣記‧朝流》：“清光緒初，滿部員之最負時望者為榮祿、端方、那桐，皆於部中最有權，當時所謂紅人也。時有聯云：六部三司官大榮、小那、端老四，九城五窯姐雙紅、二翠、萬人迷。皆喻其紅也。”</DIV>TTTTT
===
朴,朴pu2,朴piao2
1228:   <B>朴</B><DIV><DIV>(參見[^樸])<BR>    SSSSSV<NB>pú<NB>ㄆㄨˊ<NB>〔《集韻》披尤切，平尤，滂。〕<NB>姓。<NB>三國魏有巴七姓夷王朴胡。見《三國志‧魏志‧武帝紀》。<BR>TTTTT    SSSSSVI<NB>piáo<NB>ㄆ〡ㄠˊ<NB>姓。<NB>明代有朴素。<BR>TTTTT
===
仵
1727:   <B>仵</B><DIV><DIV>wŭ<BR>ㄨˇ<BR>〔《廣韻》疑古切，上姥，疑。〕<BR>    SSSSS6.姓。<NB>唐有仵士政。見《資治通鑒‧唐高祖武德元年》。<BR>TTTTT    SSSSS9.通“[^伍]”。姓。<NB>《敦煌變文‧伍子胥變文》：“楚之上相，姓仵名奢……伍奢乃有二子，見事於君，小者子胥，大者子尚。”<NB>《敦煌變文‧伍子胥變文》：“下官身是仵子胥，避楚逃逝入南吳。”</DIV>TTTTT
===
相,相xiang1,相xiang4
1792:   <B>相</B><DIV>    SSSSSI<NB>xiāng<NB>ㄒ〡ㄤ<NB>〔《廣韻》息良切，平陽，心。〕<NB>7.姓。<NB>晉有相龍。見《晉書‧五行志上》。<BR>TTTTT    SSSSSII<NB>xiàng<NB>ㄒ〡ㄤˋ<NB>〔《廣韻》息亮切，去漾，心。〕<NB>23.姓。<NB>晉有相雲。見《晉書‧姚興載記上》。</DIV>TTTTT
===
余,余yu2,余yu4
2021:   <B>余</B><DIV><DIV>(參見[^餘])<BR>    SSSSSI<NB>yú<NB>ㄩˊ<NB>〔《廣韻》以諸切，平魚，以。〕<NB>5.姓。<NB>TTTTT    SSSSSII<NB>yù<NB>ㄩˋ<NB>〔《集韻》羊茹切，去御，以。〕<NB>姓。見“[^余且]”。<BR>TTTTT
===
俞,俞yu2,俞chou4
2026:   <B>俞</B><DIV>    SSSSSI<NB>yú<NB>ㄩˊ<NB>〔《廣韻》羊朱切，平虞，以。〕<NB>9.姓。<BR>TTTTT    SSSSSV<NB>chòu<NB>ㄔㄡˋ<NB>〔《廣韻》丑救切，去宥，徹。〕<NB>姓。<NB>漢有司徒掾俞連。見《廣韻‧去宥》。</DIV>TTTTT
]]
[[打补丁+更新:
?script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..欧路词典.汉语大辞典.词典-初步清理.out.txt
    误删，重返
?script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
    打补丁
        『矍』之后『矍相』
        『司』之后『司鴻』
刷新:
    view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt
    view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt
===
矍相
2025:('<B>矍相</B><DIV><DIV>1.古地名。在山東省曲阜市城內闕里西。後借指學宮中習射的場所。<NB>《禮記‧射義》：“孔子射於矍相之圃，蓋觀者如堵牆。”<NB>鄭玄注：“矍相，地名。”<NB>《北史‧張普惠傳》：“乞至九月，備飾盡行，然後奏《狸首》之章，宣矍相之命。”<NB>宋王禹偁《射宮選士賦》：“煥乎得矍相之義，洋然有闕里之儀。”<BR>2.複姓。見《通志‧氏族三》。</DIV></DIV>',)
===
司鴻
3455:('<B>司鴻</B><DIV><DIV>(司鴻,司鸿)<BR>複姓。<NB>漢有中大夫司鴻儀。見《通志‧氏族四》。</DIV></DIV>',)
]]







bug『麼』已删，待刷新
bug『矍相/司鸿』已加，待刷新
py_adhoc_call   script.字词典囗姓氏提取囗   @not_show.提取囗人工编辑过的过滤文件囗 --encoding:u8  --ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt --may_opath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
diff /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
    相同，无『麼』



化繁为简:
繁体字->简体字
繁体词->简体词
input:
    view /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
    view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt
worker:
    view ../../python3_src/seed/recognize/cmdline/txt_process.py
    view ../../python3_src/nn_ns/CJK/CJK_common/化繁为简.py

ipath='../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt'
ipath4table=/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt


opath=/sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt
py_adhoc_call   nn_ns.CJK.CJK_common.化繁为简   @化繁为简囗囗文件路径囗 --encoding:u8 +是否输出囗繁简对照表 --路径囗输入囗繁简对照表:"$ipath4table"   --路径囗输入囗繁体词:"$ipath"  +discard_bad_line_in_table  --路径囗输出:"$opath" --may_fallback_table='dict(幺="幺")' +force
    ok!
view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt
么:
幺:
枚:

矍:
矍相:
君:

司:
司鴻:司鸿
司空:


opath=/sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt
py_adhoc_call   nn_ns.CJK.CJK_common.化繁为简   @化繁为简囗囗文件路径囗 --encoding:u8 -是否输出囗繁简对照表 --路径囗输入囗繁简对照表:"$ipath4table"   --路径囗输入囗繁体词:"$ipath"  +discard_bad_line_in_table  --路径囗输出:"$opath" --may_fallback_table='dict(幺="幺")'
view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt
么
幺
枚

矍
矍相
君

司
司鸿
司空







=====
=====
=====
TODO:
view ++enc=utf16le /sdcard/0my_files/unzip/e_book/字词典/现代汉语词典（第五版）全文_更新.txt
=====
py_adhoc_call   nn_ns.CJK.CJK_common.is_hz   @not_show.show_partition_charset_by_is_hz__5path_  --encoding:u8  --may_opath=None  --may_ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt

py_adhoc_call   nn_ns.CJK.CJK_common.is_hz   @not_show.show_partition_charset_by_is_hz__5path_  --encoding:u8  --may_opath=None  --may_ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.现代汉语词典.词典.out.txt
    发现:『房』『焦』'\ue7a1'
        该 私用区字符 是多余的

py_adhoc_call   nn_ns.CJK.CJK_common.is_hz   @not_show.show_partition_charset_by_is_hz__5path_  --encoding:u8  --may_opath=None  --may_ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..TXT.中文字典囗.新华字典.格式化.out.txt

py_adhoc_call   nn_ns.CJK.CJK_common.is_hz   @not_show.show_partition_charset_by_is_hz__5path_  --encoding:u8  --may_ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语辞海囗.dump.out.txt   --may_opath=None
py_adhoc_call   nn_ns.CJK.CJK_common.is_hz   @not_show.show_partition_charset_by_is_hz__5path_  --encoding:u8  --may_ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语字典囗.dump.out.txt   --may_opath=None
py_adhoc_call   nn_ns.CJK.CJK_common.is_hz   @not_show.show_partition_charset_by_is_hz__5path_  --encoding:u8  --may_ipath:/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.古汉语字典囗.dump.out.txt   --may_opath=None

======
!mkdir script/字词典囗姓氏提取囗.py.outs/

cp -t script/字词典囗姓氏提取囗.py.outs/   /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
view script/字词典囗姓氏提取囗.py.outs/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
    确认无『麼』
    确认:多音姓
        /^[樂那朴相余俞]

ls  /sdcard/0my_files/tmp/out4py/*提取囗人工编辑过的过滤文件囗*
ls  /sdcard/0my_files/tmp/out4py/*人工编辑+提取囗人工编辑过的过滤文件囗*
cp -t script/字词典囗姓氏提取囗.py.outs/  /sdcard/0my_files/tmp/out4py/*人工编辑+提取囗人工编辑过的过滤文件囗*

du -h script/字词典囗姓氏提取囗.py.outs/
52k

!mkdir script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/
cp -t script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/   /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
du -h script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
    300K

cp -t script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/   /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.现代汉语词典.词典.out.txt
du -h script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.现代汉语词典.词典.out.txt
    32K


for x in $( ls script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/ ) ; do  echo $x ;   done

for nm in $( ls script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/ ) ; do  { echo $nm ; diff /sdcard/0my_files/tmp/out4py/$nm  script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/$nm ; }  done




for nm in $( ls script/字词典囗姓氏提取囗.py.outs/ ) ; do { echo $nm ; diff /sdcard/0my_files/tmp/out4py/$nm  script/字词典囗姓氏提取囗.py.outs/$nm ; }  done

du -h script/字词典囗姓氏提取囗.py.outs/
52k

du -h script/字词典囗姓氏提取囗.py.outs/*
4.0K    script/字词典囗姓氏提取囗.py.outs/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.古汉语字典囗.dump.out.txt
8.0K    script/字词典囗姓氏提取囗.py.outs/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语字典囗.dump.out.txt
8.0K    script/字词典囗姓氏提取囗.py.outs/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..TXT.中文字典囗.新华字典.格式化.out.txt
16K     script/字词典囗姓氏提取囗.py.outs/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
4.0K    script/字词典囗姓氏提取囗.py.outs/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.现代汉语词典.词典.out.txt
8.0K    script/字词典囗姓氏提取囗.py.outs/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语辞海囗.dump.out.txt



du -h script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/*
304K    script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
32K     script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+再过滤+只保留关键义项..欧路词典.现代汉语词典.词典.out.txt






[、﹑]
ch2nm 、﹑
、
    'name': 'IDEOGRAPHIC COMMA',
    'unicode_hex': '0x3001'
﹑
    'name': 'SMALL IDEOGRAPHIC COMMA'
    'unicode_hex': '0xfe51'

x吹律定姓
101:('1.吹律定声，以别其姓。',)
e others/杂/词语解释/二十等爵.txt
e others/杂/词语解释/干支.txt

汉语大辞典
代人
指繼任者。
 《世說新語‧言語》“陶公疾篤，都無獻替之言，朝士以為恨”南朝梁劉孝標注：“按王隱《晉書》載侃（陶侃）臨終表曰：‘……伏願遴選代人，使必得良才，足以奉宣王猷，遵成志業，則雖死之日，猶生之年。’有表若此，非無獻替。”

貓
 《禮記‧郊特牲》：“迎貓，為其食田鼠也。”

椒举
388:('1.即春秋楚大夫伍举，为伍子胥祖父。因邑于椒，以邑为姓，故又称椒举。',)
以邑为姓!!!
    地、国号、官职、父名、父字、加后缀[孙/...]，


e ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏.py

[[
!mkdir ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/
cp -t ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/  script/字词典囗姓氏提取囗.py.outs/*
du -h ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/
    52K
cp -t ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/  script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/*

src=/sdcard/0my_files/tmp/out4py
dst=../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总
dst=script/字词典囗姓氏提取囗.py.outs
dst=script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项

show diffs:
for nm in $( ls "$dst/" ) ; do {  if [[ '' != $( diff "$src/$nm"  "$dst/$nm" -q ) ]] ; then echo "$nm" ; fi }  done

copy overwrite diffs:
for nm in $( ls "$dst/" ) ; do {  if [[ '' != $( diff "$src/$nm"  "$dst/$nm" -q ) ]] ; then cp -t "$dst/"  "$src/$nm" ; fi }  done




cp -t ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/   /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt   /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt

cp -t script/字词典囗姓氏提取囗.py.outs/  /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt   /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt

du -h ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/
    428K
du -h ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/*
16K     ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt
20K     ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt
    忽略前缀:『../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗』
304K    ...+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
32K     ...+人工编辑+再过滤+只保留关键义项..欧路词典.现代汉语词典.词典.out.txt
4.0K    ...+人工编辑+提取囗人工编辑过的过滤文件囗..APP.古汉语字典囗.dump.out.txt
8.0K    ...+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语字典囗.dump.out.txt
8.0K    ...+人工编辑+提取囗人工编辑过的过滤文件囗..TXT.中文字典囗.新华字典.格式化.out.txt
16K     ...+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
4.0K    ...+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.现代汉语词典.词典.out.txt
8.0K    ...+再过滤+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语辞海囗.dump.out.txt
]]








乐:④（Lè）姓（与Yuè不同姓）。②（Yuè）姓（与Lè不同姓）。
    !!!
余俞相朴那樂:多音不同姓
余:
I
 yú
5.姓。
II
 yù
姓。見“余且”。
俞:
I
 yú
 9.姓。
V
 chòu
 姓。
 漢有司徒掾俞連。見《廣韻‧去宥》

相:
I
 xiāng
 7.姓。
 晉有相龍。見《晉書‧五行志上》。
II
 xiàng
 23.姓。
 晉有相雲。見《晉書‧姚興載記上》。

朴:
V
 pú
 姓。
 三國魏有巴七姓夷王朴胡。見《三國志‧魏志‧武帝紀》。
VI
 piáo
 姓。
 明代有朴素。

那
I
 nuó
 8.姓。
 明有那嵩。見明陳士元《姓觿》卷三、《明史》本傳。
VII
 nā
 ㄋㄚ
 姓。
 《清史稿‧那桐傳》：“那桐，字琴軒，葉赫那拉氏，內務府滿洲鑲黃旗人。”

樂:
I
 yuè
 7.姓。
 戰國時有燕將樂毅
II
 lè
 9.姓(與樂yuè不同姓)。

多音字 有必要 拆出多字#古今字











终古
『姓/氏/名/尊/贵/同/異/庶/女/之/有/無/復/單/賜/別/自/己/吾/它/人/家/邦/國』都是姓


姓
6.姓。
 漢代有姓偉。見《漢書‧食貨志下》。

氏
 18.姓。
 五代有氏叔琮。見《舊五代史‧梁書》本傳。
名@现代汉语词典
⑨（Míng）姓。

尊姓大名
貴姓大名

尊
18.姓。
 明代有尊德。傳為尊廬氏之後。

贵
12.姓。
 漢有廬江太守貴遷。見《通志‧氏族五》引漢應劭《風俗通》。


 《詩‧小雅‧伐木》“籩豆有踐，兄弟無遠”唐孔穎達疏：“《禮》有同姓、異姓、庶姓。同姓，王之同宗，是父之黨也；異姓，王舅之親；庶姓，與王無親者。”

同
 29.姓。
 元代有同恕，見《元史》本傳。

異
14.姓。
 《通志‧氏族四》：“異氏。
 《姓纂》云：‘今溫州白水蠻有此姓。’”

庶
 9.姓。
 春秋時邾國有庶其。見《左傳‧襄公二十一年》。

女
III
 rŭ
 2.姓。
 春秋晉有女賈、女寬。見《左傳‧昭公二十六年》。

有男
古國名。後用作姓氏。有，詞頭。
 《史記‧夏本紀論》：“禹為姒姓，其後分封，用國為姓，故有夏后氏、有扈氏、有男氏。”

之
20.姓。
 漢代有之馬宇，明代有之輔。

有
 30.姓。
 漢有有祿。見漢應劭《風俗通‧姓氏下》。

無
 15.通“鄦”。古國名。後以為姓氏，假“許”為之。
 周宣王時有無專。
 《積古齋鐘鼎彝器款識‧周無專鼎》：“司徒南仲右，無專入門立中廷。”
 阮元釋：“無專，‘無’字當讀為鄦。古鄦字每省邑。”


复
複姓
復
20.姓。
 春秋楚有復遂。見《左傳‧文公十年》。

單
III
 shàn
 1.姓。
 春秋有單豹。
 唐有單雄信。見《莊子‧達生》、《新唐書‧李密傳》。



?性命賜別自己吾他她牠祂它人家族邦國
.xxxx..........xxxxxxxx......xx....
?父母子女祖孫兄弟姐妹夫妻叔伯姑舅姨丈甥
?君尔此彼則之以而也矣乎哉
?易变换更改隐藏埋冒俗
?其別我本俗內外受授皇帝王将相
?刁毫鼎小大左右上下揚顯望強僻希賎假詭公改革
?一二三两百万萬群
一,兩,雙,五,六,七,柒,八,九
    <<== 柒
不第
第二
第三
第五
第八

性xxx
命xxx
賜
8.姓。
 《世本‧氏姓》：“賜氏，齊大夫簡子賜之後。”
別
 26.姓。
 宋有別之傑。
自
12.姓。
 明有自勖。
己
II
 qĭ
 姓。
 漢有己茂。見《通志‧氏族三》。
吾
 3.姓。
 三國吳有吾粲。見《三國志‧吳志》本傳。
他她牠祂xxx
它
 6.姓。
 戰國有它囂。見《荀子‧非十二子》。
人
22.姓。
 明代有人傑。
家
 30.姓。
 春秋晉有家僕徒。見《左傳‧僖公十五年》。
族xxx
邦
7.姓。
 孔子有弟子邦巽。見《史記‧仲尼弟子列傳》。
國
14.姓。
 春秋齊有國佐。見《左傳‧成公十八年》。


終古
4.複姓。相傳為夏桀內史終古之後。見《通志‧氏族四》。

中华成语大词典
天下大屈
【拼音】：tiān xià dà jué
【解释】：屈：竭，天下财富耗尽。形容天灾人祸后，民穷财尽的情景。
【出处】：汉·贾谊《论积贮疏》：“兵旱相乘，天下大屈，有勇力者聚徒而衡击，罢夫赢老易子而咬其骨。”
]]

[[
e /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.古汉语字典囗.dump.out.txt
mv /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗..APP.古汉语字典囗.dump.out.txt /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..APP.古汉语字典囗.dump.out.txt
view  /sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑..APP.古汉语字典囗.dump.out.txt
======
0.不是姓:词条加前缀『x』
1.是姓:不变
2.是复姓:改词条
3.姓+复姓:改词条为序列
4.解释中包含姓氏，但词条本身不是:改词条为『序列#词条』

>>> ''.join(map(chr, range(0x2460, 0x2500)))
'①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓪⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾⓿'
>>> ''.join(map(chr, range(0x25b2, 0x2609+1)))
'▲△▴▵▶▷▸▹►▻▼▽▾▿◀◁◂◃◄◅◆◇◈◉◊○◌◍◎●◐◑◒◓◔◕◖◗◘◙◚◛◜◝◞◟◠◡◢◣◤◥◦◧◨◩◪◫◬◭◮◯◰◱◲◳◴◵◶◷◸◹◺◻◼◽◾◿☀☁☂☃☄★☆☇☈☉'


[[若『姓』多
先处理:
^[复姓氏]
再处理:
\(\(\\n\|.[\u2460-\u24ff\u25b2-\u2609]\)姓\(氏\?。\|\\n\|'\)\)\@!..姓
\(\(\\n\|\/>\|\d\.\|.[\]）\u2460-\u24ff\u25b2-\u2609]\)姓\(氏\?。\|\\n\|'\)\)\@!..姓
冠『x』之前先高亮:#比如:『贵』:否则，漏
/姓
从下向上
]]
[[若『姓』少:汉语大辞典
插入一个待处理符:
:%s/=\n\(.*\)$/=\rz\1
搜:
?姓\|^z
?姓\|亦作\|^x\|[^z]z[^z]\|^z[^z]\|\(^z\)\@!z
从下向上
x - 删『z』
rx - 『z』->『x』
    或 p - 『z』->『zz』
]]
===
贵
639:('8890:贝:9:251212534:khgm:gui:guì', '贵（貴）\nguì\n价钱高，与“贱”相对：贵贱（ａ．价格的高低；ｂ．指人的地位高低；ｃ．方言，无论如何）。春雨贵如油。\n指地位高：贵族。贵戚。贵望（尊贵的门第和声望）。\n敬辞，称与对方有关的事物：贵国。贵庚（请问别人年龄）。贵姓。贵干（问人要做什么）。\n特别好的，重要的：贵重。珍贵。尊贵。民为贵。\n值得看重，重视：可贵。\n指中国贵州省：云贵高原。\n姓。\n贱')
===
己,董,彭,秃,妘,曹,斟,芈,栾,郄,胥,原,狐,续,庆,伯,穆,陆,贺,刘,楼,干,嵇,尉,朱,李,王,石,刘,郭,柴#八姓
19:('1.祝融之后的八姓﹐即己﹑董﹑彭﹑秃﹑妘﹑曹﹑斟﹑芈。 2.晋八姓﹐即栾﹑郄﹑胥﹑原﹑狐﹑续﹑庆﹑伯。 3.北魏八姓﹐即穆﹑陆﹑贺﹑刘﹑楼﹑干﹑嵇﹑尉。 4.五代八姓﹐即梁(朱氏)﹑唐(庄宗李氏;明帝出身沙陀民，姓氏不明;废帝王氏)﹑晋(石氏)﹑汉(刘氏)﹑周(太祖郭氏﹐世宗柴氏)的八姓。',)

===
丁
0:('62:一:1:2:12:ding&zheng', 'dīng\n①<名>钉子。《晋书·陶侃传》：“及桓温伐蜀，又以侃所贮竹头作～装船。”\n②<形>健大。王充《论衡·无形》：“齿落复生，身气～强。”\n③<名>成年男性。《塞翁失马》：“～壮者引弦而战。”白居易《新丰折臂翁》：“无何天宝大征兵，户有三～点一～。”\n④<名>人口。《南史·何承天传》：“计～课仗。”\n⑤<名>从事某种职业的人。如庖丁、畦丁、园丁。《庄子·庖丁解牛》：“庖～为文惠君解牛。”\n⑥<名>天干的第四位。苏轼《石钟山记》：“元丰七年六月～丑，余自齐安舟行适临汝。”\n⑦姓。\n\nzhēng见“丁丁”。\n\n【丁丁】zhēngzhēng伐木声。\n【丁男】成年男子。\n【丁女】成年女子。\n【丁年】壮年。\n【丁役】服劳役的壮丁。\n【丁忧】遭父母之丧。')
===
万俟
1:('68:一:1:3:153:mo&wan', 'wàn\n①<数>十个一千。《孙膑减灶》：“使齐军入魏地为十～灶，明日为五～灶，又明日为三～灶。”\n\n【又】泛指众多。《察今》：“臂之若良医，病～变，药亦～变。”\n②<副>极；非常。韩愈《柳子厚暮志铭》：“无辞以白其大，且～无母子俱往理。”\n③<名>古代一种大型舞蹈的名字。《左传·隐公五年》：“九月，考仲子之宫，将～焉。”\n【注】万，萬。古代“万”读“mò”，用于复姓“万俟”。“萬”作数词时可以用“万”，如今简化统一作“万”。\n【万福】⒈多福，用于祝颂。⒉唐宋时女子行礼，常口称“万福”，后指女子行礼。\n【万机】古时专指皇帝处理日常杂事。\n【万籁】自然界的各种声响。\n【万乘】⒈万辆兵车。⒉周制，天子地方千里，兵车万辆，故以万乘称天子。⒊指大国。')
===
x丧
2:('100:一:1:8:12431534:sang', 'sàng\n①<动>丧失；失去。《鱼我所欲也》：“人皆有之，贤者能勿～耳。”\n②<动>丧亡；灭亡。《六国论》：“五国既～，齐亦不免矣。”\n③<动>葬；安葬。《寡人之于国也》：“是使民养生～死无憾也。”\n\nsāng<名>丧事。《殽之战》：“秦不哀吾～而伐吾同姓。”')
===
万,万俟
9:('68:一:3:153:dnv:mo,wan:mǒ,wàn', '万（萬）\nwàn\n数目，十个一千：万户侯（中国汉代侯爵的最高一级，享有万户农民的赋税。后泛指高官）。\n喻极多：万物。万方（a.指全国和世界各地；b.指姿态多种多样）。日理万机。气象万千。\n极，很，绝对：万万。万幸。\n姓。\n\n万\n（萬）\nmò\n〔万俟（\n（萬）q?）〕原为中国古代鲜卑族部落名；后为复姓。')
===
尉,尉迟
334:('3300:寸:11:51311234124:nfif:wei,yu:wèi,yù', '尉wèi\n古代官名，一般是武官：县尉。都尉。卫尉。太尉。\n军衔的一级，在校以下：尉官。少尉。上尉。\n〔尉氏〕地名，在中国河南省。\n姓。\n\n尉\nyù\n\u3000ㄩˋ\n〔尉迟〕复姓。\n〔尉犁〕地名，在中国新疆维吾尔自治区。')
===
司,司空,司徒,司马,司寇
385:('3748:口:5:51251:ngkd:si:sī', '司sī\n主管，操作：司法。司机。司令。司南（古代用磁石做成的辨别方向的仪器，为现在指南针的始祖）。司空（ａ．古代中央政府中掌管工程的长官；ｂ．复姓）。司徒（ａ．古代中央政府中掌管土地和徒役的长官，后为丞相；ｂ．复姓）。司马（ａ．古代中央政府中掌管军务的长官；ｂ．复姓）。司寇（ａ．古代中央政府中掌管刑狱、纠察的长官；ｂ．复姓）。\n官署名称：人事司。\n视察：司日月之长短。\n姓。')


#欧路词典.现代汉语词典
===
敖
3:('áo<br />BS 攵 | BH 6<br />①同‘遨’。<br />②（ào）姓。',)
===
邴
27:('Bǐng<br />BS 阝 | BH 5<br />姓。',)
===
啖
97:('dàn<br />BS 囗 | BH 8<br />啖1（啗、噉）〈书〉<br />①吃或给别人吃：～饭ㄧ以枣～之。<br />②拿利益引诱人：～以重利。<br /><br />啖2<br />[Dàn]姓。',)
===
乐
382:('（樂）lè<br />BS 丿 | BH 4<br />①快乐：欢～ㄧ～事ㄧ～不可支ㄧ心里～得像开了花。<br />②乐于：～此不疲。<br />③笑：他说了个笑话把大家逗～了。<br />④（Lè）姓（与Yuè不同姓）。另见yuè。<br /><br />◆ 乐（樂）<br />yuè<br />BS 丿 | BH 4<br />①音乐：奏～│～器。<br />②（Yuè）姓（与Lè不同姓）。另见lè。',)



#欧路词典.汉语大辞典
===
作
... ...28.姓。<NB>... ...


]]


#]]]'''
__all__ = r'''
    过滤出候选姓氏囗格式化囗字词典囗
        迭代读取囗格式化囗字词典囗

    提取囗人工编辑过的过滤文件囗
        迭代提取囗人工编辑过的过滤文件囗
        再过滤囗人工编辑过的过滤文件囗
            囗迭代读取囗人工编辑过的过滤文件囗
                iter_blocks5line_contents_
                icut_if_eq_

'''.split()#'''
__all__


#from seed.str_tools.iter_split_ex_by_ import iter_split_ex_by_
from seed.seq_tools.find_all import find_all_, iter_all_
from seed.iters.isplit_if import iter_split_if_starts_, iter_split_if_ends_, iter_split_with_sep_if_, iter_split_without_sep_if_
from seed.io.iter_line_contents__ver2 import iter_line_contents_ex__path__human, iter_line_contents__path
#def iter_line_contents__path(ipath, /, *, encoding, newline=default_may_smay_newline, kwargs4open=None, may_newlines=default_may_newlines, without_last_line_if_empty=False):
from seed.tiny import mk_fprint, ifNone
from seed.io.savefile__str_tuple import SaveStrTupleAsMultiLine, std_saver4str_tuple
    #def iter_read_str_tuple_from_ifile_(sf, ifile, /):
from seed.io.may_open import open4w, open4w_err, open4r
#def open4w(may_opath, /, *, force, xencoding):
from itertools import islice


def 迭代读取囗格式化囗字词典囗(ipath, /, *, encoding):
    if not encoding: raise TypeError
    with open4r(ipath, xencoding=encoding) as ifile:
        for t in std_saver4str_tuple.iter_read_str_tuple_from_ifile_(ifile):
            word = t[0]
            data = t[1:]
            yield word, data

def _in_(sub, whole, /):
    return f',{sub},' in whole
def _is_good_(s, /):
    for i in iter_all_('姓', s):
        assert '姓' == s[i]
        if not (_in_(s[i-1:i+1], ',百姓,万姓,种姓,同姓,家姓,异姓,隐姓,贵姓,尊姓,萬姓,種姓,異姓,隱姓,貴姓,何姓,諸姓,诸姓,姜姓,姬姓,') or _in_(s[i:i+2], ',姓名,姓姬,姓杨,姓李,姓刘,姓劉,姓楊,姓韓,姓孫,姓趙,姓甚,')):
            #remove:赐姓,賜姓,
            return True
        if '氏曰' in s or '姓曰' in s:
            return True
    return False
assert not _is_good_('')
assert not _is_good_('氏')
assert not _is_good_('百姓')
assert not _is_good_('百姓同姓名种姓百姓姓李')
assert _is_good_('姓')
assert _is_good_('姓百姓')
assert _is_good_('百姓姓')
assert _is_good_('<B>有呂</B><DIV><DIV>(有呂,有吕)<BR>古國名。<NB>姜姓。傳為四岳之後。其國故址在今河南南陽西。<NB>春秋初年為楚國所滅。有，詞頭。<NB>《國語‧周語下》：“祚四嶽國，命以侯伯，賜姓曰姜、氏曰有呂。”<NB>韋昭注：“以國為氏也。”</DIV></DIV>')

def 过滤出候选姓氏囗格式化囗字词典囗(*args4islice, ipath, may_opath, encoding, force=False):
    if not encoding: raise TypeError
    it = 迭代读取囗格式化囗字词典囗(ipath, encoding=encoding)
    #it = ((word, data) for word, data in it if any('姓' in s for s in data))
    it = ((word, data) for word, data in it if any(map(_is_good_, data)))
    if args4islice:
        it = islice(it, *args4islice)

    with open4w(may_opath, xencoding=encoding, force=force) as ofile:
        fprint = mk_fprint(ofile)
        for idx, (word, data) in enumerate(it):
            fprint('===')
            fprint(word)
            fprint(idx, data, sep=':')

def 提取囗人工编辑过的过滤文件囗(*args4islice, ipath, may_opath, encoding, force=False):
    if not encoding: raise TypeError
    it = 迭代提取囗人工编辑过的过滤文件囗(ipath, encoding=encoding)
    if args4islice:
        it = islice(it, *args4islice)

    with open4w(may_opath, xencoding=encoding, force=force) as ofile:
        fprint = mk_fprint(ofile)
        for word in it:
            fprint(word)

def _iter5words_str_(words_str, /):
    if not words_str.startswith('x'):
        assert not 'x' in words_str or (words_str[0]=='相' and 'xiang' in words_str), words_str
        assert not 'z' in words_str, words_str
        assert not '，' in words_str, words_str
        assert not '、' in words_str, words_str
        assert not '﹑' in words_str, words_str

        ws, _, _ = words_str.partition('#')
        assert not '#' in ws
        assert ws
        assert ws.split() == [ws], ws
        surnames = ws.split(',')
        assert surnames
        assert all(surnames), words_str
        yield from surnames
    return
def 迭代提取囗人工编辑过的过滤文件囗(ipath, /, *, encoding):
    pairs = 囗迭代读取囗人工编辑过的过滤文件囗(ipath, encoding=encoding)
    #surnames = (word for words_str, payload in pairs if not words_str.startswith('x') for word in words_str.split(','))
    surnames = (word for words_str, payload in pairs for word in _iter5words_str_(words_str))
    return surnames
def 囗迭代读取囗人工编辑过的过滤文件囗(ipath, /, *, encoding):
    line_contents = iter_line_contents__path(ipath, encoding=encoding, without_last_line_if_empty=True)
    pairs = blocks = iter_blocks5line_contents_([], '===', line_contents)
    return pairs
def iter_blocks5line_contents_(header, sep, line_contents, /):
    line_contentss = icut_if_eq_(sep, line_contents)
    for _header in line_contentss:
        assert _header == [*header], (_header, header)
        #discard header
        break
    blocks = line_contentss
    return blocks
def icut_if_eq_(sep, strs, /):
    f = lambda s:s == sep
    return iter_split_without_sep_if_(f, strs)

def 再过滤囗人工编辑过的过滤文件囗(*args4islice, ipath, may_opath, encoding, force=False, may_is_good_=None):
    is_good_ = ifNone(may_is_good_, _is_good_)
    pairs = 囗迭代读取囗人工编辑过的过滤文件囗(ipath, encoding=encoding)
    it = pairs = ((words_str, payload) for words_str, payload in pairs if (not words_str.startswith('x')) and is_good_(payload))

    if args4islice:
        it = islice(it, *args4islice)

    with open4w(may_opath, xencoding=encoding, force=force) as ofile:
        fprint = mk_fprint(ofile)
        for idx, (words_str, payload) in enumerate(it):
            _idx, _sep, data = payload.partition(':')
            assert _sep
            fprint('===')
            fprint(words_str)
            fprint(idx, data, sep=':')



from script.字词典囗姓氏提取囗 import *
