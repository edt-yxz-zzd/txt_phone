#sym_rot_mx_det

#file:///storage/emulated/0/0my_files/py_doc/sympy-docs-html-1.5/modules/solvers/solveset.html
#sympy.solvers.solveset.nonlinsolve(system, *symbols)

#file:///storage/emulated/0/0my_files/py_doc/sympy-docs-html-1.5/modules/solvers/inequalities.html
#sympy.solvers.inequalities.solve_rational_inequalities(eqs)
#sympy.solvers.inequalities.solve_poly_inequality(poly, rel)
#sympy.solvers.inequalities.solve_poly_inequalities(polys)

#file:///storage/emulated/0/0my_files/py_doc/sympy-docs-html-1.5/modules/polys/basics.html
#solve_poly_system

from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve
from sympy import *
from sympy.interactive.printing import init_printing
init_printing(use_unicode=False, wrap_line=False)
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt
from sympy.solvers.inequalities import (
	solve_poly_inequalities
	,solve_poly_inequality
	,solve_rational_inequalities
	)
from sympy.polys import Poly
solve_poly_system


def _t_nonlinsolve():
	x, y, z = symbols('x, y, z', real=True)
	r = nonlinsolve([x*y - 1, 4*x**2 + y**2 - 5], [x, y])

	print(srepr(r))
	print(r)
#_t_nonlinsolve()

def _t_nonlinsolve__params():
	x, y, z = symbols('x, y, z', real=True)
	r = nonlinsolve([x*y - z, z*x**2 + y**2 - 5], [x, y])

	#print(srepr(r))
	print(r)
	print(r.intersect(S.Reals**2))
	#print(r.limit(z,0))#no attr
_t_nonlinsolve__params()


'''
m =
	[x+iy, z+iw
	;a0x+a1y+a3z+a4w+i(...), ...+i(...)
	]
'''

mxx = Matrix
pr = print
rg = range

def add_syms(d, syms):
	for s in syms:
		d[str(s)] = s
def mk_syms(n):
	a = symbols(f'a:{2*n}', real=True)
	#bs = []
	mx_ = [a]
	d = {}
	add_syms(d, a)
	for r in rg(1, n):
		mx = []
		for c in rg(2*n):
			b = symbols(f'b{r}x{c}m:{2*n}', real=True)
			add_syms(d, b)
			#bs.extend(b)
			mx.append(b)
		col = mxx(mx)*mxx(a)
		mx_.append(col.T)
		####
		mx2 = mxx(n,2, col)
		col = mx2*mxx([1, I])
	
	mx = [
		[r[c] + I*r[c+1]
			for c in rg(0,2*n,2)
		]
		for r in mx_
		]
	mx = mxx(mx)
	mx2 = [
		(mxx(n,2, r)*mxx([1, I])).T
		for r in mx_
		]
	mx2 = mxx(mx2)
	mx3 = mxx(n,n, lambda r,c:
		mx_[r][2*c] + I*mx_[r][2*c+1]
		)
	if 0:
		pr(mx2)
		pr(mx2.shape)
		pr('\n'*4)
		pr(mx3)
	assert mx == mx3
	assert mx == mx2
	assert len(d) == 2*n + (n-1)*(2*n)**2
	return d, mx

def _t_mk_syms(n):
	d, mx = mk_syms(n)
	pr(d)
	pr(mx)
#_t_mk_syms(2)


def _t_ineq():
	from sympy.abc import x,y
	r = solve_poly_inequalities(
			((Poly(x+y - 3), ">")
			,(Poly(x-y + 1), ">")
			)
		)
	pr(r)
	"""
	sympy.polys.polyerrors.PolynomialError:
		only univariate polynomials are allowed
	"""
#_t_ineq()

def _t_ploys():
	from sympy.abc import x,y
	r = solve_poly_system(
			[Poly(x+y - 3)
			,(x-y**2 + 1).as_poly()
			]
			,x,y
		)
	pr(r)
#_t_ploys()
















