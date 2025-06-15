#__all__:goto
r'''[[[
e script/构造冫数列牜类似素数增长.py

script.构造冫数列牜类似素数增长
py -m nn_ns.app.debug_cmd   script.构造冫数列牜类似素数增长 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.构造冫数列牜类似素数增长:__doc__ -ht # -ff -df

[[
@20250614
类似素数n[j]~j*log2(j)增长数列
  计算简单:
    [n[j] == f(n[j//2],j%2)]
    [[i < j] -> [n[i] < n[j]]]
    ==>>:
    [[(a,b) < (c,d)] -> [(a,b) < f(c,d)]]
    or: [c-a>???]
  [n[2*j]
  ~ 2*j*log2(2*j)
  ~ 2*j + 2*j*log2(j)
  ~ 2*j + 2*n[j]
  ~ 2*j*log2(n[j])/log2(n[j]) + 2*n[j]
  ~ 2*j*log2(j)/log2(n[j]) + 2*n[j]
  ~ 2*n[j]/log2(n[j]) + 2*n[j]
  ~ (1/log2(n[j]) + 1)*2*n[j]
  ]
  [[a:<-[2..]][b:<-[0,1]]]:
    [f?(a,b) =[def]= 2*a+2*a//ceil_log2(a)+[b==1]*(1+a%ceil_log2(a))]
      除非保证:[a[j+1]-a[j] > ceil_log2(a)]

]]

py_adhoc_call  script.构造冫数列牜类似素数增长   @list.100:枚举冫数列牜类似素数增长牜乸折半构造法牜疵蛊扌
py_adhoc_call  script.构造冫数列牜类似素数增长   @list.100:枚举冫数列牜类似素数增长牜直接实数逼近牜向下取整扌

[[
TODO:
???bug:
... ...
20:292
21:295
22:292
23:295
... ...
33:620
34:620
... ...
40:648
41:653
42:655
43:663
44:648
45:653
46:655
47:663
... ...
51:686
52:684
... ...
66:1364
67:1365
68:1364
69:1365
... ...
75:1412
76:1412
... ...
80:1425
81:1434
82:1436
83:1440
84:1441
85:1447
86:1458
87:1462
88:1425
89:1434
90:1436
91:1440
92:1441
93:1447
94:1458
95:1462
96:1460
97:1465
... ...
<<==:
py_adhoc_call { -lineno }  script.构造冫数列牜类似素数增长   ,100:枚举冫数列牜类似素数增长牜乸折半构造法牜疵蛊扌
0:2
1:9
2:22
3:24
4:52
5:55
6:57
7:62
8:121
9:126
10:128
11:130
12:133
13:137
14:144
15:147
16:276
17:279
18:288
19:289
20:292
21:295
22:292
23:295
24:299
25:305
26:308
27:310
28:324
29:325
30:330
31:334
32:613
33:620
34:620
35:621
36:640
37:641
38:642
39:644
40:648
41:653
42:655
43:663
44:648
45:653
46:655
47:663
48:664
49:667
50:677
51:686
52:684
53:687
54:688
55:693
56:720
57:721
58:722
59:724
60:733
61:740
62:742
63:744
64:1348
65:1352
66:1364
67:1365
68:1364
69:1365
70:1366
71:1368
72:1408
73:1409
74:1410
75:1412
76:1412
77:1415
78:1416
79:1421
80:1425
81:1434
82:1436
83:1440
84:1441
85:1447
86:1458
87:1462
88:1425
89:1434
90:1436
91:1440
92:1441
93:1447
94:1458
95:1462
96:1460
97:1465
98:1467
99:1475
]]

[[
py_adhoc_call { -lineno }  script.构造冫数列牜类似素数增长   ,100:枚举冫数列牜类似素数增长牜直接实数逼近牜向下取整扌
0:2
1:3
2:5
3:7
4:9
5:12
6:14
7:17
8:20
9:23
10:27
11:30
12:33
13:37
14:40
15:44
16:48
17:52
18:56
19:59
20:63
21:67
22:72
23:76
24:80
25:84
26:88
27:92
28:97
29:101
30:106
31:110
32:114
33:119
34:123
35:128
36:133
37:137
38:142
39:146
40:151
41:156
42:160
43:165
44:170
45:175
46:180
47:184
48:189
49:194
50:199
51:204
52:209
53:214
54:219
55:224
56:229
57:234
58:239
59:244
60:249
61:254
62:259
63:265
64:270
65:275
66:280
67:285
68:290
69:296
70:301
71:306
72:311
73:317
74:322
75:327
76:333
77:338
78:343
79:349
80:354
81:359
82:365
83:370
84:376
85:381
86:387
87:392
88:398
89:403
90:408
91:414
92:420
93:425
94:431
95:436
96:442
97:447
98:453
99:458
]]
[[
py_adhoc_call { -lineno }  script.构造冫数列牜类似素数增长   ,100:枚举冫数列牜类似素数增长牜直接实数逼近牜向下取整牜加模间隔扌
0:2
1:4
2:5
3:8
4:10
5:13
6:14
7:18
8:22
9:24
10:28
11:32
12:33
13:38
14:42
15:47
16:48
17:53
18:56
19:62
20:63
21:68
22:74
23:79
24:80
25:85
26:90
27:94
28:97
29:105
30:108
31:113
32:116
33:120
34:127
35:128
36:133
37:139
38:144
39:150
40:151
41:157
42:162
43:168
44:174
45:175
46:182
47:186
48:192
49:198
50:199
51:205
52:211
53:217
54:223
55:224
56:230
57:236
58:242
59:248
60:249
61:255
62:261
63:268
64:274
65:275
66:281
67:287
68:292
69:300
70:301
71:307
72:311
73:320
74:326
75:330
76:334
77:340
78:343
79:353
80:354
81:362
82:367
83:375
84:380
85:382
86:388
87:395
88:401
89:407
90:408
91:415
92:422
93:428
94:435
95:441
96:443
97:448
98:456
99:461
]]


from script.构造冫数列牜类似素数增长 import *
]]]'''#'''
__all__ = r'''
魖构造法
    魖折半构造法
        乸折半构造法牜疵蛊
            枚举冫数列牜类似素数增长牜乸折半构造法牜疵蛊扌

    魖直接构造法
        乸直接构造法牜直接实数逼近牜向下取整
            枚举冫数列牜类似素数增长牜直接实数逼近牜向下取整扌
        乸直接构造法牜直接实数逼近牜向下取整牜加模间隔
            枚举冫数列牜类似素数增长牜直接实数逼近牜向下取整牜加模间隔扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func import lazy_import4func_
lazy_import4func_('seed.math.floor_ceil', 'ceil_log2', __name__)
if 0:from seed.math.floor_ceil import ceil_log2
lazy_import4func_('seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_', 'cf_ln_', __name__)
if 0:from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import cf_ln_

from math import floor
from itertools import count
from seed.tiny_.check import check_type_is, check_int_ge
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

class 魖构造法(ABC):
    __slots__ = ()
    @abstractmethod
    def __call__(sf, j, /):
        'j/uint -> n[j]'
    def __iter__(sf, /):
        '-> Iter n[j] for j in [0..]'
        return map(sf, count(0))
class 魖直接构造法(魖构造法):
    __slots__ = ()
    @abstractmethod
    def _mk_(sf, j, /):
        'j/uint -> n[j]'
    @override
    def __call__(sf, j, /):
        'j/uint -> n[j]'
        check_int_ge(0, j)
        n = sf._mk_(j)
        return n
class 魖折半构造法(魖构造法):
    __slots__ = ()
    @abstractmethod
    def _half_up_(sf, j, n4half, b, /):
        'j/pint -> n[j//2] -> b/bool{==j%2} -> n[j]'
    @property
    @abstractmethod
    def _n0_(sf, /):
        '-> n[0]'
    @override
    def __call__(sf, j, /):
        'j/uint -> n[j]'
        check_int_ge(0, j)
        ######################
        #loop:
        ######################
        stk = []
            # :: [j]
        while j:
            stk.append(j)
            j >>= 1
        assert j==0
        n = sf._n0_
        n, j # (n0, 0)
        while stk:
            j = stk.pop()
            b = bool(j&1)
            777;    n4half = n
            n = sf._half_up_(j, n4half, b)
        n, j
        return n
        ######################
        #recur:
        ######################
        if j==0:
            n = sf._n0_
        else:
            j4half = j>>1
            b = bool(j&1)
            n4half = sf(j4half)
            n = sf._half_up_(j, n4half, b)
        return n

class 乸折半构造法牜疵蛊(魖折半构造法):
    ___no_slots_ok___ = True
    @override
    def _half_up_(sf, j, n4half, b, /):
        'j/pint -> n[j//2] -> b/bool{==j%2} -> n[j]'
        # [f?(a,b) =[def]= 2*a+2*a//ceil_log2(a)+[b==1]*(1+a%ceil_log2(a))]
        a = n4half
        d = ceil_log2(a)
        za = a<<1
        n = za + za//d + (1+a%d if b else 0)
        return n
    @property
    @override
    def _n0_(sf, /):
        '-> n[0]'
        return 2

class 乸直接构造法牜直接实数逼近牜向下取整(魖直接构造法):
    '加四'
    ___no_slots_ok___ = True
    @override
    def _mk_(sf, j, /):
        'j/uint -> n[j]'
        if j < 2:
            return 2+j
        return 4+floor(j * cf_ln_((j,1)))
class 乸直接构造法牜直接实数逼近牜向下取整牜加模间隔(魖直接构造法):
    '加四再加模间隔'
    ___no_slots_ok___ = True
    _f = 乸直接构造法牜直接实数逼近牜向下取整()
    @override
    def _mk_(sf, j, /):
        'j/uint -> n[j]'
        f = sf._f
        m0 = f(j)
        m1 = f(j+1)
        gap = m1-m0
        assert gap > 0
        n = m0+j%gap
        assert m0 <= n < m1
        return n

def 枚举冫数列牜类似素数增长牜乸折半构造法牜疵蛊扌():
    return iter(乸折半构造法牜疵蛊())
def 枚举冫数列牜类似素数增长牜直接实数逼近牜向下取整扌():
    return iter(乸直接构造法牜直接实数逼近牜向下取整())
def 枚举冫数列牜类似素数增长牜直接实数逼近牜向下取整牜加模间隔扌():
    return iter(乸直接构造法牜直接实数逼近牜向下取整牜加模间隔())



__all__
from script.构造冫数列牜类似素数增长 import *
