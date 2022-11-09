r'''[[[
e script/matrix_chain_product.py
[[
古典的动态编程(保存中间变量):O(N**3) #表格规模为O(N**2)，其中每一项的计算(min{...})为O(N)

e others/book/matrix_chain_product/矩阵乘法链.txt
e others/book/matrix_chain_product/On-instances-of-the-matrix-chain-product-problem-solved-in-linear-time (2009)(Sana).pdf.txt
    论文 只考察 单调的 矩阵乘法链维数序列 及其循环移动变体
      O(N)

e others/book/matrix_chain_product/Computation of matrix chain products I,II(1984)(Hu)(Shing)[polygon partitioning].pdf.txt
      O(NlogN)
]]


a*b*c
    (a*b)*c
    a*(b*c)




L2num_tests, upper4weight, version
py -m nn_ns.app.debug_cmd   script.matrix_chain_product
py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法 '--L2num_tests={L:L for L in range(2,10)}' '--upper4weight=10000' '--version=1'
py script/matrix_chain_product.py @随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法 '--L2num_tests={L:L for L in range(2,100)}' '--upper4weight=10000' '--version=2'


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

    矩阵乘法链囗所有最优打括号方案囗暂存子问题结果囗立方性算法
        matrix_chain_product__dynamic_programming__O_NNN
        std_api4matrix_chain_product__dynamic_programming__O_NNN
        tail4std_api4matrix_chain_product__dynamic_programming__O_NNN

    sort_idc_of_seq
    sort_idc
    collect_idx_ph_arcs_that_cut_local_max
    collect_vv_ph_arcs_that_cut_local_max
    merge_sort__2

    矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法
        matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N
        std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N
        tail4std_api4matrix_chain_product__special_case__single_increase_phase_and_single_decrease_phase__O_N
    mk_mno_tree_from_binary_arc_tree

    mk_offset_
    mk_unoffset_
    unoffset_arcs_
    iter_outer_arcs_of
    iter_inner_outer_arcs_from_inner_arcs
    mk_binary_arc_tree_from_inner_arcs
    mk_binary_arc_tree_from_arc2next_triangle_vtx
    mk_arc2next_triangle_vtx_from_inner_arcs
    is_triangle_order
    mk_arc2next_triangle_vtx_from_v2ordered_vtc
    mk_arc2another_triangle_vtc_from_v2ordered_vtc
    mk_v2ordered_vtc_from_inner_outer_arcs
    mk_v2unordered_vtc_from_inner_outer_arcs
    mk_v2sorted_vtc_from_v2unordered_vtc
    mk_v2ordered_vtc_from_v2sorted_vtc


    iter_randrange
    iter_list_of_randrange
    迭代囗随机生成囗矩阵乘法链维数序列
    迭代囗随机生成囗矩阵乘法链维数序列囗单调
    单调化囗
    单例测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法
    随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法
    '''.split()

from itertools import pairwise, chain, islice
from random import randrange
from heapq import nsmallest
    #nsmallest(n, iterable, key=None)
from seed.iters.is_sorted import is_sorted, is_strict_sorted
from collections import defaultdict
from seed.tiny import echo, fst, snd
from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
from seed.seq_tools.inverse_uint_bijection_array import inverse_uint_bijection_array
from seed.types.view.SeqLeftRotateView import SeqLeftRotateView
from seed.algo.bucket_sort.bucket_sort_per_row import bucket_sort_per_row

def check_pint_seq(ls, /):
    assert all(type(d) is int for d in ls)
    assert all(d > 0 for d in ls)
    ls[:0]
    len(ls)
def check_matrix_chain_product_arg(矩阵乘法链维数序列, /):
    check_pint_seq(矩阵乘法链维数序列)
    assert len(矩阵乘法链维数序列) >= 2
    assert len(矩阵乘法链维数序列[:2]) == 2

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

def std_api4matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    num_matrices2mno_begin_mids_end_tpls = matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列)
    mno_tree = tail4std_api4matrix_chain_product__dynamic_programming__O_NNN(矩阵乘法链维数序列, num_matrices2mno_begin_mids_end_tpls)
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
#def collect_idx_ph_arcs_that_cut_local_max(imin, imax, i2xv, /):
def collect_idx_ph_arcs_that_cut_local_max(imin, i2xv, /):
    'imin/idx -> i2xv[#ls/i2rv/[pint]{L} or inv_idc/i2vv/[vv]{L}#] -> (idx_ph_arcs/[(idx,idx)]{L-3}, [idx]{3})'
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
        #idx_ph_arcs.append(tuple(sorted([idx,idx0])))
        #idx_ph_arcs.append((idx,idx0))
        idx_ph_arcs.append((idx0,idx))
        return
    ilast = (imin-1)%L
    it = chain(range(imin+1, L), range(0, imin))
    idx_stack = [imin]
    idx_ph_arcs = []
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
    if not len(idx_stack)+len(idx_ph_arcs) == L-1: raise logic-err

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
    assert len(idx_ph_arcs) == L-3
    #assert idx_stack == [i0,i1,i2] or idx_stack == [i0,i2,i1]
    return idx_ph_arcs, idx_stack


def collect_vv_ph_arcs_that_cut_local_max(vv2i, i2vv, /):
    'idc/vv2i/[i]{L} -> i2vv -> vv_ph_arcs/[(vv,vv)]{L-3}'
    #output (L-3) arcs
    L = len(vv2i)
    if not L >= 3: raise IndexError#LengthError

    def pop_(vv, /):
        vv1 = vv_stack.pop() #discard
        vv0 = vv_stack[-1]
        #assert vv0 < vv1
        #assert vv < vv1
        #vv_ph_arcs.append(tuple(sorted([vv,vv0])))
        #vv_ph_arcs.append((vv,vv0))
        vv_ph_arcs.append((vv0,vv))
        return
    i0 = imin = vv2i[0]
    ilast = (imin-1)%L
    it = chain(range(imin+1, L), range(0, imin))
    assert i2vv[i0] == 0
    vv_stack = [0]
    vv_ph_arcs = []
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
    if not len(vv_stack)+len(vv_ph_arcs) == L-1:
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
    assert len(vv_ph_arcs) == L-3
    assert vv_stack == [0,1,2] or vv_stack == [0,2,1]
    return vv_ph_arcs

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
    idx_ph_arcs, idx_stack = collect_idx_ph_arcs_that_cut_local_max(imin_, i2rv_)
    if 0:
        #bug: not at tail
        while idx_ph_arcs and imin_ in idx_ph_arcs[-1]:
            #bug:case(0,9,4)->arc(0,4):while idx_ph_arcs and idx_ph_arcs[-1][1]==imin_:
            idx_ph_arcs.pop()
    idx_ph_arcs = [arc for arc in idx_ph_arcs if not imin_ in arc]
    assert not any(idx_ == imin_ for arc in idx_ph_arcs for idx_ in arc), idx_ph_arcs
    idx_ph_arcs = [arc for arc in idx_ph_arcs if arc[0] < imax_ < arc[1]]








    def side_product_between(curr_arc, ceil_arc, /):
        if ceil_arc is top_arc:
            return side_product(curr_arc)
        return side_product(curr_arc) -side_product(ceil_arc) +base_product(ceil_arc)
    def side_product(idx_arc, /):
        (i_,j_) = idx_arc
        return side_products__from0[j_] -side_products__from0[i_]
    def base_product(idx_arc, /):
        (i_,j_) = idx_arc
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
        assert 0 <= i_ <= x_ < y_ <= j_ < L, ((i_, x_, y_, j_, L), idx_ph_arcs)
        return (i_, x_, y_, j_)

    def H0(curr_arc, above_arc, /):
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
    # 因为『?//D』supporting_weight4curr_arc可能为0，supporting_weight4imax改为-1
    top_arc = True #imax
    bottom_arc = False #imin
    supporting_weight4imax = -1
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
        idx_ph_arcs, idx_stack = collect_idx_ph_arcs_that_cut_local_max(imin, i2rv)

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
        vv_ph_arcs = collect_vv_ph_arcs_that_cut_local_max(vv2i, i2vv)

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
            inner_arcs = unoffset_arcs_(L, imin, idx_all_inner_arcs_)
        return MNO4whole, inner_arcs


    MNO4whole, inner_arcs = f()
    #rint(f'inner_arcs = {inner_arcs}')

    end4ground_outer_arc = 0
    binary_arc_tree = mk_binary_arc_tree_from_inner_arcs(L, end4ground_outer_arc, inner_arcs)
    mno_tree = mk_mno_tree_from_binary_arc_tree(ls, binary_arc_tree)
    assert MNO4whole == mno_tree[0], (L, ls, inner_arcs, MNO4whole, mno_tree)
    return mno_tree

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
    def unoffset_(i, /):
        return (i+imin)%L
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
def iter_inner_outer_arcs_from_inner_arcs(L, inner_arcs, /):
    yield from inner_arcs
    outer_arcs = iter_outer_arcs_of(L)
    yield from outer_arcs

def mk_binary_arc_tree_from_inner_arcs(L, end4ground_outer_arc, inner_arcs, /):
    arc2next_triangle_vtx = mk_arc2next_triangle_vtx_from_inner_arcs(L, inner_arcs)
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
        assert (x==(y+1)%L) is (may_v is None)
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
def mk_arc2next_triangle_vtx_from_inner_arcs(L, inner_arcs, /):
    inner_outer_arcs = iter_inner_outer_arcs_from_inner_arcs(L, inner_arcs)
    v2ordered_vtc = mk_v2ordered_vtc_from_inner_outer_arcs(L, inner_outer_arcs)
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
def mk_v2ordered_vtc_from_inner_outer_arcs(L, inner_outer_arcs, /):
    v2unordered_vtc = mk_v2unordered_vtc_from_inner_outer_arcs(L, inner_outer_arcs)
    v2sorted_vtc = mk_v2sorted_vtc_from_v2unordered_vtc(L, v2unordered_vtc)
    v2ordered_vtc = mk_v2ordered_vtc_from_v2sorted_vtc(L, v2sorted_vtc)
    return v2ordered_vtc
def mk_v2unordered_vtc_from_inner_outer_arcs(L, inner_outer_arcs, /):
    #inner_outer_arcs = [*inner_outer_arcs]; print(inner_outer_arcs)
    v2unordered_vtc = [[] for _ in range(L)]
    for i, j in inner_outer_arcs:
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
                assert mno_tree__testing[0] == mno_tree__ans[0], (version, L, ls, mno, (mno_tree__testing, mno_tree__ans))
        else:
            raise Exception(version)
    except Exception as e:
        raise Exception((e, version, L, ls))
    f()

def 随机测试囗囗矩阵乘法链囗多边形囗最优切分方案囗只有一个升降周期的特例囗线性算法(*, L2num_tests, upper4weight, version):
    lss = [
    #非单调:[7265, 8194, 2762, 7363, 7947]
    [1,1]
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
    vv_ph_arcs=[(2,1),(0,1)]
    idx_ph_arcs=[(1,3),(0,3)]
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
    vv_ph_arcs=[(1,3),(1,2)]
    idx_ph_arcs=[(1,3),(1,4)]
    H0((1,3), 2) = 4502*9824*6895



line 549, in _H0
    assert 0 <= i_ <= x_ < y_ <= j_ < L, (i_, x_, y_, j_, L)
Exception: (AssertionError((6, 3, 4, 8, 12)), [5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571, 1136, 4140, 5674])
    [5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571, 1136, 4140, 5674]
    [1136, 4140, 5674, 5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571]
    bug:
        xxx:offseted_i2vv=[0,4,6,7,11,10,9,8,5,3,2,1]
        vv_ph_arcs=[(7,10),(7,9),(7,8),(7,5),(6,5),(4,5),(4,3),(0,3),(0,2)]
        vv_ph_arcs=[(7,10),(7,9),(7,8),(7,5),(6,5),(4,5),(4,3)]
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
    真正有毛病的是i2vv&vv_ph_arcs
        上面 将 [000,555,333,333] 转化为 [0,3,2,1] 以满足单调性，是错的！
            应当是:[0,3,1,2]
            反正one_sweep_algorithm并不在乎 单调性

再来一次:
    [1136, 4140, 5674, 5680, 7956, 6693, 6613, 6613, 4220, 3284, 1642, 1571]
    offseted_i2vv=[0,4,6,7,11,10,8,9,5,3,2,1]
        one_sweep_algorithm(vv_ph_arcs)单调性 无关紧要
    vv_ph_arcs=[(7,10),(7,8),(8,5),(7,5),(6,5),(4,5),(4,3),(0,3),(0,2)]
    idx_ph_arcs=[(3,5),(3,6),(6,8),(3,8),(2,8),(1,8),(1,9)]
异常:
    (x_,y_)=(3,4)不存在，其实是top_arc/imax_/4-->(3,4)
    (i_,j_)=(6,8)存在于idx_ph_arcs
    但是 由于 不满足 单调性:(6,8)其实是v_arc??
    新增:
        idx_ph_arcs = [arc for arc in idx_ph_arcs if arc[0] < imax_ < arc[1]]


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

#]]]'''



if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call(globals(), None)
        #main()


