#primitive_polynomial_over_GF2


class Polynomial_over_GF2:
	#poly = (*sorted(exps),) :: sorted[uint]
	#@classmethod
	def from_exps(sf, exps):
		return (*sorted(exps),)
	def to_exps(sf, poly):
		return poly
	def get_poly__0(sf):
		return sf.from_exps(())
	def get_poly__1(sf):
		return sf.from_exps((0,))
	def get_poly__x(sf):
		return sf.from_exps((1,))
	
	def from_uint(sf, u):
		assert u>=0
		s = f"{u:b}"
		assert s.startswith("0b")
		#s = s[::-1]
		ls = []
		for i,c in enumerate(reversed(s)):
			if c=="1":
				ls.append(i)
		return (*ls,)
	def to_uint(sf, poly):
		if not poly:
			u = 0
		else:
			ls = [0]*(poly[-1]+1)
			for i in poly:
				ls[i] = 1
			s = ''.join(map(str, reversed(ls)))
			u = int(s, 2)
		return u
	def eq(sf, lhs, rhs):
		return len(lhs)==len(rhs) and all(a==b for a,b in zip(lhs, rhs))
	def sub(sf, lhs, rhs):
		return sf.add(lhs, rhs)
	def neg(sf, poly):
		return poly
	def add(sf, lhs, rhs):
		ls = []
		i = j = 0
		i = len(lhs)-1
		j = len(rhs)-1
		while i>=0 and j>=0:
			a = lhs[i]
			b = rhs[j]
			if a < b:
				ls.append(b)
				j -= 1
			elif a > b:
				ls.append(a)
				i -= 1
			#elif a == b:
			else:
				i -= 1
				j -= 1
		if i >= 0:
			init = lhs[i:]
		elif j >= 0:
			init = rhs[j:]
		else:
			init = []
			
		r = (*init, *ls[::-1])
		return r
	def mul(sf, lhs, rhs):
		if len(lhs) < len(rhs):
			lhs, rhs = rhs, lhs
		r = ()
		for e in rhs:
			s = [e+i for i in lhs]
			r = sf.add(r, s)
		return r
	def deg(sf, poly):
		if not poly:
			return None
		return poly[-1]
	def is_zero_poly(sf, poly):
		return not poly
	def exp2coeff(sf, poly, e):
		exps = poly
		if exps:
			i = bisect(exps, e)
			r = exps[i] == e
		else:
			r = 0
		return int(r)
	
	#def eval(sf, 
	def square(sf, poly, ee=1):
		#poly^2^ee
		_2e = 1<<ee
		return (*(_2e*e for e in poly),)
	def mod(sf, poly, m):
	def pow_mod(sf, poly, e, m):
def is_primitive_polynomial_over_GF2(ops, poly, int2factor2exp):
	#int2factor2exp(2**(deg f)-1)
	#
	if not ops.exp2coeff(0):
		return False
	
	n = ops.deg(poly)
	_x = ops.get_poly__x()
	_1 = ops.get_poly__1()
	
	eee = 2**n -1
	r = ops.pow_mod(_x, eee, poly)
	if not ops.eq(r, _1):
		return False
	
	
	p2e = int2factor2exp(eee)
	ps = sorted(p2e)
	for p in reversed(ps):
		ee = eee//p
		r = ops.pow_mod(_x, ee, poly)
		if ops.eq(r, _1):
			return False
	return True

	
	
	



