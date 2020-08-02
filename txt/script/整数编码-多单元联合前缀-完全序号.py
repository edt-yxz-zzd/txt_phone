r"""
整数编码 多单元联合前缀 完全序号

状态计数::列向量<状态->计数>
状态转移::单元值->矩阵<状态->状态->计数>



完全序号 合法编码 =
	带状态完全序号 最长必然前缀后状态 合法编码[len(最长必然前缀):]
带状态完全序号 状态 状态后合法后缀 =
	case 状态后合法后缀 of
		[] -> 0
		v:ls -> 带状态完全序号 (状态转移 v 状态) ls + sum~ 状态空间大小 (状态转移 vv 状态) len(ls) {vv<-[0..v-1]}
状态空间大小 状态 状态后长度 =
	(完全混沌状态转移矩阵^状态后长度 * 列向量{状态:1})[+mt]
完全混沌状态转移矩阵 = sum~ 状态转移 单元值 {单元值}

这里只考虑 单元值 为 比特 的 情形
0{mh}(.*)1{mt}
	[mh>=2][mt>=2]

由于前 (mh+1) 位 必是 0{mh}1 ，初始状态 便是 1
st =
	-i ...10{i}
	+j ...01{j}
	=====
	i <- [1..mh]
	j <- [1..mt]
	-mh error
	+mt final
st2st<?> :: mx<n,n>
	-1..-mh,+mt..+1
	n = mh+mt
st2st<0> =
	# mh=mt=3
	|010000 # -1
	|001000
	|000100 # -mt -> +mh
	|000100 # +mh -> +mh
	|100000
	|100000 # +1
st2st<1> =
	# mh=mt=3
	|000001 # -1
	|000001
	|000100 # -mt -> +mh
	|000100 # +mh -> +mh
	|000100
	|000010 # +1
st2st = st2st<0> + st2st<1> =
	# mh=mt=3
	|010001 # -1
	|001001
	|000200 # -mt -> +mh
	|000200 # +mh -> +mh
	|100100
	|1000010 # +1


(st2st^n)[0,mt-1]

====

====
sm = \
	["010001"
	,"001001"
	,"000200"
	,"000200"
	,"100100"
	,"100010"
	]

ls = [*map(int, ''.join(sm))]
from sympy import Matrix;
m = Matrix(6, 6, ls)
(P, D) = m.diagonalize()
>>> import sympy as sy
>>> sp = sy.sympify
>>> sf = sy.simplify
>>> sy.var('a,b,c,d,e')
>>> sy.diag(0,a,b,c,d,e)
pow_mx = lambda mx, i: sf(pow_mx(mx,i-1)*mx) if i>=1 else sy.eye(*mx.shape)
mul_mx = lambda mx, *ms: sf(sf(mx)*mul_mx(*ms)) if ms else sf(mx)
mul_mx(P, sy.diag(0,a,b,c,d,e), P.inv())


=========usage:sympy
>>> from sympy import Matrix
>>> m = Matrix(3, 3, [1, 2, 0, 0, 3, 0, 2, -4, 2])
>>> m
Matrix([
[1,  2, 0],
[0,  3, 0],
[2, -4, 2]])
>>> (P, D) = m.diagonalize()
>>> D
Matrix([
[1, 0, 0],
[0, 2, 0],
[0, 0, 3]])
>>> P
Matrix([
[-1, 0, -1],
[ 0, 0, -1],
[ 2, 1,  2]])
>>> P.inv() * m * P
Matrix([
[1, 0, 0],
[0, 2, 0],
[0, 0, 3]])

#"""


import sympy as sy
sp = sy.sympify
sf = sy.simplify

def mk_st2st_0(mh, mt):
	assert mh >= 2
	assert mt >= 2
	n = mh+mt
	m = sy.zeros(n, n)
	for i in range(mt):
		m[i,i+1] = 1
	for i in range(1, mh):
		m[-i,0] = 1
	m[-mh, -mh] = 1
	c = sy.ones(n, 1)
	r = sy.ones(1, n)
	assert m*c == c
	assert (r*m)[0, mt] == 2
	return m

def mk_st2st_1(mh, mt):
	assert mh >= 2
	assert mt >= 2
	n = mh+mt
	m = sy.zeros(n, n)
	for i in range(mt-1):
		m[i,-1] = 1
	m[mt-1, -mh] = 1
	for i in range(1, mh):
		m[-i,-i-1] = 1
	m[-mh, -mh] = 1
	c = sy.ones(n, 1)
	r = sy.ones(1, n)
	assert m*c == c
	assert (r*m)[0, mt] == 3
	return m

def mk_st2st(mh, mt):
	return mk_st2st_0(mh, mt) + mk_st2st_1(mh, mt)

def _t(mh, mt):
	m = mk_st2st(mh, mt)
	(P, D) = m.diagonalize()
	n = mh+mt
	ds = [D[i,i] for i in range(n)]
	if not D == sy.diag(*ds):
		print(D)
	assert D == sy.diag(*ds)
	xs = sy.symbols(f'x[:{n}]')
	ys = [d if d==0 or d==1 else x for d, x in zip(ds, xs)]
	ddd = sy.diag(*ys)
	#(P*ddd*P.inv())[0, mt-1]
	print('P=', P)
	print('ds=', ds)
	invP = P.inv() # noreturn???
	r = sy.zeros(1, n)
	r[0,0] = 1
	c = sy.zeros(n, 1)
	c[mt-1, 0] = 1
	z = (r*P)*ddd*(invP*c)
	z = sy.expand(z)
	assert z.shape == (1, 1)
	z = z[0, 0]
	z = sf(z)
	return ds, z

_t(3,3)


#P.inv() too slow
#_t(2,3)
#_t(4,4)


r"""
_t(3,3)
D
Matrix([
[0, 0,                  0,                  0,               0,               0],
[0, 2,                  0,                  0,               0,               0],
[0, 0, -1/2 - sqrt(3)*I/2,                  0,               0,               0],
[0, 0,                  0, -1/2 + sqrt(3)*I/2,               0,               0],
[0, 0,                  0,                  0, 1/2 - sqrt(5)/2,               0],
[0, 0,                  0,                  0,               0, 1/2 + sqrt(5)/2]])


P
Matrix([
[ 0, 1,                 -1,                 -1,                1,                1],
[-1, 1, -1/2 + sqrt(3)*I/2, -1/2 - sqrt(3)*I/2, -sqrt(5)/2 - 1/2, -1/2 + sqrt(5)/2],
[-1, 1,                  0,                  0,                0,                0],
[ 0, 1,                  0,                  0,                0,                0],
[ 0, 1,  1/2 - sqrt(3)*I/2,  1/2 + sqrt(3)*I/2, -sqrt(5)/2 - 1/2, -1/2 + sqrt(5)/2],
[ 1, 1,                  1,                  1,                1,                1]])

>>> P*diag(0,a,b,c,d,e)*P.inv()
~/tmp/mx.txt
>>> mx[0,2]
-b/4 - sqrt(3)*I*b/12 - c/4 + sqrt(3)*I*c/12 + sqrt(5)*d/20 + d/4 - sqrt(5)*e/20 + e/4
===
(-1/2 - sqrt(3)*I/2)*(-1/4 - sqrt(3)*I/12)
	=sqrt(3)*I/6

#"""
