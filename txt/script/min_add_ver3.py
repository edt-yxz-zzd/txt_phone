r'''[[[
e script/min_add_ver3.py
最小加法链
    应改称为『最短加链』
        # <<== A003313		Length of shortest addition chain for n.
            # view script/min_add_ver2.py


最短扩张
有空更新:view others/数学/最小加法链.txt


等价归类:
    割点:乘法拆分:乘法交换律
    出度为1的点可省略:加法交换律
    混合？比如:m*n+1
      #不算: (a*b)*c+(a*b)==(a*b)*(c+1)
      局部串并联两端分割
  等价归类后的加法链表达:
    ???



加法链 -> 连通有限有向无环图DAG
* 加法链 -> 具象加法连通有限有向无环图
    (正整数) 为 点
    (加法操作数->加法之和) 为 有向边
    点的总数有限
    允许重复边
    唯一一个 入度为零 的 点 的对应正整数 为 1
    其余点的入度为2

    [源点入度==0]#定义:源点
    [终点出度==0]#定义:终点
    [非源点入度==2]
    [非终点出度>=1]
    [终点==源点]==>>[点的总数==1]
    [出度的总和==入度的总和==(点的总数-1)*2==加法次数*2]
        # [加法次数==加法链长度==点的总数-1]
    [1 <= 重复度<起点,讫点> <= 2]
        # 因为 [入度<讫点> == 2]

    * 单终点具象加法连通有限有向无环图
        即 有唯一一个 出度为零 的 点 的 具象加法连通有限有向无环图
    * 多终点具象加法连通有限有向无环图
        可用于 表达 最短扩张 的 中间态
        这就是 前一版本min_add_ver2的基本逻辑(区别在于min_add_ver2的中间状态混合了 多个 具象加法连通有限有向无环图:当某个正整数存在多种拆分时)

* 加法链 -> 关键节点连通有限有向无环图
    #出度为1的点可省略:加法交换律
    #之所以称之为『关键节点』，是因为 它的存在 节省了 加法数量(被重复利用<==>出度大于等于二)
    #
    将 具象加法连通有限有向无环图 中的 出度为一 的 点 删去
        只剩下 关键节点(=[def]=出度大于等于二的点)(可能包含 源点)、终点(=[def]=出度为零的点)(可能多个，可能是 源点) #源点(=[def]=入度为零的点 = 1)
    再将 相应 关键节点 与 非源的关键节点/非源的终点 连接成 有向边
        保持 非源的关键节点 的 出度不变
        但 非源的关键节点/非源的终点 的 入度可能增加

    [源点入度==0]#定义:源点
    [终点出度==0]#定义:终点
    [非源点入度>=2] #不同于 具象加法连通有限有向无环图
    [非终点出度>=2] #不同于 具象加法连通有限有向无环图
    [终点==源点]==>>[点的总数==1]
    [出度的总和==入度的总和==加法次数*2]
        # [加法次数==加法链长度==关键节点的总数+被删除的点的总数-1]
    [1 <= 重复度<起点,讫点> <= 3]
        # 超过3则可令(起点*2)成为新的关键节点 以减少 加法次数
        # 但 出度<起点>可能超过3: 例如:(1, 2, 3, 6, 12, 13)其中起点『1』的出度为4:{(1 -[2]-> 2), (1 -[1]-> 3), (1 -[1]-> 13)}
    [@起点 -> [len{讫点 | [重复度<起点,讫点> >= 2]} <= 1]]
        # 超过2则可令(起点*2)成为新的关键节点 以减少 加法次数
    我的盲点:
      [@讫点 -> [len{起点 | [重复度<起点,讫点> >= 2]} <= 1]]
        # 超过2则可令(起点1+起点2+...)成为新的关键节点 以减少 加法次数

    #####
    推论一:
        [关键节点连通有限有向无环图]:[任一 非源点，隐含了(非源点入度-2)个被删除的 非关键节点]

    #####
    * 单终点关键节点连通有限有向无环图
        推论二:
            [单终点关键节点连通有限有向无环图]:[次大节点 的 所有有向边 均指向 唯一终点(都是重复边)]

    表达形式:
        关键节点连通有限有向无环图 :: {起点:{讫点:重复度}}
        约束:
            [1 <= 起点 < 讫点]
            [重复度 >= 1]
            [出度<起点> == sum{重复度<起点,讫点>}]
            [入度<讫点> == sum{重复度<起点,讫点>}]
            [出度<起点> >= 2]or[出度<起点> == 0]
            [入度<讫点> >= 2]or[入度<讫点> == 0]
            [[入度<讫点> == 0] <-> [讫点==1]]
            [讫点 == sum{起点*重复度<起点,讫点>}]
例子:
    * (1, 2, 3):
        * 具象加法连通有限有向无环图:
            有向边集 = {(1 -[2]-> 2), (1 -[1]-> 3), (2 -[1]-> 3)}
        * 关键节点连通有限有向无环图:
            有向边集 = {(1 -[3]-> 3)}

    * (1, 2, 4, 5, 9):
        * 具象加法连通有限有向无环图:
            有向边集 = {(1 -[2]-> 2), (2 -[2]-> 4), (1 -[1]-> 5), (4 -[1]-> 5), (4 -[1]-> 9), (5 -[1]-> 9)}
        * 关键节点连通有限有向无环图:
            有向边集 = {(1 -[2]-> 2), (2 -[2]-> 4), (1 -[1]-> 9), (4 -[2]-> 9)}


#割点:乘法拆分:乘法交换律
乘法交换律:
    * (3, 6, 2, [(1, 2, 3, 6), (1, 2, 4, 6)])
        6==3*2==2*3
        (1, 2, 3, 6) == (1, 2, 3) <*> (1, 2)
        (1, 2, 4, 6) == (1, 2) <*> (1, 2, 3)

    * (4, 9, 3, [(1, 2, 3, 6, 9), (1, 2, 4, 5, 9), (1, 2, 4, 8, 9)])
        9==3*3
        (1, 2, 3, 6, 9) == (1, 2, 3) <*> (1, 2, 3)

    * (5, 15, 4, [(1, 2, 3, 5, 10, 15), (1, 2, 3, 6, 9, 15), (1, 2, 3, 6, 12, 15), (1, 2, 4, 5, 10, 15)])
        15==5*3==3*5
        (1, 2, 3, 5, 10, 15) == (1, 2, 3, 5) <*> (1, 2, 3)
        (1, 2, 3, 6, 9, 15) == (1, 2, 3) <*> (1, 2, 3, 5)

        (1, 2, 4, 5, 10, 15) == (1, 2, 4, 5) <*> (1, 2, 3)
        (1, 2, 3, 6, 12, 15) == (1, 2, 3) <*> (1, 2, 4, 5)
    * (4, 12, 3, [(1, 2, 3, 6, 12), (1, 2, 4, 6, 12), (1, 2, 4, 8, 12)])
        12==3*2*2==2*3*2==2*2*3
        (1, 2, 3, 6, 12) == (1, 2, 3) <*> (1, 2) <*> (1, 2)
        (1, 2, 4, 6, 12) == (1, 2) <*> (1, 2, 3) <*> (1, 2)
        (1, 2, 4, 8, 12) == (1, 2) <*> (1, 2) <*> (1, 2, 3)


混合:局部串并联两端分割:
    * (5, 13, 10, [(1, 2, 3, 5, 8, 13), (1, 2, 3, 5, 10, 13), (1, 2, 3, 6, 7, 13), (1, 2, 3, 6, 12, 13), (1, 2, 4, 5, 8, 13), (1, 2, 4, 5, 9, 13), (1, 2, 4, 6, 7, 13), (1, 2, 4, 6, 12, 13), (1, 2, 4, 8, 9, 13), (1, 2, 4, 8, 12, 13)])
        13==1+12

    [x 是 局部并联分支的起点]:
        #必要条件:
        [x 是 关键节点]
        [存在点(2*x)][存在边:(x -[2]-> 2*x)][毛病？(2*x)无需是关键节点]
            # 相当于 (1 -[2]-> 2)，只是相差x倍
    [y 是 局部并联分支的讫点]:
        #必要条件:
        #bug:[y 是 关键节点]
        [不使用 新点种『含不同乘法因子的局部串联讫点』]:
            [y 是 关键节点]
        [存在关键节点z][出度(z)<-{2,3}][存在边:(z -[出度(z)]-> y)]
            # z 相当于 y 的 极大关键节点
    -----更改识别对象:
    [x2 是 局部并联分支的起点 的 两倍点2*x]:
        #必要条件:
        [x2%2==0]
        [入度<x2> == 2]
        [x := x2///2]
        [存在关键节点x]
        [x 是 关键节点]
        [存在边:(x -[2]-> x2)]
            # 而非 {((x-a) -[1]-> x2, (b -[1]-> x2), ((x-a-b) -[1]-> x2)}
    [y_23 是 局部并联分支的讫点 的 所有入点中的 极大关键节点]:
        [y_23 是 关键节点]
        [出度(y_23)<-{2,3}]
        [存在点y][存在边:(y_23 -[出度(y_23)]-> y)]
        [不使用 新点种『含不同乘法因子的局部串联讫点』]:
            [y 是 关键节点]

[m,n,w>=1][gcd(m,n)==1]:
    [s,t>=0][s*m-t*n==1]:
        [(s+k*n)*m-(t+k*m)*n==1]
        [w*(s+k*n)*m-w*(t+k*m)*n==w]
        [(w*s-k*n)*m-(w*t-k*m)*n==w]
        [(w*s-k*n) >= 0][(w*t-k*m) <= 0]:
            <==> [k<=floor_div(w*s,n)][k>=ceil_div(w*t,m)]
            <==> [(w*t-1)//m +1 <= k <= (w*s)//n]
            <==> [(w*t-1)//m < k <= (w*s)//n]
        [(w*t-1)//m +1 <= (w*s)//n]:
            [(w*t-1)//m < (w*s)//n]
            [(w*t-1)//m *m*n < (w*s)//n *n*m]
            [((w*t-1)-(w*t-1)%m) *n < ((w*s)-(w*s)%n) *m]
[m,n,w>=1]:
    [可加法表达([m,n];w) =[def]= [?[a,b>=0] -> [w == a*m+b*n]]]
[ls :: [pint]][w>=1]:
    [可加法表达(ls;w) =[def]= [?[us :: [uint]{len=len(ls)}] -> [w == inner_product(us, ls)]]]
        # [可加法表达([m,n];w)] == [可非负线性表达(m,n;w)]
[[m,w>=1][w%m==0] -> [可加法表达([m];w)]]
[[m,n,w>=1][s,t>=0][s*m-t*n==1][(w*t-1)//m +1 <= (w*s)//n] -> [可加法表达([m,n];w)]]
    如何推广？得到[len(ls) >= 3]得充要条件？




backtrack++prune # pruning function
  渐深迭代-深度优先-大数优先-提前修剪-回溯算法
    修剪条件:见:
    view others/数学/最小加法链.txt
      http://wwwhomes.uni-bielefeld.de/achim/siam_thurber.pdf
      wget 'http://wwwhomes.uni-bielefeld.de/achim/siam_thurber.pdf' -O 'Efficient generation of minimal length addition chains(Edward G. Thurber)(1999).pdf'
搜索:最短加链:回溯算法:我的版本:
    使用 关键节点链 而非 任意点链
    识别 局部并联分支的乘法串联，只允许 非严格递降的乘法因子(2优先--因为翻倍最常见)
        但:这样一来，似乎 需要 在 关键节点+终点 之外，另设 新的节点种类『含不同乘法因子的局部串联讫点』因为 它 不一定是 关键节点 或 终点
        或者 选择 无视...

[[
Clift NM (2011), "Calculating Optimal Addition Chains", Computing. New York, NY, USA, March, 2011. Vol. 91(3), pp. 265-284. Springer-Verlag New York, Inc..
    Calculating Optimal Addition Chains(2011)(Clift).pdf
    https://link.springer.com/content/pdf/10.1007%2Fs00607-010-0118-8.pdf
    惊人的相似-关键节点忽略出度为一的点:
    我的盲点:
      [@讫点 -> [len{起点 | [重复度<起点,讫点> >= 2]} <= 1]]

Thurber EG and Clift NM, "Addition chains, vector chains, and efficient computation", Discrete Mathematics, Volume 344, Issue 2, 2021,
    https://www.researchgate.net/publication/347774866_Addition_chains_vector_chains_and_efficient_computation/fulltext/5febd54645851553a004f79a/Addition-chains-vector-chains-and-efficient-computation.pdf
    'Addition chains, vector chains, and efficient computation(2021)(Edward G.Thurber).pdf'
    修剪条件:改进了『Efficient generation of minimal length addition chains(Edward G. Thurber)(1999).pdf』

Edward G. Thurber, Efficient generation of minimal length addition chains, SIAM J. Comput. 28 (1999), 1247-1263.
    wget 'http://wwwhomes.uni-bielefeld.de/achim/siam_thurber.pdf' -O 'Efficient generation of minimal length addition chains(Edward G. Thurber)(1999).pdf'
]]

#]]]'''
__all__ = '''

    '''.split()
from copy import deepcopy
from itertools import pairwise


class 搜索最短加链囗回溯算法:
    def __init__(sf, 终点, /):
        assert 终点 >= 1
        sf.终点 = 终点
        sf.囗初始化囗最短加链长度囗上下限()
        sf.最短加链长度囗下限
        sf.最短加链长度囗猜想囗下限
        sf.最短加链长度囗上限
        assert 0 <= sf.最短加链长度囗下限 <= sf.最短加链长度囗猜想囗下限 <= sf.最短加链长度囗上限
        sf.囗初始化囗修剪算法囗参数()

    def 囗初始化囗最短加链长度囗上下限(sf, /):
        raise NotImplementedError
    def 囗初始化囗修剪算法囗参数(sf, /):
        raise NotImplementedError
    def 囗修剪算法囗单点(sf, us__i, /):
        raise NotImplementedError
    def 囗修剪算法囗两点(sf, us__i_neg1, us__i, /):
        raise NotImplementedError
    def 迭代搜索所有最短加链囗关键节点链等价类版(sf, /):
        r'''[[[
        关键节点链 = [(序号, 关键节点, {入点:重复度/uint{1,2,3}})]
        [不使用 新点种『含不同乘法因子的局部串联讫点』]

        #]]]'''
        最短加链长度囗下限 = sf.最短加链长度囗下限
        最短加链长度囗上限 = sf.最短加链长度囗猜想囗下限
        最短加链长度囗上限 = sf.最短加链长度囗上限
        if not 0 <= 最短加链长度囗下限 <= 最短加链长度囗猜想囗下限 <= 最短加链长度囗上限:raise logic-err
        #长度 = None
        ls = None
        #bug:for 最短加链长度囗最大允许值 in range(最短加链长度囗猜想囗下限, 1+最短加链长度囗上限):
        #   不行！待会 先输出 部分 非最短加链
        for 最短加链长度囗最大允许值 in range(最短加链长度囗下限, 1+最短加链长度囗上限):
            for ls in sf.囗迭代搜索所有最短加链囗关键节点链等价类版():
                if not ls[-1][0] == 最短加链长度囗最大允许值:raise logic-err
                if not ls[-1][1] == sf.终点:raise logic-err
                sf.检查关键节点链(ls)

                #yield deepcopy(ls)
                yield [(序号, 关键节点或终点, {**入点之重复度}) for (序号, 关键节点或终点, 入点之重复度) in ls]
            if not ls is None:
                break
        return
    def 检查关键节点链(sf, ls, /):
        终点 = sf.终点
        assert ls
        assert ls[0] == (0, 1, {})
        assert ls[-1][1] == 终点
        点之序号 = {关键节点或终点:序号 for (序号, 关键节点或终点, 入点之重复度) in ls}
        for (囗序号, 囗关键节点或终点, 囗入点之重复度), (序号, 关键节点或终点, 入点之重复度) in pairwise(ls):
            assert 囗序号 < 序号
            assert 囗关键节点或终点 < 关键节点或终点
            assert 入点之重复度
            入度 = sum(入点之重复度.values())
            assert 入度 >= 2
            assert all(1 <= 重复度 <= 3 for 重复度 in 入点之重复度.values())
            assert 入点之重复度.keys() <= 点之序号.keys()

            assert 囗序号+入度-1 == 序号
            assert sum(入点*重复度 for 入点, 重复度 in 入点之重复度.items()) == 关键节点或终点
        #####
        起点之重复度之讫点集 = {点:{1:set(), 2:set(), 3:set()} for 点之序号}
        讫点之重复度之起点集 = {点:{1:set(), 2:set(), 3:set()} for 点之序号}
        for (序号, 关键节点或终点, 入点之重复度) in ls:
            讫点 = 关键节点或终点
            for 入点, 重复度 in 入点之重复度.items():
                起点 = 入点
                起点之重复度之讫点集[起点][重复度].add(讫点)
                讫点之重复度之起点集[讫点][重复度].add(起点)

        for (起点, 重复度之讫点集) in 起点之重复度之讫点集.items():
            assert any(重复度之讫点集)
            出度 = sum(重复度*len(讫点集) for (重复度, 讫点集) in 重复度之讫点集.items())
            assert 出度 >= 2 if not 起点 == 终点 else 出度==0
            assert 出度-len(重复度之讫点集[1]) <= 3
            assert len(重复度之讫点集[2])+len(重复度之讫点集[3]) <= 1

        #####检查:乘法因子降序
        局部极大点之候选局部太上终点 = {}
        局部极大点之候选局部终点 = {}
        for (起点, 重复度之讫点集) in 起点之重复度之讫点集.items():
            if (not 起点 == 终点) and len(重复度之讫点集[1]) == 0:
                assert len(重复度之讫点集[2])+len(重复度之讫点集[3]) == 1
                局部极大点 = 起点
                [候选局部太上终点] = [*重复度之讫点集[2], *重复度之讫点集[3]]
                局部极大点之候选局部太上终点[局部极大点] = 候选局部太上终点
                #
                # !![不使用 新点种『含不同乘法因子的局部串联讫点』]
                #   即:要求:候选局部终点 是 关键节点/终点，隐含点 被无视，因为情形太复杂
                重复度之起点集 = 讫点之重复度之起点集[候选局部太上终点]
                bug:允许多入点:if sum(map(len, 重复度之起点集)) == 1:
                    assert len(重复度之起点集[1]) == 0 and len(重复度之起点集[2])+len(重复度之起点集[3]) == 1
                    候选局部终点 = 候选局部太上终点
                    [囗局部极大点] = [*重复度之起点集[2], *重复度之起点集[3]]
                    assert 囗局部极大点 == 局部极大点
                    重复度 = 候选局部终点//局部极大点
                    assert 局部极大点**重复度 == 候选局部终点
                    assert 重复度之讫点集[重复度] == {候选局部终点}
                    assert 重复度之起点集[重复度] == {局部极大点}
                    局部极大点之候选局部终点[局部极大点] = 候选局部终点

        局部二三倍点之局部源点 = {}
        for (讫点, 重复度之起点集) in 讫点之重复度之起点集.items():
            if sum(map(len, 重复度之起点集)) == 1:
                assert len(重复度之起点集[1]) == 0 and len(重复度之起点集[2])+len(重复度之起点集[3]) == 1
                局部二三倍点 = 讫点
                [局部源点] = [*重复度之起点集[2], *重复度之起点集[3]]
                局部二三倍点之局部源点[局部二三倍点] = 局部源点

        局部极大点之候选局部太上终点
        局部极大点之候选局部终点
        局部二三倍点之局部源点
        讫点之重复度之起点集
        起点之重复度之讫点集
        TODO:识别:局部乘法串联

    def 囗迭代搜索所有最短加链囗关键节点链等价类版(sf, 最短加链长度囗最大允许值, /):
        终点 = sf.终点
        assert 终点 >= 1
        ls = [(0, 1, {}), (1, 2, {1:2})]
            return
        if 终点<=2:
            yield ls[:终点]
            return

        assert 终点 >= 2