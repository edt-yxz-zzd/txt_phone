"""
perm_comb
	e.g.
		to generate symmetric_poly of pattern a^3*b^3*c for generators [w,x,y,z]
			perm_comb(4,[2,1])

perm_comb=permutations+combinations:
	combinations('ABCD', 2) --> AB AC AD
	permutations('ABCD', 2) --> AB AC AD BA BC
	perm_comb :: [a]->[uint]->[[{a}]]
	comb_comb :: [a]->{uint:uint}->[{{a}}]
	perm_comb_comb :: [a]->[(uint,uint)]->[[{{a}}]]
	perm :: [a]->uint->[[a]]
	comb :: [a]->uint->[{a}]
	perm(n,r)
		~perm_comb(n,[1]*r)
		~perm_comb_comb(n, [(1,1)]*r)
	comb(n,r)
		~perm_comb(n,[r])
		~comb_comb(n,{1:r})
		~comb_comb(n,{r:1})
		~perm_comb_comb(n, [(r,1)or(1,r)])
	perm_comb(n,rs)
		~perm_comb_comb(n, [(r,1)or(1,r) for r in rs])
	comb_comb(n,z2r)
		~perm_comb_comb(n, [(z,r) for z,r in z2r.items()])


comb  <
combr <=
perm  ><
permr >=<

???patternr<combr,permr>???
pattern<comb,perm>
	= 0
	| 1
	| ordered_list
			{refs :: [(pattern, uint)]
			,unordered_channel_idc
				:: [uint{%m}]
				:: [(@ri::uint{%len(refs)}, uint{%refs[ri][1]})]
				where m = sum(map snd refs)
			}


pattern
	= 0|1|([(sf, u)], [(u%,u%)])
		#_list:([(ref,num_cs)], [(ri,ci)])
		#_list:(ref2nc, rici)
std_pattern
	= 0|1
	|(u2=, sf1, u2)
		#_set:(sz,ref,count)
	#|(u2=, [(sf1:u1)],u2=, [(u%,u%)], [(sf2=:[u2=])])
		#_list:(sz,[(ref:num_cs)],num_cs, [(ri,ci)], [(ref:[count])])
		#_list:(sz,ref2nc,nc, rici, ref2cts)
	|(u2=, [(sf1:u1)],u2=, [(u%,u%)], ri_sf2=,[[u2=]])
		#_list:(sz,[(ref:num_cs)],num_cs, [(ri,ci)], ri_sf2,[[count]])
		#_list:(sz,ref2nc,nc, rici, ri_sf2,ctss)
		

std_pattern
	= 0
	| std_pattern_ge1
std_pattern_ge1
	= 1
	| std_pattern_ge2
	
std_pattern_ge2
	= std_pattern_ge2__unordered_set
	| std_pattern_ge2__ordered_list

std_pattern_ge2__unordered_set
			{sz :: uint{>=2}
				== _count*ref.sz
			,ref :: std_pattern_ge1
			,unordered_channel_count
				:: uint{>=2}
				if <=1: not "unordered_set"
				num_unordered_channels==1
			}
std_pattern_ge2__ordered_list
			{sz :: uint{>=2}
				== sum [sz| idx<-..._idc
							, ri = _idx2ref_idx[idx]
							, (p,_) = sorted_refs[ri]
							, sz = 1 if p==1 else p.sz
							]
			,refs
				:: {std_pattern_ge1: uint{>=1}}{len>=1}
			,unordered_channel_idx2count
				:: [uint{>=1}]{len=num_unordered_channels}
				== [_idc.count(i) | i<-[0..?]]
				1:uint{>=1}
				std_pattern_ge2: uint{>=2}
					if ==1: unpack
			,sorted_refs
				:: [(std_pattern_ge1, uint)]
				== sorted(refs.items())
			,unordered_channel_idx2ref_idx
				:: [uint{%len(refs)}]{len=num_unordered_channels}
			,num_unordered_channels
				:: uint{>=2}
				== sum(refs.values())
				if ==1:
					not "ordered_list"
					see "unordered_set"
			,unordered_channel_idc
				:: [uint{%num_unordered_channels}]
				set(unordered_channel_idc
					) == set(rg(num_unordered_channels))
			}



"""


from common_short_hand import *
from seed.iters.is_sorted import is_sorted
from itertools import (
	permutations
	, product as product_
	, combinations
	, combinations_with_replacement
	)
from collections import Counter
#perm_comb :: [a]->[uint]->[[{a}]]
#comb_comb :: [a]->{uint:uint}->[{{a}}]




#product==_permutations_with_replacement
def _combinations_with_replacement(n, r):
	# combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
	# :: uint -> uint -> [[uint]]
	# :: uint -> uint -> sorted_lt[sorted_le[uint]]
	# :: @n:uint. @r:uint. sorted_lt[sorted_le[uint{%n}]{len=r}]
	range(r,n)
	if n<0 or r<0 or (n==0 and r>0):
		return
	
	indices = [0] * r
	yield tuple(indices)
	n1 = n-1
	while True:
		for i in reversed(range(r)):
			if indices[i] != n1:
				break
		else:
			return
		indices[i:] = [indices[i] + 1] * (r - i)
		yield tuple(indices)
#product==_permutations_with_replacement
def _permutations_with_replacement(n, r):
	# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
	# :: uint -> uint -> [[uint]]
	# :: uint -> uint -> sorted_lt[[uint]]
	# :: @n:uint. @r:uint. sorted_lt[[uint{%n}]{len=r}]
	range(r,n)
	if n<0 or r<0 or (n==0 and r>0):
		return
	
	indices = [0] * r
	yield tuple(indices)
	n1 = n-1
	while True:
		for i in reversed(range(r)):
			if indices[i] != n1:
				break
		else:
			return
		indices[i] += 1
		indices[i+1:] = [0] * (r-1 - i)
		yield tuple(indices)

def _combinations(n, r):
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# combinations(range(4), 3) --> 012 013 023 123
	# :: uint -> uint -> [{uint}]
	# :: uint -> uint -> [[uint]]
	# :: uint -> uint -> sorted_lt[sorted_lt[uint]]
	# :: @n:uint. @r:uint. sorted_lt[sorted_lt[uint{%n}]{len=r}]
	range(r,n)
	it = _combinations_with_replacement(n-r+1, r)
	rs = range(r)
	for indices in it:
		yield tuple(map(opss.add, rs, indices))

def _permutations(n, r):
	# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
	# permutations(range(3)) --> 012 021 102 120 201 210
	# :: uint -> uint -> [[uint]]
	# :: uint -> uint -> sorted_lt[unique[uint]]
	# :: @n:uint. @r:uint. sorted_lt[unique[uint{%n}]{len=r}]
	range(r,n)
	if not 0 <= r <= n:
		return
	
	idc = list(range(n))
	#js = list(range(1, r+1))
	js = [nnn]*r
	i = 0
	"""
	0 <= i <= r
	idc[:i] fixed
	idc[i:] sorted_lt
	[n>=i'>=i>0]:
		j = js[i'-1]
		0 <= i'-1 < j <= n
		k = idc[i'-1]
		idc[j-1] <= k
		[j<n]:
			idc[j-1] <= k < idc[j]
			[i'<j]:
				idc[j-1] < k < idc[j]
			
	"""
	
	while 1:
		if i < r:
			assert 0 <= i < r
			js[i:] = rg(i+1, r+1)
			assert len(js) == r
			i = r
		else:
			assert 0 <= i == r
			yield tuple(idc[:r])
			for i1 in reversed(rg(i)):
				j = js[i1]
				assert 0 <= i1 < j <= n
				if j != n: break
			else:
				assert idc[:r] == list(reversed(rg(n-r, n)))
				#pr(idc[:r])
				break#return
			assert 0 < i == r
			assert 0 <= i1 < j < n
			#idc[new_i:i] dec
			#idc[i:] inc
			#if new_i != i != n: idc[i-1] > idc[n-1]
			#if __debug__:
			new_i1 = i1
			new_i = i1+1
			assert 0 < new_i <= i == r
			try:
				assert all(idc[x] > idc[x+1] for x in rg(new_i, i-1))
				assert not new_i<i<n or idc[i-1] > idc[n-1]
				#too slow:assert all(idc[x] < idc[x+1] for x in rg(i, n-1))
				if new_i < i:
					assert all(idc[x] < idc[x+1] for x in rg(i, n-1))
			except:
				prn("n,r; i,new_i,j; js; idc", locs())
				raise
			#swap i1,j
			#before swap, restore idc[i1+1:]
			
			if new_i < i:
				#restore idc[new_i:]
				#bug: idc[new_i:] = idc[i:] + idc[new_i:i]
				idc[new_i:] = [*idc[i:], *reversed(idc[new_i:i])]
				assert len(idc) == n
			
			i = new_i
			#swap i1,j
			try:
				if i==j:
					assert idc[j-1] == idc[i1] < idc[j]
				else:
					assert idc[j-1] < idc[i1] < idc[j]
			except:
				prn("n,r; i,j; js; idc", locs())
				raise
			idc[i1], idc[j] = idc[j], idc[i1]
			js[i1] = j+1

def _ts(f, g):
	for n in rg(0, 5):
		for r in rg(0, 5):
			[*a] = f(rg(n), r)
			[*b] = g(n, r)
			try:
				assert a==b
			except:
				pr(f, g)
				pr(n, r)
				pr(a)
				pr(b)
				raise

def __product(it, r):
	return product_(it, repeat=r)
def _tss():
	_ts(combinations, _combinations)
	_ts(permutations, _permutations)
	_ts(combinations_with_replacement, _combinations_with_replacement)
	_ts(__product, _permutations_with_replacement)


##############
def perm_comb(n, rs):
	# perm_comb(4, [2,1]) --> 012 013 021 023 031 032 120 123 130 132 230 231
	# :: uint -> [uint] -> [[uint]]
	# :: uint -> [uint] -> sorted_lt[unique[uint]{as[{uint}]}]
	# :: @n:uint. @rs:[uint]. sorted_lt[unique[uint{%n}]{len=sum(rs)}{as[{uint}]}]
	rs = (*rs,)
	r = sum(rs)
	for r_ in rs: range(r_,n)
	if not (0 <= r <= n
				and all(r_ >= 0 for r_ in rs)
				):
		return
	
	i2sz = [
		sz
		for r_ in rs
		for sz in reversed(rg(r_))
		]
		# remain size of block that cover index i
	
		
	#############
	idc = list(range(n))
	#js = list(range(1, r+1))
	js = [nnn]*r
	i = 0
	"""
	0 <= i <= r
	idc[:i] fixed
	idc[i:] sorted_lt
	[n>=i'>=i>0]:
		j = js[i'-1]
		0 <= i'-1 < j <= n
		k = idc[i'-1]
		idc[j-1] <= k
		[j<n]:
			idc[j-1] <= k < idc[j]
			[i'<j]:
				idc[j-1] < k < idc[j]
			
	"""
	
	while 1:
		if i < r:
			assert 0 <= i < r
			js[i:] = rg(i+1, r+1)
			assert len(js) == r
			i = r
		else:
			assert 0 <= i == r
			yield tuple(idc[:r])
			for i1 in reversed(rg(i)):
				j = js[i1]
				sz = i2sz[i1]
				assert 0 <= i1 < j <= n
				if j+sz != n:
					assert j+sz < n
					break
			else:
				if __debug__:
					ls = list(reversed(rg(n-r, n)))
					y = 0
					for r_ in rs:
						x = y
						y += r_
						try:
							assert 0 <= x <= y <= r == len(ls) <= n
						except:
							#fail???:pr('len(ls)={len(ls)}'.format(ls=ls))
							#fail???:pr('len(ls)={len(ls)!r}'.format(ls=ls))
							prn('x,y,r,ls,n', locs())
							raise
						rvs(ls, x,y)
					assert idc[:r] == ls
				#pr(idc[:r])
				break#return
			assert 0 < i == r
			assert 0 <= i1 < j < n
			#idc[new_i:i] blocks dec # inc per block
			#idc[i:] inc # last big block, min
			
			new_i1 = i1
			new_i = i1+1
			assert 0 < new_i <= i == r
			# mk ss
			if 1:
					ss = []
					_b = new_i
					while _b < i:
						_e = _b+i2sz[_b]+1
						if _e > i:
							_e = i
						ss.append((_b,_e))
						_b = _e
					if i < n:
						ss.append((i,n))
			if __debug__ and new_i < i:
				try:
					for _b,_e in ss:
						for _i in rg(_b,_e-1):
							assert idc[_i] < idc[_i+1]
					for x in rg(len(ss)-1):
						_pre_b = ss[x][0]
						_e = ss[x+1][1]
						assert idc[_pre_b] > idc[_e-1]
						
				except:
					prn("n,r; i,new_i,j; js; idc", locs())
					raise
			#swap i1,j
			#before swap, restore idc[i1+1:]
			
			if new_i < i:
				#restore idc[new_i:]
				for _b,_e in ss:
					rvs(idc, _b,_e)
				rvs(idc, new_i, n)
				assert len(idc) == n
				assert all(idc[x] < idc[x+1] for x in rg(new_i, n-1))
			
			i = new_i
			#swap i1,j
			try:
				if i==j:
					assert idc[j-1] == idc[i1] < idc[j]
				else:
					assert idc[j-1] < idc[i1] < idc[j]
			except:
				prn("n,r; i,j; js; idc", locs())
				raise
			idc[i1], idc[j] = idc[j], idc[i1]
			js[i1] = j+1
			###########
			###########
			###########
			sz = i2sz[i1]
			if sz:
				# idc[i1] is update
				# now fill the tail of curr block
				jj = js[i1]
				if i < jj:
					#(i,jj,jj+sz) >> sz
					lshf(idc, -sz, i,jj+sz)
				js[i:i+sz] = rg(jj+1, jj+sz+1)
				assert len(js) == r
				i += sz



def _t_perm_comb(perm_comb=perm_comb):
	# perm_comb(4, [2,1]) --> 012 013 021 023 031 032 120 123 130 132 230 231
	ts = [
		#n,rs,ans
		(4, [0,2,0,0,1,0]
			, [(*map(int, s),)
				for s in "012 013 021 023 031 032 120 123 130 132 230 231"
				.split()
				]
		),(0,[0,0,0]
				,[()]
		),(0,[1]
				,[]
		),(1,[1,0]
				,[(0,)]
		#),(5, [2,2,0,1],[]
		)
		]
	ts += [
		(n, [1]*r
			,[*permutations(rg(n), r)]
		)
		for n in rg(5)
		for r in rg(5)
		]
	ts += [
		(n, [r]
			,[*combinations(rg(n), r)]
		)
		for n in rg(5)
		for r in rg(5)
		]
	

	for n,rs,ans in ts:
		[*r] = perm_comb(n, rs)
		try:
			assert r==ans
		except:
			prn('n,rs;ans;r', locs())
			raise


if __name__ == "__main__":
	_tss()
	_t_perm_comb()


















###############


"""
pattern
	= 0|1|([(sf, u)], [(u%,u%)])
		#_list:([(ref,num_cs)], [(ri,ci)])
		#_list:(ref2nc, rici)
impattern
	= (0,)|(1,)|(sz=,[(sf, u)], [(u%,u%)])
		# for sort
std_pattern
	= 0|1
	|(u2=, sf1, u2)
		#_set:(sz,ref,count)
	#|(u2=, [(sf1:u1)],u2=, [(u%,u%)], [(ri_sf2=:[u2=])])
		#_list:(sz,[(ref:num_cs)],num_cs, [(ri,ci)], [(ri:[count])])
		#_list:(sz,ref2nc,nc, rici, ri2cts)
	|(u2=, [(sf1:u1)],u2=, [(u%,u%)], ri_sf2=,[[u2=]])
		#_list:(sz,[(ref:num_cs)],num_cs, [(ri,ci)], ri_sf2,[[count]])
		#_list:(sz,ref2nc,nc, rici, ri_sf2,ctss)
		
std_impattern
	= (0, g.em)|(1, g.sl)|(sz, g.us, g.ol...std_pattern)
"""
class g:
	# case for sort
	# fail:[(1,),((),)].sort()
	em = -1 #empty
	sl = -2 #single
	us = -3 #unordered_set
	ol = -4 #ordered_list
_01 = (0,1)
def _2ps(it):
	return tpl((i,j) for i,j in it)

class pattern2std:
	def _mk_imp_01(sf, sz):
		if sz == 0:
			case = g.em
		elif sz == 1:
			case = g.sl
		else:
			raise eee
		return (sz, case)
	def _imp_ver1_to_ver2(sf, p):
		s = len(p)
		if s==1:
			[sz] = p
			p_ = sf._mk_imp_01(sz)
		elif s==3:
			(sz,ref,count) = p
			p_ = (sz,g.us,ref,count)
		else:
			(sz,ref2nc,nc, rici, ri_sf2,ctss) = p
			p_ = (sz,g.ol,ref2nc,nc, rici, ri_sf2,ctss)
		return p_
	def pattern2std_impattern(sf, pattern):
		p = sf.pattern2impattern(pattern)
		return sf.impattern2std(p)
	def impattern2std(sf, impattern):
		p1 = sf._impattern2std_v1(impattern)
		p2 = sf._imp_ver1_to_ver2(p1)
		return p2
	def _impattern2std_v1(sf, impattern):
		p = impattern
		sz = p[0]
		if sz < 2:
			assert p == (sz,)
			return p
		f = sf.impattern2std
		(sz, ref2nc, rici) = p
		
		t1t3 = sf._ref2nc_rici_f_to_t1t3(
			ref2nc, rici, f)
		if sz != t1t3[0]: raise eee
		
		(_, ref2nc, rici) = t1t3
		assert sz >= 2
		
		# unpack sf2 channel(rc) count <2
		rc2ct = Counter(rici)
		#prn("rc2ct;rici;ref2nc;;;", locs())
		rici_ = []
		ref2nc_ = [*ref2nc]
		for rc in rici:
			r,_ = rc
			ref,_ = ref2nc[r]
				#bug:once ref2nc be hidden
			sz = ref[0]
			ct = rc2ct[rc]
			#pr(1,ref)
			if sz >= 2 and ct < 2:
				assert ct==1
				#unpack
				r_ = len(ref2nc_)
				if len(ref)==4:#3:
					(_,_,ref,count)=ref
					assert count>=2
					ref2nc_.append((ref,1))
					rici_ += [(r_,0)]*count
				else:
					#pr(2,ref)
					(sz,_,_ref2nc,nc, _rici, ri_sf2,ctss)=ref
					ref2nc_ += _ref2nc
					rici_ += [(r+r_,c)for r,c in _rici]
			else:
				rici_.append(rc)
		rici = rici_
		ref2nc = ref2nc_
		
		t1t3 = sf._ref2nc_rici_f_to_t1t3(
			ref2nc, rici, id)
		(sz, ref2nc, rici) = t1t3
		
		assert sz >= 2
		if len(ref2nc)==1:
			[(ref,nc)] = ref2nc
			if nc == 1:
				#(u2=, sf1, u2)
				#_set:(sz,ref,count)
				count = len(rici)
				assert rici == ((0,0),)*count
				assert count
				if count >= 2:
					new_p = (sz, ref, count)
				else:
					new_p = ref
				return new_p
		#######(sz,ref,count)(sz,ref2nc,nc, rici, ri_sf2,ctss)
		#(u2=, [(sf1:u1)],u2=, [(u%,u%)], ri_sf2=,[[u2=]])
		#_list:(sz,[(ref:num_cs)],num_cs, [(ri,ci)], ri_sf2,[[count]])
		#_list:(sz,ref2nc,nc, rici, ri_sf2,ctss)
		(sz,ref2nc, rici)
		nc = sum(map(snd, ref2nc))
		assert nc == len(set(rici))
		ri_sf2 = -1
		for ri_sf2, (ref,_) in enm(ref2nc):
			if ref[0] >= 2:
				break
		else:
			ri_sf2 += 1
		ctss = [
			[0]*nc
			for _,nc in ref2nc[ri_sf2:]
			]
		for r,c in rici:
			if ri_sf2 <= r:
				ctss[r-ri_sf2][c] += 1
		ctss = (*map(tpl, ctss),)
		try:
			assert all(ct >= 2 for cts in ctss for ct in cts)
		except:
			prn("ctss;ri_sf2;rici;ref2nc;", locs())
			raise
		new_p = (sz,ref2nc,nc, rici, ri_sf2,ctss)
		return new_p
	def pattern2impattern(sf, p):
		# pattern->impattern
		if p in _01:
			sz = _01[p]
			return (sz,)
		
		f = sf.pattern2impattern
		(ref2nc, rici) = p
		rici = _2ps(rici)
		ref2nc = _2ps(ref2nc)
		
		return sf._ref2nc_rici_f_to_t1t3(
			ref2nc, rici, f)
	def _ref2nc_rici_f_to_t1t3(
			sf, ref2nc, rici, f):
		# -> (sz,)|(sz, ref2nc, rici)
		ref2nc, rici
		rr = len(ref2nc)
		for ri,ci in rici:
			if not 0<=ri<rr:raise eee
			ref,nc = ref2nc[ri]
			if not 0<=ci<nc:raise eee
		#r2sz = [nnn]*rr
		r2p = [nnn]*rr
		for r,_ in rici:
			if r2p[r] is nnn:
				p,_ = ref2nc[r]
				p = f(p)
				assert p is not nnn
				r2p[r] = p
				#r2sz[r] = sz
		# remove sz=0
		for r,_ in rici:
			p = r2p[r]
			if p is not nnn and p[0] == 0:
				r2p[r] = nnn
				#r2sz[r] = nnn
		return sf._rici_r2may_p_to_t1t3(
			rici, r2p)
	def _rici_r2may_p_to_t1t3(
			sf, rici, r2may_p):
		# -> (sz,)|(sz, ref2nc, rici)
		r2p = r2may_p # p is imp...
		rici
		rici = [rc for rc in rici if r2p[rc[0]] is not nnn]
		sz = sum(r2p[rc[0]][0] for rc in rici)
		if sz < 2:
			sz = _01[sz]
			return (sz,)
		(ref2nc, rici
		)=sf._rici_r2may_p_to_ref2nc_rici(
			rici, r2p)
		new_p = (sz, ref2nc, rici)
		return new_p
	def _rici_r2may_p_to_ref2nc_rici(
			sf, rici, r2may_p):
		r2p = r2may_p # p is imp...
		rici
		k2p = sorted(set(filter(nnn, r2p)))
		p2k = {p:k for k,p in enm(k2p)}
		r2k = [p2k[p] if p else nnn for p in r2p]
		
		kk = len(k2p)
		k2rc2j = [{} for _ in rg(kk)]
		for rc in rici:
			ri,ci = rc
			k = r2k[ri]
			rc2j = k2rc2j[k]
			if rc not in rc2j:
				j = len(rc2j)
				rc2j[rc] = j
			#j = rc2j[rc]
		rici = [(k,j)
			for rc in rici
			for r in [rc[0]]
			for k in [r2k[r]]
			for j in [k2rc2j[k][rc]]
			]
		ref2nc = [
			(k2p[k], len(rc2j))
			for k,rc2j in enm(k2rc2j)
			]
		
		ref2nc = (*ref2nc,)
		rici = (*rici,)
		return ref2nc, rici



"""

pattern
	= 0|1|([(sf, u)], [(u%,u%)])
		#_list:([(ref,num_cs)], [(ri,ci)])
		#_list:(ref2nc, rici)
"""
def _t_pattern2std():
		sf = pattern2std()
		f=sf.pattern2std_impattern
		sf.impattern2std
		sf.pattern2impattern
		ts = [
			0,1
			,([(0,0),(0,2),(1,1),(1,4)]
				, [(1,1),(3,3),(2,0)]
				)
			,([(([(1,1)],[(0,0),(0,0)]), 3)]
				,[(0,0),(0,1),(0,0),(0,2)]
				)
			,([(([(1,2)],[(0,0),(0,1)]), 3)]
				,[(0,0),(0,1)]
				)
			]
		rs = [
			(0,-1)
			,(1,-2)
			#(2, (((1,), 2),), 2, ((0, 0), (0, 1)), 1, [])
			,(2,-4
				, (((1,-2), 2),)
				, 2
				, ((0, 0), (0, 1))
				, 1, ()
				)
			#(8, (((1,), 2), ((2, (1,), 2), 1)), 3, ((1, 0), (0, 0), (0, 0), (1, 0), (0, 1), (0, 1)), 1, [[2]])
			,(8,-4
				, (((1,-2), 2)
					,((2,-3, (1,-2), 2), 1)
					)
					, 3
					, ((1, 0), (0, 0), (0, 0), (1, 0), (0, 1), (0, 1))
					, 1, ((2,),)
					)
			#(4, -4, (((1, -2), 4),), 4, ((0, 0), (0, 1), (0, 2), (0, 3)), 1, ())
			,(4, -4
				, (((1, -2), 4),)
				, 4
				, ((0, 0), (0, 1), (0, 2), (0, 3))
				, 1, ())
			]
		rs += [()]*100
		for p,ans in zip(ts,rs):
			ip = f(p)
			#prn("p;ans;ip", locs())
			try:
				assert ip==ans
			except:
				prn("p;ans;ip", locs())
				#return
				raise
		return

_t_pattern2std()
p=0
ip=(0,)
p=1
ip=(1,)
p=([(0, 0), (0, 2), (1, 1), (1, 4)], [(1, 1), (3, 3), (2, 0)])
ip=(2, (((1,), 2),), 2, ((0, 0), (0, 1)), 1, [])
p=([(([(1, 1)], [(0, 0), (0, 0)]), 3)], [(0, 0), (0, 1), (0, 0), (0, 2)])
ip=(8, (((1,), 2), ((2, (1,), 2), 1)), 3, ((1, 0), (0, 0), (0, 0), (1, 0), (0, 1), (0, 1)), 1, [[2]])
p=([(([(1, 2)], [(0, 0), (0, 1)]), 3)], [(0, 0), (0, 1)])
ip=(4, -4, (((1, -2), 4),), 4, ((0, 0), (0, 1), (0, 2), (0, 3)), 1, ())


























##############
def perm_comb_comb__def(n, rcs):
	rcs = [(r,c) for r,c in rcs]
	for r,c in rcs:
		if r<0 or c<0:return
	rr = sum(r*c for r,c in rcs)
	for t in permutations(rg(n),rr):
		i = 0
		for r,c in rcs:
			j = i+r*c
			ls = t[i:j]
			i = j
			mx = ls2mx(ls, r)
			if not (is_sorted(mx)
					and all(map(is_sorted, mx))
					):
				break
		else:
			yield t

def perm_comb_comb(n, rcs):
	# perm_comb_comb(4, [(2,1),(1,1)]) --> 012 013 021 023 031 032 120 123 130 132 230 231
	# :: uint -> [(uint,uint)] -> [[uint]]
	# :: uint -> [(uint,uint)] -> sorted_lt[unique[uint]{as[{{uint}}]}]
	# :: @n:uint. @rcs:[(uint,uint)]. sorted_lt[unique[uint{%n}]{len=sum(r*c for r,c in rcs)}{as[{{uint}{len=r}}{len=c}]}]
	return iter(perm_comb_comb_t(n, rcs))
class _eee(eee):pass
class perm_comb_comb_t:
	def __init__(sf, n, rcs):
		try:
			rcs = sf._std_rcs(rcs)
			rr = sum(r*c for r,c in rcs)
			if not 0 <= rr <= n: raise _eee
		except _eee:
			n = nnn
			rcs = nnn
		else:
			[sf._i2ib
			,sf._ib2iend
			,sf._ib2ibb
			,sf._ibb2ibend
			] = sf._mk_i2_ib2__(rcs)
			sf._rr = rr
			sf._lb = sum(c for r,c in rcs)
			sf._lbb = len(rcs)
			assert rr == len(sf._i2ib)
			assert sf._lb == len(sf._ib2iend)
			assert sf._lb == len(sf._ib2ibb)
			assert sf._lbb == len(sf._ibb2ibend)
		sf._n = n
		sf._rcs = rcs
		if n is not nnn:
			sf._i2xsz = [*map(sf.__i2xsz, rg(rr))]

	def _std_rcs(sf, rcs):
		(*rcs,) = ((r,c) for r,c in rcs if r and c)
		ls = []
		for r,c in rcs:
			if not (r>0 and c>0): raise _eee
			if r==1:
				r,c = c,r
			ls.append((r,c))
		rcs = (*ls,); del ls
		return rcs

	def _mk_i2_ib2__(sf, rcs):
		# block lens
		bls = [r for r,c in rcs for _ in rg(c)]
		# blockblock lens
		bbls = [c for r,c in rcs]
		
		i2ib, ib2iend = sf._mk_i2__(bls)
		ib2ibb, ibb2ibend = sf._mk_i2__(bbls)
		return i2ib, ib2iend, ib2ibb, ibb2ibend
	def _mk_i2__(sf, bls):
		if len(bls):
			i2ib = [ib for ib,bl in enm(bls) for _ in rg(bl)]
			new = lambda x:[x]
			def op(ls, x):
					ls.append(ls[-1]+x)
					return ls
			ib2iend = acc(bls, op=op, new=new)
			assert ib2iend[-1] == len(i2ib)
		else:
			i2ib = ib2iend = []
		i2ib = (*i2ib,)
		ib2iend = (*ib2iend,)
		return i2ib, ib2iend

	def i2ib(sf, i):
		return sf._i2ib[i]
	def ib2iend(sf, ib):
		return sf._ib2iend[ib]
	def ib2ibb(sf, ib):
		return sf._ib2ibb[ib]
	def ibb2ibend(sf, ibb):
		return sf._ibb2ibend[ibb]
	def i2ibb(sf, i):
		ib = sf.i2ib(i)
		ibb = sf.ib2ibb(ib)
		return ibb
	def ib2istart(sf, ib):
		istart = sf.ib2iend(ib-1) if ib else 0
		return istart
	"""
	def ibb2ibstart(sf, ibb):
		ibstart = sf.ibb2biend(ibb-1) if ibb else 0
		return ibstart
	def ibb2istart(sf, ibb):
		ibstart = sf.ibb2ibstart(ibb)
		istart = sf.ib2istart(ibstart)
		return istart
	"""
	def ibb2iend(sf, ibb):
		ibend = sf.ibb2ibend(ibb)
		iend = sf.ib2istart(ibend)
		return iend
	def i2bisz(sf, i):
		# isz : tail sz include i # >=1
		# bisz : isz of ib
		ib = sf.i2ib(i)
		iend = sf.ib2iend(ib)
		isz = iend - i
		return isz
	def i2bbisz(sf, i):
		# isz : tail sz include i # >=1
		# bbisz : isz of ibb
		ibb = sf.i2ibb(i)
		iend = sf.ibb2iend(ibb)
		isz = iend - i
		return isz
	"""
	def i2ibistart(sf, i):
		# i to istart of ib
		ib = sf.i2ib(i)
		istart = sf.ib2istart(ib)
		return istart
	"""
	def __i2isz(sf, i):
		# isz : tail sz include i # >=1
		if sf.is_ibistart(i):
			f = sf.i2bbisz
		else:
			f = sf.i2bisz
		isz = f(i)
		assert isz >= 1
		return isz
	def __i2xsz(sf, i):
		# xsz : tail sz exclude i # >=0
		isz = sf.__i2isz(i)
		xsz = isz -1
		assert xsz >= 0
		return xsz
	def i2xsz(sf, i):
		return sf._i2xsz[i]
	def i2isz(sf, i):
		return sf.i2xsz(i) +1
	def i2r(sf, i):
		ibb = sf.i2ibb(i)
		r,c = sf._rcs[ibb]
		return r
	def is_ibistart(sf, i):
		return sf.i2r(i) == sf.i2bisz(i)
		return i == sf.i2ibistart(i)
	def is_ibbistart(sf, i):
		ibb = sf.i2ibb(i)
		r,c = sf._rcs[ibb]
		return r*c == sf.i2bbisz(i)
	def mk_end_st(sf):
		ls = []
		n_ = sf._n
		for r,c in sf._rcs:
			n_ -= r*c
			sf._ex_rc(ls, n_, r,c)
		return (*ls,)
	def _ex_rc(sf, ls, n_, r,c):
		fsts = rg(n_, n_+c)
		if r==1:
			assert c==1
			ls += fsts
		else:
			#bug:@r==1
			snds = rvd(rg(n_+c, n_+r*c, r-1))
			for fst, snd in zip(fsts, snds):
				ls += [fst, *rg(snd, snd+r-1)]

	def _restore_idc_new_i_n(sf, idc, new_i):
		rr = sf._rr
		rcs = sf._rcs
		#n = sf._n
		assert new_i < rr

		ib0 = sf.i2ib(new_i)
		ibb0 = sf.ib2ibb(ib0)
		is_ibi0 = bool(sf.is_ibistart(new_i))
		is_ibbi0 = bool(sf.is_ibbistart(new_i))

		ls = idc[rr:]; del idc[rr:]
		def fibb(ibb):
			r,c = rcs[ibb]
			_f_rc(r,c)
		def _f_rc(r,c):
			nonlocal ls
			#bug:@c==0
			if c==0: return
			ls += idc[-r*c::r]
			if r==1:
				assert c==1
				idc.pop()
			else:
				for _ in rg(c):
					ls += idc[1-r:]
					del idc[-r:]
		def fib(ibb, ib):
			r,c = rcs[ibb]
			if 1:
				ibend = sf.ibb2ibend(ibb)
				c = ibend-ib
			else:
				#bug: @ib == ibb.end
				i0 = sf.ib2istart(ib)
				assert sf.i2ibb(i0) == ibb
				bbisz = sf.i2bbisz(i0)
				c = bbisz//r
				assert r*c == bbisz
			_f_rc(r,c)
		def fi(ib, i):
			nonlocal ls
			if 1:
				#i is not i0
				bisz = isz = sf.i2isz(i)
			else:
				bisz = sf.i2bisz(i)
			ls += idc[-bisz:]
			del idc[-bisz:]
		########
		for ibb in rvd(rg(ibb0+1-is_ibbi0, sf._lbb)):
			fibb(ibb)
		if not is_ibbi0:
			fib(ibb0, ib0+1-is_ibi0)
			if not is_ibi0:
				fi(ib0, new_i)
		########
		idc += ls
		assert len(idc) == sf._n





	def __check(sf, n, rr, idc, js, i):
		return tt
		try:
			return sf.___check(n, rr, idc, js, i)
		except:
			prn("n,rr,i;idc;js;", locs())
			raise
	def ___check(sf, n, rr, idc, js, i):
		assert len(idc) == n
		assert len(js) == rr
		assert 0 <= i <= rr <= n
		assert is_sorted(idc[i:])
		assert set(idc) == set(rg(n))
		for i1, a in enm(idc[:i]):
			j = js[i1]
			assert i1 < j <= n
			k = sum(a<b for b in idc[i1+1:])
			assert j+k == n
		if i:
			xsz = sf.i2bbisz(i-1)-1
			ls = idc[:i]
			ls += rg(n,n+xsz)
			i1 = len(ls) -1
			ibb1 = sf.i2ibb(i1)
			for ibb in rg(ibb1+1):
				sf.__check_ibb(ibb, ls)
		return tt
	def __check_ibb(sf, ibb, idc_):
		r,c = sf._rcs[ibb]
		iend = sf.ibb2iend(ibb)
		istart = iend-r*c
		assert is_sorted(idc_[istart:iend:r])
		for i in rg(istart, iend, r):
			assert is_sorted(idc_[i:i+r])
		return tt
	def __iter__(sf):
		n = sf._n
		if n is nnn:
			return
		rr = sf._rr
		i2xsz = sf.i2xsz
		#############
		idc = list(range(n))
		#js = list(range(1, rr+1))
		js = [nnn]*rr
		i = 0
		"""
		0 <= i <= rr
		idc[:i] fixed
		idc[i:] sorted_lt
		[n>=i'>=i>0]:
			j = js[i'-1]
			0 <= i'-1 < j <= n
			k = idc[i'-1]
			idc[j-1] <= k
			[j<n]:
				idc[j-1] <= k < idc[j]
				[i'<j]:
					idc[j-1] < k < idc[j]
				
		"""
		
		while 1:
			assert sf.__check(n, rr, idc, js, i)
			if i < rr:
				assert 0 <= i < rr
				js[i:] = rg(i+1, rr+1)
				assert len(js) == rr
				i = rr
			else:
				assert 0 <= i == rr
				yield tuple(idc[:rr])
				for i1 in reversed(rg(i)):
					j = js[i1]
					xsz = i2xsz(i1)
					assert 0 <= i1 < j <= n
					if j+xsz != n:
						assert j+xsz < n
						break
				else:
					assert (*idc[:rr],) == sf.mk_end_st()
					assert idc[rr:] == [*rg(n-rr)]
					#pr(idc[:rr])
					break#return
				assert 0 < i == rr
				assert 0 <= i1 < j < n
				#idc[new_i:i] block[2:]s dec;block[0]s inc # inc per block
				#idc[i:] inc # last big block, min
				
				new_i1 = i1
				new_i = i1+1
				assert 0 < new_i <= i == rr
				#swap i1,j
				#before swap, restore idc[i1+1:]
				
				if new_i < i:
					#restore idc[new_i:]
					sf._restore_idc_new_i_n(idc, new_i)
					assert len(idc) == n
					assert all(idc[x] < idc[x+1] for x in rg(new_i, n-1))
				
				i = new_i
				assert sf.__check(n, rr, idc, js, i)
				#swap i1,j
				try:
					if i==j:
						assert idc[j-1] == idc[i1] < idc[j]
					else:
						assert idc[j-1] < idc[i1] < idc[j]
				except:
					prn("n,rr; i,j; js; idc", locs())
					raise
				idc[i1], idc[j] = idc[j], idc[i1]
				js[i1] = j+1
				assert sf.__check(n, rr, idc, js, i)
				###########
				###########
				###########
				# idc[i1] is update
				# now fill the tail of curr ibb of i1
				if i==rr: continue
				ib = sf.i2ib(i)
				ib1 = sf.i2ib(i1)
				if ib1 == ib:
					bisz = sf.i2bisz(i1)
					sz = bisz-1
					assert sz
					#if sz:
					jj = js[i1]
					sf.__swap(js, idc, i, jj, sz)
				else:
					sz = 0
				i2 = i+sz
				######
				######
				######
				if i2==rr:
					i = i2
					continue
				assert sf.__check(n, rr, idc, js, i2)
				ibb1 = sf.i2ibb(i1)
				ibb2 = sf.i2ibb(i2)
				if ibb1 == ibb2:
					bbisz = sf.i2bbisz(i2)
					sz = bbisz
					assert sz
					i10 = sf.ib2istart(ib1)
					a = idc[i10]
					jj = bisect_right(idc, a, i2)
					assert jj < n
					sf.__swap(js, idc, i2, jj, sz)
				else:
					sz = 0
				i3 = i2+sz
				#######
				#######
				#######
				#######
				i = i3
	def __swap(sf, js, idc, i, j, sz):
		assert i <= j <= j+sz <= len(idc)
		if i<j and sz:
			#
			#(i,j,j+sz) >> sz
			lshf(idc, -sz, i,j+sz)
		rr = len(js)
		js[i:i+sz] = rg(j+1, j+sz+1)
		assert len(js) == rr
from bisect import bisect_right



def _t_perm_comb_comb(perm_comb_comb=perm_comb_comb):
	# perm_comb_comb(n, [(r,1)for r in rs]) == perm_comb(n, rs)
	def perm_comb(n, rs):
		return perm_comb_comb(n, [(r,1)for r in rs])
	_t_perm_comb(perm_comb=perm_comb)

	f0 = perm_comb_comb__def
	f1 = perm_comb_comb
	ts = [
			6, [(1,3),(1,1),(0,5)]
			,8, [(2,3),(3,0)]
			,8, [(1,1),(2,2),(0,5)]
			]
	ts = ls2mx(ts, 2)
	for n, rcs in ts:
		[*r0] = f0(n, rcs)
		[*r1] = f1(n, rcs)
		try:
			assert r0==r1
		except:
			prn("n;ts;", locs)
			raise


if __name__ == "__main__":
	_t_perm_comb_comb()

