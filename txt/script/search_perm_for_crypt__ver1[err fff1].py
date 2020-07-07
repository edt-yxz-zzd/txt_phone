#search_perm_for_crypt

r"""

$ python search_perm_for_crypt.py -n 3  > search_perm_for_crypt.py.out3.txt
(2^3)! == 40320 #16 bits
(2^4)! == 20922789888000 #45 bits
(2^5)! == 263130836933693530167218012160000000 #118 bits

"""



from collections import defaultdict

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
def iter_perm(nn):
	nnn=factorial(nn)
	for u in range(nnn):
		yield u2perm(nn, u)


def search_perm_for_crypt(n):
	assert n>=2
	nn=2**n
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

def _show(n):
	it = search_perm_for_crypt(n)
	print(f"n={n}:")
	mask = (1<<n)-1
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
	for j,perm in enumerate(it):
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
		
		print(f"perm<{n}>[{j}]={perm} #flags_lens={fl}@@{flc}@fi={fc}@li={c};{suffix};cycle_lens={cycle_lens}@{cc}@{cycles};foyc={foyc}")
		
	
	lens2c = sorted(lens2c.items())
	print(f"lens2c<{n}>={lens2c}")
	flags2c = sorted(flags2c.items())
	print(f"flags2c<{n}>={flags2c}")
	flags_lens2c = sorted(flags_lens2c.items())
	print(f"flags_lens2c<{n}>={flags_lens2c}")
	cycle_lens2c = sorted(cycle_lens2c.items())
	print(f"cycle_lens2c<{n}>={cycle_lens2c}")
	flags_oplens_cclens2c = sorted(flags_oplens_cclens2c.items())
	print(f"flags_oplens_cclens2c<{n}>={flags_oplens_cclens2c}")



def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description="search_perm_for_crypt"
        , epilog=""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-n', '--bit_size', type=int, default=[], nargs="*"
                        , help='n bits')
    
    args = parser.parse_args(args)
    
    ns = args.bit_size
    for n in ns:
      if n>=2:
        _show(n)



def _t(n):
	sz = factorial(2**n)
	print(f"(2^{n})! == {sz} #{sz.bit_length()} bits")
	return

#for n in range(3,6):_t(n)


if __name__ == "__main__":
    main()


