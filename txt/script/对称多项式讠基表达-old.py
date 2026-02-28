#__all__:goto
r'''[[[
e script/对称多项式讠基表达.py
view ../../python3_src/seed/recognize/rgnr/example/example4SimpleRecognizer.py

script.对称多项式讠基表达
py -m nn_ns.app.debug_cmd   script.对称多项式讠基表达 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.对称多项式讠基表达:__doc__ -ht # -ff -df

[[
@20250325
copy from:view others/数学/polynomial/拆分冫对称多项式讠基础.txt
===
view script/symmetric_poly2basic.py

对称多项式:symmetric polynomial
???如何用『基础对称多项式』表达『任意对称多项式』???

基础对称多项式:
[n,k::uint][n >= k][xs::[symbol]{len==n}]:
  #basic-symmetric-polynomial
  [bspoly(n,k;xs) =[def]= sum[II[xs[j] | [j:<-js]] | [js:<-combinations(range(n),k)]]]
  [bspoly(3,2;xs) == (x0*x1+x1*x2+x2*x0)]
  [bspoly(n,0;xs) == 1]
  [[0<=n<k] -> [bspoly(n,k;xs) == 0]]
简单对称多项式牜加型:
[n::uint][exp2repeat::{pint:pint}][k := sum(exp2repeat.values())][n >= k][xs::[symbol]{len==n}]:
  # [_exp2repeat:={0:n-k,**exp2repeat} if n>k else exp2repeat]
  [_es:=[0]*(n-k)++[exp for exp,repeat in exp2repeat.items() for _ in range(repeat)]]
  #sum-symmetric-polynomial
  [sspoly(n,exp2repeat;xs) =[def]= sum[II(xs[j]**e for j, e in enumerate(es) if e) | [es:<-{*permutations(_es)}]]]
  [sspoly(4,{1:2,3:1};xs) == (x0*x1*x2**3+x0*x1*x3**3 + x1*x2*x0**3+x1*x2*x3**3 + ...)]
  [sspoly(n,{};xs) == 1]
  [[0<=n<k] -> [sspoly(n,k;xs) == 0]]
  [m := sum(exp*repeat for exp,repeat in exp2repeat.items())]
  [[[n>=m] -> [sspoly(n,exp2repeat;xs) 以 {bspoly(n,k;xs) | [k:<-[0..]]} 表达 形式不变]]]
    #定理:对称简并单项式以对称简并基础单项式表达则形式不变
  ==>>:
[xs::[symbol]{len==+oo}]:
  # [f(xs;z) := II[(1+xs[j]*(-z**-1)) | [j:<-[0..]]]]
  # [f(xs;z) == II[(1-xs[j]/z) | [j:<-[0..]]] == sum[bspoly(+oo,k;xs)/z**k | [k:<-[0..]]] == sum[bs[k]/z**k | [k:<-[0..]]]] where [bs[k] == bspoly(+oo,k;xs)][bs[1] == bspoly(+oo,1;xs) == 1]
  # SUM_IIgbspK = (...+K[?]*(...*bs[k]**e4bs[k]*...)+...) ~ [(K, {k:e4bs[k]})]
  #     [(int{=!=0}, {uint:pint})]
  # SUM_gsspK = (...+K[?]*(...*(II(xs[...:...+e2ns[e]]))**e*...)+...) ~ [(K, {e:e2ns[e]})]
  #     [(int{=!=0}, {pint:pint})]
  #
  #单项式对称化==>>:
  对称简并单项式
  #symmetric-degenerate-monomial
  [gsspoly(exp2repeat;xs) =[def]= sspoly(+oo,exp2repeat;xs)]
    #regex"gssp\._(\d+[a-j]+)*"
    #   exp-数字
    #   repeat-字母
    #带系数:regex"gsspK\._(\d+[a-j]+)*\d*K[np]"
    # [np] <=> [-+]
    #和纟带系数:regex"SUM_gsspK\._((\d+[a-j]+)*\d*K[np])*"

  对称简并基础单项式
  #symmetric-degenerate-basic-monomial
  [gbspoly(k;xs) =[def]= bspoly(+oo,k;xs)]
    #regex"gbsp\._\d+"
    #   k-数字
    #乘积:regex"IIgbsp\._(\d+[a-j]+)*"
    #   k-数字
    #   exp-字母
    #和纟带系数乘积:regex"SUM_IIgbspK\._((\d+[a-j]+)*\d*K[np])*"
    ==>>:
    SUM_gsspK用SUM_IIgbspK表达简单对称多项式牜乘型:
[n::uint][coeffs::[number]][xs::[symbol]{len==n}]:
  #mul-symmetric-polynomial
  [mspoly(n,coeffs;xs) =[def]= II[sum[coeffs[k]*xs[j]**k | [k:<-[0..<len(coeffs]]] | [j:<-[0..<n]]]]
  [mspoly(3,[1,2,5];xs) == (1+2*x0+5*x0**2)*(1+2*x1+5*x1**2)*(1+2*x2+5*x2**2)]
  view others/数学/polynomial/范巛共轭根纟多项式.txt
    ==>> resultant


??? 递归关系:
  bspoly(n,k;xs)
  sspoly(n,exp2repeat;xs)
  mspoly(n,coeffs;xs)
#拆出xs[n-1]:
[[k>1] -> [bspoly(n,k;xs) == xs[n-1]*bspoly(n-1,k-1;xs[:n-1]) +bspoly(n-1,k;xs[:n-1])]]

xxx:[[len(exp2repeat)>0] -> [min_e:=min(exp2repeat)] -> [repeat4min_e:=exp2repeat[min_e]] -> [_exp2repeat:=exp2repeat\-\{min_e:repeat4min_e}] -> [sspoly(n,exp2repeat;xs) == sspoly(n,_exp2repeat;xs)*bspoly(n,repeat4min_e;xs)**min_e +-???]]
xxx:[[len(exp2repeat)>0] -> [sspoly(n,exp2repeat;xs) -II(bspoly(n,repeat;xs)**exp for exp,repeat in exp2repeat.items()) == +-???]]
#拆出xs[n-1]:
[[len(exp2repeat)>0] -> [_n:=n-1] -> [_xs:=xs[:n-1]] -> [_poly5e_(e) := ??? if e==0 then (if n==sum(exp2repeat.values()) then 0 else sspoly(_n,exp2repeat;_xs)) else (sspoly(_n,exp2repeat\-\{e:exp2repeat[e]};_xs))] -> [sspoly(n,exp2repeat;xs) == sum[_poly5e_(e)*xs[n-1]**e | [e:<-{0,*exp2repeat}]]]]
  无用！

bug:[rank4sspoly_(sspoly(n,exp2repeat;xs)) =[def]= (-len(exp2repeat),max(exp2repeat, default=0))]
bug:[rank4sspoly_(sspoly(n,exp2repeat;xs)) =[def]= (-len(exp2repeat),sorted(exp2repeat.items(),reverse=True))]
  # 成立:[rank4sspoly_(sspoly(n,exp2repeat;xs)) > rank4sspoly_(sspoly(n,_e2r;xs))]
  # 但不一定:[rank4sspoly_(sspoly(n,exp2repeat;xs)) > rank4sspoly_(sspoly(n,_exp2repeat;xs))]
[rank4sspoly_(sspoly(n,exp2repeat;xs)) =[def]= (sorted(exp2repeat.items(),reverse=True))]
  # 但不一定成立:[rank4sspoly_(sspoly(n,exp2repeat;xs)) > rank4sspoly_(sspoly(n,_e2r;xs))]
  # 成立:[rank4sspoly_(sspoly(n,exp2repeat;xs)) > rank4sspoly_(sspoly(n,_exp2repeat;xs))]
#拆分后,rank4sspoly_下降#保持齐次(m不变)
[[max(exp2repeat, default=0)==0] -> [k := sum(exp2repeat.values())] -> [[exp2repeat=={}][k==0][sspoly(n,exp2repeat;xs) == bspoly(n,k;xs) == 1]]]
  # ==0
[[max(exp2repeat, default=0)==1] -> [k := sum(exp2repeat.values())] -> [[exp2repeat=={1:k}][k>=1][sspoly(n,exp2repeat;xs) == bspoly(n,k;xs)]]]
  # ==1
[[max(exp2repeat, default=0)>=2] -> [k := sum(exp2repeat.values())] -> [_exp2repeat:={e-1:r for e,r in exp2repeat.items() if e>=2}] -> [sspoly(n,exp2repeat;xs) == (bspoly(n,k;xs)*sspoly(n,_exp2repeat;xs) -sum[_c*sspoly(n,_e2r;xs) | [(_c,_e2r):<-_iter4tail_partition4sspoly_(k,_exp2repeat)]])]]
  # >=2
  # [rank4sspoly_(sspoly(n,exp2repeat;xs)) > rank4sspoly_(sspoly(n,_exp2repeat;xs))]
  # [rank4sspoly_(sspoly(n,exp2repeat;xs)) > rank4sspoly_(sspoly(n,_e2r;xs))]
  # ==>> 定理:对称简并单项式以对称简并基础单项式表达则形式不变
  where:
   #xxx:... -> [r1:=exp2repeat.get(1,0)] -> [_c1:=C(n-(k-r1);r1)] -> ...
   [r1:=exp2repeat.get(1,0)]
   [_r1:=_exp2repeat.get(1,0)]
  [_iter4tail_partition4sspoly_(k,_exp2repeat) := [(_c,_e2r) | [[sz4miss:<-[1..=k]][(_c,_e2r):<-_iter4tail_partition4sspoly__inner_(k,_exp2repeat,sz4miss)]]]]
    # [_c1:=1][sz4miss==0] is the lhs:(_c1,exp2repeat)
  [_iter4tail_partition4sspoly__inner_(k,_exp2repeat,sz4miss) := [(_c,_e2r) | [
    # [sz4miss:<-[0..=k]]
    #   but used only:[sz4miss:<-[1..=k]]
    [_e2num_overlaps::{pint:pint}]
    [_e2num_overlaps.keys() <= _exp2repeat.keys()]
    [sum(_e2num_overlaps.values()) == k-sz4miss]
    [all(1<=num_overlaps<=_exp2repeat[e] for e,num_overlaps in _e2num_overlaps.items())]
    [_e2r := add4counter_(subtract4counter_(_exp2repeat,_e2num_overlaps), {e+1:num_overlaps for e,num_overlaps in _e2num_overlaps.items()}, {1:sz4miss})]
    [_c:=II(C(r;(if e==0 then sz4miss else _e2num_overlaps.get(e-1,0))) for e,r in _e2r.items())]
    # [[_e2r::{pint:pint}][sum(_e2r.values()) == k+sz4miss[#每项变量数增加#]][sum(exp*repeat for exp,repeat in _e2r.items()) == sum(exp*repeat for exp,repeat in exp2repeat.items())[#保持齐次#]][_c>0]]
    ]]]
subtract4counter_
add4counter_
#update4counter_
#remove_zero_keys_or_values4counter_
#sorted_items5counter_

===
]]

py_adhoc_call   script.对称多项式讠基表达   @f
from script.对称多项式讠基表达 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#类标识符表示讠有序对纟自然数扌:goto
from seed.recognize.rgnr.utils.auxiliary import Helper4mk_rgnr_, mk_args4recur_call_ex_
    # hmk = Helper4mk_rgnr_(rgnr_name_server)
    # (args4recur_call, name2rgnr, name2cipost, hmk, FuncAccess, basic_recognize_) = mk_args4recur_call_ex_(seq_view, seq_begin_idx=None, seq_end_idx=None, name2rgnr=None, static_globals4rgnr_group=None, name2ref_rgnr=None, name2cipost=None, ignore=False, local_ctx=None)

from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
def _API():
    def merge_two_sorted_iterables(lefts, rights
        #, *, __le__=None, Left=None, Right=None):
        , *, left_key=None, right_key=None, before=None
        , Left=None, Right=None):
        ...
#end-def _API():
import re
import string
from itertools import groupby #islice
from functools import cached_property
from seed.tiny_.check import check_type_is, check_int_ge
from seed.math.II import II
from seed.math.combination import C

from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...


def 枚举冫进制数牜变基数牜无零扌(radixes, v0=None, /):
    'radixes/[pint{>=2}] -> rev_sorted[(j/uint%len(radixes),digit/pint{<radixes[j]})]'
    #for:_iter4tail_partition4sspoly_
    if v0 is None:
        v0 = []
    ls = v0
    yield ls
    if len(radixes) == 0:
        return
    L = len(radixes)
    j = 0 # next inc at j
    while j < L:
        if not ls or ls[-1][0] > j:
            d = 1
            # [1 <= d <= radixes[j]]
        else:
            (_j, d) = ls.pop()
            assert _j==j
            assert d > 0
            # [1 <= d < radixes[j]]
            d += 1
            # [2 <= d <= radixes[j]]
            # [1 <= d <= radixes[j]]
        # [1 <= d <= radixes[j]]
        j, d
        if not d < radixes[j]:
            j += 1
            continue
        # [1 <= d < radixes[j]]
        ls.append((j, d))
        yield ls
        j = 0
#end-def 枚举冫进制数牜变基数牜无零扌(radixes, v0=None, /):
def _iter4tail_partition4sspoly_(k, _exp2repeat, /):
    'k -> _exp2repeat -> Iter (_c,_e2r)'
    m = k + sum(exp*repeat for exp,repeat in _exp2repeat.items())
    e_r_pairs = rev_sorted_items(_exp2repeat)
    exps = list(map(fst, e_r_pairs))
    radixes = [1+r for e, r in e_r_pairs]
    it = 枚举冫进制数牜变基数牜无零扌(radixes)
    for j_d_pairs in it:
        _e2num_overlaps = {exps[j]:d for j, d in j_d_pairs}
        num_overlaps = sum(_e2num_overlaps.values())
        sz4miss = k-num_overlaps
        if sz4miss == 0:
            assert _e2num_overlaps == _exp2repeat
            continue
        assert sz4miss > 0
        # [1 <= sz4miss <= k]
        [_e2r := add4counter_(subtract4counter_(_exp2repeat,_e2num_overlaps), {e+1:num_overlaps for e,num_overlaps in _e2num_overlaps.items()}, {1:sz4miss})]
        [_c:=II(C(r,(sz4miss if e==0 else _e2num_overlaps.get(e-1,0))) for e,r in _e2r.items())]
        assert m == sum(exp*repeat for exp,repeat in _e2r.items())
        yield (_c, _e2r)
#end-def _iter4tail_partition4sspoly_(k, _exp2repeat, /):
def add4counter_(lhs, rhs, /):
    e2r = {**lhs}
    for e, r in rhs.items():
        e2r[e] = e2r.get(e,0) + r
    return _std4counter_(e2r)
def subtract4counter_(lhs, rhs, /):
    e2r = {**lhs}
    for e, r in rhs.items():
        #e2r[e] = e2r.get(e,0) - r
        e2r[e] -= r
    return _std4counter_(e2r)
def _std4counter_(e2r, /):
    if not all(e > 0 and r > 0 for e, r in e2r.items()):
        if not all(e >= 0 and r >= 0 for e, r in e2r.items()):raise Exception(e2r)
        e2r = {e:r for e, r in e2r.items() if not (e == 0 or r == 0)}
        assert all(e > 0 and r > 0 for e, r in e2r.items())
    return e2r
def remove_zero_keys_or_values4counter_(d, /):
    if not all(d.values()):
        d = {k:v for k,v in d.items() if v}
    return d

#class 魖:#(ABC):
    #__slots__ = ()
    #___no_slots_ok___ = True
class Counter:
    '[exp2repeat :: {pint:pint}]'
    def __init__(sf, exp2repeat, /):
        exp2repeat = {**exp2repeat}
        for exp, repeat in exp2repeat.items():
            check_int_ge(0, exp)
            check_int_ge(0, repeat)
        exp2repeat = remove_zero_keys_or_values4counter_(exp2repeat)
        sf._exp2repeat = exp2repeat
    @property
    def exp2repeat(sf, /):
        return sf._exp2repeat
    @cached_property
    def rev_sorted_items(sf, /):
        rev_sorted_items = sorted_items5counter_(sf.exp2repeat, reverse=True)
        return rev_sorted_items
    def __add__(sf, ot, /):
        cls = type(sf)
        e_r_pairs = merge_two_sorted_iterables(sf.rev_sorted_items, ot.rev_sorted_items, left_key=fst, right_key=fst, before=int.__gt__)
        exp2repeat = {e:sum(map(snd, e_r_pairs)) for e, e_r_pairs in groupby(e_r_pairs, key=fst)}
        return cls(exp2repeat)
    def __sub_(sf, ot, /):
        cls = type(sf)
        e2r4ot = ot.exp2repeat
        assert (ot.exp2repeat.keys() <= sf.exp2repeat.keys()), (set(ot.exp2repeat) - set(sf.exp2repeat))
        # [ot.exp2repeat.keys() <= sf.exp2repeat.keys()]
        exp2repeat = {e:r-e2r4ot[e] for e, r in sf.rev_sorted_items}
        return cls(exp2repeat)
            # raise if there are some values neg
    #def __sub_(sf, ot, /):
_tbl409aj = str.maketrans(string.digits, string.ascii_lowercase[:10])
def letters5str8digits_(str8digits, /):
    return str8digits.translate(_tbl409aj)
assert letters5str8digits_('09') == 'aj'
_tbl4aj09 = str.maketrans(string.ascii_lowercase[:10], string.digits)
def letters2str8digits_(letters8digits, /):
    return letters8digits.translate(_tbl4aj09)
assert letters2str8digits_('aj') == '09'
def 类标识符表示巛有序对纟自然数扌(header, uint_pairs, /):
    def __():
        for u, v in uint_pairs:
            check_int_ge(0, u)
            check_int_ge(0, v)
            yield str(u)
            yield letters5str8digits_(str(v))
    return header + ''.join(__())
_re409aj = re.compile('([0-9]+|[a-j]+)')
_re4digits = re.compile('([0-9]+)')
def 类标识符表示讠有序对纟自然数扌(header, s, /):
    if not s.startswith(header):raise ValueError(s, header)
    _s = s[len(header):]
    ss = _re4digits.split(_s)
    if not (len(ss)&1):raise ValueError(s)
    if ss[0]:raise ValueError(s)
    if not ss[-1]:raise ValueError(s)
    digits_strs = ss[1::2]
    letters_strs = ss[2::2]
    if not len(digits_strs) == len(letters_strs):raise ValueError(s)
    k_strs = digits_strs
    v_strs = letters5str8digits_(letters_strs)
    ks = map(int, k_strs)
    vs = map(int, v_strs)
    return tuple(zip(ks, vs))
    k2v = dict(zip(ks, vs))
    return k2v
def parse4sum_k_u2u_(s, /):
    parser4sum_k_u2u
    . .
def _mk_parser4sum_k_u2u_(s, /):
    from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import SimpleRecognizeReply, Args4recur_call, Common4recur_call, SimpleRecognizerNameServer, InputSeqEx
    name2rgnr = {}
    rgnr_name_server = SimpleRecognizerNameServer(name2rgnr, static_globals4rgnr_group=None, name2ref_rgnr=None)
    hmk = Helper4mk_rgnr_(rgnr_name_server)
    ######################
    rgnr3digits = hmk.ref('digits')
    rgnr3ajs = hmk.ref('ajs')
    rgnr3dsKnp = hmk.ref('dsKnp')
    rgnr3main = hmk.ref('main')
    ######################
    rgnr3uint8digits = hmk.post6ok(rgnr3digits, int, False)
    rgnr3uint8ajs = hmk.post6ok(rgnr3ajs, uint5ajs:=letters2str8digits_, False)
    rgnr3uint8dsKnp = hmk.post6ok(hmk.flatten4Rope(rgnr3dsKnp, False), tag_sign_, False)
    rgnr3u_u = hmk.flatten4Rope(hmk.chain([box(rgnr3uint8digits), box(rgnr3uint8ajs)]))
    rgnr3u2u = hmk.flatten4Rope(hmk.many(box(rgnr3u_u), 0, None))
    rgnr3u2u_K = hmk.flatten4Rope(hmk.chain([box(rgnr3u2u), box(rgnr3dsKnp)]))
    ######################
    name2rgnr['digits'] = hmk.py_regex(r'\d+', True)
    name2rgnr['ajs'] = hmk.py_regex(r'[a-j]+', True)
    name2rgnr['dsKnp'] = hmk.flatten4Rope(hmk.chain([box(rgnr3uint8digits), box(hmk.py_regex(r'K[np]', True))]))
    name2rgnr['main'] = hmk.flatten4Rope(hmk.many(box(rgnr3u2u_K), 0, None))
    ######################
    rgnz_reply__main = basic_recognize_('main', args4recur_call)
    ######################
    ######################
    input_seq_ex = InputSeqEx(seq_view, seq_begin_idx, seq_end_idx)
    name2rgnr = _dict5may_dict_(name2rgnr)
    #static_globals4rgnr_group = _dict5may_dict_(static_globals4rgnr_group)
    #name2ref_rgnr = _dict5may_dict_(name2ref_rgnr)
    rgnr_name_server = SimpleRecognizerNameServer(name2rgnr, static_globals4rgnr_group, name2ref_rgnr)
    hmk = Helper4mk_rgnr_(rgnr_name_server)
    name2cipost = _dict5may_dict_(name2cipost)
    common4recur_call = Common4recur_call(name2cipost, rgnr_name_server, input_seq_ex)
    args4recur_call = Args4recur_call(common4recur_call, begin_idx=input_seq_ex.seq_begin_idx, end_idx=input_seq_ex.seq_end_idx, ignore=ignore, local_ctx=local_ctx)
    #rgnz_reply = SimpleRecognizeReply(end_idx4reply, rgnz_eresult)
    #rgnz_reply = basic_recognize_('main', args4recur_call)
    #f = FuncAccess(__name__, 'f')
    FuncAccess
    basic_recognize_
    return (args4recur_call, name2rgnr, name2cipost, hmk, FuncAccess, basic_recognize_)


class 乸对称简并单项式:
    'gsspoly(exp2repeat;xs)'
    def __init__(sf, exp2repeat, /):
        sf._ctr = Counter(exp2repeat)
    @property
    def exp2repeat(sf, /):
        '-> exp2repeat'
        return sf._ctr.exp2repeat
    @cached_property
    def 类标识符表示(sf, /):
        '-> str{fmt:gssp}'
        ls = sf._ctr.rev_sorted_items
        return 类标识符表示巛有序对纟自然数扌(sf.header, ls)
    header = 'gssp._'

    @cached_property
    def num_vars_per_monomial(sf, /):
        '-> k/num_vars_per_monomial/变量数量每单项式'
        return sum(sf.exp2repeat.values())
    @cached_property
    def total_degree(sf, /):
        '-> total_degree/总幂次数每单项式'
        return sum(exp*repeat for exp,repeat in sf.exp2repeat.items())
    def eval_(sf, xs, /):
class 乸对称简并基础单项式:
    'gbspoly(k;xs) # [exp2repeat==if k==0 then {} else {1:k}]'
    def __init__(sf, k, /):
    @property
    def k(sf, /):
        '-> k'
        return sf._k
    @cached_property
    def 类标识符表示(sf, /):
        '-> str{fmt:gbsp}'
    header = 'gbsp._'
    @cached_property
    def num_vars_per_monomial(sf, /):
        '-> k/num_vars_per_monomial/变量数量每单项式'
        return sf.k
    @cached_property
    def total_degree(sf, /):
        '-> total_degree/总幂次数每单项式'
        return sf.k
    def eval_(sf, xs, /):
class 乸对称简并基础单项式表达:
    '[对称简并基础单项式表达 ~=~ [([(对称简并基础单项式/uint,幂次数/pint)], 系数/int{!=0})]]'
    def __init__(sf, iter__gbspoly_exp_pairs__coeff__pairs, /):
    @cached_property
    def 类标识符表示(sf, /):
        '-> str{fmt:SUM_IIgbspK}'
    header = 'SUM_IIgbspK._'
    @cached_property
    def is_homogeneous(sf, /):
        '-> bool'
    def __add__(sf, ot, /):
    def __sub__(sf, ot, /):
    def __mul_(sf, ot, /):

        . .
    def eval_(sf, xs, /):
class 魖匴对称简并单项式讠对称简并基础单项式表达(ABC):
    __slots__ = ()
    'cache <-> cache_file'
    def 枚举冫对称简并单项式巛类标识符表示扌(sf, s, /):
        'str{fmt:SUM_gsspK} -> Iter 对称简并单项式'
    def 枚举冫对称简并基础单项式巛类标识符表示扌(sf, s, /):
        'str{fmt:SUM_IIgbspK} -> Iter 对称简并基础单项式'
    def 对称简并单项式讠对称简并基础单项式表达扌(sf, 对称简并单项式, /):
        '[缓存] => 对称简并单项式 -> 对称简并基础单项式表达'
        鬽对称简并基础单项式表达 = sf.罓查找冫对称简并单项式讠鬽对称简并基础单项式表达扌(对称简并单项式)
        if 鬽对称简并基础单项式表达 is None:
            对称简并基础单项式表达 = sf.罓对称简并单项式讠对称简并基础单项式表达扌(对称简并单项式)
            sf.罓保存冫对称简并单项式辻鬽对称简并基础单项式表达扌(对称简并单项式, 对称简并基础单项式表达)
        else:
            对称简并基础单项式表达 = 鬽对称简并基础单项式表达
        对称简并基础单项式表达
        return 对称简并基础单项式表达
    @abstractmethod
    def 罓保存冫对称简并单项式辻鬽对称简并基础单项式表达扌(sf, 对称简并单项式, 对称简并基础单项式表达, /):
        '[缓存] => (对称简并单项式, 对称简并基础单项式表达) -> None'
    @abstractmethod
    def 罓查找冫对称简并单项式讠鬽对称简并基础单项式表达扌(sf, 对称简并单项式, /):
        '[缓存] => 对称简并单项式 -> may 对称简并基础单项式表达'
    #@abstractmethod
    def 罓对称简并单项式讠对称简并基础单项式表达扌(sf, 对称简并单项式, /):
        '[无缓存] => 对称简并单项式 -> 对称简并基础单项式表达'
        exp2repeat = 对称简并单项式.exp2repeat
        k = 对称简并单项式.num_vars_per_monomial
        #m = 对称简并单项式.total_degree
        #对称简并单项式.类标识符表示
        recur_ = sf.对称简并单项式讠对称简并基础单项式表达扌
        gbspoly_exp_pairs__coeff__pairs = []
        gbspoly = 乸对称简并基础单项式(k)
        gbspoly_exp_pairs__coeff__pairs = [([(gbspoly, 1)], 1)]
        SUM_IIgbspK = 乸对称简并基础单项式表达(gbspoly_exp_pairs__coeff__pairs)
        max_e = max(exp2repeat, default=0)
        if max_e <= 1:
            # [[max(exp2repeat, default=0)==0] -> [k := sum(exp2repeat.values())] -> [[exp2repeat=={}][k==0][sspoly(n,exp2repeat;xs) == bspoly(n,k;xs) == 1]]]
            # [[max(exp2repeat, default=0)==1] -> [k := sum(exp2repeat.values())] -> [[exp2repeat=={1:k}][k>=1][sspoly(n,exp2repeat;xs) == bspoly(n,k;xs)]]]
            assert exp2repeat == {} if max_e == 0 else exp2repeat == {1:k}
            SUM_IIgbspK;pass
        else:
            # [[max(exp2repeat, default=0)>=2] -> [k := sum(exp2repeat.values())] -> [_exp2repeat:={e-1:r for e,r in exp2repeat.items() if e>=2}] -> [sspoly(n,exp2repeat;xs) == (bspoly(n,k;xs)*sspoly(n,_exp2repeat;xs) -sum[_c*sspoly(n,_e2r;xs) | [(_c,_e2r):<-_iter4tail_partition4sspoly_(k,_exp2repeat)]])]]
            [_exp2repeat:={e-1:r for e,r in exp2repeat.items() if e>=2}]
            gsspoly = 乸对称简并单项式(_exp2repeat)
            _SUM_IIgbspK = recur_(gsspoly)
            SUM_IIgbspK *= _SUM_IIgbspK
            for (_c,_e2r) in _iter4tail_partition4sspoly_(k,_exp2repeat):
                gsspoly = 乸对称简并单项式(_e2r)
                _SUM_IIgbspK = recur_(gsspoly)
                SUM_IIgbspK -= _SUM_IIgbspK*_c
        SUM_IIgbspK
        return SUM_IIgbspK
    def __repr__(sf, /):
        return repr_helper(sf, *args, **kwargs)
class 匴对称简并单项式讠对称简并基础单项式表达(魖匴对称简并单项式讠对称简并基础单项式表达):
    'cache <-> cache_file'
    ___no_slots_ok___ = True
    @override
    def 罓保存冫对称简并单项式辻鬽对称简并基础单项式表达扌(sf, 对称简并单项式, 对称简并基础单项式表达, /):
        '[缓存] => (对称简并单项式, 对称简并基础单项式表达) -> None'
        . .TODO
    @override
    def 罓查找冫对称简并单项式讠鬽对称简并基础单项式表达扌(sf, 对称简并单项式, /):
        '[缓存] => 对称简并单项式 -> may 对称简并基础单项式表达'
        . .
if __name__ == "__main__":
    raise NotImplementedError


__all__
from script.对称多项式讠基表达 import *
