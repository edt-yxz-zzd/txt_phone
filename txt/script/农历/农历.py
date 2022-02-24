
#[[[goto:end_my_all__src_code__output
#[[[goto:end_my_src_code
#goto:mk__all__
#goto:__all__
#goto:import
#goto:begin_of_packed_kwargs__txt#已打包关键数据的输出文件内容
#[[[__doc__-begin
#[[[
r'''
e script/农历/农历.py
    view others/数学/编程/农历/py农历.txt
    #   https://blog.csdn.net/wqlineky1/article/details/80945299

TODO:
    +main()::subcmd...
    update __doc__::py_cmd-section

#[[[py_cmd
py /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py
py /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py > /sdcard/0my_files/tmp/out4py/农历/农历.py.解析所有数据并计算关键数据.out.txt
    #尝试解析所有数据并计算关键数据
view /sdcard/0my_files/tmp/out4py/农历/农历.py.解析所有数据并计算关键数据.out.txt
du -bh /sdcard/0my_files/tmp/out4py/农历/农历.py.解析所有数据并计算关键数据.out.txt
30K     /sdcard/0my_files/tmp/out4py/农历/农历.py.解析所有数据并计算关键数据.out.txt

cp -t /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/ /sdcard/0my_files/tmp/out4py/农历/农历.py.解析所有数据并计算关键数据.out.txt
view /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.解析所有数据并计算关键数据.out.txt



py /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py
    #尝试_读并打包并写
view /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.解析所有数据并计算关键数据.out.已打包.txt
du -bh /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.解析所有数据并计算关键数据.out.已打包.txt
3.8K    /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.解析所有数据并计算关键数据.out.已打包.txt
    已打包关键数据=packed_kwargs
    最长一行:2419_Byte@农历相邻节气的日份距离已打包::radix=3->10
        (200年)*(24节气/年)*(log2(3)_bit/节气)/(log2(10)bit/byte)
        ~(4800*log10(3) Byte)
        ~(4800*0.47712125471966244 Byte)
        ~(2290.1820226543796 Byte)
        < 2419_Byte


py /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py > /sdcard/0my_files/tmp/out4py/农历/农历.py.打印公历农历日期对照表.out.txt
    #尝试_打印公历农历日期对照表
view /sdcard/0my_files/tmp/out4py/农历/农历.py.打印公历农历日期对照表.out.txt
du -bh /sdcard/0my_files/tmp/out4py/农历/农历.py.打印公历农历日期对照表.out.txt
1.7M    /sdcard/0my_files/tmp/out4py/农历/农历.py.打印公历农历日期对照表.out.txt
    #ver1: f'{g_date_str}={n_date_str}')
1.9M    /sdcard/0my_files/tmp/out4py/农历/农 历.py.打印公历农历日期对照表.out.txt
    #ver2: f'{g_date_str}={n_date_str}{jq_str}')


压缩
    /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.打印公历农历日期对照表.out.txt.zip
du -bh /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.打印公历农历日期对照表.out.txt.zip
394K    /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.打印公历农历日期对照表.out.txt.zip

#]]]py_cmd

====
我的农历数据组织:
    农历各月天数
        农历起始月的年份
        农历起始月的月份
        农历起始月初一的相应公历日期
        不完整的最后一个农历月的初一的相应公历日期
    农历相邻闰月的月份距离
        农历起始闰月相对于农历起始月的月份距离
    农历相邻节气的日份距离
        农历起始节气相对于农历起始月初一的日份距离
        农历起始节气的节气索引
节日数据/节日函数/干支纪年函数:
    农历节日
    公历节日
    求公历年份的干支索引



====
====
农历公历对照表 农历节日 公历节日
  e others/数学/编程/农历/py农历.txt
=====
https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T1904c.txt
mkdir /sdcard/0my_files/tmp/curl_/农历数据/
cd /sdcard/0my_files/tmp/curl_/农历数据/
curl https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T[1901-2100]c.txt   --create-dirs -o 'T#1c.txt'

cd /sdcard/0my_files/tmp/curl_/
mv -T ./农历数据/ ./香港天文台农历对照表（文字版）/
/sdcard/0my_files/git_repos/txt_phone/txt/script/农历/香港天文台农历对照表（文字版）.zip
view ++enc=big5 /sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T2021c.txt
view ++enc=big5 /sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T1941c.txt
    最后一行:
        '香港於1941年6月15日至9月30日期間實施了夏令時間 (香港夏令時間 = 香港標準時間 + 1小時)'
view ++enc=big5 /sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T2058c.txt
    第一行:
        '2058 年1月1日          初七        星期二'
view ++enc=big5 /sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T1901c.txt




#ref:节气名及节气索引及節氣名
#ref:天干字及天干索引
#ref:地支字及地支索引
#ref:干支计数及干支索引
干支
    天干=十干=甲、乙、丙、丁、戊、己、庚、辛、壬、癸
    地支=岁阴=子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥
生肖=属相，地支+属相=子鼠、丑牛、寅虎、卯兔、辰龙、巳蛇、午马、未羊、申猴、酉鸡、戌狗、亥猪
天干 = '甲乙丙丁戊己庚辛壬癸'
地支 = '子丑寅卯辰巳午未申酉戌亥'
生肖 = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

#solar term 节气
节气
二十四个节气=立春、雨水、惊蜇、春分、清明、谷雨、立夏、小满、芒种、夏至、小暑、大暑、立秋、处暑、白露、秋分、寒露、霜降、立冬、小雪、大雪、冬至、小寒、大寒


====格式:
文件头:
    \d{4}(\w{2} - 肖\w)年公曆與農曆日期對照表
列表头:
    公曆日期\s+農曆日期\s+星期\s+節氣
公曆日期
    \d{4}年(0?[1-9]|1[0-2])月(0?[1-9]|[12][0-9]|3[01])日
農曆日期
    (閏?([正二三四五六七八九十]|十[一二])月|初[二三四五六七八九十]|十[一二三四五六七八九]|二十|廿[一二三四五六七八九]|三十)
星期
    星期[一二三四五六日]
節氣
    \w{2}?
    空 或者 两字节气名
[[[====格式示例:
1901(辛丑-肖牛)年公曆與農曆日期對照表                                                     
  
公曆日期         農曆日期               星期              節氣                  
1901年01月01日    十一                  星期二                                

1901年01月18日    廿八                  星期五                                
1901年01月19日    廿九                  星期六                                
1901年01月20日    十二月                星期日                                
1901年01月21日    初二                  星期一            大寒                  
    ##==>> 1901_01_20__12_01__0
    ##==>> ???1900_12_31__11_10__1???十一月？閏十一月？
    ##无法确定 是否 闰月，看来只能跳回前20项，从 1901_01_20__12_01__0 开始


2021(辛丑 - 肖牛)年公曆與農曆日期對照表

公曆日期              農曆日期    星期        節氣
2021年1月1日          十八        星期五              

2021年1月12日         廿九        星期二              
2021年1月13日         十二月      星期三              
2021年1月14日         初二        星期四              

2021年2月10日         廿九        星期三              
2021年2月11日         三十        星期四              
2021年2月12日         正月        星期五              
2021年2月13日         初二        星期六              
2021年2月14日         初三        星期日              
2021年2月15日         初四        星期一              

2021年2月18日         初七        星期四      雨水    

2021年2月21日         初十        星期日              
2021年2月22日         十一        星期一              

2021年3月3日          二十        星期三              
2021年3月4日          廿一        星期四              




1901年02月04日    十六                  星期一            立春                  
1901年02月19日    正月                  星期二            雨水                  
    # 立春可能在正月春节前！

1903年01月21日    廿三                  星期三            大寒                  
1903年01月29日    正月                  星期四                                
1903年02月05日    初八                  星期四            立春                  
    # 立春可能在正月春节后！

1985年02月19日    三十                  星期二            雨水                  
1985年02月20日    正月                  星期三                                
    # 雨水可能在正月春节前！


2050年12月31日        十八        星期六              
2051年1月1日          十九        星期六              
2051年12月31日        廿九        星期六              
2052年1月1日          三十        星期一              
    #整个 2051 年文件 星期 错位 偏移一天
    #error!!! detected by isoweekday()
    #   assert 本行公历年月日.isoweekday()%7 == 星期索引







1901年01月20日    十二月                星期日                                
    #==>> _打印公历农历日期对照表() 输出的第一行: g19010120x0=n190012c01fJQ


2100年12月1日         十一月      星期三              

2100年12月30日        三十        星期四              
2100年12月31日        十二月      星期五              
    #==>> _打印公历农历日期对照表() 输出的最后一行: g21001230x4=n210011c30fJQ


1901年02月19日    正月                  星期二            雨水                  
    #==>> _打印公历农历日期对照表() 输出的第一个春节: g19010219x2=n190101c01j01

1902年02月08日    正月                  星期六                                
    #==>> _打印公历农历日期对照表() 输出的第二个春节: g19020208x6=n190201c01fJQ


1903年05月27日    五月                  星期三                                

1903年06月25日    閏五月                星期四                                
    #==>> _打印公历农历日期对照表() 输出的第一个闰月初一: g19030625x4=n190305r01fJQ
1903年07月24日    六月                  星期五            大暑                    
    #==>> _打印公历农历日期对照表() 输出的第一个闰月的下一个初一: g19030724x5=n190306c01j11


1906年04月24日    四月                  星期二                                

1906年05月23日    閏四月                星期三                                
    #==>> _打印公历农历日期对照表() 输出的第二个闰月初一: g19060523x3=n190604r01fJQ
    #bug: 打印输出 g19060523x3=n190605c01;g19060622x5=n190605r01 #代码有误！
    #       已修正！初始化闰月距离立即减一
    #前两个闰月之间的月份距离=n190604r01-n190305r01=12+12+12{假设无闰的3年后的五月}-1{四月}+1{闰四月}=36
    #   view /sdcard/0my_files/tmp/out4py/农历/农历.py.解析所有数据并计算关键数据.out.txt
    #       农历相邻闰月的月份距离=[36, ...]
    #   生成的数据无误！
1906年06月22日    五月                  星期五            夏至                  
    #==>> _打印公历农历日期对照表() 输出的第二个闰月的下一个初一: g19060622x5=n190605c01j09


1901年03月20日    二月                  星期三                                
    #上面检查了 第一第二个农历月份初一
    #   g19010120x0=n190012c01
    #   g19010219x2=n190101c01
    #这里是 第三个农历月份初一
    #   g19010320x3=n190102c01
    #==>> _打印公历农历日期对照表() 输出的第三个初一: g19010320x3=n190102c01fJQ


2021年9月7日          八月        星期二      白露    
    #==>> _打印公历农历日期对照表() 输出的2021年八月初一白露: g20210907x2=n202108c01j14

2021年9月21日         十五        星期二              
    #==>> _打印公历农历日期对照表() 输出的2021年中秋节: g20210921x2=n202108c15fJQ

2020年5月23日         閏四月      星期六              
    #==>> _打印公历农历日期对照表() 输出的2020年闰四月初一: g20200523x6=n202004r01fJQ


#ref:节气名及节气索引及節氣名
1901年01月06日    十六                  星期日            小寒                  
    #起始月之前，不计

1901年01月20日    十二月                星期日                                
1901年01月21日    初二                  星期一            大寒                  
    #==>> _打印公历农历日期对照表() 输出的第一个节气: g19010121x1=n190012c02j23
1901年02月04日    十六                  星期一            立春                  
    #==>> _打印公历农历日期对照表() 输出的第二个节气: g19010204x1=n190012c16j00
1901年02月19日    正月                  星期二            雨水                  
    #==>> _打印公历农历日期对照表() 输出的第三个节气: g19010219x2=n190101c01j01
    #重复 ==>> _打印公历农历日期对照表() 输出的第一个春节: g19010219x2=n190101c01j01
1901年03月06日    十六                  星期三            驚蟄                  
    #==>> _打印公历农历日期对照表() 输出的第四个节气: g19010306x3=n190101c16j02
2100年12月22日        廿二        星期三      冬至    
    #==>> _打印公历农历日期对照表() 输出的倒数第一个节气: g21001222x3=n210011c22j21
2100年12月7日         初七        星期二      大雪    
    #==>> _打印公历农历日期对照表() 输出的倒数第二个节气: g21001207x2=n210011c07j20
2100年11月22日        廿一        星期一      小雪    
    #==>> _打印公历农历日期对照表() 输出的倒数第三个节气: g21001122x1=n210010c21j19
2100年11月7日         初六        星期日      立冬    
    #==>> _打印公历农历日期对照表() 输出的倒数第四个节气: g21001107x0=n210010c06j18
以下 证明 上面 皆 常月:
1901年01月20日    十二月                星期日                                
1901年02月19日    正月                  星期二            雨水                  
1901年03月20日    二月                  星期三                                
2100年11月2日         十月        星期二              
2100年12月1日         十一月      星期三              
2100年12月31日        十二月      星期五              



######################
gvim:ctrl+v ==>> visual-block
0
1
2
3
4
5
6
7
8
9

节气名及节气索引及節氣名:
立春00立春
雨水01雨水
惊蜇02驚蟄
春分03春分
清明04清明
谷雨05穀雨
立夏06立夏
小满07小滿
芒种08芒種
夏至09夏至
小暑10小暑
大暑11大暑
立秋12立秋
处暑13處暑
白露14白露
秋分15秋分
寒露16寒露
霜降17霜降
立冬18立冬
小雪19小雪
大雪20大雪
冬至21冬至
小寒22小寒
大寒23大寒


天干字及天干索引:
甲0
乙1
丙2
丁3
戊4
己5
庚6
辛7
壬8
癸9



地支字及地支索引:
子00
丑01
寅02
卯03
辰04
巳05
午06
未07
申08
酉09
戌10
亥11


干支计数及干支索引:
甲子00
乙丑01
丙寅02
丁卯03
戊辰04
己巳05
庚午06
辛未07
壬申08
癸酉09
甲戌10
乙亥11
丙子12
丁丑13
戊寅14
己卯15
庚辰16
辛巳17
壬午18
癸未19
甲申20
乙酉21
丙戌22
丁亥23
戊子24
己丑25
庚寅26
辛卯27
壬辰28
癸巳29
甲午30
乙未31
丙申32
丁酉33
戊戌34
己亥35
庚子36
辛丑37
壬寅38
癸卯39
甲辰40
乙巳41
丙午42
丁未43
戊申44
己酉45
庚戌46
辛亥47
壬子48
癸丑49
甲寅50
乙卯51
丙辰52
丁巳53
戊午54
己未55
庚申56
辛酉57
壬戌58
癸亥59




]]]====格式示例

#'''
#]]]
#]]]__doc__-end


#[[[mk__all__
r'''
##################################
##################################
##################################
[[[
==========
grep '^\(\w\+\)\s*= ' /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py
已打包关键数据的输出文件内容
packed_kwargs__txt

grep '^\(def\|class\) ' /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py
class FormatError(Exception):pass
class LengthError(Exception):pass
def tuple2date(tpl, /):
def date2tuple(date, /):
def 求公历年公历月公历日的相应公历年月日(公历年份, 公历月份, 公历日份, /):
def 求日份距离(lhs, rhs, /):
def 求公历年月日的星期索引(公历年月日, /):
class 相关常用函数集合:
def _try_相关常用函数集合():
class 读取香港天文台农历对照表文字版(相关常用函数集合):
class _T:
def _try_读取香港天文台农历对照表文字版():
def main():


.,.+12s/^\(def\|class\)\s\+\([^(:]\+\).*$/\2/
已打包关键数据的输出文件内容
packed_kwargs__txt
FormatError
LengthError
tuple2date
date2tuple
求公历年公历月公历日的相应公历年月日
求日份距离
求公历年月日的星期索引
相关常用函数集合
_try_相关常用函数集合
读取香港天文台农历对照表文字版
_T
_try_读取香港天文台农历对照表文字版
main

==========
]]]
##################################
##################################
##################################
#'''
#]]]mk__all__


__all__ = '''
    已打包关键数据的输出文件内容
        packed_kwargs__txt

    FormatError
    LengthError

    tuple2date
    date2tuple
    求公历年公历月公历日的相应公历年月日
    求日份距离
    求公历年月日的星期索引
    相关常用函数集合
    _try_相关常用函数集合

    读取香港天文台农历对照表文字版
    _T
    _try_读取香港天文台农历对照表文字版
    main
    '''.split()
r'''
usage:
    已打包关键数据的输出文件内容
    未打包关键数据 = _T()._读取已打包关键数据并解包(已打包关键数据的输出文件内容, input_is_text_not_path=True):
    _T()._打印公历农历日期对照表(未打包关键数据, may_fout=None)
#'''


from seed.tiny import print_err, mk_fprint
from seed.iters.zip_me import zip_me2

from pathlib import Path
import io
import re
import datetime
import itertools
import ast

if 1:
    from seed.int_tools.digits.Packer4BoundedIntSeq import pack_from_bounded_int_seq, Packer4BoundedIntSeq__little_endian#safe_exec::nonlocals
    from seed.iters.minmax import minmax_default
    from seed.helper.safe_eval import safe_exec


#[[[已打包关键数据=packed_kwargs
#已打包关键数据的输出文件内容 = packed_kwargs__txt
#来源:
#   <-- copy from: /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.解析所有数据并计算关键数据.out.已打包.txt
#   <-- 尝试_读并打包并写: /sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.解析所有数据并计算关键数据.out.txt
#   <-- 尝试解析所有数据并计算关键数据: curl_fmt'/sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T[1901-2100]c.txt'
#   <-- 下载@20210919: curl https://www.hko.gov.hk/tc/gts/time/calendar/text/files/T[1901-2100]c.txt   --create-dirs -o 'T#1c.txt'
# 已发现错误:
#   * 整个 2051 年文件 星期 错位 偏移一天
#       因此，关键数据 不包含 星期/农历起始日份的星期索引; 见下面:求公历年公历月公历日的星期索引
#
#begin_of_packed_kwargs__txt
已打包关键数据的输出文件内容 = packed_kwargs__txt = r'''
农历各月天数已打包=Packer4BoundedIntSeq__little_endian(2473, 1634749503082924305707673643006528564343668428871125259616506522845239303874579874249329654397940326870676029000757574076245715152671593249760017511380795259180383761662614186821352515451854346614263203646186481231794392435628289115609528180981617289477780653872600353895134178530039078140060706966580559407627853421619750292582481767546302762012167252173436686797951183054550760114034887434750841228916230723615298572241549402978389786000039035547441777597686572770198709881546656709299300870433816117135204673045874422061536231183127660028673553825487164593621375592472007482342587470202549185368677113649813259962926637720435910029395459778609744783986746473966628306981337756271087104433322803541402392259935888646527445176558200413865946789, int_lower_bound = 29, int_upper_bound = 30)
农历起始月的年份=1900
农历起始月的月份=12
农历起始月初一的相应公历日期=(1901, 1, 20)
不完整的最后一个农历月的初一的相应公历日期=(2100, 12, 31)
农历相邻闰月的月份距离已打包=Packer4BoundedIntSeq__little_endian(72, 90116331300939110899003516668539770227658639295611051891284827703, int_lower_bound = 29, int_upper_bound = 36)
农历起始闰月相对于农历起始月的月份距离=30
农历相邻节气的日份距离已打包=Packer4BoundedIntSeq__little_endian(4798, 845664990957012438970446034379659020772862387745469349759299693609205833981913471657368675592828952387436216790766582660113839303344936422974837721418449407228083046896945948670154630226841471436028365755864218706707796946153802075940929072146866474810116403899099806429484728267471317345795568639279034850521288840294430472961405961034044733652851261740839706170887479299181279740045107020852039173041008495978167437657940789663036074622282457434317443887790405639157781935065928043393037832048764483775174519155199151590083981922311947555579660340614189091705612564413623146391946813048114817910966201854382023776063922059759579660171766304902068540638446919248755413919120512278072786333184099533292219021851920570072197026497445364129365248397550199855048797449829769965002165652248449091378871491443668024440655860195118151868620887263802739524072837800146791945650756099379048124520957514303387804265965540802663623369614594254265836204898697250871382193235111724874201542193901997007063863620729510941000996879178223145656175880217883159153302137070299580719346559734517531856977342913335015837403883306739570799261737678758256059232887222509915865513444978864400090080879517720672863258974080103620396384380941928943393141319022859311408443115008278720806078251938042785973347329097644265299064329050876924458618295833565140748158048927692023575623814802710583118315777141510727580930822493808117379441577018314311566428455445863501548636837526240000032544644853253990300937328294491045824392533787372914685716407763196612456434153170845603056178187007993386912902142218171434756678851643196606853034618633316421156506715562026390755836821024353558079214688215003611273054761795361018301623855097321065316265568909628361860677289693900344786405662119330311572084352435811414901486736806960281993104181014870469698295121604286977270537582231689602928620410894977574541010647889180350597727150801674748886422360718113240443173434640029080616721696068838264358627879631725921678190156521113058573886868588000873038169400055076896060567843478341038569387987072661219809584615716631863286132568096439601856191528145905159690254224762248011675889339888699713061617725508098770659919365996756603512017660368067902836856074335402180761119586469118903147411121562705874781799618359936135083, int_lower_bound = 14, int_upper_bound = 16)
农历起始节气相对于农历起始月初一的日份距离=1
农历起始节气的节气索引=23
#'''[1:-1]
#]]]已打包关键数据=packed_kwargs








#######################
#######################
#######################
#ref:天干字及天干索引
#ref:地支字及地支索引
天干 = '甲乙丙丁戊己庚辛壬癸'
地支 = '子丑寅卯辰巳午未申酉戌亥'
#生肖
生肖简体字 = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
生肖繁体字雞犬 = '鼠牛虎兔龍蛇馬羊猴雞犬豬'
    #雞vs鷄
    #犬vs狗
生肖繁体字雞犬狗格式 = '[鼠牛虎兔龍蛇馬羊猴雞犬狗豬]'

if 0:
    天干奇 = '甲  丙  戊  庚  壬  '
    天干偶 = '  乙  丁  己  辛  癸'
    地支奇 = '子  寅  辰  午  申  戌  '
    地支偶 = '  丑  卯  巳  未  酉  亥'

天干奇 = '甲丙戊庚壬'
天干偶 = '乙丁己辛癸'
地支奇 = '子寅辰午申戌'
地支偶 = '丑卯巳未酉亥'

#ref:干支计数及干支索引
六十干支格式 = \
    fr'(?:[{天干奇}][{地支奇}]|[{天干偶}][{地支偶}])'



if 0:
    二十四个节气 = '立春|雨水|惊蜇|春分|清明|谷雨|立夏|小满|芒种|夏至|小暑|大暑|立秋|处暑|白露|秋分|寒露|霜降|立冬|小雪|大雪|冬至|小寒|大寒'
    {'', '小滿', '', '', '', '', '', '處暑', '', '', '', '', '驚蟄', '', '', '', '', '穀雨', '', '', '', '芒種', '', ''}
    {'立夏', '小滿', '大雪', '霜降', '立冬', '白露', '立秋', '處暑', '小寒', '小暑', '秋分', '寒露', '驚蟄', '清明', '立春', '夏至', '大暑', '穀雨', '小雪', '春分', '冬至', '芒種', '雨水', '大寒'}
#ref:节气名及节气索引及節氣名
二十四个节气 = '立春|雨水|惊蜇|春分|清明|谷雨|立夏|小满|芒种|夏至|小暑|大暑|立秋|处暑|白露|秋分|寒露|霜降|立冬|小雪|大雪|冬至|小寒|大寒'
二十四個節氣 = '立春|雨水|驚蟄|春分|清明|穀雨|立夏|小滿|芒種|夏至|小暑|大暑|立秋|處暑|白露|秋分|寒露|霜降|立冬|小雪|大雪|冬至|小寒|大寒'


文件头行格式 = \
    fr'(?P<公历年份>\d+)\((?P<干支纪年>{六十干支格式})\s*-\s*肖(?P<生肖属相>{生肖繁体字雞犬狗格式})\)年公曆與農曆日期對照表'
列表头行格式 = \
    r'公曆日期\s+農曆日期\s+星期\s+節氣'

公曆日期格式 = \
    r'(?:(?P<公历年份>\d+)年(?P<公历月份>0?[1-9]|1[0-2])月(?P<公历日份>0?[1-9]|[12][0-9]|3[01])日)'
農曆日期格式 = \
    r'(?:閏?(?:[正二三四五六七八九十]|十[一二])月|初[二三四五六七八九十]|十[一二三四五六七八九]|二十|廿[一二三四五六七八九]|三十)'
星期格式 = \
    r'(?:星期[一二三四五六日])'
節氣格式 = \
    fr'(?:{二十四個節氣})'
    #r'(?:\w{2})'

数据行格式 = fr'(?P<公曆日期>{公曆日期格式})\s+(?P<農曆日期>{農曆日期格式})\s+(?P<星期>{星期格式})(?:\s+(?P<節氣>{節氣格式}))?'

文件头行正则表达式 = re.compile(文件头行格式)
列表头行正则表达式 = re.compile(列表头行格式)
数据行正则表达式 = re.compile(数据行格式)
if 0:
    公曆日期正则表达式 = re.compile(公曆日期格式)
    農曆日期正则表达式 = re.compile(農曆日期格式)
    星期正则表达式 = re.compile(星期格式)
    節氣正则表达式 = re.compile(節氣格式)



文件头行示例 = '1901(辛丑-肖牛)年公曆與農曆日期對照表'
assert 文件头行正则表达式.fullmatch(文件头行示例)
数据行示例甲 = '1901年01月01日    十一                  星期二'
assert 数据行正则表达式.fullmatch(数据行示例甲)
数据行示例乙 = '1903年06月25日    閏五月                星期四'
assert 数据行正则表达式.fullmatch(数据行示例乙)
数据行示例丙 = '2033年12月22日        閏十一月    星期四'
assert 数据行正则表达式.fullmatch(数据行示例丙)









class FormatError(Exception):pass
class LengthError(Exception):pass


def tuple2date(tpl, /):
    return datetime.date(*tpl)
def date2tuple(date, /):
    return (date.year, date.month, date.day)
def 求公历年公历月公历日的相应公历年月日(公历年份, 公历月份, 公历日份, /):
    公历年月日 = tuple2date((公历年份, 公历月份, 公历日份))
    return 公历年月日
def 求日份距离(lhs, rhs, /):
    r'datetime.date -> datetime.date -> int'
    timedelta = lhs - rhs
    return timedelta.days
def 求公历年月日的星期索引(公历年月日, /):
    r'datetime.date -> uint%7'
    星期索引 = 公历年月日.isoweekday()%7
    return 星期索引

class 相关常用函数集合:
    r'''
    #'''
    def 求公历年公历月公历日的星期索引(sf, 公历年份, 公历月份, 公历日份, /):
        公历年月日 = 求公历年公历月公历日的相应公历年月日(公历年份, 公历月份, 公历日份)
        return 求公历年月日的星期索引(公历年月日)
    def 求公历年份的干支索引(sf, 公历年份, /):
        r'''
        1901辛丑条约~干支索引37
        (干支索引-37) =[%60]= (公历年份-1901)
        干支索引 = ((公历年份-1901)+37)%60
        #'''
        if not type(公历年份) is int: raise TypeError
        干支索引 = ((公历年份-1901)+37)%60
        return 干支索引

    #ref:天干字及天干索引
    def 求天干字(sf, 天干索引, /):
        if not 0 <= 天干索引 < 10: raise ValueError
        return 天干[天干索引]
    #ref:地支字及地支索引
    def 求地支字(sf, 地支索引, /):
        if not 0 <= 地支索引 < 12: raise ValueError
        return 地支[地支索引]
    #ref:干支计数及干支索引
    def 求干支计数(sf, 干支索引, /):
        if not 0 <= 干支索引 < 60: raise ValueError
        天干索引 = 干支索引%10
        地支索引 = 干支索引%12
        天干字 = sf.求天干字(天干索引)
        地支字 = sf.求地支字(地支索引)
        干支计数 = 天干字 + 地支字
        assert len(干支计数) == 2
        return 干支计数

    def 求天干索引(sf, 天干字, /):
        if len(天干字) != 1: raise ValueError
        i = 天干.index(天干字)
        assert 0 <= i < 10
        return i
    def 求地支索引(sf, 地支字, /):
        if len(地支字) != 1: raise ValueError
        i = 地支.index(地支字)
        assert 0 <= i < 12
        return i
    def 求干支索引(sf, 干支计数, /):
        if len(干支计数) != 2: raise ValueError
        天干字, 地支字 = 干支计数
        天干索引 = sf.求天干索引(天干字)
        地支索引 = sf.求地支索引(地支字)
        if 天干索引%2 != 地支索引%2: raise ValueError
        r'''
        x%10 = 天干索引
        x%12 = 地支索引
            ==>> x%60 = ???

        x%5 = 天干索引%5
        x%12 = 地支索引
        5*5%12==1
        3*12%5==1
            ==>> x%60 = (36*(天干索引%5) + 25*地支索引)%60
        #'''
        干支索引 = x = (36*(天干索引%5) + 25*地支索引)%60
        if 0:
            print(f'干支计数={干支计数}')
            print(f'天干索引={天干索引}')
            print(f'地支索引={地支索引}')
            print(f'干支索引={干支索引}')
        assert 干支索引%10 == 天干索引
        assert 干支索引%12 == 地支索引
        assert 0 <= 干支索引 < 60
        return 干支索引

    ##
    #ref:节气名及节气索引及節氣名
    def 求节气名(sf, 节气索引, /):
        节气名 = sf._求节气名(二十四个节气, 节气索引)
        assert 节气索引 == sf._求节气索引(二十四个节气, 节气名)
        return 节气名
    def 求节气索引(sf, 节气名, /):
        节气索引 = sf._求节气索引(二十四个节气, 节气名)
        assert 节气名 == sf._求节气名(二十四个节气, 节气索引)
        return 节气索引
    ##
    def 求節氣名(sf, 節氣索引, /):
        節氣名 = sf._求節氣名(二十四個節氣, 節氣索引)
        assert 節氣索引 == sf._求節氣索引(二十四個節氣, 節氣名)
        return 節氣名
    def 求節氣索引(sf, 節氣名, /):
        節氣索引 = sf._求節氣索引(二十四個節氣, 節氣名)
        assert 節氣名 == sf._求節氣名(二十四個節氣, 節氣索引)
        return 節氣索引
    def _求節氣名(sf, 二十四個節氣, 節氣索引, /):
        if not 0 <= 節氣索引 < 24: raise ValueError
        i = 節氣索引*3
        節氣名 = 二十四個節氣[i:i+2]
        assert len(節氣名) == 2
        return 節氣名

    def _求節氣索引(sf, 二十四個節氣, 節氣名, /):
        if len(節氣名) != 2: raise ValueError
        i = 二十四個節氣.index(節氣名)//3
        assert 0 <= i < 24
        return i
    def 求星期索引(sf, 星期, /):
        if len(星期) != 3: raise ValueError
        if not 星期.startswith('星期'): raise ValueError
        i = '日一二三四五六'.index(星期[2:])
        assert 0 <= i < 7
        return i
    def 解析中文數字從一至三十(sf, 中文數字, /):
        L = len(中文數字)
        if L == 1:
            i = 1+'一二三四五六七八九十'.index(中文數字)
        elif L == 2:
            if 中文數字[0] not in '十二廿三':
                raise FormatError(f'bad format:unknown 中文數字:中文數字[0] not in "十二廿三":{中文數字!r}')
            if 中文數字[-1] == '十':
                i = 10*(2+'二三'.index(中文數字[0]))
            else:
                i10 = 10*(1+'十廿'.index(中文數字[0]))
                _i1 = sf.解析中文數字從一至三十(中文數字[1:])
                i = i10 + _i1
        else:
            raise FormatError(f'bad format:unknown 中文數字 too long or empty:{中文數字!r}')
        return i
def _try_相关常用函数集合():
    sf = 相关常用函数集合()
    assert 0 == sf.求干支索引('甲子')
    assert 1 == sf.求干支索引('乙丑')
    assert 59 == sf.求干支索引('癸亥')
    assert '癸亥' == sf.求干支计数(59)
    assert '乙丑' == sf.求干支计数(1)
    assert '甲子' == sf.求干支计数(0)
    if 0:
        print(sf.求干支索引('甲午'))#1894中日甲午战争
        print(sf.求干支索引('戊戌'))#1898戊戌变法
        print(sf.求干支索引('辛丑'))#1901辛丑条约
        print(sf.求干支索引('辛亥'))#1911辛亥革命
            #30 34 37 47
    test_data = dict(
        甲子=0
        ,乙丑=1
        ,癸亥=59
        ,甲午=30
        ,戊戌=34
        ,辛丑=37
        ,辛亥=47
        )
    for 干支计数, 干支索引 in test_data.items():
        assert 干支索引 == sf.求干支索引(干支计数)
        assert 干支计数 == sf.求干支计数(干支索引)

    test_data = dict(
        甲午=1894#中日甲午战争
        ,戊戌=1898#戊戌变法
        ,辛丑=1901#辛丑条约
        ,辛亥=1911#辛亥革命
        )
    for 干支计数, 公历年份 in test_data.items():
        assert sf.求公历年份的干支索引(公历年份) == sf.求干支索引(干支计数)

_try_相关常用函数集合()
#raise


class 读取香港天文台农历对照表文字版(相关常用函数集合):
    r'''
    #'''

    if 0:
        skipped_lines = {
        '香港於1941年6月15日至9月30日期間實施了夏令時間 (香港夏令時間 = 香港標準時間 + 1小時)'
        ,'香港於1942年1月1日至12月31日期間實施了夏令時間 (香港夏令時間 = 香港標準時間 + 1小時)'
        }
    def _strip_and_skip_empty_lines(sf, lines):
        for line in lines:
            line = line.strip()
            if line:
                #if line not in sf.skipped_lines:
                if not line.startswith('香港於'):
                    yield line
                else:
                    if 0: print_err(line)
        pass
    def 解析農曆日期(sf, 農曆日期, /):
        r'-> (可選閏月與否, 可選農曆月份, 農曆日份,)'
        if 農曆日期[-1] == '月':
            農曆月份 = 農曆日期[:-1]
            閏月與否 = 農曆月份[0] == '閏'
            if 閏月與否:
                農曆月份 = 農曆月份[1:]
            if 農曆月份 == '正':
                農曆月份 = 1
            else:
                農曆月份 = sf.解析中文數字從一至三十(農曆月份)
            農曆日份 = 1
            閏月與否, 農曆月份, 農曆日份,
            (可選閏月與否, 可選農曆月份, 農曆日份,) = 閏月與否, 農曆月份, 農曆日份,
        elif 農曆日期[0] in '初十二廿三':
            if 農曆日期[0] == '初':
                農曆日份 = 農曆日期[1:]
            else:
                農曆日份 = 農曆日期
            農曆日份 = sf.解析中文數字從一至三十(農曆日份)
            農曆日份,
            (可選閏月與否, 可選農曆月份, 農曆日份,) = None, None, 農曆日份,
        else:
            raise FormatError(f'bad format:unknown 農曆日期:{農曆日期!r}')
        return (可選閏月與否, 可選農曆月份, 農曆日份,)

    def 解析文件头行数据(sf, 文件头行数据, /):
        (公历年份, 干支纪年, 生肖属相) = 文件头行数据
        公历年份 = int(公历年份)
        年份干支索引 = sf.求干支索引(干支纪年)
        return (公历年份, 年份干支索引)
    def 解析数据行数据(sf, 数据行数据, /):
        ((公历年份, 公历月份, 公历日份), 農曆日期, 星期, 可選節氣) = 数据行数据
        if 1:
            公历年份 = int(公历年份)
            公历月份 = int(公历月份)
            公历日份 = int(公历日份)
        (可選閏月與否, 可選農曆月份, 農曆日份,) = sf.解析農曆日期(農曆日期)
        星期索引 = sf.求星期索引(星期)
        if 可選節氣:
            節氣 = 可選節氣
            節氣索引 = sf.求節氣索引(節氣)
            可選節氣索引 = 節氣索引
        else:
            可選節氣索引 = None
        可選節氣索引

        return ((公历年份, 公历月份, 公历日份), (可選閏月與否, 可選農曆月份, 農曆日份,), 星期索引, 可選節氣索引)



    def __init__(sf, /,*
            , encoding = 'big5'
            , year_first=1901
            , year_last =2100
            , ifname_fmt='T{}c.txt'
            ):
        sf.encoding = encoding
        sf.year_first = year_first
        sf.year_last = year_last
        sf.ifname_fmt = ifname_fmt
    def read_all_txt_ifile(sf,/,*, idir, 解析与否:bool=False):
        year2may_file_header_data = {}
        year2row_data_list = {}
        for year, ipath in sf.iter_all_txt_ipaths__with_year(idir=idir):
            it = sf.iter_read_single_file__path(ipath)
            may_file_header_data, [*row_data_list] = sf._cut_the_iter_result(it)
            year2row_data_list[year] = row_data_list
            year2may_file_header_data[year] = may_file_header_data

        if 解析与否:
            ####
            ####
            #for may_file_header_data in year2may_file_header_data.values():
            for year in sorted(year2may_file_header_data):
                may_file_header_data = year2may_file_header_data[year]
                if may_file_header_data:
                    [file_header_data] = may_file_header_data
                    文件头行数据 = file_header_data
                    文件头行数据已解析 = (公历年份, 年份干支索引) = sf.解析文件头行数据(文件头行数据)
                    year2may_file_header_data[year] = (文件头行数据已解析,)

            ####
            ####
            for row_data_list in year2row_data_list.values():
                #for 数据行数据 in row_data_list:
                for i in range(len(row_data_list)):
                    数据行数据 = row_data_list[i]
                    row_data_list[i] = 数据行数据已解析 = ((公历年份, 公历月份, 公历日份), (可選閏月與否, 可選農曆月份, 農曆日份,), 星期索引, 可選節氣索引) = sf.解析数据行数据(数据行数据)
        return year2may_file_header_data, year2row_data_list

    def iter_all_txt_ipaths__with_year(sf,/,*, idir):
        idir = Path(idir)
        for year, ifname in sf.iter_all_txt_ifile_basenames__with_year():
            yield year, idir/ifname
    def iter_all_years(sf, /):
        return iter(range(sf.year_first, sf.year_last+1))
    def iter_all_txt_ifile_basenames__with_year(sf,/):
        for year in sf.iter_all_years():
            yield year, sf.ifname_fmt.format(year)
    def list_read_single_file__path(sf, ipath, /):
        with open(ipath, 'rt', encoding=sf.encoding) as fin:
            return [*sf.iter_read_single_file__txt_ifile(fin)]
    def _cut_the_iter_result(sf, it, /):
        'iter([x?, None, ...]) -> (may x, iter(...))'
        it = iter(it)
        for head in it:
            if head is None:
                return (), it
            break
        else:
            raise ValueError('empty iterable')
        for snd in it:
            if snd is None:
                return (head,), it
            else:
                raise ValueError('None not in iterable[:2]')

    def iter_read_single_file__path(sf, ipath, /):
        with open(ipath, 'rt', encoding=sf.encoding) as fin:
            yield from sf.iter_read_single_file__txt_ifile(fin)
    def iter_read_single_file__txt(sf, txt, /):
        fin = io.StringIO(txt)
        return sf.iter_read_single_file__txt_ifile(fin)

    def iter_read_single_file__txt_ifile(sf, txt_ifile, /):
        lines = iter(txt_ifile)
        return sf.iter_read_single_file__lines(lines)
    def iter_read_single_file__lines(sf, lines, /):
        r'''
        output:
            [可选]yield (公历年份, 干支纪年, 生肖属相)
            yield None
            loop:
                yield ((公历年份, 公历月份, 公历日份), 農曆日期, 星期, 可選節氣)
        #'''
        it = iter(lines)
        it = sf._strip_and_skip_empty_lines(it)

        for 文件头行 in it:
            m4file_head = 文件头行正则表达式.fullmatch(文件头行)
            if m4file_head is None:
                try:
                    数据行 = 文件头行
                    data_of_first_line = sf.读取数据行(数据行)
                except FormatError:
                    raise FormatError(f'bad format:unknown 文件头行:{文件头行!r}')
                else:
                    break
            break
        else:
            raise FormatError('bad format:no 文件头行')

        if m4file_head:
            公历年份 = m4file_head['公历年份']
            干支纪年 = m4file_head['干支纪年']
            生肖属相 = m4file_head['生肖属相']
            #yield dict(公历年份=公历年份, 干支纪年=干支纪年, 生肖属相=生肖属相)
            #文件头行数据
            yield (公历年份, 干支纪年, 生肖属相)

        if m4file_head:
            for 列表头行 in it:
                m4table_head = 列表头行正则表达式.fullmatch(列表头行)
                if m4table_head is None:
                    try:
                        数据行 = 列表头行
                        data_of_first_line = sf.读取数据行(数据行)
                    except FormatError:
                        raise FormatError(f'bad format:unknown 列表头行:{列表头行!r}')
                    else:
                        break
                break
            else:
                raise FormatError('bad format:no 列表头行')

        if 1:
            yield None
        if m4file_head is None or m4table_head is None:
            #第一行 或 第二行 是 数据行
            yield data_of_first_line

        ##################
        ##################
        ##################
        ##################
        ##################
        for 数据行 in it:
            #数据行数据
            #yield ((公历年份, 公历月份, 公历日份), 農曆日期, 星期, 可選節氣)
            yield sf.读取数据行(数据行)
    def 读取数据行(sf, 数据行, /):
        数据行 = 数据行.strip()
        if 1:
            m = 数据行正则表达式.fullmatch(数据行)
            if m is None:
                raise FormatError(f'bad format:unknown 数据行:{数据行!r}')

            ##################
            公历年份 = m['公历年份']
            公历月份 = m['公历月份']
            公历日份 = m['公历日份']

            農曆日期 = m['農曆日期']
            星期 = m['星期']
            可選節氣 = m['節氣']
            if 可選節氣 is None:
                可選節氣 = ''

            return ((公历年份, 公历月份, 公历日份), 農曆日期, 星期, 可選節氣)


    def 解析所有数据并检查数据(sf, /,*, idir):
        r'''
        检查结果:
            * 生肖 未检查 #而且 文件头行 自 2058 起 取消
            * 整个 2051 年文件 星期 错位 偏移一天
            * 其他正常
                * 手动检查 1901 确实是 辛丑年#1901辛丑条约
                * 标准库检查 公历年月日 的 递增
                * 标准库检查 真实星期

        #'''
        year2may_file_header_data, year2row_data_list = sf.read_all_txt_ifile(idir=idir, 解析与否=True)
        one_day = datetime.timedelta(days=1)

        if 1:
            距离前一个节气几天 = 0
            可选前一天农历年份 = None
            可选前一天公历年月日 = None
            可选前一天農曆日份 = None
            可选前一天農曆月份 = None
            可选前一天農曆月份閏月與否 = None
            可选前一天星期索引 = None
            可选前一个年份干支索引 = None
            可选前一个节气索引 = None
        for year in sf.iter_all_years():

            ##################
            ##################
            may_file_header_data = year2may_file_header_data[year]
            if may_file_header_data:
                [file_header_data] = may_file_header_data
                文件头行数据已解析 = file_header_data
                (公历年份, 年份干支索引) = 文件头行数据已解析
                assert 公历年份 == year
                #新的公历年开始
                if 可选前一天农历年份 is not None:
                    前一天农历年份 = 可选前一天农历年份
                    #print(前一天农历年份)
                    assert (前一天农历年份+1) == 公历年份
                #bug:前一天农历年份 = 可选前一天农历年份 = 公历年份-1 #this round
                #   文件头行 可能不存在

                if 可选前一个年份干支索引 is not None:
                    前一个年份干支索引 = 可选前一个年份干支索引
                    assert (前一个年份干支索引+1)%60 == 年份干支索引
            if may_file_header_data:
                前一天农历年份 = 可选前一天农历年份 = 公历年份-1
                    #this round
                可选前一个年份干支索引 = 年份干支索引
                    #next round
            else:
                #   文件头行 可能不存在
                前一天农历年份 = 可选前一天农历年份 = year-1
                    #this round
                if 可选前一个年份干支索引 is not None:
                    前一个年份干支索引 = 可选前一个年份干支索引
                    可选前一个年份干支索引 = (前一个年份干支索引+1)%60
                        #next round

                #... ...

            ##################
            ##################
            row_data_list = year2row_data_list[year]
            for 数据行数据已解析 in row_data_list:
                ((公历年份, 公历月份, 公历日份), (可選閏月與否, 可選農曆月份, 農曆日份,), 星期索引, 可選節氣索引) = 数据行数据已解析
                if 0:#[01]
                    print((公历年份, 公历月份, 公历日份))
                assert 公历年份 == year
                本行公历年月日 = 求公历年公历月公历日的相应公历年月日(公历年份, 公历月份, 公历日份)
                if 可选前一天公历年月日 is not None:
                    前一天公历年月日 = 可选前一天公历年月日
                    assert 前一天公历年月日+one_day == 本行公历年月日
                可选前一天公历年月日 = 本行公历年月日
                    #next round

                assert (可選閏月與否 is None) is (可選農曆月份 is None) is (農曆日份 != 1)
                if 可选前一天農曆日份 is not None:
                    前一天農曆日份 = 可选前一天農曆日份
                    if 農曆日份 == 1:
                        #新的农历月份开始
                        assert 前一天農曆日份 in (29,30)
                    else:
                        assert 前一天農曆日份 + 1 == 農曆日份
                else:
                    pass
                可选前一天農曆日份 = 農曆日份
                    #next round

                if 農曆日份 == 1:
                    #新的农历月份开始
                    閏月與否, 農曆月份 = 可選閏月與否, 可選農曆月份
                    if 可选前一天農曆月份 is not None:
                        前一天農曆月份 = 可选前一天農曆月份
                        前一天農曆月份閏月與否 = 可选前一天農曆月份閏月與否
                        assert 前一天農曆月份閏月與否+閏月與否 <= 1
                        if 閏月與否:
                            assert 前一天農曆月份 == 農曆月份
                        else:
                            if 農曆月份 == 1:
                                #新的农历年开始
                                assert 前一天農曆月份 == 12
                            else:
                                assert 前一天農曆月份+1 == 農曆月份
                else:
                    pass


                if 農曆日份 == 1 and 農曆月份 == 1 and not 閏月與否:
                    #新的农历年开始
                    ##################
                    可选前一天农历年份 = 前一天农历年份+1
                        #next round
                    if 0:#[01]
                        print(前一天农历年份)
                        print(可选前一天农历年份)
                        print(公历年份)
                    assert 可选前一天农历年份 == 公历年份
                    ##################
                    if 可选前一个节气索引 is not None:
                        前一个节气索引 = 可选前一个节气索引
                        #bug:assert 前一个节气索引 == 23
                        #       立春可能在正月春节前！
                        #bug:assert 前一个节气索引 == 0
                        #       立春可能在正月春节后！
                        #bug:assert 前一个节气索引 in (23, 0)
                        #       雨水可能在正月春节前！
                        assert 前一个节气索引 in (23, 0, 1)




                if 1:
                    真实星期索引 = 本行公历年月日.isoweekday()%7
                    文件存储的星期索引 = 星期索引
                    if 文件存储的星期索引 != 真实星期索引:
                        print_err(f'星期出错: {(公历年份, 公历月份, 公历日份)}: 文件存储的星期索引={文件存储的星期索引}, 真实星期索引={真实星期索引}')

                if 文件存储的星期索引 == 真实星期索引:
                    assert 本行公历年月日.isoweekday()%7 == 星期索引

                    if 可选前一天星期索引 is not None:
                        前一天星期索引 = 可选前一天星期索引
                        #assert (前一天星期索引+1)%7 == 星期索引
                        if (前一天星期索引+1)%7 != 星期索引:
                            print_err(f'星期出错: {(公历年份, 公历月份, 公历日份)}: 文件存储的星期索引={文件存储的星期索引}, 文件存储的前一天星期索引={前一天星期索引}')
                可选前一天星期索引 = 星期索引
                    #next round

                可選節氣索引
                距离前一个节气几天 += 1
                assert 距离前一个节气几天 < 366//24+3
                if 可選節氣索引 is not None:
                    節氣索引 = 可選節氣索引
                    if 可选前一个节气索引 is not None:
                        前一个节气索引 = 可选前一个节气索引
                        assert (前一个节气索引+1)%24 == 節氣索引
                        assert 距离前一个节气几天 > 366//24-3
                    可选前一个节气索引 = 節氣索引
                        #next round
                    距离前一个节气几天 = 0
                        #next round


                #... ...

    #end-def 解析所有数据并检查数据(sf, /,*, idir):
    def 解析所有数据并计算关键数据(sf, /,*, idir, result_as_dict_not_tuple:bool):
        r'''
        农历起始月的年份
        农历起始月的月份
        农历各月初一的相应公历日期并闰月与否
        农历起始节气的节气索引
        农历各节气的相应公历日期
        ====

    农历各月天数~~~~农历各月初一的相应公历日期
        农历起始月的年份
        农历起始月的月份
        农历起始月初一的相应公历日期
        不完整的最后一个农历月的初一的相应公历日期
    农历相邻闰月的月份距离~~~~农历各闰月相对于农历起始月的月份距离~~~~农历各月初一的相应公历日期并闰月与否
        农历起始闰月相对于农历起始月的月份距离
    农历相邻节气的日份距离~~~~农历各节气的相应公历日期
        农历起始节气相对于农历起始月初一的日份距离
        农历起始节气的节气索引
        #'''
        (农历起始月的年份,农历起始月的月份,农历各月初一的相应公历日期并闰月与否,农历起始节气的节气索引,农历各节气的相应公历日期) = sf._解析所有数据并计算关键数据(idir=idir)
        ######################
        ######################
        农历各月天数 = [
            求日份距离(succ[0], curr[0])
            for curr, succ in zip_me2(农历各月初一的相应公历日期并闰月与否)
        ]

        农历起始月初一的相应公历日期 = 农历各月初一的相应公历日期并闰月与否[0][0]


        不完整的最后一个农历月的初一的相应公历日期 = 农历各月初一的相应公历日期并闰月与否[-1][0]
        农历各闰月相对于农历起始月的月份距离 = [
            相对于农历起始月的月份距离
            for 相对于农历起始月的月份距离, (_, 闰月与否) in enumerate(农历各月初一的相应公历日期并闰月与否[:-1])
            if 闰月与否
        ]

        农历相邻闰月的月份距离 = [
            succ - curr
            for curr, succ in zip_me2(农历各闰月相对于农历起始月的月份距离)
        ]

        农历起始闰月相对于农历起始月的月份距离 = 农历各闰月相对于农历起始月的月份距离[0]


        农历相邻节气的日份距离 = [
            求日份距离(succ, curr)
            for curr, succ in zip_me2(itertools.takewhile(不完整的最后一个农历月的初一的相应公历日期.__gt__, 农历各节气的相应公历日期))
        ]

        农历起始节气相对于农历起始月初一的日份距离 = 求日份距离(农历各节气的相应公历日期[0], 农历起始月初一的相应公历日期)
        assert 农历起始节气相对于农历起始月初一的日份距离 >= 0

        农历起始节气的节气索引

        if 1:
            assert min(农历各月天数, default=30) >= 29
            assert max(农历各月天数, default=29) <= 30

            assert min(农历相邻闰月的月份距离, default=36) >= 29
            assert max(农历相邻闰月的月份距离, default=29) <= 36
            assert 0 <= 农历起始闰月相对于农历起始月的月份距离 <= 36

            assert min(农历相邻节气的日份距离, default=16) >= 14
            assert max(农历相邻节气的日份距离, default=14) <= 16
            assert 0 <= 农历起始节气相对于农历起始月初一的日份距离 <= 16

        if 0:
            assert min(农历各月天数) == 29
            assert max(农历各月天数) == 30

            assert min(农历相邻闰月的月份距离) == 29
            assert max(农历相邻闰月的月份距离) == 36

            assert min(农历相邻节气的日份距离) == 14
            assert max(农历相邻节气的日份距离) == 16



        农历起始月初一的相应公历日期 = date2tuple(农历起始月初一的相应公历日期)
        不完整的最后一个农历月的初一的相应公历日期 = date2tuple(不完整的最后一个农历月的初一的相应公历日期)
        result__tuple = (
            农历各月天数#29,30#1bit*M
                ,农历起始月的年份
                ,农历起始月的月份
                ,农历起始月初一的相应公历日期
                ,不完整的最后一个农历月的初一的相应公历日期
            ,农历相邻闰月的月份距离#29..36#3bit*R
                ,农历起始闰月相对于农历起始月的月份距离#0..36#6bit
            ,农历相邻节气的日份距离#14..16#2bit*J
                ,农历起始节气相对于农历起始月初一的日份距离#0..16#5bit
                ,农历起始节气的节气索引
            )

        result__dict = 未打包关键数据=unpacked_kwargs= dict\
        (农历各月天数=农历各月天数
            ,农历起始月的年份=农历起始月的年份
            ,农历起始月的月份=农历起始月的月份
            ,农历起始月初一的相应公历日期=农历起始月初一的相应公历日期
            ,不完整的最后一个农历月的初一的相应公历日期=不完整的最后一个农历月的初一的相应公历日期
        ,农历相邻闰月的月份距离=农历相邻闰月的月份距离
            ,农历起始闰月相对于农历起始月的月份距离=农历起始闰月相对于农历起始月的月份距离
        ,农历相邻节气的日份距离=农历相邻节气的日份距离
            ,农历起始节气相对于农历起始月初一的日份距离=农历起始节气相对于农历起始月初一的日份距离
            ,农历起始节气的节气索引=农历起始节气的节气索引
            )
        assert len(unpacked_kwargs) == 10
        assert len(result__tuple) == 10
        assert len(result__dict) == 10
        return result__dict if result_as_dict_not_tuple else result__tuple
        (农历各月天数
            ,农历起始月的年份
            ,农历起始月的月份
            ,农历起始月初一的相应公历日期
            ,不完整的最后一个农历月的初一的相应公历日期
        ,农历相邻闰月的月份距离
            ,农历起始闰月相对于农历起始月的月份距离
        ,农历相邻节气的日份距离
            ,农历起始节气相对于农历起始月初一的日份距离
            ,农历起始节气的节气索引
        ) = result__tuple

    #end-def 解析所有数据并计算关键数据(sf, /,*, idir):


    def _解析所有数据并计算关键数据(sf, /,*, idir):
        year2may_file_header_data, year2row_data_list = sf.read_all_txt_ifile(idir=idir, 解析与否=True)
        del year2may_file_header_data
        one_day = datetime.timedelta(days=1)

        if 1:
            农历起始月的年份 = None
            农历起始月的月份 = None
            农历各月初一的相应公历日期并闰月与否 = [] #[(初一的相应公历日期, 闰月与否)]
            农历起始节气的节气索引 = None
            农历各节气的相应公历日期 = []

        if 1:
            可选前一天农历年份 = None
        for year in sf.iter_all_years():
            ##################
            if 可选前一天农历年份 is None:
                可选前一天农历年份 = year-1
                    #this round
            前一天农历年份 = 可选前一天农历年份
            ##################
            ##################
            row_data_list = year2row_data_list[year]
            for 数据行数据已解析 in row_data_list:
                ((公历年份, 公历月份, 公历日份), (可選閏月與否, 可選農曆月份, 農曆日份,), 星期索引, 可選節氣索引) = 数据行数据已解析
                if 0:#[01]
                    print((公历年份, 公历月份, 公历日份))
                assert 公历年份 == year
                本行公历年月日 = 求公历年公历月公历日的相应公历年月日(公历年份, 公历月份, 公历日份)

                assert (可選閏月與否 is None) is (可選農曆月份 is None) is (農曆日份 != 1)

                if 農曆日份 == 1:
                    #新的农历月份开始
                    閏月與否, 農曆月份 = 可選閏月與否, 可選農曆月份

                if 農曆日份 == 1 and 農曆月份 == 1 and not 閏月與否:
                    #新的农历年开始
                    ##################
                    本行农历年份 = 前一天农历年份+1
                    assert 本行农历年份 == 公历年份
                    可选前一天农历年份 = 本行农历年份
                        #next round
                else:
                    本行农历年份 = 前一天农历年份
                本行农历年份

                if 農曆日份 == 1:
                    #新的农历月份开始
                    农历各月初一的相应公历日期并闰月与否.append((本行公历年月日, 閏月與否))
                    if 农历起始月的年份 is None:
                        农历起始月的年份 = 本行农历年份
                        农历起始月的月份 = 農曆月份


                if 农历起始月的年份 is not None:
                    可選節氣索引
                    if 可選節氣索引 is not None:
                        節氣索引 = 可選節氣索引
                        if 农历起始节气的节气索引 is None:
                            农历起始节气的节气索引 = 節氣索引
                        农历各节气的相应公历日期.append(本行公历年月日)
        return (农历起始月的年份,农历起始月的月份,农历各月初一的相应公历日期并闰月与否,农历起始节气的节气索引,农历各节气的相应公历日期)

    #end-def _解析所有数据并计算关键数据(sf, /,*, idir):
#end-class 读取香港天文台农历对照表文字版(相关常用函数集合):


class _T:
    #path4unpacked_kwargs = r'/sdcard/0my_files/git_repos/txt_phone/txt/script/农历/农历.py.解析所有数据并计算关键数据.out.txt'
    path4unpacked_kwargs = Path(__file__).parent/r'农历.py.解析所有数据并计算关键数据.out.txt'
    path4packed_kwargs = Path(__file__).parent/r'农历.py.解析所有数据并计算关键数据.out.已打包.txt'
    unpacked_names = ('农历各月天数', '农历相邻闰月的月份距离', '农历相邻节气的日份距离')
    packed_names = ('农历各月天数已打包', '农历相邻闰月的月份距离已打包', '农历相邻节气的日份距离已打包')
    packed_kwargs__txt = 已打包关键数据的输出文件内容 = globals()['已打包关键数据的输出文件内容']

    def _impl_打印公历农历日期对照表(sf, /,*
        , may_fout
        , 农历各月天数
            ,农历起始月的年份
            ,农历起始月的月份
            ,农历起始月初一的相应公历日期
            ,不完整的最后一个农历月的初一的相应公历日期
        ,农历相邻闰月的月份距离
            ,农历起始闰月相对于农历起始月的月份距离
        ,农历相邻节气的日份距离
            ,农历起始节气相对于农历起始月初一的日份距离
            ,农历起始节气的节气索引
        ):
        r'''
        公历日期: g{yyyy}{mm}{dd}x{w}
        农历日期:
            * 农历闰月日期: n{yyyy}{mm}r{dd}
            * 农历常月日期: n{yyyy}{mm}c{dd}
                #为何 不是 r{mm}? 方便 排序
        农历节气信息后缀:
            *  节气: j{jj}
            *  非节气/平常普通: fJQ
        ########################
        g:gong_li:公历
        n:nong_li:农历
        x:xing_qi:星期
        r:run_yue:闰月
        c:chang_yue:常月
        j:jie_qi:节气
        fJQ:fei_jie_qi:非节气
        #p:ping_chang/pu_tong:非节气
        ########################
        #mk _data4verify via gvim:
        #   /#.*: \(\w*\)=\(\w*\)
        #   :.,.+19s//,\1='\2'
        #==>> _打印公历农历日期对照表() 输出的第一行: g19010120x0=n190012c01fJQ
        #==>> _打印公历农历日期对照表() 输出的最后一行: g21001230x4=n210011c30fJQ
        #==>> _打印公历农历日期对照表() 输出的第一个春节: g19010219x2=n190101c01j01
        #==>> _打印公历农历日期对照表() 输出的第二个春节: g19020208x6=n190201c01fJQ
        #==>> _打印公历农历日期对照表() 输出的第一个闰月初一: g19030625x4=n190305r01fJQ
        #==>> _打印公历农历日期对照表() 输出的第二个闰月初一: g19060523x3=n190604r01fJQ
        #==>> _打印公历农历日期对照表() 输出的第三个初一: g19010320x3=n190102c01fJQ
        #==>> _打印公历农历日期对照表() 输出的第一个闰月的下一个初一: g19030724x5=n190306c01j11
        #==>> _打印公历农历日期对照表() 输出的第二个闰月的下一个初一: g19060622x5=n190605c01j09
        #==>> _打印公历农历日期对照表() 输出的2021年中秋节: g20210921x2=n202108c15fJQ
        #==>> _打印公历农历日期对照表() 输出的2021年八月初一白露: g20210907x2=n202108c01j14
        #==>> _打印公历农历日期对照表() 输出的2020年闰四月初一: g20200523x6=n202004r01fJQ
        #==>> _打印公历农历日期对照表() 输出的第一个节气: g19010121x1=n190012c02j23
        #==>> _打印公历农历日期对照表() 输出的第二个节气: g19010204x1=n190012c16j00
        ##重复 第一个春节##==>> _打印公历农历日期对照表() 输出的第三个节气: g19010219x2=n190101c01j01
        #==>> _打印公历农历日期对照表() 输出的第四个节气: g19010306x3=n190101c16j02
        #==>> _打印公历农历日期对照表() 输出的倒数第一个节气: g21001222x3=n210011c22j21
        #==>> _打印公历农历日期对照表() 输出的倒数第二个节气: g21001207x2=n210011c07j20
        #==>> _打印公历农历日期对照表() 输出的倒数第三个节气: g21001122x1=n210010c21j19
        #==>> _打印公历农历日期对照表() 输出的倒数第四个节气: g21001107x0=n210010c06j18
        #'''
        _data4verify = dict(
            g19010120x0='n190012c01fJQ'
            ,g21001230x4='n210011c30fJQ'
            ,g19010219x2='n190101c01j01'
            ,g19020208x6='n190201c01fJQ'
            ,g19030625x4='n190305r01fJQ'
            ,g19060523x3='n190604r01fJQ'
            ,g19010320x3='n190102c01fJQ'
            ,g19030724x5='n190306c01j11'
            ,g19060622x5='n190605c01j09'
            ,g20210921x2='n202108c15fJQ'
            ,g20210907x2='n202108c01j14'
            ,g20200523x6='n202004r01fJQ'
            ,g19010121x1='n190012c02j23'
            ,g19010204x1='n190012c16j00'
            ,g19010306x3='n190101c16j02'
            ,g21001222x3='n210011c22j21'
            ,g21001207x2='n210011c07j20'
            ,g21001122x1='n210010c21j19'
            ,g21001107x0='n210010c06j18'
            )
        _g_dates_of_data4verify = {k[:-2] for k in _data4verify}
        g_date0 = 求公历年公历月公历日的相应公历年月日(*农历起始月初一的相应公历日期)
        n_year0 = 农历起始月的年份
        n_month0 = 农历起始月的月份
        n_day0 = 1 #初一
            #不完整的第一个农历月的闰月与否 未知，是故 从 第一个完整月的初一 开始
        g_date_end = 求公历年公历月公历日的相应公历年月日(*不完整的最后一个农历月的初一的相应公历日期)
        if not g_date0 < g_date_end: raise ValueError
        one_day = datetime.timedelta(days=1)
        g_date_fmt = 'g%Y%m%dx%w'
        _cr_ = 'cr'
        #n_date_fmt = 'n{n_year:0>4}{n_month:0>2}{_cr_[int(is_n_leap_month)]}{n_day:0>2}'
        n_date_fmt = 'n{n_year:0>4}{n_month:0>2}{c_or_r}{n_day:0>2}'
        jq_fmt = 'j{jq_idx:0>2}'
        fjq_fmt = 'fJQ'
        fprint = mk_fprint(may_fout)
        def next_or_raise(iterator, err):
            assert iter(iterator) is iterator
            for head in iterator:
                return head
            raise err
        if 1:
            #确保 下面 distance_of_next_leap_month_include_curr_month_to_curr_month=3000 的处理 有界 不至于溢出
            农历相邻闰月的月份距离的上限 = 40
                #int_lower_bound = 29, int_upper_bound = 36
                #72==36*2 < 2*x < 29*3==87
                #choose 2*x=80
            if not len(农历相邻闰月的月份距离) <= len(农历各月天数): raise ValueError
            if not 农历起始闰月相对于农历起始月的月份距离+sum(农历相邻闰月的月份距离) <= len(农历各月天数): raise ValueError
            if not max(农历起始闰月相对于农历起始月的月份距离, *农历相邻闰月的月份距离) <= 农历相邻闰月的月份距离的上限: raise ValueError
            if not len(农历各月天数) <= 农历起始闰月相对于农历起始月的月份距离+sum(农历相邻闰月的月份距离)+农历相邻闰月的月份距离的上限: raise ValueError
                #考虑到 不完整的最后一个农历月 的 来月 起 的下一个闰月信息 并不存在
            if 1:
                #改用itertools.chain+检查sum
                using_itertools_chain = True
                pass
            #####################
            #节气相关
            农历相邻节气的日份距离的上限 = 18
                #lower_bound = 14, int_upper_bound = 16
                #32==16*2 < 2*x < 14*3==42
                #choose 2*x=36
            if not sum(农历相邻节气的日份距离) <= sum(农历各月天数): raise ValueError
            if not 农历起始节气相对于农历起始月初一的日份距离+sum(农历相邻节气的日份距离) <= sum(农历各月天数): raise ValueError
            if not max(农历起始节气相对于农历起始月初一的日份距离, *农历相邻节气的日份距离) <= 农历相邻节气的日份距离的上限: raise ValueError
            if not sum(农历各月天数) <= 农历起始节气相对于农历起始月初一的日份距离+sum(农历相邻节气的日份距离)+农历相邻节气的日份距离的上限: raise ValueError
                #考虑到 不完整的最后一个农历月 的 初二 起 的下一个节气信息 并不存在
        if 1:
            # loop-init
            g_date = g_date0
            n_year = n_year0
            n_month = n_month0
            n_day = n_day0
            iter_num_days_per_month = iter(农历各月天数)
            if using_itertools_chain:
                #改用itertools.chain+检查sum
                iter_distance_of_neighbor_leap_months_ex = itertools.chain(农历相邻闰月的月份距离, [农历相邻闰月的月份距离的上限])
            else:
                iter_distance_of_neighbor_leap_months = iter(农历相邻闰月的月份距离)
            distance_of_next_leap_month_include_curr_month_to_curr_month = 农历起始闰月相对于农历起始月的月份距离
                #本农历月份起的下一个闰月与本农历月份的月份距离 #下一个闰月 含 本月
            assert  0 <= distance_of_next_leap_month_include_curr_month_to_curr_month
            is_n_leap_month = 0==distance_of_next_leap_month_include_curr_month_to_curr_month
                #本农历月份闰月与否
            ######################
            ######################
            #节气相关
            if using_itertools_chain:
                #改用itertools.chain+检查sum
                iter_jq_distances_ex = itertools.chain(农历相邻节气的日份距离, [农历相邻节气的日份距离的上限])
            else:
                iter_jq_distances = iter(农历相邻节气的日份距离)
            jq_distance = 农历起始节气相对于农历起始月初一的日份距离
                #本农历日份起的下一个节气与本农历日份的日份距离 #下一个节气 含 本日
                #今天起下一个节气相对于今天的日份距离
            assert 0 <= jq_distance
            is_today_jq = 0==jq_distance
                #今天是某个节气与否
            the_coming_jq_idx = 农历起始节气的节气索引
                #今天起下一个节气的节气索引
        while g_date != g_date_end:
            if 1:
                #今天相关信息，已更新
                g_date, n_year, n_month, n_day, distance_of_next_leap_month_include_curr_month_to_curr_month, is_n_leap_month
                ######################
                #节气相关
                jq_distance, the_coming_jq_idx, is_today_jq
            if 1:
                # round-init
                # have not been updated: remain_num_days_of_curr_month_include_today
                if n_day == 1:
                    # 开始 新的农历月份
                    remain_num_days_of_curr_month_include_today = next_or_raise(iter_num_days_per_month, LengthError)
                    assert 29 <= remain_num_days_of_curr_month_include_today <= 30
                    if n_month == 1 and not is_n_leap_month:
                        # 开始 新的农历年份
                        pass
                else:
                    remain_num_days_of_curr_month_include_today -= 1
                assert 0 < remain_num_days_of_curr_month_include_today
            ######################
            if 1:
                # round-body
                g_date_str = g_date.strftime(g_date_fmt)
                assert type(is_n_leap_month) is bool
                n_date_str = n_date_fmt.format(n_year=n_year, c_or_r='cr'[is_n_leap_month], n_month=n_month, n_day=n_day)
                if is_today_jq:
                    #今天是某个节气
                    jq_idx4today = the_coming_jq_idx
                    jq_str = jq_fmt.format(jq_idx=jq_idx4today)
                else:
                    jq_str = fjq_fmt.format()
                jq_str

                if 1:
                    #main_job
                    fprint(f'{g_date_str}={n_date_str}{jq_str}')
                if 1:
                    #verify
                    #if g_date_str in _data4verify:
                    if g_date_str[:-2] in _g_dates_of_data4verify:
                        #排除 星期信息 减少 手录错误
                        try:
                            assert n_date_str+jq_str == _data4verify[g_date_str]
                        except (AssertionError, KeyError):
                            print_err(f'g_date_str={g_date_str!r}; n_date_str={n_date_str!r}; jq_str={jq_str!r}')
                            raise
                if 1:
                    #clean
                    del g_date_str
                    del n_date_str
                    del jq_str
            ######################
            if 1:
                # next round prepare
                g_date += one_day
                if remain_num_days_of_curr_month_include_today == 1:
                    #今天是本农历月份的最后一天
                    #明天初一
                    # 开始 新的农历月份
                    n_day = 1
                        #明天的农历日份
                    assert 0 <= distance_of_next_leap_month_include_curr_month_to_curr_month
                        #本农历月份起的下一个闰月与本农历月份的月份距离
                    if is_n_leap_month:
                        #本农历月份 是 闰月
                        assert 0 == distance_of_next_leap_month_include_curr_month_to_curr_month
                        if using_itertools_chain:
                            #改用itertools.chain+检查sum
                            distance_of_next_leap_month_include_curr_month_to_curr_month = next_or_raise(iter_distance_of_neighbor_leap_months_ex, LengthError)
                        else:
                            #无论 不完整的最后一个农历月 是否闰月，长度缺一:distance_of_next_leap_month_include_curr_month_to_curr_month = next_or_raise(iter_distance_of_neighbor_leap_months, LengthError)
                            for distance_of_next_leap_month_include_curr_month_to_curr_month in iter_distance_of_neighbor_leap_months:
                                #下一个农历月份起的下一个闰月与本农历月份的月份距离
                                break
                            else:
                                #本农历月份 是 最后一个闰月
                                distance_of_next_leap_month_include_curr_month_to_curr_month = 3000
                    else:
                        #本农历月份 不是 闰月
                        assert 0 < distance_of_next_leap_month_include_curr_month_to_curr_month
                            #下一个农历月份起的下一个闰月与本农历月份的月份距离 == 本农历月份起的下一个闰月与本农历月份的月份距离
                        pass
                    assert 0 < distance_of_next_leap_month_include_curr_month_to_curr_month
                        #下一个农历月份起的下一个闰月与本农历月份的月份距离
                    distance_of_next_leap_month_include_curr_month_to_curr_month -= 1
                        #下一个农历月份起的下一个闰月与下一个农历月份的月份距离 = -1+下一个农历月份起的下一个闰月与本农历月份的月份距离
                    is_n_leap_month = 0==distance_of_next_leap_month_include_curr_month_to_curr_month
                        #下一个农历月份 闰月与否
                    if is_n_leap_month:
                        #下一个农历月份 是 闰月
                        # 月份 不改
                        # 年份 不改
                        pass
                    else:
                        #下一个农历月份 不是 闰月
                        # 月份 更改
                        if n_month == 12:
                            # 开始 新的农历年份
                            n_month = 1
                            n_year += 1
                        else:
                            n_month += 1
                else:
                    n_day += 1
                ######################
                ######################
                # 节气相关 next round prepare
                assert 0 <= jq_distance
                    #今天起下一个节气相对于今天的日份距离
                if is_today_jq:
                    assert 0 == jq_distance
                    #今天是某个节气
                    jq_idx4today = the_coming_jq_idx
                    the_coming_jq_idx += 1
                    the_coming_jq_idx %= 24
                        #明天起下一个节气的节气索引 = (1+今天起下一个节气的节气索引)%24
                        #
                    #jq_distance = next_or_raise(iter_jq_distances_ex, LengthError)
                        #明天起下一个节气相对于今天的日份距离
                    if using_itertools_chain:
                        #改用itertools.chain+检查sum
                        jq_distance = next_or_raise(iter_jq_distances_ex, LengthError)
                            #明天起下一个节气相对于今天的日份距离
                    else:
                        #无论 不完整的最后一个农历月的初一 是否节气，长度缺一:jq_distance = next_or_raise(iter_jq_distances, LengthError)
                        for jq_distance in iter_jq_distances:
                            #明天起的下一个节气与今天的日份距离
                            break
                        else:
                            #今天 是 最后一个节气
                            jq_distance = 3000
                    assert 0 < jq_distance
                        #明天起下一个节气相对于今天的日份距离
                else:
                    #今天不是任何节气
                    assert 0 < jq_distance
                    jq_distance = jq_distance
                        #明天起下一个节气相对于今天的日份距离 = 今天起下一个节气相对于今天的日份距离
                assert 0 < jq_distance
                    #明天起下一个节气相对于今天的日份距离
                jq_distance -= 1
                    #明天起下一个节气相对于明天的日份距离 = -1+明天起下一个节气相对于今天的日份距离
                assert 0 <= jq_distance
                is_today_jq = 0==jq_distance
                    #明天是某个节气与否
                #... ...
    def _打印公历农历日期对照表(sf, unpacked_kwargs, /,*, may_fout):
        未打包关键数据 = unpacked_kwargs
        assert len(unpacked_kwargs) == 10
        return sf._impl_打印公历农历日期对照表(may_fout=may_fout, **unpacked_kwargs)
        if 1:
            农历各月天数 = unpacked_kwargs["农历各月天数"]
            农历起始月的年份 = unpacked_kwargs["农历起始月的年份"]
            农历起始月的月份 = unpacked_kwargs["农历起始月的月份"]
            农历起始月初一的相应公历日期 = unpacked_kwargs["农历起始月初一的相应公历日期"]
            不完整的最后一个农历月的初一的相应公历日期 = unpacked_kwargs["不完整的最后一个农历月的初一的相应公历日期"]
            农历相邻闰月的月份距离 = unpacked_kwargs["农历相邻闰月的月份距离"]
            农历起始闰月相对于农历起始月的月份距离 = unpacked_kwargs["农历起始闰月相对于农历起始月的月份距离"]
            农历相邻节气的日份距离 = unpacked_kwargs["农历相邻节气的日份距离"]
            农历起始节气相对于农历起始月初一的日份距离 = unpacked_kwargs["农历起始节气相对于农历起始月初一的日份距离"]
            农历起始节气的节气索引 = unpacked_kwargs["农历起始节气的节气索引"]

    def _打印未打包关键数据(sf, unpacked_kwargs, /,*, may_fout):
        未打包关键数据 = unpacked_kwargs
        assert len(unpacked_kwargs) == 10
        fprint = mk_fprint(may_fout)
        if 1:
            fprint(f'农历各月天数={unpacked_kwargs["农历各月天数"]!r}')
            fprint(f'农历起始月的年份={unpacked_kwargs["农历起始月的年份"]!r}')
            fprint(f'农历起始月的月份={unpacked_kwargs["农历起始月的月份"]!r}')
            fprint(f'农历起始月初一的相应公历日期={unpacked_kwargs["农历起始月初一的相应公历日期"]!r}')
            fprint(f'不完整的最后一个农历月的初一的相应公历日期={unpacked_kwargs["不完整的最后一个农历月的初一的相应公历日期"]!r}')
            fprint(f'农历相邻闰月的月份距离={unpacked_kwargs["农历相邻闰月的月份距离"]!r}')
            fprint(f'农历起始闰月相对于农历起始月的月份距离={unpacked_kwargs["农历起始闰月相对于农历起始月的月份距离"]!r}')
            fprint(f'农历相邻节气的日份距离={unpacked_kwargs["农历相邻节气的日份距离"]!r}')
            fprint(f'农历起始节气相对于农历起始月初一的日份距离={unpacked_kwargs["农历起始节气相对于农历起始月初一的日份距离"]!r}')
            fprint(f'农历起始节气的节气索引={unpacked_kwargs["农历起始节气的节气索引"]!r}')


    def _打印已打包关键数据(sf, packed_kwargs, /,*, may_fout):
        已打包关键数据 = packed_kwargs
        assert len(packed_kwargs) == 10
        fprint = mk_fprint(may_fout)
        if 1:
            fprint(f'农历各月天数已打包={packed_kwargs["农历各月天数已打包"]!r}')
            fprint(f'农历起始月的年份={packed_kwargs["农历起始月的年份"]!r}')
            fprint(f'农历起始月的月份={packed_kwargs["农历起始月的月份"]!r}')
            fprint(f'农历起始月初一的相应公历日期={packed_kwargs["农历起始月初一的相应公历日期"]!r}')
            fprint(f'不完整的最后一个农历月的初一的相应公历日期={packed_kwargs["不完整的最后一个农历月的初一的相应公历日期"]!r}')
            fprint(f'农历相邻闰月的月份距离已打包={packed_kwargs["农历相邻闰月的月份距离已打包"]!r}')
            fprint(f'农历起始闰月相对于农历起始月的月份距离={packed_kwargs["农历起始闰月相对于农历起始月的月份距离"]!r}')
            fprint(f'农历相邻节气的日份距离已打包={packed_kwargs["农历相邻节气的日份距离已打包"]!r}')
            fprint(f'农历起始节气相对于农历起始月初一的日份距离={packed_kwargs["农历起始节气相对于农历起始月初一的日份距离"]!r}')
            fprint(f'农历起始节气的节气索引={packed_kwargs["农历起始节气的节气索引"]!r}')

    def _读并打包并写(sf, ipath4unpacked_kwargs, opath4packed_kwargs, /):
        if ipath4unpacked_kwargs is None:
            ipath4unpacked_kwargs = sf.path4unpacked_kwargs
        ipath4unpacked_kwargs = Path(ipath4unpacked_kwargs)
        if opath4packed_kwargs is None:
            opath4packed_kwargs = sf.path4packed_kwargs
        opath4packed_kwargs = Path(opath4packed_kwargs)
        #################################
        unpacked_kwargs = sf._读取_解析所有数据并计算关键数据_的输出(ipath4unpacked_kwargs)
        assert len(unpacked_kwargs) == 10
        packed_kwargs = sf._打包关键数据(**unpacked_kwargs)
        with open(opath4packed_kwargs, 'xt', encoding='utf8') as fout:
            sf._打印已打包关键数据(packed_kwargs, may_fout=fout)
        _2_unpacked_kwargs = sf._读取已打包关键数据并解包(opath4packed_kwargs)
        assert _2_unpacked_kwargs == unpacked_kwargs
        return
    def _读取已打包关键数据并解包(sf, ipath4packed_kwargs=None, /, input_is_text_not_path=False):
        if input_is_text_not_path:
            txt = ipath4packed_kwargs
            if type(txt) is not str: raise TypeError
        else:
            if ipath4packed_kwargs is None:
                ipath4packed_kwargs = sf.path4packed_kwargs
            ipath4packed_kwargs = Path(ipath4packed_kwargs)
            txt = ipath4packed_kwargs.read_text(encoding='utf8')
        del ipath4packed_kwargs
        txt
        packed_kwargs = safe_exec(txt, nonlocals=dict(Packer4BoundedIntSeq__little_endian=Packer4BoundedIntSeq__little_endian))
        return sf._解包关键数据(**packed_kwargs)
    def _解包关键数据(sf, /,**packed_kwargs):
        r'(**已打包关键数据) -> 未打包关键数据'
        assert len(packed_kwargs) == 10
        packed_kwargs['农历各月天数已打包']
        packed_kwargs['农历相邻闰月的月份距离已打包']
        packed_kwargs['农历相邻节气的日份距离已打包']
        unpacked_kwargs = {**packed_kwargs}
        for packed_name in sf.packed_names:
            assert packed_name.endswith('已打包')
            packed_ls = unpacked_kwargs.pop(packed_name)
            unpacked_ls = packed_ls.unpack()
            unpacked_name = packed_name[:-3]
            unpacked_kwargs[unpacked_name] = unpacked_ls
        return unpacked_kwargs
    def _打包关键数据(sf, /,**unpacked_kwargs):
        r'(**未打包关键数据) -> 已打包关键数据'
        assert len(unpacked_kwargs) == 10
        r'''
            农历各月天数#29,30#1bit*M
            ,农历相邻闰月的月份距离#29..36#3bit*R
            ,农历相邻节气的日份距离#14..16#2bit*J
        #'''
        unpacked_kwargs['农历各月天数']
        unpacked_kwargs['农历相邻闰月的月份距离']
        unpacked_kwargs['农历相邻节气的日份距离']
        #from seed.int_tools.digits.Packer4BoundedIntSeq import pack_from_bounded_int_seq, Packer4BoundedIntSeq, Packer4BoundedIntSeq__little_endian, Packer4BoundedIntSeq__big_endian
        packed_kwargs = {**unpacked_kwargs}
        for unpacked_name in sf.unpacked_names:
            #unpacked_ls = unpacked_kwargs[unpacked_name]
            unpacked_ls = packed_kwargs.pop(unpacked_name)
            (m, M) = minmax_default((0,0), unpacked_ls)
            packed_ls = pack_from_bounded_int_seq(unpacked_ls, int_lower_bound=m, int_upper_bound=M, is_big_endian=False)
            packed_name = unpacked_name + '已打包'
            packed_kwargs[packed_name] = packed_ls
        assert unpacked_kwargs == sf._解包关键数据(**packed_kwargs)
        return packed_kwargs

    def _读取_解析所有数据并计算关键数据_的输出(sf, ipath4unpacked_kwargs, /):
        r'即 读取 解析所有数据并计算关键数据() 的 输出文件 -> 未打包关键数据'
        if ipath4unpacked_kwargs is None:
            ipath4unpacked_kwargs = sf.path4unpacked_kwargs
        ipath4unpacked_kwargs = Path(ipath4unpacked_kwargs)
        txt = ipath4unpacked_kwargs.read_text(encoding='utf8')
        if 1:
            #from seed.helper.safe_eval import safe_eval, safe_exec, data_eval
            try:
                d = safe_exec(txt)
            except AttributeError as e:
                #AttributeError: 'mappingproxy' object has no attribute '__import__'
                if not str(e) == "'mappingproxy' object has no attribute '__import__'":
                    print_err(txt)
                raise
        else:
            txt = txt.strip()
            txt = txt.replace('\n', ',"')
            txt = txt.replace('=', '":')
            txt = f'{{"{txt}}}'
            d = ast.literal_eval(txt)
        assert len(d) == 10
        unpacked_kwargs = {k:(tuple(v) if type(v) is list else v) for k, v in d.items()}
        assert len(unpacked_kwargs) == 10
        return unpacked_kwargs










def _try_读取香港天文台农历对照表文字版():
    from seed.helper.case import otherwise, Case, clear_case, case2may_key, Flag, clear_flag, _flag2keys

    ipath_2021 = Path(r'/sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T2021c.txt')
    idir = ipath_2021.parent

    sf = 读取香港天文台农历对照表文字版()
    case = Case(
        尝试_打印公历农历日期对照表
        #尝试_读并打包并写
        #尝试_读取_解析所有数据并计算关键数据_的输出
        #尝试解析所有数据并计算关键数据
        #尝试解析所有数据并检查数据
        #尝试解析所有数据行数据并打印闰月
        #收集繁体节气名
        #基础测试尝试读取所有文件
        = True
        )
    if not case:
        pass
    elif case.尝试_打印公历农历日期对照表:
        已打包关键数据的输出文件内容
        未打包关键数据 = _T()._读取已打包关键数据并解包(已打包关键数据的输出文件内容, input_is_text_not_path=True)
        _T()._打印公历农历日期对照表(未打包关键数据, may_fout=None)
    elif case.尝试_读并打包并写:
        _T()._读并打包并写(_T.path4unpacked_kwargs, _T.path4packed_kwargs)
    elif case.尝试_读取_解析所有数据并计算关键数据_的输出:
        d = _T()._读取_解析所有数据并计算关键数据_的输出(_T.path4unpacked_kwargs)
    elif case.尝试解析所有数据并计算关键数据:
        if 0:
            year_first, year_last = 1901, 1903
            sf = 读取香港天文台农历对照表文字版(year_first=year_first, year_last=year_last)

        未打包关键数据=unpacked_kwargs = sf.解析所有数据并计算关键数据(idir=idir, result_as_dict_not_tuple=True)
        assert len(unpacked_kwargs) == 10
        _T()._打印未打包关键数据(unpacked_kwargs, may_fout=None)

    elif case.尝试解析所有数据并检查数据:
        if 0:
            year_last = 1901
            year_last = 1902
            year_last = 1980
            year_first = 1984
            year_last = 1989
            year_last = 2050
            year_first, year_last = 2048, 2100
            year_first, year_last = 2057, 2060
            year_first, year_last = 2059, 2100
            sf = 读取香港天文台农历对照表文字版(year_first=year_first, year_last=year_last)
        sf.解析所有数据并检查数据(idir=idir)
    elif case.尝试解析所有数据行数据并打印闰月:
        year2may_file_header_data, year2row_data_list = sf.read_all_txt_ifile(idir=idir)
        for row_data_list in year2row_data_list.values():
            for 数据行数据 in row_data_list:
                r = ((公历年份, 公历月份, 公历日份), (可選閏月與否, 可選農曆月份, 農曆日份,), 星期索引, 可選節氣索引) = sf.解析数据行数据(数据行数据)
                if 可選閏月與否:
                    #1901(辛丑-肖牛) 1901年01月01日 十一 星期二
                        ##==>> 1901_01_20__12_01__0
                        ##==>> ???1900_12_31__11_10__1???十一月？閏十一月？
                        ##无法确定 是否 闰月，看来只能跳回前20项，从 1901_01_20__12_01__0 开始
                    print(r)#see below: 所有閏月
    elif case.收集繁体节气名:
        year2may_file_header_data, year2row_data_list = sf.read_all_txt_ifile(idir=idir)
        节气名集合 = set()
            #solar term 节气
        for row_data_list in year2row_data_list.values():
            for _, _, _, 可選節氣 in row_data_list:
                #yield ((公历年份, 公历月份, 公历日份), 農曆日期, 星期, 可選節氣)
                if 可選節氣:
                    節氣 = 可選節氣
                    节气名集合.add(節氣)
        print(节气名集合)
        {'立夏', '小滿', '大雪', '霜降', '立冬', '白露', '立秋', '處暑', '小寒', '小暑', '秋分', '寒露', '驚蟄', '清明', '立春', '夏至', '大暑', '穀雨', '小雪', '春分', '冬至', '芒種', '雨水', '大寒'}
    elif case.基础测试尝试读取所有文件:
        for year in range(1901, 2100+1):
            ipath = idir/f'T{year}c.txt'
            print(f'testing:{year}: read {ipath}')
            it = sf.list_read_single_file__path(ipath)
            for _ in it:
                pass

        sf.read_all_txt_ifile(idir=idir)
    else:
        pass

    r'''see below:所有非法数据行

testing:1941: read /sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T1941c.txt
FormatError: bad format:unknown 数据行:'香港於1941年6月15日至9月30日期間實施了夏令時間 (香港夏令時間 = 香港標準時間 + 1小時)'

testing:1941: read /sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T1942c.txt
FormatError: bad format:unknown 数据行:'香港於1942年1月1日至12月31日期間實施了夏令時間 (香港夏令時間 = 香港標準時間 + 1小時)'

... ...
... ...
... ...


testing:2058: read /sdcard/0my_files/tmp/curl_/香港天文台农历对照表（文字版）/T2058c.txt
FormatError: bad format:unknown 文件头行:'2058 年1月1日          初七        星期二'
#'''



def main():
    pass


if __name__ == '__main__':
    _try_读取香港天文台农历对照表文字版()
    main()

#]]]here_is:end_my_src_code

r'''[
所有閏月:
((1903, 6, 25), (True, 5, 1), 4, None)
((1906, 5, 23), (True, 4, 1), 3, None)
((1909, 3, 22), (True, 2, 1), 1, None)
((1911, 7, 26), (True, 6, 1), 3, None)
((1914, 6, 23), (True, 5, 1), 2, None)
((1917, 3, 23), (True, 2, 1), 5, None)
((1919, 8, 25), (True, 7, 1), 1, None)
((1922, 6, 25), (True, 5, 1), 0, None)
((1925, 5, 22), (True, 4, 1), 5, None)
((1928, 3, 22), (True, 2, 1), 4, None)
((1930, 7, 26), (True, 6, 1), 6, None)
((1933, 6, 23), (True, 5, 1), 5, None)
((1936, 4, 21), (True, 3, 1), 2, None)
((1938, 8, 25), (True, 7, 1), 4, None)
((1941, 7, 24), (True, 6, 1), 4, None)
((1944, 5, 22), (True, 4, 1), 1, None)
((1947, 3, 23), (True, 2, 1), 0, None)
((1949, 8, 24), (True, 7, 1), 3, None)
((1952, 6, 22), (True, 5, 1), 0, None)
((1955, 4, 22), (True, 3, 1), 5, None)
((1957, 9, 24), (True, 8, 1), 2, None)
((1960, 7, 24), (True, 6, 1), 0, None)
((1963, 5, 23), (True, 4, 1), 4, None)
((1966, 4, 21), (True, 3, 1), 4, None)
((1968, 8, 24), (True, 7, 1), 6, None)
((1971, 6, 23), (True, 5, 1), 3, None)
((1974, 5, 22), (True, 4, 1), 3, None)
((1976, 9, 24), (True, 8, 1), 5, None)
((1979, 7, 24), (True, 6, 1), 2, None)
((1982, 5, 23), (True, 4, 1), 0, None)
((1984, 11, 23), (True, 10, 1), 5, None)
((1987, 7, 26), (True, 6, 1), 0, None)
((1990, 6, 23), (True, 5, 1), 6, None)
((1993, 4, 22), (True, 3, 1), 4, None)
((1995, 9, 25), (True, 8, 1), 1, None)
((1998, 6, 24), (True, 5, 1), 3, None)
((2001, 5, 23), (True, 4, 1), 3, None)
((2004, 3, 21), (True, 2, 1), 0, None)
((2006, 8, 24), (True, 7, 1), 4, None)
((2009, 6, 23), (True, 5, 1), 2, None)
((2012, 5, 21), (True, 4, 1), 1, None)
((2014, 10, 24), (True, 9, 1), 5, None)
((2017, 7, 23), (True, 6, 1), 0, None)
((2020, 5, 23), (True, 4, 1), 6, None)
((2023, 3, 22), (True, 2, 1), 3, None)
((2025, 7, 25), (True, 6, 1), 5, None)
((2028, 6, 23), (True, 5, 1), 5, None)
((2031, 4, 22), (True, 3, 1), 2, None)
((2033, 12, 22), (True, 11, 1), 4, None)
((2036, 7, 23), (True, 6, 1), 3, None)
((2039, 6, 22), (True, 5, 1), 3, None)
((2042, 3, 22), (True, 2, 1), 6, None)
((2044, 8, 23), (True, 7, 1), 2, None)
((2047, 6, 23), (True, 5, 1), 0, None)
((2050, 4, 21), (True, 3, 1), 4, None)
((2052, 9, 23), (True, 8, 1), 1, None)
((2055, 7, 24), (True, 6, 1), 6, None)
((2058, 5, 22), (True, 4, 1), 3, None)
((2061, 4, 20), (True, 3, 1), 3, None)
((2063, 8, 24), (True, 7, 1), 5, None)
((2066, 6, 23), (True, 5, 1), 3, None)
((2069, 5, 21), (True, 4, 1), 2, None)
((2071, 9, 24), (True, 8, 1), 4, None)
((2074, 7, 24), (True, 6, 1), 2, None)
((2077, 5, 22), (True, 4, 1), 6, None)
((2080, 4, 20), (True, 3, 1), 6, None)
((2082, 8, 24), (True, 7, 1), 1, None)
((2085, 6, 22), (True, 5, 1), 5, None)
((2088, 5, 21), (True, 4, 1), 5, None)
((2090, 9, 24), (True, 8, 1), 0, None)
((2093, 7, 23), (True, 6, 1), 4, None)
((2096, 5, 22), (True, 4, 1), 2, None)
((2099, 3, 22), (True, 2, 1), 0, None)

所有閏月
#]'''


r'''[
所有非法数据行:
香港於1941年6月15日至9月30日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1942年1月1日至12月31日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1943年1月1日至12月31日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1944年1月1日至12月31日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1945年1月1日至12月31日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1946年4月20日至12月1日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1947年4月13日至11月30日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1948年5月2日至10月31日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1949年4月3日至10月30日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1950年4月2日至10月29日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1951年4月1日至10月28日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1952年4月6日至11月2日期間實施了夏令時間 ( 香港夏 令時 間 = 香港標 準時間 + 1小時)
香港於1953年4月5日至11月1日期間實施了夏令時間 ( 香港夏 令時 間 = 香港標 準時間 + 1小時)
香港於1954年3月21日至10月31日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1955年3月20日至11月6日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1956年3月18日至11月4日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1957年3月24日至11月3日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1958年3月23日至11月2日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1959年3月22日至11月1日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1960年3月20日至11月6日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1961年3月19日至11月5日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1962年3月18日至11月4日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1963年3月24日至11月3日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1964年3月22日至11月1日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1965年4月18日至10月17日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1966年4月17日至10月16日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1967年4月16日至10月22日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1968年4月21日至10月20日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1969年4月20日至10月19日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1970年4月19日至10月18日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1971年4月18日至10月17日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1972年4月16日至10月22日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1973年4月22日至10月21日及12月30日至12月31 日期間 實施 了夏 令時間 (香港夏 令時間 = 香港標準時 間 + 1小時)
香港於1974年1月1日至10月20日期間實施了夏令時 間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1975年4月20日至10月19日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1976年4月18日至10月17日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)
香港於1979年5月13日至10月21日期間實施了夏令時間 (香港夏令時 間 = 香港標 準時間 + 1小時)

所有非法数据行
#]'''

#]]]here_is:end_my_all__src_code__output

if 0:
    #view others/数学/编程/农历/py农历.txt
    #   https://blog.csdn.net/wqlineky1/article/details/80945299
    # e script/农历/external农历-1.py
    pass


