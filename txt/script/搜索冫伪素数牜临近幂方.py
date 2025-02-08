#__all__:goto
r'''[[[
e script/搜索冫伪素数牜临近幂方.py
断点续搜耂命令行集中处:goto


script.搜索冫伪素数牜临近幂方
py -m nn_ns.app.debug_cmd   script.搜索冫伪素数牜临近幂方 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.搜索冫伪素数牜临近幂方:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   script.搜索冫伪素数牜临近幂方   @搜索冫偏移量纟伪素数牜临近幂方扌  =2  =16 =200
(2, 16, 200, [-15, -17, -39, -57, -87, -89, -99, -113, -117, -123, -129, -143, -155, -165, -179, -183], [1, 3, 7, 15, 21, 27, 43, 45, 51, 63, 73, 81, 93, 97, 111, 115, 121, 141, 151, 163, 165, 171, 177, 181, 183, 193, 195])

    #def print_iterable_with_lineno_(max_sz, xs, /, *, offset=0, to_str=repr):
    #def print_iterable_(max_sz, xs, /, *, to_str=repr, may_min_lineno=None):
>>> from seed.tiny_.print_iterable_with_lineno_ import print_iterable_with_lineno_, print_iterable_, print_iterable_with_linenoT, print_iterableT

py_adhoc_call   script.搜索冫伪素数牜临近幂方   ,迭代搜索冫偏移量纟伪素数牜临近幂方扌  '=[2,3]'  '=range(16, 20)' =10 --scale_vs_max4offset_vs_count=0
>>> print_iterable_(9999, 迭代搜索冫偏移量纟伪素数牜临近幂方扌([2,3], range(16, 20), 10))
(2, 16, 160, [-15, -17, -39, -57, -87, -89, -99, -113, -117, -123, -129, -143, -155], [1, 3, 7, 15, 21, 27, 43, 45, 51, 63, 73, 81, 93, 97, 111, 115, 121, 141, 151])
(2, 17, 170, [-1, -9, -13, -31, -49, -61, -63, -85, -91, -99, -103, -115, -145], [29, 39, 41, 57, 71, 77, 99, 131, 141, 149, 159])
(2, 18, 180, [-5, -11, -17, -23, -33, -35, -41, -65, -75, -93, -95, -117, -137, -161, -167, -171, -173], [3, 7, 9, 43, 49, 73, 87, 93, 109, 117, 127, 159, 169, 177])
(2, 19, 190, [-1, -19, -27, -31, -45, -57, -67, -69, -85, -87, -91, -99, -117, -139, -165, -169, -175, -189], [21, 53, 59, 63, 65, 81, 99, 101, 123, 125, 141, 165])
(3, 16, 160, [-98, -104, -110, -118, -122, -134, -140, -142], [26, 28, 58, 68, 110, 146])
(3, 17, 170, [-10, -14, -56, -80, -94, -104, -106, -140], [34, 50, 64, 88, 106, 140, 148, 166])
(3, 18, 180, [-10, -32, -46, -56, -98, -166, -178], [10, 70, 100, 128, 140, 152])
(3, 19, 190, [-14, -20, -64, -88, -110, -128, -154], [56, 104, 122, 136, 152, 184, 190])
>>> print_iterable_(9999, 迭代搜索冫偏移量纟伪素数牜临近幂方扌([2,3], range(16, 20), 10, may_prime_basis=[2]))
(2, 16, 160, (2,), [-15, -17, -39, -57, -87, -89, -99, -113, -117, -123, -129, -143, -155], [1, 3, 7, 15, 21, 27, 43, 45, 51, 63, 73, 81, 93, 97, 111, 115, 121, 141, 151])
(2, 17, 170, (2,), [-1, -9, -13, -31, -49, -61, -63, -85, -91, -99, -103, -115, -145], [29, 39, 41, 57, 71, 77, 99, 131, 141, 149, 159])
(2, 18, 180, (2,), [-5, -11, -17, -23, -33, -35, -41, -65, -75, -93, -95, -117, -137, -161, -167, -171, -173], [3, 7, 9, 43, 49, 73, 87, 93, 109, 117, 127, 159, 169, 177])
(2, 19, 190, (2,), [-1, -19, -27, -31, -45, -57, -67, -69, -85, -87, -91, -99, -117, -139, -165, -169, -175, -189], [21, 53, 59, 63, 65, 81, 99, 101, 123, 125, 141, 165])
(3, 16, 160, (2,), [-98, -104, -110, -118, -122, -134, -140, -142], [26, 28, 58, 68, 110, 146])
(3, 17, 170, (2,), [-10, -14, -56, -80, -94, -104, -106, -140], [34, 50, 64, 88, 106, 140, 148, 166])
(3, 18, 180, (2,), [-10, -32, -46, -56, -98, -166, -178], [10, 70, 100, 128, 140, 152])
(3, 19, 190, (2,), [-14, -20, -64, -88, -110, -128, -154], [56, 104, 122, 136, 152, 184, 190])
>>> print_iterable_(9999, 迭代搜索冫偏移量纟伪素数牜临近幂方扌([2], range(16, 20), 4, scale_vs_max4offset_vs_count=0, may_prime_basis=[2]))
(2, 16, 64, (2,), [-15, -17, -39, -57], [1, 3, 7, 15, 21, 27, 43, 45, 51, 63])
(2, 17, 68, (2,), [-1, -9, -13, -31, -49, -61, -63], [29, 39, 41, 57])
(2, 18, 72, (2,), [-5, -11, -17, -23, -33, -35, -41, -65], [3, 7, 9, 43, 49])
(2, 19, 76, (2,), [-1, -19, -27, -31, -45, -57, -67, -69], [21, 53, 59, 63, 65])
>>> print_iterable_(9999, 迭代搜索冫偏移量纟伪素数牜临近幂方扌([2], range(16, 20), 40, scale_vs_max4offset_vs_count=1, may_prime_basis=[2]))
(2, 16, 40, (2,), [-15, -17, -39], [1, 3, 7, 15, 21, 27])
(2, 17, 40, (2,), [-1, -9, -13, -31], [29, 39])
(2, 18, 40, (2,), [-5, -11, -17, -23, -33, -35], [3, 7, 9])
(2, 19, 40, (2,), [-1, -19, -27, -31], [21])
>>> print_iterable_(9999, 迭代搜索冫偏移量纟伪素数牜临近幂方扌([2], range(16, 20), 4, scale_vs_max4offset_vs_count=2, may_prime_basis=[2]))
(2, 16, -4, (2,), [-15, -17, -39, -57], [1, 3, 7, 15])
(2, 17, -4, (2,), [-1, -9, -13, -31], [29, 39, 41, 57])
(2, 18, -4, (2,), [-5, -11, -17, -23], [3, 7, 9, 43])
(2, 19, -4, (2,), [-1, -19, -27, -31], [21, 53, 59, 63])





######################
四种类输出:
    x10     None#自适应
    x10     2-SPRP
    max200  2-SPRP
    sz4     2-SPRP
    ###
    起步皆为:2**16
    ###释义:
    x10     偏移范围: [-exp*10..=+exp*10]
    max200  偏移范围: [-200..=+200]
    sz4     数目纟偏移量:4+4
    #########
    #########
    #2-SPRP:可能有毛病:第一次
    由于seed.math.prime_gens.is_prime__tribool_():打补丁『增加了 试除@[skip_A014233==True]』
        if skip_A014233 and not skip_check:
            # trial_division_if_skip_A014233
    此补丁 主要是 为了使用试除来更快 识别含小因子的合数
    此补丁 可能导致 某些伪素数在新版本之中被分解
    => _重检牜文件扌()DONE!
    打补丁时 3个2-SPRP快照:输出至:
        x10:    (2, 430, 4300, (2,), [-677, -797, -1023, -1671, -2385, -3093, -3735, -3933, -4277], [73, 1105, 2173, 2535, 2647, 2869, 3075, 3907, 3913, 4053])
        max200: (2, 2003, 200, (2,), [-1], [])
        sz4:    (2, 1250, -4, (2,), [-597, -1221, -1841, -2205], [1447, 3879, 7243, 8545])
        #剩下的:自适应.非2-SPRP:x10:    (2, 1168, 11680, [-1013, -1533, -3023, -3395, -4245, -4325, -6137, -6573, -6599, -7493, -9035, -10077, -10323, -10815, -10907, -11247], [597, 1341, 1611, 2071, 5527, 5877, 5995, 6247, 7371, 7605, 7791, 8053, 10531, 10585, 11175])
    #########
    #########
    #2-SPRP:可能有毛病:第二次
    #new-version:USING_is_strong_pseudoprime__basis__with_trial_division_:goto
    不过毛病应该不大，只是嫌改来改去 很繁琐，新建一个函数is_strong_pseudoprime__basis__with_trial_division_
    此时:
        view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.out.txt
        (2, 1168, 11680, [-1013, -1533, -3023, -3395, -4245, -4325, -6137, -6573, -6599, -7493, -9035, -10077, -10323, -10815, -10907, -11247], [597, 1341, 1611, 2071, 5527, 5877, 5995, 6247, 7371, 7605, 7791, 8053, 10531, 10585, 11175])
        view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt
        (2, 430, 4300, (2,), [-677, -797, -1023, -1671, -2385, -3093, -3735, -3933, -4277], [73, 1105, 2173, 2535, 2647, 2869, 3075, 3907, 3913, 4053])
        view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt
        (2, 3000, 200, (2,), [], [])
        view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt
        (2, 1350, -4, (2,), [-291, -833, -1071, -2363], [315, 717, 849, 1809])
    #########
    #########
    由于2-SPRP 包含 大量 (2**ez-1) 
        view ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
    此后 采用 2_3_5_7-SPRP
    #########
==>>:
#无需重检:py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,_重检牜文件扌 +仅试除 +欤重建 :script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.out.txt >> script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.out.fixed
DONE:py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,_重检牜文件扌 +仅试除 +欤重建 :script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt >> script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.fixed
view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.fixed
diff script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.fixed script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt
mv -iv script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.fixed script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt
DONE:py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,_重检牜文件扌 +仅试除 +欤重建 :script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt  >> script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.fixed
    #发现超多 bad_offset 都是 -1，少量+1
    #   比如: (2**23-1), (2**32+1)
view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.fixed
diff script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.fixed  script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt
mv -iv  script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.fixed  script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt
DONE:py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,_重检牜文件扌 +仅试除 +欤重建 :script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt >> script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.fixed
view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.fixed
diff script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.fixed script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt
mv -iv script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.fixed script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt

<<==:
new:
view script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt
view script/搜索冫伪素数牜临近幂方.py..header.24.1-_.sz4.2_3_5_7-SPRP.out.txt
old:
    view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.out.txt
    view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt
    view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt
    view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt
<<==:
断点续搜耂命令行集中处:here
new:
py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield +to_show_timedelta --may_args4PeriodicToilLeisureTime='(60,60)' --may_prompt_string6resting:$'\n\n    resting...\n\n' }  script.搜索冫伪素数牜临近幂方   ,main  =2  =1 =3000+1   =2 =4  --may_prime_basis='[2,3,5,7]' --path:script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt
    done@20250208
    du -h script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt
        236K
    view script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt
        (2, 2999, -4, (2, 3, 5, 7), [-1417, -5325, -5881, -7947], [233, 4613, 5565, 6171])
        (2, 3000, -4, (2, 3, 5, 7), [-2699, -3533, -3645, -5415], [3993, 4785, 9741, 11191])
    view ../../python3_src/seed/for_libs/for_tarfile.py
    tar -cvf script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt.tar.lzma  --lzma script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt
    du -h script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt.tar.lzma
        56K
py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield +to_show_timedelta --may_args4PeriodicToilLeisureTime='(60,60)' --may_prompt_string6resting:$'\n\n    resting...\n\n' }  script.搜索冫伪素数牜临近幂方   ,main  =24  =1 =3000+1   =2 =4  --may_prime_basis='[2,3,5,7]' --path:script/搜索冫伪素数牜临近幂方.py..header.24.1-_.sz4.2_3_5_7-SPRP.out.txt
<<==:
old:
    由于2-SPRP 包含 大量 (2**ez-1) 
#py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,main  =2  =16 =3000+1   =0 =10  --may_prime_basis='None' --path:script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.out.txt
#py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,main  =2  =16 =3000+1   =0 =10  --may_prime_basis='[2]' --path:script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt
#py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,main  =2  =16 =3000+1   =1 =200  --may_prime_basis='[2]' --path:script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt
#py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,main  =2  =16 =3000+1   =2 =4  --may_prime_basis='[2]' --path:script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt
<<==:
######################
#py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,迭代搜索冫偏移量纟伪素数牜临近幂方扌  '=[2]'  '=range(16, 3000+1)' =10 --scale_vs_max4offset_vs_count=0 >> script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.out.txt
#view script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.out.txt
    #
    (2, 16, 160, [-15, -17, -39, -57, -87, -89, -99, -113, -117, -123, -129, -143, -155], [1, 3, 7, 15, 21, 27, 43, 45, 51, 63, 73, 81, 93, 97, 111, 115, 121, 141, 151])
    ...
    (2, 1168, 11680, [-1013, -1533, -3023, -3395, -4245, -4325, -6137, -6573, -6599, -7493, -9035, -10077, -10323, -10815, -10907, -11247], [597, 1341, 1611, 2071, 5527, 5877, 5995, 6247, 7371, 7605, 7791, 8053, 10531, 10585, 11175])
    #
    du -h script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.out.txt
        228K@1168
    #
#diff script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.out.txt script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.out.txt
('script.搜索冫伪素数牜临近幂方._0worker_', (2, 0, 10, None), {})
rm script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.out.txt
py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,main  =2  =16 =3000+1   =0 =10  --may_prime_basis='None' --path:script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.out.txt
view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.out.txt


######################
#py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,迭代搜索冫偏移量纟伪素数牜临近幂方扌  '=[2]'  '=range(16, 3000+1)' =10 --scale_vs_max4offset_vs_count=0 --may_prime_basis='[2]' >> script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.2-SPRP.out.txt
#view script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.2-SPRP.out.txt
    #
    (2, 16, 160, (2,), [-15, -17, -39, -57, -87, -89, -99, -113, -117, -123, -129, -143, -155], [1, 3, 7, 15, 21, 27, 43, 45, 51, 63, 73, 81, 93, 97, 111, 115, 121, 141, 151])
    ...
    (2, 430, 4300, (2,), [-677, -797, -1023, -1671, -2385, -3093, -3735, -3933, -4277], [73, 1105, 2173, 2535, 2647, 2869, 3075, 3907, 3913, 4053])
    #
#du -h script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.2-SPRP.out.txt
        80K@430
    #
#diff script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.2-SPRP.out.txt script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt
('script.搜索冫伪素数牜临近幂方._0worker_', (2, 0, 10, [2]), {})
rm script/搜索冫伪素数牜临近幂方.py..2.16-_.x10.2-SPRP.out.txt

py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,main  =2  =16 =3000+1   =0 =10  --may_prime_basis='[2]' --path:script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt
view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.x10.2-SPRP.out.txt



######################
#py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,迭代搜索冫偏移量纟伪素数牜临近幂方扌  '=[2]'  '=range(16, 3000+1)' =200 --scale_vs_max4offset_vs_count=1 --may_prime_basis='[2]' >> script/搜索冫伪素数牜临近幂方.py..2.16-_.max200.2-SPRP.out.txt
#view script/搜索冫伪素数牜临近幂方.py..2.16-_.max200.2-SPRP.out.txt
    (2, 16, 200, (2,), [-15, -17, -39, -57, -87, -89, -99, -113, -117, -123, -129, -143, -155, -165, -179, -183], [1, 3, 7, 15, 21, 27, 43, 45, 51, 63, 73, 81, 93, 97, 111, 115, 121, 141, 151, 163, 165, 171, 177, 181, 183, 193, 195])
    ...
    (2, 752, 200, (2,), [], [])
    ...
    (2, 1708, 200, (2,), [], [183])
    ...
    #
#du -h script/搜索冫伪素数牜临近幂方.py..2.16-_.max200.2-SPRP.out.txt
        60K@1708
    #
    #py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,迭代搜索冫偏移量纟伪素数牜临近幂方扌  '=[2]'  '=range(752+1, 3000+1)' =200 --scale_vs_max4offset_vs_count=1 --may_prime_basis='[2]' >> script/搜索冫伪素数牜临近幂方.py..2.16-_.max200.2-SPRP.out.txt
    #
    #py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,迭代搜索冫偏移量纟伪素数牜临近幂方扌  '=[2]'  '=range(1708+1, 3000+1)' =200 --scale_vs_max4offset_vs_count=1 --may_prime_basis='[2]' >> script/搜索冫伪素数牜临近幂方.py..2.16-_.max200.2-SPRP.out.txt
    #
diff script/搜索冫伪素数牜临近幂方.py..2.16-_.max200.2-SPRP.out.txt script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt
('script.搜索冫伪素数牜临近幂方._0worker_', (2, 1, 200, [2]), {})
rm script/搜索冫伪素数牜临近幂方.py..2.16-_.max200.2-SPRP.out.txt

py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,main  =2  =16 =3000+1   =1 =200  --may_prime_basis='[2]' --path:script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt
view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.max200.2-SPRP.out.txt



######################
#py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,迭代搜索冫偏移量纟伪素数牜临近幂方扌  '=[2]'  '=range(16, 3000+1)' =4 --scale_vs_max4offset_vs_count=2 --may_prime_basis='[2]' >> script/搜索冫伪素数牜临近幂方.py..2.16-_.sz4.2-SPRP.out.txt
#view script/搜索冫伪素数牜临近幂方.py..2.16-_.sz4.2-SPRP.out.txt
    (2, 16, -4, (2,), [-15, -17, -39, -57], [1, 3, 7, 15])
    ...
    (2, 1246, -4, (2,), [-165, -633, -1265, -1301], [139, 2277, 7665, 9613])
    ...
#du -h script/搜索冫伪素数牜临近幂方.py..2.16-_.sz4.2-SPRP.out.txt
    84K@1246
#diff script/搜索冫伪素数牜临近幂方.py..2.16-_.sz4.2-SPRP.out.txt  script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt
    #diff since ++header
('script.搜索冫伪素数牜临近幂方._0worker_', (2, 2, 4, [2]), {})
rm script/搜索冫伪素数牜临近幂方.py..2.16-_.sz4.2-SPRP.out.txt

def main(base, begin_exp, end_exp, scale_vs_max4offset_vs_count, scale_or_max4offset_or_count, may_prime_basis, path, kwds4cls={}, **kwds4run):
py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,main  =2  =16 =3000+1   =2 =4  --may_prime_basis='[2]' --path:script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt
view script/搜索冫伪素数牜临近幂方.py..header.2.16-_.sz4.2-SPRP.out.txt


######################

]]]'''#'''
__all__ = r'''
main

枚举冫偏移量纟伪素数牜临近扌
搜索冫偏移量纟伪素数牜临近幂方扌
迭代搜索冫偏移量纟伪素数牜临近幂方扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import dropwhile, takewhile, product, islice, filterfalse
from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt, check_non_ABC
from seed.abc.abc__ver1 import abstractmethod, override, ABC

from seed.math.prime_gens import prime_gen
from seed.math.prime_gens import mk_tribool_delegate5PRP_test_, is_strong_pseudoprime__basis__with_trial_division_
    # 替代:is_prime__tribool_
    #def is_prime__tribool_(n, /, *, case:[Case4is_prime__tribool_,tuple], skip_check=False, skip_A014233=False, params4is_strong_pseudoprime__basis__with_trial_division_=None):
    # (xfilter4continuous_bases4div, bases4SPRP) = params4is_strong_pseudoprime__basis__with_trial_division_
from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__tribool_
#def is_strong_pseudoprime__basis_(basis, n, /, *, to_find_sqrt_neg1=False):
    #basis-SPRP
from seed.math.prime_gens import iter_pseudoprimes__inside_, iter_pseudoprimes__ge_lt_# iter_pseudoprimes__between_

from seed.math.prime_gens import next_pseudoprime__ge_, prev_may_pseudoprime__lt_
from seed.math.prime_gens import iter_pseudoprimes__ge_, reversed_iter_pseudoprimes__lt_

from seed.io.continue_io__naive import ILineContinueIO, ILineContinueIO__mixins__init# LineContinueIO__offset_args0
    #LineContinueIO__offset_args0(offset4lineno, path, encoding, qnm4worker, args4worker, kwds4worker)

___end_mark_of_excluded_global_names__0___ = ...


def 枚举冫偏移量纟伪素数牜临近扌(u, /, *, reverse, **kwds):
    check_type_is(bool, reverse)
    check_int_ge(0, u)
    f = reversed_iter_pseudoprimes__lt_ if reverse else iter_pseudoprimes__ge_
    return map(u.__rsub__, f(u, **kwds))
def 搜索冫偏移量纟伪素数牜临近幂方扌(base, exp, /, max4offset_or_count, *, max4offset_vs_count=False, may_prime_basis=None):
    check_int_ge(2, base)
    check_int_ge(1, exp)
    check_int_ge(1, max4offset_or_count)
    check_type_is(bool, max4offset_vs_count)

    if not may_prime_basis is None:
        may_prime_basis = tuple(may_prime_basis)
        bases4test = prime_basis = (may_prime_basis)
        kwds = dict(case=prime_basis, skip_A014233=True)
    else:
        kwds = dict(case=None, skip_A014233=False)
    kwds
    if 1:
        #new-version:USING_is_strong_pseudoprime__basis__with_trial_division_:here
      if not may_prime_basis is None:
        xfilter4continuous_bases4div = None
        bases4SPRP = prime_basis
        #kwds = dict(params4is_strong_pseudoprime__basis__with_trial_division_ = (xfilter4continuous_bases4div, bases4SPRP))
        delegate = mk_tribool_delegate5PRP_test_(is_strong_pseudoprime__basis__with_trial_division_, xfilter4continuous_bases4div, bases4SPRP)
        kwds = dict(case=delegate)
    kwds

    pw = base**exp
    if max4offset_vs_count:
        count = max4offset_or_count
        xctrl = -count
        assert xctrl < 0
        neg_offsets = [*islice(枚举冫偏移量纟伪素数牜临近扌(pw, reverse=True, **kwds), count)]
        pos_offsets = [*islice(枚举冫偏移量纟伪素数牜临近扌(pw, reverse=False, **kwds), count)]
    else:
        max4offset = max4offset_or_count
        xctrl = +max4offset
        assert xctrl > 0
        #old-version: slow since go beyond range until first SPRP
        #.neg_offsets = [*takewhile((-max4offset).__le__, 枚举冫偏移量纟伪素数牜临近扌(pw, reverse=True))]
        #.pos_offsets = [*takewhile((+max4offset).__ge__, 枚举冫偏移量纟伪素数牜临近扌(pw, reverse=False))]
        ps = iter_pseudoprimes__ge_lt_(pw-max4offset, pw+max4offset+1, **kwds)
        offsets = [*map(pw.__rsub__, ps)]
        neg_offsets = [*takewhile((0).__gt__, offsets)]
        777; neg_offsets.reverse()
        pos_offsets = [*dropwhile((0).__gt__, offsets)]
    xctrl
    neg_offsets
    pos_offsets
    assert (xctrl < 0) is max4offset_vs_count
    if may_prime_basis is None:
        return (base, exp, xctrl, neg_offsets, pos_offsets)
    else:
        prime_basis
        return (base, exp, xctrl, prime_basis, neg_offsets, pos_offsets)
def 迭代搜索冫偏移量纟伪素数牜临近幂方扌(bases, exps, scale_or_max4offset_or_count, /, *, may_prime_basis=None, scale_vs_max4offset_vs_count=0):
    check_int_ge_lt(0, 3, scale_vs_max4offset_vs_count)
    check_int_ge(1, scale_or_max4offset_or_count)
    b_scale = False
    max4offset_vs_count = False
    match scale_vs_max4offset_vs_count:
        case 0:
            scale4max4offset = scale_or_max4offset_or_count
            b_scale = True
        case 1:
            max4offset = scale_or_max4offset_or_count
            max4offset_or_count = max4offset
        case 2:
            count = scale_or_max4offset_or_count
            #raise NotImplementedError(scale_vs_max4offset_vs_count)
            max4offset_or_count = count
            max4offset_vs_count = True
        case _:
            raise Exception(scale_vs_max4offset_vs_count)
    max4offset_vs_count
    b_scale
    #######
    kwds = dict(may_prime_basis=may_prime_basis, max4offset_vs_count=max4offset_vs_count)
    if not b_scale:
        kwds.update(max4offset_or_count=max4offset_or_count)
    #######
    kwds
    b_scale
        #?scale4max4offset
    #######
    999; lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref to avoid recomputing PRIMES
    for base, exp in product(bases, exps):
        if b_scale:
            max4offset = exp*scale4max4offset
            kwds.update(max4offset_or_count=max4offset)
        yield 搜索冫偏移量纟伪素数牜临近幂方扌(base, exp, **kwds)

class _乸断点续搜冫偏移量纟伪素数牜临近幂方扌(ILineContinueIO__mixins__init):
    r'''[[[
    迭代搜索冫偏移量纟伪素数牜临近幂方扌(bases, exps, scale_or_max4offset_or_count, /, *, may_prime_basis=None, scale_vs_max4offset_vs_count=0)
    ==>>:
    [args4worker = (base, scale_vs_max4offset_vs_count, scale_or_max4offset_or_count, may_prime_basis)]
    [kwds4worker := {}]
    ==>>:
    # [updated_args4worker == (begin_exp, base, scale_vs_max4offset_vs_count, scale_or_max4offset_or_count, may_prime_basis)]
    [updated_args4worker := (begin_exp:=last_lineno+sf.offset4lineno, *args4worker)]
    [updated_kwds4worker := kwds4worker]
    [extra_kwds4worker == {end_exp=?}]
    [worker :: ((*updated_args4worker, **updated_kwds4worker, **extra_kwds4worker) -> Iterator record)]

    #]]]'''#'''
    #_乸断点续搜冫偏移量纟伪素数牜临近幂方扌(offset4lineno, path, args4worker, qnm4worker=?, kwds4worker={}, encoding='u8')
    def __init__(sf, /, offset4lineno, path, args4worker, qnm4worker=f'{__name__}._0worker_', kwds4worker={}, encoding='u8'):
        check_type_is(int, offset4lineno)
        super().__init__(path, encoding, qnm4worker, args4worker, kwds4worker)
        sf._offset = offset4lineno
        sf._init4repr(offset4lineno, path, args4worker, qnm4worker, kwds4worker, encoding)

    @property
    def offset4lineno(sf, /):
        '-> offset4lineno/int'
        return sf._offset
    @override
    def _update_settings_(sf, last_lineno, tmay_last_record, args4worker, kwds4worker, /):
        'last_lineno -> tmay_last_record -> args4worker -> kwds4worker -> updated_settings/(updated_args4worker, updated_kwds4worker)'
        updated_args4worker = (begin_exp:=last_lineno+sf.offset4lineno, *args4worker)
        updated_kwds4worker = kwds4worker
        updated_settings = (updated_args4worker, updated_kwds4worker)
        if tmay_last_record:
            [last_record] = tmay_last_record
            last_exp = last_record[1]
            assert begin_exp == last_exp+1
        return updated_settings
check_non_ABC(_乸断点续搜冫偏移量纟伪素数牜临近幂方扌)

def _0worker_(begin_exp, base, scale_vs_max4offset_vs_count, scale_or_max4offset_or_count, may_prime_basis, /, end_exp):
    return 迭代搜索冫偏移量纟伪素数牜临近幂方扌([base], exps:=range(begin_exp, end_exp), scale_or_max4offset_or_count, may_prime_basis=may_prime_basis, scale_vs_max4offset_vs_count=scale_vs_max4offset_vs_count)
def main(base, begin_exp, end_exp, scale_vs_max4offset_vs_count, scale_or_max4offset_or_count, may_prime_basis, path, kwds4cls={}, **kwds4run):
    args4worker = (base, scale_vs_max4offset_vs_count, scale_or_max4offset_or_count, may_prime_basis)
    extra_kwds4worker = dict(end_exp=end_exp)
    offset4lineno = begin_exp
    with _乸断点续搜冫偏移量纟伪素数牜临近幂方扌(offset4lineno, path, args4worker, **kwds4cls) as sf:
        #def iter_run_(sf, /, *, also_to_stderr=False, to_postpone_KeyboardInterrupt_until_yield=False, prompt_string4postpone_KeyboardInterrupt_until_yield=None, extra_kwds4worker=None):
        yield from sf.iter_run_(extra_kwds4worker=extra_kwds4worker, **kwds4run)

def _重检牜记录扌(base, exp, may_prime_basis, neg_offsets, pos_offsets, 仅试除, 欤重建):
    '-> (Iter (base, exp, may_prime_basis, bad_offset)) if not 欤重建 else (Iter (base, exp, may_prime_basis, neg_offsets, pos_offsets))'
    _may_prime_basis = () if 仅试除 else may_prime_basis
    offsets = [*neg_offsets, *pos_offsets]
    bad_offsets = set()
    pw = base**exp
    for offset in offsets:
        u = pw + offset
        if False is is_prime__tribool_(u, case=_may_prime_basis):
            if not 欤重建:
                yield (base, exp, may_prime_basis, bad_offset:=offset)
            else:
                bad_offsets.add(offset)
    if 欤重建:
        neg_offsets = [*filterfalse(bad_offsets.__contains__, neg_offsets)]
        pos_offsets = [*filterfalse(bad_offsets.__contains__, pos_offsets)]
        yield (base, exp, may_prime_basis, neg_offsets, pos_offsets)
def _重检牜文件扌(path, 仅试除=True, 欤重建=True):
    '-> (Iter (base, exp, may_prime_basis, bad_offset)) if not 欤重建 else (Iter [?header?; record...])'
    '因为补丁新增试除'
    check_type_is(bool, 仅试除)
    check_type_is(bool, 欤重建)
    with open(path, 'rt', encoding='u8') as ifile:
        for lineno, line in enumerate(ifile):
            row = eval(line)
            x0 = row[0]
            if type(x0) is str:
                if not lineno == 0:raise Exception(path, lineno, line)
                # header.qnm4worker
                if 欤重建:
                    yield row
                continue
            if len(row) == 5:
                # [may_prime_basis is None]
                (base, exp, _2, neg_offsets, pos_offsets) = row
                may_prime_basis = None
                if 欤重建:
                    tm = ()
            elif len(row) == 6:
                # [not may_prime_basis is None]
                (base, exp, _2, prime_basis, neg_offsets, pos_offsets) = row
                check_type_is(tuple, prime_basis)
                may_prime_basis = prime_basis
                if 欤重建:
                    tm = (prime_basis,)
            else:
                raise Exception(path, lineno, line)
            it = _重检牜记录扌(base, exp, may_prime_basis, neg_offsets, pos_offsets, 仅试除, 欤重建)
            if not 欤重建:
                yield from it
            else:
                for (base, exp, may_prime_basis, neg_offsets, pos_offsets) in it:
                    yield (base, exp, _2, *tm, neg_offsets, pos_offsets)
__all__
from script.搜索冫伪素数牜临近幂方 import 枚举冫偏移量纟伪素数牜临近扌,搜索冫偏移量纟伪素数牜临近幂方扌,迭代搜索冫偏移量纟伪素数牜临近幂方扌
from script.搜索冫伪素数牜临近幂方 import *
