#__all__:goto
r'''[[[
e script/蛮力搜索冫最短加链牜修剪搜索树.py
    deprecate...
        moving to:
            e ../../python3_src/seed/math/power/addition_chain/shortest/search.py

py -m script.蛮力搜索冫最短加链牜修剪搜索树
py -m nn_ns.app.debug_cmd   script.蛮力搜索冫最短加链牜修剪搜索树 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.蛮力搜索冫最短加链牜修剪搜索树:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd script.蛮力搜索冫最短加链牜修剪搜索树:_doctest__Fraction_from_2_13_ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'script.蛮力搜索冫最短加链牜修剪搜索树:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
view others/数学/最短加链/最短加链-论文-概览.txt
    view others/数学/最短加链/最短加链-论文-批量处理.txt
        ...有向无环图...
    view others/数学/最短加链/最短加链-论文-向量链.txt
        一些定义、修剪方法
    view others/数学/最短加链/最短加链--py_doc-www-杂录.txt
        一些定义、公式
come_from:居前代码:
    view script/搜索冫最短加链长度.py
        蛮力搜索
    view script/min_add_ver4__pseudo_addition_chain.py
        简并态:指导搜索
        首失败点:12509
            [[靶值:<-[1..<12509]] -> [显链长纟最短递归加链{靶值}==显链长纟最短加星链{靶值}==显链长纟最短加链{靶值}==显链长纟递归最短加链{靶值}]]
            [[靶值:=12509] -> [递归最短加链{靶值}不存在][显链长纟最短递归加链{靶值}==显链长纟最短加星链{靶值}<显链长纟最短加链{靶值}]]
]]
[[
view script/搜索冫最短加链长度.py
蛮力搜索+关键节点
[关键节点=[def]=(靶数/末尾节点/节点牜出度等于零|节点牜出度大于等于二)]
[加链牜关键节点版 :: (j2u/[关键节点]{严格递增},j2imay_k4dup_j_js8sum_pair/[(毝址引纟讫址牜重复,[讫址]{严格递增})],j2imay_k4dup_j_js8addend_pair/[(毝址引纟起址牜重复,[起址]{严格递增})])]
加性冗余:
  (x+y) 至多出现一次
    特例:x*2
    特例:x*3
    禁止:x*4
    禁止:(x+y)+(x+y)即x*2+y*2
      => 剩余义务贡献度
    禁止:(x+y+...), (x+y+...) 生成 不同关键节点
      =>互斥条款牜不再见

  [关键节点牜讫==sum(关键节点牜起...)+[可选]其中某个关键节点牜起*(1|2)]
要点/内部关键节点 至少出现 2次
  剩余义务贡献度:{2,1,0}
  剩余义务累计值:sum(内部关键节点*剩余义务贡献度{内部关键节点} for 内部关键节点 in 前缀)
  [剩余义务累计值 <= 靶数]
  !! 互斥条款牜不再见
  => 可进一步优化...
    简单点:将某次大批求和的所有加数孤立起来自成一格，每一格都得成为 关键节点，除去 末尾节点 外 都得 翻倍(新内部关键节点的义务)...
  两两相加，结果可能是:(关键节点|非关键节点)
    关键节点 需承担 更多义务(至少两倍)
    非关键节点 需符合 相加次序(连续性生成非关键节点 其加数 只能 越来越小 即 取大优先)
乘性冗余{浮于型格之上}:
  (a+b)*(c+d) vs (c+d)*(a+b)
  对于 精简 最终集合表达 有用，对于 搜索 无用
修剪方法 参考一下:
  view others/数学/最短加链/最短加链-论文-向量链.txt
    /sdcard/0my_files/book/math/addition_chains/'Addition chains, vector chains, and efficient computation(2021)(Edward G.Thurber).pdf'

[u:<-[1..]]:
  [ℓ(u)==最少加次纟(u)==减一长度纟最短加链纟(u)==-1+长度纟最短加链纟(u)==显链长纟最短加链纟(u)]

节点分类:义务参与次数:杈型
  *末点/叶点/靶点:总参与次数==义务参与次数==0
  *介点:总参与次数==义务参与次数==1
    摞点/累点/叠点/跳点/链点/接点/介点/毌点/申点/串点
  *叉点:总参与次数>=义务参与次数==2
节点分类:值:
  隐点:值==1#即:起点
  显点:值>=2#即:非起点
全局属性:
  靶值:<-[1..] #u
  首爻位纟靶值==x2:=floor_log2(靶值) #λ(u)
  阳爻数纟靶值==y2:=靶值.bit_count() #ν#ν2(u)
  试用显链长:<-[ceil_log2(靶值*阳爻数纟靶值/2**2.13)..=首爻位纟靶值+阳爻数纟靶值-1]
    显链长下界:[显链长>=ceil(log2(靶值)+log2(阳爻数纟靶值)-2.13)]
    猜想牜显链长下界:[显链长>=首爻位纟靶值+ceil_log2(阳爻数纟靶值)]
        成立于:[u:<-[1..=2**64]]
            旧结论:成立于:[u:<-[1..=327678]]
                [327678 == 2**18 +2**16 -2]
        成立于:[阳爻数纟靶值:<-[1..=16]]
        [u:<-[1..]]:
          [Knuth_Stolarsky_conjecture_at_(u) =[def]= [ℓ(u) >= λ(u) + ceil_log2(ν(u))]]
        [[m:<-[0..=3]] -> [u:<-[1..]] -> [ν(u) >= 2**m+1] -> [ℓ(u) >= λ(u) + m+1]]
          => [[u:<-[1..]] -> [ν(u)<-[1..=16]] -> [Knuth_Stolarsky_conjecture_at_(u)]]

        [[u:<-[1..=2**64]] -> [Knuth_Stolarsky_conjecture_at_(u)]]
        [[u:<-[1..]] -> [s(u) <= 5] -> [Knuth_Stolarsky_conjecture_at_(u)]]
            # [num_small_steps_(u) <= 5]


节点属性:
  全局属性
  值:<-[1..=靶值]
  虚设:前置节点列表::[节点] #or:左指链表{(长度,节点)} #or:鬽前一节点
  虚设:鬽前一节点::鬽 节点
    [鬽前一节点 := None if 节点.欤显性 else (节点as显节点).前一节点]
  址引:=len(前置节点列表)<=试用显链长
  欤显性:=[值>1]
  义务参与次数:<-[0..=2]
  剩余义务参与次数:<-[0..=义务参与次数]
  债务累计值/累计未来义务总值::uint
  *显点属性:
    虚设:小加点址引:uint #or:左指链表{(长度,节点)} #or:小加点
    虚设:大加点址引:uint #or:左指链表{(长度,节点)} #or:大加点
      [显点.值 := 前置节点列表[显点.小加点址引].值 + 前置节点列表[显点.大加点址引].值]
      [0 <= 显点.小加点址引 <= 显点.大加点址引 < 显点.址引 == 1+显点.前一节点.址引 == len(前置节点列表) <= 试用显链长]
    前一节点::节点
    小加点::节点
    大加点::节点
      [显点.址引 := 1+显点.前一节点.址引]
      [显点.小加点址引 == 显点.小加点..址引]
      [显点.大加点址引 == 显点.大加点..址引]



]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,蛮力搜索冫最短加链扌 =True :修剪牜极简 =10 =0 -乱序丷反序
(1, 2, 4, 8, 10)
(1, 2, 4, 6, 10)
(1, 2, 4, 5, 10)
(1, 2, 3, 5, 10)
]]
[[
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,蛮力搜索冫最短加链扌 =True :修剪牜极简 =20 =0 -乱序丷反序
(1, 2, 4, 8, 16, 20)
(1, 2, 4, 8, 12, 20)
(1, 2, 4, 8, 10, 20)
(1, 2, 4, 6, 10, 20)
(1, 2, 4, 5, 10, 20)
(1, 2, 3, 5, 10, 20)
]]
[[
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,蛮力搜索冫最短加链扌 =True :修剪牜极简 =100 =0 -乱序丷反序
    62行:
(1, 2, 4, 8, 16, 32, 64, 96, 100)
(1, 2, 4, 8, 16, 32, 64, 68, 100)
(1, 2, 4, 8, 16, 32, 48, 96, 100)
(1, 2, 4, 8, 16, 32, 48, 52, 100)
(1, 2, 4, 8, 16, 32, 48, 50, 100)
(1, 2, 4, 8, 16, 32, 36, 68, 100)
(1, 2, 4, 8, 16, 32, 36, 64, 100)
(1, 2, 4, 8, 16, 32, 34, 68, 100)
(1, 2, 4, 8, 16, 32, 34, 66, 100)
(1, 2, 4, 8, 16, 32, 34, 50, 100)
(1, 2, 4, 8, 16, 24, 48, 96, 100)
(1, 2, 4, 8, 16, 24, 48, 52, 100)
(1, 2, 4, 8, 16, 24, 48, 50, 100)
(1, 2, 4, 8, 16, 24, 26, 50, 100)
(1, 2, 4, 8, 16, 24, 25, 50, 100)
(1, 2, 4, 8, 16, 20, 40, 80, 100)
(1, 2, 4, 8, 16, 20, 40, 60, 100)
(1, 2, 4, 8, 16, 18, 34, 50, 100)
(1, 2, 4, 8, 16, 18, 32, 50, 100)
(1, 2, 4, 8, 16, 17, 34, 50, 100)
(1, 2, 4, 8, 16, 17, 33, 50, 100)
(1, 2, 4, 8, 16, 17, 25, 50, 100)
(1, 2, 4, 8, 12, 24, 48, 96, 100)
(1, 2, 4, 8, 12, 24, 48, 52, 100)
(1, 2, 4, 8, 12, 24, 48, 50, 100)
(1, 2, 4, 8, 12, 24, 26, 50, 100)
(1, 2, 4, 8, 12, 24, 25, 50, 100)
(1, 2, 4, 8, 12, 20, 40, 80, 100)
(1, 2, 4, 8, 12, 20, 40, 60, 100)
(1, 2, 4, 8, 12, 13, 25, 50, 100)
(1, 2, 4, 8, 10, 20, 40, 80, 100)
(1, 2, 4, 8, 10, 20, 40, 60, 100)
(1, 2, 4, 8, 10, 20, 40, 50, 100)
(1, 2, 4, 8, 10, 20, 30, 50, 100)
(1, 2, 4, 8, 9, 17, 25, 50, 100)
(1, 2, 4, 8, 9, 16, 25, 50, 100)
(1, 2, 4, 6, 12, 24, 48, 96, 100)
(1, 2, 4, 6, 12, 24, 48, 52, 100)
(1, 2, 4, 6, 12, 24, 48, 50, 100)
(1, 2, 4, 6, 12, 24, 26, 50, 100)
(1, 2, 4, 6, 12, 24, 25, 50, 100)
(1, 2, 4, 6, 12, 13, 25, 50, 100)
(1, 2, 4, 6, 10, 20, 40, 80, 100)
(1, 2, 4, 6, 10, 20, 40, 60, 100)
(1, 2, 4, 6, 10, 20, 40, 50, 100)
(1, 2, 4, 6, 10, 20, 30, 50, 100)
(1, 2, 4, 5, 10, 20, 40, 80, 100)
(1, 2, 4, 5, 10, 20, 40, 60, 100)
(1, 2, 4, 5, 10, 20, 40, 50, 100)
(1, 2, 4, 5, 10, 20, 30, 50, 100)
(1, 2, 4, 5, 10, 20, 25, 50, 100)
(1, 2, 4, 5, 10, 15, 25, 50, 100)
(1, 2, 3, 6, 12, 24, 48, 50, 100)
(1, 2, 3, 6, 12, 24, 26, 50, 100)
(1, 2, 3, 6, 12, 24, 25, 50, 100)
(1, 2, 3, 6, 12, 13, 25, 50, 100)
(1, 2, 3, 5, 10, 20, 40, 80, 100)
(1, 2, 3, 5, 10, 20, 40, 60, 100)
(1, 2, 3, 5, 10, 20, 40, 50, 100)
(1, 2, 3, 5, 10, 20, 30, 50, 100)
(1, 2, 3, 5, 10, 20, 25, 50, 100)
(1, 2, 3, 5, 10, 15, 25, 50, 100)
]]
[[
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,蛮力搜索冫最短加链扌 =True :修剪牜极简 =11 =0 -乱序丷反序
(1, 2, 4, 8, 10, 11)
(1, 2, 4, 8, 9, 11)
(1, 2, 4, 6, 10, 11)
(1, 2, 4, 6, 7, 11)
(1, 2, 4, 5, 10, 11)
(1, 2, 4, 5, 9, 11)
(1, 2, 4, 5, 7, 11)
(1, 2, 4, 5, 6, 11)
(1, 2, 3, 6, 9, 11)
(1, 2, 3, 6, 8, 11)
(1, 2, 3, 5, 10, 11)
(1, 2, 3, 5, 8, 11)
(1, 2, 3, 5, 6, 11)
(1, 2, 3, 4, 8, 11)
(1, 2, 3, 4, 7, 11)
]]
[[
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,蛮力搜索冫最短加链扌 =True :修剪牜极简 =11 =0 +乱序丷反序
    同上...
]]
[[
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,1:蛮力搜索冫最短加链扌 =True :修剪牜极简 =12509 =0 -乱序丷反序
^KeyboardInterrupt
    超过6分钟
]]
[[
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,1:蛮力搜索冫最短加链扌 =True :修剪牜极简 =12509 =0 +乱序丷反序
^KeyboardInterrupt
    超过6分钟
]]
[[
'-> (靶值数量, 列表纟最佳次数, 列表纟独占最佳的次数, (坏值数量,已知最小显链长的值的数目,未知最小显链长的值的数目), 列表纟真最优次数, 综合真最优次数) # 次序:(二进制拆分,窗式拆分,窗式拆分牜排除零值片段,窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略{初版牜毛病,原文版,去零版},连分数拆分牜二幂冃平方根策略)'
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   @_比较冫三种显链长上界算法扌  ='range(1,1001)'
初版:次序:(二进制拆分,窗式拆分,连分数拆分牜二幂冃平方根策略)
(1000, [407, 56, 990], [10, 0, 593])
++窗式拆分牜排除零值片段
(1000, [363, 56, 554, 939], [3, 0, 52, 339])
++窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略
(1000, [321, 56, 507, 984, 888], [0, 0, 16, 56, 0])
++列表纟真最优次数
(1000, [321, 56, 507, 984, 888], [0, 0, 16, 56, 0], (0, 1000, 0), [288, 56, 412, 864, 771], 880)
++f1()/cache@求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略扌-->求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜初版牜毛病扌-->_多版囗求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略扌
(1000, [321, 56, 507, 984, 888], [0, 0, 16, 56, 0], (0, 1000, 0), [288, 56, 412, 864, 771], 880)
++kw:ver@_多版囗求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略扌
++求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜原文版扌
(1000, [301, 56, 447, 999, 817], [0, 0, 1, 127, 0], (0, 1000, 0), [288, 56, 412, 951, 771], 952)
    #唯一被反超:(484, [12, 16, 11, 12, 12], 11)
    #   还是存在 不如 排除零值片段 的 可能性，why！？
    #   发现:{排除零值片段}版 可能的 bug:最低位零值片段 是否 应该排除？
                #答:应该排除，不是bug
    发现:原文版的具现版有毛病:bug__small_fragment_at_LSB:
++求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜去零版扌
(1000, [301, 56, 447, 999, 998, 817], [0, 0, 1, 1, 0, 0], (0, 1000, 0), [288, 56, 412, 951, 950, 771], 952)
    #bug__small_fragment_at_LSB

++fixed:bug__small_fragment_at_LSB
(1000, [303, 56, 447, 1000, 1000, 819], [0, 0, 0, 0, 0, 0], (0, 1000, 0), [288, 56, 412, 950, 950, 771], 950)

===
初版:连分数拆分牜二幂冃平方根策略 > 二进制拆分 > 窗式拆分
    ？？？窗式拆分 包含 二进制拆分，怎么会 不如？
    因为 没有 排除 片段0
    ==>> ++窗式拆分牜排除零值片段

===
？？？初版牜毛病:窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略 怎么会可能不如 窗式拆分牜排除零值片段
    ===
    Exception: (30, 7, 6)
    [u==30]:
        7:窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略
        6:窗式拆分牜排除零值片段
    ===
    因为 人为边界，导致 没有 排除零值片段
        再仔细一想，发现 原文版 有毛病
          原文版:直接求加靶链:cf_chain__many_(靶集:=({N}\-/τ(N)), γ_:=σ) #使用:γ_{dichotomic_strategy}
            原文版 确实如此，但感觉不太对
              我认为应该是 直接求 窗式拆分框架x制表{加靶链{二进制切分片段序列.奇数部}}
              TODO:窗式拆分牜排除零值片段辻制表牜加靶链优化牜连分数拆分牜二幂冃平方根策略
    ===
    发现初版有毛病:
    ++原文版:求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜原文版扌
    ===
    发现:原文版的具现版有毛病:bug__small_fragment_at_LSB:
]]
[[
构造冫加靶链牜加辗链构造式扌
$ szmm4shortest_addition_chain 484
    [ℓ(484) == 11]
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   @构造冫加靶链牜加辗链构造式扌  --策略名纟连分数拆分:二幂冃平方根策略  ='[484]'
    (1, 2, 4, 8, 12, 24, 28, 30, 60, 120, 240, 480, 484)
        #[链长==13][显链长==12]
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   @构造冫加靶链牜加辗链构造式扌  --策略名纟连分数拆分:窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略  ='[484]'
    (1, 2, 3, 6, 12, 15, 30, 60, 120, 240, 242, 484)
        #[链长==12][显链长==11]
    #bug__small_fragment_at_LSB:
        (1, 2, 3, 6, 7, 14, 15, 30, 60, 120, 121, 242, 484)
            #[链长==13][显链长==12]

===
view others/数学/最短加链/最短加链--py_doc-www-杂录.txt
    [191==min{u | [u:<-[1..]][ℓ(2*u) == ℓ(u)]}]
    [171==min{u | [u:<-[1..]][ℓ(3*u) == ℓ(u)]}]
    [3277==min{u | [u:<-[1..]][ℓ(5*u) == ℓ(u)]}]
    [2731==min{u | [u:<-[1..]][ℓ(6*u) == ℓ(u)]}]
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,枚举冫靶值集辻加靶链牜加辗链构造式扌  +欤添加显链长 --策略名纟连分数拆分:窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略  ='[191, 2*191, 171, 3*171, 3277, 5*3277, 2731, 6*2731]'
(191, 11, (1, 2, 3, 6, 9, 11, 22, 44, 47, 94, 188, 191))
(382, 11, (1, 2, 4, 5, 9, 14, 23, 46, 92, 184, 368, 382))
(171, 10, (1, 2, 3, 5, 10, 20, 40, 42, 84, 168, 171))
(513, 10, (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 513))
(3277, 15, (1, 2, 3, 6, 12, 24, 48, 51, 102, 204, 408, 816, 819, 1638, 3276, 3277))
(16385, 15, (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 16385))
(2731, 15, (1, 2, 3, 5, 10, 20, 40, 42, 84, 168, 336, 341, 682, 1364, 2728, 2731))
(16386, 15, (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 8193, 16386))
===
py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   ,枚举冫靶值集辻加靶链牜加辗链构造式扌 +欤添加显链长  --策略名纟连分数拆分:窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略  ='range(1,1+200)'
    结果见:
        view ../../python3_src/seed/math/power/addition_chain/short/cf_chain.py
===
]]



[[
TODO:不仅 lb/假想上界 逐步递增，而且 加贪链宽度 也逐步递增
    泛化{加星链}: [加辗链 <: 加星链==加贪链{宽度<=1} <: 加链]
    [u:=靶值][lb:=假想上界{u}][us:<-加链{u}{len=lb}]:
        [k:<-[1..=lb]]:
            [单步加贪链宽度{u,lb;us;k} =[def]= min{(k-j) | [[j:<-[0..<k]][i:<-[0..=j]][us[k] == us[j]+us[i]]]}]
        [加贪链宽度{u,lb;us} =[def]= min[单步加贪链宽度{u,lb;us;k} | [k:<-[1..=lb]]]]
            刚性:至少一次 达到 加贪链宽度
            若当前 前缀纟加链 尚未 达到 加贪链宽度:
                则 单点下界估值@k:
                    *[k>=加贪链宽度]:
                        [us[k] >= 2*us[k-加贪链宽度]]
                    ?t :=> [t:<-[max(0,加贪链宽度-k)..=lb-k]][us[k+t] <= 2*us[k+t-加贪链宽度]]
                    [u == us[lb]
                    <= 2**(lb-(k+t)+1)*us[t-(加贪链宽度-k)]
                    * [t>=加贪链宽度]:
                        ... <= 2**(lb-(k+t)+1) * 2**(t-加贪链宽度)*us[k]
                            == 2**(lb+1-k-加贪链宽度)*us[k]
                    ]
                    * [加贪链宽度<=t<=lb-k]:
                        [u[k] >= u/2**(lb+1-k-加贪链宽度)]
                    * [max(0,加贪链宽度-k)<=t<加贪链宽度]:
                        [us[k-(加贪链宽度-t)] >= u/2**(lb+1-k-t) == 2**-(加贪链宽度-t) * u/2**(lb+1-k-加贪链宽度)]
                    ?t :=> [[t:<-[max(0,加贪链宽度-k)..=min(加贪链宽度,lb-k)]][us[k-(加贪链宽度-t)] >= 2**-(加贪链宽度-t) * u/2**(lb+1-k-加贪链宽度)]]
                        这么看，似乎还可以 泛化 加贪链宽度 成 尾部刚需加贪链宽度降序统计:降序:[(加贪链宽度,出现次数)] 只有 大的 加贪链宽度 耗尽，才会 考虑使用 小的 加贪链宽度，而 大的 加贪链宽度 之间 出现的 小的 加贪链宽度 不予考虑。
                            (k-j) => 还可考虑 (j-i)
    泛化:
        首差统计:完全统计:{k-j:count}
        次差统计:完全统计:{j-i:count}
        [sum count == 加次 == 显链长]
        估值冫上下限纟靶值纟加链{显链长;首差统计{显链长},次差统计{显链长}}
            这是 稀疏范围 只能 估计 下限
            能不能 部分稠密范围？
                要是某些值被涵盖 => 该值显链长上界 进而 裁剪

跨度间放大系数越大则本次加法放大系数越小
    假设 翻倍型步数 足够多 则 其他 非翻倍型步 可以 互不交叠，此时靶值最小
    II max(1,(2**(1-首差)+2**(1-首差-次差)))
        不行！非严序
    只有 尾部刚需加贪链宽度降序统计 才容易估值
    改名:尾部刚需首差降序统计

加链==严序加链『<』
    允许非末点出度为零 以 允许多靶值
    xx:非末点出度不为零
松序加链 『<=』
散漫加链 无序 允许下溢加零
mkdir ../../python3_src/seed/math/power/
mkdir ../../python3_src/seed/math/power/addition_chain/
mkdir ../../python3_src/seed/math/power/addition_chain/short/
mkdir ../../python3_src/seed/math/power/addition_chain/shortest/
mkdir ../../python3_src/seed/math/power/addition_chain/common/
e ../../python3_src/seed/math/power/addition_chain/common/README-defs.txt
]]


py_adhoc_call   script.蛮力搜索冫最短加链牜修剪搜索树   @_test__divisor7dichotomic_strategy_
from script.蛮力搜索冫最短加链牜修剪搜索树 import *
]]]'''#'''
__all__ = r'''
蛮力搜索冫最短加链扌
蛮力搜索冫加链扌

魖回溯型蛮力搜索最短加链
    魖回溯型蛮力搜索最短加链牜初始化基础参数
    魖回溯型蛮力搜索最短加链牜初始化搜索结果为鬽最短加链
    魖回溯型蛮力搜索最短加链牜修剪
        魖回溯型蛮力搜索最短加链牜修剪牜极简
            乸回溯型蛮力搜索最短加链牜修剪牜极简

求冫显链长上界牜连分数拆分牜二幂冃平方根策略扌
    divisor7dichotomic_strategy_
求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜初版牜毛病扌
求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜原文版扌
求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜去零版扌

乸杈型
乸全局属性弱
乸全局属性













检查冫严序加链乊靶值扌
    检查冫严序加链扌
        检查冫严序加链内容扌
魖加辗链构造式
    乸加辗链串接式
    乸加辗链附尾式
    乸加辗链础链式
        加辗链构造式牜幺
构造冫加链牜二进制拆分扌
构造冫加辗链构造式冃加靶链扌
    取造冫加辗链构造式扌
        规范化冫候选分母集扌
    匴策略纟连分数拆分
        构造冫加靶链牜加辗链构造式扌
        枚举冫靶值集辻加靶链牜加辗链构造式扌

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

#.#################################
from seed.math.power.addition_chain.short.cf_chain import (
魖加辗链构造式
,    乸加辗链串接式
,    乸加辗链附尾式
,    乸加辗链础链式
,        加辗链构造式牜幺
,构造冫加链牜二进制拆分扌
,构造冫加辗链构造式冃加靶链扌
,    取造冫加辗链构造式扌
,        规范化冫候选分母集扌
,    匴策略纟连分数拆分
,        构造冫加靶链牜加辗链构造式扌
,        枚举冫靶值集辻加靶链牜加辗链构造式扌
)
if 1:
    from seed.math.power.addition_chain.short.cf_chain import divisor7dichotomic_strategy_, _test__divisor7dichotomic_strategy_
    from seed.math.power.addition_chain.short.cf_chain import _初版牜毛病mk_us_, _原文版mk_us_, _去零版mk_us_
#.#################################

from enum import Enum
from functools import cached_property, cache
from fractions import Fraction

from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_int_ge_le
from seed.tiny_.check import check_non_ABC
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC

#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.debug.print_err import print_err
    from seed.math.floor_ceil import floor_log2, ceil_log2
    from math import log2, nextafter
    from math import ceil
    from bisect import bisect_right
    from itertools import pairwise#islice
    from seed.math.power.addition_chain.common.check import 检查冫严序加链乊靶值扌, 检查冫严序加链扌, 检查冫严序加链内容扌
    #from seed.for_libs.for_heapq import Heap
#.    from seed.iters.flatten_recur import flatten_recur
#.    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.    from seed.func_tools.dot_ import dot_


#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0
#.from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
#.
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

def 蛮力搜索冫最短加链扌(欤花哨, tag, /, *args, **kwds):
    '-> Iter 最短加链'
    nm = f'乸回溯型蛮力搜索最短加链牜{tag!s}' #修剪牜极简
    cls = globals()[nm]
    obj = cls(*args, **kwds)
    g = 乸全局属性弱(欤花哨, obj.靶值)
    #.print_err((g.显链长下界, obj.下界冃上界纟显链长纟靶值))
    显链长下界 = max(g.显链长下界, obj.下界冃上界纟显链长纟靶值)
    显链长上界 = g.显链长上界
    for 下界冃上界纟显链长纟靶值 in range(显链长下界, 1+显链长上界):
        obj = obj.再造牜更改冫下界冃上界纟显链长纟靶值扌(下界冃上界纟显链长纟靶值)
        #.print_err((显链长下界, 下界冃上界纟显链长纟靶值, obj.下界冃上界纟显链长纟靶值))
        #.print_err('lb =', obj.下界冃上界纟显链长纟靶值)
        it = iter(obj.枚举冫加链扌())
        for 加链 in it:
            yield 加链
            break
        else:
            #未发现:加链
            #加大:显链长
            continue
        break
    yield from it
    return
def 蛮力搜索冫加链扌(tag, /, *args, **kwds):
    '-> Iter 加链'
    nm = f'乸回溯型蛮力搜索最短加链牜{tag!s}' #修剪牜极简
    cls = globals()[nm]
    obj = cls(*args, **kwds)
    return obj.枚举冫加链扌()
    return obj.搜索扌()

class 魖回溯型蛮力搜索最短加链(ABC):
    __slots__ = ()
    @abstractmethod
    def 再造牜更改冫下界冃上界纟显链长纟靶值扌(sf, 下界冃上界纟显链长纟靶值, /):
        '-> __class__'
    @property
    @abstractmethod
    def 乱序丷反序(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def 靶值(sf, /):
        '-> u/uint{>=1}'
    @property
    @abstractmethod
    def 下界冃上界纟显链长纟靶值(sf, /):
        '-> lb/uint'
    @abstractmethod
    def 乊发现冫加链扌(sf, 加链, /):
        '-> b_stop/bool'
        return True
    @abstractmethod
    def 欤停止搜索扌(sf, /):
        '-> b_stop/bool # 用作 暂停降温点、提前结束点'
        return False
    @abstractmethod
    def 欤已搜索过扌(sf, to_set_searched, /):
        'to_set_searched/bool -> b_searched/bool # 读写'
    @property
    @abstractmethod
    def 搜索结果(sf, /):
        '([b_searched] =>) -> 搜索结果 #只读 # 必须在 搜索扌()之后'
    @abstractmethod
    def 构造冫后一状态扌(sf, 状态栈, 前缀纟加链, /):
        '-> 状态'
    @abstractmethod
    def 求取冫鬽丮下一个状态辻后一个值厈扌(sf, 状态栈, 前缀纟加链, 状态, /):
        '-> may (下一个状态, 后一个值/uint) # 注：搜索扌()内含缓存用于去除重复的 后一个值'

    def 搜索扌(sf, /):
        '-> 搜索结果'
        #####################
        if sf.欤已搜索过扌(False):
            return sf.搜索结果
        sf.欤已搜索过扌(True)
        if not sf.欤已搜索过扌(False): raise Exception
        #####################
        for 加链 in sf.枚举冫加链扌():
            b_stop = sf.乊发现冫加链扌(加链)
            if b_stop: break
        return sf.搜索扌()
    def 枚举冫加链扌(sf, /):
        '-> Iter 加链'
        #####################
        状态栈 = []
        后值集栈 = []
        前缀纟加链 = [1]
            # 新节点已加入
        #####################
        while not (b_stop := sf.欤停止搜索扌()):
            assert 1+len(状态栈) == len(前缀纟加链)
            assert len(状态栈) == len(后值集栈)
            # 新节点已加入
            if 前缀纟加链[-1] == sf.靶值:
                #达成靶值
                加链 = tuple(前缀纟加链)
                yield 加链
                del 加链
                #不深入
                pass
            elif -1+len(前缀纟加链) == sf.下界冃上界纟显链长纟靶值:
                #不深入
                pass
            else:
                # 深入:后一个节点
                st = sf.构造冫后一状态扌(状态栈, 前缀纟加链)
                状态栈.append(st)
                后值集栈.append(set())
                前缀纟加链.append(None)
                # 虚拟旧节点已加入

            # 不深入:更换为下一个值
            while 状态栈:
                前缀纟加链.pop()
                vs = 后值集栈.pop()
                st = 状态栈.pop()
                    # !! export 前缀纟加链,状态栈 to outer method:求取冫鬽丮下一个状态辻后一个值厈扌
                    # => .pop() instead .[-1]
                while not None is (m := sf.求取冫鬽丮下一个状态辻后一个值厈扌(状态栈, 前缀纟加链, st)):
                    (_st, v) = m
                    b_drop = False
                    b_drop = b_drop or v <= 前缀纟加链[-1]
                        # drop small v
                        #if 乱序丷反序:
                    b_drop = b_drop or v in vs
                        # drop old v
                    if b_drop:
                        # drop v
                        st = _st
                        continue
                    else:
                        # new v
                        vs.add(v)
                        break
                else:
                    # [m is None]
                    # no new v
                    #回溯
                    continue
                # new v
                break
            else:
                #退出
                break
            # new v
            #(_st, v) = m
            状态栈.append(_st)
            后值集栈.append(vs)
            前缀纟加链.append(v)
            # 新节点已加入
        #end-while
        return
        return sf.搜索结果
    #end-def 枚举冫加链扌(sf, /):
#end-class 魖回溯型蛮力搜索最短加链(ABC):
class 魖回溯型蛮力搜索最短加链牜初始化基础参数(魖回溯型蛮力搜索最短加链):
    ___no_slots_ok___ = True
    def __init__(sf, 靶值, 下界冃上界纟显链长纟靶值, /, 乱序丷反序):
    #.def __init__(sf, 欤花哨, 靶值, 下界冃上界纟显链长纟靶值, /):
        #.check_type_is(bool, 欤花哨)
        check_type_is(bool, 乱序丷反序)
        check_int_ge(1, 靶值)
        check_int_ge(0, 下界冃上界纟显链长纟靶值)
        #.sf._g = 乸全局属性弱(欤花哨, 靶值)
        #.sf._fancy = 欤花哨
        sf._reverse = 乱序丷反序
        sf._u = 靶值
        sf._lb = 下界冃上界纟显链长纟靶值
        sf._done = False
    @override
    def 再造牜更改冫下界冃上界纟显链长纟靶值扌(sf, 下界冃上界纟显链长纟靶值, /):
        '-> __class__'
        #.return type(sf)(sf.欤花哨, sf.靶值, sf.下界冃上界纟显链长纟靶值)
        #bug:return type(sf)(sf.靶值, sf.下界冃上界纟显链长纟靶值)
        return type(sf)(sf.靶值, 下界冃上界纟显链长纟靶值, 乱序丷反序=sf.乱序丷反序)
    #.@property
    #.@override
    #.def 欤花哨(sf, /):
    #.    '-> bool'
    #.    return sf._fancy
    @property
    @override
    def 乱序丷反序(sf, /):
        '-> bool'
        return sf._reverse
    @property
    @override
    def 靶值(sf, /):
        '-> u/uint{>=1}'
        return sf._u
    @property
    @override
    def 下界冃上界纟显链长纟靶值(sf, /):
        '-> lb/uint'
        return sf._lb
    @override
    def 欤已搜索过扌(sf, to_set_searched, /):
        'to_set_searched/bool -> b_searched/bool # 读写'
        #match emay_True:
            #case ...:
                # SyntaxError: invalid syntax
        match to_set_searched:
            case False:
                pass
            case True:
                sf._done = True
            case _:
                raise TypeError
        return sf._done
#end-class 魖回溯型蛮力搜索最短加链牜初始化基础参数(魖回溯型蛮力搜索最短加链):
class 魖回溯型蛮力搜索最短加链牜初始化搜索结果为鬽最短加链(魖回溯型蛮力搜索最短加链):
    ___no_slots_ok___ = True
    def __init__(sf, /):
        sf._may_us = None
    @property
    def 鬽最短加链(sf, /):
        '-> may 最短加链 # 必须在搜索过后'
        return sf._may_us
    @property
    @override
    def 搜索结果(sf, /):
        '([b_searched] =>) -> 搜索结果 #只读 # 必须在 搜索扌()之后'
        if not sf.欤已搜索过扌(False):raise TypeError
        return sf.鬽最短加链
    @override
    def 乊发现冫加链扌(sf, 加链, /):
        '-> b_stop/bool'
        sf._may_us = 加链
        return True
    @override
    def 欤停止搜索扌(sf, /):
        '-> b_stop/bool # 用作 暂停降温点、提前结束点'
        return False
#end-class 魖回溯型蛮力搜索最短加链牜初始化搜索结果为鬽最短加链(魖回溯型蛮力搜索最短加链):

class 魖回溯型蛮力搜索最短加链牜修剪(魖回溯型蛮力搜索最短加链):
    ___no_slots_ok___ = True
    @abstractmethod
    def 求取冫下界纟后一个值扌(sf, 前缀纟加链, /):
        '-> 下界{后一个值}/low/uint'
    @abstractmethod
    def 欤修剪掉牜仅等于扌(sf, 前缀纟加链, 后一个值, /):
        '-> bool'
    @override
    def 构造冫后一状态扌(sf, 状态栈, 前缀纟加链, /):
        '-> 状态'
        st0 = sf._乊乱序囗构造冫后一状态扌(状态栈, 前缀纟加链)
        if not sf.乱序丷反序:
            #乱序
            return st0
        else:
            #反序
            ls = [st0]
            vs = set()
            while not None is (m := sf._乊乱序囗求取冫鬽丮下一个状态辻后一个值厈扌(状态栈, 前缀纟加链, ls[-1])):
                (_st, v) = m
                ls.append(_st)
                vs.add(v)
            vs = sorted(vs)
            return (len(vs), vs)

            ...
    @override
    def 求取冫鬽丮下一个状态辻后一个值厈扌(sf, 状态栈, 前缀纟加链, 状态, /):
        '-> may (下一个状态, 后一个值/uint) # 注：搜索扌()内含缓存用于去除重复的 后一个值'
        if not sf.乱序丷反序:
            #乱序
            return sf._乊乱序囗求取冫鬽丮下一个状态辻后一个值厈扌(状态栈, 前缀纟加链, 状态)
        else:
            #反序
            (j, vs) = 状态
            if not j:
                return None
            j -= 1
            st = (j, vs)
            v = vs[j]
            return (st, v)
    def _乊乱序囗构造冫后一状态扌(sf, 状态栈, 前缀纟加链, /):
        '-> 状态'
        low = sf.求取冫下界纟后一个值扌(前缀纟加链)
        low = max(low, 1+前缀纟加链[-1])
        j = k = len(前缀纟加链) -1
        st = (j, k, low)
        return st
    def _乊乱序囗求取冫鬽丮下一个状态辻后一个值厈扌(sf, 状态栈, 前缀纟加链, 状态, /):
        '-> may (下一个状态, 后一个值/uint) # 注：搜索扌()内含缓存用于去除重复的 后一个值'
        st = 状态
        #print_err(st)
        (j, k, low) = st
        # [j >= k >= -1]
        while 1:
            # [j >= k >= -1]
            assert j >= k >= -1, (j, k)
            #print_err(st, (j, k))
            if k == -1:
                if j == -1:return None
                # [j > -1 == k]
                j = k = j-1
                # [j >= k >= -1]
                continue
            v = 前缀纟加链[j] + 前缀纟加链[k]
            if not v >= low:
                if k == j: return None
                j = k = j-1
                continue
            if sf.欤修剪掉牜仅等于扌(前缀纟加链, v):
                k -= 1
                continue
            break
        v
        _st = (j, k-1, low)
        return (_st, v)
class 魖回溯型蛮力搜索最短加链牜修剪牜极简(魖回溯型蛮力搜索最短加链牜修剪):
    ___no_slots_ok___ = True
    def __init__(sf, /):
        u = sf.靶值
        lb = sf.下界冃上界纟显链长纟靶值
        sf._j2low = [1+(u-1)//2**(lb-j) for j in range(1+lb)]

    @override
    def 求取冫下界纟后一个值扌(sf, 前缀纟加链, /):
        '-> 下界{后一个值}/low/uint'
        j = len(前缀纟加链)
        return sf._j2low[j]
        #.try:
        #.    return sf._j2low[j]
        #.except IndexError:
        #.    err = (sf.下界冃上界纟显链长纟靶值, len(sf._j2low), j, 前缀纟加链)
        #.    print_err(err)
        #.    raise IndexError(err)
    @override
    def 欤修剪掉牜仅等于扌(sf, 前缀纟加链, 后一个值, /):
        '-> bool'
        return False

class 乸回溯型蛮力搜索最短加链牜修剪牜极简(魖回溯型蛮力搜索最短加链牜修剪牜极简, 魖回溯型蛮力搜索最短加链牜初始化搜索结果为鬽最短加链, 魖回溯型蛮力搜索最短加链牜初始化基础参数):
    def __init__(sf, 靶值, 下界冃上界纟显链长纟靶值, /, **kwds):
    #.def __init__(sf, 欤花哨, 靶值, 下界冃上界纟显链长纟靶值, /):
        #.魖回溯型蛮力搜索最短加链牜初始化基础参数.__init__(sf, 欤花哨, 靶值, 下界冃上界纟显链长纟靶值)
        魖回溯型蛮力搜索最短加链牜初始化基础参数.__init__(sf, 靶值, 下界冃上界纟显链长纟靶值, **kwds)
        魖回溯型蛮力搜索最短加链牜初始化搜索结果为鬽最短加链.__init__(sf)
        魖回溯型蛮力搜索最短加链牜修剪牜极简.__init__(sf)

check_non_ABC(乸回溯型蛮力搜索最短加链牜修剪牜极简)
#raise

class 乸杈型(Enum):
    '杈型'
    末点 = 0
    介点 = 1
    叉点 = 2
    @property
    def 义务参与次数(sf, /):
        return sf.value
    @cached_property
    def 欤末点(sf, /):
        return sf is  __class__.末点
    @cached_property
    def 欤介点(sf, /):
        return sf is  __class__.介点
    @cached_property
    def 欤叉点(sf, /):
        return sf is  __class__.叉点

class _doctest__Fraction_from_2_13_:
    r'''[[[
>>> 1/2**2.13
0.22845786255735015
>>> (1/2**2.13).as_integer_ratio()
(8231061957465137, 36028797018963968)

>>> nextafter(2**2.13, 9.0).as_integer_ratio()
(1232065176307937, 281474976710656)
>>> 281474976710656/1232065176307937
0.22845786255735012

>>> nextafter(1/2**2.13, -1.0).as_integer_ratio()
(514441372341571, 2251799813685248)
>>> 514441372341571/2251799813685248
0.22845786255735012





>>> _fr = Fraction(*(1/2**2.13).as_integer_ratio())
>>> _fr
Fraction(8231061957465137, 36028797018963968)
>>> (1/_fr)**100 > 2**213
False
>>> _fr00 = _fr


>>> _fr = 1/Fraction(*(2**2.13).as_integer_ratio())
>>> _fr
Fraction(1125899906842624, 4928260705231747)
>>> (1/_fr)**100 > 2**213
False
>>> _fr10 = _fr

>>> _fr = Fraction(*nextafter(1/2**2.13, -1.0).as_integer_ratio())
>>> _fr
Fraction(514441372341571, 2251799813685248)
>>> (1/_fr)**100 > 2**213
True
>>> _fr01 = _fr

>>> _fr = 1/Fraction(*nextafter(2**2.13, 9.0).as_integer_ratio())
>>> _fr
Fraction(281474976710656, 1232065176307937)
>>> (1/_fr)**100 > 2**213
True
>>> _fr11 = _fr

>>> _fr10 > _fr00 > _fr01 > _fr11
True

_fr10 > _fr00 太大，无效
_fr01 > _fr11 有效，选最大:_fr01
>>> fr01
Fraction(514441372341571, 2251799813685248)
>>> x = 1/_fr01**100
>>> ceil(x).bit_length()
214
>>> hex(ceil(x)).upper()
'0X200000000000333439D1CD2A088ABFC7D04F437622E6B55DC1381E'

>>> x = 1/_fr11**100
>>> ceil(x).bit_length()
214
>>> hex(ceil(x)).upper()
'0X20000000000069B6BEC6B57D3DBA2A7621B7D55915E0C680E6F54C'

>>> x = 1/_fr10**100
>>> ceil(x).bit_length()
213
>>> hex(ceil(x)).upper()
'0X1FFFFFFFFFFFB2F29331172EBDC5AC8CDA8C7E1416799141C26E1E'

>>> x = 1/_fr00**100
>>> ceil(x).bit_length()
213
>>> hex(ceil(x)).upper()
'0X1FFFFFFFFFFFC5C64E9E73CC1F484F1573D89D90628988BA48480E'

    #]]]'''#'''
_fr = Fraction(*nextafter(1/2**2.13, -1.0).as_integer_ratio())
assert _fr == Fraction(514441372341571, 2251799813685248)

class 乸全局属性弱:
    '全局属性弱'
    #__slots__ = '_u _lb _x2 _y2'
    r'''[[[
    view others/数学/最短加链/次优加链-论文-连分数-批量处理.txt
      重要界限公式:
        [[u:<-[1..]] -> [ℓ(u) >= log2(u) +log2(ν(u)) -2.13]]
        [[u:<-[1..]] -> [ℓ(u) <= (λ(u) +ν(u) -1)]]
        #窗式拆分:
        简版:[[u:<-[1..]] -> [k:<-[1..]] -> [ℓ(u) <= λ(u)+1-k +λ(u)//k +(2**(k-1))]]

    view others/数学/最短加链/最短加链-论文-向量链.txt
        [u:<-[1..]]:
          [Knuth_Stolarsky_conjecture_at_(u) =[def]= [ℓ(u) >= λ(u) + ceil_log2(ν(u))]]
        [[u:<-[1..=2**64]] -> [Knuth_Stolarsky_conjecture_at_(u)]]
        [[m:<-[0..=3]] -> [u:<-[1..]] -> [ν(u) >= 2**m+1] -> [ℓ(u) >= λ(u) + m+1]]
          => [[u:<-[1..]] -> [ν(u)<-[1..=16]] -> [Knuth_Stolarsky_conjecture_at_(u)]]

    #]]]'''#'''
    def __init__(sf, 欤花哨, 靶值, /):
        check_type_is(bool, 欤花哨)
        check_int_ge(1, 靶值)
        sf._u = 靶值
        sf._fancy = 欤花哨
    @property
    def 欤花哨(sf, /):
        return sf._fancy
    @property
    def 靶值(sf, /):
        return sf._u
    @cached_property
    def 首爻位纟靶值(sf, /):
        return floor_log2(sf.靶值) #λ(u)
    @cached_property
    def 阳爻数纟靶值(sf, /):
        return sf.靶值.bit_count() #ν#ν2(u)
    assert 0x1_0000_0000_0000_0000 == 2**64
    @cached_property
    def 显链长下界(sf, /):
        #.return ceil_log2(ceil(sf.靶值*sf.阳爻数纟靶值*_fr))
        #.return ceil_log2(sf.靶值*sf.阳爻数纟靶值/2**2.13)
        #.return ceil(log2(sf.靶值*sf.阳爻数纟靶值) -2.13)
        显链长下界牜通用版 = ceil_log2(ceil(sf.靶值*sf.阳爻数纟靶值*_fr))
        if sf.欤花哨 and (sf.靶值 <= 0x1_0000_0000_0000_0000 or sf.阳爻数纟靶值 <= 16):
            # 可应用:
            # 猜想牜显链长下界:[显链长>=首爻位纟靶值+ceil_log2(阳爻数纟靶值)]
            #     成立于:[u:<-[1..=2**64]]
            #     成立于:[阳爻数纟靶值:<-[1..=16]]
            显链长下界牜花哨版 = sf.首爻位纟靶值+ceil_log2(sf.阳爻数纟靶值)
        elif sf.欤花哨:
            显链长下界牜花哨版 = sf.首爻位纟靶值+min(4, ceil_log2(sf.阳爻数纟靶值))
        else:
            显链长下界牜花哨版 = 0
        显链长下界 = max(显链长下界牜花哨版, 显链长下界牜通用版)
        return 显链长下界
    @cached_property
    def 显链长上界(sf, /):
        if sf.欤花哨 and sf.阳爻数纟靶值 > 3 and sf.显链长上界牜二进制拆分 > sf.显链长下界:
            #窗式拆分
            #连分数拆分牜二幂冃平方根策略
            显链长上界 = min(sf.显链长上界牜二进制拆分, sf.显链长上界牜窗式拆分, sf.显链长上界牜窗式拆分牜排除零值片段, sf.显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略, sf.显链长上界牜连分数拆分牜二幂冃平方根策略)
        else:
            显链长上界 = sf.显链长上界牜二进制拆分
        return 显链长上界

    @cached_property
    def 显链长上界牜二进制拆分(sf, /):
        #二进制拆分
        return sf.首爻位纟靶值+sf.阳爻数纟靶值-1
    @cached_property
    def 显链长上界牜窗式拆分(sf, /):
        #窗式拆分
        if sf.阳爻数纟靶值 <= 2:
            return sf.显链长上界牜二进制拆分
        (k, min_sz) = sf._扩展囗显链长上界牜窗式拆分
        return min_sz
    @cached_property
    def _扩展囗显链长上界牜窗式拆分(sf, /):
        assert sf.阳爻数纟靶值 > 2
        #[[u:<-[1..]] -> [k:<-[1..]] -> [ℓ(u) <= λ(u)+1-k +λ(u)//k +(2**(k-1))]]
        Au = sf.首爻位纟靶值
        assert Au >= 2
        min_sz = 2*Au
        for k in range(1, 1+Au):
            sz = (Au+1-k +Au//k + 2**(k-1))
            if sz < min_sz:
                min_sz = sz
            elif sz > min_sz:
                break
        else:
            raise 000
        return (k, min_sz)
    @cached_property
    def 显链长上界牜窗式拆分牜排除零值片段(sf, /):
        #窗式拆分
        if sf.阳爻数纟靶值 <= 2:
            return sf.显链长上界牜二进制拆分
        #[[u:<-[1..]] -> [k:<-[1..]] -> [ℓ(u) <= λ(u)+1-k +λ(u)//k +(2**(k-1))]]
        Au = sf.首爻位纟靶值
        assert Au >= 2
        min_sz = 2*Au
        (k, min_sz) = sf._扩展囗显链长上界牜窗式拆分
        max_k = min(Au, k+9)
        s = f'{sf.靶值:b}'
        for k in range(1, 1+max_k):
            sz = (Au+1-k +Au//k + 2**(k-1))
            零值片段数量 = sum(1 for j in range(0, len(s), k) if not '1' in s[j:j+k])
            #{排除零值片段}版 可能的 bug:最低位零值片段 是否 应该排除？
                #答:应该排除，不是bug
            sz -= 零值片段数量
            if sz < min_sz:
                min_sz = sz
        return min_sz
    @cached_property
    def 显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略(sf, /):
        return 求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜原文版扌(sf.靶值)
    @cached_property
    def 显链长上界牜连分数拆分牜二幂冃平方根策略(sf, /):
        #连分数拆分牜二幂冃平方根策略
        if sf.阳爻数纟靶值 <= 3:
            return sf.显链长上界牜二进制拆分
        return 求冫显链长上界牜连分数拆分牜二幂冃平方根策略扌(sf.靶值)

class _ver:
    初版牜毛病 = 0
    原文版 = 1
    去零版 = 2
def 求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜初版牜毛病扌(靶值, /):
    return _多版囗求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略扌(靶值, ver=_ver.初版牜毛病)
def 求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜原文版扌(靶值, /):
    return _多版囗求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略扌(靶值, ver=_ver.原文版)
def 求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜去零版扌(靶值, /):
    return _多版囗求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略扌(靶值, ver=_ver.去零版)
def _多版囗求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略扌(靶值, /, *, ver):
    #显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略
    @cache
    def f1(u, /):
        return 求冫显链长上界牜连分数拆分牜二幂冃平方根策略扌(u)
    def f(us, /):
        # us : sorted
        assert us
        assert us[0] >= 2
        assert len(us) == 1 or us[0] >= 3
        if len(us) == 1:
            [u] = us
            return main(u)
            return f1(u)
            return 求冫显链长上界牜连分数拆分牜二幂冃平方根策略扌(u)
        (d, u) = us[-2:]
        assert 3 <= d < u
        (q, r) = divmod(u, d)
        # [u == d*q +r]
        us.pop()
        if r >= 3:
            j = bisect_right(us, r, 0, len(us)-1)
            if not (j > 0 and us[j-1] == r):
                # not r in us
                us.insert(j, r)
        #bug:return f(us) + f([q]) + bool(r)
        return f(us) + main(q) + bool(r)
    match ver:
        case _ver.初版牜毛病:
            mk_us_ = _初版牜毛病mk_us_
        case _ver.原文版:
            mk_us_ = _原文版mk_us_
        case _ver.去零版:
            mk_us_ = _去零版mk_us_
        case _:
            raise 000
    mk_us_
        #反序
    def main_k_(k, u, s, /):
        assert k >= 1
        L = len(s)
        us = mk_us_(k, u, L)
        while us and us[-1] < 3:
            us.pop()
        if not us:
            return f1(u)
        #us.insert(0, u)
        us.reverse()
        us.append(u)
        return f(us)
    @cache
    def main(u, /):
        v2 = u.bit_count()
        if v2 <= 3:
            #显链长上界牜二进制拆分
            return floor_log2(u) +v2 -1
        assert u >= 15
        d = divisor7dichotomic_strategy_(u)
        assert 3 <= d < u

        Au = floor_log2(u)
        s = f'{u:b}'
        assert len(s) == 1+Au

        sf = 乸全局属性弱(False, u)
        (k, min_sz) = sf._扩展囗显链长上界牜窗式拆分
        max_k = min(Au, k+9)
        _min_sz = min(main_k_(k, u, s) for k in range(1, 1+max_k))
        assert _min_sz <= min_sz
        if 0b0000:
            _0_min_sz = sf.显链长上界牜窗式拆分牜排除零值片段
            if _0_min_sz < _min_sz:
                raise Exception(u, _min_sz, _0_min_sz)
            # Exception: (30, 7, 6)
        return _min_sz
    return main(靶值)

def _初版牜毛病mk_us_(k, u, L, /):
    us = [1<<(L-j) for j in range(k, L, k)]
    return us
def _原文版mk_us_(k, u, L, /):
    #bug{bug__small_fragment_at_LSB}:us = [u>>j for j in range(k, L, k)]
    rk = 1+ (L-1)%k
    us = [u>>j for j in range(rk, L, k)]
    return us
def _去零版mk_us_(k, u, L, /):
    us = _原文版mk_us_(k, u, L)
    mask = (1<<k)-1
    us = [v for v in us if v&mask]
    #.us = [v for v, v_ in zip(us, chain([u], us)) if v_&mask]
    return us


def 求冫显链长上界牜连分数拆分牜二幂冃平方根策略扌(靶值, /):
    #显链长上界牜连分数拆分牜二幂冃平方根策略
    @cache
    def f(u, /):
        v2 = u.bit_count()
        if v2 <= 3:
            #显链长上界牜二进制拆分
            return floor_log2(u) +v2 -1
        assert u >= 15
        d = divisor7dichotomic_strategy_(u)
        assert d >= 2
            # !! [d == N//2**((floor_log2(N)+1)//2) >= sqrtN/sqrt2 >= sqrt15/sqrt2 > sqrt7 > 2]
        assert d >= 3
            # !! [u >= 15]
        assert 3 <= d < u
        return h(u, d)
    def g(d, r, /):
        assert 0 <= r < d
        if r <= 2:
            return f(d)
        assert 3 <= r < d
        return h(d, r)
    def h(u, d, /):
        assert 3 <= d < u
        (q, r) = divmod(u, d)
        # [u == d*q +r]
        return g(d,r) + f(q) + bool(r)
    return f(靶值)

def _比较冫三种显链长上界算法扌(us, /):
    '-> (靶值数量, 列表纟最佳次数, 列表纟独占最佳的次数) # 次序:(二进制拆分,窗式拆分,窗式拆分牜排除零值片段,窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略{初版牜毛病,原文版,去零版},连分数拆分牜二幂冃平方根策略)'
    from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length
    u2szmm = pint2shortest_addition_chain_length
    #.for u in range(1, len(u2szmm)):
    def f(u, /):
        x = 乸全局属性弱(False, u)
        ls = [
        x.显链长上界牜二进制拆分
        ,x.显链长上界牜窗式拆分
        ,x.显链长上界牜窗式拆分牜排除零值片段
        #,x.显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略
        ,求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜原文版扌(u)
        #,求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜初版牜毛病扌(u)
        ,求冫显链长上界牜窗式拆分牜加靶链优化牜连分数拆分牜二幂冃平方根策略囗牜去零版扌(u)
        ,求冫显链长上界牜连分数拆分牜二幂冃平方根策略扌(u)
        ]
        return ls
    L = len(f(1))
    j2n = [0]*L
    j2u = [0]*L
    j2m = [0]*L
    num_bads = 0
    num_oks = 0
    num_too_bigs = 0
    num_hits = 0
    for sz, u in enumerate(us, 1):
        if not u >= 1:
            num_bads += 1
            continue
        ls = f(u)
        m = min(ls)
        js = [j for j, x in enumerate(ls) if x == m]
        for j in js:
            #最佳
            j2n[j] += 1
        if len(js) == 1:
            #独占最佳
            for j in js:
                j2u[j] += 1
            #.if 0b0001 and not js==[3]:print_err((u, ls, u2szmm[u if u < len(u2szmm) else 0]))
                # (484, [12, 16, 11, 12, 12], 11)
        if u < len(u2szmm):
            num_oks += 1
            szmm = u2szmm[u]
            if not szmm <= m:raise Exception((u, ls, szmm))
            js = [j for j, x in enumerate(ls) if x == szmm]
            #最优
            for j in js:
                j2m[j] += 1
            if js:
                num_hits += 1
        else:
            num_too_bigs += 1
    assert sz == sum((num_bads, num_oks, num_too_bigs))
    return (sz, j2n, j2u, (num_bads, num_oks, num_too_bigs), j2m, num_hits)

#class 乸全局属性(乸全局属性弱):
class 乸全局属性:
    '全局属性'
    def __getattr__(sf, nm, /):
        return getattr(sf._g, nm)
    def __init__(sf, 全局属性弱, 试用显链长, /):
        #super().__init__(靶值)
        check_type_is(乸全局属性弱, 全局属性弱)
        check_int_ge_le(全局属性弱.显链长下界, 全局属性弱.显链长上界, 试用显链长)
        sf._g = 全局属性弱
        sf._lb = 试用显链长
    @property
    def 试用显链长(sf, /):
        return sf._lb

#.class 乸节点弱:
#.    '节点弱'
#.    def __init__(sf, 全局属性, 鬽三前节点弱, 杈型, /):
#.        check_type_is(乸全局属性, 全局属性)
#.        check_type_is(乸杈型, 杈型)
#.        if 鬽三前节点弱 is None:
#.            (鬽小加点弱, 鬽大加点弱, 鬽前一节点弱) = (None, None, None)
#.            值 = 1
#.        else:
#.            三前节点弱 = 鬽三前节点弱
#.            (小加点弱, 大加点弱, 前一节点弱) = 三前节点弱
#.            (鬽小加点弱, 鬽大加点弱, 鬽前一节点弱) = 鬽三前节点弱 = 三前节点弱 = (小加点弱, 大加点弱, 前一节点弱)
#.            check_type_le(乸节点弱, 小加点弱)
#.            check_type_le(乸节点弱, 大加点弱)
#.            check_type_le(乸节点弱, 前一节点弱)
#.            if not all(节点弱.全局属性 is 全局属性 for 节点弱 in 三前节点弱):raise TypeError
#.            if not (小加点弱.址引 <= 大加点弱.址引 <= 前一节点弱.址引):raise TypeError
#.        (鬽小加点弱, 鬽大加点弱, 鬽前一节点弱)
#.        if 鬽前一节点弱 is None:
#.            址引 = 0
#.            值 = 1
#.        else:
#.            #前一节点弱 = 鬽前一节点弱
#.            址引 = 1+前一节点弱.址引
#.            值 = 小加点弱.值 + 大加点弱.值
#.            check_int_ge(1+前一节点弱.值, 值)
#.        址引
#.        值
#.        check_int_ge_le(0, 全局属性.试用显链长, 址引)
#.        check_int_ge_le(1, 全局属性.靶值, 值)
#.
#.        if not (值 == 1) is (址引 == 0) is (鬽前一节点弱 is None):raise TypeError
#.        if not (值 == 全局属性.靶值) is (义务参与次数 == 0):raise TypeError
#.        if not (值 == 全局属性.靶值) is (址引 == 全局属性.试用显链长):raise TypeError
#.
#.        欤显性 = 值>1
#.        #if 义务参与次数 == 0:
#.        if not 欤显性:
#.            #隐节点弱
#.        else:
#.            #显节点弱
#.
#.        sf._g = 全局属性
#.        sf._v = 值
#.        sf._j = 址引
#.        (鬽小加点弱, 鬽大加点弱, 鬽前一节点弱)
#.    全局属性
#.    值
#.    址引
#.    欤显性
#.    义务参与次数
#.    xx:剩余义务参与次数
#.    xx:债务累计值
#.
#.[u:<-[1..]][us :<- 最短加链{u}][len(us) >= 5]:
#.    # 都是 裁剪下界
#.    # 这里看看 裁剪上界
#.    [un1 := us[-1]]
#.    [un2 := us[-2]]
#.    [un3 := us[-3]]
#.    [un4 := us[-4]]
#.    [un5 := us[-5]]
#.    [un1 == u]
#.    [u > un2 >= u/2]
#.    [总参与次数{u;us;un2} <- {1,2}]
#.    [[总参与次数{u;us;un2} == 2] <-> [un2 == u/2]]
#.    [[总参与次数{u;us;un2} == 1] <-> [u > un2 > u/2]]
#.    [u == un2+uX]
#.    * [uX == un2]:
#.        [u == 2*un2]
#.        [总参与次数{u;us;un2} == 2]
#.        [un2 == u/2]
#.    * [uX < un2]:
#.        [总参与次数{u;us;un2} == 1]
#.        [u > un2 > u/2]
#.        倒退 擦除 un2
#.        !! [总参与次数{u;us;un3} >= 1]
#.        ?Y,Z :=>[3 <= Y <= Z][u == un3+uY+uZ]
#.        * [3 == Y == Z]:
#.            [u == 3*un3]
#.            [un2 == 2*u3]
#.            [u == un2+un3]
#.            [un2 == (2/3)*u]
#.        * [3 == Y < Z]:
#.            [u == 2*un3 + unZ]
#.            [unZ < un3]
#.            [unZ < (1/3)*u < un3]
#.            [unZ+un3==u-un3 < (2/3)*u < u-unZ==2*un3]
#.            :> [un2_ := unZ+un3]
#.            [un2_ < (2/3)*u]
#.            [用 un2_ 替换 un2@us 仍然是 最短加链{u}]
#.        * [3 < Y == Z]:
#.            [u == un3 + 2*unY]
#.            [unY < un3]
#.            [unY < (1/3)*u < un3]
#.            [2*unY < (2/3)*u]
#.            :> [un2_ := 2*unY]
#.            [un2_ < (2/3)*u]
#.            [用 un2_ 替换 un2@us 仍然是 最短加链{u}]
#.        * [3 < Y < Z]:
#.            [u == un3+uY+uZ]
#.            [unZ < unY < un3]
#.            [(1/3)*u < un3]
#.            [(2/3)*u > u-un3 == unY+unZ]
#.            :> [un2_ := unY+unZ]
#.            [un2_ < (2/3)*u]
#.            [用 un2_ 替换 un2@us 仍然是 最短加链{u}]
#.        [?[vs:<-最短加链{u}] -> [vs[-2] <= (2/3)*u]]
#.            此结论 可推广到 [u:<-[2..]]
#.            能否 倒退 更多几步？
#.                感觉可以
#.                [ℓ:=len(us)-1]
#.                [全链入度==2*ℓ]
#.                !! [全链出度==全链入度]
#.                [全链出度==2*ℓ]
#.                [全链出度分配到前ℓ个非末点，平均每个非末点出度为2]
#.                [非末点出度>=1]
#.                [全链待分配出度==ℓ]
#.                [非末点出度总贡献纟叉点<=3]
#.            不过感觉用处不大:搜索时子节点从小到大枚举
#.
#.
#.
#.class 乸节点:
#.    '节点'
#.    def __init__(sf, 全局属性, 鬽三前节点, 义务参与次数, 毝剩余义务参与次数, /):
#.    def __init__(sf, 全局属性, 节点弱, /):
#.        check_int_ge_le(0, 2, 义务参与次数)
#.        check_int_ge_le(-1, 义务参与次数, 毝剩余义务参与次数)
#.        剩余义务参与次数 = 义务参与次数 if 毝剩余义务参与次数 == -1 else 毝剩余义务参与次数
#.        check_int_ge_le(0, 义务参与次数, 剩余义务参与次数)
#.
#.
#.        if 鬽三前节点 is None:
#.            (鬽小加点, 鬽大加点, 鬽前一节点) = (None, None, None)
#.            值 = 1
#.        else:
#.            三前节点 = 鬽三前节点
#.            (小加点, 大加点, 前一节点) = 三前节点
#.            (鬽小加点, 鬽大加点, 鬽前一节点) = 鬽三前节点 = 三前节点 = (小加点, 大加点, 前一节点)
#.            check_type_le(乸节点, 小加点)
#.            check_type_le(乸节点, 大加点)
#.            check_type_le(乸节点, 前一节点)
#.            if not all(节点.全局属性 is 全局属性 for 节点 in 三前节点):raise TypeError
#.            if not (小加点.址引 <= 大加点.址引 <= 前一节点.址引):raise TypeError
#.        (鬽小加点, 鬽大加点, 鬽前一节点)
#.        if 鬽前一节点 is None:
#.            址引 = 0
#.            值 = 1
#.        else:
#.            #前一节点 = 鬽前一节点
#.            址引 = 1+前一节点.址引
#.            值 = 小加点.值 + 大加点.值
#.            check_int_ge(1+前一节点.值, 值)
#.            债务累计值 = 前一节点.债务累计值
#.            for 囜加点 in [小加点,大加点]:
#.                if 囜加点.剩余义务参与次数:
#.                    囜加点.剩余义务参与次数 -= 1
#.                    债务累计值 -= 囜加点.值
#.                else:
#.                    if not 囜加点.杈型 is 叉点:raise TypeError
#.                囜加点.总参与次数 += 1
#.                    杈型:叉点|介点|叶点
#.
#.        址引
#.        值
#.        check_int_ge_le(0, 全局属性.试用显链长, 址引)
#.        check_int_ge_le(1, 全局属性.靶值, 值)
#.
#.        if not (值 == 1) is (址引 == 0) is (鬽前一节点 is None):raise TypeError
#.        if not (值 == 全局属性.靶值) is (义务参与次数 == 0):raise TypeError
#.        if not (值 == 全局属性.靶值) is (址引 == 全局属性.试用显链长):raise TypeError
#.
#.        欤显性 = 值>1
#.        #if 义务参与次数 == 0:
#.        if not 欤显性:
#.            #隐节点
#.            债务累计值
#.        else:
#.            #显节点
#.            债务累计值
#.        债务累计值
#.        check_int_ge(0, 债务累计值)
#.
#.        sf._g = 全局属性
#.        sf._v = 值
#.        sf._j = 址引
#.        (鬽小加点, 鬽大加点, 鬽前一节点)
#.    全局属性
#.    值
#.    址引
#.    欤显性
#.    义务参与次数
#.    剩余义务参与次数
#.    债务累计值
#.  值:<-[1..=靶值]
#.  虚设:前置节点列表::[节点] #or:左指链表{(长度,节点)} #or:鬽前一节点
#.  鬽前一节点::鬽 节点
#.    [鬽前一节点 := None if 节点.欤显性 else (节点as显节点).前一节点]
#.  址引:=len(前置节点列表)<=试用显链长
#.  欤显性:=[值>1]
#.  义务参与次数:<-[0..=2]
#.  剩余义务参与次数:<-[0..=义务参与次数]
#.  债务累计值/累计未来义务总值::uint
#.  *显点属性:
#.    虚设:小加点址引:uint #or:左指链表{(长度,节点)} #or:小加点
#.    虚设:大加点址引:uint #or:左指链表{(长度,节点)} #or:大加点
#.      [显点.值 := 前置节点列表[显点.小加点址引].值 + 前置节点列表[显点.大加点址引].值]
#.      [0 <= 显点.小加点址引 <= 显点.大加点址引 < 显点.址引 == 1+显点.前一节点.址引 == len(前置节点列表) <= 试用显链长]
#.    前一节点::节点
#.    小加点::节点
#.    大加点::节点
#.      [显点.址引 := 1+显点.前一节点.址引]
#.      [显点.小加点址引 == 显点.小加点..址引]
#.      [显点.大加点址引 == 显点.大加点..址引]
#.




__all__
from script.蛮力搜索冫最短加链牜修剪搜索树 import *
