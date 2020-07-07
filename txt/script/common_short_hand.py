#common_short_hand
#from common_short_hand import *
#for n in sorted(globals().keys()): print(f"\t{n}")

pr = print
rg = range
ff = not 1
tt = not 0
eee = Exception
nnn = {}.get(0)
nnn = None
err = Exception
tt, ff = True, False
inf = oo = float('inf')
assert repr(inf)=='inf'
enm = enumerate
tpl = tuple
pr=print
def sw(a):
	pr(a, end='')
def prx(n):
	for _ in rg(n): pr()

locs = locals
def prn(nms, locs):
	c = ';'
	nmss = nms.replace('\n', c).split(c)
	for nms in nmss:
		c = ' '
		nms = nms.replace(',', c).split()
		s = '; '.join(
			'{}={!r}'.format(
				nm, locs[nm])
			for nm in nms
			)
		pr(s)
		continue
		fmt = '; '.join(
			'{nm}={{{nm}!r}}'.format(
				nm=nm)
			for nm in nms
			)
		pr(fmt)
		s = fmt.format(**locs)
		pr(s)

def ls2mx(ls, col):
	if col == len(ls)==0: return []
	if col < 1 or len(ls)%col: raise eee
	return [ls[i:i+col] for i in rg(0, len(ls), col)]
		
rvd = reversed
def _mk_i(n,i,d):
	if i is nnn:
		i = d
	if i < 0:
		i+=n
	if not 0<=i<=n: raise eee
	return i
def rvs(ls, i=0,j=nnn):
	n = len(ls)
	i = _mk_i(n, i, 0)
	j = _mk_i(n, j, n)
	if j-i >= 2:
		#prn("i,j,n,ls", locs())
		#pr(ls[i:j], ls[j-1:i-1:-1])
		#bug@i=0:ls[i:j] = ls[j-1:i-1:-1]
		ls[i:j] = rvd(ls[i:j])
		assert len(ls) == n
def lshf(ls, k, i=0, j=nnn):
	if not k: return
	n = len(ls)
	if not n: return
	i = _mk_i(n, i, 0)
	j = _mk_i(n, j, n)
	m = j-i
	if m<2: return
	k %= m
	assert 0<=k<m
	if not k: return
	k += i
	assert i<k<j
	rvs(ls, i,k)
	rvs(ls, k,j)
	rvs(ls, i,j)

def rrr():
	raise eee
def fst(kv):
	return kv[0]
def snd(kv):
	return kv[1]
def id(x):
	return x
def sgn(x):
	return -1 if x<0 else (
		1 if x>0 else 0)
def acc(xs, *, op, new, f0=nnn):
	xs = iter(xs)
	for r in xs: break
	else:
		if f0 is nnn: raise eee
		return f0()
	r = new(r)
	for x in xs:
		r = op(r, x)
	return r
def fold1(op, xs):
	it = iter(xs)
	for h in  it: break
	else: raise err
	return fold(op, h, it)
def fold(op, h, xs):
	for x in xs:
		h = op(h, x)
	return h

import operator as opss
def fall(n, e):
	return fold(opss.mul, 1, rg(n, n-e, -1))
def fff(n):
	return fall(n, n)
def choose(n, e):
	return fall(n, e)//fff(e)







from fractions import Fraction as fr
fr0 = fr(0)
fr1 = fr(1)
import math as M
#print(dir(M))
fcc = factorial = F  = M.factorial
if 1:
	try:
		choose = C = M.comb
	except AttributeError:
		pass
chh = C = choose
def C_(n, i):
    if not 0 <= i <= n: return 0
    return F(n)//F(i)//F(n-i)




import itertools
import functools
from collections import defaultdict, Counter
from itertools import (
	permutations as perm
	, product as product_
	)
from itertools import product as pdt





class gggg:
	using_sympy=ff
	using_seed=tt
if gggg.using_seed:
	_mypaths_ = [
		"/storage/emulated/0/0my_files/python3_src-master/"
		,"/storage/emulated/0/0my_files/txt/script/"
		]
	import sys
	sys.path[0:0] = _mypaths_
	import seed
	#pr("seed")
	from seed.io.savefile.SaveFile import SaveFileDict
	"""
	encoding = 'u8'
	kwargs = {'a':b'', 0:[]}
	mk = lambda T, iofile, kwargs: T(iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs)
	iofile = io.StringIO()
	T = SaveFileDict
	C = mk(T, iofile, kwargs)
	g_cache = C
	"""
	class savefile_helper:
		def __init__(sf, T, **kw):
			d = dict(encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True)
			d.update(kw)
			sf.kw = d
			sf.T = T
		def mk(sf, iofile, kwargs):
			return sf.T(iofile, kwargs=kwargs, **sf.kw)
	dict_infile = savefile_helper(SaveFileDict)
		#g_sv = dict_infile.mk("sv.symmetric_poly2basic_expand.py.txt", dict(n="inf", gen="symmetric_poly2basic_expand.py"))

if gggg.using_sympy:
	from sympy import *
	dd = nnn
	#dd = QQ[I]
	#dd = CC
	mxx = Matrix
	sy0 = _0 = sympify(0)
	sy1 = _1 = sympify(1)
	
	def is_real(x):
		return im(x)==0




#########my mx

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

