



'''
see:
    "NOTE/group/group finite description.txt"
    "NOTE/玄学/50-49.txt"
        the 5 groups of order 50
        #G50

'''

__all__ = '''
    IGroupOrderedFiniteDescription
    verify_group_finite_description
    verify_group_finite_description__std_ordered_repr
    verify_group_finite_description__relationship
    '''.split()

from abc import ABC, abstractmethod
from itertools import chain, product
from seed.tiny import fst, snd

def is_of_type(obj, tp):
    return type(obj) is tp
def is_bool(obj):
    return is_of_type(obj, bool)
def is_sint(obj):
    return is_of_type(obj, int)
def is_tuple(obj):
    return is_of_type(obj, tuple)
def is_pair(obj):
    return is_tuple(obj) and len(obj) == 2

#is_sequence
is_tuple
is_pair
is_sint
is_bool


class IGroupOrderedFiniteDescription(ABC):
    '''

generator
pairwise_sorted_relationship
degenerate_relationship
non_degenerate_exponent_range
degenerate_exponent
mayinv_generator :: (generator, is_inv::Bool)
unordered_repr :: unordered[(generator, exp::SInt)]
    group_elmenent_unordered_repr
ordered_repr :: ordered[(generator, exp::SInt)]
    group_elmenent_ordered_repr

(group (ordered finite_description))
group_ordered_finite_description<g>
    .get_ordered_generators :: [g]
    .compare_generator :: g -> g -> (-1|0|+1)
    .get_pairwise_sorted_relationship :: (g, Bool) -> (g, Bool) -> ordered[(g, SInt)]
    .get_maybe_degenerate_relationship :: g -> (() | (PInt, ordered[(g, SInt)]))
    .get_maybe_degenerate_exponent_of :: g -> (None|PInt)
    ##.get_maybe_non_degenerate_exponent_range_of :: g -> (None|PInt)
    .mul
'''
    __slots__ = ()

    @abstractmethod
    def _is_generator_(self, g):
        # -> Bool
        raise NotImplementedError
    @abstractmethod
    def _always_verify_class_(self):
        # -> Bool
        raise NotImplementedError
    @abstractmethod
    def __get_ordered_generators__(self):
        # -> [g]
        raise NotImplementedError
    @abstractmethod
    def __compare_generator__(self, lhs_generator, rhs_generator):
        # :: g -> g -> (-1|0|+1)
        raise NotImplementedError
    @abstractmethod
    def __get_pairwise_sorted_relationship__(self, mayinv_lhs_generator, mayinv_rhs_generator):
        # :: (g, Bool) -> (g, Bool) -> ordered[(g, SInt)]
        raise NotImplementedError
    @abstractmethod
    def __get_maybe_degenerate_relationship__(self, generator):
        # :: g -> (() | (PInt, ordered[(g, SInt)]))
        raise NotImplementedError




    def _is_ordered_generators_(self, gs):
        return self._is_generators_(gs) and self._are_generators_ordered_(gs)
    def _is_generators_(self, gs):
        return is_tuple(generators) and self._are_generators_(gs)
    def _are_generators_(self, gs):
        return all(map(slef._is_generator_, gs))
    def _are_generators_ordered_(self, gs):
        it = iter(gs)
        for head in it:
            break
        else:
            return True
        cmp = self.compare_generator
        for x in it:
            if -1 != cmp(head, x): return False
            head = x
        return True

    def get_ordered_generators(self):
        # -> [g]
        generators = type(self).__get_ordered_generators__(self)
        assert not self._always_verify_class_() or self._is_ordered_generators_(generators)
        return generators
    def compare_generator(self, lhs, rhs):
        # :: g -> g -> (-1|0|+1)
        r = type(self).__compare_generator__(self, lhs, rhs)
        assert type(r) is int and -1 <= r <= 1
        return r

    def is_ordered_repr_std(self, group_elmenent_repr):
        # is all exp in non_degenerate_exponent_range
        for g, exp in group_elmenent_repr:
            may_exp = self.get_maybe_degenerate_exponent_of(g)
            if may_exp is not None:
                exp_modulus = may_exp
                assert exp_modulus >= 2
                if not (1 <= exp < exp_modulus):
                    return False
        return True
    def is_ordered_repr(self, group_elmenent_repr):
        # is ordered[(g, SInt)]
        return (is_tuple(group_elmenent_repr)
            and all(map(is_pair, group_elmenent_repr))
            and all(map(is_sint, map(snd, group_elmenent_repr)))
            and all(map(self._is_generator_, map(fst, group_elmenent_repr)))
            and self._are_generators_ordered_(map(fst, group_elmenent_repr))
            )
    def is_ordered_repr_gt(self, group_elmenent_repr, g):
        # g < any generator in group_elmenent_repr
        return (self.is_ordered_repr(group_elmenent_repr)
            and (not group_elmenent_repr
                or -1 == self.compare_generator(g, fst(group_elmenent_repr[0]))
                )
            )


    def is_ordered_repr_ge(self, group_elmenent_repr, g):
        # g <= any generator in group_elmenent_repr
        return (self.is_ordered_repr(group_elmenent_repr)
            and (not group_elmenent_repr
                or 1 != self.compare_generator(g, fst(group_elmenent_repr[0]))
                )
            )

    def get_pairwise_sorted_relationship(self, mayinv_lhs, mayinv_rhs):
        # :: (g, Bool) -> (g, Bool) -> ordered[(g, SInt)]
        b = self._always_verify_class_()
        if b:
            assert is_pair(mayinv_lhs)
            assert is_pair(mayinv_rhs)
            lhs, l_is_inv = mayinv_lhs
            rhs, r_is_inv = mayinv_rhs
            assert self._is_generator_(lhs)
            assert self._is_generator_(rhs)
            assert is_bool(l_is_inv)
            assert is_bool(r_is_inv) # rhs^(+1) or rhs^(-1)
            assert 1 == self.compare_generator(lhs, rhs)
            # lhs > rhs

        (group_elmenent_ordered_repr
        ) = type(self).__get_pairwise_sorted_relationship__(
            self, mayinv_lhs, mayinv_rhs)

        if b:
            assert self.is_ordered_repr_ge(group_elmenent_ordered_repr, rhs)
            #assert self.is_ordered_repr_std(group_elmenent_ordered_repr)
            # rhs <= (any generator in result)
        return group_elmenent_ordered_repr

    def get_maybe_degenerate_relationship(self, g):
        # :: g -> (() | (PInt, ordered[(g, SInt)]))
        (maybe_degenerate_relationship
        ) = type(self).__get_maybe_degenerate_relationship__(self, g)
        if self._always_verify_class_():
            assert is_tuple(maybe_degenerate_relationship)
            L = len(maybe_degenerate_relationship)
            assert L in (0,2)
            if L == 2:
                degenerate_relationship = maybe_degenerate_relationship
                degenerate_exponent, eqn_rhs_order_repr = degenerate_relationship
                assert is_sint(degenerate_exponent)
                assert degenerate_exponent >= 2
                assert self.is_ordered_repr_gt(eqn_rhs_order_repr, g)
                #assert self.is_ordered_repr_std(eqn_rhs_order_repr)
                # g < (any generator in eqn_rhs_order_repr)
        return maybe_degenerate_relationship


    def get_maybe_degenerate_exponent_of(self, g):
        # :: g -> (None|PInt)
        maybe_degenerate_relationship = self.get_maybe_degenerate_relationship(g)
        if not maybe_degenerate_relationship:
            return None
        degenerate_relationship = maybe_degenerate_relationship
        degenerate_exponent, _ = degenerate_relationship
        return degenerate_exponent

    '''
    def get_maybe_non_degenerate_exponent_range_of(self, g):
        # :: g -> (None|PInt)
        #
        # None - ZZ
        # k:PInt - [0..k-1]
        return maybe_degenerate_exponent??????
        maybe_degenerate_exponent = self.get_maybe_degenerate_exponent_of(g)

        if maybe_degenerate_exponent is None:
            return None
        degenerate_exponent = maybe_degenerate_exponent
        return range(degenerate_exponent)
    '''

    def order_group_elmenent_unordered_repr(self, iter_group_elmenent_unordered_repr):
        left_stack = [] # unordered_repr
        right_stack = [] # reversed ordered_repr
        def push(stack, g, exp):
            if not exp: return
            if stack:
                g_, exp_ = stack[-1]
                if 0 == self.compare_generator(g, g_):
                    # g == g_
                    stack.pop()
                    exp += exp_
            if not exp: return
            stack.append((g, exp))
        def may_pop(stack):
            # -> (None|mayinv_generator)
            # -> (None|(g, Bool))
            while stack:
                g, exp = stack.pop()
                if not exp: continue
                elif exp < 0:
                    exp += 1
                    is_inv = True
                else:
                    exp -= 1
                    is_inv = False
                break
            else:
                return None
            if exp:
                stack.append((g, exp))
            return (g, is_inv)

        def push_many(stack, pairs):
            for g, exp in pairs:
                push(stack, g, exp)
        def try_to_move_left_to_right():
            # push(right_stack, *left_stack.pop())
            #   but take care of BIG exp
            assert left_stack
            lhs = left_stack[-1][0]
            assert not right_stack or -1 == cmp(lhs, right_stack[-1][0])

            if reduce_last_of_left_stack_if_too_big():
                return False
            push(right_stack, *left_stack.pop())
            return True
        def reduce_last_of_left_stack_if_too_big():
            # -> Bool
            #   True - too big and reduce
            #   False - do nothing
            assert left_stack
            lhs = left_stack[-1][0]
            assert not right_stack or 0 != cmp(lhs, right_stack[-1][0])
            may_exp_repr_pair = self.get_maybe_degenerate_relationship(lhs)
            while True:
                if not may_exp_repr_pair: break
                exp_modulus, eqn_rhs_order_repr = may_exp_repr_pair
                assert exp_modulus >= 2

                lhs, exp = left_stack[-1]
                if 0 <= exp < exp_modulus: break

                q, r = divmod(exp, exp_modulus)
                assert r >= 0
                if not q:
                    assert r == exp
                    break

                left_stack.pop()
                push(left_stack, lhs, r) # push back
                if q < 0:
                    unordered_repr = [(g, -exp) for g, exp in reversed(eqn_rhs_order_repr)]
                    q = -q
                else:
                    unordered_repr = eqn_rhs_order_repr
                del eqn_rhs_order_repr

                for _ in range(q):
                    push_many(left_stack, unordered_repr)
                return True
            return False

        # collect neighbors
        push_many(left_stack, iter_group_elmenent_unordered_repr)
        del iter_group_elmenent_unordered_repr

        cmp = self.compare_generator

        #print('\n'*5); print('='*60)
        while True:
            #print(f'left_stack={left_stack}')
            #print(f'right_stack={right_stack}')
            if not right_stack:
                if not left_stack: break
                try_to_move_left_to_right()
                continue
            assert right_stack

            if not left_stack: break
            assert left_stack

            lhs = left_stack[-1][0]
            rhs = right_stack[-1][0]
            r = cmp(lhs, rhs)
            #print(f'cmp last = {r}')
            if r == -1:
                # lhs < rhs
                try_to_move_left_to_right()
                continue
            elif r == 0:
                # lhs == rhs
                push(left_stack, *right_stack.pop())
                    # since exp may overflow!
                try_to_move_left_to_right()
                continue
            assert r == 1
            # lhs > rhs
            if reduce_last_of_left_stack_if_too_big():
                continue

            may_mayinv_lhs = may_pop(left_stack)
            if may_mayinv_lhs is None:
                raise logic-error
            mayinv_lhs = may_mayinv_lhs

            may_mayinv_rhs = may_pop(right_stack)
            if may_mayinv_rhs is None:
                raise logic-error
            mayinv_rhs = may_mayinv_rhs

            ordered_repr = self.get_pairwise_sorted_relationship(mayinv_lhs, mayinv_rhs)
            push_many(left_stack, ordered_repr)
            continue
        #end while

        #bug: result_ordered_repr = tuple(right_stack)
        result_ordered_repr = tuple(reversed(right_stack))
        assert self.is_ordered_repr(result_ordered_repr)
        assert self.is_ordered_repr_std(result_ordered_repr)
        return result_ordered_repr



    def mul(self, lhs_group_elmenent_ordered_repr, rhs_group_elmenent_ordered_repr):
        lhs = lhs_group_elmenent_ordered_repr
        rhs = rhs_group_elmenent_ordered_repr
        return self.order_group_elmenent_unordered_repr(chain(lhs, rhs))
    def eq_std_ordered_repr(self, lhs, rhs):
        assert self.is_ordered_repr(lhs)
        assert self.is_ordered_repr(rhs)
        assert self.is_ordered_repr_std(lhs)
        assert self.is_ordered_repr_std(rhs)
        def eq(lhs_g, rhs_g):
            return 0 == self.compare_generator(lhs_g, rhs_g)
        return (len(lhs) == len(rhs)
            and all(le == re for (lg, le), (rg, re) in zip(lhs, rhs))
            and all(eq(lg, rg) for (lg, le), (rg, re) in zip(lhs, rhs))
            )

"""
class IFiniteGroupOrderedFiniteDescription(ABC):
    '''

(finite_group (ordered finite_description))
    .get_degenerate_relationship :: g -> (PInt, ordered[(g, SInt)])
    .get_degenerate_exponent_of
'''
    __slots__ = ()
    def get_ordered_generators(self):
"""


class VerifyFail(Exception): pass

def verify_group_finite_description__mul_table(self):
    (idx2ordered_element, mul_table) = self.make_mul_table()
    SZ = len(mul_table)
    for i in range(SZ):
     for j in range(SZ):
      for k in range(SZ):
        # (i*j)*k = i*(j*k)
        if mul_table[mul_table[i][j]][k] != mul_table[i][mul_table[j][k]]:
            raise VerifyFail
            return False
    return True

def verify_group_finite_description(self, *, verify_mul_table:bool=True):
    assert isinstance(self, IGroupOrderedFiniteDescription)

    if __debug__:
        assert verify_group_finite_description__std_ordered_repr(self)
        assert verify_group_finite_description__relationship(self)
        if verify_mul_table:
            assert verify_group_finite_description__mul_table(self)
    return (verify_group_finite_description__std_ordered_repr(self)
        and verify_group_finite_description__relationship(self)
        and (not verify_mul_table or verify_group_finite_description__mul_table(self))
        )

def verify_group_finite_description__std_ordered_repr(self):
    '''
whether all eqn_rhs_order_repr in either relationship are std ordered_repr
'''
    assert isinstance(self, IGroupOrderedFiniteDescription)

    ordered_generators = self.get_ordered_generators()
    cmp = self.compare_generator
    mul = self.mul
    eq = self.eq_std_ordered_repr
    L = len(ordered_generators)
    def mk_singleton(g, exp):
        # -> ordered_repr of len 1
        return ((g, exp),)
    def iter_two_cases(g):
        yield mk_singleton(g, +1)
        yield mk_singleton(g, -1)
    def singleton2pn_g(ordered_repr):
        [(g, pn_1)] = ordered_repr
        assert abs(pn_1) == 1
        is_inv = pn_1 == -1
        return (g, is_inv)


    for i in reversed(range(L)):
     gi = ordered_generators[i]
     for j in reversed(range(i+1, L)):
      gj = ordered_generators[j]
      for a in iter_two_cases(gi):
       for b in iter_two_cases(gj):
        # b*a
        pn_gi = singleton2pn_g(a)
        pn_gj = singleton2pn_g(b)
        r = mul(b, a)
        ordered_repr = self.get_pairwise_sorted_relationship(pn_gj, pn_gi)

        if not self.is_ordered_repr_ge(ordered_repr, gi):
            raise VerifyFail; return False
        if not self.is_ordered_repr_std(ordered_repr):
            raise VerifyFail; return False
        if not eq(ordered_repr, r):
            raise VerifyFail; return False

    for i in reversed(range(L)):
        gi = ordered_generators[i]
        may_exp_repr_pair = self.get_maybe_degenerate_relationship(gi)
        if not may_exp_repr_pair: continue
        exp, ordered_repr = may_exp_repr_pair
        if not exp >= 2:
            raise VerifyFail; return False
        if not self.is_ordered_repr_gt(ordered_repr, gi):
            raise VerifyFail; return False
        if not self.is_ordered_repr_std(ordered_repr):
            raise VerifyFail; return False
    return True

def verify_group_finite_description__relationship(self):
    '''
    # below var x stands for x^1 or x^(-1)
    c*b*a
        # c > b > a
        = (c*b)*a = (b^i*...) * a
        = c*(b*a) = c * (a^i*...)
    b^k*a
        # b >= a
        # k = degenerate_exponent_of(ord, b)
        = (b^k)*a = (c^i*...)*a
        = b*(b*(...(b*a))) = b*(b*(...(a^i*...)))
    c*a^k
        # c >= a
        # k = degenerate_exponent_of(ord, a)
        = (((c*a)...)*a)*a = (((a^i*...)...)*a)*a
        = c*(a^k) = c*(b^i*...)
'''
    assert isinstance(self, IGroupOrderedFiniteDescription)

    ordered_generators = self.get_ordered_generators()
    cmp = self.compare_generator
    mul = self.mul
    eq = self.eq_std_ordered_repr
    def to_inv_unordered_repr(unordered_repr):
        unordered_repr = tuple((g, -exp) for g, exp in reversed(unordered_repr))
        return unordered_repr

    L = len(ordered_generators)
    def mk_singleton(g, exp):
        # -> ordered_repr of len 1
        return ((g, exp),)
    def iter_two_cases(g):
        yield mk_singleton(g, +1)
        yield mk_singleton(g, -1)

    #c*b*a
        # c > b > a
    for i in reversed(range(L)):
     gi = ordered_generators[i]
     for j in reversed(range(i+1, L)):
      gj = ordered_generators[j]
      for k in reversed(range(j+1, L)):
        gk = ordered_generators[k]
        assert i < j < k
        assert -1 == cmp(gi, gj)
        assert -1 == cmp(gj, gk)
        for a in iter_two_cases(gi):
         for b in iter_two_cases(gj):
          for c in iter_two_cases(gk):
            # c*b*a
            # = (c*b)*a = (b^i*...) * a
            # = c*(b*a) = c * (a^i*...)
            r0 = mul(mul(c,b), a)
            r1 = mul(c, mul(b,a))
            if not eq(r0, r1):
                raise VerifyFail; return False

    pos_exp = +1
    neg_exp = -1
    #b^k*a
        # b >= a
    for i in reversed(range(L)):
     gi = ordered_generators[i]
     for j in reversed(range(i, L)): # no +1
        gj = ordered_generators[j]

        may_exp_repr_pair = self.get_maybe_degenerate_relationship(gj)
        if not may_exp_repr_pair: continue
        k, eqn_rhs_order_repr = may_exp_repr_pair

        pos_repr = eqn_rhs_order_repr
        neg_repr = to_inv_unordered_repr(eqn_rhs_order_repr)
        ls = [(pos_exp, pos_repr), (neg_exp, neg_repr)]
        for a in iter_two_cases(gi):
         for x_exp, x_repr in ls:
            b = mk_singleton(gj, x_exp)
            # b^k*a
            # = (b^k)*a = (c^i*...)*a
            # = b*(b*(...(b*a))) = b*(b*(...(a^i*...)))

            r0 = mul(x_repr, a)
            r1 = a
            for _ in range(k):
                r1 = mul(b, r1)
            if not eq(r0, r1):
                raise VerifyFail; return False

    #c*a^k
        # c >= a
    for i in reversed(range(L)):
     gi = ordered_generators[i]
     for j in reversed(range(i, L)): # no +1
        gj = ordered_generators[j]

        may_exp_repr_pair = self.get_maybe_degenerate_relationship(gi)
        if not may_exp_repr_pair: continue
        k, eqn_rhs_order_repr = may_exp_repr_pair

        pos_repr = eqn_rhs_order_repr
        neg_repr = to_inv_unordered_repr(eqn_rhs_order_repr)
        ls = [(pos_exp, pos_repr), (neg_exp, neg_repr)]
        for c in iter_two_cases(gj):
         for x_exp, x_repr in ls:
            a = mk_singleton(gi, x_exp)
            # c*a^k
            # = (((c*a)...)*a)*a = (((a^i*...)...)*a)*a
            # = c*(a^k) = c*(b^i*...)

            r0 = mul(c, x_repr)
            r1 = c
            for _ in range(k):
                r1 = mul(r1, a)
            if not eq(r0, r1):
                raise VerifyFail; return False

    return True


class GroupOrderedFiniteDescriptionABC(IGroupOrderedFiniteDescription):
    __slots__ = ()
    def __init__(self
        , ordered_generators
        ):
        ordered_generators = tuple(ordered_generators)
        L = len(ordered_generators)

        generator2ord = dict(zip(ordered_generators, range(L)))

        self.ordered_generators = ordered_generators
        self.generator2ord = generator2ord
        self.attr__always_verify_class = False
        #verify_group_finite_description(self)


    def _is_generator_(self, g):
        return g in self.generator2ord
    def __compare_generator__(self, lhs, rhs):
        # :: g -> g -> (-1|0|+1)
        d = self.generator2ord
        l_ord = d[lhs]
        r_ord = d[rhs]
        if l_ord < r_ord: return -1
        elif l_ord > r_ord: return +1
        else: return 0
    def _always_verify_class_(self):
        # -> Bool
        return self.attr__always_verify_class

    def __get_ordered_generators__(self):
        # -> [g]
        return self.ordered_generators




class FiniteGroupOrderedFiniteDescription(GroupOrderedFiniteDescriptionABC):
    def __init__(self
        , ordered_generators
        , generator2degenerate_relationship
        , generator_pair2pairwise_sorted_relationship
        ):
        super().__init__(ordered_generators)
        ordered_generators = self.ordered_generators
        L = len(ordered_generators)

        assert len(generator2degenerate_relationship) == L
        assert set(generator2degenerate_relationship) == set(ordered_generators)
        assert len(generator_pair2pairwise_sorted_relationship) == L*(L-1)//2
            # choose(L, 2)

        (self.generator2degenerate_relationship
        ) = generator2degenerate_relationship
        (self.generator_pair2pairwise_sorted_relationship
        ) = generator_pair2pairwise_sorted_relationship

        (self.cache__mayinv_generator_pair2pairwise_sorted_relationship
        ) = {}
        self.cache__maybe_all_ordered_elements = None

    def __get_maybe_degenerate_relationship__(self, generator):
        # :: g -> (() | (PInt, ordered[(g, SInt)]))
        return self.generator2degenerate_relationship[generator]


    def __get_pairwise_sorted_relationship__(self, mayinv_lhs_generator, mayinv_rhs_generator):
        # :: (g, Bool) -> (g, Bool) -> ordered[(g, SInt)]
        cache = self.cache__mayinv_generator_pair2pairwise_sorted_relationship
        mayinv_generator_pair = mayinv_lhs_generator, mayinv_rhs_generator
        may_ordered_repr = cache.get(mayinv_generator_pair)
        if may_ordered_repr is not None:
            ordered_repr = may_ordered_repr
            return ordered_repr

        lhs, l_is_inv = mayinv_lhs_generator
        rhs, r_is_inv = mayinv_rhs_generator
        if not l_is_inv and not r_is_inv:
            generator_pair = (lhs, rhs)
            ordered_repr = self.generator_pair2pairwise_sorted_relationship[generator_pair]
        else:
            def mk_singleton(g, exp):
                # -> ordered_repr of len 1
                return ((g, exp),)
            def mk(g, is_inv):
                return mk_singleton(g, -1 if is_inv else +1)
            try:
                ordered_repr = IGroupOrderedFiniteDescription.mul(
                            self
                            ,mk(lhs, l_is_inv)
                            ,mk(rhs, r_is_inv)
                            )
            except RecursionError:
                print(mayinv_generator_pair)
                raise
        cache[mayinv_generator_pair] = ordered_repr
        return ordered_repr


    def _iter_generator_ord2exponent_modulus_(self):
        ordered_generators = self.ordered_generators
        generator2degenerate_relationship = self.generator2degenerate_relationship

        it_ord2exp = (generator2degenerate_relationship[g][0] for g in ordered_generators)
        return it_ord2exp
    def _iter_all_exponentss_of_ordered_elements_(self):
        it_ord2exp = self._iter_generator_ord2exponent_modulus_()
        return product(*map(range, it_ord2exp))
    def _make_all_ordered_elements_(self):
        ordered_generators = self.ordered_generators
        L = len(ordered_generators)

        def mk(es):
            assert len(es) == L
            ordered_repr = tuple((g,exp) for g, exp in zip(ordered_generators, es) if exp)
            return ordered_repr
        it_ess = self._iter_all_exponentss_of_ordered_elements_()
        all_ordered_elements = tuple(map(mk, it_ess))

        assert all(map(self.is_ordered_repr, all_ordered_elements))
        assert all(map(self.is_ordered_repr_std, all_ordered_elements))
        return all_ordered_elements
    @property
    def cache__all_ordered_elements(self):
        return self.make_all_ordered_elements()
    def make_all_ordered_elements(self):
        may_cache = self.cache__maybe_all_ordered_elements
        if may_cache is None:
            all_ordered_elements = self._make_all_ordered_elements_()
            self.cache__maybe_all_ordered_elements = all_ordered_elements
        else:
            all_ordered_elements = may_cache
        return all_ordered_elements

    def make_mul_table(self):
        # -> (idx2ordered_element, mul_table)
        # -> ([std_ordered_repr], [[UInt]])
        all_ordered_elements = self.make_all_ordered_elements()
        generator2ord = self.generator2ord


        L = len(generator2ord)
        SZ = len(all_ordered_elements)

        def ordered_repr2complete_exps(ordered_repr):
            def extend_es_util(pos):
                es.extend((i, 0) for i in range(len(es), pos))
            es = []
            for g, exp in ordered_repr:
                ord = generator2ord[g]
                extend_es_util(ord)
                assert len(es) == ord
                es.append((ord, exp))
            else:
                # bug: once without this block
                extend_es_util(L)
            assert len(es) == L
            return tuple(es)
        es2idx = {ordered_repr2complete_exps(ordered_repr):i
                for i, ordered_repr in enumerate(all_ordered_elements)}

        idxL2idxR2idxAns = []
        for i in range(SZ):
          idxR2idxAns = []
          lhs = all_ordered_elements[i]
          for j in range(SZ):
            rhs = all_ordered_elements[j]
            r = self.mul(lhs, rhs)
            es = ordered_repr2complete_exps(r)
            idxAns = es2idx[es]
            idxR2idxAns.append(idxAns)
          idxL2idxR2idxAns.append(tuple(idxR2idxAns))
        idxL2idxR2idxAns = tuple(idxL2idxR2idxAns)

        mul_table = idxL2idxR2idxAns
        complete_exponent2idx = es2idx
        idx2ordered_element = all_ordered_elements
        return idx2ordered_element, mul_table





class GroupOrderedFiniteDescription(GroupOrderedFiniteDescriptionABC):
    def __init__(self
        , ordered_generators
        , partial_generator2degenerate_relationship
        , mayinv_generator_pair2pairwise_sorted_relationship
        ):
        super().__init__(ordered_generators)
        ordered_generators = self.ordered_generators
        L = len(ordered_generators)


        assert len(partial_generator2degenerate_relationship) <= L
        assert set(partial_generator2degenerate_relationship) <= set(ordered_generators)
        assert len(mayinv_generator_pair2pairwise_sorted_relationship) == L*(L-1) * 2
            # choose(L, 2) * 4

        (self.partial_generator2degenerate_relationship
        ) = partial_generator2degenerate_relationship
        (self.mayinv_generator_pair2pairwise_sorted_relationship
        ) = mayinv_generator_pair2pairwise_sorted_relationship

    def __get_maybe_degenerate_relationship__(self, generator):
        # :: g -> (() | (PInt, ordered[(g, SInt)]))
        return self.partial_generator2degenerate_relationship.get(generator, ())

    def __get_pairwise_sorted_relationship__(self, mayinv_lhs_generator, mayinv_rhs_generator):
        # :: (g, Bool) -> (g, Bool) -> ordered[(g, SInt)]
        lhs, l_is_inv = mayinv_lhs_generator
        rhs, r_is_inv = mayinv_rhs_generator
        mayinv_generator_pair = (mayinv_lhs_generator, mayinv_rhs_generator)
        ordered_repr = self.mayinv_generator_pair2pairwise_sorted_relationship[mayinv_generator_pair]
        return ordered_repr




class Generator:
    def __init__(self, arg):
        self.arg = arg
    def __repr__(self):
        return f'Generator({self.arg!r})'













##############################################
rotation0 = 'rotation0'
rotation1 = 'rotation1'
mirror = 'mirror'
[rotation0, rotation1, mirror
    ] = map(Generator, [rotation0, rotation1, mirror])

def _C6():
    C6 = FiniteGroupOrderedFiniteDescription(
        [rotation0, rotation1]
        #, generator2degenerate_relationship
        , {rotation0: (3, ())
          ,rotation1: (2, ())
          }
        #, generator_pair2pairwise_sorted_relationship
        , {(rotation1, rotation0): ((rotation0, 1), (rotation1, 1))
          }
        )

    assert verify_group_finite_description(C6)
    return C6

def _D3():
    D3 = FiniteGroupOrderedFiniteDescription(
        [rotation0, mirror]
        #, generator2degenerate_relationship
        , {rotation0: (3, ())
          ,mirror: (2, ())
          }
        #, generator_pair2pairwise_sorted_relationship
        , {(mirror, rotation0): ((rotation0, 2), (mirror, 1))
          }
        )

    assert verify_group_finite_description(D3)
    return D3

'''
    C25*C2
    C25:C2
    C5*C5*C2
    (C5*C5):C2
    C5*(C5:C2)
    '''
def _G50_5x5_i2():
    # (C5*C5):C2
    G50_5x5_i2 = FiniteGroupOrderedFiniteDescription(
        [rotation0, rotation1, mirror]
        #, generator2degenerate_relationship
        , {rotation0: (5, ())
          ,rotation1: (5, ())
          ,mirror: (2, ())
          }
        #, generator_pair2pairwise_sorted_relationship
        , {(mirror, rotation0): ((rotation0, 4), (mirror, 1))
          ,(mirror, rotation1): ((rotation1, 4), (mirror, 1))
          ,(rotation1, rotation0): ((rotation0, 1), (rotation1, 1))
          }
        )

    assert verify_group_finite_description(G50_5x5_i2)
    return G50_5x5_i2


def _G50_5x_5i2():
    # C5*(C5:C2)
    G50_5x_5i2 = FiniteGroupOrderedFiniteDescription(
        [rotation0, rotation1, mirror]
        #, generator2degenerate_relationship
        , {rotation0: (5, ())
          ,rotation1: (5, ())
          ,mirror: (2, ())
          }
        #, generator_pair2pairwise_sorted_relationship
        , {(mirror, rotation0): ((rotation0, 1), (mirror, 1))
          ,(mirror, rotation1): ((rotation1, 4), (mirror, 1))
          ,(rotation1, rotation0): ((rotation0, 1), (rotation1, 1))
          }
        )

    assert verify_group_finite_description(G50_5x_5i2)
    return G50_5x_5i2



def _G50_5x5x2():
    # C5*C5*C2
    G50_5x5x2 = FiniteGroupOrderedFiniteDescription(
        [rotation0, rotation1, mirror]
        #, generator2degenerate_relationship
        , {rotation0: (5, ())
          ,rotation1: (5, ())
          ,mirror: (2, ())
          }
        #, generator_pair2pairwise_sorted_relationship
        , {(mirror, rotation0): ((rotation0, 1), (mirror, 1))
          ,(mirror, rotation1): ((rotation1, 1), (mirror, 1))
          ,(rotation1, rotation0): ((rotation0, 1), (rotation1, 1))
          }
        )

    assert verify_group_finite_description(G50_5x5x2)
    return G50_5x5x2

def _G50_25x2():
    # C25*C2
    G50_25x2 = FiniteGroupOrderedFiniteDescription(
        [rotation0, mirror]
        #, generator2degenerate_relationship
        , {rotation0: (25, ())
          ,mirror: (2, ())
          }
        #, generator_pair2pairwise_sorted_relationship
        , {(mirror, rotation0): ((rotation0, 1), (mirror, 1))
          }
        )

    assert verify_group_finite_description(G50_25x2)
    return G50_25x2



def _G50_25i2():
    # C25:C2
    G50_25i2 = FiniteGroupOrderedFiniteDescription(
        [rotation0, mirror]
        #, generator2degenerate_relationship
        , {rotation0: (25, ())
          ,mirror: (2, ())
          }
        #, generator_pair2pairwise_sorted_relationship
        , {(mirror, rotation0): ((rotation0, 24), (mirror, 1))
          }
        )

    assert verify_group_finite_description(G50_25i2)
    return G50_25i2






if __name__ == '__main__':
    C6 = _C6()
    D3 = _D3()
    #raise halt
    G50_5x5_i2 = _G50_5x5_i2()
    G50_5x_5i2 = _G50_5x_5i2()
    G50_5x5x2 = _G50_5x5x2()
    G50_25x2 = _G50_25x2()
    G50_25i2 = _G50_25i2()

def _show_mul_table(GD):
    (idx2ordered_element, mul_table) = GD.make_mul_table()
    print(f'idx2ordered_element = {idx2ordered_element}')
    print(f'mul_table = {mul_table}')

def _show_main():
    names_of_GD = '''
        C6
        D3
        G50_5x5_i2
        G50_5x_5i2
        G50_5x5x2
        G50_25x2
        G50_25i2
        '''.split()
    d = globals()
    for name in names_of_GD:
        print('\n'*5); print('='*60)
        print(name)
        GD = d[name]
        _show_mul_table(GD)



if __name__ == '__main__':
    _show_main()



