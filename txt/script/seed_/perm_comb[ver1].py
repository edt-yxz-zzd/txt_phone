"""
perm_comb

perm_comb=permutations+combinations:
	combinations('ABCD', 2) --> AB AC AD
	permutations('ABCD', 2) --> AB AC AD BA BC
	perm_comb :: [a]->[uint]->[[{a}]]
	comb_comb :: [a]->{uint:uint}->[{{a}}]
	perm :: [a]->uint->[[a]]
	comb :: [a]->uint->[{a}]
	perm(it,n)~perm_comb(it,[1]*n)
	comb(it,n)~perm_comb(it,[n])

"""


from common_short_hand import *
from itertools import (
	permutations
	, product as product_
	, combinations
	, combinations_with_replacement
	)

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



def _t_perm_comb():
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




