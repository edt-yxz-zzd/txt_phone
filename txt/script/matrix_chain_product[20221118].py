#__all__:goto
r'''[[[
[[本文件已过时，不再更新20221118
部分移至并修改:
    e ../../python3_src/seed/math/matrix_chain_product/*
        已修改
        本文件已过时，不再更新，仅用于 参考:调试，历史
    未移动部分:单调版，所有测试
]]
[[[[
TODO:[[
    DONE:更新 __all__
    DONE:重启__floor_div__ 替代 Fraction
    DONE:bug已解决:[[
        xxx #我自己添加的:min_weight4whole
        xxx #   论文中 ceil_arc_ 嵌套，现在 不会了
        xxx 但仔细想想，这似乎表明，论文算法 有无法更正的 根本性错误！
        [not ceil_arc_.supporting_weight < curr_arc_.supporting_weight] -> [ceil_arc_ 变 hidden_son of curr_arc_]
        但 重新计算后的curr_arc_.supporting_weight可能比ceil_arc_.supporting_weight还大，若next_curr_arc_.min_weight正好在它们之间，则 curr_arc_无法存活，但 ceil_arc_仍可幸存，故ceil_arc_不是son。
        并不会！！因为[supporting_weight=[def]=MNO_between(...)/diff_between(...)]
        [supporting_weightA <= supporting_weightB] -> [supporting_weightA <= new_supporting_weightA == (MNO_between4A+MNO_between4B)/(diff_between4A+diff_between4B) <= supporting_weightB]
        我错在:[使用 批量比较，再批量处理，通过num_ceil_hidden_children4curr_arc_的改变判断是否继续循环]
            这样不行，必须一个ceil_arc_变son就更新一次curr_arc_.supporting_weight，ceil_arc_.supporting_weight必须最小，而且不能使用整数值(MNO_between//diff_between)，必须用Fraction！(supporting_weight不断提高，严格次序源自于 跨越整数边界的时候)
        细想之下，整数边界 无影响，只有 ls 都是 正整数 就行，不过 中间变量curr_arc_.unorder_ceil_arcs_/unorder_ceil_hidden_children_ 会不同
        ]]
        [[之前的尝试:
        可能是 def base_product(idx_arc, /):
            不对，非单调版 没毛病:def get_base_product_of_curr_arc_(sf, curr_arc_, /):
        应该是diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_<Imin8Arc_>计算有误
            或者说，计算无误，但Imin8Arc_情形 该分母需要特殊计算。
                不对，因为Imin8Arc_提前退场
                    不对之不对，虽然提前退场，但之前求final_unorder_above_arcs4curr_arc_<Imin8Arc_>呢??
                        似乎也没毛病...
            xxx 但确实算错，见『_ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_』
                而且是 初始化 出错
                错的是calc_side_product_between_
                    没错get_diff__side_product_above_curr_arc__base_product_above_curr_arc_
                    没错get_side_product_above_curr_arc_
                    最后发现错的竟然是_ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
                        错的竟然是_ON_debug__all_sides_between_curr_arc_ceil_arcs_
                            原因:忘记补上空洞
        ]]

    DONE:代码效率 似乎劣于 算法效率 ONlogN，有待提高
        一在:求final_unorder_above_arcs4curr_arc_时:
            unorder_above_arcs_.extend(_unorder_above_arcs_)
        一在:ceil_arc变hidden_child时:
            _heap_pushs(ceil_arc_.unorder_ceil_arcs_)
        待办:使用:
            ceil_arc_.unorder_ceil_arcs_ :: recur_heap<recur_heap>
            ...mergeable_heap/unbanlance_tree min_sz[height] = min_sz[height-1] + min_sz[height-2] + 1
                统一上下两次对移除above_arc_/ceil_arc_的处理
                from seed.types.MergeableHeap import MergeableHeap, HeapError__Empty, HeapError__EatSelf

    DONE:删除Ilocal_max8Arc_

    DONE:测试 待更新:现在有:『词典序最先的最优三角化方案囗立方算法囗』，而 测试 还停留在 比较 mno。待办:比较sorted_inner_arcs_(offseted by imin)
        mno_tree -> inner_arcs
            mno_tree -> binary_arc_tree
            binary_arc_tree -> inner_arcs
        mk_binary_arc_tree_from_mno_tree
        mk_inner_arcs_from_binary_arc_tree
        mk_binary_arc_tree_from_unsorted_inner_arcs
        mk_mno_tree_from_binary_arc_tree
        'binary_arc_tree = (root_arc, may ((root_arc[1], mid, root_arc[0]), binary_arc_tree, binary_arc_tree))'
            root_arc是有向边，外边(i,i+1)%L 的 向心方向 指向 多边形内部反之朝外；内边以此类推。
        'mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'

]]
mno:最小操作数

e script/matrix_chain_product.py
e others/book/matrix_chain_product/Computation of matrix chain products I,II(1984)(Hu)(Shing)[polygon partitioning].pdf.txt
[[程序调试:发现重灾区是H0
即:
    聚焦型 即 扇形 -> MNO 求值
    聚焦型 即 扇形 -> 生成 所有 竖对角线
重点是:边界条件:点的移动 混合 outer_arc/ceil_arc 而非 仅仅 +1/-1
]]
[[摘要:重大更进:
论文定义的概念:[潜在的潜在的横对角线]
自定义的概念:[除零的类横对角线囗第二版]

[one_sweep_algorithm 输出所有 潜在的潜在的横对角线]
[第二版的除零的类横对角线是无印版的潜在的潜在的横对角线]
[若某词典序最先的最优三角化方案不含第二版的除零的类横对角线则该方案为聚焦于最小处的扇形方案]
]]
[[
古典的动态编程(保存中间变量):O(N**3) #表格规模为O(N**2)，其中每一项的计算(min{...})为O(N)

e others/book/matrix_chain_product/矩阵乘法链.txt
e others/book/matrix_chain_product/On-instances-of-the-matrix-chain-product-problem-solved-in-linear-time (2009)(Sana).pdf.txt
    论文 只考察 单调的 矩阵乘法链维数序列 及其循环移动变体
      O(N)

e others/book/matrix_chain_product/Computation of matrix chain products I,II(1984)(Hu)(Shing)[polygon partitioning].pdf.txt
      O(NlogN)
]]


[[顺时针++升序标记顶点:
多边形顶点标记:
  (L-1)个矩阵相乘，L个维数
  [ls :<- 矩阵乘法链维数序列]
  [ls :: [pint]{len>=2}]
  [L := len(ls)]
  [L >= 2]
  矩阵乘法链从左到右的(L-1)个矩阵的行列维数是:[(ls[i], ls[i+1]) | [i :<- [0..=L-2]]]
  ###
  * [L==2]: 多边形退化成一条边(0,1)
  * [L>=3]:
    以从左到右的有向边(0,L-1)为地基
    以从右到左的有向边(L-1,0)为地基，，顺时针方向依次标记多边形的所有顶点
    顺时针方向外边弧(0~L-1)代表整个表达式
    假设矩阵乘法链最外层拆分成L-1==(k)+(L-k-1)个矩阵
      即 最外层乘号的左操作数含(k)个矩阵，右操作数含(L-k-1)个矩阵
    则:ls[k]共享:(ls[:k+1], ls[k:])
    顺时针方向外边弧(0~k)代表整个表达式的左操作数
    顺时针方向外边弧(k~L-1)代表整个表达式的右操作数
    三角形(0,k,L-1)代表最外层乘号
]]


a*b*c
    (a*b)*c
    a*(b*c)
]]]]


py -m nn_ns.app.debug_cmd   script.matrix_chain_product

L2num_tests, upper4weight, version

py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 '--L2num_tests={L:L for L in range(2,10)}' '--upper4weight=10000' '--version=1'

py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=2'

py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 '--L2num_tests={L:10*L for L in range(2,100)}' '--upper4weight=10000' '--version=2'

py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 '--L2num_tests={L:10*L for L in range(2,100)}' '--upper4weight=10000' '--version=3' '--_turnon_debug=0'


py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=3' '--_turnon_debug=0'










py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法 '--L2num_tests={L:L for L in range(2,10)}' '--upper4weight=10000' '--version=1'
py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法 '--L2num_tests={L:L for L in range(2,100)}' '--upper4weight=10000' '--version=2'
py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法 '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=2'


py script/matrix_chain_product.py @std_api4matrix_chain_product__dynamic_programming__O_NNN ='[1,2,3,4]'
(18, 0, (6, 0, (0, 0, (1, 2)), 1, (0, 1, (2, 3)), 3, (1, 2, 3)), 2, (0, 2, (3, 4)), 4, (1, 3, 4))
    #(18, 0, (6, 0, (0, 0), 1, (0, 1), 3), 2, (0, 2), 4)

py script/matrix_chain_product.py @std_api4matrix_chain_product__dynamic_programming__O_NNN ='[2,1,3,4]'
(20, 0, (0, 0, (2, 1)), 1, (12, 1, (0, 1, (1, 3)), 2, (0, 2, (3, 4)), 4, (1, 3, 4)), 4, (2, 1, 4))
    #(20, 0, (0, 0), 1, (12, 1, (0, 1), 2, (0, 2), 4), 4)

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[1,2,3,4]'
[]
[]
[(6, 0, [1], 3)]
[(18, 0, [2], 4)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[2,1,3,4]'
[]
[]
[(12, 1, [2], 4)]
[(20, 0, [1], 4)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[1,3,2,4]'
[]
[]
[(6, 0, [1], 3)]
[(14, 0, [2], 4)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[3,1,2,4]'
[]
[]
[(8, 1, [2], 4)]
[(20, 0, [1], 4)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[2,3,1,4]'
[]
[]
[(6, 0, [1], 3)]
[(14, 0, [2], 4)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[3,2,1,4]'
[]
[]
[(6, 0, [1], 3)]
[(18, 0, [2], 4)]


py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[1,1,1,1]'
[]
[]
[(1, 0, [1], 3), (1, 1, [2], 4)]
[(2, 0, [1, 2], 4)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[1,1,1,1,1]'
[]
[]
[(1, 0, [1], 3), (1, 1, [2], 4), (1, 2, [3], 5)]
[(2, 0, [1, 2], 4), (2, 1, [2, 3], 5)]
[(3, 0, [1, 2, 3], 5)]





py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[3,2,4,6]'
[]
[]
[(48, 1, [2], 4)]
[(84, 0, [1], 4)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[3,2,4,12]'
[]
[]
[(24, 0, [1], 3), (96, 1, [2], 4)]
[(168, 0, [1, 2], 4)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[3,2,4,24]'
[]
[]
[(24, 0, [1], 3)]
[(312, 0, [2], 4)]



[四稳定多边形三角化方案 不必是 最优多边形三角化方案]
  例:
    [ls := [10,11,25,40,12]]
    [左结合优先方案<5> = 聚焦于ls[0]的方案 <- 四稳定多边形三角化方案<ls>]
    [右结合优先方案<5> = 聚焦于ls[-1]的方案 <- 最优多边形三角化方案<ls>]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[10,11,25,40,12]'
[]
[]
[(12000, 2, [3], 5)]
[(15300, 1, [2], 5)]
[(16620, 0, [1], 5)]

py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[10,11,25,40]'
[]
[]
[(2750, 0, [1], 3)]
[(12750, 0, [2], 4)]
py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[10,25,40,12]'
[]
[]
[(10000, 0, [1], 3)]
[(14800, 0, [2], 4)]








[[
[ls == [w,x,y,z]]:
    [(1/w - 1/x) < (1/z - 1/y)]:
        [(x-w)/w/x < (y-z)/z/y]
        [(x-w)*y*z < (y-z)*w*x]
        [(x*y*z-w*y*z) < (y*w*x-z*w*x)]
        [(x*y*z+z*w*x) < (y*w*x+w*y*z)]
        [右结合优先操作数 ==(x*y+w*x)*z < w*(x*y+y*z) == 左结合优先操作数]
        [左结合优先操作数 > 右结合优先操作数]
        [此时 3个矩阵 右结合 最优]
    # 比较:[(1/w + 1/y) <?> (1/z + 1/x)]
    [w < y][x < z][y < z]:
        * [w < y < x < z]:
            [1/w > 1/y > 1/x > 1/z]
            [1/w + 1/y > 1/x + 1/z]
            [1/w - 1/x > 1/z - 1/y]
            [此时 3个矩阵 左结合 最优]
        * [w < x < y < z]:
            [1/w > 1/x > 1/y > 1/z]
            [1/w + 1/y > 1/x + 1/z]
            [此时 3个矩阵 左结合 最优]
        * [x < w < y < z]:
            [(w,x,y,z) == (3,2,4,6)]:
                [1/w + 1/y = 7/12 < 8/12 = 2/3 = 1/x + 1/z]
                [此时 3个矩阵 右结合 最优]
            [(w,x,y,z) == (3,2,4,12)]:
                [1/w + 1/y = 7/12 = 1/x + 1/z]
                [此时 3个矩阵 左结合 右结合 等同计算量]
            [(w,x,y,z) == (3,2,4,24)]:
                [1/w + 1/y = 7/12 = 14/24 > 13/24 = 1/x + 1/z]
                [此时 3个矩阵 左结合 最优]
]]

#]]]'''
__all__ = '''
check_pint_seq
check_matrix_chain_product_arg

matrix_chain_product__dynamic_programming__O_NNN
    矩阵乘法链囗所有最优打括号方案囗暂存子问题结果囗立方性算法
    std_api4matrix_chain_product__dynamic_programming__O_NNN
    tail4std_api4matrix_chain_product__dynamic_programming__O_NNN

准备囗词典序最先的最优三角化方案

词典序最先的最优三角化方案囗立方算法囗




sort_idc_of_seq
sort_idc
collect_idx_pph_arcs_that_cut_local_max
collect_vv_pph_arcs_that_cut_local_max
merge_sort__2




matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N
    矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法
    std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N
    tail4std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N

radix_sort__arcs
mk_sorted_unoffseted_arcs_from_unsorted_offseted_arcs_
mk_mno_tree_from_unsorted_inner_arcs
mk_inner_arcs_from_mno_tree
mk_inner_arcs_from_binary_arc_tree
mk_binary_arc_tree_from_mno_tree
mk_mno_tree_from_binary_arc_tree




mk_offset_
mk_unoffset_
unoffset_arcs_
iter_outer_arcs_of
iter_unsorted_inner_outer_arcs_from_unsorted_inner_arcs
mk_binary_arc_tree_from_unsorted_inner_arcs
mk_binary_arc_tree_from_arc2next_triangle_vtx
mk_arc2next_triangle_vtx_from_unsorted_inner_arcs


is_triangle_order

mk_arc2next_triangle_vtx_from_v2ordered_vtc
mk_arc2another_triangle_vtc_from_v2ordered_vtc
mk_v2ordered_vtc_from_unsorted_inner_outer_arcs

mk_v2unordered_vtc_from_unsorted_inner_outer_arcs
mk_v2sorted_vtc_from_v2unordered_vtc
mk_v2ordered_vtc_from_v2sorted_vtc


iter_randrange
iter_list_of_randrange

迭代囗随机生成囗矩阵乘法链维数序列
迭代囗随机生成囗矩阵乘法链维数序列囗单调
单调化囗
单例测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法
随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法



囗矩阵乘法链维数序列囗相关函数
Imin8Arc_
IdxArc_
matrix_chain_product__polygon_partitioning__O_NlogN

    矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗等同排序算法耗时
    std_api4matrix_chain_product__polygon_partitioning__O_NlogN
    tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN
单例测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时
随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时



    '''.split()

__all__
from fractions import Fraction
from itertools import pairwise, chain, islice, filterfalse
from random import randrange
from heapq import nsmallest, heapify, heappop, heappush
    #nsmallest(n, iterable, key=None)
from seed.iters.is_sorted import is_sorted, is_strict_sorted
from collections import defaultdict
from seed.tiny import echo, fst, snd
from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
from seed.seq_tools.inverse_uint_bijection_array import inverse_uint_bijection_array
from seed.types.view.SeqLeftRotateView import SeqLeftRotateView
from seed.algo.bucket_sort.bucket_sort_per_row import bucket_sort_per_row
from seed.algo.bucket_sort.radix_sort_with_table import radix_sort_with_table
from seed.tiny_.check import check_uint_lt
from seed.types.MergeableHeap import MergeableHeap


def check_pint_seq(ls, /):
    assert all(type(d) is int for d in ls)
    assert all(d > 0 for d in ls)
    ls[:0]
    len(ls)
def check_matrix_chain_product_arg(矩阵乘法链维数序列, /):
    check_pint_seq(矩阵乘法链维数序列)
    assert len(矩阵乘法链维数序列) >= 2
    assert len(矩阵乘法链维数序列[:2]) == 2
        #seq

def matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, /):
    '-> num_matrices2mno_begin_mids_end_tpls/[[(mno, begin, mids, end)]]{N} #DP:O(N**3):[N>=2]:total (N-1) matrices'
    check_matrix_chain_product_arg(矩阵乘法链维数序列)
    ls = 矩阵乘法链维数序列
    L = N = len(ls)
    #if L == 2: num_matrices2mno_begin_mids_end_tpls = [[], []]
    def _MNO__lookup(begin, end, /):
        assert begin+2 <= end
        if begin+2 == end:
            return 0
        assert begin+3 <= end
        idx = j = end-begin-1
        assert 0 <= idx <= len(lss)
        if not idx == len(lss):
            return lss[idx][begin][0]
        raise LookupError
    def _MNO__mid_(k, begin, end, /):
        #assert begin+1 <= k < k+2 <= end
        assert begin < k < end-1
        return (_MNO__lookup(begin,k+1)+_MNO__lookup(k,end)+ls[begin]*ls[k]*ls[end-1])
    def _MNO__min(begin, end, /):
        assert begin+2 <= end
        return min(_MNO__mid_(k, begin, end) for k in range(begin+1,end-1))
    def MNO(begin, end, /):
        assert begin+2 <= end
        try:
            return _MNO__lookup(begin, end)
        except LookupError:
            return _MNO__min(begin, end)
        pass

    #table_2 = [(ls[i-1]*ls[i]*ls[i+1], i-1,[i],i+1) for i in range(1,L-1)]
    #lss = [None, None, table_2]
    lss = [None, None]
        # lss[j]:j 是 矩阵个数,j==end-begin-1
    for j in range(2,L):
        table_j = [(MNO(begin,end), begin,[],end) for begin in range(L-j) for end in [begin+j+1]]
        lss.append(table_j)
    #rint(lss)

    for j in range(2,L):
        table_j = lss[j]
        for (mno, begin, mids, end) in table_j:
            assert mids == []
            mids.extend(k for k in range(begin+1,end-1) if _MNO__mid_(k, begin, end)==mno)
            assert mids

    if L > 2:
        [(mno, begin, mids, end)] = lss[L-1]
        assert begin == 0
        assert end == L

    todo = [[False for end in range(j+1, L+1)] for j in range(L)]
    ouputss = [[] for j in range(L)]
    num_matrices2mno_begin_mids_end_tpls = ouputss
    def _get(begin, end, /):
        j = end-begin-1
        table_j = lss[j]
        r = (mno, _begin, mids, _end) = table_j[begin]
        assert _begin == begin
        assert _end == end
        return r
    def _put(begin, end, /):
        j = end-begin-1
        todo[j][begin] = True
        return
    _put(0,L)
    for j in reversed(range(2,L)):
        ouputss_j = ouputss[j]
        for begin, required in enumerate(todo[j]):
            if not required: continue
            end = j+begin+1
            # output (begin, end)
            r = (mno, _begin, mids, _end) = _get(begin, end)
            for k in mids:
                _put(begin, k+1)
                _put(k, end)
            ouputss_j.append(r)

    return num_matrices2mno_begin_mids_end_tpls
    return ouputss
#end-def matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, /):

矩阵乘法链囗所有最优打括号方案囗暂存子问题结果囗立方性算法 = matrix_chain_product__dynamic_programming__O_NNN

def std_api4matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, /, *, version=1):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    num_matrices2mno_begin_mids_end_tpls = matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列)
    if version==1:
        mno_tree = tail4std_api4matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, num_matrices2mno_begin_mids_end_tpls)
    elif version==2:
        raise Exception(version)
        词典序最先的最优三角化方案囗立方算法囗
    else:
        raise Exception(version)
    return mno_tree
def tail4std_api4matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, num_matrices2mno_begin_mids_end_tpls, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    assert len(num_matrices2mno_begin_mids_end_tpls) == len(矩阵乘法链维数序列)
    ls = 矩阵乘法链维数序列
    L = len(num_matrices2mno_begin_mids_end_tpls)
    def mk_one_mno_tree(begin, end, /):
        i = end-begin-1
        assert i >= 1
        if i == 1:
            return (0, begin, (ls[begin],ls[begin+1]))
        assert i >= 2
        for (mno, _begin, mids, _end) in num_matrices2mno_begin_mids_end_tpls[i]:
            if _begin == begin:
                break
        else:
            raise logic-err
        assert _end == end
        mid = mids[0]
        lhs_mno_tree = mk_one_mno_tree(begin, mid+1)
        rhs_mno_tree = mk_one_mno_tree(mid, end)
        return (mno, begin, lhs_mno_tree, mid, rhs_mno_tree, end, (ls[begin],ls[mid],ls[end-1]))
    return mk_one_mno_tree(0, L)

r'''[[[
def xxx词典序最先的最优三角化方案囗立方算法囗(矩阵乘法链维数序列, /, *, may_imin):
x   '-> (mno, L, imin, sorted_inner_arcs_)'
x   #xxx :raise logic-err #算法思路有误，必须 先定位某个范围里的最小内边，再bottomup识别祖先，但 这有祖先，右侧全空，而且bottomup 需要控制 祖先范围
x   #   上面的想法已实现，只是仍有毛病:比如最小边为(0,6)，并非长度为2
x   #
x   (ls, imin, L, ls_, imin_) = 准备囗词典序最先的最优三角化方案(矩阵乘法链维数序列, may_imin=may_imin)
x   num_matrices2mno_begin_mids_end_tpls_ = matrix_chain_product__dynamic_programming__O_NNN(ls_)
x       #必须先偏移再列表，不能反转次序，否则，地基线/最低外边 选取不同，各自的自然成长树不同(树有根则有向，若无向化才会等同)，难求
x
x
x   if 0:
x       #通通取消
x       offset_idx_ = mk_offset_(L, imin)
x       def L_(i_, /):
x           return i_%L
x   else:
x       offset_idx_ = mk_offset_(L, 0)
x       def L_(i_, /):
x           return i_
x
x   num_matrices2begin2mids_ = []
x   for num_matrices, mno_begin_mids_end_tpls in enumerate(num_matrices2mno_begin_mids_end_tpls_):
x       assert len(num_matrices2begin2mids_) == num_matrices
x       begin2mids_ = {}
x       for mno, begin, mids, end in mno_begin_mids_end_tpls:
x           assert end-begin-1 == num_matrices
x           begin_ = offset_idx_(begin)
x           mids_ = [*map(offset_idx_, mids)]
x           begin2mids_[begin_] = mids_
x       num_matrices2begin2mids_.append(begin2mids_)
x   num_matrices2begin2mids_
x   #######
x   r''[[[
x   if 1:
x       #可怕！！意料之外的bug:num_matrices==(L-1) 即最后一行:begin,end已无意义，因为首尾相连 成环
x       if L >= 3:
x           [(begin_, mids_)] = num_matrices2begin2mids_[-1].items()
x           num_matrices2begin2mids_[-1] = {???0:mids_}
x           ...无法继续！！！
x   #]]]''
x   #######
x   num_matrices2begin2mid_leftmost_leaf_pair_ = []
x   def get_leftmost_leaf_(num_matrices, begin_, /):
x       #bug:(mid_, leftmost_leaf_) = num_matrices2begin2mid_leftmost_leaf_pair_[num_matrices][begin]
x       (mid_, leftmost_leaf_) = num_matrices2begin2mid_leftmost_leaf_pair_[num_matrices][begin_]
x       return leftmost_leaf_
x
x   for num_matrices, begin2mids_ in enumerate(num_matrices2begin2mids_):
x       assert len(num_matrices2begin2mid_leftmost_leaf_pair_) == num_matrices
x       begin2mid_leftmost_leaf_pair_ = {}
x       for begin_, mids_ in begin2mids_.items():
x           end_ = L_(num_matrices+begin_+1)
x           if num_matrices == 2:
x               [mid_] = mids_
x               assert mid_ == L_(begin_+1) == L_(end_-2)
x               leftmost_leaf_ = (*sorted([begin_, L_(begin_+num_matrices)]),)
x           else:
x               assert num_matrices >= 3
x               xs = []
x               for mid_ in mids_:
x                   if mid_ == L_(begin_+1):
x                       leftmost_leaf_ = get_leftmost_leaf_(num_matrices-L_(mid_-begin_), mid_)
x                   else:
x                       #bug:leftmost_leaf_ = get_leftmost_leaf_(num_matrices-(mid_-begin_), begin_)
x                       leftmost_leaf_ = get_leftmost_leaf_(L_(mid_-begin_), begin_)
x                   xs.append((leftmost_leaf_, mid_))
x
x               (leftmost_leaf_, mid_) = min(xs)
x           mid_leftmost_leaf_pair_ = (mid_, leftmost_leaf_)
x           begin2mid_leftmost_leaf_pair_[begin_] = mid_leftmost_leaf_pair_
x
x       num_matrices2begin2mid_leftmost_leaf_pair_.append(begin2mid_leftmost_leaf_pair_)
x   num_matrices2begin2mid_leftmost_leaf_pair_
x   #######
x   #######
x   #######
x   if 1:
x       print(num_matrices2mno_begin_mids_end_tpls_)
x       print(num_matrices2begin2mids_)
x       print(num_matrices2begin2mid_leftmost_leaf_pair_)
x   #######
x   unsorted_inner_arcs_ = []
x   todo_arcs_ = []
x   def leftmost_idx_of_(i_, j_, /):
x       num_matrices = j_-i_
x       (mid_, leftmost_leaf_) = num_matrices2begin2mid_leftmost_leaf_pair_[num_matrices][i_]
x       #mid_ 无用！
x       k_, t_ = leftmost_leaf_
x       assert t_==k_+2
x       return k_
x   def bottomup_leftmost_front_(i_, j_, /):
x       assert i_ < j_
x       if i_+1==j_:
x           return
x       k_ = leftmost_idx_of_(i_, j_)
x       mids_ = [L_(k_+num_matrices) for num_matrices, begin2mids_ in enumerate(num_matrices2begin2mids_) if k_ in begin2mids_]
x       print(i_, j_)
x       print(k_, mids_)
x       unsorted_inner_arcs_.extend((k_, mid_) for mid_ in mids_)
x       todo_arcs_.extend(pairwise(mids_))
x   bottomup_leftmost_front_(0, L-1)
x   while todo_arcs_:
x       (i_, j_) = arc_ = todo_arcs_.pop()
x       bottomup_leftmost_front_(i_, j_)
x
x   sorted_inner_arcs_ = radix_sort__arcs(L, unsorted_inner_arcs_, None)
x   assert len(sorted_inner_arcs_) == max(0, L-3), sorted_inner_arcs_
x   mno = 0 if L==2 else num_matrices2mno_begin_mids_end_tpls_[L-1][0][0]
x   return (mno, L, imin, sorted_inner_arcs_)
x   r''[[[
x
x   unsorted_inner_arcs_ = []
x   def _put_todo(i_, j_, /):
x       assert 0 <= i_ < j_ < L
x       if j_-i_ >= 2:
x           arc_ = (i_, j_)
x           unsorted_inner_arcs_.append(arc_)
x           todo_arcs_.append(arc_)
x   #end-def _put_todo(i_, j_, /):
x   if 0:
x       #bug:L==2
x       todo_arcs_ = [(0, L-1)]
x   elif 0:
x       #bug: put into unsorted_inner_arcs_
x       todo_arcs_ = []
x       _put_todo(0, L-1)
x   else:
x       todo_arcs_ = [] if L==2 else [(0, L-1)]
x   while todo_arcs_:
x       (i_, j_) = arc_ = todo_arcs_.pop()
x       num_matrices = j_-i_
x       (mid_, leftmost_leaf_) = num_matrices2begin2mid_leftmost_leaf_pair_[num_matrices][i_]
x       _put_todo(i_, mid_)
x       _put_todo(mid_, j_)
x       #if arc_ == leftmost_leaf_:
x   sorted_inner_arcs_ = radix_sort__arcs(L, unsorted_inner_arcs_, None)
x   assert len(sorted_inner_arcs_) == max(0, L-3)
x   mno = 0 if L==2 else num_matrices2mno_begin_mids_end_tpls_[L-1][0][0]
x   return (mno, L, imin, sorted_inner_arcs_)
x   #]]]''

#end-def 词典序最先的最优三角化方案囗立方算法囗(矩阵乘法链维数序列, /, *, may_imin):
#]]]'''

r'''[[[
def xxx词典序最先的最优三角化方案囗立方算法囗(矩阵乘法链维数序列, /, *, may_imin):
x   '-> (mno, L, imin, sorted_inner_arcs_)'
x   #xxx :raise logic-err #算法思路有误，必须 先定位某个范围里的最小内边，再bottomup识别祖先，但 这有祖先，右侧全空，而且bottomup 需要控制 祖先范围
x   #   上面的想法已实现，只是仍有毛病:比如最小边为(0,6)，并非长度为2
x   raise logic-err #含有『未经证明TODO』的 片段
x   #   见『others/book/matrix_chain_product/Computation of matrix chain products I,II(1984)(Hu)(Shing)[polygon partitioning].pdf.txt』『找反例的过程』
x   #   存在反例:[ls=[70, 111, 185, 148, 74]]
x   (ls, imin, L, ls_, imin_) = 准备囗词典序最先的最优三角化方案(矩阵乘法链维数序列, may_imin=may_imin)
x   num_matrices2mno_begin_mids_end_tpls_ = matrix_chain_product__dynamic_programming__O_NNN(ls_)
x       #必须先偏移再列表，不能反转次序，否则，地基线/最低外边 选取不同，各自的自然成长树不同(树有根则有向，若无向化才会等同)，难求
x
x
x   if 0:
x       #通通取消
x       offset_idx_ = mk_offset_(L, imin)
x       def L_(i_, /):
x           return i_%L
x   else:
x       offset_idx_ = mk_offset_(L, 0)
x       def L_(i_, /):
x           return i_
x
x   num_matrices2begin2mids_ = []
x   for num_matrices, mno_begin_mids_end_tpls in enumerate(num_matrices2mno_begin_mids_end_tpls_):
x       assert len(num_matrices2begin2mids_) == num_matrices
x       begin2mids_ = {}
x       for mno, begin, mids, end in mno_begin_mids_end_tpls:
x           assert end-begin-1 == num_matrices
x           begin_ = offset_idx_(begin)
x           mids_ = [*map(offset_idx_, mids)]
x           begin2mids_[begin_] = mids_
x       num_matrices2begin2mids_.append(begin2mids_)
x   num_matrices2begin2mids_
x   #######
x   num_matrices2begin2mid_leftmost_node_pair_ = []
x   #def get_leftmost_leaf_(num_matrices, begin_, /):
x   def get_leftmost_node_or_self_(num_matrices, begin_, /):
x       #不必是叶节点，范围不一定是2
x       (mid_, leftmost_node_) = num_matrices2begin2mid_leftmost_node_pair_[num_matrices][begin_]
x       self_ = (*sorted([begin_, L_(begin_+num_matrices)]),)
x       leftmost_node_ = min(leftmost_node_, self_)
x       return leftmost_node_
x
x   for num_matrices, begin2mids_ in enumerate(num_matrices2begin2mids_):
x       assert len(num_matrices2begin2mid_leftmost_node_pair_) == num_matrices
x       begin2mid_leftmost_node_pair_ = {}
x       for begin_, mids_ in begin2mids_.items():
x           end_ = L_(num_matrices+begin_+1)
x           if num_matrices == 2:
x               [mid_] = mids_
x               assert mid_ == L_(begin_+1) == L_(end_-2)
x               leftmost_node_ = (*sorted([begin_, L_(begin_+num_matrices)]),)
x           else:
x               assert num_matrices >= 3
x               xs = []
x               for mid_ in mids_:
x                   if mid_ == L_(begin_+1):
x                       leftmost_node_ = get_leftmost_node_or_self_(num_matrices-L_(mid_-begin_), mid_)
x                   else:
x                       leftmost_node_ = get_leftmost_node_or_self_(L_(mid_-begin_), begin_)
x                   #bug:xs.append((leftmost_node_, +mid_))
x                   xs.append((leftmost_node_, -mid_))
x                       #未经证明TODO
x                       #   存在反例:[ls=[70, 111, 185, 148, 74]]
x
x               (leftmost_node_, mid_) = min(xs)
x           mid_leftmost_node_pair_ = (mid_, leftmost_node_)
x           begin2mid_leftmost_node_pair_[begin_] = mid_leftmost_node_pair_
x
x       num_matrices2begin2mid_leftmost_node_pair_.append(begin2mid_leftmost_node_pair_)
x   num_matrices2begin2mid_leftmost_node_pair_
x   #######
x   #######
x   #######
x   if 1:
x       print(num_matrices2mno_begin_mids_end_tpls_)
x       print(num_matrices2begin2mids_)
x       print(num_matrices2begin2mid_leftmost_node_pair_)
x   #######
x   unsorted_inner_arcs_ = []
x   todo_arcs_ = []
x   def mid_of_(i_, j_, /):
x       num_matrices = j_-i_
x       (mid_, leftmost_node_) = num_matrices2begin2mid_leftmost_node_pair_[num_matrices][i_]
x       return mid_
x   def topdown(i_, j_, /):
x       assert i_ < j_
x       if i_+1==j_:
x           return
x       mid_ = mid_of_(i_, j_)
x       print(i_, j_)
x       print(mid_)
x       _put_todo(i_, mid_)
x       _put_todo(mid_, j_)
x
x   def _put_todo(i_, j_, /):
x       assert 0 <= i_ < j_ < L
x       if j_-i_ >= 2:
x           arc_ = (i_, j_)
x           unsorted_inner_arcs_.append(arc_)
x           todo_arcs_.append(arc_)
x   #end-def _put_todo(i_, j_, /):
x   topdown(0, L-1)
x       #避开_put_todo
x   while todo_arcs_:
x       (i_, j_) = arc_ = todo_arcs_.pop()
x       topdown(i_, j_)
x
x   sorted_inner_arcs_ = radix_sort__arcs(L, unsorted_inner_arcs_, None)
x   assert len(sorted_inner_arcs_) == max(0, L-3), sorted_inner_arcs_
x   mno = 0 if L==2 else num_matrices2mno_begin_mids_end_tpls_[L-1][0][0]
x   return (mno, L, imin, sorted_inner_arcs_)

#end-def 词典序最先的最优三角化方案囗立方算法囗(矩阵乘法链维数序列, /, *, may_imin):

#]]]'''


def 词典序最先的最优三角化方案囗立方算法囗(矩阵乘法链维数序列, /, *, may_imin):
    '-> (mno, L, imin, sorted_inner_arcs_)'
    (ls, imin, L, ls_, imin_) = 准备囗词典序最先的最优三角化方案(矩阵乘法链维数序列, may_imin=may_imin)
    num_matrices2mno_begin_mids_end_tpls_ = matrix_chain_product__dynamic_programming__O_NNN(ls_)
    if 0:
        #通通取消
        offset_idx_ = mk_offset_(L, imin)
        def L_(i_, /):
            return i_%L
    else:
        offset_idx_ = mk_offset_(L, 0)
        def L_(i_, /):
            return i_

    num_matrices2begin2mids_ = []
    for num_matrices, mno_begin_mids_end_tpls in enumerate(num_matrices2mno_begin_mids_end_tpls_):
        assert len(num_matrices2begin2mids_) == num_matrices
        begin2mids_ = {}
        for mno, begin, mids, end in mno_begin_mids_end_tpls:
            assert end-begin-1 == num_matrices
            begin_ = offset_idx_(begin)
            mids_ = [*map(offset_idx_, mids)]
            begin2mids_[begin_] = mids_
        num_matrices2begin2mids_.append(begin2mids_)
    num_matrices2begin2mids_
    #######
    num_matrices2begin2mid_leftmost_nodes_pair_ = []
    def mk_leftmost_nodes_or_self_(num_matrices, begin_, /):
        #最左不必是叶节点，范围不一定是2
        if num_matrices >= 2:
            (mid_, leftmost_nodes_) = num_matrices2begin2mid_leftmost_nodes_pair_[num_matrices][begin_]
        else:
            leftmost_nodes_ = []
        return leftmost_nodes_

    for num_matrices, begin2mids_ in enumerate(num_matrices2begin2mids_):
        assert len(num_matrices2begin2mid_leftmost_nodes_pair_) == num_matrices
        begin2mid_leftmost_nodes_pair_ = {}
        for begin_, mids_ in begin2mids_.items():
            end_ = L_(num_matrices+begin_+1)
            self_ = (*sorted([begin_, L_(begin_+num_matrices)]),)
            xs = []
            for mid_ in mids_:
                if mid_ == L_(begin_+1):
                    leftmost_nodes_ = mk_leftmost_nodes_or_self_(num_matrices-L_(mid_-begin_), mid_)
                else:
                    leftmost_nodes_ = mk_leftmost_nodes_or_self_(L_(mid_-begin_), begin_)
                leftmost_nodes_ = [*leftmost_nodes_, self_]
                xs.append((leftmost_nodes_, mid_))

            (leftmost_nodes_, mid_) = min(xs)
            leftmost_nodes_ = min([self_,], leftmost_nodes_)
            mid_leftmost_nodes_pair_ = (mid_, leftmost_nodes_)
            begin2mid_leftmost_nodes_pair_[begin_] = mid_leftmost_nodes_pair_

        num_matrices2begin2mid_leftmost_nodes_pair_.append(begin2mid_leftmost_nodes_pair_)
    num_matrices2begin2mid_leftmost_nodes_pair_
    #######
    #######
    #######
    if 0:
        print(num_matrices2mno_begin_mids_end_tpls_)
        print(num_matrices2begin2mids_)
        print(num_matrices2begin2mid_leftmost_nodes_pair_)
    #######
    unsorted_inner_arcs_ = []
    todo_arcs_ = []
    def mid_of_(i_, j_, /):
        num_matrices = j_-i_
        (mid_, leftmost_nodes_) = num_matrices2begin2mid_leftmost_nodes_pair_[num_matrices][i_]
        return mid_
    def topdown(i_, j_, /):
        assert i_ < j_
        if i_+1==j_:
            return
        mid_ = mid_of_(i_, j_)
        #print(i_, j_)
        #print(mid_)
        _put_todo(i_, mid_)
        _put_todo(mid_, j_)

    def _put_todo(i_, j_, /):
        assert 0 <= i_ < j_ < L
        if j_-i_ >= 2:
            arc_ = (i_, j_)
            unsorted_inner_arcs_.append(arc_)
            todo_arcs_.append(arc_)
    #end-def _put_todo(i_, j_, /):
    topdown(0, L-1)
        #避开_put_todo
    while todo_arcs_:
        (i_, j_) = arc_ = todo_arcs_.pop()
        topdown(i_, j_)

    sorted_inner_arcs_ = radix_sort__arcs(L, unsorted_inner_arcs_, None)
    assert len(sorted_inner_arcs_) == max(0, L-3), sorted_inner_arcs_
    mno = 0 if L==2 else num_matrices2mno_begin_mids_end_tpls_[L-1][0][0]
    return (mno, L, imin, sorted_inner_arcs_)

#end-def 词典序最先的最优三角化方案囗立方算法囗(矩阵乘法链维数序列, /, *, may_imin):






def 准备囗词典序最先的最优三角化方案(矩阵乘法链维数序列, /, *, may_imin):
    '-> (ls, imin, L, ls_, imin_)'
    check_matrix_chain_product_arg(矩阵乘法链维数序列)
    ls = 矩阵乘法链维数序列
    L = len(ls)
    if may_imin is None:
        imin = min(range(L), key=lambda i:ls[i])
    else:
        imin = may_imin
        check_uint_lt(L, imin)
        if not ls[imin] == min(ls): raise ValueError
    check_uint_lt(L, imin)

    ls_ = SeqLeftRotateView(ls, imin)
    imin_ = 0
    return (ls, imin, L, ls_, imin_)


def sort_idc_of_seq(ls, /, *, reverse=False, key=None):
    L = len(ls)
    ls[:0]
    if key is None:
        key = echo
    def key_(i, /):
        return key(ls[i])
    return sorted(range(L), key=key_)

def sort_idc(iterable, /, *, reverse=False, key=None):
    if key is None:
        key = echo
    it = ((key(v), i) for i,v in enumerate(iterable))
    ls = sorted(it, key=fst, reverse=reverse)
    ls = [*map(snd, ls)]
    return ls



#one_sweep_algorithm
#def collect_idx_pph_arcs_that_cut_local_max(imin, imax, i2xv, /):
def collect_idx_pph_arcs_that_cut_local_max(imin, i2xv, /):
    'imin/idx -> i2xv[#ls/i2rv/[pint]{L} or inv_idc/i2vv/[vv]{L}#] -> (idx_pph_arcs/[(idx,idx)]{L-3}, [idx]{3})'
    #output (L-3) arcs
    L = len(i2xv)
    if not L >= 3: raise IndexError#LengthError
    if not 0 <= imin < L >= 3: raise IndexError
    #if not 0 <= imax < L >= 3: raise IndexError
    if not i2xv[imin] == min(i2xv): raise ValueError
    #rint(f'i2xv = {i2xv}')

    def i2v(i, /):
        return i2xv[i], (i-imin)%L
            #not bug
        return i2xv[i]
        #???not bug:return i2xv[i], (i-imin)%L
        #   可能在降序阶段 变升序

    if 0:
        r'''[[[
        imax_ = (imax-imin)%L
        def i2v(i, /):
            ##???不对！这是通用的，非专业于 单调多边形！
            i_ = (i-imin)%L
            b = i_>=imax_
            return (i2xv[i], b, (-i_ if b else i_))
        #]]]'''

    def lt(i,j,/):
        return i2v(i) < i2v(j)
    def pop_(idx, /):
        idx1 = idx_stack.pop() #discard
        idx0 = idx_stack[-1]
        # idx0 *<=* idx1 *>* idx
        #assert not lt(idx1, idx0)
        #assert lt(idx, idx1)
        #idx_pph_arcs.append(tuple(sorted([idx,idx0])))
        #idx_pph_arcs.append((idx,idx0))
        idx_pph_arcs.append((idx0,idx))
        return
    ilast = (imin-1)%L
    it = chain(range(imin+1, L), range(0, imin))
    idx_stack = [imin]
    idx_pph_arcs = []
    #第一阶段:不处理 最后一个 idx
    ###now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v)
    for idx in it:
        #rint(f'idx = {idx}')
        #rint(f'i2v(idx) = {i2v(idx)}')
        #assert len(idx_stack) >= 1
        ###now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v)
        if idx == ilast:
            for _ in it: raise logic-err
            break
        while lt(idx, idx_stack[-1]):
            #assert len(idx_stack) >= 2
            pop_(idx)
            #assert len(idx_stack) >= 1
        #assert len(idx_stack) >= 1
        #assert not lt(idx, idx_stack[-1])
        idx_stack.append(idx)
        #rint(idx_stack)
        #assert len(idx_stack) >= 2
        ###now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v)
    else:
        raise logic-err
    ###now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v)
    assert len(idx_stack) >= 2
    if not len(idx_stack)+len(idx_pph_arcs) == L-1: raise logic-err

    #第二阶段:处理 最后一个 idx
    while lt(idx, idx_stack[-1]) and len(idx_stack) >= 3:
        #assert len(idx_stack) >= 3
        ###now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v)
        pop_(idx)
        #assert len(idx_stack) >= 2
        ###now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v)
    #assert len(idx_stack) >= 2
    assert lt(idx_stack[-1], idx) or len(idx_stack) == 2
    ###now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v)
    idx_stack.append(idx)
    #assert len(idx_stack) >= 3
    #####now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v) or idx_stack == [i0,i2,i1]
    while len(idx_stack) > 3:
        ###now:i2v allow eq:xxx assert is_strict_sorted(idx_stack, key=i2v)
        pop_(imin)
    assert len(idx_stack) == 3
    assert len(idx_pph_arcs) == L-3
    #assert idx_stack == [i0,i1,i2] or idx_stack == [i0,i2,i1]
    return idx_pph_arcs, idx_stack


def collect_vv_pph_arcs_that_cut_local_max(vv2i, i2vv, /):
    'idc/vv2i/[i]{L} -> i2vv -> vv_pph_arcs/[(vv,vv)]{L-3}'
    #output (L-3) arcs
    L = len(vv2i)
    if not L >= 3: raise IndexError#LengthError

    def pop_(vv, /):
        vv1 = vv_stack.pop() #discard
        vv0 = vv_stack[-1]
        #assert vv0 < vv1
        #assert vv < vv1
        #vv_pph_arcs.append(tuple(sorted([vv,vv0])))
        #vv_pph_arcs.append((vv,vv0))
        vv_pph_arcs.append((vv0,vv))
        return
    i0 = imin = vv2i[0]
    ilast = (imin-1)%L
    it = chain(range(imin+1, L), range(0, imin))
    assert i2vv[i0] == 0
    vv_stack = [0]
    vv_pph_arcs = []
    #第一阶段:不处理 最后一个 vv
    for i in it:
        #assert len(vv_stack) >= 1
        vv = i2vv[i]
        if i == ilast:
            for _ in it: raise logic-err
            break
        while vv < vv_stack[-1]:
            #assert len(vv_stack) >= 2
            pop_(vv)
            #assert len(vv_stack) >= 1
        #assert len(vv_stack) >= 1
        assert vv > vv_stack[-1]
        vv_stack.append(vv)
        #assert len(vv_stack) >= 2
    else:
        raise logic-err
    assert len(vv_stack) >= 2
    if not len(vv_stack)+len(vv_pph_arcs) == L-1:
        raise logic-err

    #第二阶段:处理 最后一个 vv
    while vv < vv_stack[-1] and len(vv_stack) >= 3:
        #assert len(vv_stack) >= 3
        pop_(vv)
        #assert len(vv_stack) >= 2
    #assert len(vv_stack) >= 2
    assert vv > vv_stack[-1] or len(vv_stack) == 2
    #assert is_strict_sorted(vv_stack)
    vv_stack.append(vv)
    #assert len(vv_stack) >= 3
    #assert is_strict_sorted(vv_stack) or vv_stack == [0,2,1]
    while len(vv_stack) > 3:
        #assert is_strict_sorted(vv_stack)
        pop_(0)
    assert len(vv_stack) == 3
    assert len(vv_pph_arcs) == L-3
    assert vv_stack == [0,1,2] or vv_stack == [0,2,1]
    return vv_pph_arcs

if 0:
  ##???bug:
  #not bug, but api changed
  #one_sweep_algorithm#protect kk:=idx to 3th min value
  def collect_arcs_that_cut_local_max__first_idx_get_min_value(i2v, idc, /):
    'idc/[i]{L} -> inv_idc/[i]{L} -> ([(i,i)]{L-3}, (i,i,i))'
    #output (L-3) arcs
    L = len(idc)
    if not L >= 3: raise IndexError#LengthError
    [ii,jj,kk] = nsmallest(3, idc, key=i2v)
    if not ii == idc[0]: raise ValueError
    #protect:should not pop kk

    it = iter(idc);del idc
    stack = []
    arcs = []
    for i0 in it:
        assert i0 == ii
        stack.append(i0)
    for i1 in it:
        stack.append(i1)
    def lt(i,j,/):
        return i2v(i) < i2v(j)
    assert len(stack) >= 2
    for i in it:
        while lt(i, stack[-1]):
            assert len(stack) >= 2
            ilocal_max = stack.pop()
            if ilocal_max == kk:
                assert i == jj
                stack.append(kk)
                assert len(stack) == 2
                break
            arc = (stack[-1], i)
            arcs.append(arc)
            assert stack
        assert stack
        stack.append(i)
        assert len(stack) >= 2
    assert len(stack) >= 3
    while len(stack) > 3:
        ilocal_max = stack.pop()
        assert not ilocal_max == kk
        arc = (stack[-1], ii)
        arcs.append(arc)
    assert len(stack) == 3
    assert len(arcs) == L-3 >= 0
    assert stack == [ii, jj, kk] or stack == [ii, kk, jj]
    return arcs, stack

def merge_sort__2(lhs, rhs, /, *, key):
    return merge_two_sorted_iterables(lhs, rhs, left_key=key, right_key=key)

def matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(矩阵乘法链维数序列, /):
    '-> (MNO4whole, imin, may (imax_, idx_ceil_arcs_, idx_h_arcs_, idx_all_inner_arcs_)) #offseted!! should +imin%L'
    check_matrix_chain_product_arg(矩阵乘法链维数序列)
    ls = 矩阵乘法链维数序列
    L = len(ls)
    imin = min(range(L), key=ls.__getitem__)
    ls_ = SeqLeftRotateView(ls, imin)
    imin_ = 0
    imax_ = max(reversed(range(L)), key=ls_.__getitem__)
        #imin右侧最远的imax
    imax = (imax_+imin)%L
    save = (ls, imin, imax)
    del ls, imin, imax
    ls_, imin_, imax_

    #pairwise
    if not is_sorted(ls_[i] for i in range(imax_)):raise ValueError#单调的矩阵乘法链维数序列
    if not is_sorted(ls_[i] for i in reversed(range(imax_, L))):raise ValueError#单调的矩阵乘法链维数序列


    if L == 2:
        (ls, imin, imax) = save
        MNO4whole = 0
        return (MNO4whole, imin, None)
    assert L >= 3

    i2rv_ = ls_
    idx_pph_arcs, idx_stack = collect_idx_pph_arcs_that_cut_local_max(imin_, i2rv_)
    if 0:
        #bug: not at tail
        while idx_ph_arcs and imin_ in idx_ph_arcs[-1]:
            #bug:case(0,9,4)->arc(0,4):while idx_ph_arcs and idx_ph_arcs[-1][1]==imin_:
            idx_ph_arcs.pop()
    if 0:
        idx_ph_arcs = [arc for arc in idx_ph_arcs if not imin_ in arc]
        assert not any(idx_ == imin_ for arc in idx_ph_arcs for idx_ in arc), idx_ph_arcs
        idx_ph_arcs = [arc for arc in idx_ph_arcs if arc[0] < imax_ < arc[1]]
    def fw(i_,/):
        return ls_[i_], i_
    # 关于one_sweep_algorithm后续修正:见: [词典序最先的最优三角化方案囗潜在的横对角线的必要条件] #not:[无用囗词典序最先的最优三角化方案囗横对角线的必要条件]
    # 要求:单调多边形情形下 简化为: [(x_,y_) := sorted(arc, key=fw)][(i_,j_) := sorted(arc)][imin_ < i_ < imax_ < j_][fw(imin_) < fw(x_) <= fw(y_) < min(fw(i_+1),fw(j_-1))]
    # not 要求:单调多边形情形下 简化为: [(i_,j_) := sorted(arc)][imin_ < i_ < imax_ < j_][ls_[imin_] < min(ls_[i_],ls_[j_]) <= max(ls_[i_],ls_[j_]) < min(ls_[i_+1],ls_[j_-1])]
    #
    if 0:
        def is_idx_ph_arc4mono_polygon(arc, /):
            (i_,j_) = sorted(arc)
            (x_,y_) = sorted(arc, key=fw)
            return (fw(imin_) < fw(x_) <= fw(y_) < min(fw(i_+1),fw(j_-1)))
            return (imin_ < i_ < imax_ < j_ and fw(imin_) < fw(x_) <= fw(y_) < min(fw(i_+1),fw(j_-1)))
        idx_ph_arcs = [*filter(is_idx_ph_arc4mono_polygon, idx_pph_arcs)]


    ##!!#重启！:[无用囗词典序最先的最优三角化方案囗横对角线的必要条件]
    # 并非无用，而是必要，用以应付:[11,33,22,22,11]
    #之前为何觉得有毛病？因为之前 H0只考虑一种情形，导致ls=[11,11,33,22] 出错:(1,3)是pph,是ph,不满足h_arc必要条件[11=11],但构成 最优解
    #   在考虑H0的第二种可能后，(1,3)会以 竖对角线 的身份回归
    if 0:
        def is_idx_ph_arc4mono_polygon(arc, /):
            (i_,j_) = sorted(arc)
            return (ls_[imin_] < min(ls_[i_],ls_[j_]) <= max(ls_[i_],ls_[j_]) < min(ls_[i_+1],ls_[j_-1]))
        idx_ph_arcs = [*filter(is_idx_ph_arc4mono_polygon, idx_pph_arcs)]

    #论文本身有bug！
    #现启用自定义『除零的类横对角线囗第二版』
    #现在 还需证明:
        #对应于:[横对角线是潜在的潜在的横对角线]
        #[第二版的除零的类横对角线是无印版的潜在的潜在的横对角线]
            #已证明
            #这个命名不太行:[除零的类横对角线是潜在的潜在的横对角线囗第二版]
        #[若某词典序最先的最优三角化方案不含第二版的除零的类横对角线则该方案为聚焦于最小处的扇形方案]
            #已证明
            #即 H0只有一种情形

    #[有用囗词典序最先的最优三角化方案囗横对角线的必要条件囗第二版]
    def is_除零的类横对角线囗第二版4mono_polygon(arc, /):
        (i_,j_) = sorted(arc)
        return (imin_ < i_ < j_) and (max(ls_[i_],ls_[j_]) < min(ls_[i_+1],ls_[j_-1]))
            #对比前面:return (ls_[imin_] < min(ls_[i_],ls_[j_]) <= max(ls_[i_],ls_[j_]) < min(ls_[i_+1],ls_[j_-1]))
    idx_removed_imin_psuedo_h_arcs = [*filter(is_除零的类横对角线囗第二版4mono_polygon, idx_pph_arcs)]

    if 0:
        # 废弃:『有效的类横对角线囗第二版』
        def 保留唯一边或保留次低边(arcs, /):
            def f():
                raise 'TODO:唯一边'
                i2count = [0]*L
                for arc in reversed(arcs):
                    #arcs 由高至低
                    (i_,j_) = arc
                    if i2count[i_] == 1 or i2count[j_] == 1:
                        yield arc
                    i2count[i_] += 1
                    i2count[j_] += 1
            arcs = [*f()]
            arcs.reverse()
            return arcs

        idx_ph_arcs = 保留唯一边或保留次低边(idx_removed_imin_psuedo_h_arcs)
    idx_ph_arcs = (idx_removed_imin_psuedo_h_arcs)








    def side_product_between(curr_arc, ceil_arc, /):
        if ceil_arc is top_arc:
            return side_product(curr_arc)
        return side_product(curr_arc) -side_product(ceil_arc) +base_product(ceil_arc)
    def side_product(idx_arc, /):
        (i_,j_) = idx_arc
        return side_products__from0[j_] -side_products__from0[i_]
    if 1:
        #not bug:
        def base_product(idx_arc, /):
            (i_,j_) = idx_arc
            assert i_ < j_
            return (ls_[i_] * ls_[j_])
    else:
        def base_product(idx_arc, /):
            (i_,j_) = idx_arc
            if i_ == j_:
                return 0
            return (ls_[i_] * ls_[j_])
    side_products__from0 = [0]
    def _():
        for i_ in range(1, L):
            side_products__from0.append(side_products__from0[-1]+base_product((i_-1,i_)))
    _()
    assert len(side_products__from0)==L


    def _H0(curr_arc, above_arc, /):
        if above_arc is top_arc:
            assert 0 < imax_
            if 1 < imax_:
                (x_,y_) = (imax_-1, imax_)
            else:
                (x_,y_) = (imax_, imax_+1)
        else:
            (x_,y_) = above_arc
        assert 0 < x_ < y_ < L
        if curr_arc is bottom_arc:
            (i_,j_) = (0, L-1)
        else:
            (i_,j_) = curr_arc
            assert 0 < i_ < j_ < L
        assert 0 <= i_ <= x_ < y_ <= j_ < L, ((i_, x_, y_, j_, L), (curr_arc, above_arc), (imin_, imax_), idx_ph_arcs)
        return (i_, x_, y_, j_)

    def H0(curr_arc, above_arc, /):
        r'''[[[
使用『横对角线囗第二版』...
    ==>> H0 只有一种情形:聚焦于局部i0
bug:[[注意:基本多边形的fan扇形三角化方案/聚焦型三角化方案 有 两种可能！！！
  聚焦于i0或i1
  [[ls[i0] == ls[i1]] -> [聚焦于i1]]
  [[ls[i0] < ls[i1]] -> [聚焦于i0]]
  ]]

        #]]]'''
        (i_, x_, y_, j_) = _H0(curr_arc, above_arc)
        if (ls_[i_] <= ls_[j_]):
            k_ = i_
            if k_ == x_:
                return ls_[k_]*side_product((y_,j_))
            else:
                return ls_[k_]*(side_product((i_+1,x_))+base_product((x_,y_))+side_product((y_,j_)))
        else:
            k_ = j_
            if k_ == y_:
                return ls_[k_]*side_product((i_,x_))
            else:
                return ls_[k_]*(side_product((i_,x_))+base_product((x_,y_))+side_product((y_,j_-1)))
                return ls_[k_]*(side_product((i_,x_))+base_product((x_,y_))+side_product((y_,j_+1)))
                    #bug?: [j_+1==L]
        pass
    def arc2min_weight(idx_arc, /):
        if idx_arc is bottom_arc:
            return ls_[imin_]
        (i_,j_) = idx_arc
        return min(ls_[i_], ls_[j_])
    def bind_get_set(d, /):
        def get(k, /):
            return d[id(k)]
        def set(k, v, /):
            assert id(k) not in d
            d[id(k)] = v
        return get, set
    r'''[[[
    def get_supporting_weight_of
    def set_supporting_weight_of
    def get_ceil_arc_of
    def set_ceil_arc_of
    def get_MNO4high_half_above_
    def set_MNO4high_half_above_
    def add_child_of
    #]]]'''
    (get_supporting_weight_of
    ,set_supporting_weight_of) = bind_get_set({})
    (get_ceil_arc_of
    ,set_ceil_arc_of) = bind_get_set({})
    (get_MNO4high_half_above_
    ,set_MNO4high_half_above_) = bind_get_set({})
    def add_child_of(arc, child, /):
        arc2children[id(arc)].append(child)
    arc2children = defaultdict(list)

    #[supporting_weight4imax == 0 < 1 <= ls[imin] == min(ls)] ==>> imax 永远有效存在于 最优解
    #bug:-1没错！:bug:因为『?//D』supporting_weight4curr_arc可能为0，supporting_weight4imax改为-1
    #   因为『?//D』中的『?』可能小于0，这也是 最后能存在的保证
    #   改用neg_oo
    #   改回-1
    top_arc = True #imax
    bottom_arc = False #imin
    supporting_weight4imax = -1 #= neg_oo
    MNO4high_half4imax = 0
    above_arc = top_arc
    set_supporting_weight_of(above_arc, supporting_weight4imax)
    set_MNO4high_half_above_(above_arc, MNO4high_half4imax)

    idx_ph_arcs.append(bottom_arc)
    for curr_arc in idx_ph_arcs:
        min_weight4curr_arc = arc2min_weight(curr_arc)
        while not get_supporting_weight_of(above_arc) < min_weight4curr_arc:
        #while not supporting_weight4above_arc < min_weight4curr_arc:
            #above_arc = remove_above_arc(above_arc)
            above_arc = get_ceil_arc_of(above_arc)
            #   [supporting_weight4imax==-1 < 1 <= min_weight4curr_arc]
            #   above_arc 最高 止于 imax
        #assert get_supporting_weight_of(above_arc) < min_weight4curr_arc:
        ceil_arc = above_arc
        MNO4high_half4curr_arc = get_MNO4high_half_above_(ceil_arc) + H0(curr_arc, ceil_arc)
        #rint(f'curr_arc = {curr_arc}')
        #rint(f'MNO4high_half4curr_arc = {MNO4high_half4curr_arc}')

        if curr_arc is bottom_arc:
            set_ceil_arc_of(curr_arc, ceil_arc)
            set_MNO4high_half_above_(curr_arc, MNO4high_half4curr_arc)
            break

        #定位:ceil_arc<curr_arc> #除去child 的 最低 above_arc
        #supporting_weight4curr_arc<ceil_arc>
        while 1:
            #rint(f'ceil_arc = {ceil_arc}')
            D = (side_product_between(curr_arc, ceil_arc) -base_product(curr_arc))
            assert D > 0
            supporting_weight4curr_arc = (MNO4high_half4curr_arc-get_MNO4high_half_above_(ceil_arc))//D
            #rint(f'D = {D}')
            #rint(f'supporting_weight4curr_arc = {supporting_weight4curr_arc}')

            if get_supporting_weight_of(ceil_arc) < supporting_weight4curr_arc:
                break
            #ceil_arc is child of curr_arc, hence not a ceil_arc
            add_child_of(curr_arc, ceil_arc)
            ceil_arc = get_ceil_arc_of(ceil_arc)
        #assert get_supporting_weight_of(ceil_arc) < supporting_weight4curr_arc
        #   [supporting_weight4imax==-1 < 0 <= supporting_weight4curr_arc]
        #   ceil_arc 最高 止于 imax
        set_ceil_arc_of(curr_arc, ceil_arc)
        ########next round
        above_arc = curr_arc
        set_MNO4high_half_above_(curr_arc, MNO4high_half4curr_arc)
        set_supporting_weight_of(curr_arc, supporting_weight4curr_arc)
    #end-while
    ...

    MNO4whole = get_MNO4high_half_above_(bottom_arc)
    idx_ceil_arcs_ = []
    ceil_arc = get_ceil_arc_of(bottom_arc)
    while not ceil_arc is top_arc:
        idx_ceil_arcs_.append(ceil_arc)
        ceil_arc = get_ceil_arc_of(ceil_arc)
    idx_h_arcs_ = []
    def put_h_arcs(h_arcs, /):
        for h_arc in h_arcs:
            put_h_arc(h_arc)
    def put_h_arc(h_arc, /):
        idx_h_arcs_.append(h_arc)
        put_h_arcs(arc2children[id(h_arc)])
    put_h_arcs(idx_ceil_arcs_)

    idx_all_inner_arcs_ = []
    def iter_v_arcs_between(low_arc, h_arc, /):
        #bug:(i_, x_, y_, j_) = _H0(curr_arc, above_arc)
        (i_, x_, y_, j_) = _H0(low_arc, h_arc)
        #rint((i_, x_, y_, j_))
        if (ls_[i_] <= ls_[j_]):
            k_ = i_
            if k_ == x_:
                #return ls_[k_]*side_product((y_,j_))
                for t_ in range(y_+1, j_):
                    yield (k_, t_)
            else:
                #return ls_[k_]*(side_product((i_+1,x_))+base_product((x_,y_))+side_product((y_,j_)))
                for t_ in range(i_+2, x_+1):
                    yield (k_, t_)
                for t_ in range(y_, j_):
                    yield (k_, t_)
        else:
            k_ = j_
            if k_ == y_:
                #return ls_[k_]*side_product((i_,x_))
                for t_ in range(i_+1, x_):
                    yield (t_, k_)
            else:
                #return ls_[k_]*(side_product((i_,x_))+base_product((x_,y_))+side_product((y_,j_-1)))
                for t_ in range(i_+1, x_+1):
                    yield (t_, k_)
                for t_ in range(y_, j_-1):
                    yield (t_, k_)
        pass

    def put_v_arcs_between(low_arc, h_arc, /):
        #rint((low_arc, h_arc))
        #rint([*iter_v_arcs_between(low_arc, h_arc)])
        idx_all_inner_arcs_.extend(iter_v_arcs_between(low_arc, h_arc))
    imin_, imax_
    low_arc = bottom_arc
    for h_arc in idx_h_arcs_:
        put_v_arcs_between(low_arc, h_arc)
        idx_all_inner_arcs_.append(h_arc)
        low_arc = h_arc
    put_v_arcs_between(low_arc, top_arc)

    (ls, imin, imax) = save
    return (MNO4whole, imin, (imax_, idx_ceil_arcs_, idx_h_arcs_, idx_all_inner_arcs_))#offseted!! should +imin%L

#end-def matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(矩阵乘法链维数序列, /):
    r'''[[[
    check_matrix_chain_product_arg(矩阵乘法链维数序列)
    ls = 矩阵乘法链维数序列
    L = len(ls)
    imin = min(range(L), key=ls.__getitem__)

    #imax = max(range(L), key=ls.__getitem__)
    def unoffset_(i, /):
        return (i+imin)%L
    imax = max(map(unoffset_, reversed(range(L))), key=ls.__getitem__)
        #imin左侧最近的imax
        #imin右侧最远的imax

    #bug:if not is_sorted(ls[imin-L:imax])
    #pairwise
    if not is_sorted(ls[i] for i in range(imin-L,imax)):raise ValueError#单调的矩阵乘法链维数序列
    if not is_sorted(ls[i] for i in reversed(range(imax-L,imin))):raise ValueError#单调的矩阵乘法链维数序列


    if 0:
        unoffseted_idc = [*map(unoffset_, range(L))]
        arcs, _ = collect_arcs_that_cut_local_max__first_idx_get_min_value(ls.__getitem__, unoffseted_idc)
        assert len(arcs) == L - 3
        assert (not arcs)> or (arcs[0][0]+1)%L == imax
                #imin右侧最远的imax

    if 0:
        i2rv = ls
        idx_pph_arcs, idx_stack = collect_idx_pph_arcs_that_cut_local_max(imin, i2rv)

    if 0:
        if 0:
            unoffseted_idc = [*map(unoffset_, range(L))]
            assert unoffseted_idc[imin-imin] == imin
            assert unoffseted_idc[imax-imin] == imax
            #bug?:
            vv2i = idc = [*merge_sort__2(unoffseted_idc[:imax-imin], reversed(unoffseted_idc[imax-imin:]), key=ls.__getitem__)]
                #reversed(unoffseted_idc[imax-imin:]) 并不保持稳定性
        offseted_imax = (imax-imin)%L
        vv2i = idc = [*map(unoffset_, merge_sort__2(range(0,offseted_imax), reversed(range(offseted_imax,L)), key=lambda i:(ls[(i+imin)%L],i)))]
        assert vv2i[0] == imin
        i2vv = inv_idc = inverse_uint_bijection_array(vv2i)
        vv_pph_arcs = collect_vv_pph_arcs_that_cut_local_max(vv2i, i2vv)

    #supporting_weight4imax == 0 < 1 <= ls[imin] == min(ls)
    supporting_weight4imax = 0
    for i in range(L):
        TODO
    #]]]'''
#end-def matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(矩阵乘法链维数序列, /):


矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法 = matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N

#mno_tree
def std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(矩阵乘法链维数序列, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    result = matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(矩阵乘法链维数序列)
    mno_tree = tail4std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(矩阵乘法链维数序列, result)
    return mno_tree


def tail4std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(矩阵乘法链维数序列, result, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    (MNO4whole, imin, may) = result
    ls = 矩阵乘法链维数序列
    L = len(ls)
    def f():
        if L==2:
            assert may is None
            if 0:
                i = 0
                return (0,i,(ls[i],ls[i+1]))
            MNO4whole = 0
            inner_arcs = []
        else:
            assert L >= 3
            (MNO4whole, imin, (imax_, idx_ceil_arcs_, idx_h_arcs_, idx_all_inner_arcs_)) = result
            #rint(f'idx_all_inner_arcs_ = {idx_all_inner_arcs_}')
            #rint(f'(MNO4whole, imin, (imax_, idx_ceil_arcs_, idx_h_arcs_, idx_all_inner_arcs_)) = {result}')
            unsorted_inner_arcs = unoffset_arcs_(L, imin, idx_all_inner_arcs_)
                #??mk_sorted_unoffseted_arcs_from_unsorted_offseted_arcs_
        return MNO4whole, unsorted_inner_arcs


    MNO4whole, unsorted_inner_arcs = f()
    #rint(f'unsorted_inner_arcs = {unsorted_inner_arcs}')

    end4ground_outer_arc = 0
    mno_tree = mk_mno_tree_from_unsorted_inner_arcs(ls, end4ground_outer_arc, unsorted_inner_arcs)
        #binary_arc_tree = mk_binary_arc_tree_from_unsorted_inner_arcs(L, end4ground_outer_arc, unsorted_inner_arcs)
        #mno_tree = mk_mno_tree_from_binary_arc_tree(ls, binary_arc_tree)
    assert MNO4whole == mno_tree[0], (L, ls, unsorted_inner_arcs, MNO4whole, mno_tree)
    return mno_tree

r'''[[[
mno_tree <-> inner_arcs
    mno_tree <-> binary_arc_tree
    binary_arc_tree <-> inner_arcs

    mk_sorted_unoffseted_arcs_from_unsorted_offseted_arcs_
    mk_inner_arcs_from_binary_arc_tree
    mk_binary_arc_tree_from_unsorted_inner_arcs
    mk_mno_tree_from_binary_arc_tree
    mk_binary_arc_tree_from_mno_tree
    mk_inner_arcs_from_mno_tree
    mk_mno_tree_from_unsorted_inner_arcs
#]]]'''

def radix_sort__arcs(L, unsorted_arcs, may_table, /):
    if may_table is None:
        table = [[] for _ in range(L)]
    else:
        table = may_table
    sorted_arcs = radix_sort_with_table([L,L], unsorted_arcs, table)
    return sorted_arcs
def mk_sorted_unoffseted_arcs_from_unsorted_offseted_arcs_(L, imin, unsorted_offseted_arcs_, /):
    unsorted_unoffseted_arcs = unoffset_arcs_(L, imin, unsorted_offseted_arcs_)
    sorted_unoffseted_arcs = radix_sort__arcs(L, unsorted_unoffseted_arcs, None)
    return sorted_unoffseted_arcs
def mk_mno_tree_from_unsorted_inner_arcs(矩阵乘法链维数序列, end4ground_outer_arc, unsorted_inner_arcs, /):
    L = len(矩阵乘法链维数序列)
    binary_arc_tree = mk_binary_arc_tree_from_unsorted_inner_arcs(L, end4ground_outer_arc, unsorted_inner_arcs)
    mno_tree = mk_mno_tree_from_binary_arc_tree(矩阵乘法链维数序列, binary_arc_tree)
    return mno_tree
def mk_inner_arcs_from_mno_tree(L, mno_tree, /):
    binary_arc_tree = mk_binary_arc_tree_from_mno_tree(L, mno_tree)
    inner_arcs = mk_inner_arcs_from_binary_arc_tree(L, binary_arc_tree)
    return inner_arcs
def mk_inner_arcs_from_binary_arc_tree(L, binary_arc_tree, /):
    assert L >= 2
    unsorted_inner_arcs = []
    todo_ls = [binary_arc_tree]
    while todo_ls:
        (root_arc, may_) = todo_ls.pop()
        if may_ is None:
            continue
        unsorted_inner_arcs.append(root_arc)
        (_, lhs_binary_arc_tree, rhs_binary_arc_tree) = may_
        todo_ls.append(lhs_binary_arc_tree)
        todo_ls.append(rhs_binary_arc_tree)
    assert len(unsorted_inner_arcs) == max(1, L-2)
    assert unsorted_inner_arcs
    del unsorted_inner_arcs[0]
    assert len(unsorted_inner_arcs) == max(0, L-3)
    sorted_inner_arcs = radix_sort__arcs(L, unsorted_inner_arcs, None)
    return sorted_inner_arcs

def mk_binary_arc_tree_from_mno_tree(L, mno_tree, /):
    'binary_arc_tree = (root_arc, may ((root_arc[1], mid, root_arc[0]), binary_arc_tree, binary_arc_tree))'
    'mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    def recur(mno_tree, /):
        if mno_tree[0] == 0:
            assert len(mno_tree)==3
            (_0,i,_ls_i_i1) = mno_tree
            i1 = (i+1)%L
            root_arc = leaf_arc = (i1, i)
            binary_arc_tree = (root_arc, None)
        else:
            assert len(mno_tree)==7
            (mno, begin, lhs_mno_tree, mid, rhs_mno_tree, end, ls_b_m_eneg1) = mno_tree
            root_arc = (end-1, begin)
            lhs_binary_arc_tree = recur(lhs_mno_tree)
            rhs_binary_arc_tree = recur(rhs_mno_tree)
            binary_arc_tree = (root_arc, ((root_arc[1], mid, root_arc[0]), lhs_binary_arc_tree, rhs_binary_arc_tree))
        return binary_arc_tree
    return recur(mno_tree)
def mk_mno_tree_from_binary_arc_tree(矩阵乘法链维数序列, binary_arc_tree, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    ls = 矩阵乘法链维数序列
    L = len(ls)
    assert L >= 2
    def mk_mno_tree(binary_arc_tree, /):
        (root_arc, may_yvx_children) = binary_arc_tree
        if may_yvx_children is None:
            (x,y) = root_arc
            assert x == (y+1)%L
            i = y
            mno_tree = (0,i,(ls[i],ls[i+1]))
        else:
            (yvx, lhs_binary_arc_tree, rhs_binary_arc_tree) = may_yvx_children
            (y,v,x) = yvx
            assert is_triangle_order(v,x,y)

            #bug:begin,mid,end = y,v,x
            begin,mid,end = y,v,x+1
            lhs_mno_tree = mk_mno_tree(lhs_binary_arc_tree)
            rhs_mno_tree = mk_mno_tree(rhs_binary_arc_tree)

            mno = lhs_mno_tree[0] + rhs_mno_tree[0] + (ls[begin]*ls[mid]*ls[end-1])
            mno_tree = (mno, begin, lhs_mno_tree, mid, rhs_mno_tree, end, (ls[begin],ls[mid],ls[end-1]))
        return mno_tree
    return mk_mno_tree(binary_arc_tree)





def mk_offset_(L, imin, /):
    assert 0 <= imin < L
    def offset_(i, /):
        return (i-imin)%L
    return offset_

def mk_unoffset_(L, imin, /):
    assert 0 <= imin < L
    def unoffset_(i_, /):
        return (i_+imin)%L
    return unoffset_
def unoffset_arcs_(L, imin, arcs_, /):
    unoffset_ = mk_unoffset_(L, imin)
    arcs = [(unoffset_(i_), unoffset_(j_))for i_, j_ in arcs_]
    return arcs




def iter_outer_arcs_of(L, /):
    assert L >= 1
    if L==1:
        return;yield
    assert L >= 2
    if L==2:
        yield (0,1)
        return
    assert L >= 3
    for i in range(L):
        j = (i+1)%L
        arc = (i, j)
        yield arc
def iter_unsorted_inner_outer_arcs_from_unsorted_inner_arcs(L, unsorted_inner_arcs, /):
    yield from unsorted_inner_arcs
    outer_arcs = iter_outer_arcs_of(L)
    yield from outer_arcs

r'''[[[

inner_arcs -> unsorted_inner_arcs
inner_outer_arcs -> unsorted_inner_outer_arcs
mk_mno_tree_from_inner_arcs
mk_binary_arc_tree_from_inner_arcs
mk_arc2next_triangle_vtx_from_inner_arcs
iter_inner_outer_arcs_from_inner_arcs
mk_v2ordered_vtc_from_inner_outer_arcs
mk_v2unordered_vtc_from_inner_outer_arcs


mk_mno_tree_from_unsorted_inner_arcs
mk_binary_arc_tree_from_unsorted_inner_arcs
mk_arc2next_triangle_vtx_from_unsorted_inner_arcs
iter_unsorted_inner_outer_arcs_from_unsorted_inner_arcs
mk_v2ordered_vtc_from_unsorted_inner_outer_arcs
mk_v2unordered_vtc_from_unsorted_inner_outer_arcs
#]]]'''


def mk_binary_arc_tree_from_unsorted_inner_arcs(L, end4ground_outer_arc, unsorted_inner_arcs, /):
    arc2next_triangle_vtx = mk_arc2next_triangle_vtx_from_unsorted_inner_arcs(L, unsorted_inner_arcs)
    binary_arc_tree = mk_binary_arc_tree_from_arc2next_triangle_vtx(L, end4ground_outer_arc, arc2next_triangle_vtx)
    return binary_arc_tree
def mk_binary_arc_tree_from_arc2next_triangle_vtx(L, end4ground_outer_arc, arc2next_triangle_vtx, /):
    'binary_arc_tree = (root_arc, may ((root_arc[1], mid, root_arc[0]), binary_arc_tree, binary_arc_tree))'
    # [end4ground_outer_arc==0] -> [ground_outer_arc==(L-1,0)]即 代表的整个矩阵乘法链表达式的unoffseted_arc
    assert L >= 2
    begin4ground_outer_arc = (end4ground_outer_arc-1)%L
    root_arc = ground_outer_arc = (begin4ground_outer_arc, end4ground_outer_arc)
    def mk_tree(root_arc, /):
        (x,y) = xy = root_arc
        may_v = arc2next_triangle_vtx.get(root_arc)
        assert (x==(y+1)%L) is (may_v is None), (L, end4ground_outer_arc, root_arc, arc2next_triangle_vtx)
        if may_v is None:
            may_yvx_children = None
        else:
            v = may_v
            assert is_triangle_order(v,x,y)
            if 0:
                #bug: xy, yv, vx 皆向内;应当是 xy向内, vy,xv向外
                yv = (y,v)
                vx = (v,x)
                # [y==0][x==L-1]
                # yvx
                lhs_arc = yv
                rhs_arc = vx
            vy = (v,y)
            xv = (x,v)
            # [y==0][x==L-1]
            # yvx
            lhs_arc = vy
            rhs_arc = xv
            lhs_binary_arc_tree = mk_tree(lhs_arc)
            rhs_binary_arc_tree = mk_tree(rhs_arc)
            yvx = (y, v, x)
            may_yvx_children = (yvx, lhs_binary_arc_tree, rhs_binary_arc_tree)
        return (root_arc, may_yvx_children)
    binary_arc_tree = mk_tree(root_arc)
    return binary_arc_tree
def mk_arc2next_triangle_vtx_from_unsorted_inner_arcs(L, unsorted_inner_arcs, /):
    if __debug__:
        unsorted_inner_arcs = [*unsorted_inner_arcs]
        assert len(unsorted_inner_arcs) == max(0,L-3), (L, unsorted_inner_arcs)
    unsorted_inner_outer_arcs = iter_unsorted_inner_outer_arcs_from_unsorted_inner_arcs(L, unsorted_inner_arcs)
    v2ordered_vtc = mk_v2ordered_vtc_from_unsorted_inner_outer_arcs(L, unsorted_inner_outer_arcs)
    arc2next_triangle_vtx = mk_arc2next_triangle_vtx_from_v2ordered_vtc(L, v2ordered_vtc)
    return arc2next_triangle_vtx
def is_triangle_order(v,x,y, /):
    #循环移动后 递增
    return v < x < y or y < v < x or x < y < v
def mk_arc2next_triangle_vtx_from_v2ordered_vtc(L, v2ordered_vtc, /):
    arc2next_triangle_vtx = {}
    for v, ordered_vtc in enumerate(v2ordered_vtc):
        for x, y in pairwise(ordered_vtc):
            # triangle(v,x,y)
            assert is_triangle_order(v,x,y), (L, (v,x,y), (v, ordered_vtc))
            xy = (x,y)
            arc2next_triangle_vtx[xy] = v
    return arc2next_triangle_vtx
def mk_arc2another_triangle_vtc_from_v2ordered_vtc(L, v2ordered_vtc, /):
    arc2another_triangle_vtc = defaultdict(list)
    for v, ordered_vtc in enumerate(v2ordered_vtc):
        for x, y in pairwise(ordered_vtc):
            # triangle(v,x,y)
            xy = (x,y) if x < y else (y,x)
            arc2another_triangle_vtc[xy].append(v)
    arc2another_triangle_vtc = {**arc2another_triangle_vtc}
    return arc2another_triangle_vtc
def mk_v2ordered_vtc_from_unsorted_inner_outer_arcs(L, unsorted_inner_outer_arcs, /):
    v2unordered_vtc = mk_v2unordered_vtc_from_unsorted_inner_outer_arcs(L, unsorted_inner_outer_arcs)
    v2sorted_vtc = mk_v2sorted_vtc_from_v2unordered_vtc(L, v2unordered_vtc)
    v2ordered_vtc = mk_v2ordered_vtc_from_v2sorted_vtc(L, v2sorted_vtc)
    return v2ordered_vtc
def mk_v2unordered_vtc_from_unsorted_inner_outer_arcs(L, unsorted_inner_outer_arcs, /):
    #unsorted_inner_outer_arcs = [*unsorted_inner_outer_arcs]; print(unsorted_inner_outer_arcs)
    v2unordered_vtc = [[] for _ in range(L)]
    for i, j in unsorted_inner_outer_arcs:
        assert not i == j
        assert 0 <= i < L
        assert 0 <= j < L
        v2unordered_vtc[i].append(j)
        v2unordered_vtc[j].append(i)
    return v2unordered_vtc
def mk_v2sorted_vtc_from_v2unordered_vtc(L, v2unordered_vtc, /):
    v2sorted_vtc = bucket_sort_per_row(L, v2unordered_vtc, None)
    return v2sorted_vtc
def mk_v2ordered_vtc_from_v2sorted_vtc(L, v2sorted_vtc, /):
    def iter_(v2sorted_vtc, /):
        for v, sorted_vtc in enumerate(v2sorted_vtc):
            k = -1
            for k, u in enumerate(sorted_vtc):
                if v < u: break
            else:
                k += 1
            if k > 0:
                assert sorted_vtc[k-1] < v
            if k < len(sorted_vtc):
                assert v < sorted_vtc[k]
            ordered_vtc = sorted_vtc[k:] + sorted_vtc[:k]
            yield ordered_vtc

    v2ordered_vtc = [*iter_(v2sorted_vtc)]
    return v2ordered_vtc






def iter_randrange(*args):
    while 1:
        yield randrange(*args)

def _iter_list_of_len_(L, iterable, /):
    it = iter(iterable)
    while 1:
        yield [*islice(it, L)]
def iter_list_of_randrange(L, /, *args):
    it = iter_randrange(*args)
    return _iter_list_of_len_(L, it)
def 迭代囗随机生成囗矩阵乘法链维数序列(L, upper4weight, /):
    assert L >= 2

    #bug: return iter_list_of_randrange(L, upper4weight)
    #   output 0
    return iter_list_of_randrange(L, 1, upper4weight)
def 迭代囗随机生成囗矩阵乘法链维数序列囗单调(L, upper4weight, /):
    lss = 迭代囗随机生成囗矩阵乘法链维数序列(L, upper4weight)
    jks = iter_list_of_randrange(2, L+1)
    return map(单调化囗, lss, jks)
    js = iter_randrange(L+1)
    #for ls, j in zip(lss, js):
    return map(单调化囗, lss, js)
def 单调化囗(ls, jk, /):
    #这是ls[]标准，允许:[11,33,22,22]
    #   若按fw()标准，这就不是 monotone polygon
    j, k = jk
    ls0 = ls[:j]
    ls1 = ls[j:]
    ls0.sort()
    ls1.sort(reverse=True)
    ls = ls0+ls1
    ls0 = ls[:k]
    ls1 = ls[k:]
    ls = ls1+ls0
    return ls



def 单例测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法(version, ls, /):
    L = len(ls)
    #version = 2
    try:
        if version==1:
            (MNO4whole, imin, may) = matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(ls)
            mno = 0 if L==2 else matrix_chain_product__dynamic_programming__O_NNN(ls)[L-1][0][0]
            def f():
                assert MNO4whole == mno, (version, L, ls, mno, (MNO4whole, imin, may))
        elif version==2:
            mno_tree__testing = std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N(ls)
            mno_tree__ans = std_api4matrix_chain_product__dynamic_programming__O_NNN(ls)
            def f():
                assert mno_tree__testing[0] == mno_tree__ans[0], (version, L, ls, (mno_tree__testing[0], mno_tree__ans[0]), (mno_tree__testing, mno_tree__ans))
        else:
            raise Exception(version)
    except Exception as e:
        raise Exception((e, version, L, ls))
    f()

def 随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法(*, L2num_tests, upper4weight, version):
    #见下面:随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时
    lss = [
    #非单调:[7265, 8194, 2762, 7363, 7947]
    [1,1]
    ,[11,11,33,22]
        #idx_pph_arcs=[(1,3)]
        #(1,3)源自:fw全局最大值:...,11,33,22,...
        #(1,3)是pph,是ph,不满足h_arc必要条件[11=11],但构成 最优解
    ,[11,44,33,33,22]
        ,[11,33,22,22,11] #差不多
        #若按fw标准，这就不是 monotone polygon
        #idx_pph_arcs=[(0,2),(2,4)]
        #(2,4)源自:fw局部极大值:...,22,22,11,...
        #(2,4)是pph,是ph,不满足h_arc必要条件[22=22],不构成 最优解
    ####
    ,[1,1,2,3,2,2,1]
    ,[1,3,2,2]
    ,[1,2,3,2,2]
    ,[1,1,1,2,2,2,3,3,3,2,2,2,1,1]
    ,[453, 353, 353, 1935]
    ,[453, 353, 353, 1935, 8405]
    ,[453, 353, 353, 1935, 8405, 9970, 9860]

    ,[8325, 7643, 7361, 7234, 6011, 5254, 4867, 4826, 4528, 3637, 3493, 2884, 2704, 2114, 1979, 1915, 1593, 1222, 700, 453, 353, 353, 1935, 2502, 4561, 6117, 8405, 9970, 9860, 9471, 9399, 9311, 8482, 8414]
    ,[9824, 6895, 5575, 3841, 4502]
    ,[1,1,1]
    ,[1,1,1,1]
    ,[1,1,1,1,1]
    ,[1,2,3,4]
    ,[2,1,3,4]
    ,[3,2,1,4]
    ,[3,1,2,4]
    ,[3,2,4,6]
    ,[3,2,4,12]
    ,[3,2,4,24]
    ,[10,11,25,40,12]
    ,[9824, 6895, 5575, 3841, 4502]
    ,[5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571, 1136, 4140, 5674]
    ]
    for ls in lss:
        print(f'L = {len(ls)}; ls = {ls}')
        单例测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法(version, ls)

    for L, num_tests in sorted(L2num_tests.items()):
        print(f'L = {L}')
        it = 迭代囗随机生成囗矩阵乘法链维数序列囗单调(L, upper4weight)
        it = islice(it, num_tests)
        for ls in it:
            print(f'L = {L}; ls = {ls}')
            单例测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法(version, ls)
            r'''[[[
(3, [1794, 6812, 7970], (97399202160, 0, [1], 3), (97399202160, 0, (2, [], [], [])))
[8901, 3352, 7329, 3825]

line:479@matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N
    assert not any(idx_ == imin_ for arc in idx_ph_arcs for idx_ in arc), idx_ph_arcs
Exception: (AssertionError([(0, 2)]), [8169, 7445, 8023, 5354])


line:540@matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N::_H0
        assert 0 <= i_ <= x_ < y_ <= j_ < L
Exception: (AssertionError(), [7265, 8194, 2762, 7363, 7947])
    [7265, 8194, 2762, 7363, 7947]
    [2762, 7363, 7947, 7265, 8194]
    [0,2,3,1,4]
    vv_pph_arcs=[(2,1),(0,1)]
    idx_pph_arcs=[(1,3),(0,3)]
    idx_ph_arcs=[(1,3)]
        (1,3) : h_arc? v_arc?
        原来是 输入有毛病！并非单调！
        改:迭代囗随机生成囗矩阵乘法链维数序列 ---> 迭代囗随机生成囗矩阵乘法链维数序列囗单调

line 656, in put_h_arc
    put_h_arcs(arc2children(h_arc))
Exception: (TypeError("'collections.defaultdict' object is not callable"), [2843, 3701, 4250, 4612, 8564, 9245, 1756, 1690, 2256])



AssertionError: (5, [9824, 6895, 5575, 3841, 4502], 571825827475, (574408739360, 3, (2, [(1, 4), (1, 3)], [(1, 4), (1, 3)], [(1, 4), (1, 3)])))
    [9824, 6895, 5575, 3841, 4502]
    [3841, 4502, 9824, 6895, 5575]
    offseted_i2vv=[0, 1, 4, 3, 2]
    vv_pph_arcs=[(1,3),(1,2)]
    idx_ph_arcs=[(1,3),(1,4)]
    H0((1,3), 2) = 4502*9824*6895



line 549, in _H0
    assert 0 <= i_ <= x_ < y_ <= j_ < L, (i_, x_, y_, j_, L)
Exception: (AssertionError((6, 3, 4, 8, 12)), [5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571, 1136, 4140, 5674])
    [5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571, 1136, 4140, 5674]
    [1136, 4140, 5674, 5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571]
    bug:
        xxx:offseted_i2vv=[0,4,6,7,11,10,9,8,5,3,2,1]
        vv_pph_arcs=[(7,10),(7,9),(7,8),(7,5),(6,5),(4,5),(4,3),(0,3),(0,2)]
        vv_pph_arcs=[(7,10),(7,9),(7,8),(7,5),(6,5),(4,5),(4,3)]
        idx_ph_arcs=[(3,5),(3,6),(3,7),(3,8),(2,8),(1,8),(1,9)]
    imax_ = 4
更新:
    assert 0 <= i_ <= x_ < y_ <= j_ < L, ((i_, x_, y_, j_, L), idx_ph_arcs)
Exception: (AssertionError(((6, 3, 4, 8, 12), [(3, 5), (3, 6), (6, 8), (3, 8), (2, 8), (1, 8), (1, 9), False])), [5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571, 1136, 4140, 5674])
后来发现不是bug:
    xxx not bug:def i2v()
    def i2v(i, /):
        return i2xv[i], (i-imin)%L
    i2v(6) = (6613, 6)
    i2v(7) = (6613, 7)
        xxx 在降序阶段 变升序 xxx
    真正有毛病的是i2vv&vv_pph_arcs
        上面 将 [000,555,333,333] 转化为 [0,3,2,1] 以满足单调性，是错的！
            应当是:[0,3,1,2]
            反正one_sweep_algorithm并不在乎 单调性

再来一次:
    [1136, 4140, 5674, 5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571]
    offseted_i2vv=[0,4,6,7,11,10,8,9,5,3,2,1]
        one_sweep_algorithm(vv_pph_arcs)单调性 无关紧要
    vv_pph_arcs=[(7,10),(7,8),(8,5),(7,5),(6,5),(4,5),(4,3),(0,3),(0,2)]
    idx_pph_arcs=[(3,5),(3,6),(6,8),(3,8),(2,8),(1,8),(1,9)]
异常:
    (x_,y_)=(3,4)不存在，其实是top_arc/imax_/4-->(3,4)
    (i_,j_)=(6,8)存在于idx_pph_arcs
    但是 由于 不满足 单调性:(6,8)其实是v_arc??
    新增:
        idx_ph_arcs = [arc for arc in idx_ph_arcs if arc[0] < imax_ < arc[1]]
    改进:is_idx_ph_arc4mono_polygon
# 关于one_sweep_algorithm后续修正:见: [词典序最先的最优三角化方案囗潜在的横对角线的必要条件] #not:[无用囗词典序最先的最优三角化方案囗横对角线的必要条件]


[version==2]:
line 1012, in tail4std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N
    assert MNO4whole == mno_tree[0], (L, ls, inner_arcs, MNO4whole, mno_tree)
AssertionError: (4, [1, 2, 3, 4], [(0, 2)], 18, (13, 0, (4, 0, (0, 0, (1, 2)), 1, (0, 1, (2, 3)), 2, (1, 2, 2)), 2, (0, 2, (3, 4)), 3, (1, 3, 3)))



line 928, in mk_arc2next_triangle_vtx_from_v2ordered_vtc
    assert is_triangle_order(v,x,y), (L, (v,x,y), (v, ordered_vtc))
AssertionError: (5, (1, 3, 3), (1, (2, 3, 3, 4, 0)))
raise Exception((e, version, L, ls))
Exception: (AssertionError((5, (1, 3, 3), (1, (2, 3, 3, 4, 0)))), 2, 5, [9824, 6895, 5575, 3841, 4502])
tail4std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N:
    inner_arcs = [(3, 1), (4, 1), (3, 1)]
    idx_all_inner_arcs_ = [(0, 3), (1, 3), (0, 3)]
    (MNO4whole, imin, (imax_, idx_ceil_arcs_, idx_h_arcs_, idx_all_inner_arcs_)) = (571825827475, 3, (2, [(1, 3)], [(1, 3)], [(0, 3), (1, 3), (0, 3)]))
    修正:
    def iter_v_arcs_between(low_arc, h_arc, /):
        #bug:(i_, x_, y_, j_) = _H0(curr_arc, above_arc)
        (i_, x_, y_, j_) = _H0(low_arc, h_arc)



使用is_idx_ph_arc4mono_polygon后:
[version==2]:
    assert mno_tree__testing[0] == mno_tree__ans[0], (version, L, ls, (mno_tree__testing[0], mno_tree__ans[0]), (mno_tree__testing, mno_tree__ans))
AssertionError: (2, 4, [1, 1, 3, 2], (9, 8), ((9, 0, (3, 0, (0, 0, (1, 1)), 1, (0, 1, (1, 3)), 3, (1, 1, 3)), 2, (0, 2, (3, 2)), 4, (1, 3, 2)), (8, 0, (0, 0, (1, 1)), 1, (6, 1, (0, 1, (1, 3)), 2, (0, 2, (3, 2)), 4, (1, 3, 2)), 4, (1, 1, 2))))
[version==1]:
    assert MNO4whole == mno, (version, L, ls, mno, (MNO4whole, imin, may))
AssertionError: (1, 4, [1, 1, 3, 2], 8, (9, 0, (2, [], [], [(0, 2)])))

是逻辑出错is_idx_ph_arc4mono_polygon



line 703, in _H0
    assert 0 <= i_ <= x_ < y_ <= j_ < L, ((i_, x_, y_, j_, L), idx_ph_arcs)
    AssertionError: ((2, 1, 2, 4, 5), [(2, 4), False])
    raise Exception((e, version, L, ls))
    Exception: (AssertionError(((2, 1, 2, 4, 5), [(2, 4), False])), 1, 5, [11, 44, 33, 33, 22])
    assert 0 <= i_ <= x_ < y_ <= j_ < L, ((i_, x_, y_, j_, L), (curr_arc, above_arc), idx_ph_arcs)
    AssertionError: ((2, 1, 2, 4, 5), ((2, 4), True), [(2, 4), False])
    assert 0 <= i_ <= x_ < y_ <= j_ < L, ((i_, x_, y_, j_, L), (curr_arc, above_arc), (imin_, imax_), idx_ph_arcs)
    AssertionError: ((2, 1, 2, 4, 5), ((2, 4), True), (0, 1), [(2, 4), False])

#]]]'''
#end-def 随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法(*, L2num_tests, upper4weight, version):














































class 囗矩阵乘法链维数序列囗相关函数:
    def fw(sf, i_, /):
        return sf.ls_[i_], i_
    def lt__fw(sf, i_, j_, /):
        return sf.fw(i_) < sf.fw(j_)
    def lt__ls(sf, i_, j_, /):
        return sf.ls_[i_] < sf.ls_[j_]
    def __init__(sf, 矩阵乘法链维数序列, /, *, may_imin, _turnon_debug):
        (ls, imin, L, ls_, imin_) = 准备囗词典序最先的最优三角化方案(矩阵乘法链维数序列, may_imin=may_imin)

        save = (ls, imin)
        del ls, imin
        ls_, imin_, L, save


        min_weight4whole = ls_[imin_]
        sf.ls_ = ls_
            #enable:sf.fw)
        if L >= 3:
            #bug:
            #   [i0_,i1_,i2_]= nsmallest(3, range(L), key=sf.fw)
            #   ground_triangle_ = i012_ = (i0_,i1_,i2_) or (i0_,i2_,i1_)
            #逻辑错误:{i0_,i1_}确实有，但第三个，必须在i1_之后，除非[i1_==L-1]
            # 现改正:012-->01X
            i0_ = imin_
            i1_ = min(range(1,L), key=sf.fw)
            if i1_ == L-1:
                iX_ = min(range(1,L-1), key=sf.fw)
                ground_triangle_ = (i0_,iX_,i1_)
                assert i0_ < iX_ < i1_
            else:
                iX_ = min(range(i1_+1,L), key=sf.fw)
                ground_triangle_ = (i0_,i1_,iX_)
                assert i0_ < i1_ < iX_
            ground_triangle_
            assert is_triangle_order(*ground_triangle_)
            assert ground_triangle_[0] < ground_triangle_[1] < ground_triangle_[2]

        sf.min_weight4whole = min_weight4whole
        sf._turnon_debug = _turnon_debug
        sf.L = L
        sf.save = save
        sf.imin_ = imin_
        if L >= 3:
            sf._init4get_side_product_above_curr_arc_()
        if L >= 3:
            sf.ground_triangle_ = ground_triangle_

    def _init4get_side_product_above_curr_arc_(sf, /):
        #get_side_product_above_curr_arc_
        L = sf.L
        assert L >= 3
        ls_ = sf.ls_
        accs_ = [0]
        for j_ in range(1, L):
            i_ = j_-1
            accs_.append(accs_[-1]+ls_[i_]*ls_[j_])
        accs_.append(accs_[-1]+ls_[-1]*ls_[0])
        assert len(accs_) == L+1
        sf.accs_ = accs_


    def 迭代囗三角化方案囗潜在的潜在的横对角线(sf, /):
        'one_sweep_algorithm-extend arc with upper triangle vtx'
        L = sf.L
        assert L >= 3
        ground_triangle_ = sf.ground_triangle_
        imin_ = sf.imin_
        assert imin_ == 0

        stack = [imin_] #0 == imin_
        def _mk_idx_pph_arc(i_, /):
            i_up_ = stack.pop()
            #bug:idx_pph_arc_ = sf.mk_idx_arc__iup_(i_up_, (i_, stack[-1]))
            idx_pph_arc_ = sf.mk_idx_arc__iup_(i_up_, (stack[-1], i_))
            return idx_pph_arc_

        for i_ in range(imin_+1, L-1):
            while sf.lt__fw(i_, stack[-1]):
                yield _mk_idx_pph_arc(i_)
            stack.append(i_)
        assert len(stack) >= 2

        if 1:
            i_ = L-1
            while len(stack) >= 3 and sf.lt__fw(i_, stack[-1]):
                yield _mk_idx_pph_arc(i_)
            stack.append(i_)
        assert len(stack) >= 3

        if 1:
            i_ = imin_
            while len(stack) >= 4:
                yield _mk_idx_pph_arc(i_)
        assert len(stack) == 3

        assert stack == [*ground_triangle_], (stack, ground_triangle_)
        #    inner edges of ground_triangle_ are children of root of idx_arc_tree_(root is Imin8Arc_(imin_))
        #曾经的反例:[11,33,22,44] --> [11,22,44]
        #   现在 由i012_改为i01X_
        return
    #end-def 迭代囗三角化方案囗潜在的潜在的横对角线(sf, /):

    def mk_idx_arc__iup_(sf, i_up_, idx_arc_, /):
        L = sf.L
        assert L >= 3

        (i_, j_) = idx_arc_
        if j_ > 0:
            assert 0 <= i_ < i_up_ < j_ < L
        else:
            assert j_ == 0 < i_ < i_up_ < L
        idx_arc_ = IdxArc_(i_, j_)
        idx_arc_.i_up_ = i_up_
        return idx_arc_

    def mk_idx_arc_tree_(sf, idx_pph_arcs_, /):
        'fan_out tree growing_from_ground_to_up'
        # -> (root_, i_up2may_idx_pph_arc_)

        L = sf.L
        assert L >= 3
        ground_triangle_ = sf.ground_triangle_
        imin_ = sf.imin_
        assert imin_ == 0

        #idx_pph_arcs_ = [*sf.迭代囗三角化方案囗潜在的潜在的横对角线()]
        assert len(idx_pph_arcs_) == L-3
        idx_pph_arcs_[:0]


        i_up2may_idx_pph_arc_ = [None]*L
        def _fill__i_up2may_idx_pph_arc_():
            for idx_pph_arc_ in idx_pph_arcs_:
                assert i_up2may_idx_pph_arc_[idx_pph_arc_.i_up_] is None
                i_up2may_idx_pph_arc_[idx_pph_arc_.i_up_] = idx_pph_arc_
            assert i_up2may_idx_pph_arc_.count(None) == 3
            assert all(i_up2may_idx_pph_arc_[i_] is None for i_ in ground_triangle_)
        _fill__i_up2may_idx_pph_arc_()

        root_ = Imin8Arc_(imin_)
        def _iter_tree_children_of_root_():
            s = {*ground_triangle_}
            #bug:for may_child_ in i_up2may_idx_pph_arc_:
            #   order of root_.tree_children_ matter
            for idx_pph_arc_ in idx_pph_arcs_:
                child_ = idx_pph_arc_
                if {*child_} < s:
                    yield child_
        root_.tree_children_ = [*_iter_tree_children_of_root_()]
        assert (L>=4) <= len(root_.tree_children_) <= 3
        #   order of root_.tree_children_ matter

        def _init__tree_children_of_nonroot_():
            for parent_ in idx_pph_arcs_:
                parent_.tree_children_ = []
                    # init
                    # why not lhs_child_+rhs_child_??
                    #   some arcs will be removed from tree
                    #
        _init__tree_children_of_nonroot_()

        #改为内边函数，因为没啥用，树一直在变动
        def __tree_child2parent_(sf, root_, i_up2may_idx_pph_arc_, child_, /):
            if child_ is root_:
                raise logic-err
            #begin-__tree_child2parent_
            if child_ in root_.tree_children_:
                return root_

            k_ = max(child_, key=sf.fw)
            parent_ = i_up2may_idx_pph_arc_[k_]
            assert parent_ is not None
            if __debug__:
                [e_] = {*parent_}&{*child_}
                assert {*child_} == {e_,k_}
            #end-__tree_child2parent_
            return (k_, parent_)

        def _fill__tree_children_of_nonroot_():
            #direction:
            #   find:child_ -> parent_
            #   but set/get:parent_ -> child_
            for child_ in idx_pph_arcs_:
                i_up_ = child_.i_up_
                if child_ in root_.tree_children_:
                    continue
                (k_, parent_) = __tree_child2parent_(sf, root_, i_up2may_idx_pph_arc_, child_)
                parent_.tree_children_.append(child_)

                'fan_out tree growing_from_ground_to_up'
                    # from_ground_to_up --> lhs_child_/rhs_child_
                    # fan_out --> (parent_->child_)
                    # why not fan_in?? the tree will change many times
        _fill__tree_children_of_nonroot_()

        def _fill__leaf5local_max():
            for parent_ in idx_pph_arcs_:
                # case len(parent_.tree_children_) of:
                #   2 => no child be outer edge
                #   1 => one child be outer edge
                #   0 => two children be outer edge

                (i_, j_) = parent_
                if len(parent_.tree_children_):
                    assert not (i_+2)%L == j_
                else:
                    assert (i_+1) == parent_.i_up_
                    assert (i_+2)%L == j_
                    #删Ilocal_max8Arc_之前:parent_.tree_children_.append(Ilocal_max8Arc_(parent_.i_up_))
        _fill__leaf5local_max()

        def _():
            for parent_ in idx_pph_arcs_:
                #删Ilocal_max8Arc_之前:assert 1 <= len(parent_.tree_children_) <= 2
                assert 0 <= len(parent_.tree_children_) <= 2
        _()
        return (root_, i_up2may_idx_pph_arc_)
    #end-def mk_idx_arc_tree_(sf, idx_pph_arcs_, /):

    def _remove_arcs_as_nodes_of_tree_emplace_if_not(sf, arc2ok_, root_, /):
        assert type(root_) is Imin8Arc_
        def _recur__parent_(outs, parent_, /):
            #has .tree_children_
            #IdxArc_ and whole tree root_
            for child_ in parent_.tree_children_:
                _recur__sub_root_(outs, child_)
            return
        def _recur__sub_root_(outs, sub_root_, /):
            r'''[[[#删Ilocal_max8Arc_
            if type(sub_root_) is Ilocal_max8Arc_:
                leaf_ = sub_root_
                yield leaf_
                return
            #]]]'''
            assert type(sub_root_) is IdxArc_ or sub_root_ is root_

            parent_ = sub_root_
            if parent_ is root_ or arc2ok_(parent_):
                outs.append(parent_)
                outs = []
                _recur__parent_(outs, parent_)
                parent_.tree_children_ = outs
            else:
                # remove parent_
                _recur__parent_(outs, parent_)
                pass
            return
        def _():
            outs = []
            _recur__sub_root_(outs, root_)
            [_root_] = outs
            assert _root_ is root_
        _()
        return None


    def 潜在的潜在的横对角线树至第二版的除零的类横对角线树囗就地移除(sf, idx_pph_arcs_, root_, /):
        #移除 部分 潜在的潜在的横对角线
        #只保留 除零的类横对角线囗第二版
        L = sf.L
        assert L >= 3
        imin_ = sf.imin_
        assert imin_ == 0
        ls_ = sf.ls_


        def is_除零的类横对角线囗第二版(idx_arc_, /):
            (i_,j_) = idx_arc_
            return (imin_ < i_ < j_) and (max(ls_[i_],ls_[j_]) < ls_[idx_arc_.i_up_])

        sf._remove_arcs_as_nodes_of_tree_emplace_if_not(is_除零的类横对角线囗第二版, root_)
        idx_r0psh_arcs_ = [*filter(is_除零的类横对角线囗第二版, idx_pph_arcs_)]
        return idx_r0psh_arcs_

        r'''[[[#删Ilocal_max8Arc_

        def _remove_neighbor_local_max(it, /):
            def key(child_, /):
                return sf.fw(child_.i_)
            may_prev_local_max_child_ = None
            for child_ in it:
                if type(child_) is Ilocal_max8Arc_:
                    if may_prev_local_max_child_ is None:
                        may_prev_local_max_child_ = child_
                    else:
                        may_prev_local_max_child_ = max(child_, may_prev_local_max_child_, key=key)
                else:
                    if not may_prev_local_max_child_ is None:
                        yield may_prev_local_max_child_
                    yield child_
                    may_prev_local_max_child_ = None
            else:
                if not may_prev_local_max_child_ is None:
                    yield may_prev_local_max_child_
            #end-for child_ in it:
            return
        #]]]'''

        def _iter_recur__parent_(parent_, /):
            #has .tree_children_
            #IdxArc_ and whole tree root_
            for child_ in parent_.tree_children_:
                yield from _iter_recur__sub_root_(child_)
            return
        def _iter_recur__sub_root_(sub_root_, /):
            r'''[[[#删Ilocal_max8Arc_
            if type(sub_root_) is Ilocal_max8Arc_:
                leaf_ = sub_root_
                yield leaf_
                return
            #]]]'''
            assert type(sub_root_) is IdxArc_ or sub_root_ is root_

            parent_ = sub_root_
            it = _iter_recur__parent_(parent_)
            if parent_ is root_ or is_除零的类横对角线囗第二版(parent_):
                parent_.tree_children_[:] = it #删Ilocal_max8Arc_: #= _remove_neighbor_local_max(it)
                    #这个效率...希望 yield from 不要太拿衣服
                    #可以考虑 改为 使用 输出列表outs作为 输入
                yield parent_
            else:
                # remove parent_
                yield from it
            return
        [_root_] = _iter_recur__sub_root_(root_)
        assert _root_ is root_
        #return None
        idx_r0psh_arcs_ = [*filter(is_除零的类横对角线囗第二版, idx_pph_arcs_)]
        return idx_r0psh_arcs_
    #end-def 潜在的潜在的横对角线树至第二版的除零的类横对角线树囗就地移除(sf, root_, /):


    def two_vtc5arcs_(sf, arcs_, /):
        return [*map(sf.two_vtx5curr_arc_, arcs_)]
    def two_vtx5curr_arc_(sf, curr_arc_, /):
        #allow pair/tuple
        #bug:assert not type(curr_arc_) is Ilocal_max8Arc_
        #   calc_H0_between_curr_arc_ceil_arcs_ work with Ilocal_max8Arc_
        #if type(curr_arc_) is Imin8Arc_: return (0, 0)
        #删Ilocal_max8Arc_: if type(curr_arc_) is Ilocal_max8Arc_ or type(curr_arc_) is Imin8Arc_:
        if type(curr_arc_) is Imin8Arc_:
            i_ = curr_arc_.i_
            return (i_, i_)

        assert type(curr_arc_) is IdxArc_ or type(curr_arc_) is tuple, (type(curr_arc_), curr_arc_)
        (i_, j_) = curr_arc_
        return (i_, j_)
    if 0:
        def get_lhs_up_outer_edge_(sf, curr_arc_, /):
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            return (i_, (i_+1)%sf.L)
        def get_rhs_up_outer_edge_(sf, curr_arc_, /):
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            return ((j_-1)%sf.L, j_)
    def get_side_product_above_curr_arc_(sf, curr_arc_, /):
        d = sf._get_side_product_above_curr_arc_(curr_arc_)
        if sf._turnon_debug and __debug__:
            _d = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, []) + sf.get_base_product_of_curr_arc_(curr_arc_)
            assert _d==d, (d, _d, sf.two_vtx5curr_arc_(curr_arc_))
        return d
    def _get_side_product_above_curr_arc_(sf, curr_arc_, /):
        accs_ = sf.accs_
        if type(curr_arc_) is Imin8Arc_:
            return accs_[-1]
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert 0 <= i_ <= j_ < sf.L
        r = accs_[j_] -accs_[i_]
        assert (r > 0) ^ (i_ == j_ > 0)
        return r
    def get_base_product_of_curr_arc_(sf, curr_arc_, /):
        ls_ = sf.ls_
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        return ls_[i_] *ls_[j_] if not i_ == j_ else 0
        #删Ilocal_max8Arc_: if type(curr_arc_) is Ilocal_max8Arc_ or type(curr_arc_) is Imin8Arc_:
        if type(curr_arc_) is Imin8Arc_:
            return 0
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert 0 <= i_ < j_ < sf.L
        return ls_[i_] *ls_[j_]
    def get_diff__side_product_above_curr_arc__base_product_above_curr_arc_(sf, curr_arc_, /):
        d = sf.get_side_product_above_curr_arc_(curr_arc_)-sf.get_base_product_of_curr_arc_(curr_arc_)
            #因为 除零的类横对角线囗第二版 的 定义:上方权值 比 横线 大
        #删Ilocal_max8Arc_: assert (d > 0) ^ (type(curr_arc_) is Ilocal_max8Arc_)
        assert (d > 0)
        if sf._turnon_debug and __debug__:
            _d = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, [])
            assert _d==d, (d, _d, sf.two_vtx5curr_arc_(curr_arc_))
        return d

    def get_min_weight4curr_arc_(sf, curr_arc_, /):
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        ls_ = sf.ls_
        return min(ls_[i_], ls_[j_])
    def find_the_focus_vtx4H0_above_curr_arc_(sf, curr_arc_, leftmost_above_or_side_arc4curr_arc_, rightmost_above_or_side_arc4curr_arc_, /):
        base_product4disappear_arcL4H0_ = sf.get_base_product_of_curr_arc_(leftmost_above_or_side_arc4curr_arc_)
        base_product4disappear_arcR4H0_ = sf.get_base_product_of_curr_arc_(rightmost_above_or_side_arc4curr_arc_)
        if type(curr_arc_) is Imin8Arc_:
            delta4h0 = base_product4disappear_arcL4H0_ + base_product4disappear_arcR4H0_
            focus_vtx4H0_above_curr_arc_ = sf.imin_

        else:
            r'''[[[无需如此！否则 横对角线
            (focus_vtx4H0_above_curr_arc_, delta4h0) = (curr_arc_.i_lhs_, base_product4disappear_arcL4H0_) if (ls_[curr_arc_.i_lhs_], -base_product4disappear_arcL4H0_) <= (ls_[curr_arc_.i_rhs_], -base_product4disappear_arcR4H0_) else (curr_arc_.i_rhs_, base_product4disappear_arcR4H0_)
            #]]]'''
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            assert i_ < j_
            k_ = min(i_, j_, key=sf.fw)
            focus_vtx4H0_above_curr_arc_ = k_
            delta4h0 = base_product4disappear_arcL4H0_ if i_==k_ else base_product4disappear_arcR4H0_
        return (focus_vtx4H0_above_curr_arc_, delta4h0)

    def calc_H0_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        #删Ilocal_max8Arc_: assert not type(curr_arc_) is Ilocal_max8Arc_
        if iter(unorder_ceil_arcs_) is unorder_ceil_arcs_:
            unorder_ceil_arcs_ = [*unorder_ceil_arcs_]
                #重复使用
        len(unorder_ceil_arcs_)
        h0 = sf.get_side_product_above_curr_arc_(curr_arc_)
        for ceil_arc_ in unorder_ceil_arcs_:
            h0 -= sf.get_diff__side_product_above_curr_arc__base_product_above_curr_arc_(ceil_arc_)

        #删Ilocal_max8Arc_: ij_unorder_ceil_arcs_ = [sf.two_vtx5curr_arc_(ceil_arc_) for ceil_arc_ in unorder_ceil_arcs_ if not type(ceil_arc_) is Ilocal_max8Arc_]
        ij_unorder_ceil_arcs_ = [sf.two_vtx5curr_arc_(ceil_arc_) for ceil_arc_ in unorder_ceil_arcs_]
        ls_ = sf.ls_
        L = sf.L
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert 0 <= i_ < j_ < L or i_ == j_ == 0

        #print(f'ij_unorder_ceil_arcs_ = {ij_unorder_ceil_arcs_}')
        def delta4h0__i_eq_k_():
            k_ = i_
            a_ = i_+1
            assert a_ < L
            (b_, c_) = min(ij_unorder_ceil_arcs_, key=fst, default=(a_,a_))
            iL_ = c_ if b_==i_ else a_
            #h0 -= ls_[i_]*ls_[iL_]
            return ls_[i_]*ls_[iL_]
        def delta4h0__j_eq_k_():
            k_ = j_
            z_ = (j_-1)%L
            #bug:(x_, y_) = min(ij_unorder_ceil_arcs_, key=snd, default=(z_,z_))
            (x_, y_) = max(ij_unorder_ceil_arcs_, key=snd, default=(z_,z_))
            jR_ = x_ if y_==j_ else z_
            #h0 -= ls_[j_]*ls_[jR_]
            return ls_[j_]*ls_[jR_]
        #'''[[[#not-bug:
        k_ = min(i_, j_, key=sf.fw)
        if i_==k_:
            h0 -= delta4h0__i_eq_k_()
        #######
        if j_==k_:
            h0 -= delta4h0__j_eq_k_()
        #]]]'''
        r'''[[[无需如此！否则 横对角线
        if j_ == 0:
            h0 -= delta4h0__i_eq_k_()
            h0 -= delta4h0__j_eq_k_()
        elif sf.ls_[i_] == sf.ls_[j_]:
            h0 -= max(delta4h0__i_eq_k_(), delta4h0__j_eq_k_())
        else:
            k_ = min(i_, j_, key=sf.fw)
            assert not i_ < j_
            if i_==k_:
                h0 -= delta4h0__i_eq_k_()
            else:
                #if j_==k_:
                h0 -= delta4h0__j_eq_k_()
        #]]]'''
        #min_weight4curr_arc_ = sf.get_min_weight4curr_arc_(curr_arc_)
        min_weight4curr_arc_ = ls_[k_]
        H0_between_curr_arc_ceil_arcs_ = h0*min_weight4curr_arc_
        return H0_between_curr_arc_ceil_arcs_
        r'''[[[

        #以下有毛病:当ceil_arc_与curr_arc_相接时
        assert not type(curr_arc_) is Ilocal_max8Arc_
        #bug:h0 = sf.get_side_product_above_curr_arc_(((i_+b)%L, (j_-1+b)%L))
        #   without detect imin_ ---> cause neg mno

        L = sf.L
        if type(curr_arc_) is Imin8Arc_:
            h0 = sf.get_side_product_above_curr_arc_((1, L-1))
        else:
            #(i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            (i_, j_) = (curr_arc_)
            assert 0 <= i_ < j_ < L
            k_ = min(i_, j_, key=sf.fw)
            b = k_==i_
            #bug:h0 = sf.get_side_product_above_curr_arc_(((i_+1)%L, (j_-1)%L))
            h0 = sf.get_side_product_above_curr_arc_(((i_+b)%L, (j_-1+b)%L))

        for ceil_arc_ in unorder_ceil_arcs_:
            h0 -= sf.get_diff__side_product_above_curr_arc__base_product_above_curr_arc_(ceil_arc_)

        min_weight4curr_arc_ = sf.get_min_weight4curr_arc_(curr_arc_)
        H0_between_curr_arc_ceil_arcs_ = h0*min_weight4curr_arc_
        return H0_between_curr_arc_ceil_arcs_
        #]]]'''

    def calc_diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(sf, curr_arc_, unorder_ceil_arcs_, /):
        f = sf.get_diff__side_product_above_curr_arc__base_product_above_curr_arc_
        d = f(curr_arc_)
        d -= sum(map(f, unorder_ceil_arcs_))
        diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ = d
        return diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
    def calc_side_product_between_(sf, curr_arc_, unorder_ceil_arcs_, /):
        s = sf.get_side_product_above_curr_arc_(curr_arc_)
        for ceil_arc_ in unorder_ceil_arcs_:
            s -= sf.get_diff__side_product_above_curr_arc__base_product_above_curr_arc_(ceil_arc_)

        side_product_between_curr_arc_ceil_arcs_ = s

        if sf._turnon_debug and __debug__:
            _D = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, unorder_ceil_arcs_)
            _s = _D+sf.get_base_product_of_curr_arc_(curr_arc_)
            assert s == _s, (s, _s, sf.two_vtx5curr_arc_(curr_arc_), sf.two_vtc5arcs_(unorder_ceil_arcs_))
        return side_product_between_curr_arc_ceil_arcs_

    def _ON_debug__iter_all_sides_above_(sf, curr_arc_, /):
        L = sf.L
        imin_ = sf.imin_

        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert 0 <= i_ <= j_ < L
        if i_ == j_:
            #if not j_ == imin_:raise logic-err
            if not j_ == imin_:
                s = range(i_, j_)
            else:
                s = range(L)
        else:
            if not imin_  <= i_ < j_:raise logic-err
            s = range(i_, j_)
        for i_ in s:
            j_ = (i_+1)%L
            yield (i_, j_)
        return
    def _ON_debug__all_sides_above_(sf, curr_arc_, /):
        return [*sf._ON_debug__iter_all_sides_above_(curr_arc_)]

    def _ON_debug__all_sides_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        f = sf._ON_debug__iter_all_sides_above_
        s = {*()}
        s.update(*map(f, unorder_ceil_arcs_))
        arcs_ = [arc_ for arc_ in f(curr_arc_) if arc_ not in s]


        if 0:
            print(f'curr_arc_ = {sf.two_vtx5curr_arc_(curr_arc_)}')
            print(f'unorder_ceil_arcs_ = {sf.two_vtc5arcs_(unorder_ceil_arcs_)}')
            print(f'arcs_ = {arcs_}')
            r'''[[[
        bug: 忘记 填充 unorder_ceil_arcs_ 本身！
            curr_arc_ = (3, 7)
            unorder_ceil_arcs_ = [(6, 6), (3, 5)]
            arcs_ = [(5, 6), (6, 7)]

        #]]]'''

        assert arcs_ == sorted(arcs_)
        arcs_.extend((i_,j_) for (i_,j_) in sf.two_vtc5arcs_(unorder_ceil_arcs_) if not i_ == j_)
        arcs_.sort()

        return arcs_
    def _ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(sf, curr_arc_, unorder_ceil_arcs_, /):
        #-> diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
        #-> diff__side_product_between_curr_arc_ceil_arcs__base_product_
        f = sf.get_base_product_of_curr_arc_
        return sum(map(f, sf._ON_debug__all_sides_between_curr_arc_ceil_arcs_(curr_arc_, unorder_ceil_arcs_))) -f(curr_arc_)



    def _ON_debug__all_vtc_above_(sf, curr_arc_, /):
        L = sf.L
        imin_ = sf.imin_

        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert 0 <= i_ <= j_ < L
        if i_ == j_:
            #if not j_ == imin_:raise logic-err
            if not j_ == imin_:
                s = range(i_, j_+1)
            else:
                s = range(L)
        else:
            if not imin_  <= i_ < j_:raise logic-err
            s = range(i_, j_+1)
        return s
    def _ON_debug__all_vtc_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        f = sf._ON_debug__all_vtc_above_
        s = {*()}
        for ceil_arc_ in unorder_ceil_arcs_:
            s |= {*f(ceil_arc_)}
        g = sf.two_vtx5curr_arc_
        for ceil_arc_ in unorder_ceil_arcs_:
            s -= {*g(ceil_arc_)}
        return [i_ for i_ in f(curr_arc_) if i_ not in s]
    def weights5ordered_vtc_(sf, ordered_vtc_, /):
        ls_ = sf.ls_
        xs__ = [ls_[k_] for k_ in ordered_vtc_]
        return xs__
    def _ONNN_debug__weights_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        return sf.weights5ordered_vtc_(sf._ON_debug__all_vtc_between_curr_arc_ceil_arcs_(curr_arc_, unorder_ceil_arcs_))
    def _ONNN_debug__weights_above_(sf, curr_arc_, /):
        return sf.weights5ordered_vtc_(sf._ON_debug__all_vtc_above_(curr_arc_))
    ##def _ONNN_debug__H0_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):必是MNO
    def _ONNN_debug__MNO_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        xs = sf._ONNN_debug__weights_between_curr_arc_ceil_arcs_(curr_arc_, unorder_ceil_arcs_)
        mno_tree = std_api4matrix_chain_product__dynamic_programming__O_NNN(xs)
        return mno_tree[0]
    def _ONNN_debug__MNO_above_(sf, curr_arc_, /):
    #def _ONNN_debug__MNO_above_(sf, MNO_above_curr_arc_, curr_arc_, /):
        L = sf.L
        ls_ = sf.ls_
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert i_ <= j_
        if j_==0:
            j_ = L-1
        assert i_ <= j_
        xs = [ls_[k_] for k_ in range(i_, j_+1)]
        assert 3 <= len(xs) == j_+1-i_ <= L
        assert xs == sf._ONNN_debug__weights_above_(curr_arc_)
        mno_tree = std_api4matrix_chain_product__dynamic_programming__O_NNN(xs)
        #assert MNO_above_curr_arc_ == mno_tree[0], ((i_, j_), MNO_above_curr_arc_, mno_tree[0])
        return mno_tree[0]

    def 词典序最先的最优三角化方案囗(sf, /):
        '-> (MNO4whole, imin, 所有对角线囗偏移囗有序, (所有显式横对角线囗第二版囗偏移囗有序, 所有隐式横对角线囗第二版囗偏移囗有序, 所有竖对角线囗第二版囗偏移囗有序))'
        L = sf.L
        min_weight4whole = sf.min_weight4whole
        if L == 2:
            def _mk_result():
                (_ls, _imin) = sf.save
                result = (MNO4whole, imin, 所有对角线囗偏移囗有序, (所有显式横对角线囗第二版囗偏移囗有序, 所有隐式横对角线囗第二版囗偏移囗有序, 所有竖对角线囗第二版囗偏移囗有序)) = (0, _imin, [], ([], [], []))
                return result
            return _mk_result()
        assert L >= 3
        idx_pph_arcs_ = [*sf.迭代囗三角化方案囗潜在的潜在的横对角线()]
        (root_, i_up2may_idx_pph_arc_) = sf.mk_idx_arc_tree_(idx_pph_arcs_)
        idx_r0psh_arcs_ = sf.潜在的潜在的横对角线树至第二版的除零的类横对角线树囗就地移除(idx_pph_arcs_, root_)
        del idx_pph_arcs_
        #ls_ = sf.ls_


        def get_initial_above_arcs_of(curr_arc_, /):
            #here child-parent of tree not child-ceil of paper
            #not-bug:
            #   有些已被移除？不可能
            return curr_arc_.tree_children_
        def get_unorder_ceil_arcs_of(curr_arc_, /):
            #here child-parent of tree not child-ceil of paper
            return curr_arc_.unorder_ceil_arcs_
        if 0:
            r'''[[[
        #改进效率:def _init_unorder_ceil_arcs4curr_arc_(curr_arc_, /):
            unorder_ceil_arcs4curr_arc_ = [] #MergeableHeap() #TODO
            unorder_above_arcs_ = [*get_initial_above_arcs_of(curr_arc_)]
            #ijs = sf.two_vtc5arcs_(unorder_above_arcs_);print(f'unorder_above_arcs_ = {ijs}')
            while unorder_above_arcs_:
                above_arc_ = unorder_above_arcs_.pop()
                if not above_arc_.supporting_weight < min_weight4curr_arc_:
                    #删Ilocal_max8Arc_: assert not type(above_arc_) is Ilocal_max8Arc_
                    #discard above_arc_
                    _unorder_above_arcs_ = get_unorder_ceil_arcs_of(above_arc_)
                    #删Ilocal_max8Arc_: assert _unorder_above_arcs_, (sf.two_vtc5arcs_(_unorder_above_arcs_), sf.two_vtx5curr_arc_(above_arc_))
                    unorder_above_arcs_.extend(_unorder_above_arcs_)
                        #??这不就是O(N**2)??
                        #   不能这么搞
                        #   unorder_ceil_arcs4curr_arc_ 必须 组织起来: heap? tree? heap<heap>
                else:
                    ceil_arc_ = above_arc_
                    unorder_ceil_arcs4curr_arc_.append(ceil_arc_)
            #   [supporting_weight4local_max==-1 < 1 <= min_weight4curr_arc_]
            #   above_arc_ 最高 止于 local_max
            assert all(ceil_arc_.supporting_weight < min_weight4curr_arc_ for ceil_arc_ in unorder_ceil_arcs4curr_arc_)
            #删Ilocal_max8Arc_: assert (len(unorder_ceil_arcs4curr_arc_) >= 1) ^ (L==3), (sf.two_vtx5curr_arc_(curr_arc_), sf.two_vtc5arcs_(unorder_ceil_arcs4curr_arc_), L)
                #至少有一个local_max

            initial_unorder_ceil_arcs4curr_arc_ = final_unorder_above_arcs4curr_arc_ = unorder_ceil_arcs4curr_arc_
            return initial_unorder_ceil_arcs4curr_arc_
        #end-def _init_unorder_ceil_arcs4curr_arc_():
            #]]]'''

        def _init_find_leftmost_above_or_side_arc4curr_arc_(curr_arc_, /):
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            leftmost_side_arc4curr_arc_ = (i_, i_+1)
            unorder_above_arcs_ = get_initial_above_arcs_of(curr_arc_)
            if unorder_above_arcs_:
                #leftmost_above_or_side_arc4curr_arc_ = (*min(unorder_above_arcs_),)
                leftmost_above_or_side_arc4curr_arc_ = min(map(tuple, unorder_above_arcs_))
                if not leftmost_above_or_side_arc4curr_arc_[0] == i_:
                    leftmost_above_or_side_arc4curr_arc_ = leftmost_side_arc4curr_arc_
            else:
                leftmost_above_or_side_arc4curr_arc_ = leftmost_side_arc4curr_arc_
            return leftmost_above_or_side_arc4curr_arc_

        def _init_find_rightmost_above_or_side_arc4curr_arc_(curr_arc_, /):
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            rightmost_side_arc4curr_arc_ = ((j_-1)%L, j_)
            unorder_above_arcs_ = get_initial_above_arcs_of(curr_arc_)
            if unorder_above_arcs_:
                #rightmost_above_or_side_arc4curr_arc_ = (*max(unorder_above_arcs_),)
                rightmost_above_or_side_arc4curr_arc_ = max(map(tuple, unorder_above_arcs_))
                if not rightmost_above_or_side_arc4curr_arc_[-1] == j_:
                    rightmost_above_or_side_arc4curr_arc_ = rightmost_side_arc4curr_arc_
            else:
                rightmost_above_or_side_arc4curr_arc_ = rightmost_side_arc4curr_arc_
            return rightmost_above_or_side_arc4curr_arc_
        def key4heap4ceil_arc_(ceil_arc_, /):
            return -ceil_arc_.supporting_weight
        def _init_unorder_ceil_arcs4curr_arc_(curr_arc_, min_weight4curr_arc_, /):
            #改进效率:unorder_above_arcs_ = [*get_initial_above_arcs_of(curr_arc_)]
            unorder_above_arcs_ = MergeableHeap(get_initial_above_arcs_of(curr_arc_), key=key4heap4ceil_arc_)
            diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ = sf.calc_diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, unorder_above_arcs_)
            leftmost_above_or_side_arc4curr_arc_ = _init_find_leftmost_above_or_side_arc4curr_arc_(curr_arc_)
            rightmost_above_or_side_arc4curr_arc_ = _init_find_rightmost_above_or_side_arc4curr_arc_(curr_arc_)
            MNO_above_ceil_arcs4curr_arc_ = sum(above_arc_.MNO_above_curr_arc_ for above_arc_ in unorder_above_arcs_)
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            assert diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ > 0
            assert i_ == leftmost_above_or_side_arc4curr_arc_[0]
            assert j_ == rightmost_above_or_side_arc4curr_arc_[-1]
            assert MNO_above_ceil_arcs4curr_arc_ >= 0
                # 0 is ok

            #ijs = sf.two_vtc5arcs_(unorder_above_arcs_);print(f'unorder_above_arcs_ = {ijs}')
            while unorder_above_arcs_:
                above_arc_ = unorder_above_arcs_.peak()
                if not above_arc_.supporting_weight < min_weight4curr_arc_:
                    #删Ilocal_max8Arc_: assert not type(above_arc_) is Ilocal_max8Arc_
                    #discard above_arc_
                    unorder_above_arcs_.pop()
                    _unorder_above_arcs_ = get_unorder_ceil_arcs_of(above_arc_)
                    #删Ilocal_max8Arc_: assert _unorder_above_arcs_, (sf.two_vtc5arcs_(_unorder_above_arcs_), sf.two_vtx5curr_arc_(above_arc_))
                    #改进效率:unorder_above_arcs_.extend(_unorder_above_arcs_)
                        #??这不就是O(N**2)??
                        #   不能这么搞
                        #   unorder_ceil_arcs4curr_arc_ 必须 组织起来: heap? tree? heap<heap>
                    if 1:
                        assert above_arc_.unorder_ceil_arcs_ is _unorder_above_arcs_
                        above_arc_.unorder_ceil_arcs_ = None
                            #eat() clear _unorder_above_arcs_
                        unorder_above_arcs_.eat(_unorder_above_arcs_)
                        assert not _unorder_above_arcs_
                    diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ += above_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
                    leftmost_above_or_side_arc4curr_arc_ = min(leftmost_above_or_side_arc4curr_arc_, above_arc_.leftmost_above_or_side_arc_)
                    rightmost_above_or_side_arc4curr_arc_ = max(rightmost_above_or_side_arc4curr_arc_, above_arc_.rightmost_above_or_side_arc_)
                    MNO_above_ceil_arcs4curr_arc_ -= above_arc_.MNO_between_curr_arc_ceil_arcs_
                    assert diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ > 0
                    assert i_ == leftmost_above_or_side_arc4curr_arc_[0]
                    assert j_ == rightmost_above_or_side_arc4curr_arc_[-1]
                    assert MNO_above_ceil_arcs4curr_arc_ >= 0
                else:
                    break
            #   [supporting_weight4local_max==-1 < 1 <= min_weight4curr_arc_]
            #   above_arc_ 最高 止于 local_max
            unorder_ceil_arcs4curr_arc_ = unorder_above_arcs_
            #改进效率:assert all(ceil_arc_.supporting_weight < min_weight4curr_arc_ for ceil_arc_ in unorder_ceil_arcs4curr_arc_)
            #删Ilocal_max8Arc_: assert (len(unorder_ceil_arcs4curr_arc_) >= 1) ^ (L==3), (sf.two_vtx5curr_arc_(curr_arc_), sf.two_vtc5arcs_(unorder_ceil_arcs4curr_arc_), L)
                #至少有一个local_max

            initial_unorder_ceil_arcs4curr_arc_ = final_unorder_above_arcs4curr_arc_ = unorder_ceil_arcs4curr_arc_
            (focus_vtx4H0_above_curr_arc_, delta4h0) = sf.find_the_focus_vtx4H0_above_curr_arc_(curr_arc_, leftmost_above_or_side_arc4curr_arc_, rightmost_above_or_side_arc4curr_arc_)
            base_product4curr_arc_ = sf.get_base_product_of_curr_arc_(curr_arc_)
            H0_between_curr_arc_final_unorder_above_arcs_ = min_weight4curr_arc_*(diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_+base_product4curr_arc_-delta4h0)
                #new:find_the_focus_vtx4H0_above_curr_arc_
                #update:calc_H0_between_curr_arc_ceil_arcs_
                #update:_iter_all_unorder_v_ij_arcs4all_arcs_/_iter_all_unorder_v_ij_arcs4curr_arc_
            MNO_between_curr_arc_ceil_arcs_ = H0_between_curr_arc_final_unorder_above_arcs_
            MNO_above_curr_arc_ = MNO_above_ceil_arcs4curr_arc_ + MNO_between_curr_arc_ceil_arcs_
                #final: MNO_above_curr_arc_, H0_between_curr_arc_final_unorder_above_arcs_
                #but not final:(MNO_above_ceil_arcs4curr_arc_, MNO_between_curr_arc_ceil_arcs_)
            return (initial_unorder_ceil_arcs4curr_arc_, H0_between_curr_arc_final_unorder_above_arcs_, diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_, leftmost_above_or_side_arc4curr_arc_, rightmost_above_or_side_arc4curr_arc_, MNO_above_curr_arc_)
        #end-def _init_unorder_ceil_arcs4curr_arc_():
        r'''[[[#改进效率:
        def _sum_MNO_above_(unorder_ceil_arcs_, /):
            return sum(ceil_arc_.MNO_above_curr_arc_ for ceil_arc_ in unorder_ceil_arcs_)
        #]]]'''




        idx_r0psh_arcs_
        #testing___________goto
        for sub_root_ in chain(idx_r0psh_arcs_, [root_]):
            assert type(sub_root_) is IdxArc_ or sub_root_ is root_
            #assert sub_root_ is not root_
            #删Ilocal_max8Arc_: assert (len(sub_root_.tree_children_) >= 1) ^ (L==3)
            #   无用:assert (len(sub_root_.tree_children_) >= 0)
            if 0:
                r'''[[[#删Ilocal_max8Arc_:
                #bug:
                if type(sub_root_.tree_children_[-1]) is Ilocal_max8Arc_:
                    assert len(sub_root_.tree_children_) == 1, [11, 22, 44, 33, 33, 22] #(1,5).tree_children_ == [(2,),(4,)]
                else:
                    assert len(sub_root_.tree_children_) >= 2, [11, 22, 33, 44, 22] #(1,4).tree_children_ == [(2,4)]
                #]]]'''
            #######

            #parent_ = sub_root_
            #for child_ in parent_.tree_children_:

            curr_arc_ = sub_root_
            min_weight4curr_arc_ = sf.get_min_weight4curr_arc_(curr_arc_)
            ##_init_unorder_ceil_arcs4curr_arc_ requires min_weight4curr_arc_
            #改进效率:initial_unorder_ceil_arcs4curr_arc_ = final_unorder_above_arcs4curr_arc_ = _init_unorder_ceil_arcs4curr_arc_(curr_arc_)
            #H0_between_curr_arc_ceil_arcs_ = H0_between_curr_arc_final_unorder_above_arcs_
            #改进效率:H0_between_curr_arc_final_unorder_above_arcs_ = sf.calc_H0_between_curr_arc_ceil_arcs_(curr_arc_, final_unorder_above_arcs4curr_arc_)
            (initial_unorder_ceil_arcs4curr_arc_, H0_between_curr_arc_final_unorder_above_arcs_, diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_, leftmost_above_or_side_arc4curr_arc_, rightmost_above_or_side_arc4curr_arc_, MNO_above_curr_arc_) = _init_unorder_ceil_arcs4curr_arc_(curr_arc_, min_weight4curr_arc_)
            final_unorder_above_arcs4curr_arc_ = initial_unorder_ceil_arcs4curr_arc_
            assert H0_between_curr_arc_final_unorder_above_arcs_ > 0
            #final_unorder_above_arcs4curr_arc_
            if sf._turnon_debug and __debug__:
                final_unorder_above_arcs4curr_arc_ = [*final_unorder_above_arcs4curr_arc_]
                    #protected from eat()
                _mno = sf._ONNN_debug__MNO_between_curr_arc_ceil_arcs_(curr_arc_, final_unorder_above_arcs4curr_arc_)
                assert H0_between_curr_arc_final_unorder_above_arcs_ == _mno, (sf.two_vtx5curr_arc_(curr_arc_), H0_between_curr_arc_final_unorder_above_arcs_, _mno, sf.two_vtc5arcs_(curr_arc_.tree_children_), sf.two_vtc5arcs_(final_unorder_above_arcs4curr_arc_), [above_arc_.supporting_weight for above_arc_ in final_unorder_above_arcs4curr_arc_])
            curr_arc_.leftmost_above_or_side_arc_ = leftmost_above_or_side_arc4curr_arc_
            curr_arc_.rightmost_above_or_side_arc_ = rightmost_above_or_side_arc4curr_arc_
            #改进效率:会变:curr_arc_.final_unorder_above_arcs_ = final_unorder_above_arcs4curr_arc_
                # 用于生成 竖对角线
            #改进效率:curr_arc_.MNO_above_curr_arc_ = _sum_MNO_above_(curr_arc_.final_unorder_above_arcs_) + H0_between_curr_arc_final_unorder_above_arcs_
            curr_arc_.MNO_above_curr_arc_ = MNO_above_curr_arc_
            del MNO_above_curr_arc_
            assert curr_arc_.MNO_above_curr_arc_ > 0
            if sf._turnon_debug and __debug__:
                sf._ONNN_debug__MNO_above_(curr_arc_.MNO_above_curr_arc_, curr_arc_)
                _mno = sf._ONNN_debug__MNO_above_(curr_arc_)
                #改进效率:assert curr_arc_.MNO_above_curr_arc_ == _mno, (sf.two_vtx5curr_arc_(curr_arc_), curr_arc_.MNO_above_curr_arc_, _mno, sf.two_vtc5arcs_(curr_arc_.tree_children_), sf.two_vtc5arcs_(curr_arc_.final_unorder_above_arcs_), [above_arc_.supporting_weight for above_arc_ in curr_arc_.final_unorder_above_arcs_])
                assert curr_arc_.MNO_above_curr_arc_ == _mno, (sf.two_vtx5curr_arc_(curr_arc_), curr_arc_.MNO_above_curr_arc_, _mno, sf.two_vtc5arcs_(curr_arc_.tree_children_), sf.two_vtc5arcs_(final_unorder_above_arcs4curr_arc_), [above_arc_.supporting_weight for above_arc_ in final_unorder_above_arcs4curr_arc_])
            if curr_arc_ is root_:
                curr_arc_.unorder_ceil_arcs_ = initial_unorder_ceil_arcs4curr_arc_
                if 0:
                    print(f'curr_arc_=root_')
                    print(f'curr_arc_.MNO_above_curr_arc_={curr_arc_.MNO_above_curr_arc_}')
                    print(f'curr_arc_.H0_between_curr_arc_final_unorder_above_arcs_={H0_between_curr_arc_final_unorder_above_arcs_}')

                break

            r'''[[[#改进效率:
            #heapq
            def _mk_heap_item(ceil_arc_, /):
                return (-ceil_arc_.supporting_weight, sf.two_vtx5curr_arc_(ceil_arc_), ceil_arc_)
            def _heap_push(ceil_arc_, /):
                heappush(heap, _mk_heap_item(ceil_arc_))
            def _heap_pushs(unorder_ceil_arcs_, /):
                for _ in map(_heap_push, unorder_ceil_arcs_):pass
            def _heap_pop():
                (_,_,ceil_arc_) = heappop(heap)
                return ceil_arc_
            heap = [*map(_mk_heap_item, initial_unorder_ceil_arcs4curr_arc_)]
            heapify(heap)
            #]]]'''
            if 1:
                heap = initial_unorder_ceil_arcs4curr_arc_
                #会改变:initial_unorder_ceil_arcs4curr_arc_/final_unorder_above_arcs4curr_arc_
                del initial_unorder_ceil_arcs4curr_arc_, final_unorder_above_arcs4curr_arc_ # curr_arc_.final_unorder_above_arcs_ 没有了
            #定位:ceil_arcs_<curr_arc_> #除去paper-child(not『tree-child』) 的 最低 above_arc_
            #supporting_weight4curr_arc_<ceil_arcs_>
            #
            MNO_between_curr_arc_ceil_arcs_ = H0_between_curr_arc_final_unorder_above_arcs_
            r'''[[[#改进效率:
            if 0:
                base_product4curr_arc_ = sf.get_base_product_of_curr_arc_(curr_arc_)
                side_product_between_curr_arc_ceil_arcs_ = sf.calc_side_product_between_(curr_arc_, initial_unorder_ceil_arcs4curr_arc_)
                diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ = (side_product_between_curr_arc_ceil_arcs_ -base_product4curr_arc_)
                del side_product_between_curr_arc_ceil_arcs_, base_product4curr_arc_
            else:
                diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ = sf.calc_diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, initial_unorder_ceil_arcs4curr_arc_)
                #D
                pass
            #]]]'''
            diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_

            if sf._turnon_debug and __debug__:
                _D = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, initial_unorder_ceil_arcs4curr_arc_)
                D = diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
                assert D==_D, (D, _D, sf.two_vtx5curr_arc_(curr_arc_))

            curr_arc_.unorder_ceil_hidden_children_ = []
            #while 1:
            if 1:
                assert diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ > 0
                    #这是因为 上方 的 最小权值 都比 当前横对角线端点权值大
                assert MNO_between_curr_arc_ceil_arcs_ > 0
                #bug:supporting_weight4curr_arc_ = MNO_between_curr_arc_ceil_arcs_//diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
                #assert supporting_weight4curr_arc_ >= 0
                #删Ilocal_max8Arc_: #bug:-1没错！:bug:改-1为neg_oo:assert supporting_weight4curr_arc_ >= 0, (sf.two_vtx5curr_arc_(curr_arc_), supporting_weight4curr_arc_)
                if 0:
                    #重启__floor_div__ 替代 Fraction
                    supporting_weight4curr_arc_ = Fraction(MNO_between_curr_arc_ceil_arcs_,diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_)
                    assert 0 < supporting_weight4curr_arc_ < min_weight4curr_arc_
                else:
                    supporting_weight4curr_arc_ = MNO_between_curr_arc_ceil_arcs_//diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
                    assert 0 <= supporting_weight4curr_arc_ < min_weight4curr_arc_

                #heapq
                #num_ceil_hidden_children4curr_arc_ = len(curr_arc_.unorder_ceil_hidden_children_)
                #bug:while heap:
            while heap:
                if 1:
                    #改进效率:(_,_,ceil_arc_) = heap[0]
                    ceil_arc_ = heap.peak()
                    assert ceil_arc_.supporting_weight < min_weight4curr_arc_
                    #assert 0 < supporting_weight4curr_arc_ < min_weight4curr_arc_
                    if ceil_arc_.supporting_weight < supporting_weight4curr_arc_:
                        break
                    assert 0 < supporting_weight4curr_arc_ <= ceil_arc_.supporting_weight < min_weight4curr_arc_
                    #testing___________goto
                    #xxx 我自己添加的:min_weight4whole
                    #xxx   论文中 ceil_arc_ 嵌套，现在 不会了
                    #xxx if ceil_arc_.supporting_weight < min_weight4whole: break
                    #   论文没错！!!!不能批量比较！因为 supporting_weight4curr_arc_不断增长！
                    #删Ilocal_max8Arc_: assert not type(ceil_arc_) is Ilocal_max8Arc_
                        #Ilocal_max8Arc_.supporting_weight = -1 < curr_arc_ is not Imin8Arc_
                    #改进效率:_heap_pop()
                    heap.pop()
                    #if not type(ceil_arc_) is Ilocal_max8Arc_:
                    if 1:
                        #改进效率:_heap_pushs(ceil_arc_.unorder_ceil_arcs_)
                        heap.eat(ceil_arc_.unorder_ceil_arcs_)
                    #ceil_arc_ is hidden-child of curr_arc_, hence not a ceil_arc_ anymore
                    curr_arc_.unorder_ceil_hidden_children_.append(ceil_arc_)
                    r'''[[[
                    ... ...TODO
                    xxx update side_product_between_curr_arc_ceil_arcs_
                    xxx update H0_between_curr_arc_ceil_arcs_
                    update diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
                    update MNO_between_curr_arc_ceil_arcs_
                    #]]]'''
                    diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ += ceil_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
                    MNO_between_curr_arc_ceil_arcs_ += ceil_arc_.MNO_between_curr_arc_ceil_arcs_
                    #H0_between_curr_arc_ceil_arcs_ += min_weight4curr_arc_*ceil_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
                    assert diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ > 0
                    assert MNO_between_curr_arc_ceil_arcs_ > 0
                    old_supporting_weight4curr_arc_ = supporting_weight4curr_arc_
                    if 0:
                        #重启__floor_div__ 替代 Fraction
                        new_supporting_weight4curr_arc_ = Fraction(MNO_between_curr_arc_ceil_arcs_,diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_)
                        assert 0 < old_supporting_weight4curr_arc_ <= new_supporting_weight4curr_arc_ <= ceil_arc_.supporting_weight < min_weight4curr_arc_
                    else:
                        new_supporting_weight4curr_arc_ = MNO_between_curr_arc_ceil_arcs_//diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
                        assert 0 <= old_supporting_weight4curr_arc_ <= new_supporting_weight4curr_arc_ <= ceil_arc_.supporting_weight < min_weight4curr_arc_
                    supporting_weight4curr_arc_ = new_supporting_weight4curr_arc_

                    if sf._turnon_debug and __debug__:
                        __unorder_ceil_arcs4curr_arc_ = [ceil_arc_ for (_,_,ceil_arc_) in heap]
                        _D = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, __unorder_ceil_arcs4curr_arc_)
                        D = diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
                        assert D==_D, (D, _D, sf.two_vtx5curr_arc_(curr_arc_))
                        _mno = sf._ONNN_debug__MNO_between_curr_arc_ceil_arcs_(curr_arc_, __unorder_ceil_arcs4curr_arc_)
                        assert MNO_between_curr_arc_ceil_arcs_ == _mno
                #xxx end-while heap:
                #if num_ceil_hidden_children4curr_arc_ == len(curr_arc_.unorder_ceil_hidden_children_): break
            ####end-while 1:
            #end-while heap:
            #   [supporting_weight4local_max==-1 < 0 <= supporting_weight4curr_arc_]
            #   ceil_arc_ 最高 止于 local_max
            #改进效率:unorder_ceil_arcs4curr_arc_ = [ceil_arc_ for (_,_,ceil_arc_) in heap]
            unorder_ceil_arcs4curr_arc_ = heap

            ########next round
            #删Ilocal_max8Arc_: assert unorder_ceil_arcs4curr_arc_, (sf.two_vtx5curr_arc_(curr_arc_))
            #改进效率:assert all(ceil_arc_.supporting_weight < supporting_weight4curr_arc_ for ceil_arc_ in unorder_ceil_arcs4curr_arc_)
            if 0:
                #重启__floor_div__ 替代 Fraction
                assert supporting_weight4curr_arc_*diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ == MNO_between_curr_arc_ceil_arcs_
            else:
                assert supporting_weight4curr_arc_ == MNO_between_curr_arc_ceil_arcs_//diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
            if sf._turnon_debug and __debug__:
                _D = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, unorder_ceil_arcs4curr_arc_)
                D = diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
                assert D==_D, (D, _D, sf.two_vtx5curr_arc_(curr_arc_))
                _mno = sf._ONNN_debug__MNO_between_curr_arc_ceil_arcs_(curr_arc_, unorder_ceil_arcs4curr_arc_)
                assert MNO_between_curr_arc_ceil_arcs_ == _mno
            curr_arc_.unorder_ceil_arcs_ = unorder_ceil_arcs4curr_arc_
            curr_arc_.supporting_weight = supporting_weight4curr_arc_
            curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_ = diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
            curr_arc_.MNO_between_curr_arc_ceil_arcs_ = MNO_between_curr_arc_ceil_arcs_
            #curr_arc_.H0_between_curr_arc_ceil_arcs_ = H0_between_curr_arc_ceil_arcs_
            #bug:curr_arc_.MNO_above_curr_arc_ = _sum_MNO_above_(curr_arc_.unorder_ceil_arcs_) + H0_between_curr_arc_ceil_arcs_
            curr_arc_.MNO_above_curr_arc_
            curr_arc_.leftmost_above_or_side_arc_
            curr_arc_.rightmost_above_or_side_arc_
            curr_arc_.unorder_ceil_hidden_children_
            if 0:
                #testing___________goto
                print(f'curr_arc_={tuple(curr_arc_)}')
                print(f'min_weight4curr_arc_={min_weight4curr_arc_}')
                #改进效率:print(f'curr_arc_.final_unorder_above_arcs_={sf.two_vtc5arcs_(curr_arc_.final_unorder_above_arcs_)}')
                print(f'curr_arc_.unorder_ceil_arcs_={sf.two_vtc5arcs_(curr_arc_.unorder_ceil_arcs_)}')
                print(f'curr_arc_.unorder_ceil_hidden_children_={sf.two_vtc5arcs_(curr_arc_.unorder_ceil_hidden_children_)}')
                print(f'curr_arc_.MNO_above_curr_arc_={curr_arc_.MNO_above_curr_arc_}')
                #print(f'curr_arc_.H0_between_curr_arc_ceil_arcs_={H0_between_curr_arc_ceil_arcs_}')
                print(f'curr_arc_.MNO_between_curr_arc_ceil_arcs_={curr_arc_.MNO_between_curr_arc_ceil_arcs_}')
                print(f'curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_={curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_}')
                print(f'curr_arc_.supporting_weight={curr_arc_.supporting_weight}')
        #end-while

        def _iter_all_unorder_ceil_arcs_(ceil_arc_, /):
            #删Ilocal_max8Arc_: if not type(ceil_arc_) is Ilocal_max8Arc_:
            if 1:
                yield from chain.from_iterable(map(_iter_all_unorder_ceil_arcs__not_top_, ceil_arc_.unorder_ceil_arcs_))
        def _iter_all_unorder_ceil_arcs__not_top_(ceil_arc_, /):
            yield ceil_arc_
            yield from _iter_all_unorder_ceil_arcs_(ceil_arc_)
        def _iter_all_unorder_ceil_hidden_children_(ceil_arc_, /):
            #bug:yield ceil_arc_
            #print(f'ceil_arc_ = {tuple(ceil_arc_)}')
            #print(f'ceil_arc_.unorder_ceil_hidden_children_ = {ceil_arc_.unorder_ceil_hidden_children_}')
            yield from chain.from_iterable(map(_iter_all_unorder_ceil_hidden_children__not_top_, ceil_arc_.unorder_ceil_hidden_children_))
        def _iter_all_unorder_ceil_hidden_children__not_top_(ceil_arc_, /):
            yield ceil_arc_
            yield from _iter_all_unorder_ceil_hidden_children_(ceil_arc_)
            #bug:yield from map(_iter_all_unorder_ceil_hidden_children__not_top_, ceil_arc_.unorder_ceil_hidden_children_)
            #bug:yield from map(_iter_all_unorder_ceil_hidden_children__not_top_, ceil_arc_.unorder_ceil_arcs_))
        def _iter_all_unorder_v_ij_arcs4all_arcs_(root_, all_unorder_h_arcsII_, /):
            for curr_arc_ in all_unorder_h_arcsII_:
                yield from _iter_all_unorder_v_ij_arcs4curr_arc_(curr_arc_)
            yield from _iter_all_unorder_v_ij_arcs4curr_arc_(root_)
        def _iter_all_unorder_v_ij_arcs4curr_arc_(curr_arc_, /):
            r'''[[[
            下面的代码有毛病，反例:
            curr_arc_ == (1,4)
            curr_arc_.final_sorted_above_arcs_ == [(1,3)]
            输出会 有(1,3)
            [[[
            ===
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            assert i_ <= j_
            k_ = min(i_, j_, key=sf.fw)
            first_ = i_+1 + (i_ == k_)
            last_ = (j_-1 - (j_ == k_))%L
            if k_ == i_:
                def _mk(z_, /):
                    return (k_, z_)
            else:
                def _mk(z_, /):
                    return (z_, k_)

            for above_arc_ in curr_arc_.final_sorted_above_arcs_:
                if type(above_arc_) is Ilocal_max8Arc_:
                    continue

                (x_, y_) = above_arc_
                for z_ in range(first_, x_+1):
                    yield _mk(z_)
                first_ = y_
            for z_ in range(first_, last_+1):
                yield _mk(z_)


            ]]]

            #]]]'''
            #删Ilocal_max8Arc_: assert not type(curr_arc_) is Ilocal_max8Arc_
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            assert i_ <= j_
            assert 0 <= i_ < j_ < L or i_==j_==0==sf.imin_
            k_ = min(i_, j_, key=sf.fw)
            if k_ == i_:
                def _mk(z_, /):
                    return (k_, z_)
            else:
                def _mk(z_, /):
                    return (z_, k_)

            # i_~first_:最多3点:i_.+{0,1,2}
            # 可能出 幺蛾子的是:
            #   Ilocal_max8Arc_(i_) 不可能
            #   Ilocal_max8Arc_(i_+1) 可无视
            #   Ilocal_max8Arc_(i_+2) 无视
            #   (i_, i_+2) 唯一可能出状况的情形
            #   (i_, i_+1) 外边 不可能
            #   (i_+1, i_+2) 外边 不可能

            #删Ilocal_max8Arc_: sorted_above_arcs_ = [tuple(above_arc_) for above_arc_ in curr_arc_.final_sorted_above_arcs_ if not type(above_arc_) is Ilocal_max8Arc_]
            sorted_above_arcs_ = [tuple(above_arc_) for above_arc_ in curr_arc_.final_sorted_above_arcs_]
            def moveL(i_, idx, /):
                if idx == len(sorted_above_arcs_):
                    return i_+1, idx
                a_,b_ = sorted_above_arcs_[idx]
                if a_ == i_:
                    return b_, idx+1
                return i_+1, idx
            def moveR(j_, idx, /):
                if idx == -len(sorted_above_arcs_)-1:
                    return (j_-1)%L, idx
                x_,y_ = sorted_above_arcs_[idx]
                if y_ == j_:
                    return x_, idx-1
                return (j_-1)%L, idx
            def apply_(n, f, k_, idx, /):
                for _ in range(n):
                    (k_, idx) = f(k_, idx)
                return (k_, idx)
            b_, idxA = apply_(1+(i_ == k_), moveL, i_, 0)
            x_, idxY = apply_(1+(j_ == k_), moveR, j_, -1)
            if 0:
                print(f'sorted_above_arcs_ = {sorted_above_arcs_}')
                print(f'i_ = {i_}')
                print(f'j_ = {j_}')
                print(f'b_ = {b_}')
                print(f'x_ = {x_}')
            while b_ <= x_:
                yield _mk(b_)
                (b_, idxA) = moveL(b_, idxA)






        def is_h_arcII_(arc, /):
            return arc.is_h_arcII_
        def _setting__final_sorted_above_arcs_(root_, all_unorder_h_arcsII_, /):
            #setting:final_sorted_above_arcs_
            for may_idx_pph_arc_ in i_up2may_idx_pph_arc_:
                if may_idx_pph_arc_ is not None:
                    idx_pph_arc_ = may_idx_pph_arc_
                    idx_pph_arc_.is_h_arcII_ = False
            for h_arc_ in all_unorder_h_arcsII_:
                h_arc_.is_h_arcII_ = True
            sf._remove_arcs_as_nodes_of_tree_emplace_if_not(is_h_arcII_, root_)
                #now tree_children_ are final_unorder_above_arcs_
            unorder_ij_above_arcss_ = []
            ps_iups_ = []
            def _add(curr_arc_, ps_i_up_, /):
                assert _get(ps_i_up_) is curr_arc_
                #改进效率:unorder_ij_above_arcss_.append([(*sf.two_vtx5curr_arc_(above_arc_), above_arc_) for above_arc_ in curr_arc_.final_unorder_above_arcs_])
                unorder_ij_above_arcss_.append([(*sf.two_vtx5curr_arc_(above_arc_), above_arc_) for above_arc_ in curr_arc_.tree_children_])
                ps_iups_.append(ps_i_up_)
            def _get(ps_i_up_, /):
                if ps_i_up_ == sf.imin_:
                    return root_
                return i_up2may_idx_pph_arc_[ps_i_up_]

            for curr_arc_ in all_unorder_h_arcsII_:
                _add(curr_arc_, curr_arc_.i_up_)
            else:
                _add(root_, sf.imin_)

            #######
            unorder_ij_above_arcss_
            fst, snd
            table = [[] for _ in range(L)]
            unorder_ij_above_arcss_ = bucket_sort_per_row(L, unorder_ij_above_arcss_, table, key=snd)
            sorted_ij_above_arcss_ = bucket_sort_per_row(L, unorder_ij_above_arcss_, table, key=fst)
            sorted_above_arcss_ = [[above_arc_ for (i_, j_, above_arc_) in sorted_ij_above_arcs_] for sorted_ij_above_arcs_ in sorted_ij_above_arcss_]
            #print(f'unorder_ij_above_arcss_ = {unorder_ij_above_arcss_}')
            #print(f'sorted_ij_above_arcss_ = {sorted_ij_above_arcss_}')

            for ps_i_up_, sorted_above_arcs_ in zip(ps_iups_, sorted_above_arcss_):
                curr_arc_ = _get(ps_i_up_)
                curr_arc_.final_sorted_above_arcs_ = sorted_above_arcs_
        #end-def _setting__final_sorted_above_arcs_(root_, all_unorder_h_arcsII_, /):


        def _():
            #bug:all_unorder_ceil_arcs_ = [ceil_arc_ for ceil_arc_ in root_.unorder_ceil_arcs_ if type(ceil_arc_) is not Ilocal_max8Arc_]
            #删Ilocal_max8Arc_: all_unorder_ceil_arcs_ = [ceil_arc_ for ceil_arc_ in _iter_all_unorder_ceil_arcs_(root_) if type(ceil_arc_) is not Ilocal_max8Arc_]
            all_unorder_ceil_arcs_ = [ceil_arc_ for ceil_arc_ in _iter_all_unorder_ceil_arcs_(root_)]
            #rint(f'all_unorder_ceil_arcs_={all_unorder_ceil_arcs_}')
            #bug:all_unorder_ceil_hidden_children_ = [*_iter_all_unorder_ceil_hidden_children_(root_)]
            all_unorder_ceil_hidden_children_ = [*chain.from_iterable(map(_iter_all_unorder_ceil_hidden_children_, all_unorder_ceil_arcs_))]
            #rint(f'all_unorder_ceil_hidden_children_={all_unorder_ceil_hidden_children_}')
            all_unorder_h_arcsII_ = all_unorder_ceil_arcs_+all_unorder_ceil_hidden_children_
            所有显式横对角线囗第二版囗偏移囗无序 = [(i_, j_) for (i_, j_) in all_unorder_ceil_arcs_]
            所有隐式横对角线囗第二版囗偏移囗无序 = [(i_, j_) for (i_, j_) in all_unorder_ceil_hidden_children_]


            #using:final_sorted_above_arcs_
            _setting__final_sorted_above_arcs_(root_, all_unorder_h_arcsII_)
            #bug:所有竖对角线囗第二版囗偏移囗无序 = _iter_all_unorder_v_ij_arcs4all_arcs_(root_, all_unorder_h_arcsII_)
            所有竖对角线囗第二版囗偏移囗无序 = [*_iter_all_unorder_v_ij_arcs4all_arcs_(root_, all_unorder_h_arcsII_)]
            assert len(所有显式横对角线囗第二版囗偏移囗无序) + len(所有隐式横对角线囗第二版囗偏移囗无序) + len(所有竖对角线囗第二版囗偏移囗无序) == L-3, (L, (所有显式横对角线囗第二版囗偏移囗无序, 所有隐式横对角线囗第二版囗偏移囗无序, 所有竖对角线囗第二版囗偏移囗无序))
            def _iter_with(k, xss, /):
                for xs in xss:
                    yield (*xs, k)
            def _it_3s():
                yield from _iter_with(0, 所有显式横对角线囗第二版囗偏移囗无序)
                yield from _iter_with(1, 所有隐式横对角线囗第二版囗偏移囗无序)
                yield from _iter_with(2, 所有竖对角线囗第二版囗偏移囗无序)
            it = _it_3s()
            table = [[] for _ in range(L)]
            ij_kind_ls_ = radix_sort_with_table([L, L], it, table)
            assert len(ij_kind_ls_) == L-3
            inner_idx_arcs_ = []
            [ceil_idx_arcs_
            ,hide_idx_arcs_
            ,ps_vertical_idx_arcs_
            ] = kind2ls = ([], [], [])
            for i_, j_, kind in ij_kind_ls_:
                ij_ = (i_, j_)
                inner_idx_arcs_.append(ij_)
                kind2ls[kind].append(ij_)
            assert len(inner_idx_arcs_) == L-3
            return (inner_idx_arcs_, (ceil_idx_arcs_, hide_idx_arcs_, ps_vertical_idx_arcs_))
        (inner_idx_arcs_, (ceil_idx_arcs_, hide_idx_arcs_, ps_vertical_idx_arcs_)) = _()
        所有对角线囗偏移囗有序 = inner_idx_arcs_
        所有显式横对角线囗第二版囗偏移囗有序 = ceil_idx_arcs_
        所有隐式横对角线囗第二版囗偏移囗有序 = hide_idx_arcs_
        所有竖对角线囗第二版囗偏移囗有序 = ps_vertical_idx_arcs_
        MNO4whole = root_.MNO_above_curr_arc_
        def _mk_result():
            (_ls, imin) = sf.save
            result = (MNO4whole, imin, 所有对角线囗偏移囗有序, (所有显式横对角线囗第二版囗偏移囗有序, 所有隐式横对角线囗第二版囗偏移囗有序, 所有竖对角线囗第二版囗偏移囗有序))
            return result
        result = _mk_result()
        if sf._turnon_debug and __debug__ and 0:
            #tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN
            #rint(f'result={result}')
            (_ls, _imin) = sf.save
            tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN(_ls, result)
        return result


    #end-def 词典序最先的最优三角化方案囗(sf, /):
#end-class 囗矩阵乘法链维数序列囗相关函数:

r'''[[[
class PosInf:
    def __new__(cls, /):
        try:
            return PosInf.__the
        except AttributeError:
            PosInf.__the = object.__new__(cls)
            return PosInf()
    def __eq__(sf, ot, /):
        return sf is ot
    def __ne__(sf, ot, /):
        return not sf is ot
    __gt__ = __ne__
    __le__ = __eq__
    def __ge__(sf, ot, /):
        return True
    def __lt__(sf, ot, /):
        return False
    def __pos__(sf, /):
        return sf
    def __neg__(sf, /):
        return neg_oo
pos_oo = PosInf()


class NegInf:
    def __new__(cls, /):
        try:
            return NegInf.__the
        except AttributeError:
            NegInf.__the = object.__new__(cls)
            return NegInf()
    def __eq__(sf, ot, /):
        return sf is ot
    def __ne__(sf, ot, /):
        return not sf is ot
    __lt__ = __ne__
    __ge__ = __eq__
    def __le__(sf, ot, /):
        return True
    def __gt__(sf, ot, /):
        return False
    def __pos__(sf, /):
        return sf
    def __neg__(sf, /):
        #必需的，heapq 反转优先级
        return pos_oo
neg_oo = NegInf()
neg_oo = -1

#]]]'''
#class Idx8Arc_:
r'''[[[
无用，单调多边形情形是因为Maybe，可使用Ilocal_max8Arc_简化，通用情形下，ceil_idx_arcs_以list出现，Ilocal_max8Arc_毫无意义
class Ilocal_max8Arc_:
    __slots__ = 'i_'.split()
    #bug:-1没错！:bug:因为『?//diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_』supporting_weight4curr_arc可能为0，supporting_weight4local_max改为-1
    #   因为『?//D』中的『?』可能小于0，这也是 最后能存在的保证
    #   改用neg_oo
    #   改回-1
    #supporting_weight = supporting_weight4local_max = -1
    supporting_weight = supporting_weight4local_max = -1 #= neg_oo
    diff__side_product_between_curr_arc_ceil_arcs__base_product_ = 0
    MNO_between_curr_arc_ceil_arcs_ = 0
    MNO_above_curr_arc_ = 0
    #unorder_ceil_arcs_ = ()
    def __init__(sf, i_, /):
        sf.i_ = i_
#]]]'''

class Imin8Arc_:
    __slots__ = '''
        i_
        tree_children_
        leftmost_above_or_side_arc_
        rightmost_above_or_side_arc_
        MNO_above_curr_arc_
        unorder_ceil_arcs_
        final_sorted_above_arcs_
        '''.split()
        #改进效率:final_unorder_above_arcs_
    unorder_ceil_hidden_children_ = ()
    r'''[[[#改进效率:
    @property
    def unorder_ceil_arcs_(sf, /):
        return sf.final_unorder_above_arcs_
    #]]]'''
    def __init__(sf, i_, /):
        sf.i_ = i_
class IdxArc_:
    __slots__ = '''
        i_lhs_
        i_rhs_
        i_up_
        tree_children_
        leftmost_above_or_side_arc_
        rightmost_above_or_side_arc_
        unorder_ceil_hidden_children_
        unorder_ceil_arcs_
        supporting_weight
        diff__side_product_between_curr_arc_ceil_arcs__base_product_
        MNO_between_curr_arc_ceil_arcs_
        MNO_above_curr_arc_
        is_h_arcII_
        final_sorted_above_arcs_
        '''.split()
        #改进效率:final_unorder_above_arcs_
    def __init__(sf, i_lhs_, i_rhs_, /):
        sf.i_lhs_ = i_lhs_
        sf.i_rhs_ = i_rhs_
    def __iter__(sf, /):
        yield sf.i_lhs_
        yield sf.i_rhs_
    def __contains__(sf, k_, /):
        return (k_ == sf.i_lhs_) or (k_ == sf.i_rhs_)

assert 0 in IdxArc_(0,1)
assert 1 in IdxArc_(0,1)

def matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, /, *, may_imin, _turnon_debug):
    sf = 囗矩阵乘法链维数序列囗相关函数(矩阵乘法链维数序列, may_imin=may_imin, _turnon_debug=_turnon_debug)
    return sf.词典序最先的最优三角化方案囗()
矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗等同排序算法耗时 = matrix_chain_product__polygon_partitioning__O_NlogN

def std_api4matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    result = matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, may_imin=None)
    return tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, result)
def tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, result, /):
    (MNO4whole, imin, 所有对角线囗偏移囗有序, (所有显式横对角线囗第二版囗偏移囗有序, 所有隐式横对角线囗第二版囗偏移囗有序, 所有竖对角线囗第二版囗偏移囗有序)) = result

    ls = 矩阵乘法链维数序列
    L = len(ls)
    if 0:
        #无用:
        #只能保证mno的值，但mno_tree_不是mno_tree
        ls_ = SeqLeftRotateView(ls, imin)
        imin_ = 0
            #end4ground_outer_arc
        所有对角线囗偏移囗有序
            #inner_arcs
        mno_tree_ = mk_mno_tree_from_unsorted_inner_arcs(ls_, imin_, 所有对角线囗偏移囗有序)
            #binary_arc_tree_ = mk_binary_arc_tree_from_unsorted_inner_arcs(L, imin_, 所有对角线囗偏移囗有序)
            #mno_tree_ = mk_mno_tree_from_binary_arc_tree(ls_, binary_arc_tree_)
    inner_arcs_ = 所有对角线囗偏移囗有序
    unsorted_inner_arcs = unoffset_arcs_(L, imin, inner_arcs_)
    end4ground_outer_arc = 0
    mno_tree = mk_mno_tree_from_unsorted_inner_arcs(ls, end4ground_outer_arc, unsorted_inner_arcs)

        #inner_arcs = mk_sorted_unoffseted_arcs_from_unsorted_offseted_arcs_(L, imin, inner_arcs_)
        #mno_tree = mk_mno_tree_from_unsorted_inner_arcs(ls, end4ground_outer_arc, inner_arcs)
    assert MNO4whole == mno_tree[0], (L, 矩阵乘法链维数序列, 所有对角线囗偏移囗有序, imin, MNO4whole, mno_tree)
    return mno_tree


def 单例测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时(version, ls, /, *, _turnon_debug):
    #见上面:单例测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法
    L = len(ls)
    #version = 2
    try:
        if version==1:
            (MNO4whole, imin, inner_idx_arcs_, kind2ij_ls) = matrix_chain_product__polygon_partitioning__O_NlogN(ls, may_imin=None, _turnon_debug=_turnon_debug)
            mno = 0 if L==2 else matrix_chain_product__dynamic_programming__O_NNN(ls)[L-1][0][0]
            def f():
                assert MNO4whole == mno, (version, L, ls, mno, (MNO4whole, inner_idx_arcs_, kind2ij_ls))
        elif version==2:
            mno_tree__testing = std_api4matrix_chain_product__polygon_partitioning__O_NlogN(ls)
            mno_tree__ans = std_api4matrix_chain_product__dynamic_programming__O_NNN(ls)
            def f():
                assert mno_tree__testing[0] == mno_tree__ans[0], (version, L, ls, (mno_tree__testing[0], mno_tree__ans[0]), (mno_tree__testing, mno_tree__ans))
        elif version==3:
            (MNO4whole, imin, inner_idx_arcs_, kind2ij_ls) = matrix_chain_product__polygon_partitioning__O_NlogN(ls, may_imin=None, _turnon_debug=_turnon_debug)
            (_mno, _L, _imin, sorted_inner_arcs_) = 词典序最先的最优三角化方案囗立方算法囗(ls, may_imin=None)
            def f():
                assert MNO4whole == _mno, (version, L, ls, (imin, _imin), (MNO4whole, _mno), (inner_idx_arcs_, sorted_inner_arcs_))
                assert inner_idx_arcs_ == sorted_inner_arcs_, (version, L, ls, (imin, _imin), (MNO4whole, _mno), (inner_idx_arcs_, sorted_inner_arcs_))
        else:
            raise Exception(version)
    except Exception as e:
        raise Exception((e, version, L, ls))
    f()


def 随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时(*, L2num_tests, upper4weight, version, _turnon_debug):
    #见上面:随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法
    lss = [
    [1,1]
    ,[9577, 3341, 3263, 4362, 8859, 4464]
    #
    ,[1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281]
    #   比下面少3个:, 4880, 7349, 6392
    #
    ,[1260, 4880, 2101, 9659, 2273, 9458, 8399, 9039, 7349, 5002, 6392, 1281]
    ,[6392, 1281, 1260, 4880, 2101, 9659, 2273, 9458, 8399, 9039, 7349, 5002]
    ,[5900, 2220, 711, 2354, 8990, 2424, 3635]
    ,[8499, 1895, 5503, 936, 566, 1102]
    ,[5779, 7186, 7654, 9627, 5932, 7396]
    ,[5366, 2499, 6032, 1410, 1452, 8474]
    ,[44, 33, 55, 11, 22, 66]
    ,[11,33,22,44]
    ,[10,11,25,40,12]
    ,[1,2,3,2,2]
    ,[1,3,2,2]
    ,[1,1,1]
    ,[1,1,1,1]
    ,[1,1,1,1,1]
    ,[1,2,3,4]
    ,[2,1,3,4]
    ,[3,2,1,4]
    ,[3,1,2,4]
    ,[3,2,4,6]
    ,[3,2,4,12]
    ,[3,2,4,24]
    ,[11,11,33,22]
    ,[11,44,33,33,22]
    ,[11,33,22,22,11]
    ,[1,1,2,3,2,2,1]
    ,[1,1,1,2,2,2,3,3,3,2,2,2,1,1]
    ]
    for ls in lss:
        print(f'L = {len(ls)}; ls = {ls}')
        单例测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时(version, ls, _turnon_debug=_turnon_debug)

    for L, num_tests in sorted(L2num_tests.items()):
        print(f'L = {L}')
        it = 迭代囗随机生成囗矩阵乘法链维数序列(L, upper4weight)
        it = islice(it, num_tests)
        for ls in it:
            print(f'L = {L}; ls = {ls}')
            单例测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时(version, ls, _turnon_debug=_turnon_debug)
            r'''[[[
assert len(所有显式横对角线囗第二版囗偏移囗无 序) + len(所有隐式横对角线囗第二版囗偏移囗无序) + len(所有竖对角线囗第二版囗偏移囗无序) == L-3, (L, (所有显式横对角线囗第二版囗偏移囗无序, 所有隐式横 对角线囗第二版囗偏移囗无序, 所有竖对角线囗第二版囗偏移囗无序))
AssertionError: (6, ([(1, 4)], [(1, 3)], [(1, 3), (0, 4)]))
raise Exception((e, version, L, ls))
Exception: (AssertionError((6, ([(1, 4)], [(1, 3)], [(1, 3), (0, 4)]))), 2, 6, [5366, 2499, 6032, 1410, 1452, 8474])





line 2283, in tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN                               assert MNO4whole == mno_tree[0], (L, 矩阵乘法 链维数序列, 所有对角线囗偏移囗有序, imin, MNO4whole, mno_tree)
AssertionError: (6, [5366, 2499, 6032, 1410, 1452, 8474], [(0, 4), (1, 3), (1, 4)], 3, 105313322064, (111865930896, 0, (90611636016, 0, (0, 0, (1410, 1452)), 1, (85495383336, 1, (66024594768, 1, (0, 1, (1452, 8474)), 2, (0, 2, (8474, 5366)), 4, (1452, 8474, 5366)), 3, (0, 3, (5366, 2499)), 5, (1452, 5366, 2499)), 5, (1410, 1452, 2499)), 4, (0, 4, (2499, 6032)), 6, (1410, 2499, 6032)))



L = 6; ls = [5366, 2499, 6032, 1410, 1452, 8474]  curr_arc_=(1, 3)
curr_arc_.MNO_above_curr_arc_=66024594768
curr_arc_.MNO_between_curr_arc_ceil_arcs_=66024594768
curr_arc_.supporting_weight=1320
curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_=49984300
curr_arc_=(1, 4)
curr_arc_.MNO_above_curr_arc_=78942774504
curr_arc_.MNO_between_curr_arc_ceil_arcs_=78942774504
curr_arc_.supporting_weight=1168
curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_=67556818
curr_arc_=root_
curr_arc_.MNO_above_curr_arc_=105313322064
curr_arc_.H0_between_curr_arc_final_unorder_above_arcs_=26370547560
all_unorder_ceil_arcs_=[<__main__.IdxArc_ object at 0x7cd70c5840>]
all_unorder_ceil_hidden_children_=[<__main__.IdxArc_ object at 0x7cd7027140>]
>>> xs
[1410, 1452, 8474, 5366, 2499, 6032]
>>> xs[1]*xs[2]*xs[3]
66024594768
>>> 1452*8474*5366
66024594768
>>> 1452*8474+8474*5366-1452*5366
49984300
>>> xs[1]*xs[3]*xs[4]
19470788568
>>> xs[1]*xs[3]*xs[4] + xs[1]*xs[2]*xs[3]
85495383336

xs[1]*xs[3]*xs[4]
xs[1]*xs[3]*xs[4] + xs[1]*xs[2]*xs[3]
xs[1]*xs[3]*xs[2] + xs[2]*xs[4]*xs[3]
1452*8474*5366
1452*8474+8474*5366-1452*5366






assert len(所有显式横对角线囗第二版囗偏移囗无 序) + len(所有隐式横对角线囗第二版囗偏移囗无序) + len(所有竖对角线囗第二版囗偏移囗无序) == L-3, (L, (所有显式横对角线囗第二版囗偏移囗无序, 所有隐式横 对角线囗第二版囗偏移囗无序, 所有竖对角线囗第二版囗偏移囗无序))
AssertionError: (6, ([(1, 4)], [], [(0, 4)]))
raise Exception((e, version, L, ls))
Exception: (AssertionError((6, ([(1, 4)], [], [(0, 4)]))), 2, 6, [5779, 7186, 7654, 9627, 5932, 7396])


line 2035, in 词典序最先的最优三角化方案囗
_heap_pushs(ceil_arc_.unorder_ceil_arcs_)
AttributeError: 'Ilocal_max8Arc_' object has no attribute 'unorder_ceil_arcs_'
raise Exception((e, version, L, ls))
Exception: (AttributeError("'Ilocal_max8Arc_' object has no attribute 'unorder_ceil_arcs_'"), 2, 6, [8499, 1895, 5503, 936, 566, 1102])


line 1957, in _init_unorder_ceil_arcs4curr_arc_
assert (len(unorder_ceil_arcs4curr_arc_) >= 1) ^ (L==3), (sf.two_vtx5curr_arc_(curr_arc_), sf.two_vtc5arcs_(unorder_ceil_arcs4curr_arc_), L)
AssertionError: ((0, 0), [], 7)
raise Exception((e, version, L, ls))
Exception: (AssertionError(), 2, 7, [5900, 2220, 711, 2354, 8990, 2424, 3635])






assert MNO4whole == mno_tree[0], (L, 矩阵乘法链维数序列, 所有对角线囗偏移囗有序, imin, MNO4whole, mno_tree)
raise Exception((e, version, L, ls))
Exception: (AssertionError((6, [9577, 3341, 3263, 4362, 8859, 4464], [(1, 3), (1, 5), (3, 5)], 2, 370871931341, (427944674094, 0, (0, 0, (3263, 4362)), 1, (380391532848, 1, (172502164512, 1, (0, 1, (4362, 8859)), 2, (0, 2, (8859, 4464)), 4, (4362, 8859, 4464)), 3, (142833523248, 3, (0, 3, (4464, 9577)), 4, (0, 4, (9577, 3341)), 6, (4464, 9577, 3341)), 6, (4362, 4464, 3341)), 6, (3263, 4362, 3341)))), 2, 6, [9577, 3341, 3263, 4362, 8859, 4464])




assert MNO4whole == mno, (version, L, ls, mno, (MNO4whole, inner_idx_arcs_, kind2ij_ls))
AssertionError: (1, 12, [6392, 1281, 1260, 4880, 2101, 9659, 2273, 9458, 8399, 9039, 7349, 5002], 466946248771, (468034834344, [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (9, 11)], ([(9, 11)], [], [(0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9)])))
assert mno_tree__testing[0] == mno_tree__ans[0], (version, L, ls, (mno_tree__testing[0], mno_tree__ans[0]), (mno_tree__testing, mno_tree__ans))
AssertionError: (2, 12, [6392, 1281, 1260, 4880, 2101, 9659, 2273, 9458, 8399, 9039, 7349, 5002], (468034834344, 466946248771), ((468034834344, 0, (419004169920, 0, (372686950440, 0, (288988160580, 0, (193330773720, 0, (93239218800, 0, (66151695960, 0, (38488513140, 0, (12918628800, 0, (0, 0, (1260, 4880)), 1, (0, 1, (4880, 2101)), 3, (1260, 4880, 2101)), 2, (0, 2, (2101, 9659)), 4, (1260, 2101, 9659)), 3, (0, 3, (9659, 2273)), 5, (1260, 9659, 2273)), 4, (0, 4, (2273, 9458)), 6, (1260, 2273, 9458)), 5, (0, 5, (9458, 8399)), 7, (1260, 9458, 8399)), 6, (0, 6, (8399, 9039)), 8, (1260, 8399, 9039)), 7, (0, 7, (9039, 7349)), 9, (1260, 9039, 7349)), 8, (0, 8, (7349, 5002)), 10, (1260, 7349, 5002)), 9, (40957136304, 9, (0, 9, (5002, 6392)), 10, (0, 10, (6392, 1281)), 12, (5002, 6392, 1281)), 12, (1260, 5002, 1281)), (466946248771, 0, (0, 0, (6392, 1281)), 1, (425989112467, 1, (0, 1, (1281, 1260)), 2, (417915584347, 2, (371598364867, 2, (287899575007, 2, (192242188147, 2, (92150633227, 2, (65063110387, 2, (12918628800, 2, (0, 2, (1260, 4880)), 3, (0, 3, (4880, 2101)), 5, (1260, 4880, 2101)), 4, (46127259607, 4, (0, 4, (2101, 9659)), 5, (0, 5, (9659, 2273)), 7, (2101, 9659, 2273)), 7, (1260, 2101, 2273)), 6, (0, 6, (2273, 9458)), 8, (1260, 2273, 9458)), 7, (0, 7, (9458, 8399)), 9, (1260, 9458, 8399)), 8, (0, 8, (8399, 9039)), 10, (1260, 8399, 9039)), 9, (0, 9, (9039, 7349)), 11, (1260, 9039, 7349)), 10, (0, 10, (7349, 5002)), 12, (1260, 7349, 5002)), 12, (1281, 1260, 5002)), 12, (6392, 1281, 5002))))

assert mno_tree__testing[0] == mno_tree__ans[0], (version, L, ls, (mno_tree__testing[0], mno_tree__ans[0]), (mno_tree__testing, mno_tree__ans))
AssertionError: (2, 12, [1260, 4880, 2101, 9659, 2273, 9458, 8399, 9039, 7349, 5002, 6392, 1281], (468034834344, 466946248771), (
(468034834344, 0, (419004169920, 0, (372686950440, 0, (288988160580, 0, (193330773720, 0, (93239218800, 0, (66151695960, 0, (38488513140, 0, (12918628800, 0, (0, 0, (1260, 4880)), 1, (0, 1, (4880, 2101)), 3, (1260, 4880, 2101)), 2, (0, 2, (2101, 9659)), 4, (1260, 2101, 9659)), 3, (0, 3, (9659, 2273)), 5, (1260, 9659, 2273)), 4, (0, 4, (2273, 9458)), 6, (1260, 2273, 9458)), 5, (0, 5, (9458, 8399)), 7, (1260, 9458, 8399)), 6, (0, 6, (8399, 9039)), 8, (1260, 8399, 9039)), 7, (0, 7, (9039, 7349)), 9, (1260, 9039, 7349)), 8, (0, 8, (7349, 5002)), 10, (1260, 7349, 5002)), 9, (40957136304, 9, (0, 9, (5002, 6392)), 10, (0, 10, (6392, 1281)), 12, (5002, 6392, 1281)), 12, (1260, 5002, 1281))
, (466946248771
    , 0, (417915584347
        , 0, (371598364867
            , 0, (287899575007
                , 0, (192242188147
                    , 0, (92150633227
                        , 0, (65063110387
                            , 0, (12918628800
                                , 0, (0, 0, (1260, 4880))
                                , 1, (0, 1, (4880, 2101))
                                , 3, (1260, 4880, 2101)
                                )
                            , 2, (46127259607
                                , 2, (0, 2, (2101, 9659))
                                , 3, (0, 3, (9659, 2273))
                                , 5, (2101, 9659, 2273)
                                )
                            , 5, (1260, 2101, 2273)
                            )
                        , 4, (0, 4, (2273, 9458))
                        , 6, (1260, 2273, 9458)
                        )
                    , 5, (0, 5, (9458, 8399))
                    , 7, (1260, 9458, 8399)
                    )
                , 6, (0, 6, (8399, 9039))
                , 8, (1260, 8399, 9039)
                )
            , 7, (0, 7, (9039, 7349))
            , 9, (1260, 9039, 7349)
            )
        , 8, (0, 8, (7349, 5002))
        , 10, (1260, 7349, 5002)
        )
    , 9, (40957136304
        , 9, (0, 9, (5002, 6392))
        , 10, (0, 10, (6392, 1281))
        , 12, (5002, 6392, 1281)
        )
    , 12, (1260, 5002, 1281)
    )
))



line 1935, in _ONNN_debug__MNO_above_
    assert MNO_above_curr_arc_ == mno_tree[0], ((i_, j_), MNO_above_curr_arc_, mno_tree[0])
raise Exception((e, version, L, ls))
Exception: (AssertionError(((0, 8), 340104267295, 340022952607)), 2, 9, [1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281])

echo $[340104267295-340022952607]
81314688


assert curr_arc_.MNO_above_curr_arc_ == _mno, (sf.two_vtx5curr_arc_(curr_arc_), curr_arc_.MNO_above_curr_arc_, _mno, sf.two_vtc5arcs_(curr_arc_.tree_children_), sf.two_vtc5arcs_(curr_arc_.final_unorder_above_arcs_), [above_arc_.supporting_weight for above_arc_ in curr_arc_.final_unorder_above_arcs_])
raise Exception((e, version, L, ls))
Exception: (AssertionError(((0, 0), 340104267295, 340022952607, [(1, 8)], [(1, 8)], [1256])), 1, 9, [1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281])




line 2051, in calc_side_product_between_
    assert s == _s, (s, _s, sf.two_vtx5curr_arc_(curr_arc_), sf.two_vtc5arcs_(unorder_ceil_arcs_))
AssertionError: (140222566, 121131639, (3, 7), [(6, 6), (3, 5)])
raise Exception((e, version, L, ls))
Exception: (AssertionError((140222566, 121131639, (3, 7), [(6, 6), (3, 5)])), 1, 9, [1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281])
37~35,56,67

assert MNO4whole == _mno, (version, L, ls, (imin, _imin), (MNO4whole, _mno), (inner_idx_arcs_, sorted_inner_arcs_))
AssertionError: (3, 9, [1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281], (0, 0), (340104267295, 340022952607), ([(1, 3), (1, 8), (3, 8), (4, 8), (5, 8), (6, 8)], [(0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 3)]))

[(1, 3), (1, 8), (3, 8), (4, 8), (5, 8), (6, 8)]
[(0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 3)]
# [1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281]
#   0,1,3,8
py script/matrix_chain_product.py ,matrix_chain_product__dynamic_programming__O_NNN ='[1260,2101,2273,1281]'
[]
[]
[(6117509013, 1, [2], 4)]
[(9508649073, 0, [1], 4)]

[[[
===
L = 9; ls = [1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281]
curr_arc_=(1, 3)
min_weight4curr_arc_=2101
curr_arc_.final_unorder_above_arcs_=[(2, 2)]
curr_arc_.unorder_ceil_arcs_=[(2, 2)]
curr_arc_.unorder_ceil_hidden_children_=[]
curr_arc_.MNO_above_curr_arc_=46127259607
curr_arc_.MNO_between_curr_arc_ceil_arcs_=46127259607
curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_=37472893
curr_arc_.supporting_weight=1230
curr_arc_=(3, 5)
min_weight4curr_arc_=2273
curr_arc_.final_unorder_above_arcs_=[(4, 4)]
curr_arc_.unorder_ceil_arcs_=[(4, 4)]
curr_arc_.unorder_ceil_hidden_children_=[]
curr_arc_.MNO_above_curr_arc_=180561987566
curr_arc_.MNO_between_curr_arc_ceil_arcs_=180561987566
curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_=81844849
curr_arc_.supporting_weight=2206
curr_arc_=(5, 7)
min_weight4curr_arc_=5002
curr_arc_.final_unorder_above_arcs_=[(6, 6)]
curr_arc_.unorder_ceil_arcs_=[(6, 6)]
curr_arc_.unorder_ceil_hidden_children_=[]
curr_arc_.MNO_above_curr_arc_=379744642122
curr_arc_.MNO_between_curr_arc_ceil_arcs_=379744642122
curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_=79119841
curr_arc_.supporting_weight=4799
curr_arc_=(3, 7)
min_weight4curr_arc_=2273
curr_arc_.final_unorder_above_arcs_=[(6, 6), (3, 5)]
curr_arc_.unorder_ceil_arcs_=[(4, 4), (6, 6)]
curr_arc_.unorder_ceil_hidden_children_=[(3, 5)]
curr_arc_.MNO_above_curr_arc_=455894203013
curr_arc_.MNO_between_curr_arc_ceil_arcs_=455894203013
curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_=210697869
curr_arc_.supporting_weight=2163
curr_arc_=(3, 8)
min_weight4curr_arc_=1281
curr_arc_.final_unorder_above_arcs_=[(6, 6), (4, 4)]
curr_arc_.unorder_ceil_arcs_=[(4, 4), (6, 6)]
curr_arc_.unorder_ceil_hidden_children_=[]
curr_arc_.MNO_above_curr_arc_=284468358615
curr_arc_.MNO_between_curr_arc_ceil_arcs_=284468358615
curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_=225563264
curr_arc_.supporting_weight=1261
curr_arc_=(1, 8)
min_weight4curr_arc_=1281
curr_arc_.final_unorder_above_arcs_=[(3, 8), (1, 3)]
curr_arc_.unorder_ceil_arcs_=[(2, 2), (6, 6), (4, 4)]
curr_arc_.unorder_ceil_hidden_children_=[(3, 8), (1, 3)]
curr_arc_.MNO_above_curr_arc_=336713127235
curr_arc_.MNO_between_curr_arc_ceil_arcs_=336713127235
curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_=268032062
curr_arc_.supporting_weight=1256
Traceback (most recent call last):
]]]






testing___________goto
词典序最先的最优三角化方案囗
词典序最先的最优三角化方案囗立方算法囗



#]]]'''


def _tt():
    d = 340104267295-340022952607
    print(d)
    xs = [1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281]
    for x in xs:
        if d%x == 0:
            print(x)
            print('  ', d//x)

    raise
#_tt()
def _tt():
    xs = [1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281]
    ks = [3,5,6,7]
        #(37,[35])~35,56,67
    s = sum(xs[i]*xs[j] for i,j in pairwise(ks))
    print(s)
    assert s == 140222566

    raise
#_tt()




if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call(globals(), None)
        #main()


