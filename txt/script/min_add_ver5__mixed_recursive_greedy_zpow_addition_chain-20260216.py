#__all__:goto
# [:曾经主要作业命令行]:goto
# [:主要简并记录输出文件]:goto
# [:主要尾六表另档文件]:goto
# [:当前主要作业命令行]:goto
r'''[[[
e script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py
    简并态{递归婪溟链}
    # [:约束牜定义冫递归婪溟链]:goto
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py

script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain
py -m nn_ns.app.debug_cmd   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain:__doc__ -ht # -ff -df
#######

[[
溟隘链-->简并态算法牜加溟链
猜想出处:view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
  view ../../python3_src/bash_script/app/szmm4shortest_addition_chain
view script/min_add_ver4__pseudo_addition_chain.py
  view script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺精深.out.txt
  枚举冫相关信息纟最短短程加链牜简并态算法扌
      [相关信息 :: (自然数, 长度纟最短短程加链, 规模纟次大点集纟所有最短短程加链, 规模纟点集纟所有最短短程加链, 次大点集纟所有最短短程加链, 简并态/点集纟所有最短短程加链, 最短短程加链牜水平反转后词典序最小,最短短程加链牜水平反转后词典序最大)]
        (6, 4, 2, 5, [3, 4], RT({1: 4, 6: 1}), [1, 2, 3, 6], [1, 2, 4, 6])
        (n, sz4chain, num_submaxs, num_nodes, submaxs4n, nodes4n, ls0, ls1) = n2info[n]
        (靶值, 最小显链长, 数目{次大数}, 数目{简并态点集}, 次大数点集, RT(简并态点集), 最短加链牜右侧最小, 最短加链牜右侧最大)
          RT:"NonTouchRanges"
          [RT({1: 4, 6: 1}) == [1..<1+4]++[6..<6+1]]


view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite2.py
    溟隘链、溟母链
        未必:递归最短
        糅合:介点/出度为一
]]
[[
递归婪溟链
    强调:递归最短{在不考虑 溟化值 的前提下 递归最短}{溟化值集 构成 跳线，不是 主线}
    『婪』-贪婪型:类比于:加星链
    『溟』-二幂环

# [:约束牜定义冫递归婪溟链]:here
[靶值 == 次大数 + (内点<<溟次)]
[内点 in 简并集纟次大数]
[最小显链长纟靶值 == 最小显链长纟次大数 +1 +溟次]
[溟化值集 := {内点<<ez | [n:<-[1..=溟次]]}]
]]



'#'; __doc__ = r'#'
>>>



[[
xxx:py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=1  --休眠期:auto   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.out.txt
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.out.txt
[靶值==1270] =>: resting...: 14.999647877999998 seconds
... ....
1270:resting...: 14.999647877999998 seconds
8406: resting...: 108.16011947200002 seconds
12999:resting...: 135.65701834099855 seconds
14836:resting...: 130.62248388499995 seconds
15148:resting...: 158.15175883699976 seconds
15270:resting...: 138.40876877500068
17010:resting...: 309.90105902899995 seconds
18030:resting...: 101.91477030200258 seconds
18146:resting...: 199.71460082900012 seconds
18180:resting...: 357.4434666979978 seconds
18252:resting...: 249.11337842399735 seconds
24042:consumed: 455.2927567769998 seconds
24241:consumed: 331.8897022779993 seconds
24254:consumed: 254.6687823809998 seconds
25270:consumed: 488.849069959997 seconds
25934:consumed: 520.0703521059986 seconds
25942:consumed: 453.9847385569992 seconds
25946:consumed: 501.7201072550015 seconds
27002:consumed: 414.01798976400096 seconds
27306:consumed: 252.93409234700084 seconds
27378:consumed: 522.2650140949991 seconds
]]
[[
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫文件格式纟简并记录纟递归婪溟链扌  --verI=1  --verO=2    :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.out.txt   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.out.txt
    4.0M @[靶值<=2858]
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
    2.1M @[靶值<=2858]
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt

]]
[[
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
    #见下面:分裂文件
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
]]
[[
测试:分裂文件:
    文件路径冃靶值讠简并记录-->列表纟文件路径冃靶值讠简并记录
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt
file_startswith_    /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt    script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt
    =>same
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto  :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto  :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto  :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt    :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part4.test-out.txt

view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.test-out.txt
    [1..=86]
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt
    [87..=126]
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt
    [127..=158]
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt
    [159..=190]

cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt  | head -n 126  | tail -n +87  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.test-out.txt
    => ... are identical
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt  | head -n 158  | tail -n +127  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.test-out.txt
    => ... are identical
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt  | head -n 190  | tail -n +159  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part4.test-out.txt
    => ... are identical

]]
[[
分裂文件:
mv -iv   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.out.txt   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --ver=2  --休眠期:auto   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt    :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-_.out.txt
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-_.out.txt

]]
[[
DONE:由 自顶向下搜索 改为 自底向上注册
===
自顶向下搜索:
def _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自顶向下搜索扌(靶值讠简并记录, 靶值, /):
    for 次大数 in reversed(range(1, 靶值)):
        溟化值 = 靶值 -次大数
        ... ...
        assert 靶值 == 次大数 + (内点<<溟次)
        assert 内点 in 简并集纟次大数
        ... ...
        显链长纟靶值 = 最小显链长纟次大数 +1 +溟次
    ... ...
    return (最小显链长纟靶值, 次大数讠溟次)
===
自底向上注册:
[靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈 :: {靶值:{显链长纟靶值:[(次大数,内点,溟次)]}}{靶值>=当前靶值}]
def _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, /):
    靶值 = len(靶值讠简并记录)
    assert 靶值 >= 2
    最小显链长纟靶值 = min(d:=靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈[靶值])
    ls = d[最小显链长纟靶值]
    次大数讠溟次 = {次大数:溟次 for (次大数,内点,溟次) in ls}
    return (最小显链长纟靶值, 次大数讠溟次)
def 后续更新冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊已有后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 简并记录纟当前靶值, /):
    当前靶值 = len(靶值讠简并记录)
    assert 当前靶值 >= 2
    assert 当前靶值 == 简并记录纟当前靶值.靶值
    ... ...
def 初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, /):
    当前靶值 = len(靶值讠简并记录)
    assert 当前靶值 >= 2
    ... ...
    assert min(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈) == 当前靶值
    return 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈

===
]]
[[
++kw:自顶向下搜索丷自底向上注册
测试:自底向上注册
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt

暂停使用冫自顶向下搜索
file_startswith_    /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt    script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
    =>same
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt
    [1..=445]
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt  | head -n 445  | tail -n +1  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt
    => ... are identical

]]
[[
自底向上注册:
mv -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-_.out.txt    script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-9192.out.txt
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto   :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt    :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-9192.out.txt  :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-_.bottomup.out.txt

@20260208
mv -iv   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-_.bottomup.out.txt   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-13013.bottomup.out.txt
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-13013.bottomup.out.txt
(12509, 17, 6, 41, FD('{:[#Bh1+B-B-gh-BAy-D];B:[#BBV+B];}'), RT('[#B+E-B-B-D+C-C+C-G-H-P-P-f-f-.-.-B.-M-By-Q-Du-M-Dy-Q-II-IH-QQ+C-QP-Q-gQ-B-M-B-gQ-Q-BAy-D-M]'), [1, 2, 3, 6, 12, 13, 24, 48, 96, 192, 384, 397, 781, 1562, 3123, 4181, 6261, 12509], [1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 8328, 12496, 12509], [1, 2, 3, 6, 12, 13, 24, 48, 96, 192, 384, 397, 781, 1562, 3124, 6248, 6261, 12509], [1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 8328, 12492, 12509], [1, 2, 3, 6, 12, 13, 24, 48, 96, 192, 384, 397, 781, 1562, 3124, 6248, 6261, 12509], [1, 2, 4, 8, 12, 13, 24, 48, 96, 192, 384, 768, 781, 1562, 3124, 6248, 12496, 12509])

du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
    5.5M
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0002.6018-9192.out.txt
    4.1M
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0003.9193-13013.bottomup.out.txt
    5.1M

]]
[[
@20260208
++kw:鬽最大靶值
++乸异常牜最大靶值
测试:kw:鬽最大靶值
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=500 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1.bottomup.test-out.txt   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
    再次执行:^script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.乸异常牜最大靶值: 500
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt  | head -n 500  | tail -n +446  |  diff  -s  -   /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
    => ... are identical

]]
[[
@20260208
++kw:彣匹配模板纟前置文件路径冃靶值讠简并记录#smay_shell_pattern4pre_ipaths
测试:kw:彣匹配模板纟前置文件路径冃靶值讠简并记录
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=500 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto   --彣匹配模板纟前置文件路径冃靶值讠简并记录:'/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
]]
[[
分离出来:规范冫列表纟文件路径冃靶值讠简并记录扌
分离出来:mk_rest_func_
测试:规范冫列表纟文件路径冃靶值讠简并记录扌
测试:mk_rest_func_
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=530  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part*.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.501-530.bottomup.test-out.txt
cat script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt  | head -n 530  | tail -n +501  |  diff  -s  -   ${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.501-530.bottomup.test-out.txt
    => ... are identical
rm -iv ${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part3.501-530.bottomup.test-out.txt
]]
[[
@20260208
自底向上注册x鬽最大靶值x彣匹配模板纟前置文件路径冃靶值讠简并记录:
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=16016  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt
    完成@20260209晚八点
    # [:曾经主要作业命令行]:goto

du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
    5.5M #1-6017.out.txt
    4.1M #6018-9192.out.txt
    5.1M #9193-13013.bottomup.out.txt
    4.6M #13014-16016.bottomup.out.txt
    ~=20M
]]
[[
@20260208
失败:加强猜测约束牜极简次大数集:
  [靶值 == 次大数 + (内点<<溟次)]
  [内点 in {次大数, *靶值讠简并记录[次大数].次大数讠溟次, 2, 1}]
极简次大数集-->极简次大数讠溟次
另档冫极简次大数集纟简并记录纟递归婪溟链扌
def 另档冫极简次大数集纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠极简次大数集, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
测试:另档冫极简次大数集纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫极简次大数集纟简并记录纟递归婪溟链扌  --ver=2   :${prefix}另档冫极简次大数集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
    ^Exception: 59
    失败！
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫极简次大数集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt

rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫极简次大数集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
]]
[[
@20260208
失败:加强猜测约束牜幸存次大数必由集:
  [靶值 == 次大数 + (内点<<溟次)]
  [内点 in {次大数, 2, 1, *靶值讠幸存次大数必由集[次大数].幸存次大数讠溟次.keys(), *chains(靶值讠幸存次大数必由集[次大数].幸存次大数讠必由集.values())}]
幸存次大数必由集-->(幸存次大数讠溟次, 幸存次大数讠必由集)
另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌
def 另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠幸存次大数必由集, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
测试:另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌  --ver=2   :${prefix}另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
    ^Exception: 77
    失败！
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt



]]
[[
@20260208
失败:双定点最短加靶链简并态
(靶值讠定点讠简并态, 靶值讠次大数讠溟次)
    [1<=定点<=靶值]
* [1 <= 定点 < 靶值]:
    #########
    #xxx:[靶值讠定点讠简并态[靶值][定点] := {u | [[(次大数,溟次):<-靶值讠次大数讠溟次[靶值].items()][内点 := (靶值-次大数)>>溟次][次偏简并态:=靶值讠定点讠简并态[次大数][内点]][定点 <- 次偏简并态][u:<-???如何筛选:次偏简并态]]}]
        不行！除非:[定点<-{次大数,内点}]，否则:需要:仨定点简并态！
    #########
* [定点 == 靶值]:
    #########
    ... ...
    #########

]]
[[
@20260208
失败{@靶值=2077}:易来简并态
    易来:容易得到的，计算量小的
双定点最短加靶链易来简并态
双点易来简并态
(靶值讠定点讠易来简并态, 靶值讠易来次大数讠溟次)
    [1<=定点<=靶值]
* [3 <= 定点 < 靶值]:
    #########
    [靶值讠定点讠易来简并态[靶值][定点] := {u | [[(次大数,溟次):<-靶值讠易来次大数讠溟次[靶值].items()][内点 := (靶值-次大数)>>溟次][内点溟化值集 := {内点<<ez | [ez:<-[0..=溟次]]}][内有效集 := if [定点 <- {次大数,min(次大数,2),1}\-/内点溟化值集] then 靶值讠定点讠易来简并态[次大数][内点] elif [定点>次大数] then {} elif [内点 <- {次大数,min(次大数,2),1}] then 靶值讠定点讠易来简并态[次大数][定点] elif [定点<-靶值讠定点讠易来简并态[次大数][内点]] then {定点} else {}][有效集 := if 内有效集 then {靶值,次大数,2,1}\-/内点溟化值集\-/内有效集 else {}][u:<-有效集]]}]
    #########
* [定点 == 靶值]or[定点<=min(靶值,2)]:
    #########
    [靶值讠定点讠易来简并态[靶值][定点] := {靶值,定点}\-/{u | [[(次大数,溟次):<-靶值讠易来次大数讠溟次[靶值].items()][内点 := (靶值-次大数)>>溟次][内点溟化值集 := {内点<<ez | [ez:<-[0..=溟次]]}][内有效集 := 靶值讠定点讠易来简并态[次大数][内点]][有效集 := 内点溟化值集\-/内有效集][u:<-有效集]]}]
    #########

另档冫双点易来简并态纟简并记录纟递归婪溟链扌
def 另档冫双点易来简并态纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠双点易来简并态, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
测试:另档冫双点易来简并态纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫双点易来简并态纟简并记录纟递归婪溟链扌  --ver=2   :${prefix}另档冫双点易来简并态纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
    3.4M

小数据成功，但是 存储空间开销大
    =>考虑使用:NonTouchRanges+intern()
    但 更重要更难避免的毛病 是 计算时间开销大


===
欤按需计算:=True
    有用性？
    只保留:靶值讠易来简并态
        因为 后面 此靶值 将作为 更大靶值 的 潜在次大数 出现，需要 查询 内点 是否 在内
    靶值讠定点讠易来简并态-->靶值讠定点讠易来简并态扌

    靶值讠定点讠易来简并态扌(靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 靶值, 定点) -> 易来简并态

按需计算
另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌
def 另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌(输出文件路径冃靶值讠双点易来简并态, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
测试:另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌  --ver=2   :${prefix}另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2.1-500.bottomup.test-out.txt
小数据成功
    但见下面:^Exception: 2077
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2.1-500.bottomup.test-out.txt
    216K#py.dict+py.set
    120K#py.dict+ranges2delta_txt_
    84K#_表述冫次大数讠溟次讠文本表达扌+ranges2delta_txt_


]]
[[
回到上面:见上面:按需计算
#.@20260208
#.易来偏次简并态
#.    易来简并态:容易得到的，计算量小的
#.    偏次简并态:[双定点==(靶值,靶值or次大数)]
#.(靶值讠定点讠易来偏次简并态, 靶值讠易来偏次次大数讠溟次)
#.    [定点 <- {靶值}\-/易来偏次次大数讠溟次.keys()]
#.        #[1<=定点<=靶值]
#.
#.
#.[靶值讠定点讠易来偏次简并态[靶值][靶值] := 缓存...]
#.    因为 后面 此靶值 将作为 更大靶值 的 潜在次大数 出现，需要 查询 内点 是否 在内
#.
#.按需计算:[靶值讠定点讠易来偏次简并态[靶值][次大数] := ...]
#.
#.[按需计算:靶值讠定点讠易来偏次简并态[靶值][1] := 靶值讠定点讠易来偏次简并态[靶值][靶值]]
#.[按需计算:靶值讠定点讠易来偏次简并态[靶值][2] := 靶值讠定点讠易来偏次简并态[靶值][靶值]]
#.
#.[按需计算:靶值讠定点讠易来偏次简并态[靶值][定点] := {u | [[(次大数,溟次):<-靶值讠易来次大数讠溟次[靶值].items()][内点 := (靶值-次大数)>>溟次][内点溟化值集 := {内点<<ez | [ez:<-[0..=溟次]]}][内有效集 := if [定点 <- {次大数,min(次大数,2),1}\-/内点溟化值集] then 靶值讠定点讠易来偏次简并态[次大数][内点] elif [定点>次大数] then {} elif [内点 <- {次大数,min(次大数,2),1}] then 靶值讠定点讠易来偏次简并态[次大数][定点] elif [定点<-靶值讠定点讠易来偏次简并态[次大数][内点]] then {定点} else {}][有效集 := if 内有效集 then {靶值,次大数,2,1}\-/内点溟化值集\-/内有效集 else {}][u:<-有效集]]}]
#.

]]
[[
按需计算
另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌
prefix0=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
###py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌  --ver=2  +verbose  :${prefix0}另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2-3-4.1-14781.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt
    ^Exception: 2077
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2-3-4.1-14781.bottomup.test-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2-3-4.1-14781.bottomup.test-out.txt
    636K
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part-1-2-3-4.1-14781.bottomup.test-out.txt


py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌  --ver=2  +verbose  :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part1.1-2076.test-out.txt    :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
    ^Exception: 2077
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part1.1-2076.test-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part1.1-2076.test-out.txt
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌.ver2.part1.1-2076.test-out.txt

]]
[[
测试:另档冫尾六表纟简并记录纟递归婪溟链扌
def 另档冫尾六表纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠尾六表, /, *列表纟输入文件路径冃靶值讠尾六表, ver, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False):
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  +verbose  --ver=2   :${prefix}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt




提取数据:提取冫尾六表:
prefix0=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=2  +verbose  :${prefix0}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-15062.extract-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt

15062
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-15062.extract-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-15062.extract-out.txt
    6.8M
    =>ver3
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-15062.extract-out.txt


]]
[[
++ver3
++MAX_VERSION
下上界辻左右大小四色最短加链-->(自然数集,6址引列表)$ranges2delta_txt_

测试:转换冫文件格式纟简并记录纟递归婪溟链灬扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫文件格式纟简并记录纟递归婪溟链灬扌  +verbose  --verI=2 --verO=3   :${prefix}转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫文件格式纟简并记录纟递归婪溟链灬扌  +verbose  --verI=3 --verO=1   :${prefix}转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2.1-500.bottomup.test-out.txt   :${prefix}转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2.1-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt

du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2.1-500.bottomup.test-out.txt
    324K
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt
    176K

rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2.1-500.bottomup.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver3.part-1-2.1-500.bottomup.test-out.txt


]]
[[
测试:转换冫尾六表纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫尾六表纟简并记录纟递归婪溟链扌  +verbose  --verI=2 --verO=3   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫尾六表纟简并记录纟递归婪溟链扌  +verbose  --verI=3 --verO=2   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt

du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
    212K
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt
    176K

rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.test-out.txt


]]
[[
++kw:欤删除中段数据
++kw:欤允许输入输出是同版本
测试:转换冫尾六表纟简并记录纟递归婪溟链扌
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫尾六表纟简并记录纟递归婪溟链扌  +欤删除中段数据  +verbose  --verI=2 --verO=3   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫尾六表纟简并记录纟递归婪溟链扌  +欤允许输入输出是同版本   +欤删除中段数据  +verbose  --verI=2 --verO=2   :${prefix}转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt

view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt
view /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt

du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt
    128K
du -h /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt
    92K

rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt
rm -iv /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2.1-500.bottomup.欤删除中段数据.test-out.txt



提取数据:提取冫尾六表:
prefix0=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=2  +verbose  :${prefix0}另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt

16016-ver2
head script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt
    ver2:       7.3M
    vs:ver3:    4.9M
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt

===
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @另档冫尾六表纟简并记录纟递归婪溟链扌  --ver=-1 --verI=2  --verO=3  +verbose  :${prefix0}另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt    --彣匹配模板纟前置文件路径冃靶值讠尾六表:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt

16016-ver3
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt
    ver3:       4.9M
    vs:ver2:    7.3M
    但是，转换格式费时显著！
rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt


===
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma --lzma -C script/  min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma --lzma -C script/  min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt

du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver?.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma
    600K#ver2#看来还是原版更好压缩
    1.1M#ver3

rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver3.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma


tar -xvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt.tar.lzma -O | more
    # [:主要尾六表另档文件]:here
===
]]
[[
1-16016完成@20260209晚八点
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.out.txt.tar.lzma --lzma   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.out.txt.tar.lzma
    4.3M # vs ~20M
tar -xf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.out.txt.tar.lzma -O | head -n 6019 | tail -n +6016 | more
    # [:主要简并记录输出文件]:here
from seed.for_libs.for_tarfile import iter_chain_read_multi_tarfile_

===
尝试:压缩ver1:结果不如ver2
prefix0=script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @转换冫文件格式纟简并记录纟递归婪溟链灬扌  +verbose  --verI=2 --verO=1   :${prefix0}转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt    --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix0}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :${prefix0}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt
head script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt
    46M
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.part-1-2-3-4.1-16016.out.txt.tar.lzma --lzma   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver1.part-1-2-3-4.1-16016.out.txt.tar.lzma
    ver1:       6.1M # vs 46M
    vs:ver2:    4.3M # vs ~20M

rm -iv script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..转换冫文件格式纟简并记录纟递归婪溟链灬扌.ver1.part-1-2-3-4.1-16016.out.txt
]]
[[
DONE:最短加链牜左侧最大:头部二幂多长？
    看来，总有 最短加链牜左侧最大:[1,2,3,...]
head script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..另档冫尾六表纟简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.extract-out.txt
求最小比率: 长度纟头部二幂/最小显链长
def 求冫丮最小比率辻靶值列表厈牜长度纟头部二幂纟左侧最大最短加链之于最小显链长纟靶值扌(*列表纟输入文件路径冃靶值讠尾六表, ver, verbose=False):

echo script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt  |  sed 's/script/:\0/g'
printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   @求冫丮最小比率辻靶值列表厈牜长度纟头部二幂纟左侧最大最短加链之于最小显链长纟靶值扌  +verbose  --ver=2      $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt)
    =>: (Fraction(1, 17), [14759, 15449])
        # 注意:局限于[靶值<-[1..=16016]]
===
tail -n 1258 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt | head -n 1
(14759, 17, 4, 32, FD('{:[#CKa+B-B9-oF-D7];}'), RT('[#B+D-B-E-C-G-C-Q-F-h-L-BD-X-CH-v-EP-C-Bc-Ii-C8-RF-F5-M-D7-oF-B9-uM-B9-oF-D7-uM]'), [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 368, 643, 1283, 2566, 2957, 5775, 8858, 14759], [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 736, 1472, 2944, 3209, 5901, 11802, 14759], [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 368, 736, 1472, 2944, 2957, 5901, 8858, 14759], [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 643, 1283, 2566, 3209, 5775, 11550, 14759], [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 368, 736, 1472, 2944, 2957, 5901, 8858, 14759], [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 368, 736, 1472, 2944, 2957, 5901, 11802, 14759])
===
tail -n 568 script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0004.13014-16016.bottomup.out.txt | head -n 1
(15449, 17, 6, 41, FD('{:[#CQ2+B-P3-n-fv-vC];B:[#BRT+B];}'), RT('[#B+D-B+C-D-B-H-D-P-H-f-P+C-_-f+D-B9-.-B-D9-CD-H7-EH-P3-C-IM-C-fs-C-n-n-PP-wS-PP-n-n-fv-vC-BP]'), [1, 2, 3, 5, 10, 20, 40, 80, 97, 193, 386, 772, 1544, 2563, 3091, 5163, 9270, 15449], [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 640, 1280, 2560, 5120, 5123, 10246, 15369, 15449], [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 2563, 5123, 5163, 10286, 15449], [1, 2, 3, 6, 12, 24, 48, 96, 192, 384, 386, 772, 1544, 3088, 3091, 6179, 12358, 15449], [1, 2, 3, 6, 12, 24, 48, 96, 97, 193, 386, 772, 1544, 3088, 3091, 6179, 9270, 15449], [1, 2, 3, 5, 10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 5123, 10246, 15369, 15449])
===


]]
[[
@20260210
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=20020  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0005.16017-20020.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260210清晨:启动:16017..
    @20260211清晨:..=17500
    @20260212清晨:完成

du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0005.16017-20020.bottomup.out.txt
    6.7M

]]
[[
@20260212
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=23023  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0006.20021-23023.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260212傍晚:启动:20021..
    @20260213深夜:完成
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0006.20021-23023.bottomup.out.txt
    4.6M

]]
[[
@20260213
DONE:丢弃越界:鬽最大靶值x自底向上
测试:丢弃越界:
prefix=/sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=500 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto   --彣匹配模板纟前置文件路径冃靶值讠简并记录:${prefix}'枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt'   :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part2.446-500.bottomup.test-out.txt


py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=253 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto    :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1-2.1-500.bottomup.test-out2.txt
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=323 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto    :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1-2.1-500.bottomup.test-out2.txt
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌 --鬽最大靶值=500 +自顶向下搜索丷自底向上注册  --ver=2  --休眠期:auto    :${prefix}枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1-2.1-500.bottomup.test-out2.txt
file_startswith_    /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part1-2.1-500.bottomup.test-out2.txt   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0001.1-6017.out.txt
    =>same
]]
[[
DONE{内点址距 不可控}:递归婪溟链:最大纟最小主线距离纟次大数辻内点乊靶值==max{min{址引纟次大数-址引纟内点 | [us:<-最短加链/-\递归婪溟链][主线:=递归婪溟链主线纟(us)][次大数:=主线[-2]][内点:=max{n | [ez:<-[0..]][n:=(靶值-次大数)/2**ez][n<-us]}][址引纟次大数:=主线.index(次大数)][址引纟内点:=主线.index(内点)]} | [靶值:<-[2..]]}
from seed.math.power.addition_chain.shortest.rewrite3 import 枚举冫递归婪溟链巛严序加链扌
  .次大数址引讠内点址距
最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌  +欤趃输出 +欤记录首峰值位 +verbose  --ver=2      $(printf ' :%s' /sdcard/0my_files/tmp/out4py/script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part?.bottomup.test-out.txt)
    # 注意:局限于[靶值<-[1..=455]]
... ...
靶值: 445
8
(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369)
(1, 2, 4, 8, 16, 80, 144, 288, 368, 369)
(1, 3, 5, 10, 13, 26, 52, 104, 208, 209, 417)
(1, 3, 6, 7, 13, 26, 52, 104, 208, 209, 417)
(1, [(1, 3, 7), (1, 3, 4, 7)])
(2, [(1, 3, 5, 10, 13), (1, 3, 6, 7, 13)])
(3, [(1, 3, 9, 18, 19, 37), (1, 5, 9, 18, 19, 37), (1, 2, 4, 36, 37)])
(4, [(1, 3, 5, 10, 20, 21, 41), (1, 2, 4, 8, 40, 41)])(5, [(1, 3, 5, 10, 20, 40, 41, 81), (1, 2, 4, 8, 16, 80, 81)])
(6, [(1, 3, 5, 7, 14, 19, 38, 76, 152, 157), (1, 3, 9, 18, 21, 39, 78, 79, 157)])
(7, [(1, 3, 5, 10, 13, 23, 46, 92, 93, 185), (1, 2, 4, 8, 40, 72, 144, 184, 185)])
(8, [(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369), (1, 2, 4, 8, 16, 80, 144, 288, 368, 369)])


(369, 11, 20, 94, ..., [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369], [1, 2, 4, 8, 16, 32, 64, 80, 144, 288, 368, 369], [1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369], [1, 2, 4, 8, 16, 32, 48, 80, 160, 320, 368, 369])
    尾四链 只要 3条
(417, 11, 16, 77, ..., [1, 2, 3, 5, 10, 13, 26, 52, 104, 208, 209, 417], [1, 2, 4, 8, 16, 32, 64, 128, 256, 384, 416, 417], [1, 2, 3, 6, 7, 13, 26, 52, 104, 208, 209, 417], [1, 2, 4, 8, 16, 32, 64, 128, 256, 384, 416, 417])
    尾四链 只要 3条

>>> uss = ([1, 2, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369], [1, 2, 4, 8, 16, 32, 64, 80, 144, 288, 368, 369], [1, 2, 4, 8, 16, 32, 48, 80, 160, 320, 368, 369])
>>> [[(str(递归婪溟链), max(递归婪溟链.次大数址引讠内点址距)) for 递归婪溟链 in 枚举冫递归婪溟链巛严序加链扌(us)] for us in uss]
[[('[1~3~5~10~13~23~46~92~184~185~369]', 8)], [('[1~2~4~8~16~80~144~288~368~369]', 8)], [('[1~2~4~8~16~48~80~160~320~368~369]', 9)]]





py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌  +欤趃输出 +欤记录首峰值位 +verbose  --ver=2      $(printf ' :%s' script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt)
    # 注意:局限于[靶值<-[1..=22463]]
... ...
靶值: 22463
14
(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369, 738, 1476, 2952, 5904, 5905, 11809)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 4608, 9216, 11776, 11808, 11809)
(1, 3, 5, 10, 13, 23, 46, 92, 184, 368, 371, 739, 1478, 2956, 5912, 5913, 11825)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 2576, 4624, 9248, 11824, 11825)
(1, 3, 5, 10, 13, 23, 46, 92, 93, 185, 370, 740, 1480, 2960, 5920, 5921, 11841)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 4608, 9216, 11776, 11840, 11841)
(1, 3, 5, 10, 13, 23, 46, 92, 184, 187, 371, 742, 1484, 2968, 5936, 5937, 11873)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 2592, 4640, 9280, 11872, 11873)
(1, 3, 5, 10, 13, 26, 52, 104, 105, 209, 418, 836, 1672, 3344, 6688, 6689, 13377)
(1, 3, 6, 7, 13, 26, 52, 104, 105, 209, 418, 836, 1672, 3344, 6688, 6689, 13377)
(1, 3, 7, 14, 28, 31, 59, 118, 236, 267, 503, 1006, 2012, 4024, 8048, 8049, 16097)
(1, 3, 6, 12, 13, 25, 75, 125, 250, 253, 503, 1006, 2012, 4024, 8048, 8049, 16097)
(1, 3, 5, 10, 13, 23, 46, 59, 151, 302, 604, 1208, 2416, 4832, 9664, 9665, 19329)
(1, 3, 9, 18, 36, 72, 73, 79, 151, 302, 604, 1208, 2416, 4832, 9664, 9665, 19329)
(1, 5, 9, 18, 36, 41, 77, 154, 155, 309, 618, 1236, 2472, 4944, 9888, 9889, 19777)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 2304, 4352, 8704, 17408, 19712, 19776, 19777)
(1, 3, 5, 10, 13, 39, 78, 156, 312, 624, 627, 1251, 2502, 5004, 10008, 10009, 20017)
(1, 3, 9, 18, 21, 39, 78, 156, 312, 624, 627, 1251, 2502, 5004, 10008, 10009, 20017)
(1, 3, 5, 10, 13, 39, 78, 156, 312, 624, 637, 1261, 2522, 5044, 10088, 10089, 20177)
(1, 3, 6, 7, 13, 39, 78, 156, 312, 624, 637, 1261, 2522, 5044, 10088, 10089, 20177)
(1, 3, 5, 10, 20, 40, 80, 160, 320, 640, 641, 1281, 2562, 5124, 10248, 10249, 20497)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20496, 20497)
(1, 3, 5, 10, 20, 40, 80, 160, 320, 321, 641, 1282, 2564, 5128, 10256, 10257, 20513)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20512, 20513)
(1, 3, 5, 10, 20, 40, 80, 160, 161, 321, 642, 1284, 2568, 5136, 10272, 10273, 20545)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20544, 20545)
(1, 3, 5, 10, 20, 40, 80, 81, 161, 322, 644, 1288, 2576, 5152, 10304, 10305, 20609)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20608, 20609)
(1, 3, 5, 10, 20, 40, 41, 81, 162, 324, 648, 1296, 2592, 5184, 10368, 10369, 20737)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20736, 20737)
(1, 3, 5, 10, 20, 21, 41, 82, 164, 328, 656, 1312, 2624, 5248, 10496, 10497, 20993)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 20480, 20992, 20993)
(1, 2, 6, 10, 20, 40, 46, 86, 172, 344, 688, 1376, 2752, 5504, 11008, 11009, 11015, 22023)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4610, 8706, 17412, 22022, 22023)
(1, 3, 5, 10, 20, 23, 43, 86, 172, 344, 688, 1376, 1377, 2753, 5506, 11012, 22024, 22029)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4612, 8708, 17416, 22028, 22029)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4616, 8712, 17424, 22040, 22041)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4624, 8720, 17440, 22064, 22065)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 4608, 4640, 8736, 17472, 22112, 22113)
(1, [(1, 3, 7), (1, 3, 4, 7)])
(2, [(1, 3, 5, 10, 13), (1, 3, 6, 7, 13)])
(3, [(1, 3, 9, 18, 19, 37), (1, 5, 9, 18, 19, 37), (1, 2, 4, 36, 37)])
(4, [(1, 3, 5, 10, 20, 21, 41), (1, 2, 4, 8, 40, 41)])(5, [(1, 3, 5, 10, 20, 40, 41, 81), (1, 2, 4, 8, 16, 80, 81)])
(6, [(1, 3, 5, 7, 14, 19, 38, 76, 152, 157), (1, 3, 9, 18, 21, 39, 78, 79, 157)])
(7, [(1, 3, 5, 10, 13, 23, 46, 92, 93, 185), (1, 2, 4, 8, 40, 72, 144, 184, 185)])
(8, [(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369), (1, 2, 4, 8, 16, 80, 144, 288, 368, 369)])
(9, [(1, 3, 5, 10, 20, 21, 41, 82, 164, 328, 329, 657), (1, 2, 4, 8, 16, 32, 64, 128, 640, 656, 657)])
(10, [(1, 3, 5, 10, 20, 40, 41, 81, 162, 324, 648, 649, 1297), (1, 2, 4, 8, 16, 32, 64, 128, 256, 1280, 1296, 1297)])
(11, [(1, 3, 5, 10, 20, 40, 80, 81, 161, 322, 644, 1288, 1289, 2577), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 2576, 2577)])
(12, [(1, 3, 5, 10, 20, 40, 80, 160, 161, 321, 642, 1284, 2568, 2569, 5137), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 5120, 5136, 5137)])
(13, [(1, 3, 5, 10, 13, 23, 46, 92, 93, 185, 370, 740, 1480, 2960, 2961, 5921), (1, 2, 4, 8, 16, 32, 64, 128, 256, 1280, 2304, 4608, 5888, 5920, 5921)])
(14, [(1, 3, 5, 10, 13, 23, 46, 92, 184, 185, 369, 738, 1476, 2952, 5904, 5905, 11809), (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2560, 4608, 9216, 11776, 11808, 11809)])

]]
[[
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=26026  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0007.23024-26026.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260213深夜:启动
    @20260215下午:完成
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0007.23024-26026.bottomup.out.txt
    5.0M
]]
[[
py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=29029  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0008.26027-29029.bottomup.out.txt
    # [:曾经主要作业命令行]:goto
    @20260215下午:启动
    @20260216傍晚:完成
du -h script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0008.26027-29029.bottomup.out.txt
    5.4M
]]
[[
文件改名中...:py_adhoc_call   script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain   ,str.枚举生成冫文件后续简并记录纟递归婪溟链扌  --鬽最大靶值=32032  +自顶向下搜索丷自底向上注册   --ver=2  --休眠期:auto      --彣匹配模板纟前置文件路径冃靶值讠简并记录:'script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt'     :script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part0009.29030-32032.bottomup.out.txt
    @20260216傍晚:启动
    # [:当前主要作业命令行]:here
e ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain.py

]]

















from script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain import *
]]]'''#'''
__all__ = r'''
枚举生成冫文件后续简并记录纟递归婪溟链扌
    加载冫数据扌
        构造冫局部变量环境纟解读简并记录扌

    枚举冫后续简并记录纟递归婪溟链牜自顶向下搜索扌
        求冫后续简并记录纟递归婪溟链牜自顶向下搜索扌
            构造冫简并记录纟靶值一扌
        枚举冫最短加链乊内点集扌

    枚举冫后续简并记录纟递归婪溟链牜自底向上注册扌
        求冫后续简并记录纟递归婪溟链牜自底向上注册扌
            后续更新冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊已有后续简并记录纟递归婪溟链牜靶值大于一扌
        初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌


乸简并记录纟递归婪溟链
    表述冫简并集讠文本表达扌
    表述冫次大数讠溟次讠文本表达扌

MAX_VERSION
转换冫文件格式纟简并记录纟递归婪溟链扌
转换冫文件格式纟简并记录纟递归婪溟链灬扌
转换冫尾六表纟简并记录纟递归婪溟链扌
另档冫尾六表纟简并记录纟递归婪溟链扌
求冫丮最小比率辻靶值列表厈牜长度纟头部二幂纟左侧最大最短加链之于最小显链长纟靶值扌
最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌


乸异常牜最大靶值
规范冫列表纟文件路径冃靶值讠简并记录扌
reverse_
'''.split()#'''
    #另档冫极简次大数集纟简并记录纟递归婪溟链扌
    #另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌
    #另档冫双点易来简并态纟简并记录纟递归婪溟链扌
    #另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌

__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from functools import cached_property
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.filesys.check_paths_exist import check_paths_exist
    #.def check_paths_exist(paths, *, all_files=False, all_folders=False):

    from seed.tiny_.funcs import echo, fst, snd
    from seed.iters.chains import chains
    from itertools import pairwise, accumulate # islice
    from time import sleep, process_time, thread_time
    from seed.for_libs.for_time import sleep9KeyboardInterrupt_, resting9KeyboardInterrupt_, mk_rest_func_

    from seed.debug.print_err import print_err
    from seed.math.power.addition_chain.common.check import 检查冫严序加链乊靶值扌, 检查冫严序加链扌, 检查冫严序加链内容扌
    from seed.tiny_.check import check_type_in, check_type_is, check_int_ge, check_int_ge_le, check_may_
    from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3 import 靶值讠最小显链长扌 #取冫靶值讠最小显链长扌
    from seed.helper.stable_repr import stable_repr
    from seed.types.FrozenDict import mk_FrozenDict
    from seed.tiny_.containers import mk_tuple
    from seed.data_funcs.rngs import make_NonTouchRanges, sorted_ints_to_iter_nontouch_ranges
    from seed.data_funcs.rngs import ranges2hex2sz, ranges5hex2sz
        # [ver:=1]
    from seed.data_funcs.rngs import ranges2delta_txt_, ranges5delta_txt_, uint2base64_, uint5base64_
        # [ver:=2]
    from seed.mapping_tools.dict_op import inv__k2v_to_v2ks
    #.def inv__group_keys_by_value__immutable(k2v, ks=None, /, *, set_vs_list=False):
    #.    'Map k v -> Map v (Set k) #see also: seed.tiny_.dict__add_fmap_filter.group4dict_value'
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #[mk_namedtuple_,mk_namedtuple__check6make_] = lazy_import4funcs_('seed.for_libs.for_collections.override_repr4namedtuple', 'mk_namedtuple_,mk_namedtuple__check6make_', __name__)
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):


    #########
    #.from seed.data_funcs.rngs import make_Ranges, sorted_rngs_to_iter_nontouch_ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
        #TouchRangeBasedIntMapping.from_value2begin2sz/.from_rng_value_pairs/.from_clone_of_rngs_with_default
    #.from seed.data_funcs.rngs import IRanges
        #for:.from_hexXhexszpair_list/.from_hex_repr_pair_list/.from_len_rng2hexbegins/.from_len_rng2begin_chars/.from_char_pairs__str/.from_wave_rngtxt/.from_hex_sz_pair_list/.from_hex2sz
        #for:.from_touch_rngs/.from_sorted_rngs/.from_unsorted_rngs/.from_sorted_ints/.from_unsorted_ints/.from_sorted_chars/.from_unsorted_chars
    #.from seed.data_funcs.rngs import NonTouchRanges, TouchRanges, make_NonTouchRanges, make_TouchRanges
    #.from seed.data_funcs.rngs import len_of__rng, len_of__rng__neg_as0
    #########
    #########



#.#################################
___end_mark_of_excluded_global_names__0___ = ...


__all__


def reverse_(xs, /):
    return xs[::-1]

######################
#copy_from:view script/min_add_ver4__pseudo_addition_chain.py
#   _mkrs4rngs_()
######################
def _mkrs4rngs_():
    global _mkrs4rngs_
    old = _mkrs4rngs_
    ######################
    from seed.data_funcs.rngs import make_Ranges, sorted_rngs_to_iter_nontouch_ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
        #TouchRangeBasedIntMapping.from_value2begin2sz/.from_rng_value_pairs/.from_clone_of_rngs_with_default
    from seed.data_funcs.rngs import IRanges
        #for:.from_hexXhexszpair_list/.from_hex_repr_pair_list/.from_len_rng2hexbegins/.from_len_rng2begin_chars/.from_char_pairs__str/.from_hex_sz_pair_list/.from_hex2sz
        #for:.from_touch_rngs/.from_sorted_rngs/.from_unsorted_rngs/.from_sorted_ints/.from_unsorted_ints/.from_sorted_chars/.from_unsorted_chars
    from seed.data_funcs.rngs import NonTouchRanges, TouchRanges, make_NonTouchRanges, make_TouchRanges
    ######################
    from seed.helper.repr_input import repr_helper
    from seed.helper.stable_repr import stable_repr
    class RT:
        def __init__(sf, ranges, ):
            check_type_is(NonTouchRanges, ranges)
            sf._rs = ranges
        def __repr__(sf, /):
            s = stable_repr({int(u):sz for u, sz in sf._rs.to_hex_sz_pair_list()})
                #from_hex2sz
                #from_hex_sz_pair_list
            return f'RT({s})'
            return repr_helper(sf, sf._rs.ranges)
    ######################
    Mk = IRanges.from_sorted_ints
    _mkrs4rngs = (Mk, NonTouchRanges, RT)
    def _mkrs4rngs_():
        return _mkrs4rngs
    new = _mkrs4rngs_
    assert not new is old
    return _mkrs4rngs_()
######################

class 乸异常牜最大靶值(Exception):pass

#.class RT:
#.    '简并集'
#.    def __init__(sf, rngs, /):
#.        check_type_is(NonTouchRanges, rngs)
#.        sf._rngs = rngs
#.    @property
#.    def 简并集(sf, /):
#.        return sf._rngs
#.    def __repr__(sf, /):
_乸简并记录纟递归婪溟链 = mk_namedtuple__check6make_(__name__, '_乸简并记录纟递归婪溟链', '靶值  最小显链长 规模纟次大数集  规模纟简并集 次大数讠溟次  简并集     最短加链位置讠下界   最短加链位置讠上界    最短加链牜左侧最小 最短加链牜左侧最大 最短加链牜右侧最小 最短加链牜右侧最大')
    #RT(简并集)
class 乸简并记录纟递归婪溟链(_乸简并记录纟递归婪溟链):
    def _check6make_(sf, /):
        #check_type_is(NonTouchRanges, sf.简并集)
        sf.简并集.to_hex_sz_pair_list
        sf.次大数讠溟次.items
        check_int_ge(1, sf.靶值)
        check_int_ge(0, sf.最小显链长)
        L = 1+sf.最小显链长
        check_int_ge(0, sf.规模纟次大数集)
        check_int_ge(L, sf.规模纟简并集)
        assert sf.规模纟次大数集 == len(sf.次大数讠溟次)
        assert sf.规模纟简并集 == sf.简并集.len_ints()

        for x in sf[-6:]:
            check_type_is(tuple, x)
            assert len(x) == L
            assert x[-1] == sf.靶值
        for x in sf[-4:]:
            检查冫严序加链乊靶值扌(sf.靶值, x)


        左右小大 = (sf.最短加链牜左侧最小, sf.最短加链牜左侧最大, sf.最短加链牜右侧最小, sf.最短加链牜右侧最大)
        assert 左右小大 == sf[-4:]
        assert sf.最短加链牜左侧最小 == min(左右小大)
        assert sf.最短加链牜左侧最大 == max(左右小大)
        assert sf.最短加链牜右侧最小 == min(左右小大, key=reverse_)
        assert sf.最短加链牜右侧最大 == max(左右小大, key=reverse_)

        assert sf.最短加链位置讠下界 <= sf.最短加链位置讠上界

        assert (__:=靶值讠最小显链长扌(sf.靶值)) == sf.最小显链长, (sf, __)
    #def __str__(sf, /):
    def to_str(sf, /, *, ver):
        check_int_ge_le(1, MAX_VERSION, ver)
        match sf:
            case 乸简并记录纟递归婪溟链(靶值=靶值, 最小显链长=最小显链长, 规模纟次大数集=规模纟次大数集, 规模纟简并集=规模纟简并集, 次大数讠溟次=次大数讠溟次, 简并集=简并集, 最短加链位置讠下界=最短加链位置讠下界, 最短加链位置讠上界=最短加链位置讠上界, 最短加链牜左侧最小=最短加链牜左侧最小, 最短加链牜左侧最大=最短加链牜左侧最大, 最短加链牜右侧最小=最短加链牜右侧最小, 最短加链牜右侧最大=最短加链牜右侧最大):
                pass
            case _:
                raise 000

        def _0():
            yield 靶值
            yield 最小显链长
            yield 规模纟次大数集
            yield 规模纟简并集
            yield 表述冫次大数讠溟次讠文本表达扌(次大数讠溟次, ver=ver)
            yield 表述冫简并集讠文本表达扌(简并集, ver=ver)
            yield from _1(ver, _2())
        def _1(ver, uss, /):
            match ver:
                case 1 | 2:
                    yield from uss
                case 3:
                    yield _ver3__repr7uss_(uss)
                case bad:
                    raise Exception(ver)
        def _2():
            yield list(最短加链位置讠下界)
            yield list(最短加链位置讠上界)
            yield list(最短加链牜左侧最小)
            yield list(最短加链牜左侧最大)
            yield list(最短加链牜右侧最小)
            yield list(最短加链牜右侧最大)
        s = ', '.join(map(str, _0()))
        s = f'({s})'
        return s

MAX_VERSION = 3
    # check_int_ge_le
    # 构造冫局部变量环境纟解读简并记录扌()
    # 乸简并记录纟递归婪溟链.to_str()

def _ver3__eval7uss_(s8uss, /):
    ss = s8uss.split(';')
    if not len(ss) == 7:raise TypeError(s8uss)
    [j2u, *jss] = ([*ranges5delta_txt_(s).iter_ints()] for s in ss)
    uss = [[j2u[j] for j in js] for js in jss]
    if not len(uss) == 6:raise 000
    return uss
def _ver3__str7uss_(uss, /):
    uss = [*uss]
    if not len(uss) == 6:raise TypeError(uss)
    j2u = sorted(set(chains(uss)))
    u2j = {u:j for j, u in enumerate(j2u)}
    ss = []
    if 1:
        s8j2u = ranges2delta_txt_(_转换集合扌(j2u), validate=True)
        ss.append(s8j2u)
    for us in uss:
        js = [u2j[u] for u in us]
        s8js = ranges2delta_txt_(_转换集合扌(js), validate=True)
        ss.append(s8js)
    if not len(ss) == 7:raise Exception(uss)
    s8uss = ';'.join(ss)
    if not uss == (_uss:=_ver3__eval7uss_(s8uss)):raise Exception(uss, _uss, s8uss)
    return s8uss
def _ver3__repr7uss_(uss, /):
    s8uss = _ver3__str7uss_(uss)
    s = f'*UJ({s8uss!r})'
    return s
def _UJ6ver3_(txt, /):
    return _ver3__eval7uss_(txt)

def _FD6ver2_(txt, /):
    return mk_FrozenDict(_解读冫次大数讠溟次巛文本表达扌(txt))
def _解读冫次大数讠溟次巛文本表达扌(txt, /):
    'view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py'
    if not txt: raise Exception('bad format')
    if not txt[0] == '{': raise Exception('bad format')
    if not txt[-1] == '}': raise Exception('bad format')
    if txt == '{}':
        return {}
    ss = txt[1:-1].split(';')
    if not '' == ss[-1]: raise Exception('bad format')
    ss.pop()
    d = {}
    for s in ss:
        sk, sv = s.split(':', 1)
        溟次 = uint5base64_(sk)
        #.ssv = sv.split(',')
        #.差分表 = map(uint5base64_, ssv)
        #.次大数列表 = list(accumulate(差分表))
        #.assert len(次大数列表) == len(ssv)
        次大数列表 = list(ranges5delta_txt_(sv).iter_ints())
        sz = len(d)
        d.update((次大数, 溟次) for 次大数 in 次大数列表)
        assert sz + len(次大数列表) == len(d), (txt, sz, d, 次大数列表)
    d
    次大数讠溟次 = d
    return 次大数讠溟次
def _表述冫次大数讠溟次讠文本表达扌(次大数讠溟次, /):
    #次大数讠溟次 = dict(次大数讠溟次)
    check_type_is(dict, 次大数讠溟次)
    def __():
        溟次讠次大数列表 = inv__k2v_to_v2ks(次大数讠溟次, sorted(次大数讠溟次), set_vs_list=True)
        yield '{'
        for 溟次, 次大数列表 in sorted(溟次讠次大数列表.items()):
            yield uint2base64_(溟次)
            yield ':'
            #.yield ','.join(map(uint2base64_, _差分扌(次大数列表)))
            yield make_NonTouchRanges(sorted_ints_to_iter_nontouch_ranges(次大数列表)).to_delta_txt(validate=True)
            yield ';'
        yield '}'
    txt = ''.join(__())
    assert 次大数讠溟次 == (__:=_解读冫次大数讠溟次巛文本表达扌(txt)), (次大数讠溟次, txt, __)
    return txt
def _差分扌(us, /):
    us = list(us)
    差分表 = list(_0差分扌(us))
    _us = list(accumulate(差分表))
    assert us == _us, (us, _us)
    return 差分表
def _0差分扌(us, /):
    assert len(us)
    u = us[0]
    assert u >= 0
    yield u
    for u, v in pairwise(us):
        d = v - u
        assert d >= 0
        yield d
#_表述冫次大数讠溟次讠文本表达扌({36: 2, 82: 0, 84: 0, 92: 0, 98: 0, 100: 0, 132: 0, 144: 0, 160: 0})
def 表述冫次大数讠溟次讠文本表达扌(次大数讠溟次, /, *, ver):
    match ver:
        case 1:
            s = stable_repr(dict(次大数讠溟次))
        case 2 | 3:
            s = _表述冫次大数讠溟次讠文本表达扌(dict(次大数讠溟次))
            s = repr(s)
        case _:
            raise Exception('unknown ver', ver)
        #case
    s
    s = f'FD({s})'
    return s
def 表述冫简并集讠文本表达扌(简并集, /, *, ver):
    match ver:
        case 1:
            s = stable_repr({int(u):sz for u, sz in 简并集.to_hex_sz_pair_list()})
        case 2 | 3:
            #s = 简并集.to_delta_txt(validate=True)
            s = ranges2delta_txt_(简并集, validate=True)
            s = repr(s)
        case _:
            raise Exception('unknown ver', ver)
        #case
    s
    s = f'RT({s})'
    return s
    #.check_type_is(NonTouchRanges, 简并集)
    #.(Mk, NonTouchRanges, RT) = _mkrs4rngs_()
    #.return repr(RT(简并集))


def 构造冫简并记录纟靶值一扌():
    from seed.data_funcs.rngs import NonTouchRanges
    us = (1,)
    RT = NonTouchRanges.from_hex2sz
    简并记录纟靶值一 = 乸简并记录纟递归婪溟链(靶值=1, 最小显链长=0, 规模纟次大数集=0, 规模纟简并集=1, 次大数讠溟次=mk_FrozenDict({}), 简并集=RT({1:1}), 最短加链位置讠下界=us, 最短加链位置讠上界=us, 最短加链牜左侧最小=us, 最短加链牜左侧最大=us, 最短加链牜右侧最小=us, 最短加链牜右侧最大=us)
    return 简并记录纟靶值一

def 构造冫局部变量环境纟解读简并记录扌(ver, /):
    from seed.data_funcs.rngs import IRanges
    ex = {}
    match ver:
        case 1:
            ranges5hex2sz
            RT = IRanges.from_hex2sz
            FD = mk_FrozenDict
        case 2:
            ranges5delta_txt_
            RT = IRanges.from_delta_txt
            FD = _FD6ver2_
        case 3:
            ranges5delta_txt_
            RT = IRanges.from_delta_txt
            FD = _FD6ver2_
            ex = dict(UJ = _UJ6ver3_)
        case _:
            raise Exception('unknown ver', ver)
        #case

    RT, FD, ex
    _locals_ = dict(RT=RT, FD=FD, **ex)
    return _locals_
def 加载冫数据扌(ifile, /, *, ver, pre_ipaths, 鬽最大靶值):
    _locals_ = 构造冫局部变量环境纟解读简并记录扌(ver)

    ########
    靶值讠简并记录 = [None]
    ########
    for pre_ipath in pre_ipaths:
        with open(pre_ipath, 'rt', encoding='ascii') as pre_ifile:
            _加载冫数据扌(靶值讠简并记录, _locals_, pre_ifile, 鬽最大靶值)
    ########
    ifile.seek(0)
    _加载冫数据扌(靶值讠简并记录, _locals_, ifile, 鬽最大靶值)
    ########
    return 靶值讠简并记录
def _加载冫数据扌(靶值讠简并记录, _locals_, ifile, 鬽最大靶值, /):
    for i, line in enumerate(ifile, len(靶值讠简并记录)):
        row = eval(line, _locals_)
        check_type_is(tuple, row)
        assert row[0] == i
        简并记录 = 乸简并记录纟递归婪溟链(*row[:-6], *map(tuple, row[-6:]))
        assert 简并记录.靶值 == len(靶值讠简并记录)
        assert 简并记录.靶值 == i
        靶值讠简并记录.append(简并记录)
        if 简并记录.靶值 == 鬽最大靶值:
            raise 乸异常牜最大靶值(鬽最大靶值)#OverflowError
        #########
        #:if 0b00001:
        #:    # ^AssertionError: (15, 5, 5, 10, FD({3: 2, 5: 1, 9: 0, 10: 0, 12: 0}), RT({1: 6, 9: 2, 12: 1, 15: 1}), [1, 2, 3, 5, 9, 15], [1, 2, 4, 6, 12, 15], [1, 2, 3, 5, 10, 15], [1, 2, 4, 5, 10, 15], [1, 2, 3, 6, 9, 15], [1, 2, 3, 6, 12, 15])
        #:    assert 简并记录.最短加链位置讠上界 == 简并记录.最短加链牜右侧最大, 简并记录.to_str(ver=ver)
        #:    assert 简并记录.最短加链位置讠上界 == 简并记录.最短加链牜左侧最大, 简并记录.to_str(ver=ver)
        #########
        #:if 0b00001:
        #:    assert len(set(简并记录[-6:])) < 6, 简并记录.to_str(ver=ver)
        #:        # ^AssertionError: (15, 5, 5, 10, FD({3: 2, 5: 1, 9: 0, 10: 0, 12: 0}), RT({1: 6, 9: 2, 12: 1, 15: 1}), [1, 2, 3, 5, 9, 15], [1, 2, 4, 6, 12, 15], [1, 2, 3, 5, 10, 15], [1, 2, 4, 5, 10, 15], [1, 2, 3, 6, 9, 15], [1, 2, 3, 6, 12, 15])
        #########
    return



##################
def 转换冫文件格式纟简并记录纟递归婪溟链扌(输入文件路径冃靶值讠简并记录, 输出文件路径冃靶值讠简并记录, /, *, verI, verO):
    '注意:此版vs后一版:输入输出文件路径次序颠倒'
    return 转换冫文件格式纟简并记录纟递归婪溟链灬扌(输出文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录, verI=verI, verO=verO, 彣匹配模板纟前置文件路径冃靶值讠简并记录='')
def 转换冫文件格式纟简并记录纟递归婪溟链灬扌(输出文件路径冃靶值讠简并记录, /, *列表纟输入文件路径冃靶值讠简并记录, verI, verO, verbose=False, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
    check_int_ge_le(1, MAX_VERSION, verI)
    check_int_ge_le(1, MAX_VERSION, verO)
    assert not verI == verO, (verI, verO)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠简并记录, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=verI, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None)
        靶值讠简并记录
        for 靶值, 简并记录 in enumerate(靶值讠简并记录):
            if 靶值 == 0:continue
            verbose and print_err('靶值 =', 靶值)
            print(简并记录.to_str(ver=verO), file=ofile)
##################
def 另档冫极简次大数集纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠极简次大数集, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
    print_err('失败@[靶值==59]')
    check_int_ge_le(1, MAX_VERSION, ver)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠极简次大数集, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None)
            靶值讠极简次大数讠溟次 = [None]
            for 靶值, 简并记录 in enumerate(靶值讠简并记录):
                if 靶值 == 0:continue
                assert 靶值 == 简并记录.靶值
                assert 靶值 == len(靶值讠极简次大数讠溟次)
                极简次大数讠溟次 = {}
                for 次大数, 溟次 in 简并记录.次大数讠溟次.items():
                    内点 = (靶值 -次大数) >> 溟次
                    if 内点 in [次大数, 2, 1] or 内点 in 靶值讠极简次大数讠溟次[次大数]:
                        #递归/递降
                        极简次大数讠溟次[次大数] = 溟次
                极简次大数讠溟次
                if not (极简次大数讠溟次 or 靶值==1):raise Exception(靶值)
                    # ^Exception: 59
                靶值讠极简次大数讠溟次.append(极简次大数讠溟次)
                s = stable_repr((靶值, 简并记录.最小显链长, len(极简次大数讠溟次), 极简次大数讠溟次))
                print(s, file=ofile)

##################
def 另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠幸存次大数必由集, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
    print_err('失败@[靶值==77]')
    check_int_ge_le(1, MAX_VERSION, ver)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠幸存次大数必由集, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None)
            #幸存次大数必由集-->(幸存次大数讠溟次, 幸存次大数讠必由集)
            #必由集-->内点溟化值集
            靶值讠幸存次大数讠溟次 = [None]
            #靶值讠幸存次大数讠必由集 = [None]
            #靶值讠幸存次大数讠内点溟化值集 = [None]
            靶值讠内点溟化值合集 = [None]
            for 靶值, 简并记录 in enumerate(靶值讠简并记录):
                if 靶值 == 0:continue
                assert 靶值 == 简并记录.靶值
                assert 靶值 == len(靶值讠幸存次大数讠溟次)
                assert 靶值 == len(靶值讠内点溟化值合集)
                幸存次大数讠溟次 = {}
                内点溟化值合集 = set()
                for 次大数, 溟次 in 简并记录.次大数讠溟次.items():
                    内点 = (靶值 -次大数) >> 溟次
                    if 内点 in [次大数, 2, 1] or 内点 in 靶值讠幸存次大数讠溟次[次大数] or 内点 in 靶值讠内点溟化值合集[次大数]:
                        #递归/递降
                        幸存次大数讠溟次[次大数] = 溟次
                        内点溟化值合集.update(内点<<ez for ez in range(1+溟次))
                幸存次大数讠溟次
                内点溟化值合集
                if not (幸存次大数讠溟次 or 靶值==1):raise Exception(靶值)
                    # ^Exception: 77
                靶值讠幸存次大数讠溟次.append(幸存次大数讠溟次)
                靶值讠内点溟化值合集.append(内点溟化值合集)
                s = stable_repr((靶值, 简并记录.最小显链长, len(幸存次大数讠溟次), 幸存次大数讠溟次, len(内点溟化值合集), 内点溟化值合集))
                print(s, file=ofile)


##################
def 另档冫双点易来简并态纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠双点易来简并态, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
    check_int_ge_le(1, MAX_VERSION, ver)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠双点易来简并态, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None)
            #双点易来简并态-->(易来次大数讠溟次, 定点讠易来简并态)
            靶值讠易来次大数讠溟次 = [None]
            靶值讠定点讠易来简并态 = [None]
            for 靶值, 简并记录 in enumerate(靶值讠简并记录):
                if 靶值 == 0:continue
                assert 靶值 == 简并记录.靶值
                assert 靶值 == len(靶值讠易来次大数讠溟次)
                assert 靶值 == len(靶值讠定点讠易来简并态)
                ######
                易来次大数讠溟次 = _求冫易来次大数讠溟次扌(靶值讠易来次大数讠溟次, 靶值讠定点讠易来简并态, 靶值, 简并记录.次大数讠溟次)
                if not (易来次大数讠溟次 or 靶值==1):raise Exception(靶值)
                    # xxx^Exception: 77
                ######
                定点讠易来简并态 = _求冫定点讠易来简并态扌(靶值讠定点讠易来简并态, 靶值, 易来次大数讠溟次)
                if not 定点讠易来简并态.get(靶值):raise Exception(靶值)
                ######
                靶值讠易来次大数讠溟次.append(易来次大数讠溟次)
                靶值讠定点讠易来简并态.append(定点讠易来简并态)
                s = stable_repr((靶值, 简并记录.最小显链长, len(易来次大数讠溟次), 易来次大数讠溟次, len(定点讠易来简并态), 定点讠易来简并态))
                print(s, file=ofile)


def _求冫易来次大数讠溟次扌(靶值讠易来次大数讠溟次, 靶值讠定点讠易来简并态, 靶值, 次大数讠溟次, /):
    易来次大数讠溟次 = {}
    for 次大数, 溟次 in 次大数讠溟次.items():
        内点 = (靶值 -次大数) >> 溟次
        #内点溟化值集 = {内点<<ez for ez in range(1+溟次)}
        if 内点 in [次大数, 2, 1] or 内点 in 靶值讠易来次大数讠溟次[次大数] or 靶值讠定点讠易来简并态[次大数].get(内点):
            #递归/递降
            易来次大数讠溟次[次大数] = 溟次
    return 易来次大数讠溟次
def _求冫定点讠易来简并态扌(靶值讠定点讠易来简并态, 靶值, 易来次大数讠溟次, /):
    '-> 定点讠易来简并态'
    定点讠易来简并态 = {}
    if 靶值 <= 3:
        简并态 = set(range(1, 1+靶值))
        定点讠易来简并态 = {定点:简并态 for 定点 in 简并态}
    else:
        定点讠易来简并态 = {}
        for 定点 in range(3, 1+靶值):
            有效集 = 易来简并态纟靶值乊定点 = _求冫易来简并态巛定点牜大于二扌(靶值讠定点讠易来简并态, 靶值, 易来次大数讠溟次, 定点)
            if 有效集:
                定点讠易来简并态[定点] = 有效集
        #end-for 定点 in range(3, 靶值):
        for 定点 in [1, 2]:
            定点讠易来简并态[定点] = 定点讠易来简并态[靶值]
    return 定点讠易来简并态


def _求冫易来简并态巛定点牜大于二扌(靶值讠定点讠易来简并态, 靶值, 易来次大数讠溟次, 定点, /):
    '... -> 定点 -> 易来简并态'
    def 鬽取臫靶值讠定点讠易来简并态扌(次大数, 内点, 缺省值, /):
        return 靶值讠定点讠易来简并态[次大数].get(内点, 缺省值)
    return _求冫易来简并态巛定点牜大于二牜共用扌(鬽取臫靶值讠定点讠易来简并态扌, 靶值, 易来次大数讠溟次, 定点)
##################
#上下共用:
def _求冫易来简并态巛定点牜大于二牜共用扌(鬽取臫靶值讠定点讠易来简并态扌, 靶值, 易来次大数讠溟次, 定点, /):
    assert 3 <= 定点 <= 靶值
    有效集 = set()
    for (次大数, 溟次) in 易来次大数讠溟次.items():
        内点 = (靶值 -次大数) >> 溟次
        内点溟化值集 = [内点<<ez for ez in range(1+溟次)]
            #可能有:[次大数 < max(内点溟化值集)]
        if 定点 in [靶值, 次大数, 2, 1] or 定点 in 内点溟化值集:
            #s = 靶值讠定点讠易来简并态[次大数].get(内点, [])
            s = 鬽取臫靶值讠定点讠易来简并态扌(次大数, 内点, [])
        elif 定点 > 次大数:
            s = []
        elif 内点 in [次大数, 2, 1]:
            #s = 靶值讠定点讠易来简并态[次大数].get(定点, [])
            s = 鬽取臫靶值讠定点讠易来简并态扌(次大数, 定点, [])
        #elif 定点 in 靶值讠定点讠易来简并态[次大数].get(内点, []):
        elif 定点 in 鬽取臫靶值讠定点讠易来简并态扌(次大数, 内点, []):
            s = [定点]
        else:
            s = []
        内有效集 = s
        if 内有效集:
            有效集.update(内有效集)
            有效集.update(内点溟化值集)
    有效集
    if 有效集:
        有效集.update([靶值, 次大数, 2, 1])
    return (易来简并态:=有效集)
##################
def 另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌(输出文件路径冃靶值讠双点易来简并态, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录='', verbose=False):
    '按需计算'
    check_int_ge_le(1, MAX_VERSION, ver)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠双点易来简并态, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            verbose and print_err('loading data...')
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None)
            verbose and print_err('main loop...')
            #双点易来简并态-->(易来次大数讠溟次, 定点讠易来简并态)
            靶值讠易来次大数讠溟次 = [None]
            靶值讠易来简并态 = [None]
            缓存冃靶值讠定点讠易来简并态 = [None]
            for 靶值, 简并记录 in enumerate(靶值讠简并记录):
                if 靶值 == 0:continue
                verbose and print_err('靶值 =', 靶值)
                assert 靶值 == 简并记录.靶值
                assert 靶值 == len(靶值讠易来次大数讠溟次)
                assert 靶值 == len(靶值讠易来简并态)
                assert 靶值 == len(缓存冃靶值讠定点讠易来简并态)
                ######
                缓存冃靶值讠定点讠易来简并态.append({})
                ######
                易来次大数讠溟次 = _求冫易来次大数讠溟次牜按需计算扌(靶值讠易来简并态, 靶值, 简并记录.次大数讠溟次)
                if not (易来次大数讠溟次 or 靶值==1):raise Exception(靶值)
                    # ^Exception: 2077
                ######
                易来简并态纟靶值 = _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 靶值)
                if not 易来简并态纟靶值:raise Exception(靶值)
                ######
                靶值讠易来次大数讠溟次.append(易来次大数讠溟次)
                靶值讠易来简并态.append(易来简并态纟靶值)
                #s = stable_repr((靶值, 简并记录.最小显链长, len(易来次大数讠溟次), 易来次大数讠溟次, len(易来简并态纟靶值), 易来简并态纟靶值))
                s4s = ranges2delta_txt_(_转换集合扌(易来简并态纟靶值), validate=True)
                #.s = stable_repr((靶值, 简并记录.最小显链长, len(易来次大数讠溟次), 易来次大数讠溟次, len(易来简并态纟靶值), s4s))
                s4d = _表述冫次大数讠溟次讠文本表达扌(易来次大数讠溟次)
                s = stable_repr((靶值, 简并记录.最小显链长, len(易来次大数讠溟次), s4d, len(易来简并态纟靶值), s4s))
                print(s, file=ofile)

def _求冫易来次大数讠溟次牜按需计算扌(靶值讠易来简并态, 靶值, 次大数讠溟次, /):
    易来次大数讠溟次 = {}
    for 次大数, 溟次 in 次大数讠溟次.items():
        内点 = (靶值 -次大数) >> 溟次
        #内点溟化值集 = [内点<<ez for ez in range(1+溟次)]
        #if 内点 in [次大数, 2, 1] or 内点 in 靶值讠易来次大数讠溟次[次大数] or 内点 in 靶值讠易来简并态[次大数]:
        if 内点 in 靶值讠易来简并态[次大数]:
            #递归/递降
            易来次大数讠溟次[次大数] = 溟次
    return 易来次大数讠溟次


def _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 定点, /):
    '-> 易来简并态纟靶值乊定点'
    assert 1 <= 定点 <= 靶值
    v2s = 缓存冃靶值讠定点讠易来简并态[靶值]
    if not None is (s:=v2s.get(定点)):
        return s
    s = _0靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 定点)
    v2s[定点] = s
    return _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 定点)
def _0靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 定点, /):
    if 靶值 == 定点:
        if 靶值 < len(靶值讠易来简并态):
            return 靶值讠易来简并态[靶值]
        if not 靶值 == len(靶值讠易来简并态):raise 000
        if 靶值 <= 3:
            return set(range(1, 1+靶值))
        # [4 <= 定点 == 靶值 == len(靶值讠易来简并态)]
    else:
        # [1 <= 定点 < 靶值]
        pass
    # [4 <= 定点 == 靶值]or[1 <= 定点 < 靶值]
    if 定点 <= 2:
        # [1 <= 定点 < 靶值]
        assert 靶值 > 定点
        return _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 靶值)
    # [3 <= 定点]
    # [4 <= 定点 == 靶值]or[3 <= 定点 < 靶值]
    def 鬽取臫靶值讠定点讠易来简并态扌(次大数, 内点, 缺省值, /):
        s = _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 靶值讠易来次大数讠溟次[次大数], 次大数, 内点)
        return s if s else 缺省值
    有效集 = 易来简并态纟靶值乊定点 = _求冫易来简并态巛定点牜大于二牜共用扌(鬽取臫靶值讠定点讠易来简并态扌, 靶值, 易来次大数讠溟次, 定点)
    return 易来简并态纟靶值乊定点

##################
#共用:
def _get_s4u_5line__verX_(line, /):
    a = 1+line.index('(')
    ')'
    b = line.index(',', a)
    s4u = line[a:b]
    return (s4u, a, b)
def _get_s4uss_5line__ver1_ver2_(line, /):
    '('
    j = line.rindex(')')
    i = j
    for _ in range(6):
        i = line.rindex(', [1', 0, i)
        ']'
    assert line[i:i+4] == ', [1'
    ']'
    i += 2
    s4uss = line[i:j]
    return (s4uss, i, j)



    #.'('
    #.i = line.rindex(')', 0, j)
    #.'('
    #.assert line[i:i+5] == '), [1'
    #.']'
    #.s4uss = line[i+3:j]
    #.return s4uss
def _get_s4uss_5line__ver3_(line, /):
    '('
    j = line.rindex(')')
    i = line.rindex(', *UJ(', 0, j)
    ')'
    i += 2
    s4uss = line[i:j]
    return (s4uss, i, j)
def _mk_get_s4uss_5line__5ver_(ver, /):
    match ver:
        case 1 | 2:
            get_s4uss_5line__verX_ = _get_s4uss_5line__ver1_ver2_
        case 3:
            get_s4uss_5line__verX_ = _get_s4uss_5line__ver3_
        case bad:
            raise Exception(ver)
        #case
    return get_s4uss_5line__verX_
##################
_ver3__eval7uss_
_ver3__str7uss_
_ver3__repr7uss_
def _repr5uss__ver3_(uss, /):
    '-> s4uss'
    assert len(uss) == 6
    return _ver3__repr7uss_(uss)
def _repr5uss__ver1_ver2_(uss, /):
    '-> s4uss'
    assert len(uss) == 6
    return str(uss)[1:-1]
def _repr2uss__ver3_(s4uss, /):
    '-> uss'
    s = f'[{s4uss}]'
    return eval(s, dict(UJ=_ver3__eval7uss_))
def _repr2uss__ver1_ver2_(s4uss, /):
    '-> uss'
    s = f'[{s4uss}]'
    return eval(s)
def _mk_repr25uss__5ver_(ver, /):
    match ver:
        case 1 | 2:
            _repr25uss_ = (_repr2uss__ver1_ver2_, _repr5uss__ver1_ver2_)
        case 3:
            _repr25uss_ = (_repr2uss__ver3_, _repr5uss__ver3_)
        case bad:
            raise Exception(ver)
        #case
    return _repr25uss_
##################
##################
def 转换冫尾六表纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠尾六表, /, *列表纟输入文件路径冃靶值讠尾六表, verI, verO, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', 欤删除中段数据=False, 欤允许输入输出是同版本=False, verbose=False):
    #++kw:欤删除中段数据
    #++kw:欤允许输入输出是同版本
    '[尾六表 =[def]= regex"({靶值}.*, {六表})"] #eg:简并记录,下上界辻左右大小四色最短加链'
    check_int_ge_le(1, MAX_VERSION, verI)
    check_int_ge_le(1, MAX_VERSION, verO)
    _verI = max(verI, 2)
    _verO = max(verO, 2)
    if _verI == _verO and not 欤允许输入输出是同版本:raise Exception((verI, verO))
    (前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠尾六表, 列表纟输入文件路径冃靶值讠尾六表)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(verI)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(verI)
    (_repr2uss__verO_, _repr5uss__verO_) = _mk_repr25uss__5ver_(verO)
    def body_(ipath, ifile, ofile, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            (s4u, a, b) = _get_s4u_5line__verX_(line)
            verbose and print_err(f'靶值: {s4u!s}')
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            s4ussO = _repr5uss__verO_(uss)
            if 欤删除中段数据:
                t = f'({s4u}, {s4ussO})'
            else:
                prefix = line[a:i]
                t = f'({prefix}{s4ussO})'
            print(t, file=ofile)
    def main():
        with open(输出文件路径冃靶值讠尾六表, 'xt', encoding='ascii') as ofile:
            for ipath in [*前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表]:
                with open(ipath, 'rt', encoding='ascii') as ifile:
                    body_(ipath, ifile, ofile)
    return main()


##################
def 另档冫尾六表纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠尾六表, /, *列表纟输入文件路径冃靶值讠尾六表, ver, verI=-1, verO=-1, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False):
    #原名:另档冫下上界辻左右大小四色最短加链纟简并记录纟递归婪溟链扌
    '[尾六表 =[def]= regex"({靶值}.*, {六表})"] #eg:简并记录,下上界辻左右大小四色最短加链'
    check_type_is(int, ver)
    check_type_is(int, verI)
    check_type_is(int, verO)
    if not ver == -1:
        check_int_ge_le(1, MAX_VERSION, ver)
        if not verI == -1:raise TypeError
        if not verO == -1:raise TypeError
        verI = ver
        verO = ver
    check_int_ge_le(1, MAX_VERSION, verI)
    check_int_ge_le(1, MAX_VERSION, verO)
    return 转换冫尾六表纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠尾六表, *列表纟输入文件路径冃靶值讠尾六表, verI=verI, verO=verO, 彣匹配模板纟前置文件路径冃靶值讠尾六表=彣匹配模板纟前置文件路径冃靶值讠尾六表, 欤删除中段数据=True, 欤允许输入输出是同版本=True, verbose=verbose)
    #.(前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠尾六表, 列表纟输入文件路径冃靶值讠尾六表)
    #.get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(ver)
    #.def body_(ipath, ifile, ofile, /):
    #.    verbose and print_err(f'ipath: {ipath!r}')
    #.    for line in ifile:
    #.        (s4u, a, b) = _get_s4u_5line__verX_(line)
    #.        verbose and print_err(f'靶值: {s4u!s}')
    #.        (s4uss, i, j) = get_s4uss_5line__verX_(line)
    #.        s = f'({s4u}, {s4uss})'
    #.        if 0:
    #.            _s = s.replace(', *UJ', '')
    #.            if (__:=set(_s) -set('0123456789, []()')):raise Exception(__)
    #.            u_uss = tuple(map(tuple, eval(s)))
    #.            assert len(u_uss) == 1+6
    #.        s
    #.        print(s, file=ofile)
    #.def main():
    #.    with open(输出文件路径冃靶值讠尾六表, 'xt', encoding='ascii') as ofile:
    #.        for ipath in [*前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表]:
    #.            with open(ipath, 'rt', encoding='ascii') as ifile:
    #.                body_(ipath, ifile, ofile)
    #.return main()

##################
def 求冫丮最小比率辻靶值列表厈牜长度纟头部二幂纟左侧最大最短加链之于最小显链长纟靶值扌(*列表纟输入文件路径冃靶值讠尾六表, ver, verbose=False):
    from fractions import Fraction
    check_int_ge_le(1, MAX_VERSION, ver)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(ver)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(ver)
    def body_(ipath, ifile, 最小比率, 列表纟靶值, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            (s4u, a, b) = _get_s4u_5line__verX_(line)
            verbose and print_err(f'靶值: {s4u!s}')
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            靶值 = int(s4u)
            最短加链牜左侧最大 = uss[3]
            最小显链长纟靶值 = -1+len(最短加链牜左侧最大)
            长度纟头部二幂 = 0
            for u, v in pairwise(最短加链牜左侧最大):
                if v == (u<<1):
                    长度纟头部二幂 += 1
                else:
                    break
            长度纟头部二幂
            if 最小显链长纟靶值 == 0:
                continue
            比率 = Fraction(长度纟头部二幂, 最小显链长纟靶值)
            if 比率 < 最小比率:
                最小比率 = 比率
                列表纟靶值 = [靶值]
            elif 比率 == 最小比率:
                列表纟靶值.append(靶值)
            else:
                continue
        return (最小比率, 列表纟靶值)
    def main():
        最小比率 = Fraction(1)
        列表纟靶值 = [1]
        for ipath in 列表纟输入文件路径冃靶值讠尾六表:
            with open(ipath, 'rt', encoding='ascii') as ifile:
                (最小比率, 列表纟靶值) = body_(ipath, ifile, 最小比率, 列表纟靶值)
        return (最小比率, 列表纟靶值)
    return main()



##################
def 最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌(*列表纟输入文件路径冃靶值讠尾六表, ver, verbose=False, 欤记录首峰值位=False, 欤趃输出=False):
    from seed.math.power.addition_chain.shortest.rewrite3 import 枚举冫递归婪溟链巛严序加链扌
    from seed.iters.maxs import maxs_, maxs7continue_, mins_, mins7continue_

    check_int_ge_le(1, MAX_VERSION, ver)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(ver)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(ver)
    def 最大内点址距辻列表乊加链扌(加链, /):
        #mins_-max
        (最小纟最大内点址距, 列表纟主线) = mins_(lambda 递归婪溟链:max(递归婪溟链.次大数址引讠内点址距), lambda 递归婪溟链:递归婪溟链.主线, 枚举冫递归婪溟链巛严序加链扌(加链))
            #先最大{@递归婪溟链}再最小{@加链}！
        return (最小纟最大内点址距, 列表纟主线)
    def 最小化乊尾四链冫最大内点址距乊加链扌(尾四链, /):
        (最小纟最大内点址距, 列表纟列表纟主线) = mins_(fst, snd, map(最大内点址距辻列表乊加链扌, sorted(set(map(mk_tuple, 尾四链)))))
        return (最小纟最大内点址距, 列表纟列表纟主线)
    def body_(ipath, ifile, 最大内点址距, 列表纟输出, 列表纟首峰值位, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            (s4u, a, b) = _get_s4u_5line__verX_(line)
            verbose and print_err(f'靶值: {s4u!s}')
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            尾六表 = uss
            assert len(尾六表) == 6
            尾四链 = 尾六表[2:]
            assert len(尾四链) == 4

            靶值 = int(s4u)
            if 靶值 == 1:
                continue
            (最小纟最大内点址距, 列表纟列表纟主线) = 最小化乊尾四链冫最大内点址距乊加链扌(尾四链)
            if 最小纟最大内点址距 < 最大内点址距:
                continue
            if 最小纟最大内点址距 > 最大内点址距:
                最大内点址距 = 最小纟最大内点址距
                列表纟输出 = []
                if 欤记录首峰值位:
                    列表纟首峰值位.append((最大内点址距, list(chains(列表纟列表纟主线))))
            列表纟输出.extend(chains(列表纟列表纟主线))
        return (最大内点址距, 列表纟输出)
    def main():
        列表纟首峰值位 = []
        最大内点址距 = 0
        列表纟输出 = [(1,)]
        for ipath in 列表纟输入文件路径冃靶值讠尾六表:
            with open(ipath, 'rt', encoding='ascii') as ifile:
                (最大内点址距, 列表纟输出) = body_(ipath, ifile, 最大内点址距, 列表纟输出, 列表纟首峰值位)
        总输出 = (最大内点址距, 列表纟输出) if not 欤记录首峰值位 else (最大内点址距, 列表纟输出, 列表纟首峰值位)
        if 欤趃输出:
            总输出 = chains([总输出[:1], *总输出[1:]])
        return 总输出
    return main()


##################




##################
##################
#move_to: view ../../python3_src/seed/for_libs/for_time.py
mk_rest_func_
##################
def 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟文件路径冃靶值讠简并记录, /):
    check_type_is(tuple, 列表纟文件路径冃靶值讠简并记录)
    #########
    (*前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录) = 列表纟文件路径冃靶值讠简并记录
    777;0b00000 and print_err('verbose:', (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录, 彣匹配模板纟前置文件路径冃靶值讠简并记录))
    if 彣匹配模板纟前置文件路径冃靶值讠简并记录:
        if 前置列表纟文件路径冃靶值讠简并记录:raise TypeError(前置列表纟文件路径冃靶值讠简并记录, 彣匹配模板纟前置文件路径冃靶值讠简并记录)
        import pathlib, glob
        iopath = pathlib.Path(文件路径冃靶值讠简并记录)
        #.idir = pathlib.Path('.')
        #.前置列表纟文件路径冃靶值讠简并记录 = sorted(idir.glob(彣匹配模板纟前置文件路径冃靶值讠简并记录))
        前置列表纟文件路径冃靶值讠简并记录 = sorted(glob.iglob(彣匹配模板纟前置文件路径冃靶值讠简并记录))
        777;0b00000 and print_err('verbose:', (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录))
        if iopath.exists():
            if 前置列表纟文件路径冃靶值讠简并记录 and iopath.samefile(前置列表纟文件路径冃靶值讠简并记录[-1]):
                前置列表纟文件路径冃靶值讠简并记录.pop()
            for pre_ipath in 前置列表纟文件路径冃靶值讠简并记录:
                if iopath.samefile(pre_ipath):raise TypeError(iopath, pre_ipath)
        if not 'y' == input(f'ok?:{前置列表纟文件路径冃靶值讠简并记录}:{iopath!r}:{len(前置列表纟文件路径冃靶值讠简并记录)}+1:ok?(y):'):
            if 0:
                #需改变接口: -> may (xx, yy)
                print_err('abort')
                return
            raise Exception('abort')
        777;0b00000 and print_err('verbose:', (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录))
    前置列表纟文件路径冃靶值讠简并记录
    #########
    #前置列表纟文件路径冃靶值讠简并记录 = tuple(map(Path, 前置列表纟文件路径冃靶值讠简并记录))
    前置列表纟文件路径冃靶值讠简并记录 = tuple(前置列表纟文件路径冃靶值讠简并记录)
    check_paths_exist(前置列表纟文件路径冃靶值讠简并记录, all_files=True)
    文件路径冃靶值讠简并记录
    return (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录)
    #########
#.def 枚举生成冫文件后续简并记录纟递归婪溟链扌(文件路径冃靶值讠简并记录, /, *, ver, 休眠期=0.0):
def 枚举生成冫文件后续简并记录纟递归婪溟链扌(*列表纟文件路径冃靶值讠简并记录, ver, 休眠期=0.0, 苏醒期=2.0, 自顶向下搜索丷自底向上注册=False, 鬽最大靶值=None, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
    if not 列表纟文件路径冃靶值讠简并记录:raise TypeError
    check_type_is(bool, 自顶向下搜索丷自底向上注册)
    check_type_in([float, str], 休眠期)
    check_int_ge_le(1, MAX_VERSION, ver)
    check_may_([check_int_ge, 1], 鬽最大靶值)
    check_type_is(str, 彣匹配模板纟前置文件路径冃靶值讠简并记录)

    #########
    _rest = mk_rest_func_(休眠期, 苏醒期)
    #########
    (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟文件路径冃靶值讠简并记录)
    #########
    with open(文件路径冃靶值讠简并记录, 'at+', encoding='ascii') as iofile:
        起点 = iofile.tell()
        iofile.seek(0)
        靶值讠简并记录 = 加载冫数据扌(iofile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=鬽最大靶值)
            #^乸异常牜最大靶值
        assert 起点 == iofile.tell()
        assert None is 鬽最大靶值 or -1+len(靶值讠简并记录) < 鬽最大靶值
        777;_rest()
        枚举冫后续简并记录纟递归婪溟链牜囜囜囜扌 = 枚举冫后续简并记录纟递归婪溟链牜自顶向下搜索扌 if not 自顶向下搜索丷自底向上注册 else 枚举冫后续简并记录纟递归婪溟链牜自底向上注册扌
        for 简并记录 in 枚举冫后续简并记录纟递归婪溟链牜囜囜囜扌(靶值讠简并记录, 鬽最大靶值=鬽最大靶值):
            assert 1+简并记录.靶值 == len(靶值讠简并记录)
            s = 简并记录.to_str(ver=ver)
            777;print(s, file=iofile)
            777;yield s
            #if 简并记录.靶值 == 鬽最大靶值: return
            777;_rest()
def 枚举冫后续简并记录纟递归婪溟链牜自顶向下搜索扌(靶值讠简并记录, /, *, 鬽最大靶值):
    777;0b00001 and print_err('自顶向下搜索')
    if not len(靶值讠简并记录):raise TypeError
    check_may_([check_int_ge, len(靶值讠简并记录)], 鬽最大靶值)

    raise 暂停使用冫自顶向下搜索
    000
    if not 鬽最大靶值 is None and 鬽最大靶值 < len(靶值讠简并记录): return
    while 1:
        简并记录 = 求冫后续简并记录纟递归婪溟链牜自顶向下搜索扌(靶值讠简并记录)
        assert 简并记录.靶值 == len(靶值讠简并记录)
        靶值讠简并记录.append(简并记录)
        yield 简并记录
        if 简并记录.靶值 == 鬽最大靶值: return


def 求冫后续简并记录纟递归婪溟链牜自顶向下搜索扌(靶值讠简并记录, /):
    assert 靶值讠简并记录
    靶值 = len(靶值讠简并记录)
    if 靶值 == 1:
        return 构造冫简并记录纟靶值一扌()
    (最小显链长纟靶值, 次大数讠溟次) = _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自顶向下搜索扌(靶值讠简并记录, 靶值)
    777;伪简并集纟靶值 = make_NonTouchRanges([(1, 1+靶值)])
    777;伪简并记录纟靶值 = _乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 伪简并集纟靶值.len_ints(), 次大数讠溟次, 伪简并集纟靶值, None, None, None, None, None, None)
    777;靶值讠简并记录.append(伪简并记录纟靶值)
    try:
        (简并集纟靶值, 下上界, 左右小大) = _过滤乊内点集扌(靶值讠简并记录, 靶值, ())
    finally:
        if not 靶值讠简并记录.pop() is 伪简并记录纟靶值:raise 000
    (最短加链位置讠下界, 最短加链位置讠上界) = 下上界
    (最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大) = 左右小大
    简并集纟靶值 = _转换集合扌(简并集纟靶值)
    #.777;0b00001 and print_err(靶值, 简并集纟靶值)
    简并记录纟靶值 = 乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 简并集纟靶值.len_ints(), 次大数讠溟次, 简并集纟靶值, 最短加链位置讠下界, 最短加链位置讠上界, 最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大)
    #:if 0b00001:
    #:    #:    # ^AssertionError: (15, 5, 5, 10, FD({3: 2, 5: 1, 9: 0, 10: 0, 12: 0}), RT({1: 6, 9: 2, 12: 1, 15: 1}), [1, 2, 3, 5, 9, 15], [1, 2, 4, 6, 12, 15], [1, 2, 3, 5, 10, 15], [1, 2, 4, 5, 10, 15], [1, 2, 3, 6, 9, 15], [1, 2, 3, 6, 12, 15])
    #:    assert 最短加链位置讠上界 == 最短加链牜右侧最大, 简并记录纟靶值.to_str(ver=ver)
    #:    assert 最短加链位置讠上界 == 最短加链牜左侧最大, 简并记录纟靶值.to_str(ver=ver)
    return 简并记录纟靶值

    #bug:最短加链:缺失:内点*2**ez
    #.s = {靶值}
    #.ss = []
    #.lus = []
    #.lrs = []
    #.for 次大数, 溟次 in 次大数讠溟次.items():
    #.    内点 = (靶值 -次大数) >> 溟次
    #.    777;s.update(内点<<ez for ez in range(1, 1+溟次))
    #.    (简并集纟次大数乊内点, 下上界, 左右小大) = _过滤乊内点集扌(靶值讠简并记录, 次大数, {内点})
    #.    #简并集纟靶值乊次大数
    #.    ss.append(简并集纟次大数乊内点)
    #.    lus.append(下上界)
    #.    lrs.append(左右小大)
    #.s, ss, lus, lrs
    #.简并集纟靶值 = _集合并扌(s, ss)
    #.下上界 = _求冫下上界扌(靶值, lus)
    #.左右小大 = _求冫左右小大扌(靶值, lrs)
    #.(最短加链位置讠下界, 最短加链位置讠上界) = 下上界
    #.(最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大) = 左右小大
    #.简并记录纟靶值 = 乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 简并集纟靶值.len_ints(), 次大数讠溟次, 简并集纟靶值, 最短加链位置讠下界, 最短加链位置讠上界, 最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大)
    #.return 简并记录纟靶值
def _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自顶向下搜索扌(靶值讠简并记录, 靶值, /):
    #DONE:由 自顶向下搜索 改为 自底向上注册
    #   _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自底向上注册扌
    assert 靶值 >= 2
    最小显链长纟靶值 = 1+靶值
    777;次大数讠溟次 = None
    for 次大数 in reversed(range(1, 靶值)):
        溟化值 = 靶值 -次大数
        简并记录纟次大数 = 靶值讠简并记录[次大数]
        简并集纟次大数 = 简并记录纟次大数.简并集
        最小显链长纟次大数 = 简并记录纟次大数.最小显链长

        欤成功 = False
        内点 = 溟化值
        for 溟次 in range(最小显链长纟靶值 -最小显链长纟次大数):
            if 内点 <= 次大数 and 内点 in 简并集纟次大数:
                欤成功 = True
                break
            if 内点 & 1:
                break
            内点 >>= 1
        if not 欤成功:
            continue
        #########
        # [:约束牜定义冫递归婪溟链]:goto
        assert 靶值 == 次大数 + (内点<<溟次)
        assert 内点 in 简并集纟次大数
        显链长纟靶值 = 最小显链长纟次大数 +1 +溟次
        #########
        assert 显链长纟靶值 <= 最小显链长纟靶值
        if 显链长纟靶值 == 最小显链长纟靶值:
            次大数讠溟次[次大数] = 溟次
        elif 显链长纟靶值 < 最小显链长纟靶值:
            最小显链长纟靶值 = 显链长纟靶值
            次大数讠溟次 = {次大数:溟次}
        else:
            raise 000
    次大数讠溟次
    assert 次大数讠溟次
    assert 最小显链长纟靶值 < 靶值
    return (最小显链长纟靶值, 次大数讠溟次)

def 枚举冫最短加链乊内点集扌(靶值讠简并记录, 靶值, 内点集, /):
    L = 1 + 靶值讠简并记录[靶值].最小显链长
    us = []         #部分纟最短加链
    ns = set(内点集)#内点集#过滤器
    ns.discard(靶值)
    def _f1(u, /):
        assert not u in ns
        us.append(u)
        if u == 1:
            #assert not ns, (us, ns)
            #   ^AssertionError: ([11, 6, 5, 2, 4, 1], {3})
            #       5 1 2 1 True {1} {3} [11, 6, 5, 2, 4, 1]
            #       11 5 1 3 True set() {3} [11, 6, 5, 2, 4, 1]
            if not ns:
                最短加链 = reverse_(us)
                最短加链.sort()
                assert L == len(最短加链)
                yield tuple(最短加链)
            else:
                pass#<<==us.pop()
            #bug:if ns:return
        else:
            yield from _f2(u)
        us.pop()
    def _f2(靶值, /):
        nonlocal us, ns
        assert 靶值 > 1
        简并记录 = 靶值讠简并记录[靶值]
        s = 简并记录.简并集
        #if not all(n in s for n in ns):
        if (_ns:=sorted(ns, reverse=True)) and not (_ns[0] <= 靶值 and all(n in s for n in _ns)):
            return
        sz4us = len(us)
        sz4ns = len(ns)
        for 次大数, 溟次 in 简并记录.次大数讠溟次.items():
            内点 = (靶值 -次大数) >> 溟次
            777;ls = [内点<<ez for ez in range(1, 1+溟次)]
            777;s = {次大数, *ls}

            777;b = not 内点 in ns
            if b:ns.add(内点)
            #次序不可颠倒<<== 可能[内点==次大数]
            777;delta = {n for n in s if n in ns}
            #777;delta = s & ns
            ns -= delta
            if ls:us += ls
            try:
                777;yield from _f1(次大数)
            except:
                777;0b00001 and print_err(靶值, 次大数, 溟次, 内点, b, delta, ns, us)
                    #5 1 2 1 True {1} {3} [11, 6, 5, 2, 4, 1]
                    #11 5 1 3 True set() {3} [11, 6, 5, 2, 4, 1]
                raise
            if ls:del us[-len(ls):]
            ns |= delta
            if b:ns.remove(内点)
            assert sz4ns == len(ns)
            assert sz4us == len(us)

    return _f1(靶值)
def _过滤乊内点集扌(靶值讠简并记录, 靶值, 内点集, /):
    it = 枚举冫最短加链乊内点集扌(靶值讠简并记录, 靶值, 内点集)
    最短加链 = next(it)
    最短加链位置讠下界 = 最短加链
    最短加链位置讠上界 = 最短加链
    最短加链牜左侧最小 = 最短加链
    最短加链牜左侧最大 = 最短加链
    反转后最短加链 = reverse_(最短加链)
    反转后最短加链牜右侧最小 = 反转后最短加链
    反转后最短加链牜右侧最大 = 反转后最短加链
    s = set(最短加链)
    for 最短加链 in it:
        s.update(最短加链)
        最短加链位置讠下界 = tuple(map(min, 最短加链位置讠下界, 最短加链))
        最短加链位置讠上界 = tuple(map(max, 最短加链位置讠上界, 最短加链))

        最短加链牜左侧最小 = min(最短加链牜左侧最小, 最短加链)
        最短加链牜左侧最大 = max(最短加链牜左侧最大, 最短加链)

        反转后最短加链 = reverse_(最短加链)
        反转后最短加链牜右侧最小 = min(反转后最短加链牜右侧最小, 反转后最短加链)
        反转后最短加链牜右侧最大 = max(反转后最短加链牜右侧最大, 反转后最短加链)
    最短加链牜右侧最小 = reverse_(反转后最短加链牜右侧最小)
    最短加链牜右侧最大 = reverse_(反转后最短加链牜右侧最大)

    下上界 = (最短加链位置讠下界, 最短加链位置讠上界)
    左右小大 = (最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大)
    简并集纟靶值乊内点集 = s
    return (简并集纟靶值乊内点集, 下上界, 左右小大)
def _转换集合扌(s, /):
    简并集纟靶值 = make_NonTouchRanges(sorted_ints_to_iter_nontouch_ranges(sorted(s)))
    return 简并集纟靶值
def _集合并扌(s, ss, /):
    s = set(s)
    s.union(*ss)
    简并集纟靶值 = _转换集合扌(s)
    return 简并集纟靶值
def _求冫下上界扌(靶值, lus, /):
    (下界, 上界) = lus[0]
    for (_下界, _上界) in lus:
        下界 = tuple(map(min, 下界, _下界))
        上界 = tuple(map(max, 上界, _上界))
    下界 += (靶值,)
    上界 += (靶值,)
    下上界 = (下界, 上界)
    return 下上界
def _求冫左右小大扌(靶值, lrs, /):
    (左侧最小, 左侧最大, 右侧最小, 右侧最大) = lrs[0]
    反转后右侧最小 = reverse_(右侧最小)
    反转后右侧最大 = reverse_(右侧最大)
    for (_左侧最小, _左侧最大, _右侧最小, _右侧最大) in lrs:
        _反转后右侧最小 = reverse_(_右侧最小)
        _反转后右侧最大 = reverse_(_右侧最大)

        左侧最小 = min(左侧最小, _左侧最小)
        左侧最大 = max(左侧最大, _左侧最大)

        反转后右侧最小 = min(反转后右侧最小, _反转后右侧最小)
        反转后右侧最大 = max(反转后右侧最大, _反转后右侧最大)
    #左侧最小 = 左侧最小.copy()
    #左侧最大 = 左侧最大.copy()
    右侧最小 = reverse_(反转后右侧最小)
    右侧最大 = reverse_(反转后右侧最大)
    左右小大 = (左侧最小, 左侧最大, 右侧最小, 右侧最大)
    return 左右小大








def _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, /):
    靶值 = len(靶值讠简并记录)
    assert 靶值 >= 2
    最小显链长纟靶值 = min(d:=靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈[靶值])
    ls = d[最小显链长纟靶值]
    次大数讠溟次 = {次大数:溟次 for (次大数,内点,溟次) in ls}
    return (最小显链长纟靶值, 次大数讠溟次)
def 后续更新冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊已有后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 简并记录纟当前靶值, 鬽最大靶值, /):
    当前靶值 = len(靶值讠简并记录)
    assert 当前靶值 >= 2
    assert 当前靶值 == 简并记录纟当前靶值.靶值, 当前靶值
    _mdu = 当前靶值<<1
    最大靶值 = _mdu if None is 鬽最大靶值 else min(_mdu, 鬽最大靶值)
    assert 2 <= 当前靶值 <= 最大靶值

    u2szmm2ls = 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
    #########
    d = u2szmm2ls.pop(当前靶值)
    for 显链长, ls in d.items():
        _显链长 = 1+显链长
        for (次大数,内点,溟次) in ls:
            _溟次 = 1+溟次
            _靶值 = 次大数 + (内点<<_溟次)
            if _靶值 <= 最大靶值:
                u2szmm2ls.setdefault(_靶值, {}).setdefault(_显链长, []).append((次大数,内点,_溟次))
    u2szmm2ls

    #########
    次大数 = 当前靶值
    _溟次 = 0
    _显链长 = 1+简并记录纟当前靶值.最小显链长
    for 内点 in 简并记录纟当前靶值.简并集.iter_ints():
        _靶值 = 次大数 + (内点<<_溟次)
        if _靶值 <= 最大靶值:
            u2szmm2ls.setdefault(_靶值, {}).setdefault(_显链长, []).append((次大数,内点,_溟次))
        else:
            break
    u2szmm2ls
    #########
    assert not 当前靶值 in 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
    assert ((1+当前靶值) in 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)  is  (not 鬽最大靶值 == 当前靶值), (鬽最大靶值, 当前靶值, sorted(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈), ((1+当前靶值) in 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈),  (not 鬽最大靶值 == 当前靶值))
    #########
    return None
def 初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, /, *, 鬽最大靶值):
    if not len(靶值讠简并记录):raise TypeError
    check_may_([check_int_ge, len(靶值讠简并记录)], 鬽最大靶值)

    当前靶值 = len(靶值讠简并记录)
    assert 当前靶值 >= 2
    _mdu = 当前靶值<<1
    最大靶值 = _mdu if None is 鬽最大靶值 else min(_mdu, 鬽最大靶值)
    assert 2 <= 当前靶值 <= 最大靶值

    u2szmm2ls = 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈 = {}
    it = enumerate(靶值讠简并记录)
    777;next(it)
    for 次大数, 简并记录纟次大数 in it:
        最小显链长纟次大数 = 简并记录纟次大数.最小显链长
        差距 = 当前靶值 -次大数
        溟次 = 0
        777;显链长 = 最小显链长纟次大数+1+溟次
        for 内点 in 简并记录纟次大数.简并集.iter_ints_(reverse=True):
            溟化值 = 内点 << 溟次
            欤更新溟次 = False
            while 溟化值 < 差距:
                欤更新溟次 = True
                溟次 += 1
                溟化值 <<= 1
            if 欤更新溟次:
                assert 溟化值 == 内点 << 溟次
                777;显链长 = 最小显链长纟次大数+1+溟次
            靶值 = 次大数 +溟化值
            assert 靶值 >= 当前靶值
            if 欤更新溟次:
                assert 次大数+(溟化值>>1) < 当前靶值
            if 靶值 <= 最大靶值:
                u2szmm2ls.setdefault(靶值, {}).setdefault(显链长, []).append((次大数,内点,溟次))
    u2szmm2ls

    assert min(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈) == 当前靶值
    return 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈

def 求冫后续简并记录纟递归婪溟链牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 鬽最大靶值, /):
    assert 靶值讠简并记录
    靶值 = len(靶值讠简并记录)
    if 靶值 == 1:
        assert not 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
        #.简并记录纟靶值 = 构造冫简并记录纟靶值一扌()
        #.return (简并记录纟靶值, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)
        return 构造冫简并记录纟靶值一扌()
    (最小显链长纟靶值, 次大数讠溟次) = _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)
    777;伪简并集纟靶值 = make_NonTouchRanges([(1, 1+靶值)])
    777;伪简并记录纟靶值 = _乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 伪简并集纟靶值.len_ints(), 次大数讠溟次, 伪简并集纟靶值, None, None, None, None, None, None)
    777;靶值讠简并记录.append(伪简并记录纟靶值)
    try:
        (简并集纟靶值, 下上界, 左右小大) = _过滤乊内点集扌(靶值讠简并记录, 靶值, ())
    finally:
        if not 靶值讠简并记录.pop() is 伪简并记录纟靶值:raise 000
    (最短加链位置讠下界, 最短加链位置讠上界) = 下上界
    (最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大) = 左右小大
    简并集纟靶值 = _转换集合扌(简并集纟靶值)
    #.777;0b00001 and print_err(靶值, 简并集纟靶值)
    简并记录纟靶值 = 乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 简并集纟靶值.len_ints(), 次大数讠溟次, 简并集纟靶值, 最短加链位置讠下界, 最短加链位置讠上界, 最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大)
    777;后续更新冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊已有后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 简并记录纟靶值, 鬽最大靶值)
    #.return (简并记录纟靶值, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)
    return 简并记录纟靶值

def 枚举冫后续简并记录纟递归婪溟链牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈=None, /, *, 鬽最大靶值):
    777;0b00001 and print_err('自底向上注册')
    if not (None is 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈 or 1 <= len(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)):raise TypeError

    if not len(靶值讠简并记录):raise TypeError
    check_may_([check_int_ge, len(靶值讠简并记录)], 鬽最大靶值)

    def nop(): pass
    def to_init_():
        nonlocal to_init_, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
        if None is 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈:
            if len(靶值讠简并记录) >= 2:
                靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈 = 初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, 鬽最大靶值=鬽最大靶值)
                777;to_init_ = nop
            else:
                assert not to_init_ is nop
                assert None is 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
                pass
        else:
            assert len(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)
            777;to_init_ = nop
    #end-def to_init_():
    if not 鬽最大靶值 is None and 鬽最大靶值 < len(靶值讠简并记录): return
    while 1:
        to_init_()
        简并记录 = 求冫后续简并记录纟递归婪溟链牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 鬽最大靶值)
        assert 简并记录.靶值 == len(靶值讠简并记录)
        靶值讠简并记录.append(简并记录)
        yield 简并记录
        if 简并记录.靶值 == 鬽最大靶值: return






__all__
from script.min_add_ver5__mixed_recursive_greedy_zpow_addition_chain import *
