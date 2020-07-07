"""
stable_poly
poly(v.v.)::[pg26]::1.1.5. Routh-Hurwitz problem
stable_poly 1.1.5. Routh-Hurwitz
stable_poly := {f<-univariate_poly | @z. [f(z)=0] --> [Re(z)<0]}
"""
__all__ = """
	is_stable_poly
	""".split()

from sympy import *
pr = print
rg = range
ff = not 1
tt = not 0
eee = Exception
nnn = {}.get(0)
dd = nnn
#dd = QQ[I]
#dd = CC
mxx = Matrix
_0 = sympify(0)
_1 = sympify(1)

def is_real(x):
	return im(x)==0
def are_coeffs_all_positive(f):
	return all(c>0 for c in f.all_coeffs())
	return all(f.nth(i)>0 for i in rg(1+f.degree()))
def are_coeffs_all_real(f):
	return all(map(is_real, f.all_coeffs()))

if 1:
		def iter_half_Sylvester_mx(n,cs):
			cs = [*cs]
			z1 = (_0,)
			n1 = n-1
			for i in rg(n):
				yield [*z1*i, *cs, *z1*(n1-i)]
			
		def mk_Sylvester_mx(cs0,cs1):
			n = len(cs0)+len(cs1)-2
			
			mx = [
				*iter_half_Sylvester_mx(len(cs1)-1, cs0)
				,*iter_half_Sylvester_mx(len(cs0)-1, cs1)
				]
			mx = mxx(mx)
			assert mx.shape == (n,n)
			return mx
		def mk_resultant(cs0,cs1):
			mx = mk_Sylvester_mx(cs0,cs1)
			return mx.det()
		def exsqrt_monic(f):
			if degree(f) < 1:
				return f.monic()
			_, ps = f.sqf_list(all=tt)
			#pr(f); pr(ps)
			
			g, e0 = ps[0]
			assert e0==1
			assert g==1 #poly(1)
			
			for h, e in ps[1:]:
				if degree(h) == 0:
					continue
				if e%2:
					raise eee("f is not ex square")
				g *= h**(e//2)
			return g
			#bug: f=g^4*h^6 -> g*h
			f_ = f.monic()
			g = f_.sqf_part()
			assert g.is_monic
			if g**2 != f_:
				pr(f)
				pr(f_)
				pr(g)
				pr(degree(f), degree(g))
				raise eee("f is not ex square")
			return g
def is_stable_poly(f):
	if not (f.is_univariate and f.degree()>0):
		return ff
	
	dd = f.domain
	f = poly(f, domain=dd)
	if not f.is_monic:
		f = f.monic() #f/f.LC()
		dd = f.domain
	if are_coeffs_all_real(f):
		p = f
	else:
		#mk p
		#x = f.gen
		#p = f*conj(f(conj(x)))
		#conj(p)=
		#		= conj(f*conj(f(conj(x))))
		#		= conj(f)*f(conj(x)))
		#p(conj(x))=
		#		= f(conj(x))*conj(f(x))
		#		= f(conj(x))*conj(f)
		#		= conj(f)*f(conj(x)))
		#		= conj(p)
		#==>> are_coeffs_all_real(p)
		###
		cs = f.all_coeffs()
		x = f.gen
		d = f.degree()
		assert d+1 == len(cs)
		p = f*sum(conjugate(cs[i])*x**(d-i) for i in rg(d+1)).as_poly(domain=dd)
		del d,x
	del f
	assert p.is_monic
	assert are_coeffs_all_real(p)

	if not are_coeffs_all_positive(p):
		return ff
	
	
	n = p.degree()
	x = p.gen
	#mk q
	#deg(q)=C(n,2)
	#rs = all_roots(p)
	#assert n == len(rs)
	#q = II(x-(rs[i]+rs[j]) for i,j in itertools.combinations(rg(n), 2)).as_poly()
	#
	#Res1(f,g,x) := det(Sylvester_mx(f.all_coeffs(x), g.all_coeffs(x)))
	#mx<k,k>
	#k = x+y = (fd+1)+x-1 = (gd+1)+y-1
	#==>> k=fd+gd
	#==>> f.cs shift x=gd times/rows
	#
	#Res1(p(t),p(x-t), t) = c*q*q*p(x/2)
	t = Dummy('t')
	#pr(p)
	#p(x/2)#raise!!!!!
	px_2 = (p*2**n).subs(x,x/2).as_poly(x,domain=dd)
		#gen = x/2 after subs!!!!
	#resultant(p(t),p(x-t), t)
	#rx = resultant(p.subs(x,t),p.subs(x,x-t), t)
	pxt = p.subs(x,x-t).as_poly(t,domain=dd[x])
	if 1:
		pt = p.subs(x,t).as_poly(t,domain=dd[x])
			#raise@[dd=CC]!!! sympy bugs???
		rx = pt.resultant(pxt)
	else:
		pt = p.subs(x,t)
		cs0 = pt.all_coeffs()
		cs1 = pxt.all_coeffs()
		rx = mk_resultant(cs0,cs1)
	rx = rx.as_poly(x,domain=dd)

	assert rx.degree(x) == n*n
	#resultant(p(t),p(x-t), t).exquo(p(x/2))
	#pr(rx, px_2)
	cqq = rx.exquo(px_2)
	#q = sqrt(resultant(p(t),p(x-t), t).exquo(p(x/2))).monic()
	#q = exsqrt(cqq).monic()
	q = exsqrt_monic(cqq)
	del p
	assert q.is_monic
	assert are_coeffs_all_real(q)
	return are_coeffs_all_positive(q)

def _t():
	x = symbols('x')
	f2ans = {
		(x+1):1
		,(x+1)**2:1
		,(x+1)*(3*x+2):1
		,(x+1)**2 *(x+3)*(x**2 +2*x +25)
			:1
		,(x-1):0
		,(x-1)**2:0
		,(x-1)*(x+2):0
		,(x-1)*(3*x-2):0
		,(x*x+7 -2*x) *(x*x+7+5*x)
			:0
		#(xx+n -2x)(xx+n +kx)
		#=(xx+n)**2 +(k-2)x(xx+n) -2kxx
		#[k>2][2n>2k]
		}
	for f,r in f2ans.items():
		r = bool(r)
		pr(f, r)
		f = f.as_poly()
		pr(f)
		r_ = is_stable_poly(f)
		assert r_ is r
if __name__ == '__main__':
	_t()





