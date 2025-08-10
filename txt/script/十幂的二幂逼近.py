#__all__:goto
r'''[[[
e script/十幂的二幂逼近.py

script.十幂的二幂逼近
py -m nn_ns.app.debug_cmd   script.十幂的二幂逼近 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.十幂的二幂逼近:__doc__ -ht # -ff -df

[[
>>> 1.024**30
2.0370359763344874
>>> 1.024**29
1.9892929456391477
>>> f=lambda n:(10**n).bit_length()/n
>>> f(3)
3.3333333333333335
>>> f(1)
4.0
>>> min((f(n),n) for n in range(1,1000))
(3.3219284603421464, 643)
>>> min((f(n),n) for n in range(1,643))
(3.3219315895372232, 497)
>>> min((f(n),n) for n in range(1,497))
(3.321937321937322, 351)
>>> min((f(n),n) for n in range(1,351))
(3.321951219512195, 205)
>>> min((f(n),n) for n in range(1,205))
(3.3220338983050848, 59)
>>> min((f(n),n) for n in range(1,59))
(3.3225806451612905, 31)
>>> min((f(n),n) for n in range(1,31))
(3.3333333333333335, 3)
>>> min((f(n),n) for n in range(1,3))
(3.5, 2)
>>> min((f(n),n) for n in range(1,2))
(4.0, 1)

>>> from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import iter_continued_fraction_of_log__truncated_
>>> from seed.math.continued_fraction.continued_fraction_fold import iter_approximate_fraction_NDs5continued_fraction_
>>> [*iter_continued_fraction_of_log__truncated_(1000000, 2, 10)]
[3, 3, 9, 2, 2, 4]
>>> [*iter_approximate_fraction_NDs5continued_fraction_([3, 3, 9, 2, 2, 4])]
[(3, 1), (10, 3), (93, 28), (196, 59), (485, 146), (2136, 643)]


[1, 2, 3, 31, 59, 205, 351, 497, 643, ...]
vs:[3, 59, 643, ...]
    <<==: [1, 3, 28, 59, 146, 643, ...]
[31,205,...] 是怎么多出来的？

>>> (10**3).bit_length()
10

>>> (10**31).bit_length()
103
>>> (10**30).bit_length()
100
>>> 100/30 > 103/31
True
>>> 100*31 > 103*30
True
>>> 10/3 > 103/31
True

>>> (10**59).bit_length()
196
>>> (2**196)/10**59
1.004336277661869
>>> (10**58).bit_length()
193
>>> (2**193)/10**58
1.2554203470773362
>>> 193/58 > 196/59
True
>>> 193*59 > 196*58
True
>>> 193/58 > 103/31 > 196/59
True

>>> (10**205).bit_length()
681
>>> (10**204).bit_length()
678
>>> 678*205 > 681*204
True
>>> 678/204 > 196/59 > 681/205
True

10**90:see below:
>>> (10**90).bit_length()
299
>>> (10**89).bit_length()
296
>>> 296/89 > 299/90 > 196/59
True
>>> 296/89 > 103/31 > 299/90 > 196/59
True


prev_k = 1
for n in range(1, 100):
    k = (10**n).bit_length()
    delta_k = k -prev_k
    assert delta_k in (3,4)
    if delta_k == 3:
        print((n, k))
    prev_k = k

>>> prev_k = 1
>>> for n in range(1, 100):
...     k = (10**n).bit_length()
...     delta_k = k -prev_k
...     assert delta_k in (3,4)
...     if delta_k == 3:
...         print((n, k))
...     prev_k = k
(1, 4)
(2, 7)
(3, 10)
(5, 17)
(6, 20)
(8, 27)
(9, 30)
(11, 37)
(12, 40)
(14, 47)
(15, 50)
(17, 57)
(18, 60)
(20, 67)
(21, 70)
(23, 77)
(24, 80)
(26, 87)
(27, 90)
(29, 97)
(30, 100)
(31, 103)
(33, 110)
(34, 113)
(36, 120)
(37, 123)
(39, 130)
(40, 133)
(42, 140)
(43, 143)
(45, 150)
(46, 153)
(48, 160)
(49, 163)
(51, 170)
(52, 173)
(54, 180)
(55, 183)
(57, 190)
(58, 193)
(59, 196)
(61, 203)
(62, 206)
(64, 213)
(65, 216)
(67, 223)
(68, 226)
(70, 233)
(71, 236)
(73, 243)
(74, 246)
(76, 253)
(77, 256)
(79, 263)
(80, 266)
(82, 273)
(83, 276)
(85, 283)
(86, 286)
(88, 293)
(89, 296)
(90, 299)
(92, 306)
(93, 309)
(95, 316)
(96, 319)
(98, 326)
(99, 329)


prev_k = 1
for n in range(1, 100):
    k = (10**n).bit_length()
    delta_k = k -prev_k
    assert delta_k in (3,4)
    if delta_k == 4:
        print((n, k))
    prev_k = k

>>> prev_k = 1
>>> for n in range(1, 100):
...     k = (10**n).bit_length()
...     delta_k = k -prev_k
...     assert delta_k in (3,4)
...     if delta_k == 4:
...         print((n, k))
...     prev_k = k
(4, 14)
(7, 24)
(10, 34)
(13, 44)
(16, 54)
(19, 64)
(22, 74)
(25, 84)
(28, 94)
(32, 107)
(35, 117)
(38, 127)
(41, 137)
(44, 147)
(47, 157)
(50, 167)
(53, 177)
(56, 187)
(60, 200)
(63, 210)
(66, 220)
(69, 230)
(72, 240)
(75, 250)
(78, 260)
(81, 270)
(84, 280)
(87, 290)
(91, 303)
(94, 313)
(97, 323)

==>>:
间隔是{3,4}:
    间隔一般是3
    间隔4=>:28~32:31, 56~60:59, 87~91:90, ...


]]

py_adhoc_call   script.十幂的二幂逼近   @f
from script.十幂的二幂逼近 import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
#.repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
#.lazy_import4funcs_('seed.tiny', 'mk_tuple,print_err,ifNone:ifNone_', __name__)
#.if 0:from seed.tiny import mk_tuple,print_err,ifNone as ifNone_ #xxx:null_tuple #xxx:echo,fst,snd
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


__all__
#[f,g] = lazy_import4funcs_('script.十幂的二幂逼近', 'f,g', __name__)
from script.十幂的二幂逼近 import *
