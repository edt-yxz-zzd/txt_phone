#__all__:goto
r'''[[[
e script/extend_uint_19.py

19:围棋棋盘:19*19:19=4*5-1:2**n*(2**n+1)-1=2**(2*n)+2**n-1
    ver1:2**(2*n)+2**n-1
    ver2:n**2+n-1
    ver3:n**2+n-1
    ver3:n**2+3*n+1==[m:=n+1]==m**2+m-1

    ====
    (x(n)+1)*y(n)-1 = x_*y_ +y_ -1
        #x=3,y=5
    (x_*y_ +y_ -1)**2 -1
        = (x_*y_ +y_)*(x_*y_ +y_ -2)
        = (x_ +1)*y_*(x_*y_ +y_ -2)
        [y_=x_+2]:
            ... = (x_ +1)*y_*(x_*y_ +x_)
                = (x_ +1)*y_*x_*(y_ +1)
                = x_*(x_ +1)*y_*(y_ +1)
                = x_*(x_ +1)*(x_ +2)*(x_ +3)
                #3*4*5*6=360
    [y_=x_+2]:
        (x_*y_ +y_ -1)
            = (x_*(x_+2) +(x_+2) -1)
            = (x_*x_ +3*x_ +1)
            = (x_+1)**2 +x_
            = (x_+1)**2 +(x_+1) -1


py_adhoc_call   script.extend_uint_19   ,iter_seq_ex19__ver1_ =16
1
5
19
71
271
1055
4159
16511
65791
262655
1049599
4196351
16781311
67117055
268451839
1073774591

py_adhoc_call   script.extend_uint_19   ,iter_seq_ex19__ver2_ =16
-1
1
5
11
19
29
41
55
71
89
109
131
155
181
209
239

py_adhoc_call   script.extend_uint_19   ,iter_seq_ex19__ver_ =3 =16
1
5
11
19
29
41
55
71
89
109
131
155
181
209
239
271


script.extend_uint_19
py -m nn_ns.app.debug_cmd   script.extend_uint_19 -x
py -m nn_ns.app.doctest_cmd script.extend_uint_19:__doc__ -ff -v
py_adhoc_call   script.extend_uint_19   @f
from script.extend_uint_19 import *

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

r'''[[[
#]]]'''#'''

def iter_seq_ex19__ver_(ver, n, /):
    for i in range(n):
        yield at_seq_ex19__ver_(ver, i)
def at_seq_ex19__ver_(ver, n, /):
    if ver == 1:
        return 2**(2*n)+2**n-1
    if ver == 2:
        return n**2+n-1
    if ver == 3:
        return n**2+3*n+1

def at_seq_ex19__ver2_(n, /):
    return n**2+n-1
def iter_seq_ex19__ver2_(n, /):
    for i in range(n):
        yield at_seq_ex19__ver2_(i)

def at_seq_ex19__ver1_(n, /):
    return 2**(2*n)+2**n-1

def iter_seq_ex19__ver1_(n, /):
    for i in range(n):
        yield at_seq_ex19__ver1_(i)
