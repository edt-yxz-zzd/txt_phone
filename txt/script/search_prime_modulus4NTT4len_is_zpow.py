#__all__:goto
r'''[[[
e script/search_prime_modulus4NTT4len_is_zpow.py
view ../../python3_src/seed/math/primality_proving__plain.py
    see:seed.math.primality_proving__plain:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
view /storage/emulated/0/0my_files/book/math/fxtbook[Matters Computational][Algorithms for Programmers].pdf
#???#view script/辅助冫幂方判定.py

script.search_prime_modulus4NTT4len_is_zpow
py -m nn_ns.app.debug_cmd   script.search_prime_modulus4NTT4len_is_zpow -x # -off_defs
py -m nn_ns.app.doctest_cmd script.search_prime_modulus4NTT4len_is_zpow:__doc__ -ht # -ff -df



[[
py_adhoc_call   script.search_prime_modulus4NTT4len_is_zpow   ,iter_ex_prime_moduli4NTT4len_is_zpow_  +only_zpow_dominance   --min0_log2_zpow=4  --may_max1_log2_zpow=None   --min0_prime_modulus='2**3' --max1_prime_modulus='2**10'
((-8, 1), 0x101, 3)
((-8, 3), 0x301, 7)
((-7, 5), 0x281, 3)
((-6, 3), 0xC1, 5)
((-6, 7), 0x1C1, 3)
((-6, 9), 0x241, 5)
((-5, 3), 0x61, 5)
((-5, 11), 0x161, 3)
((-5, 21), 0x2A1, 5)
((-5, 29), 0x3A1, 3)
((-4, 1), 0x11, 3)
((-4, 7), 0x71, 3)
((-4, 15), 0xF1, 7)
#if[min0_log2_zpow:=3]:++((-3, 5), 0x29, 3)

]]
[[
py_adhoc_call   script.search_prime_modulus4NTT4len_is_zpow   ,iter_ex_prime_moduli4NTT4len_is_zpow_  +only_zpow_dominance   --min0_log2_zpow=4  --may_max1_log2_zpow=None   --min0_prime_modulus='2**8' --max1_prime_modulus='2**16'
((-13, 5), 0xA001, 3)
((-12, 3), 0x3001, 11)
((-12, 15), 0xF001, 11)
((-11, 9), 0x4801, 5)
((-11, 29), 0xE801, 3)
((-10, 13), 0x3401, 3)
((-10, 15), 0x3C01, 7)
((-10, 19), 0x4C01, 3)
((-10, 25), 0x6401, 3)
((-10, 37), 0x9401, 3)
((-10, 39), 0x9C01, 5)
((-10, 49), 0xC401, 3)
((-10, 57), 0xE401, 7)
((-10, 63), 0xFC01, 5)
((-9, 15), 0x1E01, 13)
((-9, 21), 0x2A01, 5)
((-9, 23), 0x2E01, 3)
((-9, 35), 0x4601, 3)
((-9, 45), 0x5A01, 11)
((-9, 51), 0x6601, 5)
((-9, 63), 0x7E01, 5)
((-9, 71), 0x8E01, 3)
((-9, 89), 0xB201, 3)
((-9, 101), 0xCA01, 3)
((-8, 1), 0x101, 3)
((-8, 3), 0x301, 7)
((-8, 13), 0xD01, 3)
((-8, 31), 0x1F01, 3)
((-8, 37), 0x2501, 3)
((-8, 55), 0x3701, 3)
((-8, 57), 0x3901, 5)
((-8, 87), 0x5701, 5)
((-8, 91), 0x5B01, 3)
((-8, 105), 0x6901, 11)
((-8, 121), 0x7901, 3)
((-8, 123), 0x7B01, 7)
((-8, 141), 0x8D01, 5)
((-8, 147), 0x9301, 5)
((-8, 157), 0x9D01, 3)
((-8, 163), 0xA301, 3)
((-8, 171), 0xAB01, 5)
((-8, 181), 0xB501, 3)
((-8, 193), 0xC101, 3)
((-8, 195), 0xC301, 19)
((-8, 223), 0xDF01, 3)
((-8, 225), 0xE101, 7)
((-8, 235), 0xEB01, 3)
((-7, 5), 0x281, 3)
((-7, 9), 0x481, 5)
((-7, 11), 0x581, 3)
((-7, 21), 0xA81, 13)
((-7, 27), 0xD81, 5)
((-7, 35), 0x1181, 3)
((-7, 39), 0x1381, 5)
((-7, 51), 0x1981, 7)
((-7, 57), 0x1C81, 5)
((-7, 75), 0x2581, 13)
((-7, 77), 0x2681, 3)
((-7, 81), 0x2881, 11)
((-7, 89), 0x2C81, 3)
((-7, 95), 0x2F81, 3)
((-7, 105), 0x3481, 11)
((-7, 107), 0x3581, 3)
((-7, 119), 0x3B81, 3)
((-7, 125), 0x3E81, 3)
((-6, 7), 0x1C1, 3)
((-6, 9), 0x241, 5)
((-6, 19), 0x4C1, 3)
((-6, 25), 0x641, 3)
((-6, 33), 0x841, 5)
((-6, 43), 0xAC1, 3)
((-6, 49), 0xC41, 3)
((-5, 11), 0x161, 3)
((-5, 21), 0x2A1, 5)
((-5, 29), 0x3A1, 3)
]]
[[
py_adhoc_call   script.search_prime_modulus4NTT4len_is_zpow   ,iter_ex_prime_moduli4NTT4len_is_zpow_  +only_zpow_dominance   --min0_log2_zpow=27  --may_max1_log2_zpow=None   --min0_prime_modulus='2**30' --max1_prime_modulus='2**32'
((-30, 3), 0xC0000001, 5)
((-28, 13), 0xD0000001, 3)
((-27, 15), 0x78000001, 11)
((-27, 17), 0x88000001, 3)
((-27, 29), 0xE8000001, 3)
]]
[[
py_adhoc_call   script.search_prime_modulus4NTT4len_is_zpow   ,iter_ex_prime_moduli4NTT4len_is_zpow_  +only_zpow_dominance   --min0_log2_zpow=27  --may_max1_log2_zpow=28   --min0_prime_modulus='2**30' --max1_prime_modulus='2**32'
((-27, 15), 0x78000001, 11)
((-27, 17), 0x88000001, 3)
((-27, 29), 0xE8000001, 3)
]]
[[
py_adhoc_call   script.search_prime_modulus4NTT4len_is_zpow   ,iter_ex_prime_moduli4NTT4len_is_zpow_  +only_zpow_dominance   --min0_log2_zpow=54  --may_max1_log2_zpow=None   --min0_prime_modulus='2**62' --max1_prime_modulus='2**64'
((-59, 27), 0xD800000000000001, 5)
((-57, 71), 0x8E00000000000001, 3)
((-57, 75), 0x9600000000000001, 7)
((-57, 95), 0xBE00000000000001, 3)
((-57, 123), 0xF600000000000001, 5)
((-56, 87), 0x5700000000000001, 5)
((-56, 175), 0xAF00000000000001, 3)
((-56, 235), 0xEB00000000000001, 3)
((-56, 247), 0xF700000000000001, 3)
((-55, 131), 0x4180000000000001, 3)
((-55, 197), 0x6280000000000001, 3)
((-55, 285), 0x8E80000000000001, 11)
((-55, 329), 0xA480000000000001, 3)
((-55, 357), 0xB280000000000001, 5)
((-55, 359), 0xB380000000000001, 3)
((-55, 411), 0xCD80000000000001, 11)
((-55, 429), 0xD680000000000001, 5)
((-54, 333), 0x5340000000000001, 5)
((-54, 429), 0x6B40000000000001, 5)
((-54, 439), 0x6DC0000000000001, 3)
((-54, 477), 0x7740000000000001, 11)
((-54, 505), 0x7E40000000000001, 3)
((-54, 595), 0x94C0000000000001, 3)
((-54, 603), 0x96C0000000000001, 5)
((-54, 637), 0x9F40000000000001, 3)
((-54, 669), 0xA740000000000001, 5)
((-54, 705), 0xB040000000000001, 7)
((-54, 817), 0xCC40000000000001, 3)
((-54, 847), 0xD3C0000000000001, 3)
((-54, 925), 0xE740000000000001, 3)
]]
[[
[int(2**61.99) == 4579830776212149248]
>>> int(2**61.99)
4579830776212149248
>>> 2**62 -int(2**61.99)
31855242215238656
>>> (2**62 -int(2**61.99)).bit_length()
55

py_adhoc_call   script.search_prime_modulus4NTT4len_is_zpow   ,1000:iter_ex_prime_moduli4NTT4len_is_zpow_  +only_zpow_dominance   --min0_log2_zpow=44  --may_max1_log2_zpow=None   --min0_prime_modulus='int(2**61.99)' --max1_prime_modulus='2**62'
((-50, 4087), 0x3FDC000000000001, 3)
((-49, 8141), 0x3F9A000000000001, 3)
((-49, 8163), 0x3FC6000000000001, 5)
((-48, 16291), 0x3FA3000000000001, 3)
((-47, 32627), 0x3FB9800000000001, 3)
((-47, 32715), 0x3FE5800000000001, 7)
((-47, 32721), 0x3FE8800000000001, 7)
((-46, 65097), 0x3F92400000000001, 19)
((-46, 65263), 0x3FBBC00000000001, 3)
((-46, 65317), 0x3FC9400000000001, 3)
((-46, 65319), 0x3FC9C00000000001, 5)
((-46, 65365), 0x3FD5400000000001, 3)
((-46, 65455), 0x3FEBC00000000001, 3)
((-46, 65515), 0x3FFAC00000000001, 3)
((-46, 65535), 0x3FFFC00000000001, 7)
((-45, 130181), 0x3F90A00000000001, 3)
((-45, 130215), 0x3F94E00000000001, 17)
((-45, 130295), 0x3F9EE00000000001, 3)
((-45, 130389), 0x3FAAA00000000001, 11)
((-45, 130425), 0x3FAF200000000001, 13)
((-45, 130431), 0x3FAFE00000000001, 5)
((-45, 130553), 0x3FBF200000000001, 3)
((-45, 130581), 0x3FC2A00000000001, 5)
((-45, 130583), 0x3FC2E00000000001, 3)
((-45, 130589), 0x3FC3A00000000001, 3)
((-45, 130719), 0x3FD3E00000000001, 11)
((-45, 130809), 0x3FDF200000000001, 23)
((-45, 130851), 0x3FE4600000000001, 5)
((-45, 130853), 0x3FE4A00000000001, 3)
((-45, 130869), 0x3FE6A00000000001, 7)
((-45, 130883), 0x3FE8600000000001, 3)
((-45, 130919), 0x3FECE00000000001, 3)
((-45, 131003), 0x3FF7600000000001, 3)
((-45, 131013), 0x3FF8A00000000001, 5)
((-44, 260371), 0x3F91300000000001, 3)
((-44, 260403), 0x3F93300000000001, 7)
((-44, 260463), 0x3F96F00000000001, 13)
((-44, 260667), 0x3FA3B00000000001, 5)
((-44, 260743), 0x3FA8700000000001, 3)
((-44, 260763), 0x3FA9B00000000001, 11)
((-44, 260805), 0x3FAC500000000001, 13)
((-44, 260887), 0x3FB1700000000001, 3)
((-44, 260901), 0x3FB2500000000001, 5)
((-44, 261001), 0x3FB8900000000001, 3)
((-44, 261123), 0x3FC0300000000001, 13)
((-44, 261135), 0x3FC0F00000000001, 13)
((-44, 261163), 0x3FC2B00000000001, 3)
((-44, 261165), 0x3FC2D00000000001, 13)
((-44, 261181), 0x3FC3D00000000001, 3)
((-44, 261201), 0x3FC5100000000001, 5)
((-44, 261237), 0x3FC7500000000001, 5)
((-44, 261277), 0x3FC9D00000000001, 3)
((-44, 261313), 0x3FCC100000000001, 3)
((-44, 261327), 0x3FCCF00000000001, 5)
((-44, 261361), 0x3FCF100000000001, 3)
((-44, 261387), 0x3FD0B00000000001, 5)
((-44, 261391), 0x3FD0F00000000001, 3)
((-44, 261433), 0x3FD3900000000001, 3)
((-44, 261445), 0x3FD4500000000001, 3)
((-44, 261465), 0x3FD5900000000001, 7)
((-44, 261477), 0x3FD6500000000001, 5)
((-44, 261487), 0x3FD6F00000000001, 3)
((-44, 261493), 0x3FD7500000000001, 3)
((-44, 261501), 0x3FD7D00000000001, 5)
((-44, 261523), 0x3FD9300000000001, 3)
((-44, 261657), 0x3FE1900000000001, 5)
((-44, 261673), 0x3FE2900000000001, 3)
((-44, 261705), 0x3FE4900000000001, 7)
((-44, 261745), 0x3FE7100000000001, 3)
((-44, 261775), 0x3FE8F00000000001, 3)
((-44, 261853), 0x3FEDD00000000001, 3)
((-44, 261925), 0x3FF2500000000001, 3)
((-44, 262053), 0x3FFA500000000001, 7)
((-44, 262063), 0x3FFAF00000000001, 3)
((-44, 262075), 0x3FFBB00000000001, 3)
((-44, 262081), 0x3FFC100000000001, 3)
((-44, 262101), 0x3FFD500000000001, 5)
((-44, 262105), 0x3FFD900000000001, 3)
((-44, 262111), 0x3FFDF00000000001, 3)
]]
[[
py_adhoc_call   script.search_prime_modulus4NTT4len_is_zpow   ,1000:iter_ex_prime_moduli4NTT4len_is_zpow_  -only_zpow_dominance   --min0_log2_zpow=44  --may_max1_log2_zpow=None   --min0_prime_modulus='int(2**61.99)' --max1_prime_modulus='2**62'
((-50, 4087), 0x3FDC000000000001, [2, 61, 67], [50, 1, 1], (3, 2, 2))
((-49, 8141), 0x3F9A000000000001, [2, 7, 1163], [49, 1, 1], (3, 2, 2))
((-49, 8163), 0x3FC6000000000001, [2, 3, 907], [49, 2, 1], (5, 3, 2))
((-48, 16291), 0x3FA3000000000001, [2, 11, 1481], [48, 1, 1], (3, 2, 2))
((-47, 32627), 0x3FB9800000000001, [2, 7, 59, 79], [47, 1, 1, 1], (3, 2, 2, 2))
((-47, 32715), 0x3FE5800000000001, [2, 3, 5, 727], [47, 2, 1, 1], (7, 2, 2, 2))
((-47, 32721), 0x3FE8800000000001, [2, 3, 13, 839], [47, 1, 1, 1], (7, 2, 2, 2))
((-46, 65097), 0x3F92400000000001, [2, 3, 2411], [46, 3, 1], (19, 3, 2))
((-46, 65263), 0x3FBBC00000000001, [2, 11, 17, 349], [46, 1, 1, 1], (3, 2, 2, 2))
((-46, 65317), 0x3FC9400000000001, [2, 7, 31, 43], [46, 2, 1, 1], (3, 2, 2, 2))
((-46, 65319), 0x3FC9C00000000001, [2, 3, 21773], [46, 1, 1], (5, 2, 2))
((-46, 65365), 0x3FD5400000000001, [2, 5, 17, 769], [46, 1, 1, 1], (3, 2, 2, 2))
((-46, 65455), 0x3FEBC00000000001, [2, 5, 13, 19, 53], [46, 1, 1, 1, 1], (3, 2, 3, 2, 2))
((-46, 65515), 0x3FFAC00000000001, [2, 5, 13103], [46, 1, 1], (3, 2, 2))
((-46, 65535), 0x3FFFC00000000001, [2, 3, 5, 17, 257], [46, 1, 1, 1, 1], (7, 2, 3, 2, 2))
((-45, 130181), 0x3F90A00000000001, [2, 29, 67], [45, 1, 2], (3, 2, 2))
((-45, 130215), 0x3F94E00000000001, [2, 3, 5, 8681], [45, 1, 1, 1], (17, 2, 3, 2))
((-45, 130295), 0x3F9EE00000000001, [2, 5, 11, 23, 103], [45, 1, 1, 1, 1], (3, 3, 2, 2, 2))
((-45, 130389), 0x3FAAA00000000001, [2, 3, 7, 887], [45, 1, 2, 1], (11, 2, 3, 2))
((-45, 130425), 0x3FAF200000000001, [2, 3, 5, 37, 47], [45, 1, 2, 1, 1], (13, 2, 2, 2, 2))
((-45, 130431), 0x3FAFE00000000001, [2, 3, 7, 6211], [45, 1, 1, 1], (5, 3, 3, 2))
((-45, 130553), 0x3FBF200000000001, [2, 130553], [45, 1], (3, 2))
((-45, 130581), 0x3FC2A00000000001, [2, 3, 11, 1319], [45, 2, 1, 1], (5, 5, 2, 2))
((-45, 130583), 0x3FC2E00000000001, [2, 67, 1949], [45, 1, 1], (3, 2, 2))
((-45, 130589), 0x3FC3A00000000001, [2, 130589], [45, 1], (3, 2))
((-45, 130719), 0x3FD3E00000000001, [2, 3, 43573], [45, 1, 1], (11, 3, 2))
((-45, 130809), 0x3FDF200000000001, [2, 3, 7, 6229], [45, 1, 1, 1], (23, 2, 2, 2))
((-45, 130851), 0x3FE4600000000001, [2, 3, 7, 31, 67], [45, 2, 1, 1, 1], (5, 2, 2, 2, 2))
((-45, 130853), 0x3FE4A00000000001, [2, 19, 71, 97], [45, 1, 1, 1], (3, 2, 2, 2))
((-45, 130869), 0x3FE6A00000000001, [2, 3, 37, 131], [45, 3, 1, 1], (7, 2, 2, 2))
((-45, 130883), 0x3FE8600000000001, [2, 17, 7699], [45, 1, 1], (3, 3, 2))
((-45, 130919), 0x3FECE00000000001, [2, 89, 1471], [45, 1, 1], (3, 2, 2))
((-45, 131003), 0x3FF7600000000001, [2, 269, 487], [45, 1, 1], (3, 2, 2))
((-45, 131013), 0x3FF8A00000000001, [2, 3, 14557], [45, 2, 1], (5, 3, 2))
((-44, 260371), 0x3F91300000000001, [2, 83, 3137], [44, 1, 1], (3, 2, 2))
((-44, 260403), 0x3F93300000000001, [2, 3, 11, 13, 607], [44, 1, 1, 1, 1], (7, 2, 2, 2, 2))
((-44, 260463), 0x3F96F00000000001, [2, 3, 7, 79, 157], [44, 1, 1, 1, 1], (13, 2, 2, 2, 2))
((-44, 260667), 0x3FA3B00000000001, [2, 3, 11, 2633], [44, 2, 1, 1], (5, 2, 2, 2))
((-44, 260743), 0x3FA8700000000001, [2, 7, 193], [44, 1, 2], (3, 2, 2))
((-44, 260763), 0x3FA9B00000000001, [2, 3, 17, 5113], [44, 1, 1, 1], (11, 2, 2, 2))
((-44, 260805), 0x3FAC500000000001, [2, 3, 5, 17387], [44, 1, 1, 1], (13, 5, 3, 2))
((-44, 260887), 0x3FB1700000000001, [2, 11, 37, 641], [44, 1, 1, 1], (3, 2, 2, 2))
((-44, 260901), 0x3FB2500000000001, [2, 3, 3221], [44, 4, 1], (5, 3, 2))
((-44, 261001), 0x3FB8900000000001, [2, 13, 17, 1181], [44, 1, 1, 1], (3, 2, 3, 2))
((-44, 261123), 0x3FC0300000000001, [2, 3, 87041], [44, 1, 1], (13, 3, 2))
((-44, 261135), 0x3FC0F00000000001, [2, 3, 5, 7, 829], [44, 2, 1, 1, 1], (13, 2, 3, 2, 2))
((-44, 261163), 0x3FC2B00000000001, [2, 7, 37309], [44, 1, 1], (3, 2, 2))
((-44, 261165), 0x3FC2D00000000001, [2, 3, 5, 23, 757], [44, 1, 1, 1, 1], (13, 7, 2, 2, 2))
((-44, 261181), 0x3FC3D00000000001, [2, 139, 1879], [44, 1, 1], (3, 2, 2))
((-44, 261201), 0x3FC5100000000001, [2, 3, 83, 1049], [44, 1, 1, 1], (5, 3, 2, 2))
((-44, 261237), 0x3FC7500000000001, [2, 3, 31, 53], [44, 1, 1, 2], (5, 2, 2, 2))
((-44, 261277), 0x3FC9D00000000001, [2, 227, 1151], [44, 1, 1], (3, 2, 2))
((-44, 261313), 0x3FCC100000000001, [2, 13, 20101], [44, 1, 1], (3, 2, 2))
((-44, 261327), 0x3FCCF00000000001, [2, 3, 11, 7919], [44, 1, 1, 1], (5, 2, 2, 2))
((-44, 261361), 0x3FCF100000000001, [2, 31, 8431], [44, 1, 1], (3, 2, 2))
((-44, 261387), 0x3FD0B00000000001, [2, 3, 7, 461], [44, 4, 1, 1], (5, 2, 2, 2))
((-44, 261391), 0x3FD0F00000000001, [2, 13, 20107], [44, 1, 1], (3, 2, 2))
((-44, 261433), 0x3FD3900000000001, [2, 261433], [44, 1], (3, 2))
((-44, 261445), 0x3FD4500000000001, [2, 5, 52289], [44, 1, 1], (3, 2, 2))
((-44, 261465), 0x3FD5900000000001, [2, 3, 5, 17431], [44, 1, 1, 1], (7, 5, 2, 2))
((-44, 261477), 0x3FD6500000000001, [2, 3, 17, 1709], [44, 2, 1, 1], (5, 2, 2, 2))
((-44, 261487), 0x3FD6F00000000001, [2, 23, 11369], [44, 1, 1], (3, 2, 2))
((-44, 261493), 0x3FD7500000000001, [2, 29, 71, 127], [44, 1, 1, 1], (3, 2, 2, 2))
((-44, 261501), 0x3FD7D00000000001, [2, 3, 67, 1301], [44, 1, 1, 1], (5, 2, 2, 2))
((-44, 261523), 0x3FD9300000000001, [2, 261523], [44, 1], (3, 2))
((-44, 261657), 0x3FE1900000000001, [2, 3, 11, 881], [44, 3, 1, 1], (5, 3, 2, 2))
((-44, 261673), 0x3FE2900000000001, [2, 261673], [44, 1], (3, 2))
((-44, 261705), 0x3FE4900000000001, [2, 3, 5, 73, 239], [44, 1, 1, 1, 1], (7, 3, 2, 2, 2))
((-44, 261745), 0x3FE7100000000001, [2, 5, 11, 4759], [44, 1, 1, 1], (3, 2, 2, 2))
((-44, 261775), 0x3FE8F00000000001, [2, 5, 37, 283], [44, 2, 1, 1], (3, 2, 3, 2))
((-44, 261853), 0x3FEDD00000000001, [2, 401, 653], [44, 1, 1], (3, 2, 2))
((-44, 261925), 0x3FF2500000000001, [2, 5, 10477], [44, 2, 1], (3, 2, 2))
((-44, 262053), 0x3FFA500000000001, [2, 3, 11, 2647], [44, 2, 1, 1], (7, 2, 2, 2))
((-44, 262063), 0x3FFAF00000000001, [2, 503, 521], [44, 1, 1], (3, 2, 2))
((-44, 262075), 0x3FFBB00000000001, [2, 5, 11, 953], [44, 2, 1, 1], (3, 2, 2, 2))
((-44, 262081), 0x3FFC100000000001, [2, 137, 1913], [44, 1, 1], (3, 2, 2))
((-44, 262101), 0x3FFD500000000001, [2, 3, 7, 1783], [44, 1, 2, 1], (5, 2, 3, 2))
((-44, 262105), 0x3FFD900000000001, [2, 5, 19, 31, 89], [44, 1, 1, 1, 1], (3, 3, 2, 2, 2))
((-44, 262111), 0x3FFDF00000000001, [2, 262111], [44, 1], (3, 2))
]]


from script.search_prime_modulus4NTT4len_is_zpow import *
]]]'''#'''
__all__ = r'''
iter_ex_prime_moduli4NTT4len_is_zpow_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge



from seed.tiny_.HexReprInt import HEXReprInt as HexReprInt

from seed.math.floor_ceil import ceil_log2
from seed.math.prime_gens import all_prime_factors_gen #tabulate_may_factorization4uint_lt_
from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division

from seed.math.primality_proving__plain import return_version____primality_test__Nmm__plain__sqrt_case_
    #see:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
def __():
  def return_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, /, *, complete_factorization__vs__using_gcd=True):
    '-> (case, payload)/((odd_prime_case/0, j2g) | (1, witness4composite) | (2, nontrivial_factor) | (even_prime_case/3, None)) | ^ERH__fail/Fail__unknown_fine_upperbound4primitive_root | ^ValueError__not_complete_factorization | ^ValueError__not_sqrt_case'

___end_mark_of_excluded_global_names__0___ = ...




def iter_ex_prime_moduli4NTT4len_is_zpow_(*, min0_log2_zpow, may_max1_log2_zpow, min0_prime_modulus, max1_prime_modulus, only_zpow_dominance:bool):
    '-> Iter (((-log2_zpow4Pmm, odd_part4Pmm), prime_modulus, j2prime_factor4Pmm, j2exp4ft4Pmm, j2partial_primitive_root4ft4Pmm) if not only_zpow_dominance else ((-ez{log2_zpow4Pmm}, odd_part4Pmm), prime_modulus, gz{partial_primitive_root4zpow4Pmm})) # [sorted by:(-log2_zpow4Pmm, odd_part4Pmm)] # [prime_modulus == odd_part4Pmm*2**log2_zpow4Pmm == II_p2e_(dict(zip(j2prime_factor4Pmm, j2exp4ft4Pmm)))]'
    #lower_bound4prime_modulus, upper_bound4prime_modulus
    check_type_is(bool, only_zpow_dominance)
    check_int_ge(0, min0_log2_zpow)
    if not may_max1_log2_zpow is None:
        max1_log2_zpow = may_max1_log2_zpow
        check_int_ge(0, max1_log2_zpow)
    check_int_ge(0, min0_prime_modulus)
    check_int_ge(0, max1_prime_modulus)
    if not min0_prime_modulus < max1_prime_modulus:
        return
    # [0 <= min0_prime_modulus < max1_prime_modulus]

    _max1_log2_zpow = ceil_log2(max1_prime_modulus)
    max1_log2_zpow = min(max1_log2_zpow, _max1_log2_zpow) if not may_max1_log2_zpow is None else _max1_log2_zpow
    min0_log2_zpow = max(1, min0_log2_zpow)
    if not min0_log2_zpow < max1_log2_zpow:
        return
    # [1 <= min0_log2_zpow < max1_log2_zpow]

    if only_zpow_dominance:
        g = _iter4test_ez_odd__zpow_dominance_
    else:
        f = _iter4test_ez_odd__p2e_
        u2ps = all_prime_factors_gen()
            # hold weakref
        def u2p2e_(u, /):
            # u > 0
            ps = u2ps[u]
            (p2e, _1) = semi_factor_pint_via_trial_division(ps, u)
            assert _1 == 1
            return p2e

    min0_Pmm = min0_prime_modulus -1
    max1_Pmm = max1_prime_modulus -1
    for ez in reversed(range(min0_log2_zpow, max1_log2_zpow)):
        # [ez == log2_zpow4Pmm]
        # [ez >= min0_log2_zpow >= 1]
        zpow = 1<<ez
        # [p == (odd<<ez) +1]
        # [min0_Pmm/2**ez <= odd == (p-1)/2**ez < max1_Pmm/2**ez]
        # [ceil(min0_Pmm/2**ez) <= odd < ceil(max1_Pmm/2**ez)]
        #min0_odd = ceil_div(min0_Pmm, zpow)
        #max1_odd = ceil_div(max1_Pmm, zpow)
        min0_odd = -((-min0_Pmm)>>ez)
        max1_odd = -((-max1_Pmm)>>ez)
        if only_zpow_dominance:
            #[Nmm is zpow_dominance]
            max1_odd = min(max1_odd, zpow)

        # [odd == 1+2*half4odd]
        # [(min0_odd-1)/2 <= half4odd == (odd-1)/2 < (max1_odd-1)/2]
        # [ceil((min0_odd-1)/2) <= half4odd < ceil((max1_odd-1)/2)]
        # [(min0_odd//2) <= half4odd < (max1_odd//2)]
        #min0_odd = (min0_odd//2)*2+1
        #max1_odd = (max1_odd//2)*2+1
        min0_odd |= 1
        max1_odd |= 1
        #u2p2e = tabulate_may_factorization4uint_lt_(max1_odd)
            # or:all_prime_factors_gen
        #for p in range((1+(min0_odd<<ez)), (1+(max1_odd<<ez)), (ez<<1)):
        for odd in range(min0_odd, max1_odd, 2):
            if only_zpow_dominance:
                yield from g(ez, odd) #_iter4test_ez_odd__zpow_dominance_
            else:
                #p2e4odd = u2p2e[odd]
                p2e4odd = u2p2e_(odd)
                yield from f(ez, odd, p2e4odd) #_iter4test_ez_odd__p2e_
def _iter4test_ez_odd__zpow_dominance_(ez, odd, /):
    '-> Iter ((-ez{log2_zpow4Pmm}, odd_part4Pmm), prime_modulus, gz{partial_primitive_root4zpow4Pmm})'
    # [only_zpow_dominance == True]
    assert (odd >> ez) == 0, (ez, odd)
    N = 1 + (odd<<ez)
    # vivi:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    j2prime_factor4ft4Nmm = (2,)
    j2exp4ft4Nmm = (ez,)
    (case, payload) = return_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, complete_factorization__vs__using_gcd=True)
    if case == 0:
        #odd_prime_case
        j2g = payload
        #gz = g2
        [gz] = j2g
        yield ((-ez, odd), HexReprInt(N), gz)
    return

def _iter4test_ez_odd__p2e_(ez, odd, p2e4odd, /):
    '-> Iter ((-log2_zpow4Pmm, odd_part4Pmm), prime_modulus, j2prime_factor4Pmm, j2exp4ft4Pmm, j2partial_primitive_root4ft4Pmm)'
    # [only_zpow_dominance == False]
    N = 1 + (odd<<ez)
    #p2e4Nmm = {2:ez, **p2e4odd}
    p_e_pairs4Nmm = [(2,ez), *sorted(p2e4odd.items())]
    j2p4Nmm = [p for p, e in p_e_pairs4Nmm]
    j2e4Nmm = [e for p, e in p_e_pairs4Nmm]

    (case, payload) = return_version____primality_test__Nmm__plain__sqrt_case_(N, j2p4Nmm, j2e4Nmm, complete_factorization__vs__using_gcd=False)
    if 0:
        assert 0 <= case < 4
        whether_prime = case in (0, 3)
    # !! [N =!= 2]
    # [case =!= 3]
    assert 0 <= case < 3
    whether_prime = case == 0
    if whether_prime:
        #j2partial_primitive_root4ft4Pmm
        j2g = payload
        yield ((-ez, odd), HexReprInt(N), j2p4Nmm, j2e4Nmm, j2g) # ((-log2_zpow4Pmm, odd_part4Pmm), prime_modulus, j2prime_factor4Pmm, j2exp4ft4Pmm, j2partial_primitive_root4ft4Pmm)
    return

__all__
from script.search_prime_modulus4NTT4len_is_zpow import *
