
'''
generalize of: v*u = [a*b for a,b in zip(v,u)]

Artificial Intelligence -- A Modern Approach (3ed)(2010)(Stuart Russell)
[page 52] Section 14.4. Exact Inference in Bayesian Networks

class Hashable => Name name
class Hashable => Domain domain where
    type DType domain :: *
newtype FactoredDomain name domain = F (Map name domain)
instance (Name name, Domain domain) =>
    Domain (FactoredDomain name domain) where
    type DType domain = Map Name (DType domain)
newtype Vector domain value = V (Map domain value)

v .*. u | domain v == domain u =
    -- vector.from_pairs((key, v[key]*u[key]) for key in (domain v))
    mk_vector (domain v) (\key -> v[key]*u[key])
v .*. u | match_FactoredDomain(factored_domain v, factored_domain u) =
    to_name2domain = to_map . factored_domain
    common_sub_factored_domain = to_name2domain v /-\ to_name2domain u
    total_factored_domain = to_name2domain v \-/ to_name2domain u
    result_domain = to_factored_domain to_factored_domain
    u_keys = keySet (to_name2domain u)
    v_keys = keySet (to_name2domain v)
    v_not_u = v_keys \\ u_keys
    u_not_v = u_keys \\ v_keys
    mk_vector result_domain (\key -> v[key.remove_keys(u_not_v)]*u[key.remove_keys(v_not_u)])



'''

from seed.mapping_tools.dict_discards import dict_discards
from seed.mapping_tools.dict_match import dict_match
def pointwise(vector_ops, result_value_domain, element_binary_op, u, v):
    '''
vector_ops
    get_key_domain_ops(self) -> domain_ops
    key_domain_of(self, v) -> domain
    domain_key2value_to_vector(self, key_domain, value_domain
            , key2value_func:'key->value') -> vector
    get_value(self, v, key) -> vector_element
domain_ops
    domain_equal(self, domainL, domainR) -> bool
factored_domain_ops
    domain2dict(self, domain) -> {name:(ops, factor_domain)}
    dict2domain(self, name2ops_factor_domain) -> domain
    domain_value2dict(self, domain, domain_value) -> {name:factor_domain_value}
    domain_dict2value(self, domain, name2value) -> domain_value
'''
    ops = vector_ops
    key_domain_ops = ops.get_key_domain_ops()
    u_key_domain = ops.key_domain_of(u)
    v_key_domain = ops.key_domain_of(v)
    key2value = lambda key: element_binary_op(getu(u, key), getv(v, key))
    mk = lambda: ops.domain_key2value_to_vector(
                r_key_domain, result_value_domain, key2value)
    if key_domain_ops.domain_equal(u_key_domain, v_key_domain):
        r_key_domain = u_key_domain
        getu = getv = ops.get_value
        return mk()
    if not isinstance(key_domain_ops, IFactoredDomainOps):
        raise NotImplementedError

    # now, original vector keys are the direct product of the factored_domains
    u_name2ops_subdomain = key_domain_ops.domain2dict(u_key_domain)
    v_name2ops_subdomain = key_domain_ops.domain2dict(v_key_domain)
    # does match??
    u_names = set(u_name2ops_subdomain)
    v_names = set(v_name2ops_subdomain)
    uv_names = u_names & v_names
    '''
    ERROR!
    bug: key_domain_ops.domain_equal is error
    if not dict_match(u_name2domain, v_name2domain
            , common_keys=uv_names, value_eq = key_domain_ops.domain_equal):
        return NotImplementedError
    if not all(key_domain_ops.domain_equal
        (u_name2domain[name], v_name2domain[name]) for name in uv_names):
        return NotImplementedError
    '''
    def pair_eq(ops_sub_domainL, ops_sub_domainR):
        opsL, sub_domainL = ops_sub_domainL
        opsR, sub_domainR = ops_sub_domainR
        return opsL == opsR and opsL.domain_equal(sub_domainL, sub_domainR)
    if not all(pair_eq(u_name2ops_subdomain[name], v_name2ops_subdomain[name])
                    for name in uv_names):
        return NotImplementedError

    # matched

    # r_key_domain, get
    d = dict(u)
    d.update(v)
    r_key_domain = key_domain_ops.dict2domain(d)


    u_not_v_names = u_names - v_names
    v_not_u_names = v_names - u_names
    def getu(u, r_key):
        return getx(u, r_key, u_key_domain, v_not_u_names)
    def getv(v, r_key):
        return getx(v, r_key, v_key_domain, u_not_v_names)
    def getx(x_vector, r_key,  x_key_domain, y_not_x_names):
        # x is u/v vector, y is v/u vector
        # ops, key_domain_ops, r_key_domain
        r_key_domain_value = r_key
        r_key_name2value = key_domain_ops.domain_value2dict(
                            r_key_domain, r_key_domain_value)
        x_key_name2value = dict_discards(r_key_name2value, y_not_x_names)
        x_key_domain_value = key_domain_ops.domain_dict2value(
                            x_key_domain, x_key_name2value)
        x_key = x_key_domain_value
        return ops.get_value(x_vector, x_key)

    return mk()


class IOps:
    '''
    def __eq__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self is other
    def __ne__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return not (self == other)
    '''
    pass

class INameOps(IOps):
    # name should be hashable
    def is_element(self, x):pass
class IDomainOps(IOps):
    # ??????domain should be hashable??????
    def is_element(self, x):pass
    def domain_equal(self, x, y):pass
class IFiniteDomainOps(IDomainOps):
    def iter_values_of(self, d):pass
class IFactoredDomainOps(IDomainOps):
    def domain2dict(self, domain) -> '{name:(ops, factor_domain)}':pass
    def dict2domain(self, name2ops_factor_domain) -> 'domain':pass
    def domain_value2dict(self, domain, domain_value) -> '{name:factor_domain_value}':pass
    def domain_dict2value(self, domain, name2value) -> 'domain_value':pass
class IFactoredFiniteDomainOps(IFactoredDomainOps, IFiniteDomainOps):
    def domain2dict(self, domain) -> '{name:factor_finite_domain}':pass

class IVectorOps(IOps):
    def get_key_domain_ops(self) -> 'domain_ops': pass
    def key_domain_of(self, v) -> 'domain': pass

    def get_key_domain_ops(self) -> 'domain_ops': pass
    def value_domain_of(self, v) -> 'domain': pass

    def domain_key2value_to_vector(self, key_domain, value_domain
            , key2value_func:'key->value') -> 'vector': pass
    def get_value(self, v, key) -> 'vector_element': pass
class IFiniteVectorOps(IOps):
    def get_key_domain_ops(self) -> 'finite_domain_ops': pass
    # value_domain need not be finite

class StrAsNameOps(INameOps):
    def is_element(self, x): return type(x) is str


'''
class IVariableOps:
    # variable,name,domain should be hashable
    def is_element(self, x):pass
    def name_of(self, x):pass
    def domain_of(self, x):pass
class IIndicesOps:
    # seq: has one index variable, and its domain is [0..len-1]
    def is_element(self, x):pass
    def variables_of(self, x):pass
    def names_of(self, x):pass
    def domains_of(self, x):pass

    def match(self, x, y):
        # x.name2domain(name) == y.name2domain(name) for name in (x.names/\y.names)
        pass


class IGeneralVectorOps:
    def is_vector(self, v):pass
    def is_key(self, key):pass
    def is_value(self, val):pass

    # indices
    def get_indices_ops(self):pass
    def indices_of(self, v):pass
    def match(self, v, u):
        ops = self.get_indices_ops()
        if ops.match(self.indices_of(v), self.indices_of(u)):
            v_names = set(self.names_of(v))
            u_names = set(self.names_of(u))
            return all(for name in v_names&u_names)
            if 

    # mapping
    def keys_of(self, v):pass
    def values_of(self, v):pass
    def items_of(self, v):pass
    def get_value(self, v, key):pass

    # multi indices
    def get_partial_vector(self, v, partial_key):pass
    # exclude the input key
    def partial_keys_of(self, v, partial_key):pass
    def partial_values_of(self, v, partial_key):pass
    def partial_items_of(self, v, partial_key):pass

    def key_domains_of(self, v):pass
    def 
'''



