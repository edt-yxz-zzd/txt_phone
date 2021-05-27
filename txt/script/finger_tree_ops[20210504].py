#HHHHH
the -> cls The... ISingleton

arg:iterator/seq/tree
reverse
L/R end
insert at?
replace
extend/join
times/mul
split at?
delete at?

cased_tuple/tuple/FrozenDict-record
    per element monoid_ops
    measure by index

grep '^def|^class|^\w+\s*=' __file__
grep '^[a-zA-Z_]' __file__
_debug.py forgots


buttom -> bottom
grep buttom -r . -l -i
./nn_ns/CJK/cjk_subsets/cjk_subsets__relationship.py
./nn_ns/CJK/cjk_subsets/cjk_subsets__relationship.py.out/cjk_rel_more.txt
./nn_ns/CJK/cjk_subsets/cjk_subsets__relationship.py.result.txt
./nn_ns/CJK/cjk_subsets/cjk_common_subset.py
./nn_ns/filedir/backup_tools/fsys_mapping_ex.py
./nn_ns/filedir/backup_tools/fsys_mapping_patch.py
./nn_ns/graph/biconnected_planar_d2d3.py
./nn_ns/math_nn/matrix_api.py


r'''
e script/finger_tree_ops.py
py script/finger_tree_ops.py
view others/数学/编程/tree/finger_tree.txt
finger_tree_ops
raw_finger_tree_ops



mk same name wrapper method:
^\(\s*def \)\(\w*\)\(.*\n.*\):_'$
%s//\1___\2___\3:\2'\r\1\2\3:___\2___'
    @abstractmethod
    def f(...):
        '... #see:_'
    ==>>
    @abstractmethod
    def ___f___(...):
        '... #see:f'
    def f(...):
        '... #see:___f___'

get abstractmethod decl
    each abstractmethod decl occupy 3 lines
    copy whole class body to file end
    exec below vim q/ search-cmd && q: edit-cmd, to remove non-abstractmethod func
^\(\s*@abstractmethod.*\)\n\(.*\)\n\(.*\)
.,$s//##?!\1\r##?!\2\r##?!\3
^\(##?!\)\@!.*\n
.,$s//
^\(##?!\)
.,$s//


forward call 4 wrapper class
    the undering obj/wrapped obj named '__ops'
    each abstractmethod decl has form regex'^\s*def .*/):$''
    each abstractmethod decl occupy 3 lines
    copy all abstractmethod decls to file end
    exec below vim q/ search-cmd && q: edit-cmd, to remove non-abstractmethod func
^\(\s*@abstractmethod.*\)\n\(\s*def \s*\)\([a-zA-Z]\w*\)[(]\(\w\+\)\(, \)\?\(.*\), [/][)]:\n\(\s*\)\(\S.*\)
.,$s//\1\r\2\3(\4\5\6, \/):\r\7\8\r\7return \4.__ops.\3(\6)
^\(\s*@abstractmethod.*\)\n\(\s*def \s*\)\(__\w*__\)[(]\(\w\+\)\(.*\), [/][)]:\n\(\s*\)\(\S.*\)
.,$s//\1\r\2\3(\4\5, \/):\r\6\7\r\6return type(\4.__ops).\3(\4.__ops\5)
@abstractmethod$
.,$s//@override

ReversedFingerTreeOps


TODO:
DONE:
    xnodes -> xnode_seq
    nodes -> node_seq
    elements -> element_seq
DONE:
    careless_check_ input
    careless_check_ output
        mk_node
        unbox_node
        get_auto_info_from_node
        get_num_child_xnode_seq_of_node
        calc_auto_info_from_xnode_seq





finger_tree_ops__setting__2c3__1T4
finger_tree_ops__setting__3c4__3T7
finger_tree_ops__setting__2c5__2T7
finger_tree_ops__setting__3c5__4T9
finger_tree_ops__setting__3c4c5__2T7
finger_tree_ops__setting__4c5c6c7__2T9
finger_tree_ops__setting__4c5c6c7__2T10


the_monoid_ops4size
the_monoid_ops4max__imay
the_monoid_ops4max__uint
the_monoid_ops4max__tmay


def check_finger_tree_ops__setting(finger_tree_ops__setting:IFingerTreeOps__setting, /):
def tuple_reversed(seq, /):
def _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops, /):
def mk_ReversedFingerTreeOps(finger_tree_ops, /):
def mk_ReversedMeasurableOps(measurable_ops, /):
def mk_ReversedMonoidOps(monoid_ops, /):
def mk_ReversedAssocBinaryOps(assoc_bin_ops, /):
def mk_NamedTuple4FingerTreeOps__setting(nens, min_max_den_pair, overflow_nen, may_ordered_nens, /):
def mk_FingerTreeOps__setting(nens, min_max_den_pair, overflow_nen, may_ordered_nens, /):
def _mk_FingerTreeOps__setting(nens, min_max_den_pair, /):
def check_cased_tuple__with_depth(case_name, sz, depth, obj, /):

class IAssocBinaryOps(ABC):
class IAssocBinaryOps__commutable(IAssocBinaryOps):
class IMonoidOps(IAssocBinaryOps):
class IMonoidOps__commutable(IMonoidOps, IAssocBinaryOps__commutable):
class IMeasurableOps(IMonoidOps):
class IFingerTreeOps__setting(ABC):
class IFingerTreeOps(IFingerTreeOps__setting):
class ReversedAssocBinaryOps(IAssocBinaryOps):
class ReversedMonoidOps(ReversedAssocBinaryOps, IMonoidOps):
class ReversedMeasurableOps(ReversedMonoidOps, IMeasurableOps):
class WrappedFingerTreeOps__setting(IFingerTreeOps__setting):
class IFingerTreeOps__wrapped_setting(WrappedFingerTreeOps__setting, IFingerTreeOps):
    pass
class WrappedFingerTreeOps(IFingerTreeOps__wrapped_setting):
class ReversedFingerTreeOps(WrappedFingerTreeOps):
class abstractmethod_decls_of_IFingerTreeOps(IFingerTreeOps):
NamedTuple4FingerTreeOps__setting = namedtuple(...)
class FingerTreeOps__setting(IFingerTreeOps__setting):
class IFingerTreeOps__raw_mk_element(IFingerTreeOps):
class IFingerTreeOps__cased_data(IFingerTreeOps__raw_mk_element):
class FingerTreeOps__funcs(IFingerTreeOps__cased_data, IFingerTreeOps__wrapped_setting):
class MonoidOps4size(IMonoidOps__commutable, ISingleton):
class IMonoidOps4max(IMonoidOps__commutable):
class MonoidOps4max__imay(IMonoidOps4max, ISingleton):
class MonoidOps4max__uint(IMonoidOps4max, ISingleton):
class MonoidOps4max__tmay_pyobj(IMonoidOps4max, ISingleton):
class MonoidOps4max__funcs(IMonoidOps4max):

#'''

#HHHHH
from seed.helper.check.checkers import check_mapping, check_int, check_uint, check_strict_sorted, check_int_ge1, check_int_ge2, check_all, check_tuple, check_pair, check_instance, check_uint_imay, check_type_is, check_seq, check_len_of, check_str, check_union_of_cased_tuples, check_cased_tuple, check_callable, check_tmay, check_is_None, check_result_of_cmp, check_result_of_partial_cmp

from seed.types.FrozenDict import FrozenDict, mk_FrozenDict
#from seed.math.floor_ceil import offsetted_divmod
from seed.math.cut_uint_into_uints import Helper4cut_uint_into_uints, calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints
from seed.for_libs.for_functools.reduce import reduce_with_tmay
from seed.abc.abc import override
from seed.abc.ISingleton import ISingleton
from seed.tiny import echo

from abc import ABC, abstractmethod
import itertools
from collections import namedtuple
import operator


check_mapping
check_int
check_uint
check_strict_sorted
check_int_ge1
check_int_ge2
check_all
check_tuple
check_pair
check_instance

#HHHHH
class IOps4OneMainObjType(ABC):
    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    #def careless_check_io_arg_of_assoc_bin_op(sf, x, /):
    def careless_check_main_obj(sf, x, /):
        'a -> (None|raise) #see:___careless_check_main_obj___'
        r = type(sf).___careless_check_main_obj___(sf, x)
        check_is_None(r)
        return None
    def careless_check_main_objs(sf, /, *xs, /):
        '*a -> (None|raise) #see:careless_check_main_obj'
        for _ in map(sf.careless_check_main_obj, xs):pass

class IEqOps(IOps4OneMainObjType):
    r'''

    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    @abstractmethod
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
    #'''
    @abstractmethod
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
    def eq(sf, lhs, rhs, /):
        '-> bool #see:___eq___'
        sf.careless_check_main_objs(lhs, rhs)
        b = type(sf).___eq___(sf, lhs, rhs)
        check_bool(b)
        _check_eq__when_is(b, lhs, rhs)
        return b

    def ne(sf, lhs, rhs, /):
        '-> bool #see:eq'
        return not sf.eq(lhs, rhs)

class ResultOfCMP:
    LT = -1
    EQ = 0
    GT = +1
    check = check_result_of_cmp
class ResultOfPartialCMP(ResultOfCMP):
    NA = -2
    check = check_result_of_partial_cmp
def cmp__int(lhs, rhs, /):
    return cmp__default(lhs, rhs)
def cmp__by_lt(lt, lhs, rhs, /):
    if lt(lhs, rhs):
        return ResultOfCMP.LT
    elif lt(rhs, lhs):
        return ResultOfCMP.GT
    else:
        return ResultOfCMP.EQ
def cmp__by_eq_lt(eq, lt, lhs, rhs, /):
    if eq(lhs, rhs):
        return ResultOfCMP.EQ
    elif lt(lhs, rhs):
        return ResultOfCMP.LT
    else:
        return ResultOfCMP.GT
def cmp__default__lt_eq_gt(lhs, rhs, /):
    if lhs < rhs:
        return ResultOfCMP.LT
    elif lhs == rhs:
        return ResultOfCMP.EQ
    else:
        return ResultOfCMP.GT
def cmp__default__lt_gt_eq(lhs, rhs, /):
    if lhs < rhs:
        return ResultOfCMP.LT
    elif lhs > rhs:
        return ResultOfCMP.GT
    else:
        return ResultOfCMP.EQ
def cmp__default__eq_lt_gt(lhs, rhs, /):
    if lhs == rhs:
        return ResultOfCMP.EQ
    elif lhs < rhs:
        return ResultOfCMP.LT
    else:
        return ResultOfCMP.GT
cmp__default = cmp__default__eq_lt_gt
    #better than cmp__default__lt_eq_gt #since eq stop faster and may used in loop
cmp__default__by_eq_lt = cmp__default__eq_lt_gt
cmp__default__by_lt = cmp__default__lt_gt_eq


def _check_eq__when_is(result, lhs, rhs, /):
    if lhs is rhs:
        if not result is True: raise ValueError
def _check_partial_le__when_is(result, lhs, rhs, /):
    if lhs is rhs:
        if not result is True: raise ValueError
def _check_partial_lt__when_is(result, lhs, rhs, /):
    if lhs is rhs:
        if not result is False: raise ValueError
def _check_partial_cmp__when_is(result, lhs, rhs, /):
    if lhs is rhs:
        if not result == ResultOfPartialCMP.EQ: raise ValueError
_check_lt__when_is = _check_partial_lt__when_is
_check_cmp__when_is = _check_partial_cmp__when_is

class IPartialOrderingOps(IEqOps):
    r'''
    ResultOfPartialCMP/check_result_of_partial_cmp: -2=N/A; -1=LT; 0=EQ; +1=GT

    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    @abstractmethod
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
    @abstractmethod
    def ___partial_le___(sf, lhs, rhs, /):
        '-> bool #see:partial_le'
    @abstractmethod
    def ___partial_lt___(sf, lhs, rhs, /):
        '-> bool #see:partial_lt'
    @abstractmethod
    def ___partial_cmp___(sf, lhs, rhs, /):
        '-> [-2..+1] #see:partial_cmp'
    #'''
    @abstractmethod
    def ___partial_le___(sf, lhs, rhs, /):
        '-> bool #see:partial_le'
    def partial_le(sf, lhs, rhs, /):
        '-> bool #see:___partial_le___'
        sf.careless_check_main_objs(lhs, rhs)
        b = type(sf).___partial_le___(sf, lhs, rhs)
        check_bool(b)
        _check_partial_le__when_is(b, lhs, rhs)
        return b

    @abstractmethod
    def ___partial_lt___(sf, lhs, rhs, /):
        '-> bool #see:partial_lt'
    def partial_lt(sf, lhs, rhs, /):
        '-> bool #see:___partial_lt___'
        sf.careless_check_main_objs(lhs, rhs)
        b = type(sf).___partial_lt___(sf, lhs, rhs)
        check_bool(b)
        _check_partial_lt__when_is(b, lhs, rhs)
        return b

    @abstractmethod
    def ___partial_cmp___(sf, lhs, rhs, /):
        '-> [-2..+1] #see:partial_cmp'
    def partial_cmp(sf, lhs, rhs, /):
        '-> [-2..+1] #see:___partial_cmp___'
        sf.careless_check_main_objs(lhs, rhs)
        r = type(sf).___partial_cmp___(sf, lhs, rhs)
        check_result_of_partial_cmp(r)
        _check_partial_cmp__when_is(r, lhs, rhs)
        return r
#end of class IPartialOrderingOps(IEqOps):
class IPartialOrderingOps__with_max_TOP(IPartialOrderingOps):
    @abstractmethod
    def ___get_max_TOP___(sf, /):
        '-> (TOP::main_obj) #the max main_obj #[any main_obj <= TOP] #see:get_max_TOP'
    def get_max_TOP(sf, /):
        '-> (TOP::main_obj) #the max main_obj #[any main_obj <= TOP] #see:___get_max_TOP___'
        TOP = type(sf).___get_max_TOP___(sf)
        sf.careless_check_main_obj(TOP)
        return TOP
#end of class IPartialOrderingOps__with_max_TOP(IPartialOrderingOps):
class IPartialOrderingOps__with_min_BOTTOM(IPartialOrderingOps):
    @abstractmethod
    def ___get_min_BOTTOM___(sf, /):
        '-> (BOTTOM::main_obj) #the min main_obj #[BOTTOM <= any main_obj] #see:get_min_BOTTOM'
    def get_min_BOTTOM(sf, /):
        '-> (BOTTOM::main_obj) #the min main_obj #[BOTTOM <= any main_obj] #see:get_min_BOTTOM'
        BOTTOM = type(sf).___get_min_BOTTOM___(sf)
        sf.careless_check_main_obj(BOTTOM)
        return BOTTOM
#end of class IPartialOrderingOps__with_min_BOTTOM(IPartialOrderingOps):



#begin of class_ITotalOrderingOps(IPartialOrderingOps):
class ITotalOrderingOps(IPartialOrderingOps):
    #class IComparableOps(IOps4OneMainObjType):
    #begin of __doc__ITotalOrderingOps:ITotalOrderingOps.__doc__
    r'''
    ResultOfCMP/check_result_of_cmp: -1=LT; 0=EQ; +1=GT

    not default impl eq by cmp:
        <<== see eq__seq impl
        shortcut when len diff!!!
        ITotalOrderingOps__cmp2eq
        ITotalOrderingOps__cmp2eq_lt
    default impl lt by cmp:
        <<== see lt__seq impl
            call cmp__seq inside
        ITotalOrderingOps__cmp2lt
            # almost use ITotalOrderingOps__cmp2lt instead of ITotalOrderingOps
    impl cmp by detect eq first:
        why ???use cmp__default__eq_lt_gt instead of cmp__default__lt_eq_gt???
        <<== see cmp__seq/cmp__int impl
            detect element eq inside loop
            detect element lt outside loop
        i.e. cmp__default__by_eq_lt = use cmp__default__eq_lt_gt instead of cmp__default__lt_eq_gt

    #####################################
    #####################################
    #####################################
    #####################################
    #####################################
    why ???no ITotalOrderingOps__lt2cmp/ITotalOrderingOps__lt2eq???
        see:
            ITotalOrderingOps__lt2eq_cmp
            ITotalOrderingOps__eq_lt2cmp
        ##################
        no ITotalOrderingOps__lt2cmp
            if impl cmp by lt:
                if use cmp__default__eq_lt_gt/cmp__default__lt_eq_gt:
                    ==>> must have eq
                    ==>> ITotalOrderingOps__eq_lt2cmp
                if use cmp__default__lt_gt_eq:
                    ==>> impl eq by lt
                    ==>> ITotalOrderingOps__lt2eq_cmp
        ##################
        no ITotalOrderingOps__lt2eq
            if impl eq by lt:
                ==>> use cmp__default__lt_gt_eq
                ==>> impl cmp by lt
                ==>> ITotalOrderingOps__lt2eq_cmp


########################################
########################################
########################################
class ITotalOrderingOps(IPartialOrderingOps):
class ITotalOrderingOps__seq(ITotalOrderingOps):
class ITotalOrderingOps__default_total_ordering(ITotalOrderingOps):
class ITotalOrderingOps__cmp2eq(ITotalOrderingOps):
class ITotalOrderingOps__cmp2lt(ITotalOrderingOps):
class ITotalOrderingOps__cmp2eq_lt(ITotalOrderingOps__cmp2lt, ITotalOrderingOps__cmp2eq):pass
class ITotalOrderingOps__eq_lt2cmp(ITotalOrderingOps):
class ITotalOrderingOps__lt2eq_cmp(ITotalOrderingOps__cmp2eq):

########################################
########################################
########################################

    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    @abstractmethod
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
    @abstractmethod
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
    @abstractmethod
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'

    #'''
    #end of __doc__ITotalOrderingOps


    @abstractmethod
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
    def lt(sf, lhs, rhs, /):
        '-> bool #see:___lt___'
        sf.careless_check_main_objs(lhs, rhs)
        b = type(sf).___lt___(sf, lhs, rhs)
        check_bool(b)
        _check_lt__when_is(b, lhs, rhs)
        return b

    @abstractmethod
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
    def cmp(sf, lhs, rhs, /):
        '-> [-1..+1] #see:___cmp___'
        sf.careless_check_main_objs(lhs, rhs)
        r = type(sf).___cmp___(sf, lhs, rhs)
        check_result_of_cmp(r)
        _check_cmp__when_is(r, lhs, rhs)
        return r


    @override
    def ___partial_le___(sf, lhs, rhs, /):
        '-> bool #see:partial_le'
        return not type(sf).___lt___(sf, rhs, lhs)
    @override
    def ___partial_lt___(sf, lhs, rhs, /):
        '-> bool #see:partial_lt'
        return type(sf).___lt___(sf, lhs, rhs)
    @override
    def ___partial_cmp___(sf, lhs, rhs, /):
        '-> [-2..+1] #see:partial_cmp'
        return type(sf).___cmp___(sf, lhs, rhs)

    def le(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return not sf.lt(rhs, lhs)
    def gt(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return sf.lt(rhs, lhs)
    def ge(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return not sf.lt(lhs, rhs)

    def max(sf, lhs, rhs, /):
        return rhs if sf.lt(lhs, rhs) else lhs
    def min(sf, lhs, rhs, /):
        return rhs if sf.lt(rhs, lhs) else lhs
    def max1s(sf, lhs, rhss, /):
        'a -> Iter a -> a'
        op = sf.max
        #functools.reduce
        return reduce_with_tmay(op, [lhs], rhss)
    def min1s(sf, lhs, rhss, /):
        'a -> Iter a -> a'
        op = sf.min
        #functools.reduce
        return reduce_with_tmay(op, [lhs], rhss)

#end of class ITotalOrderingOps(IPartialOrderingOps):
#end of class_ITotalOrderingOps(IPartialOrderingOps):
class ITotalOrderingOps__with_max_TOP(ITotalOrderingOps, IPartialOrderingOps__with_max_TOP):pass
class ITotalOrderingOps__with_min_BOTTOM(ITotalOrderingOps, IPartialOrderingOps__with_min_BOTTOM):pass
class ITotalOrderingOps__with_min_BOTTOM_max_TOP(ITotalOrderingOps__with_min_BOTTOM, ITotalOrderingOps__with_max_TOP):pass


def eq__seq(element_eq, lhs, rhs, /):
    return eq__sized_ordered_iterable(element_eq, lhs, rhs)
def eq__sized_ordered_iterable(element_eq, lhs, rhs, /):
    if len(lhs) != len(rhs): return False
    if 0:
        return eq__ordered_iterable(element_eq, lhs, rhs)
    else:
        for x, y in zip(lhs, rhs):
            if not element_eq(x, y): return False
        return True
def eq__ordered_iterable(element_eq, lhs, rhs, /):
    def element_partial_cmp(x, y, /):
        if element_eq(x, y):
            return ResultOfPartialCMP EQ
        else:
            return ResultOfPartialCMP NA
    r = partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs)
    return r == ResultOfCMP.EQ

def cmp__seq(element_cmp, lhs, rhs, /):
    return partial_cmp__seq(element_cmp, lhs, rhs)
def cmp__sized_ordered_iterable(element_cmp, lhs, rhs, /):
    return partial_cmp__sized_ordered_iterable(element_cmp, lhs, rhs)
def cmp__ordered_iterable(element_cmp, lhs, rhs, /):
    return partial_cmp__ordered_iterable(element_cmp, lhs, rhs)
def lt__seq(element_cmp, lhs, rhs, /):
    return partial_lt__seq(element_cmp, lhs, rhs)
def lt__sized_ordered_iterable(element_cmp, lhs, rhs, /):
    return partial_lt__sized_ordered_iterable(element_cmp, lhs, rhs)
def lt__ordered_iterable(element_cmp, lhs, rhs, /):
    return partial_lt__ordered_iterable(element_cmp, lhs, rhs)


def partial_le__seq(element_partial_cmp, lhs, rhs, /):
    return partial_le__sized_ordered_iterable(element_partial_cmp, lhs, rhs)
def partial_le__sized_ordered_iterable(element_partial_cmp, lhs, rhs, /):
    if not rhs: return not lhs
    if not lhs: return True

    if 1:
        return partial_le__ordered_iterable(element_partial_cmp, lhs, rhs)
    else:
        lsz, rsz = len(lhs), len(rhs)
        for x, y in zip(lhs, rhs):
            r = element_partial_cmp(x, y)
            if r != ResultOfCMP.EQ:
                return r == ResultOfCMP.LT
        return lsz <= rsz
        #bug: may be iterator: return len(lhs) <= len(rhs)
def partial_le__ordered_iterable(element_partial_cmp, lhs, rhs, /):
    r = partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs)
    return r == ResultOfCMP.LT or r == ResultOfCMP.EQ




def partial_lt__seq(element_partial_cmp, lhs, rhs, /):
    return partial_lt__sized_ordered_iterable(element_partial_cmp, lhs, rhs)
def partial_lt__sized_ordered_iterable(element_partial_cmp, lhs, rhs, /):
    if not rhs: return False
    if not lhs: return True

    if 1:
        return partial_lt__ordered_iterable(element_partial_cmp, lhs, rhs)
    else:
        lsz, rsz = len(lhs), len(rhs)
        for x, y in zip(lhs, rhs):
            r = element_partial_cmp(x, y)
            if r != ResultOfCMP.EQ:
                return r == ResultOfCMP.LT
        return lsz < rsz
        #bug: may be iterator: return len(lhs) < len(rhs)
def partial_lt__ordered_iterable(element_partial_cmp, lhs, rhs, /):
    r = partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs)
    return r == ResultOfCMP.LT


def partial_cmp__seq(element_partial_cmp, lhs, rhs, /):
    return partial_cmp__sized_ordered_iterable(element_partial_cmp, lhs, rhs)
def partial_cmp__sized_ordered_iterable(element_partial_cmp, lhs, rhs, /):
    if not rhs:
        if not lhs:
            return ResultOfCMP.EQ
        else:
            return ResultOfCMP.GT
    else:
        if not lhs:
            return ResultOfCMP.LT
        else:
            pass

    if 1:
        return cmp__ordered_iterable(element_partial_cmp, lhs, rhs)
    else:
        for x, y in zip(lhs, rhs):
            r = element_partial_cmp(x, y)
            if r != ResultOfCMP.EQ:
                return r
        return cmp__int(len(lhs), len(rhs))

def partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs, /):
    lhs = iter(lhs)
    rhs = iter(rhs)
    #for x, y in zip(lhs, rhs):
    Nothing = []
    while 1:
        x = next(lhs, Nothing)
        y = next(rhs, Nothing)
        if x is Nothing:
            if y is Nothing:
                #[], []
                return ResultOfCMP.EQ
            else:
                #[], [y]
                return ResultOfCMP.LT
        else:
            if y is Nothing:
                #[x], []
                return ResultOfCMP.GT
            else:
                #[x], [y]
                pass

        r = element_partial_cmp(x, y)
        if r != ResultOfCMP.EQ:
            return r
    raise logic-err
    #return cmp__int(len(lhs), len(rhs))
#end of def partial_cmp__ordered_iterable(element_partial_cmp, lhs, rhs, /):






class ITotalOrderingOps__seq(ITotalOrderingOps):
    @abstractmethod
    def ___get_seq_element_total_ordering_ops___(sf, /):
        '-> (element_total_ordering_ops::ITotalOrderingOps<element in seq>) #see:get_seq_element_total_ordering_ops'
    def get_seq_element_total_ordering_ops(sf, /):
        '-> (element_total_ordering_ops::ITotalOrderingOps<element in seq>) #see:___get_seq_element_total_ordering_ops___'
        element_total_ordering_ops = type(sf).___get_seq_element_total_ordering_ops___(sf)
        check_instance(ITotalOrderingOps, element_total_ordering_ops)
        return element_total_ordering_ops

    @override
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
        if len(lhs) != len(rhs): return False
        ops = sf.get_seq_element_total_ordering_ops()
        element_eq = ops.eq
        return eq__seq(element_eq, lhs, rhs)

    @override
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
        ops = sf.get_seq_element_total_ordering_ops()
        element_cmp = ops.cmp
        return lt__seq(element_cmp, lhs, rhs)

    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-2..+1] #see:cmp'
        ops = sf.get_seq_element_total_ordering_ops()
        element_cmp = ops.cmp
        return cmp__seq(element_cmp, lhs, rhs)
#end of class ITotalOrderingOps__seq(ITotalOrderingOps):



class ITotalOrderingOps__default_total_ordering(ITotalOrderingOps):
    @override
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
        return lhs == rhs
    @override
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return lhs < rhs
    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
        return cmp__default(lhs, rhs)
        return cmp__default__eq_lt_gt(lhs, rhs)
#end of class ITotalOrderingOps__default_total_ordering(ITotalOrderingOps):
class TheTotalOrderingOps__default_total_ordering(ITotalOrderingOps__default_total_ordering, ISingleton):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        pass
the_default_py_obj_total_ordering_ops = TheTotalOrderingOps__default_total_ordering()
assert the_default_py_obj_total_ordering_ops is TheTotalOrderingOps__default_total_ordering()

class ITotalOrderingOps__cmp2eq(ITotalOrderingOps):
    @override
    def ___eq___(sf, lhs, rhs, /):
        '-> bool #see:eq'
        return sf.cmp(lhs, rhs) == ResultOfCMP.EQ
#end of class ITotalOrderingOps__cmp2eq(ITotalOrderingOps):
class ITotalOrderingOps__cmp2lt(ITotalOrderingOps):
    @override
    def ___lt___(sf, lhs, rhs, /):
        '-> bool #see:lt'
        return sf.cmp(lhs, rhs) == ResultOfCMP.LT
#end of class ITotalOrderingOps__cmp2lt(ITotalOrderingOps):
class ITotalOrderingOps__cmp2eq_lt(ITotalOrderingOps__cmp2lt, ITotalOrderingOps__cmp2eq):pass
#end of class ITotalOrderingOps__cmp2eq_lt(ITotalOrderingOps__cmp2lt, ITotalOrderingOps__cmp2eq):pass
class ITotalOrderingOps__eq_lt2cmp(ITotalOrderingOps):
    r'''
    why ???no ITotalOrderingOps__lt2cmp/ITotalOrderingOps__lt2eq???
        see: ITotalOrderingOps.__doc__
        #__doc__ITotalOrderingOps
    why ???use cmp__default__eq_lt_gt instead of cmp__default__lt_eq_gt???
        see: ITotalOrderingOps.__doc__
        #__doc__ITotalOrderingOps
    #'''
    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
        return cmp__by_eq_lt(sf.eq, sf.lt, lhs, rhs)
#end of class ITotalOrderingOps__eq_lt2cmp(ITotalOrderingOps):
class ITotalOrderingOps__lt2eq_cmp(ITotalOrderingOps__cmp2eq):
    r'''
    why ???no ITotalOrderingOps__lt2cmp/ITotalOrderingOps__lt2eq???
        see: ITotalOrderingOps.__doc__
        #__doc__ITotalOrderingOps
    #'''
    @override
    def ___cmp___(sf, lhs, rhs, /):
        '-> [-1..+1] #see:cmp'
        return cmp__by_lt(sf.lt, lhs, rhs)
#end of class ITotalOrderingOps__lt2eq_cmp(ITotalOrderingOps__cmp2eq):










class Mixin__Ops4OneMainObjType__int(IOps4OneMainObjType):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_int(x)
class Mixin__Ops4OneMainObjType__imay(Mixin__Ops4OneMainObjType__int):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_uint_imay(x)
class Mixin__Ops4OneMainObjType__uint(Mixin__Ops4OneMainObjType__imay):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_uint(x)
class Mixin__Ops4OneMainObjType__tmay_pyobj(IOps4OneMainObjType):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_tmay(x)

class ITotalOrderingOps__default_total_ordering__with_max_TOP(ITotalOrderingOps__default_total_ordering, ITotalOrderingOps__with_max_TOP):
class ITotalOrderingOps__default_total_ordering__with_min_BOTTOM(ITotalOrderingOps__default_total_ordering, ITotalOrderingOps__with_min_BOTTOM):
class ITotalOrderingOps__default_total_ordering__with_min_BOTTOM_max_TOP(ITotalOrderingOps__default_total_ordering, ITotalOrderingOps__with_min_BOTTOM_max_TOP):

class TotalOrderingOps__int(Mixin__Ops4OneMainObjType__int, ITotalOrderingOps__default_total_ordering):
class TotalOrderingOps__uint(Mixin__Ops4OneMainObjType__uint, ITotalOrderingOps__default_total_ordering__with_min_BOTTOM):
class TotalOrderingOps__imay(Mixin__Ops4OneMainObjType__imay, ITotalOrderingOps__default_total_ordering__with_min_BOTTOM):


class TheTotalOrderingOps__int(TotalOrderingOps__int, ISingleton):
class TheTotalOrderingOps__uint(TotalOrderingOps__uint, ISingleton):
class TheTotalOrderingOps__imay(TotalOrderingOps__imay, ISingleton):










class IAssocBinaryOps(IOps4OneMainObjType):
    r'''
    associative law
    law of association
    #'''
    @abstractmethod
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
    def is_assoc_bin_op_commutable(sf, /):
        '-> (commutable::bool) #see:___is_assoc_bin_op_commutable___'
        b = type(sf).___is_assoc_bin_op_commutable___(sf)
        check_bool(b)
        return b

    @abstractmethod
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:assoc_bin_op'
    def assoc_bin_op(sf, lhs, rhs, /,*, flip:bool=False):
        'a -> a -> a # (a*b)*c === a*(b*c) #see:___assoc_bin_op___'
        sf.careless_check_main_objs(lhs, rhs)
        if flip:
            lhs, rhs = rhs, lhs
        result = type(sf).___assoc_bin_op___(sf, lhs, rhs)
        sf.careless_check_main_obj(result)
        return result
    def assoc_op1s(sf, lhs, rhss, /,*, flip:bool=False):
        'a -> Iter a -> a'
        op = sf.assoc_bin_op
        #functools.reduce
        return reduce_with_tmay(op, [lhs], rhss, flip=flip)
class IAssocBinaryOps__commutable(IAssocBinaryOps):
    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return True
class IMonoidOps(IAssocBinaryOps):
    r'''
    Monoid
    semigroup

    @abstractmethod
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
    @abstractmethod
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
    @abstractmethod
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c)'
    @abstractmethod
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
    #'''

    @abstractmethod
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
    def get_monoid_identity(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:___get_monoid_identity___'
        monoid_identity = type(sf).___get_monoid_identity___(sf)
        sf.careless_check_main_obj(monoid_identity)
        return monoid_identity

    def assoc_op0s(sf, rhss, /,*, flip:bool=False):
        'Iter a -> a'
        init = sf.get_monoid_identity()
        return sf.assoc_op1s(init, rhss)
    def assoc_op01s__tmay(sf, tmay_lhs, rhss, /,*, flip:bool=False):
        if tmay_lhs:
            [lhs] = tmay_lhs
            return sf.assoc_op1s(lhs, rhss)
        else:
            return sf.assoc_op0s(rhss)
class IMonoidOps__commutable(IMonoidOps, IAssocBinaryOps__commutable):
    pass

class IMeasurableOps(IMonoidOps):
    'IMeasurableOps<measurable_monoid_obj, measured_result_monoid_obj>'
    @abstractmethod
    def ___get_monoid_ops4measured_result___(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:get_monoid_ops4measured_result'
    def get_monoid_ops4measured_result(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:___get_monoid_ops4measured_result___'
        monoid_ops4measured_result = type(sf).___get_monoid_ops4measured_result___(sf)
        check_instance(IMonoidOps, monoid_ops4measured_result)
        if measurable_ops.is_assoc_bin_op_commutable() and not monoid_ops4measured_result.is_assoc_bin_op_commutable():raise ValueError
        return monoid_ops4measured_result

    @abstractmethod
    def ___measure___(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:measure'
    def measure(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:___measure___'
        measured_result = type(measurable_ops).___measure___(measurable_ops, measurable_obj)
        monoid_ops4measured_result = measurable_ops.get_monoid_ops4measured_result()
        monoid_ops4measured_result.careless_check_main_obj(measured_result)
        return measured_result



class IMeasurableOps__commutable(IMeasurableOps, IMonoidOps__commutable):
    @override
    def get_monoid_ops4measured_result(measurable_ops, /):
        '-> commutable monoid_ops<measured_result>::IMonoidOps #see:___get_monoid_ops4measured_result___'
        monoid_ops4measured_result = super().get_monoid_ops4measured_result()
        commutable_monoid_ops4measured_result = monoid_ops4measured_result
        if not commutable_monoid_ops4measured_result.is_assoc_bin_op_commutable(): raise ValueError
        return commutable_monoid_ops4measured_result
    def get_commutable_monoid_ops4measured_result(measurable_ops, /):
        '-> commutable monoid_ops<measured_result>::IMonoidOps #see:___get_monoid_ops4measured_result___'
        commutable_monoid_ops4measured_result = sf.get_monoid_ops4measured_result()
        return commutable_monoid_ops4measured_result

















#HHHHH
class IFingerTreeOps__setting(ABC):
    r'''
    nd=nen <- nens = node_element_numbers
    dg=den <- dens = digit_element_numbers
    m = min digit_element_numbers
    M = max digit_element_numbers

    ====outdated, see IFingerTreeOps.__doc__ instead
    Node e
        = Node {element_seq::tuple<e>{len<-nens}, auto_info}
    Digit e
        = Digit {element_seq::tuple<e>{len<-dens}, auto_info}

    FingerTree depth e
        = Line {xnode_seq::tuple<e>{len<-[0..2*m-1]}, auto_info}
        | Deep {ldigit::Digit e, mtree::FingerTree (depth+1) (Node e), rdigit::Digit e, auto_info}
    #'''
    @abstractmethod
    def get_sorted_node_element_numbers(sf, /):
        '-> sorted tuple<uint>'
    @abstractmethod
    def get_node_element_number_frozenset(sf, /):
        '-> frozenset<uint>'
    @abstractmethod
    def get_min_max_digit_element_number_pair(sf, /):
        '-> (min digit_element_numbers::uint, max digit_element_numbers::uint)'


    @abstractmethod
    def ___split_size__case_digit_seq_digit___(sf, sz, /):
        '[2*min digit_element_numbers..] -> {nen:uint} #see:split_size__case_digit_seq_digit'
    def split_size__case_digit_seq_digit(sf, sz, /):
        '[2*min digit_element_numbers..] -> {nen:uint} #see:join__tqt/xnode_seq2node_seq__dqd/___split_size__case_digit_seq_digit___'
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        check_int(sz, min=2*min_den)
        nen2count = type(sf).___split_size__case_digit_seq_digit___(sf, sz)
        _ops_check_result_of_split_size__case_digit_seq_digit(sf, sz, nen2count)
        return mk_FrozenDict(nen2count)
    @abstractmethod
    def ___split_size__case_digit_seq___(sf, sz, /):
        '[min digit_element_numbers..] -> (den, {nen:uint}) #see:split_size__case_digit_seq'
    def split_size__case_digit_seq(sf, sz, /):
        '[min digit_element_numbers..] -> (den, {nen:uint}) #see: join__qt/mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size/xnode_seq2ldigit_node_seq__qd/___split_size__case_digit_seq___'
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        check_int(sz, min=1*min_den)
        den, nen2count = type(sf).___split_size__case_digit_seq___(sf, sz)
        _ops_check_result_of_split_size__case_digit_seq(sf, sz, den, nen2count)
        return (den, mk_FrozenDict(nen2count))
    @abstractmethod
    def ___split_size__case_seq___(sf, sz, /):
        '[2*min digit_element_numbers..] -> (a::den, b::den, {nen:uint}){a<=b} #see:split_size__case_seq'
    def split_size__case_seq(sf, sz, /):
        '[2*min digit_element_numbers..] -> (a::den, b::den, {nen:uint}){a<=b} #see:mk_tree_from_xnode_seq/xnode_seq2ldigit_node_seq_rdigit__q/___split_size__case_seq___'
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        check_int(sz, min=2*min_den)
        small_den, big_den, nen2count = type(sf).___split_size__case_seq___(sf, sz)
        _ops_check_result_of_split_size__case_seq(sf, sz, small_den, big_den, nen2count)
        return (small_den, big_den, mk_FrozenDict(nen2count))


    @abstractmethod
    def ___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf, /):
        '-> num_child_xnode_seq=overflow_nen::nen #see:get_num_child_xnode_seq_of_new_node_when_push_overflow'
    def _get_num_child_xnode_seq_of_new_node_when_push_overflow(sf, /):
        '-> num_child_xnode_seq=overflow_nen::nen #to avoid recur by not use _ops_check_overflow_nen #see: get_num_child_xnode_seq_of_new_node_when_push_overflow'
        overflow_nen = type(sf).___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf)
        _ops_check_overflow_nen__part(sf, overflow_nen)
        return overflow_nen
    def get_num_child_xnode_seq_of_new_node_when_push_overflow(sf, /):
        '-> num_child_xnode_seq=overflow_nen::nen #see: ipushL__tree/___get_num_child_xnode_seq_of_new_node_when_push_overflow___'
        overflow_nen = type(sf).___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf)
        _ops_check_overflow_nen(sf, overflow_nen)
        return overflow_nen


    def _check_nen(sf, nen, /):
        check_int_ge2(nen)
        nen_set = sf.get_node_element_number_frozenset()
        if not nen in nen_set: raise ValueError
    def _check_den(sf, den, /):
        check_uint(den)
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        if not min_den <= den <= max_den: raise ValueError
    def _check_len_line_tree(sf, sz0, /):
        check_uint(sz0)
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        if not sz0 < 2*min_den: raise ValueError
#end of class IFingerTreeOps__setting(ABC):










#HHHHH
def check_finger_tree_ops__setting(finger_tree_ops__setting:IFingerTreeOps__setting, /):
    r'''
view others/数学/编程/tree/finger_tree.txt
最终约束
  #由来 见下面safe
  +[2 <= min nd <= max nd <= max dg -min dg]
    约束甲
    #错:其实可以放宽，因为达到(1+max dg)后，可以拆成多个Node，max dg 不用太大
    #   单Node补充，单Node进位
  +[min nd <= 2*min dg][nd值可以组成[2*min dg..]的所有值]
    约束乙
  变量说明:
    nd 即 Node 的各种可能大小#下文给出[2..3]
    dg 即 Digit 的各种可能大小#下文给出[1..4]
  可选方案:
    0: nd<-[2,3], dg <-[1..>=4]
    1: nd<-[3,4], dg <-[3..>=7]
    2: nd<-[2,5], dg <-[2..>=7]
    3: nd<-[3,5], dg <-[4..>=9]
    4: nd<-[3,4,5], dg <-[2..>=7]
    5: nd<-[4,5,6,7], dg <-[2..>=9]
        nd<-[4,5,6,7], dg <-[2..10]
          2..5..7..10




    #'''
    check_instance(IFingerTreeOps__setting, finger_tree_ops__setting)
    nens = node_element_numbers = finger_tree_ops__setting.get_sorted_node_element_numbers()
    if 1:
        check_tuple(nens)
        check_all(check_int_ge2, nens)
        check_strict_sorted(nens)
        check_int(len(nens), min=2)
        lowbd = calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints(nens)
            #check inside gcd==1

    nen_set = node_element_number_set = finger_tree_ops__setting.get_node_element_number_frozenset()
    if 1:
        check_type_is(frozenset, nen_set)
        check_all(check_int_ge2, nen_set)
        check_len_of(nens, sz=len(nen_set))
        if not frozenset(nens) == nen_set: raise ValueError




    mM_den_pair = min_max_digit_element_number_pair = finger_tree_ops__setting.get_min_max_digit_element_number_pair()
    if 1:
        check_pair(mM_den_pair)
        check_all(check_int_ge1, mM_den_pair)
        check_strict_sorted(mM_den_pair)

    min_den, max_den = mM_den_pair
    min_nen = min(nens)
    max_nen = max(nens)
    if not 2 <= min_nen <= max_nen <= max_den - min_den: raise ValueError('约束甲')
    if not min_nen <= lowbd <= 2*min_den: raise ValueError('约束乙')


    if 1:
        def _check_sz2__dqd(sz2, /):
            nen2count = finger_tree_ops__setting.split_size__case_digit_seq_digit(sz2)
            _check_result_of_split_size__case_digit_seq_digit(nen_set, sz2, nen2count)
        def _check_sz2__q(sz2, /):
            small_den, big_den, nen2count = finger_tree_ops__setting.split_size__case_seq(sz2)
            _check_result_of_split_size__case_seq(nen_set, min_den, max_den, sz2, small_den, big_den, nen2count)
        def _check_sz1__dq(sz1, /):
            den, nen2count = finger_tree_ops__setting.split_size__case_digit_seq(sz1)
            _check_result_of_split_size__case_digit_seq(nen_set, min_den, max_den, sz1, den, nen2count)

    #nen_set = set(nens)
    #for i in range(min_nen):
    for i in range(sum(nens)):
        sz2 = 2*min_den +i
        _check_sz2__dqd(sz2)
        _check_sz2__q(sz2)

        sz1 = 1*min_den +i
        _check_sz1__dq(sz1)


    ###
    overflow_nen = finger_tree_ops__setting.get_num_child_xnode_seq_of_new_node_when_push_overflow()
    _ops_check_overflow_nen(finger_tree_ops__setting, overflow_nen)
#end of def check_finger_tree_ops__setting(finger_tree_ops__setting:IFingerTreeOps__setting, /):











#HHHHH
#begin of def _ops_check_result_of_...
if 1:
    def _check_nen2count(nen_set, sz, nen2count, /):
        check_mapping(nen2count)
        check_all(check_uint, nen2count.keys())
        check_all(check_uint, nen2count.values())
        if not len(nen2count) <= len(nen_set): raise ValueError
        if not set(nen2count) <= nen_set: raise ValueError
        if not sz == sum(nen*count for nen, count in nen2count.items()): raise ValueError

    def _ops_check_result_of_split_size__case_digit_seq_digit(finger_tree_ops__setting, sz2, nen2count, /):
        nen_set = finger_tree_ops__setting.get_node_element_number_frozenset()
        min_den, max_den = finger_tree_ops__setting.get_min_max_digit_element_number_pair()
        check_int(sz2, min=2*min_den)
        _check_result_of_split_size__case_digit_seq_digit(nen_set, sz2, nen2count)
    def _ops_check_result_of_split_size__case_seq(finger_tree_ops__setting, sz2, small_den, big_den, nen2count, /):
        nen_set = finger_tree_ops__setting.get_node_element_number_frozenset()
        min_den, max_den = finger_tree_ops__setting.get_min_max_digit_element_number_pair()
        check_int(sz2, min=2*min_den)
        _check_result_of_split_size__case_seq(nen_set, min_den, max_den, sz2, small_den, big_den, nen2count)
    def _ops_check_result_of_split_size__case_digit_seq(finger_tree_ops__setting, sz1, den, nen2count, /):
        nen_set = finger_tree_ops__setting.get_node_element_number_frozenset()
        min_den, max_den = finger_tree_ops__setting.get_min_max_digit_element_number_pair()
        check_int(sz1, min=1*min_den)
        _check_result_of_split_size__case_digit_seq(nen_set, min_den, max_den, sz1, den, nen2count)

    def _check_result_of_split_size__case_digit_seq_digit(nen_set, sz2, nen2count, /):
        _check_nen2count(nen_set, sz2, nen2count)
    def _check_result_of_split_size__case_seq(nen_set, min_den, max_den, sz2, small_den, big_den, nen2count, /):
        check_uint(small_den)
        check_uint(big_den)
        if not min_den <= small_den <= big_den <= max_den: raise ValueError
        if not small_den + big_den <= sz2: raise ValueError
        _check_nen2count(nen_set, sz2 - (small_den + big_den), nen2count)
    def _check_result_of_split_size__case_digit_seq(nen_set, min_den, max_den, sz1, den, nen2count, /):
        check_uint(den)
        if not min_den <= den <= max_den: raise ValueError
        if not den <= sz1: raise ValueError
        _check_nen2count(nen_set, sz1 - den, nen2count)

    def _ops_check_overflow_nen__part(finger_tree_ops__setting, overflow_nen, /):
        nen_set = finger_tree_ops__setting.get_node_element_number_frozenset()
        check_int_ge2(overflow_nen)
        if not overflow_nen in nen_set: raise ValueError

    def _ops_check_overflow_nen(finger_tree_ops__setting, overflow_nen, /):
        'see:get_num_child_xnode_seq_of_new_node_when_push_overflow'
        ####overflow_nen = finger_tree_ops__setting.get_num_child_xnode_seq_of_new_node_when_push_overflow()
        _ops_check_overflow_nen__part(finger_tree_ops__setting, overflow_nen)

        min_den, max_den = finger_tree_ops__setting.get_min_max_digit_element_number_pair()
        sz1 = max_den+1 #overflow@ipushL__tree
        check_int(sz1, min=1*min_den)
        den, nen2count = finger_tree_ops__setting.split_size__case_digit_seq(sz1)
            #recur?
        check_uint(den)
        check_mapping(nen2count)
        #if not nen2count == FrozenDict({overflow_nen:1}):raise ValueError
        if not len(nen2count) == 1:raise ValueError
        if not dict(nen2count) == {overflow_nen:1}:raise ValueError

        finger_tree_ops__setting._check_den(den)
        if not min_den+1 <= den == sz1-overflow_nen <= max_den-1:raise logic-err
#end of def _ops_check_result_of_...












#HHHHH
class IFingerTreeOps(IFingerTreeOps__setting):
    r'''
    tree<depth>
        = line_tree<depth>
        | deep_tree<depth>

    line_tree<depth>
        = Line (depth::uint, xnode_seq::[xnode<depth-1>], auto_info)
        where len(xnode_seq) <- [0..2*min_den-1]

    deep_tree<depth>
        = Deep (depth::uint, ldigit::digit<depth>, mtree::tree<depth+1>, rdigit::digit<depth>, auto_info)

    digit<depth>
        = Digit (depth::uint, xnode_seq::[xnode<depth-1>], auto_info)
        where len(xnode_seq) <- [min_den..max_den]

    xnode<imay_depth>
        | imay_depth == -1 = element
        | imay_depth >= 0 = let depth = imay_depth in node<depth>

    node<depth>
        = Node (depth::uint, xnode_seq::[xnode<depth-1>], auto_info)
        where len(xnode_seq) <- nens

    element
        = Element (user_obj, auto_info)

    #'''


    @abstractmethod
    def ___get_monoid_ops4auto_info___(sf, /):
        '-> monoid_ops<auto_info>::IMonoidOps #see:get_monoid_ops4auto_info'
    def get_monoid_ops4auto_info(sf, /):
        '-> monoid_ops<auto_info>::IMonoidOps #see:___get_monoid_ops4auto_info___'
        monoid_ops4auto_info = type(sf).___get_monoid_ops4auto_info___(sf)
        check_instance(IMonoidOps, monoid_ops4auto_info)
        return monoid_ops4auto_info

    @abstractmethod
    def ___get_auto_info_from_element___(sf, element, /):
        'element -> auto_info #see:get_auto_info_from_element'
    def get_auto_info_from_element(sf, element, /):
        'element -> auto_info #see:___get_auto_info_from_element___'
        sf.careless_check_element(element)
        auto_info = type(sf).___get_auto_info_from_element___(sf, element)
        sf.careless_check_auto_info(auto_info)
        return auto_info
    @abstractmethod
    def ___get_auto_info_from_node___(sf, depth, node, /):
        'depth -> node<depth> -> auto_info #see:get_auto_info_from_node'
    def get_auto_info_from_node(sf, depth, node, /):
        'depth -> node<depth> -> auto_info #see:___get_auto_info_from_node___'

        sf.careless_check_depth_of_node(depth, node)
        auto_info = type(sf).___get_auto_info_from_node___(sf, depth, node)
        sf.careless_check_auto_info(auto_info)
        return auto_info
    @abstractmethod
    def ___get_auto_info_from_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> auto_info #see:get_auto_info_from_digit'
    def get_auto_info_from_digit(sf, depth, digit, /):
        'depth -> digit<depth> -> auto_info #see:___get_auto_info_from_digit___'
        sf.careless_check_depth_of_digit(depth, digit)
        auto_info = type(sf).___get_auto_info_from_digit___(sf, depth, digit)
        sf.careless_check_auto_info(auto_info)
        return auto_info
    @abstractmethod
    def ___get_auto_info_from_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> auto_info #see:get_auto_info_from_line_tree'
    def get_auto_info_from_line_tree(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> auto_info #see:___get_auto_info_from_line_tree___'
        sf.careless_check_depth_of_line_tree(depth, line_tree)
        auto_info = type(sf).___get_auto_info_from_line_tree___(sf, depth, line_tree)
        sf.careless_check_auto_info(auto_info)
        return auto_info
    @abstractmethod
    def ___get_auto_info_from_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> auto_info #see:get_auto_info_from_deep_tree'
    def get_auto_info_from_deep_tree(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> auto_info #see:___get_auto_info_from_deep_tree___'
        sf.careless_check_depth_of_deep_tree(depth, deep_tree)
        auto_info = type(sf).___get_auto_info_from_deep_tree___(sf, depth, deep_tree)
        sf.careless_check_auto_info(auto_info)
        return auto_info



    @abstractmethod
    def ___get_num_child_xnode_seq_of_node___(sf, depth, node, /):
        'depth -> node<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_node'
    def get_num_child_xnode_seq_of_node(sf, depth, node, /):
        'depth -> node<depth> -> num_child_xnode_seq #see:___get_num_child_xnode_seq_of_node___'
        sf.careless_check_depth_of_node(depth, node)
        num_child_xnode_seq = type(sf).___get_num_child_xnode_seq_of_node___(sf, depth, node)
        nen = num_child_xnode_seq
        sf._check_nen(nen)
        return num_child_xnode_seq
    @abstractmethod
    def ___get_num_child_xnode_seq_of_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_digit'
    def get_num_child_xnode_seq_of_digit(sf, depth, digit, /):
        'depth -> digit<depth> -> num_child_xnode_seq #see:___get_num_child_xnode_seq_of_digit___'
        sf.careless_check_depth_of_digit(depth, digit)
        num_child_xnode_seq = type(sf).___get_num_child_xnode_seq_of_digit___(sf, depth, node)
        den = num_child_xnode_seq
        sf._check_den(den)
        return num_child_xnode_seq
    @abstractmethod
    def ___get_num_child_xnode_seq_of_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_line_tree'
    def get_num_child_xnode_seq_of_line_tree(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> num_child_xnode_seq #see:___get_num_child_xnode_seq_of_line_tree___'
        sf.careless_check_depth_of_line_tree(depth, line_tree)
        num_child_xnode_seq = type(sf).___get_num_child_xnode_seq_of_line_tree___(sf, depth, line_tree)
        sz0 = num_child_xnode_seq
        sf._check_len_line_tree(sz0)
        return num_child_xnode_seq


    # careless_check_... used only in mk_.../unbox_.../get_auto_info_from_.../get_num_child_xnode_seq_of_.../calc_auto_info_from_.../careless_check_...
    @abstractmethod
    def ___careless_check_auto_info___(sf, auto_info, /):
        'obj{?auto_info} -> (None|raise) #see:careless_check_auto_info'
    def careless_check_auto_info(sf, auto_info, /):
        'obj{?auto_info} -> (None|raise) #see:___careless_check_auto_info___'
        sf.get_monoid_ops4auto_info().careless_check_main_obj(auto_info)
        type(sf).___careless_check_auto_info___(sf, auto_info)
    @abstractmethod
    def careless_check_user_obj(sf, user_obj, /):
        'obj{?user_obj} -> (None|raise)'
    @abstractmethod
    def careless_check_element(sf, element, /):
        'obj{?element} -> (None|raise)'
    @abstractmethod
    def ___careless_check_depth_of_node___(sf, depth, node, /):
        'depth -> obj{?node<depth>} -> (None|raise) #see:careless_check_depth_of_node'
    def careless_check_depth_of_node(sf, depth, node, /):
        'depth -> obj{?node<depth>} -> (None|raise) #see:___careless_check_depth_of_node___'
        check_uint(depth)
        type(sf).___careless_check_depth_of_node___(sf, depth, node)
    @abstractmethod
    def ___careless_check_depth_of_digit___(sf, depth, digit, /):
        'depth -> obj{?digit<depth>} -> (None|raise) #see:careless_check_depth_of_digit'
    def careless_check_depth_of_digit(sf, depth, digit, /):
        'depth -> obj{?digit<depth>} -> (None|raise) #see:___careless_check_depth_of_digit___'
        check_uint(depth)
        type(sf).___careless_check_depth_of_digit___(sf, depth, digit)
    @abstractmethod
    def ___careless_check_depth_of_line_tree___(sf, depth, line_tree, /):
        'depth -> obj{?line_tree<depth>} -> (None|raise) #see:careless_check_depth_of_line_tree'
    def careless_check_depth_of_line_tree(sf, depth, line_tree, /):
        'depth -> obj{?line_tree<depth>} -> (None|raise) #see:___careless_check_depth_of_line_tree___'
        check_uint(depth)
        type(sf).___careless_check_depth_of_line_tree___(sf, depth, line_tree)
    @abstractmethod
    def ___careless_check_depth_of_deep_tree___(sf, depth, deep_tree, /):
        'depth -> obj{?deep_tree<depth>} -> (None|raise) #see:careless_check_depth_of_deep_tree'
    def careless_check_depth_of_deep_tree(sf, depth, deep_tree, /):
        'depth -> obj{?deep_tree<depth>} -> (None|raise) #see:___careless_check_depth_of_deep_tree___'
        check_uint(depth)
        type(sf).___careless_check_depth_of_deep_tree___(sf, depth, deep_tree)


    def careless_check_depth_of_tree(sf, depth, tree, /):
        'depth -> obj{?tree<depth>} -> (None|raise)'
        check_uint(depth)
        #but is_tree_line?? assume tree!!!
        if sf._is_tree_line(depth, tree):
            sf.careless_check_depth_of_line_tree(depth, tree)
        else:
            sf.careless_check_depth_of_deep_tree(depth, tree)
    def careless_check_depth_of_xnode(sf, depth, xnode, /):
        'depth -> obj{?xnode<depth-1>} -> (None|raise)'
        check_uint(depth)
        if not depth:
            sf.careless_check_element(xnode)
        else:
            node = xnode
            sf.careless_check_depth_of_node(depth, node)
    def careless_check_depth_of_xnode_seq(sf, depth, xnode_seq, /):
        'depth -> obj{?[xnode<depth-1>]} -> (None|raise)'
        check_uint(depth)
        check_seq(xnode_seq)
        for xnode in xnode_seq:
            sf.careless_check_depth_of_xnode(depth, xnode)



    def calc_auto_info_from_auto_infos(sf, auto_infos, /):
        'Iter auto_info -> auto_info'
        monoid_ops4auto_info = sf.get_monoid_ops4auto_info(auto_info)
        auto_info = monoid_ops4auto_info.assoc_op0s(auto_infos)
        sf.careless_check_auto_info(auto_info)
        return auto_info
    def calc_auto_info_from_xnode_seq(sf, depth, xnode_seq, /):
        'depth -> [xnode<depth-1>] -> auto_info'
        sf.careless_check_depth_of_xnode_seq(depth, xnode_seq)
        auto_infos = (sf.get_auto_info_from_xnode(depth, xnode) for xnode in xnode_seq)
        auto_info = sf.calc_auto_info_from_auto_infos(auto_infos)
        sf.careless_check_auto_info(auto_info)
        return auto_info

    @abstractmethod
    def ___mk_element__calc_auto_info___(sf, user_obj, /):
        'raw user_obj -> boxed element #see:mk_element'
    def mk_element(sf, user_obj, /):
        'raw user_obj -> boxed element #see:___mk_element__calc_auto_info___'
        sf.careless_check_user_obj(user_obj)
        element = type(sf).___mk_element__calc_auto_info___(sf, user_obj)
        sf.careless_check_element(element)
        auto_info = sf.get_auto_info_from_element(element)
        sf.careless_check_auto_info(auto_info)
        return element

    @abstractmethod
    def ___mk_node__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> node<depth> #see:mk_node'
    def mk_node(sf, depth, xnode_seq, /):
        'depth -> [xnode<depth-1>] -> node<depth> #see:___mk_node__not_auto___'
        sf.careless_check_depth_of_xnode_seq(depth, xnode_seq)
        nen = len(xnode_seq)
        sf._check_nen(nen)
        auto_info = sf.calc_auto_info_from_xnode_seq(depth, xnode_seq)
        sf.careless_check_auto_info(auto_info)
        node = type(sf).___mk_node__not_auto___(sf, depth, xnode_seq, auto_info)

        sf.careless_check_depth_of_node(depth, node)
        return node

    @abstractmethod
    def ___mk_digit__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> digit<depth> #see:mk_digit'
    def mk_digit(sf, depth, xnode_seq, /):
        'depth -> [xnode<depth-1>] -> digit<depth> #see:___mk_digit__not_auto___'
        sf.careless_check_depth_of_xnode_seq(depth, xnode_seq)
        den = len(xnode_seq)
        sf._check_den(den)
        auto_info = sf.calc_auto_info_from_xnode_seq(depth, xnode_seq)
        sf.careless_check_auto_info(auto_info)
        digit = type(sf).___mk_digit__not_auto___(sf, depth, xnode_seq, auto_info)

        sf.careless_check_depth_of_digit(depth, digit)
        return digit

    @abstractmethod
    def ___mk_line_tree__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> line_tree<depth> #see:mk_line_tree'
    def mk_line_tree(sf, depth, xnode_seq, /):
        'depth -> [xnode<depth-1>] -> line_tree<depth> #see:___mk_line_tree__not_auto___'
        sf.careless_check_depth_of_xnode_seq(depth, xnode_seq)
        sz0 = len(xnode_seq)
        sf._check_len_line_tree(sz0)
        auto_info = sf.calc_auto_info_from_xnode_seq(depth, xnode_seq)
        sf.careless_check_auto_info(auto_info)
        line_tree = type(sf).___mk_line_tree__not_auto___(sf, depth, xnode_seq, auto_info)

        sf.careless_check_depth_of_line_tree(depth, line_tree)
        return line_tree

    @abstractmethod
    def ___mk_deep_tree__not_auto___(sf, depth, ldigit, mtree, rdigit, auto_info, /):
        'depth -> digit<depth> -> tree<depth+1> -> digit<depth> -> auto_info -> deep_tree<depth> #see:mk_deep_tree'
    def mk_deep_tree(sf, depth, ldigit, mtree, rdigit, /):
        'depth -> digit<depth> -> tree<depth+1> -> digit<depth> -> deep_tree<depth> #see:___mk_deep_tree__not_auto___'
        sf.careless_check_depth_of_digit(depth, ldigit)
        sf.careless_check_depth_of_digit(depth, rdigit)
        sf.careless_check_depth_of_tree(depth+1, mtree)

        auto_infoL = sf.get_auto_info_from_digit(depth, ldigit)
        auto_infoR = sf.get_auto_info_from_digit(depth, rdigit)
        auto_infoM = sf.get_auto_info_from_tree(depth+1, mtree)

        auto_infos = [auto_infoL, auto_infoM, auto_infoR]
        auto_info = sf.calc_auto_info_from_auto_infos(depth, auto_infos)
        sf.careless_check_auto_info(auto_info)
        deep_tree = type(sf).___mk_deep_tree__not_auto___(sf, depth, ldigit, mtree, rdigit, auto_info)

        sf.careless_check_depth_of_deep_tree(depth, deep_tree)
        return deep_tree


    @abstractmethod
    def ___unbox_element___(sf, element, /):
        'boxed element -> (raw user_obj, auto_info) #see:unbox_element'
    def unbox_element(sf, element, /):
        'boxed element -> (raw user_obj, auto_info) #see:___unbox_element___'
        sf.careless_check_element(element)
        user_obj, auto_info = type(sf).___unbox_element___(sf, element)
        sf.careless_check_user_obj(user_obj)
        sf.careless_check_auto_info(auto_info)
        return user_obj, auto_info

    @abstractmethod
    def ___unbox_node___(sf, depth, node, /):
        'depth -> node<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_node'
    def unbox_node(sf, depth, node, /):
        'depth -> node<depth> -> ([xnode<depth-1>], auto_info) #see:___unbox_node___'
        sf.careless_check_depth_of_node(depth, node)
        xnode_seq, auto_info = type(sf).___unbox_node___(sf, depth, node)
        sf.careless_check_depth_of_xnode_seq(depth, xnode_seq)
        sf.careless_check_auto_info(auto_info)

        nen = len(xnode_seq)
        sf._check_nen(nen)
        return xnode_seq, auto_info

    @abstractmethod
    def ___unbox_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_digit'
    def unbox_digit(sf, depth, digit, /):
        'depth -> digit<depth> -> ([xnode<depth-1>], auto_info) #see:___unbox_digit___'
        sf.careless_check_depth_of_digit(depth, digit)
        xnode_seq, auto_info = type(sf).___unbox_digit___(sf, depth, digit)
        sf.careless_check_depth_of_xnode_seq(depth, xnode_seq)
        sf.careless_check_auto_info(auto_info)

        den = len(xnode_seq)
        sf._check_den(den)
        return xnode_seq, auto_info

    @abstractmethod
    def ___unbox_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_line_tree'
    def unbox_line_tree(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> ([xnode<depth-1>], auto_info) #see:___unbox_line_tree___'
        sf.careless_check_depth_of_line_tree(depth, line_tree)
        xnode_seq, auto_info = type(sf).___unbox_line_tree___(sf, depth, line_tree)
        sf.careless_check_depth_of_xnode_seq(depth, xnode_seq)
        sf.careless_check_auto_info(auto_info)

        sz0 = len(xnode_seq)
        sf._check_len_line_tree(sz0)
        return xnode_seq, auto_info

    @abstractmethod
    def ___unbox_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> (digit<depth>, tree<depth+1>, digit<depth>, auto_info) #see:unbox_deep_tree'
    def unbox_deep_tree(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> (digit<depth>, tree<depth+1>, digit<depth>, auto_info) #see:___unbox_deep_tree___'
        sf.careless_check_depth_of_deep_tree(depth, deep_tree)
        ldigit, mtree, rdigit, auto_info = type(sf).___unbox_deep_tree___(sf, depth, deep_tree)
        sf.careless_check_depth_of_digit(depth, ldigit)
        sf.careless_check_depth_of_digit(depth, rdigit)
        sf.careless_check_depth_of_tree(depth+1, mtree)
        sf.careless_check_auto_info(auto_info)

        return ldigit, mtree, rdigit, auto_info


    @abstractmethod
    def ___is_tree_line___(sf, depth, tree, /):
        'depth -> tree<depth> -> bool'
    def is_tree_line(sf, depth, tree, /):
        'depth -> tree<depth> -> bool'
        sf.careless_check_depth_of_tree(depth, tree)
        return sf._is_tree_line(depth, tree)
    def _is_tree_line(sf, depth, tree, /):
        'depth -> tree<depth> -> bool'
        b = type(sf).___is_tree_line___(sf, depth, tree)
        check_bool(b)
        return b
    def is_tree_deep(sf, depth, tree, /):
        'depth -> tree<depth> -> bool'
        return not sf.is_tree_line(depth, tree)


    def mk_top_tree_from_user_objs(sf, user_objs, /,*, reverse:bool):
        'Iter user_obj -> tree<depth=0> #see:mk_tree_from_xnode_seq/ipushL__top_tree'
        depth = 0
        if 0:
            element_seq = list(map(sf.mk_element, user_objs))
            xnode_seq = element_seq
            if reverse:
                xnode_seq.reverse()
            top_tree = sf.mk_tree_from_xnode_seq(depth, xnode_seq)
        else:
            top_tree = sf.mk_empty_tree(depth)
            ipush = sf.ipushL__top_tree if reverse else sf.ipushR__top_tree
            for user_obj in user_objs:
                top_tree = ipush(top_tree, user_obj)
        return top_tree

    def iter_user_objs__tree(sf, depth, tree, /,*, reverse:bool):
        'depth -> tree<depth> -> Iter user_obj'
        if sf.is_tree_line(depth, tree):
            return sf.iter_user_objs__line_tree(depth, tree, reverse=reverse)
        else:
            return sf.iter_user_objs__deep_tree(depth, tree, reverse=reverse)
    def iter_user_objs__deep_tree(sf, depth, deep_tree, /,*, reverse:bool):
        'depth -> deep_tree<depth> -> Iter user_obj'
        (ldigit, mtree, rdigit, auto_info) = sf.unbox_deep_tree(depth, tree)
        if reverse:
            ldigit, rdigit = rdigit, ldigit
        yield from sf.iter_user_objs__digit(depth, ldigit, reverse=reverse)
        yield from sf.iter_user_objs__tree(depth+1, mtree, reverse=reverse)
        yield from sf.iter_user_objs__digit(depth, rdigit, reverse=reverse)
        return
    def iter_user_objs__line_tree(sf, depth, line_tree, /,*, reverse:bool):
        'depth -> line_tree<depth> -> Iter user_obj'
        xnode_seq, auto_info = sf.unbox_line_tree(depth, line_tree)
        return sf.iter_user_objs__xnode_seq(depth, xnode_seq, reverse=reverse)
    def iter_user_objs__digit(sf, depth, digit, /,*, reverse:bool):
        'depth -> digit<depth> -> Iter user_obj'
        xnode_seq, auto_info = sf.unbox_digit(depth, digit)
        return sf.iter_user_objs__xnode_seq(depth, xnode_seq, reverse=reverse)
    def iter_user_objs__xnode_seq(sf, depth, xnode_seq, /,*, reverse:bool):
        'depth -> [xnode<depth-1>] -> Iter user_obj'
        f = reversed if reverse else iter
        for xnode in f(xnode_seq):
            yield from sf.iter_user_objs__xnode(depth, xnode, reverse=reverse)
    def iter_user_objs__xnode(sf, depth, xnode, /,*, reverse:bool):
        'depth -> xnode<depth-1> -> Iter user_obj'
        check_uint(depth)
        if depth:
            node = xnode
            depth -= 1
            return sf.iter_user_objs__node(depth, node, reverse=reverse)
        else:
            element = xnode
            return sf.iter_user_objs__element(element, reverse=reverse)
    def iter_user_objs__node(sf, depth, node, /,*, reverse:bool):
        'depth -> node<depth> -> Iter user_obj'
        xnode_seq, auto_info = sf.unbox_node(depth, node)
        return sf.iter_user_objs__xnode_seq(depth, xnode_seq, reverse=reverse)
    def iter_user_objs__element(sf, element, /,*, reverse:bool):
        'element -> Iter user_obj'
        user_obj, auto_info = sf.unbox_element(element)
        yield user_obj
        return

    def mk_empty_tree(sf, depth, /):
        'depth -> tree<depth>{len=0}'
        empty_tree = sf.mk_line_tree(depth, ())
        return empty_tree
    def mk_tree(sf, depth, is_deep_tree, payload, /):
        'depth -> (is_deep_tree::bool) -> (payload::tuple{see args@mk_deep_tree/mk_line_tree}) -> tree<depth>'
        if is_deep_tree:
            (ldigit, mtree, rdigit) = payload
            deep_tree = sf.mk_deep_tree(depth, ldigit, mtree, rdigit)
            new_tree = deep_tree
        else:
            (xnode_seq,) = payload
            line_tree = sf.mk_line_tree(depth, xnode_seq)
            new_tree = line_tree
        return new_tree
    def unbox_tree(sf, depth, tree, /):
        'depth -> tree<depth> -> ((is_deep_tree::bool), (payload::tuple{see args@mk_deep_tree/mk_line_tree}), auto_info)'
        is_deep_tree = sf.is_tree_deep(depth, tree)
        if is_deep_tree:
            (ldigit, mtree, rdigit, auto_info) = sf.unbox_deep_tree(depth, tree)
            payload = (ldigit, mtree, rdigit)
        else:
            (xnode_seq, auto_info) = sf.unbox_line_tree(depth, tree)
            payload = (xnode_seq,)
        return is_deep_tree, payload, auto_info

    def get_auto_info_from_tree(sf, depth, tree, /):
        'depth -> tree<depth> -> auto_info'
        is_deep_tree = sf.is_tree_deep(depth, tree)
        if is_deep_tree:
            auto_info = sf.get_auto_info_from_deep_tree(depth, tree)
        else:
            auto_info = sf.get_auto_info_from_line_tree(depth, tree)
        return auto_info


    def mk_tree_from_xnode_seq(sf, depth, xnode_seq, /):
        'depth -> [xnode<depth-1>] -> tree<depth>'
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        def _recur_mk_tree_from_xnode_seq(depth, xnode_seq, /):
            sz = len(xnode_seq)
            if sz < 2*min_den:
                new_tree = sf.mk_line_tree(depth, xnode_seq)
            else:
                (ldigit, node_seqM, rdigit) = sf.xnode_seq2ldigit_node_seq_rdigit__q(depth, xnode_seq)
                new_mtree = _recur_mk_tree_from_xnode_seq(depth+1, node_seqM)
                new_tree = sf.mk_deep_tree(depth, ldigit, new_mtree, rdigit)
            return new_mtree
        new_tree = _recur_mk_tree_from_xnode_seq(depth, xnode_seq)
        return new_mtree

    def mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size(sf, depth, xnode_seqL, mtree, rdigit, /):
        'depth -> [xnode<depth-1>] -> tree<depth+1> -> digit<depth> -> tree<depth>'
        #(xnode_seqL, mtree, rdigit)
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        #def _recur_mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size(sf, depth, xnode_seqL, mtree, rdigit, /):
        sz = len(xnode_seqL)
        if sz <= max_den:
            xnode_seqLs = [xnode_seqL]
            def _put(xnode_seq, /):
                nonlocal sz
                xnode_seqLs.append(xnode_seq)
                sz += len(xnode_seq)
            def _join():
                new_xnode_seqL = tuple(itertools.chain.from_iterable(xnode_seqLs))
                assert len(new_xnode_seqL) == sz
                return new_xnode_seqL

            while sz < min_den:
                #(xnode_seqLs, mtree, rdigit)
                m = sf.may_ipopL__tree(depth+1, mtree)
                if m is None:
                    #(xnode_seqLs, (), rdigit)
                    (xnode_seqR, auto_info) = sf.unbox_digit(depth, rdigit)
                    _put(xnode_seqR)
                    new_xnode_seqL = _join()
                    #(xnode_seqLs, (), ())
                    new_tree = mk_tree_from_xnode_seq(depth, new_xnode_seqL)
                    break
                else:
                    mtree, node = m
                    xnode_seqM, auto_info = sf.unbox_node(depth, node)
                    #(xnode_seqLs, xnode_seqM, mtree, rdigit)
                    _put(xnode_seqM)
                    #(xnode_seqLs, mtree, rdigit)
            else:
                #(xnode_seqLs, mtree, rdigit)
                if not min_den <= sz <= max_den: raise logic-err #<<== max_nen <= max_den-min_den
                #new_mtree = mtree
                new_xnode_seqL = _join()
                ldigit = sf.mk_digit(depth, new_xnode_seqL)
                new_tree = sf.mk_deep_tree(depth, ldigit, mtree, rdigit)
            new_tree
        else:
            ldigit, node_seqL = sf.xnode_seq2ldigit_node_seq__qd(depth, xnode_seqL)
            #(ldigit, node_seqL, mtree, rdigit)
            new_mtree = sf.join__qt(depth+1, node_seqL, mtree)
                #_recur_mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size
            #(ldigit, new_mtree, rdigit)
            new_tree = sf.mk_deep_tree(depth, ldigit, new_tree, rdigit)
        return new_tree
    #end of def mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size(sf, depth, xnode_seqL, tree, rdigit, /):

    def mk_pseudo_deep_tree__with_xnode_seqR_of_arbitrary_size(sf, depth, ldigit, mtree, xnode_seqR, /):
        'depth -> digit<depth> -> tree<depth+1> -> [xnode<depth-1>] -> tree<depth>'
        ops = mk_ReversedFingerTreeOps(sf)
        return ops.mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size(depth, tuple_reversed(xnode_seqR), tree, ldigit)
            #input flip here!!!

    def is_empty__tree(sf, depth, tree, /):
        'depth -> tree<depth> -> bool'
        return sf.is_tree_line(depth, tree) and not sf.get_num_child_xnode_seq_of_line_tree(depth, tree)
    def __tail__may_ipopX__top_tree(sf, may, /):
        'may (tree<depth=0>, element) -> may (tree<depth=0>, user_obj)'
        if may is None:
            return None
        else:
            new_tree, element = may
            user_obj, auto_info = sf.unbox_element(element)
            return new_tree, user_obj
    def may_ipopL__top_tree(sf, top_tree, /):
        'tree<depth=0> -> may (tree<depth=0>, user_obj)'
        may = sf.may_ipopL__tree(0, tree)
        return sf.__tail__may_ipopX__top_tree(may)

    def may_ipopR__top_tree(sf, top_tree, /):
        'tree<depth=0> -> may (tree<depth=0>, user_obj)'
        may = sf.may_ipopR__tree(0, tree)
        return sf.__tail__may_ipopX__top_tree(may)

    def may_ipopL__tree(sf, depth, tree, /):
        'depth -> tree<depth> -> may (tree<depth>, xnode<depth-1>)'
        (is_deep_tree, payload, auto_info) = sf.unbox_tree(depth, tree)
        if is_deep_tree:
            (ldigit, mtree, rdigit) = payload
            (xnode_seq, auto_info) = sf.unbox_digit(depth, ldigit)
            min_den, max_den = sf.get_min_max_digit_element_number_pair()
            head, tail = xnode_seq[0], xnode_seq[1:]
            if len(xnode_seq) > min_den:
                tail_ldigit = sf.mk_digit(depth, tail)
                tail_tree = sf.mk_deep_tree(depth, tail_ldigit, mtree, rdigit)
                m = (head, tail_tree)
            elif len(xnode_seq) == min_den:
                m1 = sf.may_ipopL__tree(depth+1, mtree)
                if m1 is None:
                    (xnode_seqR, auto_info) = sf.unbox_digit(depth, rdigit)
                    tail_tree = sf.mk_tree_from_xnode_seq(depth, (*tail, *xnode_seqR))
                    m = (head, tail_tree)
                else:
                    (new_mtree, shifted_node) = m1

                    (shifted_xnode_seq, auto_info) = sf.unbox_node(depth, shifted_node)
                    new_xnode_seqL = (*tail, *shifted_xnode_seq)
                    if not min_den+1 <= len(new_xnode_seqL) <= max_den-1: raise logic-err
                    new_ldigit = sf.mk_digit(depth, new_xnode_seqL)
                    tail_tree = sf.mk_deep_tree(depth, new_ldigit, new_mtree, rdigit)
                    m = (head, tail_tree)
            else:
                raise logic-err
        else:
            (xnode_seq,) = payload
            if not xnode_seq:
                m = None
            else:
                head, tail = xnode_seq[0], xnode_seq[1:]
                tail_tree = sf.mk_line_tree(depth, tail)
                m = (head, tail_tree)
        return m
    def may_ipopR__tree(sf, depth, tree, /):
        'depth -> tree<depth> -> may (tree<depth>, xnode<depth-1>)'
        ops = mk_ReversedFingerTreeOps(sf)
        return ops.may_ipopL__tree(depth, tree)

    def ipushL__top_tree(sf, top_tree, user_obj, /):
        'tree<depth=0> -> user_obj -> tree<depth=0>'
        element = sf.mk_element(user_obj)
        return sf.ipushL__tree(0, top_tree, element)
    def ipushR__top_tree(sf, top_tree, user_obj, /):
        'tree<depth=0> -> user_obj -> tree<depth=0>'
        element = sf.mk_element(user_obj)
        return sf.ipushR__tree(0, top_tree, element)
    def ipushL__tree(sf, depth, tree, xnode, /):
        'depth -> tree<depth> -> xnode<depth-1> -> tree<depth>'
        (is_deep_tree, payload, auto_info) = sf.unbox_tree(depth, tree)
        if is_deep_tree:
            (ldigit, mtree, rdigit) = payload
            (xnode_seq, auto_info) = sf.unbox_digit(depth, ldigit)
            min_den, max_den = sf.get_min_max_digit_element_number_pair()
            if len(xnode_seq) < max_den:
                new_xnode_seqL = (xnode, *xnode_seq)
                new_ldigit = sf.mk_digit(depth, new_xnode_seqL)
                new_tree = sf.mk_deep_tree(depth, new_ldigit, mtree, rdigit)
            elif len(xnode_seq) == max_den:
                #recur:overflow_nen = sf.get_num_child_xnode_seq_of_new_node_when_push_overflow()
                overflow_nen = sf._get_num_child_xnode_seq_of_new_node_when_push_overflow()
                num_remain = max_den-overflow_nen
                new_xnode_seqL = (xnode, *xnode_seq[:num_remain])

                new_node = sf.mk_node(depth, xnode_seq[num_remain:])

                new_ldigit = sf.mk_digit(depth, new_xnode_seqL)
                new_mtree = sf.ipushL__tree(depth+1, mtree, new_node)
                new_tree = sf.mk_deep_tree(depth, new_ldigit, new_mtree, rdigit)
            else:
                raise logic-err
        else:
            (xnode_seq,) = payload
            new_xnode_seq = (xnode, *xnode_seq)
            new_tree = sf.mk_tree_from_xnode_seq(depth, new_xnode_seq)
        return new_tree
    def ipushR__tree(sf, depth, tree, xnode, /):
        'depth -> tree<depth> -> xnode<depth-1> -> tree<depth>'
        ops = mk_ReversedFingerTreeOps(sf)
        return ops.ipushL__tree(depth, tree, xnode)


    r'''outdated by +tmay_mid_xnode
    isplit L/R tree
        a = auto_info
        r = measured_result
    isplit L tree:
        [nonempty ltree] ==>> [not ok (init r, ltree)]
        [nonempty rtree] ==>> [ok (init r, ltree, head rtree)]
    isplit R tree:
        [nonempty rtree] ==>> [not ok (rtree, init r)]
        [nonempty ltree] ==>> [ok (last ltree, rtree, init r)]

    #'''
    def get_auto_info_from_xnode(sf, depth, xnode, /):
        'depth -> xnode<depth-1> -> auto_info #input depth instead of imay_depth!!!'
        #input depth instead of depth-1!!!
        #check_uint_imay
        check_uint(depth)
        if depth:
            node = xnode
            auto_info = sf.get_auto_info_from_node(depth-1, node)
        else:
            element = xnode
            auto_info = sf.get_auto_info_from_element(element)
        return auto_info
    def __isplitL__xnode_seq(sf, depth, xnode_seq, measurable_ops4auto_info, init_measured_result, measured_result2is_ok, /):
        r'''depth -> [xnode<depth-1>] -> measurable_ops<auto_info> -> measured_result -> (measured_result->bool) -> (xnode_seqL::[xnode<depth-1>], measured_result_before_mid_xnode, mid_xnode::xnode<depth-1>, xnode_seqR::[xnode<depth-1>])
        precondition:
            [nonempty xnode_seq]
            [ok(init, xnode_seq)]
        #'''
        monoid_ops4measured_result = measurable_ops4auto_info.get_monoid_ops4measured_result()
        _get_auto_info = sf.get_auto_info_from_xnode
        acc_measured_result = init_measured_result
        for i, xnode in enumerate(xnode_seq):
            auto_info = _get_auto_info(depth, xnode)
                #not depth-1!!!
            measured_result = measurable_ops4auto_info.measure(auto_info)
            old_acc = acc_measured_result
            acc_measured_result = monoid_ops4measured_result.assoc_bin_op(old_acc, measured_result)
            if measured_result2is_ok(acc_measured_result):
                mid_xnode = xnode
                measured_result_before_mid_xnode = old_acc
                break
        else:
            i = len(xnode_seq)
            raise logic-err--precondition
        xnode_seqL, _mid_xnode, xnode_seqR = xnode_seq[:i], xnode_seq[i], xnode_seq[i+1:]
        assert mid_xnode is _mid_xnode
        xnode_seqL = tuple(xnode_seqL)
        xnode_seqR = tuple(xnode_seqR)
        return xnode_seqL, measured_result_before_mid_xnode, mid_xnode, xnode_seqR
    def isplitL__tree(sf, depth, tree, measurable_ops4auto_info, init_measured_result, measured_result2is_ok, /):
        #return (ltree, measured_result_after_ltree, tmay_mid_xnode, rtree, mxrtree)
        r'''depth -> tree<depth> -> measurable_ops<auto_info> -> measured_result -> (measured_result->bool) -> (ltree::tree<depth>, measured_result_after_ltree, tmay_mid_xnode::(tmay xnode<depth-1>), rtree::tree<depth>, mxrtree::tree<depth>)
        [toList tree === toList ltree ++ toList tmay_mid_xnode ++ toList rtree]
        [toList tree === toList ltree ++ toList mxrtree]
            [toList mxrtree === toList tmay_mid_xnode ++ toList rtree]
            [tmay_mid_xnode === tmay_head mxrtree]

        [measured_result_after_ltree === measure(init, ltree)]

        [nonempty ltree] ==>> [not ok(init, ltree)]
            [ok(init, ltree)] ==>> [empty ltree]

        [nonempty tmay_mid_xnode] ==>> [ok(init, ltree ++++ tmay_mid_xnode)]

        [empty tmay_mid_xnode] <==> [empty mxrtree] <==> [tree === ltree] <==> [empty tree]or[not ok(init, tree)]
            [empty tmay_mid_xnode] ==>> [empty rtree]
            [nonempty tmay_mid_xnode] <==> [nonempty tree][ok(init, tree)]
        #'''
        monoid_ops4measured_result = measurable_ops4auto_info.get_monoid_ops4measured_result()
        def _main_isplitL__tree():
            if sf.is_empty__tree(depth, tree):
                #[empty tree]
                empty_tree = tree
                ltree = rtree = mxrtree = empty_tree
                tmay_mid_xnode = ()
                measured_result_after_ltree = init_measured_result
            else:
                #[nonempty tree]
                auto_infoT = sf.get_auto_info_from_tree(depth, tree)
                measured_resultT = measurable_ops4auto_info.measure(auto_infoT)
                measured_result_IT = monoid_ops4measured_result.assoc_bin_op(init_measured_result, measured_resultT)
                if measured_result2is_ok(measured_result_IT):
                    #[nonempty tree][ok(init, tree)]
                    #<==>[nonempty tmay_mid_xnode]
                    ltree, measured_result_before_mid_xnode, mid_xnode, rtree = _recur_isplitL__tree(depth, tree, init_measured_result)
                    measured_result_after_ltree = measured_result_before_mid_xnode
                    if sf.is_empty__tree(depth, rtree)):
                        empty_tree = rtree
                        ltree, mid_xnode = sf.may_ipopR__tree(depth, tree)
                        rtree = empty_tree
                    else:
                        pass
                    tmay_mid_xnode = (mid_xnode,)
                    if sf.is_empty__tree(depth, ltree)):
                        empty_tree = ltree
                        mxrtree = tree
                        rtree, mid_xnode = sf.may_ipopL__tree(depth, mxrtree)
                        ltree = empty_tree
                    else:
                        mxrtree = sf.ipushL__tree(depth, rtree, mid_xnode)
                    mxrtree

                else:
                    #[nonempty tree][not ok(init, tree)]
                    ltree = tree
                    tmay_mid_xnode = ()
                    rtree = mxrtree = sf.mk_empty_tree(depth)
                    measured_result_after_ltree = measured_result_IT
            return (ltree, measured_result_after_ltree, tmay_mid_xnode, rtree, mxrtree)
        #end of def _main_isplitL__tree():
        def _recur_isplitL__tree(depth, tree, init_measured_result, /):
            r'''depth -> tree<depth> -> measurable_ops<auto_info> -> measured_result -> (measured_result->bool) -> (ltree::tree<depth>,  measured_result_before_mid_xnode, mid_xnode::xnode<depth-1>, rtree::tree<depth>)   #MUST xnode, not tmay
            precondition:
                [nonempty tree]
                [ok(init, tree)]
            #'''
            (is_deep_tree, payload, auto_info) = sf.unbox_tree(depth, tree)
            if is_deep_tree:
                (ldigit, mtree, rdigit) = payload
                auto_infoL = sf.get_auto_info_from_digit(ldigit)
                measured_resultL = measurable_ops4auto_info.measure(auto_infoL)
                measured_result_IL = monoid_ops4measured_result.assoc_bin_op(init_measured_result, measured_resultL)
                if measured_result2is_ok(measured_result_IL):
                    (xnode_seqL, auto_infoL) = sf.unbox_digit(depth, ldigit)
                    xnode_seq_LL, measured_result_before_mid_xnode, mid_xnode, xnode_seq_LR = sf.__isplitL__xnode_seq(depth, xnode_seqL, measurable_ops4auto_info, init_measured_result, measured_result2is_ok)

                    ltree = sf.mk_line_tree(depth, xnode_seq_LL)
                    measured_result_before_mid_xnode, mid_xnode
                    rtree = sf.mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size(depth, xnode_seq_LR, mtree, rdigit)
                else:
                    auto_infoM = sf.get_auto_info_from_tree(mtree)
                    measured_resultM = measurable_ops4auto_info.measure(auto_infoM)
                    measured_result_ILM = monoid_ops4measured_result.assoc_bin_op(measured_result_IL, measured_resultM)
                    if measured_result2is_ok(measured_result_ILM):
                        mtreeL, measured_result_before_mid_node, mid_node, mtreeR = _recur_isplitL__tree(depth+1, mtree, measured_result_IL)
                        mid_xnode_seq, auto_info = sf.unbox_node(depth, mid_node)
                        mid_xnode_seqL, measured_result_before_mid_xnode, mid_xnode, mid_xnode_seqR = sf.__isplitL__xnode_seq(depth, mid_xnode_seq, measurable_ops4auto_info, measured_result_before_mid_node, measured_result2is_ok)
                        ltree = sf.mk_pseudo_deep_tree__with_xnode_seqR_of_arbitrary_size(depth, ldigit, mtreeL, mid_xnode_seqL)
                        measured_result_before_mid_xnode, mid_xnode
                        rtree = sf.mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size(depth, mid_xnode_seqR, mtreeR, rdigit)
                    else:
                        auto_infoR = sf.get_auto_info_from_digit(rdigit)
                        measured_resultR = measurable_ops4auto_info.measure(auto_infoR)
                        measured_result_ILMR = monoid_ops4measured_result.assoc_bin_op(measured_result_ILM, measured_resultR)
                        if measured_result2is_ok(measured_result_ILMR):
                            (xnode_seqR, auto_infoR) = sf.unbox_digit(depth, rdigit)
                            xnode_seq_RL, measured_result_before_mid_xnode, mid_xnode, xnode_seq_RR = sf.__isplitL__xnode_seq(depth, xnode_seqR, measurable_ops4auto_info, measured_result_ILM, measured_result2is_ok)

                            ltree = sf.mk_pseudo_deep_tree__with_xnode_seqR_of_arbitrary_size(depth, ldigit, mtree, xnode_seq_RL)
                            measured_result_before_mid_xnode, mid_xnode
                            rtree = sf.mk_line_tree(depth, xnode_seq_RR)
                        else:
                            raise logic-err

            else:
                (xnode_seqT,) = payload
                xnode_seq_TL, measured_result_before_mid_xnode, mid_xnode, xnode_seq_TR = sf.__isplitL__xnode_seq(depth, xnode_seqT, measurable_ops4auto_info, init_measured_result, measured_result2is_ok)
                ltree = sf.mk_line_tree(depth, xnode_seq_TL)
                measured_result_before_mid_xnode, mid_xnode
                rtree = sf.mk_line_tree(depth, xnode_seq_TR)
            return ltree, measured_result_before_mid_xnode, mid_xnode, rtree
        #end of def _recur_isplitL__tree


        (ltree, measured_result_after_ltree, tmay_mid_xnode, rtree, mxrtree) = _main_isplitL__tree()
        return (ltree, measured_result_after_ltree, tmay_mid_xnode, rtree, mxrtree)
    #end of def isplitL__tree

    def isplitR__tree(sf, depth, tree, measurable_ops4auto_info, init_measured_result, measured_result2is_ok, /):
        #return (lmxtree, ltree, tmay_mid_xnode, measured_result_before_rtree, rtree)
        r'''depth -> tree<depth> -> measurable_ops<auto_info> -> measured_result -> (measured_result->bool) -> (lmxtree::tree<depth>, ltree::tree<depth>, tmay_mid_xnode::(tmay xnode<depth-1>), measured_result_before_rtree, rtree::tree<depth>)
        [toList tree === toList ltree ++ toList tmay_mid_xnode ++ toList rtree]
        [toList tree === toList lmxtree ++ toList rtree]
            [toList lmxtree === toList ltree ++ toList tmay_mid_xnode]
            [tmay_mid_xnode === tmay_last lmxtree]

        [measured_result_before_rtree === measureR(rtree, init)]

        [nonempty rtree] ==>> [not okR(rtree, init)]
            [okR(rtree, init)] ==>> [empty rtree]

        [nonempty tmay_mid_xnode] ==>> [okR(tmay_mid_xnode ++++ rtree, init)]

        [empty tmay_mid_xnode] <==> [empty lmxtree] <==> [tree === rtree] <==> [empty tree]or[not okR(tree, init)]
            [empty tmay_mid_xnode] ==>> [empty ltree]
            [nonempty tmay_mid_xnode] <==> [nonempty tree][okR(tree, init)]
        #'''
        ######################
        'old api: depth -> tree<depth> -> measurable_ops<auto_info> -> measured_result -> (measured_result->bool) -> (ltree::tree<depth>, rtree::tree<depth>)'
        ops = mk_ReversedFingerTreeOps(sf)
        ops4auto_info = mk_ReversedMeasurableOps(measurable_ops4auto_info)
        (rtree, measured_result_before_rtree, tmay_mid_xnode, ltree, lmxtree) = ops.isplitL__tree(depth, tree, ops4auto_info, init_measured_result, measured_result2is_ok)
            #output flip here!!!
        return (lmxtree, ltree, tmay_mid_xnode, measured_result_before_rtree, rtree)

    def join__qt(sf, depth, xnode_seq, rtree, /):
        'depth -> (xnode_seq::[xnode<depth-1>]) -> (rtree::tree<depth>) -> tree<depth>'
        if sf.is_tree_line(depth, rtree):
            (xnode_seqR, auto_info) = sf.unbox_line_tree(depth, rtree)
            new_xnode_seq = (*xnode_seq, *xnode_seqR)
            new_tree = sf.mk_tree_from_xnode_seq(depth, new_xnode_seq)
        else:
            (ldigitR, mtreeR, rdigitR, auto_info) = sf.unbox_deep_tree(depth, rtree)
            (xnode_seqR, auto_info) = sf.unbox_digit(depth, ldigitR)
            new_xnode_seq = (*xnode_seq, *xnode_seqR)
            #(new_xnode_seq, mtreeR, rdigitR)
            new_tree = sf.mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size(depth, new_xnode_seq, mtreeR, rdigitR)
        return new_tree
    def join__tq(sf, depth, ltree, xnode_seq, /):
        'depth -> (ltree::tree<depth>) -> (xnode_seq::[xnode<depth-1>]) -> tree<depth>'
        ops = mk_ReversedFingerTreeOps(sf)
        return ops.join__qt(depth, tuple_reversed(xnode_seq), ltree)
            #input flip here!!!
    def join__tqt(sf, depth, ltree, xnode_seq, rtree, /):
        'depth -> (ltree::tree<depth>) -> (xnode_seq::[xnode<depth-1>]) -> (rtree::tree<depth>) -> tree<depth>'
        r'''
        mk_tree_from_xnode_seq
        mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size
        mk_pseudo_deep_tree__with_xnode_seqR_of_arbitrary_size
        join__qt
        join__tq
        #'''
        def _recur_join__tqt(depth, ltree, xnode_seq, rtree, /):
            if sf.is_tree_line(depth, ltree):
                (xnode_seqL, auto_info) = sf.unbox_line_tree(depth, ltree)
                new_xnode_seq = (*xnode_seqL, *xnode_seq)
                new_tree = sf.join__qt(depth, new_xnode_seq, rtree)
            elif sf.is_tree_line(depth, rtree):
                (xnode_seqR, auto_info) = sf.unbox_line_tree(depth, rtree)
                new_xnode_seq = (*xnode_seq, *xnode_seqR)
                new_tree = sf.join__tq(depth, ltree, new_xnode_seq)
            else:
                (ldigitL, mtreeL, rdigitL, auto_info) = sf.unbox_deep_tree(depth, ltree)
                (ldigitR, mtreeR, rdigitR, auto_info) = sf.unbox_deep_tree(depth, rtree)
                (xnode_seqL, auto_info) = sf.unbox_digit(depth, rdigitL)
                (xnode_seqR, auto_info) = sf.unbox_digit(depth, ldigitR)
                #(ldigitL, mtreeL, xnode_seqL, xnode_seq, xnode_seqR, mtreeR, rdigitR)
                new_xnode_seq = (*xnode_seqL, *xnode_seq, *xnode_seqR)
                new_node_seq = sf.xnode_seq2node_seq__dqd(depth, new_node_seq)
                #(ldigitL, mtreeL, new_node_seq, mtreeR, rdigitR)
                new_mtree = _recur_join__tqt(depth+1, mtreeL, new_node_seq, mtreeR)
                #(ldigitL, new_mtree, rdigitR)
                new_tree = sf.mk_deep_tree(depth, ldigitL, new_mtree, rdigitR)
            return new_tree
        #end of def _recur_join__tqt(depth, ltree, xnode_seq, rtree, /):
        new_tree = _recur_join__tqt(depth, ltree, xnode_seq, rtree)
        return new_tree
    #end of def join__tqt(sf, depth, ltree, xnode_seq, rtree, /):

    def _xnode_seq2node_seq__nen_count_pairs(sf, depth, xnode_seq, begin, nen2count, /,*, end=None):
        if end is None:
            end = len(xnode_seq)
        nen_count_pairs = sorted(nen2count.items())
        node_seq = sf.xnode_seq2node_seq__nen_count_pairs(depth, xnode_seq, begin, end, nen_count_pairs)
        return node_seq
    def xnode_seq2node_seq__nen_count_pairs(sf, depth, xnode_seq, begin, end, nen_count_pairs, /):
        if not 0 <= begin <= end <= len(xnode_seq): raise ValueError
        saved_end = end

        node_seq = []
        for nen, count in nen_count_pairs:
            for _ in range(count):
                end = begin + nen
                if not begin < end <= saved_end: raise ValueError
                node = sf.mk_node(depth, xnode_seq[begin:end])
                node_seq.append(node)
                begin = end
        if begin != saved_end: raise ValueError
        node_seq = tuple(node_seq)
        return node_seq

    def xnode_seq2node_seq__dqd(sf, depth, xnode_seq, /):
        'depth -> (xnode_seq::[xnode<depth-1>]{len>=2*min_den}) -> (node_seq::[node<depth>]) #see:join__tqt'
        sz2 = len(xnode_seq)
        nen2count = sf.split_size__case_digit_seq_digit(sz2)
        begin = 0
        node_seq = sf._xnode_seq2node_seq__nen_count_pairs(depth, xnode_seq, begin, nen2count)
        return node_seq
    def xnode_seq2ldigit_node_seq__qd(sf, depth, xnode_seq, /):
        'depth -> (xnode_seq::[xnode<depth-1>]{len>=1*min_den}) -> (ldigit::digit<depth>, node_seq::[node<depth>]) #see:join__qt/mk_pseudo_deep_tree__with_xnode_seqL_of_arbitrary_size'
        #split_size__case_digit_seq
        sz1 = len(xnode_seq)
        den, nen2count = sf.split_size__case_digit_seq(sz1)
        begin = den
        ldigit = sf.mk_digit(depth, xnode_seq[:begin])
        node_seq = sf._xnode_seq2node_seq__nen_count_pairs(depth, xnode_seq, begin, nen2count)
        return ldigit, node_seq

    def xnode_seq2ldigit_node_seq_rdigit__q(sf, depth, xnode_seq, /):
        'depth -> (xnode_seq::[xnode<depth-1>]{len>=2*min_den}) -> (ldigit::digit<depth>, node_seq::[node<depth>], rdigit::digit<depth>) #see:mk_tree_from_xnode_seq'
        #split_size__case_seq
        sz2 = len(xnode_seq)
        small_den, big_den, nen2count = sf.split_size__case_seq(sz2)
        begin = small_den
        end = sz2-big_den
        ldigit = sf.mk_digit(depth, xnode_seq[:begin])
        rdigit = sf.mk_digit(depth, xnode_seq[end:])
        node_seq = sf._xnode_seq2node_seq__nen_count_pairs(depth, xnode_seq, begin, nen2count, end=end)
        return ldigit, node_seq, rdigit


#end of class IFingerTreeOps(IFingerTreeOps__setting):















#HHHHH
r'''
tuple_reversed
ReversedMonoidOps(IMonoidOps)
ReversedMeasurableOps(IMeasurableOps)
mk_ReversedMonoidOps
mk_ReversedMeasurableOps
mk_ReversedFingerTreeOps
#'''

def tuple_reversed(seq, /):
    return tuple(reversed(seq))
def _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops, /):
    assert issubclass(ReversedOps, BaseOps)
    assert isinstance(ops, BaseOps)
    assert hasattr(ReversedOps, attr2get_original_ops)

    if type(ops) is ReversedOps:
        reversed_ops = ops
        r = getattr(reversed_ops, attr2get_original_ops)()
    else:
        r = ReversedOps(ops)
    return r

def mk_ReversedFingerTreeOps(finger_tree_ops, /):
    BaseOps = IFingerTreeOps
    ReversedOps = ReversedFingerTreeOps
    attr2get_original_ops = 'get_original_finger_tree_ops'
    ops = finger_tree_ops
    return _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops)
def mk_ReversedMeasurableOps(measurable_ops, /):
    if measurable_ops.is_assoc_bin_op_commutable():
        return measurable_ops
    BaseOps = IMeasurableOps
    ReversedOps = ReversedMeasurableOps
    attr2get_original_ops = 'get_original_measurable_ops'
    ops = measurable_ops
    return _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops)
def mk_ReversedMonoidOps(monoid_ops, /):
    if monoid_ops.is_assoc_bin_op_commutable():
        return monoid_ops
    BaseOps = IMonoidOps
    ReversedOps = ReversedMonoidOps
    attr2get_original_ops = 'get_original_monoid_ops'
    ops = monoid_ops
    return _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops)
def mk_ReversedAssocBinaryOps(assoc_bin_ops, /):
    if assoc_bin_ops.is_assoc_bin_op_commutable():
        return assoc_bin_ops
    BaseOps = IAssocBinaryOps
    ReversedOps = ReversedAssocBinaryOps
    attr2get_original_ops = 'get_original_assoc_bin_ops'
    ops = assoc_bin_ops
    return _mk_reversed_ops(BaseOps, ReversedOps, attr2get_original_ops, ops)






class ReversedAssocBinaryOps(IAssocBinaryOps):
    def __init__(sf, assoc_bin_ops, /):
        check_instance(IAssocBinaryOps, assoc_bin_ops)
        sf.__ops = assoc_bin_ops
        if type(sf.__ops) is __class__: raise TypeError
        if sf.__ops.is_assoc_bin_op_commutable(): raise ValueError

    def get_original_assoc_bin_ops(sf, /):
        '-> (assoc_bin_ops::IAssocBinaryOps)'
        return sf.__ops

    @override
    def ___is_assoc_bin_op_commutable___(sf, /):
        '-> (commutable::bool) #see:is_assoc_bin_op_commutable'
        return False
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        return sf.__ops.careless_check_main_obj(x)
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c)'
        return type(sf.__ops).___assoc_bin_op___(sf.__ops, rhs, lhs)
#end of class ReversedAssocBinaryOps(IAssocBinaryOps):
class ReversedMonoidOps(ReversedAssocBinaryOps, IMonoidOps):
    def __init__(sf, monoid_ops, /):
        check_instance(IMonoidOps, monoid_ops)
        super().__init__(monoid_ops)
        if type(sf.__ops) is __class__: raise TypeError
    @property
    def __ops(sf, /):
        return sf.get_original_assoc_bin_ops()
    def get_original_monoid_ops(sf, /):
        '-> (monoid_ops::IMonoidOps)'
        return sf.__ops


    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.__ops.get_monoid_identity()
#end of class ReversedMonoidOps(ReversedAssocBinaryOps, IMonoidOps):
class ReversedMeasurableOps(ReversedMonoidOps, IMeasurableOps):
    def __init__(sf, measurable_ops, /):
        check_instance(IMeasurableOps, measurable_ops)
        #sf.__ops = measurable_ops
        #if type(sf.__ops) is __class__: raise TypeError
        sf.__rops4r = mk_ReversedMonoidOps(measurable_ops.get_monoid_ops4measured_result())
        super().__init__(measurable_ops)
        if type(sf.__ops) is __class__: raise TypeError
    @property
    def __ops(sf, /):
        return sf.get_original_monoid_ops()
    def get_original_measurable_ops(sf, /):
        return sf.__ops

    @override
    def ___get_monoid_ops4measured_result___(measurable_ops, /):
        '-> monoid_ops<measured_result>::IMonoidOps #see:get_monoid_ops4measured_result'
        sf = measurable_ops
        return sf.__rops4r
    @override
    def ___measure___(measurable_ops, measurable_obj, /):
        'measurable_obj -> (measured_result::monoid_obj) #see:measure'
        sf = measurable_ops
        return sf.__ops.measure(measurable_obj)
#end of class ReversedMeasurableOps(ReversedMonoidOps, IMeasurableOps):









#HHHHH
class WrappedFingerTreeOps__setting(IFingerTreeOps__setting):
    'vivi UserDict/UserList'
    def __init__(sf, finger_tree_ops__setting, /):
        check_instance(IFingerTreeOps__setting, finger_tree_ops__setting)
        sf.__ops = finger_tree_ops__setting
    def get_original_finger_tree_ops__setting(sf, /):
        return sf.__ops
    #begin of overrides_of_WrappedFingerTreeOps__setting

#begin of wrapper_impl_of_IFingerTreeOps__setting
    ##################################
    ##################################
    ######IFingerTreeOps__setting#####
    ##################################
    ##################################
    @override
    def get_sorted_node_element_numbers(sf, /):
        '-> sorted tuple<uint>'
        return sf.__ops.get_sorted_node_element_numbers()
    @override
    def get_node_element_number_frozenset(sf, /):
        '-> frozenset<uint>'
        return sf.__ops.get_node_element_number_frozenset()
    @override
    def get_min_max_digit_element_number_pair(sf, /):
        '-> (min digit_element_numbers::uint, max digit_element_numbers::uint)'
        return sf.__ops.get_min_max_digit_element_number_pair()


    @override
    def ___split_size__case_digit_seq_digit___(sf, sz, /):
        '[2*min digit_element_numbers..] -> {nen:uint} #see:split_size__case_digit_seq_digit'
        return type(sf.__ops).___split_size__case_digit_seq_digit___(sf.__ops, sz)
    @override
    def ___split_size__case_digit_seq___(sf, sz, /):
        '[min digit_element_numbers..] -> (den, {nen:uint}) #see:split_size__case_digit_seq'
        return type(sf.__ops).___split_size__case_digit_seq___(sf.__ops, sz)
    @override
    def ___split_size__case_seq___(sf, sz, /):
        '[2*min digit_element_numbers..] -> (a::den, b::den, {nen:uint}){a<=b} #see:split_size__case_seq'
        return type(sf.__ops).___split_size__case_seq___(sf.__ops, sz)
    @override
    def ___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf, /):
        '-> num_child_xnode_seq=overflow_nen::nen #see:get_num_child_xnode_seq_of_new_node_when_push_overflow'
        return type(sf.__ops).___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf.__ops)

#end of wrapper_impl_of_IFingerTreeOps__setting
    #end of overrides_of_WrappedFingerTreeOps__setting
#end of class WrappedFingerTreeOps__setting(IFingerTreeOps__setting):


class IFingerTreeOps__wrapped_setting(WrappedFingerTreeOps__setting, IFingerTreeOps):
    pass
class WrappedFingerTreeOps(IFingerTreeOps__wrapped_setting):
    'vivi UserDict/UserList'
    def __init__(sf, finger_tree_ops, /):
        check_instance(IFingerTreeOps, finger_tree_ops)
        super().__init__(finger_tree_ops)
        #sf.__ops = finger_tree_ops
    @property
    def __ops(sf, /):
        return sf.get_original_finger_tree_ops__setting()
    def get_original_finger_tree_ops(sf, /):
        return sf.__ops
    #begin of overrides_of_WrappedFingerTreeOps

    r'''
step of making wrapper_impl_of_IFingerTreeOps

forward call 4 wrapper class
    the undering obj/wrapped obj named '__ops'
    each abstractmethod decl has form regex'^\s*def .*/):$''
    each abstractmethod decl occupy 3 lines
    copy all abstractmethod decls to file end
    exec below vim q/ search-cmd && q: edit-cmd, to remove non-abstractmethod func
^\(\s*@abstractmethod.*\)\n\(\s*def \s*\)\([a-zA-Z]\w*\)[(]\(\w\+\)\(, \)\?\(.*\), [/][)]:\n\(\s*\)\(\S.*\)
.,$s//\1\r\2\3(\4\5\6, \/):\r\7\8\r\7return \4.__ops.\3(\6)
^\(\s*@abstractmethod.*\)\n\(\s*def \s*\)\(__\w*__\)[(]\(\w\+\)\(.*\), [/][)]:\n\(\s*\)\(\S.*\)
.,$s//\1\r\2\3(\4\5, \/):\r\6\7\r\6return type(\4.__ops).\3(\4.__ops\5)
@abstractmethod$
.,$s//@override


#'''

#begin of wrapper_impl_of_IFingerTreeOps
    ##################################
    ##################################
    ######IFingerTreeOps__setting#####
    ##################################
    ##################################
    @override
    def get_sorted_node_element_numbers(sf, /):
        '-> sorted tuple<uint>'
        return sf.__ops.get_sorted_node_element_numbers()
    @override
    def get_node_element_number_frozenset(sf, /):
        '-> frozenset<uint>'
        return sf.__ops.get_node_element_number_frozenset()
    @override
    def get_min_max_digit_element_number_pair(sf, /):
        '-> (min digit_element_numbers::uint, max digit_element_numbers::uint)'
        return sf.__ops.get_min_max_digit_element_number_pair()


    @override
    def ___split_size__case_digit_seq_digit___(sf, sz, /):
        '[2*min digit_element_numbers..] -> {nen:uint} #see:split_size__case_digit_seq_digit'
        return type(sf.__ops).___split_size__case_digit_seq_digit___(sf.__ops, sz)
    @override
    def ___split_size__case_digit_seq___(sf, sz, /):
        '[min digit_element_numbers..] -> (den, {nen:uint}) #see:split_size__case_digit_seq'
        return type(sf.__ops).___split_size__case_digit_seq___(sf.__ops, sz)
    @override
    def ___split_size__case_seq___(sf, sz, /):
        '[2*min digit_element_numbers..] -> (a::den, b::den, {nen:uint}){a<=b} #see:split_size__case_seq'
        return type(sf.__ops).___split_size__case_seq___(sf.__ops, sz)
    @override
    def ___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf, /):
        '-> num_child_xnode_seq=overflow_nen::nen #see:get_num_child_xnode_seq_of_new_node_when_push_overflow'
        return type(sf.__ops).___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf.__ops)
    ##################################
    ##################################
    ###########IFingerTreeOps#########
    ##################################
    ##################################
    ##################################
    @override
    def ___get_monoid_ops4auto_info___(sf, /):
        '-> monoid_ops<auto_info>::IMonoidOps #see:get_monoid_ops4auto_info'
        return type(sf.__ops).___get_monoid_ops4auto_info___(sf.__ops)
    @override
    def ___get_auto_info_from_element___(sf, element, /):
        'element -> auto_info #see:get_auto_info_from_element'
        return type(sf.__ops).___get_auto_info_from_element___(sf.__ops, element)
    @override
    def ___get_auto_info_from_node___(sf, depth, node, /):
        'depth -> node<depth> -> auto_info #see:get_auto_info_from_node'
        return type(sf.__ops).___get_auto_info_from_node___(sf.__ops, depth, node)
    @override
    def ___get_auto_info_from_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> auto_info #see:get_auto_info_from_digit'
        return type(sf.__ops).___get_auto_info_from_digit___(sf.__ops, depth, digit)
    @override
    def ___get_auto_info_from_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> auto_info #see:get_auto_info_from_line_tree'
        return type(sf.__ops).___get_auto_info_from_line_tree___(sf.__ops, depth, line_tree)
    @override
    def ___get_auto_info_from_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> auto_info #see:get_auto_info_from_deep_tree'
        return type(sf.__ops).___get_auto_info_from_deep_tree___(sf.__ops, depth, deep_tree)
    @override
    def ___get_num_child_xnode_seq_of_node___(sf, depth, node, /):
        'depth -> node<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_node'
        return type(sf.__ops).___get_num_child_xnode_seq_of_node___(sf.__ops, depth, node)
    @override
    def ___get_num_child_xnode_seq_of_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_digit'
        return type(sf.__ops).___get_num_child_xnode_seq_of_digit___(sf.__ops, depth, digit)
    @override
    def ___get_num_child_xnode_seq_of_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_line_tree'
        return type(sf.__ops).___get_num_child_xnode_seq_of_line_tree___(sf.__ops, depth, line_tree)
    @override
    def ___careless_check_auto_info___(sf, auto_info, /):
        'obj{?auto_info} -> (None|raise) #see:careless_check_auto_info'
        return type(sf.__ops).___careless_check_auto_info___(sf.__ops, auto_info)
    @override
    def careless_check_user_obj(sf, user_obj, /):
        'obj{?user_obj} -> (None|raise)'
        return sf.__ops.careless_check_user_obj(user_obj)
    @override
    def careless_check_element(sf, element, /):
        'obj{?element} -> (None|raise)'
        return sf.__ops.careless_check_element(element)
    @override
    def ___careless_check_depth_of_node___(sf, depth, node, /):
        'depth -> obj{?node<depth>} -> (None|raise) #see:careless_check_depth_of_node'
        return type(sf.__ops).___careless_check_depth_of_node___(sf.__ops, depth, node)
    @override
    def ___careless_check_depth_of_digit___(sf, depth, digit, /):
        'depth -> obj{?digit<depth>} -> (None|raise) #see:careless_check_depth_of_digit'
        return type(sf.__ops).___careless_check_depth_of_digit___(sf.__ops, depth, digit)
    @override
    def ___careless_check_depth_of_line_tree___(sf, depth, line_tree, /):
        'depth -> obj{?line_tree<depth>} -> (None|raise) #see:careless_check_depth_of_line_tree'
        return type(sf.__ops).___careless_check_depth_of_line_tree___(sf.__ops, depth, line_tree)
    @override
    def ___careless_check_depth_of_deep_tree___(sf, depth, deep_tree, /):
        'depth -> obj{?deep_tree<depth>} -> (None|raise) #see:careless_check_depth_of_deep_tree'
        return type(sf.__ops).___careless_check_depth_of_deep_tree___(sf.__ops, depth, deep_tree)
    @override
    def ___mk_element__calc_auto_info___(sf, user_obj, /):
        'raw user_obj -> boxed element #see:mk_element'
        return type(sf.__ops).___mk_element__calc_auto_info___(sf.__ops, user_obj)
    @override
    def ___mk_node__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> node<depth> #see:mk_node'
        return type(sf.__ops).___mk_node__not_auto___(sf.__ops, depth, xnode_seq, auto_info)
    @override
    def ___mk_digit__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> digit<depth> #see:mk_digit'
        return type(sf.__ops).___mk_digit__not_auto___(sf.__ops, depth, xnode_seq, auto_info)
    @override
    def ___mk_line_tree__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> line_tree<depth> #see:mk_line_tree'
        return type(sf.__ops).___mk_line_tree__not_auto___(sf.__ops, depth, xnode_seq, auto_info)
    @override
    def ___mk_deep_tree__not_auto___(sf, depth, ldigit, mtree, rdigit, auto_info, /):
        'depth -> digit<depth> -> tree<depth+1> -> digit<depth> -> auto_info -> deep_tree<depth> #see:mk_deep_tree'
        return type(sf.__ops).___mk_deep_tree__not_auto___(sf.__ops, depth, ldigit, mtree, rdigit, auto_info)
    @override
    def ___unbox_element___(sf, element, /):
        'boxed element -> (raw user_obj, auto_info) #see:unbox_element'
        return type(sf.__ops).___unbox_element___(sf.__ops, element)
    @override
    def ___unbox_node___(sf, depth, node, /):
        'depth -> node<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_node'
        return type(sf.__ops).___unbox_node___(sf.__ops, depth, node)
    @override
    def ___unbox_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_digit'
        return type(sf.__ops).___unbox_digit___(sf.__ops, depth, digit)
    @override
    def ___unbox_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_line_tree'
        return type(sf.__ops).___unbox_line_tree___(sf.__ops, depth, line_tree)
    @override
    def ___unbox_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> (digit<depth>, tree<depth+1>, digit<depth>, auto_info) #see:unbox_deep_tree'
        return type(sf.__ops).___unbox_deep_tree___(sf.__ops, depth, deep_tree)
    @override
    def ___is_tree_line___(sf, depth, tree, /):
        'depth -> tree<depth> -> bool'
        return type(sf.__ops).___is_tree_line___(sf.__ops, depth, tree)
#end of wrapper_impl_of_IFingerTreeOps


    #end of overrides_of_WrappedFingerTreeOps
#end of class WrappedFingerTreeOps(IFingerTreeOps):










#HHHHH
class ReversedFingerTreeOps(WrappedFingerTreeOps):
    r'''
    reverse xnode_seq for input@___mk.../output@unbox...
    flip lhs/rhs@monoid_ops<auto_info>
    flip lhs/rhs@monoid_ops<measured_result>
        to impl R by L @IFingerTreeOps:
            may_ipopR__tree <<== may_ipopL__tree
            ipushR__tree <<== ipushL__tree
            isplitR__tree <<== isplitL__tree
            join__??
    #'''
    def __init__(sf, finger_tree_ops, /):
        super().__init__(finger_tree_ops)
        if type(sf.__ops) is __class__: raise TypeError
        sf.__rops4a = mk_ReversedMonoidOps(finger_tree_ops.get_monoid_ops4auto_info())
    def __ops(sf, /):
        return sf.get_original_finger_tree_ops()

    #begin of overrides_of_ReversedFingerTreeOps
    @override
    def ___get_monoid_ops4auto_info___(sf, /):
        '-> monoid_ops<auto_info>::IMonoidOps #see:get_monoid_ops4auto_info'
        '[modified]'; return sf.__rops4a
        return type(sf.__ops).___get_monoid_ops4auto_info___(sf.__ops)
    @override
    def ___mk_node__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> node<depth> #see:mk_node'
        '[modified]'; return type(sf.__ops).___mk_node__not_auto___(sf.__ops, depth, tuple_reversed(xnode_seq), auto_info)
        return type(sf.__ops).___mk_node__not_auto___(sf.__ops, depth, xnode_seq, auto_info)
    @override
    def ___mk_digit__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> digit<depth> #see:mk_digit'
        '[modified]'; return type(sf.__ops).___mk_digit__not_auto___(sf.__ops, depth, tuple_reversed(xnode_seq), auto_info)
        return type(sf.__ops).___mk_digit__not_auto___(sf.__ops, depth, xnode_seq, auto_info)
    @override
    def ___mk_line_tree__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> line_tree<depth> #see:mk_line_tree'
        '[modified]'; return type(sf.__ops).___mk_line_tree__not_auto___(sf.__ops, depth, tuple_reversed(xnode_seq), auto_info)
        return type(sf.__ops).___mk_line_tree__not_auto___(sf.__ops, depth, xnode_seq, auto_info)
    @override
    def ___mk_deep_tree__not_auto___(sf, depth, ldigit, mtree, rdigit, auto_info, /):
        'depth -> digit<depth> -> tree<depth+1> -> digit<depth> -> auto_info -> deep_tree<depth> #see:mk_deep_tree'
        '[modified]'; return type(sf.__ops).___mk_deep_tree__not_auto___(sf.__ops, depth, rdigit, mtree, ldigit, auto_info)
        return type(sf.__ops).___mk_deep_tree__not_auto___(sf.__ops, depth, ldigit, mtree, rdigit, auto_info)
    @override
    def ___unbox_node___(sf, depth, node, /):
        'depth -> node<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_node'
        '[modified]'; (xnode_seq, auto_info) = type(sf.__ops).___unbox_node___(sf.__ops, depth, node); return (tuple_reversed(xnode_seq), auto_info)
        return type(sf.__ops).___unbox_node___(sf.__ops, depth, node)
    @override
    def ___unbox_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_digit'
        '[modified]'; (xnode_seq, auto_info) = type(sf.__ops).___unbox_digit___(sf.__ops, depth, node); return (tuple_reversed(xnode_seq), auto_info)
        return type(sf.__ops).___unbox_digit___(sf.__ops, depth, digit)
    @override
    def ___unbox_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_line_tree'
        '[modified]'; (xnode_seq, auto_info) = type(sf.__ops).___unbox_line_tree___(sf.__ops, depth, node); return (tuple_reversed(xnode_seq), auto_info)
        return type(sf.__ops).___unbox_line_tree___(sf.__ops, depth, line_tree)
    @override
    def ___unbox_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> (digit<depth>, tree<depth+1>, digit<depth>, auto_info) #see:unbox_deep_tree'
        '[modified]'; (rdigit, mtree, ldigit, auto_info) = type(sf.__ops).___unbox_line_tree___(sf.__ops, depth, node); return (ldigit, mtree, rdigit, auto_info)
        return type(sf.__ops).___unbox_deep_tree___(sf.__ops, depth, deep_tree)
    #end of overrides_of_ReversedFingerTreeOps
#end of class ReversedFingerTreeOps(IFingerTreeOps):


r'''
def check_finger_tree_ops__part1__nens(finger_tree_ops:IFingerTreeOps, /):
    check_instance(IFingerTreeOps, finger_tree_ops)
    check_finger_tree_ops__setting(finger_tree_ops)
    ... ...
#'''








#HHHHH

r'''
step of making abstractmethod_decls_of_IFingerTreeOps
get abstractmethod decl
    each abstractmethod decl occupy 3 lines
    copy whole class body to file end
    exec below vim q/ search-cmd && q: edit-cmd, to remove non-abstractmethod func
^\(\s*@abstractmethod.*\)\n\(.*\)\n\(.*\)
.,$s//##?!\1\r##?!\2\r##?!\3
^\(##?!\)\@!.*\n
.,$s//
^\(##?!\)
.,$s//

#'''


#begin of abstractmethod_decls_of_IFingerTreeOps
class abstractmethod_decls_of_IFingerTreeOps(IFingerTreeOps):
    ##################################
    ##################################
    ######IFingerTreeOps__setting#####
    ##################################
    ##################################
    @abstractmethod
    def get_sorted_node_element_numbers(sf, /):
        '-> sorted tuple<uint>'
    @abstractmethod
    def get_node_element_number_frozenset(sf, /):
        '-> frozenset<uint>'
    @abstractmethod
    def get_min_max_digit_element_number_pair(sf, /):
        '-> (min digit_element_numbers::uint, max digit_element_numbers::uint)'


    @abstractmethod
    def ___split_size__case_digit_seq_digit___(sf, sz, /):
        '[2*min digit_element_numbers..] -> {nen:uint} #see:split_size__case_digit_seq_digit'
    @abstractmethod
    def ___split_size__case_digit_seq___(sf, sz, /):
        '[min digit_element_numbers..] -> (den, {nen:uint}) #see:split_size__case_digit_seq'
    @abstractmethod
    def ___split_size__case_seq___(sf, sz, /):
        '[2*min digit_element_numbers..] -> (a::den, b::den, {nen:uint}){a<=b} #see:split_size__case_seq'
    @abstractmethod
    def ___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf, /):
        '-> num_child_xnode_seq=overflow_nen::nen #see:get_num_child_xnode_seq_of_new_node_when_push_overflow'
    ##################################
    ##################################
    ###########IFingerTreeOps#########
    ##################################
    ##################################
    ##################################
    @abstractmethod
    def ___get_monoid_ops4auto_info___(sf, /):
        '-> monoid_ops<auto_info>::IMonoidOps #see:get_monoid_ops4auto_info'
    @abstractmethod
    def ___get_auto_info_from_element___(sf, element, /):
        'element -> auto_info #see:get_auto_info_from_element'
    @abstractmethod
    def ___get_auto_info_from_node___(sf, depth, node, /):
        'depth -> node<depth> -> auto_info #see:get_auto_info_from_node'
    @abstractmethod
    def ___get_auto_info_from_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> auto_info #see:get_auto_info_from_digit'
    @abstractmethod
    def ___get_auto_info_from_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> auto_info #see:get_auto_info_from_line_tree'
    @abstractmethod
    def ___get_auto_info_from_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> auto_info #see:get_auto_info_from_deep_tree'
    @abstractmethod
    def ___get_num_child_xnode_seq_of_node___(sf, depth, node, /):
        'depth -> node<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_node'
    @abstractmethod
    def ___get_num_child_xnode_seq_of_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_digit'
    @abstractmethod
    def ___get_num_child_xnode_seq_of_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_line_tree'
    @abstractmethod
    def ___careless_check_auto_info___(sf, auto_info, /):
        'obj{?auto_info} -> (None|raise) #see:careless_check_auto_info'
    @abstractmethod
    def careless_check_user_obj(sf, user_obj, /):
        'obj{?user_obj} -> (None|raise)'
    @abstractmethod
    def careless_check_element(sf, element, /):
        'obj{?element} -> (None|raise)'
    @abstractmethod
    def ___careless_check_depth_of_node___(sf, depth, node, /):
        'depth -> obj{?node<depth>} -> (None|raise) #see:careless_check_depth_of_node'
    @abstractmethod
    def ___careless_check_depth_of_digit___(sf, depth, digit, /):
        'depth -> obj{?digit<depth>} -> (None|raise) #see:careless_check_depth_of_digit'
    @abstractmethod
    def ___careless_check_depth_of_line_tree___(sf, depth, line_tree, /):
        'depth -> obj{?line_tree<depth>} -> (None|raise) #see:careless_check_depth_of_line_tree'
    @abstractmethod
    def ___careless_check_depth_of_deep_tree___(sf, depth, deep_tree, /):
        'depth -> obj{?deep_tree<depth>} -> (None|raise) #see:careless_check_depth_of_deep_tree'
    @abstractmethod
    def ___mk_element__calc_auto_info___(sf, user_obj, /):
        'raw user_obj -> boxed element #see:mk_element'
    @abstractmethod
    def ___mk_node__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> node<depth> #see:mk_node'
    @abstractmethod
    def ___mk_digit__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> digit<depth> #see:mk_digit'
    @abstractmethod
    def ___mk_line_tree__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> line_tree<depth> #see:mk_line_tree'
    @abstractmethod
    def ___mk_deep_tree__not_auto___(sf, depth, ldigit, mtree, rdigit, auto_info, /):
        'depth -> digit<depth> -> tree<depth+1> -> digit<depth> -> auto_info -> deep_tree<depth> #see:mk_deep_tree'
    @abstractmethod
    def ___unbox_element___(sf, element, /):
        'boxed element -> (raw user_obj, auto_info) #see:unbox_element'
    @abstractmethod
    def ___unbox_node___(sf, depth, node, /):
        'depth -> node<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_node'
    @abstractmethod
    def ___unbox_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_digit'
    @abstractmethod
    def ___unbox_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_line_tree'
    @abstractmethod
    def ___unbox_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> (digit<depth>, tree<depth+1>, digit<depth>, auto_info) #see:unbox_deep_tree'
    @abstractmethod
    def ___is_tree_line___(sf, depth, tree, /):
        'depth -> tree<depth> -> bool'
#end of abstractmethod_decls_of_IFingerTreeOps















#HHHHH
NamedTuple4FingerTreeOps__setting = namedtuple(
    'NamedTuple4FingerTreeOps__setting', '''
        sorted_nens
        nen_set
        min_max_den_pair
        overflow_nen

        may_ordered_nens
    '''.split()
    )

def mk_NamedTuple4FingerTreeOps__setting(nens, min_max_den_pair, overflow_nen, may_ordered_nens, /):
    nen_set = frozenset(nens)
    sorted_nens = tuple(sorted(nens))
    return NamedTuple4FingerTreeOps__setting(sorted_nens ,nen_set ,min_max_den_pair ,overflow_nen ,may_ordered_nens)
def mk_FingerTreeOps__setting(nens, min_max_den_pair, overflow_nen, may_ordered_nens, /):
    config = mk_NamedTuple4FingerTreeOps__setting(nens, min_max_den_pair, overflow_nen, may_ordered_nens)
    finger_tree_ops__setting = FingerTreeOps__setting(config)
    return finger_tree_ops__setting
def _mk_FingerTreeOps__setting(nens, min_max_den_pair, /):
    nens = set(nens)
    overflow_nen = max_nen = max(nens)
    may_ordered_nens = None
    finger_tree_ops__setting = mk_FingerTreeOps__setting(nens, min_max_den_pair, overflow_nen, may_ordered_nens)
    return finger_tree_ops__setting


class FingerTreeOps__setting(IFingerTreeOps__setting):
    'usage:subclass<IFingerTreeOps__wrapped_setting>(finger_tree_ops__setting:FingerTreeOps__setting)'
    def __init__(sf, named_tuple4FingerTreeOps__setting:NamedTuple4FingerTreeOps__setting, /):
        check_instance(NamedTuple4FingerTreeOps__setting, named_tuple4FingerTreeOps__setting)
        sf.__config = named_tuple4FingerTreeOps__setting
        sf.__helper = Helper4cut_uint_into_uints(sf.__config.nen_set)
        may_ordered_nens = sf.__config.may_ordered_nens
        if may_ordered_nens is not None:
            ordered_nens = may_ordered_nens
            check_tuple(ordered_nens)
            check_all(check_int_ge2, ordered_nens)
            nen_set = sf.__config.nen_set
            check_len_of(ordered_nens, sz=len(nen_set))
            if not set(ordered_nens) == nen_set: raise ValueError
        check_finger_tree_ops__setting(sf)

    ## source from abstractmethod_decls_of_IFingerTreeOps
    @override
    def get_sorted_node_element_numbers(sf, /):
        '-> sorted tuple<uint>'
        return sf.__config.sorted_nens
    @override
    def get_node_element_number_frozenset(sf, /):
        '-> frozenset<uint>'
        return sf.__config.nen_set
    @override
    def get_min_max_digit_element_number_pair(sf, /):
        '-> (min digit_element_numbers::uint, max digit_element_numbers::uint)'
        return sf.__config.min_max_den_pair
    @override
    def ___get_num_child_xnode_seq_of_new_node_when_push_overflow___(sf, /):
        '-> num_child_xnode_seq=overflow_nen::nen #see:get_num_child_xnode_seq_of_new_node_when_push_overflow'
        return sf.__config.overflow_nen



    r'''
    Helper4cut_uint_into_uints
        possible_parts_of
        calc_lowerbound_of_inf_compact_domain_rng
        cut_uint_into_uints__greedy
        cut_uint_into_uints__greedy_last__ordered_part_uints
    #'''

    @override
    def ___split_size__case_digit_seq_digit___(sf, sz, /):
        '[2*min digit_element_numbers..] -> {nen:uint} #see:split_size__case_digit_seq_digit'
        may_ordered_nens = sf.__config.may_ordered_nens
        nen2count = sf.__helper.cut_uint_into_uints__greedy_last__ordered_part_uints(may_ordered_nens, sz)
        return nen2count
    @override
    def ___split_size__case_digit_seq___(sf, sz, /):
        '[min digit_element_numbers..] -> (den, {nen:uint}) #see:split_size__case_digit_seq'
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        assert min_den <= sz
        if sz <= max_den:
            den = sz
            nen2count = {}
        else:
            #recur:overflow_nen = sf.get_num_child_xnode_seq_of_new_node_when_push_overflow()
            overflow_nen = sf._get_num_child_xnode_seq_of_new_node_when_push_overflow()
            try_den = min_den
            tsz = sz-try_den # >max_den-min_den >= max_nen >= overflow_nen
            q, r = divmod(tsz, overflow_nen)
            den = try_den + r # <= min_den+overflow_nen-1 <= min_den+max_nen-1 <= max_den-1
            assert min_den <= den < max_den
            nen2count = {overflow_nen:q}
        return den, nen2count

    @override
    def ___split_size__case_seq___(sf, sz, /):
        '[2*min digit_element_numbers..] -> (a::den, b::den, {nen:uint}){a<=b} #see:split_size__case_seq'
        min_den, max_den = sf.get_min_max_digit_element_number_pair()
        assert 2*min_den <= sz
        if sz <= 2*max_den:
            den2 = sz
            nen2count = {}
        else:
            #recur:overflow_nen = sf.get_num_child_xnode_seq_of_new_node_when_push_overflow()
            overflow_nen = sf._get_num_child_xnode_seq_of_new_node_when_push_overflow()
            try_den2 = 2*min_den
            tsz = sz-try_den2 # >2*(max_den-min_den) >= 2*max_nen >= 2*overflow_nen
            q, r = divmod(tsz, overflow_nen)
            den2 = try_den2 + r # <= 2*min_den+overflow_nen-1 <= 2*min_den+max_nen-1 <= min_den+max_den-1
            assert 2*min_den <= den2 < min_den+max_den
            nen2count = {overflow_nen:q}
        assert 2*min_den <= den2 <= 2*max_den
        small_den = den2//2
        big_den = den2 - small_den
        return small_den, big_den, nen2count
#end of class FingerTreeOps__setting(IFingerTreeOps__setting):

r'''
可选方案:
    0: nd<-[2,3], dg <-[1..>=4]
    1: nd<-[3,4], dg <-[3..>=7]
    2: nd<-[2,5], dg <-[2..>=7]
    3: nd<-[3,5], dg <-[4..>=9]
    4: nd<-[3,4,5], dg <-[2..>=7]
    5: nd<-[4,5,6,7], dg <-[2..>=9]
        nd<-[4,5,6,7], dg <-[2..10]
          2..5..7..10
#'''

finger_tree_ops__setting__2c3__1T4 \
    = _mk_FingerTreeOps__setting({2,3}, (1,4))
finger_tree_ops__setting__3c4__3T7 \
    = _mk_FingerTreeOps__setting({3,4}, (3,7))
finger_tree_ops__setting__2c5__2T7 \
    = _mk_FingerTreeOps__setting({2,5}, (2,7))
finger_tree_ops__setting__3c5__4T9 \
    = _mk_FingerTreeOps__setting({3,5}, (4,9))
finger_tree_ops__setting__3c4c5__2T7 \
    = _mk_FingerTreeOps__setting({3,4,5}, (2,7))
finger_tree_ops__setting__4c5c6c7__2T9 \
    = _mk_FingerTreeOps__setting({4,5,6,7}, (2,9))
finger_tree_ops__setting__4c5c6c7__2T10 \
    = _mk_FingerTreeOps__setting({4,5,6,7}, (2,10))


finger_tree_ops__setting__2c3__1T4
finger_tree_ops__setting__3c4__3T7
finger_tree_ops__setting__2c5__2T7
finger_tree_ops__setting__3c5__4T9
finger_tree_ops__setting__3c4c5__2T7
finger_tree_ops__setting__4c5c6c7__2T9
finger_tree_ops__setting__4c5c6c7__2T10


class IFingerTreeOps__raw_mk_element(IFingerTreeOps):
    r'''
    @abstractmethod
    def ___mk_element__not_auto___(sf, user_obj, auto_info, /):
        'user_obj -> auto_info -> element #see:___mk_element__calc_auto_info___'
    @abstractmethod
    def ___calc_auto_info_from_user_obj___(sf, user_obj, /):
        'user_obj -> auto_info #see:calc_auto_info_from_user_obj'
    #'''
    @abstractmethod
    def ___mk_element__not_auto___(sf, user_obj, auto_info, /):
        'user_obj -> auto_info -> element #see:___mk_element__calc_auto_info___'
    @override
    def ___mk_element__calc_auto_info___(sf, user_obj, /):
        'raw user_obj -> boxed element #see:mk_element'
        auto_info = sf.calc_auto_info_from_user_obj(user_obj)
        element = type(sf).___mk_element__not_auto___(sf, user_obj, auto_info)
        sf.careless_check_element(element)
        return element
    @abstractmethod
    def ___calc_auto_info_from_user_obj___(sf, user_obj, /):
        'user_obj -> auto_info #see:calc_auto_info_from_user_obj'
    def calc_auto_info_from_user_obj(sf, user_obj, /):
        'user_obj -> auto_info #see:___calc_auto_info_from_user_obj___'
        sf.careless_check_user_obj(user_obj)
        auto_info = type(sf).___calc_auto_info_from_user_obj___(sf, user_obj)
        sf.careless_check_auto_info(auto_info)
        return auto_info
#end of class IFingerTreeOps__raw_mk_element(IFingerTreeOps):








class IFingerTreeOps__cased_data(IFingerTreeOps__raw_mk_element):
    'except:user_obj, auto_info'
    case_name_of_element = 'element'
    case_name_of_node = 'node'
    case_name_of_digit = 'digit'
    case_name_of_line_tree = 'line_tree'
    case_name_of_deep_tree = 'deep_tree'


    #IFingerTreeOps__raw_mk_element
    @override
    def ___mk_element__not_auto___(sf, user_obj, auto_info, /):
        'user_obj -> auto_info -> element #see:___mk_element__calc_auto_info___'
        return (sf.case_name_of_element, user_obj, auto_info)

    # abstractmethod_decls_of_IFingerTreeOps
    @override
    def ___get_auto_info_from_element___(sf, element, /):
        'element -> auto_info #see:get_auto_info_from_element'
        return element[-1]
    @override
    def ___get_auto_info_from_node___(sf, depth, node, /):
        'depth -> node<depth> -> auto_info #see:get_auto_info_from_node'
        return node[-1]
    @override
    def ___get_auto_info_from_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> auto_info #see:get_auto_info_from_digit'
        return digit[-1]
    @override
    def ___get_auto_info_from_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> auto_info #see:get_auto_info_from_line_tree'
        return line_tree[-1]
    @override
    def ___get_auto_info_from_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> auto_info #see:get_auto_info_from_deep_tree'
        return deep_tree[-1]

    @override
    def ___get_num_child_xnode_seq_of_node___(sf, depth, node, /):
        'depth -> node<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_node'
        return len(node[2])
    @override
    def ___get_num_child_xnode_seq_of_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_digit'
        return len(digit[2])
    @override
    def ___get_num_child_xnode_seq_of_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> num_child_xnode_seq #see:get_num_child_xnode_seq_of_line_tree'
        return len(line_tree[2])

    @override
    def careless_check_element(sf, element, /):
        'obj{?element} -> (None|raise)'
        check_cased_tuple(sf.case_name_of_element, 3, element)
    @override
    def ___careless_check_depth_of_node___(sf, depth, node, /):
        'depth -> obj{?node<depth>} -> (None|raise) #see:careless_check_depth_of_node'
        check_cased_tuple__with_depth(sf.case_name_of_node, 4, depth, node)
    @override
    def ___careless_check_depth_of_digit___(sf, depth, digit, /):
        'depth -> obj{?digit<depth>} -> (None|raise) #see:careless_check_depth_of_digit'
        check_cased_tuple__with_depth(sf.case_name_of_digit, 4, depth, digit)
    @override
    def ___careless_check_depth_of_line_tree___(sf, depth, line_tree, /):
        'depth -> obj{?line_tree<depth>} -> (None|raise) #see:careless_check_depth_of_line_tree'
        check_cased_tuple__with_depth(sf.case_name_of_line_tree, 4, depth, line_tree)
    @override
    def ___careless_check_depth_of_deep_tree___(sf, depth, deep_tree, /):
        'depth -> obj{?deep_tree<depth>} -> (None|raise) #see:careless_check_depth_of_deep_tree'
        check_cased_tuple__with_depth(sf.case_name_of_deep_tree, 6, depth, deep_tree)

    @override
    def ___mk_node__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> node<depth> #see:mk_node'
        return (sf.case_name_of_node, depth, xnode_seq, auto_info)
    @override
    def ___mk_digit__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> digit<depth> #see:mk_digit'
        return (sf.case_name_of_digit, depth, xnode_seq, auto_info)
    @override
    def ___mk_line_tree__not_auto___(sf, depth, xnode_seq, auto_info, /):
        'depth -> [xnode<depth-1>] -> auto_info -> line_tree<depth> #see:mk_line_tree'
        return (sf.case_name_of_line_tree, depth, xnode_seq, auto_info)
    @override
    def ___mk_deep_tree__not_auto___(sf, depth, ldigit, mtree, rdigit, auto_info, /):
        'depth -> digit<depth> -> tree<depth+1> -> digit<depth> -> auto_info -> deep_tree<depth> #see:mk_deep_tree'
        return (sf.case_name_of_deep_tree, depth, ldigit, mtree, rdigit, auto_info)

    @override
    def ___unbox_element___(sf, element, /):
        'boxed element -> (raw user_obj, auto_info) #see:unbox_element'
        return element[1:]
    @override
    def ___unbox_node___(sf, depth, node, /):
        'depth -> node<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_node'
        return node[2:]
    @override
    def ___unbox_digit___(sf, depth, digit, /):
        'depth -> digit<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_digit'
        return digit[2:]
    @override
    def ___unbox_line_tree___(sf, depth, line_tree, /):
        'depth -> line_tree<depth> -> ([xnode<depth-1>], auto_info) #see:unbox_line_tree'
        return line_tree[2:]
    @override
    def ___unbox_deep_tree___(sf, depth, deep_tree, /):
        'depth -> deep_tree<depth> -> (digit<depth>, tree<depth+1>, digit<depth>, auto_info) #see:unbox_deep_tree'
        return deep_tree[2:]

    @override
    def ___is_tree_line___(sf, depth, tree, /):
        'depth -> tree<depth> -> bool'
        check_union_of_cased_tuples({sf.case_name_of_line_tree:4, sf.case_name_of_deep_tree:6}, tree)
        is_deep_tree = tree[0] == sf.case_name_of_deep_tree
        if is_deep_tree:
            check_cased_tuple__with_depth(sf.case_name_of_deep_tree, 6, depth, deep_tree)
        else:
            check_cased_tuple__with_depth(sf.case_name_of_line_tree, 4, depth, line_tree)
        return not is_deep_tree
#end of class IFingerTreeOps__cased_data(IFingerTreeOps__raw_mk_element):
abstractmethod_decls_of_IFingerTreeOps
#
def check_cased_tuple__with_depth(case_name, sz, depth, obj, /):
    check_int_ge2(sz)
    check_uint(depth)
    check_cased_tuple(case_name, sz, obj)
    tpl2s = obj
    check_uint(tpl2s[1])
    if tpl2s[1] != depth: raise TypeError










class FingerTreeOps__funcs(IFingerTreeOps__cased_data, IFingerTreeOps__wrapped_setting):
    def __init__(sf, finger_tree_ops__setting:IFingerTreeOps__setting, monoid_ops4auto_info:IMonoidOps, /,*, calc_auto_info_from_user_obj, careless_check_user_obj):
        check_instance(IMonoidOps, monoid_ops4auto_info)
        check_callable(calc_auto_info_from_user_obj)
        check_callable(careless_check_user_obj)
        sf._monoid_ops4auto_info = monoid_ops4auto_info
        sf._calc_auto_info_from_user_obj = calc_auto_info_from_user_obj
        sf._careless_check_user_obj = careless_check_user_obj
        #sf._finger_tree_ops__setting = finger_tree_ops__setting
        super().__init__(finger_tree_ops__setting)

    @override
    def ___careless_check_auto_info___(sf, auto_info, /):
        'obj{?auto_info} -> (None|raise) #see:careless_check_auto_info'
        return
    @override
    def ___get_monoid_ops4auto_info___(sf, /):
        '-> monoid_ops<auto_info>::IMonoidOps #see:get_monoid_ops4auto_info'
        return sf._monoid_ops4auto_info
    @override
    def ___calc_auto_info_from_user_obj___(sf, user_obj, /):
        'user_obj -> auto_info #see:calc_auto_info_from_user_obj'
        return sf._calc_auto_info_from_user_obj(user_obj)
    @override
    def careless_check_user_obj(sf, user_obj, /):
        'obj{?user_obj} -> (None|raise)'
        return sf._careless_check_user_obj(user_obj)
    pass
#end of class FingerTreeOps__funcs(IFingerTreeOps__cased_data, IFingerTreeOps__wrapped_setting):
FingerTreeOps__funcs()

class MonoidOps4size(IMonoidOps__commutable, ISingleton):
    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        check_uint(x)

    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c)'
        return lhs + rhs

    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return 0
the_monoid_ops4size = MonoidOps4size()
assert the_monoid_ops4size is MonoidOps4size()

class IMonoidOps4max(IMonoidOps__commutable, ITotalOrderingOps__with_min_BOTTOM):
    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.get_min_BOTTOM()
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c)'
        return sf.max(lhs, rhs)

class IMonoidOps4max__default_total_ordering_ops(IMonoidOps4max, ITotalOrderingOps__default_total_ordering__with_min_BOTTOM):pass

class MonoidOps4max__imay(TotalOrderingOps__imay, IMonoidOps4max__default_total_ordering_ops):pass
the_monoid_ops4max__imay = MonoidOps4max__imay()
assert the_monoid_ops4max__imay is MonoidOps4max__imay()

class MonoidOps4max__uint(TotalOrderingOps__uint, IMonoidOps4max__default_total_ordering_ops):pass
the_monoid_ops4max__uint = MonoidOps4max__uint()
assert the_monoid_ops4max__uint is MonoidOps4max__uint()

class MonoidOps4max__tmay_pyobj(Mixin__Ops4OneMainObjType__tmay_pyobj, IMonoidOps4max__default_total_ordering_ops):pass
the_monoid_ops4max__tmay_pyobj = MonoidOps4max__tmay_pyobj()
assert the_monoid_ops4max__tmay_pyobj is MonoidOps4max__tmay_pyobj()

class MonoidOps4max__nmay_pyobj(IMonoidOps4max__default_total_ordering_ops, ISingleton):
class MonoidOps4max__tmay_var(IMonoidOps4max):
    def __init__(sf, arg_max_monoid_ops:IMonoidOps4max, /):
class MonoidOps4max__nmay_var(IMonoidOps4max):
    def __init__(sf, arg_max_monoid_ops:IMonoidOps4max, /):


def _do_nothing(x, /):pass
class MonoidOps4max__funcs(IMonoidOps4max):
    def __init__(sf, /,*, key_total_ordering_ops__with_min=None, key=None, careless_check_main_obj=None):
    def __init__(sf, /,*, min, __lt__=None, key=None, careless_check_main_obj=None):
        if __lt__ is None:
            __lt__ = operator.__lt__
        if key is None:
            key = echo
        if careless_check_main_obj is None:
            careless_check_main_obj = _do_nothing

        check_callable(__lt__)
        check_callable(key)
        check_callable(careless_check_main_obj)

        sf.__min = min
        sf.__lt = __lt__
        sf.__key = key
        sf.__check = careless_check_main_obj
    @override
    def ___assoc_bin_op___(sf, lhs, rhs, /):
        'a -> a -> a # (a*b)*c === a*(b*c)'
        if sf.__lt(sf.__key(lhs), sf.__key(rhs)):
            return rhs
        else:
            return lhs

    @override
    def ___careless_check_main_obj___(sf, x, /):
        'a -> (None|raise) #see:careless_check_main_obj'
        sf.__check(x)

    @override
    def ___get_monoid_identity___(sf, /):
        '-> 1 # 1*a === a*1 === a::monoid_obj #see:get_monoid_identity'
        return sf.__min











class IFingerTreeOps__sized(IFingerTreeOps):
    @abstractmethod
    def ___get_measurable_ops4auto_info2size___(sf, /):
        '-> IMeasurableOps<auto_info, size> #see:get_measurable_ops4auto_info2size'
    def get_measurable_ops4auto_info2size(sf, /):
        '-> IMeasurableOps<auto_info, size> #see:___get_measurable_ops4auto_info2size___'
        measurable_ops4auto_info2size = type(sf).___get_measurable_ops4auto_info2size___(sf)
        check_instance(IMeasurableOps, measurable_ops4auto_info2size)
        monoid_ops4size = measurable_ops4auto_info2size.get_monoid_ops4measured_result()
        if not monoid_ops4size is the_monoid_ops4size: raise ValueError #even mk_ReversedMonoidOps since commutable
        return measurable_ops4auto_info2size

    def len__tree(sf, depth, tree, /):
        'depth -> tree<depth> -> (size::uint)'
        auto_info = sf.get_auto_info_from_tree(depth, tree)
        measurable_ops4auto_info2size = sf.get_measurable_ops4auto_info2size()

        sz = measurable_ops4auto_info2size.measure(auto_info)
        check_uint(sz)
        return sz
    def len__element(sf, element, /):
        'element -> (size::uint)'
        return sf.len__xnode(0, element)#check inside
    def len__node(sf, depth, node, /):
        'depth -> node<depth> -> (size::uint)'
        check_uint(depth)
        return sf.len__xnode(depth+1, node)
    def len__xnode(sf, depth, xnode, /):
        'depth -> xnode<depth-1> -> (size::uint)'
        check_uint(depth)
        auto_info = sf.get_auto_info_from_xnode(depth, xnode)
        measurable_ops4auto_info2size = sf.get_measurable_ops4auto_info2size()

        sz = measurable_ops4auto_info2size.measure(auto_info)
        check_uint(sz)
        if not depth:
            element = xnode
            if not sz == 1: raise logic-err
        return sz


    def isplitL_at__tree(sf, depth, tree, i, /):
        #return (ltree, sz_ltree, imay_offsetL_inside_mid_xnode, sz_mid, tmay_mid_xnode, rtree, mxrtree)
        r'''depth -> tree<depth> -> (i::int) -> ((ltree<depth>, sz_ltree::uint, imay_offsetL_inside_mid_xnode::imay, sz_mid::uint, tmay_mid_xnode::(tmay xnode<depth-1>), rtree<depth>, mxrtree<depth>) |raise IndexError)

        [not abs(i) <= len tree] <==> [raise IndexError]
        let offsetted_i = i+sz if i < 0 else i

        output:
            ltree, sz_ltree=measured_result_after_ltree, tmay_mid_xnode, rtree, mxrtree
                see:isplitL__tree.__doc__
            imay_offsetL_inside_mid_xnode
                == offsetted_i - sz_ltree if tmay_mid_xnode else -1
                "L" means count from L to R based at end of ltree, i.e. begin of mid_xnode
            sz_mid
                == sum $ map len tmay_mid_xnode

        #'''
        #####################
        r'''old api:depth -> tree<depth> -> (i::int) -> ((ltree<depth>, rtree<depth>, ex4head_rtree::(()|(head_xnode_of_rtree::xnode<depth-1>, offsetL_inside_xnode::uint, sz_xnode::uint))) |raise IndexError)
        [not abs(i) <= len tree] <==> [raise IndexError]
        [empty rtree] <==> [() == ex4head_rtree]
        [nonempty rtree] <==> [(head rtree, idx_fromLtoR@head, len head) == ex4head_rtree]
        [tree === join(ltree, rtree)]
        [offsetted i@input === len ltree + offsetL_inside_xnode]
        [0 <= offsetL_inside_xnode < len head]
        #'''
        sz = sf.len__tree(depth, tree)
        i = offset_signed_idx_by_sz(sz, i)
        check_int(i, min=0, max=sz)

        measurable_ops4auto_info2size = sf.get_measurable_ops4auto_info2size()
        def measured_result2is_ok(sz, /):
            return i < sz
        init_sz = 0
        (ltree, sz_ltree, tmay_mid_xnode, rtree, mxrtree) = sf.isplitL__tree(depth, tree, measurable_ops4auto_info2size, init_sz, measured_result2is_ok)

        if not (sz_ltree == sf.len__tree(depth, ltree)): raise logic-err
        if tmay_mid_xnode:
            [mid_xnode] = tmay_mid_xnode
            sz_mid = sf.len__xnode(depth, mid_xnode)
            assert sz_mid > 0
            imay_offsetL_inside_mid_xnode = i - sz_ltree
        else:
            sz_mid = 0
            imay_offsetL_inside_mid_xnode = -1
        sz_lmxtree = sz_ltree + sz_mid

        if not (sz_mid == 0 <= sz_ltree==i==sz_lmxtree==sz or sz_mid > 0 <= sz_ltree <= i < sz_lmxtree <= sz): raise logic-err
        if depth==0:
            if not (0 <= sz_mid <= 1): raise logic-err
            if not (0 <= sz_ltree==i <=sz): raise logic-err

        if not (-1 <= imay_offsetL_inside_mid_xnode < sz_mid): raise logic-err
        if not (-1 == imay_offsetL_inside_mid_xnode < sz_mid == 0 or 0 <= imay_offsetL_inside_mid_xnode < sz_mid): raise logic-err

        return (ltree, sz_ltree, imay_offsetL_inside_mid_xnode, sz_mid, tmay_mid_xnode, rtree, mxrtree)

        may = sf.may_ipopL__tree(depth, mxrtree)
        if i < sz:
            if may is None: raise logic-err
            tail_of_rtree, head_xnode_of_rtree = may

            szL = sf.len__tree(depth, ltree)
            sz_xnode = sf.len__xnode(depth, head_xnode_of_rtree)
            if not 0 <= szL <= i < szL+sz_xnode <= sz: raise logic-err
            offsetL_inside_xnode = i - szL
            if not 0 <= offsetL_inside_xnode < sz_xnode: raise logic-err
            ex4head_rtree = (head_xnode_of_rtree, offsetL_inside_xnode, sz_xnode)
        else:
            if not may is None: raise logic-err
            #ltree = tree
            #rtree = empty
            ex4head_rtree = ()
        return (ltree, rtree, ex4head_rtree)
    #end of def isplitL_at__tree(sf, depth, tree, i, /):
    def isplitR_at__tree(sf, depth, tree, i, /):
        #return (lmxtree, ltree, tmay_mid_xnode, sz_mid, imay_offsetR_inside_mid_xnode, sz_rtree, rtree)
        r'''depth -> tree<depth> -> (i::int) -> ((lmxtree<depth>, ltree<depth>, tmay_mid_xnode::(tmay xnode<depth-1>), sz_mid::uint, imay_offsetR_inside_mid_xnode::imay, sz_rtree::uint, rtree<depth>) |raise IndexError)

        [not abs(i) <= len tree] <==> [raise IndexError]
        let offsetted_i = i+sz if i < 0 else i

        output:
            lmxtree, ltree, tmay_mid_xnode, sz_rtree=measured_result_before_rtree, rtree
                see:isplitR__tree.__doc__
            imay_offsetR_inside_mid_xnode
                == offsetted_i - sz_rtree if tmay_mid_xnode else -1
                "R" means count from R to L based at begin of rtree, i.e. end of mid_xnode
            sz_mid
                == sum $ map len tmay_mid_xnode

        #'''
        #####################
 
        r'''old api:depth -> tree<depth> -> (i::int) -> ((ltree<depth>, rtree<depth>, ex4last_ltree::(()|(last_xnode_of_ltree::xnode<depth-1>, offsetR_inside_xnode::uint, sz_xnode::uint))) |raise IndexError)
        [not abs(i) <= len tree] <==> [raise IndexError]
        [empty ltree] <==> [() == ex4last_ltree]
        [nonempty ltree] <==> [(last ltree, idx_fromRtoL@last, len last) == ex4last_ltree]
        [tree === join(ltree, rtree)]
        [offsetted i@input === offsetR_inside_xnode + len rtree]
        [0 <= offsetR_inside_xnode < len last]
        #'''
        ops = mk_ReversedFingerTreeOps(sf)
        (rtree, sz_rtree, imay_offsetR_inside_mid_xnode, sz_mid, tmay_mid_xnode, ltree, lmxtree) = ops.isplitL_at__tree(depth, tree, i)
            #output flip here!!!
        return (lmxtree, ltree, tmay_mid_xnode, sz_mid, imay_offsetR_inside_mid_xnode, sz_rtree, rtree)

    def at__tree(sf, depth, tree, i, /):
        'depth -> tree<depth> -> (i::int) -> ((xnode<depth-1>, offsetL_inside_xnode::uint, sz_xnode::uint)|raise IndexError)'
        (ltree, sz_ltree, imay_offsetL_inside_mid_xnode, sz_mid, tmay_mid_xnode, rtree, mxrtree) = sf.isplitL_at__tree(depth, tree, i)
        if not tmay_mid_xnode: raise IndexError
        [mid_xnode] = tmay_mid_xnode
        offsetL_inside_mid_xnode = imay_offsetL_inside_mid_xnode
        check_uint(offsetL_inside_mid_xnode)

        xnode = mid_xnode
        offsetL_inside_xnode = offsetL_inside_mid_xnode
        sz_xnode = sz_mid
        return (xnode, offsetL_inside_xnode, sz_xnode)

    def isplit_at__top_tree(sf, top_tree, i, /):
        'tree<depth=0> -> (i::int) -> ((ltree<depth=0>, tmay_mid_user_obj::tmay user_obj, rtree<depth=0>, mxrtree<depth=0>) |raise IndexError)'

        'old api:tree<depth=0> -> (i::int) -> ((ltree<depth=0>, rtree<depth=0>, tmay_head_user_obj_of_rtree) |raise IndexError)'
        depth = 0
        (ltree, sz_ltree, imay_offsetL_inside_mid_xnode, sz_mid, tmay_mid_xnode, rtree, mxrtree) = sf.isplitL_at__tree(depth, top_tree, i)
            #may raise IndexError inside
        if not tmay_mid_xnode:
            () = tmay_mid_xnode
            if not -1 == imay_offsetL_inside_mid_xnode < sz_mid == 0: raise logic-err
            tmay_mid_user_obj = ()
        else:
            (mid_xnode,) = tmay_mid_xnode
            if not 0 == imay_offsetL_inside_mid_xnode < sz_mid == 1: raise logic-err
            element = mid_xnode

            user_obj, auto_info = sf.unbox_element(element)
            mid_user_obj = user_obj
            tmay_mid_user_obj = (mid_user_obj,)
        tmay_mid_user_obj
        return (ltree, tmay_mid_user_obj, rtree, mxrtree)

    def at__top_tree(sf, top_tree, i, /):
        'tree<depth=0> -> (i::int) -> (user_obj|raise IndexError)'
        if 1:
            (ltree, tmay_mid_user_obj, rtree, mxrtree) = sf.isplit_at__top_tree(top_tree, i)
            if not tmay_mid_user_obj: raise IndexError
            [user_obj] = tmay_mid_user_obj
        else:
            depth = 0
            (xnode, offsetL_inside_xnode, sz_xnode) = sf.at__tree(depth, top_tree, i)
            element = xnode
            if not 0 == offsetL_inside_xnode < sz_xnode == 1: raise logic-err
            user_obj, auto_info = sf.unbox_element(element)
        return user_obj
    def slice__top_tree(sf, top_tree, begin, end, /):
        'tree<depth=0> -> (begin::may int) -> (end::may int) -> (tree<depth=0>|raise IndexError)'
        depth = 0
        sz = sf.len__tree(depth, top_tree)
        (begin, end) = offset_may_signed_rng_by_sz(sz, begin, end)
        if end <= begin:
            empty_tree = sf.mk_empty_tree(depth)
            new_tree = empty_tree
        else:
            ltree, _tm_mid, _rtree, _mxrtree = sf.isplit_at__top_tree(top_tree, end)
            _ltreeL, _tm_midL, _rtreeL, mxrtreeL = sf.isplit_at__top_tree(ltree, begin)
            new_tree = rtreeL
        return new_tree

def offset_may_signed_rng_by_sz(sz, begin, end, /):
    if begin is None:
        begin = 0
    if end is None:
        end = sz

    begin = offset_signed_idx_by_sz(sz, begin)
    end = offset_signed_idx_by_sz(sz, end)
    return begin, end

def offset_signed_idx_by_sz(sz, idx, /):
    check_int(idx)
    check_uint(sz)
    if not -sz <= i <= sz: raise IndexError
    if idx < 0:
        idx += sz
    check_int(idx, min=0, max=sz)
    return idx

class IFingerTreeOps__max_priority(IFingerTreeOps):
    @abstractmethod
    def ___get_measurable_ops4auto_info2max_priority___(sf, /):
        '-> IMeasurableOps<auto_info, max_priority> #see:get_measurable_ops4auto_info2max_priority'
    def get_measurable_ops4auto_info2max_priority(sf, /):
        '-> IMeasurableOps<auto_info, max_priority> #see:___get_measurable_ops4auto_info2max_priority___'
        measurable_ops4auto_info2max_priority = type(sf).___get_measurable_ops4auto_info2max_priority___(sf)
        check_instance(IMeasurableOps, measurable_ops4auto_info2max_priority)
        monoid_ops4max_priority = measurable_ops4auto_info2max_priority.get_monoid_ops4measured_result()
        if not isinstance(monoid_ops4max_priority, IMonoidOps4max): raise ValueError #even mk_ReversedMonoidOps since commutable
        return measurable_ops4auto_info2max_priority
    ... ...
    pop max?
    insert at eqvL/R keep sorted as if asc/dec??

isplitL__tree
#
#HHHHH

