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



def _t():
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
_t()


@functools.total_ordering
class symb:
	def __init__(sf, n, prefix='s', suffix=''):
		sf.__pns = (prefix, n, suffix)
	def __lt__(sf, ot):
		return sf.__pns < ot.__pns
	def __le__(sf, ot):
		return sf.__pns <= ot.__pns
	def __eq__(sf, ot):
		return sf.__pns == ot.__pns
	def __hash__(sf):
		return hash(sf.__pns)
	def __repr__(sf):
		prefix,i,suffix = sf.__pns
		s = f"{prefix}{i}{suffix}"
		return repr(s)

def iter_syms__str(n, prefix='s', suffix=''):
	for i in rg(n):
		yield f"{prefix}{i}{suffix}"

def iter_syms__sym(n, prefix='s', suffix=''):
	for i in rg(n):
		#yield f"{prefix}{i}{suffix}"
		yield symb(i, prefix=prefix, suffix=suffix)

def mk_asymetry_mx(n, iter_syms=rg):
	k = (n-1)*n//2
	[*ss] = iter_syms(k+1)
	mx = [[nn]*n for _ in rg(n)]
	for i in rg(n):
		mx[i][i] = (0, ss[-1])
	
	a = 0
	for i in rg(n):
		for j in rg(i+1, n):
			s = ss[a]; a+=1
			mx[i][j] = (1, s)
			mx[j][i] = (-1, s)
	assert a == k
	return mx

def _t():
	mx = mk_asymetry_mx(3, iter_syms=iter_syms__str)
	#pr(mx)
	assert mx == [
		[(0, 's3'), (1, 's0'), (1, 's1')]
		, [(-1, 's0'), (0, 's3'), (1, 's2')]
		, [(-1, 's1'), (-1, 's2'), (0, 's3')]
		]

_t()


def _pr_det(m=8):
	for n in rg(1,m):
		mx = mk_asymetry_mx(n, iter_syms=iter_syms__sym)
		d = det(mx)
		c = Counter(d.values())
		v = max(d.values(), key=abs, default=0)
		rt_poly = _find_rt_poly(d)
		pr(n, len(d), v, c)
		pr(rt_poly)
		#pr(d)
		pr('\n\r\n\r')
def _find_rt_poly(d):
	if not d: return []
	sqs = [k for k,v in d.items() if v==1]
	assert all(k[::2] == k[1::2] for k in sqs)
	ts = [k[::2] for k in sqs]
	ts.sort()
	def mul(k,t):
		p = [*k, *t]
		p.sort()
		return tpl(p)
	
	k = ts[0]
	ss = [1]
	for t in ts[1:]:
		p = mul(k,t)
		s = 1 if 0 < d[p] else -1
		ss.append(s)
	
	d2 = {k:0 for k in d}
	for s1, t1 in zip(ss, ts):
	 for s2, t2 in zip(ss, ts):
	 	k=mul(t1,t2)
	 	s=s1*s2
	 	d2[k]+=s
	assert d==d2
	return tpl(zip(ss, ts))
	
#_pr_det(9)

"""
1 0 0 Counter()
2 1 1 Counter({1: 1})
3 0 0 Counter()
4 6 2 Counter({1: 3, -2: 2, 2: 1})
5 0 0 Counter()
6 120 2 Counter({-2: 56, 2: 49, 1: 15})
7 0 0 Counter()
8 5250 4 Counter({-2: 2476, 2: 2354, 4: 175, -4: 140, 1: 105})
	choose(105+1,2)==5565
	175+140 = 315 = 5565-5250
"""



"""
1 0 0 Counter()
[]
2 1 1 Counter({1: 1})
((1, ('s0',)),)


3 0 0 Counter()
[]



4 6 2 Counter({1: 3, -2: 2, 2: 1})
((1, ('s0', 's5')), (-1, ('s1', 's4')), (1, ('s2', 's3')))



5 0 0 Counter()
[]



6 120 2 Counter({-2: 56, 2: 49, 1: 15})
((1, ('s0', 's9', 's14')), (-1, ('s0', 's10', 's13')), (1, ('s0', 's11', 's12')), (-1, ('s1', 's6', 's14')), (1, ('s1', 's7', 's13')), (-1, ('s1', 's8', 's12')), (1, ('s2', 's5', 's14')), (-1, ('s2', 's7', 's11')), (1, ('s2', 's8', 's10')), (-1, ('s3', 's5', 's13')), (1, ('s3', 's6', 's11')), (-1, ('s3', 's8', 's9')), (1, ('s4', 's5', 's12')), (-1, ('s4', 's6', 's10')), (1, ('s4', 's7', 's9')))



7 0 0 Counter()
[]



8 5250 4 Counter({-2: 2476, 2: 2354, 4: 175, -4: 140, 1: 105})
((1, ('s0', 's13', 's22', 's27')), (-1, ('s0', 's13', 's23', 's26')), (1, ('s0', 's13', 's24', 's25')), (-1, ('s0', 's14', 's19', 's27')), (1, ('s0', 's14', 's20', 's26')), (-1, ('s0', 's14', 's21', 's25')), (1, ('s0', 's15', 's18', 's27')), (-1, ('s0', 's15', 's20', 's24')), (1, ('s0', 's15', 's21', 's23')), (-1, ('s0', 's16', 's18', 's26')), (1, ('s0', 's16', 's19', 's24')), (-1, ('s0', 's16', 's21', 's22')), (1, ('s0', 's17', 's18', 's25')), (-1, ('s0', 's17', 's19', 's23')), (1, ('s0', 's17', 's20', 's22')), (-1, ('s1', 's8', 's22', 's27')), (1, ('s1', 's8', 's23', 's26')), (-1, ('s1', 's8', 's24', 's25')), (1, ('s1', 's9', 's19', 's27')), (-1, ('s1', 's9', 's20', 's26')), (1, ('s1', 's9', 's21', 's25')), (-1, ('s1', 's10', 's18', 's27')), (1, ('s1', 's10', 's20', 's24')), (-1, ('s1', 's10', 's21', 's23')), (1, ('s1', 's11', 's18', 's26')), (-1, ('s1', 's11', 's19', 's24')), (1, ('s1', 's11', 's21', 's22')), (-1, ('s1', 's12', 's18', 's25')), (1, ('s1', 's12', 's19', 's23')), (-1, ('s1', 's12', 's20', 's22')), (1, ('s2', 's7', 's22', 's27')), (-1, ('s2', 's7', 's23', 's26')), (1, ('s2', 's7', 's24', 's25')), (-1, ('s2', 's9', 's15', 's27')), (1, ('s2', 's9', 's16', 's26')), (-1, ('s2', 's9', 's17', 's25')), (1, ('s2', 's10', 's14', 's27')), (-1, ('s2', 's10', 's16', 's24')), (1, ('s2', 's10', 's17', 's23')), (-1, ('s2', 's11', 's14', 's26')), (1, ('s2', 's11', 's15', 's24')), (-1, ('s2', 's11', 's17', 's22')), (1, ('s2', 's12', 's14', 's25')), (-1, ('s2', 's12', 's15', 's23')), (1, ('s2', 's12', 's16', 's22')), (-1, ('s3', 's7', 's19', 's27')), (1, ('s3', 's7', 's20', 's26')), (-1, ('s3', 's7', 's21', 's25')), (1, ('s3', 's8', 's15', 's27')), (-1, ('s3', 's8', 's16', 's26')), (1, ('s3', 's8', 's17', 's25')), (-1, ('s3', 's10', 's13', 's27')), (1, ('s3', 's10', 's16', 's21')), (-1, ('s3', 's10', 's17', 's20')), (1, ('s3', 's11', 's13', 's26')), (-1, ('s3', 's11', 's15', 's21')), (1, ('s3', 's11', 's17', 's19')), (-1, ('s3', 's12', 's13', 's25')), (1, ('s3', 's12', 's15', 's20')), (-1, ('s3', 's12', 's16', 's19')), (1, ('s4', 's7', 's18', 's27')), (-1, ('s4', 's7', 's20', 's24')), (1, ('s4', 's7', 's21', 's23')), (-1, ('s4', 's8', 's14', 's27')), (1, ('s4', 's8', 's16', 's24')), (-1, ('s4', 's8', 's17', 's23')), (1, ('s4', 's9', 's13', 's27')), (-1, ('s4', 's9', 's16', 's21')), (1, ('s4', 's9', 's17', 's20')), (-1, ('s4', 's11', 's13', 's24')), (1, ('s4', 's11', 's14', 's21')), (-1, ('s4', 's11', 's17', 's18')), (1, ('s4', 's12', 's13', 's23')), (-1, ('s4', 's12', 's14', 's20')), (1, ('s4', 's12', 's16', 's18')), (-1, ('s5', 's7', 's18', 's26')), (1, ('s5', 's7', 's19', 's24')), (-1, ('s5', 's7', 's21', 's22')), (1, ('s5', 's8', 's14', 's26')), (-1, ('s5', 's8', 's15', 's24')), (1, ('s5', 's8', 's17', 's22')), (-1, ('s5', 's9', 's13', 's26')), (1, ('s5', 's9', 's15', 's21')), (-1, ('s5', 's9', 's17', 's19')), (1, ('s5', 's10', 's13', 's24')), (-1, ('s5', 's10', 's14', 's21')), (1, ('s5', 's10', 's17', 's18')), (-1, ('s5', 's12', 's13', 's22')), (1, ('s5', 's12', 's14', 's19')), (-1, ('s5', 's12', 's15', 's18')), (1, ('s6', 's7', 's18', 's25')), (-1, ('s6', 's7', 's19', 's23')), (1, ('s6', 's7', 's20', 's22')), (-1, ('s6', 's8', 's14', 's25')), (1, ('s6', 's8', 's15', 's23')), (-1, ('s6', 's8', 's16', 's22')), (1, ('s6', 's9', 's13', 's25')), (-1, ('s6', 's9', 's15', 's20')), (1, ('s6', 's9', 's16', 's19')), (-1, ('s6', 's10', 's13', 's23')), (1, ('s6', 's10', 's14', 's20')), (-1, ('s6', 's10', 's16', 's18')), (1, ('s6', 's11', 's13', 's22')), (-1, ('s6', 's11', 's14', 's19')), (1, ('s6', 's11', 's15', 's18')))





"""


































def _calc_det():
	"""
		[a, b
		;-b', a'
		] = aa'+bb'
		
		mx1
		[a,   b,   c,  d
		;-b', a', -d', c'
		;-c', d',  a', -b'
		;-d, -c,   b,  a
		] =0 if b=c=0;d=ia=i;a=1 # (1,4)or(2,3)rows
		
		mx2
		[a,   b,   c, d
		;-b', a', -d', c'
		;-c', d',   a', -b'
		;-d', -c',  b', a'
		] = 0 if a=1;b=i;c=d=0 # (3,4)rows
	
		mx3 avoid 2swap
		[a,   b,   c,  d
		;-d', a', -b', c'
		;-c', d',  a', -b'
		;-b, -c,   d,  a
		] =0 if 1 1 -1 -1 (1,2)rows
	
		a    b    c    d
		f(d) g(a) h(b) p(c)
		a = t*f(d)
			= tf(tp(c))
			= tf.tp.th.tg$a
			=?= -(t*t')^2 * conj^?(a)
			= -(t*t')^2 * a
		
		f = (((-1)^fi *) . conj^fj$)
		fi+pi+hi+gi = odd
		fj+pj+hj+gj = even
		[fj,fj+pj,fj+pj+hj] has 2odd
		
		[fj=0]:
			[pj=1][hj=0][gj=1]
		[fj=1]:
			[pj=1][hj=1][gj=1]or
			[pj=0][hj=1][gj=0]
		234rows conj?:
			0101
			1111
			1010
		
		234rows neg?:
		 2:
			1000
			0001
			1011
			0010
		 4:
			0010
			0100
			1000
			1110
		 3:
			??0?
		 1234:
			0000
			x0y(x+y+1)
			zw0(z+w)
			pq(p+q+1)0
			----
			[ac sub mx]
				==>> [z=1][q=x+y]
			[bd sub mx]
				==>> [z=1][x+q=y]
			0000
			x0y(x+y+1)
			1w0(1+w)
			p(x+y)(p+x+y+1)0
			
		mx4
		[a,    b,    c,   d
		;-d,   a',   b,   c'
		;-c', -d',   a',  b'
		;-b', -c,   -d',  a
		]
		mx5
		[a,    b,    c,   d
		;-d,   a',   b,   c'
		;-c', d',   a',  -b'
		;-b', -c,   -d',  a
		]
		mx6
		[a,    b,    c,   d
		;-d,   a',   b,   c'
		;-c', d',   a',  -b'
		; b', -c,   d',  a
		]
	
	=====real mx
	mx_r = 
		[ a, b, c, d
		;-d, a, b, c
		;-c,-d, a, b
		;-b,-c,-d, a
		]
	mx_r2 from mx1
		[ a, b, c, d
		;-b, a,-d, c
		;-c, d, a,-b
		;-d,-c, b, a
		]
	
	

	mx_r3 from mx_r2 from
		s <- +-1i
		[ a,  b,  c,  d
		;-b,  a,-sd, sc
		;-c, sd,  a,-sb
		;-d,-sc, sb,  a
		]
		
		bcd=-bcd<==>flip
		[ a, -b, -c, -d
		; b,  a, sd,-sc
		; c,-sd,  a, sb
		; d, sc,-sb,  a
		]
	
	mx_r4 from mx_r3
		stpq <- +-1i
		[ a,  b,  c,  d
		;-b, ta,-sd, sc
		;-c, sd, pa,-sb
		;-d,-sc, sb, qa
		]
	
	
	mx_r5 from mx_r3
		|mx_r5|=|mx_r3(a*=1/t)(col11&row234*=t)|
				=(-aa+bb+cc+dd)^2
		t=+-i
		[ a,  b,  c,  d
		; b,  a,-td, tc
		; c, td,  a,-tb
		; d,-tc, tb,  a
		]


	
	mx_r8_4 from mx_r8_2 mx_r8_3
		[ a,  b,  c,  d
		;ib,-a',-id, -c
		;ic,  d, -a,-ib
		;id, ic,  b, a'
		] =?= (aaa'a'+bbbb+cccc+dddd)


	mx_r8_5 from mx_r8_4
		[ a,  b,  c,  d
		;ib,-a',-id,-c'
		;ic,  d, -a,-ib
		;id,ic',  b, a'
		]

	mx_r8_6 from mx_r8_5
		[  a,  b,   c,   d
		;ib',-a',-id', -c'
		; ic, d',  -a,-ib'
		; id,ic',   b,  a'
		]

	mx_r8_7 from mx_r8_5
		[  a,  b,   c,   d
		;ib',-a',-id', -c'
		; ic,  d,  -a, -ib
		;id',ic',  b',  a'
		]
	"""
	a,b,c,d = 'abcd'
	a_,b_,c_,d_ = "a' b' c' d'".split()
	
	ta,pa,qa,sa,sb,sc,sd = "ta pa qa sa sb sc sd".split()
	ta,tb,tc,td = "ta tb tc td".split()
	mx1 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(-1,b_), (1,a_), (-1,d_), (1,c_)]
		,[(-1,c_), (1,d_), (1,a_), (-1,b_)]
		,[(-1,d), (-1,c), (1,b), (1,a)]
		]
	mx4 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(-1,d), (1,a_), (1,b), (1,c_)]
		,[(-1,c_), (-1,d_), (1,a_), (1,b_)]
		,[(-1,b_), (-1,c), (-1,d_), (1,a)]
		]
	mx5 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(-1,d), (1,a_), (1,b), (1,c_)]
		,[(-1,c_), (1,d_), (1,a_), (-1,b_)]
		,[(-1,b_), (-1,c), (-1,d_), (1,a)]
		]
	mx6 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(-1,d), (1,a_), (1,b), (1,c_)]
		,[(-1,c_), (1,d_), (1,a_), (-1,b_)]
		,[(1,b_), (-1,c), (1,d_), (1,a)]
		]
	mx_r = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(-1,d), (1,a), (1,b), (1,c)]
		,[(-1,c), (-1,d), (1,a), (1,b)]
		,[(-1,b), (-1,c), (-1,d), (1,a)]
		]
	mx_r2 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(-1,b), (1,a), (-1,d), (1,c)]
		,[(-1,c), (1,d), (1,a), (-1,b)]
		,[(-1,d), (-1,c), (1,b), (1,a)]
		]
	mx_r3 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(-1,b), (1,a), (-1,sd), (1,sc)]
		,[(-1,c), (1,sd), (1,a), (-1,sb)]
		,[(-1,d), (-1,sc), (1,sb), (1,a)]
		]
	
	mx_r4 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(-1,b), (1,ta), (-1,sd), (1,sc)]
		,[(-1,c), (1,sd), (1,pa), (-1,sb)]
		,[(-1,d), (-1,sc), (1,sb), (1,qa)]
		]
	mx_r5 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(1,b), (1,a), (-1,td), (1,tc)]
		,[(1,c), (1,td), (1,a), (-1,tb)]
		,[(1,d), (-1,tc), (1,tb), (1,a)]
		]
	
	
	mx_r8_4 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(1j,b), (-1,a_), (-1j,d), (-1,c)]
		,[(1j,c), (1,d), (-1,a), (-1j,b)]
		,[(1j,d), (1j,c), (1,b), (1,a_)]
		]
	mx_r8_5 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(1j,b), (-1,a_), (-1j,d), (-1,c_)]
		,[(1j,c), (1,d), (-1,a), (-1j,b)]
		,[(1j,d), (1j,c_), (1,b), (1,a_)]
		]
	mx_r8_6 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(1j,b_), (-1,a_), (-1j,d_), (-1,c_)]
		,[(1j,c), (1,d_), (-1,a), (-1j,b_)]
		,[(1j,d), (1j,c_), (1,b), (1,a_)]
		]
	mx_r8_7 = [
		[(1,a), (1,b), (1,c), (1,d)]
		,[(1j,b), (-1,a_), (-1j,d), (-1,c_)]
		,[(1j,c), (1,d), (-1,a), (-1j,b)]
		,[(1j,d_), (1j,c_), (1,b_), (1,a_)]
		]
	
	

	nms = '''
		mx4 mx5 mx6
		mx_r mx_r2 mx_r3 mx_r4
		mx_r5
		mx_r8_4 mx_r8_5 mx_r8_6 mx_r8_7
		'''.split()
	nm_mx_ps = []
	for nm in nms:
		mx = locals()[nm]
		nm_mx_ps.append((nm,mx))

		
	
	half_mx = [
		a,  b, c, d
		,d, a_,b, c_
		,c_,d_,a_,b_
		,b_,c, d_,a
		]
	rr = 4
	it = _product(range(2), repeat=4)
	for x,y,w,p in it:
		"""
			0000
			x0y(x+y+1)
			1w0(1+w)
			p(x+y)(p+x+y+1)0
		"""
		nm = f"mx(xywp={x}{y}{w}{p})"
		sign_pows = [
			0,0,0,0
			,x,0,y,x+y+1
			,1,w,0,1+w
			,p,x+y,p+x+y+1,0
			]
		signs = [(-1)**e for e in sign_pows]
		[*ls] = zip(signs, half_mx)
		assert len(ls) == rr**2
		mx = [
			ls[i*rr: (i+1)*rr]
			for i in rg(rr)
			]
		nm_mx_ps.append((nm,mx))


	
	######pr
	for nm,mx in nm_mx_ps:
		if nm not in (
				#mx_r mx_r2 mx_r3 mx_r4 mx_r5
				#mx_r8_4 
				'''
				mx_r8_5
				mx_r8_6 mx_r8_7
				'''.split()):
			continue
		pr(nm)
		d = det(mx)
		#pr(d)
		c = Counter(d.values())
		pr(c)
	
		d2 = {''.join(k):v for k,v in d.items()}
		pr(d2)
		#rt_poly = _find_rt_poly(d)
		#pr(rt_poly)
_calc_det()





"""
mx_r
Counter({1: 4, 4: 2, -4: 2, 2: 2})
{'aaaa': 1
, 'aabd': 4
, 'abbc': -4
, 'acdd': 4
, 'aacc': 2
, 'bbdd': 2
, 'bbbb': 1
, 'bccd': -4
, 'cccc': 1
, 'dddd': 1
}
======
{
, 'aaaa': 1
, 'cccc': 1
, 'dddd': 1
, 'bbbb': 1
, 'aacc': 2
, 'bbdd': 2

, 'aabd': 4
, 'acdd': 4

, 'abbc': -4
, 'bccd': -4
}
"""


"""
mx_r2
Counter({2: 6, 1: 4})
{'aaaa': 1
, 'bbbb': 1
, 'cccc': 1
, 'dddd': 1

, 'aabb': 2
, 'aadd': 2
, 'aacc': 2
, 'bbdd': 2
, 'bbcc': 2
, 'ccdd': 2
== (rr)^2
}
"""


"""
mx_r3
Counter({1: 10, 2: 3})
{
, 'aaaa': 1
, 'aasbsb': 1
, 'aasdsd': 1
, 'aascsc': 1
, 'aabb': 1
, 'bbsbsb': 1
, 'bdsbsd': 2
, 'bcsbsc': 2
, 'aacc': 1
, 'ccscsc': 1
, 'cdscsd': 2
, 'aadd': 1
, 'ddsdsd': 1
}
"""


"""
mx_r4
Counter({1: 10, 2: 3})
{'apaqata': 1
, 'asbsbta': 1
, 'aqasdsd': 1
, 'apascsc': 1
, 'bbpaqa': 1
, 'bbsbsb': 1
, 'bdsbsd': 2
, 'bcsbsc': 2
, 'ccqata': 1
, 'ccscsc': 1
, 'cdscsd': 2
, 'ddpata': 1
, 'ddsdsd': 1
}
"""


"""
mx_r5
Counter({-1: 6, 1: 4, -2: 3})
{#+1
, 'aaaa': 1
, 'bbtbtb': -1
, 'cctctc': -1
, 'ddtdtd': -1

#-2
, 'aatbtb': 1
, 'aatctc': 1
, 'aatdtd': 1
, 'aabb': -1
, 'aacc': -1
, 'aadd': -1

#+2
, 'cdtctd': -2
, 'bdtbtd': -2
, 'bctbtc': -2
=(-aa+bb+cc+dd)^2
}
"""



"""
mx_r8_4
Counter({1: 4, -1j: 1, 1j: 1})
{"aaa'a'": 1
, 'aacc': -1j
, 'bbbb': (1+0j)
, "a'a'cc": 1j
, 'cccc': (1+0j)
, 'dddd': 1
}

"""


"""
mx_r8_5
Counter({1: 4, -1j: 1, 1j: 1})
{"aaa'a'": 1
, "aac'c'": -1j
, 'bbbb': (1+0j)
, "a'a'cc": 1j
, "ccc'c'": (1+0j)
, 'dddd': (1+0j)
=|aa+icc|^2 +b^4+d^4
}
mx_r8_6
Counter({1: 6, 1j: 5, -1j: 5, -1: 2})
{"aaa'a'": 1
, "bbb'b'": (1+0j)
, "ccc'c'": (1+0j)
, "ddd'd'": (1+0j)

#no aabb, bbdd???, ccdd
, "aac'c'": -1j
, "a'a'cc": 1j

, "aa'd'd'": 1j
, "aa'dd": -1j
, "bbcc'": 1j
, "b'b'cc'": -1j

=(ac'-a'c)(ibd+b'd -ib'd'-bd')
#ac'*+(...)
, "abc'd'": -1
, "abc'd": 1j
, "ab'c'd'": -1j
, "ab'c'd": (1+0j)

#a'c*-(...)
, "a'bcd'": (1+0j)
, "a'bcd": -1j
, "a'b'cd'": 1j
, "a'b'cd": (-1+0j)
}
mx_r8_7
Counter({-1j: 7, 1j: 7, 1: 4, -1: 2, (1-1j): 1, (1+1j): 1})
{"aaa'a'": 1
, "bbbb'": (1+0j)
, "ccc'c'": (1+0j)
, "dddd'": (1+0j)

, "aa'bb'": -1j
, "aa'dd'": -1j
, "bb'cc'": 1j
, "cc'dd'": 1j


, "aac'c'": -1j
, "a'a'cc": 1j


, "aa'bb": 1j
, "aa'dd": 1j
, "bb'dd": -1j
, "bbcc'": -1j
, "cc'dd": -1j
, "bbdd'": 1j


, "a'b'cd": -1j
, "a'bcd'": (-1+0j)
, "abc'd": (1-1j)
, "ab'c'd": -1
, "a'bcd": (1+1j)
, "abc'd'": 1j
}
"""






"""
mx4
		[a,    b,    c,   d
		;-d,   a',   b,   c'
		;-c', -d',   a',  b'
		;-b', -c,   -d',  a
		]
mx4
{
, "aaa'a'": 1
, "bbb'b'": 1
, "ddd'd'": 1
, "aa'cc'": 2-1
, "bb'dd'": 2-1
, "aa'cc'": 2-1

, "aa'b'd'": 1
, "aa'bd": 1

, "aabd'": 1
, "a'a'b'd": 1

, "ac'd'd'": 1
, "a'cdd": 1


, "acdd'": 1
, "a'c'dd'": 1



, "abb'c": -1
, "a'bb'c'": -1

, "abbc'": -1
, "a'b'b'c": -1

bc'-cd * b'c-c'd'
	no other parts
bd'-cc * b'd-c'c'
	used"ccc'c'": 1
, "bc'c'd'": -1
, "b'ccd": -1


b'c-cd * bc'-c'd'
	= cc'(b'-d)(b-d')
	no other parts
b'd'-cc' * bd-cc'
, "b'cc'd'": -1
, "bcc'd": -1
, "bb'dd'": 2-1
, "ccc'c'": 1

}
========

========save
mx4
{
,"aaa'a'": 1
, "aa'b'd'": 1
, "aabd'": 1
, "ac'd'd'": 1
, "aa'bd": 1
, "bbb'b'": 1
, "acdd'": 1
, "ccc'c'": 1
, "ddd'd'": 1
, "a'cdd": 1
, "a'c'dd'": 1
, "a'a'b'd": 1


, "abb'c": -1
, "abbc'": -1
, "bc'c'd'": -1
, "a'bb'c'": -1
, "b'ccd": -1
, "a'b'b'c": -1
, "b'cc'd'": -1
, "bcc'd": -1

, "aa'cc'": 2
, "bb'dd'": 2
}

"""
###########

"""
mx1
		[a,   b,   c,  d
		;-b', a', -d', c'
		;-c', d',  a', -b'
		;-d, -c,   b,  a
		]
		b=c=0;d=ia=i;a=1
{
ab'-c'd * a'b-cd'
==>> ab' +tib'sia = 0
==>> ab=0 or ts=1
, "ab'cd'": -2
, "a'bc'd": -2
, "aa'bb'": 2
, "cc'dd'": 2

a'c+bd' * ac'+b'd
==>> a'*tib-b*sia' == 0
==>> ab=0 or t=s
, "a'b'cd": 2
, "abc'd'": 2
, "aa'cc'": 2
, "bb'dd'": 2

aa+dd * a'a'+d'd'
==>> d=+-ia=sia
, "a'a'dd": 1
, "aad'd'": 1
, "aaa'a'": 1
, "ddd'd'": 1

bb+cc * b'b'+c'c'
==>> c=+-ib=tib
, "b'b'cc": 1
, "bbc'c'": 1
, "bbb'b'": 1
, "ccc'c'": 1
}
============:



=======save
{"aaa'a'": 1
, "bbb'b'": 1
, "ccc'c'": 1
, "ddd'd'": 1
, "aa'bb'": 2
, "aa'cc'": 2
, "bb'dd'": 2
, "cc'dd'": 2


, "ab'cd'": -2
, "a'bc'd": -2

, "a'b'cd": 2
, "abc'd'": 2

, "a'a'dd": 1
, "aad'd'": 1

, "b'b'cc": 1
, "bbc'c'": 1
}
"""










