#__all__:goto
r'''[[[
e script/英语词霸囗.py
主要输出:
    view /sdcard/0my_files/tmp/out4py/英语词霸囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt


script.英语词霸囗
py -m nn_ns.app.debug_cmd   script.英语词霸囗 -x
py -m nn_ns.app.doctest_cmd script.英语词霸囗:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd script.英语词霸囗!
py_adhoc_call   script.英语词霸囗   @f
from script.英语词霸囗 import *





[[
e script/英语词霸囗.py

du -h    /sdcard/0my_files/apk/学习查询/com.xiaoqiang.dictionary_2.9.7.apk_
6.5M
    英语词霸

7z l    /sdcard/0my_files/apk/学习查询/com.xiaoqiang.dictionary_2.9.7.apk_
                    .....      3629853      3587480  assets/dict.zip
1970-01-01 08:00:00 .....       189366       181659  assets/gdt_plugin/gdtadv2.jar
                    .....      4513508      1843904  classes.dex
                    .....       190024       190024  resources.arsc
------------------- ----- ------------ ------------  ------------------------
1970-01-01 08:00:00            9948592      6702778  598 files

mkdir /sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/
cd /sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/

7z x    /sdcard/0my_files/apk/学习查询/com.xiaoqiang.dictionary_2.9.7.apk_   assets/dict.zip

7z l /sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/assets/dict.zip
7z x /sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/assets/dict.zip
du -h /sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/dict.db
7.2M
hexdump   /sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/dict.db  -C -n 0x100 -s 0
00000000  53 51 4c 69 74 65 20 66  6f 72 6d 61 74 20 33 00  |SQLite format 3.|

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/dict.db    --nm4table:sqlite_master
('table', '英语单词', '英语单词', 2, 'CREATE TABLE [英语单词] (\r\n  [ID] INTEGER NOT NULL PRIMARY KEY, \r\n  [单词] CHAR(60), \r\n  [音标] CHAR(30), \r\n  [解释] CHAR(255), example varchar(700))')
('index', 'ID', '英语单词', 3, 'CREATE UNIQUE INDEX [ID] ON [英语单词] ([ID])')
('index', 'word', '英语单词', 4, 'CREATE INDEX [word] ON [ 英语单词] ([单词])')
('table', 'android_metadata', 'android_metadata', 2871, 'CREATE TABLE android_metadata (locale TEXT)')

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/dict.db    --nm4table:android_metadata
('en_US',)
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/dict.db    --nm4table:英语单词 =4
(1, 'a', '英 [ə; eɪ] 美 [ə; e]', 'art.一(个，件，...)', None)
(2, 'a basin of', None, '一盆…', None)
(3, 'a bill of fare', None, '菜单；节目单', None)
(4, 'a bit', None, '有点儿;有一点儿', None)
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/dict.db    --nm4table:英语单词 =4 --condition:'example NOT NULL'
(91, 'abacus', "英 ['æbəkəs] 美 ['æbəkəs]", 'n. 算盘', 'I can use abacus skillfully.\n    我会熟练地打算盘。\n    The clerk reckoned the expenditure last week with an abacus.\n    那位职员用算盘将上周的花销计算出来。')
(92, 'abandon', "英 [ə'bænd(ə)n] 美 [ə'bændən]", 'v. 放弃, 遗弃,沉溺', 'The cruel man abandoned his wife and child.\n    那个狠心的男人抛弃了他的妻儿。\n    They had abandoned all hope.\n    他们已经放弃了一切希望。')
(104, 'abatement', "英 [ə'beɪtm(ə)nt] 美 [ə'betmənt]", 'n. 减少,减轻,缓和', 'A noise abatement notice is served on the club.\n    向俱乐部发停止大声喧哗的通知。')
(109, 'abbreviate', "英 [ə'briːvɪeɪt] 美 [ə'brivɪ'et]", 'v. 缩写,使...简略', "In writing, the title 'Doctor' is abbreviated to 'Dr'.\n    在书写时, Doctor头衔的缩写是Dr.")


英语单词(ID,单词,音标,解释,example)
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd \
 '%!may2smay=lambda m:(str(m) if m else "")' \
 '%!std4NL_=lambda s:(s.replace("\r\n", "\n").replace("\r", "\n"))' \
 '%!strips=lambda s:("\n".join(map(str.strip,s.split("\n"))))' \
 '%!s_=lambda s:(strips(std4NL_(may2smay(s))).replace("\n", "\n/"))' \
 --ipath:/sdcard/0my_files/unzip/apk/dictionary/com.xiaoqiang.dictionary/dict.db \
 --nm4table:英语单词 \
 --nms4columns:单词,ID,音标,解释,example \
 --fmtr4row='(lambda 单词,ID,音标,解释,example:f",{单词}\n:{ID}:{s_(音标)}\n:{s_(解释)}\n:{s_(example)}")' \
 --opath:/sdcard/0my_files/tmp/out4py/英语词霸囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt


view /sdcard/0my_files/tmp/out4py/英语词霸囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
]]



#]]]'''
__all__ = r'''
'''.split()#'''
__all__


from script.英语词霸囗 import *
