from fractions import Fraction as F
K = F(1000)
M = K*K
B = K*M
T = K*B
R = K*T


print(F(0.1))
print(F('0.1'))
d = {
"大金刚":
	[(1, ('762.93', B), ('13.52', R))
	]
,'宣传中心':
	[(1, ('152.58', B), ('1750.00', T))
	,(2, ('228.87', B), ('2440.88', T))
	,(3, ('305.16', B), ('3592.34', T))
	]
,'UFO':
	[(1, ('30.51', B), ('228.14', T))
	,(2, ('45.76', B), ('318.20', T))
	,(3, ('61.02', B), ('468.31', T))
	,(4, ('76.27', B), ('678.47', T))
	]
,'穿孔机': 
	[(3, ('12.20', B), ('60.80', T))
	, (4, ('15.25', B), ('88.08', T))
	, (5, ('18.30', B), ('123.16', T))
	, (6, ('21.35', B), ('166.04', T))
	]
,'炼金术师': 
	[(7, ('4880', M), ('28.09', T))
	,(8, ('5490', M), ('35.67', T))
	]
,'爆破者': 
	[(10, ('1342.77', M), ('7010.36', B))
	,(11, ('1464.84', M), ('8391.40', B))
	]
,'金矿提炼厂': 
	[(19, ('488.20', M), ('3139.51', B))]
,'地心魔虫': 
	[(15, ('78.08', M), ('256.62', B))
	, (16, ('82.96', M), ('290.97', B))
	]
,'低音炮': 
	[(26, ('26.32', M), ('97.91', B))]
,'考古学家': 
	[(75, ('14.84', M), ('105.35', B))]
#,'': [(, ('0', M), ('0', B))]
}

def _get_last(v):
	if len(v) == 1:
		r = v[-1]
	else:
		r = v[-2:]
	return r

def get_last(d):
	return {k: _get_last(v) for k,v in d.items()}
	return {k: v[-1] for k,v in d.items()}

def sort(d_last):
	ls = []
	for name, y in d_last.items():
		if type(y) is list:
			[(_l, _p, _), (level, product, update)] = y
			p = calc(product) - calc(_p)
			u = calc(update)
			x = p/(level-_l) /u
		else:
			(level, product, update) = y
			p = calc(product)
			u = calc(update)
			x = p/level /u

		ls.append((x, (name, y)))
	ls.sort()
	return ls
def calc(pair):
	num, unit = pair
	z = 10000
	#r = unit*int(z*num)/z
	r = unit * F(num)
	assert type(r) is F
	return r

def show(ls):
	for a in ls:
		x, _ = a
		x = float(x)
		print(x)
		print(a)

def find_rule():
	# product(n) = a*n+b
	# update(n) = c*n*n + d*n + e
	d['UFO']
def f():
	show(sort(get_last(d)))
f()




