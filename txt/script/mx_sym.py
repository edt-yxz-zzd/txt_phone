# mx sym op for det(mx) where tp(mx)=-mx
# find mx where tp(mx)=-mx, det(mx)!=0

import functools #.total_ordering
from itertools import product as pdt
import operator as opss
from fractions import Fraction
tpl = tuple
rg = range
pr=print
def sw(a):
	pr(a, end='')
err = Exception
tt, ff = True, False
def fold1(op, xs):
	it = iter(xs)
	for h in  it: break
	else: raise err
	return fold(op, h, it)
def fold(op, h, xs):
	for x in xs:
		h = op(h, x)
	return h
def fall(n, e):
	return fold(opss.mul, 1, rg(n, n-e, -1))
def fff(n):
	return fall(n, n)
def choose(n, e):
	return fall(n, e)//fff(e)
def id(x):
	return x
def rrr():
	raise ee

def fst(kv):
	return kv[0]


def sgn(x):
	return -1 if x<0 else (
		1 if x>0 else 0)
def mx_mul(a, b):
	try:
		return __mx_mul(a, b)
	except:
		pr(a)
		pr(b)
		raise

def __mx_mul(a, b):
	assert len(a[0]) == len(b)
	def idx(ls, i):
		pr(ls)
		pr(i)
		return ls[i]
		
	return tpl(
		tpl(
			dotp(row, tpl(r[icol] for r in b))
			for icol in rg(len(b[0]))
		)
		for row in a
		)
def vadd(v, u):
	try:
		it = iter(v)
	except:
		return v+u
	return tuple(map(vadd, v, u))


def ntime(n, v):
	try:
		it = iter(v)
	except:
		return n*v
	return tuple(ntime(n, u) for u in it)

def dotp(v, u, *, add=opss.add, mul=opss.mul):
	return fold1(add, map(mul, v, u))


def col2mx(v):
	return tpl((x,) for x in v)
def col2vec(col_mx):
	return tpl(x for [x] in col_mx)
def mx_mul_col(rot_mx, v):
	mv = col2mx(v)
	col = mx_mul(rot_mx, mv)
	return col2vec(col)


def mx_transpose(mx, f=id):
	rr = len(mx)
	cc = len(mx[0])
	return tpl(
		tpl(f(mx[i][j])
			for i in rg(rr)
			)
		for j in rg(cc)
		)
tp = mx_transpose
def mx_fmap(f, mx):
	rr = len(mx)
	cc = len(mx[0])
	return tpl(
		tpl(f(mx[i][j])
			for j in rg(cc)
			)
		for i in rg(rr)
		)


class poly:
	def _expand_(sf):
		rrr()
	def _struct_eq_(sf, ot):
		rrr()
	def _struct_key_(sf):
		rrr()
	def struct_key(sf, ot):
		return (type(sf).__qualname__, sf._struct_key_())
	def struct_eq(sf, ot):
		return type(sf) is type(ot) and sf._struct_eq_(ot)
	def expand(sf):
		return sf._expand_().collect()
	def __pos__(sf):
		return sf
	def __neg__(sf):
		return p_neg(sf)
	def __add__(sf, ot):
		return p_add(sf, ot)
	def __sub__(sf, ot):
		return sf + -ot
	def __mul__(sf, ot):
		return p_mul(sf, ot)
	def __pow__(sf, ot):
		return p_pow(sf, ot)

class p_uni(poly):
	def _struct_key_(sf):
		return (sf.rhs.struct_key(),)
	def _struct_eq_(sf, ot):
		return sf.rhs.struct_eq(ot.rhs)
	def __init__(sf, rhs):
		sf.__rhs =rhs
	@property
	def rhs(sf):
		return sf.__rhs
class p_bin(poly):
	def _struct_key_(sf):
		return (
			sf.lhs.struct_key()
			,sf.rhs.struct_key()
			)
	def _struct_eq_(sf, ot):
		return (
			sf.lhs.struct_eq(ot.lhs)
			and
			sf.rhs.struct_eq(ot.rhs)
			)
	def __init__(sf, lhs, rhs):
		sf.__lhs = lhs
		sf.__rhs =rhs
	@property
	def lhs(sf):
		return sf.__lhs
	@property
	def rhs(sf):
		return sf.__rhs
class p_many0(poly):
	@classmethod
	def get_default_const(cls):
		rrr()
	@classmethod
	def collect_const(cls, acc, base, coeff):
		rrr()
	@classmethod
	def is_halt_const(cls, acc):
		rrr()
	
	def _struct_key_(sf):
		return tpl(
			(x.struct_key(), a.struct_key())
			for x,a in sf.args
			)
	def _struct_eq_(sf, ot):
		return (
			len(sf.args) == len(ot.args)
			and
			all(
				a.struct_eq(b)
				and x.struct_eq(y)
				for (x,a),(y,b) in zip(sf.args, ot.args)
				)
			)
	def collect(sf):
		it = zip(sf._struct_key_(), sf.args)
		ps = sorted(it, key=fst)
		t = type(sf)
		acc = t.get_default_const()
		iacc = t.collect_const
		pre_k = None
		pre_cff = None
		pre_base = None
		ls = []
		for (k,_), (base, coeff) in ps:
			if isinstance(base, frac):
				acc = iacc(acc, base, coeff)
			elif pre_k == k:
				pre_cff = pre_cff.fr_add(coeff)
			else:
				ls.append((pre_cff, pre_base))
				pre_cff = coeff
				pre_base = base
		else:
			ls.append((pre_cff, pre_base))
			ls[0] = (acc, frac(1))
			if t.is_halt_const(acc):
				del ls[1:]
		return t(ls)
	def __init__(sf, args):
		sf.__args = tpl((base, coeff) for base, coeff) in args)
	@property
	def args(sf):
		return sf.__args
		
class p_neg(p_uni):pass
class p_add(p_bin):pass
class p_mul(p_bin):pass
class p_pow(p_bin):pass

class p_sum(p_many0):
	@classmethod
	def get_default_const(cls):
		return frac(0)
	@classmethod
	def collect_const(cls, acc, base, coeff):
		return acc.fr_add(base.fr_mul(coeff))
	@classmethod
	def is_halt_const(cls, acc):
		return ff
class p_prod(p_many0):
	@classmethod
	def get_default_const(cls):
		return frac(1)
	@classmethod
	def collect_const(cls, acc, base, coeff):
		return acc.fr_mul(base.fr_pow(coeff))
	@classmethod
	def is_halt_const(cls, acc):
		return acc.is_zero()



@functools.total_ordering
class symbol(poly):
	def _rdata_(sf):
		rrr()
	def __lt__(sf, ot):
		return sf.rdata() < ot.rdata()
	def __le__(sf, ot):
		return sf.rdata() <= ot.rdata()
	def __eq__(sf, ot):
		return sf.rdata() == ot.rdata()
	def __hash__(sf):
		return hash(sf.rdata())
	def rdata(sf):
		return (type(sf).__qualname__, sf._rdata_())
	def conj(sf):
			return conjugate(sf)
	def _may_conj_(sf):
		if sf.is_real():
			r = sf
		elif sf.is_imag():
			r = -sf
		elif isinstance(sf, conjugate):
			r = sf.org_sym
		else:
			r = None
		return r
	def is_real(sf):
		return ff
	def is_imag(sf):
		return ff
	def is_int(sf):
		return ff
	def is_uint(sf):
		return ff
		
class symb(symbol):
	def _rdata_(sf):
		return (sf.org_name,)
	def __init__(sf, name):
		sf.__org_name = name
	@property
	def org_name(sf):
		return sf.__org_name
class frac(symbol):
	def _rdata_(sf):
		return (sf.org_frac, sf.is_real())
	def __init__(sf, *arg, imag:bool=ff):
		sf.__org_frac = Fraction(*arg)
		sf.__org_imag = bool(imag)
	@property
	def org_frac(sf):
		return sf.__org_frac
	def is_zero(sf):
		return not sf.org_frac
		
	def is_real(sf):
		return not sf.__org_imag or sf.is_zero()
	def is_imag(sf):
		return sf.__org_imag or sf.is_zero()
	def is_int(sf):
		return sf.is_real() and sf.org_frac.denominator == 1
	def is_uint(sf):
		return sf.is_int() and sf.org_frac >= 0
	def fr_add(sf, ot):
		sf. complex frac
class conjugate(symbol):
	def _rdata_(sf):
		return (sf.org_sym,)
	def __new__(cls, sym):
		if isinstance(sym, conjugate):
			r = sym.org_sym
		elif isinstance(sym, symbol):
			mr = sym._may_conj_()
			if mr is None:
				r = sf = super(cls, conjugate).__new__(cls)
				sf.__org_sym = sym
			else:
				r = mr
		else:
			rrr()
		return r
	"""
	def __init__(sf, sym):
		sf.__org_sym = sym
		"""
	@property
	def org_sym(sf):
		return sf.__org_sym


	def is_real(sf):
		return sf.org_sym.is_real()
	def is_imag(sf):
		return sf.org_sym.is_imag()
	def is_int(sf):
		return sf.org_sym.is_int()
	def is_uint(sf):
		return sf.org_sym.is_uint()














