#__all__:goto
r'''[[[
e script/hz/汉字笔顺码初步分解囗囗部件笔顺码.py

view script/hz/汉字笔顺码初步分解.py
    def 推导囗汉字部件囗笔顺码囗(opath, /, *, force=False):
        由于不限制深度，导致错误蔓延
        应当一层一层地人工解决笔顺码错误


TODO:推导出的部件笔顺码，并原有的拆分，输出为可读行格式
    show_format_lines
TODO:可读行格式:并立多种拆分、同一笔顺码不同分隔、不等价笔顺码，错误笔顺码
    _parse_line__29685_ex6_txt_
    curr line fmt:
        bk:js_ex(:js_ex)*;op,(bk,)*
[[[
===
===
===
===
du -h /storage/emulated/0/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/charts
150M
===
du -h /storage/emulated/0/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/charts-East_Asian_Scripts/
95M
===
ls /storage/emulated/0/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/charts
CodeCharts.pdf
RSIndex.pdf
Readme.txt
===
ls /storage/emulated/0/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/charts-East_Asian_Scripts/ -1
U20000.pdf
U2A700.pdf
U2B740.pdf
U2B820.pdf
U2CEB0.pdf
U2E80.pdf
U2F00.pdf
U2F800.pdf
U2FF0.pdf
U30000.pdf
U3100.pdf
U31A0.pdf
U31C0.pdf
U3400.pdf
U4E00.pdf
UF900.pdf
===
ch2nm 㧊㩛㪖
    㧊:IDEOGRAPH-39CA
    㩛:IDEOGRAPH-3A5B
    㪖:IDEOGRAPH-3A96
U3400.pdf
/sdcard/0my_files/zip/zip_selected__e_book_data/13.0.0[download_at][20200913]/charts-East_Asian_Scripts/U3400.pdf
    㧊:IDEOGRAPH-39CA#含巿 #非市
    㩛:IDEOGRAPH-3A5B#含團 #非圑
    㪖:IDEOGRAPH-3A96:G3-472F含录:T5-387C含彔
===
U3400.pdf::[3400..=4DBF] CJK Unified Ideographs Extension A
U4E00.pdf::[4E00..=9FFC] CJK Unified Ideographs
UF900.pdf::[F900..=FAFF] CJK Compatibility Ideographs
===
===
===
===
]]]


[[[
字形:一字多形:歧义
===
㪖:IDEOGRAPH-3A96:G3-472F含录:T5-387C含彔
]]]
[[[
笔顺码:一字多笔顺码:歧义
===
[[
㒊:32-53421215342121;a,亻,歰,
䔼:122-53421215342121;d,艹,歰,
53421215342121=5342121-5342121
53453421212121=534-534-2121-2121
歰:53453421212121;ra,37275,
譅:4111251-53453421212121;a,言,歰,
澀:441-53453421212121;a,氵,歰,
涩:441-5342121;a,氵,37275,
]]
[[
器:251251_251251-1344;w,㗊,犬,
嘂:251251_251251-52;w,㗊,丩,
]]
[[
𢁅:515515313112;ra,11409,
䨻:1452444425121145244442512114524444251211452444425121;r4sq,雷,
䲜:35251214444352512144443525121444435251214444;r4sq,魚,
茻:523522523522;r4sq,屮,
嚻:251251132511134251251;wa,㗊,頁,
  㗊 左右结构
囂:251251132511134251251;wd,㗊,頁,
  㗊 上下结构
]]

]]]



script.hz.汉字笔顺码初步分解囗囗部件笔顺码
py -m nn_ns.app.debug_cmd   script.hz.汉字笔顺码初步分解囗囗部件笔顺码 -x
py -m nn_ns.app.doctest_cmd script.hz.汉字笔顺码初步分解囗囗部件笔顺码:__doc__ -ff -v
from script.hz.汉字笔顺码初步分解囗囗部件笔顺码 import *








py_adhoc_call   script.hz.汉字笔顺码初步分解囗囗部件笔顺码   @main :囗单层推导部件笔顺码囗笔顺码瑕疵警惕 > ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕.out.txt
#xxx view ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕.out.txt
    #xxx see: view ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗打补丁.out.txt
    #see view ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗读编辑中文件.out.txt
e ../笔顺码分解/29685-ex6--定顶层拆分.txt
    view ../笔顺码分解/29685-ex6--定顶层拆分.第一轮修正完成.txt
e hz/歧义.txt
e script/hz/打印字符区.py

py_adhoc_call   script.hz.汉字笔顺码初步分解囗囗部件笔顺码   @main :囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗读编辑中文件  :../笔顺码分解/29685-ex6--定顶层拆分.txt  --may_start_line:===start===  --non_src_bks:⺗忄㐧㝳㡀䘮丐且世丘为主乆亊亜亞冘升及发囬夂大央失头屮手扌才斗未朱氷牛犮瓜生罒秉垂飛黽尨龙乗乘承𠄘兂可四办半坐巫夫夹平来畺疒米耳臾車𠔉𧢲戠戢貳贰㦰㦲㦳𢦏威戉戊成我䜌斑讎讟雠𥕝𧪄𦚯胤噩嚚嚻囂豳㟗幽弐㡬㢤㦱畿臧貮或武兆卿疈班亾兦囟囱囪𠧧   > ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗读编辑中文件.out.txt

view ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗读编辑中文件.out.txt



view ../笔顺码分解/29685-ex6.txt
grep '_' --before-context=1 ../笔顺码分解/29685-ex6.txt  > /sdcard/0my_files/tmp/out4grep/grep._..笔顺码分解.29685-ex6.out.txt
view  /sdcard/0my_files/tmp/out4grep/grep._..笔顺码分解.29685-ex6.out.txt
\(#\n\)\@<=
辷:_454-1;sbl,辶,㇐,
𨘀:_454-1121132511134;sbl,⻎,頊,
囯:25_1-1121;s,囗,王,
匡:1_5-1121;sl,匚,王,
衎:332_112-112;w,行,干,
褭:41_3534-1211254444;w,衣,馬,
瑴:_3554-1214511121;sr,殳,?,!#str,37047,王,
觳:_3554-1214513535112;sr,殳,?,!#str,37127,37810,
栽:121_534-1234;str,𢦏,木,
㢟:_54-215;sbl,廴,止,
廼:_54-125351;a,廴,西,
㸤:4143113_4143112-3215;w,辡,片,
驘:4152513511_354-1211254444;st,[上包围囗赢],馬,
㮟:1234_1234-13251;w,林,石,
㢽:515_515-122111;w,弜,耳,
戎:1_534-13;str,戈,𠂇,
凷:_52-121;sb,凵,土,
㻎:1_34-11211121;w,大,玨,
弌:1_54-1;str,弋,㇐,
戌:13_534-1;st,戊,㇐,
末:1_234-1;w,木,㇐,
噐:251251_251251-121;w,㗊,工,
㯻:1251245_34-135333412;d,[头囗囊],豕,木,
    xxx

py_adhoc_call   script.hz.汉字笔顺码初步分解囗囗部件笔顺码   ,stable_repr__expand_top_layer.calc_patch__29685_ex6_txt_ :../笔顺码分解/29685-ex6.txt > ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..calc_patch__29685_ex6_txt_.out.txt
view ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..calc_patch__29685_ex6_txt_.out.txt



py_adhoc_call   script.hz.汉字笔顺码初步分解囗囗部件笔顺码   @main :囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗打补丁 > ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗打补丁.out.txt
#xxx view ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗打补丁.out.txt
    #see view ../../../tmp/out4py/script.hz.汉字笔顺码初步分解囗囗部件笔顺码..main-囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗读编辑中文件.out.txt
[[
[0, 131]
121
'⺆,⺙,㇒,𠚤,𠩵,𤴡,𦍍,12203,12541,21272,37036,37060,37084,37174,37281,39068,40610,42820,46156,48555,65580,90014,91311,99697,99787'
[]
['⺗', '㐧', '㓁', '㝳', '㟗', '㡀', '㡬', '㢤', '㦱', '㨌', '㪜', '㫄', '䈠', '䏿', '䘮', '䞸', '䟫', '䢇', '䢥', '䨫', '䪟', '䰍', '丐', '且', '世', '丘', '为', '主', '乆', '义', '亊', '亜', '亞', '亡', '亾', '兆', '兦', '冘', '凢', '升', '午', '半', '卿', '及', '发', '囟', '囬', '囱', '垂', '夂', '大', '央', '失', '头', '嬲', '宀', '屮', '带', '幽', '广', '开', '弃', '弐', '忄', '或', '户', '手', '扌', '才', '敘', '敳', '斗', '未', '朱', '武', '氷', '犮', '班', '瓜', '生', '甪', '甶', '畿', '白', '秉', '罒', '羊', '羋', '羌', '羐', '聼', '聽', '育', '肻', '脊', '膂', '臧', '自', '良', '血', '貮', '車', '遙', '遥', '雟', '飛', '鰴', '黽', '鼎', '鼑', '龙', '﨤', '𠂤', '𠕇', '𠧧', '𡨴', '𢳆', '𣁋', '𣇸', '𣚺', '𤪖', '𦆮', '𦤑', '𦱳', '𧀎', '𨗈', '𨗉', '𨯿', '𨰹', '𩱳', '𪑛']
]]




#]]]'''
__all__ = r'''
'''.split()#'''
__all__

from collections import defaultdict, Counter
from seed.tiny import fmap4dict_value, group4dict_value
from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
from seed.tiny import ifNonef, ifNone, echo
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
from seed.mapping_tools.dict_op import subset_keys__immutable
from seed.mapping_tools.dict_op import mapping_symmetric_diff4patch__immutable__default, mapping_symmetric_patch4lhs__immutable__default, mapping_symmetric_patch4rhs__immutable__default


r'''[[[
def __():
    from nn_ns.CJK.CJK_data.汉字笔顺 import 汉字到笔顺码
    from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import patch__ipath_ex_, load__ipath_, patch__bk2f_bks_
    hz2js = hz2istrokes = 汉字到笔顺码
    bk2f_bks__old = load__ipath_(ipath4old, encoding=encoding)
#]]]'''#'''


def join_bks_(bks, /):
    return ','.join(map(str, bks))
if 1:
    #copy from: view script/hz/汉字笔顺码初步分解.py
    def key4bk4sort(bk, /):
        return (type(bk) is int, bk)
    def sorted__bk(bks, /):
        return sorted(bks, key=key4bk4sort)
    def load():
        #xxx#see:load_with_patch()
        from nn_ns.CJK.CJK_data.汉字笔顺 import 汉字到笔顺码
        from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import default_iter_read_cjk_decomp
        #from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import load_default, diff__bk2f_bks_, patch__bk2f_bks_
        hz2js = hz2istrokes = 汉字到笔顺码
        bk2f_bks = bk2cased_bks = dict(default_iter_read_cjk_decomp())

        cks = hz2js.keys() & bk2f_bks.keys()
        assert len(cks) == 29670
        lks = hz2js.keys() - bk2f_bks.keys()
        rks = bk2f_bks.keys() - hz2js.keys()
        assert len(lks) == 89
        assert len(rks) == 55568
        rks__hz = {x for x in rks if type(x) is str}
        rks__bk = {x for x in rks if type(x) is int}
        assert len(rks__hz) == 45081
        assert all(len(hz)==1 for hz in rks__hz)
        assert len(rks__bk) == 10487
        return hz2js, bk2f_bks
    #end-def load():


def unbox1(xs, /):
    [x] = xs
    return x
class 囗单层推导部件笔顺码囗笔顺码瑕疵警惕:
    def load(sf, /):
        bk2js__old, bk2f_bks = sf.load_()
        sf.bk2js__old, sf.bk2f_bks = bk2js__old, bk2f_bks
            #readonly
        sf.bk2js = dict(bk2js__old)
            #upatable
        sf.tgt_bk2js__acc = {}
    def deduce(sf, /):
        bk2js, bk2f_bks = sf.bk2js, sf.bk2f_bks
        (bugss, tgt_bk2js2src_bks) = sf.deduce_(bk2js, bk2f_bks)


        lens4bugss = fmapT__list(len)(bugss)
        tgt_bk2js2count = fmap4dict_value(fmapT__dict(len), tgt_bk2js2src_bks)

        tgt_bk2num_diffs = fmap4dict_value(len, tgt_bk2js2src_bks)
        tgt_bks__with_num_diffs_ge2 = join_bks_(sorted__bk(tgt_bk for tgt_bk, num_diffs in tgt_bk2num_diffs.items() if num_diffs >= 2))

        num_diffs2tgt_bk2js2src_bks = group4dict_value(len, tgt_bk2js2src_bks)
        tgt_bk2js2src_bks__unique_js = num_diffs2tgt_bk2js2src_bks.pop(1)
        tgt_bk2js = fmap4dict_value(unbox1, tgt_bk2js2src_bks__unique_js)
            #推导出的部件笔顺码

        ############################
        #tgt_bk2js2src_bks = fmap4dict_value(fmapT__dict(join_bks_), tgt_bk2js2src_bks)
        #bugss = fmapT__list(join_bks_)(bugss)
            #since:len(bks) == len(bks__str.split(','))+1

        #sf 属性赋值
        (sf.bugss, sf.tgt_bk2js2src_bks) = (bugss, tgt_bk2js2src_bks)
            #tgt_bk2js2src_bks :: {笔顺码待定的子部件:推导出来的笔顺码:[源部件]}
            #bugss :: [笔顺码未知子部件唯一囗囗推导过程异常囗囗无法确定待定子部件笔顺码的长度, 笔顺码未知子部件唯一囗囗推导结果异常囗囗笔顺码加法结果不一致, 所有子部件笔顺码已知囗囗笔顺码加法结果囗不一致]
        (sf.lens4bugss, sf.tgt_bk2js2count) = (lens4bugss, tgt_bk2js2count)
        sf.tgt_bks__with_num_diffs_ge2 = tgt_bks__with_num_diffs_ge2
            #推导出来的笔顺码有分歧的子部件列表
        sf.num_diffs2tgt_bk2js2src_bks = num_diffs2tgt_bk2js2src_bks
            #推导出来的笔顺码分歧度到子部件相关信息
        sf.tgt_bk2js2src_bks__unique_js = tgt_bk2js2src_bks__unique_js
            #推导出来的笔顺码无分歧的子部件相关信息
        sf.tgt_bk2js = tgt_bk2js
            #子部件到无分歧的推导出来的笔顺码
    def merge(sf, /):
        'bk2js |= tgt_bk2js2src_bks if len=1'
        sf.bk2js.update(sf.tgt_bk2js)
        sf.tgt_bk2js__acc.update(sf.tgt_bk2js)

    #################################
    #################################
    #################################
    def basic_load_(sf, /):
        hz2js, bk2f_bks = load()
        bk2js = hz2js
        return bk2js, bk2f_bks

    def patch_(sf, bk2js, bk2f_bks, /):
        return bk2js, bk2f_bks
    def load_(sf, /):
        bk2js, bk2f_bks = sf.basic_load_()
        bk2js, bk2f_bks = sf.patch_(bk2js, bk2f_bks)
        return bk2js, bk2f_bks

    #def is_op_ok4deuce_(sf, op, /):
        #copy from:def is_ok4try_deduce__op(op, /):
    def is_op_ok4deuce_(sf, op, tmay_bk0, /):
        #adswbrmc,lock,built
        if not tmay_bk0:
            return False
        [bk0] = tmay_bk0
        f1 = op[0]
        return (f1 in 'adsw' or (f1=='b' and op[1] in 'ad')) and not op in ['d/o', 'd/m'] and not f'{op},{bk0}' in __class__._op_bk0__ls
    _op_bk0__ls = r'''
sbl,[两点版辶]
sbl,辶
sbl,⻎
s,囗
sl,匚
w,行
w,衣
str,37047
str,37127
str,𢦏
sbl,廴
a,廴
w,辡
st,[上包围囗赢]
st,𣦼
w,林
w,弜
str,戈
sb,凵
w,大
str,弋
st,戊
w,木
w,㗊
    '''.split()#'''
    #𣦼=[上包围囗赢]

    if 0:
        def is_bk_ok4deuce__(sf, bk2js, bk2f_bks, src_bk, /):
            #see:def is_ok4try_deduce(src_bk, /):
            return bool(sf.ex_is_bk_ok4deuce__(bk2js, bk2f_bks, src_bk))
    def _is_bk_skipped4deuce_(sf, src_bk, /):
        return False
    def ex_is_bk_ok4deuce__(sf, bk2js, bk2f_bks, src_bk, /):
        '-> (-1,)|(0,)|(1,(op, dst_bks, src_js, dst_bk2count, dst_bk2may_js, tgt_bk, idc4tgt_bk))'
        #case <- {-1:笔顺码加法结果囗不一致,0:跳过,1:笔顺码未知子部件唯一}
        if sf._is_bk_skipped4deuce_(src_bk):
            # 直接跳过
            return (0,)
        op, dst_bks = bk2f_bks[src_bk]
        if not ((src_bk in bk2js) and sf.is_op_ok4deuce_(op, dst_bks[:1])):
            #skip if not satisfy precondition
            #若 源部件 没有笔顺码 或 不是 左右/上下/右上包围 等 部件次序 大概率与笔顺相同的字型布局，则 跳过
            return (0,)
        src_js = bk2js[src_bk]
        dst_bk2count = dict(Counter(dst_bks))
        dst_bk2may_js = {dst_bk:bk2js.get(dst_bk) for dst_bk in dst_bk2count}
        dst_bks__with_unknown_js = {dst_bk for dst_bk, may_js in dst_bk2may_js.items() if may_js is None}
        L = len(dst_bks__with_unknown_js)
        if L == 0:
            #所有子部件笔顺码已知，作『笔顺码』『加法』
            _js = ''.join(map(bk2js.get, dst_bks))
            if not _js == src_js:
                #笔顺码加法结果囗不一致
                return (-1,)
        if not L == 1:
            #若 超过两个子部件笔顺码未知，则 跳过
            return (0,)
        [tgt_bk] = dst_bks__with_unknown_js
        idc4tgt_bk = [i for i, _bk in enumerate(dst_bks) if _bk == tgt_bk]
        return (1, (op, dst_bks, src_js, dst_bk2count, dst_bk2may_js, tgt_bk, idc4tgt_bk))
            #笔顺码未知子部件唯一

    def deduce_(sf, bk2js, bk2f_bks, /):
        '-> (bugss, tgt_bk2js2src_bks)'
        #tgt_bk2js2count = defaultdict(lambda:defaultdict(int))
        tgt_bk2js2src_bks = defaultdict(lambda:defaultdict(list))
            #tgt_bk2js2src_bks :: {笔顺码待定的子部件:推导出来的笔顺码:[源部件]}
        bugss = [[], [], []]
            #bugss :: [笔顺码未知子部件唯一囗囗推导过程异常囗囗无法确定待定子部件笔顺码的长度, 笔顺码未知子部件唯一囗囗推导结果异常囗囗笔顺码加法结果不一致, 所有子部件笔顺码已知囗囗笔顺码加法结果囗不一致]
        for src_bk in sorted__bk(bk2f_bks):
            case, *xs = sf._1_deduce_(bk2js, bk2f_bks, src_bk)
                #result <- {(True,...):笔顺码未知子部件唯一囗囗推导结果正常, (False,-1):跳过, (False,0):笔顺码未知子部件唯一囗囗推导过程异常囗囗无法确定待定子部件笔顺码的长度, (False,1):笔顺码未知子部件唯一囗囗推导结果异常囗囗笔顺码加法结果不一致, (False,2):所有子部件笔顺码已知囗囗笔顺码加法结果囗不一致}
            if not case:
                [k] = xs
                if not k == -1:
                    bugss[k].append(src_bk)
                #else:跳过
            else:
                #笔顺码未知子部件唯一囗囗推导结果正常
                tgt_bk, tgt_js = xs
                tgt_bk2js2src_bks[tgt_bk][tgt_js].append(src_bk)

        tgt_bk2js2src_bks = fmap4dict_value(dict, tgt_bk2js2src_bks)
        return bugss, tgt_bk2js2src_bks
            #since:len(bks) == len(bks__str.split(','))+1
        tgt_bk2js2src_bks = fmap4dict_value(fmapT__dict(join_bks_), tgt_bk2js2src_bks)
        #bugss = [join_bks_(bugs) for bugs in bugss]
        bugss = fmapT__list(join_bks_)(bugss)
        return bugss, tgt_bk2js2src_bks

    def _1_deduce_(sf, bk2js, bk2f_bks, src_bk, /):
        #result <- {(True,...):笔顺码未知子部件唯一囗囗推导结果正常, (False,-1):跳过, (False,0):笔顺码未知子部件唯一囗囗推导过程异常囗囗无法确定待定子部件笔顺码的长度, (False,1):笔顺码未知子部件唯一囗囗推导结果异常囗囗笔顺码加法结果不一致, (False,2):所有子部件笔顺码已知囗囗笔顺码加法结果囗不一致}
        cased = sf.ex_is_bk_ok4deuce__(bk2js, bk2f_bks, src_bk)
            #case <- {-1:笔顺码加法结果囗不一致,0:跳过,1:笔顺码未知子部件唯一}
        case = cased[0]
        if case == 0:
            return (False, -1)
                #跳过
        if case == -1:
            return (False, 2)
                #所有子部件笔顺码已知囗囗笔顺码加法结果囗不一致
        case, x = cased
        (op, dst_bks, src_js, dst_bk2count, dst_bk2may_js, tgt_bk, idc4tgt_bk) = x
        dst_bk2len_js = {dst_bk:len(may_js) for dst_bk, may_js in dst_bk2may_js.items() if not dst_bk == tgt_bk}

        nums = len(src_js) -sum(count*dst_bk2len_js[dst_bk] for dst_bk, count in dst_bk2count.items() if not dst_bk == tgt_bk)
        cnt = dst_bk2count[tgt_bk]
        len_js4tgt_bk, r = divmod(nums, cnt)
        if not r==0:
            #bugss[0].add(src_bk)
            return (False, 0)
                #笔顺码未知子部件唯一囗囗推导过程异常囗囗无法确定待定子部件笔顺码的长度
        dst_bk2len_js[tgt_bk] = len_js4tgt_bk

        lens_js4dst_bks = [dst_bk2len_js[dst_bk] for dst_bk in dst_bks]
        i = idc4tgt_bk[0]
        len_js__pre = sum(lens_js4dst_bks[:i])
        tgt_js = src_js[len_js__pre:len_js__pre+len_js4tgt_bk]
        if 1:
            dst_bk2js = dst_bk2may_js.copy()
            dst_bk2js[tgt_bk] = tgt_js
        dst_bk2js
        dst_jss = [dst_bk2js[dst_bk] for dst_bk in dst_bks]
        if not src_js == ''.join(dst_jss):
            #bugss[1].add(src_bk)
            return (False, 1)
                #笔顺码未知子部件唯一囗囗推导结果异常囗囗笔顺码加法结果不一致
        return (True, tgt_bk, tgt_js)
                #笔顺码未知子部件唯一囗囗推导结果正常

def show_format_lines(bk2f_bks, bk2js, /):
    for line in iter_format_lines(bk2f_bks, bk2js):
        print(line)

def iter_format_lines(bk2f_bks, bk2js, /):
    #(bk2js_, bk2f_bks_) = _intersect_(bk2js, bk2f_bks)
    (bk2js_, bk2f_bks_) = (bk2js, bk2f_bks)
    for bk in sorted__bk(bk2js_):
        js = bk2js_[bk]
        if bk in bk2f_bks_:
            op, dst_bks = bk2f_bks_[bk]
            #褭:41_3534-1211254444;w,衣,馬,
            tail = ','.join(map(str, [op, *dst_bks]))
        else:
            tail = ''
        yield f'{bk!s}:{js!s};{tail!s},'

def js5ex_(js_ex, /):
    if '-' in js_ex:
        ht, bd = js_ex.split('-')
        if '_' in ht:
            h, t = ht.split('_')
            js = f'{h}{bd}{t}'
        else:
            js = f'{ht}{bd}'
    else:
        js = js_ex
    js
    assert js.isdigit(), js_ex
    return js
def js5ex_(js_ex, /):
    if not '_' in js_ex:
        jss = js_ex.split('-')
        js = ''.join(jss)
    elif '-' in js_ex:
        ht, bd = js_ex.split('-')
        if not '_' in ht:
            ht = f'{ht}_'
        if not ht.count('_') == bd.count('_') +1:raise ValueError(js_ex)
        ht_ls = ht.split('_')
        bd_ls = bd.split('_')
        assert len(ht_ls) == len(bd_ls) +1
        ss = [None]*(len(ht_ls)+len(bd_ls))
        ss[0::2] = ht_ls
        ss[1::2] = bd_ls
        js = ''.join(ss)
    else:
        js = js_ex
    js
    assert js.isdigit(), js_ex
        #Exception: 讎:32411121_32411121-4111251 ;w,雔,言,
    return js
def _parse_line__29685_ex6_txt(line, /):
    try:
        (src_bk, src_js_exs, src_js, op, dst_bks) = _parse_line__29685_ex6_txt_(line)
    except Exception as e:
        raise Exception(line) from e
        #Exception: 豳:2_52-1353334_1353334;w,山,豩,
    return (src_bk, src_js_exs, src_js, op, dst_bks)
def _parse_line__29685_ex6_txt_(line, /):
    #view ../笔顺码分解/29685-ex6.txt
    #褭:41_3534-1211254444;w,衣,馬,
    #瑴:_3554-1214511121;sr,殳,?,!#str,37047,王,
    #TODO:可读行格式:并立多种拆分、同一笔顺码不同分隔、不等价笔顺码，错误笔顺码
    #curr line fmt:
    #   bk:js_ex(:js_ex)*;op,(bk,)*
    line = line.strip()
    assert line
    assert not line[0] == '#'
    assert line[-1] == ','
        #㬆:2511-515152511;a,日,昬
    src_bk, _, s = line.partition(':')
    #src_js_ex, _, s = s.partition(';')
    src_js_exs__str, _, s = s.partition(';')
    src_js_exs = src_js_exs__str.split(':')
    _, _, op_dst_bks__str = s.rpartition('!#')
    op, *dst_bks = op_dst_bks__str[:-1].split(',')
    dst_bks = [(int if bk[0].isdigit() else echo)(bk) for bk in dst_bks]
    #src_js = js5ex_(src_js_ex)
    [src_js, *src_js_ls] = map(js5ex_, src_js_exs)
    for _src_js in src_js_ls:
        if not _src_js == src_js: raise Exception(line, src_js, _src_js)
    #return (src_bk, src_js_ex, src_js, op, dst_bks)
    return (src_bk, src_js_exs, src_js, op, dst_bks)
def _iter_parse_lines__29685_ex6_txt(lines, /):
    for line in lines:
        if not line:continue
        h = line[0]
        #bug:if h == '#' or h.isalpha():continue
        if h == '#' or 'a' <= h <= 'z':continue

        (src_bk, src_js_exs, src_js, op, dst_bks) = _parse_line__29685_ex6_txt(line)
        yield (src_bk, src_js_exs, src_js, op, dst_bks)
def _parse_lines__29685_ex6_txt(lines, /):
    bk2js = {}
    bk2f_bks = {}
    for (src_bk, src_js_exs, src_js, op, dst_bks) in _iter_parse_lines__29685_ex6_txt(lines):
        assert not src_bk in bk2js, src_bk
            #猤
        bk2js[src_bk] = src_js
        bk2f_bks[src_bk] = op, dst_bks
    return bk2js, bk2f_bks
def _intersect_(bk2js, bk2f_bks, /):
    common_bks = bk2js.keys() & bk2f_bks.keys()
    bk2js_ = subset_keys__immutable(bk2js, common_bks)
    bk2f_bks_ = subset_keys__immutable(bk2f_bks, common_bks)
    assert bk2js_.keys() == bk2f_bks_.keys()
    return (bk2js_, bk2f_bks_)
def _calc_patch__29685_ex6_txt_(bk2js, bk2f_bks, lines, /):
    (bk2js_, bk2f_bks_) = _intersect_(bk2js, bk2f_bks)
    0;   del bk2js, bk2f_bks
    assert bk2js_.keys() == bk2f_bks_.keys()

    _bk2js, _bk2f_bks = _parse_lines__29685_ex6_txt(lines)
    assert _bk2js.keys() == _bk2f_bks.keys()
    #print_err(len(_bk2js))

    patch4bk2js = mapping_symmetric_diff4patch__immutable__default(bk2js_, _bk2js)
    patch4bk2f_bks = mapping_symmetric_diff4patch__immutable__default(bk2f_bks_, _bk2f_bks)

    if 1:
        __bk2js = mapping_symmetric_patch4lhs__immutable__default(patch4bk2js, bk2js_)
        assert __bk2js == _bk2js
    if 1:
        __bk2f_bks = mapping_symmetric_patch4lhs__immutable__default(patch4bk2f_bks, bk2f_bks_)
        assert __bk2f_bks == _bk2f_bks
    return (patch4bk2js, patch4bk2f_bks)
def calc_patch__29685_ex6_txt_(ipath4_29685_ex6_txt, /):
    bk2js, bk2f_bks = load()
    with open(ipath4_29685_ex6_txt, 'rt', encoding='utf8') as fin:
        lines = iter(fin)
        (patch4bk2js, patch4bk2f_bks) = _calc_patch__29685_ex6_txt_(bk2js, bk2f_bks, lines)
    return (patch4bk2js, patch4bk2f_bks)



class 囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗读编辑中文件(囗单层推导部件笔顺码囗笔顺码瑕疵警惕):
    #ipath = '../笔顺码分解/29685-ex6--定顶层拆分.txt'
    #start_line = '===start==='
    #non_src_bks = '⺗忄㐧㝳㡀䘮丐且世丘为主乆亊亜亞冘升及发囬夂大央失头屮手扌才斗未朱氷牛犮瓜生罒秉垂飛黽尨龙乗乘承𠄘兂可四办半坐巫夫夹平来畺疒米耳臾車𠔉𧢲戠戢貳贰㦰㦲㦳𢦏威戉戊成我䜌斑讎讟雠𥕝𧪄𦚯胤噩嚚嚻囂豳㟗幽弐㡬㢤㦱畿臧貮或武兆卿疈班亾兦囟囱囪𠧧'
    def __init__(sf, ipath, /, *, may_start_line=None, non_src_bks=''):
        sf.ipath = ipath
        sf.may_start_line = may_start_line
        sf.non_src_bks = set(non_src_bks)
            #hz;uint;[人工部件名]
    def iter_lines5ipath_(sf, /):
        ipath4_29685_ex6_txt = sf.ipath
        with open(ipath4_29685_ex6_txt, 'rt', encoding='utf8') as fin:
            lines = iter(fin)
            m = sf.may_start_line
            if not m is None:
                start_line = m
                for line in lines:
                    if line.strip() == start_line:
                        break
                else:
                    raise ValueError(f'not found start_line: {start_line!r}')
                lines
            lines
            yield from lines
    #@override
    def patch_(sf, bk2js, bk2f_bks, /):
        lines = sf.iter_lines5ipath_()
        _bk2js, _bk2f_bks = _parse_lines__29685_ex6_txt(lines)
        _3_bk2js = {**bk2js, **_bk2js}
        _3_bk2f_bks = {**bk2f_bks, **_bk2f_bks}
        return _3_bk2js, _3_bk2f_bks
    #@override
    def _is_bk_skipped4deuce_(sf, src_bk, /):
        return src_bk in sf.non_src_bks
class 囗单层推导部件笔顺码囗笔顺码瑕疵警惕囗打补丁(囗单层推导部件笔顺码囗笔顺码瑕疵警惕):
    #笔顺码补丁: {'[上包围囗赢]': '4152513511354', '[头囗囊]': '125124534', '[头囗坚]': '2254', '[头囗擊]': '1251112523554', '[头囗桨]': '412354', '[头囗璺]': '321125125151145', '[头囗觉]': '44345', '[头囗餐]': '2135454', '[头囗黎]': '31234353', '[左囗郎]': '451154', '[左囗颐]': '1225125', '[断足鳥]': '3251115', '[横组户攵]': '45133134', '[横组氵氵]': '441441', '[纵三组亠口冖]': '4125145', '[纵组士冖]': '12145', '[纵组艹冖]': '12245', '⺍': '443', '⺤': '3443', '⺹': '1213', '⺼': '3541', '⻎': '454', '㇠': '5', '䍃': '3443311252', '厭': '13251125111344', '穴': '44534', '耒': '111234', '飠': '34451154', '龺': '12251112', '𤇾': '4334433445'}
    #部件替换表: {37004: '飠', 37009: '耒', 37021: '䍃', 37027: '𤇾', 37044: '[头囗觉]', 37063: '[头囗黎]', 37069: '厭', 37105: '[左囗郎]', 37106: '[纵三组亠口冖]', 37144: '[头囗坚]', 37147: '[头囗璺]', 37151: '[纵组士冖]', 37157: '[断足鳥]', 37165: '[纵组艹冖]', 37194: '[头囗桨]', 47005: '[头囗囊]', 65737: '穴', 97020: '龺', 97147: '[横组氵氵]', '𢼄': '[横组户攵]', '𣎆': '[上包围囗赢]', '𣦼': '[头囗餐]', '𣪠': '[头囗擊]', '𦣞': '[左囗颐]'}
    def patch_(sf, bk2js, bk2f_bks, /):
        (bk2js_, bk2f_bks_) = _intersect_(bk2js, bk2f_bks)
        #0;   del bk2js, bk2f_bks
        _2_bk2js = mapping_symmetric_patch4lhs__immutable__default(__class__.patch4bk2js, bk2js_)
        _2_bk2f_bks = mapping_symmetric_patch4lhs__immutable__default(__class__.patch4bk2f_bks, bk2f_bks_)
        _3_bk2js = {**bk2js, **_2_bk2js}
        return _3_bk2js, _2_bk2f_bks
    #see:calc_patch__29685_ex6_txt_
    patch4bk2js = (
{'[上包围囗赢]'
: (1, '4152513511354')
,'[头囗囊]'
: (1, '125124534')
,'[头囗坚]'
: (1, '2254')
,'[头囗尝]'
: (1, '24345')
,'[头囗擊]'
: (1, '1251112523554')
,'[头囗桨]'
: (1, '412354')
,'[头囗璺]'
: (1, '321125125151145')
,'[头囗觉]'
: (1, '44345')
,'[头囗餐]'
: (1, '2135454')
,'[头囗黎]'
: (1, '31234353')
,'[左囗郎]'
: (1, '451154')
,'[左囗颐]'
: (1, '1225125')
,'[断足鳥]'
: (1, '3251115')
,'[横组亻丨]'
: (1, '322')
,'[横组户攵]'
: (1, '45133134')
,'[横组未攵]'
: (1, '112343134')
,'[横组氵氵]'
: (1, '441441')
,'[纵三组亠口冖]'
: (1, '4125145')
,'[纵组士冖]'
: (1, '12145')
,'[纵组艹冖]'
: (1, '12245')
,'⺍'
: (1, '443')
,'⺤'
: (1, '3443')
,'⺹'
: (1, '1213')
,'⺼'
: (1, '3541')
,'⻎'
: (1, '454')
,'㇠'
: (1, '5')
,'\ue815'
: (1, '33')
,'\ue816'
: (1, '13')
,'\ue817'
: (1, '31')
,'\ue818'
: (1, '5')
,'\ue819'
: (1, '5')
,'\ue81a'
: (1, '323552335523')
,'\ue81b'
: (1, '3235511')
,'\ue81c'
: (1, '35')
,'\ue81d'
: (1, '55')
,'\ue81e'
: (1, '54')
,'\ue81f'
: (1, '2512512534')
,'\ue820'
: (1, '2512511251151221113134')
,'\ue821'
: (1, '25142551221113134')
,'\ue822'
: (1, '243')
,'\ue823'
: (1, '2444')
,'\ue824'
: (1, '4423552335523')
,'\ue825'
: (1, '44235511')
,'\ue826'
: (1, '3113')
,'\ue827'
: (1, '1212534')
,'\ue828'
: (1, '12144115')
,'\ue829'
: (1, '121324111213241112154')
,'\ue82a'
: (1, '1215454')
,'\ue82b'
: (1, '1121')
,'\ue82c'
: (1, '1221')
,'\ue82d'
: (1, '12342534')
,'\ue82e'
: (1, '1354251212534')
,'\ue82f'
: (1, '441134454')
,'\ue830'
: (1, '3121')
,'\ue831'
: (1, '11134')
,'\ue832'
: (1, '24345')
,'\ue833'
: (1, '52121')
,'\ue834'
: (1, '25111431234531')
,'\ue835'
: (1, '3123454134333')
,'\ue836'
: (1, '314314')
,'\ue837'
: (1, '55125121')
,'\ue838'
: (1, '4535')
,'\ue839'
: (1, '431113')
,'\ue83a'
: (1, '431121')
,'\ue83b'
: (1, '121534')
,'\ue83c'
: (1, '111234252215425113535')
,'\ue83d'
: (1, '1112342522112154')
,'\ue83e'
: (1, '51121')
,'\ue83f'
: (1, '35111154')
,'\ue840'
: (1, '1224453453')
,'\ue841'
: (1, '45234251212511134')
,'\ue842'
: (1, '45234251212534')
,'\ue843'
: (1, '431134')
,'\ue844'
: (1, '453312')
,'\ue845'
: (1, '451221251211354444')
,'\ue846'
: (1, '251113411212511')
,'\ue847'
: (1, '253411212511')
,'\ue848'
: (1, '2512121')
,'\ue849'
: (1, '341124314513541541')
,'\ue84a'
: (1, '311151523')
,'\ue84b'
: (1, '3111553544')
,'\ue84c'
: (1, '311154513541541')
,'\ue84d'
: (1, '3111512212132511')
,'\ue84e'
: (1, '31115431112431251')
,'\ue84f'
: (1, '3111525111251113241112154')
,'\ue850'
: (1, '251125113434121')
,'\ue851'
: (1, '25112511355112')
,'\ue852'
: (1, '4253434121')
,'\ue853'
: (1, '425355112')
,'\ue854'
: (1, '12251112')
,'\ue855'
: (1, '4334433445')
,'\ue856'
: (1, '215315352512113134')
,'\ue857'
: (1, '3525121135152')
,'\ue858'
: (1, '35251211111342511')
,'\ue859'
: (1, '35251211431253511')
,'\ue85a'
: (1, '215315352512144443134')
,'\ue85b'
: (1, '351143113435251211')
,'\ue85c'
: (1, '125235451')
,'\ue85d'
: (1, '41343435451')
,'\ue85e'
: (1, '13542235451')
,'\ue85f'
: (1, '1121251135451')
,'\ue860'
: (1, '25111134435451')
,'\ue861'
: (1, '332153153535451')
,'\ue862'
: (1, '513251414311235451')
,'\ue863'
: (1, '135341134')
,'\ue864'
: (1, '4111251554444554444')
,'郎'
: (1, '451153452')
,'凉'
: (1, '4141251234')
,'秊'
: (1, '31234312')
,'裏'
: (1, '4125112113534')
,'隣'
: (1, '52431234354152')
,'兀'
: (1, '135')
,'嗀'
: (1, '1214512513554')
,'礼'
: (1, '112345')
,'蘒'
: (1, '1223123432511255115115341')
})
    patch4bk2f_bks = (
{'[上包围囗赢]'
: (1, ('d', ['吂', '䏎']))
,'[头囗囊]'
: (1, ('d/t', [65522, '⺆']))
,'[头囗坚]'
: (1, ('a', [37255, '又']))
,'[头囗尝]'
: (1, ('', []))
,'[头囗擊]'
: (1, ('a', ['𨊥', '殳']))
,'[头囗桨]'
: (1, ('a', ['丬', '夕']))
,'[头囗璺]'
: (1, ('d', [99846, '冖']))
,'[头囗觉]'
: (1, ('d', ['⺍', '冖']))
,'[头囗餐]'
: (1, ('a', ['歺', '又']))
,'[头囗黎]'
: (1, ('a', ['禾', 99972]))
,'[左囗郎]'
: (1, ('wt', [37084, '㇔']))
,'[左囗颐]'
: (1, ('sl', ['匚', 38231]))
,'[断足鳥]'
: (1, ('w', [37398, '㇐']))
,'[横组亻丨]'
: (1, ('wr', ['亻', '㇑']))
,'[横组户攵]'
: (1, ('a', ['户', '⺙']))
,'[横组未攵]'
: (1, ('a', ['未', '⺙']))
,'[横组氵氵]'
: (1, ('ra', ['氵']))
,'[纵三组亠口冖]'
: (1, ('d', [37045, '冖']))
,'[纵组士冖]'
: (1, ('d', ['士', '冖']))
,'[纵组艹冖]'
: (1, ('d', ['艹', '冖']))
,'⺍'
: (1, ('msp', [37543]))
,'⺤'
: (1, ('mt', ['爪']))
,'⺹'
: (1, ('mtl', ['𠥼']))
,'⺼'
: (1, ('st', ['⺆', '亠']))
,'⻎'
: (1, ('d/t', [99702, '㇝']))
,'㇠'
: (1, ('c', []))
,'㛑'
: (3, (('d', ['𣦼', '女']), ('d', ['[头囗餐]', '女'])))
,'㠾'
: (3, (('d', ['夘', '巾']), ('d', ['夗', '巾'])))
,'㥎'
: (3, (('d', ['䄪', '心']), ('d', ['[头囗黎]', '心'])))
,'㪵'
: (3, (('a', ['半', '斗']), ('a', ['[撇化半]', '斗'])))
,'㫩'
: (3, (('d', ['卉', '日']), ('d', ['[头囗桒]', '日'])))
,'㯱'
: (3, (('d', [47005, '缶', '木']), ('d', ['[头囗囊]', '缶', '木'])))
,'㯻'
: (3, (('d', [47005, '豕', '木']), ('d', ['[头囗囊]', '豕', '木'])))
,'㰆'
: (3, (('d', [47005, '棐']), ('d', ['[头囗囊]', '棐'])))
,'㱘'
: (3, (('d', [37069, '止']), ('d', ['厭', '止'])))
,'㲦'
: (3, (('a', [97020, 12016]), ('a', ['龺', 12016])))
,'㳲'
: (3, (('a', [97147, '太']), ('a', ['[横组氵氵]', '太'])))
,'㴢'
: (3, (('a', [97147, '仲']), ('a', ['[横组氵氵]', '仲'])))
,'㴣'
: (3, (('a', [97147, '夷']), ('a', ['[横组氵氵]', '夷'])))
,'㴺'
: (3, (('a', [97147, '夾']), ('a', ['[横组氵氵]', '夾'])))
,'㵈'
: (3, (('a', [97147, '姑']), ('a', ['[横组氵氵]', '姑'])))
,'㵉'
: (3, (('a', [97147, '林']), ('a', ['[横组氵氵]', '林'])))
,'㵜'
: (3, (('a', [97147, '南']), ('a', ['[横组氵氵]', '南'])))
,'㶂'
: (3, (('a', [97147, '黄']), ('a', ['[横组氵氵]', '黄'])))
,'㶃'
: (3, (('a', [97147, '無']), ('a', ['[横组氵氵]', '無'])))
,'㶙'
: (3, (('a', [97147, 25284]), ('a', ['[横组氵氵]', 25284])))
,'㶝'
: (3, (('a', [97147, '應']), ('a', ['[横组氵氵]', '應'])))
,'㶳'
: (3, (('d', ['聿', '火']), ('d', ['[断尾聿]', '火'])))
,'㶾'
: (3, (('d', ['西', '灭']), ('d', ['覀', '灭'])))
,'㸨'
: (3, (('a', ['牛', '𠂈']), ('a', ['牜', '𠂈'])))
,'㸩'
: (3, (('a', ['牛', '干']), ('a', ['牜', '干'])))
,'㸪'
: (3, (('a', ['牛', '川']), ('a', ['牜', '川'])))
,'㸫'
: (3, (('a', ['牛', '斤']), ('a', ['牜', '斤'])))
,'㸬'
: (3, (('a', ['牛', '市']), ('a', ['牜', '市'])))
,'㸭'
: (3, (('a', ['牛', '巴']), ('a', ['牜', '巴'])))
,'㸮'
: (3, (('a', ['牛', '分']), ('a', ['牜', '分'])))
,'㸯'
: (3, (('a', ['牛', '斗']), ('a', ['牜', '斗'])))
,'㸰'
: (3, (('a', ['牛', '它']), ('a', ['牜', '它'])))
,'㸱'
: (3, (('a', ['牛', '㐌']), ('a', ['牜', '㐌'])))
,'㸲'
: (3, (('a', ['牛', '乍']), ('a', ['牜', '乍'])))
,'㸳'
: (3, (('a', ['牛', '令']), ('a', ['牜', '令'])))
,'㸵'
: (3, (('a', ['牛', '吉']), ('a', ['牜', '吉'])))
,'㸶'
: (3, (('a', ['牛', '因']), ('a', ['牜', '因'])))
,'㸸'
: (3, (('a', ['牛', '后']), ('a', ['牜', '后'])))
,'㸹'
: (3, (('a', ['牛', 65196]), ('a', ['牜', 65196])))
,'㸻'
: (3, (('a', ['牛', '矣']), ('a', ['牜', '矣'])))
,'㸼'
: (3, (('a', ['牛', '夆']), ('a', ['牜', '夆'])))
,'㸽'
: (3, (('a', ['牛', '貝']), ('a', ['牜', '貝'])))
,'㸾'
: (3, (('a', ['牛', '忍']), ('a', ['牜', '忍'])))
,'㸿'
: (3, (('a', ['牛', 44634]), ('a', ['牜', 44634])))
,'㹀'
: (3, (('a', ['牛', '孛']), ('a', ['牜', '孛'])))
,'㹁'
: (3, (('a', ['牛', '京']), ('a', ['牜', '京'])))
,'㹄'
: (3, (('a', ['牛', 39176]), ('a', ['牜', 39176])))
,'㹅'
: (3, (('a', ['牛', '怱']), ('a', ['牜', '怱'])))
,'㹆'
: (3, (('a', ['牛', '軍']), ('a', ['牜', '軍'])))
,'㹇'
: (3, (('a', ['牛', '曷']), ('a', ['牜', '曷'])))
,'㹉'
: (3, (('a', ['牛', '原']), ('a', ['牜', '原'])))
,'㹊'
: (3, (('a', ['牛', '隺']), ('a', ['牜', '隺'])))
,'㹋'
: (3, (('a', ['牛', '修']), ('a', ['牜', '修'])))
,'㹌'
: (3, (('a', ['牛', 12180]), ('a', ['牜', 12180])))
,'㹍'
: (3, (('a', ['牛', 19467]), ('a', ['牜', 19467])))
,'㹎'
: (3, (('a', ['牛', 92454]), ('a', ['牜', 92454])))
,'㹏'
: (3, (('a', ['牛', '堇']), ('a', ['牜', '堇'])))
,'㹑'
: (3, (('a', ['牛', '贰']), ('a', ['牜', '贰'])))
,'㹒'
: (3, (('a', ['牛', '菐']), ('a', ['牜', '菐'])))
,'㹓'
: (3, (('a', ['牛', '堯']), ('a', ['牜', '堯'])))
,'㹔'
: (3, (('a', ['牛', '畺']), ('a', ['牜', '畺'])))
,'㹖'
: (3, (('a', ['牛', '豢']), ('a', ['牜', '豢'])))
,'㹗'
: (3, (('a', ['牛', 65412]), ('a', ['牜', 65412])))
,'㹘'
: (3, (('a', ['牛', '需']), ('a', ['牜', '需'])))
,'㹙'
: (3, (('a', ['牛', '䁝']), ('a', ['牜', '䁝'])))
,'㹚'
: (3, (('a', ['牛', 40610]), ('a', ['牜', 40610])))
,'㹛'
: (3, (('a', ['牛', 39258]), ('a', ['牜', 39258])))
,'㺇'
: (3, (('a', ['犭', '𦣞', '犬']), ('a', ['犭', '[左囗颐]', '犬'])))
,'㺿'
: (3, (('a', ['王', '𦣞']), ('a', ['王', '[左囗颐]'])))
,'㼝'
: (3, (('d', ['夘', '瓦']), ('d', ['夗', '瓦'])))
,'㼢'
: (3, (('a', ['𦣞', '瓦']), ('a', ['[左囗颐]', '瓦'])))
,'㼾'
: (3, (('a', ['鹿', '瓦']), ('a', ['[左用鹿]', '瓦'])))
,'㽜'
: (3, (('d', ['夘', '田']), ('d', ['夗', '田'])))
,'䄖'
: (3, (('a', ['示', '俞']), ('a', ['礻', '俞'])))
,'䄗'
: (3, (('a', ['示', '𣶒']), ('a', ['礻', '𣶒'])))
,'䄞'
: (3, (('a', ['示', 60985]), ('a', ['礻', 60985])))
,'䄣'
: (3, (('a', ['示', '賣']), ('a', ['礻', '賣'])))
,'䅇'
: (3, (('d', ['西', '禾']), ('d', ['覀', '禾'])))
,'䆛'
: (3, (('d', [65737, '吒']), ('d', ['穴', '吒'])))
,'䆞'
: (3, (('d', [65737, '㫐']), ('d', ['穴', '㫐'])))
,'䆢'
: (3, (('d', [65737, '抉']), ('d', ['穴', '抉'])))
,'䆨'
: (3, (('d', [65737, '昊']), ('d', ['穴', '昊'])))
,'䆩'
: (3, (('d', [65737, 37140]), ('d', ['穴', 37140])))
,'䆫'
: (3, (('d', [65737, '怱']), ('d', ['穴', '怱'])))
,'䆬'
: (3, (('d', [65737, '員']), ('d', ['穴', '員'])))
,'䆭'
: (3, (('d', [65737, '軒']), ('d', ['穴', '軒'])))
,'䆯'
: (3, (('d', [65737, '叕', '女']), ('d', ['穴', '叕', '女'])))
,'䆱'
: (3, (('d', [65737, '淡']), ('d', ['穴', '淡'])))
,'䆳'
: (3, (('d', [65737, '逐']), ('d', ['穴', '逐'])))
,'䆶'
: (3, (('d', [65737, '焦']), ('d', ['穴', '焦'])))
,'䆷'
: (3, (('d', [65737, 19988]), ('d', ['穴', 19988])))
,'䆼'
: (3, (('d', [65737, 45495]), ('d', ['穴', 45495])))
,'䆽'
: (3, (('d', [65737, 39070]), ('d', ['穴', 39070])))
,'䆿'
: (3, (('d', [65737, 21304]), ('d', ['穴', 21304])))
,'䇀'
: (3, (('d', [65737, '𩊐']), ('d', ['穴', '𩊐'])))
,'䇫'
: (3, (('d', ['⺮', '𦣞']), ('d', ['⺮', '[左囗颐]'])))
,'䊍'
: (3, (('d', ['䄪', '米']), ('d', ['[头囗黎]', '米'])))
,'䍃'
: (3, (('d', ['爪', '缶']), ('d', ['⺤', '缶'])))
,'䍨'
: (3, (('a', ['羊', '市']), ('a', ['⺶', '市'])))
,'䍩'
: (3, (('a', ['羊', '⺙']), ('a', ['⺶', '⺙'])))
,'䍪'
: (3, (('a', ['羊', '末']), ('a', ['⺶', '末'])))
,'䍫'
: (3, (('a', ['羊', '它']), ('a', ['⺶', '它'])))
,'䍬'
: (3, (('a', ['羊', '平']), ('a', ['⺶', '平'])))
,'䍭'
: (3, (('a', ['羊', '母']), ('a', ['⺶', '母'])))
,'䍮'
: (3, (('a', ['羊', '兆']), ('a', ['⺶', '兆'])))
,'䍯'
: (3, (('a', ['羊', '危']), ('a', ['⺶', '危'])))
,'䍰'
: (3, (('a', ['羊', '因']), ('a', ['⺶', '因'])))
,'䍱'
: (3, (('a', ['羊', '余']), ('a', ['⺶', '余'])))
,'䍲'
: (3, (('a', ['羊', '兒']), ('a', ['⺶', '兒'])))
,'䍳'
: (3, (('a', ['羊', '叕']), ('a', ['⺶', '叕'])))
,'䍴'
: (3, (('a', ['羊', '委']), ('a', ['⺶', '委'])))
,'䍵'
: (3, (('a', ['羊', '争']), ('a', ['⺶', '争'])))
,'䍶'
: (3, (('a', ['羊', '東']), ('a', ['⺶', '東'])))
,'䍷'
: (3, (('a', ['羊', '韋']), ('a', ['⺶', '韋'])))
,'䍸'
: (3, (('a', ['羊', '尃']), ('a', ['⺶', '尃'])))
,'䍹'
: (3, (('a', ['羊', '臭']), ('a', ['⺶', '臭'])))
,'䍺'
: (3, (('a', ['羊', '患']), ('a', ['⺶', '患'])))
,'䍻'
: (3, (('a', ['羊', '巽']), ('a', ['⺶', '巽'])))
,'䍼'
: (3, (('a', ['羊', 60966]), ('a', ['⺶', 60966])))
,'䍽'
: (3, (('a', ['羊', '歷']), ('a', ['⺶', '歷'])))
,'䎐'
: (3, (('a', [97020, '羽']), ('a', ['龺', '羽'])))
,'䎧'
: (3, (('a', [37009, '咅']), ('a', ['耒', '咅'])))
,'䎩'
: (3, (('a', [37009, '甾']), ('a', ['耒', '甾'])))
,'䎪'
: (3, (('a', [37009, '㝵']), ('a', ['耒', '㝵'])))
,'䎫'
: (3, (('a', [37009, '㚇']), ('a', ['耒', '㚇'])))
,'䎭'
: (3, (('a', [37009, '造']), ('a', ['耒', '造'])))
,'䎮'
: (3, (('a', [37009, 19467]), ('a', ['耒', 19467])))
,'䎯'
: (3, (('a', [37009, 37060]), ('a', ['耒', 37060])))
,'䎰'
: (3, (('a', [37009, '斮']), ('a', ['耒', '斮'])))
,'䎱'
: (3, (('a', [37009, '罷']), ('a', ['耒', '罷'])))
,'䒮'
: (3, (('d', [37165, '凡']), ('d', ['[纵组艹冖]', '凡'])))
,'䒯'
: (3, (('d', [37165, '丸']), ('d', ['[纵组艹冖]', '丸'])))
,'䒿'
: (3, (('d', [37165, '月']), ('d', ['[纵组艹冖]', '月'])))
,'䓨'
: (3, (('d', [37165, '缶']), ('d', ['[纵组艹冖]', '缶'])))
,'䖤'
: (3, (('d', ['夘', '虫']), ('d', ['夗', '虫'])))
,'䖿'
: (3, (('d', ['䄪', '虫']), ('d', ['[头囗黎]', '虫'])))
,'䝳'
: (3, (('d', ['𣦼', '貝']), ('d', ['[头囗餐]', '貝'])))
,'䝴'
: (3, (('d', [47005, '貝']), ('d', ['[头囗囊]', '貝'])))
,'䟓'
: (3, (('a', ['足', '丁']), ('a', ['⻊', '丁'])))
,'䟔'
: (3, (('a', ['足', '卜']), ('a', ['⻊', '卜'])))
,'䟕'
: (3, (('a', ['足', '叉']), ('a', ['⻊', '叉'])))
,'䟖'
: (3, (('a', ['足', '山']), ('a', ['⻊', '山'])))
,'䟗'
: (3, (('a', ['足', '氏']), ('a', ['⻊', '氏'])))
,'䟘'
: (3, (('a', ['足', '亢']), ('a', ['⻊', '亢'])))
,'䟙'
: (3, (('a', ['足', '切']), ('a', ['⻊', '切'])))
,'䟚'
: (3, (('a', ['足', '亓']), ('a', ['⻊', '亓'])))
,'䟛'
: (3, (('a', ['足', '市']), ('a', ['⻊', '市'])))
,'䟜'
: (3, (('a', ['足', '内']), ('a', ['⻊', '内'])))
,'䟝'
: (3, (('a', ['足', '殳']), ('a', ['⻊', '殳'])))
,'䟞'
: (3, (('a', ['足', '少']), ('a', ['⻊', '少'])))
,'䟠'
: (3, (('a', ['足', '戉']), ('a', ['⻊', '戉'])))
,'䟡'
: (3, (('a', ['足', '氐']), ('a', ['⻊', '氐'])))
,'䟢'
: (3, (('a', ['足', '尔']), ('a', ['⻊', '尔'])))
,'䟣'
: (3, (('a', ['足', '术']), ('a', ['⻊', '术'])))
,'䟤'
: (3, (('a', ['足', '必']), ('a', ['⻊', '必'])))
,'䟥'
: (3, (('a', ['足', '矛']), ('a', ['⻊', '矛'])))
,'䟦'
: (3, (('a', ['足', '叐']), ('a', ['⻊', '叐'])))
,'䟧'
: (3, (('a', ['足', '田']), ('a', ['⻊', '田'])))
,'䟨'
: (3, (('a', ['足', '民']), ('a', ['⻊', '民'])))
,'䟩'
: (3, (('a', ['足', '去']), ('a', ['⻊', '去'])))
,'䟪'
: (3, (('a', ['足', '乏']), ('a', ['⻊', '乏'])))
,'䟬'
: (3, (('a', ['足', '丘']), ('a', ['⻊', '丘'])))
,'䟭'
: (3, (('a', ['足', '乍']), ('a', ['⻊', '乍'])))
,'䟮'
: (3, (('a', ['足', '伏']), ('a', ['⻊', '伏'])))
,'䟯'
: (3, (('a', ['足', '舌']), ('a', ['⻊', '舌'])))
,'䟰'
: (3, (('a', ['足', '行']), ('a', ['⻊', '行'])))
,'䟱'
: (3, (('a', ['足', '朿']), ('a', ['⻊', '朿'])))
,'䟲'
: (3, (('a', ['足', '充']), ('a', ['⻊', '充'])))
,'䟴'
: (3, (('a', ['足', '辰']), ('a', ['⻊', '辰'])))
,'䟵'
: (3, (('a', ['足', '求']), ('a', ['⻊', '求'])))
,'䟶'
: (3, (('a', ['足', '坐']), ('a', ['⻊', '坐'])))
,'䟷'
: (3, (('a', ['足', '折']), ('a', ['⻊', '折'])))
,'䟸'
: (3, (('a', ['足', 90557]), ('a', ['⻊', 90557])))
,'䟹'
: (3, (('a', ['足', 65196]), ('a', ['⻊', 65196])))
,'䟺'
: (3, (('a', ['足', '貝']), ('a', ['⻊', '貝'])))
,'䟻'
: (3, (('a', ['足', '余']), ('a', ['⻊', '余'])))
,'䟼'
: (3, (('a', ['足', '武']), ('a', ['⻊', '武'])))
,'䟽'
: (3, (('a', ['足', '㐬']), ('a', ['⻊', '㐬'])))
,'䟾'
: (3, (('a', ['足', '叕']), ('a', ['⻊', '叕'])))
,'䟿'
: (3, (('a', ['足', '录']), ('a', ['⻊', '录'])))
,'䠀'
: (3, (('a', ['足', '尚']), ('a', ['⻊', '尚'])))
,'䠁'
: (3, (('a', ['足', '亝']), ('a', ['⻊', '亝'])))
,'䠃'
: (3, (('a', ['足', '兩']), ('a', ['⻊', '兩'])))
,'䠄'
: (3, (('a', ['足', '典']), ('a', ['⻊', '典'])))
,'䠅'
: (3, (('a', ['足', '囷']), ('a', ['⻊', '囷'])))
,'䠆'
: (3, (('a', ['足', '長']), ('a', ['⻊', '長'])))
,'䠇'
: (3, (('a', ['足', '屈']), ('a', ['⻊', '屈'])))
,'䠈'
: (3, (('a', ['足', '隶']), ('a', ['⻊', '隶'])))
,'䠉'
: (3, (('a', ['足', '官']), ('a', ['⻊', '官'])))
,'䠊'
: (3, (('a', ['足', '非']), ('a', ['⻊', '非'])))
,'䠋'
: (3, (('a', ['足', '卑']), ('a', ['⻊', '卑'])))
,'䠌'
: (3, (('a', ['足', 90561]), ('a', ['⻊', 90561])))
,'䠍'
: (3, (('a', ['足', '叚']), ('a', ['⻊', '叚'])))
,'䠎'
: (3, (('a', ['足', '屋']), ('a', ['⻊', '屋'])))
,'䠏'
: (3, (('a', ['足', '癸']), ('a', ['⻊', '癸'])))
,'䠐'
: (3, (('a', ['足', '狊']), ('a', ['⻊', '狊'])))
,'䠑'
: (3, (('a', ['足', '奎']), ('a', ['⻊', '奎'])))
,'䠒'
: (3, (('a', ['足', '胡']), ('a', ['⻊', '胡'])))
,'䠓'
: (3, (('a', ['足', '酋']), ('a', ['⻊', '酋'])))
,'䠔'
: (3, (('a', ['足', 90939]), ('a', ['⻊', 90939])))
,'䠕'
: (3, (('a', ['足', '柴']), ('a', ['⻊', '柴'])))
,'䠖'
: (3, (('a', ['足', '咨']), ('a', ['⻊', '咨'])))
,'䠗'
: (3, (('a', ['足', '臭']), ('a', ['⻊', '臭'])))
,'䠘'
: (3, (('a', ['足', '𣬉']), ('a', ['⻊', '𣬉'])))
,'䠙'
: (3, (('a', ['足', '旁']), ('a', ['⻊', '旁'])))
,'䠚'
: (3, (('a', ['足', '窊']), ('a', ['⻊', '窊'])))
,'䠛'
: (3, (('a', ['足', '䍃']), ('a', ['⻊', '䍃'])))
,'䠜'
: (3, (('a', ['足', 90276]), ('a', ['⻊', 90276])))
,'䠝'
: (3, (('a', ['足', '員']), ('a', ['⻊', '員'])))
,'䠞'
: (3, (('a', ['足', '戚']), ('a', ['⻊', '戚'])))
,'䠡'
: (3, (('a', ['足', 43362]), ('a', ['⻊', 43362])))
,'䠣'
: (3, (('a', ['足', '巽']), ('a', ['⻊', '巽'])))
,'䠤'
: (3, (('a', ['足', '單']), ('a', ['⻊', '單'])))
,'䠥'
: (3, (('a', ['足', '敝']), ('a', ['⻊', '敝'])))
,'䠦'
: (3, (('a', ['足', '智']), ('a', ['⻊', '智'])))
,'䠧'
: (3, (('a', ['足', '屠']), ('a', ['⻊', '屠'])))
,'䠨'
: (3, (('a', ['足', '詹']), ('a', ['⻊', '詹'])))
,'䠩'
: (3, (('a', ['足', '歳']), ('a', ['⻊', '歳'])))
,'䠪'
: (3, (('a', ['足', 59377]), ('a', ['⻊', 59377])))
,'䠫'
: (3, (('a', ['足', 59373]), ('a', ['⻊', 59373])))
,'䠬'
: (3, (('a', ['足', '鄧']), ('a', ['⻊', '鄧'])))
,'䠭'
: (3, (('a', ['足', 24071]), ('a', ['⻊', 24071])))
,'䠮'
: (3, (('a', ['足', '駦']), ('a', ['⻊', '駦'])))
,'䠯'
: (3, (('a', ['足', 39431]), ('a', ['⻊', 39431])))
,'䠰'
: (3, (('a', ['足', 12220]), ('a', ['⻊', 12220])))
,'䠱'
: (3, (('a', ['足', '屬']), ('a', ['⻊', '屬'])))
,'䢀'
: (3, (('a', ['车', '乞']), ('a', ['[左用车]', '乞'])))
,'䢁'
: (3, (('a', ['车', '月']), ('a', ['[左用车]', '月'])))
,'䢂'
: (3, (('a', ['车', '立']), ('a', ['[左用车]', '立'])))
,'䢴'
: (3, (('a', ['千', '阝']), ('a', ['[撇化千]', '阝'])))
,'䨋'
: (3, (('d', ['雨', '乇']), ('d', ['[头用雨]', '乇'])))
,'䨌'
: (3, (('d', ['雨', '元']), ('d', ['[头用雨]', '元'])))
,'䨍'
: (3, (('d', ['雨', '井']), ('d', ['[头用雨]', '井'])))
,'䨎'
: (3, (('d', ['雨', '弘']), ('d', ['[头用雨]', '弘'])))
,'䨏'
: (3, (('d', ['雨', '次']), ('d', ['[头用雨]', '次'])))
,'䨐'
: (3, (('d', ['雨', '合']), ('d', ['[头用雨]', '合'])))
,'䨑'
: (3, (('d', ['雨', '夷']), ('d', ['[头用雨]', '夷'])))
,'䨒'
: (3, (('d', ['雨', '羽']), ('d', ['[头用雨]', '羽'])))
,'䨓'
: (3, (('d', ['雨', '回']), ('d', ['[头用雨]', '回'])))
,'䨔'
: (3, (('d', ['雨', '光']), ('d', ['[头用雨]', '光'])))
,'䨕'
: (3, (('d', ['雨', '汙']), ('d', ['[头用雨]', '汙'])))
,'䨖'
: (3, (('d', ['雨', '有']), ('d', ['[头用雨]', '有'])))
,'䨗'
: (3, (('d', ['雨', '孚']), ('d', ['[头用雨]', '孚'])))
,'䨘'
: (3, (('d', ['雨', '見']), ('d', ['[头用雨]', '見'])))
,'䨙'
: (3, (('d', ['雨', 97841]), ('d', ['[头用雨]', 97841])))
,'䨚'
: (3, (('d', ['雨', '忽']), ('d', ['[头用雨]', '忽'])))
,'䨛'
: (3, (('d', ['雨', '析']), ('d', ['[头用雨]', '析'])))
,'䨜'
: (3, (('d', ['雨', '朋']), ('d', ['[头用雨]', '朋'])))
,'䨝'
: (3, (('d', ['雨', '青']), ('d', ['[头用雨]', '青'])))
,'䨞'
: (3, (('d', ['雨', '禹']), ('d', ['[头用雨]', '禹'])))
,'䨟'
: (3, (('d', ['雨', '洼']), ('d', ['[头用雨]', '洼'])))
,'䨠'
: (3, (('d', ['雨', '曷']), ('d', ['[头用雨]', '曷'])))
,'䨡'
: (3, (('d', ['雨', '函']), ('d', ['[头用雨]', '函'])))
,'䨢'
: (3, (('d', ['雨', '甚']), ('d', ['[头用雨]', '甚'])))
,'䨣'
: (3, (('d', ['雨', '革']), ('d', ['[头用雨]', '革'])))
,'䨤'
: (3, (('d', ['雨', '迪']), ('d', ['[头用雨]', '迪'])))
,'䨥'
: (3, (('d', ['雨', '隻']), ('d', ['[头用雨]', '隻'])))
,'䨦'
: (3, (('d', ['雨', '旁']), ('d', ['[头用雨]', '旁'])))
,'䨧'
: (3, (('d', ['雨', '竛']), ('d', ['[头用雨]', '竛'])))
,'䨨'
: (3, (('d', ['雨', '追']), ('d', ['[头用雨]', '追'])))
,'䨩'
: (3, (('d', ['雨', 97844]), ('d', ['[头用雨]', 97844])))
,'䨪'
: (3, (('d', ['雨', '埋']), ('d', ['[头用雨]', '埋'])))
,'䨫'
: (3, (('d', ['雨', '夾', '夂']), ('d', ['[头用雨]', '夾', '夂'])))
,'䨬'
: (3, (('d', ['雨', '淋']), ('d', ['[头用雨]', '淋'])))
,'䨮'
: (3, (('d', ['雨', '彗']), ('d', ['[头用雨]', '彗'])))
,'䨯'
: (3, (('d', ['雨', '陳']), ('d', ['[头用雨]', '陳'])))
,'䨰'
: (3, (('d', ['雨', '㴖']), ('d', ['[头用雨]', '㴖'])))
,'䨱'
: (3, (('d', ['雨', 63064]), ('d', ['[头用雨]', 63064])))
,'䨳'
: (3, (('d', ['雨', '覞']), ('d', ['[头用雨]', '覞'])))
,'䨴'
: (3, (('d', ['雨', '對']), ('d', ['[头用雨]', '對'])))
,'䨵'
: (3, (('d', ['雨', 21423]), ('d', ['[头用雨]', 21423])))
,'䨶'
: (3, (('d', ['雨', 91012]), ('d', ['[头用雨]', 91012])))
,'䨷'
: (3, (('d', ['雨', 26025]), ('d', ['[头用雨]', 26025])))
,'䨸'
: (3, (('d', ['雨', 45581]), ('d', ['[头用雨]', 45581])))
,'䨹'
: (3, (('d', ['雨', 45582]), ('d', ['[头用雨]', 45582])))
,'䬠'
: (3, (('d', ['雨', '飛']), ('d', ['[头用雨]', '飛'])))
,'䬢'
: (3, (('a', ['食', '刀']), ('a', ['飠', '刀'])))
,'䬣'
: (3, (('a', ['食', '乞']), ('a', ['飠', '乞'])))
,'䬦'
: (3, (('a', ['食', '殳']), ('a', ['飠', '殳'])))
,'䬧'
: (3, (('a', ['食', '元']), ('a', ['飠', '元'])))
,'䬨'
: (3, (('a', [37004, '勼']), ('a', ['飠', '勼'])))
,'䬪'
: (3, (('a', ['食', '不']), ('a', ['飠', '不'])))
,'䬫'
: (3, (('a', ['食', '氐']), ('a', ['飠', '氐'])))
,'䬬'
: (3, (('a', ['食', '央']), ('a', ['飠', '央'])))
,'䬮'
: (3, (('a', ['食', '以']), ('a', ['飠', '以'])))
,'䬯'
: (3, (('a', ['食', '占']), ('a', ['飠', '占'])))
,'䬰'
: (3, (('a', ['食', '召']), ('a', ['飠', '召'])))
,'䬱'
: (3, (('a', ['食', '本']), ('a', ['飠', '本'])))
,'䬲'
: (3, (('a', ['食', '句']), ('a', ['飠', '句'])))
,'䬳'
: (3, (('a', ['食', '半']), ('a', ['飠', '半'])))
,'䬴'
: (3, (('a', ['食', '末']), ('a', ['飠', '末'])))
,'䬵'
: (3, (('a', ['食', '亥']), ('a', ['飠', '亥'])))
,'䬶'
: (3, (('a', ['食', '艮']), ('a', ['飠', '艮'])))
,'䬷'
: (3, (('a', ['食', '多']), ('a', ['飠', '多'])))
,'䬹'
: (3, (('a', ['食', '至']), ('a', ['飠', '至'])))
,'䬺'
: (3, (('a', ['食', '羊']), ('a', ['飠', '羊'])))
,'䬻'
: (3, (('a', [37004, '㦮']), ('a', ['飠', '㦮'])))
,'䬼'
: (3, (('a', [37004, '肙']), ('a', ['飠', '肙'])))
,'䬽'
: (3, (('a', ['食', '兑']), ('a', ['飠', '兑'])))
,'䬾'
: (3, (('a', ['食', '弟']), ('a', ['飠', '弟'])))
,'䬿'
: (3, (('a', ['食', '尾']), ('a', ['飠', '尾'])))
,'䭀'
: (3, (('a', ['食', '迅']), ('a', ['飠', '迅'])))
,'䭂'
: (3, (('a', ['食', '邑']), ('a', ['飠', '邑'])))
,'䭃'
: (3, (('a', ['食', '念']), ('a', ['飠', '念'])))
,'䭄'
: (3, (('a', ['食', '事']), ('a', ['飠', '事'])))
,'䭅'
: (3, (('a', ['食', '固']), ('a', ['飠', '固'])))
,'䭇'
: (3, (('a', [37004, 95907]), ('a', ['飠', 95907])))
,'䭈'
: (3, (('a', ['食', '建']), ('a', ['飠', '建'])))
,'䭉'
: (3, (('a', [37004, 51179]), ('a', ['飠', 51179])))
,'䭊'
: (3, (('a', ['食', '英']), ('a', ['飠', '英'])))
,'䭋'
: (3, (('a', ['食', '保']), ('a', ['飠', '保'])))
,'䭍'
: (3, (('a', [37004, 48616]), ('a', ['飠', 48616])))
,'䭎'
: (3, (('a', [37004, '枼']), ('a', ['飠', '枼'])))
,'䭏'
: (3, (('a', ['食', '扁']), ('a', ['飠', '扁'])))
,'䭐'
: (3, (('a', [37004, '恙']), ('a', ['飠', '恙'])))
,'䭑'
: (3, (('a', ['食', '兼']), ('a', ['飠', '兼'])))
,'䭒'
: (3, (('a', ['食', '息']), ('a', ['飠', '息'])))
,'䭓'
: (3, (('a', [37004, '豈']), ('a', ['飠', '豈'])))
,'䭔'
: (3, (('a', [37004, '追']), ('a', ['飠', '追'])))
,'䭖'
: (3, (('a', [37004, '庶']), ('a', ['飠', '庶'])))
,'䭗'
: (3, (('a', ['食', '竟']), ('a', ['飠', '竟'])))
,'䭘'
: (3, (('a', ['食', '景']), ('a', ['飠', '景'])))
,'䭙'
: (3, (('a', [37004, 60966]), ('a', ['飠', 60966])))
,'䭚'
: (3, (('a', ['食', '童']), ('a', ['飠', '童'])))
,'䭛'
: (3, (('a', ['食', '敢']), ('a', ['飠', '敢'])))
,'䭜'
: (3, (('a', ['食', '尞']), ('a', ['飠', '尞'])))
,'䭝'
: (3, (('a', [37004, 61638]), ('a', ['飠', 61638])))
,'䭞'
: (3, (('a', [37004, '睪']), ('a', ['飠', '睪'])))
,'䭟'
: (3, (('a', [37004, 90318]), ('a', ['飠', 90318])))
,'䭠'
: (3, (('a', ['食', '廉']), ('a', ['飠', '廉'])))
,'䭡'
: (3, (('a', [37004, '㥯']), ('a', ['飠', '㥯'])))
,'䭢'
: (3, (('a', ['食', '寧']), ('a', ['飠', '寧'])))
,'䭣'
: (3, (('a', [37004, '齊']), ('a', ['飠', '齊'])))
,'䭤'
: (3, (('a', [37004, '遣']), ('a', ['飠', '遣'])))
,'䭥'
: (3, (('a', [37004, 90052]), ('a', ['飠', 90052])))
,'䭦'
: (3, (('a', [37004, 65299]), ('a', ['飠', 65299])))
,'䭧'
: (3, (('a', ['食', '麼']), ('a', ['飠', '麼'])))
,'䭨'
: (3, (('a', [37004, 19795]), ('a', ['飠', 19795])))
,'䭩'
: (3, (('a', ['食', '靡']), ('a', ['飠', '靡'])))
,'䮧'
: (3, (('a', [97020, 12032]), ('a', ['龺', 12032])))
,'䱌'
: (3, (('a', ['魚', '𦣞']), ('a', ['魚', '[左囗颐]'])))
,'䱗'
: (3, (('d', ['𣦼', '魚']), ('d', ['[头囗餐]', '魚'])))
,'䴧'
: (3, (('a', ['鹿', '委']), ('a', ['[左用鹿]', '委'])))
,'䴨'
: (3, (('a', ['鹿', '原']), ('a', ['[左用鹿]', '原'])))
,'䴻'
: (3, (('d', ['䄪', '麥']), ('d', ['[头囗黎]', '麥'])))
,'亭'
: (3, (('d', [37106, '丁']), ('d', ['[纵三组亠口冖]', '丁'])))
,'亮'
: (3, (('d', [37106, '几']), ('d', ['[纵三组亠口冖]', '几'])))
,'亳'
: (3, (('d', [37106, '乇']), ('d', ['[纵三组亠口冖]', '乇'])))
,'修'
: (3, (('a', [39752, 38005]), ('a', ['[横组亻丨]', 38005])))
,'倏'
: (3, (('a', [39752, 37582]), ('a', ['[横组亻丨]', 37582])))
,'倐'
: (3, (('a', [39752, 39613]), ('a', ['[横组亻丨]', 39613])))
,'候'
: (3, (('a', [39752, 37260]), ('a', ['[横组亻丨]', 37260])))
,'偹'
: (3, (('a', [39752, '备']), ('a', ['[横组亻丨]', '备'])))
,'傜'
: (3, (('a', ['亻', 37021]), ('a', ['亻', '䍃'])))
,'儵'
: (3, (('a', [39752, 40315]), ('a', ['[横组亻丨]', 40315])))
,'刋'
: (3, (('a', ['千', '刂']), ('a', ['[撇化千]', '刂'])))
,'判'
: (3, (('a', ['半', '刂']), ('a', ['[撇化半]', '刂'])))
,'剆'
: (3, (('a', [37105, '刂']), ('a', ['[左囗郎]', '刂'])))
,'剓'
: (3, (('d', [37063, '刀']), ('d', ['[头囗黎]', '刀'])))
,'剺'
: (3, (('d', [37087, 24225]), ('d', ['[横组未攵]', 24225])))
,'労'
: (3, (('d', [37044, '力']), ('d', ['[头囗觉]', '力'])))
,'勆'
: (3, (('a', [37105, '力']), ('a', ['[左囗郎]', '力'])))
,'勞'
: (3, (('d', [37027, '力']), ('d', ['𤇾', '力'])))
,'厭'
: (3, (('stl', ['厂', '猒']), ('stl', ['厂', 38207])))
,'厴'
: (3, (('stl', [37069, '甲']), ('stl', ['厭', '甲'])))
,'变'
: (3, (('d', ['亦', '又']), ('d', ['[头囗鸾]', '又'])))
,'叛'
: (3, (('a', ['半', '反']), ('a', ['[撇化半]', '反'])))
,'啓'
: (3, (('d', ['𢼄', '口']), ('d', ['[横组户攵]', '口'])))
,'営'
: (3, (('d', [37044, '吕']), ('d', ['[头囗觉]', '吕'])))
,'喾'
: (3, (('d', [37044, '告']), ('d', ['[头囗觉]', '告'])))
,'嗂'
: (3, (('a', ['口', 37021]), ('a', ['口', '䍃'])))
,'圱'
: (3, (('a', ['千', '土']), ('a', ['[撇化千]', '土'])))
,'坚'
: (3, (('d', [37144, '土']), ('d', ['[头囗坚]', '土'])))
,'垔'
: (3, (('d', ['西', '土']), ('d', ['覀', '土'])))
,'塋'
: (3, (('d', [37027, '土']), ('d', ['𤇾', '土'])))
,'墼'
: (3, (('d', ['𣪠', '土']), ('d', ['[头囗擊]', '土'])))
,'壱'
: (3, (('d', [37151, '匕']), ('d', ['[纵组士冖]', '匕'])))
,'売'
: (3, (('d', [37151, '儿']), ('d', ['[纵组士冖]', '儿'])))
,'壷'
: (3, (('d', [37151, 99852, '㇐']), ('d', ['[纵组士冖]', 99852, '㇐'])))
,'壸'
: (3, (('d', [37151, '亚']), ('d', ['[纵组士冖]', '亚'])))
,'壺'
: (3, (('d', [37151, 37234]), ('d', ['[纵组士冖]', 37234])))
,'壼'
: (3, (('d', [37151, '亞']), ('d', ['[纵组士冖]', '亞'])))
,'変'
: (3, (('d', ['亦', '夂']), ('d', ['[头囗鸾]', '夂'])))
,'奖'
: (3, (('d', [37194, '大']), ('d', ['[头囗桨]', '大'])))
,'姜'
: (3, (('d', ['羊', '女']), ('d', ['⺷', '女'])))
,'姬'
: (3, (('a', ['女', '𦣞']), ('a', ['女', '[左囗颐]'])))
,'娈'
: (3, (('d', ['亦', '女']), ('d', ['[头囗鸾]', '女'])))
,'媱'
: (3, (('a', ['女', 37021]), ('a', ['女', '䍃'])))
,'嫈'
: (3, (('d', [37027, '女']), ('d', ['𤇾', '女'])))
,'嫠'
: (3, (('d', [37087, 45755]), ('d', ['[横组未攵]', 45755])))
,'嬮'
: (3, (('stl', [37069, '女']), ('stl', ['厭', '女'])))
,'嬴'
: (3, (('st', ['𣎆', '女']), ('st', ['[上包围囗赢]', '女'])))
,'孁'
: (3, (('d', ['雨', 37980]), ('d', ['[头用雨]', 37980])))
,'学'
: (3, (('d', [37044, '子']), ('d', ['[头囗觉]', '子'])))
,'孪'
: (3, (('d', ['亦', '子']), ('d', ['[头囗鸾]', '子'])))
,'孷'
: (3, (('d', [37087, '𠨯']), ('d', ['[横组未攵]', '𠨯'])))
,'宧'
: (3, (('d', ['宀', '𦣞']), ('d', ['宀', '[左囗颐]'])))
,'尭'
: (3, (('d', ['卉', '兀']), ('d', ['[头囗桒]', '兀'])))
,'峃'
: (3, (('d', [37044, '山']), ('d', ['[头囗觉]', '山'])))
,'峦'
: (3, (('d', ['亦', '山']), ('d', ['[头囗鸾]', '山'])))
,'島'
: (3, (('str', [37157, '山']), ('str', ['[断足鳥]', '山'])))
,'巸'
: (3, (('a', ['𦣞', '巳']), ('a', ['[左囗颐]', '巳'])))
,'弯'
: (3, (('d', ['亦', '弓']), ('d', ['[头囗鸾]', '弓'])))
,'徭'
: (3, (('a', ['彳', 37021]), ('a', ['彳', '䍃'])))
,'恋'
: (3, (('d', ['亦', '心']), ('d', ['[头囗鸾]', '心'])))
,'恙'
: (3, (('d', ['羊', '心']), ('d', ['⺷', '心'])))
,'愮'
: (3, (('a', ['忄', 37021]), ('a', ['忄', '䍃'])))
,'懕'
: (3, (('stl', [37069, '心']), ('stl', ['厭', '心'])))
,'挛'
: (3, (('d', ['亦', '手']), ('d', ['[头囗鸾]', '手'])))
,'摇'
: (3, (('a', ['扌', 37021]), ('a', ['扌', '䍃'])))
,'擊'
: (3, (('d', ['𣪠', '手']), ('d', ['[头囗擊]', '手'])))
,'擪'
: (3, (('stl', [37069, '手']), ('stl', ['厭', '手'])))
,'攸'
: (3, (('a', [39752, '⺙']), ('a', ['[横组亻丨]', '⺙'])))
,'斄'
: (3, (('d', [37087, '𠩬']), ('d', ['[横组未攵]', '𠩬'])))
,'斩'
: (3, (('a', ['车', '斤']), ('a', ['[左用车]', '斤'])))
,'晝'
: (3, (('d', ['聿', '旦']), ('d', ['[断尾聿]', '旦'])))
,'晵'
: (3, (('d', ['𢼄', '日']), ('d', ['[横组户攵]', '日'])))
,'暚'
: (3, (('a', ['日', 37021]), ('a', ['日', '䍃'])))
,'書'
: (3, (('d', ['聿', '日']), ('d', ['[断尾聿]', '日'])))
,'朗'
: (3, (('a', [37105, '月']), ('a', ['[左囗郎]', '月'])))
,'栄'
: (3, (('d', [37044, '木']), ('d', ['[头囗觉]', '木'])))
,'栾'
: (3, (('d', ['亦', '木']), ('d', ['[头囗鸾]', '木'])))
,'桒'
: (3, (('d', ['卉', '木']), ('d', ['[头囗桒]', '木'])))
,'桨'
: (3, (('d', [37194, '木']), ('d', ['[头囗桨]', '木'])))
,'條'
: (3, (('a', [39752, '条']), ('a', ['[横组亻丨]', '条'])))
,'梟'
: (3, (('str', [37157, '木']), ('str', ['[断足鳥]', '木'])))
,'棃'
: (3, (('d', [37063, '木']), ('d', ['[头囗黎]', '木'])))
,'棨'
: (3, (('d', ['𢼄', '木']), ('d', ['[横组户攵]', '木'])))
,'榣'
: (3, (('a', ['木', 37021]), ('a', ['木', '䍃'])))
,'榮'
: (3, (('d', [37027, '木']), ('d', ['𤇾', '木'])))
,'檕'
: (3, (('d', ['𣪠', '木']), ('d', ['[头囗擊]', '木'])))
,'檿'
: (3, (('stl', [37069, '木']), ('stl', ['厭', '木'])))
,'欴'
: (3, (('a', [37105, '欠']), ('a', ['[左囗郎]', '欠'])))
,'毫'
: (3, (('d', [37106, '毛']), ('d', ['[纵三组亠口冖]', '毛'])))
,'氂'
: (3, (('d', [37087, 38314]), ('d', ['[横组未攵]', 38314])))
,'泶'
: (3, (('st', [37044, '水']), ('st', ['[头囗觉]', '水'])))
,'洍'
: (3, (('a', ['氵', '𦣞']), ('a', ['氵', '[左囗颐]'])))
,'浆'
: (3, (('d', [37194, '水']), ('d', ['[头囗桨]', '水'])))
,'滎'
: (3, (('d', [37027, '水']), ('d', ['𤇾', '水'])))
,'滛'
: (3, (('a', ['氵', 37021]), ('a', ['氵', '䍃'])))
,'漦'
: (3, (('d', [37087, '𣱷']), ('d', ['[横组未攵]', '𣱷'])))
,'煢'
: (3, (('d', [37027, '卂']), ('d', ['𤇾', '卂'])))
,'熎'
: (3, (('a', ['火', 37021]), ('a', ['火', '䍃'])))
,'熒'
: (3, (('d', [37027, '火']), ('d', ['𤇾', '火'])))
,'營'
: (3, (('d', [37027, '吕']), ('d', ['𤇾', '吕'])))
,'爂'
: (3, (('d', [37147, '火']), ('d', ['[头囗璺]', '火'])))
,'爨'
: (3, (('d', [37147, 37568]), ('d', ['[头囗璺]', 37568])))
,'牝'
: (3, (('a', ['牛', '匕']), ('a', ['牜', '匕'])))
,'牞'
: (3, (('a', ['牛', '力']), ('a', ['牜', '力'])))
,'牠'
: (3, (('a', ['牛', '也']), ('a', ['牜', '也'])))
,'牡'
: (3, (('a', ['牛', '土']), ('a', ['牜', '土'])))
,'牣'
: (3, (('a', ['牛', '刃']), ('a', ['牜', '刃'])))
,'牤'
: (3, (('a', ['牛', '亡']), ('a', ['牜', '亡'])))
,'牥'
: (3, (('a', ['牛', '方']), ('a', ['牜', '方'])))
,'牦'
: (3, (('a', ['牛', '毛']), ('a', ['牜', '毛'])))
,'牧'
: (3, (('a', ['牛', '⺙']), ('a', ['牜', '⺙'])))
,'牨'
: (3, (('a', ['牛', '亢']), ('a', ['牜', '亢'])))
,'物'
: (3, (('a', ['牛', '勿']), ('a', ['牜', '勿'])))
,'牫'
: (3, (('a', ['牛', '戈']), ('a', ['牜', '戈'])))
,'牬'
: (3, (('a', ['牛', 37088]), ('a', ['牜', 37088])))
,'牭'
: (3, (('a', ['牛', '四']), ('a', ['牜', '四'])))
,'牯'
: (3, (('a', ['牛', '古']), ('a', ['牜', '古'])))
,'牰'
: (3, (('a', ['牛', '由']), ('a', ['牜', '由'])))
,'牱'
: (3, (('a', ['牛', '可']), ('a', ['牜', '可'])))
,'牲'
: (3, (('a', ['牛', '生']), ('a', ['牜', '生'])))
,'牳'
: (3, (('a', ['牛', '母']), ('a', ['牜', '母'])))
,'牴'
: (3, (('a', ['牛', '氐']), ('a', ['牜', '氐'])))
,'牷'
: (3, (('a', ['牛', '全']), ('a', ['牜', '全'])))
,'牸'
: (3, (('a', ['牛', '字']), ('a', ['牜', '字'])))
,'特'
: (3, (('a', ['牛', '寺']), ('a', ['牜', '寺'])))
,'牺'
: (3, (('a', ['牛', '西']), ('a', ['牜', '西'])))
,'牻'
: (3, (('a', ['牛', '尨']), ('a', ['牜', '尨'])))
,'牼'
: (3, (('a', ['牛', '巠']), ('a', ['牜', '巠'])))
,'牾'
: (3, (('a', ['牛', '吾']), ('a', ['牜', '吾'])))
,'牿'
: (3, (('a', ['牛', '告']), ('a', ['牜', '告'])))
,'犂'
: (3, (('d', [37063, '牛']), ('d', ['[头囗黎]', '牛'])))
,'犃'
: (3, (('a', ['牛', '咅']), ('a', ['牜', '咅'])))
,'犄'
: (3, (('a', ['牛', '奇']), ('a', ['牜', '奇'])))
,'犅'
: (3, (('a', ['牛', '岡']), ('a', ['牜', '岡'])))
,'犆'
: (3, (('a', ['牛', '直']), ('a', ['牜', '直'])))
,'犈'
: (3, (('a', ['牛', '卷']), ('a', ['牜', '卷'])))
,'犉'
: (3, (('a', ['牛', '享']), ('a', ['牜', '享'])))
,'犊'
: (3, (('a', ['牛', '卖']), ('a', ['牜', '卖'])))
,'犋'
: (3, (('a', ['牛', '具']), ('a', ['牜', '具'])))
,'犌'
: (3, (('a', ['牛', '叚']), ('a', ['牜', '叚'])))
,'犍'
: (3, (('a', ['牛', '建']), ('a', ['牜', '建'])))
,'犏'
: (3, (('a', ['牛', '扁']), ('a', ['牜', '扁'])))
,'犐'
: (3, (('a', ['牛', '科']), ('a', ['牜', '科'])))
,'犑'
: (3, (('a', ['牛', '狊']), ('a', ['牜', '狊'])))
,'犒'
: (3, (('a', ['牛', '高']), ('a', ['牜', '高'])))
,'犓'
: (3, (('a', ['牛', '芻']), ('a', ['牜', '芻'])))
,'犔'
: (3, (('a', ['牛', '氣']), ('a', ['牜', '氣'])))
,'犕'
: (3, (('a', ['牛', 37146]), ('a', ['牜', 37146])))
,'犖'
: (3, (('d', [37027, '牛']), ('d', ['𤇾', '牛'])))
,'犗'
: (3, (('a', ['牛', '害']), ('a', ['牜', '害'])))
,'犙'
: (3, (('a', ['牛', '參']), ('a', ['牜', '參'])))
,'犛'
: (3, (('d', [37087, 47747]), ('d', ['[横组未攵]', 47747])))
,'犜'
: (3, (('a', ['牛', '敦']), ('a', ['牜', '敦'])))
,'犝'
: (3, (('a', ['牛', '童']), ('a', ['牜', '童'])))
,'犞'
: (3, (('a', ['牛', '喬']), ('a', ['牜', '喬'])))
,'犠'
: (3, (('a', ['牛', '義']), ('a', ['牜', '義'])))
,'犡'
: (3, (('a', ['牛', '厲']), ('a', ['牜', '厲'])))
,'犢'
: (3, (('a', ['牛', '賣']), ('a', ['牜', '賣'])))
,'犣'
: (3, (('a', ['牛', '巤']), ('a', ['牜', '巤'])))
,'犤'
: (3, (('a', ['牛', '罷']), ('a', ['牜', '罷'])))
,'犥'
: (3, (('a', ['牛', '麃']), ('a', ['牜', '麃'])))
,'犦'
: (3, (('a', ['牛', 37094]), ('a', ['牜', 37094])))
,'犧'
: (3, (('a', ['牛', '羲']), ('a', ['牜', '羲'])))
,'犪'
: (3, (('a', ['牛', '夔']), ('a', ['牜', '夔'])))
,'猺'
: (3, (('a', ['犭', 37021]), ('a', ['犭', '䍃'])))
,'瑩'
: (3, (('d', [37027, '玉']), ('d', ['𤇾', '玉'])))
,'瑶'
: (3, (('a', ['王', 37021]), ('a', ['王', '䍃'])))
,'璺'
: (3, (('d', [37147, '玉']), ('d', ['[头囗璺]', '玉'])))
,'甇'
: (3, (('d', [37027, '瓦']), ('d', ['𤇾', '瓦'])))
,'畫'
: (3, (('d', ['聿', 38348]), ('d', ['[断尾聿]', 38348])))
,'畵'
: (3, (('d', ['聿', 38227]), ('d', ['[断尾聿]', 38227])))
,'盖'
: (3, (('d', ['羊', '皿']), ('d', ['⺷', '皿'])))
,'睝'
: (3, (('d', [37063, '目']), ('d', ['[头囗黎]', '目'])))
,'磘'
: (3, (('a', ['石', 37021]), ('a', ['石', '䍃'])))
,'礊'
: (3, (('d', ['𣪠', '石']), ('d', ['[头囗擊]', '石'])))
,'禜'
: (3, (('d', [37027, '示']), ('d', ['𤇾', '示'])))
,'稁'
: (3, (('d', [37106, '禾']), ('d', ['[纵三组亠口冖]', '禾'])))
,'穴'
: (3, (('d', ['宀', '八']), ('d', ['宀', '儿'])))
,'窰'
: (3, (('d', ['穴', 37021]), ('d', ['穴', '䍃'])))
,'竖'
: (3, (('d', [37144, '立']), ('d', ['[头囗坚]', '立'])))
,'粲'
: (3, (('d', ['𣦼', '米']), ('d', ['[头囗餐]', '米'])))
,'紧'
: (3, (('d', [37144, '糸']), ('d', ['[头囗坚]', '糸'])))
,'絛'
: (3, (('a', [39752, 38446]), ('a', ['[横组亻丨]', 38446])))
,'綮'
: (3, (('d', ['𢼄', '糸']), ('d', ['[横组户攵]', '糸'])))
,'縈'
: (3, (('d', [37027, '糸']), ('d', ['𤇾', '糸'])))
,'繇'
: (3, (('a', [37021, '系']), ('a', ['䍃', '系'])))
,'繫'
: (3, (('d', ['𣪠', '糸']), ('d', ['[头囗擊]', '糸'])))
,'罃'
: (3, (('d', [37027, '缶']), ('d', ['𤇾', '缶'])))
,'罊'
: (3, (('d', ['𣪠', '缶']), ('d', ['[头囗擊]', '缶'])))
,'美'
: (3, (('d', ['羊', '大']), ('d', ['⺷', '大'])))
,'羑'
: (3, (('d', ['羊', '久']), ('d', ['⺷', '久'])))
,'羔'
: (3, (('d', ['羊', '灬']), ('d', ['⺷', '灬'])))
,'羕'
: (3, (('d', ['羊', '永']), ('d', ['⺷', '永'])))
,'羙'
: (3, (('d', ['羊', '火']), ('d', ['⺷', '火'])))
,'羚'
: (3, (('a', ['羊', '令']), ('a', ['⺶', '令'])))
,'羛'
: (3, (('d', ['羊', '弗']), ('d', ['⺷', '弗'])))
,'羝'
: (3, (('a', ['羊', '氐']), ('a', ['⺶', '氐'])))
,'羟'
: (3, (('a', ['羊', 37030]), ('a', ['⺶', 37030])))
,'羡'
: (3, (('d', ['羊', '次']), ('d', ['⺷', '次'])))
,'羧'
: (3, (('a', ['羊', '夋']), ('a', ['⺶', '夋'])))
,'羨'
: (3, (('d', ['羊', '㳄']), ('d', ['⺷', '㳄'])))
,'義'
: (3, (('d', ['羊', '我']), ('d', ['⺷', '我'])))
,'羯'
: (3, (('a', ['羊', '曷']), ('a', ['⺶', '曷'])))
,'羰'
: (3, (('a', ['羊', '炭']), ('a', ['⺶', '炭'])))
,'羲'
: (3, (('d', ['羊', 38485]), ('d', ['⺷', 38485])))
,'羸'
: (3, (('st', ['𣎆', '羊']), ('st', ['[上包围囗赢]', '羊'])))
,'翔'
: (3, (('a', ['羊', '羽']), ('a', ['⺶', '羽'])))
,'翛'
: (3, (('a', [39752, 54060]), ('a', ['[横组亻丨]', 54060])))
,'耒'
: (3, (('wb', ['丰', '八']), ('wt', ['㇒', '未'])))
,'肇'
: (3, (('d', ['𢼄', '聿']), ('d', ['[横组户攵]', '聿'])))
,'肾'
: (3, (('d', [37144, '月']), ('d', ['[头囗坚]', '月'])))
,'脔'
: (3, (('d', ['亦', '肉']), ('d', ['[头囗鸾]', '肉'])))
,'脩'
: (3, (('a', [39752, '𡕙']), ('a', ['[横组亻丨]', '𡕙'])))
,'臝'
: (3, (('st', ['𣎆', '果']), ('st', ['[上包围囗赢]', '果'])))
,'舋'
: (3, (('d', [37147, '且']), ('d', ['[头囗璺]', '且'])))
,'茝'
: (3, (('d', ['卄', '𦣞']), ('d', ['卄', '[左囗颐]'])))
,'菞'
: (3, (('d', ['卄', 37063]), ('d', ['卄', '[头囗黎]'])))
,'蛍'
: (3, (('d', [37044, '虫']), ('d', ['[头囗觉]', '虫'])))
,'蛮'
: (3, (('d', ['亦', '虫']), ('d', ['[头囗鸾]', '虫'])))
,'螢'
: (3, (('d', [37027, '虫']), ('d', ['𤇾', '虫'])))
,'蟿'
: (3, (('d', ['𣪠', '虫']), ('d', ['[头囗擊]', '虫'])))
,'蠃'
: (3, (('st', ['𣎆', '虫']), ('st', ['[上包围囗赢]', '虫'])))
,'裊'
: (3, (('d', [37157, '衣']), ('d', ['[断足鳥]', '衣'])))
,'褮'
: (3, (('d', [37027, '衣']), ('d', ['𤇾', '衣'])))
,'覚'
: (3, (('d', [37044, '見']), ('d', ['[头囗觉]', '見'])))
,'覮'
: (3, (('d', [37027, '見']), ('d', ['𤇾', '見'])))
,'觉'
: (3, (('d', [37044, '见']), ('d', ['[头囗觉]', '见'])))
,'觕'
: (3, (('a', ['牛', '角']), ('a', ['牜', '角'])))
,'謍'
: (3, (('d', [37027, '言']), ('d', ['𤇾', '言'])))
,'謡'
: (3, (('a', ['言', 37021]), ('a', ['言', '䍃'])))
,'谣'
: (3, (('a', ['讠', 37021]), ('a', ['讠', '䍃'])))
,'谸'
: (3, (('a', ['千', '谷']), ('a', ['[撇化千]', '谷'])))
,'豪'
: (3, (('d', [37106, '豕']), ('d', ['[纵三组亠口冖]', '豕'])))
,'賁'
: (3, (('d', ['卉', '貝']), ('d', ['[头囗桒]', '貝'])))
,'賈'
: (3, (('d', ['西', '貝']), ('d', ['覀', '貝'])))
,'賾'
: (3, (('a', ['𦣞', '責']), ('a', ['[左囗颐]', '責'])))
,'贏'
: (3, (('st', ['𣎆', '貝']), ('st', ['[上包围囗赢]', '貝'])))
,'贤'
: (3, (('d', [37144, '贝']), ('d', ['[头囗坚]', '贝'])))
,'赜'
: (3, (('a', ['𦣞', '责']), ('a', ['[左囗颐]', '责'])))
,'赢'
: (3, (('st', ['𣎆', '贝']), ('st', ['[上包围囗赢]', '贝'])))
,'轚'
: (3, (('d', ['𣪠', '車']), ('d', ['[头囗擊]', '車'])))
,'轧'
: (3, (('a', ['车', '㇟']), ('a', ['[左用车]', '㇟'])))
,'轨'
: (3, (('a', ['车', '九']), ('a', ['[左用车]', '九'])))
,'轩'
: (3, (('a', ['车', '干']), ('a', ['[左用车]', '干'])))
,'轪'
: (3, (('a', ['车', '大']), ('a', ['[左用车]', '大'])))
,'轫'
: (3, (('a', ['车', '刃']), ('a', ['[左用车]', '刃'])))
,'转'
: (3, (('a', ['车', '专']), ('a', ['[左用车]', '专'])))
,'轭'
: (3, (('a', ['车', '厄']), ('a', ['[左用车]', '厄'])))
,'轮'
: (3, (('a', ['车', '仑']), ('a', ['[左用车]', '仑'])))
,'软'
: (3, (('a', ['车', '欠']), ('a', ['[左用车]', '欠'])))
,'轱'
: (3, (('a', ['车', '古']), ('a', ['[左用车]', '古'])))
,'轲'
: (3, (('a', ['车', '可']), ('a', ['[左用车]', '可'])))
,'轳'
: (3, (('a', ['车', '卢']), ('a', ['[左用车]', '卢'])))
,'轴'
: (3, (('a', ['车', '由']), ('a', ['[左用车]', '由'])))
,'轵'
: (3, (('a', ['车', '只']), ('a', ['[左用车]', '只'])))
,'轶'
: (3, (('a', ['车', '失']), ('a', ['[左用车]', '失'])))
,'轷'
: (3, (('a', ['车', '乎']), ('a', ['[左用车]', '乎'])))
,'轸'
: (3, (('a', ['车', '㐱']), ('a', ['[左用车]', '㐱'])))
,'轹'
: (3, (('a', ['车', '乐']), ('a', ['[左用车]', '乐'])))
,'轺'
: (3, (('a', ['车', '召']), ('a', ['[左用车]', '召'])))
,'轻'
: (3, (('a', ['车', 37030]), ('a', ['[左用车]', 37030])))
,'轼'
: (3, (('a', ['车', '式']), ('a', ['[左用车]', '式'])))
,'轾'
: (3, (('a', ['车', '至']), ('a', ['[左用车]', '至'])))
,'轿'
: (3, (('a', ['车', '乔']), ('a', ['[左用车]', '乔'])))
,'辀'
: (3, (('a', ['车', '舟']), ('a', ['[左用车]', '舟'])))
,'辁'
: (3, (('a', ['车', '全']), ('a', ['[左用车]', '全'])))
,'辂'
: (3, (('a', ['车', '各']), ('a', ['[左用车]', '各'])))
,'较'
: (3, (('a', ['车', '交']), ('a', ['[左用车]', '交'])))
,'辄'
: (3, (('a', ['车', '耴']), ('a', ['[左用车]', '耴'])))
,'辅'
: (3, (('a', ['车', '甫']), ('a', ['[左用车]', '甫'])))
,'辆'
: (3, (('a', ['车', '两']), ('a', ['[左用车]', '两'])))
,'辊'
: (3, (('a', ['车', '昆']), ('a', ['[左用车]', '昆'])))
,'辋'
: (3, (('a', ['车', '罔']), ('a', ['[左用车]', '罔'])))
,'辌'
: (3, (('a', ['车', '京']), ('a', ['[左用车]', '京'])))
,'辍'
: (3, (('a', ['车', '叕']), ('a', ['[左用车]', '叕'])))
,'辎'
: (3, (('a', ['车', '甾']), ('a', ['[左用车]', '甾'])))
,'辏'
: (3, (('a', ['车', 37121]), ('a', ['[左用车]', 37121])))
,'辐'
: (3, (('a', ['车', '畐']), ('a', ['[左用车]', '畐'])))
,'辑'
: (3, (('a', ['车', '咠']), ('a', ['[左用车]', '咠'])))
,'辒'
: (3, (('a', ['车', '昷']), ('a', ['[左用车]', '昷'])))
,'输'
: (3, (('a', ['车', '俞']), ('a', ['[左用车]', '俞'])))
,'辕'
: (3, (('a', ['车', '袁']), ('a', ['[左用车]', '袁'])))
,'辖'
: (3, (('a', ['车', '害']), ('a', ['[左用车]', '害'])))
,'辗'
: (3, (('a', ['车', '展']), ('a', ['[左用车]', '展'])))
,'辘'
: (3, (('a', ['车', '鹿']), ('a', ['[左用车]', '鹿'])))
,'辙'
: (3, (('a', ['车', 37112]), ('a', ['[左用车]', 37112])))
,'辚'
: (3, (('a', ['车', '粦']), ('a', ['[左用车]', '粦'])))
,'郎'
: (3, (('a', [37105, '阝']), ('a', ['[左囗郎]', '阝'])))
,'郒'
: (3, (('a', [37105, '邑']), ('a', ['[左囗郎]', '邑'])))
,'鄜'
: (3, (('a', ['鹿', '阝']), ('a', ['[左用鹿]', '阝'])))
,'酱'
: (3, (('d', [37194, '酉']), ('d', ['[头囗桨]', '酉'])))
,'醟'
: (3, (('d', [37027, '酉']), ('d', ['𤇾', '酉'])))
,'釁'
: (3, (('d', [37147, 37669]), ('d', ['[头囗璺]', 37669])))
,'釐'
: (3, (('d', [37087, '厘']), ('d', ['[横组未攵]', '厘'])))
,'銮'
: (3, (('d', ['亦', '金']), ('d', ['[头囗鸾]', '金'])))
,'錅'
: (3, (('d', [37063, '金']), ('d', ['[头囗黎]', '金'])))
,'鎐'
: (3, (('a', ['金', 37021]), ('a', ['金', '䍃'])))
,'鎣'
: (3, (('d', [37027, '金']), ('d', ['𤇾', '金'])))
,'雩'
: (3, (('d', ['雨', '亏']), ('d', ['[头用雨]', '亏'])))
,'雪'
: (3, (('d', ['雨', '彐']), ('d', ['[头用雨]', '彐'])))
,'雫'
: (3, (('d', ['雨', '下']), ('d', ['[头用雨]', '下'])))
,'雬'
: (3, (('d', ['雨', '木']), ('d', ['[头用雨]', '木'])))
,'雭'
: (3, (('d', ['雨', '及']), ('d', ['[头用雨]', '及'])))
,'雮'
: (3, (('d', ['雨', '毛']), ('d', ['[头用雨]', '毛'])))
,'雯'
: (3, (('d', ['雨', '文']), ('d', ['[头用雨]', '文'])))
,'雰'
: (3, (('d', ['雨', '分']), ('d', ['[头用雨]', '分'])))
,'雱'
: (3, (('d', ['雨', '方']), ('d', ['[头用雨]', '方'])))
,'雲'
: (3, (('d', ['雨', '云']), ('d', ['[头用雨]', '云'])))
,'雳'
: (3, (('d', ['雨', '历']), ('d', ['[头用雨]', '历'])))
,'雴'
: (3, (('d', ['雨', '立']), ('d', ['[头用雨]', '立'])))
,'雵'
: (3, (('d', ['雨', '央']), ('d', ['[头用雨]', '央'])))
,'零'
: (3, (('d', ['雨', '令']), ('d', ['[头用雨]', '令'])))
,'雷'
: (3, (('d', ['雨', '田']), ('d', ['[头用雨]', '田'])))
,'雸'
: (3, (('d', ['雨', '甘']), ('d', ['[头用雨]', '甘'])))
,'雹'
: (3, (('d', ['雨', '包']), ('d', ['[头用雨]', '包'])))
,'雺'
: (3, (('d', ['雨', '矛']), ('d', ['[头用雨]', '矛'])))
,'電'
: (3, (('d', ['雨', '电']), ('d', ['[头用雨]', '电'])))
,'雼'
: (3, (('d', ['雨', '石']), ('d', ['[头用雨]', '石'])))
,'雽'
: (3, (('d', ['雨', '乎']), ('d', ['[头用雨]', '乎'])))
,'雾'
: (3, (('d', ['雨', '务']), ('d', ['[头用雨]', '务'])))
,'雿'
: (3, (('d', ['雨', '兆']), ('d', ['[头用雨]', '兆'])))
,'需'
: (3, (('d', ['雨', '而']), ('d', ['[头用雨]', '而'])))
,'霁'
: (3, (('d', ['雨', '齐']), ('d', ['[头用雨]', '齐'])))
,'霂'
: (3, (('d', ['雨', '沐']), ('d', ['[头用雨]', '沐'])))
,'霃'
: (3, (('d', ['雨', '沈']), ('d', ['[头用雨]', '沈'])))
,'霄'
: (3, (('d', ['雨', '肖']), ('d', ['[头用雨]', '肖'])))
,'霅'
: (3, (('d', ['雨', '言']), ('d', ['[头用雨]', '言'])))
,'霆'
: (3, (('d', ['雨', '廷']), ('d', ['[头用雨]', '廷'])))
,'震'
: (3, (('d', ['雨', '辰']), ('d', ['[头用雨]', '辰'])))
,'霈'
: (3, (('d', ['雨', '沛']), ('d', ['[头用雨]', '沛'])))
,'霉'
: (3, (('d', ['雨', '每']), ('d', ['[头用雨]', '每'])))
,'霊'
: (3, (('d', ['雨', 37604]), ('d', ['[头用雨]', 37604])))
,'霋'
: (3, (('d', ['雨', '妻']), ('d', ['[头用雨]', '妻'])))
,'霌'
: (3, (('d', ['雨', '周']), ('d', ['[头用雨]', '周'])))
,'霍'
: (3, (('d', ['雨', '隹']), ('d', ['[头用雨]', '隹'])))
,'霎'
: (3, (('d', ['雨', '妾']), ('d', ['[头用雨]', '妾'])))
,'霏'
: (3, (('d', ['雨', '非']), ('d', ['[头用雨]', '非'])))
,'霐'
: (3, (('d', ['雨', '泓']), ('d', ['[头用雨]', '泓'])))
,'霑'
: (3, (('d', ['雨', '沾']), ('d', ['[头用雨]', '沾'])))
,'霓'
: (3, (('d', ['雨', '兒']), ('d', ['[头用雨]', '兒'])))
,'霔'
: (3, (('d', ['雨', '注']), ('d', ['[头用雨]', '注'])))
,'霖'
: (3, (('d', ['雨', '林']), ('d', ['[头用雨]', '林'])))
,'霗'
: (3, (('d', ['雨', '泠']), ('d', ['[头用雨]', '泠'])))
,'霘'
: (3, (('d', ['雨', '洞']), ('d', ['[头用雨]', '洞'])))
,'霙'
: (3, (('d', ['雨', '英']), ('d', ['[头用雨]', '英'])))
,'霚'
: (3, (('d', ['雨', '敄']), ('d', ['[头用雨]', '敄'])))
,'霛'
: (3, (('d', ['雨', '𢏝']), ('d', ['[头用雨]', '𢏝'])))
,'霜'
: (3, (('d', ['雨', '相']), ('d', ['[头用雨]', '相'])))
,'霝'
: (3, (('d', ['雨', '𠱠']), ('d', ['[头用雨]', '𠱠'])))
,'霞'
: (3, (('d', ['雨', '叚']), ('d', ['[头用雨]', '叚'])))
,'霟'
: (3, (('d', ['雨', '洪']), ('d', ['[头用雨]', '洪'])))
,'霠'
: (3, (('d', ['雨', 38214]), ('d', ['[头用雨]', 38214])))
,'霡'
: (3, (('d', ['雨', '脉']), ('d', ['[头用雨]', '脉'])))
,'霢'
: (3, (('d', ['雨', '脈']), ('d', ['[头用雨]', '脈'])))
,'霣'
: (3, (('d', ['雨', '員']), ('d', ['[头用雨]', '員'])))
,'霤'
: (3, (('d', ['雨', '留']), ('d', ['[头用雨]', '留'])))
,'霥'
: (3, (('d', ['雨', '冡']), ('d', ['[头用雨]', '冡'])))
,'霦'
: (3, (('d', ['雨', '彬']), ('d', ['[头用雨]', '彬'])))
,'霧'
: (3, (('d', ['雨', '務']), ('d', ['[头用雨]', '務'])))
,'霨'
: (3, (('d', ['雨', '尉']), ('d', ['[头用雨]', '尉'])))
,'霩'
: (3, (('d', ['雨', '郭']), ('d', ['[头用雨]', '郭'])))
,'霪'
: (3, (('d', ['雨', '淫']), ('d', ['[头用雨]', '淫'])))
,'霫'
: (3, (('d', ['雨', '習']), ('d', ['[头用雨]', '習'])))
,'霬'
: (3, (('d', ['雨', '異']), ('d', ['[头用雨]', '異'])))
,'霭'
: (3, (('d', ['雨', '谒']), ('d', ['[头用雨]', '谒'])))
,'霮'
: (3, (('d', ['雨', '湛']), ('d', ['[头用雨]', '湛'])))
,'霯'
: (3, (('d', ['雨', '登']), ('d', ['[头用雨]', '登'])))
,'霰'
: (3, (('d', ['雨', '散']), ('d', ['[头用雨]', '散'])))
,'霱'
: (3, (('d', ['雨', '矞']), ('d', ['[头用雨]', '矞'])))
,'露'
: (3, (('d', ['雨', '路']), ('d', ['[头用雨]', '路'])))
,'霳'
: (3, (('d', ['雨', '隆']), ('d', ['[头用雨]', '隆'])))
,'霵'
: (3, (('d', ['雨', '戢']), ('d', ['[头用雨]', '戢'])))
,'霶'
: (3, (('d', ['雨', '滂']), ('d', ['[头用雨]', '滂'])))
,'霷'
: (3, (('d', ['雨', '暘']), ('d', ['[头用雨]', '暘'])))
,'霸'
: (3, (('d', ['雨', '䩗']), ('d', ['[头用雨]', '䩗'])))
,'霹'
: (3, (('d', ['雨', '辟']), ('d', ['[头用雨]', '辟'])))
,'霺'
: (3, (('d', ['雨', 38117]), ('d', ['[头用雨]', 38117])))
,'霻'
: (3, (('d', ['雨', '豊']), ('d', ['[头用雨]', '豊'])))
,'霽'
: (3, (('d', ['雨', '齊']), ('d', ['[头用雨]', '齊'])))
,'霾'
: (3, (('d', ['雨', '貍']), ('d', ['[头用雨]', '貍'])))
,'霿'
: (3, (('d', ['雨', 38134]), ('d', ['[头用雨]', 38134])))
,'靀'
: (3, (('d', ['雨', '蒙']), ('d', ['[头用雨]', '蒙'])))
,'靁'
: (3, (('d', ['雨', '畾']), ('d', ['[头用雨]', '畾'])))
,'靂'
: (3, (('d', ['雨', '歷']), ('d', ['[头用雨]', '歷'])))
,'靃'
: (3, (('d', ['雨', '雔']), ('d', ['[头用雨]', '雔'])))
,'靄'
: (3, (('d', ['雨', '謁']), ('d', ['[头用雨]', '謁'])))
,'靇'
: (3, (('d', ['雨', '龍']), ('d', ['[头用雨]', '龍'])))
,'靈'
: (3, (('d', ['雨', 38045]), ('d', ['[头用雨]', 38045])))
,'靊'
: (3, (('d', ['雨', '豐']), ('d', ['[头用雨]', '豐'])))
,'靋'
: (3, (('d', ['雨', '瀝']), ('d', ['[头用雨]', '瀝'])))
,'靌'
: (3, (('d', ['雨', '寳']), ('d', ['[头用雨]', '寳'])))
,'靍'
: (3, (('d', ['雨', '䳡']), ('d', ['[头用雨]', '䳡'])))
,'靎'
: (3, (('d', ['雨', '鵭']), ('d', ['[头用雨]', '鵭'])))
,'靏'
: (3, (('d', ['雨', '鶴']), ('d', ['[头用雨]', '鶴'])))
,'靨'
: (3, (('stl', [37069, '面']), ('stl', ['厭', '面'])))
,'鞗'
: (3, (('a', [39752, 37779]), ('a', ['[横组亻丨]', 37779])))
,'韰'
: (3, (('d', ['𣦼', '韭']), ('d', ['[头囗餐]', '韭'])))
,'頖'
: (3, (('a', ['半', '頁']), ('a', ['[撇化半]', '頁'])))
,'頤'
: (3, (('a', ['𦣞', '頁']), ('a', ['[左囗颐]', '頁'])))
,'颐'
: (3, (('a', ['𦣞', '页']), ('a', ['[左囗颐]', '页'])))
,'颻'
: (3, (('a', [37021, '風']), ('a', ['䍃', '風'])))
,'飖'
: (3, (('a', [37021, '风']), ('a', ['䍃', '风'])))
,'飠'
: (3, (('d', ['人', 37105]), ('msp', ['𩙿'])))
,'餐'
: (3, (('d', ['𣦼', '食']), ('d', ['[头囗餐]', '食'])))
,'饜'
: (3, (('stl', [37069, '食']), ('stl', ['厭', '食'])))
,'驘'
: (3, (('st', ['𣎆', '馬']), ('st', ['[上包围囗赢]', '馬'])))
,'魘'
: (3, (('stl', [37069, '鬼']), ('stl', ['厭', '鬼'])))
,'鯈'
: (3, (('a', [39752, 37926]), ('a', ['[横组亻丨]', 37926])))
,'鯬'
: (3, (('d', [37063, '魚']), ('d', ['[头囗黎]', '魚'])))
,'鰩'
: (3, (('a', ['魚', 37021]), ('a', ['魚', '䍃'])))
,'鲎'
: (3, (('st', [37044, '鱼']), ('st', ['[头囗觉]', '鱼'])))
,'鳐'
: (3, (('a', ['鱼', 37021]), ('a', ['鱼', '䍃'])))
,'鳥'
: (3, (('str', [37157, '灬']), ('str', ['[断足鳥]', '灬'])))
,'鳬'
: (3, (('str', [37157, '几']), ('str', ['[断足鳥]', '几'])))
,'鵉'
: (3, (('d', ['亦', '鳥']), ('d', ['[头囗鸾]', '鳥'])))
,'鵹'
: (3, (('d', [37063, '鳥']), ('d', ['[头囗黎]', '鳥'])))
,'鶯'
: (3, (('d', [37027, '鳥']), ('d', ['𤇾', '鳥'])))
,'鷂'
: (3, (('a', [37021, '鳥']), ('a', ['䍃', '鳥'])))
,'鸁'
: (3, (('st', ['𣎆', '鳥']), ('st', ['[上包围囗赢]', '鳥'])))
,'鸴'
: (3, (('d', [37044, '鸟']), ('d', ['[头囗觉]', '鸟'])))
,'鸾'
: (3, (('d', ['亦', '鸟']), ('d', ['[头囗鸾]', '鸟'])))
,'鹞'
: (3, (('a', [37021, '鸟']), ('a', ['䍃', '鸟'])))
,'麣'
: (3, (('a', ['鹿', '嚴']), ('a', ['[左用鹿]', '嚴'])))
,'黉'
: (3, (('d', [37044, '黄']), ('d', ['[头囗觉]', '黄'])))
,'黎'
: (3, (('d', [37063, 37271]), ('d', ['[头囗黎]', 37271])))
,'黧'
: (3, (('d', [37063, '黑']), ('d', ['[头囗黎]', '黑'])))
,'黶'
: (3, (('stl', [37069, '黑']), ('stl', ['厭', '黑'])))
,'鼖'
: (3, (('d', ['卉', '鼓']), ('d', ['[头囗桒]', '鼓'])))
,'龗'
: (3, (('d', ['雨', 37819]), ('d', ['[头用雨]', 37819])))
,'龺'
: (3, (('d', ['十', '早']), ('d', [37943, '十'])))
,'\ue815'
: (1, ('', []))
,'\ue816'
: (1, ('', []))
,'\ue817'
: (1, ('', []))
,'\ue818'
: (1, ('', []))
,'\ue819'
: (1, ('', []))
,'\ue81a'
: (1, ('', []))
,'\ue81b'
: (1, ('', []))
,'\ue81c'
: (1, ('', []))
,'\ue81d'
: (1, ('', []))
,'\ue81e'
: (1, ('', []))
,'\ue81f'
: (1, ('', []))
,'\ue820'
: (1, ('', []))
,'\ue821'
: (1, ('', []))
,'\ue822'
: (1, ('', []))
,'\ue823'
: (1, ('', []))
,'\ue824'
: (1, ('', []))
,'\ue825'
: (1, ('', []))
,'\ue826'
: (1, ('', []))
,'\ue827'
: (1, ('', []))
,'\ue828'
: (1, ('', []))
,'\ue829'
: (1, ('', []))
,'\ue82a'
: (1, ('', []))
,'\ue82b'
: (1, ('', []))
,'\ue82c'
: (1, ('', []))
,'\ue82d'
: (1, ('', []))
,'\ue82e'
: (1, ('', []))
,'\ue82f'
: (1, ('', []))
,'\ue830'
: (1, ('', []))
,'\ue831'
: (1, ('', []))
,'\ue832'
: (1, ('', []))
,'\ue833'
: (1, ('', []))
,'\ue834'
: (1, ('', []))
,'\ue835'
: (1, ('', []))
,'\ue836'
: (1, ('', []))
,'\ue837'
: (1, ('', []))
,'\ue838'
: (1, ('', []))
,'\ue839'
: (1, ('', []))
,'\ue83a'
: (1, ('', []))
,'\ue83b'
: (1, ('', []))
,'\ue83c'
: (1, ('', []))
,'\ue83d'
: (1, ('', []))
,'\ue83e'
: (1, ('', []))
,'\ue83f'
: (1, ('', []))
,'\ue840'
: (1, ('', []))
,'\ue841'
: (1, ('', []))
,'\ue842'
: (1, ('', []))
,'\ue843'
: (1, ('', []))
,'\ue844'
: (1, ('', []))
,'\ue845'
: (1, ('', []))
,'\ue846'
: (1, ('', []))
,'\ue847'
: (1, ('', []))
,'\ue848'
: (1, ('', []))
,'\ue849'
: (1, ('', []))
,'\ue84a'
: (1, ('', []))
,'\ue84b'
: (1, ('', []))
,'\ue84c'
: (1, ('', []))
,'\ue84d'
: (1, ('', []))
,'\ue84e'
: (1, ('', []))
,'\ue84f'
: (1, ('', []))
,'\ue850'
: (1, ('', []))
,'\ue851'
: (1, ('', []))
,'\ue852'
: (1, ('', []))
,'\ue853'
: (1, ('', []))
,'\ue854'
: (1, ('', []))
,'\ue855'
: (1, ('', []))
,'\ue856'
: (1, ('', []))
,'\ue857'
: (1, ('', []))
,'\ue858'
: (1, ('', []))
,'\ue859'
: (1, ('', []))
,'\ue85a'
: (1, ('', []))
,'\ue85b'
: (1, ('', []))
,'\ue85c'
: (1, ('', []))
,'\ue85d'
: (1, ('', []))
,'\ue85e'
: (1, ('', []))
,'\ue85f'
: (1, ('', []))
,'\ue860'
: (1, ('', []))
,'\ue861'
: (1, ('', []))
,'\ue862'
: (1, ('', []))
,'\ue863'
: (1, ('', []))
,'\ue864'
: (1, ('', []))
,'郎'
: (1, ('', []))
,'凉'
: (1, ('', []))
,'秊'
: (1, ('', []))
,'裏'
: (1, ('', []))
,'隣'
: (1, ('', []))
,'兀'
: (1, ('', []))
,'嗀'
: (1, ('', []))
,'礼'
: (1, ('', []))
,'蘒'
: (1, ('', []))
,'𠏉'
: (3, (('a', [97020, '余']), ('a', ['龺', '余'])))
,'𠒎'
: (3, (('str', [37157, '儿']), ('str', ['[断足鳥]', '儿'])))
,'𡜦'
: (3, (('d', ['卉', '女']), ('d', ['[头囗桒]', '女'])))
,'𣴎'
: (3, (('d', ['羊', '水']), ('d', ['⺷', '水'])))
,'𤇾'
: (3, (('d', ['炏', '⺆']), ('d', ['炏', '冖'])))
,'𤘘'
: (3, (('a', ['牛', '口']), ('a', ['牜', '口'])))
,'𤘪'
: (3, (('a', ['牛', '丹']), ('a', ['牜', '丹'])))
,'𤙥'
: (3, (('a', ['牛', '克']), ('a', ['牜', '克'])))
,'𤙴'
: (3, (('a', ['牛', '卓']), ('a', ['牜', '卓'])))
,'𤚗'
: (3, (('a', ['牛', '宣']), ('a', ['牜', '宣'])))
,'𤛔'
: (3, (('a', ['牛', '曼']), ('a', ['牜', '曼'])))
,'𤛘'
: (3, (('a', ['牛', 90394]), ('a', ['牜', 90394])))
,'𤜆'
: (3, (('a', ['牛', '龍']), ('a', ['牜', '龍'])))
,'𥀬'
: (3, (('d', [37069, '皮']), ('d', ['厭', '皮'])))
,'𥥖'
: (3, (('d', [65737, '古']), ('d', ['穴', '古'])))
,'𥥷'
: (3, (('d', [65737, '豆']), ('d', ['穴', '豆'])))
,'𥦁'
: (3, (('d', [65737, '甬']), ('d', ['穴', '甬'])))
,'𥦌'
: (3, (('d', [65737, '弄']), ('d', ['穴', '弄'])))
,'𥦬'
: (3, (('d', [65737, '八']), ('d', ['穴', '八'])))
,'𥧄'
: (3, (('d', [65737, 45797]), ('d', ['穴', 45797])))
,'𥧔'
: (3, (('d', [65737, '氣']), ('d', ['穴', '氣'])))
,'𥿠'
: (3, (('a', ['糸', '布']), ('a', ['糹', '布'])))
,'𥿻'
: (3, (('a', ['糸', '旨']), ('a', ['糹', '旨'])))
,'𦀗'
: (3, (('a', ['糸', '赤']), ('a', ['糹', '赤'])))
,'𦁠'
: (3, (('a', ['糸', '明']), ('a', ['糹', '明'])))
,'𦃭'
: (3, (('a', ['糸', '島']), ('a', ['糹', '島'])))
,'𦎾'
: (3, (('a', ['羊', '犀']), ('a', ['⺶', '犀'])))
,'𦔒'
: (3, (('a', [37009, '兹']), ('a', ['耒', '兹'])))
,'𧿳'
: (3, (('a', ['足', '弗']), ('a', ['⻊', '弗'])))
,'𧿹'
: (3, (('a', ['足', '母']), ('a', ['⻊', '母'])))
,'𨀉'
: (3, (('a', ['足', '宁']), ('a', ['⻊', '宁'])))
,'𨀞'
: (3, (('a', ['足', '聿']), ('a', ['⻊', '聿'])))
,'𨀣'
: (3, (('a', ['足', '企']), ('a', ['⻊', '企'])))
,'𨀤'
: (3, (('a', ['足', '耒']), ('a', ['⻊', '耒'])))
,'𨁈'
: (3, (('a', ['足', '更']), ('a', ['⻊', '更'])))
,'𨁍'
: (3, (('a', ['足', '見']), ('a', ['⻊', '見'])))
,'𨁸'
: (3, (('a', ['足', 90024]), ('a', ['⻊', 90024])))
,'𨂃'
: (3, (('a', ['足', '朋']), ('a', ['⻊', '朋'])))
,'𨂊'
: (3, (('a', ['足', '周']), ('a', ['⻊', '周'])))
,'𨂐'
: (3, (('a', ['足', '來']), ('a', ['⻊', '來'])))
,'𨂰'
: (3, (('a', ['足', '契']), ('a', ['⻊', '契'])))
,'𨂻'
: (3, (('a', ['足', 90297]), ('a', ['⻊', 90297])))
,'𨂽'
: (3, (('a', ['足', '泵']), ('a', ['⻊', '泵'])))
,'𨂾'
: (3, (('a', ['足', '南']), ('a', ['⻊', '南'])))
,'𨃟'
: (3, (('a', ['足', '般']), ('a', ['⻊', '般'])))
,'𨃩'
: (3, (('a', ['足', '扇']), ('a', ['⻊', '扇'])))
,'𨃴'
: (3, (('a', ['足', '骨']), ('a', ['⻊', '骨'])))
,'𨄮'
: (3, (('a', ['足', '率']), ('a', ['⻊', '率'])))
,'𨅏'
: (3, (('a', ['足', '嵐']), ('a', ['⻊', '嵐'])))
,'𨅔'
: (3, (('a', ['足', 60966]), ('a', ['⻊', 60966])))
,'𨅝'
: (3, (('a', ['足', 92314]), ('a', ['⻊', 92314])))
,'𨅯'
: (3, (('a', ['足', '華']), ('a', ['⻊', '華'])))
,'𨆉'
: (3, (('a', ['足', 90116]), ('a', ['⻊', 90116])))
,'𨆯'
: (3, (('a', ['足', '僕']), ('a', ['⻊', '僕'])))
,'𨆼'
: (3, (('a', ['足', '㕑']), ('a', ['⻊', '㕑'])))
,'𨈇'
: (3, (('a', ['足', 60112]), ('a', ['⻊', 60112])))
,'𨐈'
: (3, (('a', ['车', '光']), ('a', ['[左用车]', '光'])))
,'𨯪'
: (3, (('a', ['金', 97020, '人', '羽']), ('a', ['金', '龺', '人', '羽'])))
,'𩁹'
: (3, (('d', ['雨', '于']), ('d', ['[头用雨]', '于'])))
,'𩂈'
: (3, (('d', ['雨', '心']), ('d', ['[头用雨]', '心'])))
,'𩂋'
: (3, (('d', ['雨', '斤']), ('d', ['[头用雨]', '斤'])))
,'𩂓'
: (3, (('d', ['雨', '冬']), ('d', ['[头用雨]', '冬'])))
,'𩂯'
: (3, (('d', ['雨', '休']), ('d', ['[头用雨]', '休'])))
,'𩂰'
: (3, (('d', ['雨', '如']), ('d', ['[头用雨]', '如'])))
,'𩂱'
: (3, (('d', ['雨', '衣']), ('d', ['[头用雨]', '衣'])))
,'𩃀'
: (3, (('d', ['雨', '延']), ('d', ['[头用雨]', '延'])))
,'𩃤'
: (3, (('d', ['雨', '奇']), ('d', ['[头用雨]', '奇'])))
,'𩃥'
: (3, (('d', ['雨', '佩']), ('d', ['[头用雨]', '佩'])))
,'𩃬'
: (3, (('d', ['雨', 99608]), ('d', ['[头用雨]', 99608])))
,'𩃭'
: (3, (('d', ['雨', '松']), ('d', ['[头用雨]', '松'])))
,'𩄍'
: (3, (('d', ['雨', '秋']), ('d', ['[头用雨]', '秋'])))
,'𩄐'
: (3, (('d', ['雨', '降']), ('d', ['[头用雨]', '降'])))
,'𩄼'
: (3, (('d', ['雨', '渄']), ('d', ['[头用雨]', '渄'])))
,'𩅍'
: (3, (('d', ['雨', '曼']), ('d', ['[头用雨]', '曼'])))
,'𩅛'
: (3, (('d', ['雨', '逢']), ('d', ['[头用雨]', '逢'])))
,'𩅰'
: (3, (('d', ['雨', '斯']), ('d', ['[头用雨]', '斯'])))
,'𩆨'
: (3, (('d', ['雨', '鋒']), ('d', ['[头用雨]', '鋒'])))
,'𩗏'
: (3, (('d', ['西', '風']), ('d', ['覀', '風'])))
,'𩛩'
: (3, (('a', [37004, '夾']), ('a', ['飠', '夾'])))
,'𩜇'
: (3, (('a', [37004, '卷']), ('a', ['飠', '卷'])))
,'𩜙'
: (3, (('a', [37004, '尭']), ('a', ['飠', '尭'])))
,'𩜠'
: (3, (('a', [37004, '岩']), ('a', ['飠', '岩'])))
,'𩜲'
: (3, (('a', [37004, '复']), ('a', ['飠', '复'])))
,'𩝐'
: (3, (('a', [37004, '兹']), ('a', ['飠', '兹'])))
,'𩟔'
: (3, (('a', [37004, 60986]), ('a', ['飠', 60986])))
,'𪂂'
: (3, (('a', [97020, '鳥']), ('a', ['龺', '鳥'])))
,'𪊟'
: (3, (('a', ['鹿', '生']), ('a', ['[左用鹿]', '生'])))
,'𪊶'
: (3, (('a', ['鹿', '廷']), ('a', ['[左用鹿]', '廷'])))
,'𪊺'
: (3, (('a', ['鹿', '吝']), ('a', ['[左用鹿]', '吝'])))
,'𪋟'
: (3, (('a', ['鹿', '章']), ('a', ['[左用鹿]', '章'])))
})
def main(nm4cls, /, *args, **kwds):
    cls = globals()[nm4cls]
    sf = cls(*args, **kwds)
    sf.load()
    if 0b0:
        print(sf.bk2f_bks['㐍'])
        print(sf.bk2js['㐍'])
        op, bks = sf.bk2f_bks['㐍']
        for bk in bks:
            print(sf.bk2js.get(bk))
        return
    sf.deduce()
    i = 0
    while not sf.tgt_bks__with_num_diffs_ge2:
        i += 1
        print(f'loop:{i}')
        if not sf.tgt_bk2js2src_bks:
            break
        sf.merge()
        sf.deduce()

    (bugss, tgt_bk2js2src_bks) = (sf.bugss, sf.tgt_bk2js2src_bks)
            #bugss :: [笔顺码未知子部件唯一囗囗推导过程异常囗囗无法确定待定子部件笔顺码的长度, 笔顺码未知子部件唯一囗囗推导结果异常囗囗笔顺码加法结果不一致, 所有子部件笔顺码已知囗囗笔顺码加法结果囗不一致]
    bug_strs = '笔顺码未知子部件唯一囗囗推导过程异常囗囗无法确定待定子部件笔顺码的长度,笔顺码未知子部件唯一囗囗推导结果异常囗囗笔顺码加法结果不一致,所有子部件笔顺码已知囗囗笔顺码加法结果囗不一致'.split(',')
    assert len(bugss) == len(bug_strs)
    (lens4bugss, tgt_bk2js2count) = (sf.lens4bugss, sf.tgt_bk2js2count)
    tgt_bks__with_num_diffs_ge2 = sf.tgt_bks__with_num_diffs_ge2
    tgt_bk2js = sf.tgt_bk2js
    tgt_bk2js__acc = sf.tgt_bk2js__acc

    if 1:
        print(lens4bugss)

        ######################
        print('tgt_bks__with_num_diffs_ge2')
        print(len(tgt_bks__with_num_diffs_ge2))
        print(repr(tgt_bks__with_num_diffs_ge2))
        ######################
        #for bugs in bugss:
        for bugs, bug_str in zip(bugss, bug_strs):
            print(bug_str)
            print(bugs)
        ######################
        print('推导出的部件笔顺码tgt_bk2js')
        print(len(tgt_bk2js))
        print(stable_repr__expand_top_layer(tgt_bk2js))

        ######################
        print('num_diffs2tgt_bk2js2src_bks')
            #推导出来的笔顺码分歧度到子部件相关信息
        #print(stable_repr__expand_top_layer(sf.num_diffs2tgt_bk2js2src_bks))
        for num_diffs, _tgt_bk2js2src_bks in sorted(sf.num_diffs2tgt_bk2js2src_bks.items()):
            print(f'{num_diffs}#')
            print(stable_repr__expand_top_layer(_tgt_bk2js2src_bks))

        ######################
        #推导出的部件笔顺码，并原有的拆分，输出为可读行格式
        print('推导出的部件笔顺码囗囗累积tgt_bk2js__acc')
        print(len(tgt_bk2js__acc))
        #print(stable_repr__expand_top_layer(tgt_bk2js__acc))
        show_format_lines(sf.bk2f_bks, tgt_bk2js__acc)


        r'''[[[
[0, 205]
113
'⺆,⺙,𠚤,𠩵,𤴡,𦍍,12203,12541,21272,37036,37060,37084,37174,37281,39068,42820,46156,48555,65580,90014,91311,99697,99787'
[]
['㐍', '㐧', '㓁', '㝳', '㟗', '㡀', '㡬', '㢤', '㦱', '㨌', '㪜', '㫄', '㸨', '㸹', '㸿', '㹄', '㹌', '㹍', '㹎', '㹗', '㹚', '㹛', '䄗', '䄞', '䈠', '䍩', '䍼', '䏿', '䒿', '䘮', '䞸', '䟫', '䟸', '䟹', '䠌', '䠔', '䠘', '䠜', '䠡', '䠪', '䠫', '䠭', '䠯', '䠰', '䢇', '䢥', '䨙', '䨩', '䨱', '䨵', '䨶', '䨷', '䨸', '䨹', '䪟', '䰍', '丐', '且', '世', '丘', '为', '主', '乆', '义', '亊', '亜', '亞', '亡', '亾', '兆', '兦', '冘', '凢', '升', '午', '半', '卿', '及', '发', '囟', '囬', '囱', '垂', '夂', '大', '央', '失', '头', '嬲', '嬴', '孁', '宀', '屮', '带', '幽', '广', '开', '弃', '弐', '忄', '或', '户', '手', '扌', '才', '敘', '敳', '斗', '未', '朱', '武', '氷', '牧', '牬', '犕', '犦', '犮', '班', '瓜', '生', '甪', '甶', '畫', '畵', '畿', '白', '秉', '罒', '羊', '羋', '羌', '羐', '羟', '羲', '羸', '聼', '聽', '育', '肻', '肾', '脊', '膂', '臝', '臧', '自', '良', '蠃', '血', '豸', '貮', '贏', '赢', '車', '轧', '轻', '辏', '辙', '遙', '雟', '霊', '霛', '霝', '霠', '霺', '霿', '靈', '飛', '驘', '鰴', '鸁', '黽', '鼎', '鼑', '龗', '龙', '﨤', '𠂤', '𠕇', '𠧧', '𡨴', '𡯁', '𢳆', '𣁋', '𣇸', '𣚺', '𤛘', '𤪖', '𥦬', '𦆮', '𦤑', '𦱳', '𧀎', '𨁸', '𨂻', '𨅔', '𨅝', '𨆉', '𨈇', '𨗈', '𨗉', '𨯿', '𨰹', '𩃬', '𩱳', '𪑛']

        #]]]'''#'''


def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__


from script.hz.汉字笔顺码初步分解囗囗部件笔顺码 import *
