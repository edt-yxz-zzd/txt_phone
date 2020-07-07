
r"""
try_DLP

known m,g,g^a to find a
	f<m,g>(a,i)
		| i=0 = g^a%m
		| i>0 = g^f<m,g>(a,i-1)%m
	find the peroid!!!!!
known m,g,g^a,g^b to find g^ab
	(g^a)^g^b and so on
	g^a,g^-a,g^-b...


#"""

from abc import ABC, abstractmethod
from nn_ns.math_nn.integer.mod import invmod
from fractions import gcd

class try_DLP(ABC):
	def __init__(sf, mm,g):
		#maybe mm = p*q
		sf.mm = mm
		sf.g = g
		assert gcd(g,mm)==1
		sf.ig = invmod(g,mm)

	@abstractmethod
	def h(sf, i, ga, iga, x=None):
		#x[i]->x[i+1]
		pass
	def f(sf, a):
		mm = sf.mm
		g = sf.g
		ig = sf.ig
		ga = pow(g,a,mm)
		iga = pow(ig,a,mm)
		xs = []
		s = {...}
		x = sf.h(0, ga, iga)
		for i in range(1, mm+2):
			b = x in s
			s.add(x)
			xs.append(x)
			if b: break
			x = sf.h(i, ga, iga, x)
		else:
			raise logic-error
		return xs

def show_xs(mm,g,a,xs):
	x = xs[-1]
	print(f"{g}^{a}%{mm}:")
	print(f"\txs={xs}")
	print(f"\tlen(xs)={len(xs)}")
	xi = xs.index(x)
	pp = len(xs)-1-xi
	print(f"\t  = {xi}+{pp}+1")
	if a in xs:
		ai = xs.index(a)
		print(f"\tans={a} at {ai}")
	else:
		print(f"\tans={a} not in xs")
	
	na = mm-a
	if na in xs:
		nai = xs.index(na)
		print(f"\t-ans={na} at {nai}")
	else:
		print(f"\t-ans={na} not in xs")
	#raise Exception(f"{g}^{a}%{mm}")




def filter_coeffs(mm, a, xs, cs=None):
	#a:=(c[0]+c[1]*x)%mm
	#
	if cs is None:
		cs = {((a-c1*x)%mm, c1)
				for x in xs[:-1]
				for c1 in range(1,mm)
				}
		return cs
	s = {(c0,c1)
			for c0,c1 in cs
			if any((c0+c1*x)%mm ==a for x in xs)
			}
	return s

def ttt(cls, mm):
	print(f"start: {cls}")
	ncs_yes = 0; ncs_no = 0
	for g in range(2,mm-1):
		sf = cls(mm,g)
		nyes = 0; nno = 0
		cs = None
		for a in range(1,mm):
			xs = sf.f(a)
			cs = filter_coeffs(mm, a, xs, cs)
			show_xs(mm,g,a,xs)
			if a in xs:
				nyes += 1
			else:
				nno += 1
		print(f"@@{g}^?%{mm}: +{nyes}, -{nno};  coeffs={cs}")
		if cs:
			ncs_yes += 1
		else:
			ncs_no += 1
	print(f"@@@?^?%{mm}: +{ncs_yes}, -{ncs_no}")
	print(f"end: {cls}")






class f1(try_DLP):
	def h(sf, i, ga, iga, x=None):
		#x[i]->x[i+1]
		#g^g^...^ga
		mm = sf.mm
		g = sf.g
		ig = sf.ig
		if x is None:
			assert i==0
			return ga
		assert i>0
		y = pow(g, x, mm)
		return y
		pass

class f2(try_DLP):
	def h(sf, i, ga, iga, x=None):
		#x[i]->x[i+1]
		#ga^ga^...^ga
		mm = sf.mm
		g = sf.g
		ig = sf.ig
		if x is None:
			assert i==0
			return ga
		assert i>0
		y = pow(ga, x, mm)
		return y
		pass


class f3(try_DLP):
	def h(sf, i, ga, iga, x=None):
		#x[i]->x[i+1]
		#ga^ga^...^g
		mm = sf.mm
		g = sf.g
		ig = sf.ig
		if x is None:
			assert i==0
			return g
		assert i>0
		y = pow(ga, x, mm)
		return y
		pass




class f4(try_DLP):
	def h(sf, i, ga, iga, x=None):
		#x[i]->x[i+1]
		#ga^g^...^g
		mm = sf.mm
		g = sf.g
		ig = sf.ig
		if x is None:
			assert i==0
			return ga
		assert i>0
		y = pow(x, g, mm)
		return y
		pass

class f5(try_DLP):
	def h(sf, i, ga, iga, x=None):
		#x[i]->x[i+1]
		#g^(...^(g^ga^ig)^...)^ig
		mm = sf.mm
		g = sf.g
		ig = sf.ig
		if x is None:
			assert i==0
			return ga
		assert i>0
		y = pow(x, ig, mm)
		y = pow(g, y, mm)
		return y
		pass

class f6(try_DLP):
	def h(sf, i, ga, iga, x=None):
		#x[i]->x[i+1]
		#ga^(...^(ga^g^iga)^...)^iga
		mm = sf.mm
		g = sf.g
		ig = sf.ig
		if x is None:
			assert i==0
			return g
		assert i>0
		y = pow(x, iga, mm)
		y = pow(ga, y, mm)
		return y
		pass



#class

clss = [f1,f2,f3,f4,f5,f6]

#ttt(f1, 19)


def main(args=None):
	import argparse
	#from seed.io.may_open import may_open_stdin, may_open_stdout

	parser = argparse.ArgumentParser(
		description="try to solve DLP"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-m', '--mod', type=int, default=None
						, required=True
						, help='ZZ%m')
	parser.add_argument('-c', '--class_idx', type=int, default=None
						, required=True
						, choices = [*range(1,len(clss)+1)]
						, help='choose a cls to run')
	r"""
	parser.add_argument('-o', '--output', type=str, default=None
						, help='output file path')
	parser.add_argument('-e', '--encoding', type=str
						, default='utf8'
						, help='input/output file encoding')
	parser.add_argument('-f', '--force', action='store_true'
						, default = False
						, help='open mode for output file')
	#"""

	args = parser.parse_args(args)
	cls = clss[args.class_idx-1]
	mm = args.mod
	assert mm > 3
	ttt(cls, mm)
	r"""
	encoding = args.encoding
	omode = 'wt' if args.force else 'xt'

	may_ofname = args.output
	with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
	#"""

if __name__ == "__main__":
	main()





