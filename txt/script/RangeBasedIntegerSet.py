
r"""
./seed/data_funcs/rngs.py
BlockSet???
IRangeBasedIntegerSet
RightmostBusyRangeBasedIntegerSet


filter for
    cjk
    gb2312
    big5
    gb13000
    gbk
#"""


from .abc import ABC, abstractmethod#, override, not_implemented, ABCMeta

class IRangeBasedIntegerSet(ABC):
    #immutable
    |&-^
    __or__
    __and__
    __xor__
    __sub__
    __len__
    __contain__
    __iter__
    __reversed__
    __repr__
    __eq__

    from_ints
    from_std_int_rngs
    to_ints
    to_std_int_rngs

    num_ints
    num_int_rngs
    contain_int
    contain_int_rng
    iter_ints
    iter_int_rngs
    reversed_ints
    reversed_int_rngs
class FrozenRangeBasedIntegerSet(IRangeBasedIntegerSet):
    __hash__
class RightmostBusyRangeBasedIntegerSet(IRangeBasedIntegerSet):
    rightmost_add
    rightmost_pop
    pop
    try_add_O619
    try_add_O6logN9
    add_O6N9

