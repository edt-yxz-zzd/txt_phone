#魔方状态

from itertools import product as pdt
import operator as opss
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






class st_ops:
	def step(sf, st):
		# -> [st]
		pass
	def all_sts(sf, st):
		done = set()
		todo = {st}
		while todo:
			st = todo.pop()
			done.add(st)
			for st in sf.step(st):
				if st not in done:
					todo.add(st)
		return done

class st_level_ops(st_ops):
	def get_idx_bound(sf):
		# -> idx_bound
		pass
	def get_level_size(sf):
		# -> uint in byte
		pass
	def st2idx(sf, st):
		# st -> [0..idx_bound-1]
		pass
	def idx2may_bad_st(sf, idx):
		# idx -> (st | bad_st | raise)
		pass

	def continue_fill(sf, bad_level, begin_idx, array):
		#-> Iter begin_idx
		#usage:
		#	try:
		#		for begin_idx in sf.continue_fill(bad_level, begin_idx, array):
		#			pass
		#	finally:
		#		save(begin_idx, array.flush())
		#
		#
		i = begin_idx
		a = array
		sz = len(a)
		while 0 <= i < sz:
			begin_level = a[i]
			assert begin_level != bad_level
			next_level = begin_level+1
			for i in rg(i, sz):
				if a[i] == begin_level:
					yield i
					st = sf.idx2may_bad_st(i)
					for j in map(sf.st2idx, sf.step(st)):
						if a[j] == bad_level:
							a[j] = next_level
			else:
				for i in rg(sz):
					if a[i] == next_level:
						break
				else:
					i = sz
		yield sz

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




def iter_ps():
	ls = rg(-2, 3)
	for p in pdt(ls, ls, ls):
		acc = [0]*3
		for i in p: acc[abs(i)] += 1
		if acc[2] == 1 and acc[0] !=2:
			yield p

class g:
	ps = [p for p in iter_ps()]
	assert len(ps) == 6*8
	
	# into clock
	# clockwise 90
	r90_yp = (
		(0,0,1)
		,(0,1,0)
		,(-1,0,0)
		)
	r90_xp = (
		(1,0,0)
		,(0,0,-1)
		,(0,1,0)
		)
	r90_zp = (
		(0,-1,0)
		,(1,0,0)
		,(0,0,1)
		)
	def r270(r90):
		return fold1(mx_mul, [r90]*3)
	r90_yn = r270(r90_yp)
	r90_xn = r270(r90_xp)
	r90_zn = r270(r90_zp)
	#pr(r90_yn)
	bys = (
		(1,0,0)
		,(0,1,0,)
		,(0,0,1,)
		,(-1,0,0,)
		,(0,-1,0,)
		,(0,0,-1,)
		)
	(xp,yp,zp
	,xn,yn,zn) = bys
	by2old2new = None # do()

def ____bug___rot90(by, v):
	assert dotp(by, by) == 1
	assert abs(sum(by)) == 1
	return
	# bug: rot_mx = dotp(by, [xp...], add=vadd, mul=ntime)
def rot90(by, v):
	r90 = get_r90_mx(by)
	return mx_mul_col(r90, v)
def get_r90_mx(by):
	assert dotp(by, by) == 1
	assert abs(sum(by)) == 1
	assert set(by) < {0,1,-1}
	i = by.index(sum(by))
	xyz = 'xyz'[i]
	pn = '!pn'[by[i]]
	nm = f'r90_{xyz}{pn}'
	r90 = getattr(g, nm)
	return r90

def is_selected(by, p):
	i = by.index(sum(by))
	return sgn(p[i]) == sgn(by[i])

def sel_ps(by):
	return [p for p in g.ps
		if is_selected(by, p)
		]

#pr(sel_ps((0,0,1)))

assert len(sel_ps((0,0,1))) == 8+3*4

def _d_r90(by, d):
	return {
		(p if not is_selected(by, p) else
		rot90(by, p)
		): c
		for p, c in d.items()
		}

def t():
	d = dict(zip(g.ps, g.ps))
	by = (0,1,0)
	d2 = _d_r90(by, d)
	pr(d2)
#t()
def mk_p_old2new(by):
	d = dict(zip(g.ps, g.ps))
	d2 = _d_r90(by, d)
	old2new = {
		old:new
		for new, old in d2.items()
		}
	return old2new

def do():
	g.by2old2new ={
		by: mk_p_old2new(by)
		for by in g.bys
		}
do()###!!!!!!!



def d_r90(by, d):
	o2n = g.by2old2new[by]
	return {
		o2n[p]: c
		for p, c in d.items()
		}



class mc_ops(st_ops):
	def step(ops, st):
		return [
			st.r90(by)
			for by in g.bys
			]
class mc:
	#save mc in file
	#	1. 48position -> 6color
	#		6 ==>> 3bit
	#		48*3bit = 18byte
	#		6**48 < 2**125 < 16byte
	#	2. 48 old position -> 48 new position
	#	3. (3*8//3 old corner face position -> 3*8 new ...) + (2*12//2 old edge face -> 2*12 new ...)
	#		48//2==24 ==>> 5bit
	#		(8+12)*5bit = 100bit < 13byte
	#		24**20 < 2**92 < 12byte
	#
	#	3-2. (if wo edges)
	#		8*5bit == 5byte
	#		24**8 < 2**37 < 5byte
	#
	#	4.  int
	#		(3**8*fff(8) * 2**12*fff(12)) < 2**69
	#		2**69 < 9byte
	#
	#
	def __init__(sf, d):
		#assert len(d) <= 48
		t = tpl(sorted(d.items()))
		sf.d = d
		sf.t = t
		sf.h = hash(t)
	def __hash__(sf):
		return sf.h
	def __eq__(sf, ot):
		return sf.h == ot.h and sf.t == ot.t

	def r90(sf, by):
		return mc(d_r90(by, sf.d))

def t():
	p1, n1, p2, n2 = 1,-1,2,-2
	xz, zy, yx, yx2 = "xz zy yx yx2".split()
	ops = mc_ops()
	
	d1 = {
		(n1,n2,n1):xz
		,(n2,n1,n1):zy
		,(n1,n1,n2):yx
		}
	r1 = 3*8
	d2 = d1.copy()
	d2.update(
		{(n1,n2,p1):xz
		,(n2,n1,p1):zy
		,(n1,n1,p2):yx2
		})
	r2 = 8*7*9 #504==P(8,2)*3*3

	dat = [
		(d1,r1)
		,(d2,r2)
		]
	for d, r in dat:
		st = mc(d)
		sts = ops.all_sts(st)
		pr(len(sts))
		assert len(sts) == r

t()


_r = 3**8 * fold1(opss.mul, rg(1,9))
assert 2**27 < _r == 3**8 * fff(8) < 2**28
assert 2**40 < 2**12 * fff(12) < 2**41
2**69

# 2**28 * 5byte (mc wo edges)
# 1.25 GB

#db:
#	mc wo edge(5byte) -> level(0..20)
#		5+1 byte
#	total 1.5 GB
#	---
#	array [level] 0.25 GB
#	-----------
#	idx(32bit) -> (mc wo(5byte), level(0..20))
#		4+5+1 byte
#	total 2.5 GB
#	-----------
#	let i=mc_idx
#	i -> by -> bool(+/-90) -> (succ|prev|same_level)
#		6*2*2bit == 3byte













