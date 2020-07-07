"""
symmetric_poly2basic_expand


basic_symmetric_poly :: (n, m)
	n <- [0..]\_/{+oo}
	m :: uint
	symmetric_poly where
		all coeff==1
		[m==0]<==>[len(monomial)==0]
		[m==0]<==>[len(monomial)==1][exp==1][repeat==m]
symmetric_poly :: (n, {monomial:coeff})
	monomial :: {exp:repeat}
	exp :: pint
	repeat :: pint
	coeff != 0
	n <- [0..]\_/{+oo}
		- n variables

(<<) :: symmetric_poly -> [var] -> poly
	(symmetric_poly n monomial2coeff)<<xs =
		= sum
				let duplicated = product factorial(repeat) {repeat<-monomial.values()}
						sorted_monomial = sorted(monomial.items())
						sorted_exps =o [e|(exp,repeat)<-sorted_monomial, e<-[exp]*repeat]
				in  (coeff/duplicated)*sum
							pows(xs,idc,sorted_exps)
						{idc<-choice([0..n-1], sum(monomial.values()))}
			{(monomial,coeff)<-monomial2coeff.items()}
pows :: [var] -> [uint] -> [uint] -> monomial
pows(xs,idc,exps) = product xs[i]**e {(i,e)<-zip idc exps}


vmonomial :: [(exp,repeat)]
	vmonomial[i][0]>vmonomial[i+1][0]
	vmonomial = reversed(sorted(monomial.items()))
	vmonomial = monomial<vars>
bmonomial :: [(m,exp)]
	bmonomial[i][0]>bmonomial[i+1][0]
	bmonomial = monomial<basic_symmetric_polys>
symmetric_poly2basic_expand
	(n
			:[0..]\_/{+oo}
	,&cache<n>
			:{vmonomial:bpoly}
	,vpoly
	)->bpoly


partial_symmetric_poly2basic_expand
pvpoly2bpoly
	(n
			:[0..]\_/{+oo}
	,&cache<n>
			:{vmonomial:bpoly}
	,one
		:coeff
	,pvpoly
			:vmonomial2bp_coeff
	)->bpoly
			:bmonomial2coeff
	note:
			vmonomial2bp_coeff::{vmonomial:bp_coeff}
			bmonomial2coeff::{bmonomial:coeff}
			
			bp_coeff=bmonomial2coeff
			bpoly=bmonomial2coeff
			bp_coeff is middle coeff of vmonomial
			bpoly is final expanded result of vmonomial/vpoly/pvpoly
			
			pvpoly=vmonomial2bp_coeff
			vpoly=vmonomial2coeff
			pvpoly is middle expanded result of vmonomial/vpoly
			vpoly is poly<vars, coeff>
			bpoly is poly<bsymps, coeff>
			pvpoly is poly<vars, coeff[bsymps]>
			bsymp=basic_symmetric_poly
			
			vmonomial = monomial<vars>
			bmonomial = monomial<bsymps>


"""



from common_short_hand import *




#mapping_with_max_heap(__le__):
#	pop_max_item()->(k,v)


def mk_vmonomial(monomial):
	return tuple(reversed(sorted(monomial.items())))

class pvpoly2bpoly:
	"""
	vpoly2bpoly
	pvpoly2bpoly
	vmonomial2bpoly
	"""
	vmonomial_one = ()
	bmonomial_one = ()
	#pvpoly2bpoly(n, cache, one, zero)
	def __init__(sf
			, n, cache, one, zero, check):
			sf.cache = cache
			sf.zero = zero
			sf.one = one
			sf.n = inf if n is nnn else n
			assert sf.n >= 0
			sf.check = bool(check)
			
	
	def _check_dict_values(sf, d):
		if not sf.check: return
		if not all(d.values()): raise eee
	def _check_pairs(sf, lss):
		if not sf.check: return
		if not set(map(len, lss)) <= {2}: raise eee
	def _check_table_gt0(sf, lss):
		if not sf.check: return
		for ls in lss:
			for x in ls:
				if not x>0: raise eee
	def _check_fst_strict_gt(sf, lss):
		if not sf.check: return
		xs = map(fst, lss)
		ys = map(fst, lss[1:])
		for x,y in zip(xs,ys):
			if not x>y: raise eee
	def _check_vm_num(sf, vm):
		if not sf.check: return
		if num_vars_of(vm) > sf.n: raise eee
	def _check_m(sf, m):
		if not sf.check: return
		if not 1 <= m <= sf.n: raise eee
	def _check_bm_m(sf, bm):
		if not sf.check: return
		for m,e in bm:
			sf._check_m(m)
	def _check_bp(sf, bp):
		if not sf.check: return
		for bm in bp:
			sf._check_bm_m(bm)
		sf._check_bp_vp_pvp(bp)
	def _check_vp(sf, vp):
		if not sf.check: return
		for vm in vp:
			sf._check_vm_num(vm)
		sf._check_bp_vp_pvp(vp)
	def _check_bp_vp_pvp(sf, xp):
		if not sf.check: return
		for xm in xp:
			sf._check_fst_strict_gt(xm)
			sf._check_table_gt0(xm)
			sf._check_pairs(xm)
		sf._check_dict_values(xp)
	
	def _check_pvp(sf, pvp):
		if not sf.check: return
		for vm in pvp:
			sf._check_vm_num(vm)
		sf._check_bp_vp_pvp(pvp)
		for bp in pvp.values():
			sf._check_bp(bp)
	############
	def vpoly2pvpoly(sf, vpoly, fcoeff=id):
			sf._check_vp(vpoly)
			pvpoly = {vm:{sf.bmonomial_one:c_}
					for vm,c in vpoly.items()
					for c_ in [fcoeff(c)]
					if c_
					}
			sf._check_pvp(pvpoly)
			return pvpoly
	def vpoly2bpoly(sf, vpoly):
			#sf._check_vp(vpoly)
			return sf.pvpoly2bpoly(sf.vpoly2pvpoly(vpoly))
	def pvpoly2bpoly(sf, pvpoly):
		#(vmonomial2bp_coeff
		#)=pvpoly=dict(pvpoly)
		
		bp = sf._pvpoly2bpoly(pvpoly)
		#sf._check_bp(bp)
		return bp
	def _pvpoly2bpoly(sf, pvpoly):
		sf._check_pvp(pvpoly)
		f = sf.vmonomial2bpoly
		mul = sf.bpoly_mul
		iadd = sf._ill_bpoly_iadd
		bp0 = sf.mk_bpoly_zero()
		for vm,bc in pvpoly.items():
			assert bc
			bp = f(vm)
			assert bp
			pd = mul(bp, bc)
				#bugs: [pd={}]@[bp!={}!=bc]
			if 0:
				prx(1);
				pr(f"bp={bp}")
				pr(f"bc={bc}")
				pr(f"pd={pd}")
			assert pd
			iadd(bp0, pd)
		bp = filter_values(bp0)
		sf._check_bp(bp)
		return bp
	def vmonomial2bpoly(sf, vmonomial):
		may_bp = sf.cache.get(vmonomial)
		if may_bp is nnn:
			bp = sf._vmonomial2bpoly(vmonomial)
			sf.cache[vmonomial] = bp
		else:
			bp = may_bp
		return dict(bp)
	def _vmonomial2bpoly(sf, vmonomial):
		sf._check_vm_num(vmonomial)
		if not vmonomial:
			#1
			bp = sf.mk_bpoly_one()
		elif vmonomial[0][0]==1:
			#bsymp	
			[(_exp_eq_1, repeat)] = vmonomial
			m = repeat
			bp = sf.mk_bpoly__bsymp(m)
		else:
			k = num_vars_of(vmonomial)
			vmonomial1 = ((1,k),)
			bp1 = sf.mk_bpoly__bsymp(k)
			vmonomial0 = tpl((exp-1, rp)
								for exp,rp in vmonomial
								if exp>1
								)
			assert vmonomial0
			#vmonomial=vmonomial0*vmonomial1-...
			vpoly = sf.vmonomial_pmul(k, vmonomial0)
			
			assert vmonomial0 not in vpoly
			c = vpoly.pop(vmonomial)
			if c != sf.one:
				raise logic-error
			
			pvpoly = sf.vpoly2pvpoly(vpoly, opss.neg)
			assert vmonomial0 not in pvpoly
			pvpoly[vmonomial0] = bp1
			bp = sf._pvpoly2bpoly(pvpoly)
			if 0:
				prx(3)
				pr(f"vmonomial={vmonomial}")
				pr(f"vpoly={vpoly}")
				pr(f"pvpoly={pvpoly}")
				pr(f"bp={bp}")
		
		sf._check_bp(bp)
		assert bp # <<== "a" monomial
		return bp
	def bpoly_pmul(sf, c, bp):
		return {bm:c*c_ for bm,c_ in bp.items()}
	def bpoly_mul(sf, bp0, bp1):
		mul = sf.bmonomial_mul
		bp = defaultdict(lambda:sf.zero)
		#bug: for bm0,c0 in bp.items()
		for bm0,c0 in bp0.items():
			for bm1,c1 in bp1.items():
				bm = mul(bm0,bm1)
				c = c0*c1
				bp[bm] += c
				if 0:
					pr(f"bm0={bm0}")
					pr(f"bm1={bm1}")
					pr(f"bm={bm}")
		#bp = {bm:c for bm,c in bp.items() if c}
		bp = filter_values(bp)
		sf._check_bp(bp)
		
		if 0:
			pr(f"bp0={bp0}")
			pr(f"bp1={bp1}")
			pr(f"bp={bp}")
		assert bool(bp) is bool(bp0 and bp1)
		return bp
		
	def _ill_bpoly_iadd(sf, bp0, bp1):
		for bm,c in bp1.items():
			if bm in bp0:
				bp0[bm] += c
			else:
				bp0[bm] = c
		return
	def mk_bpoly_zero(sf):
		return {}
	def mk_bpoly_one(sf):
		return {sf.bmonomial_one:sf.one}
	def mk_bpoly__bsymp(sf, m):
		sf._check_m(m)
		return {((m,1),):sf.one}
	def bmonomial_mul(sf, bm0, bm1):
		d = defaultdict(int, bm0)
		for m,e in bm1:
			d[m] += e
		bm = (*reversed(sorted(d.items())),)
		assert max(len(bm0), len(bm1)) <= len(bm) <= len(bm0)+len(bm1)
		return bm
	def vmonomial_pmul(sf, m, vmonomial):
		#((1,m),)*vmonomial -> vpoly
		assert m>=0
		sf._check_m(m)
		sf._check_vm_num(vmonomial)
		vpoly = sf._vmonomial_pmul(sf.n, m, vmonomial)
		return vpoly
	def _vmonomial_pmul(sf, n, m, vmonomial):
		assert m <= n
		assert num_vars_of(vmonomial) <= n
		lhs = ((1,m),)
		rhs = vmonomial
		_1 = sf.one
		if m==0:
			#lhs=1; lhs is ill-form
			vpoly = {rhs:_1}
		elif not vmonomial:
			#rhs=1; now lhs is good
			vpoly = {lhs:_1}
		else:
			e,k = rhs[0]
			max_i = min(m, k)
			f = sf._vmonomial_pmul
			#vpoly = defaultdict(lambda:sf.zero)
			vpoly = {}
			_n = n-k # >= _m = m-i
				# i >= m-_n=m+k-n
			min_i = max(0, m - _n)
			assert 0 <= min_i <= max_i
			for i in rg(min_i, max_i+1):
				#may_at0 = (e+1, i) # if i!=0
				#may_at1 = (e, k-i) # if i!=k && f not ret a merge
				_m = m-i
				if _n < _m: raise logic-error
				_vpoly = f(_n, _m, rhs[1:])
				for vm,c in _vpoly.items():
					if not vm:
						#1*c; const
						if k!=i:
							vm = ((e,k-i), *vm)
					else:
						_e,_k = vm[0]
						assert _e <= e
						if _e==e:
							kk = k-i+_k
							vm = ((e,kk), *vm[1:])
							ct = choose(kk,_k)
							#pr(ct); assert ct
							c *= ct
						elif k!=i:
							vm = ((e,k-i), *vm)
					####
					if 1:
						##
						vm,c
						#pr(vm,c)
						if i:
							vm = ((e+1,i), *vm)
						##
						#vpoly[vm] += c
						assert vm not in vpoly
						vpoly[vm] = c
			###end for
			#vpoly = dict(vpoly)
		#pr(vpoly)
		return vpoly
	"""
	def (sf, ):
		return
	def (sf, ):
		return
	def (sf, ):
		return
	def (sf, ):
		return
	"""
	#pvpoly2bpoly(n, cache, one, zero)

if 1:
	def filter_values(d):
		return {k:v for k,v in d.items() if v}
	def skip_condition(n, vmonomial, coeff):
		return coeff==0 or num_vars_of(vmonomial)>n
	def num_vars_of(vmonomial):
		return sum(map(snd, vmonomial))
	vm2min_n = num_vars_of
	def vm2large_n(vm):
		return sum(e*rp for e,rp in vm)
	def vp2min_n(vp):
		return max(map(vm2min_n, vp)) if vp else 0
	def vp2large_n(vp):
		return max(map(vm2large_n, vp)) if vp else 0







#########################################
#########################################
#########################################

class g:
	using_sympy=ff
	#using_seed=tt
if 1 or g.using_seed:
	import seed
	#pr("seed")
	from seed.io.savefile.SaveFile import SaveFileDict
	dict_infile
	#g_sv = dict_infile.mk("sv.symmetric_poly2basic_expand.py.txt", dict(n="inf", gen="symmetric_poly2basic_expand.py"))
	"""
	encoding = 'u8'
	kwargs = {'a':b'', 0:[]}
	mk = lambda T, iofile, kwargs: T(iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs)
	iofile = io.StringIO()
	T = SaveFileDict
	C = mk(T, iofile, kwargs)
	g_cache = C
	"""
if g.using_sympy:
	from sympy import *
	dd = nnn
	#dd = QQ[I]
	#dd = CC
	mxx = Matrix
	sy0 = _0 = sympify(0)
	sy1 = _1 = sympify(1)
	
	def is_real(x):
		return im(x)==0

class sy_poly:
	#using_sympy
	def __init__(sf, gs):
		sf.gens = (*gs,)
		sf.n = len(sf.gens)
	def bp2spoly(sf, bp):
		p = sy0
		gs = sf.gens
		p = p.as_poly(*gs)
		for bm,c in bp.items():
			sp = sf.bm2spoly(bm)
			p += sp*c
		return p
	def bm2spoly(sf, bm):
		p = sy1
		gs = sf.gens
		p = p.as_poly(*gs)
		for m,e in bm:
			sp = sf.bm_m2spoly(m)
			p *= sp**e
		return p
	def bm_m2spoly(sf, m):
		assert m<=sf.n
		gs = sf.gens
		p = symmetric_poly(m, *gs)
		
		p = p.as_poly(*gs)
		return p
	def vp2spoly(sf, vp):
		if sf.n < vp2min_n(vp):raise eee
		p = sy0
		gs = sf.gens
		p = p.as_poly(*gs)
		for vm,c in vp.items():
			sp = sf.vm2spoly(vm)
			p += sp*c
		return p
	def vm2spoly(sf, vm):
		if sf.n < vm2min_n(vm):raise eee
		gs = sf.gens
		nv = num_vars_of(vm)
		es = []
		dup = 1
		for e,rp in vm:
			es += [e]*rp
			dup *= fff(rp)
		assert nv == len(es)
		p = sy0
		for xs in perm(gs, nv):
			assert nv == len(xs)
			xes = map(opss.pow, xs, es)
			p += fold(opss.mul, sy1, xes)
		
		p = p.as_poly(*gs)
		(dup_, p) = primitive(p)
		assert dup_ == dup
		return p



def vm_from_dict(d):
	return vm_from_pairs(d.items())
def vm_from_pairs(ps):
	ps = ((e,rp) for e,rp in ps)
	ps = reversed(sorted(ps))
	vm = (*ps,)
	return vm
def vm2vp(vm,one):
	return {vm:one}
def verify(vp, n, cache, one, zero, check):
	if n is nnn or (
		type(n) is str
		and n in ['oo', 'inf']
		):
		n = inf
	assert n >= vp2min_n(vp)
	if n == inf:
		n_ = vp2large_n(vp)
	else:
		n_ = n
	assert n_ >= vp2min_n(vp)
	

	if 0:
		zero=0#fr0
		one=1#fr1
		check=ff
		cache={}
	sf = pvpoly2bpoly(n, cache, one, zero, check)
	vm2bp = sf.vmonomial2bpoly
	vp2bp = sf.vpoly2bpoly
	pvp2bp = sf.pvpoly2bpoly
	
	bp = vp2bp(vp)
	######
	if 1:
		pr(f"n={n}")
		pr(f"n_={n_}")
		pr(f"len(vp)={len(vp)}")
		pr(f"vp={vp}")
		prx(2);
		pr(f"len(bp)={len(bp)}")
		pr(f"bp={bp}")
		if not g.using_sympy:
			pr("not verified")
		prx(4);
	######sympy; using n_
	if not g.using_sympy:
		return
	gs = symbols(f'a:{n_}')
	sf = sy_poly(gs)
	bp2sp = sf.bp2spoly
	vp2sp = sf.vp2spoly
	
	p0 = bp2sp(bp)
	p1 = vp2sp(vp)
	pz = expand(p0-p1)
	if pz!=sy0:raise eee

def mk_cache(n):
		if n is nnn or n == inf:
			n_repr = "inf"
		else:
			assert type(n) is int
			if n >= 0:
				n_repr = repr(n)
			else:
				raise eee(f"n={n}<0")
		
		assert type(n_repr) is str
		g_sv = dict_infile.mk(
			f"sv[{n_repr}]symmetric_poly2basic_expand.py.txt"
			, dict(n=n_repr, gen="symmetric_poly2basic_expand.py")
			)
		cache=g_sv
		return cache

def main(args=None):
    import argparse


    parser = argparse.ArgumentParser(
        description="symmetric_poly repr by basic_symmetric_poly"
        , epilog=""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-n', '--n', type=int, default=None
                        , help='num gens; =inf')
    """
    parser.add_argument('-vm', '--vmonomial', type=str, default=None
                        , help='::[(exp,repeat)] or {exp:repeat}')
    parser.add_argument('-vp', '--vpoly', type=str, default=None
                        , help='::{reversed_sorted[(exp,repeat)]:coeff}'
                        )
    """
    parser.add_argument('vmonomial_or_vpoly', type=str
                        , help='::[(exp,repeat)] or {exp:repeat}; ::{reversed_sorted[(exp,repeat)]:coeff}'
                        )
    
    parser.add_argument('-vp', '--is_vpoly', action='store_true'
                        , default = False
                        , help='input is vp?')

    args = parser.parse_args(args)
    _main(args)
def _main(args):
		n = args.n
		if 1:
			zero=0#fr0
			one=1#fr1
			check=ff
			cache = mk_cache(n)
			#cache={}
			
		x = eval(args.vmonomial_or_vpoly)
		if args.is_vpoly:
			vp = x
		else:
			if type(x) is dict:
				d = x
				vm = vm_from_dict(d)
			else:
				vm = vm_from_pairs(x)
			vp = vm2vp(vm,one)
		vp,n
		

		pr(f"len(cache)={len(cache)}")
		verify(vp, n, cache, one, zero, check)
		pr(f"len(cache)={len(cache)}")
		#del cache
if 0:
	from seed.helper.stable_repr import (
			stable_repr
			,stable_repr_print
			)
	_1level_expand_kwargs = dict(indent='', depth=0, maybe_max_depth=1, has_head_eol_when_indent=False)
	def _tt(information):
			stable_repr_print(sys.stdout, information, **_1level_expand_kwargs)
	_tt(dict(n="inf", gen="symmetric_poly2basic_expand.py"))

if __name__ == "__main__":
    main()



def _t_sy():
	f=symmetric_poly
	n=4
	gs = symbols(f'a:{n}')
	pr(f(n, *gs))
#_t_sy()

def _t():
	"""
	vpoly2bpoly
	pvpoly2bpoly
	vmonomial2bpoly
	"""
	if 1:
		n=inf
		zero=0#fr0
		one=1#fr1
		#cache={}
		check=ff
		cache = mk_cache(n)
	sf = pvpoly2bpoly(n, cache, one, zero, check)
	vm2bp = sf.vmonomial2bpoly
	vp2bp = sf.vpoly2bpoly
	pvp2bp = sf.pvpoly2bpoly
	
	vm_d_bp_pairs = [
		{}
			,{():1}
		
		,{2:1,1:2}
			,{((4, 1),): -4, ((3, 1), (1, 1)): 1}
		
		,{3:2}
			,{((2, 3),): 1, ((3, 2),): 3, ((6, 1),): 3, ((4, 1), (1, 2)): 3, ((4, 1), (2, 1)): -3, ((5, 1), (1, 1)): -3, ((3, 1), (2, 1), (1, 1)): -3}
		
		#,{4:3,3:5,1:2}
		#	,{((29, 1),): -7308, ((10, 2), (9, 1)): -8, ((11, 1), (9, 2)): -9, ((11, 2), (7, 1)): -70, ((12, 2), (5, 1)): -126, ((13, 1), (8, 2)): -80, ((13, 2), (3, 1)): 11, ((14, 2), (1, 1)): 1099, ((15, 1), (7, 2)): -196, ((15, 1), (14, 1)): -1491, ((16, 1), (13, 1)): 1900, ((17, 1), (6, 2)): -330, ((17, 1), (12, 1)): 1086, ((18, 1), (11, 1)): -2394, ((19, 1), (5, 2)): -483, ((19, 1), (10, 1)): -577, ((20, 1), (3, 3)): 51, ((20, 1), (9, 1)): 3078, ((21, 1), (4, 2)): -714, ((21, 1), (8, 1)): -336, ((22, 1), (7, 1)): -3857, ((23, 1), (2, 3)): -441, ((23, 1), (3, 2)): -1011, ((23, 1), (6, 1)): 2064, ((24, 1), (5, 1)): 4188, ((25, 1), (2, 2)): -1169, ((25, 1), (4, 1)): -4592, ((26, 1), (1, 3)): 2100, ((26, 1), (3, 1)): -3612, ((27, 1), (1, 2)): -5740, ((27, 1), (2, 1)): 7119, ((28, 1), (1, 1)): 5740, ((10, 1), (8, 2), (3, 1)): 1, ((10, 1), (9, 2), (1, 1)): 8, ((10, 2), (6, 1), (3, 1)): 2, ((10, 2), (7, 1), (2, 1)): 3, ((10, 2), (8, 1), (1, 1)): -15, ((11, 1), (10, 1), (8, 1)): 55, ((11, 2), (4, 1), (3, 1)): 7, ((11, 2), (5, 1), (2, 1)): 18, ((11, 2), (6, 1), (1, 1)): -20, ((12, 1), (7, 2), (3, 1)): 5, ((12, 1), (8, 2), (1, 1)): 28, ((12, 1), (9, 1), (8, 1)): -12, ((12, 1), (10, 1), (7, 1)): -19, ((12, 1), (11, 1), (3, 2)): -15, ((12, 1), (11, 1), (6, 1)): 150, ((12, 2), (3, 1), (2, 1)): 69, ((12, 2), (4, 1), (1, 1)): 32, ((13, 1), (7, 2), (2, 1)): -6, ((13, 1), (9, 1), (7, 1)): 181, ((13, 1), (10, 1), (3, 2)): 19, ((13, 1), (10, 1), (6, 1)): -174, ((13, 1), (11, 1), (5, 1)): 39, ((13, 1), (12, 1), (2, 2)): -109, ((13, 1), (12, 1), (4, 1)): 126, ((13, 2), (2, 1), (1, 1)): 318, ((14, 1), (6, 2), (3, 1)): 12, ((14, 1), (7, 2), (1, 1)): 42, ((14, 1), (8, 1), (7, 1)): 56, ((14, 1), (9, 1), (3, 2)): 15, ((14, 1), (9, 1), (6, 1)): -186, ((14, 1), (10, 1), (5, 1)): 288, ((14, 1), (11, 1), (2, 2)): 144, ((14, 1), (11, 1), (4, 1)): -231, ((14, 1), (12, 1), (3, 1)): 69, ((14, 1), (13, 1), (1, 2)): -462, ((14, 1), (13, 1), (2, 1)): -493, ((15, 1), (6, 2), (2, 1)): -27, ((15, 1), (8, 1), (3, 2)): -36, ((15, 1), (8, 1), (6, 1)): 339, ((15, 1), (9, 1), (5, 1)): -177, ((15, 1), (10, 1), (2, 2)): 77, ((15, 1), (10, 1), (4, 1)): -12, ((15, 1), (11, 1), (3, 1)): -45, ((15, 1), (12, 1), (1, 2)): 595, ((15, 1), (12, 1), (2, 1)): 537, ((15, 1), (13, 1), (1, 1)): -245, ((16, 1), (5, 2), (3, 1)): 22, ((16, 1), (6, 2), (1, 1)): 65, ((16, 1), (7, 1), (3, 2)): 1, ((16, 1), (7, 1), (6, 1)): 145, ((16, 1), (8, 1), (5, 1)): -364, ((16, 1), (9, 1), (2, 2)): -196, ((16, 1), (9, 1), (4, 1)): 394, ((16, 1), (10, 1), (3, 1)): -243, ((16, 1), (11, 1), (1, 2)): 345, ((16, 1), (11, 1), (2, 1)): 507, ((16, 1), (12, 1), (1, 1)): -2250, ((17, 1), (5, 2), (2, 1)): -72, ((17, 1), (6, 1), (3, 2)): 54, ((17, 1), (7, 1), (5, 1)): 536, ((17, 1), (8, 1), (2, 2)): -27, ((17, 1), (8, 1), (4, 1)): -274, ((17, 1), (9, 1), (3, 1)): 177, ((17, 1), (10, 1), (1, 2)): -804, ((17, 1), (10, 1), (2, 1)): -660, ((17, 1), (11, 1), (1, 1)): 819, ((18, 1), (4, 2), (3, 1)): 35, ((18, 1), (5, 1), (3, 2)): -48, ((18, 1), (5, 2), (1, 1)): 130, ((18, 1), (6, 1), (5, 1)): 210, ((18, 1), (7, 1), (2, 2)): 281, ((18, 1), (7, 1), (4, 1)): -497, ((18, 1), (8, 1), (3, 1)): 474, ((18, 1), (9, 1), (1, 2)): -128, ((18, 1), (9, 1), (2, 1)): -603, ((18, 1), (10, 1), (1, 1)): 2379, ((19, 1), (4, 1), (3, 2)): -35, ((19, 1), (4, 2), (2, 1)): -150, ((19, 1), (6, 1), (2, 2)): -103, ((19, 1), (6, 1), (4, 1)): 837, ((19, 1), (7, 1), (3, 1)): -606, ((19, 1), (8, 1), (1, 2)): 1050, ((19, 1), (8, 1), (2, 1)): 1026, ((19, 1), (9, 1), (1, 1)): -1674, ((20, 1), (4, 2), (1, 1)): 288, ((20, 1), (5, 1), (2, 2)): -369, ((20, 1), (5, 1), (4, 1)): 234, ((20, 1), (6, 1), (3, 1)): -522, ((20, 1), (7, 1), (1, 2)): -276, ((20, 1), (7, 1), (2, 1)): 618, ((20, 1), (8, 1), (1, 1)): -2454, ((21, 1), (3, 2), (2, 1)): -321, ((21, 1), (4, 1), (2, 2)): 422, ((21, 1), (5, 1), (3, 1)): 1293, ((21, 1), (6, 1), (1, 2)): -1250, ((21, 1), (6, 1), (2, 1)): -1749, ((21, 1), (7, 1), (1, 1)): 3066, ((22, 1), (3, 1), (2, 2)): 321, ((22, 1), (3, 2), (1, 1)): 519, ((22, 1), (4, 1), (3, 1)): 229, ((22, 1), (5, 1), (1, 2)): 924, ((22, 1), (5, 1), (2, 1)): -142, ((22, 1), (6, 1), (1, 1)): 2041, ((23, 1), (4, 1), (1, 2)): 1365, ((23, 1), (4, 1), (2, 1)): 2441, ((23, 1), (5, 1), (1, 1)): -5029, ((24, 1), (2, 2), (1, 1)): 1596, ((24, 1), (3, 1), (1, 2)): -2031, ((24, 1), (3, 1), (2, 1)): -747, ((24, 1), (4, 1), (1, 1)): -524, ((25, 1), (2, 1), (1, 2)): -1596, ((25, 1), (3, 1), (1, 1)): 7147, ((26, 1), (2, 1), (1, 1)): -1939, ((10, 1), (9, 1), (7, 1), (3, 1)): -2, ((10, 1), (9, 1), (8, 1), (2, 1)): -1, ((11, 1), (8, 1), (7, 1), (3, 1)): -1, ((11, 1), (9, 1), (6, 1), (3, 1)): 3, ((11, 1), (9, 1), (7, 1), (2, 1)): 2, ((11, 1), (9, 1), (8, 1), (1, 1)): -7, ((11, 1), (10, 1), (5, 1), (3, 1)): -7, ((11, 1), (10, 1), (6, 1), (2, 1)): -13, ((11, 1), (10, 1), (7, 1), (1, 1)): 30, ((12, 1), (8, 1), (6, 1), (3, 1)): -9, ((12, 1), (8, 1), (7, 1), (2, 1)): -4, ((12, 1), (9, 1), (5, 1), (3, 1)): 6, ((12, 1), (9, 1), (6, 1), (2, 1)): 9, ((12, 1), (9, 1), (7, 1), (1, 1)): -47, ((12, 1), (10, 1), (4, 1), (3, 1)): 1, ((12, 1), (10, 1), (5, 1), (2, 1)): 2, ((12, 1), (10, 1), (6, 1), (1, 1)): 19, ((12, 1), (11, 1), (4, 1), (2, 1)): -46, ((12, 1), (11, 1), (5, 1), (1, 1)): -4, ((13, 1), (7, 1), (6, 1), (3, 1)): -5, ((13, 1), (8, 1), (5, 1), (3, 1)): 14, ((13, 1), (8, 1), (6, 1), (2, 1)): 20, ((13, 1), (8, 1), (7, 1), (1, 1)): -18, ((13, 1), (9, 1), (4, 1), (3, 1)): -20, ((13, 1), (9, 1), (5, 1), (2, 1)): -40, ((13, 1), (9, 1), (6, 1), (1, 1)): 40, ((13, 1), (10, 1), (4, 1), (2, 1)): 51, ((13, 1), (10, 1), (5, 1), (1, 1)): -30, ((13, 1), (11, 1), (3, 1), (2, 1)): -14, ((13, 1), (11, 1), (4, 1), (1, 1)): 27, ((13, 1), (12, 1), (3, 1), (1, 1)): -169, ((14, 1), (7, 1), (5, 1), (3, 1)): -19, ((14, 1), (7, 1), (6, 1), (2, 1)): -1, ((14, 1), (8, 1), (4, 1), (3, 1)): 5, ((14, 1), (8, 1), (5, 1), (2, 1)): -9, ((14, 1), (8, 1), (6, 1), (1, 1)): -73, ((14, 1), (9, 1), (4, 1), (2, 1)): 50, ((14, 1), (9, 1), (5, 1), (1, 1)): 62, ((14, 1), (10, 1), (3, 1), (2, 1)): -149, ((14, 1), (10, 1), (4, 1), (1, 1)): -93, ((14, 1), (11, 1), (3, 1), (1, 1)): 178, ((14, 1), (12, 1), (2, 1), (1, 1)): -65, ((15, 1), (6, 1), (5, 1), (3, 1)): -12, ((15, 1), (7, 1), (4, 1), (3, 1)): 31, ((15, 1), (7, 1), (5, 1), (2, 1)): 62, ((15, 1), (7, 1), (6, 1), (1, 1)): -14, ((15, 1), (8, 1), (4, 1), (2, 1)): -70, ((15, 1), (8, 1), (5, 1), (1, 1)): 35, ((15, 1), (9, 1), (3, 1), (2, 1)): 57, ((15, 1), (9, 1), (4, 1), (1, 1)): -68, ((15, 1), (10, 1), (3, 1), (1, 1)): 203, ((15, 1), (11, 1), (2, 1), (1, 1)): -674, ((16, 1), (6, 1), (4, 1), (3, 1)): -32, ((16, 1), (6, 1), (5, 1), (2, 1)): 17, ((16, 1), (7, 1), (4, 1), (2, 1)): -66, ((16, 1), (7, 1), (5, 1), (1, 1)): -141, ((16, 1), (8, 1), (3, 1), (2, 1)): 175, ((16, 1), (8, 1), (4, 1), (1, 1)): 180, ((16, 1), (9, 1), (3, 1), (1, 1)): -274, ((16, 1), (10, 1), (2, 1), (1, 1)): 252, ((17, 1), (5, 1), (4, 1), (3, 1)): -22, ((17, 1), (6, 1), (4, 1), (2, 1)): 137, ((17, 1), (6, 1), (5, 1), (1, 1)): -10, ((17, 1), (7, 1), (3, 1), (2, 1)): -149, ((17, 1), (7, 1), (4, 1), (1, 1)): 63, ((17, 1), (8, 1), (3, 1), (1, 1)): -203, ((17, 1), (9, 1), (2, 1), (1, 1)): 748, ((18, 1), (5, 1), (4, 1), (2, 1)): 59, ((18, 1), (6, 1), (3, 1), (2, 1)): -186, ((18, 1), (6, 1), (4, 1), (1, 1)): -302, ((18, 1), (7, 1), (3, 1), (1, 1)): 437, ((18, 1), (8, 1), (2, 1), (1, 1)): -593, ((19, 1), (5, 1), (3, 1), (2, 1)): 337, ((19, 1), (5, 1), (4, 1), (1, 1)): -39, ((19, 1), (6, 1), (3, 1), (1, 1)): 131, ((19, 1), (7, 1), (2, 1), (1, 1)): -738, ((20, 1), (4, 1), (3, 1), (2, 1)): 67, ((20, 1), (5, 1), (3, 1), (1, 1)): -641, ((20, 1), (6, 1), (2, 1), (1, 1)): 1117, ((21, 1), (4, 1), (3, 1), (1, 1)): -34, ((21, 1), (5, 1), (2, 1), (1, 1)): 502, ((22, 1), (4, 1), (2, 1), (1, 1)): -1848, ((23, 1), (3, 1), (2, 1), (1, 1)): 162}

		]
	assert len(vm_d_bp_pairs)%2==0
	
	vm_d_bp_pairs = [
		*zip(
			vm_d_bp_pairs[0::2]
			,vm_d_bp_pairs[1::2]
			)
		]
	
	
	#symmetric_poly
	#pr(f"n={n}")
	for vm_d, ans_bp in vm_d_bp_pairs:
		vm = vm_from_dict(vm_d)
		#pr(vm)
		bp = vm2bp(vm)
		try:
			assert bp == ans_bp
		except:
			pr(f"vm={vm}")
			pr(f"bp={bp}")
			pr(f"ans_bp={ans_bp}")
			pr(len(bp))
			pr(f"len(bp)={len(bp)}")
			pr(f"len(ans_bp)={len(ans_bp)}")
			raise
	
	
_t()




