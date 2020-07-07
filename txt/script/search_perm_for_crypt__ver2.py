#search_perm_for_crypt

r"""
see:
	加密的安全性.txt
	加密.txt


$ python search_perm_for_crypt.py -n 3  > search_perm_for_crypt.py.out3.txt
(2^3)! == 40320 #16 bits
(2^4)! == 20922789888000 #45 bits
(2^5)! == 263130836933693530167218012160000000 #118 bits




n=4:
perm<4>[0]=(13, 11, 3, 10, 15, 6, 14, 8, 9, 0, 4, 2, 7, 1, 12, 5) #flags_lens=('-0+0~1', (11, 9, 11))@@0@fi=0@li=0;i^o=11@[1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15];i-o=9@[2, 3, 5, 6, 8, 9, 10, 12, 15];i+o=11@[1, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15];cycle_lens=(16,)@0@((0, 13, 1, 11, 2, 3, 10, 4, 15, 5, 6, 14, 12, 7, 8, 9),);foyc=0
0000->1101
0001->1011
0010->0011
0011->1010
0100->1111
0101->0110
0110->1110
0111->1000
1000->1001
1001->0000
1010->0100
1011->0010
1100->0111
1101->0001
1110->1100
1111->0101
















n=3
	total perm 2304/40320
	2304=2^8*3^2
	40320=2^7*3^2*5*7
	phi(40320)=2^6 *2*3 *4*6 = 2^10*3^2
	2304=phi(40320)///4
perm=04127653
000->000
001->100
010->001
011->010
100->111
101->110
110->101
111->011

perm=02371654 = inv 04127653
	(0, 2, 3, 7, 1, 6, 5, 4)
000->000
001->010
010->011
011->111
100->001
101->110
110->101
111->100



select lens=575
flags_oplens_cclens2c<3>=
	[...
	,(('-1+1~0', (5, 7, 5), (1, 2, 5)), 8)
	,...
	,(('-1+1~1', (5, 7, 5), (1, 2, 5)), 8)
	]
perm<3>[271]=(4, 2, 0, 3, 7, 6, 5, 1) #flags_lens=('-1+1~0', (5, 7, 5))@@0@fi=39@li=0;i^o=5@[0, 2, 3, 4, 6];i-o=7@[0, 1, 2, 4, 5, 6, 7];i+o=5@[0, 2, 3, 4, 6];cycle_lens=(1, 2, 5)@25@((0, 4, 7, 1, 2), (3,), (5, 6));foyc=0
perm<3>[579]=(2, 7, 1, 3, 0, 6, 5, 4) #flags_lens=('-1+1~0', (5, 7, 5))@@1@fi=88@li=1;i^o=5@[0, 2, 3, 4, 6];i-o=7@[0, 1, 2, 3, 4, 6, 7];i+o=5@[0, 2, 3, 4, 6];cycle_lens=(1, 2, 5)@56@((0, 2, 1, 7, 4), (3,), (5, 6));foyc=1
perm<3>[721]=(6, 3, 5, 7, 4, 2, 1, 0) #flags_lens=('-1+1~1', (5, 7, 5))@@0@fi=43@li=2;i^o=5@[0, 2, 4, 6, 7];i-o=7@[0, 2, 3, 4, 5, 6, 7];i+o=5@[0, 2, 4, 6, 7];cycle_lens=(1, 2, 5)@89@((0, 6, 1, 3, 7), (2, 5), (4,));foyc=0
perm<3>[805]=(7, 6, 5, 1, 4, 2, 0, 3) #flags_lens=('-1+1~1', (5, 7, 5))@@1@fi=53@li=3;i^o=5@[0, 2, 4, 6, 7];i-o=7@[0, 1, 2, 3, 4, 5, 6];i+o=5@[0, 2, 4, 6, 7];cycle_lens=(1, 2, 5)@109@((0, 7, 3, 1, 6), (2, 5), (4,));foyc=1
perm<3>[922]=(7, 6, 5, 3, 0, 2, 4, 1) #flags_lens=('-1+1~1', (5, 7, 5))@@2@fi=61@li=4;i^o=5@[0, 2, 4, 6, 7];i-o=7@[0, 1, 2, 3, 4, 5, 6];i+o=5@[0, 2, 4, 6, 7];cycle_lens=(1, 2, 5)@132@((0, 7, 1, 6, 4), (2, 5), (3,));foyc=2
perm<3>[936]=(4, 7, 5, 3, 6, 2, 1, 0) #flags_lens=('-1+1~1', (5, 7, 5))@@3@fi=64@li=5;i^o=5@[0, 2, 4, 6, 7];i-o=7@[0, 2, 3, 4, 5, 6, 7];i+o=5@[0, 2, 4, 6, 7];cycle_lens=(1, 2, 5)@139@((0, 4, 6, 1, 7), (2, 5), (3,));foyc=3
perm<3>[1025]=(2, 6, 5, 4, 0, 3, 1, 7) #flags_lens=('-1+1~1', (5, 7, 5))@@4@fi=81@li=6;i^o=5@[0, 2, 4, 6, 7];i-o=7@[0, 2, 3, 4, 5, 6, 7];i+o=5@[0, 2, 4, 6, 7];cycle_lens=(1, 2, 5)@150@((0, 2, 5, 3, 4), (1, 6), (7,));foyc=4
perm<3>[1252]=(4, 6, 0, 5, 3, 2, 1, 7) #flags_lens=('-1+1~1', (5, 7, 5))@@5@fi=103@li=7;i^o=5@[0, 2, 4, 6, 7];i-o=7@[0, 1, 2, 3, 4, 5, 6];i+o=5@[0, 2, 4, 6, 7];cycle_lens=(1, 2, 5)@193@((0, 4, 3, 5, 2), (1, 6), (7,));foyc=5
perm<3>[1389]=(3, 2, 1, 5, 0, 6, 4, 7) #flags_lens=('-1+1~0', (5, 7, 5))@@2@fi=219@li=8;i^o=5@[0, 2, 3, 4, 6];i-o=7@[0, 1, 2, 4, 5, 6, 7];i+o=5@[0, 2, 3, 4, 6];cycle_lens=(1, 2, 5)@224@((0, 3, 5, 6, 4), (1, 2), (7,));foyc=2
perm<3>[1452]=(4, 2, 1, 0, 6, 3, 5, 7) #flags_lens=('-1+1~0', (5, 7, 5))@@3@fi=228@li=9;i^o=5@[0, 2, 3, 4, 6];i-o=7@[0, 1, 2, 3, 4, 6, 7];i+o=5@[0, 2, 3, 4, 6];cycle_lens=(1, 2, 5)@235@((0, 4, 6, 5, 3), (1, 2), (7,));foyc=3
perm<3>[1454]=(3, 2, 1, 7, 4, 6, 0, 5) #flags_lens=('-1+1~0', (5, 7, 5))@@4@fi=229@li=10;i^o=5@[0, 2, 3, 4, 6];i-o=7@[0, 1, 2, 4, 5, 6, 7];i+o=5@[0, 2, 3, 4, 6];cycle_lens=(1, 2, 5)@236@((0, 3, 7, 5, 6), (1, 2), (4,));foyc=4
perm<3>[1468]=(6, 2, 1, 0, 4, 7, 5, 3) #flags_lens=('-1+1~0', (5, 7, 5))@@5@fi=237@li=11;i^o=5@[0, 2, 3, 4, 6];i-o=7@[0, 1, 2, 3, 4, 6, 7];i+o=5@[0, 2, 3, 4, 6];cycle_lens=(1, 2, 5)@239@((0, 6, 5, 7, 3), (1, 2), (4,));foyc=5
perm<3>[1546]=(0, 2, 4, 1, 7, 6, 5, 3) #flags_lens=('-1+1~0', (5, 7, 5))@@6@fi=268@li=12;i^o=5@[0, 2, 3, 4, 6];i-o=7@[0, 1, 2, 4, 5, 6, 7];i+o=5@[0, 2, 3, 4, 6];cycle_lens=(1, 2, 5)@252@((0,), (1, 2, 4, 7, 3), (5, 6));foyc=6
perm<3>[1619]=(0, 3, 1, 7, 2, 6, 5, 4) #flags_lens=('-1+1~0', (5, 7, 5))@@7@fi=291@li=13;i^o=5@[0, 2, 3, 4, 6];i-o=7@[0, 1, 2, 3, 4, 6, 7];i+o=5@[0, 2, 3, 4, 6];cycle_lens=(1, 2, 5)@270@((0,), (1, 3, 7, 4, 2), (5, 6));foyc=7
perm<3>[2113]=(0, 6, 5, 4, 2, 7, 1, 3) #flags_lens=('-1+1~1', (5, 7, 5))@@6@fi=245@li=14;i^o=5@[0, 2, 4, 6, 7];i-o=7@[0, 2, 3, 4, 5, 6, 7];i+o=5@[0, 2, 4, 6, 7];cycle_lens=(1, 2, 5)@377@((0,), (1, 6), (2, 5, 7, 3, 4));foyc=6
perm<3>[2134]=(0, 6, 4, 7, 3, 2, 1, 5) #flags_lens=('-1+1~1', (5, 7, 5))@@7@fi=253@li=15;i^o=5@[0, 2, 4, 6, 7];i-o=7@[0, 1, 2, 3, 4, 5, 6];i+o=5@[0, 2, 4, 6, 7];cycle_lens=(1, 2, 5)@382@((0,), (1, 6), (2, 4, 3, 7, 5));foyc=7



"""


from collections import defaultdict
import sys

def factorial(n):
	if n>0:
		return n*factorial(n-1)
	elif n==0:
		return 1

def swap(ls,i,j):
	ls[i],ls[j] = ls[j],ls[i]
def u2perm(nn, u):
	ls = [*range(nn)]
	for i in reversed(range(1,nn)):
		u,r = divmod(u,i+1)
		swap(ls, r,i)
	assert 0<=u<2
	return (*ls,)
def iter_perm(nn, *, begin):
	nnn=factorial(nn)
	for u in range(begin, nnn):
		yield u, u2perm(nn, u)


def inv_perm(perm):
	ls = [None]*len(perm)
	for i,o in enumerate(perm):
		ls[o] = i
	return ls
def fff1(perm):
	if fff1_half(perm):
		inv = inv_perm(perm)
		return fff1_half(inv)
	return False
def fff1_half(perm):
	L = len(perm)
	B = L.bit_length()-1
	#print(B, L)
	assert 2**B == L
	C = L//4
	rgL = range(L)
	rgB = range(B)
	ki = 1
	for ji in rgB:
		ko = 1
		for jo in rgB:
			c = [0,0]
			for mi in rgL:
				mid = mi^ki
				mo = perm[mi]
				mod = perm[mid]
				do = bool((mo&ko) ^ (mod&ko))
				s = bool(mi&ki)
				c[s] += do
			if not (C == c[0] == c[1]):
				return False
			ko<<=1
		ki<<=1
	return True

def perm2cycles(perm):
	[*perm] = perm
	n = len(perm)
	cycles = []
	def get(k):
		r = perm[k]
		perm[k] = None
		return r
	for j in range(n):
		i = get(j)
		if i is None:
			#break
			continue
		cycle = [j]
		cycles.append(cycle)
		while i != j:
			cycle.append(i)
			i = get(i)
	cycles = (*map(tuple, cycles),)
	assert n == sum(map(len, cycles))
	return cycles


#_print = print
def print_air(*args, **kw):pass
def print_err(*args, file=sys.stderr, **kw):
	print(*args, file=file, **kw)
	#file.flush()


class SearchPerm4Crypt__ver2:
	def __init__(sf, n, *
			, verbose
			, begin, num_found
			, fout
			):
		assert n>=2
		sf.n = n
		sf.verbose = verbose
		sf.fout = fout
		#sf.ferr = ferr
		#sf.end = begin
		#sf.num_found = num_found
		#sf.tmp = {}
		sf.data = dict(end=begin, num_found=num_found)

		sf._print_err = print_err if verbose else print_air

		n = sf.n
		assert n>=2
		nn=2**n
		nnn=factorial(nn)
		#sf.factorial_2pow_n = nnn
		sf.len_perm = nn
		sf.total_perms = nnn
	@property
	def end(sf):
		return sf.data["end"]
	@property
	def num_found(sf):
		return sf.data["num_found"]
	#print_err(dir(end))
	@end.setter
	def end(sf, i):
		sf.data["end"] = i

	def _print(sf, *args, **kw):
		print(*args, file=sf.fout, **kw)
	def search_perm_for_crypt(sf):
			#n, verbose , *, begin, num_found, output, fout
		###
		n = sf.n
		assert n>=2
		nn = sf.len_perm
		nnn = sf.total_perms
		###
		i_mask = 2**13-1
		derty = False
		begin = sf.end
		i = begin-1
		for i,ls in iter_perm(nn, begin=begin):
			sf.end = i
			if not (i&i_mask):
				if derty:
					sf.fout.flush()
					derty = False
				if sf.verbose: sf._print_err(f"found {sf.num_found}@{i}/{nnn}={i/nnn}")
			###
			if fff1(ls):
				yield i, ls
				derty = True
				tmp = dict(end=sf.end+1, num_found=sf.num_found+1)
				sf.data = tmp
					# KeyboardInterrupt
				if sf.verbose: sf._print_err(f"found {sf.num_found} perm @{sf.end}")
		else:
			i += 1
			assert begin <= i <= nnn
			sf.end = i
		return
		#############
		#############
		#############err:
		ss=nn//4
		#nnn=factorial(nn)
		masks = [1<<i for i in range(n)]
		for ls in iter_perm(nn):
			for i in range(n):
				idc = (k for k in range(nn) if k&masks[i])
				idc = (*idc,)
				
				for j in range(n):
					mask = masks[j]
					if ss != sum(1 for k in idc if ls[k]&mask):
						break
				else:
					continue
				break
			else:
				yield ls
		else:
			return
		



	def _show(sf):
		#n, verbose, *, begin, num_found, output , fout):
		n = sf.n
		it = sf.search_perm_for_crypt()
		def f(p):
			op, it = p
			s = set(it)
			s = sorted(s)
			return f"i{op}o={len(s)}@{s}"
		
		lens2c = defaultdict(int)
		flags2c = defaultdict(int)
		flags_lens2c = defaultdict(int)
		lens2cycless = defaultdict(list)
		cycle_lens2c = defaultdict(int)
		flags_oplens_cclens2c = defaultdict(int)
		mask = (1<<n)-1
		j_mask = 2**4-1
		for j,(uuu, perm) in enumerate(it, sf.num_found):
			#avoid j == sf.num_found
			#    0,+-1
			if not (j&j_mask): sf.fout.flush()
			xor_io = {i^o for i,o in enumerate(perm)}
			sub_io = {(i-o)&mask for i,o in enumerate(perm)}
			add_io = {(i+o)&mask for i,o in enumerate(perm)}
			ps = [("^", xor_io), ("-", sub_io), ("+", add_io)]
			suffix = ';'.join(map(f,ps))
			
			lens = (len(s) for op,s in ps)
			lens = (*lens,)
			c = lens2c[lens]
			lens2c[lens] += 1
			
			ops = "-+~"
			flags = [0 in sub_io, 0 in add_io, mask in add_io]
			flags = [0+b for b in flags]
			flags = (*flags,)
			fs = "".join(op+str(b) for op,b in zip(ops,flags))
			fc = flags2c[fs]
			flags2c[fs] += 1
			
			
			fl = (fs, lens)
			flc = flags_lens2c[fl]
			flags_lens2c[fl] += 1
			
			cycles = perm2cycles(perm)
			cycle_lens = (*sorted(map(len, cycles)),)
			cycless = lens2cycless[cycle_lens]
			cc = len(cycless)
			cycless.append(cycles)
			cycle_lens2c[cycle_lens] += 1
			
			foy = (fs, lens, cycle_lens)
			foyc = flags_oplens_cclens2c[foy]
			flags_oplens_cclens2c[foy] +=1
			
			sf._print(f"perm<{n}>[{j}]={perm} #flags_lens={fl}@@{flc}@fi={fc}@li={c};{suffix};cycle_lens={cycle_lens}@{cc}@{cycles};foyc={foyc}####@u2perm({uuu})")
			
		
		lens2c = sorted(lens2c.items())
		sf._print(f"lens2c<{n}>={lens2c}")
		flags2c = sorted(flags2c.items())
		sf._print(f"flags2c<{n}>={flags2c}")
		flags_lens2c = sorted(flags_lens2c.items())
		sf._print(f"flags_lens2c<{n}>={flags_lens2c}")
		cycle_lens2c = sorted(cycle_lens2c.items())
		sf._print(f"cycle_lens2c<{n}>={cycle_lens2c}")
		flags_oplens_cclens2c = sorted(flags_oplens_cclens2c.items())
		sf._print(f"flags_oplens_cclens2c<{n}>={flags_oplens_cclens2c}")


	def show(sf):
		sf._print(f"@{__class__.__name__}")
		sf._print(f"n={sf.n}, begin={sf.end}, num_found={sf.num_found}:")
		nnn = sf.total_perms

		try:
			sf._show()
		finally:
			s = f"break@(n={sf.n}, end={sf.end}, num_found={sf.num_found}, data={sf.data}, total_perms={nnn}, remain={nnn-sf.end})"
			sf._print(s)
			sf._print("\n"*2)
			sf._print_err(s)
			sf.fout.flush()









def main(args=None):
	import argparse

	parser = argparse.ArgumentParser(
		description="search_perm_for_crypt"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-n', '--bit_size'
			, type=int, default=[], nargs="*"
			, help='n bits')
	parser.add_argument('-v', '--verbose'
			, action="store_true"
			, default=False
			, help="show more"
			)
	parser.add_argument('-b0', '--begin'
			, type=int, default=0
			, help='value from prev exec "end" of output to continue the exec')
	parser.add_argument('-nf0', '--num_found'
			, type=int, default=0
			, help='value from prev exec "num_found" of output to continue the exec')
	
	args = parser.parse_args(args)
	
	ns = args.bit_size
	assert args.begin >= 0
	assert args.num_found >= 0

	fout = sys.stdout
	for n in ns:
		if n>=2:
			sf = SearchPerm4Crypt__ver2(n
					, verbose = args.verbose
					, begin = args.begin
					, num_found = args.num_found
					, fout=fout
					)
			sf.show()



def _t(n):
	sz = factorial(2**n)
	print(f"(2^{n})! == {sz} #{sz.bit_length()} bits")
	return

#for n in range(3,6):_t(n)


if __name__ == "__main__":
	main()


r"""
python search_perm_for_crypt__ver2.py -n 2 -v > search_perm_for_crypt__ver2.py.out2.txt

python search_perm_for_crypt__ver2.py -n 3 -v > search_perm_for_crypt__ver2.py.out3.txt

python search_perm_for_crypt__ver2.py  -n 4 -v -b0 0 -nf0 0 >> search_perm_for_crypt__ver2.py.out4.txt
python search_perm_for_crypt__ver2.py  -n 4 -v -b0 2207957 -nf0 0 >> search_perm_for_crypt__ver2.py.out4.txt
python search_perm_for_crypt__ver2.py  -n 4 -v -b0 8969491 -nf0 1 >> search_perm_for_crypt__ver2.py.out4.txt
python search_perm_for_crypt__ver2.py  -n 4 -v -b0 19598901 -nf0 11 >> search_perm_for_crypt__ver2.py.out4.txt
python search_perm_for_crypt__ver2.py  -n 4 -v -b0 29371948 -nf0 21 >> search_perm_for_crypt__ver2.py.out4.txt









n=4, begin=0:
perm<4>[0]=(13, 11, 3, 10, 15, 6, 14, 8, 9, 0, 4, 2, 7, 1, 12, 5) #flags_lens=('-0+0~1', (11, 9, 11))@@0@fi=0@li=0;i^o=11@[1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15];i-o=9@[2, 3, 5, 6, 8, 9, 10, 12, 15];i+o=11@[1, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15];cycle_lens=(16,)@0@((0, 13, 1, 11, 2, 3, 10, 4, 15, 5, 6, 14, 12, 7, 8, 9),);foyc=0####@u2perm(2207957)
break@(n=4, end=6544784, num_found=1)
break@(n=4, end=8969491, num_found=1, tmp=None)


n=4, begin=8969491:
perm<4>[1]=(15, 9, 12, 4, 11, 10, 7, 8, 0, 2, 13, 5, 3, 6, 1, 14) #flags_lens=('-0+1~1', (6, 8, 9))@@0@fi=0@li=0;i^o=6@[1, 7, 8, 11, 14, 15];i-o=8@[1, 6, 7, 8, 9, 11, 13, 15];i+o=9@[0, 3, 7, 8, 10, 11, 13, 14, 15];cycle_lens=(16,)@0@((0, 15, 14, 1, 9, 2, 12, 3, 4, 11, 5, 10, 13, 6, 7, 8),);foyc=0####@u2perm(14906430)
perm<4>[2]=(1, 9, 3, 4, 5, 10, 12, 8, 0, 2, 15, 7, 11, 6, 13, 14) #flags_lens=('-0+0~1', (9, 7, 11))@@0@fi=0@li=0;i^o=9@[1, 3, 5, 7, 8, 10, 11, 12, 15];i-o=7@[1, 4, 7, 8, 10, 11, 15];i+o=11@[1, 2, 3, 5, 7, 8, 9, 10, 11, 13, 15];cycle_lens=(16,)@1@((0, 1, 9, 2, 3, 4, 5, 10, 15, 14, 13, 6, 12, 11, 7, 8),);foyc=0####@u2perm(15020862)
perm<4>[3]=(1, 9, 3, 4, 5, 10, 13, 8, 0, 2, 15, 7, 11, 14, 12, 6) #flags_lens=('-0+0~1', (10, 8, 10))@@0@fi=1@li=0;i^o=10@[1, 2, 3, 5, 7, 8, 9, 11, 12, 15];i-o=8@[1, 2, 4, 7, 8, 9, 11, 15];i+o=10@[1, 2, 3, 5, 7, 8, 9, 10, 11, 15];cycle_lens=(16,)@2@((0, 1, 9, 2, 3, 4, 5, 10, 15, 6, 13, 14, 12, 11, 7, 8),);foyc=0####@u2perm(15022278)
perm<4>[4]=(1, 9, 3, 4, 5, 10, 12, 8, 0, 2, 15, 7, 11, 14, 13, 6) #flags_lens=('-0+0~1', (10, 8, 9))@@0@fi=2@li=0;i^o=10@[1, 3, 5, 7, 8, 9, 10, 11, 12, 15];i-o=8@[1, 4, 7, 8, 9, 10, 11, 15];i+o=9@[1, 2, 5, 7, 8, 9, 10, 11, 15];cycle_lens=(2, 14)@0@((0, 1, 9, 2, 3, 4, 5, 10, 15, 6, 12, 11, 7, 8), (13, 14));foyc=0####@u2perm(15022534)
perm<4>[5]=(1, 9, 3, 4, 5, 14, 11, 15, 0, 2, 7, 10, 8, 12, 6, 13) #flags_lens=('-0+0~0', (7, 8, 11))@@0@fi=0@li=0;i^o=7@[1, 2, 4, 7, 8, 11, 13];i-o=8@[1, 2, 3, 4, 7, 8, 11, 15];i+o=11@[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];cycle_lens=(16,)@3@((0, 1, 9, 2, 3, 4, 5, 14, 6, 11, 10, 7, 15, 13, 12, 8),);foyc=0####@u2perm(15667309)
perm<4>[6]=(1, 9, 3, 4, 5, 14, 11, 15, 0, 2, 7, 10, 13, 12, 6, 8) #flags_lens=('-0+0~0', (5, 6, 10))@@0@fi=1@li=0;i^o=5@[1, 7, 8, 11, 13];i-o=6@[1, 3, 7, 8, 11, 15];i+o=10@[1, 3, 4, 5, 6, 7, 8, 9, 10, 11];cycle_lens=(2, 14)@1@((0, 1, 9, 2, 3, 4, 5, 14, 6, 11, 10, 7, 15, 8), (12, 13));foyc=0####@u2perm(15680744)
perm<4>[7]=(15, 14, 3, 12, 5, 6, 7, 10, 11, 13, 8, 0, 4, 2, 9, 1) #flags_lens=('-0+1~1', (10, 11, 11))@@0@fi=1@li=0;i^o=10@[1, 2, 3, 4, 7, 8, 11, 13, 14, 15];i-o=11@[1, 2, 3, 5, 7, 8, 11, 12, 13, 14, 15];i+o=11@[0, 1, 2, 3, 5, 6, 7, 9, 11, 13, 15];cycle_lens=(16,)@4@((0, 15, 1, 14, 9, 13, 2, 3, 12, 4, 5, 6, 7, 10, 8, 11),);foyc=0####@u2perm(15738865)
perm<4>[8]=(13, 9, 3, 4, 5, 14, 7, 15, 0, 2, 8, 10, 1, 12, 6, 11) #flags_lens=('-0+0~0', (7, 8, 11))@@1@fi=2@li=1;i^o=7@[1, 2, 4, 7, 8, 11, 13];i-o=8@[1, 2, 3, 4, 7, 8, 11, 15];i+o=11@[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13];cycle_lens=(16,)@5@((0, 13, 12, 1, 9, 2, 3, 4, 5, 14, 6, 7, 15, 11, 10, 8),);foyc=1####@u2perm(16167947)
perm<4>[9]=(1, 9, 3, 4, 5, 14, 7, 15, 0, 2, 13, 10, 8, 12, 6, 11) #flags_lens=('-0+0~0', (5, 6, 11))@@0@fi=3@li=0;i^o=5@[1, 4, 7, 8, 11];i-o=6@[1, 4, 7, 8, 13, 15];i+o=11@[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13];cycle_lens=(16,)@6@((0, 1, 9, 2, 3, 4, 5, 14, 6, 7, 15, 11, 10, 13, 12, 8),);foyc=0####@u2perm(16191467)
perm<4>[10]=(13, 9, 3, 4, 5, 14, 7, 15, 0, 2, 11, 10, 1, 12, 6, 8) #flags_lens=('-0+0~0', (5, 6, 10))@@1@fi=4@li=1;i^o=5@[1, 7, 8, 11, 13];i-o=6@[1, 3, 7, 8, 11, 15];i+o=10@[3, 4, 5, 6, 7, 8, 9, 10, 11, 13];cycle_lens=(2, 14)@2@((0, 13, 12, 1, 9, 2, 3, 4, 5, 14, 6, 7, 15, 8), (10, 11));foyc=1####@u2perm(17216264)
break@(n=4, end=19598901, num_found=11, tmp={'end': 17216265, 'num_found': 11})




@SearchPerm4Crypt__ver2
n=4, begin=19598901, num_found=11:
perm<4>[11]=(1, 13, 9, 10, 5, 6, 7, 11, 12, 15, 4, 8, 14, 2, 0, 3) #flags_lens=('-0+0~1', (10, 9, 11))@@0@fi=0@li=0;i^o=10@[1, 2, 3, 4, 6, 9, 11, 12, 14, 15];i-o=9@[3, 4, 6, 9, 10, 11, 12, 14, 15];i+o=11@[1, 2, 3, 4, 8, 9, 10, 11, 13, 14, 15];cycle_lens=(16,)@0@((0, 1, 13, 2, 9, 15, 3, 10, 4, 5, 6, 7, 11, 8, 12, 14),);foyc=0####@u2perm(19743843)
perm<4>[12]=(14, 2, 9, 10, 5, 6, 7, 11, 0, 3, 4, 8, 13, 1, 15, 12) #flags_lens=('-0+0~0', (8, 7, 8))@@0@fi=0@li=0;i^o=8@[1, 3, 8, 9, 10, 11, 12, 14];i-o=7@[2, 3, 6, 8, 9, 12, 15];i+o=8@[2, 3, 8, 9, 11, 12, 13, 14];cycle_lens=(16,)@1@((0, 14, 15, 12, 13, 1, 2, 9, 3, 10, 4, 5, 6, 7, 11, 8),);foyc=0####@u2perm(19747164)
perm<4>[13]=(14, 2, 9, 10, 5, 6, 7, 11, 0, 3, 4, 8, 13, 1, 12, 15) #flags_lens=('-1+0~0', (10, 8, 9))@@0@fi=0@li=0;i^o=10@[0, 1, 2, 3, 8, 9, 10, 11, 12, 14];i-o=8@[0, 2, 3, 6, 8, 9, 12, 15];i+o=9@[2, 3, 8, 9, 10, 11, 12, 13, 14];cycle_lens=(1, 15)@0@((0, 14, 12, 13, 1, 2, 9, 3, 10, 4, 5, 6, 7, 11, 8), (15,));foyc=0####@u2perm(19747167)
perm<4>[14]=(14, 2, 9, 10, 5, 6, 7, 11, 0, 3, 4, 8, 1, 13, 12, 15) #flags_lens=('-1+0~0', (11, 9, 9))@@0@fi=1@li=0;i^o=11@[0, 1, 2, 3, 8, 9, 10, 11, 12, 13, 14];i-o=9@[0, 2, 3, 6, 8, 9, 11, 12, 15];i+o=9@[2, 3, 8, 9, 10, 11, 12, 13, 14];cycle_lens=(1, 1, 14)@0@((0, 14, 12, 1, 2, 9, 3, 10, 4, 5, 6, 7, 11, 8), (13,), (15,));foyc=0####@u2perm(19750047)
perm<4>[15]=(1, 13, 9, 10, 5, 6, 7, 11, 0, 3, 4, 8, 2, 14, 15, 12) #flags_lens=('-0+0~0', (8, 8, 9))@@0@fi=1@li=0;i^o=8@[1, 3, 8, 9, 10, 11, 12, 14];i-o=8@[3, 4, 6, 8, 9, 10, 12, 15];i+o=9@[1, 2, 3, 8, 9, 11, 12, 13, 14];cycle_lens=(16,)@2@((0, 1, 13, 14, 15, 12, 2, 9, 3, 10, 4, 5, 6, 7, 11, 8),);foyc=0####@u2perm(19753164)
perm<4>[16]=(1, 13, 9, 10, 5, 6, 7, 11, 0, 3, 4, 8, 2, 14, 12, 15) #flags_lens=('-1+0~0', (10, 10, 10))@@0@fi=2@li=0;i^o=10@[0, 1, 2, 3, 8, 9, 10, 11, 12, 14];i-o=10@[0, 2, 3, 4, 6, 8, 9, 10, 12, 15];i+o=10@[1, 2, 3, 8, 9, 10, 11, 12, 13, 14];cycle_lens=(1, 15)@1@((0, 1, 13, 14, 12, 2, 9, 3, 10, 4, 5, 6, 7, 11, 8), (15,));foyc=0####@u2perm(19753167)
perm<4>[17]=(1, 13, 9, 10, 5, 6, 7, 11, 15, 12, 4, 8, 14, 2, 3, 0) #flags_lens=('-0+0~1', (11, 9, 11))@@0@fi=1@li=0;i^o=11@[1, 2, 3, 5, 7, 9, 11, 12, 13, 14, 15];i-o=9@[3, 4, 6, 9, 11, 12, 13, 14, 15];i+o=11@[1, 2, 3, 5, 7, 9, 10, 11, 13, 14, 15];cycle_lens=(16,)@3@((0, 1, 13, 2, 9, 12, 14, 3, 10, 4, 5, 6, 7, 11, 8, 15),);foyc=0####@u2perm(19753968)
perm<4>[18]=(1, 13, 12, 15, 5, 6, 7, 11, 0, 3, 4, 8, 14, 2, 9, 10) #flags_lens=('-0+0~1', (10, 9, 12))@@0@fi=2@li=0;i^o=10@[1, 2, 3, 5, 7, 8, 10, 12, 14, 15];i-o=9@[3, 4, 5, 6, 8, 11, 12, 14, 15];i+o=12@[1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15];cycle_lens=(16,)@4@((0, 1, 13, 2, 12, 14, 9, 3, 15, 10, 4, 5, 6, 7, 11, 8),);foyc=0####@u2perm(19774234)
perm<4>[19]=(1, 13, 9, 10, 5, 6, 7, 11, 0, 3, 4, 8, 14, 2, 12, 15) #flags_lens=('-1+0~1', (11, 11, 11))@@0@fi=0@li=0;i^o=11@[0, 1, 2, 3, 8, 9, 10, 11, 12, 14, 15];i-o=11@[0, 2, 3, 4, 6, 8, 9, 11, 12, 14, 15];i+o=11@[1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15];cycle_lens=(1, 2, 13)@0@((0, 1, 13, 2, 9, 3, 10, 4, 5, 6, 7, 11, 8), (12, 14), (15,));foyc=0####@u2perm(19784367)
perm<4>[20]=(15, 2, 14, 4, 5, 6, 13, 11, 0, 3, 8, 12, 10, 7, 9, 1) #flags_lens=('-0+1~1', (11, 10, 11))@@0@fi=0@li=0;i^o=11@[1, 2, 3, 6, 7, 8, 10, 11, 12, 14, 15];i-o=10@[1, 2, 4, 5, 6, 8, 9, 12, 14, 15];i+o=11@[0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 15];cycle_lens=(16,)@5@((0, 15, 1, 2, 14, 9, 3, 4, 5, 6, 13, 7, 11, 12, 10, 8),);foyc=0####@u2perm(21962785)
break@(n=4, end=29371948, num_found=21, data={'end': 29371948, 'num_found': 21}, total_perms=20922789888000, remain=20922760516052)



"""






