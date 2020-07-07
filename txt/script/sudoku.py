r"""
sudoku
宫:行r,列c
n=r*c
数独大小:n*n
对称:
	旋转:pi*k
	镜像:x=0,y=0
	4
	if r==c:
		旋转:pi/2*k
		镜像:x=0,y=0,x=y,x=-y
		8
元素排列:n!
方程组:
	def mk(ps:位置):
		ret II z-p {p<-ps}
	for 位置 in 每宫/行/列:
		mk(位置) == mk(首行位置)
	无关方程数目<=3*(n-1)
	变量数目(不含z)==n*n
	自由度>=n^2-3n+3
Groebner basis:remove z

"""

from common_short_hand import *
import sympy as sy

def u2len(upper, radix):
	assert upper >= 1
	assert radix >= 2
	i = 0
	u = upper - 1
	while u:
		u //= radix
		i += 1
	assert radix**(i-1) < upper <= radix**i
	return i
def u2digits(u, radix):
	assert u >= 0
	assert radix >= 2
	digits = []
	while u:
		u,r = divmod(u, radix)
		digits.append(r)
	digits.reverse()
	return digits
def u2str(u, len_, digit_strs, sep):
	radix = len(digit_strs)
	digits = u2digits(u, radix)
	zs = len_ - len(digits)
	assert zs >= 0
	if zs > 0:
		digits = [0]*zs + digits
	s = sep.join(map(digit_strs.__getitem__, digits))
	return s
class idc2name:
	radix = 10
	digit_strs = ''.join(map(str, rg(10)))
	def __init__(sf, prefix, sep, suffix, *uppers):
		sf.prefix = prefix
		sf.sep = sep
		sf.suffix = suffix
		sf.uppers = uppers
		sf.lens = tpl(u2len(u,sf.radix) for u in uppers)
	def mk(sf, *idc):
		assert len(idc) == len(sf.uppers)
		def f(uu, len_, u):
			assert 0 <= u < uu
			s = u2str(u, len_, sf.digit_strs, '')
			return s
		m = sf.sep.join(map(f, sf.uppers, sf.lens, idc))
		s = f'{sf.prefix}{m}{sf.suffix}'
		return s

class sudoku:
	z = sy.Symbol('z')
	sy1 = z+1-z
	class caseM(type):
		def __le__(sf, ot):
			return issubclass(sf, ot)
	
	class case(metaclass=caseM):pass
	class case_free(case):pass
	class case_num_roots(case_free):pass
	class case_fix_row0(case_num_roots):pass
	class case_fix_min_per_blk(case_num_roots):pass
	class case_fix_row0_and_min(case_fix_min_per_blk, case_fix_row0):pass
	case = 1
	case_free = case
	case <<= 1
	case_num_roots = case | case_free
	case <<= 1
	case_fix_row0 = case | case_num_roots
	case <<= 1
	case_fix_min_per_blk = case | case_num_roots
	case_fix_row0_and_min = case_fix_row0 | case_fix_min_per_blk
	case <<= 1
	del case
	
	case_nms = """
	case_free
	case_num_roots
	case_fix_row0
	case_fix_min_per_blk
	case_fix_row0_and_min
	""".split()
	d = dict(locals())
	cases = (*map(d.__getitem__, case_nms),)
	case2nm = dict(zip(cases, case_nms))
	nm2case = dict(zip(case_nms, cases))
	del d

	def __init__(sf, r, c, case):
		assert r > 0
		assert c > 0
		assert case in sf.cases
		n = r*c # cc=r; rr=c
		sf.n = n
		sf.r = r
		sf.c = c
		sf.case = case
		sf.mk_nm = idc2name('s', 'x', '', n, n)
		sf.nm_mx = tpl(tpl(
				sf.mk_sym(i,j)
				for j in rg(n)
			)for i in rg(n)
			)
		sf.polys = (*sf.iter_polys(),)
	def iter_vars(sf):
		for nms in sf.nm_mx:
			yield from nms
	def eval_gb(sf, order):
		#lex, grlex and grevlex, or a user defined one, via order keyword.
		gbasis = sy.groebner(sf.polys, domain='ZZ', order=order)
		return gbasis
	def iter_row_pss(sf):
		return map(sf.row2ps, rg(sf.n))
	def iter_col_pss(sf):
		return map(sf.col2ps, rg(sf.n))
	def iter_blk_pss(sf):
		# cc=r; rr=c
		return map(sf.blk2ps, rg(sf.c), rg(sf.r))
	def iter_pss(sf):
		yield from sf.iter_row_pss()
		yield from sf.iter_col_pss()
		yield from sf.iter_blk_pss()
	def ps2vars(sf, ps):
		xs = {sf.nm_mx[i][j] for i,j in ps}
		return xs
	def ps2zpoly(sf, ps):
		vs = sf.ps2vars(ps)
		zp = sf.mk_zp(vs)
		return zp
	def mk_num_roots(sf):
		n = sf.n
		m = n//2
		xs = [*rg(-m,m+1)]
		if len(xs) != n:
			assert xs[m]==0
			del xs[m]
		assert len(xs) == n
		return tpl(xs)
	def mk_zp(sf, xs):
		assert len(xs) == sf.n
		z = sf.z
		zp = sf.sy1
		for x in xs:
			zp *= z-x
		return zp
	def zp2polys(sf, zp, zp0):
		zp -= zp0
		zp = zp.as_poly(sf.z)
		cs = zp.all_coeffs()
		yield from cs
	def iter_polys(sf):
		f = lambda ps:sf.ps2zpoly(ps).expand()
		case = sf.case
		def lt(case, _c):
			return (case & _c) == _c
		if lt(case, sf.case_free):
			ps0 = sf.row2ps(0)
			#zp0 = f(ps0)
			vs0 = sf.ps2vars(ps0)
			zp0 = sf.mk_zp(vs0)
			zp0 = zp0.expand()
			zp0_vs0 = zp0
			
			#, sf.case_fix_row0]:
			if lt(case, sf.case_num_roots):
				xs = sf.mk_num_roots()
				zp0 = sf.mk_zp(xs)
				zp0 = zp0.expand()
				if lt(case, sf.case_fix_row0):
					vs0 = sorted(vs0, key=str)
					for v, x in zip(vs0, xs):
						yield v-x
				#
				if lt(case, sf.case_fix_min_per_blk):
					x_min = sf.sy1 * xs[0]
					for ii in rg(sf.c):
						for jj in rg(sf.r):
							i = ii*sf.r + jj
							j = jj*sf.c + ii
							v = sf.nm_mx[i][j]
							yield v-x_min
		else:
			raise eee
		z = sf.z
		for v in sf.iter_vars():
			yield zp0.subs(z,v)
		it = (f(ps) for ps in sf.iter_pss())
		for zp in it:
			yield from sf.zp2polys(zp, zp0)
	def row2ps(sf, i):
		return ((i,j) for j in rg(sf.n))
	def col2ps(sf, j):
		return ((i,j) for i in rg(sf.n))
	def blk2ps(sf, ii, jj):
		r = sf.r
		c = sf.c
		i0 = ii*r
		j0 = jj*c
		ps = ((i,j)
				for j in rg(j0,j0+c)
				for i in rg(i0,i0+r)
			)
		return ps
	
	def mk_sym(sf, i,j):
		nm = sf.mk_nm.mk(i,j)
		return sy.Symbol(nm)


def _t(r,c,order,case):
	sf = sudoku(r,c,case)
	pr(f'sudoku({r},{c},{sf.case2nm[case]!r})')
	pr(f'order={order}')
	#for p in sf.polys:pr('\t', p.as_expr())
	
	gb = sf.eval_gb(order)
	#pr('\t', gb)
	polys, xs = gb.args
	for p in polys: pr('\t', p.as_expr())

[lex, grlex, grevlex
] = 'lex grlex grevlex'.split()
_t(1,2,grevlex,sudoku.case_free)
_t(2,2,lex,sudoku.case_fix_row0_and_min)
_t(3,2,lex,sudoku.case_fix_row0_and_min)
_t(3,3)

































































































