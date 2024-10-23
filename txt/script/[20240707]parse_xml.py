#__all__:goto
r'''[[[
e script/parse_xml.py

script.parse_xml
py -m nn_ns.app.debug_cmd   script.parse_xml -x
py -m nn_ns.app.doctest_cmd script.parse_xml:__doc__ -ht


mkdir ../../python3_src/seed/recognize/xml/
mv -iv script/parse_xml.py   'script/[20240707]parse_xml.py'
cp -iv  'script/[20240707]parse_xml.py'   ../../python3_src/seed/recognize/xml/SimpleParser4XML.py
.+1,$s/script[.]parse_xml/seed.recognize.xml.SimpleParser4XML/g



[[

bs4 依赖于 lxml，但还是很慢

假设xml用于保存数据
    (例如:UCD::ucd.nounihan.grouped.xml/5.1M)

假设:极简格式:
    * xxx:没有:文本:<...>之外只能是空格
        有序序列<<==children
        无序属性<<==nm2s
        并非超文本==>>没有:外部文本
       由于有『<description>Unicode 14.0.0</description>』
       现加入 text_tag
    * 没有:引用:『&...;』
    * 没有:真值属性，即所有属性需得显式赋值『=』
    * 没有:单引号属性值，即只能用双引号
    * 没有:无引号属性值，即必须用双引号
    * 没有:转义序列，即属性值字面上不含『\』『"』,允许『'』
        由于有:『90』vs『90'』==>>允许『'』
      <cjk-radical number="90" radical="2F59" ideograph="723F"/>
      <cjk-radical number="90'" radical="2EA6" ideograph="4E2C"/>
    * 没有:标签名规范化，即标签名必须严格配对
]]

[[
view /sdcard/0my_files/unzip/unicode14_0/xml/ucd.nounihan.grouped.xml
===

<?xml version="1.0" encoding="utf-8" standalone="yes"?>

<!-- © 2020 Unicode®, Inc. -->
<!-- For terms of use, see http://www.unicode.org/terms_of_use.html -->


<ucd xmlns="http://www.unicode.org/ns/2003/ucd/1.0">
   <description>Unicode 14.0.0</description>
   <repertoire>
...
      <group age="3.0" JSN="" gc="Lo" ccc="0" dt="none" dm="#" nt="None" nv="NaN" bc="AL" bpt="n" bpb="#" Bidi_M="N" bmg="" suc="#" slc="#" stc="#" uc="#" lc="#" tc="#" scf="#" cf="#" jt="U" jg="No_Joining_Group" ea="N" lb="AL" sc="Thaa" scx="Thaa" Dash="N" WSpace="N" Hyphen="N" QMark="N" Radical="N" Ideo="N" UIdeo="N" IDSB="N" IDST="N" hst="NA" DI="N" ODI="N" Alpha="Y" OAlpha="N" Upper="N" OUpper="N" Lower="N" OLower="N" Math="N" OMath="N" Hex="N" AHex="N" NChar="N" VS="N" Bidi_C="N" Join_C="N" Gr_Base="Y" Gr_Ext="N" OGr_Ext="N" Gr_Link="N" STerm="N" Ext="N" Term="N" Dia="N" Dep="N" IDS="Y" OIDS="N" XIDS="Y" IDC="Y" OIDC="N" XIDC="Y" SD="N" LOE="N" Pat_WS="N" Pat_Syn="N" GCB="XX" WB="LE" SB="LE" CE="N" Comp_Ex="N" NFC_QC="Y" NFD_QC="Y" NFKC_QC="Y" NFKD_QC="Y" XO_NFC="N" XO_NFD="N" XO_NFKC="N" XO_NFKD="N" FC_NFKC="#" CI="N" Cased="N" CWCF="N" CWCM="N" CWKCF="N" CWL="N" CWT="N" CWU="N" NFKC_CF="#" InSC="Other" InPC="NA" PCM="N" vo="R" RI="N" blk="Thaana" isc="" na1="" Emoji="N" EPres="N" EMod="N" EBase="N" EComp="N" ExtPict="N">
         <char cp="0780" na="THAANA LETTER HAA"/>
         <char cp="0781" na="THAANA LETTER SHAVIYANI"/>
         <char cp="0782" na="THAANA LETTER NOONU"/>
         <char cp="0783" na="THAANA LETTER RAA"/>
         <char cp="0784" na="THAANA LETTER BAA"/>
         <char cp="0785" na="THAANA LETTER LHAVIYANI"/>
         <char cp="0786" na="THAANA LETTER KAAFU"/>
         <char cp="0787" na="THAANA LETTER ALIFU"/>
         <char cp="0788" na="THAANA LETTER VAAVU"/>
         <char cp="0789" na="THAANA LETTER MEEMU"/>
         <char cp="078A" na="THAANA LETTER FAAFU"/>
         <char cp="078B" na="THAANA LETTER DHAALU"/>
         <char cp="078C" na="THAANA LETTER THAA"/>
         <char cp="078D" na="THAANA LETTER LAAMU"/>
         <char cp="078E" na="THAANA LETTER GAAFU"/>
         <char cp="078F" na="THAANA LETTER GNAVIYANI"/>
         <char cp="0790" na="THAANA LETTER SEENU"/>
         <char cp="0791" na="THAANA LETTER DAVIYANI"/>
         <char cp="0792" na="THAANA LETTER ZAVIYANI"/>
         <char cp="0793" na="THAANA LETTER TAVIYANI"/>
         <char cp="0794" na="THAANA LETTER YAA"/>
         <char cp="0795" na="THAANA LETTER PAVIYANI"/>
         <char cp="0796" na="THAANA LETTER JAVIYANI"/>
         <char cp="0797" na="THAANA LETTER CHAVIYANI"/>
         <char cp="0798" na="THAANA LETTER TTAA"/>
         <char cp="0799" na="THAANA LETTER HHAA"/>
         <char cp="079A" na="THAANA LETTER KHAA"/>
         <char cp="079B" na="THAANA LETTER THAALU"/>
         <char cp="079C" na="THAANA LETTER ZAA"/>
         <char cp="079D" na="THAANA LETTER SHEENU"/>
         <char cp="079E" na="THAANA LETTER SAADHU"/>
         <char cp="079F" na="THAANA LETTER DAADHU"/>
         <char cp="07A0" na="THAANA LETTER TO"/>
         <char cp="07A1" na="THAANA LETTER ZO"/>
         <char cp="07A2" na="THAANA LETTER AINU"/>
         <char cp="07A3" na="THAANA LETTER GHAINU"/>
         <char cp="07A4" na="THAANA LETTER QAAFU"/>
         <char cp="07A5" na="THAANA LETTER WAAVU"/>
         <char cp="07A6" na="THAANA ABAFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07A7" na="THAANA AABAAFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07A8" na="THAANA IBIFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07A9" na="THAANA EEBEEFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07AA" na="THAANA UBUFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07AB" na="THAANA OOBOOFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07AC" na="THAANA EBEFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07AD" na="THAANA EYBEYFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07AE" na="THAANA OBOFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07AF" na="THAANA OABOAFILI" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07B0" na="THAANA SUKUN" gc="Mn" bc="NSM" jt="T" lb="CM" OAlpha="Y" Gr_Base="N" Gr_Ext="Y" Dia="Y" IDS="N" XIDS="N" GCB="EX" WB="Extend" SB="EX" CI="Y"/>
         <char cp="07B1" age="3.2" na="THAANA LETTER NAA"/>
         <reserved first-cp="07B2" last-cp="07BF" age="unassigned" na="" gc="Cn" lb="XX" sc="Zzzz" scx="Zzzz" Alpha="N" Gr_Base="N" IDS="N" XIDS="N" IDC="N" XIDC="N" WB="XX" SB="XX"/>
      </group>
...
   </repertoire>
   <blocks>
      <block first-cp="0000" last-cp="007F" name="Basic Latin"/>
...
   </blocks>
   <named-sequences>
      <named-sequence name="ARABIC SEQUENCE NOON WITH KEHEH" cps="0646 06A9"/>
...
   </named-sequences>
   <normalization-corrections>
      <normalization-correction cp="F951" old="96FB" new="964B" version="3.2.0"/>
...
   </normalization-corrections>
   <standardized-variants>
      <standardized-variant cps="0030 FE00" desc="short diagonal stroke form" when=""/>
...
   </standardized-variants>
   <cjk-radicals>
      <cjk-radical number="1" radical="2F00" ideograph="4E00"/>
...
   </cjk-radicals>
   <emoji-sources>
      <emoji-source unicode="0023 20E3" docomo="F985" kddi="F489" softbank="F7B0"/>
...
   </emoji-sources>
</ucd>


]]




py_adhoc_call   script.parse_xml   ,parse_xml__ipath --encoding:u8   :/sdcard/0my_files/unzip/unicode14_0/xml/ucd.nounihan.grouped.xml  +to_strip_gap_txt +to_drop_space_gap_txt | more


#]]]'''
__all__ = r'''
ParseFail
SimpleParser4XML
    simple_parser4XML
        parse_xml__ipath
            parse_xml__ifile
                parse_xml__PeekableIterator



tag_prefixes
tag_suffixess

iter_chars5ifile_

is_start_with
    try_skip_prefix_
skip_while_
    skip_spaces
read_while_

'''.split()#'''
__all__
from seed.iters.PeekableIterator import PeekableIterator, echo_or_mk_PeekableIterator
from seed.tiny_.check import check_type_is, check_int_ge
from collections import OrderedDict

_i2case4w = 'WGMQ'
    #W: normal tag/whole_tree
    #G: text tag/gap
    #M: comment tag
    #Q: decl tag
_jk2case = 'FCDSH'
    #footer: </footer>
    #comment: <!--comment-->
    #decl: <?decl?>
    #solo: <solo/>
    #header: <header/>
_i2case4v = 'FCDSHT'
    #++text
assert _i2case4v[:-1] == _jk2case
assert len(__:=_i2case4w+_i2case4v) == len({*__})

_tag_prefix_suffixes = r'''
</ >
,<!-- -->
,<? ?>
,< /> >
'''#'''

def __():
    tag_prefixes = []
    tag_suffixess = []
    for s in _tag_prefix_suffixes.split(','):
        [prefix, *suffixes] = s.split()
        assert suffixes
        tag_prefixes.append(prefix)
        tag_suffixess.append(suffixes)
    tag_prefixes = tuple(tag_prefixes)
    tag_suffixess = tuple(map(tuple, tag_suffixess))
    return (tag_prefixes, tag_suffixess)
(tag_prefixes, tag_suffixess) = __()
assert tag_prefixes[-1] == '<'
assert tag_suffixess[-1] == ('/>', '>')


def iter_chars5ifile_(ifile, /):
    while (c := ifile.read(1)):
        yield c
def is_start_with(prefix, it, /):
    L = len(prefix)
    t = it.peek_le(L)
    return len(t) == L and prefix == ''.join(t)
def try_skip_prefix_(prefix, it, /):
    if not is_start_with(prefix, it):
        return False
    L = len(prefix)
    it.read_le(L)
    return True
def _select_prefix_(prefixes, it, /):
    for j, prefix in enumerate(prefixes):
        if try_skip_prefix_(prefix, it):
            return (j, prefix)
    raise ParseFail
def skip_while_(f, it, /):
    while not it.is_empty():
        c = it.head
        if not f(c):
            break
        it.read1()
def read_while_(f, it, /):
    cs = []
    while not it.is_empty():
        c = it.head
        if not f(c):
            break
        cs.append(c)
        it.read1()
    s = ''.join(cs)
    return s


def skip_spaces(it, /):
    skip_while_(str.isspace, it)
def _read_endby_(suffix, it, /):
    if not suffix:raise ValueError(suffix)
    L = len(suffix)
    cs = []
    while not try_skip_prefix_(suffix, it):
        c = it.head
        cs.append(c)
        it.read1()
        if not it.len_ge(L):
            raise ParseFail
    s = ''.join(cs)
    return s



class ParseFail(Exception):pass

class SimpleParser4XML:
    def parse_xml__ipath(sf, ipath, /, *, encoding, **kwds4parse):
        '-> whole_tags6toplevel/[whole_tag] #[whole_tag==(("W",nm4tag,nm2s,children/[whole_tag])|("M",comment_txt)|("Q",nm4tag,nm2s))]'
        with open(ipath, 'rt', encoding=encoding) as ifile:
            whole_tags6toplevel = sf.parse_xml__ifile(ifile, **kwds4parse)
        return whole_tags6toplevel
    def parse_xml__ifile(sf, ifile, /, **kwds4parse):
        '-> whole_tags6toplevel/[whole_tag] #[whole_tag==(("W",nm4tag,nm2s,children/[whole_tag])|("M",comment_txt)|("Q",nm4tag,nm2s))]'
        it = iter_chars5ifile_(ifile)
        it = echo_or_mk_PeekableIterator(it)
        return sf.parse_xml__PeekableIterator(it, **kwds4parse)

    def parse_xml__PeekableIterator(sf, it, /, *, to_strip_gap_txt=False, to_drop_space_gap_txt=False):
        #, **kwds4parse=[def]=to_strip_gap_txt, to_drop_space_gap_txt
        '-> whole_tags6toplevel/[whole_tag] #[whole_tag==(("W",nm4tag,nm2s,may_children/may[whole_tag])|("G",gap_txt)|("M",comment_txt)|("Q",nm4tag,nm2s))]'
        '#假设:标签名必须严格配对'
        check_type_is(PeekableIterator, it)
        check_type_is(bool, to_strip_gap_txt)
        check_type_is(bool, to_drop_space_gap_txt)


        tagss = stack = [[]]
            # :: [[(whole_tag|tag)]]
            # [tagss[i] is partial-children of tagss[i-1][-1]]
        bbb = to_strip_gap_txt or to_drop_space_gap_txt
        try:
            for u, tag in enumerate(sf._parse_tags(it)):
                (case4v, nm4tag_or_comment_or_gaptxt, may_nm2s) = tag
                assert case4v in _i2case4v
                assert (u&1 == 0) is (case4v == 'T')
                if bbb and (case4v == 'T'):
                    gap_txt = tag[1]
                    if to_strip_gap_txt:
                        gap_txt = gap_txt.strip()
                    #
                    if to_drop_space_gap_txt:
                        if not gap_txt or gap_txt.isspace():
                            #drop
                            continue
                    tag = (case4v, gap_txt, may_nm2s)
                tag
                sf._update_tagss(tagss, tag, case4v)
            if not len(tagss) == 1:raise ParseFail
        except ParseFail:
            raise ParseFail(tagss)
        [whole_tags6toplevel] = tagss
        return whole_tags6toplevel
    def _update_tagss(sf, tagss, tag, c, /):
        if c == 'T':
            gap_text_tag = tag
            (_case4tag, gap_txt, _) = gap_text_tag
            whole_tag = (case4w:='G', gap_txt)
        elif c == 'F':
            footer = tag
            #close/exit
            (case4v, nm4tag, may_nm2s) = tag
            if not may_nm2s is None:raise 000
            if len(tagss) == 1:raise ParseFail
            children = tagss.pop()
            header = tagss[-1].pop()
            assert header[0] == 'H'
            if not header[1] == footer[1]:raise ParseFail
                #假设:标签名必须严格配对
            (_case4tag, nm4tag, nm2s) = header
            whole_tag = (case4w:='W', nm4tag, nm2s, children)
        elif c == 'H':
            header = tag
            #open/enter
            tagss[-1].append(header)
            tagss.append([])
            return
        elif c == 'S':
            solo = tag
            (_case4tag, nm4tag, nm2s) = solo
            whole_tag = (case4w:='W', nm4tag, nm2s, may_children:=None)
        elif c == 'C':
            comment_tag = tag
            (_case4tag, comment_txt, _) = comment_tag
            whole_tag = (case4w:='M', comment_txt)
        elif c == 'D':
            decl = tag
            (_case4tag, nm4tag, nm2s) = decl
            whole_tag = (case4w:='Q', nm4tag, nm2s)
        else:
            raise 000
        whole_tag
        assert whole_tag[0] in _i2case4w #'WGMQ'
        tagss[-1].append(whole_tag)
        return
    #end-def _update_tagss(sf, tagss, c, /):


    def _parse_tags(sf, it, /):
        '-> Iter tag/(case4v/"FCDSHT", nm4tag_or_comment_or_gaptxt, may_nm2s)'
        while 1:
            if 0:
                skip_spaces(it)
            else:
                gap_txt = sf._parse_gap_text(it)
                gap_text_tag = (case4v:='T', gap_txt, None)
                yield gap_text_tag

            if it.is_empty():
                break
            tag = sf._parse_tag(it)
            yield tag
    def _parse_tag(sf, it, /):
        '-> tag/(case4tag/"FCDSH", nm4tag_or_comment/(nm4tag|comment), may_nm2s)'
        (j, prefix) = _select_prefix_(tag_prefixes, it)
        suffixes = tag_suffixess[j]
        skip_spaces(it)
        if prefix == '<!--':
            [suffix] = suffixes
            k = 0
            comment = _read_endby_(suffix, it)
            nm4tag_or_comment = comment
            may_nm2s = None
        else:
            nm4tag = sf._parse_nm(it)
            nm4tag_or_comment = nm4tag
            if prefix == '</':
                may_nm2s = None
            else:
                skip_spaces(it)
                nm2s = sf._parse_dict(it)
                may_nm2s = nm2s
            may_nm2s

            skip_spaces(it)
            (k, suffix) = _select_prefix_(suffixes, it)
        nm4tag_or_comment
        may_nm2s
        k, suffix
        oe = ' '.join([prefix, suffix])
        if k:
            assert oe == '< >'
            assert j == 3
        else:
            assert oe in '</ > ; <!-- --> ; <? ?> ; < />'
        jk = j+k
        case4tag = _jk2case[jk]
        return (case4tag, nm4tag_or_comment, may_nm2s)


    def _is_char4nm(sf, c, /):
        return c.isalnum() or c in '-_:'
    def _parse_nm(sf, it, /, *, raise_vs_return=False):
        smay_nm = sf._parse_smay_nm(it)
        if not smay_nm:
            raise ParseFail
        nm = smay_nm
        return nm
    def _parse_smay_nm(sf, it, /):
        smay_nm = read_while_(sf._is_char4nm, it)
        return smay_nm


    def _parse_dict(sf, it, /):
        nm2s = OrderedDict()
        while 1:
            skip_spaces(it)
            smay_nm = sf._parse_smay_nm(it)
            if not smay_nm:
                break
            nm = smay_nm
            if nm in nm2s:
                raise ParseFail
            skip_spaces(it)
            if not try_skip_prefix_('=', it):
                raise ParseFail
            skip_spaces(it)
            s = sf._parse_property_value(it)
            nm2s[nm] = s
        return nm2s


    def _is_literal_char(sf, c, /):
        assert len(c) == 1
        #return c.isprintable() and not c in (r'\"' "'")
        #now:『'』ok
        return c.isprintable() and not c in (r'\"')
    assert not _is_literal_char(0, '\u3000')
    assert not _is_literal_char(0, '\n')
    assert not _is_literal_char(0, '\\')
    assert not _is_literal_char(0, '\"')

    #assert not _is_literal_char('\'')
    assert _is_literal_char(0, '\'')

    def _parse_property_value(sf, it, /):
        r'假设:属性值必须用双引号&&字面不含『\』'
        if not try_skip_prefix_('"', it):
            raise ParseFail
        s = read_while_(sf._is_literal_char, it)
        if not try_skip_prefix_('"', it):
            raise ParseFail
        return s


    def _is_char4gap(sf, c, /):
        return not c in '<>&'
    def _parse_gap_text(sf, it, /):
        s = read_while_(sf._is_char4gap, it)
        return s

#end-class SimpleParser4XML:
simple_parser4XML = SimpleParser4XML()
parse_xml__ipath = simple_parser4XML.parse_xml__ipath
parse_xml__ifile = simple_parser4XML.parse_xml__ifile
parse_xml__PeekableIterator = simple_parser4XML.parse_xml__PeekableIterator



if __name__ == "__main__":
    ...
__all__
from script.parse_xml import ParseFail
from script.parse_xml import parse_xml__ipath, parse_xml__ifile, parse_xml__PeekableIterator
from script.parse_xml import *
