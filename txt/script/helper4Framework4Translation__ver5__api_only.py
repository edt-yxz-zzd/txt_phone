#__all__:goto
r'''[[[
e script/helper4Framework4Translation__ver5__api_only.py

script.helper4Framework4Translation__ver5__api_only
py -m nn_ns.app.debug_cmd   script.helper4Framework4Translation__ver5__api_only -x # -off_defs
py -m nn_ns.app.doctest_cmd script.helper4Framework4Translation__ver5__api_only:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'script.helper4Framework4Translation__ver5__api_only:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
源起:
    view ../../python3_src/haskell_src/Framework4Translation__ver5__api_only.hs
目标:
    逐步投喂(vm_p_6w|tr_t5s_6w)
    求出目前所拥有的所有文件
    输出所有新增文件
    判断是否包含靶文件
    靶文件出现时，最后添加的文件是必须的，以此为根据 迭代输出 所有 最小需求文件集合{靶文件}

view ../../python3_src/seed/types/mapping/DynamicStackedMapping.py
from seed.types.mapping.DynamicStackedMapping import DynamicStackedMapping
]]
[[
copy from:
    view ../../python3_src/haskell_src/Framework4Translation__ver5__api_only.hs
==>>:
四基础虚拟封装:
  # 串联同文:[tr_t5s_6w == cat_Tr_ tr_t5x_6w tr_x5s_6w]
  # 串联虚拟:[vm_p_6w == cat_Vm_ vm_p_6x vm_x_6w] # [?不太基础?]
  # 虚设格式:[tr_t5s_6w == mock_Tr_ vm_x_6w tr_t5s_6x] #仅限于『程序文件』，其实 串联虚拟cat_Vm_ ~= flip mock_Tr_ 只要 虚设格式 放宽到所有程序而非限于翻译诀
  # 虚设虚拟:[vm_n_6w == mock_Vm_ tr_y5n_6w vm_y_6w]
    ===
    思考:这几个东西能生成啥样子的系统？
      e script/helper4Framework4Translation__ver5__api_only.py
    ===
    由来的理论支持:
        源代码的两种短程用途:
          + 被宿主机运行后功能等效
          + 被翻译后这两种用途递归功能等效
        归结为一:源代码的递归长程用途:
          + 被多次翻译后被宿主机运行后功能等效
    ===
    虽然相似，但不等同:[vm_n_6w =!= tr_w5n_6w]，也不存在谁替换谁
        不同之处在于:
        * vm_n_6w被翻译成vm_n_6m~?=tr_m5n_6m, 而tr_w5n_6w被翻译成tr_w5n_6m
          =>tr_w5n_6w不能用来替换vm_n_6w
        * tr_w5n_6w用作翻译器 可将dat_v_6n翻译成dat_v_6w，而vm_n_6w启动后只能运行程序并不能翻译文件
          =>vm_n_6w不能用来替换tr_w5n_6w
        相似之处在于:
        + tr_w5n_6w用作翻译器 可将tr_t5s_6n翻译成tr_t5s_6n，而vm_n_6w可以通过 虚设格式 伪作封装 得tr_t5s_6n
          tr_t5s_6n与dat_v_6n的区别在于tr_t5s_6n只强调『函数功能』而非『数据』，所以有『虚设格式』用于『程序文件』而不能用于『数据文件』
===
ls ../../python3_src/haskell_src/Framework4Translation-ver5-images/ -1
串联同文.png
串联虚拟.png
虚设格式.png
虚设虚拟.png
===
]]

'#'; __doc__ = r'#'
>>>



py_adhoc_call   script.helper4Framework4Translation__ver5__api_only   ,findout_level4target_  :vm_x_6y :vm_x_6y
('vm_x_6y', 0)

py_adhoc_call   script.helper4Framework4Translation__ver5__api_only   ,findout_level4target_  :vm_x_6z :vm_x_6y,vm_y_6z
('vm_x_6z', 1)


py_adhoc_call   script.helper4Framework4Translation__ver5__api_only   ,findout_level4target_  :tr_t5s_6w :vm_x_6w,tr_x5y_6x,tr_t5s_6y
('tr_t5s_6w', 3)

py_adhoc_call   script.helper4Framework4Translation__ver5__api_only   ,findout_level4target_  =None  :vm_x_6w,tr_x5y_6x,tr_t5s_6y
('vm_x_6w', 0)
('tr_x5y_6x', 0)
('tr_y5s_6t', 0)
('tr_w5y_6x', 1)
('vm_y_6w', 2)
('tr_w5s_6t', 3)

py_adhoc_call   script.helper4Framework4Translation__ver5__api_only   ,findout_level4target_  =None  :vm_x_6w,tr_x5y_6x,tr_y5z_6y,tr_t5s_6z
('vm_x_6w', 0)
('tr_x5y_6x', 0)
('tr_y5z_6y', 0)
('tr_z5s_6t', 0)
('tr_w5y_6x', 1)
('vm_y_6w', 2)
('tr_w5z_6y', 3)
('tr_w5z_6x', 4)
('vm_z_6w', 4)
('tr_w5s_6t', 5)



]]]'''#'''
__all__ = r'''
findout_level4target_
    Role
    Vm
    Tr

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import re
from enum import Enum, auto
from functools import cached_property
from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
from seed.algo.almost_graph.closure.IClosureLevelUp import IClosureLevelUp
#.
#.from abc import update_abstractmethods
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_

lazy_import4funcs_('seed.tiny_.types5py', 'mk_MapView,curry1,kwargs2Attrs', __name__)
if 0:from seed.tiny_.types5py import mk_MapView#curry1,kwargs2Attrs #,MapView

lazy_import4funcs_('seed.tiny_.containers', 'mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str', __name__)
if 0:from seed.tiny_.containers import mk_tuple__split_first_if_str#mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_ #xxx:null_tuple
lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
if 0:from seed.debug.print_err import print_err

from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#    def _check6make_(sf, /):

___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__
class Role(Enum):
    CatTr_in = auto()
    CatTr_out = auto()
    CatVm_low = auto()
    CatVm_high = auto()
    MockTr_tr = auto()
    MockTr_vm = auto()
    MockVm_tr = auto()
    MockVm_vm = auto()
    def __invert__(sf, /):
        return sf._opposite
    @property
    def opposition(sf, /):
        return sf._opposite
    @property
    def filetype(sf, /):
        '-> str'
        return sf._ft
    @property
    def contact_points(sf, /):
        '-> [Char]/str'
        return sf._cs
Role.CatTr_in._opposite = Role.CatTr_out
Role.CatTr_out._opposite = Role.CatTr_in
Role.CatVm_low._opposite = Role.CatVm_high
Role.CatVm_high._opposite = Role.CatVm_low
Role.MockTr_tr._opposite = Role.MockTr_vm
Role.MockTr_vm._opposite = Role.MockTr_tr
Role.MockVm_tr._opposite = Role.MockVm_vm
Role.MockVm_vm._opposite = Role.MockVm_tr
assert ~Role.MockVm_vm is Role.MockVm_tr

Role.CatTr_in._ft = 'tr'
Role.CatTr_out._ft = 'tr'
Role.CatVm_low._ft = 'vm'
Role.CatVm_high._ft = 'vm'
Role.MockTr_tr._ft = 'tr'
Role.MockTr_vm._ft = 'vm'
Role.MockVm_tr._ft = 'tr'
Role.MockVm_vm._ft = 'vm'
assert Role.MockVm_vm.filetype == 'vm'

Role.CatTr_in._cs = 'ht'
Role.CatTr_out._cs = 'hs'
Role.CatVm_low._cs = 'n'
Role.CatVm_high._cs = 'w'
Role.MockTr_tr._cs = 'h'
Role.MockTr_vm._cs = 'n'
Role.MockVm_tr._cs = 'ht'
Role.MockVm_vm._cs = 'wn'
assert Role.MockVm_vm.contact_points == 'wn'

_BaseVm = mk_named_pseudo_tuple_(__name__, '_BaseVm', 'w,n')
class Vm(_BaseVm):
    'vm_n_6w'
    filetype = 'vm'
    def _check6make_(sf, /):
        ...
    @cached_property
    def role2key(sf, /):
        return mk_MapView(dict(sf.iter_role_key_pairs_()))
    def iter_role_key_pairs_(sf, /):
        '-> Iter (role, key6role)'
        yield (Role.CatVm_low, sf.n)
        yield (Role.CatVm_high, sf.w)
        yield (Role.MockTr_vm, sf.n)
        yield (Role.MockVm_vm, (sf.w, sf.n))
        return
    def derive_(sf, ot, role4ot, /):
        'sf -> ot/(Tr|Vm) -> role{ot} -> res/(Tr|Vm)'
        assert ot.filetype == role4ot.filetype
        assert sf.role2key[~role4ot] == ot.role2key[role4ot]
        match role4ot:
            case Role.CatVm_low:
                if not sf.w == ot.n:raise ValueError
                return Vm(ot.w, sf.n)
            case Role.CatVm_high:
                if not sf.n == ot.w:raise ValueError
                return Vm(sf.w, ot.n)
            case Role.MockTr_tr:
                if not sf.n == ot.h:raise ValueError
                return Tr(sf.w, ot.s, ot.t)
            case Role.MockVm_tr:
                if not sf.w == ot.h:raise ValueError
                if not sf.n == ot.t:raise ValueError
                return Vm(sf.w, ot.s)
        raise ValueError(role4ot)
assert Vm('w', 'n') == Vm('w', 'n')
assert hash(Vm('w', 'n')) == hash(Vm('w', 'n'))

_BaseTr = mk_named_pseudo_tuple_(__name__, '_BaseTr', 'h,s,t')
class Tr(_BaseTr):
    'tr_t5s_6h'
    filetype = 'tr'
    def _check6make_(sf, /):
        ...
    @cached_property
    def role2key(sf, /):
        return mk_MapView(dict(sf.iter_role_key_pairs_()))
    def iter_role_key_pairs_(sf, /):
        '-> Iter (role, key6role)'
        yield (Role.CatTr_in, (sf.h, sf.t))
        yield (Role.CatTr_out, (sf.h, sf.s))
        yield (Role.MockTr_tr, sf.h)
        yield (Role.MockVm_tr, (sf.h, sf.t))
        return
    def derive_(sf, ot, role4ot, /):
        'sf -> ot/(Tr|Vm) -> role{ot} -> res/(Tr|Vm)'
        assert ot.filetype == role4ot.filetype
        assert sf.role2key[~role4ot] == ot.role2key[role4ot]
        match role4ot:
            case Role.CatTr_in:
                if not sf.h == ot.h:raise ValueError
                if not sf.s == ot.t:raise ValueError
                return Tr(sf.h, ot.s, sf.t)
            case Role.CatTr_out:
                if not sf.h == ot.h:raise ValueError
                if not sf.t == ot.s:raise ValueError
                return Tr(sf.h, sf.s, ot.t)
            case Role.MockTr_vm:
                if not sf.h == ot.n:raise ValueError
                return Tr(ot.w, sf.s, sf.t)
            case Role.MockVm_vm:
                if not sf.h == ot.w:raise ValueError
                if not sf.t == ot.n:raise ValueError
                return Vm(sf.h, sf.t)
        raise ValueError(role4ot)




_lang = r'(?:[a-z]+)'
_rex4nm = re.compile(fr'(?:tr_({_lang})5({_lang})_6({_lang})|vm_({_lang})_6({_lang}))')
def _inv_parse_nm(x, /):
    match x.filetype:
        case 'tr':
            return f'tr_{x.h}5{x.s}_6{x.t}'
        case 'vm':
            return f'vm_{x.n}_6{x.w}'
    raise TypeError(x)
def _parse_nm(nm, /):
    m = _rex4nm.fullmatch(nm)
    if m is None:
        raise ValueError(nm)
    if m.group(1):
        #bug:x = Tr(*m.group(1,2,3))
        x = Tr(*m.group(3,2,1))
    else:
        #bug:x = Vm(*m.group(4,5))
        x = Vm(*m.group(5,4))
    x
    return x
def _parse_nms(nms, /):
    return tuple(map(_parse_nm, (nms)))
    return set(map(_parse_nm, set(nms)))

class _ClosureLevelUp4vm_tr_ops(IClosureLevelUp):
    ___no_slots_ok___ = True
    @override
    def _iter_derive_child_vertices_when_new_vtx_induced_(sf, lvl, v, processed_vtc, /):
        'lvl/level{v}/uint -> v/vtx/vertex -> Iter vtx -> (Iter vtx){expect generate vertices of next level; but arbitrary vertices are ok}'
        #.for u in processed_vtc:
        for role, key in v.iter_role_key_pairs_():
            opposite_role = ~role
            for a in sf._iter_processed_vtc_meet_(opposite_role, key):
                b = a.derive_(v, role)
                yield b
    @override
    def on_vertex_added_(sf, lvl, v, /):
        'lvl/level{v}/uint -> v/vtx/vertex -> None'
        #if 0b0001:print_err(('added:', lvl, v))
        pass
    @override
    def on_vertex_processed_(sf, lvl, v, /):
        'lvl/level{v}/uint -> v/vtx/vertex -> None'
        #if 0b0001:print_err(('processed:', lvl, v))
        for role, key in v.iter_role_key_pairs_():
            #bug:sf._processed_role2key2vtc[role][key].append(v)
            sf._processed_role2key2vtc.setdefault(role, {}).setdefault(key, []).append(v)
    def _iter_processed_vtc_meet_(sf, role, key, /):
        #bug:vs = sf._processed_role2key2vtc[role][key]
        vs = sf._processed_role2key2vtc.get(role, {}).get(key, [])
        return islice(vs, 0, len(vs))

    def __init__(sf, src_vtc, /):
        sf._processed_role2key2vtc = {}
            # :: {role:{key:[vtx]}}
        super().__init__(src_vtc)
#end-class _ClosureLevelUp4vm_tr_ops(IClosureLevelUp):


def _closure_fill_with_height_(src_vtc, /):
    sf = _ClosureLevelUp4vm_tr_ops(src_vtc)
    (lvl2vtc, vtx2lvl) = sf.inflate_closure__via_progressively_levelup_()
    return (lvl2vtc, vtx2lvl)

def findout_level4target_(may_nms8targets, nms8sources, /):
    'may-Iter nm8target -> Iter nm8sources -> Iter (nm8target, level)'
    b_all_targets = may_nms8targets is None
    if not b_all_targets:
        nms8targets = may_nms8targets
        nms8targets = mk_tuple__split_first_if_str(nms8targets, ',')
        xs8targets = _parse_nms(nms8targets)

    nms8sources = mk_tuple__split_first_if_str(nms8sources, ',')
    xs8sources = _parse_nms(nms8sources)
    (lvl2vtc, vtx2lvl) = _closure_fill_with_height_(xs8sources)
    #if 0b0001:print_err(('lvl2vtc:', lvl2vtc))
    #if 0b0001:print_err(('vtx2lvl:', vtx2lvl))

    if not b_all_targets:
        for j, x8tgt in enumerate(xs8targets):
            lvl = vtx2lvl[x8tgt]
            nm8tgt = nms8targets[j]
            yield (nm8tgt, lvl)
    else:
        for lvl, xs in enumerate(lvl2vtc):
            for x in xs:
                nm8x = _inv_parse_nm(x)
                yield (nm8x, lvl)



__all__
#lazy_import4funcs_('script.helper4Framework4Translation__ver5__api_only', 'findout_level4target_', __name__)
from script.helper4Framework4Translation__ver5__api_only import findout_level4target_
from script.helper4Framework4Translation__ver5__api_only import Role, Vm, Tr
from script.helper4Framework4Translation__ver5__api_only import *
