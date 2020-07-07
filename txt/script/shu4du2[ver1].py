
import math as mh
import operator as op
digits = '123456789'
tt, ff = True, False
ee = Exception

rg = range
pr = print
def sw(s):
	pr(s, end='')
def prx(n):
	for _ in rg(n): pr()


class 数独:
	def __init__(sf, nrc, cs, sp, tb, ohvx):
		nr, nc = nrc
		sf.nrc = nr, nc # per sub-square
		sf.cs = cs
		sf.sp = sp
		sf.tb = tb
		sf.ts = None
		sf.ohvx = ohvx
		n2 = nr*nc
		assert type(nr) is int and nr > 0
		assert type(nc) is int and nc > 0
		assert type(cs) is str
		assert len(cs) == n2
		assert len(set(cs)) == n2
		assert type(sp) is str
		assert len(sp) == 1
		assert len(set(cs+sp)) == n2 + 1
		assert len(tb) == n2
		for row in tb:
			assert len(row) == n2
			assert set(row) <= set(cs+sp)
		assert len(set(cs+sp+ohvx)) == n2 + 5

	def show(sf):
		assert sf.ts is not None
		nr, nc = sf.nrc
		cs = sf.cs
		sp = sf.sp
		o,h,v,x = sf.ohvx
		ts = sf.ts
		n2 = nr*nc; n3r = n2*nc; n3c = n2*nr
		rs = (x+(x+h*nr)*nc)*nr
		assert len(rs) == n3c + n2 + nr
		for rr in range(n3r):
			if rr%n2 == 0: pr(rs)
			if rr%nc == 0: pr(rs)
			
			r = rr//nc; i = rr%nc
			for c in range(n2):
				ss = ts[r][c]
				if c%nc == 0: sw(v)
				sw(v)
				beg = i*nr; end = beg + nr
				for ch in cs[beg:end]:
					sw(ch if ch in ss else o)
			pr()
	def final_show(sf):
		ts = sf.ts
		nr, nc = sf.nrc
		cs = sf.cs
		sp = sf.sp
		o,h,v,x = sf.ohvx
		ts = sf.ts
		n2 = nr*nc; n3r = n2*nc; n3c = n2*nr
		sz = max(len(s) for row in ts for s in row)
		sz += (sz>1)
		rs = (x+h*sz*nc)*nr
		for r in rg(n2):
			if r%nr == 0: pr(rs)
			for c in rg(n2):
				if c%nc == 0: sw(v)
				s = ts[r][c]
				s = ''.join(sorted(s))
				sw(o*(sz-len(s)) + s)
			pr()
	def start(sf):
		ts = [[set(sf.cs) if ch == sf.sp else set(ch)
			for ch in row]
			for row in sf.tb
			]
		sf.ts = ts
	def run(sf, *, x=ff, sw=tt):
		sf.start()
		ns = 'do_h do_v do_sq'.split()
		if x: ns.append('do_x')
		#fs = [getattr(sf, nm) for nm in ns]
		def shw(m, nm, *, __i = [-1]):
			if m and sw:
				prx(2)
				sf.show()
				__i[0] += 1
				pr(); pr(__i[0], nm); pr()
		m = tt; shw(m, 'start')
		while m:
			m = ff
			for nm in ns:
				r = getattr(sf, nm)(); shw(r, nm); m |= r
		if sw:
			prx(2)
			sf.final_show()

	def do_v(sf):
		ts = sf.ts
		nr, nc = sf.nrc; n2 = nr*nc
		m = ff
		for c in rg(n2):
			col = [ts[r][c] for r in rg(n2)]
			m |= sf.do(col)
		return m
	def do_x(sf):
		ts = sf.ts
		nr, nc = sf.nrc; n2 = nr*nc
		m = ff
		bw = [ts[r][r] for r in rg(n2)]
		fw = [ts[r][-1-r] for r in rg(n2)]
		m |= sf.do(bw)
		m |= sf.do(fw)
		return m
	def do_sq(sf):
		ts = sf.ts
		nr, nc = sf.nrc; n2 = nr*nc
		m = ff
		for i in rg(nc):
			rows = ts[i*nr:i*nr+nr]
			for j in rg(nr):
				sq = [s for row in rows for s in row[j*nc:j*nc+nc]]
				m |= sf.do(sq)
		return m
	def do_h(sf):
		ts = sf.ts
		nr, nc = sf.nrc; n2 = nr*nc
		m = ff
		for r in rg(n2):
			row = ts[r]
			m |= sf.do(row)
		return m
	def do(sf, line):
		nr, nc = sf.nrc
		return do(sf.nrc, sf.cs, line)
def acc(xs, *, op, new):
	xs = iter(xs)
	for r in xs: break
	else: raise ee
	r = new(r)
	for x in xs:
		r = op(r, x)
	return r
def do(nrc, chars, sets_of_line):
	# -> modified
	ss = sets_of_line
	cs = chars
	nr, nc = nrc; n2 = nr*nc
	assert n2 == len(cs) == len(ss)
	assert n2 == len(set(cs))
	try:
		assert set(cs) == acc(ss, op=op.__or__, new=set)
	except:
		pr(acc(ss, op=op.__or__, new=set))
		pr(ss)
		raise
	find = lambda ch: [s for s in ss if ch in s]
	xfind = lambda ch: [s for s in ss if ch not in s]
	def hdl(sub, opp):
		if sub and opp: 
			_hdl(sub, opp)
			_hdl(opp, sub)
	def _hdl(sub, opp):
		assert len(sub) + len(opp) == n2
		s = acc(sub, op=op.__or__, new=set)
		assert len(s) >= len(sub)
		if len(s) == len(sub):
			rm(s, opp)
	def rm(s, opp):
		nonlocal d
		for s_ in opp:
			if s_ & s:
				d = ff
				s_ -= s
	ch_sz = lambda ch: len(find(ch))
	d = ff
	m = ff
	while not d:
		d = tt
		for ch in cs:
			yss = find(ch)
			#ys = acc(yss, op=op.__and__, new=set)
			xss = xfind(ch)
			#xs = acc(xss, op=op.__or__, new=set)
			#sz = len(s)
			hdl(yss, xss)
		if not d:
			m = tt
	return m

def guess_n2(len_tb_s):
	x = len_tb_s*4+5
	r = round(mh.sqrt(x))
	assert (r-1)**2 < x < (r+1)**2
	if r**2 != x: raise ee
	if r&1 != 1: raise ee
	n2 = (r-1)//2
	assert n2**2+n2-1 == len_tb_s
	return n2
def guess_nrc(n2):
	r = mh.floor(mh.sqrt(n2))
	for r in rg(r, -1, -1):
		c = n2//r
		if r*c == n2: break
	else: raise ee
	assert 0 < r <= c <= r*c == n2
	nrc = r, c
	return nrc
def main(tb_s):
	n2 = guess_n2(len(tb_s))
	nrc = guess_nrc(n2)
	cs = g.cs[:n2]
	if len(cs) != n2: raise ee
	main_(nrc, cs, '0', '_-|+', ';', tb_s)

def main_(nrc, cs, sp, ohvx, sep, tb_s):
	nr, nc = nrc; n2 = nr*nc
	assert len(tb_s) == n2**2 + (n2-1)*len(sep)
	tb = tb_s.split(sep)
	sf = 数独(nrc, cs, sp, tb, ohvx)
	sf.run()

def mk_s(fst, lst):
	return ''.join(map(chr, rg(ord(fst), ord(lst)+1)))
class g:
	cs = mk_s('1', '9') + mk_s('a', 'z')
	tb_s33 = '008600100;100048796;560000000;800965473;000200009;000037021;015009300;203074500;084300912'
	assert len(tb_s33) == 89
	tb_s33_2 = '063000080;700080000;090641000;000900050;300007000;100820004;005000100;200700009;030060200'
	#tb_s33_3 = '063000081;700080000;090641000;000900050;300007000;100820004;005000100;200700009;030060200'
	#tb_s33_4 = '063000082;700080000;090641000;000900050;300007000;100820004;005000100;200700009;030060200'
	tb_s23 =  '563104;200056;320401;016030;150603;604012'
	assert len(tb_s23) == 41
	tb_s22 = '0310;1003;2034;0420'
	assert len(tb_s22) == 19
	tb_ss = [tb_s33
			, tb_s33_2
			#, tb_s33_3
			#, tb_s33_4
			, tb_s23, tb_s22
			]


def f():
	import sys
	[_, tb_s] = sys.argv
	if tb_s:
		#main([3,3], digits, '0', 'X-|+', ';', tb_s)
		main(tb_s)
	else:
		for tb_s in g.tb_ss:
			prx(3); pr('='*60); pr(tb_s)
			main(tb_s)



if __name__ == '__main__':
	f()
