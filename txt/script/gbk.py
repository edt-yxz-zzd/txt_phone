
r"""
	双字节 [0x81..0xFE][0x40..0x7E,0x80..0xFE]
		23940==126*190
			> 21886
			兼容 gbk
	
目标：
	gb18030:2bytes /-\ gb18030:4bytes == {}
		see: _g(), may yes
	gbk:2bytes <: gb18030:2bytes
	gbk gb18030 在双字节上的真实编码空间
		gbk -2149 +21791
		gb18030 -0 +23940

		但是 gbk 该有 21886 !!!
			21886-21791==95


#"""

def try_(err, f):
	try:
		f()
	except err:
		return True
	except:
		pass
	return False
def find_not__0x7F(encoding):
	ls = []
	begin = end = None
	m = 0
	c = 0
	y = 0x7f
	for x in range(0x81, 0xff):
		bs = bytes([x,y])
		if try_(UnicodeError, lambda:bs.decode(encoding)):
			m += 1
			if end==x:
				end += 1
			else:
				if begin != end:
					ls.append((begin, end))
				begin = x
				end = x+1
		else:
			c += 1
	else:
		if begin != end:
			ls.append((begin, end))
	assert m+c == 126
	return -m, +c, ls

def find_not(encoding):
	lss = []
	m = 0
	c = 0
	for x in range(0x81, 0xff):
		ls = []
		begin = end = None
		n = 0
		for y in range(0x40, 0xff):
			if y == 0x7f:
				n += 1
				if end==y:
					end += 1
				continue
			bs = bytes([x,y])
			if try_(UnicodeError, lambda:bs.decode(encoding)):
				n += 1
				if end==y:
					end += 1
				else:
					if begin != end:
						ls.append((begin, end))
					begin = y
					end = y+1
			else:
				c += 1
		else:
			if begin != end:
				ls.append((begin, end))
		assert n>=1
		m += n-1
		if ls:
			assert n>=2
			lss.append((x,-n, ls))
		else:
			assert n==1
	assert 0xff - 0x81 == 126
	assert 0xff - 0x40 -1 == 190
	#print(m, c, m+c, 126*190)
	assert m+c == 126*190
	return -m, +c, lss

def _g():
	#c = b"\x81\x30\x81\x30".decode("gb18030")
	#print(fr'{c!r} = b"\x81\x30\x81\x30".decode("gb18030")')
	ss = [
			r'\x81\x30\x81\x30'  # 0x80
			,r'\x81\x30\x82\x30'
			,r'\x81\x30\x82\x36'
			,r'\x81\x30\x8b\x38'
			,r'\x81\x30\x81\x31'
			,r'\x81\x30\x81\x32'
			,r'\x81\x30\x81\x34'
			,r'\x81\x30\x81\x38'
			,r'\x81\x30\x82\x36'
			,r'\x81\x30\x84\x32'
			,r'\x81\x30\x87\x34' # ???
			,r'\x81\x30\x86\x38' # 0xC0 ???
			,r'\x81\x30\x85\x38'
			,r'\x81\x30\x85\x30'
			,r'\x81\x30\x84\x36' # 0xA5 ???
			,r'\x81\x30\x84\x34'
			,r'\x81\x30\x84\x35' # 0xA3
			###since '\xA4'.encode('gbk') == b'\xa1\xe8'
			###ascii&gbk are excluded by gb18030:4bytes
			]
	for s in ss:
		s = fr'b"{s!s}".decode("gb18030")'
		c = eval(s)
		i = ord(c)
		print(fr'"\U{i:0>8X}" = {s!s}')
def _t():
	for encoding in ['gbk', 'gb18030']:
		print(encoding, find_not(encoding))
		print(encoding, '(?, 0x7F)', find_not__0x7F(encoding))
_t()
_g()

r"""
gbk -2149 +21791
gb18030 -0 +23940
$ py gbk.py
gbk (-2149, 21791, [(161, -97, [(64, 161)]), (162, -109, [(64, 161), (171, 177), (227, 229), (239, 241), (253, 255)]), (163, -97, [(64, 161)]), (164, -108, [(64, 161), (244, 255)]), (165, -105, [(64, 161), (247, 255)]), (166, -124, [(64, 161), (185, 193), (217, 224), (236, 238), (243, 244), (246, 255)]), (167, -125, [(64, 161), (194, 209), (242, 255)]), (168, -39, [(150, 161), (188, 189), (191, 192), (193, 197), (234, 255)]), (169, -47, [(88, 89), (91, 92), (93, 96), (137, 150), (151, 164), (240, 255)]), (170, -95, [(161, 255)]), (171, -95, [(161, 255)]), (172, -95, [(161, 255)]), (173, -95, [(161, 255)]), (174, -95, [(161, 255)]), (175, -95, [(161, 255)]), (215, -6, [(250, 255)]), (248, -95, [(161, 255)]), (249, -95, [(161, 255)]), (250, -95, [(161, 255)]), (251, -95, [(161, 255)]), (252, -95, [(161, 255)]), (253, -95, [(161, 255)]), (254, -175, [(80, 255)])])
gbk (?, 0x7F) (-126, 0, [(129, 255)])
gb18030 (0, 23940, [])
gb18030 (?, 0x7F) (-126, 0, [(129, 255)])
\U00000080 = b"\x81\x30\x81\x30".decode("gb18030")
\U0000008A = b"\x81\x30\x82\x30".decode("gb18030")
\U00000090 = b"\x81\x30\x82\x36".decode("gb18030")
\U00000100 = b"\x81\x30\x8b\x38".decode("gb18030")
\U00000081 = b"\x81\x30\x81\x31".decode("gb18030")
\U00000082 = b"\x81\x30\x81\x32".decode("gb18030")
\U00000084 = b"\x81\x30\x81\x34".decode("gb18030")
\U00000088 = b"\x81\x30\x81\x38".decode("gb18030")
\U00000090 = b"\x81\x30\x82\x36".decode("gb18030")
\U000000A0 = b"\x81\x30\x84\x32".decode("gb18030")
\U000000C6 = b"\x81\x30\x87\x34".decode("gb18030")
\U000000C0 = b"\x81\x30\x86\x38".decode("gb18030")
\U000000B5 = b"\x81\x30\x85\x38".decode("gb18030")
\U000000AB = b"\x81\x30\x85\x30".decode("gb18030")
\U000000A5 = b"\x81\x30\x84\x36".decode("gb18030")
\U000000A2 = b"\x81\x30\x84\x34".decode("gb18030")
\U000000A3 = b"\x81\x30\x84\x35".decode("gb18030")
#"""


