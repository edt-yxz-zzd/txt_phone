r"""
underlying container <: IMutable
rollbackable container <: IMutable

[IHashable <: IImmutable]
[IImmutable /-\ IMutable == {}]
[IRollbackUnderlyingContainer <: IMutable]
[IImmutable /-\ IRollbackUnderlyingContainer == {}]

[IImmutableElement <: IImmutable]
data IEitherNEOW
	= (None, IImmutableElement)
	| (IRollbackWrapperOps, IRollbackWrapper)
	#immutable element or mutable container wrapper
data IEitherEC
	= IImmutableElement
	| IRollbackUnderlyingContainer
	#immutable element or mutable underlying container
data UpdateResult

data IRollbackUnderlyingContainer
	= IRollbackUnderlyingContainer<IEitherEC>

	= set<IHashable>
	| dict<IKey,IEitherEC>
	| union{nm=IEitherEC,...}
	| struct{nm=IEitherEC,...}
	| typed_dict{nm:IEitherEC,...}
		#== fixed_keyed_dict{nm:IEitherEC,...}
		#allow multi-keys be same key to vivi namedtuple
	| list<IEitherEC>
	| array<n, IEitherEC>
	| tuple<IEitherEC...>
	| namedtuple<nm=IEitherEC, ...>
	

[IKey <: IHashable]
data ElementFormat
	= None
	| (IRollbackWrapperOps, ElementFormat)
	| (IRollbackWrapperOps, {IKey: ElementFormat})
	= ImmutableElementFormat
	| IContainerFormat
data IContainerFormat
	= UniqueValueTypeContainerFormat IRollbackWrapperOps ElementFormat
	| KeyedValueTypeContainerFormat IRollbackWrapperOps {IKey: ElementFormat}
xxx data DirectPath = [IKey]
data ForwardPath
	= None
	| (IKey, ForwardPath)
data BackwardPath
	= None
	| (BackwardPath, IKey)

data MayBackwardPathPtrKeyPair
	= None
	| (BackwardPathPtr, IKey)
xxx BackwardPathPtr = weakref uint
BackwardPathPtr = object


xxx data RecordStackTail = [(Time, BackwardPathPtr, IRollbackRecord, {IKey:bool})]
data RecordStackTail = [(Time, BackwardPathPtr, IRollbackRecord)]
data RecordStack = [(0,)]++RecordStackTail

data SavePoint
	= (Time, Length)
	= (uint, uint)
	= (record_stack[-1][0], len(record_stack))


class IRollbackRecord(IImmutable):
	#modify inplace
	#when del key, we should save the value in record to rollback, hence record cannot be IHashable
	def __repr__(sf):
	def forward(sf, container)->UpdateResult:
	def backward(sf, container)->UpdateResult:

class RollbackWrapper__hidden_ref(IImmutable):
	.container_format
	.main_mngr
	.bpath_ptr
		#container_format
		#     ::IContainerFormat
		#
		#main_mngr:
		#     main_mngr.record(bpath_ptr, record)
		#     main_mngr.get_bpath_ptr(bpath_ptr, std_key=std_key)
		#     xxx main_mngr.on_key_disappear(bpath_ptr, key)
		#
		#bpath_ptr:
		#     ::BackwardPathPtr
		#

class IRollbackWrapper(ABC):
	#vivi underlying container API
	.???wrapper_hidden_ref???::RollbackWrapper__hidden_ref
	.???wrapper_hidden_ctnr???::IRollbackUnderlyingContainer
	#should avoid assign/setitem/setatttr unless element is IImmutableElement for record how to create the whole value
	#mk the element container from empty

class IRollbackWrapperOps(IImmutable):
	#all ops method:
	#     classmethod of type
	#  or bounded method of factory_obj
	#
	#
	#bug:def mk(sf, elem_format, main_mngr, path, container)->IRollbackWrapper:
	#  shouldnot init with raw container for the sake of record
		#xxx container:
		#     underlying container obj for wrapper
		#
	def mk(sf, wrapper_hidden_ref)->IRollbackWrapper:
	def _wrap_(sf, wrapper_hidden_ref, underlying_container)->IRollbackWrapper:
		#wrapper_hidden_ref
		#     ::RollbackWrapper__hidden_ref
		#
		#underlying_container
		#     ::IRollbackUnderlyingContainer
		#
	def to_std_key(sf, wrapper, key)->IKey:
	def _to_std_key_(sf, underlying_container, key)->IKey:
	def _raw_at_(sf, underlying_container, key)->IEitherEC:
	def _at_(sf, wrapper, key)->IEitherNEOW:
	def at(sf, wrapper, fpath)->IEitherNEOW:
		#fpath:
		#     ::ForwardPath
	def get_wrapper_hidden_ref(sf, wrapper)->RollbackWrapper__hidden_ref:
	def _get_underlying_container_(sf, wrapper)->IRollbackUnderlyingContainer:

	def _mk_raw_(sf)->IRollbackUnderlyingContainer:
	def _sub_container_info_at_key_(sf, wrapper, key)->Tuple[IRollbackWrapperOps, RollbackWrapper__hidden_ref]:

class IRollbackManager(ABC):
	#1. record_slot in record_stack hold deepest bpath_ptr
	#2. child requires parent: otherwise how (new_parent, key) -> child???
	#3. generate new bpath_ptr when we try to modify the container instead of when create the container
	#.may_bpath_ptr_key_pair2ptr
	#.bpath_ptr2bpath
	#.root_bpath_ptr
	#
	#outdate:
		#use weakref_dict again with .root_bpath_ptr
		#    since prev record_slot in record_stack contains bpath_ptr, hard to handle
		#.root_bpath_ptr
		#outdate:
			#neednot/shouldnot weakref_dict
			#remove explicit when a key/attr/idx disappear
			#.on_key_disappear
			#.bpath_ptr2key2ptr
			#.bpath_ptr2fpath

	.may_bpath_ptr_key_pair2ptr
		:: WeakValueDictionary{MayBackwardPathPtrKeyPair: BackwardPathPtr}
	.bpath_ptr2bpath
		:: WeakKeyDictionary{BackwardPathPtr: BackwardPath}
	.root_bpath_ptr

	xxx .bpath_ptr2key2ptr
		:: WeakKeyDictionary{BackwardPathPtr: {IKey: BackwardPathPtr}}
		xxx :: {BackwardPathPtr: {IKey: BackwardPathPtr}}
		xxx :: {(BackwardPathPtr, IKey): BackwardPathPtr}
		xxx :: WeakValueDictionary{(BackwardPathPtr, IKey): BackwardPathPtr}

	xxx .bpath_ptr2fpath
		:: WeakKeyDictionary{BackwardPathPtr:ForwardPath}
		xxx :: {BackwardPathPtr:ForwardPath}
		xxx :: WeakKeyDictionary{BackwardPathPtr:ForwardPath}

	.record_stack
		:: [(0,)]++RecordStackTail
	.time
		:: Time
	xxx .main_wrapper_ops
		:: IRollbackWrapperOps
	.main_container_format
		:: IContainerFormat

	def mk_main_wrapper(sf)->IRollbackWrapper:
	def get_main_container_format(sf)->IContainerFormat:
	def get_main_wrapper_ops(sf)->IRollbackWrapperOps:
	def get_root_bpath_ptr(sf)->BackwardPathPtr:
	def get_bpath_ptr(sf, bpath_ptr, *, std_key)->BackwardPathPtr:
	def bpath_ptr2fpath(sf, bpath_ptr)->ForwardPath:
	def tell(sf)->SavePoint:
	def rollback(sf, main_wrapper, save_point):
	def record(sf, bpath_ptr, record):
	xxx def record(sf, bpath_ptr, record, key2delset):
	xxx def on_key_disappear(sf, bpath_ptr, key):

#"""




from abc import ABC, abstractmethod, ABCMeta
from typing import (
	NewType
	,TypeVar
	,Generic
	#,Protocol
	#,overload
	#,final
	#,Any
	,Hashable
	)


override = lambda x:x
ST = TypeVar('ST')
OBJ = TypeVar('OBJ')


class IHiddenAccess(Generic[OBJ, ST], ABC):
	@abstractmethod
	def set_hidden_state(sf, obj:OBJ, st:ST)->None:
		pass
	@abstractmethod
	def get_hidden_state(sf, obj:OBJ)->ST:
		pass



class HiddenAccessABC(IHiddenAccess[OBJ,ST]):
	@abstractmethod
	def get_hidden_key(sf)->Hashable:
		pass
	@override
	def set_hidden_state(sf, obj:OBJ, st:ST)->None:
		d = object.__getattribute__(obj, "__dict__")
		k = sf.get_hidden_key()
		if k in d:
			raise Exception("hidden_state {k!r} already exists")
		d[k] = st

	@override
	def get_hidden_state(sf, obj:OBJ)->ST:
		d = object.__getattribute__(obj, "__dict__")
		k = sf.get_hidden_key()
		return d[k]


class HiddenAccess(HiddenAccessABC[OBJ,ST]):
	def __init__(sf, hidden_key:Hashable):
		assert hash(hidden_key) or 1
		sf.__k = hidden_key
	@override
	def get_hidden_key(sf)->Hashable:
		return sf.__k












##############
from weakref import WeakKeyDictionary, WeakValueDictionary
from abc import ABC, abstractmethod
from typing import (
	Union, Collection, Hashable
	,Mapping, MappingView
	,Tuple, List, Dict
	#, TypedDict
	#,ForwardRef
	,Iterable, Iterator
	,ContextManager
	)
from typing import (
	NewType
	,TypeVar
	,Generic
	#,Protocol
	,overload
	#,final
	,Any
	)
import contextlib#contextlib.contextmanager

override = lambda x:x
T = TypeVar('T')
S = TypeVar('S')
uint = NewType('uint', int)

class IMutable(ABC):pass
class IImmutable(ABC):pass
class IHashable(Hashable, IImmutable):pass
class IKey(IHashable):pass
IImmutableElement = NewType("IImmutableElement", IImmutable)
UpdateResult = NewType("UpdateResult", Any)

class IRollbackUnderlyingContainer(Collection[T], IMutable):pass
	#= IRollbackUnderlyingContainer<IEitherEC>

IEitherNEOW = Union[Tuple[None, IImmutableElement], Tuple["IRollbackWrapperOps", "IRollbackWrapper"]]
	#immutable element or mutable container wrapper
IEitherEC = Union[IImmutableElement, IRollbackUnderlyingContainer["IEitherEC"]]
	#immutable element or mutable underlying container
IRollbackUnderlyingContainer = IRollbackUnderlyingContainer[IEitherEC]

#ElementFormat = Union[None, Tuple["IRollbackWrapperOps", Union["ElementFormat", Mapping[IKey, "ElementFormat"]]]]
class ElementFormat(ABC):pass
class ImmutableElementFormat(ElementFormat):
	# for immutable element instead of sub_container
	def __new__(cls):
		raise Exception
		return super().__new__(cls)
theImmutableElementFormat = ElementFormat.__new__(ImmutableElementFormat)

class IContainerFormat(ElementFormat):
	@abstractmethod
	def get_wrapper_ops(sf)->"IRollbackWrapperOps":
		pass
	@abstractmethod
	def get_elem_format_at(sf, key:IKey)->ElementFormat:
		pass
class ContainerFormatABC(IContainerFormat):
	def __init__(sf, wrapper_ops:"IRollbackWrapperOps"):
		sf.__wrapper_ops = wrapper_ops
	@override
	def get_wrapper_ops(sf)->"IRollbackWrapperOps":
		return sf.__wrapper_ops
class UniqueValueTypeContainerFormat(ContainerFormatABC):
	def __init__(sf
			, wrapper_ops:"IRollbackWrapperOps"
			, elem_format:ElementFormat
			):
		sf.__elem_format = elem_format
		super().__init__(wrapper_ops)
	@override
	def get_elem_format_at(sf, key:IKey)->ElementFormat:
		return sf.__elem_format
class KeyedValueTypeContainerFormat(ContainerFormatABC):
	def __init__(sf
			, wrapper_ops:"IRollbackWrapperOps"
			, key2elem_format:Mapping[IKey, ElementFormat]
			):
		sf.__key2elem_format = key2elem_format
		super().__init__(wrapper_ops)
	@override
	def get_elem_format_at(sf, key:IKey)->ElementFormat:
		return sf.__key2elem_format[key]
#IContainerFormat = Union[UniqueValueTypeContainerFormat, KeyedValueTypeContainerFormat]
#ElementFormat = Union[ImmutableElementFormat, IContainerFormat]

ForwardPath = Union[None, Tuple[IKey, "ForwardPath"]]
BackwardPath = Union[None, Tuple["BackwardPath", IKey]]

#MayBackwardPathPtrKeyPair = Union[None, Tuple["BackwardPathPtr", IKey]]
#BackwardPathPtr = weakref uint
#BackwardPathPtr = NewType("BackwardPathPtr", object)
#  TypeError: cannot create weak reference to 'object' object
class BackwardPathPtr:pass


Time = NewType("Time", uint)
Length = NewType("Length", uint)
RecordStackTail = List[Tuple[Time, BackwardPathPtr, "IRollbackRecord", Dict[IKey, bool]]]
SavePoint = Tuple[Time, Length]
	#= (record_stack[-1][0], len(record_stack))







##################################
##################################
##################################
##################################

class IRollbackRecord(IImmutable):
	r"""
	#modify inplace
	#when del key, we should save the value in record to rollback, hence record cannot be IHashable
	#"""
	@abstractmethod
	def __repr__(sf):
		pass
	@abstractmethod
	def forward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		pass
	@abstractmethod
	def backward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		pass


class RollbackWrapper__hidden_ref(IImmutable):
	def __init__(sf
			, container_format:IContainerFormat
			, main_mngr:"IRollbackManager"
			, bpath_ptr:BackwardPathPtr
			):
		sf.__container_format = container_format
		sf.__main_mngr = main_mngr
		sf.__bpath_ptr = bpath_ptr
	@property
	def container_format(sf)->IContainerFormat:
		return sf.__container_format
	@property
	def main_mngr(sf)->"IRollbackManager":
		return sf.__main_mngr
	@property
	def bpath_ptr(sf)->BackwardPathPtr:
		return sf.__bpath_ptr


class IRollbackWrapper(ABC):
	r"""
	#vivi underlying container API
	.???wrapper_hidden_ref???::RollbackWrapper__hidden_ref
	#should avoid assign/setitem/setatttr unless element is IImmutableElement for record how to create the whole value
	#mk the element container from empty

	"""
class IRollbackWrapperOps(IImmutable):
	@abstractmethod
	def mk(sf
			, wrapper_hidden_ref:RollbackWrapper__hidden_ref
			)->IRollbackWrapper:
		pass
	@abstractmethod
	def _mk_raw_(sf)->IRollbackUnderlyingContainer:
		pass
	@abstractmethod
	def _sub_container_info_at_key_(sf
			, wrapper:IRollbackWrapper
			, key:IKey
			)->Tuple["IRollbackWrapperOps", RollbackWrapper__hidden_ref]:
		pass
	@abstractmethod
	def _wrap_(sf
			, wrapper_hidden_ref:RollbackWrapper__hidden_ref
			,underlying_container:IRollbackUnderlyingContainer
			)->IRollbackWrapper:
		pass
	@abstractmethod
	def to_std_key(sf
			, wrapper:IRollbackWrapper
			, key:IKey
			)->IKey:
		pass
	@abstractmethod
	def _to_std_key_(sf
			, underlying_container:IRollbackUnderlyingContainer
			, key:IKey
			)->IKey:
		pass
	@abstractmethod
	def _raw_at_(sf
			, underlying_container:IRollbackUnderlyingContainer
			, key:IKey
			)->IEitherEC:
		pass
	@abstractmethod
	def _at_(sf
			, wrapper:IRollbackWrapper
			, key:IKey
			)->IEitherNEOW:
		pass
	@abstractmethod
	def at(sf
			, wrapper:IRollbackWrapper
			, fpath:ForwardPath
			)->IEitherNEOW:
		pass
	@abstractmethod
	def get_wrapper_hidden_ref(sf
			, wrapper:IRollbackWrapper
			)->RollbackWrapper__hidden_ref:
		pass
	@abstractmethod
	def _get_underlying_container_(sf
			, wrapper:IRollbackWrapper
			)->IRollbackUnderlyingContainer:
		pass


class IRollbackManager(ABC):
	@abstractmethod
	def mk_main_wrapper(sf)->IRollbackWrapper:
		pass
	@abstractmethod
	def get_main_container_format(sf)->IContainerFormat:
		pass
	@abstractmethod
	def get_main_wrapper_ops(sf)->IRollbackWrapperOps:
		pass
	@abstractmethod
	def tell(sf)->SavePoint:
		pass
	@abstractmethod
	def rollback(sf
			, main_wrapper:IRollbackWrapper
			, save_point:SavePoint
			)->None:
		pass
	@abstractmethod
	def bpath_ptr2fpath(sf
			, bpath_ptr:BackwardPathPtr
			)->ForwardPath:
		pass
	@abstractmethod
	def get_root_bpath_ptr(sf)->BackwardPathPtr:
		pass
	@abstractmethod
	def get_bpath_ptr(sf
			, bpath_ptr:BackwardPathPtr
			,*
			, std_key:IKey
			)->BackwardPathPtr:
		pass
	@abstractmethod
	def record(sf
			, bpath_ptr:BackwardPathPtr
			, record:IRollbackRecord
			#, key2delset:Dict[IKey, bool]
			)->None:
		pass
	"""
	@abstractmethod
	def on_key_disappear(sf
			, bpath_ptr:BackwardPathPtr
			, key:IKey
			)->None:
		pass
	"""


@contextlib.contextmanager
def restoring(main_mngr:IRollbackManager, main_wrapper:IRollbackWrapper)->ContextManager[None]:
	save_point = main_mngr.tell()
	try:
		yield None
	finally:
		main_mngr.rollback(main_wrapper, save_point)
class RollbackManagerWith:
	def __init__(sf
			, main_mngr:IRollbackManager
			, main_wrapper:IRollbackWrapper
			):
		sf.main_mngr = main_mngr
		sf.main_wrapper = main_wrapper
	def restoring(sf)->ContextManager[None]:
		return restoring(sf.main_mngr, sf.main_wrapper)
	__call__ = restoring

def bpath2fpath(bpath:BackwardPath)->ForwardPath:
	fpath = None
	while bpath is not None:
		bpath, key = bpath
		fpath = key, fpath
	return fpath
class RollbackManager(IRollbackManager):
	def __init__(sf, main_container_format:IContainerFormat):
		#sf._main_wrapper_ops = main_wrapper_ops
		sf._main_container_format = main_container_format
		sf._record_stack = [(0,)]
		sf._time = 1

		root_bpath_ptr = sf.__new_bpath_ptr()
		sf._may_bpath_ptr_key_pair2ptr = WeakValueDictionary({None:root_bpath_ptr})
		sf._bpath_ptr2bpath = WeakKeyDictionary({root_bpath_ptr:None})
		sf._root_bpath_ptr = root_bpath_ptr
	def __new_bpath_ptr(sf)->BackwardPathPtr:
		return BackwardPathPtr()

	@override
	def mk_main_wrapper(sf)->IRollbackWrapper:
		main_mngr = sf
		main_container_format = main_mngr.get_main_container_format()
		root_bpath_ptr = main_mngr.get_root_bpath_ptr()
		wrapper_hidden_ref = RollbackWrapper__hidden_ref(main_container_format, main_mngr, root_bpath_ptr)
		main_wrapper_ops = main_mngr.get_main_wrapper_ops()
		main_wrapper = main_wrapper_ops.mk(wrapper_hidden_ref)
		return main_wrapper


	@override
	def get_main_container_format(sf)->IContainerFormat:
		return sf._main_container_format
	@override
	def get_main_wrapper_ops(sf)->IRollbackWrapperOps:
		return sf.get_main_container_format().get_wrapper_ops()
	@override
	def bpath_ptr2fpath(sf
			, bpath_ptr:BackwardPathPtr
			)->ForwardPath:
		bpath = sf._bpath_ptr2bpath[bpath_ptr]
		fpath = bpath2fpath(bpath)
		return fpath
		pass
	@override
	def get_root_bpath_ptr(sf)->BackwardPathPtr:
		return sf._root_bpath_ptr
		pass
	@override
	def get_bpath_ptr(sf
			, bpath_ptr:BackwardPathPtr
			,*
			, std_key:IKey
			)->BackwardPathPtr:
		key = std_key
		p = bpath_ptr, key
		cache = sf._may_bpath_ptr_key_pair2ptr
		m = cache.get(p)
		if m is None:
			child = sf.__new_bpath_ptr()
			cache[p] = child
			dd = sf._bpath_ptr2bpath
			dd[child] = (dd[bpath_ptr], key)
		else:
			child = m
		return child
		pass
	@override
	def tell(sf)->SavePoint:
		ls = sf._record_stack
		return (ls[-1][0], len(ls))
	@override
	def rollback(sf
			, main_wrapper:IRollbackWrapper
			, save_point:SavePoint
			)->None:
		t, n = save_point
		ls = sf._record_stack
		if not 0 < n <= len(ls) or t != ls[n-1][0]:
			raise Exception(f"bad save_point")
		ops = sf.get_main_wrapper_ops()
		wrapper = main_wrapper
		while n < len(ls):
			_, bpath_ptr, record, = ls.pop()
			fpath = sf.bpath_ptr2fpath(bpath_ptr)
			sub_ops, sub_wrapper = ops.at(wrapper, fpath)
			sub_container = sub_ops._get_underlying_container_(sub_wrapper)
			record.backward(sub_container)
		assert sf.tell() == save_point
		pass
	@override
	def record(sf
			, bpath_ptr:BackwardPathPtr
			, record:IRollbackRecord
			#, key2delset:Dict[IKey, bool]
			)->None:
		ls = sf._record_stack
		ls.append((sf._time, bpath_ptr, record))
		sf._time += 1
		pass
	"""
	@override
	def on_key_disappear(sf
			, bpath_ptr:BackwardPathPtr
			, key:IKey
			)->None:
		del sf._bpath_ptr2key2ptr[bpath_ptr][key]
		?????
	"""




#######################################
#######################################
#######################################

class RollbackRecordABC(IRollbackRecord):
	def __init__(sf, *args):
		sf.args = args
	@override
	def __repr__(sf):
		s = ", ".join(map(repr, sf.args))
		nm = type(sf).__qualname__
		return f"{nm}({s})"
	def __invert__(sf)->IRollbackRecord:
		return RollbackRecordABC__inv(sf)

class RollbackRecordABC__inv(RollbackRecordABC):
	def __init__(sf, record:IRollbackRecord):
		super().__init__(record)
	@override
	def forward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		[record] = sf.args
		return record.backward(container)
	@override
	def backward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		[record] = sf.args
		return record.forward(container)



class RollbackWrapperABC(IRollbackWrapper):
	def __init__(sf
			, wrapper_hidden_ref:RollbackWrapper__hidden_ref
			, underlying_container:IRollbackUnderlyingContainer
			):
		Globals.hidden_access__ref.set_hidden_state(sf, wrapper_hidden_ref)
		Globals.hidden_access__ctnr.set_hidden_state(sf, underlying_container)

class RollbackWrapperOpsABC(IRollbackWrapperOps):
	_rollback_wrapper_type_ = None
	_underlying_container_type_ = None
	@abstractmethod
	def _to_std_key_(sf
			, underlying_container:IRollbackUnderlyingContainer
			, key:IKey
			)->IKey:
		pass
	@abstractmethod
	def _raw_at_(sf
			, underlying_container:IRollbackUnderlyingContainer
			, key:IKey
			)->IEitherEC:
		pass

	def get_hidden_access(sf, wrapper):
		hidden_access = HasHiddenState__data.get_hidden_access__from_cls(type(wrapper))#type(wrapper).__hidden_access__
		return hidden_access
	@override
	def _mk_raw_(sf)->IRollbackUnderlyingContainer:
		Container = sf._underlying_container_type_
		raw = Container()
		return raw
	@override
	def mk(sf
			, wrapper_hidden_ref:RollbackWrapper__hidden_ref
			)->IRollbackWrapper:
		underlying_container = sf._mk_raw_()
		return sf._wrap_(wrapper_hidden_ref, underlying_container)
		pass
	@override
	def _wrap_(sf
			, wrapper_hidden_ref:RollbackWrapper__hidden_ref
			,underlying_container:IRollbackUnderlyingContainer
			)->IRollbackWrapper:
		assert sf is wrapper_hidden_ref.container_format.get_wrapper_ops()
		Wrapper = sf._rollback_wrapper_type_
		wrapper = Wrapper(wrapper_hidden_ref, underlying_container)
		return wrapper
		pass

	@override
	def to_std_key(sf
			, wrapper:IRollbackWrapper
			, key:IKey
			###wrapper_hidden_ref
			)->IKey:
		underlying_container = sf._get_underlying_container_(wrapper)
		std_key = sf._to_std_key_(underlying_container, key)
		return std_key
		pass
	@override
	def _at_(sf
			, wrapper:IRollbackWrapper
			, key:IKey
			)->IEitherNEOW:
		r = sf._info_at_key_(wrapper, key)
		underlying_container = r[0]
		elem_or_container = sf._raw_at_(underlying_container, key)
		if len(r) == 1:
			raw_elem = elem_or_container
			return None, raw_elem

		sub_container = elem_or_container
		[underlying_container, container_format, sub_ops, sub_hidden_ref] = r
		sub_wrapper = sub_ops._wrap_(sub_hidden_ref, sub_container)
		return sub_ops, sub_wrapper
	
	def _info_at_key_(sf
			, wrapper:IRollbackWrapper
			, key:IKey
			)->Union[Tuple[IRollbackUnderlyingContainer], Tuple[IRollbackUnderlyingContainer, IContainerFormat, IRollbackWrapperOps, RollbackWrapper__hidden_ref]]:
		#value of key may not exist yet!
		#->(underlying_container,)
		#->(underlying_container, container_format, sub_ops, sub_hidden_ref)
		underlying_container = sf._get_underlying_container_(wrapper)
		wrapper_hidden_ref = sf.get_wrapper_hidden_ref(wrapper)
		ops = sf

		###wrapper_hidden_ref, ops, underlying_container, key
		container_format = wrapper_hidden_ref.container_format
		elem_format = container_format.get_elem_format_at(key)
		if elem_format is theImmutableElementFormat:
			return (underlying_container,)

		main_mngr = wrapper_hidden_ref.main_mngr
		bpath_ptr = wrapper_hidden_ref.bpath_ptr

		std_key = ops._to_std_key_(underlying_container, key)
		sub_bpath_ptr = main_mngr.get_bpath_ptr(bpath_ptr, std_key=std_key)
		sub_ops = elem_format.get_wrapper_ops()
		sub_hidden_ref = RollbackWrapper__hidden_ref(elem_format, main_mngr, sub_bpath_ptr)
		###sub_ops, sub_hidden_ref
		return underlying_container, container_format, sub_ops, sub_hidden_ref
	@override
	def _sub_container_info_at_key_(sf
			, wrapper:IRollbackWrapper
			, key:IKey
			)->Tuple[IRollbackWrapperOps, RollbackWrapper__hidden_ref]:
		wrapper_ops = sf
		r = wrapper_ops._info_at_key_(wrapper, key)
		if len(r) == 1:
			raise TypeError("elem_format is not IContainerFormat")
		[underlying_container, container_format, sub_ops, sub_hidden_ref] = r
		return (sub_ops, sub_hidden_ref)




	@override
	def at(sf
			, wrapper:IRollbackWrapper
			, fpath:ForwardPath
			)->IEitherNEOW:
		may_ops = sf
		elem_or_wrapper = wrapper
		while fpath is not None:
			key, fpath = fpath
			ops = may_ops
			wrapper = elem_or_wrapper
			may_ops, elem_or_wrapper = ops._at_(wrapper, key)
		return may_ops, elem_or_wrapper
		pass
	@override
	def get_wrapper_hidden_ref(sf
			, wrapper:IRollbackWrapper
			)->RollbackWrapper__hidden_ref:
		wrapper_hidden_ref = Globals.hidden_access__ref.get_hidden_state(wrapper)
		return wrapper_hidden_ref
		pass
	@override
	def _get_underlying_container_(sf
			, wrapper:IRollbackWrapper
			)->IRollbackUnderlyingContainer:
		underlying_container = Globals.hidden_access__ctnr.get_hidden_state(wrapper)
		return underlying_container
		pass



########################################
########################################
########################################
class RollbackWrapperOps__list(RollbackWrapperOpsABC):
	#_rollback_wrapper_type_ = RollbackWrapper__listE/C
	_underlying_container_type_ = list
	def __init__(sf
			, is_element_mutable:bool
			):
		sf.__wt = RollbackWrapper__listE if not is_element_mutable else RollbackWrapper__listC
	@property
	def _rollback_wrapper_type_(sf)->type:
		return sf.__wt

	@override
	def _to_std_key_(sf
			, underlying_container:IRollbackUnderlyingContainer
			, key:IKey
			)->IKey:
		#not slice
		if not isinstance(key, int):raise TypeError
		n = len(underlying_container)
		if -n <= key < 0:
			key += n
		return key#err_key remain err

		pass
	@override
	def _raw_at_(sf
			, underlying_container:IRollbackUnderlyingContainer
			, key:IKey
			)->IEitherEC:
		#not slice
		if not isinstance(key, int):raise TypeError
		raw = underlying_container[key]
		return raw
		pass


r"""

class RollbackWrapper__listR(RollbackWrapperABC):
	#readonly except get element
	def __contains__(sf, x:IImmutableElement)->bool:
	def __iter__(sf)->Iterator[IImmutableElement]:
	def __reversed__(sf)->Iterator[IImmutableElement]:
	def __len__(sf)->Length:
	def __bool__(sf)->bool:
	def __repr__(sf)->str:
	def __str__(sf)->str:
	def index(sf, x:IImmutableElement)->uint:
	def count(sf, x:IImmutableElement)->uint:

class RollbackWrapper__listE(RollbackWrapper__listR):
	#update with immutable element; get element
	def extend(sf, it:Iterable[IImmutableElement]):
	def append(sf, x:IImmutableElement):
	def pop(sf)->IImmutableElement:
	def __setitem__(sf, i:int, x:IImmutableElement):
	@overload
	def __getitem__(sf, i:int)->IImmutableElement:
	@overload
	def __getitem__(sf, sl:slice)->List[IImmutableElement]:
class RollbackWrapper__listC(RollbackWrapper__listR):
	#sub_container new/del key; get element
	def append_new(sf)->None:
	def del_last(sf)->None:
	def __getitem__(sf, i:int)->IRollbackWrapper:
#"""










class Globals:
	#def __new__(cls): return cls
	hidden_access__ref = HiddenAccess(RollbackWrapper__hidden_ref)
	hidden_access__ctnr = HiddenAccess(IRollbackUnderlyingContainer)
	@classmethod
	def wrapper_abc_get_underlying_container(cls
			, wrapper:RollbackWrapperABC
			)->IRollbackUnderlyingContainer:
		underlying_container = cls.hidden_access__ctnr.get_hidden_state(wrapper)
		xs = underlying_container
		return xs
	@classmethod
	def wrapper_abc_get_wrapper_hidden_ref(cls
			, wrapper:RollbackWrapperABC
			)->RollbackWrapper__hidden_ref:
		wrapper_hidden_ref = cls.hidden_access__ref.get_hidden_state(wrapper)
		return wrapper_hidden_ref

	@classmethod
	def wrapper_abc_get_mngr_ptr_xs(cls
			, wrapper:RollbackWrapperABC
			)->Tuple[IRollbackManager, BackwardPathPtr, IRollbackUnderlyingContainer]:
		hidden_ref = cls.wrapper_abc_get_wrapper_hidden_ref(wrapper)
		xs = cls.wrapper_abc_get_underlying_container(wrapper)
		main_mngr = hidden_ref.main_mngr
		bpath_ptr = hidden_ref.bpath_ptr
		return main_mngr, bpath_ptr, xs

	@classmethod
	def wrapper_abc_forward(cls
			, wrapper:RollbackWrapperABC
			, record:IRollbackRecord
			)->UpdateResult:
		main_mngr, bpath_ptr, xs = cls.wrapper_abc_get_mngr_ptr_xs(wrapper)
		r = record.forward(xs)
		try:
			main_mngr.record(bpath_ptr, record)
		except:
			record.backward(xs)
			raise
		return r

class RollbackWrapperABC__R(RollbackWrapperABC):
	#readonly except get element
	def __iter__(sf)->Iterator[IImmutableElement]:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return iter(xs)
	def __reversed__(sf)->Iterator[IImmutableElement]:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return reversed(xs)
	def __len__(sf)->Length:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return len(xs)
	def __bool__(sf)->bool:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return bool(xs)
	def __repr__(sf)->str:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return repr(xs)
	def __str__(sf)->str:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return str(xs)

class RollbackWrapperABC__R_key(RollbackWrapperABC__R):
	def __contains__(sf, k:IKey)->bool:
		k2x = Globals.wrapper_abc_get_underlying_container(sf)
		return k in k2x
class RollbackWrapperABC__R_value(RollbackWrapperABC__R):
	def __contains__(sf, x:IImmutableElement)->bool:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return x in xs
class RollbackWrapper__listR(RollbackWrapperABC__R_value):
	#readonly except get element
	def index(sf, x:IImmutableElement)->uint:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return xs.index(x)
	def count(sf, x:IImmutableElement)->uint:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return xs.count(x)

class RollbackRecord__listE__extend(RollbackRecordABC):
	def __init__(sf, ls:Tuple[IImmutableElement]):
		assert type(ls) is tuple
		super().__init__(ls)
	@override
	def forward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		return container.extend(*sf.args)
	@override
	def backward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		[ls] = sf.args
		assert not ls or ls[-1] is container[-1]
		del container[len(container)-len(ls):]
		return


class RollbackRecord__listE__append(RollbackRecordABC):
	def __init__(sf, x:IImmutableElement):
		super().__init__(x)
	@override
	def forward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		return container.append(*sf.args)
	@override
	def backward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		x = container.pop()
		assert x is sf.args[0]
		return x
class RollbackRecord__listE__setitem(RollbackRecordABC):
	def __init__(sf, i:int, old:IImmutableElement, new:IImmutableElement):
		if not isinstance(i, int):
			raise TypeError(f"index must be int not {type(i)}")
		super().__init__(i, old, new)
	@override
	def forward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		i, old, new = sf.args
		container[i] = new
		return
	@override
	def backward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		i, old, new = sf.args
		assert container[i] is new
		container[i] = old
		return




class RollbackWrapper__listE(RollbackWrapper__listR):
	#update with immutable element; get element
	def extend(sf, it:Iterable[IImmutableElement]):
		ls = (*it,); del it
		record = RollbackRecord__listE__extend(ls)
		return Globals.wrapper_abc_forward(sf, record)
	def append(sf, x:IImmutableElement):
		record = RollbackRecord__listE__append(x)
		return Globals.wrapper_abc_forward(sf, record)
	def pop(sf)->IImmutableElement:
		x = sf[-1]
		record = ~RollbackRecord__listE__append(x)
		return Globals.wrapper_abc_forward(sf, record)
	def __setitem__(sf, i:int, x:IImmutableElement):
		j = type(i).__index__(i)
		if not isinstance(j, int):
			raise TypeError(f"index must be int not {type(i)}")
		old = sf[j]
		record = RollbackRecord__listE__setitem(j, old, x)
		return Globals.wrapper_abc_forward(sf, record)
	@overload
	def __getitem__(sf, i:int)->IImmutableElement:
		...
	@overload
	def __getitem__(sf, sl:slice)->List[IImmutableElement]:
		...
	def __getitem__(sf, i_or_sl):
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		return xs[i_or_sl]



class RollbackRecord__listC__del_last(RollbackRecordABC):
	def __init__(sf, sub_container:IRollbackUnderlyingContainer):
		super().__init__(sub_container)
	@override
	def forward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		[sub_container] = sf.args
		assert sub_container is container[-1]
		container.pop()
		return
	@override
	def backward(sf, container:IRollbackUnderlyingContainer)->UpdateResult:
		[sub_container] = sf.args
		container.append(sub_container)
		return


class RollbackWrapper__listC(RollbackWrapper__listR):
	#sub_container new/del key; get element
	def append_new(sf)->None:
		wrapper = sf
		key = len(sf)
		wrapper_hidden_ref = Globals.wrapper_abc_get_wrapper_hidden_ref(wrapper)
		container_format = wrapper_hidden_ref.container_format
		elem_format = container_format.get_elem_format_at(key)
		####
		sub_ops = elem_format.get_wrapper_ops()
		x = sub_ops._mk_raw_()
		record = ~RollbackRecord__listC__del_last(x)
		return Globals.wrapper_abc_forward(sf, record)
	def del_last(sf)->None:
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		x = xs[-1]
		record = RollbackRecord__listC__del_last(x)
		return Globals.wrapper_abc_forward(sf, record)
	def __getitem__(sf, i:int)->IRollbackWrapper:
		j = type(i).__index__(i)
		if not isinstance(j, int):
			raise TypeError(f"index must be int not {type(i)}")
		xs = Globals.wrapper_abc_get_underlying_container(sf)
		x = xs[j]
		###
		wrapper = sf
		key = len(sf)
		#wrapper_ops = list_opsC
		wrapper_hidden_ref = Globals.wrapper_abc_get_wrapper_hidden_ref(wrapper)
		container_format = wrapper_hidden_ref.container_format
		wrapper_ops = container_format.get_wrapper_ops()
		####
		[sub_ops, sub_hidden_ref] = wrapper_ops._sub_container_info_at_key_(wrapper, key)
		sub_wrapper = sub_ops._wrap_(sub_hidden_ref, x)
		return sub_wrapper



list_opsE = RollbackWrapperOps__listE = RollbackWrapperOps__list(False)
list_opsC = RollbackWrapperOps__listC = RollbackWrapperOps__list(True)







def _t__list():
	list_opsE
	list_formatE = UniqueValueTypeContainerFormat(list_opsE, theImmutableElementFormat)
	main_mngr = RollbackManager(list_formatE)
	list_wrapper = main_mngr.mk_main_wrapper()
	w = RollbackManagerWith(main_mngr, list_wrapper)

	save0 = main_mngr.tell()
	print(list_wrapper)
	print(bool(list_wrapper))
	list_wrapper.append(7)
	save7 = main_mngr.tell()
	print(list_wrapper)
	assert 7 == list_wrapper.pop()
	save_ = main_mngr.tell()
	print(list_wrapper)
	list_wrapper.extend([5,4])
	save54 = main_mngr.tell()
	print(list_wrapper)
	list_wrapper.extend([])
	save54_ = main_mngr.tell()
	print(list_wrapper)
	list_wrapper[-2] = 0
	save04 = main_mngr.tell()
	print(list_wrapper)
	print(1 in list_wrapper)
	print(0 in list_wrapper)
	print(len(list_wrapper))
	print(list(list_wrapper))
	print(list(reversed(list_wrapper)))
	print(repr(list_wrapper))
	print(list_wrapper[1])
	print(list_wrapper[::-1])
	print(list_wrapper.index(4))
	print(list_wrapper.count(4))
	with w():
		print(list_wrapper)
		list_wrapper.extend([8,9,3])
		print(list_wrapper)
	print(list_wrapper)


	main_mngr.rollback(list_wrapper, save54_)
	print(list_wrapper)
	main_mngr.rollback(list_wrapper, save54)
	print(list_wrapper)
	main_mngr.rollback(list_wrapper, save_)
	print(list_wrapper)
	main_mngr.rollback(list_wrapper, save7)
	print(list_wrapper)
	main_mngr.rollback(list_wrapper, save0)
	print(list_wrapper)
_t__list()




