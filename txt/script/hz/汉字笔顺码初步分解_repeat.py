#__all__:goto
r'''[[[
e script/hz/汉字笔顺码初步分解_repeat.py

[[[
生成并还原29685-ex6.txt
===
程序:
view script/hz/汉字笔顺码初步分解_repeat.py
    view script/hz/汉字笔顺码初步分解__save_20230423.py
view ../../python3_src/bash_script/app/patch_o
    patch
===
输入:
view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表\[20200913]/stroke-seq_MB-master\[汉字笔顺表]\[20200827]/单字_笔顺码_29685个.txt
    原版
view ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
    原版
view script/hz/patchs429685-ex6.txt/29685-ex6--diff--orgnl-vs-repeat-2.txt
    补丁
===
步骤:
py_adhoc_call   script.hz.汉字笔顺码初步分解_repeat   @main4repeat =2 :../笔顺码分解/29685-ex6--repeat-2.txt +笔顺码相同的部首再聚类 +启用囗局部部件替换 --启用共同双缀当作部首笔顺码的最小区规模=4
patch_o -ib ../笔顺码分解/29685-ex6--repeat-2.txt  -ip ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt -o ../笔顺码分解/29685-ex6--5patch--repeat-2.txt -R
diff  ../笔顺码分解/29685-ex6.txt   ../笔顺码分解/29685-ex6--5patch--repeat-2.txt
    same
===
view ../笔顺码分解/29685-ex6--5patch--repeat-2.txt
]]]

script.hz.汉字笔顺码初步分解_repeat
py -m nn_ns.app.debug_cmd   script.hz.汉字笔顺码初步分解_repeat -x
py -m nn_ns.app.doctest_cmd script.hz.汉字笔顺码初步分解_repeat:__doc__ -ff -v
py_adhoc_call   script.hz.汉字笔顺码初步分解_repeat   @f
from script.hz.汉字笔顺码初步分解_repeat import *






[[
前提:已还原:
view ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
    是 原版

重复生成ex6
py_adhoc_call  script.hz.汉字笔顺码初步分解   @main1 :../笔顺码分解/29685-ex6--repeat-1.txt +笔顺码相同的部首再聚类 +启用囗局部部件替换 --启用共同双缀当作部首笔顺码的最小区规模=4
失败:部件拆分更正囗:
    assert bk2f_bks[bk] in (old_f_bks, may_new_f_bks), (bk, bk2f_bks[bk], old_f_bks, may_new_f_bks)
AssertionError: ('囗', ('d/t', ['⺆', '㇐']), ('d/t', ['[无钩冂自部首⺆]', '㇐']), ('c_null', []))
]]



[[
前提:已还原:
view ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
覆盖:
script.hz.汉字笔顺码初步分解.load = load__between_load_and_load_with_patch
===
py_adhoc_call   script.hz.汉字笔顺码初步分解_repeat   @main1 :../笔顺码分解/29685-ex6--repeat-1.txt +笔顺码相同的部首再聚类 +启用囗局部部件替换 --启用共同双缀当作部首笔顺码的最小区规模=4
失败:
    ts = 区首字到区[区首字]
KeyError: '㼝'
===
++前提:覆盖:
script.hz.汉字笔顺码初步分解.load = load__between_load_and_load_with_patch
script.hz.汉字笔顺码初步分解.load_with_patch = load__between_load_and_load_with_patch
:
失败:
    囗打补丁囗(hz2js, nm8bk2js__patch_1)
AttributeError: 'mappingproxy' object has no attribute 'setdefault'
===
++前提:覆盖:
script.hz.汉字笔顺码初步分解.load_with_patch = _load_with_patch
:
失败:
    smay_lcp, lcs = a_b.split('_')
AttributeError: 'list' object has no attribute 'split'
===
++前提:更正:script.hz.汉字笔顺码初步分解:加『,_』
            if '_' in js_:
                a_b,_ = js_.split('-')
                smay_lcp, lcs = a_b.split('_')
:
ok!
===
diff ../笔顺码分解/29685-ex6.txt ../笔顺码分解/29685-ex6--repeat-1.txt
有点多

===
++前提:覆盖:
script.hz.汉字笔顺码初步分解.load_with_patch = load_with_patch_ #还原
script.hz.汉字笔顺码初步分解.部件拆分更正囗 = dummy_部件拆分更正囗
失败:
    assert a or b, (a,b,(lcp,lcs),js, ts[:5])
AssertionError: (0, 0, ('', ''), '122132511212151534354', [('d', ['卝', '夒'], '122132511212151534354', '蘷'), ('d', ['卝', '扌'], '2121112', '𦍋'), ('d', ['卝', 38407], '2121121354', '羐'), ('d', ['卝', '隹'], '212132411121', '雈'), ('d', ['卝', '句'], '212135251', '茍')])
===
++前提:覆盖:
script.hz.汉字笔顺码初步分解.load_with_patch = load_with_patch_ #还原
script.hz.汉字笔顺码初步分解.部件拆分更正囗 = _部件拆分更正囗
py_adhoc_call   script.hz.汉字笔顺码初步分解_repeat   @main1 :../笔顺码分解/29685-ex6--repeat-2.txt +笔顺码相同的部首再聚类 +启用囗局部部件替换 --启用共同双缀当作部首笔顺码的最小区规模=4
:
ok!
===
diff ../笔顺码分解/29685-ex6.txt ../笔顺码分解/29685-ex6--repeat-2.txt
diff ../笔顺码分解/29685-ex6--repeat-1.txt ../笔顺码分解/29685-ex6--repeat-2.txt

]]
[[
now:using main4repeat()
    main1 --> main1_
===
!cp script/hz/汉字笔顺码初步分解.py script/hz/汉字笔顺码初步分解__save_20230423.py
===
py_adhoc_call   script.hz.汉字笔顺码初步分解_repeat   @main4repeat =1 :../笔顺码分解/29685-ex6--repeat-1.txt +笔顺码相同的部首再聚类 +启用囗局部部件替换 --启用共同双缀当作部首笔顺码的最小区规模=4
===
py_adhoc_call   script.hz.汉字笔顺码初步分解_repeat   @main4repeat =2 :../笔顺码分解/29685-ex6--repeat-2.txt +笔顺码相同的部首再聚类 +启用囗局部部件替换 --启用共同双缀当作部首笔顺码的最小区规模=4
===
diff ../笔顺码分解/29685-ex6.txt ../笔顺码分解/29685-ex6--repeat-1.txt  > ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-1.txt
diff ../笔顺码分解/29685-ex6.txt ../笔顺码分解/29685-ex6--repeat-2.txt  > ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt
diff ../笔顺码分解/29685-ex6--repeat-1.txt ../笔顺码分解/29685-ex6--repeat-2.txt  > ../笔顺码分解/29685-ex6--diff--repeat-1-vs-repeat-2.txt

===
view ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-1.txt
    1442行
view ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt
    1436行
view ../笔顺码分解/29685-ex6--diff--repeat-1-vs-repeat-2.txt
    2464行
===
patch ../笔顺码分解/29685-ex6.txt -o ../笔顺码分解/29685-ex6--repeat-2--5patch.txt  -i ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt
patch: **** Can't create file ../笔顺码分解/29685-ex6--repeat-2--5patch.txt : Cross-device link

patch_o -ib ../笔顺码分解/29685-ex6.txt  -ip ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt -o ../笔顺码分解/29685-ex6--repeat-2--5patch.txt
patch: **** Can't create file ../笔顺码分解/29685-ex6--repeat-2--5patch.txt : Cross-device link
$ info
    搜索 /path
    得: realpath, readlink
$ realpath ../笔顺码分解/29685-ex6--repeat-2--5patch.txt
/storage/emulated/0/0my_files/git_repos/txt_phone/笔顺码分解/29685-ex6--repeat-2--5patch.txt
add:
opath=$( realpath "$opath" )

patch_o -ib ../笔顺码分解/29685-ex6.txt  -ip ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt -o ../笔顺码分解/29685-ex6--repeat-2--5patch.txt
    ok!
diff  ../笔顺码分解/29685-ex6--repeat-2.txt   ../笔顺码分解/29685-ex6--repeat-2--5patch.txt
    same

patch -R ../笔顺码分解/29685-ex6--repeat-2.txt  -i ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt
    !!!inpace patch without 『-o』!!!
diff ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt ../笔顺码分解/29685-ex6--5patch--repeat-2.txt
cp -n ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt ../笔顺码分解/29685-ex6--5patch--repeat-2.txt
cp -n -t ../笔顺码分解/29685-ex6--5patch--repeat-2.txt ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt

view ../笔顺码分解/29685-ex6--5patch--repeat-2.txt
===
rm ../笔顺码分解/29685-ex6--5patch--repeat-2.txt

patch_o -ib ../笔顺码分解/29685-ex6--repeat-2.txt  -ip ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt -o ../笔顺码分解/29685-ex6--5patch--repeat-2.txt -R
diff  ../笔顺码分解/29685-ex6.txt   ../笔顺码分解/29685-ex6--5patch--repeat-2.txt
    same
view ../笔顺码分解/29685-ex6--5patch--repeat-2.txt

===
du -h ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt
mkdir script/hz/patchs429685-ex6.txt/
cp ../笔顺码分解/29685-ex6--diff--orgnl-vs-repeat-2.txt -t script/hz/patchs429685-ex6.txt/
view script/hz/patchs429685-ex6.txt/29685-ex6--diff--orgnl-vs-repeat-2.txt

===

]]


#]]]'''
__all__ = r'''
'''.split()#'''
__all__


from seed.io.read_file_as_python_object import read_file_as_python_object
from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import patch__ipath_ex_, load__ipath_, patch__bk2f_bks_
if 0:
    #copy from  nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp:
  def patch__ipath_ex_(*, patch, ipath4old, encoding):
    bk2f_bks__old = load__ipath_(ipath4old, encoding=encoding)
    bk2f_bks__new = patch__bk2f_bks_(patch, bk2f_bks__old)
    return (bk2f_bks__old, bk2f_bks__new)

import script.hz.汉字笔顺码初步分解__save_20230423 as MMM
import sys
sys.modules['script.hz.汉字笔顺码初步分解'] = MMM
import script.hz.汉字笔顺码初步分解 as _MMM
assert _MMM is MMM

import script.hz.汉字笔顺码初步分解
script.hz.汉字笔顺码初步分解 = _MMM
assert script.hz.汉字笔顺码初步分解 is MMM
    #NameError: name 'script' is not defined
    #AttributeError: module 'script.hz' has no attribute '汉字笔顺码初步分解'


script.hz.汉字笔顺码初步分解.__name__ = 'script.hz.汉字笔顺码初步分解'
    #...输出文件头不同:
r'''
1c1
< #script.hz.汉字笔顺码初步分解:参数: {'双缀延长正错比例': 4, '双缀延长错字上限': 5, '启用共同双缀当作部首笔顺码的最小区规模': 4, '启用囗局部部件替换': True, '笔顺码相同的部首再聚类': True}
---
> #script.hz.汉字笔顺码初步分解__save_20230423:参数: {'双缀延长正错比例': 4, '双缀延长错字上限': 5, '启用共同双缀当作 部首笔顺码的最小区规模': 4, '启用囗局部部件替换': True, '笔顺码相同的部首再聚类': True}
'''#'''

from pathlib import Path
from script.hz.汉字笔顺码初步分解 import (main1 as main1_
    , load as load_
    , load_with_patch as load_with_patch_
    , 部件拆分更正囗 as 部件拆分更正囗_
    )

def main4repeat(ver, /, *args, **kwargs):
    globals()[f'prepare4repeat__ver_{ver}']()
    main1_(*args, **kwargs)

#yyy#del script.hz.汉字笔顺码初步分解.load
#yyy#script.hz.汉字笔顺码初步分解.load = load__between_load_and_load_with_patch
#yyy#script.hz.汉字笔顺码初步分解.load_with_patch = _load_with_patch
#==>> prepare4repeat__ver_1
#yyy#script.hz.汉字笔顺码初步分解.load_with_patch = load_with_patch_ #还原
#yyy#script.hz.汉字笔顺码初步分解.部件拆分更正囗 = dummy_部件拆分更正囗
#yyy#script.hz.汉字笔顺码初步分解.load_with_patch = load_with_patch_ #还原
#yyy#script.hz.汉字笔顺码初步分解.部件拆分更正囗 = _部件拆分更正囗
#==>> prepare4repeat__ver_2
def prepare4repeat__ver_1():
    script.hz.汉字笔顺码初步分解.load = load__between_load_and_load_with_patch
    script.hz.汉字笔顺码初步分解.load_with_patch = _load_with_patch

def prepare4repeat__ver_2():
    script.hz.汉字笔顺码初步分解.load = load__between_load_and_load_with_patch
    script.hz.汉字笔顺码初步分解.部件拆分更正囗 = _部件拆分更正囗






#yyy#del script.hz.汉字笔顺码初步分解.load
def load__between_load_and_load_with_patch():
    'load() between load_() load_with_patch()'
    ipath4patch = Path(__file__).parent/'patchs4cjk-decomp-0.4.0.txt/patch-20230422-cjk-decomp-0.4.0.txt'
    encoding = 'u8'
    # view script/hz/patchs4cjk-decomp-0.4.0.txt/patch-20230422-cjk-decomp-0.4.0.txt
    patch = read_file_as_python_object(ipath4patch, encoding=encoding)

    [hz2js#汉字到笔顺码
    ,bk2f_bks#部件到字型零件
    ] = load_()
    bk2f_bks__old = bk2f_bks


    bk2f_bks__new = patch__bk2f_bks_(patch, bk2f_bks__old)

    return hz2js, bk2f_bks__new
def _load_with_patch():
    [hz2js#汉字到笔顺码
    ,bk2f_bks#部件到字型零件
    ] = load_()
    hz2js = dict(hz2js)
    return hz2js, bk2f_bks
def _load_with_patch_2():
    [hz2js#汉字到笔顺码
    ,bk2f_bks#部件到字型零件
    ] = load_()
    hz2js = dict(hz2js)
    部件拆分更正囗(bug_hz_set, bk2f_bks)
    部件笔顺码更正囗(bug_hz_set, bk2js)
    全局部件替换囗(bk2js, bk2f_bks)
    return hz2js, bk2f_bks
#yyy#script.hz.汉字笔顺码初步分解.load = load__between_load_and_load_with_patch
#yyy#script.hz.汉字笔顺码初步分解.load_with_patch = _load_with_patch

def dummy_部件拆分更正囗(bug_hz_set, bk2f_bks, /):pass
#yyy#script.hz.汉字笔顺码初步分解.load_with_patch = load_with_patch_ #还原
#yyy#script.hz.汉字笔顺码初步分解.部件拆分更正囗 = dummy_部件拆分更正囗

def _部件拆分更正囗(bug_hz_set, bk2f_bks, /):
    mmm = script.hz.汉字笔顺码初步分解
    d = mmm.部件拆分更正表囗单个囗数据
    #del d['㼝']
    ls = d; del d
    if 0:
        for a,b in ls:
            if a=='㼝':
                print(b)
        raise
    p = ('㼝', (('d', ['夘', '瓦']), ('d', ['夗', '瓦'])))
    del ls[ls.index(p)]
    mmm.否决囗囗双缀还可能延长囗字集 = mmm.否决囗囗双缀还可能延长囗字集.replace('廵', '')
    mmm.整区不拆囗原首字囗字集 = mmm.整区不拆囗原首字囗字集.replace('扌', '').replace('羐', '')
    部件拆分更正囗_(bug_hz_set, bk2f_bks)
#yyy#script.hz.汉字笔顺码初步分解.load_with_patch = load_with_patch_ #还原
#yyy#script.hz.汉字笔顺码初步分解.部件拆分更正囗 = _部件拆分更正囗


from script.hz.汉字笔顺码初步分解_repeat import *
