

r"""

from 密码学场景与函数.txt
		derived_key<rnd_at,n> :: bit{2^n} -> [bit{2^(n-1)}]{rnd_at(n-1)}
		rnd_at :: int{>=0} -> int{>=2}
			why [output>=2]??
				if [output==1]:
					half bits were not encrypted
		def recur_Feistel<rnd_at, derived_key, n, key>(msg):
			#[rnd_at(?)===2]:
			#   O(n*2^n) i.e. O(N*log2(N))
			#   derived_key<>(key) := [key[:/2], key[/2:]]
			assert [bit_len(msg)==2^n==bit_len(key)>=1]
			if n==0:
				return key xor msg
			
			F<round_key> := recur_Feistel<rnd_at, derived_key, n-1, round_key>
			L, R := msg
			for round_key in derived_key<rnd_at, n>(key):
				L, R := R, L xor F<round_key>(R)
			return L++R

#"""

from abc import ABC, abstractmethod


class RecurFeistel__keys:
	def __init__(sf, cipher:"RecurFeistelABC", m, n, key):
		#sf._cipher = cipher
		#sf._m = m
		#sf._n = n

		N = 1<<n
		M = 1<<N
		assert 0<=key<M
		kkk = M-1-key
		if not m >=0:raise ValueError
		m1 = m//2
		m0 = m-m1
		assert 0<=m1<=m0<=m
		sf._r0 = range(key, key+m0)
		sf._r1 = range(kkk+1-m1, kkk+1)
		sf._M = M
		sf._0gt1 = m0>m1

		try:
			assert [*reversed(sf)] == [*reversed([*sf])]
		except:
			s0,s1 = [*reversed(sf)], [*reversed([*sf])]
			print(f"m={m};n={n};key={key}")
			print(f"s0={s0};s1={s1};")
			raise
	def __iter__(sf):
		it0 = iter(sf._r0)
		it1 = reversed(sf._r1)
		for p in zip(it0, it1):
			for k in p:
				yield k%sf._M
		#for k in it0: yield k%sf._M
		if sf._0gt1:
			yield next(reversed(sf._r0))
	def __reversed__(sf):
		it0 = reversed(sf._r0)
		it1 = iter(sf._r1)
		if sf._0gt1:
			yield next(it0)
		it = zip(it1, it0)
		for p in it:
			for k in p:
				yield k%sf._M
		#for k in it0: yield k%sf._M
def _test__RecurFeistel__keys():
	for m in range(4):
		for n in range(4):
			N = 1<<n
			M = 1<<N
			for k in range(M):
				sf = RecurFeistel__keys(None, m, n, k)
				s0 = [*iter(sf)]
				s1 = [*reversed(sf)]
				s1.reverse()
				try:
					assert s0==s1
				except:
					print(f"m={m};n={n};k={k}")
					print(f"s0={s0};s1={s1};")
					raise
_test__RecurFeistel__keys()

class RecurFeistelABC(ABC):
	@abstractmethod
	def rnd_at(sf, n:int):
		pass
	@abstractmethod
	def iter_derived_keys(sf, to_decrypt:bool, n:int, key:int):
		pass
	def recur_Feistel__repeat_m(sf, m:int, to_decrypt:bool, n:int, key:int, msg:int):
		keys = RecurFeistel__keys(sf, m, n, key)
		return sf.recur_Feistel__repeat(to_decrypt, n, keys, msg)

	def recur_Feistel__repeat(sf, to_decrypt:bool, n:int, keys:"reversible[int]", msg:int):
		to_decrypt = bool(to_decrypt)
		if to_decrypt:
			it = reversed(keys)
		else:
			it = iter(keys)
		f = sf.recur_Feistel
		for key in it:
			msg = f(to_decrypt, n, key, msg)
		return msg
	def recur_Feistel(sf, to_decrypt:bool, n:int, key:int, msg:int):
		if n==0:
			assert 0 <= key < 2
			assert 0 <= msg < 2
			return key ^ msg
		to_decrypt = bool(to_decrypt)
		
		N_2 = 1<<(n-1)
		L, R = half_cut(N_2, msg)
		n_1 = n-1
		if to_decrypt:
			L, R = R, L
		for round_key in sf.iter_derived_keys(to_decrypt, n, key):
			#bug: False instead to_decrypt
			#     to_decrypt use only in toplayer
			L, R = R, L ^ sf.recur_Feistel(False, n_1, round_key, R)
		if to_decrypt:
			L, R = R, L
		return half_concat(N_2, L, R)

def half_cut(N_2, i):
	#bug: L, R = i>>N_2, i&(N_2-1)
	L, R = i>>N_2, i&((1<<N_2)-1)
	return L, R
def half_concat(N_2, L, R):
		return (L<<N_2) | R
class RecurFeistel__fixed_2round(RecurFeistelABC):
	r"""
	TIME(recur_Feistel) = O(n*2**n) = O(N*log2(N))
		N == 2**n == bit_len(key) == bit_len(msg)
	not perfect:
		key := 0
		*[msg := 0]:
			out == 0
		*[msg := 1<<x][x>N/4]:
			out is not random
		==>> recur_Feistel__repeat
	#"""
	def rnd_at(sf, n:int):
		return 2
	def iter_derived_keys(sf, to_decrypt:bool, n:int, key:int):
		assert n>0
		to_decrypt = bool(to_decrypt)
		N_2 = 1<<(n-1)
		L, R = half_cut(N_2, key)
		if to_decrypt:
			yield R
			yield L
		else:
			yield L
			yield R





def recur_Feistel__bytes__fixed_2round(m:int, to_decrypt:bool, n:int, key:bytes, msg:bytes, *, byteorder:'big|little'):
	sf = RecurFeistel__fixed_2round()
	to_decrypt = bool(to_decrypt)
	return recur_Feistel__bytes(sf, m, to_decrypt, n, key, msg, byteorder=byteorder)
def recur_Feistel__bytes(sf, m:int, to_decrypt:bool, n:int, key:bytes, msg:bytes, *, byteorder:'big|little'):
	to_decrypt = bool(to_decrypt)
	N = 2**n
	if not len(key)==len(msg) == N:
		raise eee
	key = int.from_bytes(key, byteorder=byteorder)
	msg = int.from_bytes(msg, byteorder=byteorder)
	#mmm = sf.recur_Feistel(to_decrypt, n+3, key, msg)
	mmm = sf.recur_Feistel__repeat_m(m, to_decrypt, n+3, key, msg)
	mmm = int.to_bytes(mmm, N, byteorder=byteorder)
	return mmm



if 1:
	def choice_decode(n, x_fmt, bs):
		if not isinstance(bs, bytes): raise TypeError
		if not 1<<n == len(bs): raise ValueError
		if x_fmt == "hex":
			i = int.from_bytes(bs, 'big')
			x = f"{i:0>{2*len(bs)}x}"
		elif x_fmt == "raw_ascii":
			x = bs.decode("ascii")
		elif x_fmt == "repr_bytes":
			x = repr(bs)
		else:
			raise Exception("unknown case: {x_fmt!s}")
		return x
	def choice_encode(n, x_fmt, x):
		if x_fmt == "hex":
			x = x.replace("-", "")
			x = x.replace("_", "")
			if not x: raise ValueError
			if len(x) &1: raise Exception('not even')
			i = int(f"0x{x!s}", base=16)
			bs = i.to_bytes(len(x)>>1, 'big')
		elif x_fmt == "raw_ascii":
			bs = x.encode("ascii")
		elif x_fmt == "repr_bytes":
			x = ast.literal_eval(x)
			if not isinstance(x, bytes): raise TypeError(f"{type(x)}")
			bs = x
		else:
			raise Exception("unknown case: {x_fmt!s}")
		if len(bs) != 1<<n: raise Exception("len not match log2_len")
		return bs
def main(args=None):
	import argparse, ast

	choices = "hex raw_ascii repr_bytes".split()
	parser = argparse.ArgumentParser(
		description="recur Feistel construction to mk block cipher"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('-r', '--repeat', type=int, default=None
						, required=True
						, help='encrypt r round; 0-not encrypt;1-same as recur_Feistel; recommand at least 4')
	parser.add_argument('-n', '--log2_len', type=int, default=None
						, required=True
						, help='2**n == len(key) == len(msg)')
	parser.add_argument('-k', '--key', type=str, default=None
						, required=True
						, help='key')
	parser.add_argument('-m', '--msg', type=str, default=None
						, required=True
						, help='msg to encrypt/decrypt')
	parser.add_argument('-kf', '--key_format', type=str
						, default=None
						, choices=choices
						, required=True
						, help='how to input key')
	parser.add_argument('-mf', '--msg_format', type=str
						, default=None
						, choices=choices
						, required=True
						, help='how to input msg')
	parser.add_argument('-of', '--out_format', type=str
						, default=None
						, choices=choices
						, required=True
						, help='how to output result')
	parser.add_argument('-d', '--decrypt', action='store_true'
						, default = False
						, help='to decrypt instead of encrypt')
	parser.add_argument('-ltt', '--little', action='store_true'
						, default = False
						, help='little endian instead of big endian')


	args = parser.parse_args(args)
	f = recur_Feistel__bytes__fixed_2round
	nn = args.log2_len
	if not nn >= 0: raise ValueError
	mm = args.repeat
	if not mm >= 0: raise ValueError
	key_bs = choice_encode(nn, args.key_format, args.key)
	msg_bs = choice_encode(nn, args.msg_format, args.msg)
	if 1:
		_key = choice_decode(nn, args.key_format, key_bs)
		_msg = choice_decode(nn, args.msg_format, msg_bs)
		print(f"key={_key!s}")
		print(f"msg={_msg!s}")

	byteorder = "little" if args.little else "big"
	direction = "decrypt" if args.decrypt else "encrypt"
	if 1:
		print(f"byteorder={byteorder!r}")
		print(f"direction={direction!r}")
	mmm_bs = f(mm, args.decrypt, nn, key_bs, msg_bs, byteorder=byteorder)
	mmm = choice_decode(nn, args.out_format, mmm_bs)
	if 1:
		_mmm_bs = choice_encode(nn, args.out_format, mmm)
		assert _mmm_bs == mmm_bs
	print(f"out={mmm!s}")
	if 1:
		_msg_bs = f(mm, not args.decrypt, nn, key_bs, mmm_bs, byteorder=byteorder)
		assert _msg_bs == msg_bs

if __name__ == "__main__":
	main()



