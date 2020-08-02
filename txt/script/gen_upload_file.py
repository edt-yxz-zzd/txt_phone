
r"""

	ofile=\0upf-0\n{sha256}\n{file_size}\n{mtime}\n{fname{<128B}}\n{num_parts}\n{part_idx}\n{part_sz}\n\0{tgz/7z}{fmt}{fmt_len{2B,big}}
		7z is better, neednot split+cat
	opath=idir/{sha256[:16B]}_{file_idx}_{num_parts}_{part_idx}.upf
	global_list :: file_idx -> (sha256,file_size)
#"""

r"""
pip install libarchive
	The libarchive library does not support multi-volume archives, nor the old GNU long filename format. 
#"""

import pathlib
import datetime
import subprocess
import tempfile
#with tempfile.TemporaryDirectory() as tmpdirname:
		dir4zip_parts = pathlib.Path(dir4zip_parts)
		dir4zip_parts.mkdir(parents=True, exist_ok=True)
def ask_choice(s, **kw):
	v2k = {v:k for k,v in kw.items()}
	assert len(v2k) == len(kw)
	ans = input(s)
	ss = str(sorted(v2k))
	while ans not in v2k:
		ans = input(ss)
	return v2k[ans]

def write_file__rb(*, fout, ifpath, block_size):
	with open(ifpath, 'rb') as fin:
		write_file(
				fout=fout
				,fin=fin
				,block_size=block_size
				)
def write_file(*, fout, fin, block_size):
	while 1:
		bs = fin.read(block_size)
		if not bs: break
		fout.write(bs)

def is_empty_dir(path, glob_pattern):
	path = pathlib.Path(path)
	if not path.is_dir():
		return False

	if glob_pattern is None:
		it = path.iterdir()
	else:
		it = path.glob(glob_pattern)
	for _ in it:
		return False
	return True
def calc_sha256_of(ifpath)
	args = ['sha256sum']
	with open(ifpath, 'rb') as fin:
		r = subprocess.run(args, check=True, capture_output=True, stdin=fin)
	sha256_bs = r.stdout
	assert type(sha256_bs) is bytes
	assert len(sha256_bs)*4 == 256
	sha256_str = sha256_bs.decode('ascii').upper()
	return sha256_str

class NotEmptyDirectoryError(OSError):pass
class UploadFile:
	r"""
	requires:
		7z
		sha256sum
	#"""
	def get_version_str(self):
		return 0
	def get_upf_fmt_str(self):
		#upf-{version}
		#hash=sha256
		return b"\0upf-0\n{sha256}\n{file_size}\n{mtime}\n{fname{<128B}}\n{num_parts}\n{part_idx}\n{part_sz}\n\0{7z}{fmt}{fmt_len{2B,big}}"
	def get_upf_fmt_len(self):
		return 2
	def get_upf_fmt_len_byteorder(self):
		return 'big'
	def get_timestamp_fmt(self):
		return '%Z~%Y_%m_%d_%H:%M:%S~%z'
	def get_upf_part_fname_hash_prefix_len(self):
		return 16

	def mk_upf_part(self, *, fname_bs, sha256_bs, file_size, mtime_bs, num_parts, part_idx, part_fpath, fout):
		if not (type(sha256_bs) is bytes and len(sha256_bs)*4 == 256): raise TypeError
		mtime_bs = memoryview(mtime_bs)
		fname_bs = memoryview(fname_bs)
		if not len(fname_bs) < 128: raise ValueError(f"fname too long: 128 <= {len(fname_bs)} == len({fname_bs!r})")
		fmt = self.get_upf_fmt_str()
		assert len(fmt) < 1<<(2*8)
		fmt_len_bs = len(fmt).to_bytes(2, 'big')
		head_fmt = fmt[:fmt.index(b'{7z}')]
		head_fmt = head_fmt.replace(b"{fname{<128B}}", b"{fname}")
		assert b'<' not in head_fmt
		part_sz = part_fpath.stat().st_size
		head = head_fmt.format(
				sha256=sha256_bs
				,file_size=file_size
				,mtime=mtime_bs
				,fname=fname_bs
				,num_parts=num_parts
				,part_idx=part_idx
				,part_sz=part_sz
				)

		fout.write(head)
		write_file__rb(fout=fout, ifpath=part_fpath)
		fout.write(fmt)
		fout.write(fmt_len_bs)
		return

	def mtime2bytes(self, mtime):
		timestamp_fmt = self.get_timestamp_fmt()
		d_t = datetime.datetime.fromtimestamp(mtime)
		timestamp_str = d_t.strftime(timestamp_fmt)
		_d_t = datetime.datetime.strptime(timestamp_str)
		assert d_t == _d_t
		mtime_bs = timestamp_str.encode('ascii')
		return mtime_bs

	def gen_upf_parts(self, *, file_idx, ifpath, volume, oprefix, dir4zip_parts, dir4upf_parts):
		assert file_idx >= 0
		assert volume > 0
		if not dir4upf_parts.is_dir(): raise NotADirectoryError

		if not ifpath.is_file(): raise TypeError
		opart_fpaths = self.gen_zip_parts(
				volume=volume
				,ipaths=[ifpath]
				,oprefix=oprefix
				,dir4zip_parts=dir4zip_parts
				)

		sha256_str = calc_sha256_of(ifpath)
		nn = self.get_upf_part_fname_hash_prefix_len()
		num_parts = len(opart_fpaths)
		upf_part_fname_prefix = f"{sha256_str[:nn]}_{file_idx}_{num_parts}"

		sha256_bs = sha256_str.encode('ascii')
		fname_bs = ifpath.name.encode('ascii')
		st = ifpath.stat()
		file_size = st..st_size
		mtime_bs = self.mtime2bytes(st.st_mtime)

		for part_idx, part_fpath in enumerate(opart_fpaths):
			upf_part_fname = f"{upf_part_fname_prefix}_{part_idx}.upf"
			upf_part_fpath = dir4upf_parts / upf_part_fname
			while 1:
				try:
					fout = open(upf_part_fpath, 'xb')
					break
				except FileExistsError:
					if upf_part_fpath.is_dir():
						ans = ask_choice(f"{upf_part_fpath!r} is dir: retry? (y/n):", yes='y', no='n')
						if ans == 'yes':
							continue
						elif ans == 'no':
							raise
						else:
							raise logic-error
					else:
						ans = ask_choice(f"{upf_part_fpath!r} exists: overwrite? retry? abort? (o/r/a):", overwrite='o', retry='r', abort='a')
						if ans == 'overwrite':
							fout = open(upf_part_fpath, 'wb')
							break
						elif ans == 'retry':
							continue
						elif ans == 'abort':
							raise
						else:
							raise logic-error

			with fout as fout:
				self.mk_upf_part(
					fname_bs=fname_bs
					,sha256_bs=sha256_bs
					,file_size=file_size
					,mtime_bs=mtime_bs
					,num_parts=num_parts
					,part_idx=part_idx
					,part_fpath=part_fpath
					,fout=fout
					)

	def gen_zip_parts(self, *, volume, ipaths, oprefix, dir4zip_parts):
		# -> [opart_fpath]
		assert len(ipaths)
		assert type(oprefix) is str
		assert type(volume) is int
		assert volume > 0
		#if not dir4zip_parts.exists(): raise NotADirectoryError
		#if not dir4zip_parts.is_dir(): raise NotADirectoryError
		#dir4zip_parts = pathlib.Path(dir4zip_parts)
		#dir4zip_parts.mkdir(parents=True, exist_ok=True)
		if '*' in oprefix: raise ValueError
		if '?' in oprefix: raise ValueError
		if not is_empty_dir(dir4zip_parts, f"{oprefix}.*"): raise NotEmptyDirectoryError
		args = ['7z', 'a', f"{oprefix!s}.", f'-v{volume}b', '-t7z', '-o{dir4zip_parts!s}', *ipaths]
		subprocess.run(args, check=True)
			# even output only one volume, suffix is ".001"
			# ".001" .. ".999" .. ".1000" ....
			# int("009")==9
			# volume==1 is ok!!!
			# [oprefix=="xxx."] ==>> [opart_fpaths[0]=="xxx.001"]
			# [oprefix=="xxx.."] ==>> [opart_fpaths[0]=="xxx..001"]

		d = {}
		for opath in dir4zip_parts.iterdir():
			suffix = opath.suffix
			name = opath.name
			assert oprefix+suffix == name
			assert suffix[:1] == '.'
			i = suffix[1:]
			i = int(i)
			assert i
			assert i not in d
			d[i] = opath

		opart_fpaths = [d[i+1] for i in range(len(d))]
		return opart_fpaths

	#def gen_parts_of_upload_file(self, file_idx, ifpath, volume, odir, tmp_dir):




