
from common_short_hand import *
from nn_ns.math_nn.floor_sqrt import (
	floor_sqrt
	,floor_kth_root
	)
from seed.math.gcd import gcd_many
#from nn_ns.math_nn.continued_fraction.continued_fraction import (
#	continued_fraction_pack_to_ND_pairs
#	)
import itertools



def continued_fraction_pack_to_ND_pairs(cf, ND_2=(0,1), ND_1=(1,0)):
    '''x = xs[0] = (0+1*xs[0])/(1+0*xs[0])
    = cf[0] + 1/xs[1] = (1+cf[0]*xs[1])/(0 + 1*xs[1])
    = (N[i-1]+N[i]*xs[i+1])/(D[i-1]+D[i]*xs[i+1])
    # xs[i] = cf[i] + 1/xs[i+1]
    = (N[i] + (N[i-1]+N[i]*cf[i+1])*xs[i+2])
    /(D[i] + (D[i-1]+D[i]*cf[i+1])*xs[i+2])
    ==>> N[-2] = 0, N[-1] = 1; D[-2] = 1, D[-1] = 0
    ==>> N[-1] = 1, N[0] = cf[0]; D[-1] = 0, D[0] = 1
    ==>> N[i+1] = N[i-1]+N[i]*cf[i+1]; D[i+1] = D[i-1]+D[i]*cf[i+1]

return (N[i], D[i]) for i in range(len(cf))

x = (N[i-2]+N[i-1]*xs[i])/(D[i-2]+D[i-1]*xs[i])
(D[i-2]+D[i-1]*xs[i])x = (N[i-2]+N[i-1]*xs[i])
D[i-2]x - N[i-2] = N[i-1]*xs[i] - D[i-1]*xs[i]x
-N[i-2] + D[i-2]x = (N[i-1] - D[i-1]x)*xs[i]
xs[i] = (-N[i-2]+D[i-2]*x)/(N[i-1]-D[i-1]*x)
'''
    N_2, D_2 = ND_2
    N_1, D_1 = ND_1
    for c in cf:
        N0 = N_2 + N_1*c
        D0 = D_2 + D_1*c
        yield N0, D0
        N_2, D_2 = N_1, D_1
        N_1, D_1 = N0, D0
        
    return



class 稠密多项式:
	@classmethod
	def std(cls, cs):
		it = itertools.dropwhile(lambda x: not x, cs)
		cs = [*it]
		if cs:
			g = gcd_many(cs)
			if cs[0]*g < 0:
				g = -g
			it = map(lambda x:x//g, cs)
			cs = tpl(it)
			assert cs[0] > 0
		else:
			cs = ()
		return cs
		

		
	@classmethod
	def eval(cls, cs, x):
		r = 0*x
		if not x:
			for r in cs[-1:]: pass
		else:
			it = iter(cs); del cs
			for r in it:
				if r: break
			for c in it:
				if c:
					r = r*x+c
				else:
					r = r*x
		return r
	@classmethod
	def diff(cls, cs):
		if not cs:
			df = ()
		else:
			df = tpl(map(opss.__mul__, rvd(rg(len(cs))), cs))
		return df
	@classmethod
	def iter_newton_method(cls, cs, df, x0, *, div = opss.__truediv__):
		"""
		x1 = x0 - f(x0)/df(x0)
		"""
		while 1:
			fx0 = cls.eval(cs, x0)
			dfx0 = cls.eval(df, x0)
			x0 -= div(fx0, dfx0)
			yield x0
	def __init__(sf, coeffs):
		sf._cs = tpl(coeffs)
		sf._ds = 0 #diff coeffs











#整系数三元一次方程单实根连分数
"""
在一般形式的一元三次方程ax^3+bx^2+cx+d=0中，一般采用盛金判别法，即
令
	A=b2-3ac
	B=bc-9ad
	C=c2-3bd
当A=B=0时，方程有一个三重实根。
当Δ=B2－4AC>0时，方程有一个实根和一对共轭虚根。
当Δ=B2－4AC=0时，方程有三个实根，其中有一个二重根。
当Δ=B2－4AC<0时，方程有三个不相等的实根。



https://baike.baidu.com/item/%E7%9B%9B%E9%87%91%E5%85%AC%E5%BC%8F
盛金公式
盛金定理
盛金判别法
=====
a,b,c,d <- RR
[a/=0]
	重根判别式
	A=b2-3ac
	B=bc-9ad
	C=c2-3bd
	总判别式
	Δ=B2－4AC
====盛金定理1..9[d1..d9]
[A=0]:
	[B=0]:
		[Δ=0]
		[b=0]:
			d1:[c=d=0]
		[b!=0]:
			d2:[c!=0][3c/b=b/a=9d/c]
		d3:[C=0]
	[B/=0]:
		d4:[Δ>0]
[A<0]:
	d5:[Δ>0]
[Δ=0]:
	[A=0]:
		d6:[B=0]
	[B/=0]:
		d7:[A>0]
[Δ<0]:
	d8:[A>0]
	d9:[-1<T<1]
===from above
[A<=0]:
	[Δ>=0] ^d8
[Δ>0]:
	*[A=0][B/=0]
	*[A<0]
	*[A>0][???] #C<B2/(4A)
===盛金公式1..4[g1..g4]
[Δ=0][A=0]:
		<==>[A=0][B=0]
		g1:[x1=x2=x3=-b/(3a)]
		[b!=0]:
			[x1=x2=x3=-b/(3a)=-c/b=-3d/c]
[Δ=0][A/=0]:
	[K:=B/A]:
		g3:[x1=-b/a+K][x2=x3=-K/2]
[Δ>0]:
	[{y1,y2}:=Ab+3a(-B+[+-]sqrt(Δ))/2]
	[{z1,z2}:={y1,y2}.^(1/3)]
	[w1:=z1+z2][{w2,w3}:=[+-](y1-y2)]:
		g2:[x1=(-b-w1)/(3a)][{x2,x3}=(-b+1/2*w+[+-]i*sqrt(3)/2*w2)/(3a)]
[Δ<0]:
	[T:=(Ab-3/2*aB)/A^(3/2)]
	[t:=arccos(T)/3]
	[p:=cos(t)][q:=sin(t)]:
		g4:[x1=(-b-2sqrt(A)*p)/(3a)][{x2,x3}=(-b+2sqrt(A)(1/2*p+[+-]sqrt(3)/2*q))/(3a)]


===================

	Df/Dx = 3ax2+2bx+c
		DDD=(2b)2-4*3a*c=4(b2-3ac)=4A
	* 无峰
		[DDD<=0]
		[A<=0]
	* 两峰
		[DDD>0]
		[A>0]
	center=-b/3a


===================
整系数三元一次方程单实根连分数
	[Δ>0]
	x=root(x,ax3+bx2+cx+d)
		=root([a,b,c,d])
		=X+1/root(y,a(1/y+X)^3+b(1/y+X)2+c(1/y+X)+d)
		=X+1/root([(aX3+bX2+cX+d),(3aX2+2bX+c),(3aX+b),a])
		====
		a(1+yX)^3+by(1+yX)2+cyy(1+yX)+dy3
			=a(1+3yX+3y2X2+y3X3)
			+by(1+2yX+y2X2)
			+cyy(1+yX)+dy3
			=y3(aX3+bX2+cX+d)
			+y2(3aX2+2bX+c)
			+y(3aX+b)
			+a
		====
		X=??? floor root
			from center=-b/3a
			[X<center]
			?<==>?[a*f(center)>0]
			<==>[(3a)3*f(-b/3a)>0]
			<==>[a(2b3-9abc+27da2)>0]
			
			
	* 无峰
		[Δ>0][A<=0]
	* 两峰
		[Δ>0][A>0]
		
	[Δ>0]:
		由g2判断是否不可约
		[{y1,y2}:=Ab+3a(-B+[+-]sqrt(Δ))/2]
		[{z1,z2}:={y1,y2}.^(1/3)]
		[w1:=z1+z2]
		[x1=(-b-w1)/(3a)]
		
		[{Y1,Y2}:=8Ab+12a(-B+[+-]sqrt(Δ))]
		[{Z1,Z2}:={Y1,Y2}.^(1/3)]
		[W1:=Z1+Z2=2w1]
		[x1=(-2b-W1)/(6a)]
			m=8Ab-12aB
			n=12a*sqrt(Δ)
			{Y1,Y2}:=m[+-]n
		X = floor(x1)
			= floor((-2b-W1)/(6a))
			= floor(floor(-2b-W1)/(6a))
			= floor((-2b+floor(-W1))/(6a))
			= floor((-2b+floor(-((m+n)^/3 + (m-n)^/3)))/(6a))
			= floor((-2b+floor(-(m+n)^/3 - (m-n)^/3))/(6a))
			= floor((+[0|1] -2b +floor(-(m+n)^/3) +floor(-(m-n)^/3))/(6a))
		floor(-(m[+-]n)^/3)
			= floor3th(-(m[+-]n))
			= floor3th(floor(-(m[+-]n)))
			= floor3th(-m +floor([-+]n))
			= floor3th(-m +floor([-+]sqrt(Δ(12a)2)))
			= floor3th(-m +floor(-sqrt(Δ(12a)2)))
			| floor3th(-m +floor(+sqrt(Δ(12a)2)))
			= floor3th(-m -ceil2th(Δ(12a)2))
			| floor3th(-m +floor2th(Δ(12a)2))
			
		可约:
			ax3+bx2+cx+d
				=(ex+f)(gx2+hx+k)
				=(1/a)(ax+fg)(ax2+ehx+ek)
			x=-fg/a
			(-2b-W1)/6 是整数
			(-2b-W1) 是整数
			W1 是整数
			m=8Ab-12aB
			n=12a*sqrt(Δ)
			((m+n)^/3 + (m-n)^/3) 是整数
				eg
					(3x+4)(5x2+1)=0
					15x3+20x2+3x+4=0
					a=15,b=20,c=3,d=4
					A=b2-3ac=265
					B=bc-9ad=-480
					C=c2-3bd=-231
					Δ=B2－4AC=475260>0
					689<sqrt(Δ)<690
					m=8Ab-12aB=8*265*20+12*15*480=128800
					n=12a*sqrt(Δ)=180*sqrt(475260)
					W1=(M+K*√D)^(1/3)+(M-K*√D)^(1/3)=80
					x1=(-2b-W1)/(6a)=-20/a=-4/3
			
"""

class 盛金判别法:
	def __init__(sf, a, b, c, d):
		if not a: raise eee
		(a, b, c, d) = 稠密多项式.std((a, b, c, d))
		sf.a = a
		sf.b = b
		sf.c = c
		sf.d = d

		A=b*b-3*a*c
		B=b*c-9*a*d
		C=c*c-3*b*d
		ddd = B*B-4*A*C

		sf.A = A
		sf.B = B
		sf.C = C
		sf.ddd = ddd

def floor3th(x):
	if x >= 0:
		r = floor_kth_root(x,3)
	else:
		r = -floor_kth_root(-x,3)
		r3 = r**3
		if r3 <= x:
			assert x < (r+1)**3
		else:
			r -= 1
			assert r**3 < x
	return r
	
def floor2th(x):
	return floor_sqrt(x)
def floorceil2th(x):
	y = floor2th(x)
	z = y + bool(y**2 < x)
	return y, z

def cf2denominators(cf):
	f = continued_fraction_pack_to_ND_pairs
	for n,d in f(cf):
		yield d

class 整系数三元一次方程单实根连分数:
	def __init__(sf, a, b, c, d):
		assert type(a) is int
		assert type(b) is int
		assert type(c) is int
		assert type(d) is int
		sj = 盛金判别法(a, b, c, d)
		if not sj.ddd > 0:raise eee("非单实根双虚根")
		sf.sj = sj
	def is_root_rational_ex(sf):
		"-> (bool, cf_init::[int], cf_tail::Iter int)"
		cf = []
		it = sf.iter_root_cf()
		def mk():
			for k in it:
				cf.append(k)
				yield k
		_a = abs(sf.sj.a)
		for d in cf2denominators(mk()):
			if _a < d:
				r = ff #irrational
				break
		else:
			r = tt #rational
			for _ in it:
				raise logic-error
		cf_init = tpl(cf)
		cf_tail = it
		return (r, cf_init, cf_tail)
		
	def iter_root_cf(sf):
		p = 稠密多项式
		cls = 整系数三元一次方程单实根连分数
		
		_x, _0, _1 = sf.floor_root_ex()
		yield _x
		while _0:
			sj = sf.sj
			[a,b,c,d] = [sj.a,sj.b,sj.c,sj.d]
				# abcd will be diff when cls(a,b,c,d)
			#pr((a,b,c,d));pr((_x,_0,_1)); input()
			_3a = 3*a
			_a = _0
			_b = p.eval([_3a,2*b,c], _x)
			_c = p.eval([_3a,b], _x)
			_d = a
			a,b,c,d = _a, _b, _c, _d
			sf = cls(a,b,c,d)
			_x, _0,_1 = sf.floor_root_ex()
			yield _x

	def floor_root(sf):
		_x, _,_ = sf.floor_root_ex()
		return _x
	def floor_root_ex(sf):
		p = 稠密多项式
		sj = sf.sj
		[a,b,c,d,A,B,C,ddd
		] = [sj.a,sj.b,sj.c,sj.d,sj.A,sj.B,sj.C,sj.ddd]
		m = 8*A*b-12*a*B
		n2 = ddd*(12*a)**2
		_n, n_ = floorceil2th(n2)
		_y1,_y2 = _n-m, -n_-m
		_z1 = floor3th(_y1)
		_z2 = floor3th(_y2)
		u = _z1+_z2-2*b
		v = u+1
		_6a = 6*a
		ss = {u//_6a, v//_6a}
		cs = (a,b,c,d)
		for _x in ss:
			_0 = p.eval(cs, _x)
			if not _0:
				_1 = _0
				break
			_1 = p.eval(cs, _x+1)
			if _0*_1 < 0: break
		else:
			raise logic-error
		#pr((a,b,c,d));pr((_x,_0,_1)); input()
		return _x, _0, _1



def _mk_cf3(a,b,c,d):
	cls = 整系数三元一次方程单实根连分数
	sf = cls(a, b, c, d)
	return sf.iter_root_cf()
def _main(a,b,c,d):
	for k in _mk_cf3(a,b,c,d):
		pr(k)#;input()

def _t():
	cs = (15,20,3,4)
	f = 稠密多项式.eval
	for x in rg(-1,2):
		y = f(cs, x)
		pr(cs, x,y)
#_t()
#_main(a=15,b=20,c=3,d=4)
assert [*_mk_cf3(15,20,3,4)]==[-2,1,2]







def main(args=None):
    import argparse
    
    parser = argparse.ArgumentParser(
        description="整系数三元一次方程单实根连分数"
        , epilog=""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('coeffs', type=int
                        ,nargs=4, help='4 coeffs (a,b,c,d) for a*x^3+b*x^2+c*x+d=0')
    parser.add_argument('-n', "--num_output_le", type=int
                        ,default=-1
                        , help='output cf prefix at most num_output_le; neg then inf')
    parser.add_argument('-ir', "--irrational_detect"
                        , action='store_true'
                        , default = False
                        , help='if cf inf then endswith "...irrational@{?}..." else "...rational@{?}..."')


    args = parser.parse_args(args)
    cs = args.coeffs
    n = args.num_output_le
    ir = args.irrational_detect
    
    cls = 整系数三元一次方程单实根连分数
    sf = cls(*cs)
    
    def show_le(it, n):
        if n >= 0:
            it = itertools.islice(it, n)
        for k in it:
            pr(k)
    if ir:
        (r, cf_init, cf_tail) = sf.is_root_rational_ex()
        cf = itertools.chain(cf_init, cf_tail)
        L = len(cf_init)
        if n < 0:
            n = len(cf_init)
        show_le(cf, n)
        if not r:
            pr(f"...irrational@{L}...")
        else:
            pr(f"...rational@{L}...")
    else:
        cf = sf.iter_root_cf()
        show_le(cf, n)

if __name__ == "__main__":
    main()




