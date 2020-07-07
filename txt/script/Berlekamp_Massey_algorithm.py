r"""
Berlekamp–Massey algorithm



LFSR Linear Feedback Shift Register
	The period is maximal if and only if that polynomial is primitive.
Berlekamp–Massey algorithm


Berlekamp–Massey algorithm
	problem:
		input:
			kkk <: field
			ss :: [kkk]
				nnn := len ss
		output:
			cc :: [kkk]
				lll := len cc-1
				lll is min
				lll >= 0
				cc[0] = 1
				for i in [lll:nnn-1]:
					#0 == ss[i]+sum ss[i-j]*cc[j] {j=1..lll}
					0 == sum ss[i-j]*cc[j] {j=0..lll}
					

ss ==>> cc
[0]*n ==>> [1]
[0]*n + [x] + [0]*m ==>> [1]+[?]*(1+n)
[ss = [0]*n + [x] + [0]*m + [y]]
	* [n<=m]:
		==>> [cc = [1]+[0]*m+[-y/x]]
	* [n>m]:
		==>> [cc = [1]+[0]*m+[-y/x]+[?]*(n-m)]


"""

__all__ = """
	Berlekamp_Massey_algorithmABC
	Berlekamp_Massey_algorithm4fractions
	Berlekamp_Massey_algorithm4prime_field

	fraction2int
	fraction2int_mod

	mod
	gcd_ex
	ginv_mod
	inv_mod
	""".split()
	#main override debug_print


from abc import ABC, abstractmethod
import functools
import fractions # Fraction




"""
class Vector(ABC):
	def add_per_elem(sf, u, v):pass
	def mul_per_elem(sf, u, v):pass
	def from_iter(sf, it):pass
	def inner_product
"""

debug_print = print
def debug_print(*args, **kw): pass

def fraction2int_mod(fr, p):
	#n,d = fr.as_integer_ratio()
	n,d = fr.numerator, fr.denominator
	i = inv_mod(d,p)
	return mod(n*i,p)

def fraction2int(fr):
	#n,d = fr.as_integer_ratio()
	n,d = fr.numerator, fr.denominator
	if d != 1: raise ValueError(f"{fr} is not integer")
	return n



def gcd_ex(a,p):
	i,j = a,p
	a2i, p2i = 1,0
	a2j, p2j = 0,1
	while j:
		q,r = divmod(i,j)
		i,j = j,r
		a2r = a2i - q*a2j
		p2r = p2i - q*p2j
		a2i, p2i = a2j, p2j
		a2j, p2j = a2r, p2r
	if i < 0:
		i,a2i,p2i = -i,-a2i,-p2i
	g = i
	assert 0<=g==a2i*a + p2i*p
	if p==0:
		assert g==abs(a)
	if g==0:
		assert a==p==0
	assert g==fractions.gcd(a,p)
	return g,a2i,p2i

def mod(a, m):
	#assume a%0 === a
	return a%m if m else a
def ginv_mod(a,p):
	#if p == 0: raise ZeroDivisionError(f"??%{p}")
	g,a2i,p2i = gcd_ex(a,p)
	if p:
		g = g%p
		b = a2i%p
	else:
		b = a2i
		assert abs(b)==1
	assert 0<=g==mod(a*b, p)
	assert 0<=g<abs(p) if p else 0<=g==abs(a)
	return g,b

def inv_mod(a,p):
	g,b = ginv_mod(a, p)
	if g != mod(1,p): raise ZeroDivisionError(f"not coprime: gcd({a},{p})%{p} == {g} != 1%{p}")
		#(f"{p} is not prime: {p}={g}*{p//g}")
	#if g == 0: raise ZeroDivisionError(f"({a})**(-1) %{p}")
		#should after "if g != 1%p:"
	assert p==p//g *g if g else 0==a==p
	assert g==1 or (g==0 < 1==abs(p))
	assert mod(a*b,p) == mod(1,p)
	return b




class Berlekamp_Massey_algorithmABC(ABC):
	@abstractmethod
	def _field_add_(sf, a, b):pass
	@abstractmethod
	def _field_mul_(sf, a, b):pass
	@abstractmethod
	def _field_eq_(sf, a, b):pass
	@abstractmethod
	def _field_inv_(sf, a):pass
	@abstractmethod
	def _field_neg_(sf, a):pass

	@abstractmethod
	def _get_field_zero_(sf):pass
	@abstractmethod
	def _get_field_one_(sf):pass

	def _is_field_zero_(sf, a):
		_0 = sf._get_field_zero_()
		return sf._field_eq_(a, _0)

	def _field_div_(sf, a, b):
		d = sf._field_inv_(b)
		q = sf._field_mul_(a, d)
		return q
	def _field_sub_(sf, a, b):
		d = sf._field_neg_(b)
		q = sf._field_add_(a, d)
		return q


	def _field_sum_(sf, v):
		_0 = sf._get_field_zero_()
		r = functools.reduce(sf._field_add_, v, _0)
		return r
	def _field_num_mul_vec_(sf, a,v):
		mul = sf._field_mul_
		return [mul(a, x) for x in v]
	def _field_vec_add_(sf, u,v):
		w = map(sf._field_add_, u, v)
		return [*w]
	def _field_vec_inner_product_(sf, u,v):
		assert len(u) == len(v)
		w = map(sf._field_mul_, u, v)
		r = sf._field_sum_(w)
		return r







	def __init__(sf):
		_1 = sf._get_field_one_()
		sf.__ss = []
			# input
		sf.__cc = (_1,)
			#coeffs
			#[i<-[lll..]] ==>> [0 == sum ss[i-j]*cc[j] {j=0..lll}]
		sf.__lll = 0
			# ?? ==len(cc)-1
			# the current number of assumed errors
		sf.__prev_d = None #_1
			#first nonzero d since lll last updated
		sf.__prev_cc = sf.__cc
			#prev first cc since lll last updated
		sf.__m = 1
			# total iter since lll, prev_d, prev_cc last updated
		sf.__prev_i = -1
		assert sf.__lll == len(sf.__cc)-1
	def __calc_cc(sf, d):
		db = sf._field_div_(d, sf.__prev_d)
		_db = sf._field_neg_(db)
		_ee = sf._field_num_mul_vec_(_db, sf.__prev_cc)
		cc = sf.__cc
		m = sf.__m
		nee = m + len(_ee)
		ncc = len(cc)
		_0 = sf._get_field_zero_()
		_ee = [*[_0]*m, *_ee, *[_0]*(ncc-nee)]
		cc = [*cc, *[_0]*(nee-ncc)]
		cc = sf._field_vec_add_(cc, _ee)
		return tuple(cc)
	def __calc_d(sf):
		#bug: d = sf._field_vec_inner_product_(sf.__cc, sf.__ss[-len(sf.__cc):])
		cc = sf.get_coeffs()  # cut by lll
		ss = sf.__ss[-1:-len(cc)-1:-1] # reverse
		d = sf._field_vec_inner_product_(cc, ss)
		return d

	def feeds(sf, ss):
		for s in ss:
			sf.feed(s)
	def get_coeffs(sf):
		assert sf.__lll == len(sf.__cc)-1
		return sf.__cc[:sf.__lll+1]
	def feed(sf, s):
		# -> cc|None
		debug_print(f"\tfeed({s})")
		assert sf.__lll == len(sf.__cc)-1
		i = len(sf.__ss)
		assert sf.__m == i-sf.__prev_i
		sf.__ss.append(s)
		d = sf.__calc_d()
		cc_ = None
		if sf._is_field_zero_(d):
			sf.__m += 1
		elif 2*sf.__lll <= i:
			if sf.__prev_d is None:
				_1 = sf._get_field_one_()
				_0 = sf._get_field_zero_()
				cc_ = (_1, *[_0]*(1+i))
			else:
				cc_ = sf.__calc_cc(d)
			sf.__lll = i+1 - sf.__lll
			assert sf.__lll == len(cc_)-1
			sf.__prev_cc = sf.__cc
			sf.__prev_d = d
			sf.__m = 1
			sf.__prev_i = i
			sf.__cc = cc_
			debug_print(f"\t\tL={sf.__lll},{sf.get_coeffs()}, {len(cc_)}, cc={cc_}")
		else:
			sf.__cc = cc_ = sf.__calc_cc(d)
			sf.__m += 1
		if sf.__lll+1 <= len(sf.__ss):
			debug_print(f"\td={d} ==>> d'={sf.__calc_d()}")
		assert sf.__lll == len(sf.__cc)-1
		return cc_
	def verify(sf, *, cc=None, ss=None):
		if cc is None:
			cc = sf.get_coeffs()
		if ss is None:
			ss = sf.__ss
		return all(sf.__iter_verify(cc=cc, ss=ss))
	def __iter_verify(sf, *, cc, ss):
		for i in range(len(cc), len(ss)+1):
			#bug: r = sf._field_vec_inner_product_(cc, ss[i-1:i-len(cc)-1:-1])
			r = sf._field_vec_inner_product_(cc[::-1], ss[i-len(cc):i])
			yield sf._is_field_zero_(r)



def override(f):
	return f

_fr = fractions.Fraction
class Berlekamp_Massey_algorithm4fractions(
		Berlekamp_Massey_algorithmABC):
	@override
	def _field_add_(sf, a, b):
		return a+b
	@override
	def _field_mul_(sf, a, b):
		return a*b
	@override
	def _field_eq_(sf, a, b):
		return a==b
	@override
	def _field_inv_(sf, a):
		return a**(-1)
	@override
	def _field_neg_(sf, a):
		return -a

	@override
	def _get_field_zero_(sf):
		return _fr(0)
	@override
	def _get_field_one_(sf):
		return _fr(1)










class Berlekamp_Massey_algorithm4prime_field(
		Berlekamp_Massey_algorithmABC):
	def __init__(sf, p:"prime"):
		assert p>1
		sf.__p = p
		super().__init__()
	@override
	def _field_add_(sf, a, b):
		return (a+b)%sf.__p
	@override
	def _field_mul_(sf, a, b):
		return (a*b)%sf.__p
	@override
	def _field_eq_(sf, a, b):
		return not (a-b)%sf.__p
	@override
	def _field_inv_(sf, a):
		"""
		s*a+t*p = 1
		"""
		p = sf.__p
		return inv_mod(a, p)
	@override
	def _field_neg_(sf, a):
		return (-a)%sf.__p

	@override
	def _get_field_zero_(sf):
		return (0)
	@override
	def _get_field_one_(sf):
		return (1)





def _t():
	cls = Berlekamp_Massey_algorithm4fractions
	sss = [
			[1], [1, 0]
			,[-2,-2], [1,-1]
			,[-2,4], [1,2]
			,[0,1,2,3], [1,-2,1]
			,[0,1,1,2,3,5], [1,-1,-1]
			,[0]*5, [1]
			,[0]*5 + [2]
				, [1]+[0]*6
			,[0]*5 + [2] + [0]*3
				, [1]+[0]*6
			,[0]*5 + [2] + [0]*3 +[3]
				, [1]+[0]*3+[_fr(-3,2)]+[0]*2
			,[1,2,4,8,16,32,1,2,4,8,16,32,1,2,4,8,16,32]
				, [1]+[0]*5+[-1]
			]
	for ss,ans in zip(sss[::2], sss[1::2]):
		#print(f"ss={ss}, ans={ans}")
		sf = cls()
		sf.feeds(ss)
		cc = sf.get_coeffs()
		try:
			assert sf.verify()
			assert [*cc]==ans
		except:
			print(f"ss={ss}, ans={ans}")
			print(f"cc={cc}")
			raise


_t()

def main(args=None):
	import argparse

	parser = argparse.ArgumentParser(
		description="Berlekamp_Massey_algorithm for fractions/prime_field"
		, epilog="""
$ python Berlekamp_Massey_algorithm.py  -i 0 0 0
[1]
s[n] = 0

$ python Berlekamp_Massey_algorithm.py  -i 0 0 0  5
[1, 0, 0, 0, 0]
s[n] = 0*s[n-4]

$ python Berlekamp_Massey_algorithm.py  -i 0 0 0 3 0 0 2 0
[1, 0, 0, -2/3, 0]
s[n] = 2/3*s[n-3] + 0*s[n-4]

$ python Berlekamp_Massey_algorithm.py  -i 0 0 0 3 0 0 2 0 1/2
[1, 0, 0, -2/3, 0, -1/6]
s[n] = 2/3*s[n-3] + 1/6*s[n-5]

$ python Berlekamp_Massey_algorithm.py  -i 0 0 0 3 0 0 2 0 1/2 0
[1, 8/3, 0, -2/3, -16/9, -1/6]
s[n] = -8/3*s[n-1] + 2/3*s[n-3] + 16/9*s[n-4] + 1/6*s[n-5]

$ python Berlekamp_Massey_algorithm.py  -i 0 0 0 3 0 0 2 0 -p 7
[1, 0, 0, 4, 0]
s[n] = 3*s[n-3] + 0*s[n-4]

$ python Berlekamp_Massey_algorithm.py  -i 0 0 0 3 0 0 2 0 1/2  -p 7
[1, 0, 0, 4, 0, 1]
s[n] = 3*s[n-3] + 6*s[n-5]

$ python Berlekamp_Massey_algorithm.py  -i 0 0 0 3 0 0 2 0 1/2 0 -p 7
[1, 5, 0, 4, 6, 1]
s[n] = 2*s[n-1] + 3*s[n-3] + 1*s[n-4] + 6*s[n-5]

		"""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-i', '--input', type=_fr, default=[]
				, nargs="*", help='input fractions')
	parser.add_argument('-p', '--prime', type=int, default=0
				, help='prime number for prime_field; default=0 for fractions')

	args = parser.parse_args(args)
	ss_fr = args.input
	p = args.prime
	if p:
		sf = Berlekamp_Massey_algorithm4prime_field(p)
		ss_p = [fraction2int_mod(fr,p) for fr in ss_fr]
		ss = ss_p
	else:
		sf = Berlekamp_Massey_algorithm4fractions()
		ss = ss_fr

	sf.feeds(ss)
	assert sf.verify()

	cc = sf.get_coeffs()
	str_cc = ', '.join(map(str, cc))
	print(f"[{str_cc}]")

	def _it():
		for i,c in enumerate(cc[1:], 1):
			if i==len(cc)-1 or not sf._is_field_zero_(c):
				_c = sf._field_neg_(c)
				yield f"{_c}*s[n-{i}]"
	str_rhs = " + ".join(_it())
	if not str_rhs:
		str_rhs = "0"
		_0 = sf._get_field_zero_()
		str_rhs = f"{_0}"
	str_eqn = f"s[n] = {str_rhs}"
	print(f"{str_eqn}")

if __name__ == "__main__":
	main()
	#for n in sorted(globals().keys()): print(f"\t{n}")




