
'''
discrete ProbabilityDistribution

full joint distribution
a Bayesian network gives a complete representation of the full joint distribution

discrete and continuous variables
'''
__all__ = ''' '''.split()
from itertools import chain
from abc import ABCMeta, abstractmethod
from types import MappingProxyType
from collections.abc import Hashable
from seed.iters.product import py_product, iter_product
from seed.iters.direct_product import direct_product
from seed.iters.null_iter import null_iter
from seed.types.FixedLenSeq import FixedLenSeq

class IName(Hashable):pass
IName.register(str)
#IName.register(tuple)
def is_name(x):
    def this_func(x):
        if type(x) is tuple:
            return all(map(this_func, x))
        return isinstance(x, IName)
    return this_func(x)

class HashableEx(Hashable):
    @abstractmethod
    def get_hash_args(self):
        # return (__base_class__, *args)
        return (__class__,)
    def __eq__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.get_hash_args() == other.get_hash_args()
    def __ne__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return not (self == other)
    def __hash__(self):
        return hash(self.get_hash_args())
class IDomain(HashableEx):
    @abstractmethod
    def __contains__(self, x):pass
    def verify(self):return True
class ICompositeDomain(IDomain):
    @abstractmethod
    # return a tuple
    def __domains__(self): pass
    def __has_element_type__(self, x):
        return type(x) is tuple
    def __elem2values__(self, x):
        # iteratable # may or may not iterator
        # same length and order as __domains__
        assert self.__has_element_type__(x)
        # may not "x in self"
        return x
    def __values2elem__(self, iterable):
        t = tuple(iterable)
        assert self.__has_element_type__(t)
        # may not "t in self"
        return t

    @property
    def domains(self): return self.__domains__()
    @property
    def num_domains(self):
        return len(self.domains)
    def values2elem(self, iterable):
        t = tuple(iterable)
        if len(t) != self.num_domains: raise TypeError
        x = self.__values2elem__(t)
        assert x in self
        return x
    def elem2values(self, x):
        # return a tuple
        if x not in self: raise TypeError
        values = tuple(self.__elem2values__(x))
        if len(values) != self.num_domains: raise logic-error
        return values

    def __contains__(self, x):
        if not self.__has_element_type__(x): return False
        values = tuple(self.__elem2values__(x))
        domains = self.domains
        if len(values) != len(domains): return False
        return all((value in domain) for domain, value in zip(domains, values))
    def verify(self):
        return (type(self.domains) is tuple
            and all(domain.verify() for domain in self.domains)
            and super().verify()
            )

class IDiscreteDomain(IDomain):pass
class IFiniteDomain(IDiscreteDomain):
    @abstractmethod
    def __iter__(self):pass
    @abstractmethod
    def __len__(self):pass

    @abstractmethod
    # return self.domain.index(x)
    def to_index(self, x):pass

    @abstractmethod
    # __getitem__ = to_index^-1
    def __getitem__(self, i):pass


class ISmallFiniteDomain(IFiniteDomain):
    @abstractmethod
    # return a tuple
    def __domain_values__(self):pass
    @property
    def domain_values(self): return self.__domain_values__()
    def __iter__(self):pass
        return iter(self.domain_values)

    def __getitem__(self, i):
        return self.domain_values[i]
    def __len__(self):return len(self.domain_values)
    def verify(self):
        return (type(self.domain_values) is tuple
            and all(self.to_index(v) == i and self[i] == v
                    for i, v in enumerate(self.domain_value))
            and super().verify()
            )

class ICompositeDiscreteDomain(IDiscreteDomain, ICompositeDomain):pass
    def verify(self):
        return (all(isinstance(domain, IDiscreteDomain)
                    for domain in self.domains)
            and super().verify()
            )

class ICompositeFiniteDomain(IFiniteDomain, ICompositeDiscreteDomain):
    def verify(self):
        return (all(isinstance(domain, IFiniteDomain)
                    for domain in self.domains)
            and super().verify()
            )
    @property
    # return a tuple
    def domain_sizes(self):
        return tuple(len(d) for d in self.domains)
    def to_index(self, x):
        # big-endian
        values = self.elem2values(x)
        domains = self.domains
        assert len(values) != len(domains) # elem2values is not __elem2values__
        indices = [d.to_index(v) for d,v in zip(domains, values)]
        domain_sizes = [len(d) for d in domains]
        domain_sizes.reverse()
        domain_sizes.pop()
        weights = list(iter_product(1, domain_sizes)); del domain_sizes
        weights.reverse()
        assert len(weights) == len(domains)
        return sum(idx*weight for idx, weight in zip(indices, weights))
    def __len__(self):
        return py_product(self.domain_sizes)
    def __getitem__(self, i):
        L = len(self)
        if not (-L <= i < L): raise KeyError
        if i < 0: i += L
        assert 0 <= i < L
        domains = self.domains
        indices = []
        for size in reversed(self.domain_sizes):
            i, idx = divmod(i, size)
            indices.append(idx)
        assert i == 0
        indices.reverse()
        return self.values2elem(d[idx] for d,idx in zip(domains, indices))
    def __iter__(self):
        if len(self) == 0: return null_iter
        seqviews = direct_product_view(*(d.__iter__ for d in self.domains))
        return map(self.values2elem, seqviews)

class IVariable(HashableEx):
    @abstractmethod
    def __variable_name__(self):pass
    @abstractmethod
    def __variable_domain__(self):pass

    @property
    def name(self): return self.__variable_name__()
    @property
    def domain(self): return self.__variable_domain__()
    def verify(self):
        return (is_name(self.name)
            and isinstance(self.domain, IDomain)
            )
class ICompositeVariable(IVariable):
    @abstractmethod
    # return a tuple
    def __variables__(self):pass
    #def __variable_domain__(self): return ???
    def __variable_names__(self):
        # to be overrided
        return tuple(var.name for var in self.variables)


    def __variable_name__(self):
        return self.names
    @property
    def variables(self): return self.__variables__()
    @property
    # return a tuple
    def names(self):
        return self.__variable_names__()
    @property
    def domains(self):
        return self.domain.domains

    def verify(self):
        return (all(isinstance(var, IVariable) for var in self.variables)
            and all(isinstance(domain, IDomain) for domain in self.domains)
            and all(var.domain == domain
                    for var, domain in zip(self.variables, self.domains))
            and isinstance(self.domain, ICompositeDomain)
            and super().verify()
            )

class IDiscreteVariable(IVariable):
    def verify(self):
        return (isinstance(self.domain, IDiscreteDomain)
            and super().verify()
            )
class IFiniteVariable(IDiscreteVariable):
    def verify(self):
        return (isinstance(self.domain, IFiniteDomain)
            and super().verify()
            )
class ICompositeDiscreteVariable(IDiscreteVariable, ICompositeVariable): pass
    def verify(self):
        return (isinstance(self.domain, ICompositeDiscreteDomain)
            and super().verify()
            )
class ICompositeFiniteVariable(IFiniteVariable, ICompositeDiscreteVariable):
    def verify(self):
        return (isinstance(self.domain, ICompositeFiniteDomain)
            and super().verify()
            )
















def mkFiniteDomain(iterable):
    if isinstance(iterable, IFiniteDomain): return iterable
    return SmallFiniteDomain(iterable)
class CompositeFiniteDomain(ICompositeFiniteDomain):
    def __init__(self, domains):
        domains =  tuple(domains)
        if not all(isinstance(d, IFiniteDomain) for d in domains): raise TypeError
        self.__domains = domains
        self.__len = super().__len__()
        self.__domain_sizes = super().domain_sizes
    def __domains__(self):
        return self.__domains
    @property
    def domain_sizes(self):
        return self.__domain_sizes
    def __len__(self):
        return self.__len
    def get_hash_args(self):
        return (__class__, self.__domains)

class SmallFiniteDomain(ISmallFiniteDomain):
    def __init__(self, iterable):
        domain = tuple(iterable)
        self.__domain = domain
        #self.__domain_set = frozenset(domain)
        self.__domain_map = MappingProxyType(
            {value:idx for idx,value in enumerate(domain)})
        if len(domain) != len(self.__domain_map): raise ValueError
    def __domain_values__(self):
        return self.__domain
    def __contains__(self, x):
        return x in self.__domain_map
    def to_index(self, x):
        return self.__domain_map[x]
    def get_hash_args(self):
        return (__class__, self.__domain)














class Variable(IVariable):
    def __init__(self, name, domain):
        if not is_name(name): raise TypeError
        if not isinstance(domain, IDomain): raise TypeError
        self.__name = name
        self.__domain = domain
    def __variable_name__(self): return self.__name
    def __variable_domain__(self): return self.__domain
class FiniteVariable(Variable, IFiniteVariable):
    def __init__(self, name, domain):
        if not isinstance(domain, IFiniteDomain): raise TypeError
        super().__init__(name, domain)
    def get_hash_args(self):
        return (__class__, self.name, self.domain)
class CompositeFiniteVariable(FiniteVariable, ICompositeFiniteVariable):
    def __init__(self, variables):
        variables = tuple(variables)
        if not all(isinstance(var, FiniteVariable) for var in variables): raise TypeError
        self.__variables = variables
        # name = ICompositeFiniteVariable.name.__get__(self, type(self))
        name = tuple(var.name for var in variables)
        domain = CompositeFiniteDomain(var.domain for var in variables)
        super().__init__(name, domain)
    def __variables__(self):
        return self.__variables
    def __variable_names__(self):
        return self.name
    def get_hash_args(self):
        return (__class__, self.variables)

seed.iters.minmax import minmax
seed.iters.all_the_same import all_the_same_ex

class ColumnVectorList:
    def __init__(self, colomns):
        self.__colomns = FixedLenSeq(map(FixedLenSeq, colomns))
    @property
    def colomns(self): return self.colomns
all_the_same_ex
all_equal
class FixedSizeMatrix(ColumnVectorList):
    # FixedSizeMatrix
    #   allow num_rows unknown if no colomns
    @classmethod
    def from_colomns(cls, colomns, num_rows=None):
        return cls(colomns, num_rows=num_rows)
    @property
    def size_mayR_C(self):
        return (self.__may_num_rows, self.__num_colomns)
    def __init__(self, colomns, num_rows=None):
        super().__init__(colomns)
        sizes = map(len, self.colomns)
        if num_rows is None:
            may_size = all_the_same_ex(sizes)
            # may_size :: () | (None|int,)
            if not may_size: raise TypeError
            # may_size :: (None|int,)
            [may_size] = may_size
            # may_size :: (None|int)
        else:
            num_rows = type(num_rows).__index__(num_rows)
            assert type(num_rows) is int
            if not all_equal(num_rows, sizes): raise TypeError
            may_size = num_rows
            # may_size :: int
            # may_size :: (None|int)
        # may_size :: (None|int)
        self.__may_num_rows = may_size
        self.__num_colomns = len(self.colomns)
    def may_num_rows(self): return self.__may_num_rows
    def num_colomns(self): return self.__num_colomns

    def __setitem__(self, rc, value):
        if type(rc) is not tuple: raise TypeError
        r, c = rc
        if type(c) is tuple: raise TypeError
        if type(r) is tuple: raise TypeError
        def sliceR(colomn):
            return colomn.__getitem__(r)
        colomns = self.domains
        if type(c) is slice: raise TypeError
        if type(r) is slice: raise TypeError
        colomns[c][r] = value
    def __getitem__(self, rc):
        if type(rc) is not tuple: raise TypeError
        r, c = rc
        if type(c) is tuple: raise TypeError
        if type(r) is tuple: raise TypeError
        def sliceR(colomn):
            return colomn.__getitem__(r)
        colomns = self.domains
        if type(c) is slice:
            colomns = colomns.__getitem__(c)
            cs = map(sliceR, colomns)
            if type(r) is slice:
                return type(self).from_colomns(cs)
            return type(c).from_iterable(cs)
        else:
            colomn = colomns.__getitem__(c)
            return sliceR(colomn)


def almost_equal(a, b, e=1e-30):
    return abs(a,b) < e
MatrixView
class FiniteProbabilityDistribution:
    # finite probability distribution
    def __init__(self, domainR, domainC, rc2probability):
        if not isinstance(domainR, ICompositeFiniteDomain): raise TypeError
        if not isinstance(domainC, ICompositeFiniteDomain): raise TypeError
        if not isinstance(rc2probability, FixedSizeMatrix): raise TypeError
        if not (len(domainR) > 0 and len(domainC) > 0): raise TypeError
        if rc2probability.size_mayR_C != (len(domainR), len(domainC)): raise TypeError
        if not all(almost_equal(sum(colomn), 1) for colomn in rc2probability.colomns): raise TypeError


        self.domainR = domainR
        self.domainC = domainC
        self.rc2probability = MatrixView(rc2probability)

