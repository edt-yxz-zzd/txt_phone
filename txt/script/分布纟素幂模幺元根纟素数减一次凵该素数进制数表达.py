#__all__:goto
r'''[[[
e script/分布纟素幂模幺元根纟素数减一次凵该素数进制数表达.py
?命名有误?:不是『n-th primitive root of 1:n次本原根纟幺元』应当是『primitive n-th root of 1:本原n次根纟幺元』

script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达
py -m nn_ns.app.debug_cmd   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达:__doc__ -ht # -ff -df

[[
@20250321
分布纟素幂模幺元根纟素数减一次凵该素数进制数表达
  list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_(p, k, g=None, /):
  [rs[p,k] := {r | [r:<-[1..<p**k]][r**(p-1)%p**k==1]}]
  [g[p] <- 本原根集%p]
  [1 <= len({g,g+p}/-\本原根集%p**k)]
  [gg[p,k;g] :<- ({g,g+p}/-\本原根集%p**k)]
  [ggg[p,k;g] := (gg**p**(k-1)%p**k)]
  [ggg 是 本原(p-1)次幺元根%p**k]
  [(p-1)次幺元根集%p**k == {ggg**i%p**k | [i:<-[1..<p]]}]



]]

list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_(p, k, factorization_of_pmm, primitive_root_mod_p=None, /)

[[[
===
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_ =7 =2 ='{2:1,3:1}'
(1, [0, 1])
(18, [2, 4])
(19, [2, 5])
(30, [4, 2])
(31, [4, 3])
(48, [6, 6])
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_ =7 =3 ='{2:1,3:1}'
(1, [0, 0, 1])
(18, [0, 2, 4])
(19, [0, 2, 5])
(324, [6, 4, 2])
(325, [6, 4, 3])
(342, [6, 6, 6])
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_ =7 =9 ='{2:1,3:1}'
(1, [0, 0, 0, 0, 0, 0, 0, 0, 1])
(14906455, [2, 4, 0, 4, 6, 3, 0, 2, 4])
(14906456, [2, 4, 0, 4, 6, 3, 0, 2, 5])
(25447151, [4, 2, 6, 2, 0, 3, 6, 4, 2])
(25447152, [4, 2, 6, 2, 0, 3, 6, 4, 3])
(40353606, [6, 6, 6, 6, 6, 6, 6, 6, 6])

py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_ =3 =3 ='{2:1}'
(1, [0, 0, 1])
(26, [2, 2, 2])
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_ =5 =3 ='{2:2}'
(1, [0, 0, 1])
(57, [2, 1, 2])
(68, [2, 3, 3])
(124, [4, 4, 4])
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_ =11 =2 ='{2:1,5:1}'
(1, [0, 1])
(3, [0, 3])
(9, [0, 9])
(27, [2, 5])
(40, [3, 7])
(81, [7, 4])
(94, [8, 6])
(112, [10, 2])
(118, [10, 8])
(120, [10, 10])
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_ =13 =2 ='{2:2,3:1}'
(1, [0, 1])
(19, [1, 6])
(22, [1, 9])
(23, [1, 10])
(70, [5, 5])
(80, [6, 2])
(89, [6, 11])
(99, [7, 8])
(146, [11, 3])
(147, [11, 4])
(150, [11, 7])
(168, [12, 12])
===
]]]




[[[
===
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,100:iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver1_ =2  +one_vs_all +to_output_fails +to_group  > /sdcard/0my_files/tmp/0tmp1
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,100:iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_ =2 =542  +one_vs_all +to_output_fails +to_group  > /sdcard/0my_files/tmp/0tmp2
diff /sdcard/0my_files/tmp/0tmp1 /sdcard/0my_files/tmp/0tmp2
    same
===
(-2, 0)
(-3, 0)
(-5, 0)
(-7, 0)
(11, [3, 9])
(-13, 0)
(-17, 0)
(-19, 0)
(-23, 0)
(29, [14])
(-31, 0)
(37, [18])
(-41, 0)
(43, [19])
(-47, 0)
(-53, 0)
(59, [53])
(-61, 0)
(-67, 0)
(71, [11, 26])
(-73, 0)
(79, [31])
(-83, 0)
(-89, 0)
(97, [53])
(-101, 0)
(103, [43])
(-107, 0)
(109, [96])
(113, [68])
(127, [38, 62])
(131, [58, 111])
(137, [19])
(-139, 0)
(-149, 0)
(151, [78])
(-157, 0)
(163, [65, 84])
(-167, 0)
(-173, 0)
(-179, 0)
(181, [78])
(191, [176])
(-193, 0)
(197, [143])
(199, [174])
(211, [165, 182])
(223, [69])
(-227, 0)
(229, [44, 209])
(233, [33])
(-239, 0)
(241, [94])
(-251, 0)
(257, [48])
(263, [79])
(269, [171, 180, 207])
(-271, 0)
(-277, 0)
(281, [20])
(283, [147])
(293, [91])
(307, [40])
(-311, 0)
(313, [104, 213])
(-317, 0)
(331, [18, 71, 324])
(-337, 0)
(347, [75, 156])
(349, [223, 317])
(353, [14, 196])
(359, [257, 331])
(367, [159, 205])
(373, [242])
(379, [174])
(-383, 0)
(-389, 0)
(397, [175])
(401, [280])
(-409, 0)
(419, [369])
(421, [251])
(-431, 0)
(433, [349])
(439, [194])
(-443, 0)
(449, [210])
(-457, 0)
(461, [52])
(463, [255, 345])
(-467, 0)
(-479, 0)
(487, [10, 100, 175, 307])
(-491, 0)
(499, [346])
(-503, 0)
(509, [93, 250])
(521, [308])
(523, [241])
(-541, 0)
===
]]]
[[[
view others/数学/有递增趋势的非递增序列.txt
===
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   @list.iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_ =2 =542  +one_vs_all  +to_group +to_rev_flatten
[11, 9, 3, 29, 14, 37, 18, 43, 19, 59, 53, 71, 26, 11, 79, 31, 97, 53, 103, 43, 109, 96, 113, 68, 127, 62, 38, 131, 111, 58, 137, 19, 151, 78, 163, 84, 65, 181, 78, 191, 176, 197, 143, 199, 174, 211, 182, 165, 223, 69, 229, 209, 44, 233, 33, 241, 94, 257, 48, 263, 79, 269, 207, 180, 171, 281, 20, 283, 147, 293, 91, 307, 40, 313, 213, 104, 331, 324, 71, 18, 347, 156, 75, 349, 317, 223, 353, 196, 14, 359, 331, 257, 367, 205, 159, 373, 242, 379, 174, 397, 175, 401, 280, 419, 369, 421, 251, 433, 349, 439, 194, 449, 210, 461, 52, 463, 345, 255, 487, 307, 175, 100, 10, 499, 346, 509, 250, 93, 521, 308, 523, 241]
===
]]]



[[[
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_ =2 =542 +to_group +one_vs_all
===

py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,10010:iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver1_ =2  +one_vs_all +to_output_fails  > /sdcard/0my_files/tmp/0tmp
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,10010:iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_ =2  =74201+1 +one_vs_all +to_output_fails  > /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp
du -h /sdcard/0my_files/tmp/0tmp
    136K
(-2, 0) #1
(-3, 0)
(-5, 0)
(-7, 0)
(11, 3)
(11, 9)
(-13, 0)
(-17, 0)
(-19, 0)
(-23, 0)
(29, 14)
(-31, 0)
(37, 18)
(-41, 0)
(43, 19)
(-47, 0)
(-53, 0)
(59, 53) #18
(-61, 0)
(-67, 0)
... ...
... ...
(74159, 27617) #10003
(74161, 68925)
(74167, 25129)
(-74177, 0)
(74189, 24821)
(-74197, 0)
(74201, 4486)
(74201, 69084) #10010
===
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,_reformat_ofile__collect :/sdcard/0my_files/tmp/0tmp  > /sdcard/0my_files/tmp/0tmp3
view /sdcard/0my_files/tmp/0tmp3
du -h /sdcard/0my_files/tmp/0tmp3
    124K
(-2, 0) #1
(-3, 0)
(-5, 0)
(-7, 0)
(11, [3, 9])
(-13, 0)
(-17, 0)
(-19, 0)
(-23, 0)
(29, [14])
(-31, 0)
(37, [18])
(-41, 0)
(43, [19])
(-47, 0)
(-53, 0)
(59, [53]) #17
(-61, 0) #18
... ...
... ...
(74159, [27617]) #7315
(74161, [68925])
(74167, [25129])
(-74177, 0)
(74189, [24821])
(-74197, 0)
(74201, [4486, 69084]) #7321 <==> [PRIMES_S1[7321]==74201]
===
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,_reformat_ofile__collect :/sdcard/0my_files/tmp/0tmp +to_drop_fails > /sdcard/0my_files/tmp/0tmp4
view /sdcard/0my_files/tmp/0tmp4
du -h /sdcard/0my_files/tmp/0tmp4
    92K
(11, [3, 9]) #1
(29, [14])
(37, [18])
(43, [19])
(59, [53]) #5
... ...
... ...
(74159, [27617]) #4599
(74161, [68925])
(74167, [25129])
(74189, [24821])
(74201, [4486, 69084]) #4603
===
py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,_reformat_ofile__with_neg_residuals :/sdcard/0my_files/tmp/0tmp4 +to_drop_fails > /sdcard/0my_files/tmp/0tmp5
view /sdcard/0my_files/tmp/0tmp5
du -h /sdcard/0my_files/tmp/0tmp5
    156K
(11, [3, 9], [-8, -2]) #1
(29, [14], [-15])
(37, [18], [-19])
(43, [19], [-24])
(59, [53], [-6]) #5
... ...
... ...
(74159, [27617], [-46542]) #4599
(74161, [68925], [-5236])
(74167, [25129], [-49038])
(74189, [24821], [-49368])
(74201, [4486, 69084], [-69715, -5117]) #4603
===

tar -cvf /sdcard/0my_files/tmp/0tmp5.tar.lzma --lzma -C /sdcard/0my_files/tmp/ 0tmp5
du -h /sdcard/0my_files/tmp/0tmp5.tar.lzma
    48K
tar -cvf /sdcard/0my_files/tmp/0tmp4.tar.lzma --lzma -C /sdcard/0my_files/tmp/ 0tmp4
du -h /sdcard/0my_files/tmp/0tmp4.tar.lzma
    28K

mv -iv /sdcard/0my_files/tmp/0tmp4 /sdcard/0my_files/tmp/out4py/script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达..iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_.grouped.dry.n4603_pj7321_p74201.out.txt
tar -cvf /sdcard/0my_files/tmp/out4py/script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达..iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_.grouped.dry.n4603_pj7321_p74201.out.txt.tar.lzma --lzma -C /sdcard/0my_files/tmp/out4py    script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达..iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_.grouped.dry.n4603_pj7321_p74201.out.txt
du -h /sdcard/0my_files/tmp/out4py/script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达..iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_.grouped.dry.n4603_pj7321_p74201.out.txt.tar.lzma
    28K
cp -iv /sdcard/0my_files/tmp/out4py/script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达..iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_.grouped.dry.n4603_pj7321_p74201.out.txt.tar.lzma   ./script/分布纟素幂模幺元根纟素数减一次凵该素数进制数表达..iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_.grouped.dry.n4603_pj7321_p74201.out.txt.tar.lzma
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   @str.read_solo_tarfile_  --xencoding4data:ascii  :script/分布纟素幂模幺元根纟素数减一次凵该素数进制数表达..iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_.grouped.dry.n4603_pj7321_p74201.out.txt.tar.lzma
===
]]]
[[[
===
#显然只有平凡根:{1}
xxx:py_adhoc_call   script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达   ,iter_primes_with_nontrivial_Pth_roots_of_unity_ltP__mod_PpowK__ver2_ =2 =542 +to_group +one_vs_all  > /sdcard/0my_files/tmp/0tmp6
===
===
]]]


from script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达 import *
]]]'''#'''
__all__ = r'''
iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver1_
iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_


list_all_Nth_roots_of_unity_mod_PpowK__in_radixP_
    list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_
        iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_


iter_primes_with_nontrivial_fPth_roots_of_unity_ltP__mod_PpowK__ver2_
    iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_
'''.split()#'''
    #list_all_Pth_roots_of_unity_mod_PpowK__in_radixP_
    #    iter_primes_with_nontrivial_Pth_roots_of_unity_ltP__mod_PpowK__ver2_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge

#.from itertools import islice
#.
___end_mark_of_excluded_global_names__0___ = ...


def list_all_Pmmth_roots_of_unity_mod_PpowK__in_radixP_(p, k, factorization_of_pmm, primitive_root_mod_p=None, /, *, roots_only=False):
    r'''[[[
    :: p/odd_prime -> k/int{>=1} -> factorization_of_pmm/q2e4pmm/{prime:pint}{[p-1==II__p2e_(q2e4pmm)]} -> may primitive_root_mod_p/(uint%p){min_order_mod_(p;primitive_root_mod_p)==p-1} -> sorted[(root/(uint%p**k){[root**(p-1)%p**k==1]}, digits8root/[uint%p]{[[len==k][big_endian]]})]{len==p-1}
    #]]]'''#'''
    return list_all_Nth_roots_of_unity_mod_PpowK__in_radixP_(N:=p-1, p, k, factorization_of_pmm, primitive_root_mod_p, roots_only=roots_only)
def __():
    #显然只有平凡根:{1}
  def list_all_Pth_roots_of_unity_mod_PpowK__in_radixP_(p, k, factorization_of_pmm, primitive_root_mod_p=None, /, *, roots_only=False):
    r'''[[[
    :: p/odd_prime -> k/int{>=1} -> factorization_of_pmm/q2e4pmm/{prime:pint}{[p-1==II__p2e_(q2e4pmm)]} -> may primitive_root_mod_p/(uint%p){min_order_mod_(p;primitive_root_mod_p)==p-1} -> sorted[(root/(uint%p**k){[root**p%p**k==1]}, digits8root/[uint%p]{[[len==k][big_endian]]})]{len==1 if k==1 else p}
    #]]]'''#'''
    return list_all_Nth_roots_of_unity_mod_PpowK__in_radixP_(N:=p, p, k, factorization_of_pmm, primitive_root_mod_p, roots_only=roots_only)
def list_all_Nth_roots_of_unity_mod_PpowK__in_radixP_(N, p, k, factorization_of_pmm, primitive_root_mod_p=None, /, *, roots_only=False):
    r'''[[[
    :: N/int{>=1} -> p/odd_prime -> k/int{>=1} -> factorization_of_pmm/q2e4pmm/{prime:pint}{[p-1==II__p2e_(q2e4pmm)]} -> may primitive_root_mod_p/(uint%p){min_order_mod_(p;primitive_root_mod_p)==p-1} -> sorted[(root/(uint%p**k){[root**N%p**k==1]}, digits8root/[uint%p]{[[len==k][big_endian]]})]{len==gcd(N,(p-1)*p**(k-1))}
    # odd_prime <<== [2**(e+3)剩余系群最少2个生成元]
    #]]]'''#'''
    if not roots_only:
        from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_# uint5radix_repr_
    from seed.math.II import II__p2e_
    from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import is_kth_primitive_root_mod_N__via_complete_factorization_k_
    #def is_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, /, *, _ver=2):
    #   'may k/int{>=1} -> factorization{k} -> N/int{>=2} -> r/uint%N -> bool/[k==min_order_mod_(N;r)]'
    from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_# find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_, iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
    #def find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
    from seed.math.is_prime__via_complete_factorization_Nmm_ import is_prime__via_complete_factorization_Nmm_
    #def is_prime__via_complete_factorization_Nmm_(p2e4Nmm_or_ps4Nmm, N, /):
    #   '-> bool | ^ERH__fail/Fail__unknown_fine_upperbound4primitive_root | ^ValueError__not_complete_factorization | ^ValueError__not_sqrt_case'
    if not N == p-1:
        from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
        from math import gcd

    ######################
    check_int_ge(1, N)
    check_int_ge(3, p)
    assert p&1
    check_int_ge(1, k)
    pmm = II__p2e_(factorization_of_pmm)
    assert pmm+1 == p
    assert is_prime__via_complete_factorization_Nmm_(factorization_of_pmm, p)
    if not primitive_root_mod_p is None:
        g = primitive_root_mod_p
    else:
        factorization_of_pmm
        g = find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, p)
    g
    pow_p_kmm = p**(k-1)
    phi_pk = pmm*pow_p_kmm # == phi(p**k)
    factorization_of_phi_pk = {**factorization_of_pmm, p:k-1} if k>1 else factorization_of_pmm
    pk = pow_p_k = p*pow_p_kmm
    assert is_kth_primitive_root_mod_N__via_complete_factorization_k_(pmm, factorization_of_pmm, p, g)
    # [is_kth_primitive_root_mod_N__via_complete_factorization_k_(p-1, factorization_of_pmm, p, g)]
    if not is_kth_primitive_root_mod_N__via_complete_factorization_k_(phi_pk, factorization_of_phi_pk, pk, g):
        gg = g+p
        assert is_kth_primitive_root_mod_N__via_complete_factorization_k_(phi_pk, factorization_of_phi_pk, pk, gg)
        # [is_kth_primitive_root_mod_N__via_complete_factorization_k_(phi_pk, factorization_of_phi_pk, pk, gg)]
    else:
        # [is_kth_primitive_root_mod_N__via_complete_factorization_k_(phi_pk, factorization_of_phi_pk, pk, g)]
        gg = g
        # [is_kth_primitive_root_mod_N__via_complete_factorization_k_(phi_pk, factorization_of_phi_pk, pk, gg)]
    # [is_kth_primitive_root_mod_N__via_complete_factorization_k_(phi_pk, factorization_of_phi_pk, pk, gg)]
    if N == p-1:
        n = pmm
        factorization_of_n = factorization_of_pmm
    else:
        n = gcd(N, phi_pk)
        factorization_of_n = complete_factor_pint_via_trial_division(factorization_of_phi_pk, n)
    n, factorization_of_n
    #r = pow(gg, pow_p_kmm, pk)
    r = pow(gg, phi_pk//n, pk)
    assert is_kth_primitive_root_mod_N__via_complete_factorization_k_(n, factorization_of_n, pk, r)
    # [is_kth_primitive_root_mod_N__via_complete_factorization_k_(n, factorization_of_n, pk, r)]
    roots = [r]
    while not roots[-1] == 1:
        roots.append(roots[-1]*r%pk)
    roots.sort()
    assert len(roots) == n
    if roots_only:
        return roots
    digitss = [list(uint2radix_repr_(p, root, is_big_endian=True, min_len=k)) for root in roots]
    return list(zip(roots, digitss))

def iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver1_(k, /, *, one_vs_all=False, to_output_fails=False, to_group=False):
    r'''[[[
    :: k/int{>=2} -> Iter (p,g){[[p::prime][g:<-[2..<p]][g**(p-1)%p**k==1]]}
    #]]]'''#'''
    ######################
    check_int_ge(2, k)
    #if to_group: one_vs_all = True
    check_type_is(bool, to_group)
    check_type_is(bool, to_output_fails)
    check_type_is(bool, one_vs_all)
    from seed.math.prime_gens import prime_gen
    ######################
    for p in prime_gen:
        pk = p**k
        pmm = p-1
        gs = []
        for g in range(2, p):
            if pow(g, pmm, pk) == 1:
                gs.append(g)
                if not to_group:
                    yield (p, g)
                if not one_vs_all:
                    break
        if not gs and to_output_fails:
            #yield (-p, gs if to_group else 0)
            yield (-p, 0)
        if gs and to_group:
            yield (p, gs)


def iter_primes_with_nontrivial_Pmmth_roots_of_unity_ltP__mod_PpowK__ver2_(k, max1_p, /, *, one_vs_all=False, to_output_fails=False, to_group=False, to_rev_flatten=False):
    r'''[[[
    :: k/int{>=2} -> Iter (p,g){[[p::prime][g:<-[2..<p]][g**(p-1)%p**k==1]]}
    #]]]'''#'''
    check_type_is(bool, to_group)
    check_type_is(bool, one_vs_all)
    #if to_group: one_vs_all = True
    assert to_group
    assert one_vs_all
    ######################
    return iter_primes_with_nontrivial_fPth_roots_of_unity_ltP__mod_PpowK__ver2_(p2N_:=(-1).__add__, k, max1_p, to_output_fails=to_output_fails, to_rev_flatten=to_rev_flatten)
def __():
    #显然只有平凡根:{1}
  def iter_primes_with_nontrivial_Pth_roots_of_unity_ltP__mod_PpowK__ver2_(k, max1_p, /, *, one_vs_all=False, to_output_fails=False, to_group=False, to_rev_flatten=False):
    r'''[[[
    :: k/int{>=2} -> Iter (p,g){[[p::prime][g:<-[2..<p]][g**p%p**k==1]]}
    #]]]'''#'''
    check_type_is(bool, to_group)
    check_type_is(bool, one_vs_all)
    #if to_group: one_vs_all = True
    assert to_group
    assert one_vs_all
    ######################
    return iter_primes_with_nontrivial_fPth_roots_of_unity_ltP__mod_PpowK__ver2_(p2N_:=int, k, max1_p, to_output_fails=to_output_fails, to_rev_flatten=to_rev_flatten)

def iter_primes_with_nontrivial_fPth_roots_of_unity_ltP__mod_PpowK__ver2_(p2N_, k, max1_p, /, *, to_output_fails=False, to_rev_flatten=False):
    r'''[[[
    :: p2N_/(p->N)/(prime->pint) -> k/int{>=2} -> Iter (p,g){[[p::prime][g:<-[2..<p]][g**p2N_(p)%p**k==1]]}
    #]]]'''#'''
    ######################
    check_int_ge(0, max1_p)
    check_int_ge(2, k)
    check_type_is(bool, to_rev_flatten)
    check_type_is(bool, to_output_fails)
    assert not (to_rev_flatten and to_output_fails)
    from seed.math.prime_gens import tabulate_may_factorization4uint_lt_ #all_prime_factors_gen# prime_gen
    ######################
    j2may_p2e = tabulate_may_factorization4uint_lt_(max1_p)
    for j, may_p2e in enumerate(j2may_p2e):
        if not may_p2e:continue
        p2e = may_p2e
        if not (len(p2e) == 1 and [*p2e.items()] == [(j, 1)]):continue
        # [j :: prime]
        p = j
        # [p :: prime]
        factorization_of_pmm = j2may_p2e[p-1]
        N = p2N_(p)
        check_int_ge(1, N)
        ls = [1] if p==2 else [r for r in list_all_Nth_roots_of_unity_mod_PpowK__in_radixP_(N, p, k, factorization_of_pmm, roots_only=True) if r < p]
        assert ls[0] == 1
        del ls[0]
        if to_rev_flatten:
            if ls:
                yield p
                yield from reversed(ls)
            continue
        if ls:
            yield (p, ls)
        elif to_output_fails:
            yield (-p, 0)
#end-def iter_primes_with_nontrivial_fPth_roots_of_unity_ltP__mod_PpowK__ver2_(p2N_, k, max1_p, /, *, to_output_fails=False, to_rev_flatten=False):
def _reformat_ofile__collect(ipath, /, *, to_drop_fails=False):
    from ast import literal_eval
    with open(ipath, 'rt', encoding='ascii') as ifile:
        prev_p = -1
        gs = []
        for line in ifile:
            (xp, xv) = literal_eval(line)
            if gs and prev_p != xp:
                # flush
                yield (prev_p, gs)
                gs.clear()
            #######
            if xp < 0:
                if not to_drop_fails:
                    # echo#forwarding
                    yield (xp, xv)
                continue
            #######
            p = xp
            if type(xv) is list:
                # echo#forwarding
                assert prev_p < 0
                assert not gs
                _gs = xv
                yield (p, _gs)
                continue

            #######
            g = xv
            if p == prev_p:
                # collect
                assert gs
            else:
                # init for collect
                # [prev_p==-1] or flushed
                assert prev_p < p
                assert not gs
                prev_p = p
            gs.append(g)
        #end-for
        if gs:
            assert prev_p > 0
            yield (prev_p, gs)
            gs.clear()
#end-def _reformat_ofile__collect(ipath, /, *, to_drop_fails=False):


def _reformat_ofile__with_neg_residuals(ipath, /, *, to_drop_fails=False):
    from ast import literal_eval
    with open(ipath, 'rt', encoding='ascii') as ifile:
        for line in ifile:
            (xp, xv) = literal_eval(line)
            #######
            if xp < 0:
                assert xv == 0
                if not to_drop_fails:
                    # echo#forwarding
                    yield (xp, xv, xv)
                continue
            #######
            p = xp
            if type(xv) is list:
                gs = xv
                yield (p, gs, [g-p for g in gs])
            else:
                g = xv
                yield (p, g, -g)
        #end-for
#end-def _reformat_ofile__with_neg_residuals(ipath, /, *, to_drop_fails=False):

__all__
from script.分布纟素幂模幺元根纟素数减一次凵该素数进制数表达 import *
