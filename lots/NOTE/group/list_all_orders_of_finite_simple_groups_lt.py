
'''
#list_all_orders_of_finite_simple_groups_lt
list_all_orders_of_finite_simple_groups_lt__without_repetition
    "__without_repetition" - orders of which there more than one simple groups occur in result seq only once.

see:
    "finite simple groups.txt"
        * shared orders
        * 18 families + Tits group + 26 sporadic groups
            * exclusions
        * the proof of "order_low_bound is strictly increasing"
'''

__all__ = '''
    list_all_orders_of_finite_simple_groups_lt__without_repetition
    list_all_shared_orders_of_finite_simple_groups_lt__without_repetition

    all_45_Eval_instances
        all_18_Eval_family_instances
        family_short_name2aEval

        family_short_name2family_long_name
        all_family_short_names
        all_family_long_names
        family_long_names2family_short_names
        make_family_short_names_from2
        make_family_short_names_from4

    IEvalStrictlyIncreasingTable
        IEvalOrderOfFiniteSimpleGroup
            EvalOrderOfSingletonGroup
            all_18_Eval_family_classes
                Cyclic
                Alternating
                ClassicalChevalleyGroups_An
                ClassicalChevalleyGroups_Bn
                ClassicalChevalleyGroups_Cn
                ClassicalChevalleyGroups_Dn
                ExceptionalChevalleyGroups_E6
                ExceptionalChevalleyGroups_E7
                ExceptionalChevalleyGroups_E8
                ExceptionalChevalleyGroups_F4
                ExceptionalChevalleyGroups_G2
                ClassicalSteinbergGroups__2An
                ClassicalSteinbergGroups__2Dn
                ExceptionalSteinbergGroups__2E6
                ExceptionalSteinbergGroups__3D4
                SuzukiGroups__2B2
                ReeGroups__2F4
                ReeGroups__2G2


    list_prime_numbers_lt
    list_prime_powers_lt
        aListPrimePowersLessThan
    '''.split()

'''
tools:
    override
    II
    ReIterable

    _show_list_lt
    _list_lt
    _verify_list
    _44_list_lt
    _45_list_lt
    _inplace_mk_name__order_parameterized_names_pairs

'''






from abc import ABC, abstractmethod
import itertools # count
import math # factorial
import operator # __mul__
import functools # reduce
from fractions import Fraction
from types import MappingProxyType

def override(f):
    return f
def II(iterable):
    return functools.reduce(operator.__mul__, iterable, 1)

class ReIterable:
    def __init__(self, iterable):
        self.__iterator = iter(iterable)
        self.cache = []
    def __getitem__(self, i):
        cache = self.cache
        if i >= len(cache):
            for _, x in zip(range(len(cache)-i+1), self.__iterator):
                cache.append(x)
        return cache[i] # may raise

    def __iter__(self):
        cache = self.cache
        it = self.__iterator
        i = 0
        while True:
            if i >= len(cache):
                for x in it:
                    break
                else:
                    return; yield
                cache.append(x)
            yield cache[i]
            i += 1

class IEvalStrictlyIncreasingTable(ABC):
    '''

assume ".eval_ex" is strictly increasing
    but sometimes there are small ranges that not "strictly increasing"
    hence we use
        "eval_ex :: {**kwargs} -> (result_value_low_bound, result_value)"
        instead of
            "eval_ex :: {**kwargs} -> result_value"
        where
            result_value_low_bound <= result_value
            result_value_low_bound(**kwargs) is "strictly increasing"
IEvalStrictlyIncreasingTable
    .get_parameter_names
    .get_parameter_names__should_known_upper_bound
    .get_maybe_min_result_value
    .iter_values_of_free_named_parameter
        # not get_parameter_names__should_known_upper_bound
    .list_values_of_named_parameter_lt
        # get_parameter_names__should_known_upper_bound
    .iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval
        # illegal argument_value of named_parameter
        #   but legal to be used in .eval_ex
        # used to find argument_value_upper_bound of named parameter when given result_value_upper_bound
        # sometimes it is easier than iter_values_of_free_named_parameter
        #   e.g. iter_prime_numbers vs iter_prime_powers
    .__eval_ex__
        :: {**kwargs} -> (result_value | (result_value_low_bound, result_value))
        :: {**kwargs} -> (result_value_low_bound | (result_value_low_bound, result_value))
        :: UInt^k -> (UInt|((UInt|Fraction|...), UInt))
        strictly increasing on result_value_low_bound
    .eval_maybe_min_argument_dict


    .eval_ex
        :: {**kwargs} -> (result_value_low_bound, result_value)
        :: UInt^k -> ((UInt|Fraction|...), UInt)
        strictly increasing on result_value_low_bound
    .eval_maybe_min_result_value
    .iter_unordered_result_values_lt__with_repetition
        :: UInt -> Bool -> (Iter UInt | Iter (UInt, argument_dict))
    .list_all_result_values_lt__without_repetition
    .detect_argument_value_upper_bound_for_result_value_upper_bound
'''
    __slots__ = ()

    @abstractmethod
    def does_exclude_argument_dict(self, **argument_dict):
        # -> Bool
        raise NotImplementedError
    @abstractmethod
    def get_parameter_names(self):
        # -> [str]
        raise NotImplementedError
    @abstractmethod
    def get_parameter_names__should_known_upper_bound(self):
        # -> [str]
        # return subset of .get_parameter_names()
        raise NotImplementedError

    @abstractmethod
    def get_maybe_min_result_value(self):
        # -> (None|UInt)
        # always allow return None
        return None
        raise NotImplementedError
    @abstractmethod
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        raise NotImplementedError
    @abstractmethod
    def list_values_of_named_parameter_lt(self, parameter_name, *, argument_value_upper_bound):
        # get_parameter_names__should_known_upper_bound
        raise NotImplementedError
    @abstractmethod
    def iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names__should_known_upper_bound
        raise NotImplementedError
    @abstractmethod
    def __eval_ex__(self, **kwargs):
        # :: {**kwargs} -> (result_value | (result_value_low_bound, result_value))
        # :: {**kwargs} -> (result_value_low_bound | (result_value_low_bound, result_value))
        # :: UInt^k -> (UInt|((UInt|Fraction|...), UInt))
        # strictly increasing on result_value_low_bound
        raise NotImplementedError




    def eval_ex(self, **kwargs):
        # :: {**kwargs} -> (result_value_low_bound, result_value)
        # :: UInt^k -> ((UInt|Fraction|...), UInt)
        #strictly increasing on result_value_low_bound
        r = type(self).__eval_ex__(self, **kwargs)
        if type(r) is tuple:
            # ((UInt|Fraction), UInt)
            (result_value_low_bound, result_value) = r
        else:
            result_value_low_bound = result_value = r

        assert result_value_low_bound <= result_value
        return (result_value_low_bound, result_value)

    def list_all_result_values_lt__without_repetition(self, *, result_value_upper_bound):
        it = self.iter_unordered_result_values_lt__with_repetition(
            result_value_upper_bound=result_value_upper_bound
            , with_argument_dict=False)
        return sorted(set(it))
    def iter_unordered_result_values_lt__with_repetition(self
        , *, result_value_upper_bound, with_argument_dict:bool
        ):
        # :: UInt -> Bool -> (Iter UInt | Iter (UInt, argument_dict))
        with_argument_dict = bool(with_argument_dict)
        maybe_min_result_value = self.get_maybe_min_result_value()
        if maybe_min_result_value is not None:
            min_result_value = maybe_min_result_value
            if result_value_upper_bound <= min_result_value:
                return; yield

        _parameter_names = self.get_parameter_names__should_known_upper_bound()
        parameter_name2value_seq = {}
        if _parameter_names:
            maybe_min_argument_dict = self.eval_maybe_min_argument_dict()
            if maybe_min_argument_dict is None:
                return; yield
            min_argument_dict = maybe_min_argument_dict

            __parameter_names = set(_parameter_names)
            assert len(__parameter_names) == len(_parameter_names)
            _parameter_names = __parameter_names; del __parameter_names
            for _parameter_name in _parameter_names:
                (argument_value_upper_bound
                ) = self.detect_argument_value_upper_bound_for_result_value_upper_bound(
                    parameter_name=_parameter_name
                    ,result_value_upper_bound=result_value_upper_bound
                    ,min_argument_dict=min_argument_dict
                    )
                (parameter_name2value_seq[_parameter_name]
                ) = self.list_values_of_named_parameter_lt(
                    _parameter_name
                    , argument_value_upper_bound=argument_value_upper_bound
                    )

        def _reiter_values_of_named_parameter(parameter_name):
            may_ls = parameter_name2value_seq.get(parameter_name)
            if may_ls is None:
                it = self.iter_values_of_free_named_parameter(parameter_name)
                reiter = ReIterable(it)
            else:
                reiter = ls = may_ls
            return reiter
            return ReIterable

        parameter_names = self.get_parameter_names()
        L = len(parameter_names)

        idx2parameter_names = tuple(parameter_names); del parameter_names
        idx2reiterables = tuple(map(
            _reiter_values_of_named_parameter, idx2parameter_names))
        assert L == len(set(idx2parameter_names))


        argument_dict = {}
        def f(idx):
            if idx == L:
                (result_value_low_bound, result_value) = self.eval_ex(**argument_dict)
                # MUST yield; even excluded!
                if result_value_low_bound < result_value_upper_bound:
                    excluded = ((result_value >= result_value_upper_bound)
                                or self.does_exclude_argument_dict(**argument_dict)
                                )
                    if with_argument_dict:
                        yield excluded, (result_value, dict(argument_dict))
                    else:
                        yield excluded, result_value
                return

            name = idx2parameter_names[idx]
            it_vals = iter(idx2reiterables[idx])
            for v in it_vals:
                argument_dict[name] = v
                it_result_values = f(idx+1)
                for result_value in it_result_values:
                    break
                else:
                    # nothing
                    # stop at this layer, since strictly increasing
                    break
                yield result_value
                yield from it_result_values
                # when name=v, there is "result_value" < "result_value_upper_bound"
                # try next v
            return # f()
        # end f()

        ############### should exclude here instead inside f()
        #yield from f(0)
        for excluded, r in f(0):
            if not excluded:
                yield r
        return



    def eval_maybe_min_result_value(self):
        maybe_min_argument_dict = self.eval_maybe_min_argument_dict()
        if maybe_min_argument_dict  is None:
            return None
        argument_dict = maybe_min_argument_dict

        (result_value_low_bound, result_value) = self.eval_ex(**argument_dict)
        if self.does_exclude_argument_dict(**argument_dict):
            it = aListPrimePowersLessThan.iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval('p')
            for result_value_upper_bound in it:
                if result_value_low_bound < result_value_upper_bound:
                    break
            for result_value_upper_bound in it:
                ls = self.list_all_result_values_lt__without_repetition(
                    result_value_upper_bound=result_value_upper_bound)
                if ls:
                    break
            else:
                return None
            first_result_value = ls[0]
        else:
            result_value_upper_bound = result_value + 1
            ls = self.list_all_result_values_lt__without_repetition(
                result_value_upper_bound=result_value_upper_bound)
            assert ls
            first_result_value = ls[0]
            assert result_value_low_bound <= first_result_value <= result_value
        return first_result_value

    @abstractmethod
    def eval_maybe_min_argument_dict(self):
        if self.get_parameter_names__should_known_upper_bound():
            raise logic-error
        parameter_names = self.get_parameter_names()
        L = len(parameter_names)

        idx2parameter_names = tuple(parameter_names); del parameter_names
        idx2parameter_first_value = []
        for name in idx2parameter_names:
            for first_value in self.iter_values_of_free_named_parameter(name):
                break
            else:
                return None
            idx2parameter_first_value.append(first_value)
        value_vector = idx2parameter_first_value
        argument_dict = dict(zip(idx2parameter_names, value_vector))
        return argument_dict


    def detect_argument_value_upper_bound_for_result_value_upper_bound(self
        ,parameter_name
        ,*
        ,result_value_upper_bound
        ,min_argument_dict
        ):
        # get_parameter_names__should_known_upper_bound
        pass;
        '''
        maybe_min_argument_dict = self.eval_maybe_min_argument_dict()
        if maybe_min_argument_dict  is None:
            return 0
        argument_dict = maybe_min_argument_dict
        '''
        argument_dict = min_argument_dict

        it = self.iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(parameter_name)
        for argument_value in it:
            argument_dict[parameter_name] = argument_value
            (result_value_low_bound, result_value) = self.eval_ex(**argument_dict)
            if not result_value_low_bound < result_value_upper_bound:
                argument_value_upper_bound = argument_value
                break
        return argument_value_upper_bound


class ListPrimePowersLessThan(IEvalStrictlyIncreasingTable):
    @override
    def does_exclude_argument_dict(self, **argument_dict):
        return False
    @override
    def get_parameter_names(self):
        # -> [str]
        return ("p", "k")
    @override
    def get_parameter_names__should_known_upper_bound(self):
        # -> [str]
        # return subset of .get_parameter_names()
        return ('p',)

    @override
    def get_maybe_min_result_value(self):
        # -> UInt
        return 2

    @override
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        if parameter_name != 'k': raise NameError
        return itertools.count(1)

    @override
    def list_values_of_named_parameter_lt(self, parameter_name, *, argument_value_upper_bound):
        # get_parameter_names__should_known_upper_bound
        if parameter_name != 'p': raise NameError
        ls = list_prime_numbers_lt(argument_value_upper_bound)
        return ls

    @override
    def iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names__should_known_upper_bound
        if parameter_name != 'p': raise NameError
        i = 2
        step = 1
        while True:
            yield i
            i += step
            step <<= 1
        return
        return itertools.count(3, 2)
    @override
    def __eval_ex__(self, *, p, k):
        #:: UInt^k -> UInt
        return p**k
    @override
    def eval_maybe_min_argument_dict(self):
        return dict(p=2, k=1)

aListPrimePowersLessThan = ListPrimePowersLessThan()

def list_prime_numbers_lt(prime_upper_bound):
    # -> [p] # increasing
    L = prime_upper_bound
    uint2is_prime = [False, False] # uint2is_prime
    uint2is_prime.extend(True for _ in range(L-2))
    assert len(uint2is_prime) == L

    for u in range(L):
        if uint2is_prime[u]:
            # bug: for j in range(u+u, L):
            for j in range(u+u, L, u):
                uint2is_prime[j] = False

    primes = []
    for u, is_prime in enumerate(uint2is_prime):
        if is_prime:
            primes.append(u)
    return primes
def list_prime_powers_lt(prime_power_upper_bound):
    # -> [p^k] # increasing
    return aListPrimePowersLessThan.list_all_result_values_lt__without_repetition(result_value_upper_bound=prime_power_upper_bound)


if __name__ == '__main__':
    assert list_prime_numbers_lt(100) == \
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert list_prime_powers_lt(100) == \
        [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37, 41, 43, 47, 49, 53, 59, 61, 64, 67, 71, 73, 79, 81, 83, 89, 97]



class IEvalOrderOfFiniteSimpleGroup(IEvalStrictlyIncreasingTable):
    '''

assume ".eval_order_ex" is strictly increasing
IEvalOrderOfFiniteSimpleGroup
    #.family_long_name
    #.family_short_name
    #.group_name_template
    .get_family_long_name
    .get_family_short_name
    .get_group_name_template

    .get_parameter_names
    .get_maybe_min_order
    .iter_values_of_free_named_parameter
    .__eval_order_ex__
        # like: __eval_ex__
        # :: UInt^k -> (UInt|((UInt|Fraction|...), UInt))

    .eval_order_ex
        # like .eval_ex
        # :: UInt^k -> ((UInt|Fraction|...), UInt)
    .list_prime_numbers_lt
    .list_prime_powers_lt
    .eval_maybe_min_order
    .list_all_orders_of_finite_simple_groups_lt__without_repetition
'''
    __slots__ = ()

    @abstractmethod
    def get_family_long_name(self):pass
    @abstractmethod
    def get_family_short_name(self):pass
    @abstractmethod
    def get_group_name_template(self):pass

    @abstractmethod
    def get_maybe_min_order(self):
        # -> UInt
        raise NotImplementedError
    @abstractmethod
    def __eval_order_ex__(self, **kwargs):
        # like __eval_ex__
        # :: UInt^k -> (UInt|((UInt|Fraction|...), UInt))
        raise NotImplementedError


    def eval_order_ex(self, **kwargs):
        # :: UInt^k -> ((UInt|Fraction|...), UInt)
        return self.eval_ex(**kwargs)
    def list_prime_numbers_lt(self, prime_upper_bound):
        return list_prime_numbers_lt(prime_upper_bound)
    def list_prime_powers_lt(self, prime_power_upper_bound):
        # -> [p^k] # increasing
        return list_prime_powers_lt(prime_power_upper_bound)



    @override
    def __eval_ex__(self, **kwargs):
        # :: UInt^k -> (UInt|((UInt|Fraction|...), UInt))
        return type(self).__eval_order_ex__(self, **kwargs)
    @override
    def get_maybe_min_result_value(self):
        return self.get_maybe_min_order()

    def list_all_orders_of_finite_simple_groups_lt__without_repetition(self, *, result_value_upper_bound):
        return self.list_all_result_values_lt__without_repetition(
            result_value_upper_bound=result_value_upper_bound)
    def eval_maybe_min_order(self):
        return self.eval_maybe_min_result_value()






def _verify_list(__aEval, __result_value_seq, **kwargs_for_fst_element):
    aEval = __aEval
    result_value_seq = __result_value_seq

    assert isinstance(aEval, IEvalOrderOfFiniteSimpleGroup)
    assert type(result_value_seq) is list

    ls = result_value_seq
    assert ls[0] == aEval.eval_maybe_min_order()
    assert ls[0] == aEval.eval_order_ex(**kwargs_for_fst_element)[1]

    LAST = ls[0]
    assert _list_lt(aEval, LAST) == []
    assert _list_lt(aEval, LAST+1) == [LAST]

    LAST = ls[-1]
    assert _list_lt(aEval, LAST+1) == ls




def _show_list_lt(aEval, result_value_upper_bound):
    r = _list_lt(aEval, result_value_upper_bound)
    print(r)
    return r
def _list_lt(aEval, result_value_upper_bound):
    assert isinstance(aEval, IEvalOrderOfFiniteSimpleGroup)
    return aEval.list_all_orders_of_finite_simple_groups_lt__without_repetition(
            result_value_upper_bound=result_value_upper_bound)




class Alternating(IEvalOrderOfFiniteSimpleGroup):
    @override
    def does_exclude_argument_dict(self, **argument_dict):
        return False
    @override
    def get_family_long_name(self):
        return 'Alternating'
    @override
    def get_family_short_name(self):
        return 'Alt'
    @override
    def get_group_name_template(self):
        return 'Alt[{n}]'

    @override
    def get_maybe_min_order(self):
        # -> UInt
        return 60
    @override
    def __eval_order_ex__(self, *, n):
        #:: UInt^k -> UInt
        return math.factorial(n)//2

    @override
    def get_parameter_names(self):
        # -> [str]
        return ('n',)
    @override
    def get_parameter_names__should_known_upper_bound(self):
        # -> [str]
        # return subset of .get_parameter_names()
        return ()
    @override
    def eval_maybe_min_argument_dict(self):
        return {'n':5}

    @override
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        if parameter_name != 'n': raise NameError
        return itertools.count(5)
    @override
    def list_values_of_named_parameter_lt(self, parameter_name, *, argument_value_upper_bound):
        # get_parameter_names__should_known_upper_bound
        raise logic-error
    @override
    def iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names__should_known_upper_bound
        raise logic-error


global_aAlternating = Alternating()
    # required by list_all_shared_orders_of_finite_simple_groups_lt__without_repetition
if __name__ == '__main__':
    aAlternating = Alternating()
    # A001710 Order of alternating group A_n, or number of even permutations of n letters.
    #   [1, 1, 1, 3, 12, 60, 360, 2520, 20160, 181440, 1814400, 19958400, 239500800, 3113510400, 43589145600, 653837184000, 10461394944000, 177843714048000, 3201186852864000, 60822550204416000, 1216451004088320000]
    Alt_ls = [60, 360, 2520, 20160, 181440, 1814400, 19958400, 239500800, 3113510400, 43589145600, 653837184000, 10461394944000, 177843714048000, 3201186852864000, 60822550204416000, 1216451004088320000]

    _verify_list(aAlternating, Alt_ls, n=5)


class Cyclic(IEvalOrderOfFiniteSimpleGroup):
    @override
    def does_exclude_argument_dict(self, **argument_dict):
        return False
    @override
    def get_family_long_name(self):
        return 'Cyclic'
    @override
    def get_family_short_name(self):
        return 'C'
    @override
    def get_group_name_template(self):
        return 'C[{p}]'

    @override
    def get_maybe_min_order(self):
        # -> UInt
        return 2
    @override
    def __eval_order_ex__(self, *, p):
        #:: UInt^k -> UInt
        return p

    @override
    def get_parameter_names(self):
        # -> [str]
        return ('p',)
    @override
    def get_parameter_names__should_known_upper_bound(self):
        # -> [str]
        # return subset of .get_parameter_names()
        return ('p',)
    @override
    def eval_maybe_min_argument_dict(self):
        return {'p':2}

    @override
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        raise logic-error
    @override
    def list_values_of_named_parameter_lt(self, parameter_name, *, argument_value_upper_bound):
        # get_parameter_names__should_known_upper_bound
        if parameter_name != 'p': raise NameError
        return self.list_prime_numbers_lt(argument_value_upper_bound)
    @override
    def iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names__should_known_upper_bound
        if parameter_name != 'p': raise NameError
        return aListPrimePowersLessThan.iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval('p')

if __name__ == '__main__':
    aCyclic = Cyclic()
    assert _list_lt(aCyclic, 2) == []
    assert _list_lt(aCyclic, 3) == [2]
    assert _list_lt(aCyclic, 100) == list_prime_numbers_lt(100)














class IEvalOrderOfFiniteSimpleGroup__div_gcd(IEvalOrderOfFiniteSimpleGroup):
    '''
order = numerator / gcd(gcd_left, gcd_right)
    # gcd_left may > gcd_right
    #   but most gcd_left <= gcd_right
    '''
    @override
    def get_maybe_min_order(self):
        # -> None|UInt
        return None

    def eval_order_ex__div_gcd(self, *, numerator, gcd_left, gcd_right):
        '''
may not correct in general
    but there are finite possible cases for finite simple groups
    I will check correctness for them

order = numerator / gcd(gcd_left, gcd_right)
order_low_bound = numerator / gcd_left
    # argument_dict is value_vector for named_parameters
    numerator ~ argument_dict
    gcd_left ~ argument_dict
    gcd_right ~ argument_dict

order_low_bound <= order
both order/order_low_bound may be not "strictly increasing"

but let's assume:
    order_low_bound is "strictly increasing"
        # ??, to verify for all cases
    order_low_bound <= order
        # YES
        '''
        N = numerator
        D = math.gcd(gcd_left, gcd_right)
        maxD = gcd_left
        assert 0 < D <= maxD
        orderA_low_bound = Fraction(N, maxD)
        orderA = N//D
        assert orderA_low_bound <= orderA == Fraction(N, D)
        return (orderA_low_bound, orderA)

    @abstractmethod
    def excluded_argument_dicts():pass
    @abstractmethod
    def family_long_name():pass
    @abstractmethod
    def family_short_name():pass
    @abstractmethod
    def group_name_template():pass
    @abstractmethod
    def parameter_names():pass
    @abstractmethod
    def parameter_names__should_known_upper_bound():pass
    @abstractmethod
    def min_argument_dict():pass

    @override
    def does_exclude_argument_dict(self, **argument_dict):
        return argument_dict in type(self).excluded_argument_dicts
    @override
    def get_family_long_name(self):
        return type(self).family_long_name
    @override
    def get_family_short_name(self):
        return type(self).family_short_name
    @override
    def get_group_name_template(self):
        return type(self).group_name_template

    @override
    def get_parameter_names(self):
        # -> [str]
        return tuple(type(self).parameter_names)
    @override
    def get_parameter_names__should_known_upper_bound(self):
        # -> [str]
        # return subset of .get_parameter_names()
        return tuple(type(self).parameter_names__should_known_upper_bound)
    @override
    def eval_maybe_min_argument_dict(self):
        return dict(type(self).min_argument_dict)



class IEvalOrderOfFiniteSimpleGroup__div_gcd__q_(IEvalOrderOfFiniteSimpleGroup__div_gcd):
    '''
    parameter_names__should_known_upper_bound = ('q',)

    .parameter_names = ...
    .iter_values_of_free_named_parameter = ...
    '''
    parameter_names__should_known_upper_bound = ('q',)

    @override
    def list_values_of_named_parameter_lt(self, parameter_name, *, argument_value_upper_bound):
        # get_parameter_names__should_known_upper_bound
        if parameter_name != 'q': raise NameError
        return self.list_prime_powers_lt(argument_value_upper_bound)
    @override
    def iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names__should_known_upper_bound
        if parameter_name != 'q': raise NameError
        return aListPrimePowersLessThan.iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval('p') # !!!q not q here!!!

class IEvalOrderOfFiniteSimpleGroup__div_gcd__q(IEvalOrderOfFiniteSimpleGroup__div_gcd__q_):
    '''
    parameter_names = ('q',)
    '''
    parameter_names = ('q',)

    @override
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        raise logic-error




class IEvalOrderOfFiniteSimpleGroup__div_gcd__n_q(IEvalOrderOfFiniteSimpleGroup__div_gcd__q_):
    '''
    parameter_names = ('n', 'q')
    '''
    parameter_names = ('n', 'q')

    @abstractmethod
    def min_n():pass

    @override
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        if parameter_name != 'n': raise NameError
        return itertools.count(type(self).min_n)





class ClassicalChevalleyGroups_An(IEvalOrderOfFiniteSimpleGroup__div_gcd__n_q):
    '''
    * A[n](q) if [n >= 1]
        orderA q n = q^(n*(n+1)/2)/gcd(n+1,q-1) * II q^(i+1) - 1 {i <- [1..n]}
        exclusions: A[1](2), A[1](3)

!!!!!!!!!!!!! not strictly increasing !!!!!!!!!!!!!!!
[(60, {'n': 1, 'q': 4}), (60, {'n': 1, 'q': 5}), (168, {'n': 1, 'q': 7}), (168, {'n': 2, 'q': 2}), (360, {'n': 1, 'q': 9}), (504, {'n': 1, 'q': 8}), (660, {'n': 1, 'q': 11}), (1092, {'n': 1, 'q': 13}), (2448, {'n': 1, 'q': 17}), (3420, {'n': 1, 'q': 19}), (4080, {'n': 1, 'q': 16}), (5616, {'n': 2, 'q': 3}), (6072, {'n': 1, 'q': 23}), (7800, {'n': 1, 'q': 25}), (9828, {'n': 1, 'q': 27}), (12180, {'n': 1, 'q': 29}), (14880, {'n': 1, 'q': 31}), (20160, {'n': 2, 'q': 4}), (20160, {'n': 3, 'q': 2}), (25308, {'n': 1, 'q': 37}), (32736, {'n': 1, 'q': 32})]

(n,q):
    bad:
    f(1,4) =60= f(1,5)
    f(1,9) =360<504= f(1,8)
    f(1,17) =2448<4080= f(1,16)
    f(1,19) =3420<4080= f(1,16)
    '''
    excluded_argument_dicts = (
        {'n':1, 'q':2}
        ,{'n':1, 'q':3}
        )
    family_long_name = 'ClassicalChevalleyGroups_An'
    family_short_name = 'An'
    group_name_template = 'A[{n}]({q})'
    min_argument_dict = {'n':1, 'q':2}
    min_n = 1

    @override
    def __eval_order_ex__(self, *, n, q):
        # :: UInt^k -> (Fraction, UInt)
        # orderA = q**(n*(n+1)//2) * II(q**(i+1) - 1 for i in range(1, n+1)) //math.gcd(n+1,q-1)
        N = q**(n*(n+1)//2) * II(q**(i+1) - 1 for i in range(1, n+1))
        L = n+1
        R = q-1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


def _get_argument_value_upper_bound(self, parameter_name, *, result_value_upper_bound):
    min_argument_dict = self.eval_maybe_min_argument_dict()
    if min_argument_dict is None: raise NotImplementedError
    (argument_value_upper_bound
    ) = self.detect_argument_value_upper_bound_for_result_value_upper_bound(
        parameter_name=parameter_name
        ,result_value_upper_bound=result_value_upper_bound
        ,min_argument_dict=min_argument_dict
        )
    return argument_value_upper_bound

if __name__ == '__main__':
    aClassicalChevalleyGroups_An = ClassicalChevalleyGroups_An()
    orderA_ex = lambda n, q: aClassicalChevalleyGroups_An.eval_order_ex(n=n,q=q)
    orderA = lambda n, q: orderA_ex(n,q)[1]
    assert orderA(1, 5) == orderA(1, 4)
    assert orderA(1, 9) < orderA(1, 8)
    assert orderA(1, 19) < orderA(1, 16)
    assert orderA(1, 17) < orderA(1, 16)

    assert orderA_ex(1, 5) > orderA_ex(1, 4)
    assert orderA_ex(1, 9) > orderA_ex(1, 8)
    assert orderA_ex(1, 19) > orderA_ex(1, 16)
    assert orderA_ex(1, 17) > orderA_ex(1, 16)


    An_ls = [60, 168, 360, 504, 660, 1092, 2448, 3420]
    # excluded: A[1](2), A[1](3)
    _verify_list(aClassicalChevalleyGroups_An, An_ls, n=1, q=4)







class _ClassicalChevalleyGroups_Bn_Cn(IEvalOrderOfFiniteSimpleGroup__div_gcd__n_q):
    '''
        * B[n](q) if [n >= 2]
            exclusions: B[2](2)
        * C[n](q) if [n >= 3]
            orderBC q n = q^(n^2)/gcd(2,q-1) * II q^(2*i) - 1 {i <- [1..n]}
    '''

    @override
    def __eval_order_ex__(self, *, n, q):
        # :: UInt^k -> (Fraction, UInt)
        # orderBC q n = q^(n^2)/gcd(2,q-1) * II q^(2*i) - 1 {i <- [1..n]}
        N = q**(n**2) * II(q**(2*i) - 1 for i in range(1, n+1))
        L = 2
        R = q-1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


class ClassicalChevalleyGroups_Bn(_ClassicalChevalleyGroups_Bn_Cn):
    '''
        * B[n](q) if [n >= 2]
            exclusions: B[2](2)
    '''
    excluded_argument_dicts = (
        {'n':2, 'q':2}
        ,
        )
    family_long_name = 'ClassicalChevalleyGroups_Bn'
    family_short_name = 'Bn'
    group_name_template = 'B[{n}]({q})'
    min_argument_dict = {'n':2, 'q':2}
    min_n = 2

class ClassicalChevalleyGroups_Cn(_ClassicalChevalleyGroups_Bn_Cn):
    '''
        * C[n](q) if [n >= 3]
            exclusions: None
    '''
    excluded_argument_dicts = ()
    family_long_name = 'ClassicalChevalleyGroups_Cn'
    family_short_name = 'Cn'
    group_name_template = 'C[{n}]({q})'
    min_argument_dict = {'n':3, 'q':2}
    min_n = 3

if __name__ == '__main__':
    aClassicalChevalleyGroups_Bn = ClassicalChevalleyGroups_Bn()
    aClassicalChevalleyGroups_Cn = ClassicalChevalleyGroups_Cn()

    # A003938 Order of (usually) simple Chevalley group B_2(q), q = prime power.
    #   A003938 has bug: starts with 720 which should be excluded
    #       [720, 25920, 979200, 4680000, 138297600, 1056706560, 1721606400, 12860654400, 68518981440, 1095199948800, 1004497044480, 3057017889600, 20674026236160, 47607300000000, 102804157834560, 210103196385600]
    # A003939 Order of simple Chevalley group B_3(q), q = prime power.
    #   [1451520, 4585351680, 4106059776000, 228501000000000, 273457218604953600, 9077005607176765440, 54025731402499584000, 3669292720793456064000, 122796979335906113871360, 19266960106724096212992000]
    # A003940 Order of simple Chevalley group B_4(q), q = prime power.
    #   [47377612800, 65784756654489600, 4408780839651901440000, 6973279267500000000000000, 1298254740461168363656151040000, 319368723699461283992462111539200]
    # ...B_[n](q)...
    #
    LAST = 4585351680
    Bn_ls = [25920, 979200, 1451520, 4680000, 138297600, 1056706560, 1721606400, 4585351680]
    Cn_ls = [1451520, 4585351680]

    # excluded: B[2](2)
    _verify_list(aClassicalChevalleyGroups_Bn, Bn_ls, n=2, q=3)
    _verify_list(aClassicalChevalleyGroups_Cn, Cn_ls, n=3, q=2)




class ClassicalChevalleyGroups_Dn(IEvalOrderOfFiniteSimpleGroup__div_gcd__n_q):
    '''
        * D[n](q) if [n >= 4]
            orderD q n = q^(n*(n-1)) * (q^n - 1)/gcd(4,q^n - 1) * II q^(2*i) - 1 {i <- [1..n-1]}
            # NOTE: [1..n-1] not [1..n]
    '''

    excluded_argument_dicts = ()
    family_long_name = 'ClassicalChevalleyGroups_Dn'
    family_short_name = 'Dn'
    group_name_template = 'D[{n}]({q})'
    min_argument_dict = {'n':4, 'q':2}
    min_n = 4

    @override
    def __eval_order_ex__(self, *, n, q):
        # :: UInt^k -> (Fraction, UInt)
        # orderD q n = q^(n*(n-1)) * (q^n - 1)/gcd(4,q^n - 1) * II q^(2*i) - 1 {i <- [1..n-1]}
        #   NOTE: [1..n-1] not [1..n]
        N = q**(n*(n-1)) * (q**n - 1) * II(q**(2*i) - 1 for i in range(1, (n-1)+1))
        L = 4
        R = q**n - 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aClassicalChevalleyGroups_Dn = ClassicalChevalleyGroups_Dn()

    # A003850 Order of simple Chevalley group D_4(q), q = prime power.
    #   [174182400, 4952179814400, 67010895544320000, 8911539000000000000, 112554991177798901760000, 19031213036231093492121600, 129182006871144805294080000, 35749625435272978955066880000]
    # A003851 Order of simple Chevalley group D_5(q), q = prime power.
    #   [23499295948800, 1289512799941305139200, 1154606796534757164318720000, 6807663884896875000000000000000, 52386144472825139642572263782154240000, 42863636354909175368011800612065142374400, 2154683673871373733440812330742751559680000]
    # A003852 Order of simple Chevalley group D_6(q), q = prime power.
    #   [50027557148216524800, 6762844700608770238252960972800, 5081732431326820541485324550799360000000, 3246978048053003424316406250000000000000000000, 14630778277213500974314928221817819519899234908241920000]
    # ...D_[n](q)...
    #
    Dn_ls = [D4_2, D4_3, D5_2] = [174182400, 4952179814400, 23499295948800]
    _verify_list(aClassicalChevalleyGroups_Dn, Dn_ls, n=4, q=2)


class ExceptionalChevalleyGroups_E6(IEvalOrderOfFiniteSimpleGroup__div_gcd__q):
    '''
        * E[6](q)
            orderE6 q = q^36 /gcd(3,q-1) * II q^i - 1 {i <- [2,5,6,8,9,12]}
    '''

    excluded_argument_dicts = ()
    family_long_name = 'ExceptionalChevalleyGroups_E6'
    family_short_name = 'E6'
    group_name_template = 'E[6]({q})'
    min_argument_dict = {'q':2}

    @override
    def __eval_order_ex__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # orderE6 q = q^36 /gcd(3,q-1) * II q^i - 1 {i <- [2,5,6,8,9,12]}
        N = q**36 * II(q**i - 1 for i in [2,5,6,8,9,12])
        L = 3
        R = q-1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aExceptionalChevalleyGroups_E6 = ExceptionalChevalleyGroups_E6()

    # A008871 Order of universal Chevalley group E_6 (q), q = prime power.
    # A008871 has a bug: forgot to div gcd(3,q-1) @(q=4)
    #   [214841575522005575270400, 14515406695082926420056516790429286400, 85528710781342640103833619055142765466746880000, 3175144122737732284276405334472656250000000000000000000]
    E6_2toX = [E6_2, E6_3, E6_4, E6_5] = \
        [214841575522005575270400, 14515406695082926420056516790429286400, 28509570260447546701277873018380921822248960000, 3175144122737732284276405334472656250000000000000000000]
    E6_4_at_A008871 = 85528710781342640103833619055142765466746880000
    assert 3 * E6_4 == E6_4_at_A008871
    assert [E6_2, E6_3, E6_4, E6_5] != [E6_2, E6_3, E6_4_at_A008871, E6_5]
    _verify_list(aExceptionalChevalleyGroups_E6, E6_2toX, q=2)




class ExceptionalChevalleyGroups_E7(IEvalOrderOfFiniteSimpleGroup__div_gcd__q):
    '''
        * E[7](q)
            orderE7 q = q^63 /gcd(2,q-1) * II q^i - 1 {i <- [2,6,8,10,12,14,18]}
    '''

    excluded_argument_dicts = ()
    family_long_name = 'ExceptionalChevalleyGroups_E7'
    family_short_name = 'E7'
    group_name_template = 'E[7]({q})'
    min_argument_dict = {'q':2}

    @override
    def __eval_order_ex__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # orderE7 q = q^63 /gcd(2,q-1) * II q^i - 1 {i <- [2,6,8,10,12,14,18]}
        N = q**63 * II(q**i - 1 for i in [2,6,8,10,12,14,18])
        L = 2
        R = q-1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aExceptionalChevalleyGroups_E7 = ExceptionalChevalleyGroups_E7()

    # A008869 Order of universal Chevalley group E_7 (q), q = prime power.
    # A008869 has a bug: forgot to div gcd(2,q-1) @(q=3)
    #   [7997476042075799759100487262680802918400, 2542750473636273484480959502278043289108758407541532509234790400]

    E7_2 = 7997476042075799759100487262680802918400
    E7_3 = 1271375236818136742240479751139021644554379203770766254617395200
    E7_3_at_A008869 = 2542750473636273484480959502278043289108758407541532509234790400
    assert E7_3*2 == E7_3_at_A008869

    E7_2toX = [E7_2, E7_3]
    assert [E7_2, E7_3] != [E7_2, E7_3_at_A008869]
    _verify_list(aExceptionalChevalleyGroups_E7, E7_2toX, q=2)



class ExceptionalChevalleyGroups_E8(IEvalOrderOfFiniteSimpleGroup__div_gcd__q):
    '''
        * E[8](q)
            orderE8 q = q^120 * II q^i - 1 {i <- [2,8,12,14,18,20,24,30]}
    '''

    excluded_argument_dicts = ()
    family_long_name = 'ExceptionalChevalleyGroups_E8'
    family_short_name = 'E8'
    group_name_template = 'E[8]({q})'
    min_argument_dict = {'q':2}

    @override
    def __eval_order_ex__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # orderE8 q = q^120 * II q^i - 1 {i <- [2,8,12,14,18,20,24,30]}
        N = q**120 * II(q**i - 1 for i in [2,8,12,14,18,20,24,30])
        L = 1
        R = 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aExceptionalChevalleyGroups_E8 = ExceptionalChevalleyGroups_E8()

    # A008868 Order of simple Chevalley group E_8 (q), q = prime power.
    #   [337804753143634806261388190614085595079991692242467651576160959909068800000, 18830052912953932311099032439972660332140886784940152038522449391826616580150109878711243949982163694448626420940800000, 191797292142671717754639757897512906421357507604216557533558287598236977154127870984484770345340348298409697395609822849492217656441474908160000000000]
    E8_2toX = [337804753143634806261388190614085595079991692242467651576160959909068800000, 18830052912953932311099032439972660332140886784940152038522449391826616580150109878711243949982163694448626420940800000, 191797292142671717754639757897512906421357507604216557533558287598236977154127870984484770345340348298409697395609822849492217656441474908160000000000]
    _verify_list(aExceptionalChevalleyGroups_E8, E8_2toX, q=2)






class ExceptionalChevalleyGroups_F4(IEvalOrderOfFiniteSimpleGroup__div_gcd__q):
    '''
        * F[4](q)
            orderF4 q = q^24 * II q^i - 1 {i <- [2,6,8,12]}
    '''

    excluded_argument_dicts = ()
    family_long_name = 'ExceptionalChevalleyGroups_F4'
    family_short_name = 'F4'
    group_name_template = 'F[4]({q})'
    min_argument_dict = {'q':2}

    @override
    def __eval_order_ex__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # orderF4 q = q^24 * II q^i - 1 {i <- [2,6,8,12]}
        N = q**24 * II(q**i - 1 for i in [2,6,8,12])
        L = 1
        R = 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aExceptionalChevalleyGroups_F4 = ExceptionalChevalleyGroups_F4()

    # A008913 Order of simple Chevalley group F_4(q), q = prime power
    #   [3311126603366400, 5734420792816671844761600, 19009825523840945451297669120000, 2131486317725501953125000000000000000, 86325573304608766361629193317905069834240000]

    F4_2toX = [3311126603366400, 5734420792816671844761600, 19009825523840945451297669120000, 2131486317725501953125000000000000000, 86325573304608766361629193317905069834240000]
    _verify_list(aExceptionalChevalleyGroups_F4, F4_2toX, q=2)




class ExceptionalChevalleyGroups_G2(IEvalOrderOfFiniteSimpleGroup__div_gcd__q):
    '''
        * G[2](q)
            orderG2 q = q^6 * II q^i - 1 {i <- [2,6]}
            exclusions: G[2](2)
    '''

    excluded_argument_dicts = ({'q':2},)
    family_long_name = 'ExceptionalChevalleyGroups_G2'
    family_short_name = 'G2'
    group_name_template = 'G[2]({q})'
    min_argument_dict = {'q':2}

    @override
    def __eval_order_ex__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # orderG2 q = q^6 * II q^i - 1 {i <- [2,6]}
        N = q**6 * II(q**i - 1 for i in [2,6])
        L = 1
        R = 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aExceptionalChevalleyGroups_G2 = ExceptionalChevalleyGroups_G2()

    # A008914 Order of simple Chevalley group G_2 (q), q = prime power.
    #   A008914 has a bug: starts with 12096, which should be excluded
    #   [12096, 4245696, 251596800, 5859000000, 664376138496, 4329310519296, 22594320403200, 376611192619200, 3914077489672896, 71776114783027200, 167795197370551296, 796793353927300800, 11570921621943780096]

    # excluded: G[2](2)
    G2_3toX = [4245696, 251596800, 5859000000, 664376138496, 4329310519296, 22594320403200, 376611192619200, 3914077489672896, 71776114783027200, 167795197370551296, 796793353927300800, 11570921621943780096]
    _verify_list(aExceptionalChevalleyGroups_G2, G2_3toX, q=3)



class ClassicalSteinbergGroups__2An(IEvalOrderOfFiniteSimpleGroup__div_gcd__n_q):
    '''
        * _2A[n](q^2) if [n >= 2]
            order_2A q 2 n = q^(n*(n+1)/2)/gcd(n+1,q+1) * II q^(i+1) - (-1)^(i+1) {i <- [1..n]}
            exclusions: _2A[2](2^2)
    '''

    excluded_argument_dicts = ({'n':2, 'q':2},)
    family_long_name = 'ClassicalSteinbergGroups__2An'
    family_short_name = '_2An'
    group_name_template = '_2A[{n}]({q}^2)'
    min_argument_dict = {'n':2, 'q':2}
    min_n = 2

    @override
    def __eval_order_ex__(self, *, n, q):
        # :: UInt^k -> (Fraction, UInt)
        # order_2A q 2 n = q^(n*(n+1)/2)/gcd(n+1,q+1) * II q^(i+1) - (-1)^(i+1) {i <- [1..n]}
        N = q**(n*(n+1)//2) * II(q**(i+1) - (-1)**(i+1) for i in range(1, n+1))
        L = n+1
        R = q+1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aClassicalSteinbergGroups__2An = ClassicalSteinbergGroups__2An()

    # excluded: _2A[2](2^2)
    _2An_ls = [6048, 25920, 62400, 126000, 3265920, 5515776, 5663616, 13685760, 42573600, 70915680, 811273008, 1018368000, 2317678272, 4279234560, 9196830720, 14742000000, 16938986400, 26056457856]
    _verify_list(aClassicalSteinbergGroups__2An, _2An_ls, n=2, q=3)





class ClassicalSteinbergGroups__2Dn(IEvalOrderOfFiniteSimpleGroup__div_gcd__n_q):
    '''
        * _2D[n](q^2) if [n >= 4]
            order_2D q 2 n = q^(n*(n-1)) * (q^n + 1)/gcd(4,q^n + 1) * II q^(2*i) - 1 {i <- [1..n-1]}
            # NOTE: [1..n-1] not [1..n]
    '''

    excluded_argument_dicts = ()
    family_long_name = 'ClassicalSteinbergGroups__2Dn'
    family_short_name = '_2Dn'
    group_name_template = '_2D[{n}]({q}^2)'
    min_argument_dict = {'n':4, 'q':2}
    min_n = 4

    @override
    def __eval_order_ex__(self, *, n, q):
        # :: UInt^k -> (Fraction, UInt)
        # order_2D q 2 n = q^(n*(n-1)) * (q^n + 1)/gcd(4,q^n + 1) * II q^(2*i) - 1 {i <- [1..n-1]}
        #   NOTE: [1..n-1] not [1..n]
        N = q**(n*(n-1)) * (q**n + 1) * II(q**(2*i) - 1 for i in range(1, (n-1)+1))
        L = 4
        R = q**n + 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aClassicalSteinbergGroups__2Dn = ClassicalSteinbergGroups__2Dn()

    _2Dn_ls = [197406720, 10151968619520, 25015379558400]
    _verify_list(aClassicalSteinbergGroups__2Dn, _2Dn_ls, n=4,q=2)



class ExceptionalSteinbergGroups__2E6(IEvalOrderOfFiniteSimpleGroup__div_gcd__q):
    '''
        * _2E[6](q^2)
            order_2E6 q 2 = q^36 /gcd(3,q+1) * II q^i - (-1)^i {i <- [2,5,6,8,9,12]}
    '''

    excluded_argument_dicts = ()
    family_long_name = 'ExceptionalSteinbergGroups__2E6'
    family_short_name = '_2E6'
    group_name_template = '_2E[6]({q}^2)'
    min_argument_dict = {'q':2}

    @override
    def __eval_order_ex__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # order_2E6 q 2 = q^36 /gcd(3,q+1) * II q^i - (-1)^i {i <- [2,5,6,8,9,12]}
        N = q**36 * II(q**i - (-1)**i for i in [2,5,6,8,9,12])
        L = 3
        R = q+1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aExceptionalSteinbergGroups__2E6 = ExceptionalSteinbergGroups__2E6()

    # A008916 Order of simple twisted Chevalley group 2_E_6 (q), q = prime power.
    #   [76532479683774853939200, 14636855916969695633965120680532377600, 85696576147617709485896772387584983695360000000, 1059060039628243201724264144897460937500000000000000000]
    #
    _2E6_ls = [76532479683774853939200, 14636855916969695633965120680532377600, 85696576147617709485896772387584983695360000000, 1059060039628243201724264144897460937500000000000000000]
    _verify_list(aExceptionalSteinbergGroups__2E6, _2E6_ls, q=2)




class ExceptionalSteinbergGroups__3D4(IEvalOrderOfFiniteSimpleGroup__div_gcd__q):
    '''
        * _3D[4](q^3)
            order_3D4 q 3 = q^12*(q^8 + q^4 + 1)(q^6 − 1)(q^2 − 1)
    '''

    excluded_argument_dicts = ()
    family_long_name = 'ExceptionalSteinbergGroups__3D4'
    family_short_name = '_3D4'
    group_name_template = '_3D[4]({q}^3)'
    min_argument_dict = {'q':2}

    @override
    def __eval_order_ex__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # order_3D4 q 3 = q^12*(q^8 + q^4 + 1)(q^6 − 1)(q^2 − 1)
        N = q**12*(q**8 + q**4 + 1)*(q**6 - 1)*(q**2 - 1)
        L = 1
        R = 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aExceptionalSteinbergGroups__3D4 = ExceptionalSteinbergGroups__3D4()

    _3D4_ls = [211341312, 20560831566912, 67802350642790400, 35817806390625000000, 450782974156649555296512, 19045158721552047314829312, 516964372056378442547769600, 143027806714329275383382337600]
    _verify_list(aExceptionalSteinbergGroups__3D4, _3D4_ls, q=2)














class IEvalOrderOfFiniteSimpleGroup__div_gcd__m(IEvalOrderOfFiniteSimpleGroup__div_gcd):
    '''
    parameter_names = ('m',)
    parameter_names__should_known_upper_bound = ()
    min_argument_dict = {'m':1} # m >= 1
    '''

    parameter_names = ('m',)
    parameter_names__should_known_upper_bound = ()
    min_argument_dict = {'m':1}

    @abstractmethod
    def the_p_for_q():pass
    @abstractmethod
    def __eval_order_ex_by_q__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        raise NotImplementedError


    @override
    def __eval_order_ex__(self, *, m):
        # :: UInt^k -> (Fraction, UInt)
        p = self.the_p_for_q
        q = p**(2*m+1)
        return type(self).__eval_order_ex_by_q__(self, q=q)

    @override
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        if parameter_name != 'm': raise NameError
        return itertools.count(1)



    @override
    def list_values_of_named_parameter_lt(self, parameter_name, *, argument_value_upper_bound):
        # get_parameter_names__should_known_upper_bound
        raise logic-error
    @override
    def iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names__should_known_upper_bound
        raise logic-error




class SuzukiGroups__2B2(IEvalOrderOfFiniteSimpleGroup__div_gcd__m):
    '''
        * _2B[2](q) if [q == 2^(2*n+1)][n>=1]
            order_2B2 q = q^2*(q^2 + 1)(q − 1)
    '''

    the_p_for_q = 2
    excluded_argument_dicts = ()
    family_long_name = 'SuzukiGroups__2B2'
    family_short_name = '_2B2'
    #group_name_template = '_2B[2]({q})' # not ({q}^2) !!!!!
    group_name_template = '_2B[2](2^(2*{m}+1))' # not ({q}^2) !!!!!
    @override
    def __eval_order_ex_by_q__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # order_2B2 q = q^2*(q^2 + 1)(q − 1)
        N = q**2*(q**2 + 1)*(q - 1)
        L = 1
        R = 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aSuzukiGroups__2B2 = SuzukiGroups__2B2()

    # A064487 Order of twisted Suzuki group Sz(2^(2*n + 1)), also known as the group 2B2(2^(2*n + 1)).
    # A064487 has a bug: starts with 20@m=0, where m should >= 1
    #   [20, 29120, 32537600, 34093383680, 35115786567680, 36011213418659840, 36888985097480437760, 37777778976635853209600, 38685331082014736871587840, 39614005699412557795646504960, 40564799864499450381466515537920]
    _2B2_ls = [29120, 32537600, 34093383680, 35115786567680, 36011213418659840, 36888985097480437760, 37777778976635853209600, 38685331082014736871587840, 39614005699412557795646504960, 40564799864499450381466515537920]
    _verify_list(aSuzukiGroups__2B2, _2B2_ls, m=1)



class ReeGroups__2F4(IEvalOrderOfFiniteSimpleGroup__div_gcd__m):
    '''
        * _2F[4](q) if [q == 2^(2*n+1)][n>=1]
            order_2F4 q = q^12*(q^6 + 1)(q^4 − 1)(q^3 + 1)(q − 1)
    '''

    the_p_for_q = 2
    excluded_argument_dicts = ()
    family_long_name = 'ReeGroups__2F4'
    family_short_name = '_2F4'
    #group_name_template = '_2F[4]({q})' # not ({q}^2) !!!!!
    group_name_template = '_2F[4](2^(2*{m}+1))' # not ({q}^2) !!!!!
    @override
    def __eval_order_ex_by_q__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # order_2F4 q = q^12*(q^6 + 1)(q^4 − 1)(q^3 + 1)(q − 1)
        N = q**12*(q**6 + 1)*(q**4 - 1)*(q**3 + 1)*(q - 1)
        L = 1
        R = 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aReeGroups__2F4 = ReeGroups__2F4()

    # A064586 Order of twisted group 2F4(2^(2*n + 1)).
    # A064586 has a bug: starts with 35942400@m=0, where m should >= 1
    #   [35942400, 264905352699586176614400, 1318633155799591447702161609782722560000, 6082094555322622967641341883296948240189833427183206400, 27553065698713340677402960424984119640445544581637086693954488264294400, 124270100714024486336082151164778648282667807904331482703587621226371097161732037017600]
    #
    _2F4_ls = [264905352699586176614400, 1318633155799591447702161609782722560000, 6082094555322622967641341883296948240189833427183206400, 27553065698713340677402960424984119640445544581637086693954488264294400, 124270100714024486336082151164778648282667807904331482703587621226371097161732037017600]
    _verify_list(aReeGroups__2F4, _2F4_ls, m=1)




class ReeGroups__2G2(IEvalOrderOfFiniteSimpleGroup__div_gcd__m):
    '''
        * _2G[2](q) if [q == 3^(2*n+1)][n>=1]
            order_2G2 q = q^3*(q^3 + 1)(q − 1)
            NOTE: "q=3^?" not "q=2^?"
    '''

    the_p_for_q = 3
    excluded_argument_dicts = ()
    family_long_name = 'ReeGroups__2G2'
    family_short_name = '_2G2'
    #group_name_template = '_2G[2]({q})' # not ({q}^2) !!!!!
    group_name_template = '_2G[2](2^(2*{m}+1))' # not ({q}^2) !!!!!
    @override
    def __eval_order_ex_by_q__(self, *, q):
        # :: UInt^k -> (Fraction, UInt)
        # order_2G2 q = q^3*(q^3 + 1)(q − 1)
        N = q**3*(q**3 + 1)*(q - 1)
        L = 1
        R = 1
        return self.eval_order_ex__div_gcd(numerator=N, gcd_left=L, gcd_right=R)


if __name__ == '__main__':
    aReeGroups__2G2 = ReeGroups__2G2()

    # A064584 Order of twisted group 2G2(3^(2*n + 1)).
    # A064584 has a bug: starts with 1512@m=0, where m should >= 1
    #   [1512, 10073444472, 49825657439340552, 239189910264352349332632, 1144503123693984541835958820392, 5474370186265837734230137135972625592, 26183874281059869023477124043633901590825032, 125236728809915185354190019796969393286848248539352, 599003428666412716882958241970105468686115269921659258472]

    _2G2_ls = [10073444472, 49825657439340552, 239189910264352349332632, 1144503123693984541835958820392, 5474370186265837734230137135972625592, 26183874281059869023477124043633901590825032, 125236728809915185354190019796969393286848248539352, 599003428666412716882958241970105468686115269921659258472]
    _verify_list(aReeGroups__2G2, _2G2_ls, m=1)




######################################################
"""
class IEvalOrderOfSingletonGroup(IEvalOrderOfFiniteSimpleGroup):
    __slots__ = ()

    @abstractmethod
    def family_long_name():pass
    @abstractmethod
    def family_short_name():pass
    @abstractmethod
    def the_group_order():pass


    def get_the_group_order(self):
        return self.the_group_order

    @override
    def get_family_long_name(self):
        return self.family_long_name
    @override
    def get_family_short_name(self):
        return self.family_short_name
    @override
    def get_group_name_template(self):
        return self.family_short_name

    @override
    def get_maybe_min_order(self):
        # -> UInt
        return self.get_the_group_order()
    @override
    def __eval_order_ex__(self):
        #:: UInt^k -> UInt
        return self.get_the_group_order()

    @override
    def does_exclude_argument_dict(self, **argument_dict):
        return False
    @override
    def get_parameter_names(self):
        # -> [str]
        return ()
    @override
    def get_parameter_names__should_known_upper_bound(self):
        # -> [str]
        # return subset of .get_parameter_names()
        return ()
    @override
    def eval_maybe_min_argument_dict(self):
        return {}

    @override
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        raise logic-error
    @override
    def list_values_of_named_parameter_lt(self, parameter_name, *, argument_value_upper_bound):
        # get_parameter_names__should_known_upper_bound
        raise logic-error
    @override
    def iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names__should_known_upper_bound
        raise logic-error

class Monster(IEvalOrderOfSingletonGroup):
    '''
    Monster group
        M = 808017424794512875886459904961710757005754368000000000
    '''
    family_long_name = 'Monster_group'
    family_short_name = 'M'
    the_group_order = 808017424794512875886459904961710757005754368000000000
if __name__ == '__main__':
    aMonster = Monster()
    LAST = 808017424794512875886459904961710757005754368000000000
    assert _list_lt(aMonster, LAST) == []
    assert _list_lt(aMonster, LAST+1) == [LAST]
"""
######################################################





class EvalOrderOfSingletonGroup(IEvalOrderOfFiniteSimpleGroup):
    def __init__(self, *
        ,family_long_name
        ,family_short_name
        ,the_group_order
        ):
        self.family_long_name = family_long_name
        self.family_short_name = family_short_name
        self.the_group_order = the_group_order

    @override
    def get_family_long_name(self):
        return self.family_long_name
    @override
    def get_family_short_name(self):
        return self.family_short_name
    @override
    def get_group_name_template(self):
        return self.family_short_name

    @override
    def get_maybe_min_order(self):
        # -> UInt
        return self.the_group_order
    @override
    def __eval_order_ex__(self): # no kwargs
        # like __eval_ex__
        # :: UInt^k -> (UInt|((UInt|Fraction|...), UInt))
        return self.the_group_order

    #############################

    @override
    def eval_maybe_min_argument_dict(self):
        return {}
    @override
    def does_exclude_argument_dict(self):
        # -> Bool
        return False
    @override
    def get_parameter_names(self):
        # -> [str]
        return ()
    @override
    def get_parameter_names__should_known_upper_bound(self):
        # -> [str]
        # return subset of .get_parameter_names()
        return ()

    @override
    def iter_values_of_free_named_parameter(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names - get_parameter_names__should_known_upper_bound
        raise logic-error
    @override
    def list_values_of_named_parameter_lt(self, parameter_name, *, argument_value_upper_bound):
        # get_parameter_names__should_known_upper_bound
        raise logic-error
    @override
    def iter_partial_illegal_values_of_named_parameter__but_legal_used_in_eval(self, parameter_name):
        # :: parameter_name -> Iter UInt # increasing
        # get_parameter_names__should_known_upper_bound
        raise logic-error




if __name__ == '__main__':
    aMonster = EvalOrderOfSingletonGroup(
        family_long_name='Monster'
        ,family_short_name='M'
        ,the_group_order=808017424794512875886459904961710757005754368000000000
        )

    LAST = aMonster.the_group_order
    assert _list_lt(aMonster, LAST) == []
    assert _list_lt(aMonster, LAST+1) == [LAST]








family_short_name2aEval = {}
def _add(family_long_name, family_short_name, the_group_order):
    aEval = EvalOrderOfSingletonGroup(
        family_long_name=family_long_name
        ,family_short_name=family_short_name
        ,the_group_order=the_group_order
        )
    assert family_short_name not in family_short_name2aEval
    family_short_name2aEval[family_short_name] = aEval

'''
    * _2F[4](2)' # Tits group
        order_2F4_2_ = 2^12*(2^6 + 1)(2^4 − 1)(2^3 + 1)(2 − 1)/2 = 17971200

Mathieu groups
    M11 = 7920
    M12 = 95040
    M22 = 443520
    M23 = 10200960
    M24 = 244823040
Janko groups
    J1 = 175560
    J2 = 604800
    J3 = 50232960
    J4 = 86775571046077562880
Conway groups
    Co3 = 495766656000
    Co2 = 42305421312000
    Co1 = 4157776806543360000
Fischer groups
    Fi22 = 64561751654400
    Fi23 = 4089470473293004800
    Fi24' = 1255205709190661721292800
Higman-Sims group
    HS = 44352000
McLaughlin group
    McL = 898128000
Held group
    He = 4030387200
Rudvalis group
    Ru = 145926144000
Suzuki sporadic group
    Suz = 448345497600
O'Nan group
    O'N = 460815505920
Harada-Norton group
    HN = 273030912000000
Lyons group
    Ly = 51765179004000000
Thompson group
    Th = 90745943887872000
Baby Monster group
    B = 4154781481226426191177580544000000
Monster group
    M = 808017424794512875886459904961710757005754368000000000
'''

_add('Tits',"_2F[4](2)'", 17971200)

_add('Mathieu','M11', 7920)
_add('Mathieu','M12', 95040)
_add('Mathieu','M22', 443520)
_add('Mathieu','M23', 10200960)
_add('Mathieu','M24', 244823040)

_add('Janko','J1', 175560)
_add('Janko','J2', 604800)
_add('Janko','J3', 50232960)
_add('Janko','J4', 86775571046077562880)

_add('Conway','Co1', 495766656000)
_add('Conway','Co2', 42305421312000)
_add('Conway','Co3', 4157776806543360000)

_add('Fischer','Fi22', 64561751654400)
_add('Fischer','Fi23', 4089470473293004800)
_add('Fischer',"Fi24'", 1255205709190661721292800)

_add('HigmanSims','HS', 44352000)
_add('McLaughlin','McL', 898128000)
_add('Held','He', 4030387200)

_add('Rudvalis','Ru', 145926144000)
_add('SuzukiSporadic','Suz', 448345497600)
_add('O_Nan',"O'N", 460815505920)
_add('HaradaNorton','HN', 273030912000000)

_add('Lyons','Ly', 51765179004000000)
_add('Thompson','Th', 90745943887872000)
_add('BabyMonster','B', 4154781481226426191177580544000000)
_add('Monster','M', 808017424794512875886459904961710757005754368000000000)
del _add
assert len(family_short_name2aEval) == 27

def _test_family_long_name2aEval():
    assert len(family_short_name2aEval) == 27
    assert len({aEval.the_group_order for aEval in family_short_name2aEval.values()}) == 27

    for aEval in family_short_name2aEval.values():
        LAST = aEval.the_group_order
        assert _list_lt(aEval, LAST) == []
        assert _list_lt(aEval, LAST+1) == [LAST]
_test_family_long_name2aEval()


all_18_Eval_family_classes = (
    Cyclic
    ,Alternating
    ,ClassicalChevalleyGroups_An
    ,ClassicalChevalleyGroups_Bn
    ,ClassicalChevalleyGroups_Cn
    ,ClassicalChevalleyGroups_Dn
    ,ExceptionalChevalleyGroups_E6
    ,ExceptionalChevalleyGroups_E7
    ,ExceptionalChevalleyGroups_E8
    ,ExceptionalChevalleyGroups_F4
    ,ExceptionalChevalleyGroups_G2
    ,ClassicalSteinbergGroups__2An
    ,ClassicalSteinbergGroups__2Dn
    ,ExceptionalSteinbergGroups__2E6
    ,ExceptionalSteinbergGroups__3D4
    ,SuzukiGroups__2B2
    ,ReeGroups__2F4
    ,ReeGroups__2G2
    )
assert len(all_18_Eval_family_classes) == 18 == len(set(all_18_Eval_family_classes))

all_18_Eval_family_instances = tuple(
    Eval() for Eval in all_18_Eval_family_classes
    )
assert len(all_18_Eval_family_instances) == 18

all_45_Eval_instances = all_18_Eval_family_instances + tuple(family_short_name2aEval.values())
assert len(all_45_Eval_instances) == 18 + 1+26 == 45

if True:
    family_short_name2family_long_name = {
        aEval.get_family_short_name(): aEval.get_family_long_name()
        for aEval in all_45_Eval_instances
        }
    family_short_name2family_long_name = MappingProxyType(family_short_name2family_long_name)
    all_family_short_names = frozenset(family_short_name2family_long_name)
    all_family_long_names = frozenset(family_short_name2family_long_name.values())
    assert len(family_short_name2family_long_name) == 45
    assert len(all_family_short_names) == 45
    assert len(all_family_long_names) == 45 -(5-1)-(4-1)-(3-1)-(3-1) == 34

    def family_long_names2family_short_names(family_long_names):
        family_long_names = set(family_long_names)
        return {
            family_short_name
            for family_short_name, family_long_name
            in family_short_name2family_long_name.items()
            if family_long_name in family_long_names
            }

    def make_family_short_names_from2(*, family_short_names, family_long_names):
        family_long_names = set(family_long_names)
        family_short_names = set(family_short_names)
        if not family_long_names <= all_family_long_names:
            raise ValueError(family_long_names-all_family_long_names)
        if not family_short_names <= all_family_short_names:
            raise ValueError(family_short_names-all_family_short_names)

        family_short_names |= family_long_names2family_short_names(family_long_names)
        return family_short_names

    def make_family_short_names_from4(*
        ,excluded_family_short_names#=()
        ,excluded_family_long_names#=()
        ,maybe_included_family_short_names# = None
        ,maybe_included_family_long_names# = None
        ):
        #included_family_short_names
        if maybe_included_family_long_names is None is maybe_included_family_short_names:
            included_family_short_names = all_family_short_names
        else:
            if maybe_included_family_long_names is None:
                maybe_included_family_long_names = ()
            ##
            if maybe_included_family_short_names is None:
                maybe_included_family_short_names = ()

            included_family_short_names = make_family_short_names_from2(
                family_long_names=maybe_included_family_long_names
                ,family_short_names=maybe_included_family_short_names
                )
        included_family_short_names

        excluded_family_short_names = make_family_short_names_from2(
                family_long_names=excluded_family_long_names
                ,family_short_names=excluded_family_short_names
                )

        included_family_short_names -= excluded_family_short_names
        return included_family_short_names



    family_short_name2family_long_name
    all_family_short_names
    all_family_long_names
    family_long_names2family_short_names
    make_family_short_names_from2
    make_family_short_names_from4

def list_all_orders_of_finite_simple_groups_lt__without_repetition(
    result_value_upper_bound, *
    ,with_cyclic:bool
    ,with_parameterized_names:bool=False
    ,excluded_family_short_names=()
    ,excluded_family_long_names=()
    ,maybe_included_family_short_names = None
    ,maybe_included_family_long_names = None
    ):
    '''
    :: UInt -> sorted[UInt]
    :: UInt -> sorted[(UInt, [(aEval, argument_dict)])]

input:
    result_value_upper_bound :: UInt
    with_cyclic :: Bool
        with or without orders of cyclic simple groups
    with_parameterized_names:
        order or (order, (aEval, argument_dict))
    excluded_family_short_names :: Iter family_short_name
    excluded_family_long_names :: Iter family_long_name
    maybe_included_family_short_names :: None | Iter family_short_name
    maybe_included_family_long_names :: None | Iter family_long_name
output:
    result :: sorted[UInt] if not with_parameterized_names else sorted[(UInt, aEval, argument_dict)]
'''
    with_cyclic = bool(with_cyclic)
    with_parameterized_names = bool(with_parameterized_names)
    excluded_family_short_names = frozenset(excluded_family_short_names)
    excluded_family_long_names = frozenset(excluded_family_long_names)
    assert excluded_family_short_names <= all_family_short_names
    assert excluded_family_long_names <= all_family_long_names


    included_family_short_names = make_family_short_names_from4(
        excluded_family_short_names=excluded_family_short_names
        ,excluded_family_long_names=excluded_family_long_names
        ,maybe_included_family_short_names = maybe_included_family_short_names
        ,maybe_included_family_long_names = maybe_included_family_long_names
        )

    def _iter_unordered_group_orders():
        for aEval in all_45_Eval_instances:
            if not with_cyclic and isinstance(aEval, Cyclic):
                continue
            if aEval.get_family_short_name() not in included_family_short_names:
                continue


            yield from __iter_either_output(
                aEval, result_value_upper_bound
                , with_parameterized_names=with_parameterized_names
                )

    it = _iter_unordered_group_orders()
    return __sort_and_merge_either_output(it
        , with_parameterized_names=with_parameterized_names)

def __iter_either_output(
    aEval, result_value_upper_bound, *, with_parameterized_names
    ):
    it = aEval.iter_unordered_result_values_lt__with_repetition(
        result_value_upper_bound=result_value_upper_bound
        ,with_argument_dict=with_parameterized_names
        )
    if not with_parameterized_names:
        yield from it
    else:
        for order, argument_dict in it:
            yield order, (aEval, argument_dict)

def __sort_and_merge_either_output(
    either_output, *, with_parameterized_names
    ):
    it = either_output
    if not with_parameterized_names:
        return sorted(set(it))
    else:
        fst = lambda pair:pair[0]
        ls = sorted(it, key=fst)
        output = []
        for order, it_pairs in itertools.groupby(ls, key=fst):
            parameterized_names = []
            for _order, parameterized_name in it_pairs:
                assert order == _order
                parameterized_names.append(parameterized_name)
            output.append((order, parameterized_names))
        return output



def _44_list_lt(result_value_upper_bound, *, with_parameterized_names=False):
    return list_all_orders_of_finite_simple_groups_lt__without_repetition(
        result_value_upper_bound
        ,with_cyclic=False
        ,with_parameterized_names=with_parameterized_names
        )
def _45_list_lt(result_value_upper_bound, *, with_parameterized_names=False):
    return list_all_orders_of_finite_simple_groups_lt__without_repetition(
        result_value_upper_bound
        ,with_cyclic=True
        ,with_parameterized_names=with_parameterized_names
        )

if __name__ == '__main__':
    # A001034 Orders of non-cyclic simple groups (without repetition).
    #   [60, 168, 360, 504, 660, 1092, 2448, 2520, 3420, 4080, 5616, 6048, 6072, 7800, 7920, 9828, 12180, 14880, 20160, 25308, 25920, 29120, 32736, 34440, 39732, 51888, 58800, 62400, 74412, 95040, 102660, 113460, 126000, 150348, 175560, 178920]
    A001034 = [60, 168, 360, 504, 660, 1092, 2448, 2520, 3420, 4080, 5616, 6048, 6072, 7800, 7920, 9828, 12180, 14880, 20160, 25308, 25920, 29120, 32736, 34440, 39732, 51888, 58800, 62400, 74412, 95040, 102660, 113460, 126000, 150348, 175560, 178920]
    finite_non_cylic_simple_group_orders = A001034

    LAST = finite_non_cylic_simple_group_orders[-1]
    assert _44_list_lt(LAST+1) == finite_non_cylic_simple_group_orders


if __name__ == '__main__':
    # A005180 Orders of simple groups.
    # A005180 has a bug: starts with 1
    #   [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 60, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 168, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241]
    A005180 = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 60, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 168, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241]
    finite_simple_group_orders = A005180[1:]

    LAST = finite_simple_group_orders[-1]
    assert _45_list_lt(LAST+1) == finite_simple_group_orders


def _inplace_mk_name__order_parameterized_names_pairs(pairs):
    for order, parameterized_names in pairs:
        L = len(parameterized_names)
        for i in range(L):
            try:
                aEval, argument_dict = parameterized_names[i]
            except:
                print(parameterized_names[i])
                raise
            fmt = aEval.get_group_name_template()
            name = fmt.format(**argument_dict)
            parameterized_names[i] = name
    return

if __name__ == '__main__':
    r = _45_list_lt(100, with_parameterized_names=True)
    _inplace_mk_name__order_parameterized_names_pairs(r)
    assert r == [(2, ['C[2]']), (3, ['C[3]']), (5, ['C[5]']), (7, ['C[7]']), (11, ['C[11]']), (13, ['C[13]']), (17, ['C[17]']), (19, ['C[19]']), (23, ['C[23]']), (29, ['C[29]']), (31, ['C[31]']), (37, ['C[37]']), (41, ['C[41]']), (43, ['C[43]']), (47, ['C[47]']), (53, ['C[53]']), (59, ['C[59]']), (60, ['Alt[5]', 'A[1](4)', 'A[1](5)']), (61, ['C[61]']), (67, ['C[67]']), (71, ['C[71]']), (73, ['C[73]']), (79, ['C[79]']), (83, ['C[83]']), (89, ['C[89]']), (97, ['C[97]'])]


    r = _44_list_lt(10000, with_parameterized_names=True)
    _inplace_mk_name__order_parameterized_names_pairs(r)
    assert r == [(60, ['Alt[5]', 'A[1](4)', 'A[1](5)']), (168, ['A[1](7)', 'A[2](2)']), (360, ['Alt[6]', 'A[1](9)']), (504, ['A[1](8)']), (660, ['A[1](11)']), (1092, ['A[1](13)']), (2448, ['A[1](17)']), (2520, ['Alt[7]']), (3420, ['A[1](19)']), (4080, ['A[1](16)']), (5616, ['A[2](3)']), (6048, ['_2A[2](3^2)']), (6072, ['A[1](23)']), (7800, ['A[1](25)']), (7920, ['M11']), (9828, ['A[1](27)'])]
    del r














class _Alternating__of_shared_order(Alternating):
    '''
        _Alternating__of_shared_order:
            Alt[n] if n == 8

            A[8] = A[3](2)
            A[2](4)
    '''
    @override
    def does_exclude_argument_dict(self, *, n):
        return n != 8 or super().does_exclude_argument_dict(n=n)

class _ClassicalChevalleyGroups_An__of_shared_order(ClassicalChevalleyGroups_An):
    '''
    ClassicalChevalleyGroups_An:
        * A[n](q) if [n >= 1]
            exclusions: A[1](2), A[1](3)
    _ClassicalChevalleyGroups_An__of_shared_order:
        * A[n](q) if [(n,q) in [(3,2), (2,4)]]
            A[8] = A[3](2)
            A[2](4)
    '''
    @override
    def does_exclude_argument_dict(self, *, n, q):
        return (n,q) not in ((3,2), (2,4)) or super().does_exclude_argument_dict(n=n,q=q)

class _ClassicalChevalleyGroups_Cn__of_shared_order(ClassicalChevalleyGroups_Cn):
    '''
    ClassicalChevalleyGroups_Cn:
        * C[n](q) if [n >= 3]
    _ClassicalChevalleyGroups_Cn__of_shared_order:
        * C[n](q) if [odd q][n >= 3]
    '''

    @override
    def does_exclude_argument_dict(self, *, n, q):
        return (not (q&1)) or super().does_exclude_argument_dict(n=n,q=q)
class _ClassicalChevalleyGroups_Bn__of_shared_order(ClassicalChevalleyGroups_Bn):
    '''
    ClassicalChevalleyGroups_Bn
        * B[n](q) if [n >= 2]
            exclusions: B[2](2)
    _ClassicalChevalleyGroups_Bn__of_shared_order:
        * B[n](q) if [odd q][n >= 3]
    '''
    @override
    def does_exclude_argument_dict(self, *, n, q):
        return (not (q&1)) or (not n >= 3) or super().does_exclude_argument_dict(n=n,q=q)

_the_Alternating__of_shared_order = _Alternating__of_shared_order()
_the_ClassicalChevalleyGroups_An__of_shared_order = _ClassicalChevalleyGroups_An__of_shared_order()
_the_ClassicalChevalleyGroups_Cn__of_shared_order = _ClassicalChevalleyGroups_Cn__of_shared_order()
_the_ClassicalChevalleyGroups_Bn__of_shared_order = _ClassicalChevalleyGroups_Bn__of_shared_order()

def list_all_shared_orders_of_finite_simple_groups_lt__without_repetition(
    result_value_upper_bound, *, with_parameterized_names:bool=False
    ):
    ''' :: UInt -> sorted[UInt]
order of which there are more than one finite simple groups
order of which there are 2 finite simple groups

* order = 20160:
    A[8] = A[3](2)
    A[2](4)
* [odd q][n >= 3]
    B[n](q)
    C[n](q)

input:
    result_value_upper_bound
    with_parameterized_names
        see: list_all_orders_of_finite_simple_groups_lt__without_repetition
'''
    order_of_Alt8 = 20160
    with_parameterized_names = bool(with_parameterized_names)

    def _iter_unordered_group_orders():
        ls = [] # [(aEval, result_value_upper_bound)]

        ####
        if order_of_Alt8 < result_value_upper_bound:
            aEval_Alt = _the_Alternating__of_shared_order
            aEval_An = _the_ClassicalChevalleyGroups_An__of_shared_order
            _result_value_upper_bound = order_of_Alt8+1
            ls += [(aEval_Alt, _result_value_upper_bound)
                  ,(aEval_An, _result_value_upper_bound)
                  ]
            del _result_value_upper_bound
        ####
        if True:
            aEval_Bn = _the_ClassicalChevalleyGroups_Bn__of_shared_order
            aEval_Cn = _the_ClassicalChevalleyGroups_Cn__of_shared_order
            ls += [(aEval_Bn, result_value_upper_bound)
                  ,(aEval_Cn, result_value_upper_bound)
                  ]

        for aEval, __result_value_upper_bound in ls:
            yield from __iter_either_output(
                aEval, __result_value_upper_bound
                , with_parameterized_names=with_parameterized_names
                )

    it = _iter_unordered_group_orders()
    return __sort_and_merge_either_output(it
        , with_parameterized_names=with_parameterized_names)

if __name__ == '__main__':
    # A119648 Orders for which there is more than one simple group.
    #   [20160, 4585351680, 228501000000000, 65784756654489600, 273457218604953600, 54025731402499584000, 3669292720793456064000, 122796979335906113871360, 6973279267500000000000000, 34426017123500213280276480]
    A119648 = [20160, 4585351680, 228501000000000, 65784756654489600, 273457218604953600, 54025731402499584000, 3669292720793456064000, 122796979335906113871360, 6973279267500000000000000, 34426017123500213280276480]
    shared_finite_simple_group_orders = A119648

    LAST = shared_finite_simple_group_orders[-1]
    ls = list_all_shared_orders_of_finite_simple_groups_lt__without_repetition(LAST+1)
    assert ls == shared_finite_simple_group_orders

    ################################
    ls = list_all_shared_orders_of_finite_simple_groups_lt__without_repetition(LAST+1, with_parameterized_names=True)
    _inplace_mk_name__order_parameterized_names_pairs(ls)
    assert ls == [(20160, ['Alt[8]', 'A[2](4)', 'A[3](2)']), (4585351680, ['B[3](3)', 'C[3](3)']), (228501000000000, ['B[3](5)', 'C[3](5)']), (65784756654489600, ['B[4](3)', 'C[4](3)']), (273457218604953600, ['B[3](7)', 'C[3](7)']), (54025731402499584000, ['B[3](9)', 'C[3](9)']), (3669292720793456064000, ['B[3](11)', 'C[3](11)']), (122796979335906113871360, ['B[3](13)', 'C[3](13)']), (6973279267500000000000000, ['B[4](5)', 'C[4](5)']), (34426017123500213280276480, ['B[3](17)', 'C[3](17)'])]










if __name__ == '__main__':
    if 0:
        list(map(print, globals()))

