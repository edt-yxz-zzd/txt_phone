r"""
min_add

pow(a,e)
	1+1=2
	...
	x+y=e

see: txt/others/最小加法链.txt

min_add 1 = 0
err: min_add n | n>=2 = err: 1+min {min_add i + min_add (n-i) | i<-[1..n//2]}
"""


import ast
from copy import deepcopy
from functools import reduce
import operator as opss

def subsets_of(it):
	it = iter(it)
	yield []
	ls = []
	for x in it:
		ls.append(x)
		n = len(ls)
		i = 1<<n
		for j in range(i//2, i):
			out = []
			for y in (ls):
				assert j
				if j&1:
					out.append(y)
				j >>= 1
			assert not j
			assert out[-1] is x
			yield out

#for _ in subsets_of("012"):print(_)


_ls = [
		(0, [], [])
		,(0, [1], [[1]])
		]
def _fill__main(ls, n):
	w = len(ls)
	if n <= w:
		return

	i = -1
	for i in range(w, 2):
		yield (i, _ls[i])
	del i
	w = len(ls)

	for i in range(w, n):
		(mi, ss) = _fill__search(ls, i)
		assert mi < i
		#0;print(f"i={i}; mi={mi}; ss={ss}")
		us = reduce(opss.__or__, ss)
		#0;print(f"i={i}; mi={mi}; us={us}; ss={ss}")
		#0;print(f"ls={ls}")
		yield (i, (mi, us, ss))
	w = len(ls)
	assert n <= w
	return

def _fill__search(ls, i):
	assert len(ls) == i >= 2
	g_mi = _upper_bound(ls, i)
	g_ss = []
	def update(s):
		nonlocal g_mi
		mi = len(s)-1
		assert mi <= g_mi
		if mi == g_mi:
			g_ss.append(s)
		elif mi < g_mi:
			g_mi = mi
			#bug:g_ss[:] = [s]
			del g_ss[:]
			g_ss.append(s)
		else:
			raise Exception("mi>g_mi")
		return

	#topdown

	#j -> {k} @@[arr<s> j k] @@not empty except [j==i]
	# finally: s:=set(j2arrs)
	# curr_j := min j2arrs
	j2arrs = {i:()}

	#j -> {k-j} @@[arr<s> j k]
	#@j<-j2coarrs. [j<curr_j]
	#[j2coarrs/-\j2arrs =={}]
	j2coarrs = {}

	#k -> maybe {j,k-j} @@[arr<s> j k] @@len<-{0,2}
	#keys<={curr_j..}
	#k2maybe_arr+ks_without_arr == j2arrs
	k2maybe_arr = {}
	ks_without_arr = {i}

	#{k} which require support
	#[k<-ks_wait]==>>[k2maybe_arr[k]=={}]
	#  not <<==
	#@k<-ks_wait. k>=curr_j
	#ks_wait <= ks_without_arr
	ks_wait = {i}

	#@x<-arr_forbid. ?(k:{j,k-j})<-k2maybe_arr. (k-x)<-(j2arrs\-/j2coarrs)
	#arr_forbid/-\j2arrs=={}
	#arr_forbid/-\j2coarrs=={}
	arr_forbid = set()
	4;call_stack = []
	5;__on__ = 0


	def get_mi(j):
		return ls[j][0] #mi
	def f_recur_main(j):
		4;call_stack.append(j)
		f_recur(j)#recur
		4;call_stack.pop()
	def f_recur(j):
		#@jj<-j2arrs. [jj>=j]
		assert j in j2arrs
		nonlocal __on__
		__on__ = (i,j)==(5,4)
		__on__ = call_stack==[5,4,2]
		if __on__:
			0;print(f"_fill__search.f_recur({j})@i={i}")
		4;print(f"f_recur({j})@i={i}: call_stack={call_stack}")

		if j==1:
			#bug: if not ks_wait:
			assert 1 in ks_wait
			if len(ks_wait)==1:
				s = set(j2arrs)
				update(s)
			return

		w = len(j2arrs)
		if j!=i:
			if w-1+get_mi(j) > g_mi:
				return
		w_ = len(j2coarrs)
		pad = 0
		if 1 not in j2coarrs:
			pad +=1
		if j>2:
			if 2 not in j2coarrs:
				pad +=1
			if j>4:
				if 3 not in j2coarrs and 4 not in j2coarrs:
					pad +=1
		#bug:pad = max(pad, bool(ks_wait))
		#   @j<-ks_wait
		if not pad:
			sz = len(ks_wait)-(j in ks_wait)
			pad = bool(sz)
		if __on__:
			0;print(f"fast test: {w+w_+pad-1}={w}+{w_}+{pad}-1=len(j2arrs)+len(j2coarrs)+pad-1 <?> g_mi={g_mi};ks_wait={ks_wait} @f_recur({j})@i={i}")
		if w + w_ + pad-1 > g_mi:
			return

		#if w + w_ + pad == g_mi:
			#s = set(j2arrs)|set(j2coarrs)|{1...}
		####

		if __on__:
			0;print(f"pass fast test @f_recur({j})@i={i}")
		w = len(j2arrs)
		begin = begin0 = (j+1)//2
		if j2coarrs:
			begin1 = max(j2coarrs)
			begin = max(begin0, begin1)
		end = j
		if not ks_wait:
			assert j2coarrs
			assert begin == begin1
			end = begin+1
		elif ks_wait:
			km = max(ks_wait)
			if __on__:
				#0;print(f"km={km}=?={j}=j;ks_without_arr={ks_without_arr}")
				pass
			assert km>=j
			#j_*2>=km
			begin2 = (km+1)//2
			begin = max(begin, begin2)
		if end <= begin:
			assert ks_wait
			assert begin==begin2
			0;print(f"begin={begin}>={end}=end;ks_wait={ks_wait}")
			return
		assert begin0-1 <= j-begin0 <= begin0 <= begin < end <= j

		0;_save = (j2arrs, j2coarrs, k2maybe_arr, ks_without_arr, ks_wait)
		_save = (*map(deepcopy, _save),)
		for j_ in reversed(range(begin, end)):
			0;assert _save == (j2arrs, j2coarrs, k2maybe_arr, ks_without_arr, ks_wait)
			#######
			if len(j2arrs)+get_mi(j_) > g_mi:
				continue
			handle_j_(j_)
		return#f_recur
	def add_new(jj):
	def update_arr_forbid__add_new(jj):
		#TODO: update arr_forbid
	def handle_j_(j_):
		#j2arrs, j2coarrs
		#k2maybe_arr, ks_without_arr, ks_wait
		#
		#bug:ks = [k for k in ks_without_arr if k-j_ <= j_]
		#ks = [k for k in ks_wait if k-j_ <= j_]
		ks = [*ks_wait] #since begin2
		#  before add_new
		co = j2coarrs.pop(j_, ())
		if not co:
			add_new(jj)#TODO: rollback
		#j2arrs[j_] = ???
		_arrs = [j_+d for d in co] # basic
		ks_without_arr.add(j_)
		#TODO: update ks_wait in add_new??
		#bug: ks_wait.add(j_)
		for xxx in j2coarrs:
			if j_-xxx in j2coarrs:
				break
		else:
			ks_wait.add(j_)

		if 0:
			#not take care arr_forbid
			#  result duplicate
			for _ks in subsets_of(ks):
				handle_ks(_ks, co, j_, _arrs)
		else:
			_ks = []
			apply_arr_forbid(j_, co, _arrs, 0, ks, _ks)
		ks_wait.discard(j_)
		ks_without_arr.remove(j_)
		if co:
			j2coarrs[j_] = co
		return#handle_j_


	def apply_arr_forbid(j_, co, _arrs, at, ks, _ks):
		#_ks |<=| ks[:at]
		#fill _ks as subset of ks, s.t. arr_forbid
		if at == len(ks):
			handle_ks(_ks, co, j_, _arrs)
			return
		x = ks[at]
		at += 1
		apply_arr_forbid(j_, co, _arrs, at, ks, _ks)
		#TODO: append x or skip??
		#TODO: update arr_forbid
		_ks.append(x)
		apply_arr_forbid(j_, co, _arrs, at, ks, _ks)
		_ks.pop()
		return


	def handle_ks(_ks, co, j_, _arrs):
		j2arrs[j_] = _ks+_arrs
		if j2arrs[j_]:
			_handle_ks(_ks, co, j_)
		del j2arrs[j_]
	def _handle_ks(_ks, co, j_):
		#TODO: update arr_forbid
		news = set()
		if not co:
			news.add(j_)

		for k in _ks:
			kj = k-j_
			if kj == j_:
				continue
			assert kj < j_
			_co = j2coarrs.setdefault(kj, set())
			if not _co:
				news.add(kj)
			_co.add(j_)
			ks_without_arr.remove(k)
			ks_wait.remove(k)
			k2maybe_arr[k] = {j_, kj}

		_del = set()
		for k in ks_wait:
			for jj in news:
				kjj = k-jj
				if kjj in j2arrs or kjj in j2coarrs:
					_del.add(k)
					break
		#ks_wait -= _del
		ks_wait.__isub__(_del)
		if __on__:
			0;print(f"ks_wait={ks_wait}; _del={_del}")
		
		#TODO
		f_recur_main(j_)#recur

		#recover state
		#ks_wait |= _del
		ks_wait.__ior__(_del)
		for k in _ks:
			kj = k-j_
			if kj == j_:
				continue
			_co = j2coarrs[kj]
			_co.remove(j_)
			if not _co:
				del j2coarrs[kj]
			del k2maybe_arr[k]
			ks_without_arr.add(k)
			ks_wait.add(k)
		return#handle_ks


	#TODO
	f_recur_main(i)
	return g_mi, g_ss


def _upper_bound(ls, i):
	assert len(ls) == i >= 2
	mi = min(ls[j][0]+1 for j in range((i+1)//2, i) if (i-j) in ls[j][1])
	try:
		assert mi < i
		assert mi <= ls[-1][0]+1
		assert i<4 or mi <= ls[-2][0]+1
	except:
		1;print(f"i={i}; mi={mi}")
		1;print(f"ls={ls}")
		for j in range((i+1)//2, i):
			if (i-j) in ls[j][1]:
				mi = ls[j][0]+1
		raise

	s2 = bin(i)
	assert s2.startswith("0b1")
	m = len(s2)+s2.count("1") -4
	mi = min(mi, m)

	s2 = repr_fibonacci(i)
	assert s2.startswith("0f1")
	m = len(s2)+s2.count("1") -4
	mi = min(mi, m)

	return mi


def repr_fibonacci(i):
	assert i >=0
	weight = [1, 2]
	while weight[-1] < i:
		x = sum(weight[-2:])
		weight.append(x)
	while weight[-1] > i:
		weight.pop()
	digits = []
	t = i
	for w in reversed(weight):
		if t < w:
			digits.append(0)
		else:
			digits.append(1)
			t -= w
	assert (i==0 and not digits) or (i and digits and digits[0])
	assert not t
	s = "".join(map(str, digits))
	return f"0f{s}"






class MinAdd:
	r"""
	ls :: n -> (min_add n, union_min_addsets_of n, min_addsets_of n)
	ls :: [(uint, [pint], [[pint]])]
	ls :: [(uint, {pint}, [{pint}])]
	"""
	def __init__(sf, ls):
		sf.ls = [*ls]
	def fill(sf, n):
		for i, x in _fill__main(sf.ls, n):
			sf._append_(i, x) #x==(mi, us, ss)
	def min_add(sf, n):
		if n < 0:
			raise Exception(f"min_add({n}): n<0")
		sf.fill(n+1)
		return sf.ls[n]
	def _append_(sf, i, x):
		assert i == len(sf.ls)
		sf.ls.append(x)
	def iter(sf, m, n):
		assert m >= 0
		assert n >= 0
		if 0 <= m < n:
			#sf.fill(n)
			for i in range(m, n):
				yield sf.min_add(i)
	def _get_(sf, i):
		return sf.ls[i]
	def _show_(sf, i, *, file):
		(mi, us, ss) = sf.min_add(i)
		ss = [*map(list, ss)]
		for s in ss: s.sort()
		#ss.sort()
		us = sorted(us)
		print(f"{i}:{mi}:{us}:{ss}", file=file)
	def show(sf, m, n, *, file):
		#it = enumerate(sf.iter(m,n), m)
		#for i, (mi, ps) in it:
			#ps = (*ps,)
		for i in range(m, n):
			sf._show_(i, file=file)
	@classmethod
	def parse_line(cls, s):
		s = s.strip()
		if not s or s.startswith("#"):
			return
		s = s.replace(":", ",")
		s = f"({s!s})"
		i, mi, us, ss = ast.literal_eval(s)
		us = {*us}
		ss = [*map(set, ss)]
		return i, mi, us, ss
	@classmethod
	def iter_read_lines(cls, fin):
		for lineno, s in enumerate(fin):
			try:
				m = cls.parse_line(s)
			except Exception:
				raise Exception(f"MinAdd.iter_read_lines:lineno={lineno}:{s!r}")

			if m is not None:
				yield lineno, s, m
	@classmethod
	def read(cls, fin):
		ls = []
		it = cls.iter_read_lines(fin)
		for j, (lineno, s, (i,mi,us, ss)) in enumerate(it):
			if j!=i:
				raise Exception(f"MinAdd.read:lineno={lineno}:{s!r}")
			ls.append((mi, us, ss))
		return ls
	@classmethod
	def from_file(cls, fin, **kw):
		ls = cls.read(fin)
		sf = cls(ls, **kw)
		return sf



class MinAdd__file(MinAdd):
	def __init__(sf, ls, *, fcache):
		sf.fcache = fcache
		super().__init__(ls)
	def _append_(sf, i, x):
		super()._append_(i, x)
		sf._show_(i, file=sf.fcache)















def main_(m, n, mk_fin, mk_fout):
	cls = MinAdd__file
	with mk_fin() as fin:
		#ls = cls.read(fin)
		pass
	#TODO
	0;ls = []
	with mk_fout() as fout:
		sf = cls(ls, fcache=fout)
		sf.show(m, n, file=None)

def main(args=None):
	import argparse

	parser = argparse.ArgumentParser(
		description="min_add for pow"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-io', '--inout_cache_file'
						, type=str, required=True
						, help='inout_cache_file path')
	parser.add_argument("m", type=int
						, help='begin idx for show')
	parser.add_argument("n", type=int
						, help='end idx for show')

	args = parser.parse_args(args)
	m = args.m
	n = args.n

	fname = args.inout_cache_file
	encoding="utf8"
	def mk_fin():
		try:
			return open(fname, 'rt', encoding=encoding)
		except Exception:
			with open(fname, 'xt', encoding=encoding):pass
			return open(fname, 'rt', encoding=encoding)

	def mk_fout():
		return open(fname, 'at', encoding=encoding)
	main_(m, n, mk_fin, mk_fout)

if __name__ == "__main__":
	main()






