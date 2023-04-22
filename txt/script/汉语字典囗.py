#__all__:goto
r'''[[[
e script/汉语字典囗.py
主要输出:
    view /sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
    view /sdcard/0my_files/tmp/out4py/古汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt


script.汉语字典囗
py -m nn_ns.app.debug_cmd   script.汉语字典囗 -x
py -m nn_ns.app.doctest_cmd script.汉语字典囗:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd script.汉语字典囗!
py_adhoc_call   script.汉语字典囗   @f
from script.汉语字典囗 import *


[[
汉语字典:
du -h /sdcard/0my_files/apk/学习查询/hugh.android.app.zidian_5.13.24.apk_
15M
hexdump /sdcard/0my_files/apk/学习查询/hugh.android.app.zidian_5.13.24.apk_ -C -n 0x100 -s 0x0
00000000  50 4b 03 04 14 00 08 08  08 00 d2 85 3e 4d 00 00  |PK..........>M..|
00000010  00 00 00 00 00 00 00 00  00 00 14 00 00 00 4d 45  |..............ME|
00000020  54 41 2d 49 4e 46 2f 4d  41 4e 49 46 45 53 54 2e  |TA-INF/MANIFEST.|
00000030  4d 46 8c bd c7 ce eb 58  92 35 3a 6f a0 df a1 86  |MF.....X.5:o....|
==>>:
  zip文件

mkdir ../../../unzip/apk/dictionary/han_yu_zi_dian/
cd ../../../unzip/apk/dictionary/han_yu_zi_dian/
7z l /sdcard/0my_files/apk/学习查询/hugh.android.app.zidian_5.13.24.apk_
7z x /sdcard/0my_files/apk/学习查询/hugh.android.app.zidian_5.13.24.apk_
很多ogg
/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/resources.arsc
du -h /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/resources.arsc
80K
du -b /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/resources.arsc
77828
view ++enc=utf16le /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/resources.arsc
hexdump /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/resources.arsc -C -n 0x100 -s 77604
00012fc4  08 00 00 00 b5 02 00 00  08 00 00 12 00 00 00 00  |................|
00012fd4  08 00 00 00 b6 02 00 00  08 00 00 12 00 00 00 00  |................|
00012fe4  08 00 00 00 b7 02 00 00  08 00 00 12 00 00 00 00  |................|
00012ff4  08 00 00 00 b8 02 00 00  08 00 00 12 00 00 00 00  |................|
00013004

cd /sdcard/0my_files/unzip/apk/dictionary/
hexdump /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x0 -C -n 0x100 -s 0
00000000  53 51 4c 69 74 65 20 66  6f 72 6d 61 74 20 33 00  |SQLite format 3.|
hexdump /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x1 -C -n 0x100 -s 0
du -b  /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x3
407552
hexdump /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x3 -C -n 0x100 -s 407300
du -b  /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x*
1000K   /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x0
1000K   /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x1
1000K   /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x2
400K    /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x3
加起来 3.4M??
du -b  /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x*
1024000 /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x0
1024000 /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x1
1024000 /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x2
407552  /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x3
(407552+3*1024000)/1024/1024 == 3.3

发现已解包:
du -h /sdcard/hugh.android/GHY.DAT
2.4M
  vs 3.3 ??不太对
  不对！这是 古汉语APP！
hexdump /sdcard/hugh.android/GHY.DAT -C -n 0x100 -s 0
00000000  53 51 4c 69 74 65 20 66  6f 72 6d 61 74 20 33 00  |SQLite format 3.|

du -b /sdcard/hugh.android/GHY.DAT
2483200
hexdump /sdcard/hugh.android/GHY.DAT -C -n 0x100 -s 2483000
e ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py



=====

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT =6
    [[
BEGIN TRANSACTION;
CREATE TABLE android_metadata(locale text);
INSERT INTO "android_metadata" VALUES('zh_CN');
CREATE TABLE ghy_yunghugh (
_id INTEGER primary key,
zi text,
yinjie text,
bs text,
bsbh text,
zbh text,
bsh text,
shiyi text);
INSERT INTO "ghy_yunghugh" VALUES(13,'丰','feng','丨','1','4','1112','fēng
①<形>容貌丰满而美好。《林黛玉进贾府》：“第一个肌肤微～,合中身材。”
②<形>茂盛;繁茂。《观沧海》：“树木丛生,百草～茂。”
③<名>风度；神态。李好古《张生煮海》：“则见他正色端容，道貌 仙～。”
④<形>丰收。《西江月》：“稻花香里说～年。”
⑤<形>富足；富裕。《训俭示康》：“小人寡欲则能谨身节用，远罪 ～家。”');
INSERT INTO "ghy_yunghugh" VALUES(14,'中','zhong','丨','1','4','2512','zhōng
①<名>内；里。《狼》：“一屠晚归，担～肉尽。”
②<名>中间；内部。《石钟山记》：“有大石当～流。”
③<形>半；一半。《乐羊子妻》：“若～道而归，何异断斯织乎。”
④<形>中等；不高，不低。《邹忌讽齐王纳谏》：“上书谏寡人者， 受～赏。”
⑤<名>内心。《史记·韩安国列传》：“深～隐厚。”
⑥<名>中国。《图画》：“图画之设彩者，用水彩，～外所同也。”

zhòng
①<动>符合。《劝学》：“木直中绳，輮以为轮，其曲～规。”
②<动>射中。《卖油翁》：“见其矢十～八九。”
③<动>击中。《荆轲刺秦王》：“乃引其匕首提秦王，不～。”
④<动>考中。《范时中举》：“你恭喜～了举人。”
⑤<动>猜中。《醉翁亭记》：“射者～，弈者胜。”
⑥<动>中伤。《书博鸡者事》：“臧怒，欲～守法。”

【中肠】内心。
【中人】⒈平常人。⒉朝中公卿大臣。⒊指宦官；太监。⒋宫女。
【中节】适度。
【中式】⒈科举考试被录取。⒉符合规格。');
    ]]

CREATE TABLE ghy_yunghugh (
_id INTEGER primary key,
zi text,
yinjie text,
bs text,
bsbh text,
zbh text,
bsh text,
shiyi text);
INSERT INTO "ghy_yunghugh" VALUES(...);
COMMIT;

GHY.DAT==gyh_yunghugh.awb
ghy_yunghugh(_id, zi, yinjie, bs, bsbh, zbh, bsh, shiyi)
(字，音节，部首，部首笔画数，字笔画数，笔顺编号/笔顺码，释义)

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT --opath:/sdcard/0my_files/tmp/out4py/nn_ns.fileformat.sqlite3_dump_cmd.古汉语字典._dump.out.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.fileformat.sqlite3_dump_cmd.古汉语字典._dump.out.txt
\r\n
#已重命名:mv /sdcard/0my_files/tmp/out4py/nn_ns.fileformat.sqlite3_dump_cmd.汉语字典._dump.out.txt /sdcard/0my_files/tmp/out4py/nn_ns.fileformat.sqlite3_dump_cmd.古汉语字典._dump.out.txt

#builtin table
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:sqlite_master
('table', 'android_metadata', 'android_metadata', 2, 'CREATE TABLE android_metadata(locale text)')
('table', 'ghy_yunghugh', 'ghy_yunghugh', 3, 'CREATE TABLE ghy_yunghugh (\r\n_id INTEGER primary key,\r\nzi text,\r\nyinjie text,\r\nbs text,\r\nbsbh text,\r\nzbh text,\r\nbsh text,\r\nshiyi text)')


#userdef table
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:ghy_yunghugh =600 =602
(1881, '诗', 'shi', '讠', '2', '8', '45121124', 'shī\r\n①< 名>一种文学体裁；诗歌。《孔雀东南飞》：“时人伤之，为～云尔 。”\r\n②<名>指《诗经》。《齐桓晋文之事》：“～云：‘他人有心 ，予忖度之。’”\r\n\r\n【诗馀】词的别称。')
(1882, '试', 'shi', '讠', '2', '8', '45112154', 'shì\r\n①< 动>用；任用。《礼记·乐记》：“兵革不～，五刑不用。”\r\n②<动>尝试；试探。《世态炎凉》：“守邸曰：‘～来视之。’”\r\n③<动>试验；检验。《促织》：“又～之鸡，果如成言。”\r\n④<动>考试。《左忠毅公逸事》：“及～，吏呼名史公，公瞿然注视。”\r\n\r\n【 试守】犹言试用。在正在任用之前试用。')



py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:ghy_yunghugh   --opath:/sdcard/0my_files/tmp/out4py/nn_ns.fileformat.sqlite3_dump_cmd.汉语字典.dump.GHY_DAT.out.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.fileformat.sqlite3_dump_cmd.汉语字典.dump.GHY_DAT.out.txt
    3932行-详解？
    不对！这是 古汉语APP！
        但 同一个字 使用相同id

=====




/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x0
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x0  --nm4table:sqlite_master
sqlite3.DatabaseError: database disk image is malformed



mkdir /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/
py -m nn_ns.app.concat_files /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/x* -o /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3


py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:sqlite_master
<==>
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   ,str.sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:sqlite_master --opath=...
<=?=> #eqv only if output row not sql_stmt # repr<T> vs str<T> for T=tuple|str
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   ,sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:sqlite_master --opath=...
('table', 'android_metadata', 'android_metadata', 2, 'CREATE TABLE android_metadata (locale TEXT)')
('table', 'zi', 'zi', 3, 'CREATE TABLE zi (id INTEGER primary key autoincrement,zi TEXT,py TEXT,wubi TEXT,bushou TEXT,bihua int,pinyin TEXT,jijie TEXT,xiangjie TEXT,bishun TEXT)')
('table', 'sqlite_sequence', 'sqlite_sequence', 4, 'CREATE TABLE sqlite_sequence(name,seq)')


zi(id,zi,py,wubi,bushou,bihua,pinyin,jijie,xiangjie,bishun)
字(id,字,py无音调拼音,五笔,部首,笔画,拼音,基解/基本解释,详解/详细解释,笔顺名)
    x0x1x2x3 vs 上面GHY.DAT:(字，音节，部首，部首笔画数，字笔画数，笔顺编号/笔顺码，释义)

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi =2
(1, '卝', 'guan', 'gjgd', '难检字', 4, 'guàn', '卝\nguàn\n 古代儿童将头发束成两角的样子。\n\n卝\nkuàng\n古同“矿”。', None, '2121')
(2, '羋', 'mi', 'gkgh', '难检字', 8, 'mǐ', '羋mǐ\n同“芈”。', None, '12121112')

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi =600 =602
(601, '阩', 'sheng', 'btah', '阝', 6, 'shēng', '阩shēng\n古同“升”，登上。', None, '523132')
(602, '邷', 'wa', 'gnyb', '阝', 6, 'wǎ', '邷wǎ\n古地名。\n 抓：“抛弹子，邷麽儿。”', None, '155452')

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi  --opath:/sdcard/0my_files/tmp/out4py/nn_ns.fileformat.sqlite3_dump_cmd.汉语字典.dump.x0x1x2x3.out.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.fileformat.sqlite3_dump_cmd.汉语字典.dump.x0x1x2x3.out.txt
    详解 似乎都是None
    21004行 基解

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi =4 --nms4columns:zi,xiangjie --condition:'xiangjie NOT NULL'
    无输出=>所有字 无 详解

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi =4 --nms4columns:zi,xiangjie --condition:'zi NOT NULL'
    测试SQL语句有效性
('卝', None)
('羋', None)
('羐', None)
('瑴', None)

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi =4 --nms4columns:zi --condition:'jijie IS NULL'
    部分字 无 基解
('麇',)
('\ue85f',)
('\ue859',)
('乊',)

=====

/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/sr/*
文件名:字囗笔画数
    #文件名 不是 部首囗笔画数
    {部首:[{id=,zi=,py=,bs=}]}
view /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/sr/2
{"丶":[{"id":"143","zi":"丷","py":"bā","bs":"丶"}],"丨":[{"id":"10","zi":"丩","py":"jiū","bs":"丨"}], ...}
view /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/sr/48
{"龍":[{"id":"20629","zi":"龘","py":"dá","bs":"龍"}]}
    48=16*3=龍*3





=====

cd /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/
$ ls
bdxadsdk.jar  gdt_plugin  sr  x0  x1  x2  x3
$ ls gdt_plugin/
gdtadv2.jar

7z l /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/bdxadsdk.jar
    --> classes.dex
7z l /sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian/assets/gdt_plugin/gdtadv2.jar
2018-09-07 10:45:08 .....       716088       281595  classes.dex
2018-09-07 10:45:12            1067004       419049  10 files, 73 folders

=====
后续:xxx发现已解包:
du -h /sdcard/hugh.android/GHY.DAT
2.4M
  vs 3.3 ??不太对
  不对！这是 古汉语APP！

ls /sdcard/0my_files/apk/学习查询
GuHanYu.apk_
com.afar.ele_5.0.4.apk_
com.eusoft.eudic_306.apk_
com.xiaobin.chinach_0.1.5.apk_
com.xiaoqiang.dictionary_2.9.7.apk_
hugh.android.app.zidian_5.13.24.apk_

du -h /sdcard/0my_files/apk/学习查询 -a
50M     /sdcard/0my_files/apk/学习查询/com.eusoft.eudic_306.apk_
    欧路词典
25M     /sdcard/0my_files/apk/学习查询/com.xiaobin.chinach_0.1.5.apk_
    汉语辞海
6.5M    /sdcard/0my_files/apk/学习查询/com.xiaoqiang.dictionary_2.9.7.apk_
    英语词霸
15M     /sdcard/0my_files/apk/学习查询/hugh.android.app.zidian_5.13.24.apk_
    汉语字典
1.7M    /sdcard/0my_files/apk/学习查询/GuHanYu.apk_
    古汉语
5.4M    /sdcard/0my_files/apk/学习查询/com.afar.ele_5.0.4.apk_
    电工手册
104M    /sdcard/0my_files/apk/学习查询

7z l /sdcard/0my_files/apk/学习查询/GuHanYu.apk_
2012-06-18 22:19:42 .....      1018749      1018749  assets/gyh_yunghugh.awb
2012-08-09 23:10:56            2458347      1691592  77 files


mkdir /sdcard/0my_files/unzip/apk/dictionary/GuHanYu/
cd /sdcard/0my_files/unzip/apk/dictionary/GuHanYu/
7z x /sdcard/0my_files/apk/学习查询/GuHanYu.apk_ assets/gyh_yunghugh.awb
hexdump /sdcard/0my_files/unzip/apk/dictionary/GuHanYu/assets/gyh_yunghugh.awb -C -n 0x100 -s 0
    也是zip
7z l /sdcard/0my_files/unzip/apk/dictionary/GuHanYu/assets/gyh_yunghugh.awb
2012-06-18 13:29:44 ....A      2483200      1018619  gyh_yunghugh.awb
du -b /sdcard/hugh.android/GHY.DAT
2483200
应该是同一个东西

7z x /sdcard/0my_files/unzip/apk/dictionary/GuHanYu/assets/gyh_yunghugh.awb
diff gyh_yunghugh.awb  /sdcard/hugh.android/GHY.DAT
    #same

e script/古汉语字典囗.py





=====
古汉语字典
GHY.DAT==gyh_yunghugh.awb
ghy_yunghugh(_id, zi, yinjie, bs, bsbh, zbh, bsh, shiyi)
(_id, 字，音节，部首，部首笔画数，字笔画数，笔顺编号/笔顺码，释义)
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:ghy_yunghugh --nms4columns:_id,zi,bs,bsbh,zbh,bsh,yinjie,shiyi  --fmtr4row="lambda _id,zi,bs,bsbh,zbh,bsh,yinjie,shiyi:(lambda shiyi_:f',{zi}\n:{_id}:{bs}:{bsbh}:{zbh}:{bsh}:{yinjie}\n:{shiyi_}')(shiyi.replace('\r\n', '\n').replace('\n', '\n/'))"   --opath:/sdcard/0my_files/tmp/out4py/古汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
view /sdcard/0my_files/tmp/out4py/古汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:ghy_yunghugh --nms4columns:_id,zi,bs,bsbh,zbh,bsh,yinjie,shiyi  --fmtr4row="lambda _id,zi,bs,bsbh,zbh,bsh,yinjie,shiyi:(lambda shiyi_:f',{zi}\n:{_id}:{bs}:{bsbh}:{zbh}:{bsh}:{yinjie}\n:{shiyi_}')(shiyi.replace('\r\n', '\n').replace('\n', '\n/'))" =4
,丰
:13:丨:1:4:1112:feng
:fēng
/①<形>容貌丰满而美好。《林黛玉进贾府》：“第一个肌肤微～,合中身材。”
/②<形>茂盛;繁茂。《观沧海》：“树木丛生,百草～茂。”
/③<名>风度；神态。李好古《张生煮海》：“则见他正色端容，道貌仙～。”
/④<形>丰收。《西江月》：“稻花香里说～年。”
/⑤<形>富足；富裕。《训俭示康》：“小人寡欲则能谨身节用，远罪～家。”
,中
:14:丨:1:4:2512:zhong
:zhōng
/①<名>内；里。《狼》：“一屠晚归，担～肉尽。”
/②<名>中间；内部。《石钟山记》：“有大石当～流。”
/③<形>半；一半。《乐羊子妻》：“若～道而归，何异断斯织乎。”
/④<形>中等；不高，不低。《邹忌讽齐王纳谏》：“上书谏寡人者，受～赏。”
/⑤<名>内心。《史记·韩安国列传》：“深～隐厚。”
/⑥<名>中国。《图画》：“图画之设彩者，用水彩，～外所同也。”
/
/zhòng
/①<动>符合。《劝学》：“木直中绳，輮以为轮，其曲～规。”
/②<动>射中。《卖油翁》：“见其矢十～八九。”
/③<动>击中。《荆轲刺秦王》：“乃引其匕首提秦王，不～。”
/④<动>考中。《范时中举》：“你恭喜～了举人。”
/⑤<动>猜中。《醉翁亭记》：“射者～，弈者胜。”
/⑥<动>中伤。《书博鸡者事》：“臧怒，欲～守法。”
/
/【中肠】内心。
/【中人】⒈平常人。⒉朝中公卿大臣。⒊指宦官；太监。⒋宫女。
/【中节】适度。
/【中式】⒈科举考试被录取。⒉符合规格。
,临
:22:丨:1:9:223142521:lin
:lín
/①<动>从高处向下看。《滕王阁序》：“飞阁流丹，下～无地。”
/②<动>到；靠近。《陈情表》：“州司～门，急于星火。”《观沧海》：“东～碣石，以观沧海。”
/③<动>面对；对着。《过秦论》：“据亿丈之城，～不测之渊以为固。”
/④<副>将要；快要。《出师表》：“先帝知臣谨慎，故～崩寄臣以大事也。”
/
/【临池】学习书法。
/【临存】地位高的人对下人的问候，看望。。
/【临命】将死的时候。
/【临蓐】将要分娩。
,事
:25:亅:1:8:12515112:shi
:shì
/①<名>事情。《兰亭集序》：“及其所之既倦，情随～迁，感慨系之矣。”
/②<名>特指战事。《过秦论》：“延及孝文王、庄襄王，享国之日浅，国家无～。”
/③<名>政治事务。《触龙赵太后》：“赵太后新用～。”
/④<动>从事；做。《答司马谏议书》：“如曰今日当一切不～事。”
/⑤<动>侍奉；服侍。《廉颇蔺相如列传》：“臣所以去亲戚而～君者，徒慕君之高义也。”
/⑥<量>件；样；种。郑处诲《明皇杂录》：“献白玉箫管百～。”




=====
汉语字典
x0x1x2x3
zi(id,zi,py,wubi,bushou,bihua,pinyin,jijie,xiangjie,bishun)
字(id,字,py无音调拼音,五笔,部首,笔画,拼音,基解/基本解释/maybe NULL,详解/详细解释===None,笔顺名)
    部分字 无 基解
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi --nms4columns:id,zi,bushou,bihua,bishun,wubi,py,pinyin,jijie   --fmtr4row="lambda id,zi,bushou,bihua,bishun,wubi,py,pinyin,jijie:(lambda jijie_:f',{zi}\n:{id}:{bushou}:{bihua}:{bishun}:{wubi}:{py}:{pinyin}\n:{jijie_}')('' if jijie is None else jijie.replace('\r\n', '\n').replace('\n', '\n/'))"   --opath:/sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
view /sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi --nms4columns:id,zi,bushou,bihua,bishun,wubi,py,pinyin,jijie   --fmtr4row="lambda id,zi,bushou,bihua,bishun,wubi,py,pinyin,jijie:(lambda jijie_:f',{zi}\n:{id}:{bushou}:{bihua}:{bishun}:{wubi}:{py}:{pinyin}\n:{jijie_}')('' if jijie is None else jijie.replace('\r\n', '\n').replace('\n', '\n/'))" =4
,卝
:1:难检字:4:2121:gjgd:guan:guàn
:卝
/guàn
/古代儿童将头发束成两角的样子。
/
/卝
/kuàng
/古同“矿”。
,羋
:2:难检字:8:12121112:gkgh:mi:mǐ
:羋mǐ
/同“芈”。
,羐
:3:难检字:10:2121121354:gjgy:ling:líng
:羐líng
/古同“蔆”，即“菱”。
,瑴
:4:难检字:14:12145111213554:fpgc:jue:jué
:瑴jué
/玉名：“中黄瑴玉。”
/双玉：“公为之请纳玉于王与晋侯，皆十瑴。”

TODO:格式化为: ,:

seed.io.savefile__str_tuple@std_saver4str_tuple.save_str_tuple_to_ofile_
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi --nms4columns:id,zi,bushou,bihua,bishun,wubi,py,pinyin,jijie   --fmtr4row="lambda id,zi,bushou,bihua,bishun,wubi,py,pinyin,jijie:(lambda jijie_:f',{zi}\n:{id}:{bushou}:{bihua}:{bishun}:{wubi}:{py}:{pinyin}\n:{jijie_}')(jijie.replace('\r\n', '\n').replace('\n', '\n/'))" =4





=====
=====
=====
]]




#]]]'''
__all__ = r'''
'''.split()#'''
__all__

def __():
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    if __name__ == "__main__":
        pass
__all__

from seed.io.savefile__str_tuple import SaveStrTupleAsMultiLine, std_saver4str_tuple

from script.汉语字典囗 import *
