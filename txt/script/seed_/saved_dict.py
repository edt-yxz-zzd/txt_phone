"""
saved_dict
	 collections.abc.MutableMapping

saved_dict(
	addr_infile, items_infile, items_picklefile
	,*, kwargs, allow_create_file
	)




addr_infile
	SaveFileDict
	{key:(addr,sz)}
items_infile
	aSaveFile__UpdatableDict
		#only read header
	not SaveFileSeq__TuplePerBlock
		#avoid read whole file
	{key:value}
items_picklefile
	append((key, value))
	read(addr,sz)->(key, value)





pickle.dump(obj, file)
pickle.dumps(obj)->bytes
pickle.load(file)->obj
pickle.loads(bytes_object)->obj



SaveFileABC
	open_verify_or_create_setup_savefile_header(self
        ,path_or_iofile, *
        ,encoding, kwargs
        ,allow_create_file:bool
        ,allow_write_file:bool
        ,allow_write_header:bool
        )
	#SaveFile__TuplePerBlock
	write_tuple(self, ofile, tuple_)
	
	#SaveFile__UpdatableDict
	write_item(self, ofile, case, key, value)
	caseNEW
	caseOVERWRITE
	caseNEWorOVERWRITE
	caseDELETE

"""

__all__ = '''
	saved_dict
	'''.split()

from common_short_hand import *
from seed.io.savefile.SaveFile import (
	SaveFileDict
	,aSaveFile__UpdatableDict
	)
#addr_infile # .mk :: file->kwargs->cache

from  collections.abc import MutableMapping
import pickle, os

SEEK_END = os.SEEK_END
_open_ = aSaveFile__UpdatableDict.open_verify_or_create_setup_savefile_header
_write_ = aSaveFile__UpdatableDict.write_item
_WRITE = aSaveFile__UpdatableDict.caseNEWorOVERWRITE
_DELETE = aSaveFile__UpdatableDict.caseDELETE
_nothing = object()
def _set(f, k, v):
	f.seek(0, SEEK_END)
	_write_(f, _WRITE, k, v)
def _del(f, k):
	f.seek(0, SEEK_END)
	_write_(f, _DELETE, k, 0)
def _open(f, *, kwargs, allow_create_file, _open_=_open_):
	return _open_(f
		,encoding='u8'
		,kwargs=kwargs
		,allow_create_file=allow_create_file
		,allow_write_file=tt
		,allow_write_header=tt
		)
class saved_dict(MutableMapping):
	def __init__(sf
			, addr_infile
				:'SaveFileDict<key,(addr,sz)>'
			, items_infile
				:'txt file of SaveFile__UpdatableDict'
			, items_picklefile
				:'bin file storing (key,value)'
			,* , kwargs, allow_create_file
				# for items_infile
			):
			
			if not isinstance(addr_infile, SaveFileDict):
				addr_infile = _open(addr_infile
				, kwargs=kwargs, allow_create_file=allow_create_file
				, _open_=SaveFileDict)
				
			items_infile = _open(items_infile
				, kwargs=kwargs, allow_create_file=allow_create_file)
			
			omode = ('a+b' if allow_create_file else
							'r+b')
			items_picklefile = open(items_picklefile
				,omode
				)
			#key, txt, pickle, cache
			sf._k = addr_infile
			sf._t = items_infile
			sf._p = items_picklefile
			sf._c = {}
			
	def close(sf):
				sf._t.close()
				sf._p.close()
				#sf._k.close()
				sf._k = ff
				sf._c = ff
	def __del__(self):
				self.close()
	#__getitem__, __setitem__, __delitem__, __iter__, __len__
	def __getitem__(sf, k):
				c = sf._c
				v = c.get(k, _nothing)
				if v is _nothing:
					#!k,!t,c,!p
					addr,sz = sf._k[k]
					if not sz: raise logic-error
					p = sf._p
					p.seek(addr)
					bs = p.read(sz)
					if len(bs) != sz: raise eee
						
					v = pickle.loads(bs)
					c[k] = v
				return v
	def __setitem__(sf, k, v):
				v_ = sf.get(k, _nothing)
				if v_ is _nothing or v_ not in [v]:
					#k,t,c,p
					bs = pickle.dumps(v)
					p = sf._p
					p.seek(0, SEEK_END)
					addr = p.tell()
					p.write(bs)
					sz = len(bs)
					assert sz == p.tell()-addr
					if not sz: raise logic-error
					
					sf._k[k] = (addr, sz)
					_set(sf._t, k,v)
					sf._c[k] = v
				else:
					pass
	def __delitem__(sf, k):
				#k,t,c,!p
				del sf._k[k]
				_del(sf._t, k)
				c = sf._c
				if k in c:
					del c[k]
	def __iter__(sf):
				return iter(sf._k)
	def __len__(sf):
				return len(sf._k)
	__getitem__, __setitem__, __delitem__, __iter__, __len__








