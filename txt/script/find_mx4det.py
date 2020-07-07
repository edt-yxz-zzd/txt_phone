#find_mx4det
import itertools
import operator as opss
def id(x):
	return x

# mx_det

import functools
from collections import defaultdict, Counter
from itertools import permutations as perm, product as _product
rg = range
tt = True
ff = not tt
nn = None
enm = enumerate
tpl = tuple
rg = range
pr=print
def sw(a):
	pr(a, end='')
err = Exception
tt, ff = True, False


def is_even_pm(pm):
	#012 120 201 ==>> tt
	#102 210 021 ==>> ff
	[*i2o] = pm
	rr = len(i2o)
	#pr(i2o)
	assert set(i2o) == set(rg(rr))
	o2i = [nn]*rr
	for i,o in enm(i2o):
		o2i[o] = i
	
	r = tt
	def swap(i,j):
		nonlocal r
		if i==j: return
		r = not r
		a = i2o[i]
		b = i2o[j]
		i2o[i] = b
		i2o[j] = a
		o2i[a] = j
		o2i[b] = i
	def fix(i):
		j = o2i[i]
		assert 0 <= j <= i
		swap(i,j)
	for i in reversed(rg(rr)):
		fix(i)
	assert o2i == i2o
	assert o2i == [*rg(rr)]
	return r

def _t():
	#012 120 201 ==>> tt
	#102 210 021 ==>> ff
	ts3 = '012 120 201'
	fs3 = '102 210 021'
	def s2pm(s):
		return [*map(int, s)]
	def s2pms(s):
		return [*map(s2pm, s.split())]
	def t(s_pms, r):
		pms = s2pms(s_pms)
		for pm in pms:
			assert is_even_pm(pm) == r
	data = [(fs3, ts3)]
	for fs, ts in data:
		t(fs, ff)
		t(ts, tt)

_t()







# mx = [[(fr, sym)]]
def det(mx):
	rr = len(mx)
	cc = len(mx[0])
	assert rr == cc
	pms = perm(rg(rr))
	d = defaultdict(int)
	for pm in pms:
		c = 1 if is_even_pm(pm) else -1
		ss = []
		for i,j in enm(pm):
			cff, sym = mx[i][j]
			c *= cff
			ss.append(sym)
		ss.sort()
		ss = tpl(ss)
		d[ss] += c
	d = {k:v for k,v in d.items() if v}
	return d



def _t_det(det):
	[q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m] = (
		'qwertyuiopasdfghjklzxcvbnm'
		)
	mx2 = [
		[(2, a), (3, b)]
		,[(5, c), (7, d)]
		]
	
	ans2 = {('a', 'd'): 14, ('b', 'c'): -15}
	mx3 = [
		[(0,a),(1,x),(1,y)]
		,[(-1,x),(0,a),(1,z)]
		,[(-1,y),(-1,z),(0,a)]
		]
	ans3 = {}
	data = [
		(mx2, ans2)
		,(mx3, ans3)
		]
	for mx, ans in data:
		r = det(mx)
		#pr(r)
		assert r == ans
_t_det(det)


# mx = [[a]]
def det__base(mx, *
	, acc_mul, acc_add
	, std_prod, std_sum
	, mk_neg_one4mul, mk_one4mul
	, mk_zero4add
	):
	rr = len(mx)
	cc = len(mx[0])
	assert rr == cc
	pms = perm(rg(rr))
	d = mk_zero4add()
	for pm in pms:
		c = mk_one4mul if is_even_pm(pm) else mk_neg_one4mul
		c = c()
		for i,j in enm(pm):
			a = mx[i][j]
			c = acc_mul(c, a)
		c = std_prod(c)
		d = acc_add(d, c)
	d = std_sum(d)
	return d




def _t_det2():
	def acc_mul(prod, p):
		c, ss = prod
		cff, sym = p
		c *= cff
		ss.append(sym)
		return (c,ss)
	def acc_add(d, prod):
		c, ss = prod
		d[ss] += c
		return d
	def std_prod(prod):
		c, ss = prod
		ss.sort()
		ss = tpl(ss)
		return (c,ss)
	def std_sum(d):
		d = {k:v for k,v in d.items() if v}
		return d
	def mk_neg_one4mul():
		return (-1, [])
	def mk_one4mul():
		return (1, [])
	def mk_zero4add():
		return defaultdict(int)

	def det2(mx):
		return det__base(mx
			, acc_mul=acc_mul
			, acc_add=acc_add
			, std_prod=std_prod
			, std_sum=std_sum
			, mk_neg_one4mul=mk_neg_one4mul
			, mk_one4mul=mk_one4mul
			, mk_zero4add=mk_zero4add
			)
	_t_det(det2)

_t_det2()




def mk_det__num():
	def mk_neg_one4mul():
		return -1
	def mk_one4mul():
		return 1
	def mk_zero4add():
		return 0
	def det__num(mx):
		return det__base(mx
			, acc_mul = opss.__imul__
			, acc_add = opss.__iadd__
			, std_prod=id
			, std_sum=id
			, mk_neg_one4mul=mk_neg_one4mul
			, mk_one4mul=mk_one4mul
			, mk_zero4add=mk_zero4add
			)
	return det__num


det__num = mk_det__num()

def iter_mx():
	it=itertools.product([-1,1,1j,-1j], repeat=9)
	
	for ls in it:
		mx=[
			[1]*4
			,[1,*ls[:3]]
			,[1,*ls[3:6]]
			,[1,*ls[6:]]
			];
		yield mx

def find_mx4det():
	s = set()
	c = Counter()
	ds = [4,-4,4j,-4j]
	for mx in iter_mx():
		d = det__num(mx)
		s.add(d)
		if d in ds:
			#a^4+b^4+...
			pr(d, mx)
			i = ds.index(d)
			del ds[i]
			if not ds: return
		if abs(d)==4:
			#a^4+b^4+...
			#pr(d, mx)
			#return
			c.update([d])
	pr(s)
"""
find_mx4det()

4j [[1, 1, 1, 1], [1, -1, -1, -1], [1, -1, -1, 1j], [1, -1, 1j, -1]]
(4+0j) [[1, 1, 1, 1], [1, -1, -1, -1], [1, -1, -1, 1j], [1, -1, (-0-1j), -1]]
(-4+0j) [[1, 1, 1, 1], [1, -1, -1, -1], [1, -1, -1, 1j], [1, 1, 1j, -1]]
-4j [[1, 1, 1, 1], [1, -1, -1, -1], [1, -1, -1, 1j], [1, 1, (-0-1j), -1]]
"""


def iter_mx2(n, values, row1):
	assert n==len(row1)
	it=itertools.product(values, repeat=(n-1)*n)
	
	for ls in it:
		mx=[[*row1]]
		for i in rg(0, len(ls), n):
			mx.append(ls[i:i+n])
		assert len(mx)==n
		yield mx

def __zip_mx__f(*a):
	return a
def zip_mx(a,b,f=__zip_mx__f):
	return tpl(
		#tpl(zip(r,s))
		tpl(map(f,r,s))
		for r,s in zip(a,b)
		)


def iter_mx3():
	"""
	mx_r8_2
		[ a,  b,  c,  d
		;ib, -a,-id, -c
		;ic,  d, -a,-ib
		;id, ic,  b,  a
		] = (aaaa+bbbb+cccc+dddd)
	"""
	
	mx_r8_2 =[
		[1,1,1,1]
		,[ 1j, -1, -1j,  -1]
		,[ 1j,  1,  -1, -1j]
		,[ 1j, 1j,   1,   1]
		]
	
	#-a33,-a44
	mx_r8_2_1 =[
		[1,1,1,1]
		,[ 1j, -1, -1j,  -1]
		,[ 1j,  1,   1, -1j]
		,[ 1j, 1j,   1,  -1]
		]
	
	#-a22,-a44
	mx_r8_2_2 =[
		[1,1,1,1]
		,[ 1j,  1, -1j,  -1]
		,[ 1j,  1,  -1, -1j]
		,[ 1j, 1j,   1,  -1]
		]
	#-a22,-a33
	mx_r8_2_3 =[
		[1,1,1,1]
		,[ 1j,  1, -1j,  -1]
		,[ 1j,  1,   1, -1j]
		,[ 1j, 1j,   1,   1]
		]
	
	#-b21,-b34,-b43
	#-b21,-b34
	mx_r8_2_4 =[
		[1,1,1,1]
		,[-1j, -1, -1j,  -1]
		,[ 1j,  1,  -1,  1j]
		,[ 1j, 1j,   1,   1]
		]
	
	#-b21,-b43
	mx_r8_2_5 =[
		[1,1,1,1]
		,[-1j, -1, -1j,  -1]
		,[ 1j,  1,  -1, -1j]
		,[ 1j, 1j,  -1,   1]
		]
	
	#-b34,-b43
	mx_r8_2_6 =[
		[1,1,1,1]
		,[ 1j, -1, -1j,  -1]
		,[ 1j,  1,  -1,  1j]
		,[ 1j, 1j,  -1,   1]
		]
	
	#-c24,-c31,-c42
	#-c24,-c31
	mx_r8_2_7 =[
		[1,1,1,1]
		,[ 1j, -1, -1j,   1]
		,[-1j,  1,  -1, -1j]
		,[ 1j, 1j,   1,   1]
		]
	
	#-c24,-c42
	mx_r8_2_8 =[
		[1,1,1,1]
		,[ 1j, -1, -1j,   1]
		,[ 1j,  1,  -1, -1j]
		,[ 1j,-1j,   1,   1]
		]
	
	#-c31,-c42
	mx_r8_2_9 =[
		[1,1,1,1]
		,[ 1j, -1, -1j,  -1]
		,[-1j,  1,  -1, -1j]
		,[ 1j,-1j,   1,   1]
		]
	
	#-d23,-d32,-d41
	#-d23,-d32
	mx_r8_2_10 =[
		[1,1,1,1]
		,[ 1j, -1,  1j,  -1]
		,[ 1j, -1,  -1, -1j]
		,[ 1j, 1j,   1,   1]
		]
	#-d23,-d41
	mx_r8_2_11 =[
		[1,1,1,1]
		,[ 1j, -1,  1j,  -1]
		,[ 1j,  1,  -1, -1j]
		,[-1j, 1j,   1,   1]
		]
	
	#-d32,-d41
	mx_r8_2_12 =[
		[1,1,1,1]
		,[ 1j, -1, -1j,  -1]
		,[ 1j, -1,  -1, -1j]
		,[-1j, 1j,   1,   1]
		]
	
	
	ls = [
		mx_r8_2_1
		,mx_r8_2_2
		,mx_r8_2_3
		,mx_r8_2_4
		,mx_r8_2_5
		,mx_r8_2_6
		,mx_r8_2_7
		,mx_r8_2_8
		,mx_r8_2_9
		,mx_r8_2_10
		,mx_r8_2_11
		,mx_r8_2_12
		]
	yield from ls
	
		
def find_mx4det2(iter_mx=iter_mx, show_all_per_case=ff):
	ss = set()
	cr = Counter()
	a,b,c,d = 'abcd'
	ks=[aaaa,bbbb,cccc,dddd
		]=[('a', 'a', 'a', 'a')
			, ('b', 'b', 'b', 'b')
			, ('c', 'c', 'c', 'c')
			, ('d', 'd', 'd', 'd')
			]

	mx_syms = \
		['abcd'
		,'badc'
		,'cdab'
		,'dcba'
		]
	ds = []
	ds__cff = {
		(-1j, 1j, 1j, -1j)
		,(1j, -1j, 1j, -1j)
		}
	last_known_mx__cff = \
		[[1, 1, 1, 1], [1, -1, -1, -1], [1, 1j, 1j, 1], [1, (-0-1j), (-0-1j), -1]]
	last_known_mx__cff=[]
	ds__cff=set()

	it = iter_mx()
	#it = iter_mx3()
	if last_known_mx__cff and ds__cff:
		for mx__cff in it:
			if mx__cff==last_known_mx__cff:
				break
		else:
			raise
	for mx__cff in it:
		mx = zip_mx(mx__cff, mx_syms)
		d = det(mx)
		ll = len(d)
		ss.add(ll)
		if ff and d in ds:
			#a^4+b^4+...
			pr(d, mx)
			i = ds.index(d)
			del ds[i]
			if not ds: return
		if ll==4:
			#a^4+b^4+...
			d__cff = tpl(d[k] for k in ks)
			if show_all_per_case or d__cff not in ds__cff:
				pr(d__cff, mx__cff)
				ds__cff.add(d__cff)
				#return
		cr.update([ll])
	pr(ss)
	pr(cr)

"""
find_mx4det2(iter_mx3, show_all_per_case=tt)

(1, (1+0j), (1+0j), (1+0j)) [[1, 1, 1, 1], [1j, 1, (-0-1j), -1], [1j, 1, -1, (-0-1j)], [1j, 1j, 1, -1]]
(1, (1+0j), (1+0j), (1+0j)) [[1, 1, 1, 1], [1j, 1, (-0-1j), -1], [1j, 1, 1, (-0-1j)], [1j, 1j, 1, 1]]
(1, (1+0j), (1+0j), (1+0j)) [[1, 1, 1, 1], [(-0-1j), -1, (-0-1j), -1], [1j, 1, -1, 1j], [1j, 1j, 1, 1]]
(1, (1+0j), (1+0j), (1+0j)) [[1, 1, 1, 1], [(-0-1j), -1, (-0-1j), -1], [1j, 1, -1, (-0-1j)], [1j, 1j, -1, 1]]
(1, (1+0j), (1+0j), (1+0j)) [[1, 1, 1, 1], [1j, -1, (-0-1j), 1], [(-0-1j), 1, -1, (-0-1j)], [1j, 1j, 1, 1]]
(1, (1+0j), (1+0j), (1+0j)) [[1, 1, 1, 1], [1j, -1, (-0-1j), 1], [1j, 1, -1, (-0-1j)], [1j, (-0-1j), 1, 1]]
(1, (1+0j), (1+0j), (1+0j)) [[1, 1, 1, 1], [1j, -1, 1j, -1], [1j, -1, -1, (-0-1j)], [1j, 1j, 1, 1]]
(1, (1+0j), (1+0j), (1+0j)) [[1, 1, 1, 1], [1j, -1, 1j, -1], [1j, 1, -1, (-0-1j)], [(-0-1j), 1j, 1, 1]]
{4, 5}
Counter({4: 8, 5: 4})


====
mx_r8_2=
[[1, 1, 1, 1], [1j, -1, (-0-1j), -1], [1j, 1, -1, (-0-1j)], [1j, 1j, 1, 1]]

22,44;22,33;;21,34;21,43;;24,31;24,42;;23,32;23,41
8variant of mx_r8_2
22,44
[[1, 1, 1, 1], [1j, 1, (-0-1j), -1], [1j, 1, -1, (-0-1j)], [1j, 1j, 1, -1]]

22,33
[[1, 1, 1, 1], [1j, 1, (-0-1j), -1], [1j, 1, 1, (-0-1j)], [1j, 1j, 1, 1]]

21,34
[[1, 1, 1, 1], [(-0-1j), -1, (-0-1j), -1], [1j, 1, -1, 1j], [1j, 1j, 1, 1]]

21,43
[[1, 1, 1, 1], [(-0-1j), -1, (-0-1j), -1], [1j, 1, -1, (-0-1j)], [1j, 1j, -1, 1]]

24,31
[[1, 1, 1, 1], [1j, -1, (-0-1j), 1], [(-0-1j), 1, -1, (-0-1j)], [1j, 1j, 1, 1]]

24,42
[[1, 1, 1, 1], [1j, -1, (-0-1j), 1], [1j, 1, -1, (-0-1j)], [1j, (-0-1j), 1, 1]]

23,32
[[1, 1, 1, 1], [1j, -1, 1j, -1], [1j, -1, -1, (-0-1j)], [1j, 1j, 1, 1]]

23,41
[[1, 1, 1, 1], [1j, -1, 1j, -1], [1j, 1, -1, (-0-1j)], [(-0-1j), 1j, 1, 1]]

==

22,44;22,33;;
21,34;21,43;;
24,31;24,42;;
23,32;23,41;;
==
22/21/24/23

"""







"""
8cases
find_mx4det2()

(-1j, 1j, 1j, -1j) [[1, 1, 1, 1], [1, -1, -1, -1], [1, 1j, -1, 1j], [1, (-0-1j), 1, (-0-1j)]]
(1j, -1j, 1j, -1j) [[1, 1, 1, 1], [1, -1, -1, -1], [1, 1j, 1j, 1], [1, (-0-1j), (-0-1j), -1]]
(1j, -1j, -1j, 1j) [[1, 1, 1, 1], [1, -1, -1, -1], [1, (-0-1j), -1, (-0-1j)], [1, 1j, 1, 1j]]
(-1j, 1j, -1j, 1j) [[1, 1, 1, 1], [1, -1, -1, -1], [1, (-0-1j), 1j, -1], [1, 1j, (-0-1j), 1]]
(1j, 1j, -1j, -1j) [[1, 1, 1, 1], [1, 1j, -1, 1j], [1, 1j, -1, 1j], [1, -1, 1, -1]]
(-1j, -1j, -1j, -1j) [[1, 1, 1, 1], [1, 1j, -1, 1j], [1, 1j, 1j, 1], [1, -1, (-0-1j), 1j]]
(-1j, -1j, 1j, 1j) [[1, 1, 1, 1], [1, 1j, -1, 1j], [1, (-0-1j), -1, (-0-1j)], [1, 1, 1, 1]]
(1j, 1j, 1j, 1j) [[1, 1, 1, 1], [1, 1j, -1, 1j], [1, (-0-1j), 1j, -1], [1, 1, (-0-1j), (-0-1j)]]
{4, 5, 6, 7, 8, 9, 10, 11}
"""





def find_mx4det4():
	ss = set()
	cr = Counter()
	a,b,c,d = 'abcd'
	ks=[aaaa,bbbb,cccc,dddd
		]=[('a', 'a', 'a', 'a')
			, ('b', 'b', 'b', 'b')
			, ('c', 'c', 'c', 'c')
			, ('d', 'd', 'd', 'd')
			]

	mx_syms = \
		['abcd'
		,'badc'
		,'cdab'
		,'dcba'
		]
	
	mx_r8_2__cff =\
		[[1, 1, 1, 1], [1j, -1, (-0-1j), -1], [1j, 1, -1, (-0-1j)], [1j, 1j, 1, 1]]

	dtss = Counter()
	it = iter_mx2(4, [1,-1], [1]*4)
	for mx__sign in it:
		mx__cff = zip_mx(mx__sign, mx_r8_2__cff, opss.__mul__)
		mx = zip_mx(mx__cff, mx_syms)
		d = det(mx)
		ll = len(d)
		ss.add(ll)
		sdv = sum(d.values())
		if ll==4 and sdv==4:
			#a^4+b^4+...
			d__cff = tpl(d[k] for k in ks)
			dts = sum(map(sum, mx__sign))
			dtss.update([dts])
			if tt:
				pr(f"dts={dts}", d__cff, mx__sign, mx__cff)
				#return
		cr.update([ll])
	pr("det_lens", ss)
	pr("det_len2c", cr)
	pr("dt_sign2c", dtss)

"""
find_mx4det4()

...
det_lens {8, 9, 4, 5}
det_len2c Counter({8: 2816, 9: 768, 4: 384, 5: 128})
dt_sign2c Counter({4: 80, 0: 61, 8: 42, 12: 8, 16: 1})
===
4: 80=3^4-1
"""





