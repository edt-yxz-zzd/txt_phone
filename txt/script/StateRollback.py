r"""
usage:
	**big picture**
		mngr = StateRollback__mngr()
		def frecur(mngr...):
			save = mngr.tell()
			try:
				for ...:
					mngr.rollback(save)
					frecur(mngr...)
			finally:
				mngr.rollback(save)
	**new/overwrite var**
		mngr[nm] = ops, st
		mngr.set.nm = ops, st
	**access var**
		r = mngr.get.nm.f(...)
	**update var**
		r = mngr.update.nm.f(...)
	**mk ops::IStateOps**
		ls_ops = StateOps__list()


#####################################
#####################################
#####################################
state rollback
	.ls = [(0,)]
	.time = 1
	st_mgr.st_nm = (ops, st)
		.d["st_nm"].append((ops, st))
		.ls.append((.time, "st_nm"))
		.time++
	st_mgr.st_nm.f(*xs)
		dat = ops.update("f", st, *xs)
		.ls.append((.time, "st_nm", "f", dat))
		.time++
	st_mgr.___get___("st_nm")
		-> st
	st_mgr.___tell___()
		-> (time, where)
		#bug: (.time, len(.ls))
		(.ls[-1][0], len(.ls))
	st_mgr.___rollback___((time, where))
		if len(.ls)==where:
			ret
		if time==.ls[where-1][0]:
			while len(.ls)>where:
				case .ls.pop() of:
				_, st_nm -> .d["st_nm"].pop()
				_, st_nm, f, dat -> ops.undo("f", st, dat)


#####################################
#####################################
#####################################

>>> mngr = StateRollback__mngr()
>>> save_ = mngr.tell()
>>> mngr.rollback(save_)

>>> g = mngr.get
>>> v = mngr.var
>>> u = mngr.update
>>> s = mngr.set

>>> save_0 = mngr.tell()
>>> ls_ops = StateOps__list()
>>> ls = [0,3,9]
>>> s.ls = ls_ops, ls
>>> save039 = mngr.tell()
>>> del s.ls
>>> save_1 = mngr.tell()
>>> g.ls
Traceback (most recent call last):
	...
AttributeError: ls
>>> mngr.rollback(save039)
>>> v.ls.__class__
<class 'list'>



>>> len(g.ls)
3
>>> bool(g.ls)
True
>>> 9 in g.ls
True
>>> 55 in g.ls
False
>>> g.ls[-2]
3
>>> g.ls[:2]
[0, 3]
>>> str(g.ls)
'[0, 3, 9]'
>>> repr(g.ls)
'[0, 3, 9]'

##
>>> g.ls
[0, 3, 9]
>>> save039 = mngr.tell()
>>> u.ls.pop()
9
>>> len(g.ls)
2
>>> g.ls
[0, 3]
>>> save03 = mngr.tell()
>>> u.ls.append(7)
>>> g.ls
[0, 3, 7]
>>> save037 = mngr.tell()
>>> u.ls.extend([1, 2])
>>> g.ls
[0, 3, 7, 1, 2]
>>> save03712 = mngr.tell()
>>> u.ls[-1] = 5
>>> g.ls
[0, 3, 7, 1, 5]
>>> save03715 = mngr.tell()
>>> mngr.rollback(save03715)
>>> g.ls
[0, 3, 7, 1, 5]
>>> mngr.rollback(save03712)
>>> g.ls
[0, 3, 7, 1, 2]
>>> mngr.rollback(save037)
>>> g.ls
[0, 3, 7]
>>> mngr.rollback(save03)
>>> g.ls
[0, 3]
>>> mngr.rollback(save039)
>>> g.ls
[0, 3, 9]







TODO
"""


__all__ = """
	""".split()

from collections import defaultdict
from abc import ABC, abstractmethod
from functools import partial
import sys


def print_err(*x, file=sys.stderr, **kw):
	print(*x, file=file, **kw)

class StateOpsExc(Exception): pass
class StateOpsCaseExc(StateOpsExc): pass
class IStateOps(ABC):
	@abstractmethod
	def _is_good_f4update_(sf, f, st):
		pass
	@abstractmethod
	def _is_good_f4get_(sf, f, st):
		pass
	@abstractmethod
	def _is_good_f4var_(sf, f, st):
		pass
	@abstractmethod
	def _undo_impl_(sf, f, st, dat):
		#->None
		pass
	@abstractmethod
	def _update_impl_(sf, f, st, *args, **kw):
		#->(result, dat)
		pass
	@abstractmethod
	def _get_impl_(sf, f, st, *args, **kw):
		#->result
		pass
	@abstractmethod
	def _var_impl_(sf, f, st):
		#->result
		pass

	def _undo_(sf, f, st, dat):
		#->None
		if not sf._is_good_f4update_(f, st):
			raise StateOpsCaseExc(f"{type(sf)}._undo_: f={f!r}")
		r = sf._undo_impl_(f, st, dat)
		if r is not None:
			raise Exception(f"not {type(sf)}._undo_impl_({f!r}, ...) -> None")
		return
		pass
	def _update_(sf, f, st, *args, **kw):
		#->(result, dat)
		if not sf._is_good_f4update_(f, st):
			raise StateOpsCaseExc(f"{type(sf)}._update_: f={f!r}")
		r_dat = sf._update_impl_(f, st, *args, **kw)
		try:
			r, dat = r_dat
		except Exception:
			raise Exception(f"not {type(sf)}._update_impl_({f!r}, ...) -> (r, dat)")
		return r, dat
		pass
	def _get_(sf, f, st, *args, **kw):
		#->result
		if not sf._is_good_f4get_(f, st):
			raise StateOpsCaseExc(f"{type(sf)}._get_: f={f!r}")
		r = sf._get_impl_(f, st, *args, **kw)
		return r
		pass
	def _var_(sf, f, st):
		#->result
		if not sf._is_good_f4var_(f, st):
			raise StateOpsCaseExc(f"{type(sf)}._var_: f={f!r}")
		r = sf._var_impl_(f, st)
		return r
		pass

class StateRollback__f_nm__mcls(type):
	def __getattribute__(sf, nm):
		0;print_err(nm)
		return super().__getattribute__(nm)
StateRollback__f_nm__mcls = type
class StateRollback__f_nm(
		metaclass=StateRollback__f_nm__mcls
		):
	MNGR_NM = 3
	_spec_nms_ = """
		__setattr__
		__delattr__
		__setitem__
		__delitem__
		__getitem__
		__len__
		__contains__
		__bool__
		__str__
		__repr__
		__call__
		""".split()
		#no: __hash__
	def ___get___(sf, nm):
		return object.__getattribute__(sf, nm)
	def ___mk___(sf, direct, depth, mngr_f, *nms):
		return type(sf)(direct, depth, mngr_f, *nms)
	def __init__(sf, direct, depth, mngr_f, *nms):
		assert depth >= 1
		assert callable(mngr_f)
		#sf.mngr = mngr
		cls = __class__
		d = cls.___get___(sf, "__dict__")
		d[cls.MNGR_NM] = direct, depth, mngr_f, nms
	def __getattribute__(sf, nm):
		cls = __class__
		d = cls.___get___(sf, "__dict__")
		direct, depth, mngr_f, nms = d[cls.MNGR_NM]
		depth -= 1
		if depth:
			return cls.___mk___(sf, direct, depth, mngr_f, *nms, nm)
		if direct:
			return mngr_f(*nms, nm)
		else:
			return partial(mngr_f, *nms, nm)

class _spec_f_:
	def __init__(sf, nm):
		sf.__nm = nm
	def __call__(__sf, __obj, *args, **kw):
		f = getattr(__obj, __sf.__nm)
		return f(*args, **kw)
		0;print_err(__sf.__nm)
		0;print_err(__obj)
		0;print_err(type(__obj))
		f = getattr(__obj, __sf.__nm)
		0;print_err(f)
		0;print_err(type(f))
		return 0
		return f(*args, **kw)
	def __get__(sf, instance, owner=None):
		if owner is None:
			return sf
		return partial(sf, instance)
def _f():
	cls = StateRollback__f_nm
	for nm in cls._spec_nms_:
		setattr(cls, nm, _spec_f_(nm))
_f(); del _f

class StateRollback__mngr:
	@property
	def update(sf):
		return StateRollback__f_nm(False, 2, sf.fupdate)
	@property
	def get(sf):
		return StateRollback__f_nm(False, 2, sf.fget)
	@property
	def set(sf):
		return StateRollback__f_nm(False, 1, sf.fset)
	@property
	def var(sf):
		return StateRollback__f_nm(True, 2, sf.fvar)
	def __init__(sf):
		sf.__d = {}#defaultdict(list)
			# {nm:[(ops, st)|None]}
		sf.__ls = [(0,)]
			#len>0
			#ls[1:] :: [(t, nm)|(t,nm,f,dat)]
		sf.__t = 1
			#inc only

	def tell(sf):
		ls = sf.__ls
		n = len(ls)
		position = ls[n-1][0], n
		return position

	def rollback(sf, position):
		t, n = position
		ls = sf.__ls
		assert ls
		if not 0 < n <= len(ls) or ls[n-1][0] != t:
			raise Exception("bad position")
		while n < len(ls):
			tp = ls.pop()
			d = sf.__d
			nm = tp[1]
			q = d[nm]
			if len(tp) == 2:
				_, nm = tp
				#undo: new/overwrite/del
				q.pop()
				if not q:
					del d[nm]
			else:
				_, nm, f, dat = tp
				#undo: update
				ops, st = q[-1]
				ops._undo_(f, st, dat)
		assert ls
		assert n == len(ls)
		assert ls[-1][0] == t

	def __append(sf, *args):
		sf.__ls.append((sf.__t, *args))
		sf.__t += 1
	def __get_nm(sf, nm):
		#KeyError
		#no IndexError
		vs = sf.__d[nm] #KeyError
		assert vs
		x = vs[-1]
		if x is None:
			raise KeyError(nm)
		return x


	def __setitem__(sf, nm, x):
		ops, st = x
		sf.assign(nm, ops, st)
	def __delitem__(sf, nm):
		sf.delete(nm)
	def delete(sf, nm):
		d = sf.__d
		sf.__get_nm(nm)#KeyError
		vs = d[nm]
		assert vs
		assert vs[-1] is not None
		vs.append(None)
		sf.__append(nm)
	def assign(sf, nm, ops, st):
		assert isinstance(ops, IStateOps)
		sf.__d.setdefault(nm, []).append((ops, st))
		sf.__append(nm)
	def fupdate(sf, nm, f, *args, **kw):
		try:
			ops, st = sf.__get_nm(nm)
				#KeyError
		except KeyError:
			raise AttributeError(nm)
		try:
			r, dat = ops._update_(f, st, *args, **kw)
				#StateOpsCaseExc
		except StateOpsCaseExc:
			raise AttributeError(f".{nm}.{f}")
		sf.__append(nm, f, dat)
		return r
	def fget(sf, nm, f, *args, **kw):
		try:
			ops, st = sf.__get_nm(nm)
				#KeyError
		except KeyError:
			raise AttributeError(nm)
		try:
			r = ops._get_(f, st, *args, **kw)
				#StateOpsCaseExc
		except StateOpsCaseExc:
			raise AttributeError(f".{nm}.{f}")
		return r
	def fvar(sf, nm, f):
		try:
			ops, st = sf.__get_nm(nm)
				#KeyError
		except KeyError:
			raise AttributeError(nm)
		try:
			r = ops._var_(f, st)
				#StateOpsCaseExc
		except StateOpsCaseExc:
			raise AttributeError(f".{nm}.{f}")
		return r

	#bug: def fset(sf, nm, f, *args, **kw):
	def fset(sf, f, nm, *args, **kw):
		#0;print_err(f"{f} {nm} {sf.__d}")
		if f == "__setattr__":
			sf.__setitem__(nm, *args, **kw)
		elif f == "__delattr__":
			try:
				sf.__delitem__(nm, *args, **kw)
			except KeyError:
				raise AttributeError(nm)
		else:
			raise AttributeError(f"{sf}.set.{nm}.{f}")






#########
def override(f):
	return f
class IStateUpdate(ABC):
	@abstractmethod
	def do(sf, st, *args, **kw):
		#->(result, dat)
		pass
	@abstractmethod
	def undo(sf, st, dat):
		#->None
		pass




class StateOpsABC__static_test(IStateOps):
	___f2update___ = None
		#{attr:IStateUpdate}
	___fs4get___ = None
		#{attr}
	___fs4var___ = None
		#{attr}
	#"""
	def __init_subclass__(cls, **kwargs):
		super().__init_subclass__(**kwargs)
		if cls is __class__:
			return
		nms0 = {*cls.___f2update___}
		nms1 = {*cls.___fs4get___}
		nms2 = {*cls.___fs4var___}
		s = nms0&(nms1|nms2)
		s |= nms1&nms2
		if s:
			raise Exception(f"StateOpsABC__static_test: dup attrs={s}")
		#for nm in nms0|nms1|:
		#	setattr(cls, nm, _spec_f_(nm))
	#"""

	@override
	def _is_good_f4update_(sf, f, st):
		return f in sf.___f2update___
		pass
	@override
	def _is_good_f4get_(sf, f, st):
		return f in sf.___fs4get___
		pass
	@override
	def _is_good_f4var_(sf, f, st):
		return f in sf.___fs4var___
		pass
	@override
	def _get_impl_(sf, f, st, *args, **kw):
		#->result
		try:
			ff = getattr(st, f)
		except AttributeError:
			if f == "__bool__":
				h = getattr(st, "__len__")
				ff = lambda: bool(h())
			elif f == "__str__":
				ff = getattr(st, "__repr__")
			else:
				raise
		return ff(*args, **kw)
	@override
	def _var_impl_(sf, f, st):
		#->result
		return getattr(st, f)
	@override
	def _undo_impl_(sf, f, st, dat):
		#->None
		u = sf.___f2update___[f]
		return u.undo(st, dat)
	@override
	def _update_impl_(sf, f, st, *args, **kw):
		#->(result, dat)
		u = sf.___f2update___[f]
		return u.do(st, *args, **kw)

class StateUpdate__list_append(IStateUpdate):
	@override
	def do(sf, ls, x):
		#->(result, dat)
		r = ls.append(x)
		dat = 1
		return r, dat
		pass
	@override
	def undo(sf, ls, _):
		#->None
		ls.pop()
		pass
class StateUpdate__list_pop(IStateUpdate):
	@override
	def do(sf, ls):
		#->(result, dat)
		r = ls.pop()
		dat = r
		return r, dat
		pass
	@override
	def undo(sf, ls, x):
		#->None
		ls.append(x)
		pass
class StateUpdate__list_extend(IStateUpdate):
	@override
	def do(sf, ls, it):
		#->(result, dat)
		dat = len(ls)
		r = ls.extend(it)
		return r, dat
		pass
	@override
	def undo(sf, ls, end):
		#->None
		del ls[end:]
		pass

class StateUpdate__list_setitem(IStateUpdate):
	@override
	def do(sf, ls, i, new):
		#->(result, dat)
		assert isinstance(i, int)
		try:
			old = ls[i]
		except Exception:
			#ls[i] = new
			raise
		ls[i] = new
		r = None
		dat = i, old
		return r, dat
		pass
	@override
	def undo(sf, ls, dat):
		#->None
		i, old = dat
		assert isinstance(i, int)
		ls[i] = old
		pass





class StateOps__list(StateOpsABC__static_test):
	"""
	f: dat
	append: 1
	pop: old
	extend: old_sz
	__setitem__: (i,old)
	"""

	___f2update___ = dict(
			append=StateUpdate__list_append()
			,pop=StateUpdate__list_pop()
			,extend=StateUpdate__list_extend()
			,__setitem__=StateUpdate__list_setitem()
			)

	___fs4get___ = set("""
		__getitem__
		__len__
		__bool__
		__contains__
		__str__
		__repr__
		""".split())
	___fs4var___ = set("""
		__class__
		""".split())









if __name__ == "__main__":
	import doctest
	doctest.testmod()
	#doctest: +ELLIPSIS
	#doctest: +NORMALIZE_WHITESPACE
	#doctest: +IGNORE_EXCEPTION_DETAIL
	#Traceback (most recent call last):



