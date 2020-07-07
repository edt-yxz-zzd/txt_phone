
r"""
呜呼哀哉尚飨
whazsx.py



==============
简单版
明文：他妈的
加密方选择：
	协议：呜呼哀哉尚飨
	密码提示：一蓑/烟雨/任平生
密码：哀烟雨哉
假设：$X$=呜呼哀哉尚飨.加密<哀烟雨哉>(他妈的)
密文：呜呼一蓑$X$任平生尚飨
解密方识别：
	#此处需人工识别或自动引用搜索结果
	呜呼，一蓑，任平生，尚飨
	=>协议：呜呼哀哉尚飨
	=>密码提示：一蓑/烟雨/任平生
	他妈的=呜呼哀哉尚飨.解密<哀烟雨哉>($X$)



def 呜呼哀哉尚飨.gen_byte_mask(key::bytes, L):
	global _hash_, _n_, _k0_
	k = _k0_
	for i in range(_n_):
		k = _hash_(k+key)
	ks = []; sz = 0
	for i in range(L):
		i = str(i).encode('utf8')
		k = _hash_(k+key+i)
		ks.append(k)
		sz += len(k)
		if sz >= L:
			kk = b''.join(ks)
			kk = kk[:L]
			break
	else:
		raise logic-error
	return kk
def 呜呼哀哉尚飨.read_prefix_ex(it):
	global _random_bytes_arg_
	read till (prefix[-2]-prefix[-1])%256 < _random_bytes_arg_
def 呜呼哀哉尚飨.mk_random_prefix():
def 呜呼哀哉尚飨.加密<key>(txt):
	global _zh_char256_
	bs = 呜呼哀哉尚飨.mk_random_prefix()
	key = key.encode('utf8')
	txt = txt.encode('utf8')
	L1 = len(txt)
	L2 = len(bs)+len(txt)
	kk1 = 呜呼哀哉尚飨.gen_byte_mask(bs, L1)
	kk2 = 呜呼哀哉尚飨.gen_byte_mask(key, L2)
	txt = kk1 xor txt
	mmm = kk2 xor (bs+txt)
	mmm = ''.join(_zh_char256_[b] for b in mmm)
	return mmm
def 呜呼哀哉尚飨.解密<key>(mmm):
	global _zh_char2idx_
	mmm = bytes(_zh_char2idx_[ch] for ch in mmm)
	L2 = len(mmm)
	key = key.encode('utf8')
	kk2 = 呜呼哀哉尚飨.gen_byte_mask(key, L2)
	bs = kk2 xor mmm
	bs,txt = 呜呼哀哉尚飨.read_prefix_ex(bs)
	txt = bytes(txt)
	L1 = len(txt)
	kk1 = 呜呼哀哉尚飨.gen_byte_mask(bs, L1)
	txt = kk1 xor txt
	txt = txt.decode('utf8')
	return txt





====================version2

呜呜呼哀哉尚飨v2  //呜呜 2
vs呜呼哀哉尚飨v1  //  呜 1



diff at gen k and output (k0,n)
*呜呼哀哉尚飨v1
	k = _k0_
	for i in range(_n_):
		k = _hash_(k+key)
*呜呜呼哀哉尚飨v2
	//(k0,n) are given by user
	//i begin from n
	//(i+key+k+key+i) instead of (k+key)
	k = k0
	for i in range(n, n+n):
		i = str(i).encode('utf8')
		k = _hash_(i+key+k+key+i)



python3_src-master/script/char/common_CJK/[common_CJK]ReadMe.txt
	86 矣郡惟淮荷哉嗣撰巳朕癸亥椅衙旱俺簿旬癌蕃猩塘擢薨懿裳脊稷葡憾蝗梗萄揖晏棠喀梢藩暑膊胤株筵棚沼弧敞榻殆鄂沮璋敖邸嗟膨黜悖逵漕攸蔬蛟嵌俸瘢嗜哺蕉杉侈梭麾胥汾掖琢戟甥荀斛耆隅茵檄
	256 竺笙翊釉宸潼徇礁僖臾泗瑾羲渥拷壕脯壑瑛孺熄瑚琶斡渤爰甄恁苔芍嗔偈褥痰裨舷磐勺簪蟠橡嫦逋珀佃夙濠肪枷剔薇椿蹙茄涓溥衢茸翌窒穹蛾卞衾陟琵菁雉猝曙酵邯懋眸曷瀑焙悸蛭珂揆瑁喙陂淙舫斫麝燮桔愆庠跛黍佚癖蹇曦湍蒜磬珥橙娑怏暹瓢逡嵋跏燧昴疵爻麒橄寤幄胛淞滓狎窈湫帑芹拌荻嬖盂碇燔倨皿瘠蚌祉淅洵楹秧咫筮蚣瞑攫悌跣趺褶灸樟魃倬翡傀殄岬菽俳槁蒿羸侏裟暝袈痘俑稔畛粕翕濂甑蜈葺柑楔椽匐樗嵬溟噫蔗琥匍碣嗾纛禳醵艮戡萸瓠雎槿侑枋肄暾慝梏楮檎汐豌蕨逑桎枳楸慊螟佶畦稗酊圄菖揄孱疥蓍蹉痍枸枇茯廛猊酩荏擘苒眄茱痂篁腱膈筌埴醍柝酎莪疝茴堀檗疳蒡嚆

==============
简单版
明文：他妈的
加密方选择：
	协议：呜呜呼哀哉尚飨
	密码提示：一蓑/烟雨/任平生
	初始散列值 :: str
	费力指数   :: int >0
密码：哀烟雨哉
假设：
	$X$=呜呜呼哀哉尚飨.加密<初始散列值,费力指数,哀烟雨哉>(他妈的)
	%Y%=字节串变中文(utf8(初始散列值))
	{Z}=正整数变中文(费力指数)
密文：呜呼一蓑%Y%哉$X$哉{Z}任平生尚飨
解密方识别：
	#此处需人工识别或自动引用搜索结果
	呜呼，一蓑，哉，哉，任平生，尚飨
	=>协议：呜呜呼哀哉尚飨
	=>密码提示：一蓑/烟雨/任平生
	他妈的=呜呜呼哀哉尚飨.解密<f(%Y%),g({Z}),哀烟雨哉>($X$)

"""


import hashlib
import random

def sha256(bs):
	m = hashlib.sha256()
	m.update(bs)
	return m.digest()

def remove_spaces(s):
	return ''.join(s.split())
def without_spaces(s):
	s = s.strip()
	if has_space(s):raise eee
	return s
def has_space(s):
	ls = s.split()
	return len(ls) > 1
def xor_bytes(lhs, rhs):
	if len(lhs) != len(rhs): raise eee
	return bytes(a^b for a,b in zip(lhs,rhs))




def _mk_1s_bs(L):
	return b'\1'*L
def bytes2uint__bb(bs):
	#bigendian, bijection
	u = _bytes2uint__bb(bs)
	bs_ = _uint2bytes__bb(u)
	assert bs_ == bs
	return u
def _bytes2uint__bb(bs):
	bs0 = _mk_1s_bs(len(bs))
	offset = int.from_bytes(bs0, byteorder='big')
	diff = int.from_bytes(bs, byteorder='big')
	return offset+diff
def uint2bytes__bb(u):
	#bigendian, bijection
	bs = _uint2bytes__bb(u)
	u_ = _bytes2uint__bb(bs)
	assert u_ == u
	return bs
def _uint2bytes__bb(u):
	assert u >= 0
	#bs = u.to_bytes((u.bit_length() + 7) // 8, byteorder='big')
	L = (u.bit_length() + 7) // 8
	bs0 = _mk_1s_bs(L)
	offset = int.from_bytes(bs0, byteorder='big')
	if u < offset:
		offset >>= 8
		L -= 1
	assert offset <= u
	diff = u-offset
	bs = diff.to_bytes(L, byteorder='big')
	return bs












class 呜呼哀哉尚飨默认参数:
	_hash = sha256
	_random_bytes_arg = 8
	_may_fixed_random_bytes = None
	_n = 2**16
	_k0 = bytes(range(2**8))
	_zh_char256 = "竺笙翊釉宸潼徇礁僖臾泗瑾羲渥拷壕脯壑瑛孺熄瑚琶斡渤爰甄恁苔芍嗔偈褥痰裨舷磐勺簪蟠橡嫦逋珀佃夙濠肪枷剔薇椿蹙茄涓溥衢茸翌窒穹蛾卞衾陟琵菁雉猝曙酵邯懋眸曷瀑焙悸蛭珂揆瑁喙陂淙舫斫麝燮桔愆庠跛黍佚癖蹇曦湍蒜磬珥橙娑怏暹瓢逡嵋跏燧昴疵爻麒橄寤幄胛淞滓狎窈湫帑芹拌荻嬖盂碇燔倨皿瘠蚌祉淅洵楹秧咫筮蚣瞑攫悌跣趺褶灸樟魃倬翡傀殄岬菽俳槁蒿羸侏裟暝袈痘俑稔畛粕翕濂甑蜈葺柑楔椽匐樗嵬溟噫蔗琥匍碣嗾纛禳醵艮戡萸瓠雎槿侑枋肄暾慝梏楮檎汐豌蕨逑桎枳楸慊螟佶畦稗酊圄菖揄孱疥蓍蹉痍枸枇茯廛猊酩荏擘苒眄茱痂篁腱膈筌埴醍柝酎莪疝茴堀檗疳蒡嚆"
	assert len(_zh_char256) == 2**8
	_zh_char2idx = {ch:i for i,ch in enumerate(_zh_char256)}
	assert len(_zh_char2idx) == 2**8
	#######












def echo(x):
	return x
class 呜呼哀哉尚飨:
	_version = 1
	def ireplace(sf, **kw):
		d = sf.get_init_args()
		d.update(kw)
		return type(sf)(**d)
	def get_init_args(sf):
		return dict(sf.__kw)
	def __new__(cls, **kw):
		sf = super(__class__, cls).__new__(cls)
		sf.__kw = kw
		return sf
	def __init__(呜呼哀哉尚飨, *
			,_hash = 呜呼哀哉尚飨默认参数._hash
			,_random_bytes_arg = 呜呼哀哉尚飨默认参数._random_bytes_arg
			,_may_fixed_random_bytes = 呜呼哀哉尚飨默认参数._may_fixed_random_bytes
			,_n = 呜呼哀哉尚飨默认参数._n
			,_k0 = 呜呼哀哉尚飨默认参数._k0
			#,_zh_char256 = 呜呼哀哉尚飨默认参数._zh_char256
			#,_zh_char2idx = 呜呼哀哉尚飨默认参数._zh_char2idx
			):
		呜呼哀哉尚飨._hash = _hash
		呜呼哀哉尚飨._random_bytes_arg = _random_bytes_arg
		呜呼哀哉尚飨._may_fixed_random_bytes = _may_fixed_random_bytes
		呜呼哀哉尚飨._n = _n
		呜呼哀哉尚飨._k0 = _k0
		#呜呼哀哉尚飨._zh_char256 = _zh_char256
		#呜呼哀哉尚飨._zh_char2idx = _zh_char2idx
		呜呼哀哉尚飨._zh_char256 = 呜呼哀哉尚飨默认参数._zh_char256
		呜呼哀哉尚飨._zh_char2idx = 呜呼哀哉尚飨默认参数._zh_char2idx
		assert 0 < _random_bytes_arg < 256
		assert _n > 0
		_r = _may_fixed_random_bytes
		if _r is not None:
			assert len(_r) > 1
			_r2,_ = 呜呼哀哉尚飨.read_prefix_ex(_r*2)
			assert _r2 == _r
	
	@echo
	def read_prefix_ex(呜呼哀哉尚飨, it):
		#Iter int -> (bs, Iter int)
		#global _random_bytes_arg_
		it = iter(it)
		bbb = 呜呼哀哉尚飨._random_bytes_arg_()
		b = 256
		def is_bad(x,y):
			return (x-y)%b < bbb
		for r0 in it:break
		ls = [r0]
		for r1 in it:
			ls.append(r1)
			if is_bad(r0,r1):break
			r0 = r1
		return bytes(ls), it
	@echo
	def mk_random_prefix(呜呼哀哉尚飨):
		#->bs
		_r = 呜呼哀哉尚飨._may_fixed_random_bytes_()
		if (_r is not None):
			return _r
		f = random.randrange
		b = 256
		def mk():
			while 1:
				yield f(b)
		it = mk()
		prefix, _ = 呜呼哀哉尚飨.read_prefix_ex(it)
		return prefix
	
	@classmethod
	def _version_(呜呼哀哉尚飨):
		return 呜呼哀哉尚飨._version
	@echo
	def _may_fixed_random_bytes_(呜呼哀哉尚飨):
		return 呜呼哀哉尚飨._may_fixed_random_bytes
	@echo
	def _random_bytes_arg_(呜呼哀哉尚飨):
		return 呜呼哀哉尚飨._random_bytes_arg
	@echo
	def _hash_(呜呼哀哉尚飨, bs):
		return 呜呼哀哉尚飨._hash(bs)
	@echo
	def _zh_char256_(呜呼哀哉尚飨):
		return 呜呼哀哉尚飨._zh_char256
	@echo
	def _zh_char2idx_(呜呼哀哉尚飨):
		return 呜呼哀哉尚飨._zh_char2idx
	@echo
	def _n_(呜呼哀哉尚飨):
		return 呜呼哀哉尚飨._n
	@echo
	def _k0_(呜呼哀哉尚飨):
		return 呜呼哀哉尚飨._k0
	@echo
	def mk_hashed_key(呜呼哀哉尚飨, key:bytes):
		#global _hash_, _n_, _k0_
		_hash_ = 呜呼哀哉尚飨._hash_
		_n_ = 呜呼哀哉尚飨._n_()
		_k0_ = 呜呼哀哉尚飨._k0_()
		#key = key.encode('utf8')
		k = _k0_
		for i in range(_n_):
			k = _hash_(k+key)
		return k
	@echo
	def gen_byte_mask(呜呼哀哉尚飨, key:bytes, L):
		#bs->uint->bs{len}
		#global _hash_
		_hash_ = 呜呼哀哉尚飨._hash_
		k = 呜呼哀哉尚飨.mk_hashed_key(key)
		
		ks = []; sz = 0
		for i in range(L):
			i = str(i).encode('utf8')
			k = _hash_(k+key+i)
			ks.append(k)
			sz += len(k)
			if sz >= L:
				break
		else:
			if L>0: raise Exception(f'logic-error:L={L}')
		kk = b''.join(ks)
		kk = kk[:L]
		return kk
	@echo
	def salt_encrypt(呜呼哀哉尚飨, encrypt, key, txt):
		#(bs -> bs -> bs) -> bs -> bs -> bs
		bs = 呜呼哀哉尚飨.mk_random_prefix()
		txt = encrypt(bs, txt)
		mmm = encrypt(key, bs+txt)
		return bs, mmm
	@echo
	def salt_decrypt(呜呼哀哉尚飨, decrypt, key, mmm):
		#(bs -> bs -> bs) -> bs -> bs -> bs
		bs_txt = decrypt(key, mmm)
		bs,txt = 呜呼哀哉尚飨.read_prefix_ex(bs_txt)
		txt = bytes(txt)
		txt = decrypt(bs, txt)
		return bs, txt
	@echo
	def symmetry_cipher(呜呼哀哉尚飨, key, txt):
		#bs -> bs -> bs
		L1 = len(txt)
		kk1 = 呜呼哀哉尚飨.gen_byte_mask(key, L1)
		txt = xor_bytes(kk1, txt)
		return txt
	@echo
	def bytes2zh_str(呜呼哀哉尚飨, bs):
		#global _zh_char256_
		_zh_char256_ = 呜呼哀哉尚飨._zh_char256_()
		mmm = ''.join(_zh_char256_[b] for b in bs)
		return mmm
	@echo
	def zh_str2bytes(呜呼哀哉尚飨, mmm):
		#global _zh_char2idx_
		_zh_char2idx_ = 呜呼哀哉尚飨._zh_char2idx_()
		bs = bytes(_zh_char2idx_[ch] for ch in mmm)
		return bs
	@echo
	def 加密(呜呼哀哉尚飨, key, txt):
		key = key.encode('utf8')
		txt = txt.encode('utf8')
		rs, mmm = 呜呼哀哉尚飨.salt_encrypt(
				呜呼哀哉尚飨.symmetry_cipher
				,key, txt)
		mmm = 呜呼哀哉尚飨.bytes2zh_str(mmm)
		#version = 呜呼哀哉尚飨._version_()
		return rs, mmm
	@echo
	def 解密(呜呼哀哉尚飨, key, mmm):
		key = key.encode('utf8')
		mmm = 呜呼哀哉尚飨.zh_str2bytes(mmm)
		rs, txt = 呜呼哀哉尚飨.salt_decrypt(
				呜呼哀哉尚飨.symmetry_cipher
				,key, mmm)
		txt = txt.decode('utf8')
		version = __class__._version_()
		return version, rs, txt

	def 呜呼哀哉尚飨加解密(呜呼哀哉尚飨
			, 要解密, 密码提示, 文
			):
		版本号, 随机串, 结果 = 呜呼哀哉尚飨.呜呼哀哉尚飨加解密_ex(要解密, 密码提示, 文)
		return 结果
	def 呜呼哀哉尚飨加解密_ex(呜呼哀哉尚飨
			, 要解密, 密码提示, 文
			):
		f = 呜呼哀哉尚飨.呜呼哀哉尚飨解密 if 要解密 else 呜呼哀哉尚飨.呜呼哀哉尚飨加密
		版本号, 随机串, 结果 = f(密码提示, 文)
		return 版本号, 随机串, 结果
	def 呜呼哀哉尚飨加密(呜呼哀哉尚飨
			, 密码提示, 明文
			):
		头, 密码, 尾 = 呜呼哀哉尚飨.handle_key_hint(密码提示)
		版本号 = 呜呼哀哉尚飨._version_()
		随机串, 载荷 = 呜呼哀哉尚飨.加密(密码, 明文)
		密文 = f'{头}{载荷}{尾}'
		if (版本号, 随机串, 明文) != 呜呼哀哉尚飨.呜呼哀哉尚飨解密(密码提示, 密文): raise eee
		return 版本号, 随机串, 密文
	def handle_key_hint(_, 密码提示):
		'密码提示 eg "一蓑/烟雨/任平生"'
		密码提示 = without_spaces(密码提示)
		init, mid, tail = 密码提示.split('/')
		密码 = f'哀{mid}哉'
		头, 尾 = f'呜呼{init}', f'{tail}尚飨'
		return 头, 密码, 尾
	def 呜呼哀哉尚飨解密(呜呼哀哉尚飨
			, 密码提示, 密文
			):
		头, 密码, 尾 = 呜呼哀哉尚飨.handle_key_hint(密码提示)
		密文 = remove_spaces(密文)
		if len(密文) < len(头)+len(尾): raise eee
		if not 密文.startswith(头): raise eee
		if not 密文.endswith(尾): raise eee
		载荷 = 密文[len(头):-len(尾)]
		版本号, 随机串, 明文 = 呜呼哀哉尚飨.解密(密码, 载荷)
		return 版本号, 随机串, 明文



class 呜呜呼哀哉尚飨(呜呼哀哉尚飨):
	_version = 2
	@echo
	def mk_hashed_key(呜呜呼哀哉尚飨, key:bytes):
		#global _hash_, _n_, _k0_
		_hash_ = 呜呜呼哀哉尚飨._hash_
		n = _n_ = 呜呜呼哀哉尚飨._n_()
		_k0_ = 呜呜呼哀哉尚飨._k0_()
		#key = key.encode('utf8')
		k = _k0_
		for i in range(n, n+n):
			i = str(i).encode('utf8')
			k = _hash_(i+key+k+key+i)
		return k
	
	@echo
	def 加密(呜呜呼哀哉尚飨, key, txt):
		cls1 = 呜呼哀哉尚飨
		rs, mmm = cls1.加密(呜呜呼哀哉尚飨, key, txt)
		_n_ = 呜呜呼哀哉尚飨._n_()
		_k0_ = 呜呜呼哀哉尚飨._k0_()
		bs0 = _k0_
		bs1 = uint2bytes__bb(_n_-1)
		hh = 呜呜呼哀哉尚飨.bytes2zh_str(bs0)
		tt = 呜呜呼哀哉尚飨.bytes2zh_str(bs1)
		mmm = '哉'.join([hh, mmm, tt])
		return rs, mmm
	@echo
	def 解密(呜呜呼哀哉尚飨, key, mmm0):
		ls = mmm0.split('哉')
		L = len(ls)
		if L==1:
			#bug:return super().解密(key, mmm0)
			#    since mk_hashed_key changed
			#bug:kw = 呜呜呼哀哉尚飨.get_init_args()
			cls1 = 呜呼哀哉尚飨
			kw = cls1.get_init_args(呜呜呼哀哉尚飨)
			ver1 = cls1(**kw)
			return ver1.解密(key, mmm0)
		elif L==3:
			hh, mmm1, tt = ls
			bs0 = 呜呜呼哀哉尚飨.zh_str2bytes(hh)
			bs1 = 呜呜呼哀哉尚飨.zh_str2bytes(tt)
			k0 = bs0
			n = bytes2uint__bb(bs1)+1
			#bug:
			#	sf = 呜呜呼哀哉尚飨.ireplace(_k0=k0, _n=n)
			#	return sf.解密(key, mmm1)
			if (k0==呜呜呼哀哉尚飨._k0_()
					and n==呜呜呼哀哉尚飨._n_()
					):
				cls1 = 呜呼哀哉尚飨
				ver, rs, txt = cls1.解密(呜呜呼哀哉尚飨, key, mmm1)
				assert ver == 1
				ver = __class__._version_()
				return ver, rs, txt
			else:
				#bug:
				#   cls = type(呜呜呼哀哉尚飨)
				#   kw = 呜呜呼哀哉尚飨.get_init_args()
				cls = __class__
				kw = cls.get_init_args(呜呜呼哀哉尚飨)
				kw.update(_k0=k0, _n=n)
				ver2 = cls(**kw)
				return ver2.解密(key, mmm0)
		else:
			raise eee




def test():
	clss = [呜呼哀哉尚飨, 呜呜呼哀哉尚飨]
	rrr = 呜呼哀哉尚飨默认参数._may_fixed_random_bytes
	nnn = 呜呼哀哉尚飨默认参数._n
	kkk = 呜呼哀哉尚飨默认参数._k0
	
	d = dict
	ds = (
		[d # python whazsx.py a/b/c -d -n 1 -i abc -r b\'\\0\\0\'
				(v = 1
				,kh = 'a/b/c'
				,i = 'abc'
				,o = '呜呼a臾陂桎瑾喙c尚飨'
				,rs = b'\0\0'
				,n = 1
				#,k0 =
				)
		,d # python whazsx.py a/b/c -d -i abc -r b\'\\0\\0\'
				(v = 1
				,kh = 'a/b/c'
				,i = 'abc'
				,o = '呜呼a痍嚆蔗侑滓c尚飨'
				,rs = b'\0\0'
				#,n = 1
				#,k0 =
				)
		
		,d # python whazsx.py a/b/c -d -i abc -r b\'\\x11\\xf2mh\'
				(v = 1
				,kh = 'a/b/c'
				,i = 'abc'
				,o = '呜呼a膈渥磐羸篁嬖釉c尚飨'
				,rs = b'\x11\xf2mh'
				#,n =
				#,k0 =
				)
		
		,d # python whazsx.py a/b/c -d -i abc -r b\'\\x11\\xf2mh\' -n 20
				(v = 1
				,kh = 'a/b/c'
				,i = 'abc'
				,o = '呜呼a舷甄葺麝圄琶舷c尚飨'
				,rs = b'\x11\xf2mh'
				,n = 20
				#,k0 =
				)
		
		,d # python whazsx.py a/b/c -d -i abc -n 20 -sr -r b\'\\x03\\x86\\x07\\x13\\n\\x06\'
				(v = 1
				,kh = 'a/b/c'
				,i = 'abc'
				,o = '呜呼a剔燧稗佃侑斡菖舷殄c尚飨'
				,rs = b'\x03\x86\x07\x13\n\x06'
				,n = 20
				#,k0 =
				)
		
		,d # python whazsx.py a/b/c -d -i abc -r b\'\\0\\0\' -m 2 -n 10 -k0 'abc'
				(v = 2
				,kh = 'a/b/c'
				,i = 'abc'
				,o = '呜呼a曦湍蒜哉夙盂橙痍渥哉僖c尚飨'
				,rs = b'\0\0'
				,n = 10
				,k0 = b'abc'
				)
		
			])

	for d in ds:
		print(f'test {d!r}')
		v = d['v']
		kh = d['kh']
		i = d['i']
		o = d['o']
		rr = d.get('rs', rrr)
		nn = d.get('n', nnn)
		kk = d.get('k0', kkk)
		cls = clss[v-1]
		sf = cls(_k0=kk, _n=nn, _may_fixed_random_bytes=rr)
		
		ls = [(0, o, i), (v, i, o)]
		for (mm, i, o) in ls:
			method_version, random_bytes, output = sf.呜呼哀哉尚飨加解密_ex(
					要解密=(mm==0)
					, 密码提示=kh
					, 文=i
					)
			assert method_version==v
			assert random_bytes==rr
			assert output==o
		


#argparse bug @ help='%&'
def main(args=None):
	import argparse
	import sys
	import ast

	parser = argparse.ArgumentParser(
		description="呜呼哀哉尚飨加密协议"
		, epilog=r'''
		$ python whazsx.py a/b/c -d -n 1 -i abc -r b\'\\0\\0\'
		n=1
		r=b'\x00\x00'
		呜呼a臾陂桎瑾喙c尚飨
		
		$ python whazsx.py a/b/c -d -i abc -r b\'\\0\\0\'
		r=b'\x00\x00'
		呜呼a痍嚆蔗侑滓c尚飨
		
		$ python whazsx.py a/b/c -d -m 0 -i 呜呼a膈渥磐羸篁嬖釉c尚飨 -sr
		b'\x11\xf2mh'
		abc
		
		$ python whazsx.py a/b/c -d -i abc -r b\'\\x11\\xf2mh\'
		r=b'\x11\xf2mh'
		呜呼a膈渥磐羸篁嬖釉c尚飨
		
		$ python whazsx.py a/b/c -d -i abc -r b\'\\x11\\xf2mh\' -n 20
		n=20
		r=b'\x11\xf2mh'
		呜呼a舷甄葺麝圄琶舷c尚飨
		
		$ python whazsx.py a/b/c -d -i abc -n 20 -sr -r b\'\\x03\\x86\\x07\\x13\\n\\x06\'
		n=20
		r=b'\x03\x86\x07\x13\n\x06'
		b'\x03\x86\x07\x13\n\x06'
		呜呼a剔燧稗佃侑斡菖舷殄c尚飨
		
		==============================
		
		$ python whazsx.py a/b/c -d -i abc -r b\'\\0\\0\' -m 2 -n 10 -k0 'abc'
		k0~'abc'
		k0=b'abc'
		n=10
		r=b'\x00\x00'
		呜呼a曦湍蒜哉夙盂橙痍渥哉僖c尚飨
		
		
		$ python whazsx.py a/b/c -d -i abc -m 2 -n 10 -k0 'abc' | python whazsx.py a/b/c -m 0
		k0~'abc'
		k0=b'abc'
		n=10
		abc
		
		
		$ python whazsx.py a/b/c -d -i abc -m 2 -n 10 -k0 'abc' | python whazsx.py a/b/c -m 0 -n 10 -k0 'abc'
		k0~'abc'
		k0=b'abc'
		n=10
		k0~'abc'
		k0=b'abc'
		n=10
		abc
		
		
		$ python whazsx.py a/b/c -d -i abc -m 1 -n 10 -k0 'abc' | python whazsx.py a/b/c -m 0 -n 10 -k0 'abc'
		k0~'abc'
		k0=b'abc'
		n=10
		k0~'abc'
		k0=b'abc'
		n=10
		abc
		
		'''
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	
	kkk = 呜呼哀哉尚飨默认参数._k0
	nnn = 呜呼哀哉尚飨默认参数._n
	rrr = 呜呼哀哉尚飨默认参数._may_fixed_random_bytes
	
	parser.add_argument('-t', '--test', action='store_true'
						, default = False
						, help='when both "--help"&"--test" turn on, then run test')
	parser.add_argument('-k0d', '--direct_k0', action='store_true'
						, default = False
						, help='"--initial_hashed_key" is py bytes repr, need not be encoded by utf8')
	parser.add_argument('-k0', '--initial_hashed_key', type=str
						, default=None
						, help=fr'initial value for internal_hashed_key; default=[0..255]; required by version2')
	parser.add_argument('-n', '--num_hash_calls_over_key', type=int
						, default=nnn
						, help=fr'internal_hashed_key:=(hash^n)(f(user_key)); default={nnn!r}; required by version2')
	parser.add_argument('-r', '--fixed_random_bytes', type=str
						, default=rrr
						, help=fr'''fixed random_bytes for debug; py.bytes.repr without spaces, eg "b'\0\0'"==>>"b\'\\0\\0\'"; default={rrr!r}''')
	parser.add_argument('-sr', '--show_random_bytes', action='store_true'
						, default = False
						, help='show random_bytes for debug')
	parser.add_argument('-m', '--method'
						#, choices="e1 e2 d encrypt_version1 encrypt_version2 decrypt".split()
						#, default= "encrypt_version1"
						#, help='what to do; given shorthands'
						, choices=[0,1,2]
						, default=1
						, type=int
						, help="0:decrypt; 1:encrypt_version1; 2:encrypt_version2"
						)
	parser.add_argument('-smv', '--show_method_version', action='store_true'
						, default = False
						, help='show the actual version of "--method"; useful when "-m 0"')
	
	"""
	parser.add_argument('-u', '--undo_encrypt', action='store_true'
						, default = False
						, help='decrypt')
	"""

	parser.add_argument('-d', '--direct_input', action='store_true'
						, default = False
						, help='"--input" is data not path')
	parser.add_argument('key_hint', type=str
						#, required=True
						, help='f"{word}/{word}/{word}", eg "a/b/c"')
	parser.add_argument('-i', '--input', type=str, default=None
						, help='input file path')
	parser.add_argument('-o', '--output', type=str, default=None
						, help='output file path')
	parser.add_argument('-e', '--encoding', type=str
						, default='utf8'
						, help='input/output file encoding')
	parser.add_argument('-f', '--force', action='store_true'
						, default = False
						, help='open mode for output file')
	def read(fin):
		return fin.read()
	def output(fout, txt):
		#bug: fout.write(mmm)
		if args.show_method_version:
			print(f'method_version={method_version!r}', file=fout)
		if args.show_random_bytes:
			print(f'random_bytes={random_bytes!r}', file=fout)
		print(txt, file=fout)

	if args is None:
		args = sys.argv[1:]
	try:
		args = parser.parse_args(args)
	except:
		s = set(args)
		h = set('-h --help'.split())
		t = set('-t --test'.split())
		if (s&h) and (s&t):
			test()
		raise
	kk = args.initial_hashed_key
	k0d = args.direct_k0
	mm = args.method
	nn = args.num_hash_calls_over_key
	rr = args.fixed_random_bytes
	if kk is None:
		kk = kkk
	else:
		print(f'k0~{kk!r}', file=sys.stderr)
		if k0d:
			kk = ast.literal_eval(kk)
			if type(kk) is not bytes: raise TypeError(kk)
		else:
			kk = kk.encode("utf8")
		print(f'k0={kk!r}', file=sys.stderr)

	if nn != nnn:
		print(f'n={nn!r}', file=sys.stderr)
	if rr is not None:
		rr = ast.literal_eval(rr)
		print(f'r={rr!r}', file=sys.stderr)
		if type(rr) is not bytes: raise TypeError(rr)

	clss = [呜呼哀哉尚飨, 呜呜呼哀哉尚飨]
	cls = clss[mm-1]
	sf = cls(_k0=kk, _n=nn, _may_fixed_random_bytes=rr)

	encoding = args.encoding
	omode = 'wt' if args.force else 'xt'

	may_ifname = args.input
	if args.direct_input and may_ifname is not None:
		txt = may_ifname
	elif may_ifname is None:
		txt = read(sys.stdin)
	else:
		with open(may_ifname, 'rt', encoding=encoding) as fin:
			txt = read(fin)

	method_version, random_bytes, mmm = sf.呜呼哀哉尚飨加解密_ex(
			要解密=(mm==0)
			, 密码提示=args.key_hint
			, 文=txt
			)
	
	
	may_ofname = args.output
	if may_ofname is None:
		output(sys.stdout, mmm)
	else:
		with open(may_ofname, omode, encoding=encoding) as fout:
			output(fout, mmm)


if __name__ == "__main__":
	main()

