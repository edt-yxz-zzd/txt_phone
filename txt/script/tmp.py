#__all__:goto
r'''[[[
e ./script/tmp.py

script.tmp
py -m nn_ns.app.debug_cmd   script.tmp -x
py -m nn_ns.app.doctest_cmd script.tmp:__doc__ -ht
py_adhoc_call   script.tmp   @f
from script.tmp import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__



__all__
from script.tmp import *
