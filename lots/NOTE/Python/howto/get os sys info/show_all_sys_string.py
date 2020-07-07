
r'''
argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
... -- more see below

'api_version' = 1013
'argv' = [
    'show_all_sys_string.py'
    ]
'base_exec_prefix' = 'C:\\Python36'
'base_prefix' = 'C:\\Python36'
'builtin_module_names' = <class 'tuple'>
'byteorder' = 'little'
'dllhandle' = 1872625664
'dont_write_bytecode' = False
'exec_prefix' = 'C:\\Python36'
'executable' = 'C:\\Python36\\python.exe'
'flags' = <class 'sys.flags'>
'float_info' = sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
'float_repr_style' = 'short'
'getdefaultencoding' = <class 'builtin_function_or_method'>
'getfilesystemencodeerrors' = <class 'builtin_function_or_method'>
'getfilesystemencoding' = <class 'builtin_function_or_method'>
'getwindowsversion' = <class 'builtin_function_or_method'>
'hash_info' = sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, seed_bits=128, cutoff=0)
'hexversion' = 50725616
'implementation' = <class 'types.SimpleNamespace'>
'int_info' = sys.int_info(bits_per_digit=30, sizeof_digit=4)
'intern' = <class 'builtin_function_or_method'>
'maxsize' = 9223372036854775807
'maxunicode' = 1114111
'path' = [
    'E:\\my_data\\my_record_txt\\NOTE\\Python\\howto\\get os sys info'
    'C:\\Python36\\python36.zip'
    'C:\\Python36\\DLLs'
    'C:\\Python36\\lib'
    'C:\\Python36'
    'C:\\Python36\\lib\\site-packages'
    'C:\\Python36\\lib\\site-packages\\xart-0.2.0-py3.6.egg'
    'E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src'
    'C:\\Python36\\lib\\site-packages\\win32'
    'C:\\Python36\\lib\\site-packages\\win32\\lib'
    'C:\\Python36\\lib\\site-packages\\Pythonwin'
    ]
'platform' = 'win32'
'prefix' = 'C:\\Python36'
'thread_info' = sys.thread_info(name='nt', lock=None, version=None)
'version' = '3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)]'
'version_info' = sys.version_info(major=3, minor=6, micro=2, releaselevel='final', serial=0)
'warnoptions' = [
    ]
'winver' = '3.6'

================================

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''

Static objects:

exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a struct sequence with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a struct sequence with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a struct sequence with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a struct sequence with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!

Functions:

getdlopenflags() -- returns flags to be used for dlopen() calls


'''

import sys
from collections import namedtuple
#print(sys.version_info)
#raise

doc_name = '__doc__'
name = doc_name
doc = getattr(sys, doc_name)
print(f'{name!r} = r"""')
print(doc)
print('"""')
print('\n'*3)

for name in dir(sys):
    obj = getattr(sys, name)
    if name == doc_name:
        pass
    elif name == 'builtin_module_names':
        print(f'{name!r} = {type(obj)!r}')
    elif isinstance(obj, (str, int)) or name.endswith('_info'):
        print(f'{name!r} = {obj!r}')
    elif isinstance(obj, (list, tuple)) and all(isinstance(a, str) for a in obj):
        opener, closer = '[]' if isinstance(obj, list) else '()'
        print(f'{name!r} = {opener}')
        for a in obj:
            print(f'    {a!r}')
        print('    {closer}')
    else:
        print(f'{name!r} = {type(obj)!r}')

