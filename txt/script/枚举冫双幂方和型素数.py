#__all__:goto
#TODO:goto
r'''[[[
e script/枚举冫双幂方和型素数.py
view script/枚举冫双幂方和型素数.py.out.txt
    双幂方和型素数牜非平凡平方和牜小于二的十六次方:1514行:goto
        双幂方和型素数牜非平凡平方和牜含不同双幂方和分解牜小于二的十六次方:180行:goto

    双幂方和型素数牜非平凡平方和牜小于二的二十次方:11268行:goto
        双幂方和型素数牜非平凡平方和牜含不同双幂方和分解牜小于二的二十次方:1075行:goto

    双幂方和型素数牜非平凡平方和牜小于二的二十四次方:85102行:goto
        双幂方和型素数牜非平凡平方和牜含不同双幂方和分解牜小于二的二十四次方:5950行:goto



script.枚举冫双幂方和型素数
py -m nn_ns.app.debug_cmd   script.枚举冫双幂方和型素数 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.枚举冫双幂方和型素数:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd script.枚举冫双幂方和型素数:__doc__ -ht > /sdcard/0my_files/tmp/1tmp

[[
(a**ea+b**eb)型素数
[(a**2+b**2)型素数 <==> (4*k+1)型素数]
[双幂方和型素数集牜非平凡平方和 =[def]= {p | [[a,b,ea,eb,eez::uint][a>=2][b>=1][ea>=3][eb>=2][not is_pefect_power_(a)][[is_pefect_power_(b)] <-> [b==1]][[b==1] -> [eb==2]][(ea,a) > (eb,b)][gcd(a,b)==1][gcd(ea,eb)==2**eez][p:=a**ea+b**eb][is_prime_(p)]]}]
]]

[[
目录:
    +文件类型
    +转换纟文件类型
    +数据类型
===
文件类型:
    #文件格式
    原始输出文件 :: alter_sorted_records
        RawRowFile/RRF
    非凡归组文件 :: p_sorted_alter_sorted_grouped_records++optional_epilogs
        LenGe2GroupFile/ZGF
    紧致重排文件 :: compact_file_type
        NoEpilogsCompactFile/NECF
    紧致重排文件辻窢选结束语 :: compact_file_type++optional_epilogs
        AppendEpilogsCompactFile/AECF
===
转换纟文件类型:
    [max1_p -> RRF] # 原初生成
    [RRF -> ZGF] # 归组过滤
    [RRF <-> NECF] # 紧致重排
    [ZGF <-> AECF] # 紧致重排
    [NECF -> AECF] # 直接替换[NECF <: AECF]
    [NECF -> NECF] # 缩水过滤
    <<==:
    [max1_p -> RRF] # 原初生成
        枚举冫双幂方和型素数牜非平凡平方和牜小于扌
            测试:zpow16->RRF@zpow16
    [RRF -> ZGF] # 归组过滤
        _归组过滤冫素数牜含不同双幂方和分解扌
            测试:RRF@zpow16->ZGF@zpow16
    [RRF <-> NECF] # 紧致重排
        重排格式以减小压缩包体积扌
            测试:RRF@zpow16->NECF@zpow16
        逆函数纟重排格式以减小压缩包体积扌
            测试:NECF@zpow16->RRF@zpow16
            测试:NECF@zpow16@lzma->RRF@zpow16
    [ZGF <-> AECF] # 紧致重排
        重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌
            测试:ZGF@zpow16->AECF@zpow16
        逆函数纟重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌
            测试:AECF@zpow16->ZGF@zpow16
            测试:AECF@zpow16@lzma->ZGF@zpow16
    [NECF -> AECF] # 直接替换[NECF <: AECF]
        echo
    [NECF -> NECF] # 缩水过滤
        _缩水过滤冫输出文件牜重排后牜无结束语牜压缩包扌
            测试:NECF@zpow20->NECF@zpow16
            测试:NECF@zpow20@lzma6->NECF@zpow16
    #测试用数据文件:
        RRF@zpow16
        ZGF@zpow16
        NECF@zpow16
        NECF@zpow16@lzma
        AECF@zpow16
        AECF@zpow16@lzma
        NECF@zpow20
        NECF@zpow20@lzma
        #####
        #_测试扌():goto
        #####
        \(\(测试:\|<->\|->\)\(RRF@zpow16\|ZGF@zpow16\|NECF@zpow16@lzma\|NECF@zpow16\|AECF@zpow16@lzma\|AECF@zpow16\|NECF@zpow20@lzma\|NECF@zpow20\)\)\+

===
数据类型:
    records :: [(ea, eb, a, b, p)]
        sorted_records
        alter_sorted_records # sorted by key:key4record/(ea, a, eb, b, p)
        p_sorted_alter_sorted_records # sorted by key:(p, (ea, a, eb, b))
    grouped_records :: [(p, [(ea, eb, a, b)])]
        p_sorted_alter_sorted_grouped_records # inner then outer:sorted by key:(p, (ea, a, eb, b))
    keys4records :: [(ea, a, eb, b, p)]
        #alter_sorted_keys4records
        #sorted_keys4records
    epilogs :: [(str, uint)]
        optional_epilogs
    compact_file_type :: [block4compact_file_type]
        or:compact_file_type :: [mixed_compact_record]
        block4compact_file_type :: regex"{head_line4compact_file_type}{data_line4compact_file_type}+"
            head_line4compact_file_type :: regex"[(]{ea}, {eb}[)]\n"
            data_line4compact_file_type :: regex"{pint}:{pint}(,{pint})*\n"
        block_records4compact_file_type :: (head_record4compact_file_type, *data_records4compact_file_type)
            head_record4compact_file_type :: (ea, eb)
            data_records4compact_file_type :: [data_record4compact_file_type]
            data_record4compact_file_type :: (delta_a, [delta_b])
        mixed_compact_record :: (head_record4compact_file_type|data_record4compact_file_type)
            or:mixed_compact_record :: ((ea,eb)|(delta_a,[delta_b]))

===
]]

[[
output move to:
view script/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt
view script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt
view script/枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt
view script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt
view script/枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt
view script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt
view script/枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt
view script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt
view script/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt
view script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt

ls -sSh script/枚举冫双幂方和型素数.py.*
ls -sh script/枚举冫双幂方和型素数.py.*

ls -sh script/枚举冫双幂方和型素数.py.*.out.txt
32K script/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt
260K script/枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt
2.2M script/枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt
 18M script/枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt
159M script/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt
8.0K script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt
 48K script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt
288K script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt
1.8M script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt
 11M script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt
2.8M script/枚举冫双幂方和型素数.py.out.txt


<<==:
move to:
    view script/枚举冫双幂方和型素数.py.out.txt
<<==:

===
py_adhoc_call   script.枚举冫双幂方和型素数   ,枚举冫双幂方和型素数牜非平凡平方和牜小于扌 ='2**16' > /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp
du -h /sdcard/0my_files/tmp/0tmp
    32K
    双幂方和型素数牜非平凡平方和牜小于二的十六次方:1514行:goto
===
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker=None  --_cased_doc='("path", "/sdcard/0my_files/tmp/0tmp", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker:双幂方和型素数牜非平凡平方和牜小于二的十六次方  --_cased_doc='("path", "script/枚举冫双幂方和型素数.py.out.txt", "utf8")' +to_count
du -h /sdcard/0my_files/tmp/1tmp
    8K
    # old:509行:allow is_pefect_power_
    # 180行:not is_pefect_power_
        双幂方和型素数牜非平凡平方和牜含不同双幂方和分解牜小于二的十六次方:180行:goto
... ...
(65521, [(3, 2, 33, 172), (3, 2, 40, 39)])
('num_decompositions', 1514)
('num_primes', 1320)
('num_selected_primes', 180)

mv -iv /sdcard/0my_files/tmp/0tmp script/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt
mv -iv /sdcard/0my_files/tmp/1tmp script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt

===
py_adhoc_call   script.枚举冫双幂方和型素数   ,枚举冫双幂方和型素数牜非平凡平方和牜小于扌 ='2**20' > /sdcard/0my_files/tmp/0tmp
du -h /sdcard/0my_files/tmp/0tmp
    260K
    #11268行:not is_pefect_power_
    双幂方和型素数牜非平凡平方和牜小于二的二十次方:11268行:goto
... ...
(19, 10, 2, 3, 583337)
===
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker=None  --_cased_doc='("path", "/sdcard/0my_files/tmp/0tmp", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker:双幂方和型素数牜非平凡平方和牜小于二的二十次方  --_cased_doc='("path", "script/枚举冫双幂方和型素数.py.out.txt", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
du -h /sdcard/0my_files/tmp/1tmp
    48K
    # 1075行:not is_pefect_power_
        双幂方和型素数牜非平凡平方和牜含不同双幂方和分解牜小于二的二十次方:1075行:goto
... ...
(1048361, [(3, 2, 73, 812), (4, 2, 10, 1019)])
('num_decompositions', 11268)
('num_primes', 10089)
('num_selected_primes', 1075)

mv -iv /sdcard/0my_files/tmp/0tmp script/枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt
mv -iv /sdcard/0my_files/tmp/1tmp script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt

===
py_adhoc_call   script.枚举冫双幂方和型素数   ,枚举冫双幂方和型素数牜非平凡平方和牜小于扌 ='2**32' > /sdcard/0my_files/tmp/0tmp
(3, 2, 2, 3, 17) # 第1行
... ...
(3, 2, 102, 50147, 2515782817) # 第282456行
^C KeyboardInterrupt
du -h /sdcard/0my_files/tmp/0tmp
    7.9M


===
py_adhoc_call   script.枚举冫双幂方和型素数   ,枚举冫双幂方和型素数牜非平凡平方和牜小于扌 ='2**24' > /sdcard/0my_files/tmp/0tmp
    #85102行:not is_pefect_power_
    双幂方和型素数牜非平凡平方和牜小于二的二十四次方:85102行:goto
du -h /sdcard/0my_files/tmp/0tmp
    2.2M
(3, 2, 2, 3, 17)
... ...
(23, 14, 2, 3, 13171577)
===
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker=None  --_cased_doc='("path", "/sdcard/0my_files/tmp/0tmp", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker:双幂方和型素数牜非平凡平方和牜小于二的二十四次方  --_cased_doc='("path", "script/枚举冫双幂方和型素数.py.out.txt", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
du -h /sdcard/0my_files/tmp/1tmp
    288K
    # 5950行:not is_pefect_power_
        双幂方和型素数牜非平凡平方和牜含不同双幂方和分解牜小于二的二十四次方:5950行:goto
... ...
(16775321, [(3, 2, 73, 4048), (3, 2, 178, 3337)])
('num_decompositions', 85102)
('num_primes', 78617)
('num_selected_primes', 5950)

mv -iv /sdcard/0my_files/tmp/0tmp script/枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt
mv -iv /sdcard/0my_files/tmp/1tmp script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt

===
===
py_adhoc_call   script.枚举冫双幂方和型素数   ,枚举冫双幂方和型素数牜非平凡平方和牜小于扌 ='2**28' > /sdcard/0my_files/tmp/0tmp
    #669124行:not is_pefect_power_
    双幂方和型素数牜非平凡平方和牜小于二的二十八次方:669124行:goto
du -h /sdcard/0my_files/tmp/0tmp
    18M
(3, 2, 2, 3, 17)
... ...
(27, 13, 2, 3, 135812051)
===
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker=None  --_cased_doc='("path", "/sdcard/0my_files/tmp/0tmp", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
    #py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker:双幂方和型素数牜非平凡平方和牜小于二的二十八次方  --_cased_doc='("path", "script/枚举冫双幂方和型素数.py.out.txt", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
du -h /sdcard/0my_files/tmp/1tmp
    1.8M
    # 34296行:not is_pefect_power_
        双幂方和型素数牜非平凡平方和牜含不同双幂方和分解牜小于二的二十八次方:34296行:goto
... ...
(268434721, [(3, 2, 645, 314), (4, 2, 19, 16380)])
('num_decompositions', 669124)
('num_primes', 632232)
('num_selected_primes', 34296)

mv -iv /sdcard/0my_files/tmp/0tmp script/枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt
mv -iv /sdcard/0my_files/tmp/1tmp script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt

===
===
py_adhoc_call   script.枚举冫双幂方和型素数   ,枚举冫双幂方和型素数牜非平凡平方和牜小于扌 ='2**32' > /sdcard/0my_files/tmp/0tmp
    #5484450行:not is_pefect_power_
    双幂方和型素数牜非平凡平方和牜小于二的三十二次方:5484450行:goto
du -h /sdcard/0my_files/tmp/0tmp
    159M
(3, 2, 2, 3, 17)
... ...
(31, 16, 2, 3, 2190530369)
===
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker=None  --_cased_doc='("path", "/sdcard/0my_files/tmp/0tmp", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
    #py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker:双幂方和型素数牜非平凡平方和牜小于二的三十二次方  --_cased_doc='("path", "script/枚举冫双幂方和型素数.py.out.txt", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
du -h /sdcard/0my_files/tmp/1tmp
    11M
    # 204177行:not is_pefect_power_
        双幂方和型素数牜非平凡平方和牜含不同双幂方和分解牜小于二的三十二次方:204177行:goto
... ...
(4294950929, [(3, 2, 1409, 38700), (3, 2, 1622, 5259)])
('num_decompositions', 5484450)
('num_primes', 5267756)
('num_selected_primes', 204177)

mv -iv /sdcard/0my_files/tmp/0tmp script/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt
mv -iv /sdcard/0my_files/tmp/1tmp script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt

===
DONE:
    #more-see:重排格式以减小压缩包体积:goto
tar -cvf /the_io_dir/the_output_archive.tar.lzma --lzma -C /the_io_dir/    the_input_file
tar -tvf /the_io_dir/the_output_archive.tar.lzma
tar -xvf /the_io_dir/the_output_archive.tar.lzma -O | more


view script/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt
view script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt

***
16
tar -cvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt.tar.lzma -O | more
---
tar -cvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt.tar.lzma -O | more
***
20
tar -cvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt.tar.lzma -O | more
---
tar -cvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt.tar.lzma -O | more
***
24
tar -cvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt.tar.lzma -O | more
---
tar -cvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt.tar.lzma -O | more
***
28
tar -cvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt.tar.lzma -O | more
---
tar -cvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt.tar.lzma -O | more
***
32
tar -cvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt.tar.lzma -O | more
---
tar -cvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt.tar.lzma --lzma -C script/  枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt
tar -tvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt.tar.lzma
tar -xvf script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt.tar.lzma -O | more
***

==>>:
ls -sh script/枚举冫双幂方和型素数.py.*.out.txt.tar.lzma
8.0K script/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt.tar.lzma
 44K script/枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt.tar.lzma
352K script/枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt.tar.lzma
2.9M script/枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt.tar.lzma
 25M script/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt.tar.lzma
4.0K script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt.tar.lzma
 12K script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt.tar.lzma
 60K script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt.tar.lzma
356K script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt.tar.lzma
2.2M script/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt.tar.lzma

==>>:
!mkdir script/枚举冫双幂方和型素数.py.out/
!mkdir script/枚举冫双幂方和型素数.py.out/txt/
!mkdir script/枚举冫双幂方和型素数.py.out/lzma/
mv -iv script/枚举冫双幂方和型素数.py.*.out.txt.tar.lzma script/枚举冫双幂方和型素数.py.out/lzma/
mv -iv script/枚举冫双幂方和型素数.py.*.out.txt script/枚举冫双幂方和型素数.py.out/txt/

ls -sh script/枚举冫双幂方和型素数.py.*
[[
ls -sh script/枚举冫双幂方和型素数.py.out/txt/
total 193M
 32K 枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt
260K 枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt
2.2M 枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt
 18M 枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt
159M 枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt
8.0K 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt
 48K 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt
288K 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt
1.8M 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt
 11M 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt
]]

[[
ls -sh script/枚举冫双幂方和型素数.py.out/lzma/
total 31M
8.0K 枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt.tar.lzma
 44K 枚举冫双幂方和型素数.py.decompositions_lt_2pow20.out.txt.tar.lzma
352K 枚举冫双幂方和型素数.py.decompositions_lt_2pow24.out.txt.tar.lzma
2.9M 枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt.tar.lzma
 25M 枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt.tar.lzma
4.0K 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt.tar.lzma
 12K 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow20.out.txt.tar.lzma
 60K 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow24.out.txt.tar.lzma
356K 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow28.out.txt.tar.lzma
2.2M 枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow32.out.txt.tar.lzma
]]


du -h script/枚举冫双幂方和型素数.py.out.txt
    del data{2**24}: 2.8M-->352K

e ../.gitignore
排除:
    /txt/script/枚举冫双幂方和型素数.py.out/txt/
    /txt/script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt.tar.lzma
    /txt/script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.decompositions_lt_2pow28.out.txt.tar.lzma

===



==>>:
[数量纟双幂方和型素数牜非平凡平方和牜小于扌(2**16) == 1320] # 1514-???*180
[数量纟双幂方和型素数牜非平凡平方和牜小于扌(2**20) == 10089] #11268-???*1075
[数量纟双幂方和型素数牜非平凡平方和牜小于扌(2**24) == 78617] #85102-???*5950
[数量纟双幂方和型素数牜非平凡平方和牜小于扌(2**28) == 632232] #669124-???*34296
[数量纟双幂方和型素数牜非平凡平方和牜小于扌(2**32) == 5267756] #5484450-???*204177

vs:
view ../../python3_src/seed/math/prime_pint/num_primes_le.py
    [num_primes_le(2**16) == 6542]
    [num_primes_le(2**20) == 82025]
    [num_primes_le(2**24) == 1077871]
    [num_primes_le(2**28) == 14630843]
    [num_primes_le(2**32) == 203280221]

==>>:
1320/6542
10089/82025
78617/1077871
632232/14630843
5267756/203280221
>>> 1320/6542
0.20177315805564047
>>> 10089/82025
0.12299908564462055
>>> 78617/1077871
0.07293729954697732
>>> 632232/14630843
0.04321227423464253
>>> 5267756/203280221
0.02591376560929654

==>>:
ez_np_npppp_nmwpppp_ls = [(16,6542,1320,180), (20,82025,10089,1075), (24,1077871,78617,5950), (28,14630843,632232,34296), (32,203280221,5267756,204177)]
for (ez, num_primes_le_zpowEZ, num_PowPlusPow_primes_le_zpowEZ, num_MultiwayPowPlusPow_primes_le_zpowEZ) in ez_np_npppp_nmwpppp_ls:
    zpow = 1<<ez
    assert (zpow > num_primes_le_zpowEZ > num_PowPlusPow_primes_le_zpowEZ > num_MultiwayPowPlusPow_primes_le_zpowEZ)
    print((ez, zpow, num_primes_le_zpowEZ, num_PowPlusPow_primes_le_zpowEZ, num_MultiwayPowPlusPow_primes_le_zpowEZ))
    (np, npppp, nmwpppp) = (num_primes_le_zpowEZ, num_PowPlusPow_primes_le_zpowEZ, num_MultiwayPowPlusPow_primes_le_zpowEZ)
    j2nm = 'zpow, np, npppp, nmwpppp'.split(', ')
    j2u = (zpow, num_primes_le_zpowEZ, num_PowPlusPow_primes_le_zpowEZ, num_MultiwayPowPlusPow_primes_le_zpowEZ)
    print('   ', [j2u[i]/j2u[i+1] for i in range(len(j2u)-1)])
    for i in range(len(j2u)):
        for j in range(i+1, len(j2u)):
            na = j2nm[i]
            nb = j2nm[j]
            a = j2u[i]
            b = j2u[j]
            print(f'    {na}/{nb} == {a}/{b} ==', a/b)

==>>:
>>> ez_np_npppp_nmwpppp_ls = [(16,6542,1320,180), (20,82025,10089,1075), (24,1077871,78617,5950), (28,14630843,632232,34296), (32,203280221,5267756,204177)]
>>> for (ez, num_primes_le_zpowEZ, num_PowPlusPow_primes_le_zpowEZ, num_MultiwayPowPlusPow_primes_le_zpowEZ) in ez_np_npppp_nmwpppp_ls:
...     zpow = 1<<ez
...     assert (zpow > num_primes_le_zpowEZ > num_PowPlusPow_primes_le_zpowEZ > num_MultiwayPowPlusPow_primes_le_zpowEZ)
...     print((ez, zpow, num_primes_le_zpowEZ, num_PowPlusPow_primes_le_zpowEZ, num_MultiwayPowPlusPow_primes_le_zpowEZ))
...     (np, npppp, nmwpppp) = (num_primes_le_zpowEZ, num_PowPlusPow_primes_le_zpowEZ, num_MultiwayPowPlusPow_primes_le_zpowEZ)
...     j2nm = 'zpow, np, npppp, nmwpppp'.split(', ')
...     j2u = (zpow, num_primes_le_zpowEZ, num_PowPlusPow_primes_le_zpowEZ, num_MultiwayPowPlusPow_primes_le_zpowEZ)
...     print('   ', [j2u[i]/j2u[i+1] for i in range(len(j2u)-1)])
...     for i in range(len(j2u)):
...         for j in range(i+1, len(j2u)):
...             na = j2nm[i]
...             nb = j2nm[j]
...             a = j2u[i]
...             b = j2u[j]
...             print(f'    {na}/{nb} == {a}/{b} ==', a/b)
(16, 65536, 6542, 1320, 180)
    [10.017731580556404, 4.956060606060606, 7.333333333333333]
    zpow/np == 65536/6542 == 10.017731580556404
    zpow/npppp == 65536/1320 == 49.64848484848485
    zpow/nmwpppp == 65536/180 == 364.0888888888889
    np/npppp == 6542/1320 == 4.956060606060606
    np/nmwpppp == 6542/180 == 36.34444444444444
    npppp/nmwpppp == 1320/180 == 7.333333333333333
(20, 1048576, 82025, 10089, 1075)
    [12.783614751600123, 8.130141738527108, 9.385116279069768]
    zpow/np == 1048576/82025 == 12.783614751600123
    zpow/npppp == 1048576/10089 == 103.932599861235
    zpow/nmwpppp == 1048576/1075 == 975.419534883721
    np/npppp == 82025/10089 == 8.130141738527108
    np/nmwpppp == 82025/1075 == 76.30232558139535
    npppp/nmwpppp == 10089/1075 == 9.385116279069768
(24, 16777216, 1077871, 78617, 5950)
    [15.56514276754825, 13.710406146253355, 13.212941176470588]
    zpow/np == 16777216/1077871 == 15.56514276754825
    zpow/npppp == 16777216/78617 == 213.40442906750448
    zpow/nmwpppp == 16777216/5950 == 2819.700168067227
    np/npppp == 1077871/78617 == 13.710406146253355
    np/nmwpppp == 1077871/5950 == 181.15478991596638
    npppp/nmwpppp == 78617/5950 == 13.212941176470588
(28, 268435456, 14630843, 632232, 34296)
    [18.347230983204454, 23.141573030153488, 18.434569629111266]
    zpow/np == 268435456/14630843 == 18.347230983204454
    zpow/npppp == 268435456/632232 == 424.5837856989206
    zpow/nmwpppp == 268435456/34296 == 7827.0193608584095
    np/npppp == 14630843/632232 == 23.141573030153488
    np/nmwpppp == 14630843/34296 == 426.6049393515279
    npppp/nmwpppp == 632232/34296 == 18.434569629111266
(32, 4294967296, 203280221, 5267756, 204177)
    [21.128308867786995, 38.589528634204015, 25.799948084260226]
    zpow/np == 4294967296/203280221 == 21.128308867786995
    zpow/npppp == 4294967296/5267756 == 815.3314800457728
    zpow/nmwpppp == 4294967296/204177 == 21035.509856643992
    np/npppp == 203280221/5267756 == 38.589528634204015
    np/nmwpppp == 203280221/204177 == 995.6078353585369
    npppp/nmwpppp == 5267756/204177 == 25.799948084260226
>>> None

==>>:
(16, 65536, 6542, 1320, 180)
    [10.017731580556404, 4.956060606060606, 7.333333333333333]
(20, 1048576, 82025, 10089, 1075)
    [12.783614751600123, 8.130141738527108, 9.385116279069768]
(24, 16777216, 1077871, 78617, 5950)
    [15.56514276754825, 13.710406146253355, 13.212941176470588]
(28, 268435456, 14630843, 632232, 34296)
    [18.347230983204454, 23.141573030153488, 18.434569629111266]
(32, 4294967296, 203280221, 5267756, 204177)
    [21.128308867786995, 38.589528634204015, 25.799948084260226]

===

]]
[[
重排格式以减小压缩包体积:here
文件格式纟重排:
    (ea,eb)
    a0:b0{a0},$[b1-b0],$[b2-b1],...
    $[a1-a0]:b0{a1},$[b1-b0],$[b2-b1],...
重排格式以减小压缩包体积扌
    逆函数纟重排格式以减小压缩包体积扌
===
16#test
view script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt

py_adhoc_call   script.枚举冫双幂方和型素数   ,str.重排格式以减小压缩包体积扌 --ipath:script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt  > /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp

py_adhoc_call   script.枚举冫双幂方和型素数   ,str.逆函数纟重排格式以减小压缩包体积扌 --ipath:/sdcard/0my_files/tmp/0tmp > /sdcard/0my_files/tmp/1tmp
view /sdcard/0my_files/tmp/1tmp

diff -s script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt /sdcard/0my_files/tmp/1tmp
    identical

===
32#hardwork
view script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt
du -h script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt
    159M
py_adhoc_call   script.枚举冫双幂方和型素数   ,str.重排格式以减小压缩包体积扌 --ipath:script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.decompositions_lt_2pow32.out.txt  > script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt
view script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt
du -h script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt
    14M

===
tar -cvf /the_io_dir/the_output_archive.tar.lzma --lzma -C /the_io_dir/    the_input_file
tar -tvf /the_io_dir/the_output_archive.tar.lzma
tar -xvf /the_io_dir/the_output_archive.tar.lzma -O | more

tar -cvf script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt.tar.lzma --lzma -C script/枚举冫双幂方和型素数.py.out/txt/  枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt
du -h script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt.tar.lzma
    3.3M

e ../.gitignore
排除:
    /txt/script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt

===
]]
[[
重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌

重排:
    输入行格式:
        (17, [(3, 2, 2, 3), (4, 2, 2, 1)])
        (4294950929, [(3, 2, 1409, 38700), (3, 2, 1622, 5259)])
    输出文件格式:=文件格式纟重排


===
16#test
view script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt

py_adhoc_call   script.枚举冫双幂方和型素数   ,str.重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌 --ipath:script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt  > /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp

py_adhoc_call   script.枚举冫双幂方和型素数   ,str.逆函数纟重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌 --ipath:/sdcard/0my_files/tmp/0tmp > /sdcard/0my_files/tmp/1tmp
view /sdcard/0my_files/tmp/1tmp

diff -s script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt /sdcard/0my_files/tmp/1tmp
    identical
    bug fixed
    <<==:
    not identical
    #bug:miss_epilog@[to_count:=True]@_归组过滤冫素数牜含不同双幂方和分解扌(),_core4group_extract_()
181,183d180
< ('num_decompositions', 1514)
< ('num_primes', 1320)
< ('num_selected_primes', 180)

===

]]
[[
重命名:reform-->compact
ls script/枚举冫双幂方和型素数.py.out/txt/*reform*
mv -iv script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.reform.decompositions_lt_2pow32.out.txt    script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt
ls script/枚举冫双幂方和型素数.py.out/lzma/*reform*
tar -cvf script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt.tar.lzma --lzma -C script/枚举冫双幂方和型素数.py.out/txt/  枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt
rm -iv script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.reform.decompositions_lt_2pow32.out.txt.tar.lzma
e ../.gitignore
]]
[[
DONE:打印改为枚举
    输出方式:print --> yield
    相应命令行:@ --> ,str.
TODO:
    测试用函数+测试用数据
TODO:
++kw:max1_p
    缩水过滤
def _iter_read_sorted_records5lines4compact_file_type_(may_epilogs8out, lines, /):
    '(Iter line){@compact_file_type} -> sorted (Iter record/(ea, a, eb, b, p))'
from seed.for_libs.for_tarfile import iter_read_solo_tarfile_
def iter_read_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}):
    '-> Iter line/(bytes if not xencoding4data else str)|^Error__not_solo_tarfile'

_缩水过滤冫输出文件牜重排后牜无结束语牜压缩包扌

py_adhoc_call   script.枚举冫双幂方和型素数   ,_缩水过滤冫输出文件牜重排后牜无结束语牜压缩包扌 --ipath:script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow20.out.txt.tar.lzma ='2**16'  > /sdcard/0my_files/tmp/0tmp
FileNotFoundError: [Errno 2] No such file or directory: 'script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂 方和型素数.py.compact.decompositions_lt_2pow20.out.txt.tar.lzma'


py_adhoc_call   script.枚举冫双幂方和型素数   ,_缩水过滤冫输出文件牜重排后牜无结束语牜压缩包扌 --ipath:script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow16.out.txt.tar.lzma ='2**16'  > /sdcard/0my_files/tmp/0tmp
TODO ...
]]





]]]'''#'''
__all__ = r'''
枚举冫双幂方和型素数牜非平凡平方和牜小于扌
重排格式以减小压缩包体积扌
    逆函数纟重排格式以减小压缩包体积扌
重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌
    逆函数纟重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌

text5cased_text_
iter_read_lines_
iter_eval_read_lines_
_core4compact_
    _iter_read_sorted_records5lines4compact_file_type_
    _core4compactII_
_record5key
_record2key
'''.split()#'''
    #_归组过滤冫素数牜含不同双幂方和分解扌
    #   _core4group_extract_
    #_spec_mod_pow_
    #_缩水过滤冫输出文件牜重排后牜无结束语牜压缩包扌
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.io.iter_lines5cased_text_ import iter_eval_lines5cased_text__slice_by_marker_lines_, iter_slice_lines5cased_text__by_marker_lines_
#def iter_eval_lines5cased_text__slice_by_marker_lines_(cased_text, may_line_prefix4begin_marker, may_line_prefix4end_marker, /, *, may_eval_or_name='literal_eval', may_filter_lines4eval_=filter_lines4eval_):
from seed.tiny_.check import check_type_is, check_int_ge
from math import ceil, gcd
from itertools import count, chain, groupby
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

def _制表扌(*, ver=2, prime_bases=[2,3,5,7]):
    from seed.math.II import II
    from seed.math.prime_gens import is_prime__le_pow2_81_
    prime_bases = tuple(prime_bases)
    assert len(set(prime_bases)) == len(prime_bases)
    for q in prime_bases:
        assert is_prime__le_pow2_81_(q)
        assert q < 17 # == min_output == 2**4+1 == 2**3 + 3**2
            # !! [q==17] => exclude "17"@output
            #view script/爻元数纟累积纟素数牜对比机器字长.py
            #   (5, 13, 15)
            #   (6, 17, 19)
            #   IIqs ~ 15bit
    #.for q in prime_bases:
    #.    phi_q = q-1
    #.    for ea in range(phi_q):
    #.     for eb in range(phi_q):
    #.      for a in range(q):
    #.        for b in range(q):
    #.            _Apow = _spec_mod_pow_(a, ea, q)
    #.            _Bpow = _spec_mod_pow_(b, eb, q)
    #.            if (_Apow+_Bpow)%q==0:
    q__exp2rem_pow2xs__pairs = []
    for q in prime_bases:
        phi_q = q-1
        # ??? (ea,eb,a,b) => [(a**ea+b**eb)%q==0]
        exp2rem_pow2xs = []
            # :: [{rem_pow:[x]}]
            #  [rem_pow==x**j%q]
        q__exp2rem_pow2xs__pairs.append((q, exp2rem_pow2xs))
        for ex in range(phi_q):
          if 1:
            rem_pow2xs = {}
            exp2rem_pow2xs.append(rem_pow2xs)
          for x in range(q):
            #bug:_Xpow = pow(x, ex, q)
            #   !! [pow(0,0,2) == 1]
            _Xpow = _spec_mod_pow_(x, ex, q)
            rem_pow2xs.setdefault(_Xpow, []).append(x)
    q__exp2rem_pow2xs__pairs
    q__ea2a2eb2badB__pairs = []
    for q, exp2rem_pow2xs in q__exp2rem_pow2xs__pairs:
        phi_q = q-1
        ea2a2eb2badB = [[[None for eb in range(phi_q)] for a in range(q)] for ea in range(phi_q)]
        q__ea2a2eb2badB__pairs.append((q, ea2a2eb2badB))
        for ea in range(phi_q):
         for a in range(q):
          if 1:
            #bug:_Apow = pow(a, ea, q)
            #   !! [pow(0,0,2) == 1]
            _Apow = _spec_mod_pow_(a, ea, q)
            bad_Bpow = (-_Apow)%q
          for eb in range(phi_q):
            #.for b in range(q):
            bad_B = exp2rem_pow2xs[eb].get(bad_Bpow, [])
            ea2a2eb2badB[ea][a][eb] = bad_B
    q__ea2a2eb2badB__pairs
    if ver==1:
        return q__ea2a2eb2badB__pairs
    raise 000

    IIqs = II(prime_bases)
    assert IIqs < (1<<16), 'not all:q<17'
    assert IIqs < (1<<8), 'slow?'
assert pow(0,0,2) == 1
assert pow(1,0,2) == 1
def _spec_mod_pow_(x, ex, M, /):
    '[pow(0,0,2) == 1]'
    return pow(x, ex, M) if not x == 0 == ex else 0
#end-def _制表扌(*, ver=2, prime_bases=[2,3,5,7]):


def 枚举冫双幂方和型素数牜非平凡平方和牜小于扌(max1_p, /):
    'max1_p -> Iter (ea, eb, a, b, p){[[a,b,ea,eb,eez::uint][a>=2][b>=1][ea>=3][eb>=2][not is_pefect_power_(a)][[is_pefect_power_(b)] <-> [b==1]][[b==1] -> [eb==2]][(ea,a) > (eb,b)][gcd(a,b)==1][gcd(ea,eb)==2**eez][p:=a**ea+b**eb][is_prime_(p)][p < max1_p]]}'
    from seed.math.floor_ceil import floor_kth_root_, ceil_kth_root_
    from seed.math.prime_gens import is_prime__le_pow2_81_
    max1_p = ceil(max1_p)
    max1_p = max(0, max1_p)
    check_int_ge(0, max1_p)
    # [max1_p >= 0]
    assert max1_p <= (1<<81), is_prime__le_pow2_81_
    # [max1_p <= 2**81]
    q__ea2a2eb2badB__pairs = _制表扌(prime_bases=[2,3,5,7], ver=1)
    def is_bad_b_(ea, eb, a, b):
        '拆分开来分散到不同层次的循环中'
        for q, ea2a2eb2badB in q__ea2a2eb2badB__pairs:
            phi_q = q-1
            bad_B = ea2a2eb2badB[ea%phi_q][a%q][eb%phi_q]
            if b%q in bad_B:
                #if 0b0001:print(f'is_bad_b_({ea}, {eb}, {a}, {b}):{q},{bad_B},{ea2a2eb2badB}')
                return True
        return False
    assert not is_bad_b_(3, 2, 2, 3), 17==2**3+3**2
    def f(ea, eb, a, b):
        if 0:
            #见下面:『拆分开来分散到不同层次的循环中』
            if is_bad_b_(ea, eb, a, b):
                #if 0b0001:print(f'is_bad_b_({ea}, {eb}, {a}, {b})')
                return
        assert a >= 2
        assert b >= 1
        assert ea >= 3
        assert eb >= 2

        assert not is_pefect_power_(a)
        # [not is_pefect_power_(a)]

        assert is_pefect_power_(b) is (b==1)
        # [[is_pefect_power_(b)] <-> [b==1]]

        assert not b==1 or eb==2
        # [[b==1] -> [eb==2]]

        assert (ea,a) > (eb,b)
        assert not b&1 == a&1
        # [a%2 =!= b%2]
        if a&1 == 0 == b&1 or not gcd(a,b) == 1:
            return
        #assert gcd(a,b) == 1
        # [gcd(a,b)==1]
        g = gcd(ea,eb)
        assert g&(g-1) == 0
        eez = g.bit_length()-1
        assert (1<<eez) == g
        # [gcd(ea,eb)==2**eez]
        p = a**ea+b**eb
        assert p < max1_p
        # [p < max1_p]
        # !! [max1_p <= 2**81]
        # [p < max1_p <= 2**81]
        # [p < 2**81]
        if not is_prime__le_pow2_81_(p):
            return
        # [is_prime_(p)]
        yield (ea, eb, a, b, p)
        return

    # [max1_p >= 0]
    gt_log2_max1_p = max1_p.bit_length()
    assert max1_p < (1<<gt_log2_max1_p)
    ######################
    pows = {1}
    for ex in range(2, gt_log2_max1_p):
        max1_x = ceil_kth_root_(ex, max1_p)
        assert max1_x**ex >= max1_p
        for x in range(2, max1_x):
            _Xpow = x**ex
            assert _Xpow < max1_p
            pows.add(_Xpow)
    pows
    def is_pefect_power_(y, /):
        assert 0 < y < max1_p
        return y in pows
    is_pefect_power_
    ######################

    # !! [ea >= 3]
    for ea in range(3, gt_log2_max1_p):
        #for ea in count(3):
        max1_a = ceil_kth_root_(ea, max1_p)
        # !! [a >= 2]
        A = range(2, max1_a)
        assert A or max1_a == 2 and max1_p == (1<<ea), (max1_p, gt_log2_max1_p, ea, max1_a)
        if not A:
            #raise 000
            break
        #第一层@is_bad_b_(ea, eb, a, b):拆分开来分散到不同层次的循环中
        q__a2eb2badB__pairs = [(q,ea2a2eb2badB[ea%(q-1)]) for q, ea2a2eb2badB in q__ea2a2eb2badB__pairs]
        for a in A:
            if is_pefect_power_(a):
                continue
            # [not is_pefect_power_(a)]
            #第二层@is_bad_b_(ea, eb, a, b):拆分开来分散到不同层次的循环中
            q__eb2badB__pairs = [(q,a2eb2badB[a%q]) for q, a2eb2badB in q__a2eb2badB__pairs]

            max1_Bpow = max1_p - a**ea
            assert max1_Bpow >= 1
            if 1 < max1_Bpow:
                # [b:=1]
                # !! [[b==1] -> [eb==2]]
                # [eb:=2]
                b = 1
                eb = 2
                if not b&1 == a&1:
                    # [a%2 =!= b%2]
                    (q__eb2badB__pairs, eb, b)
                    #第三层暨第四层@is_bad_b_(ea, eb, a, b):拆分开来分散到不同层次的循环中
                    if not any(b%q in eb2badB[eb%(q-1)] for q, eb2badB in q__eb2badB__pairs):
                        yield from f(ea, eb, a, b)
            gt_log2_max1_Bpow = max1_Bpow.bit_length()
            assert max1_Bpow < (1<<gt_log2_max1_Bpow)
            # !! [(ea,a) > (eb,b)]
            # [eb <= ea]
            # !! [eb >= 2]
            for eb in range(2, min(1+ea,gt_log2_max1_Bpow)):
                g = gcd(ea,eb)
                if not g&(g-1) == 0:
                    continue
                assert g&(g-1) == 0
                eez = g.bit_length()-1
                assert (1<<eez) == g
                # [gcd(ea,eb)==2**eez]
                #第三层@is_bad_b_(ea, eb, a, b):拆分开来分散到不同层次的循环中
                q__badB__pairs = [(q,eb2badB[eb%(q-1)]) for q, eb2badB in q__eb2badB__pairs]
                max1_b = ceil_kth_root_(eb, max1_Bpow)
                if eb == ea:
                    # [eb == ea]
                    # !! [(ea,a) > (eb,b)]
                    # [b < a]
                    max1_b = min(a, max1_b)
                max1_b
                # !! [b >= 1]
                #bug:B = range(1, max1_b)
                # !! [b >= 1]
                # !! yielded:[b==1]
                # [b >= 2]
                B = range(2, max1_b)
                assert B or max1_b==2, (max1_p, gt_log2_max1_p, ea, max1_a, a, max1_Bpow, gt_log2_max1_Bpow, eb, max1_b)
                if not B:
                    #raise 000
                    break
                for b in B:
                    # [b >= 2]
                    if b&1 == a&1:
                        continue
                    # [a%2 =!= b%2]
                    #第四层@is_bad_b_(ea, eb, a, b):拆分开来分散到不同层次的循环中
                    if any(b%q in bad_B for q, bad_B in q__badB__pairs):
                        continue
                    if is_pefect_power_(b):
                        continue
                    # [not is_pefect_power_(b)]
                    # !! [b >= 2]
                    # [[is_pefect_power_(b)] <-> [b==1]]
                    yield from f(ea, eb, a, b)
#end-def 枚举冫双幂方和型素数牜非平凡平方和牜小于扌(max1_p, /):



def _handle_may_marker(marker, /):
    # old{non_line_align-full-marker}-->new{line_prefix}
    if marker is None:
        (may_line_prefix4begin_marker, may_line_prefix4end_marker) = (None, None)
    else:
        (may_line_prefix4begin_marker, may_line_prefix4end_marker) = (line_prefix4begin_marker, line_prefix4end_marker) = (fr'###begin:{marker!s}', fr'###end:{marker!s}')
    return (may_line_prefix4begin_marker, may_line_prefix4end_marker)
def _iter_outputs5doc_(marker='双幂方和型素数牜非平凡平方和牜小于二的十六次方', _cased_doc=('text', __doc__)):
    ######################new:
    (may_line_prefix4begin_marker, may_line_prefix4end_marker) = _handle_may_marker(marker)
    return iter_eval_lines5cased_text__slice_by_marker_lines_(cased_text, may_line_prefix4begin_marker, may_line_prefix4end_marker, may_eval_or_name='literal_eval', may_filter_lines4eval_=None)
    ######################old:
    #._doc = text5cased_text_(_cased_doc)
    #.from seed.str_tools.cut_text_by_marker_seq import iter_eval_lines_by_marker_pair
    #.if marker is None:
    #.    it = iter_eval_lines_by_marker_pair(_doc, None, None)
    #.else:
    #.    it = iter_eval_lines_by_marker_pair(_doc, fr'###begin:{marker!s}', fr'###end:{marker!s}')
    #.return it
def _归组过滤冫素数牜含不同双幂方和分解扌(marker='双幂方和型素数牜非平凡平方和牜小于二的十六次方', _cased_doc=('text', __doc__), to_count=False):
    it = _iter_outputs5doc_(marker=marker, _cased_doc=_cased_doc)
    iter_p_sorted_alter_sorted_grouped_records = _core4group_extract_(iter_alter_sorted_records:=it, to_count=to_count)
    return iter_p_sorted_alter_sorted_grouped_records
#def _core4group_extract_(alter_sorted_records, /, *, to_count:bool):
def alter_sorted_records2iter_p_sorted_alter_sorted_grouped_records_and_optional_epilogs_(alter_sorted_records, /, *, to_count:bool):
    'alter_sorted_records -> iter_p_sorted_alter_sorted_grouped_records++optional_epilogs # (Iter record/(ea, eb, a, b, p)){sorted by key:key4record/(ea, a, eb, b, p)} -> iter_p_sorted_alter_sorted_grouped_records/(Iter grouped_record/(p, [(ea, eb, a, b)]{sorted by key:(ea, a, eb, b)})){sorted by key:p}{@compact_file_type}'
    ######################new:
    p_sorted_alter_sorted_records = sorted(alter_sorted_records, key=_record2p)
    # [p_sorted_alter_sorted_records sorted by key:(p, (ea, a, eb, b))]
    num_decompositions = 0
    num_primes = 0
    num_selected_primes = 0
    for (_p, [*grp]) in groupby(p_sorted_alter_sorted_records, key=_record2p):
        #######
        for record in grp:
            (ea, eb, a, b, p) = t = record
            assert p == _p
        #######
        num_decompositions += len(grp)
        num_primes += 1

        if len(grp) < 2:continue
        num_selected_primes += 1
        #######
        _ts = [(ea, eb, a, b) for (ea, eb, a, b, _p) in grp]
        yield ((p, _ts))
        #######
    ######################
    if to_count:
        yield ('num_decompositions', num_decompositions)
        yield ('num_primes', num_primes)
        yield ('num_selected_primes', num_selected_primes)
    ######################

    return
    ######################old:
    #.p2ts = {}
    #.sz = 0
    #.for sz, t in enumerate(alter_sorted_records, 1):
    #.    (ea, eb, a, b, p) = t
    #.    p2ts.setdefault(p, []).append(t)
    #._p2ts = {p:ts for p,ts in p2ts.items() if len(ts) > 1}
    #.for p,ts in sorted(_p2ts.items()):
    #.    for (ea, eb, a, b, _p) in ts:
    #.        assert p == _p
    #.    _ts = [(ea, eb, a, b) for (ea, eb, a, b, _p) in ts]
    #.    yield ((p, _ts))
    #.######################
    #.if to_count:
    #.    yield ('num_decompositions', sz)
    #.    yield ('num_primes', len(p2ts))
    #.    yield ('num_selected_primes', len(_p2ts))
    ######################
_core4group_extract_ = alter_sorted_records2iter_p_sorted_alter_sorted_grouped_records_and_optional_epilogs_
#end-def _core4group_extract_(alter_sorted_records, /, *, to_count:bool):

def iter_read_lines_(*, ipath, encoding):
    with open(ipath, 'rt', encoding=encoding) as ifile:
        for line in ifile:
            yield line
def iter_eval_read_lines_(*, ipath, encoding):
    from ast import literal_eval as eval_
    iter_lines = iter_read_lines_(ipath=ipath, encoding=encoding)
    return map(eval_, iter_lines)
def 重排格式以减小压缩包体积扌(*, ipath, encoding='ascii'):
    #重排格式以减小压缩包体积:goto
    #view script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.decompositions_lt_2pow16.out.txt
    #   (3, 2, 2, 3, 17)
    #   (15, 2, 2, 159, 58049)
    #   fmt:(ea, eb, a, b, p)
    iter_alter_sorted_records = iter_eval_read_lines_(ipath=ipath, encoding=encoding)
    iter_lines = _core4compact_(iter_alter_sorted_records)
    return iter_lines
    #######打印改为枚举#######
    #.for line in iter_lines:
    #.    print(line)
    #.return
def _lines5records__alter_sorted_(alter_sorted_records, /):
    '(Iter record/(ea, eb, a, b, p)){sorted by key:key4record/(ea, a, eb, b, p)} -> (Iter line){@compact_file_type}'
    #===_lines5records__alter_sorted_()===_core4compact_
    #vs:_lines5sorted_records_()
    ######################new:
    sorted_records = sorted(alter_sorted_records)
    return _lines5sorted_records_(sorted_records)
    ######################old:
    #.alter_sorted_records
    #.from collections import defaultdict
    #.#ea_eb2a2B = {}
    #.ea_eb2a2B = defaultdict(lambda:defaultdict(list))
    #.for (ea, eb, a, b, p) in alter_sorted_records:
    #.        #drop:p
    #.        #   !! [p == a**ea+b**eb]
    #.    #a2B = ea_eb2a2B.setdefault((ea,eb), {})
    #.    #B = a2B.setdefault(a, [])
    #.    B = ea_eb2a2B[(ea,eb)][a]
    #.    B.append(b)
    #.ea_eb2a2B
    #.for ea_eb, a2B in sorted(ea_eb2a2B.items()):
    #.    #print(ea_eb)
    #.    yield str(ea_eb)
    #.    a_ = 0
    #.    ss = []
    #.    f = ss.append
    #.    for a, B in sorted(a2B.items()):
    #.        delta_a = a -a_
    #.        777;    a_ = a
    #.        assert delta_a > 0, (ea_eb, a, delta_a)
    #.        #print(delta_a, end=':')
    #.        assert not ss
    #.        f(delta_a); f(':')
    #.        b_ = 0
    #.        for sz, b in enumerate(B, 1):
    #.            delta_b = b -b_
    #.            777;    b_ = b
    #.            assert delta_b > 0, (ea_eb, a, b, delta_b)
    #.            if 0:
    #.                end = ('\n' if sz==len(B) else ',')
    #.                #print(delta_b, end=end)
    #.            else:
    #.                end = ('' if sz==len(B) else ',')
    #.                f(delta_b); f(end)
    #.        yield ''.join(map(str, ss))
    #.        777; ss.clear()
_core4compact_ = _lines5records__alter_sorted_
#end-def _lines5records__alter_sorted_(alter_sorted_records, /):
def 逆函数纟重排格式以减小压缩包体积扌(*, ipath, encoding='ascii', epilog_ok=False):
    '逆函数{重排格式以减小压缩包体积扌()}'
    iter_lines = iter_read_lines_(ipath=ipath, encoding=encoding)
    iter_sorted_records = _iter_read_sorted_records5lines4compact_file_type_(may_epilogs8out:=None, iter_lines)
    alter_sorted_records = sorted(iter_sorted_records, key=_record2key)
    return alter_sorted_records
    iter_alter_sorted_records = iter(alter_sorted_records)
    return iter_alter_sorted_records
    #######打印改为枚举#######
    #.for record in alter_sorted_records:
    #.    (ea, eb, a, b, p) = t = record
    #.    print(record)
    #.return
    ######################
    #.iter_alter_sorted_keys4records = map(_record2key, iter_sorted_records)
    #.sorted_keys4records = sorted(iter_alter_sorted_keys4records)
    #.    #keys4records.sort()
    #.for (ea, a, eb, b, p) in sorted_keys4records:
    #.    t = record = (ea, eb, a, b, p)
    #.    print(record)
    #.return
    ######################
    #.# [epilogs8out may keep empty before iter_lines exhausted]
    #.if not epilog_ok and epilogs8out:raise Exception(epilogs8out)
    #.for epilog in epilogs8out:
    #.    print(epilog)
    ######################

#.def _iter_read_keys4records5lines4compact_file_type_(may_epilogs8out, lines, /):
#.    '(Iter line){@compact_file_type} -> (Iter key4record/(ea, a, eb, b, p)){sorted by key:record/(ea, eb, a, b, p)}'
def _iter_read_sorted_records5lines4compact_file_type_(may_epilogs8out, lines, /):
    '(Iter line){@compact_file_type} -> sorted (Iter record/(ea, eb, a, b, p))'
    ######################new:
    iter_mixed_compact_records = _iter_read_mixed_compact_records5lines4compact_file_type_(may_epilogs8out, lines)
    a = -0.5
    for mixed_compact_record in iter_mixed_compact_records:
        (x, y) = mixed_compact_record
        if type(y) is int:
            #head_record4compact_file_type
            (ea, eb) = ea_eb = mixed_compact_record
            check_int_ge(2, eb)
            check_int_ge(3, ea)
            check_int_ge(eb, ea)
            assert not a == 0
            a = 0
            continue
        #data_record4compact_file_type
        assert type(y) is list
        (delta_a, ls4delta_b) = mixed_compact_record
        assert len(ls4delta_b)

        a
        assert a >= 0
        check_int_ge(1, delta_a)
        for delta_b in ls4delta_b:
            check_int_ge(1, delta_b)
        assert len(ls4delta_b)

        a += delta_a
        _Apow = a**ea
        b = 0
        for delta_b in ls4delta_b:
            b += delta_b
            #p = a**ea+b**eb
            p = _Apow+b**eb
            t = record = (ea, eb, a, b, p)
            #key4record = (ea, a, eb, b, p)
                # => keys4records.sort()
            #keys4records.append(key4record)
            #yield key4record
            yield record
        #end-for delta_b in ls4delta_b:
    #end-for mixed_compact_record in iter_mixed_compact_records:
    return


    ######################old:
    #.from ast import literal_eval as eval_
    #.epilog_ok = not may_epilogs8out is None
    #.epilogs8out = may_epilogs8out if epilog_ok else []

    #.a = -0.5
    #.for line in lines:
    #.    #if 0b0001:print(line)
    #.    if line[0] == '(': # ')'
    #.        (ea_or_case, eb_or_u) = eval_(line)
    #.        if type(ea_or_case) is str:
    #.            #epilog
    #.            case = ea_or_case
    #.            u = eb_or_u
    #.            epilog = (case, u)
    #.            epilogs8out.append(epilog)
    #.            #yield epilog
    #.            continue
    #.        else:
    #.            ea = ea_or_case
    #.            eb = eb_or_u
    #.        #(ea, eb) = eval_(line)
    #.        (ea, eb)
    #.        check_int_ge(2, eb)
    #.        check_int_ge(3, ea)
    #.        check_int_ge(eb, ea)
    #.        assert not a == 0
    #.        a = 0
    #.        continue
    #.    a
    #.    assert a >= 0
    #.    s0, s1 = line.split(':', 1)
    #.    delta_a = int(s0)
    #.    ls4delta_b = [*map(int, s1.split(','))]
    #.    check_int_ge(1, delta_a)
    #.    for delta_b in ls4delta_b:
    #.        check_int_ge(1, delta_b)
    #.    assert len(ls4delta_b)

    #.    a += delta_a
    #.    _Apow = a**ea
    #.    b = 0
    #.    for delta_b in ls4delta_b:
    #.        b += delta_b
    #.        #p = a**ea+b**eb
    #.        p = _Apow+b**eb
    #.        t = record = (ea, eb, a, b, p)
    #.        #key4record = (ea, a, eb, b, p)
    #.            # => keys4records.sort()
    #.        #keys4records.append(key4record)
    #.        #yield key4record
    #.        yield record
    #.    #end-for delta_b in ls4delta_b:
    #.#end-for line in lines:

    #.# [epilogs8out may keep empty before iter_lines exhausted]
    #.if not epilog_ok and epilogs8out:raise Exception(epilogs8out)
    #.return
#end-def _iter_read_sorted_records5lines4compact_file_type_(may_epilogs8out, lines, /):
def _iter_read_mixed_compact_records5lines4compact_file_type_(may_epilogs8out, lines, /):
    '(Iter line){@compact_file_type} -> (Iter mixed_compact_record/((ea,eb)|(delta_a,[delta_b])))'
    from ast import literal_eval as eval_
    epilog_ok = not may_epilogs8out is None
    epilogs8out = may_epilogs8out if epilog_ok else []

    a = -0.5
    for line in lines:
        #if 0b0001:print(line)
        if line[0] == '(': # ')'
            (ea_or_case, eb_or_u) = eval_(line)
            if type(ea_or_case) is str:
                #epilog
                case = ea_or_case
                u = eb_or_u
                epilog = (case, u)
                epilogs8out.append(epilog)
                #yield epilog
                assert not a == 0
                a = None
                continue
            else:
                ea = ea_or_case
                eb = eb_or_u
            #(ea, eb) = eval_(line)
            (ea, eb)
            check_int_ge(2, eb)
            check_int_ge(3, ea)
            check_int_ge(eb, ea)
            assert not a == 0
            a = 0
            #yield (False, (ea, eb))
            yield (ea, eb)
            continue
        a
        assert a >= 0
        s0, s1 = line.split(':', 1)
        delta_a = int(s0)
        ls4delta_b = [*map(int, s1.split(','))]
        check_int_ge(1, delta_a)
        for delta_b in ls4delta_b:
            check_int_ge(1, delta_b)
        assert len(ls4delta_b)

        a += delta_a
        #yield (True, (delta_a, ls4delta_b))
        yield (delta_a, ls4delta_b)
    #end-for line in lines:

    # [epilogs8out may keep empty before iter_lines exhausted]
    if not epilog_ok and epilogs8out:raise Exception(epilogs8out)
#end-def _iter_read_mixed_compact_records5lines4compact_file_type_(may_epilogs8out, lines, /):



def 重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌(*, ipath, encoding='ascii'):
    #view script/枚举冫双幂方和型素数.py.out/txt/枚举冫双幂方和型素数.py.len_ge2__grouped_decompositions_lt_2pow16.out.txt
    #   (17, [(3, 2, 2, 3), (4, 2, 2, 1)])
    #   (4294950929, [(3, 2, 1409, 38700), (3, 2, 1622, 5259)])
    #   fmt:(p, [(ea, eb, a, b)])
    iter_grouped_records = iter_eval_read_lines_(ipath=ipath, encoding=encoding)
    # [iter_grouped_records sorted by key:p]
    # [iter_grouped_records unsorted ok]
    epilogs8out = []
    iter_lines = _core4compactII_(epilogs8out, iter_grouped_records)
        # '(Iter grouped_record/(p, [(ea, eb, a, b)])){unsorted ok} -> (Iter line){@compact_file_type}'
        # '(Iter grouped_record/(p, [(ea, eb, a, b)]{sorted by key:(ea, a, eb, b)})){sorted by key:p} -> (Iter line){@compact_file_type}'
    # [iter_lines :: compact_file_type]
    yield from iter_lines
    yield from epilogs8out
    return
    #######打印改为枚举#######
    #.for line in iter_lines:
    #.    print(line)
    #.for epilog in epilogs8out:
    #.    print(epilog)
    #.return
def _record2p(record, /):
    (ea, eb, a, b, p) = record
    return p
def _record2key(record, /):
    (ea, eb, a, b, p) = record
    key4record = (ea, a, eb, b, p)
    return key4record
def _record5key(key4record, /):
    (ea, a, eb, b, p) = key4record
    record = (ea, eb, a, b, p)
    return record
def _core4compactII_(epilogs8out, grouped_records, /):
    '(Iter grouped_record/(p, [(ea, eb, a, b)])){unsorted ok} -> (Iter line){@compact_file_type}'
    '(Iter grouped_record/(p, [(ea, eb, a, b)]{sorted by key:(ea, a, eb, b)})){sorted by key:p} -> (Iter line){@compact_file_type}'
    if 0b0000:
        grouped_records = list(grouped_records)
        for grouped_record in grouped_records:
            print(grouped_record)
    if 0:
        #bug:miss_epilog@[to_count:=True]@_归组过滤冫素数牜含不同双幂方和分解扌(),_core4group_extract_()
        records = [(ea, eb, a, b, p) for (p, xs) in grouped_records if not type(p) is str for (ea, eb, a, b) in xs]
            # avoid last 3 lines@[to_count=True]
    records = []
    #epilogs8out = []
    for grouped_record in grouped_records:
        check_type_is(tuple, grouped_record)
        (p_or_case, xs_or_u) = grouped_record
        if type(p_or_case) is str:
            case = p_or_case
            u = xs_or_u
            #epilog = (case, u)
            epilog = grouped_record
            epilogs8out.append(epilog)
                #epilogs8out.append(grouped_record)
        else:
            p = p_or_case
            xs = xs_or_u
            for (ea, eb, a, b) in xs:
                record = (ea, eb, a, b, p)
                records.append(record)
            records
    records.sort(key=_record2key)
    return _core4compact_(records)
    epilogs8out
    return chain(_core4compact_(records), epilogs8out)

def 逆函数纟重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌(*, ipath, encoding='ascii'):
    '逆函数{重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌()}'
    iter_lines = iter_read_lines_(ipath=ipath, encoding=encoding)
    epilogs8out = []

    iter_sorted_records = _iter_read_sorted_records5lines4compact_file_type_(epilogs8out, iter_lines)
        #'(Iter line){@compact_file_type} -> sorted (Iter record/(ea, eb, a, b, p))'
    alter_sorted_records = sorted(iter_sorted_records, key=_record2key)
    # [alter_sorted_records sorted by key:key4record]

    iter_p_sorted_alter_sorted_grouped_records = _core4group_extract_(alter_sorted_records, to_count=False)
        # '(Iter record/(ea, eb, a, b, p)){sorted by key:key4record/(ea, a, eb, b, p)} -> (Iter grouped_record/(p, [(ea, eb, a, b)]{sorted by key:(ea, a, eb, b)})){sorted by key:p}{@compact_file_type}'
    # [iter_p_sorted_alter_sorted_grouped_records sorted by key:p]

    yield from iter_p_sorted_alter_sorted_grouped_records
    yield from epilogs8out
    return
    #######打印改为枚举#######
    #.#for (p, ea_eb_a_b__ls) in iter_grouped_records:
    #.for grouped_record in iter_p_sorted_alter_sorted_grouped_records:
    #.    print(grouped_record)
    #.for epilog in epilogs8out:
    #.    print(epilog)
    #.return
#end-def 逆函数纟重排格式以减小压缩包体积纟输出文件牜含不同双幂方和分解扌(*, ipath, encoding='ascii'):

def _缩水过滤冫输出文件牜重排后牜无结束语牜压缩包扌(max1_p__or__predicator4p, /, *, ipath):
    # e.g. ipath:='script/枚举冫双幂方和型素数.py.out/lzma/枚举冫双幂方和型素数.py.compact.decompositions_lt_2pow32.out.txt.tar.lzma'
    from seed.for_libs.for_tarfile import iter_read_solo_tarfile_
    iter_lines = iter_read_solo_tarfile_(ipath, xencoding4data='ascii')
    iter_sorted_records = _iter_read_sorted_records5lines4compact_file_type_(may_epilogs8out:=None, iter_lines)
    iter_sorted_records = _filter_records_(max1_p__or__predicator4p, iter_sorted_records)
    return _lines5sorted_records_(iter_sorted_records)
#def _filter_keys4records_(max1_p__or__predicator4p, keys4records, /):
def _filter_records_(max1_p__or__predicator4p, records, /):
    if callable(max1_p__or__predicator4p):
        predicator4p = max1_p__or__predicator4p
        p2ok_ = predicator4p
    else:
        max1_p = max1_p__or__predicator4p
        #p2ok_ = max1_p.__gt__
        def p2ok_(p, /):
            return p < max1_p
    p2ok_ # :: p -> ok
    #for key4record in keys4records:
        #(ea, a, eb, b, p) = key4record
    for record in records:
        (ea, eb, a, b, p) = record
        if  p2ok_(p):
            yield record
#end-def _filter_records_(max1_p__or__predicator4p, records, /):
def _lines5sorted_records_(sorted_records, /):
    'sorted (Iter record/(ea, eb, a, b, p)) -> (Iter line){@compact_file_type}'
    #vs:_lines5records__alter_sorted_()
    ######################new:
    iter_mixed_compact_records = iter_mixed_compact_records5sorted_records_(sorted_records)
    for mixed_compact_record in iter_mixed_compact_records:
        (x, y) = mixed_compact_record
        if type(y) is int:
            #head_record4compact_file_type
            (ea, eb) = ea_eb = mixed_compact_record
            yield str(ea_eb)
        else:
            #data_record4compact_file_type
            assert type(y) is list
            (delta_a, ls4delta_b) = mixed_compact_record
            assert len(ls4delta_b)
            s = ','.join(map(str, ls4delta_b))
            yield f'{delta_a}:{s}'
    ######################old:
    #.def iter4flush_(ss, /):
    #.    if not ss:
    #.        # []
    #.        #   !! init or del big-p
    #.        return
    #.    ######################
    #.    if ss[-1] == ':':
    #.        #   !! big-p
    #.        pass
    #.    else:
    #.        assert ss[-1] == ','
    #.        ss.pop()
    #.        line = ''.join(map(str, ss))
    #.        yield line
    #.    ######################
    #.    ss.clear()
    #.    yield from iter4flush_(ss)
    #.    ######################
    #.prev__ea_eb = ()
    #.ss = []
    #.for (ea, eb, a, b, p) in sorted_records:
    #.#for (ea, a, eb, b, p) in keys4records:
    #.    #record = (ea, eb, a, b, p)
    #.    #if not p2ok_(p):continue
    #.    ea_eb = (ea, eb)
    #.    if not ea_eb == prev__ea_eb:
    #.        prev__ea_eb = ea_eb
    #.        yield str(ea_eb)
    #.        prev_a = 0
    #.    if not a == prev_a:
    #.        delta_a = a - prev_a
    #.        777;    prev_a = a
    #.        yield from iter4flush_(ss)
    #.        ss += [delta_a, ':']
    #.        prev_b = 0
    #.    if not b == prev_b:
    #.        delta_b = b - prev_b
    #.        777;    prev_b = b
    #.        ss += [delta_b, ',']
    #.#end-for (ea, a, eb, b, p) in keys4records:
    #.yield from iter4flush_(ss)
#end-def _lines5sorted_records_(sorted_records, /):
def iter_mixed_compact_records5sorted_records_(sorted_records, /):
    'sorted (Iter record/(ea, eb, a, b, p)) -> (Iter mixed_compact_record/((ea,eb)|(delta_a,[delta_b])))'
    def iter_tmay_data_record4flush_(delta_a, ls4delta_b, /):
        assert (delta_a is None) is (not ls4delta_b)
        if not ls4delta_b:
            # []
            #   !! init or del big-p
            return
        ######################
        yield (delta_a, ls4delta_b)
        ######################
        ls4delta_b.clear()
        ######################
    prev__ea_eb = ()
    ls4delta_b = []
        # :: [delta_b]
    last_delta_a = None
    for (ea, eb, a, b, p) in sorted_records:
        #record = (ea, eb, a, b, p)
        ea_eb = (ea, eb)
        if not ea_eb == prev__ea_eb:
            # new-block
            assert prev__ea_eb < ea_eb
            prev__ea_eb = ea_eb
            yield (ea_eb)
                # head_record4compact_file_type
            prev_a = 0
        if not a == prev_a:
            assert prev_a < a
            #bug:yield from iter_tmay_data_record4flush_(prev_a, ls4delta_b)
            yield from iter_tmay_data_record4flush_(last_delta_a, ls4delta_b)
                # data_record4compact_file_type
            assert not ls4delta_b
            delta_a = a - prev_a
            777;    prev_a = a
            777;    last_delta_a = delta_a
            prev_b = 0
        if not b == prev_b:
            delta_b = b - prev_b
            777;    prev_b = b
            ls4delta_b.append(delta_b)
    #end-for (ea, a, eb, b, p) in keys4records:
    yield from iter_tmay_data_record4flush_(last_delta_a, ls4delta_b)
    assert not ls4delta_b
#end-def iter_mixed_compact_records5sorted_records_(sorted_records, /):
def _mk_昵称讠路径纟测试用数据文件(*, dir_path4text='script/枚举冫双幂方和型素数.py.out/txt/', dir_path4lzma='script/枚举冫双幂方和型素数.py.out/lzma/'):
    prefix4common = '枚举冫双幂方和型素数.py.'
    neck_prefix4RRF = 'decompositions_lt_2pow'
    neck_prefix4ZGF = 'len_ge2__grouped_decompositions_lt_2pow'
    neck_prefix4NECF = 'compact.decompositions_lt_2pow'
    neck_prefix4AECF = 'compact.len_ge2__grouped_decompositions_lt_2pow'
    suffix4text = '.out.txt'
    suffix4lzma = '.out.txt.tar.lzma'
    _昵称讠路径纟测试用数据文件 = {**{}
    ,'RRF@zpow16'
        :fr'{dir_path4text!s}/{prefix4common}{neck_prefix4RRF}16{suffix4text}'
    ,'ZGF@zpow16'
        :fr'{dir_path4text!s}/{prefix4common}{neck_prefix4ZGF}16{suffix4text}'
    ,'NECF@zpow16'
        :fr'{dir_path4text!s}/{prefix4common}{neck_prefix4NECF}16{suffix4text}'
    ,'NECF@zpow16@lzma'
        :fr'{dir_path4lzma!s}/{prefix4common}{neck_prefix4NECF}16{suffix4lzma}'
    ,'AECF@zpow16'
        :fr'{dir_path4text!s}/{prefix4common}{neck_prefix4AECF}16{suffix4text}'
    ,'AECF@zpow16@lzma'
        :fr'{dir_path4lzma!s}/{prefix4common}{neck_prefix4AECF}16{suffix4lzma}'
    ,'NECF@zpow20'
        :fr'{dir_path4text!s}/{prefix4common}{neck_prefix4NECF}20{suffix4text}'
    ,'NECF@zpow20@lzma'
        :fr'{dir_path4lzma!s}/{prefix4common}{neck_prefix4NECF}20{suffix4lzma}'
    }
    return _昵称讠路径纟测试用数据文件
def _测试扌(*, dir_path4text='script/枚举冫双幂方和型素数.py.out/txt/', dir_path4lzma='script/枚举冫双幂方和型素数.py.out/lzma/'):
    ######################
    d = _mk_昵称讠路径纟测试用数据文件(dir_path4text=dir_path4text, dir_path4lzma=dir_path4lzma)
    RRF_zpow16 = d['RRF@zpow16']
    ZGF_zpow16 = d['ZGF@zpow16']
    NECF_zpow16 = d['NECF@zpow16']
    NECF_zpow16_lzma = d['NECF@zpow16@lzma']
    AECF_zpow16 = d['AECF@zpow16']
    AECF_zpow16_lzma = d['AECF@zpow16@lzma']
    NECF_zpow20 = d['NECF@zpow20']
    NECF_zpow20_lzma = d['NECF@zpow20@lzma']
    ######################
    #检查冫存在性纟测试用文件+命令纟生成冫测试用文件
    from pathlib import Path
    path = Path(RRF_zpow16)
    if not path.is_file():
        cmd = f'py_adhoc_call   script.枚举冫双幂方和型素数   ,枚举冫双幂方和型素数牜非平凡平方和牜小于扌 ='2**16' > {RRF_zpow16!s}'
        print(cmd)
    path = Path(ZGF_zpow16)
    if not path.is_file():
        cmd = f'py_adhoc_call   script.枚举冫双幂方和型素数   ,枚举冫双幂方和型素数牜非平凡平方和牜小于扌 ='2**16' > {RRF_zpow16!s}'
py_adhoc_call   script.枚举冫双幂方和型素数   ,_归组过滤冫素数牜含不同双幂方和分解扌  --marker=None  --_cased_doc='("path", "/sdcard/0my_files/tmp/0tmp", "utf8")' +to_count > /sdcard/0my_files/tmp/1tmp
        print(cmd)
    ######################
    ######################
    TODO

__all__
from script.枚举冫双幂方和型素数 import 枚举冫双幂方和型素数牜非平凡平方和牜小于扌
from script.枚举冫双幂方和型素数 import *
