
'''
used for probability

type FiniteDomain a = Set a
type VarName = String # e.g. "X", "S[0]", "S[1..t]"
data FiniteGVector v = FiniteGVector
            { domain :: Map VarName FiniteDomain ?a?
            , vector :: Map VarName ?a? -> v
            }


>>> d123 = FiniteDomain({1,2,3});
>>> truths = FiniteDomain({True, False});
>>> varD0 = 'D[0]';
>>> varT = 'T';
>>> vdomain = FiniteGVectorDomain({varD0:d123, varT:truths});
>>> def key2element(key):
...     var2value = dict(key)
...     d = var2value[varD0]
...     t = var2value[varT]
...     return -2*d if t else 7*d

>>> gv = FiniteGVector(vdomain, key2element);
>>> assert len(gv) == 6
>>> assert gv[gv.dict_as_key({varD0:2, varT:True})] == -4
>>>
>>>
>>> varD1 = 'D[1]';
>>> truths1 = FiniteDomain({True});
>>> vdomain1 = FiniteGVectorDomain({varD1:d123, varT:truths1});
>>> def key2element1(key):
...     var2value = dict(key)
...     d = var2value[varD1]
...     t = var2value[varT]
...     return 2*d if t else -7*d

>>> gv1 = FiniteGVector(vdomain1, key2element1);
>>> gv01 = FiniteGVector.joint(gv, gv1);
>>> assert len(gv01) == 3*1*3
>>> assert gv01[gv01.dict_as_key({varD0:2, varT:True, varD1:1})] == (-4,2)
>>> assert gv01({varD0:2, varD1:1}, T=True) == (-4,2)
'''

from itertools import chain, product
from functools import reduce
from operator import __mul__

class FiniteDomain:
    def __init__(self, iterable):
        self.__domain = frozenset(iterable)
    def __iter__(self):
        return iter(self.__domain)
    def __contains__(self, x):
        return x in self.__domain
    def __len__(self):
        return len(self.__domain)
    def as_set(self):
        return self.__domain

class FiniteGVectorDomain:
    def __init__(self, var2domain):
        var2domain = dict(var2domain)
        assert all(isinstance(domain, FiniteDomain) for domain in var2domain.values()), TypeError
        sorted_var_domain_pairs = sorted(var2domain.items())
        self.__var2domain = var2domain
        self.__sorted_var_domain_pairs = sorted_var_domain_pairs
    def vars(self):
        return set(self.__var2domain)
    def sorted_vars(self):
        return tuple(var for var, domain in self.__sorted_var_domain_pairs)
    def sorted_domains(self):
        return tuple(domain for var, domain in self.__sorted_var_domain_pairs)
    def is_subFiniteGVectorDomain(self, other):
        assert isinstance(other, __class__)
        self_var2domain = self.__var2domain
        other_var2domain = other.__var2domain
        return (self.vars() <= other.vars(var2domain)
            and all(domain.as_set() <= other_var2domain[var].as_set()
                    for var, domain in self_var2domain.items())
            )

    @classmethod
    def union_intersection(cls, *instances):
        # union vars; intersetion domain
        assert all(isinstance(instance, cls) for instance in instances)

        var2set = {}
        for instance in instances:
            for var, new_domain in instance.__var2domain.items():
                new_set = new_domain.as_set()
                if var not in var2set:
                    var2set[var] = new_set
                else:
                    var2set[var] &= new_set
        return cls((var, FiniteDomain(s)) for var, s in var2set.items())
    def __iter__(self):
        it = product(*self.sorted_domains())
        vars = self.sorted_vars()
        for values in it:
            yield tuple(zip(vars, values))
    def __len__(self):
        it = map(len, self.__var2domain.values())
        return reduce(__mul__, it, 1)
    def __contains__(self, key):
        return (type(key) is tuple and len(key) == len(self.__var2domain)
            and all(type(p) is tuple and len(p) == 2 for p in key)
            and tuple(var for var, _ in key) == self.sorted_vars()
            and all(value in domain for (_, value), (_, domain) in
                    zip(key, self.__sorted_var_domain_pairs))
            )
    pass


class FiniteGVector:
    def __init__(self, aFiniteGVectorDomain, key2element):
        assert callable(key2element)
        assert isinstance(aFiniteGVectorDomain, FiniteGVectorDomain)
        self.__domain = aFiniteGVectorDomain
        self.__key2element_f = key2element
        self.__key2element = {key:key2element(key) for key in aFiniteGVectorDomain}
    def map(self, f):
        return type(self)(self.__domain, lambda key: f(self[key]))
    def inplace_map(self, f):
        old_key2element = self.__key2element_f
        self.__key2element_f = lambda key: f(old_key2element(key))
        d = self.__key2element
        for key in d.keys():
            d[key] = f(d[key])

    def __len__(self):
        return len(self.__domain)
    def __contains__(self, key):
        return key in self.__domain
    def __getitem__(self, key):
        return self.__key2element[key]
        if key not in self: raise KeyError
        return self.__key2element_f(key)
    @staticmethod
    def dict_as_key(d):
        return tuple(sorted(d.items(), key=lambda p:p[0]))
    @classmethod
    def joint(cls, *instances):
        assert all(isinstance(instance, cls) for instance in instances)
        domains = tuple(instance.__domain for instance in instances)
        result_domain = FiniteGVectorDomain.union_intersection(*domains)
        def key2element(result_key):
            dict_result_key = dict(result_key)
            return tuple(get(instance, dict_result_key) for instance in instances)
        def get(instance, dict_result_key):
            domain = instance.__domain
            vars = domain.sorted_vars()
            key = tuple((var, dict_result_key[var]) for var in vars)
            return instance[key]
        return cls(result_domain, key2element)

    def __call__(self, *pairs_or_dict_ls, **kwargs):
        # like __getitem__
        for pairs_or_dict in pairs_or_dict_ls:
            kwargs.update(pairs_or_dict)
        key = self.dict_as_key(kwargs)
        return self[key]


def _test():
    d123 = FiniteDomain({1,2,3});
    assert len(d123) == 3
    assert set(d123) == {1,2,3}

    truths = FiniteDomain({True, False});
    assert len(truths) == 2
    assert set(truths) == {True, False}

    varD0 = 'D[0]';
    varT = 'T';
    vdomain = FiniteGVectorDomain({varD0:d123, varT:truths});
    assert len(vdomain) == 6

    def key2element(key):
        var2value = dict(key)
        d = var2value[varD0]
        t = var2value[varT]
        return -2*d if t else 7*d

    gv = FiniteGVector(vdomain, key2element);
    assert len(gv) == 6
    assert gv[gv.dict_as_key({varD0:2, varT:True})] == -4

    varD1 = 'D[1]';
    truths1 = FiniteDomain({True});
    vdomain1 = FiniteGVectorDomain({varD1:d123, varT:truths1});
    def key2element1(key):
        var2value = dict(key)
        d = var2value[varD1]
        t = var2value[varT]
        return 2*d if t else -7*d
    gv1 = FiniteGVector(vdomain1, key2element1);
    gv01 = FiniteGVector.joint(gv, gv1);
    assert len(gv01) == 3*1*3
    assert gv01({varD0:2, varD1:1}, T=True) == (-4,2)
_test()

if __name__ == "__main__":
    import doctest
    doctest.testmod()



