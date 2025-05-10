#__all__:goto
#[:示例纟窜改冫书架备份文件纟轻阅]:goto
r'''[[[
e script/窜改冫备份文件纟轻阅.py

script.窜改冫备份文件纟轻阅
py -m nn_ns.app.debug_cmd   script.窜改冫备份文件纟轻阅 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.窜改冫备份文件纟轻阅:__doc__ -ht # -ff -df

[[
源起:
    view others/app/usage/阅读.txt
    因为更换手机后，导入本地小说时，总是自动退出，所以需得手动窜改备份文件再从窜改后的备份文件恢复app状态。
copy from:
    view others/app/usage/阅读.txt
===
内容缓存路径:
  /storage/emulated/0/Android/data/com.gedoor.monkeybook/files/
备份路径:
  /storage/emulated/0/0my_files/tmp/xxx/
6个文件:
    config.xml myTxtChapterRule.json myBookReplaceRule.json myBookSearchHistory.json myBookSource.json myBookShelf.json
窜改流程:
  打包xxx/6个文件
  打包xxx/auto/  #6个文件 即是 所有文件
  app->点击备份
  打包xxx/6个文件
  打包xxx/auto/  #6个文件 即是 所有文件
  窜改xxx/6个文件
  app->点击恢复
    需等十几秒，直至显示成功信息
    另外:finalDate,finalRefreshData影响排序，所以可能没有置顶#另外:时间单位是秒
打包命令:实例:
    tar -cvJf auto-20250421-12-20.xz auto/
    tar -cvJf 手动备份后6文件-20250421-12-33.xz {config.xml,myTxtChapterRule.json,myBookReplaceRule.json,myBookSearchHistory.json,myBookSource.json,myBookShelf.json}
===

]]
[[
[轻阅app <: 阅读app]
<<==:
view others/app/app.txt
  阅读 @com.gedoor.monkeybook
      官网:https://github.com/gedoor/MyBookshelf
  轻阅 @com.feng.monkeybook
]]
[[
copy from:
    view others/app/usage/阅读.txt
===
@20250421
内容缓存路径:
  /storage/emulated/0/Android/data/com.gedoor.monkeybook/files/
备份路径:
  /storage/emulated/0/0my_files/tmp/xxx/
  <==>
  content://com.android.externalstorage.documents/tree/primary%3A0my_files%2Ftmp%2Fxxx
view /sdcard/0my_files/tmp/xxx/阅读app备份json/README.txt
cd /storage/emulated/0/0my_files/tmp/xxx/
cd /storage/emulated/0/0my_files/tmp/xxx/auto/
ls -t --time=mtime --full-time -g
  --full-time
    但多了『-l』
    时间的显示格式:=full-iso
ls -t --time=atime --time-style=full-iso -g
ls -t --time=birth --time-style=full-iso -g
ls -t --time=ctime --time-style=full-iso -g
ls -t --time=mtime --time-style=full-iso -g
  -t
    按某种时间排序
  --time=mtime
    某种时间:=文件修改时间
  --time-style=full-iso
    时间的显示格式:=full-iso

.../xxx/ 之下的数据文件长期不被使用(各种时间超过两三年)
  但是:
    app->点击备份 之后:
    .../xxx/6个文件被更新:
        config.xml myTxtChapterRule.json myBookReplaceRule.json myBookSearchHistory.json myBookSource.json myBookShelf.json
    .../xxx/auto/0个文件被更新:
        <None>
  可见.../xxx/手动备份
.../xxx/auto 之下的文件超过半天不被使用
  !! 各文件各时间大约都是:2025-04-20 17:56:15, 而命令执行时间为:@20250421-12:11
  可见.../xxx/auto/定时自动备份

6个文件:
    config.xml myTxtChapterRule.json myBookReplaceRule.json myBookSearchHistory.json myBookSource.json myBookShelf.json
窜改流程:
  打包xxx/6个文件
  打包xxx/auto/  #6个文件 即是 所有文件
  app->点击备份
  打包xxx/6个文件
  打包xxx/auto/  #6个文件 即是 所有文件
  窜改xxx/6个文件
  app->点击恢复
    需等十几秒，直至显示成功信息
    另外:finalDate,finalRefreshData影响排序，所以可能没有置顶#另外:时间单位是秒

cd /storage/emulated/0/0my_files/tmp/xxx/
tar -cvJf auto-20250421-12-20.xz auto/
du -h auto
  5.0M
du -h auto-20250421-12-20.xz
  336K

tar -cvJf 手动备份后6文件-20250421-12-33.xz {config.xml,myTxtChapterRule.json,myBookReplaceRule.json,myBookSearchHistory.json,myBookSource.json,myBookShelf.json}
du -h 手动备份后6文件-20250421-12-33.xz
  340K


]]
[[
窜改相关信息:
copy from:
    view others/app/usage/阅读.txt
===

>>> import time
>>> time.time_ns()    #doctest: +SKIP
1745211624197272583

  vs:1745211624197272583    纳秒
  vs:1745194242985          秒
>>> time.ctime(1745194242985)
'Sun Jan  1 18:36:25 57273'

>>> time.time()    #doctest: +SKIP
1745226507.8925745
>>> time.time_ns()    #doctest: +SKIP
1745226514488257503
>>> time.localtime()    #doctest: +SKIP
time.struct_time(tm_year=2025, tm_mon=4, tm_mday=21, tm_hour=17, tm_min=9, tm_sec=4, tm_wday=0, tm_yday=111, tm_isdst=0)
>>> time.localtime(1745226507.8925745)
time.struct_time(tm_year=2025, tm_mon=4, tm_mday=21, tm_hour=17, tm_min=8, tm_sec=27, tm_wday=0, tm_yday=111, tm_isdst=0)
>>> time.strftime('%Y%m%d-%H:%M:%S', time.localtime(1745226507.8925745))
'20250421-17:08:27'

######################
#开始:示例:myBookShelf.json
######################
[
  {
    "allowUpdate": false,
    "bookInfoBean": {
      "author": "",
      "coverUrl": "",
      "finalRefreshData": 1627443350000,
      "name": "《道德经",
      "noteUrl": "/storage/emulated/0/20220614_copy5sd__0my_files/book_txt/小说天堂txt/重命名/小说天堂txt-1/《《道德经》全文及译文》.txt",
      "origin": "本地",
      "tag": "loc_book"
    },
    "chapterListSize": 136,
    "durChapter": 101,
    "durChapterName": "\r\n\n\t四十三章",
    "durChapterPage": 0,
    "finalDate": 1745194242985,
    "finalRefreshData": 1631334465773,
    "group": 3,
    "hasUpdate": false,
    "isLoading": false,
    "lastChapterName": "\r\n\n\t八十一章",
    "newChapters": 0,
    "noteUrl": "/storage/emulated/0/20220614_copy5sd__0my_files/book_txt/小说天堂txt/重命名/小说天堂txt-1/《《道德经》全文及译文》.txt",
    "replaceEnable": false,
    "serialNumber": 0,
    "tag": "loc_book",
    "useReplaceRule": true
  },
  {
    "allowUpdate": false,
    "bookInfoBean": {
      "author": "姬叉",
      "coverUrl": "",
      "finalRefreshData": 1622129798000,
      "name": "问道红尘(仙子请自重)",
      "noteUrl": "/storage/emulated/0/20220614_copy5sd__0my_files/novel/3/《问道红尘(仙子请自重)》（校对版全本）作者：姬叉.txt",
      "origin": "本地",
      "tag": "loc_book"
    },
    "chapterListSize": 0,
    "durChapter": 0,
    "durChapterPage": 0,
    "finalDate": 1624404904911,
    "finalRefreshData": 1624404904911,
    "group": 3,
    "hasUpdate": true,
    "isLoading": false,
    "newChapters": 0,
    "noteUrl": "/storage/emulated/0/20220614_copy5sd__0my_files/novel/3/《问道红尘(仙子请自重)》（校对版全本）作者：姬叉.txt",
    "replaceEnable": false,
    "serialNumber": 0,
    "tag": "loc_book",
    "useReplaceRule": true
  },
  {
    "allowUpdate": false,
    "bookInfoBean": {
      "author": "府天",
      "coverUrl": "",
      "finalRefreshData": 1565347472000,
      "name": "公子千秋",
      "noteUrl": "/storage/emulated/0/0my_files/novel/《公子千秋》（校对版全本）作者：府天.txt",
      "origin": "本地",
      "tag": "loc_book"
    },
    "chapterListSize": 815,
    "durChapter": 62,
    "durChapterName": "第六十章 鹤鸣轩里小过堂",
    "durChapterPage": 0,
    "finalDate": 1613696297901,
    "finalRefreshData": 1612760482602,
    "group": 3,
    "hasUpdate": false,
    "isLoading": false,
    "lastChapterName": "番外六 老刘",
    "newChapters": 0,
    "noteUrl": "/storage/emulated/0/0my_files/novel/《公子千秋》（校对版全本）作者：府天.txt",
    "replaceEnable": false,
    "serialNumber": 0,
    "tag": "loc_book",
    "useReplaceRule": true
  },
  {
    "allowUpdate": false,
    "bookInfoBean": {
      "author": "再入江湖",
      "coverUrl": "",
      "finalRefreshData": 1612880284000,
      "name": "纵横天下从铁布衫开始",
      "noteUrl": "/storage/emulated/0/0my_files/novel/《纵横天下从铁布衫开始》（校对版全本）作者：再入江湖.txt",
      "origin": "本地",
      "tag": "loc_book"
    },
    "chapterListSize": 522,
    "durChapter": 521,
    "durChapterName": "第五百二十一章 新的传说（大结局）",
    "durChapterPage": 58,
    "finalDate": 1613628671031,
    "finalRefreshData": 1612881022477,
    "group": 3,
    "hasUpdate": false,
    "isLoading": false,
    "lastChapterName": "第五百二十一章 新的传说（大结局）",
    "newChapters": 0,
    "noteUrl": "/storage/emulated/0/0my_files/novel/《纵横天下从铁布衫开始》（校对版全本）作者：再入江湖.txt",
    "replaceEnable": false,
    "serialNumber": 0,
    "tag": "loc_book",
    "useReplaceRule": true
  }
]
######################
#结束:示例:myBookShelf.json
######################


######################
#开始:本地新书入架模板:myBookShelf.json
#   变量: <时间> <文件路径> <书名> <作者名>
######################
  {
    "allowUpdate": false,
    "bookInfoBean": {
      "author": "<作者名>",
      "coverUrl": "",
      "finalRefreshData": <时间>,
      "name": "<书名>",
      "noteUrl": "<文件路径>",
      "origin": "本地",
      "tag": "loc_book"
    },
    "chapterListSize": 0,
    "durChapter": 0,
    "durChapterPage": 0,
    "finalDate": <时间>,
    "finalRefreshData": <时间>,
    "group": 3,
    "hasUpdate": true,
    "isLoading": false,
    "newChapters": 0,
    "noteUrl": "<文件路径>",
    "replaceEnable": false,
    "serialNumber": 0,
    "tag": "loc_book",
    "useReplaceRule": true
  },
######################
#结束:本地新书入架模板:myBookShelf.json
######################


]]

>>> from seed.for_libs.for_tempfile import Path, mk_temp_dir_ctx_
>>> init_json = '[\n  {\n  }\n]'
>>> kwds = dict(book_file_nonexist_ok=True, 欤提示窜改流程=False)
>>> with mk_temp_dir_ctx_() as tmpdir:
...     assert type(tmpdir) is str
...     p0 = Path(tmpdir)/'0tmp0.txt'
...     with open(p0, 'xt', encoding='utf8') as f0:
...         print(init_json, file=f0)
...     with open(p0, 'rt', encoding='utf8') as f0:
...         for line in f0:
...             print(repr(line))
...     print('###')
...     窜改冫书架备份文件纟轻阅扌(path4book_shelf_json=p0, infos4local_book_texts=[('x/y/z.txt', '', '', 233), ('a/b/c.txt', '', '', 999)], **kwds)
...     窜改冫书架备份文件纟轻阅扌(path4book_shelf_json=p0, infos4local_book_texts=[], **kwds)
...     with open(p0, 'rt', encoding='utf8') as f0:
...         for line in f0:
...             print(repr(line))
...     print('###')
'[\n'
'  {\n'
'  }\n'
']\n'
###
'[\n'
'  {\n'
'  },\n'
'  {\n'
'    "allowUpdate": false,\n'
'    "bookInfoBean": {\n'
'      "author": "",\n'
'      "coverUrl": "",\n'
'      "finalRefreshData": 233,\n'
'      "name": "z.txt",\n'
'      "noteUrl": "x/y/z.txt",\n'
'      "origin": "本地",\n'
'      "tag": "loc_book"\n'
'    },\n'
'    "chapterListSize": 0,\n'
'    "durChapter": 0,\n'
'    "durChapterPage": 0,\n'
'    "finalDate": 233,\n'
'    "finalRefreshData": 233,\n'
'    "group": 3,\n'
'    "hasUpdate": true,\n'
'    "isLoading": false,\n'
'    "newChapters": 0,\n'
'    "noteUrl": "x/y/z.txt",\n'
'    "replaceEnable": false,\n'
'    "serialNumber": 0,\n'
'    "tag": "loc_book",\n'
'    "useReplaceRule": true\n'
'  },\n'
'  {\n'
'    "allowUpdate": false,\n'
'    "bookInfoBean": {\n'
'      "author": "",\n'
'      "coverUrl": "",\n'
'      "finalRefreshData": 999,\n'
'      "name": "c.txt",\n'
'      "noteUrl": "a/b/c.txt",\n'
'      "origin": "本地",\n'
'      "tag": "loc_book"\n'
'    },\n'
'    "chapterListSize": 0,\n'
'    "durChapter": 0,\n'
'    "durChapterPage": 0,\n'
'    "finalDate": 999,\n'
'    "finalRefreshData": 999,\n'
'    "group": 3,\n'
'    "hasUpdate": true,\n'
'    "isLoading": false,\n'
'    "newChapters": 0,\n'
'    "noteUrl": "a/b/c.txt",\n'
'    "replaceEnable": false,\n'
'    "serialNumber": 0,\n'
'    "tag": "loc_book",\n'
'    "useReplaceRule": true\n'
'  }\n'
']'
###
>>> with open(p0, 'rt', encoding='utf8') as f0:pass  #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
FileNotFoundError: ...



######################
py_adhoc_call   script.窜改冫备份文件纟轻阅   @窜改冫书架备份文件纟轻阅扌  -book_file_nonexist_ok +欤提示窜改流程  --path4book_shelf_json:'/sdcard/0my_files/tmp/xxx/myBookShelf.json'  --infos4local_book_texts='[("/sdcard/0my_files/tmp/xxx/myBookShelf.json/nonexist_file",)]'
FileNotFoundError: /sdcard/0my_files/tmp/xxx/myBookShelf.json/nonexist_file

######################
#[:示例纟窜改冫书架备份文件纟轻阅]:here
######################
echo $'[\n  {\n  }\n]' > /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp
[
  {
  }
]

view /sdcard/0my_files/git_repos/txt_phone/txt/古籍整理/道德经/道德经-1.txt
py_adhoc_call   script.窜改冫备份文件纟轻阅   @窜改冫书架备份文件纟轻阅扌  -book_file_nonexist_ok +欤提示窜改流程  --path4book_shelf_json:'/sdcard/0my_files/tmp/0tmp'  --infos4local_book_texts='[("/sdcard/0my_files/git_repos/txt_phone/txt/古籍整理/道德经/道德经-1.txt",), ("/sdcard/0my_files/git_repos/txt_phone/txt/古籍整理/道德经/道德经-1.txt", "", "老子 著；王弼 注")]'
view /sdcard/0my_files/tmp/0tmp
[
  {
  },
  {
    "allowUpdate": false,
    "bookInfoBean": {
      "author": "",
      "coverUrl": "",
      "finalRefreshData": 1745258422,
      "name": "道德经-1.txt",
      "noteUrl": "/sdcard/0my_files/git_repos/txt_phone/txt/古籍整理/道德经/道德经-1.txt",
      "origin": "本地",
      "tag": "loc_book"
    },
    "chapterListSize": 0,
    "durChapter": 0,
    "durChapterPage": 0,
    "finalDate": 1745258422,
    "finalRefreshData": 1745258422,
    "group": 3,
    "hasUpdate": true,
    "isLoading": false,
    "newChapters": 0,
    "noteUrl": "/sdcard/0my_files/git_repos/txt_phone/txt/古籍整理/道德经/道德经-1.txt",
    "replaceEnable": false,
    "serialNumber": 0,
    "tag": "loc_book",
    "useReplaceRule": true
  },
  {
    "allowUpdate": false,
    "bookInfoBean": {
      "author": "老子 著；王弼 注",
      "coverUrl": "",
      "finalRefreshData": 1745258422,
      "name": "道德经-1.txt",
      "noteUrl": "/sdcard/0my_files/git_repos/txt_phone/txt/古籍整理/道德经/道德经-1.txt",
      "origin": "本地",
      "tag": "loc_book"
    },
    "chapterListSize": 0,
    "durChapter": 0,
    "durChapterPage": 0,
    "finalDate": 1745258422,
    "finalRefreshData": 1745258422,
    "group": 3,
    "hasUpdate": true,
    "isLoading": false,
    "newChapters": 0,
    "noteUrl": "/sdcard/0my_files/git_repos/txt_phone/txt/古籍整理/道德经/道德经-1.txt",
    "replaceEnable": false,
    "serialNumber": 0,
    "tag": "loc_book",
    "useReplaceRule": true
  }
]
######################


实例:成功:py_adhoc_call   script.窜改冫备份文件纟轻阅   @窜改冫书架备份文件纟轻阅扌  -book_file_nonexist_ok +欤提示窜改流程  --path4book_shelf_json:'/sdcard/0my_files/tmp/xxx/myBookShelf.json'  --infos4local_book_texts='[("/sdcard/0my_files/git_repos/txt_phone/txt/古籍整理/道德经/道德经-2.txt",)]'

from script.窜改冫备份文件纟轻阅 import *
]]]'''#'''
__all__ = r'''
窜改冫书架备份文件纟轻阅扌
    模板纟入架本地新书
str2json_str_content_
构造冫列表纟打包命令纟备份文件纟轻阅
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...


from seed.tiny_.check import check_type_is, check_int_ge
from math import floor
from io import SEEK_END
from pathlib import PurePath, Path
import json
import time
#.from itertools import islice
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

模板纟入架本地新书 = '''\
  {
    "allowUpdate": false,
    "bookInfoBean": {
      "author": "<作者名>",
      "coverUrl": "",
      "finalRefreshData": <时间>,
      "name": "<书名>",
      "noteUrl": "<文件路径>",
      "origin": "本地",
      "tag": "loc_book"
    },
    "chapterListSize": 0,
    "durChapter": 0,
    "durChapterPage": 0,
    "finalDate": <时间>,
    "finalRefreshData": <时间>,
    "group": 3,
    "hasUpdate": true,
    "isLoading": false,
    "newChapters": 0,
    "noteUrl": "<文件路径>",
    "replaceEnable": false,
    "serialNumber": 0,
    "tag": "loc_book",
    "useReplaceRule": true
  }\
'''#'''
    #由于打算追附文件之后，所以最后的『,』被去掉，很可能前置(但若是第一项，则无需)
    #str2json_str_content_()=>取消:由于『"』可能出现在参数中，故而去掉双引号？...

def str2json_str_content_(s, /):
    check_type_is(str, s)
    sss = json.dumps(s, ensure_ascii=False)
    if not sss[0] == sss[-1] == '"':raise Exception(s, sss)
    return sss[1:-1]
######################
def 构造冫列表纟打包命令纟备份文件纟轻阅(path4cache_dir4book_shelf_app, prefix4archive, /):
    path = str2json_str_content_(PurePath(path4cache_dir4book_shelf_app).as_posix())
    if '$' in path:raise NotImplementedError
    formatted_str = time.strftime('%Y%m%d-%H_%M_%S', time.localtime())
    assert len(prefix4archive.split()) == 1
    cmd0 = f'tar -cvJf "{path}"/{prefix4archive}-手动备份区六文件-{formatted_str}.xz -C "{path}" {{config.xml,myTxtChapterRule.json,myBookReplaceRule.json,myBookSearchHistory.json,myBookSource.json,myBookShelf.json}}'
    cmd1 = f'tar -cvJf "{path}"/{prefix4archive}-定时备份区六文件-{formatted_str}.xz -C "{path}" auto/{{config.xml,myTxtChapterRule.json,myBookReplaceRule.json,myBookSearchHistory.json,myBookSource.json,myBookShelf.json}}'
    cmds = (cmd0, cmd1)
    return cmds

def 窜改冫书架备份文件纟轻阅扌(*, book_file_nonexist_ok:bool, 欤提示窜改流程:bool, infos4local_book_texts, path4book_shelf_json='/sdcard/0my_files/tmp/xxx/myBookShelf.json', may_time_fmt=None, local_vs_utc__or__tz=False, encoding4book_shelf_json='utf8'):
    r'''[[[
    :: infos4local_book_texts/(Iter info4local_book_text) -> path4book_shelf_json
    [info4local_book_text == (tuple(path4book_text, smay_name4book, smay_author4book, smay_timestamp4insert/(timestamp{seconds}/(int|float)|formatted_str{time_fmt,tz}/str)))]
        #formatted_str:see: seed.for_libs.for_time.timestamp5formatted_str__via_datetime__()
    #]]]'''#'''
    check_type_is(bool, book_file_nonexist_ok)
    check_type_is(bool, 欤提示窜改流程)
    check_type_is(str, encoding4book_shelf_json)
    ######################
    if not encoding4book_shelf_json=='utf8':
        if not (__:='[]  {},\r\n').encode(encoding4book_shelf_json) == __.encode('ascii'):raise Exception(encoding4book_shelf_json)
    ######################
    if isinstance(infos4local_book_texts, (str, bytes, bytearray, PurePath)): raise TypeError(type(infos4local_book_texts))
    iter(infos4local_book_texts)
    ######################
    path4book_shelf_json = Path(path4book_shelf_json)
    if not (path4book_shelf_json.is_file()):raise FileNotFoundError(path4book_shelf_json)
    path4cache_dir4book_shelf_app = path4book_shelf_json.parent
    ######################
    from seed.text.replace_substrings__simultaneously import replace_substrings__simultaneously__str
    #def replace_substrings__simultaneously__str(sub_repl_pairs, txt, /):

    #view ../../python3_src/seed/for_libs/for_time.py
    from seed.for_libs.for_time import timestamp5formatted_str__via_datetime__, get_now__timestamp
    #def timestamp5formatted_str__via_datetime__(may_time_fmt, local_vs_utc__or__tz, formatted_str, /, ):
    #    'may time_fmt/str -> tz4default/(local_vs_utc/bool | tz/tzinfo) -> formatted_str<tz4default,smay_utcoffset>/str -> timestamp<platform_epoch>/float'


    ######################
    def 提示打包(前缀纟打包文件, /):
        列表纟打包命令 = 构造冫列表纟打包命令纟备份文件纟轻阅(path4cache_dir4book_shelf_app, 前缀纟打包文件)
        多行文本纟打包命令 = '\n'.join(列表纟打包命令)
        input(f'\n窜改流程:打包命令:\n{多行文本纟打包命令}\n#(手动执行以上命令行，或者跳过)')
    ######################
    def main():
        ls4bs8info = list(map(h, infos4local_book_texts))
        if not ls4bs8info:
            return
        ######################
        if 欤提示窜改流程:
            提示打包('点击备份前')
            input('\n窜改流程:app->点击备份 # (需等十几秒，直至显示成功信息)')
            提示打包('点击备份后')
        ######################

        ######################
        _sz = 8
            # b'[\n  {'
            # b'}\r\n]\r\n' ==>> 6BYTE
        assert _sz > 0
        with open(path4book_shelf_json, 'r+b') as ibfile:
            old_file_sz = ibfile.tell()
            ibfile.seek(-_sz, SEEK_END)
            addr4neg_sz = ibfile.tell()
            bs = ibfile.read()
            assert len(bs) == _sz and (b'{}'[1:] in bs), (bs, 'empty json???')
            # [not empty json]
            # [current book will not be the first record in book_shelf]
            b'{';   j0 = bs.rindex(b'}')
            j1 = bs.rindex(b']')
            assert j0 < j1
            #.addr4overwrite = addr4neg_sz+j1
            #.ibfile.seek(addr4overwrite)
            #.if not b'[]'[1:] == ibfile.read(1):raise 000
            #.ibfile.seek(addr4overwrite)
            #.# !! [current book will not be the first record in book_shelf]
            #.#ibfile.write(b',')
            #.    # b'['
            #.    # overwrite b']' --> b','
            addr4overwrite = addr4neg_sz+j0+1
            ibfile.seek(addr4overwrite-1)
            if not b'{}'[1:] == ibfile.read(1):raise 000
            if not addr4overwrite == ibfile.tell():raise 000

            for bs8info in ls4bs8info:
                ibfile.write(b',\n')
                    # b'['
                    # !! [current book will not be the first record in book_shelf]
                    # at first round:overwrite b'\n]' --> b',\n'
                ibfile.write(bs8info)
            ibfile
            if not ibfile.tell() == addr4overwrite:
                b'[';   ibfile.write(b'\n]')
            ibfile
        ######################
        if 欤提示窜改流程:
            input('\n窜改流程:app->点击恢复 # (需等十几秒，直至显示成功信息)')
        ######################
        return
    ######################
    def h(info4local_book_text, /):
        check_type_is(tuple, info4local_book_text)
        (path4book_text, name4book, smay_author4book, timestamp4insert) = f(*info4local_book_text)
        return g(path4book_text, name4book, smay_author4book, timestamp4insert)
    ######################
    def g(path4book_text, name4book, smay_author4book, timestamp4insert, /):
        #模板纟入架本地新书
        pairs = (
        [('<文件路径>', str2json_str_content_(path4book_text))
        , ('<书名>', str2json_str_content_(name4book))
        , ('<作者名>', str2json_str_content_(smay_author4book))
        , ('<时间>', str(timestamp4insert))
        ])
        s = replace_substrings__simultaneously__str(pairs, 模板纟入架本地新书)
        return s.encode(encoding=encoding4book_shelf_json)
        return s.encode('utf8')
    ######################
    def f(path4book_text, smay_name4book='', smay_author4book='', smay_timestamp4insert='', /):
        #check_type_is(str, path4book_text)
        path4book_text = Path(path4book_text)
        check_type_is(str, smay_name4book)
        check_type_is(str, smay_author4book)
        if type(smay_timestamp4insert) in (int, float):
            timestamp = smay_timestamp4insert
        else:
            check_type_is(str, smay_timestamp4insert)
            if smay_timestamp4insert == '':
                timestamp = get_now__timestamp()
            else:
                formatted_str = smay_timestamp4insert
                timestamp = timestamp5formatted_str__via_datetime__(may_time_fmt, local_vs_utc__or__tz, formatted_str)
            timestamp
        timestamp
        timestamp4insert = floor(timestamp)
        name4book = path4book_text.name if smay_name4book == '' else smay_name4book
        if not book_file_nonexist_ok:
            if not (path4book_text.is_file()):raise FileNotFoundError(path4book_text)
        path4book_text = path4book_text.as_posix()
        return (path4book_text, name4book, smay_author4book, timestamp4insert)
    ######################
    return main()

__all__
from script.窜改冫备份文件纟轻阅 import *
