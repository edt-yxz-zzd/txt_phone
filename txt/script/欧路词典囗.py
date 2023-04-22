#__all__:goto
r'''[[[
e script/欧路词典囗.py
py -m nn_ns.app.debug_cmd    script.欧路词典囗

[大略成分:
    词义全文囗字节串(=包全文囗字节串)(不含 词条)使用zlib分段压缩。压缩前，除尾段，每段皆长0x4000。

    文件最后是2808字节的 英文二十六字母二级前缀分层

    文件次后是 词汇囗字节串(=词条数组囗字节串)

    另有 元素字节数固定的数组:
        * 压缩包地址数组
            :: [压缩包地址/addr]
        * 词汇各词字节偏移量囗信息表
            :: [(词条 于 词汇囗字节串 中的 偏移量/size/递增, 解包后 词义 于 包全文囗字节串 中的 地址/addr/无序, 解包后 词义囗字节数/size)]
    addr::uint64LE
    size::uint32LE
]

[main:本脚本主要函数:
    explain_ipath_
        _G
    试读囗囗定位关键位置全过程囗自动化囗
        试读囗囗固定囗囗压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量囗
            _mk_reader5many_addr
        试读囗囗假设简介字节数地址固定囗
            _mk_reader5addr4introduction
]


[TODO:
    errors := relpace
    see:py-src-zlib:what is
        『Error -3 while decompressing data: invalid distance too far back』
        『Error -3 while decompressing data: incorrect header check』
        view ../../../../20220614_copy5sd__0my_files/unzip/py/Python3_9_13-20220517/Python-3.9.13/Python-3.9.13/Modules/zlibmodule.c
            还没找到『"zlib.h"』
]

计算机词汇
现代汉语词典
中华成语大词典
新世纪英汉科技大词典
新世纪汉英科技大词典
二十一世纪英汉汉英双向词典
汉语大辞典
[[解析结果:
#默认使用:试读囗囗假设简介字节数地址固定囗
#   只有 二十一世纪英汉汉英双向词典 不同
计算机词汇
    无错
现代汉语词典
    无错
中华成语大词典
    无错
新世纪英汉科技大词典
    无错
新世纪汉英科技大词典
    出错:第[369, 370, 371, 372, 373, 374, 375]包
    5321行 出错
        欧路词典app:多解码出:295行

二十一世纪英汉汉英双向词典 #rrr #'20017.eudb'
    无错<<==试读囗囗固定囗囗压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量囗
        #原来推断的格式错<<==试读囗囗假设简介字节数地址固定囗
        重新推:see:定位关键位置全过程
    ??? 21世纪英汉汉英双向词典
        已确认是 双向-词典 <<==试读囗囗固定囗囗压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量囗
        『rrr』-->二十一世纪英汉汉英双向词典

汉语大辞典
    出错:第[5176, 5177]包
    61行 出错
        欧路词典app:多解码出:25行

尝试修复出错压缩包，失败。

view script/欧路词典囗.py.尝试修复-汉语大辞典.txt
!!! sd卡 错块 !!!
汉语大辞典:5176,5177
5176起始地址:0x25DE58A
5176出错地址:0x25E0000
5177起始地址:0x25E0421
错误为：file[0x25E0000:.+0x1000] := file[0x2600000:.+0x1000]

新世纪汉英科技大词典
369起始地址:0x1FF717
369出错地址:0x200000
370起始地址:0x200BEE
错误为：file[0x200000:.+0x8000] := file[0x1E0000:.+0x8000]
]]


[[[[[
ls /sdcard/0my_files/tmp/out4py/script.欧路词典囗.* -1
    查看已输出的文件+出错压缩包
======================
======================
计算机词汇
现代汉语词典
中华成语大词典
新世纪英汉科技大词典
新世纪汉英科技大词典
二十一世纪英汉汉英双向词典
汉语大辞典
======================
======================
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇.txt
======================
======================
======================
======================
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.txt
115K
======================
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词典.txt
6.7M
======================
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词典.txt
27M
======================
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词汇囗依词义序囗附词义字节串信息.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词典.txt
24M
======================
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇囗依词义序囗附词义字节串信息.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词典.txt
25M 有错 『#』
======================
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇囗依词义序囗附词义字节串信息.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词典.txt
54M
======================
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇囗依词义序囗附词义字节串信息.单列校验.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt
157M 有错 『#』
======================
======================
]]]]]
[[[[[全结果of定位关键位置全过程囗自动化囗:

py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:计算机词汇
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:现代汉语词典
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:中华成语大词典
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:新世纪英汉科技大词典
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:新世纪汉英科技大词典
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:rrr
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:汉语大辞典
======

======================
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:计算机词汇
======================
压缩包数量囗地址=0x53B=1339
压缩包数量=0x4=4
压缩包地址数组囗起始地址=0x53F=1343
压缩包地址数组囗结束地址=0x55F=1375
首个压缩包地址=0x560=1376
末尾压缩包地址=0x6E2C=28204
压缩包数组囗结束地址=0x7103=28931
词汇各词字节偏移量囗起始地址=0x7103=28931
词汇各词字节偏移量囗结束地址=0x1F033=127027
词汇量=0x17F3=6131
词汇字节数=0xA681=42625
词汇起始地址=0x1F03B=127035
词汇结束地址=0x296BC=169660
文件字节数=0x2A1B4=172468
======================




======================
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:现代汉语词典
======================
压缩包数量囗地址=0x69A=1690
压缩包数量=0x184=388
压缩包地址数组囗起始地址=0x69E=1694
压缩包地址数组囗结束地址=0x12BE=4798
首个压缩包地址=0x12BF=4799
末尾压缩包地址=0x2E07F1=3016689
压缩包数组囗结束地址=0x2E0B88=3017608
词汇各词字节偏移量囗起始地址=0x2E0B88=3017608
词汇各词字节偏移量囗结束地址=0x3C15B8=3937720
词汇量=0xE0A3=57507
词汇字节数=0x5AC7E=371838
词汇起始地址=0x3C15C0=3937728
词汇结束地址=0x41C23E=4309566
文件字节数=0x41CD36=4312374
======================




======================
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:中华成语大词典
======================
压缩包数量囗地址=0x5FB=1531
压缩包数量=0x65F=1631
压缩包地址数组囗起始地址=0x5FF=1535
压缩包地址数组囗结束地址=0x38F7=14583
首个压缩包地址=0x38F8=14584
末尾压缩包地址=0x92A68E=9610894
压缩包数组囗结束地址=0x92AFA4=9613220
词汇各词字节偏移量囗起始地址=0x92AFA4=9613220
词汇各词字节偏移量囗结束地址=0x9EC034=10403892
词汇量=0xC109=49417
词汇字节数=0x98B0B=625419
词汇起始地址=0x9EC03C=10403900
词汇结束地址=0xA84B47=11029319
文件字节数=0xA8563F=11032127
======================




======================
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:新世纪英汉科技大词典
======================
压缩包数量囗地址=0x61F=1567
压缩包数量=0x2BA=698
压缩包地址数组囗起始地址=0x623=1571
压缩包地址数组囗结束地址=0x1BF3=7155
首个压缩包地址=0x1BF4=7156
末尾压缩包地址=0x47574E=4675406
压缩包数组囗结束地址=0x4764EB=4678891
词汇各词字节偏移量囗起始地址=0x4764EB=4678891
词汇各词字节偏移量囗结束地址=0xE0757B=14710139
词汇量=0x99109=626953
词汇字节数=0xA7B300=10990336
词汇起始地址=0xE07583=14710147
词汇结束地址=0x1882883=25700483
文件字节数=0x188337B=25703291
======================




======================
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:新世纪汉英科技大词典
======================
压缩包数量囗地址=0x61F=1567
压缩包数量=0x35F=863
压缩包地址数组囗起始地址=0x623=1571
压缩包地址数组囗结束地址=0x211B=8475
首个压缩包地址=0x211C=8476
末尾压缩包地址=0x4A046F=4850799
压缩包数组囗结束地址=0x4A1948=4856136
词汇各词字节偏移量囗起始地址=0x4A1948=4856136
词汇各词字节偏移量囗结束地址=0xE1C4D8=14795992
词汇量=0x97AB9=621241
词汇字节数=0x83F579=8648057
词汇起始地址=0xE1C4E0=14796000
词汇结束地址=0x165BA59=23444057
文件字节数=0x165C551=23446865
======================




======================
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:rrr
======================
压缩包数量囗地址=0x4BE=1214
压缩包数量=0xCA6=3238
压缩包地址数组囗起始地址=0x4C2=1218
压缩包地址数组囗结束地址=0x69F2=27122
首个压缩包地址=0x69F3=27123
末尾压缩包地址=0xD27CF0=13794544
压缩包数组囗结束地址=0xD294CB=13800651
词汇各词字节偏移量囗起始地址=0xD294CB=13800651
词汇各词字节偏移量囗结束地址=0x105A0CB=17146059
词汇量=0x330C0=209088
词汇字节数=0x1D7C33=1932339
词汇起始地址=0x105A0D3=17146067
词汇结束地址=0x1231D06=19078406
文件字节数=0x12327FE=19081214
======================




======================
py_adhoc_call   script.欧路词典囗   @定位关键位置全过程囗自动化囗 --ipath:汉语大辞典
======================
压缩包数量囗地址=0x77B=1915
压缩包数量=0x263C=9788
压缩包地址数组囗起始地址=0x77F=1919
压缩包地址数组囗结束地址=0x1395F=80223
首个压缩包地址=0x13960=80224
末尾压缩包地址=0x4752476=74785910
压缩包数组囗结束地址=0x4752E78=74788472
词汇各词字节偏移量囗起始地址=0x4752E78=74788472
词汇各词字节偏移量囗结束地址=0x4CA3F58=80363352
词汇量=0x5510E=348430
词汇字节数=0x23FD56=2358614
词汇起始地址=0x4CA3F60=80363360
词汇结束地址=0x4EE3CB6=82721974
文件字节数=0x4EE47AE=82724782
======================



]]]]]















!rm /sdcard/0my_files/tmp/out4py/script.欧路词典囗.看看有哪些直接存储的字符串.现代汉语词典.gb.out.txt
!rm /sdcard/0my_files/tmp/out4py/script.欧路词典囗.看看有哪些直接存储的字符串.现代汉语词典.out.txt
!rm /sdcard/0my_files/tmp/out4py/script.欧路词典囗汉语大辞典.看看有哪些直接存储的字符串.out.txt



py_adhoc_call   script.欧路词典囗   @看看有哪些直接存储的字符串 --iencoding:utf8 --ipath:/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/999999.eudb --opath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗.看看有哪些直接存储的字符串.某某词典.out.txt
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.看看有哪些直接存储的字符串.某某词典.out.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.看看有哪些直接存储的字符串.某某词典.out.txt

py_adhoc_call   script.欧路词典囗   @read_at_0x69e_现代汉语词典
py_adhoc_call   script.欧路词典囗   @read_at_0x2e0b88_0x3c15b8_现代汉语词典
py_adhoc_call   script.欧路词典囗   @read_at_0x41c23e_现代汉语词典

~/my_tmp/out4py/xxx
view /sdcard/0my_files/tmp/out4py/xxx


现代汉语词典
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:现代汉语词典   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词汇.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.杂项.txt  +force
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词典.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.杂项.txt


du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.现代汉语词典.out.词典.txt
6.7M
du -bh /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/375916128.eudb
4.2M


计算机词汇
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:计算机词汇   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.杂项.txt
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:计算机词汇   --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.杂项.单列校验.txt
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:计算机词汇   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇.单列校验.txt
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:计算机词汇   --输出文件囗词汇囗依词义序:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇囗依词义序囗附词义字节串信息.单列校验.txt
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:计算机词汇   --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.单列校验.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇囗依词义序囗附词义字节串信息.单列校验.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.杂项.txt
diff /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.杂项.txt /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.杂项.单列校验.txt
    #same
diff /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇.txt /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词汇.单列校验.txt
    #same
diff /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.txt /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.单列校验.txt
    #same
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.txt
115K


中华成语大词典
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:中华成语大词典   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词汇.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词典.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.杂项.txt
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词典.txt
27M

新世纪英汉科技大词典
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:新世纪英汉科技大词典   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词汇.txt  --输出文件囗词汇囗依词义序:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词汇囗依词义序囗附词义字节串信息.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词汇囗依词义序囗附词义字节串信息.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词典.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.杂项.txt
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪英汉科技大词典.out.词典.txt
24M



新世纪汉英科技大词典
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:新世纪汉英科技大词典   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇.txt  --输出文件囗词汇囗依词义序:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇囗依词义序囗附词义字节串信息.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.杂项.txt
    囗出错囗写出囗
        raise Exception(folder4err_idc, len(压缩包数组), len(err_idc), err_idc, msgs)
    Exception: (PosixPath('/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗'), 863, 7, [369, 370, 371, 372, 373, 374, 375], ['error("decoding with \'zlib\' codec failed (error: Error -3 while decompressing data: incorrect header check)")', 'error("decoding with \'zlib\' codec failed (error: Error -3 while decompressing data: invalid distance too far back)")'])
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:新世纪汉英科技大词典   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇.txt  --输出文件囗词汇囗依词义序:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇囗依词义序囗附词义字节串信息.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.杂项.txt +errors_replace
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词汇囗依词义序囗附词义字节串信息.txt
[[
出错:[369, 370, 371, 372, 373, 374, 375]
==>> [369*bufsize4zlib_decompress..<376*bufsize4zlib_decompress]
==>> [369*0x4000..<376*0x4000]
printf $'%X\n%X\n' $[369*0x4000] $[376*0x4000]
5C4000
5E0000
==>> [5C4000..<5E0000]
==>>:
5321行 出错
    欧路词典:多解码出:295行
0x5C3F9E:11:放风阀绳轮
0x5C3FA9:12:放马员
0x5C3FB5:57:放高利贷
0x5C3FEE:23:放鱼道
    265432行
0x5C4005:22:政务用户电报
0x5C401B:22:政务电报
0x5C4031:26:政务电报密码
...
...
0x5C47C8:22:故障后平衡
    265515行
    欧路词典:对:post-fault equilibrium
...
0x5C4F65:22:故障消除时间
    265598行
    欧路词典:对:clearing time of fault
...
0x5C561C:8:效应因子
    265681行
    欧路词典:对:effector
...
0x5C597F:19:效率差异
    265722行
    欧路词典:对:efficiency variance
...
0x5C59B2:16:效率指数
    欧路词典:对:efficiency index
0x5C59C2:19:效率收入
    265726行
    欧路词典:对:efficiency earnings
0x5C59D5:16:效率曲线
    265727行
    欧路词典:半对错:efficiency lure
0x5C59E5:16:效率检查
    欧路词典:错:earnurepanceeffi
0x5C59F5:16:效率比
    欧路词典:错:ciaSindexeirniti
...
0x5C5C9D:13:效用水平
    265764行
    欧路词典:错:opertyprices
...
0x5CBA20:22:散装货仓库
    266762行
    欧路词典:错:imal wasteanimal breed
...
0x5D2593:12:整体刀盘
    268092行
    欧路词典:错:sisphysical
        没找到
...
0x5DC12F:17:斜率灵敏度
    欧路词典:错:ill abortion
    唯一出现在:
        ,牛流行性流产
        :foothill abortion<br />epizootic bovine abortion
...
0x5DDE4A:5:断入
    欧路词典:错:ning
...
0x5DFF9A:39:断裂分析
0x5DFFC1:31:断裂分析图
0x5DFFE0:30:断裂初始抗力
0x5DFFFE:18:断裂判据
    270752行
0x5E0010:16:断裂剖面
0x5E0020:45:断裂力学
0x5E004D:35:断裂力矩
----
echo $[270752-265432+1]
5321行 出错
    欧路词典:多解码出:295行
    echo $[265726-265432+1]
    295

echo $[265432+(270752-265432+1)/2]
268092
echo $[265432+(270752-265432+1)/4]
266762
echo $[265432+(270752-265432+1)/16]
265764
echo $[265432+(270752-265432+1)/64]
265515
echo $[265432+(270752-265432+1)/32]
265598
echo $[265598+(265764-265598)/2]
265681
echo $[265598+(265764-265598)*3/4]
265722
]]
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词典.txt
25M
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.新世纪汉英科技大词典.out.词典.txt
[[
,斑
    17533行，词汇[17533/2]
,斑疤
,斑驳
,斑驳器
,斑驳状态
,斑点
...
...
,断裂判据
    239677行
...
...
,放鱼道
    285497行
:fish pass<br />fis#####
    搜索唯一『[/^#:]#』
:##acture criterion
    搜索唯一『/#[^#]』
...
...
,政府专利
,政务电报
,政务电报密码
,政务电话
,政务通报
,政务用户电报
    1161455行，词汇[1161454/2]
]]











汉语大辞典
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:汉语大辞典   --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.杂项.单列校验.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.杂项.单列校验.txt
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:汉语大辞典   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇.单列校验.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇.单列校验.txt
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:汉语大辞典   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.杂项.txt
        ,('包数组囗整合囗全字节串', (lambda 压缩包数组, /:mk_ConstantTargetReader(b''.join(apply_decoder(zlib_decoder, bs) for bs in 压缩包数组))), ['压缩包数组'])
    zlib.error: decoding with 'zlib' codec failed (error: Error -3 while decompressing data: invalid distance too far back)
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:汉语大辞典   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.杂项.txt +errors_replace
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.杂项.txt
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt
157M
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:汉语大辞典   --输出文件囗词汇囗依词义序:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇囗依词义序囗附词义字节串信息.单列校验.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇囗依词义序囗附词义字节串信息.单列校验.txt
0x50DFE17:1235:牢落
    181914行
0x50E7E8F:1173:牧民
    181974行
    [5176, 5177]包出错
        ==>>[5176*bufsize4zlib_decompress..<5178*bufsize4zlib_decompress]
        ==>>[5176*0x4000..<5178*0x4000]
        ==>>[0x50e0000..<0x50e8000]
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt
[[
词义解包出错而被替代为『�』的
assert REPLACEMENT_CHARACTER == '\uFFFD' == chr(0xFFFD) == '�' == u8_bytes4REPLACEMENT_CHARACTER.decode('u8') == b'\x80'.decode(encoding='ascii', errors='replace')

,牧民
    部分内容丢失:前缀丢失
    350955行，词汇[350954]
    『�』只出现一次
]]
[[

view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典.txt
词义解包出错而被替代为『#』的
,牢髀
    291163行，词汇[291162/2]
    第一个
,牢車
,牢誠
,牢辭
,牢鼎
,牢飯碗
,牢護
,牢記
,牢藉
,牢酒
,牢靠
,牢醴
,牢落
    部分内容丢失:后缀丢失
    291245行，词汇[291244/2]
,牢讓
,牢騷
,牢賞
,牢蔬
,牢頭
,牢餼
,牢饌
,牦
,牦牛
,牧
,牧包
,牧伯
,牧曹
,牧場
,牧廠
,牧倅
,牧地
,牧丁
,牧兒
,牧放
,牧夫
,牧副
,牧歌
,牧工
,牧宮
,牧戶
,牧令
,牧民
    部分内容丢失:前缀丢失
    350955行，词汇[350954/2]
,牧奴
,牧區
,牧人
,牧師
,牧室
,牧守
,牧司
,牧宿
,牧所
,牧嘯
,牧業
,牧圉
,牧宰
,牧正
,牧主
,牧子
,牧字
,牣
,牣充
,牣積
    416611行，词汇[416610/2]
    最后一个


共61个词出错:但欧路词典能正常解码『牧』之前的词。
    『牧』-『牧民』36个词出错
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词汇囗依词义序囗附词义字节串信息.单列校验.txt
0x50DFE17:1235:牢落
    ---0x50e0000开始毛病
    欧路词典:『牢落』词义 无错
0x50E02EA:138:牢蔬
0x50E0374:370:牢藉
0x50E04E6:523:牢記
0x50E06F1:151:牢誠
0x50E0788:199:牢護
0x50E084F:474:牢讓
0x50E0A29:227:牢賞
0x50E0B0C:148:牢車
0x50E0BA0:175:牢辭
0x50E0C4F:219:牢酒
0x50E0D2A:307:牢醴
0x50E0E5D:574:牢靠
0x50E109B:281:牢頭
0x50E11B4:108:牢飯碗
0x50E1220:447:牢餼
0x50E13DF:405:牢饌
0x50E1574:947:牢騷
0x50E1927:187:牢髀
0x50E19E2:280:牢鼎
0x50E1AFA:1121:牣
0x50E1F5B:246:牣充
0x50E2051:329:牣積
    欧路词典:『牣積』词义 无错
0x50E219A:181:牦
    欧路词典:『牦』词义 无错
0x50E224F:214:牦牛
    欧路词典:『牦牛』词义 无错
0x50E2325:6313:牧
    欧路词典:『牧』词义 后半出错
    -----欧路词典 zlib解码器 比py.zlib灵活
0x50E3BCE:234:牧丁
    欧路词典:『牧丁』词义 全错
0x50E3CB8:408:牧主
    欧路词典:『牧主』词义 全错
0x50E3E50:1529:牧人
0x50E4449:458:牧令
0x50E4613:1003:牧伯
0x50E49FE:186:牧倅
0x50E4AB8:559:牧兒
0x50E4CE7:225:牧副
0x50E4DC8:323:牧包
0x50E4F0B:374:牧區
0x50E5081:663:牧司
0x50E5318:271:牧嘯
0x50E5427:1721:牧圉
0x50E5AE0:429:牧地
0x50E5C8D:664:牧場
0x50E5F25:490:牧夫
0x50E610F:429:牧奴
0x50E62BC:442:牧子
0x50E6476:180:牧字
0x50E652A:522:牧守
0x50E6734:374:牧室
0x50E68AA:583:牧宮
0x50E6AF1:500:牧宰
0x50E6CE5:234:牧宿
0x50E6DCF:414:牧工
0x50E6F6D:973:牧師
0x50E733A:455:牧廠
0x50E7501:256:牧戶
0x50E7601:256:牧所
0x50E7701:440:牧放
0x50E78B9:168:牧曹
0x50E7961:229:牧業
0x50E7A46:610:牧歌
0x50E7CA8:487:牧正
    欧路词典:『牧正』词义 全错
0x50E7E8F:1173:牧民
    欧路词典:『牧民』词义 全错
    ---0x50e8000再次正常
0x50E8324:244:牧漁
    欧路词典:『牧漁』词义 无错
printf $'%x\n' $[0x50e8000-0x50E2325]
5cdb
echo $[0x50e8000-0x50E2325]
23771
    #2万3千字节出毛病
echo $[0x50E2325-0x50e0000]
8997
    #9千字节可正常解压

]]
[[

欧路词典『牢落』解释 完整:[[

牢落
1.猶寥落。稀疏零落貌；零落荒蕪貌。
 《文選‧司馬相如＜上林賦＞》：“牢落陸離，爛熳遠遷。”
 李善注：“牢落陸離，群奔走也。牢落，猶遼落也。”
 晉左思《魏都賦》：“伊洛榛曠，崤函荒蕪，臨菑牢落，鄢郢丘墟。”
 唐韓愈《天星送楊凝郎中賀正》詩：“天星牢落雞喔咿，僕夫起餐車載脂。”
 唐羅鄴《僕射陂晚望》詩：“田園牢落東歸晚，道路辛勤北去長。”
 清李重華《擬魏武帝紀行》：“秦原莽牢落，空舍無炊煙。”
2.孤寂；無聊。
 晉陸機《文賦》：“心牢落而無偶，意徘徊而不能揥。”
 唐張九齡《自彭蠡湖初入江》詩：“牢落誰相顧，逶迤日自愁；更將心問影，於役復何求？”宋孟元老《＜東京夢華錄＞序》：“出京南來，避地江左，情緒牢落，漸入桑榆。”
 元馬致遠《青衫淚》第三摺：“樂天久居江鄉，牢落殊甚，下官常切懷抱。”
 清陳學洙《與繆天自夜話》詩：“牢落蕭齋病後身，燈前款款話相親。”
]]
欧路词典『牧民』解释 出错，截取了『物』的部分解释，但『物』本身解释未出毛病:[[
汉语大辞典
屬一色之義。”
 王國維《釋物》：“古者謂雜帛為物，蓋由物本雜色牛之名，後推之以名雜帛。
 《詩‧小雅》曰：‘三十維物，爾牲則具。’……謂雜色牛三十也。由雜色牛之名因之以名雜帛，更因以名萬有不齊之庶物，斯文字引申之通例矣。”參閱李孝定《甲骨� 
]]

,牢落
:<B>牢落</B><DIV><DIV>1.猶寥落。稀疏零落貌；零落荒蕪貌。<BR>&nbsp;《文選‧司馬相如＜上林賦＞》：“牢落陸離，爛熳遠遷。”<BR>&nbsp;李善注：“牢落陸離，群奔走也。牢落，猶遼落也。”<BR>&nbsp;晉左思《魏都賦》：“伊洛榛曠，崤函荒蕪，臨菑牢落，鄢郢丘墟。”<BR>&nbsp;唐韓愈《天星送楊凝郎中賀正》詩：“天星牢落雞喔咿，僕夫起餐車載脂。”<BR>&nbsp;唐羅鄴《僕射##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################



,牧民
:#################################################################################################################################################################################################################################################################################################################################################################################�，以禮樂為教，而聖人喜之，此千載牧民之良法。”<BR>&nbsp;清姚鼐《詠史》：“牧民豈謂非良幹，伐畔何教震友邦。”<BR>2.指治民的官。<BR>&nbsp;《三國志‧魏志‧明帝紀》：“其郎吏學通一經，才任牧民，博士課試，擢其高第者亟用。”<BR>&nbsp;《警世通言‧蘇知縣羅衫再合》：“我早登科甲，初任牧民，立心願為好官。”<BR>3.牧區中以畜牧為主要職業的人。<BR>&nbsp;降邊嘉措《格桑梅朵》第二十章：“由於牧民一般不吃魚，更不吃‘神湖’的魚，所以這裏的魚根本不怕人。”<BR>&nbsp;碧野《雪路雲程》：“我們的小汽車離開蒙族牧民居住的和靖縣……飛奔在依山傍河的新開闢的烏庫公路上。”</DIV></DIV>


]]



view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idc.txt
[5176, 5177]
hexdump /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5176.dat -n 0x20 -s 0x0 -C
[[
00000000  78 9c 9d 7b d9 8e 33 49  76 de ab 0c 06 f8 0d 09  |x..{..3Iv.......|
00000010  18 54 4f f7 2c ea 96 7a  1a e8 b6 6c c0 b7 06 e4  |.TO.,..z...l....|
00000020
]]

hexdump /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5177.dat -n 0x20 -s 0x0 -C
[[
00000000  f7 70 6f 04 d4 82 92 e7  3c 80 ba e8 a4 61 64 83  |.po.....<....ad.|
00000010  85 d7 98 0e 29 e7 b9 77  94 7f 47 f1 83 6b 8a 1f  |....)..w..G..k..|
00000020
======
不是『78 9c』开头！出错！
]]

py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧 路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5175.dat' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
0=0x0
6715=0x1A3B
du -b /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5175.dat
7691

py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5176.dat' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
0=0x0
du -b /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5176.dat
7831

py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5177.dat' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
971=0x3CB
du -b /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5177.dat
7908

hexdump /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5176.dat -n 0x200 -s $[7831-0x20] -C
hexdump /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5177.dat -n 0x200 -s $[7908-0x20] -C


py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-369.dat' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
0=0x0
2686=0xA7E
du -b /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-369.dat
5335

py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-370.dat' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
3540=0xDD4
du -b /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-370.dat
5613


py_adhoc_call   script.欧路词典囗   @囗尝试恢复囗新世纪汉英科技大词典囗压缩包囗369
py_adhoc_call   script.欧路词典囗   @囗尝试恢复囗汉语大辞典囗压缩包囗5177
py_adhoc_call   script.欧路词典囗   @囗尝试恢复囗汉语大辞典囗压缩包囗5176

py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5176.dat' --format4show_address $'{0}=0x{0:X}\n'    '9C 78'
无
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5177.dat' --format4show_address $'{0}=0x{0:X}\n'    '9C 78'
无




1922908499.eudb
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1922908499.eudb' --format4show_address $'{0}=0x{0:X}\n'    'xml' -e4bs ascii
1200=0x4B0

20017.eudb
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    'xml' -e4bs ascii
842207=0xCD9DF
8520398=0x8202CE

xml@0xCD9DF 偶然
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x200 -s 0xCD900 -C
[[
000cd9d0  96 dc 66 ef 2e 5a 9d 46  1a 69 2c 56 b4 71 db 78  |..f..Z.F.i,V.q.x|
000cd9e0  6d 6c e4 c7 a0 e4 07 64  f3 f4 03 db bc 02 09 e6  |ml.....d........|
000cd9f0  0d 06 92 60 6c 1e 01 63  6c f8 5f 26 ae ea f6 7f  |...`l..cl._&....|
]]
xml@0x8202CE 偶然
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x200 -s 0x820200 -C
[[
008202c0  5f ba 85 74 e0 1f 18 06  4d 27 f4 b1 0d 9a 78 6d  |_..t....M'....xm|
008202d0  6c 27 91 ae a6 b4 d9 5c  f9 8a 18 e5 13 a3 f0 a6  |l'.....\........|
008202e0  e5 83 57 08 e7 3c 71 19  db fb c6 f6 0b 37 a8 96  |..W..<q......7..|
]]

[[[[[
定位关键位置全过程
    about 20017.eudb 双向-词典
#自动化？see:定位关键位置全过程囗自动化囗
=====
zlib header4zlib
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    '78 9C' -end 0x8000
27123=0x69F3
31862=0x7C76

[[
首个压缩包地址@0x4C2=0x69F3
0x4C2==地址of首个压缩包地址of双向
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    'F3 69' -end 0x8000
6=0x6
1218=0x4C2
===vs:
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.杂项.单列校验.txt
#:2:'首个压缩包地址':@[6..<10]:@[0x6..<0xA]:=4:=0x4:80224:0x13960
#:14:'词汇各词字节偏移量囗起始地址':@[1736..<1744]:@[0x6C8..<0x6D0]:=8:=0x8:74788472:0x4752E78
#:24:'压缩包数量':@[1915..<1919]:@[0x77B..<0x77F]:=4:=0x4:9788:0x263C
0x77F==地址of首个压缩包地址of汉语大辞典
===vs:
0x4C2==地址of首个压缩包地址of双向
0x40B=0x4C2-(0x77F-0x6C8)
    xxx =?=词汇各词字节偏移量囗起始地址of双向
===
xxx 0x40B =?=词汇各词字节偏移量囗起始地址of双向
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x200 -s 0x30B -C
...
000003fb  df ce 27 5e 6e 18 56 9a  51 e3 2f 50 67 e7 f0 09  |..'^n.V.Q./Pg...|
0000040b  9a 72 2d 96 17 f8 63 bc  f8 ca d2 72 9a e6 2b fc  |.r-...c....r..+.|
0000041b  cf 94 03 f1 2d 16 a3 c7  8d 9f 54 22 90 6f a9 7a  |....-.....T".o.z|
...
000004ab  4d 35 58 ad 93 c0 30 bd  81 01 3d bc 10 da 62 8c  |M5X...0...=...b.|
000004bb  40 7b fa a6 0c 00 00 f3  69 00 00 00 00 00 00 76  |@{......i......v|
000004cb  7c 00 00 00 00 00 00 1c  8c 00 00 00 00 00 00 25  ||..............%|
==>>
压缩包数量囗地址of双向=0x4BE
压缩包数量@0x4BE=0xca6=3238
0x69f2=0x4C2+0xca6*8
b'\1'
    #补偿:\[
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x30 -s 0x69da -C
000069da  37 46 d2 00 00 00 00 00  28 62 d2 00 00 00 00 00  |7F......(b......|
000069ea  f0 7c d2 00 00 00 00 00  01 78 9c d5 5b 7d 53 13  |.|.......x..[}S.|
000069fa  59 ba ff 67 3f c0 7e 84  53 de aa 31 54 85 5c 5d  |Y..g?.~.S..1T.\]|
00006a0a
    #补偿:]
==>>
末尾压缩包地址@0x69ea=0xd27cf0
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x50 -s 0xd294bb -C
00d294bb  3f 5f 7f be fe 7c fd f9  8d 3f ff 0f 5b a2 02 d6  |?_...|...?..[...|
00d294cb  00 00 00 00 c9 2c 6a 00  00 00 00 00 0e 01 00 00  |.....,j.........|
00d294db  08 00 00 00 f0 4b 6b 00  00 00 00 00 09 01 00 00  |.....Kk.........|
00d294eb  12 00 00 00 f9 4c 6b 00  00 00 00 00 50 01 00 00  |.....Lk.....P...|
00d294fb  1a 00 00 00 70 be 09 01  00 00 00 00 01 01 00 00  |....p...........|
00d2950b
    #补偿:]
==>>
压缩包数组囗结束地址=0xd294cb=词汇各词字节偏移量囗起始地址of双向
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    'cb 94 d2 00'
    #无
===
du -bh '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb'
19M
du -b '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb'
19081214

19081214-2808==19078406
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x200 -s $[19078406-0x100] -C
[
01231cd6  e6 88 8f e5 81 9a e8 bf  90 e5 8a a8 e5 81 9a e8  |................|
01231ce6  b4 bc e5 bf 83 e8 99 9a  e5 81 9a e9 92 88 e7 ba  |................|
01231cf6  bf e6 b4 bb e5 81 9a e4  b8 bb e5 81 9a e4 bd 9c  |................|
01231d06  0a 00 00 00 15 20 00 00  da 3e 00 00 f6 6c 00 00  |..... ...>...l..|
01231d16  98 85 00 00 21 98 00 00  73 ae 00 00 8e c0 00 00  |....!...s.......|
01231d26  64 d4 00 00 ad e4 00 00  4b e9 00 00 3b ef 00 00  |d.......K...;...|
===>>:
bytes.fromhex('bf e6 b4 bb e5 81 9a e4  b8 bb e5 81 9a e4 bd 9c')[1:].decode('u8')
'活做主做作'
]
0x12327fe=19081214=字节数of双向
:0xd294cb=压缩包数组囗结束地址=词汇各词字节偏移量囗起始地址of双向

hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x50 -s 0x105a0ab -C
0105a0ab  27 7c 1d 00 3b 24 fc 02  00 00 00 00 42 00 00 00  |'|..;$......B...|
0105a0bb  2d 7c 1d 00 97 25 fc 02  00 00 00 00 5e 00 00 00  |-|...%......^...|
0105a0cb  33 7c 1d 00 00 00 00 00  28 27 29 63 61 75 73 65  |3|......(')cause|
0105a0db  28 27 29 63 65 6c 6c 69  73 74 28 27 29 63 65 6c  |(')cellist(')cel|
0105a0eb  6c 6f 28 27 29 67 61 69  6e 73 74 28 27 29 6e 65  |lo(')gainst(')ne|
0105a0fb
==>>
0x105a0cb=词汇各词字节偏移量囗结束地址of双向
词汇量of双向=209088=0x330c0=(0x105a0cb-0xd294cb)//16
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    'c0 30 03 00'
    #无
===
_mk_reader
def _mk_reader5addr4introduction(简介字节数囗地址, ...)
-->
def _mk_reader5many_addr(压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, ...)

字节数of双向=0x12327fe=19081214
压缩包数量囗地址of双向=0x4BE
压缩包数组囗结束地址of双向=词汇各词字节偏移量囗起始地址of双向=0xd294cb
词汇各词字节偏移量囗结束地址of双向=0x105a0cb
词汇量=(词汇各词字节偏移量囗结束地址-词汇各词字节偏移量囗起始地址)//16
词汇量of双向=209088=0x330c0=(0x105a0cb-0xd294cb)//16
试读囗囗固定囗囗压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量囗
===
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x500 -s 0x0 -C > /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/20017.eudb.0x0-0x500.dat
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/20017.eudb.0x0-0x500.dat
]]




#see:算法:定位关键位置全过程囗自动化囗
=====end-定位关键位置全过程
]]]]]

hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x200 -s 0x0 -C
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x200 -s 0x412 -C


>>> s = '21世纪英汉汉英双向词典'
>>> s.encode('u8').hex(' ')
'32 31 e4 b8 96 e7 ba aa e8 8b b1 e6 b1 89 e6 b1 89 e8 8b b1 e5 8f 8c e5 90 91 e8 af 8d e5 85 b8'

py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    '32 31 e4 b8 96 e7 ba aa e8 8b b1 e6 b1 89 e6 b1 89 e8 8b b1 e5 8f 8c e5 90 91 e8 af 8d e5 85 b8' -end 0x8000
    无
grep '世纪英汉汉英双向词典' '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -l
    无
grep '词典' '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -l
    有
[[
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    '词典'  -e4bs utf8
18425101=0x119250D
18446064=0x11976F0
18452724=0x11990F4
18452730=0x11990FA
18636651=0x11C5F6B
18841239=0x11F7E97  #...
18878507=0x120102B
18949955=0x1212743
18995783=0x121DA47  #---
]]
[[
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    '双向'  -e4bs utf8
18841083=0x11F7DFB
18841089=0x11F7E01
18841101=0x11F7E0D
18841119=0x11F7E1F  #...
]]
[[
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    '英汉'  -e4bs utf8
18995777=0x121DA41  #---
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    '汉英'  -e4bs utf8
  无
==>>:
'英汉'@0x121DA41
'词典'@0x121DA47

hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x200 -s $[0x121DA41-0x100] -C
]]
[[
search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    '01 00 00 00'  -end 0x121DA41 -begin 0x1200000
    无
search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' --format4show_address $'{0}=0x{0:X}\n'    '01 00 00 00'
...lots
15814808=0xF15098
15824424=0xF17628
15833928=0xF19B48
15836760=0xF1A658
15929128=0xF30F28
===
hexdump  '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/20017.eudb' -n 0x200 -s $[0xF30F28-0x100] -C
]]








======
rrr
py_adhoc_call   script.欧路词典囗   @试读囗囗假设简介字节数地址固定囗 --ipath:rrr   --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.rrr.out.词汇.txt  --输出文件囗词汇囗依词义序:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.rrr.out.词汇囗依词义序囗附词义字节串信息.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.rrr.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.rrr.out.杂项.txt
    nn_ns.codec.DecodeUtils.CheckError: not the given bytes in file : b'\x00\x00\x00\x004\x0c\x02\x00\x00\x00' != b'\x02\x00\x00\x004\x0c\x03\x00\x00\x00'
    The above exception was the direct cause of the following exception:
    raise ReadError__NamedDependentTupleReader((hex(sz4ibfile), hex(begin_addr4whole), hex(begin_addr), xname, idx4xname, sf._ts[idx4xname])) from e
    nn_ns.codec.DecodeUtils.ReadError__NamedDependentTupleReader: ('0x12327fe', '0x0', '0xa', '', 3, ('', ConstantInOutReader(b'\x02\x00\x00\x004\x0c\x03\x00\x00\x00', None), None))
======
试读囗囗固定囗囗压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量囗(*, 压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, ipath, ...)
字节数of双向=0x12327fe=19081214
压缩包数量囗地址of双向=0x4BE
压缩包数组囗结束地址of双向=词汇各词字节偏移量囗起始地址of双向=0xd294cb
词汇各词字节偏移量囗结束地址of双向=0x105a0cb
词汇量of双向=209088=0x330c0=(0x105a0cb-0xd294cb)//16

:.,$s/试读囗囗假设简介字节数地址固定囗\.rrr\./试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典./g
# py_adhoc_call   script.欧路词典囗   @试读囗囗固定囗囗压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量囗 --ipath:rrr  --压缩包数量囗地址=0x4BE --压缩包数组囗结束地址=0xd294cb --词汇量=209088 --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇.txt  --输出文件囗词汇囗依词义序:~/my_tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇囗依词义序囗附词义字节串信息.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.杂项.txt
    无错！
-->自动化:
py_adhoc_call   script.欧路词典囗   @试读囗囗定位关键位置全过程囗自动化囗 --ipath:rrr  --输出文件囗词汇:~/my_tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇.txt  --输出文件囗词汇囗依词义序:~/my_tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇囗依词义序囗附词义字节串信息.txt  --输出文件囗词典:~/my_tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词典.txt  --输出文件囗杂项:~/my_tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇囗依词义序囗附词义字节串信息.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.杂项.txt
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇.txt
    [[英语127685行;汉语81403行
000001行:(')cause
    ...
127684行:zyzzyva
127685行:zz
127686行:阿
127687行:阿比西尼亚猫
    ...
209088行:做作
    ]]
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词典.txt
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词典.txt
54M


:.,.+4s/^view \(.*\)试读囗囗定位关键位置全过程囗自动化囗\.二十一世纪英汉汉英双向词典\(.*\)/mv \1试读囗囗假设简介字节数地址固定囗.rrr\2 \1试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典\2
mv /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.rrr.out.词汇囗依词义序囗附词义字节串信息.txt /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇囗依词义序囗附词义字节串信息.txt
mv /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.rrr.out.杂项.txt /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.杂项.txt
mv /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.rrr.out.词汇.txt /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词汇.txt
mv /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.rrr.out.词典.txt /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗定位关键位置全过程囗自动化囗.二十一世纪英汉汉英双向词典.out.词典.txt


#]]]'''#'''
__all__ = r'''
    explain_ipath_
        _G
    试读囗囗定位关键位置全过程囗自动化囗
        试读囗囗固定囗囗压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量囗
            _mk_reader5many_addr
        试读囗囗假设简介字节数地址固定囗
            _mk_reader5addr4introduction
'''.split()#'''

#__all__

from zlib import decompress
import zlib
r'''
import codecs
(codecs.encode(b'abcdef', 'zlib'))
b'x\x9cKLJNIM\x03\x00\x08\x1e\x02V'
(codecs.decode(b'x\x9cKLJNIM\x03\x00\x08\x1e\x02V', 'zlib'))
(codecs.decode(b'x\x9cKLJNIM\x03\x00\x08\x1e\x02V=', 'zlib'))
    #ok!!!
(codecs.decode(b'x\x9cKLJNIM\x03\x00\x08\x1e\x02', 'zlib'))
zlib.error: decoding with 'zlib' codec failed (error: Error -5 while decompressing data: incomplete or truncated stream)
'''#'''

from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err
from seed.io.find__naive import iter_find_bytes__naive_, list_find_bytes__naive_
from seed.seq_tools.cut_seq import cut_seq_, icut_seq_
from seed.text.decode_on_err_bytes_ import decode_on_err_bytes_
    #def decode_on_err_bytes_(encoding, bs, /):
    #   :: encoding -> bytes -> (ok_strs/[str], bad_bss/[bytes]{.len=1+len(ok_strs)})
from pathlib import Path
from itertools import pairwise
from seed.tiny import mk_fprint, snd, curry1
from seed.tiny import check_type_is
from seed.io.may_open import open4w, open4w_err, open4r
from seed.func_tools.dot2 import dot



from nn_ns.codec.DecodeUtils import uintLE_decoder, uintBE_decoder

from nn_ns.codec.DecodeUtils import StrDecoder, ascii_decoder, u8_decoder, gb_decoder, zlib_decoder

from nn_ns.codec.DecodeUtils import uint32LE_reader, uint64LE_reader


#[
from nn_ns.codec.DecodeUtils import CheckError, StreamError, StreamEOFError, SeekError
from nn_ns.codec.DecodeUtils import IDecoder, IReader

from nn_ns.codec.DecodeUtils import apply_decoder, apply_reader, try_apply_decoder, try_apply_reader


from nn_ns.codec.DecodeUtils import read_bytes, skip_bytes, checked_seek, get_size_of_ibfile, size5or_size_reader__, uint5or_uint_reader__, uint_or2uint_reader_

from nn_ns.codec.DecodeUtils import echo_decoder, uintLE_decoder, uintBE_decoder

from nn_ns.codec.DecodeUtils import StrDecoder, ascii_decoder, u8_decoder, gb_decoder

from nn_ns.codec.DecodeUtils import uint32LE_reader, uint64LE_reader

from nn_ns.codec.DecodeUtils import BytesReader, ConstantInOutReader, mk_ConstantTargetReader, mk_ConstantBytesMatcher, UntilEndValueBytesReader

from nn_ns.codec.DecodeUtils import tell_addr_reader, mk_AddrAssertionReader, eof_addr_reader
from nn_ns.codec.DecodeUtils import OffsetReader, AddrReader, SeekAddrReader

from nn_ns.codec.DecodeUtils import ArrayReader, TupleReader, DependentPairReader, NamedTupleReader, NamedDependentTupleReader, ipop_and_drop4list, UntilEndValueArrayReader, UntilReadEndValueArrayReader #!!! NOTE:NamedTupleReader/NamedDependentTupleReader read result NamedTuple, using 『NamedTuple.as_getter4named_tuple()』to access attr !!!

from nn_ns.codec.DecodeUtils import FallbackReader, SkipReader, FurtherTransformReader, AssertionReader

from nn_ns.codec.DecodeUtils import AddrDereferenceReader, AddrSizedParamReader, AddrSizedParamArrayReader, ArrayTranformReader
#]





#__all__

def 看看有哪些直接存储的字符串(*, iencoding, ipath, opath=None, oencoding='utf8', force=False):
    ipath = Path(ipath)
    bs = ipath.read_bytes()
    (ok_strs, bad_bss) = decode_on_err_bytes_(iencoding, bs)
    with open4w(opath, force=force, xencoding=oencoding) as fout:
        fprint = mk_fprint(fout)
        for bad_bs, ok_str in zip(bad_bss, ok_strs):
            fprint(f'-{len(bad_bs)}')
            #fprint(f'+{ok_str!r}')
            #   \uXXXX 不行！
            for s in ok_str.split('\n'):
                fprint(f'+{s!s}')
        else:
            bad_bs = bad_bss[-1]
            fprint(f'-{len(bad_bs)}')



class _G:
    r'''[[[
计算机词汇
172K 1922908499.eudb

现代汉语词典
4.2M 375916128.eudb

中华成语大词典
11M 315772229.eudb

汉语大辞典
79M 1317108648.eudb

cd /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/
ls -S -1
1317108648.eudb
99569493.eudb
1522017926.eudb
20017.eudb
315772229.eudb
375916128.eudb
1922908499.eudb
    文件大小递减

1317108648.eudb
1046 '汉语大辞典'
99569493.eudb
1046 '新世纪英汉科技大词典'
1522017926.eudb
1046 '新世纪汉英科技大词典'
20017.eudb
1046 'r'
315772229.eudb
1046 '中华成语大词典'
375916128.eudb
1046 '现代汉语词典'
1922908499.eudb
1046 '计算机词汇'



!mkdir /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/

    #]]]'''#'''
    folder4err_idc = Path('/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/')
    folder = Path('/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/')

    计算机词汇 = folder/'1922908499.eudb'

    现代汉语词典 = folder/'375916128.eudb'

    中华成语大词典 = folder/'315772229.eudb'

    新世纪英汉科技大词典 = folder/'99569493.eudb'

    新世纪汉英科技大词典 = folder/'1522017926.eudb'

    rrr = 二十一世纪英汉汉英双向词典 = folder/'20017.eudb'

    汉语大辞典 = folder/'1317108648.eudb'
    #x = folder/'x.eudb'
        #『*』『de』『n』『v』『p』
def read_at_0x69e_现代汉语词典():
    ipath = _G.现代汉语词典
    addr = 0x69e
    bs = ipath.read_bytes()
    L = 8
    H = L//2
    u = 0
    for j,i in enumerate(range(addr, len(bs), L)):
        w = bs[i:i+L]
        if any(w[H:]):
            break
        v = uint5bytes_LE(w)
        n = v-u
        print(f'{j:0>4}:{i:0>4X}:{v:0>8X}-{u:0>8X}={n:0>4X}={n:0>4}')
        if u:
            dat = bs[u:v]
            print(decompress(dat).decode('u8'))
            # 可以解压！
            # 0002:06AE:000051BF-000031AA=2015=8213
            # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe7 in position 16383: unexpected end of data
        u = v
#int.from_bytes(bytes, byteorder, *, signed=False) #big|little
def uint5bytes_LE(bs, /):
    u = int.from_bytes(bs, 'little')
    return u

def read_at_0x2e0b88_0x3c15b8_现代汉语词典():
    ipath = _G.现代汉语词典
    begin,end = 0x2e0b88,0x3c15b8
    bs = ipath.read_bytes()
    L = 16
    W = 4
    bss = cut_seq_(L, bs, begin,end)
    ls = []
    for _bs in bss:
        _bss = cut_seq_(W, _bs)
        w4 = [*map(uint5bytes_LE, _bss)]
        a,b,c,d = w4
        assert c==0
        offset = a
        xxx = b
        _0 = c
        sz = d
        ls.append((offset,xxx,sz))
    xs = sorted(ls, key=snd)
    for A,B in pairwise(xs):
        (_,xxx,sz),(_,yyy,_) = A,B
        assert xxx+sz==yyy, (A,B)
    (_,xxx,sz) = xs[0]
    XXX = xxx
    (_,xxx,sz) = xs[-1]
    ZZZ = xxx+sz
    if 0:
        print(f'XXX==0x{XXX:X}=={XXX}')
        print(f'ZZZ==0x{ZZZ:X}=={ZZZ}')
    assert XXX==0x0==0
    assert ZZZ==0x60C6CE==6342350


def read_at_0x41c23e_现代汉语词典():
    (0x41cd36-0x41c23e)//4==702
    ipath = _G.现代汉语词典
    begin,end = (0x41c23e,0x41cd36)
    bs = ipath.read_bytes()
    W = 4
    assert len(bs)==end
    ws = cut_seq_(W, bs, begin)
    assert len(ws) == 702
    assert all(w==b'\2\0\0\0' for w in ws)


#from seed.helper.mk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples#, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk
#    bmk_triples          # bmk_triples[1:2:3, ::]
def _apply_decoder(idx, decoder, bs, /):
    try:
        return apply_decoder(decoder, bs)
    except Exception as e:
        raise Exception(idx) from e

bufsize4zlib_decompress = 0x4000
def _mk包数组囗整合囗全字节串__errors_replace(压缩包数组, /):
    return _mk包数组囗整合囗全字节串(压缩包数组, errors_replace=True)
def _mk包数组囗整合囗全字节串(压缩包数组, /, *, errors_replace=False):
    ps = []
    es = []
    msgs = set()
    for idx, 压缩包字节串 in enumerate(压缩包数组):
        try:
            原片段字节串 = apply_decoder(zlib_decoder, 压缩包字节串)
        except Exception as e:
            es.append((idx,压缩包字节串))
            msgs.add(repr(e))
        else:
            ps.append((idx,原片段字节串))
    if not es:
        整原字节串 = b''.join(map(snd, ps))
        return 整原字节串

    me = 'script.欧路词典囗:_mk包数组囗整合囗全字节串'
    for idx, 原片段字节串 in ps:
        if not (len(原片段字节串) == bufsize4zlib_decompress or idx == -1+len(压缩包数组)):
            print_err(f'{me}:not (len(原片段字节串) == bufsize4zlib_decompress or idx == -1+len(压缩包数组)):{idx!r}')


    err_idc = [*map(fst, es)]
    print_err(f'{me}:err_idc:{err_idc!r}')

    may_more_es_ps = 囗尝试恢复囗囗头部错位囗(压缩包数组, err_idc)
    if not may_more_es_ps is None:
        more_es, more_ps = may_more_es_ps
        for idx, 原片段字节串 in more_ps:
            if not (len(原片段字节串) == bufsize4zlib_decompress or idx == -1+len(压缩包数组)):
                print_err(f'{me}:not (len(原片段字节串) == bufsize4zlib_decompress or idx == -1+len(压缩包数组)):{idx!r}')
        if not more_es:
            ps_ex = [*ps, *more_ps]
            ps_ex.sort()
            assert [*map(fst, ps_ex)] == [*range(len(压缩包数组))]
            整原字节串 = b''.join(map(snd, ps_ex))
            return 整原字节串

        more_err_idc = [*map(fst, more_es)]
        print_err(f'{me}:more_err_idc:{more_err_idc!r}')

    try:
        raise 囗出错囗写出囗(压缩包数组, msgs, es, err_idc)
    except:
        if not errors_replace:
            raise
    assert errors_replace
    if errors_replace:
        伪原片段字节串 = b'#'*bufsize4zlib_decompress
        bss = [伪原片段字节串]*len(压缩包数组)
        for idx, 原片段字节串 in ps:
            bss[idx] = 原片段字节串
        整原字节串 = b''.join(bss)
        return 整原字节串
    raise 000

header4zlib = b'\x78\x9c'
def 囗尝试恢复囗囗头部错位囗(压缩包数组, err_idc, /):
    #尝试恢复:头部错位
    if err_idc[0] == 0:
        return #fail

    def has_good_header(idx, /):
        return 压缩包数组[idx].startswith(header4zlib)

    idc_blocks = []
    prev = -2
    for idx in err_idc:
        if not idx == 1+prev:
            idc_blocks.append([])
        idc_blocks[-1].append(idx)
        prev = idx
    if any(len(idc)==1 for idc in idc_blocks):
        return #fail

    if 0:
        #bug!
        #   num mismatch largely
        idc_blocks_ = []
        for idc in idc_blocks:
            if not has_good_header(idc[0]):
                return #fail
            if has_good_header(idc[-1]):
                return #fail
            for idx in idc:
                if has_good_header(idx):
                    idc_blocks_.append([])
                idc_blocks_[-1].append(idx)
        idc_blocks = idc_blocks_
        if any(len(idc)==1 for idc in idc_blocks):
            return #fail

    ps4err = []
        #vs ps:
        #compressed
        #without header4zlib!!
    for idc in idc_blocks:
        bs = b''.join(压缩包数组[idx] for idx in idc)
        bss = bs.split(header4zlib)
        assert bss[0] == b''
        del bss[0]
        if not len(bss)==len(idc):
            print_err('囗尝试恢复囗囗头部错位囗:not len(bss)==len(idc)')
            return #fail
        ps4err.extend(zip(idc, bss))
    ps = []
    es = []
    for idx, bs in ps4err:
        压缩包字节串 = header4zlib+bs
        try:
            原片段字节串 = apply_decoder(zlib_decoder, 压缩包字节串)
        except Exception as e:
            es.append((-idx,压缩包字节串))
            print_err(f'{idx}:{e!r}')
            #raise Exception(idc_blocks)
            #return #fail
        else:
            ps.append((idx,原片段字节串))
    return es, ps
#end-def 囗尝试恢复囗囗头部错位囗(压缩包数组, err_idc, /):


def 囗出错囗写出囗(压缩包数组, msgs, es, err_idc, /):
    folder4err_idc = _G.folder4err_idc
    msgs = sorted(msgs)
    me = 'script.欧路词典囗:囗出错囗写出囗'
    print_err(f'{me}:{folder4err_idc!r}')
    print_err(f'{me}:{msgs!r}')

    opath4err_idc = folder4err_idc/'err_idc.txt'
    with open(opath4err_idc, 'wt', encoding='u8') as fout:
        print(err_idc, file=fout)

    err_idc_ex = [j for idx in err_idc for j in range(idx-1, idx+2)]
    err_idc_ex = sorted({*err_idc_ex})
    print_err(f'{me}:{err_idc!r} --> {err_idc_ex!r}')
    #for idx, 压缩包字节串囗含错 in es:
    for idx in err_idc_ex:
        压缩包字节串囗含错 = 压缩包数组[idx]
        opath4err_idx = folder4err_idc/f'err_idx-{idx}.dat'
        print_err(f'{me}:{idx}:{opath4err_idx!r}')
        opath4err_idx.write_bytes(压缩包字节串囗含错)
        if 0:
            with open(opath4err_idx, 'wb') as obfile:
                obfile.write(压缩包字节串囗含错)
    raise Exception(folder4err_idc, len(压缩包数组), len(err_idc), err_idc, msgs)

def _load_err_compressed_bs(err_idx, /):
    folder4err_idc = _G.folder4err_idc
    ipath4err_idx = folder4err_idc/f'err_idx-{err_idx}.dat'
    bs = 压缩包字节串囗含错 = ipath4err_idx.read_bytes()
    return bs
def _try_fix_at__(i, bs, /):
    bs = bytearray(bs)
    ok_bytes = []
    for b in range(0x100):
        bs[i] = b
        is_ok, err_msg_or_original_bs = try_zlib_decompress(bs)
        if is_ok:
            ok_bytes.append(b)
        else:
            err_msg = err_msg_or_original_bs
            #print(f'bad_byte={b}:{err_msg!r}')
            if 'Error -5' in err_msg:
                ...
    print(f'ok_bytes={ok_bytes}')
        #[]
    return

def 囗尝试恢复囗新世纪汉英科技大词典囗压缩包囗369():
    bs_369 = _load_err_compressed_bs(369)
    if 0:
        #fail
        _try_fix_at__(2337, bs_369)
        return
    if 0:
        #print(len(bs_369))
        #print(try_zlib_decompress_on_shorter_size_to_alter_exc_msg___bisearch(bs_369))
        assert 5335 == len(bs_369)
        assert 2337 == try_zlib_decompress_on_shorter_size_to_alter_exc_msg___bisearch(bs_369)
        return
def 囗尝试恢复囗汉语大辞典囗压缩包囗5176():
    #假设长度无错，试试缩短后，异常信息的改变
    idx = 5176
    bs = _load_err_compressed_bs(5176)

    if 0:
        assert 6855 == try_zlib_decompress_on_shorter_size_to_alter_exc_msg___bisearch(bs)
        return
    if 0:
        for i, err_msg in try_zlib_decompress_on_shorter_size_to_alter_exc_msg(bs):
            print((i, err_msg))
            #(7831, 'Error -3 while decompressing data: invalid distance too far back')
            #(6855, 'Error -5 while decompressing data: incomplete or truncated stream')
            #可能是bs[6855]出错
    if 0:
        #fail
        _try_fix_at__(6855, bs)
            #[]
    return
    #fail:
    r'''[[[
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧 路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5175.dat' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
0=0x0
6715=0x1A3B
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5176.dat' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
0=0x0
py -m nn_ns.app.search_bytes_in_file -i '/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5177.dat' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
971=0x3CB
du -b /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5176.dat
7831
du -b /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗/err_idx-5177.dat
7908

    #]]]'''



    folder4err_idc = _G.folder4err_idc
    idx_ = 5175
    idx = 5176
    _idx = 5177

    ipath4err_idx_ = folder4err_idc/f'err_idx-{idx_}.dat'
    ipath4err_idx = folder4err_idc/f'err_idx-{idx}.dat'
    _ipath4err_idx = folder4err_idc/f'err_idx-{_idx}.dat'

    bs = 压缩包字节串囗含错 = ipath4err_idx.read_bytes()
    _bs = _压缩包字节串囗含错 = _ipath4err_idx.read_bytes()
    if 0:
        bs_ = 压缩包字节串囗含错 = ipath4err_idx_.read_bytes()
        j = bs_.index(header4zlib, 1)
        assert j == 6715==0x1A3B
        decompress(bs_)
        decompress(bs_+bs) #longer is ok
        decompress(bs_[:-1])
            #zlib.error: Error -5 while decompressing data: incomplete or truncated stream
    assert len(bs) == 7831
    assert len(_bs) == 7908

    bs_bs = bs+_bs
    imay = imay_try_zlib_decompress_(bs_bs)
    return imay

def 囗尝试恢复囗汉语大辞典囗压缩包囗5177():
    folder4err_idc = _G.folder4err_idc
    idx = 5177
    ipath4err_idx = folder4err_idc/f'err_idx-{idx}.dat'
    bs = 压缩包字节串囗含错 = ipath4err_idx.read_bytes()
    offset = bs.index(header4zlib)
    assert offset == 971 == 0x3CB
    _bs = bs[offset:]
    #zlib
    imay = imay_try_zlib_decompress_(_bs)
    if imay >= 0:
        return imay
    _bs_ = bs[offset:]+bs[:offset]
    imay = imay_try_zlib_decompress_(_bs_)
    return imay
def imay_try_zlib_decompress_(_bs, /):
    assert _bs.startswith(header4zlib)
    for i in reversed(range(len(_bs)+1)):
        try:
            原片段字节串 = decompress(_bs[:i])
        except:
            return -1 #longer is ok!!
            continue
        else:
            return i
    else:
        return -1

def try_zlib_decompress_on_shorter_size_to_alter_exc_msg___bisearch(bs, /):
    #see:囗尝试恢复囗汉语大辞典囗压缩包囗5176()
        #(7831, 'Error -3 while decompressing data: invalid distance too far back')
        #(6855, 'Error -5 while decompressing data: incomplete or truncated stream')
    #array = [-5,...,-5,-3,...,-3]
    def f(sz, /):
        is_ok, err_msg_or_original_bs = try_zlib_decompress(bs[:sz])
        if is_ok:
            raise Exception(f'found ok: {sz}')
        else:
            err_msg = err_msg_or_original_bs
            #print(f'{err_msg!r}')
            _, neg, _ = err_msg.split(None,2)
            return int(neg)
    L = len(bs)
    (i,j) = bisearch(-4, range(L+1), key=f)
    assert i==j, (i,j)
    assert f(i)==-3
    assert f(i-1)==-5
    return i-1
def try_zlib_decompress(bs, /):
    assert bs.startswith(header4zlib)
    try:
        original_bs = decompress(bs)
    except zlib.error as e:
        err_msg = str(e)
        #[err_msg] = e.args
        return (False, err_msg)
    return (True, original_bs)

def try_zlib_decompress_on_shorter_size_to_alter_exc_msg(bs, /):
    assert bs.startswith(header4zlib)
    sz__err_msg___pairs = [(-1, '')]
    for i in reversed(range(len(bs)+1)):
        try:
            原片段字节串 = decompress(bs[:i])
        except zlib.error as e:
            err_msg = str(e)
            if not err_msg == sz__err_msg___pairs[-1][1]:
                sz__err_msg___pairs.append((i,err_msg))
            continue
        else:
            return i
    else:
        del sz__err_msg___pairs[0]
        return sz__err_msg___pairs


def 定位关键位置全过程囗自动化囗(*, ipath, to_show=True):
    #export as cmd ==>> `ipath` be kwd
    ipath = explain_ipath_(ipath)
    #文件字节数 = get_file_size(ipath)
    with open(ipath, 'rb') as ibfile:
        r = 囗定位关键位置全过程囗自动化囗(ibfile)
    if to_show:
        ((压缩包地址数组囗起始地址,词汇各词字节偏移量囗起始地址,词汇各词字节偏移量囗结束地址), (压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量), ex, ps) = r
        print('='*22)
        for nm, v in ps:
            print(f'{nm}=0x{v:X}={v}')
        print('='*22)
    return r
#__all__
def 囗定位关键位置全过程囗自动化囗(ibfile, /):
    r'''-> ((压缩包地址数组囗起始地址,词汇各词字节偏移量囗起始地址,词汇各词字节偏移量囗结束地址), (压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量), ex, ps)

[算法:定位关键位置全过程囗自动化囗
定位关键位置全过程-自动化
def _mk_reader5many_addr(压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, ...)
其中
    压缩包数量囗地址=压缩包地址数组囗起始地址-4
    压缩包数组囗结束地址=词汇各词字节偏移量囗起始地址
    词汇量=(词汇各词字节偏移量囗结束地址-词汇各词字节偏移量囗起始地址)//16

重点在于:(压缩包地址数组囗起始地址,词汇各词字节偏移量囗起始地址,词汇各词字节偏移量囗结束地址)
    * 压缩包地址数组囗起始地址:
        首个压缩包地址=uint32LE@0x6
            #addr 但 只用 size_t
            确认header4zlib
        搜索下一个『首个压缩包地址』，并确认『第二个压缩包地址』的header4zlib
            压缩包数量囗地址=压缩包地址数组囗起始地址-4
            压缩包数量=uint32LE@压缩包数量囗地址
            压缩包地址数组囗结束地址=压缩包地址数组囗起始地址+8*压缩包数量
            确认:压缩包地址数组囗结束地址+1==首个压缩包地址
            确认:byte@压缩包地址数组囗结束地址==b'\1'
        由此 定位(小概率有误)压缩包地址数组囗起始地址=该含有『首个压缩包地址』的地址

    * 词汇各词字节偏移量囗起始地址:
        末尾压缩包地址=uint64LE@[压缩包地址数组囗结束地址-8]
        从『末尾压缩包地址』开始搜起
            搜索 『00 00 00 00』，并确认 +16后，偏移量 连续递增, 词义地址 高位为0
        由此 定位(小概率有误)词汇各词字节偏移量囗起始地址=该4个零字节 起始地址

    * 词汇各词字节偏移量囗结束地址:
        词汇结束地址=文件字节数-2808
        从『词汇各词字节偏移量囗起始地址』开始搜起
            每个16字节 匹配前8字节『?? ?? ?? ?? 00 00 00 00』，并确认 该8字节之后[&&词汇结束地址之前]是u8编码
        由此 定位(小概率有误)词汇各词字节偏移量囗结束地址=该16字节 起始地址
]
    '''#'''
    assert ibfile.tell()==0
    num_bytes4addr = 8
    num_bytes4size = 4

    _5hex = bytes.fromhex
    addr_ = uint64LE_reader
    sz_ = uint32LE_reader
    bs4sz_ = BytesReader(4) #for 『未知』
    reader4header = (NamedDependentTupleReader(
        [('', mk_ConstantBytesMatcher(_5hex('56 11')), None)
        ,('#未知', bs4sz_, None)
        ,('首个压缩包地址', sz_, None) #虽是 地址，却是uint32
        #fail: ,('', mk_ConstantBytesMatcher(_5hex('02 00 00 00 34 0c 03 00 00 00')), None)
        ,('end4header', tell_addr_reader, None)
        ,('eof', eof_addr_reader, None)
        ]
        #, to_read_ex=True
        ))
    #_checker4header4zlib = mk_ConstantBytesMatcher(header4zlib)
    #_reader4header4zlib = BytesReader(len(header4zlib))
    #
    #Reader raise Exception...
    #using func to return bool
    #   try...except??
    def is_header4zlib_(ibfile, /):
        return header4zlib == ibfile.read(len(header4zlib))
    def is_header4zlib_at_(ibfile, addr, /):
        with with4seekback__on_no_err(ibfile):
            #xxx checked_seek
            ibfile.seek(addr)
            return is_header4zlib_(ibfile)
    def is_header4zlib_at_at_(ibfile, addr4addr, /):
        #xxx checked_seek
        addr = read_addr_at_(ibfile, addr4addr)
        return is_header4zlib_at_(ibfile, addr)
    def read_addr_at_(ibfile, addr4addr, /):
        addr = read_uintLE_at_(ibfile, addr4addr, num_bytes4addr)
        return addr
    def read_size_at_(ibfile, addr4size, /):
        size = read_uintLE_at_(ibfile, addr4size, num_bytes4size)
        return size
    def read_uintLE_at_(ibfile, addr4addr, sz, /):
        bs = read_bytes_at__le_(ibfile, addr4addr, sz)
        u = int.from_bytes(bs, 'little')
        return u
    def read_bytes_at__le_(ibfile, addr4addr, sz, /):
        with with4seekback__on_no_err(ibfile):
            #xxx checked_seek
            ibfile.seek(addr4addr)
            bs = ibfile.read(sz)
        return bs

    def main1():
        #tpl, _result4ex = apply_reader(reader4header, ibfile)

        tpl = apply_reader(reader4header, ibfile)
        ns = tpl.as_getter4named_tuple()
        首个压缩包地址 = ns.首个压缩包地址
        文件字节数 = ns.eof
        ######################
        ######################
        bs = 首个压缩包地址.to_bytes(num_bytes4addr, 'little')
            #addr be 8Byte
        assert len(bs) == num_bytes4addr
        it = iter_find_bytes__naive_(bs, ibfile)
        for addr4addr in it:
            #print(hex(addr4addr))
            if is_header4zlib_at_at_(ibfile, addr4addr) and is_header4zlib_at_at_(ibfile, addr4addr+num_bytes4addr):
                压缩包地址数组囗起始地址 = addr4addr
                压缩包数量囗地址 = 压缩包地址数组囗起始地址-num_bytes4size
                #print(read_bytes_at__le_(ibfile, 压缩包数量囗地址, 4))
                压缩包数量 = read_size_at_(ibfile, 压缩包数量囗地址)
                压缩包地址数组囗结束地址 = 压缩包地址数组囗起始地址+num_bytes4addr*压缩包数量
                #print(hex(压缩包地址数组囗起始地址))
                #print(hex(压缩包数量囗地址))
                #print(压缩包数量)
                #print(hex(压缩包地址数组囗结束地址), hex(首个压缩包地址))
                #print(read_bytes_at__le_(ibfile,压缩包地址数组囗结束地址,1))
                if 压缩包地址数组囗结束地址+1==首个压缩包地址 and read_bytes_at__le_(ibfile,压缩包地址数组囗结束地址,1)==b'\1':
                    break
        else:
            raise Exception('no found:压缩包地址数组囗起始地址')
        压缩包地址数组囗起始地址 = addr4addr

        ######################
        ######################
        首个压缩包地址
        文件字节数
        压缩包数量囗地址
        压缩包数量
        压缩包地址数组囗结束地址
        压缩包地址数组囗起始地址

        末尾压缩包地址 = read_addr_at_(ibfile, 压缩包地址数组囗结束地址-num_bytes4addr)
        #if 末尾压缩包地址 > 文件字节数
        ibfile.seek(末尾压缩包地址)
        if not is_header4zlib_(ibfile):
            raise Exception('no found:压缩包地址数组囗起始地址 -->! 末尾压缩包地址')
        #从『末尾压缩包地址』开始搜起
        it = iter_find_bytes__naive_(b'\0'*num_bytes4size, ibfile)
        L = num_bytes4size+num_bytes4addr+num_bytes4size
            #(词条 于 词汇囗字节串 中的 偏移量/size/递增, 词义 于 包全文囗字节串 中的 地址/addr/无序, 词义囗字节数/size)
        N = 10
        for addr in it:
            offsets = [read_size_at_(ibfile, addr+i*L) for i in range(N)]
            zeros = [read_size_at_(ibfile, addr+2*num_bytes4size+i*L) for i in range(N)]
                #假设 地址高位 为 0
            if not any(zeros) and offsets == sorted(offsets):
                break
        else:
            raise Exception('no found:词汇各词字节偏移量囗起始地址')
        num_bytes4fst_word = offsets[1]
        词汇各词字节偏移量囗起始地址 = 压缩包数组囗结束地址 = addr

        ######################
        ######################
        首个压缩包地址
        文件字节数
        压缩包数量囗地址
        压缩包数量
        压缩包地址数组囗结束地址
        压缩包地址数组囗起始地址
        末尾压缩包地址
        压缩包数组囗结束地址
        词汇各词字节偏移量囗起始地址

        ibfile.seek(词汇各词字节偏移量囗起始地址)
        #从『词汇各词字节偏移量囗起始地址』开始搜起
        词汇结束地址=文件字节数-2808
        _z4 = b'\0'*num_bytes4size
        num_bytes4fst_word
        while 1:
            addr = ibfile.tell()

            bs = ibfile.read(L)
            z4 = bs[num_bytes4size:num_bytes4size*2]

            if not len(z4) == num_bytes4size:
                #eof
                raise Exception('no found:词汇各词字节偏移量囗结束地址')
            if z4 == _z4:
                词汇起始地址 = addr+2*num_bytes4size
                词汇字节数 = read_size_at_(ibfile, addr)
                if not 词汇结束地址 == 词汇起始地址+词汇字节数:
                    #not found
                    continue
                bs = read_bytes_at__le_(ibfile, 词汇起始地址, num_bytes4fst_word)
                try:
                    bs.decode('u8')
                except UnicodeDecodeError:
                    #not found
                    continue
                else:
                    ##found!
                    break
        词汇各词字节偏移量囗结束地址 = addr
        词汇起始地址
        词汇结束地址
        词汇字节数
        词汇量 = (词汇各词字节偏移量囗结束地址-词汇各词字节偏移量囗起始地址)//L
        assert 词汇各词字节偏移量囗结束地址 == 词汇各词字节偏移量囗起始地址 + 词汇量*L
        ######################
        ######################
        首个压缩包地址
        文件字节数
        压缩包数量囗地址
        压缩包数量
        压缩包地址数组囗结束地址
        压缩包地址数组囗起始地址
        末尾压缩包地址
        压缩包数组囗结束地址
        词汇各词字节偏移量囗起始地址
        词汇各词字节偏移量囗结束地址
        词汇量
        词汇字节数
        词汇起始地址
        词汇结束地址
        ######################
        ######################
        #:.,.+13s/\S\+/,('\0', \0)/
        ps = [0
        ,('压缩包数量囗地址', 压缩包数量囗地址)
        ,('压缩包数量', 压缩包数量)
        ,('压缩包地址数组囗起始地址', 压缩包地址数组囗起始地址)
        ,('压缩包地址数组囗结束地址', 压缩包地址数组囗结束地址)
        ,('首个压缩包地址', 首个压缩包地址)
        ,('末尾压缩包地址', 末尾压缩包地址)
        ,('压缩包数组囗结束地址', 压缩包数组囗结束地址)
        ,('词汇各词字节偏移量囗起始地址', 词汇各词字节偏移量囗起始地址)
        ,('词汇各词字节偏移量囗结束地址', 词汇各词字节偏移量囗结束地址)
        ,('词汇量', 词汇量)
        ,('词汇字节数', 词汇字节数)
        ,('词汇起始地址', 词汇起始地址)
        ,('词汇结束地址', 词汇结束地址)
        ,('文件字节数', 文件字节数)
        ]
        del ps[0]
        ######################
        ######################
        ex = (
        (压缩包数量囗地址
            ,压缩包数量
        ,压缩包地址数组囗起始地址
        ,压缩包地址数组囗结束地址
            # b'\1'
        )
        ,
        (首个压缩包地址
        ,末尾压缩包地址
        ,压缩包数组囗结束地址
        )
        ,
        (词汇各词字节偏移量囗起始地址
        ,词汇各词字节偏移量囗结束地址
            ,词汇量
            ,词汇字节数
            # b'\0'*4
        )
        ,
        (词汇起始地址
        ,词汇结束地址
        )
        ,文件字节数
        )

        return ((压缩包地址数组囗起始地址,词汇各词字节偏移量囗起始地址,词汇各词字节偏移量囗结束地址), (压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量), ex, ps)
    return main1()


def _mk_reader5many_addr(压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, /, *, 开启囗词汇, 开启囗词汇囗依词义序, 开启囗词义, errors_replace):
    #see:_mk_reader5addr4introduction
    (开启囗词汇, 开启囗词汇囗依词义序, 开启囗词义, errors, _mk包数组囗整合囗全字节串_, _5hex, addr_, sz_, bs4sz_) = _prepare4mk_reader(开启囗词汇, 开启囗词汇囗依词义序, 开启囗词义, errors_replace)

    词汇各词字节偏移量囗起始地址 = 压缩包数组囗结束地址
    reader4known = (NamedDependentTupleReader(
        [('', mk_ConstantBytesMatcher(_5hex('56 11')), None)
        ,('#未知', bs4sz_, None)
        ,('首个压缩包地址', sz_, None) #虽是 地址，却是uint32
        #fail: ,('', mk_ConstantBytesMatcher(_5hex('02 00 00 00 34 0c 03 00 00 00')), None)
        ,('end4header', tell_addr_reader, None)
        ,('#大段未知', SeekAddrReader(压缩包数量囗地址, to_read_bytes=True), None)
            ,('', mk_AddrAssertionReader(压缩包数量囗地址), None)
        ,('压缩包数量囗地址', tell_addr_reader, None)
        #,('词汇各词字节偏移量囗起始地址', addr_, None)
        #,('词汇起始地址', addr_, None)
        #,('词汇字节数', sz_, None)
        #,('词汇量', sz_, None)
        #    ,('', AssertionReader(16,sz_), None)
        #,('词汇结束地址', addr_, None)
        #    ,('', mk_ConstantBytesMatcher(b'\0'*21), None)
        ,('词汇各词字节偏移量囗起始地址', mk_ConstantTargetReader(压缩包数组囗结束地址), None)
        ,('压缩包数组囗结束地址', mk_ConstantTargetReader, ['词汇各词字节偏移量囗起始地址']) #别名#假设相等
        ,('词汇量', mk_ConstantTargetReader(词汇量), None)
            ,('词汇各词字节偏移量囗结束地址', lambda 词汇各词字节偏移量囗起始地址,词汇量,/:mk_ConstantTargetReader(词汇各词字节偏移量囗起始地址+16*词汇量), ['词汇各词字节偏移量囗起始地址','词汇量'])
            ,('词汇起始地址', lambda 词汇各词字节偏移量囗结束地址,/:mk_ConstantTargetReader(词汇各词字节偏移量囗结束地址+4+4), ['词汇各词字节偏移量囗结束地址'])
            ,('', mk_AddrAssertionReader(压缩包数量囗地址), None)
            ,('', SeekAddrReader, ['词汇各词字节偏移量囗结束地址'])
                #for 词汇结束地址 & check b'\0'*4
            ,('词汇字节数', sz_, None)
                ,('词汇结束地址', lambda 词汇起始地址,词汇字节数,/:mk_ConstantTargetReader(词汇起始地址+词汇字节数), ['词汇起始地址','词汇字节数'])
            ,('', AssertionReader(0,sz_), None)
            ,('', mk_AddrAssertionReader, ['词汇起始地址'])
            ,('', SeekAddrReader, ['压缩包数量囗地址'])
        ######################
        ######################
        ,('', mk_AddrAssertionReader(压缩包数量囗地址), None)
        ,('压缩包数量', sz_, None)
        ,('压缩包地址字节数数组', (lambda 压缩包数量, 压缩包数组囗结束地址, /:AddrSizedParamArrayReader(压缩包数量, 压缩包数组囗结束地址, addr_, None)), ['压缩包数量', '压缩包数组囗结束地址']) #<<==压缩包地址数组+压缩包数组囗结束地址
        if 开启囗词义 else ('#跳过-压缩包地址字节数数组', (lambda 压缩包数量, /:SkipReader(ArrayReader(压缩包数量, addr_))), ['压缩包数量'])
            ,('', mk_ConstantBytesMatcher(b'\1'), None)
            ,('', mk_AddrAssertionReader, ['首个压缩包地址'])
        ,('压缩包数组', (lambda 压缩包地址字节数数组, /:ArrayTranformReader(压缩包地址字节数数组, dot[BytesReader, snd])), ['压缩包地址字节数数组'])
        if 开启囗词义 else ('#跳过-压缩包数组', dot[SkipReader, SeekAddrReader], ['压缩包数组囗结束地址'])
            ,('', mk_AddrAssertionReader, ['压缩包数组囗结束地址'])
        ,('包数组囗整合囗全字节串', dot[mk_ConstantTargetReader, _mk包数组囗整合囗全字节串_], ['压缩包数组'])
        if 开启囗词义 else ('#跳过-包数组囗整合囗全字节串', mk_ConstantTargetReader(None), None)
        ,('包数组囗整合囗全文', (lambda 包数组囗整合囗全字节串, /:mk_ConstantTargetReader(包数组囗整合囗全字节串.decode('u8', errors=errors))), ['包数组囗整合囗全字节串'])
        if 开启囗词义 else ('#跳过-包数组囗整合囗全文', mk_ConstantTargetReader(None), None)
            ,('', mk_AddrAssertionReader, ['压缩包数组囗结束地址'])
            #
            ,('', mk_AddrAssertionReader, ['词汇各词字节偏移量囗起始地址'])
        ,('词汇各词字节偏移量囗差分表', (lambda 词汇量, /:AddrSizedParamArrayReader(词汇量+1, None, sz_, NamedTupleReader([('词义字节串囗解包后的偏移量', addr_), ('词义字节串囗长度', sz_)]))), ['词汇量'])
        if 开启囗词汇 else ('#跳过-词汇各词字节偏移量囗差分表', (lambda 词汇量, /:SkipReader(ArrayReader(词汇量, TupleReader(sz_,addr_,sz_)))), ['词汇量'])
        #,('词汇字节数囗再次出现', sz_, None)
        ,('#词汇字节数囗再次出现', lambda 词汇字节数:AssertionReader(词汇字节数,sz_), ['词汇字节数'])
            ,('', AssertionReader(0,sz_), None)
            ,('', mk_AddrAssertionReader, ['词汇起始地址'])
        #,('词汇囗字节串', BytesReader, ['词汇字节数'])
        ,('词汇', (lambda 词汇各词字节偏移量囗差分表, /:ArrayTranformReader(词汇各词字节偏移量囗差分表, (lambda offset__sz_x,/:BytesReader(offset__sz_x[1][0], u8_decoder)))), ['词汇各词字节偏移量囗差分表'])
        if 开启囗词汇 else ('#跳过-词汇', dot[SkipReader, SeekAddrReader], ['词汇结束地址'])
            ,('', mk_AddrAssertionReader, ['词汇结束地址'])
        ,('词汇囗依词义序囗附词义字节串信息', (lambda 词汇各词字节偏移量囗差分表, 词汇, /:mk_ConstantTargetReader(sorted((词义字节串囗解包后的偏移量,词义字节串囗长度,词条) for 词条,(offset, (sz, (词义字节串囗解包后的偏移量,词义字节串囗长度))) in zip(词汇,词汇各词字节偏移量囗差分表)))), ['词汇各词字节偏移量囗差分表', '词汇'])
        if 开启囗词汇囗依词义序 else ('#跳过-词汇囗依词义序囗附词义字节串信息', mk_ConstantTargetReader(None), None)
            ,('', mk_AddrAssertionReader, ['词汇结束地址'])
                ,('#未知#定长2808==(26+26*26)*4#已验证:英文二十六字母二级前缀分层', BytesReader(2808), None)
            ,('文件字节数', eof_addr_reader, None)
            ,('', mk_AddrAssertionReader, ['文件字节数'])
        ,('词义数组', (lambda 包数组囗整合囗全字节串, 词汇各词字节偏移量囗差分表, /:mk_ConstantTargetReader([包数组囗整合囗全字节串[词义字节串囗解包后的偏移量:词义字节串囗解包后的偏移量+词义字节串囗长度].decode('u8', errors=errors) for 词条字节串囗偏移量, (词条字节串囗字节数,(词义字节串囗解包后的偏移量,词义字节串囗长度)) in 词汇各词字节偏移量囗差分表])), ['包数组囗整合囗全字节串', '词汇各词字节偏移量囗差分表'])
        if 开启囗词汇 and 开启囗词义 else ('#跳过-词义数组', mk_ConstantTargetReader(None), None)
            ,('', mk_AddrAssertionReader, ['文件字节数'])
        ], to_read_ex=True))
    return reader4known

def _prepare4mk_reader(开启囗词汇, 开启囗词汇囗依词义序, 开启囗词义, errors_replace, /):
    check_type_is(bool, 开启囗词汇)
    check_type_is(bool, 开启囗词汇囗依词义序)
    check_type_is(bool, 开启囗词义)
    check_type_is(bool, errors_replace)
    if 开启囗词汇囗依词义序:
        开启囗词汇 = True

    _mk包数组囗整合囗全字节串_ = _mk包数组囗整合囗全字节串__errors_replace if errors_replace else _mk包数组囗整合囗全字节串

    errors = 'replace' if errors_replace else 'strict'

    _5hex = bytes.fromhex
    addr_ = uint64LE_reader
    sz_ = uint32LE_reader
    bs4sz_ = BytesReader(4) #for 『未知』
    return (开启囗词汇, 开启囗词汇囗依词义序, 开启囗词义, errors, _mk包数组囗整合囗全字节串_, _5hex, addr_, sz_, bs4sz_)
def _mk_reader5addr4introduction(简介字节数囗地址, /, *, 开启囗词汇, 开启囗词汇囗依词义序, 开启囗词义, errors_replace):
    #see:_mk_reader5many_addr
    (开启囗词汇, 开启囗词汇囗依词义序, 开启囗词义, errors, _mk包数组囗整合囗全字节串_, _5hex, addr_, sz_, bs4sz_) = _prepare4mk_reader(开启囗词汇, 开启囗词汇囗依词义序, 开启囗词义, errors_replace)
    reader4known = (NamedDependentTupleReader(
    #reader4header = (NamedDependentTupleReader(
    #    补偿:))
        [('', mk_ConstantBytesMatcher(_5hex('56 11')), None)
        ,('#未知', bs4sz_, None)
        ,('首个压缩包地址', sz_, None) #虽是 地址，却是uint32
        ,('', mk_ConstantBytesMatcher(_5hex('02 00 00 00 34 0c 03 00 00 00')), None)
        ,('end4header', tell_addr_reader, None)
    #    补偿:((
    #    ))

        #,('#大段未知', SeekAddrReader(简介字节数囗地址), None)
        ,('#大段未知', SeekAddrReader(简介字节数囗地址, to_read_bytes=True), None)
            ,('', mk_AddrAssertionReader(简介字节数囗地址), None)
        ,('简介字节数囗地址', tell_addr_reader, None)
    #reader_from_introduction = (NamedDependentTupleReader(
    #    补偿:))
        #简介:introduction,abstract
        ,('简介', BytesReader(sz_,u8_decoder), None) #简介字节数+简介
            ,('#未知', BytesReader(1), None)
            ,('', mk_ConstantBytesMatcher(_5hex('b7 32 01')), None)
            ,('', AssertionReader(0,sz_), None)
            ,('', AssertionReader(0,sz_), None)
            ,('#未知', bs4sz_, None)
        ,('词汇各词字节偏移量囗起始地址', addr_, None)
        ,('词汇起始地址', addr_, None)
        ,('词汇字节数', sz_, None)
        ,('词汇量', sz_, None)
            ,('', AssertionReader(16,sz_), None)
        ,('词汇结束地址', addr_, None)
            ,('#py.zlib.decompress:bufsize', AssertionReader(bufsize4zlib_decompress,sz_), None)
        ,('xml', BytesReader(sz_,u8_decoder), None) #len_xml+xml
            ,('', mk_ConstantBytesMatcher(b'\0'*21), None)
        ,('压缩包数组囗结束地址', mk_ConstantTargetReader, ['词汇各词字节偏移量囗起始地址']) #别名#假设相等
            #??? ,压缩包数组 #很可能 结束于 词汇各词字节偏移量囗起始地址
            #!!! yes，已经过『现代汉语词典』检验
        ,('压缩包数量', sz_, None)
        ,('压缩包地址字节数数组', (lambda 压缩包数量, 压缩包数组囗结束地址, /:AddrSizedParamArrayReader(压缩包数量, 压缩包数组囗结束地址, addr_, None)), ['压缩包数量', '压缩包数组囗结束地址']) #<<==压缩包地址数组+压缩包数组囗结束地址
        if 开启囗词义 else ('#跳过-压缩包地址字节数数组', (lambda 压缩包数量, /:SkipReader(ArrayReader(压缩包数量, addr_))), ['压缩包数量'])
            ,('', mk_ConstantBytesMatcher(b'\1'), None)
            ,('', mk_AddrAssertionReader, ['首个压缩包地址'])
        ,('压缩包数组', (lambda 压缩包地址字节数数组, /:ArrayTranformReader(压缩包地址字节数数组, dot[BytesReader, snd])), ['压缩包地址字节数数组'])
        if 开启囗词义 else ('#跳过-压缩包数组', dot[SkipReader, SeekAddrReader], ['压缩包数组囗结束地址'])
            ,('', mk_AddrAssertionReader, ['压缩包数组囗结束地址'])
        ,('包数组囗整合囗全字节串', dot[mk_ConstantTargetReader, _mk包数组囗整合囗全字节串_], ['压缩包数组'])
            #raise Exception(folder4err_idc, len(压缩包数组), len(err_idc), err_idc, sorted(msgs))
            #   Exception: (PosixPath('/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗'), 9788, 2, [5176, 5177], ['error("decoding with \'zlib\' codec failed (error: Error -3 while decompressing data: incorrect header check)")', 'error("decoding with \'zlib\' codec failed (error: Error -3 while decompressing data: invalid distance too far back)")'])
            #
            #,('包数组囗整合囗全字节串', (lambda 压缩包数组, /:mk_ConstantTargetReader(b''.join(_apply_decoder(i, zlib_decoder, bs) for i, bs in enumerate(压缩包数组)))), ['压缩包数组'])
            #raise zlib.error@汉语大辞典:,('包数组囗整合囗全字节串', (lambda 压缩包数组, /:mk_ConstantTargetReader(b''.join(apply_decoder(zlib_decoder, bs) for bs in 压缩包数组))), ['压缩包数组'])
            #   zlib.error: decoding with 'zlib' codec failed (error: Error -3 while decompressing data: invalid distance too far back)
            #
            #   _apply_decoder::Exception: 5176
            #       '压缩包数量':9788:0x263C
        if 开启囗词义 else ('#跳过-包数组囗整合囗全字节串', mk_ConstantTargetReader(None), None)
        ,('包数组囗整合囗全文', (lambda 包数组囗整合囗全字节串, /:mk_ConstantTargetReader(包数组囗整合囗全字节串.decode('u8', errors=errors))), ['包数组囗整合囗全字节串'])
        if 开启囗词义 else ('#跳过-包数组囗整合囗全文', mk_ConstantTargetReader(None), None)
            ,('', mk_AddrAssertionReader, ['压缩包数组囗结束地址'])
            #
        #... ...
    #    补偿:((
    #    ))
        ##, [],, b'\1', 压缩包数组, (...此处很可能无缝), 词汇各词字节偏移量, [词汇字节数, 0], 词汇, [2]*702 #文件结束
    #AddrDereferenceReader
    #reader_from_word_pool_info_array = (NamedDependentTupleReader(
    #    补偿:))
            ,('', mk_AddrAssertionReader, ['词汇各词字节偏移量囗起始地址'])
        #,('词汇各词字节偏移量囗信息表', ArrayReader(词汇量, NamedTupleReader([('词条字节串囗偏移量', sz_), ('词义字节串囗解包后的偏移量', addr_), ('词义字节串囗长度', sz_)])), None)
        ,('词汇各词字节偏移量囗差分表', (lambda 词汇量, /:AddrSizedParamArrayReader(词汇量+1, None, sz_, NamedTupleReader([('词义字节串囗解包后的偏移量', addr_), ('词义字节串囗长度', sz_)]))), ['词汇量'])
        if 开启囗词汇 else ('#跳过-词汇各词字节偏移量囗差分表', (lambda 词汇量, /:SkipReader(ArrayReader(词汇量, TupleReader(sz_,addr_,sz_)))), ['词汇量'])
        #,('词汇字节数囗再次出现', sz_, None)
        ,('#词汇字节数囗再次出现', lambda 词汇字节数:AssertionReader(词汇字节数,sz_), ['词汇字节数'])
            ,('', AssertionReader(0,sz_), None)
            ,('', mk_AddrAssertionReader, ['词汇起始地址'])
        #,('词汇囗字节串', BytesReader, ['词汇字节数'])
        ,('词汇', (lambda 词汇各词字节偏移量囗差分表, /:ArrayTranformReader(词汇各词字节偏移量囗差分表, (lambda offset__sz_x,/:BytesReader(offset__sz_x[1][0], u8_decoder)))), ['词汇各词字节偏移量囗差分表'])
        if 开启囗词汇 else ('#跳过-词汇', dot[SkipReader, SeekAddrReader], ['词汇结束地址'])
            ,('', mk_AddrAssertionReader, ['词汇结束地址'])
        ,('词汇囗依词义序囗附词义字节串信息', (lambda 词汇各词字节偏移量囗差分表, 词汇, /:mk_ConstantTargetReader(sorted((词义字节串囗解包后的偏移量,词义字节串囗长度,词条) for 词条,(offset, (sz, (词义字节串囗解包后的偏移量,词义字节串囗长度))) in zip(词汇,词汇各词字节偏移量囗差分表)))), ['词汇各词字节偏移量囗差分表', '词汇'])
        if 开启囗词汇囗依词义序 else ('#跳过-词汇囗依词义序囗附词义字节串信息', mk_ConstantTargetReader(None), None)
            ,('', mk_AddrAssertionReader, ['词汇结束地址'])
            #,('', ArrayReader(702, AssertionReader(2,sz_)), None)
                #,('', AssertionReader(2,sz_), None)
                #,('#未知#定长2808-4', BytesReader(2808-4), None)
                ,('#未知#定长2808==(26+26*26)*4#已验证:英文二十六字母二级前缀分层', BytesReader(2808), None)
    #    补偿:((
    #    ))
            ,('文件字节数', eof_addr_reader, None)
            ,('', mk_AddrAssertionReader, ['文件字节数'])
        ,('词义数组', (lambda 包数组囗整合囗全字节串, 词汇各词字节偏移量囗差分表, /:mk_ConstantTargetReader([包数组囗整合囗全字节串[词义字节串囗解包后的偏移量:词义字节串囗解包后的偏移量+词义字节串囗长度].decode('u8', errors=errors) for 词条字节串囗偏移量, (词条字节串囗字节数,(词义字节串囗解包后的偏移量,词义字节串囗长度)) in 词汇各词字节偏移量囗差分表])), ['包数组囗整合囗全字节串', '词汇各词字节偏移量囗差分表'])
        if 开启囗词汇 and 开启囗词义 else ('#跳过-词义数组', mk_ConstantTargetReader(None), None)
            ,('', mk_AddrAssertionReader, ['文件字节数'])
        ], to_read_ex=True))
    #return (reader4header, reader_from_introduction, reader_from_word_pool_info_array)
    return reader4known
#(reader4header, reader_from_introduction, reader_from_word_pool_info_array) = _mk_reader()
assert 2808==(26+26*26)*4

from seed.tiny import check_type_is, fst, print_err
from seed.seq_tools.bisearch import bisearch
from itertools import combinations
from pathlib import Path
assert Path('a') == Path('a')
assert not Path('a') == Path('b')
def 碰撞测试囗囗多个输出文件囗(opath_name_force_triples, /):
    '"w" mode not "a" append mode'
    def may_opath_(may_opath, /):
        if not may_opath:
            may_opath = None
        else:
            opath = may_opath
            opath = Path(opath).expanduser().resolve()
            may_opath = opath
        return may_opath
    opath_name_force_triples = [(may_opath_(may_opath), may_name, force) for (may_opath, may_name, force) in opath_name_force_triples]
    may_opath__ls = [*map(fst, opath_name_force_triples)]

    opath_name_force_triples = [(may_opath, may_name, force) for (may_opath, may_name, force) in opath_name_force_triples if may_opath]
    oks__exist = []
    oks__nonexist = []
    for (opath, may_name, force) in opath_name_force_triples:
        check_type_is(bool, force)
        if opath.exists():
            if not force:raise FileExistsError(f'{may_name!r}:{opath!r}')
            oks__exist.append((opath, may_name))
        else:
            oks__nonexist.append((opath, may_name))
    for (opath0, may_name0), (opath1, may_name1) in combinations(oks__nonexist, 2):
        #if opath0.as_posix() == opath1.as_posix():
        if opath0 == opath1:raise FileExistsError(f'same file:{may_name0!r}:{may_name1!r}:{opath0!r}')
    for (opath0, may_name0), (opath1, may_name1) in combinations(oks__exist, 2):
        #if opath0.as_posix() == opath1.as_posix():
        if opath0.samefile(opath1):raise FileExistsError(f'same file:{may_name0!r}:{may_name1!r}:{opath0!r}')
    return may_opath__ls

def 试读囗囗假设简介字节数地址固定囗(*, ipath, 简介字节数囗地址=0x412, errors_replace=False, 输出文件囗词汇=None, 输出文件囗词汇囗依词义序=None, 输出文件囗全文=None, 输出文件囗词典=None, 输出文件囗杂项=None, oencoding='utf8', force=False):
    kw = {**locals()}
    case = '简介字节数囗地址'
    args = []
    for nm in case.split('十十'):
        args.append(kw.pop(nm))
    return 试读囗囗地址固定囗(case, 简介字节数囗地址, **kw)

def 试读囗囗固定囗囗压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量囗(*, 压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, ipath, errors_replace=False, 输出文件囗词汇=None, 输出文件囗词汇囗依词义序=None, 输出文件囗全文=None, 输出文件囗词典=None, 输出文件囗杂项=None, oencoding='utf8', force=False):
    #see:定位关键位置全过程
    kw = {**locals()}
    case = '压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量'
    args = []
    for nm in case.split('十十'):
        args.append(kw.pop(nm))
    return 试读囗囗地址固定囗(case, 压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, **kw)

def 试读囗囗定位关键位置全过程囗自动化囗(*, ipath, errors_replace=False, 输出文件囗词汇=None, 输出文件囗词汇囗依词义序=None, 输出文件囗全文=None, 输出文件囗词典=None, 输出文件囗杂项=None, oencoding='utf8', force=False):
    #see:定位关键位置全过程
    kw = {**locals()}
    r = 定位关键位置全过程囗自动化囗(ipath=ipath)
    ((压缩包地址数组囗起始地址,词汇各词字节偏移量囗起始地址,词汇各词字节偏移量囗结束地址), (压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量), ex, ps) = r
    case = '压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量'
    return 试读囗囗地址固定囗(case, 压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, **kw)


def explain_ipath_(ipath, /):
    if ipath.isidentifier() and not ipath.startswith('folder') and hasattr(_G,ipath):
        #ipath = _G.现代汉语词典
        nm = ipath
        _ipath = getattr(_G, nm)
        if 0:
            print(Path)
            print(_ipath)
            print(type(_ipath))
                #pathlib.PosixPath
        #fail:if type(_ipath) is Path:
        if type(_ipath) is type(_G.folder):
            ipath = _ipath
    ipath = Path(ipath)
    return ipath

def 试读囗囗地址固定囗(case, /, *args, ipath, errors_replace, 输出文件囗词汇, 输出文件囗词汇囗依词义序, 输出文件囗全文, 输出文件囗词典, 输出文件囗杂项, oencoding, force):
    r'''[[[
    [[
小端序
地址::uint64
长度,常量::uint32
    下面:[...] (比如『[2]、[0,0]』)是 混合uint32/uint64的列表，再编码为 字节串，不是 直接字节串



文件开头: hex'56 11' uint32[?, 首个压缩包地址] hex'02 00 00 00 34 0c 03 00 00 00'
    0x14==20 BYTE=2+4*2+10
固定地址？:简介字节数囗地址==0x412==1042
固定地址？:简介囗起始地址==0x416==1046
..., [简介字节数], 简介/utf8, hex'?? b7 32 01', [0,0,?], [词汇各词字节偏移量囗起始地址/uint64,词汇起始地址/uint64,词汇字节数,词汇量], [16], [词汇结束地址/uint64], [0x4000/uint32], [len_xml], xml/utf8, b'\0'*21, [压缩包数量],压缩包地址数组, b'\1', 压缩包数组, (...此处很可能无缝), 词汇各词字节偏移量, [词汇字节数, 0], 词汇, 英文二十六字母二级前缀分层/[前缀分区的词汇量]*702 #文件结束
    # 2808=702*4
    # bug:[2]*702 只对汉字词典有效
    ===
    @[0x412:0x5d7]=[简介字节数], 简介/utf8
        (0x5e7-0x5d7)==16
    @[0x5e7:0x12be]=[词汇各词字节偏移量囗起始地址]...压缩包地址数组
        (0x12bf-0x12be)==1
    @[0x12bf:0x2e07f1+?]=压缩包数组
        (0x2e0b88-0x2e07f1)=0x397==919
    @[0x2e0b88:]=词汇各词字节偏移量...#文件结束
    ===
词汇各词字节偏移量::[16BYTE as (词条字节串囗偏移量/uint32, 词义字节串囗解包后的偏移量/uint64, 词义字节串囗长度/uint32)]{len=词汇量}
    script.欧路词典囗@read_at_0x2e0b88_0x3c15b8_现代汉语词典
    ==>>已验证:中间的uint64是偏移量(起始点未知)，但 无序。于后面的 释义数据字节数 无缝衔接
        现代汉语词典 解包后[0:0x60C6CE]，6342350 BYTE
    ]] ==>> script.欧路词典囗@试读囗囗假设简介字节数地址固定囗


0x4000 == 16K == 16384 == py.zlib.decompress:bufsize
    decompress(data, /, wbits=15, bufsize=16384)

英文二十六字母二级前缀分层/[前缀分区的词汇量]*702
    view script/欧路词典囗计算机词汇.py
        py -m nn_ns.app.adhoc_argparser__main__call8module   script.欧路词典囗计算机词汇   @尾部词条前缀分层囗检验囗
    702==26*27==26+26*26 !!! 英文26字母二级前缀分层！！
    仅有702项，却使用 L + L*L + L**3 + ...这种风格，虽然方便直查，无需二分搜索，但显然 对汉字无用。(汉字太多)

    #]]]'''#'''
    #(reader4header, reader_from_introduction, reader_from_word_pool_info_array) = _mk_reader()
    开启囗词汇 = False
    开启囗词汇囗依词义序 = False
    开启囗词义 = False
    if 输出文件囗词汇:
        开启囗词汇 = True
    if 输出文件囗词汇囗依词义序:
        开启囗词汇囗依词义序 = True
    if 输出文件囗全文:
        开启囗词义 = True
    if 输出文件囗词典:
        开启囗词汇 = True
        开启囗词义 = True
    if 输出文件囗杂项:
        pass
    kw = dict(开启囗词汇=开启囗词汇, 开启囗词汇囗依词义序=开启囗词汇囗依词义序, 开启囗词义=开启囗词义, errors_replace=errors_replace)

    if case == '简介字节数囗地址':
        [简介字节数囗地址] = args
        reader4known = _mk_reader5addr4introduction(简介字节数囗地址, **kw)
    elif case == '压缩包数量囗地址十十压缩包数组囗结束地址十十词汇量':
        [压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量] = args
        reader4known = _mk_reader5many_addr(压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, **kw)
    elif case == '自动化'
        [] = args
        reader4known = _mk_reader5many_addr(压缩包数量囗地址, 压缩包数组囗结束地址, 词汇量, **kw)
    else:
        raise Exception(f'unknown case: {case!r}')

    def __():
        print(reader4known)
        print(len(reader4known._ts))
        for i,x in enumerate(reader4known._ts):
            print(i, x)
        print(reader4known.get_exported_names())
    __()
    if 0b0:return
    check_type_is(bool, force)
    输出文件囗词汇, 输出文件囗词汇囗依词义序, 输出文件囗全文, 输出文件囗词典, 输出文件囗杂项 = 碰撞测试囗囗多个输出文件囗([(输出文件囗词汇, '输出文件囗词汇', force), (输出文件囗词汇囗依词义序, '输出文件囗词汇囗依词义序', force), (输出文件囗全文, '输出文件囗全文', force), (输出文件囗词典, '输出文件囗词典', force), (输出文件囗杂项, '输出文件囗杂项', force)])


    ipath = explain_ipath_(ipath)
    #bs = ipath.read_bytes()
    #文件字节数 = get_file_size(ipath)
    with open(ipath, 'rb') as ibfile:
        tpl, _result4ex = apply_reader(reader4known, ibfile)
            #result4ex :: (result/NamedTuple, _result4ex/((begin_addr4whole, end_addr4whole), ls4ex/[((begin_addr,end_addr), (is_xname_exported, is_xname_refered), (xname, idx4xname), may_obj)]))
    ###############
    ###############
    (begin_addr4whole, end_addr4whole), ls4ex = _result4ex
    ns = tpl.as_getter4named_tuple()
    def __():
        print(len(ns.包数组囗整合囗全字节串))
        print(len(ns.包数组囗整合囗全文))
        print(len(ns.词汇))
        for 词条字节串囗偏移量, (词条字节串囗字节数,(词义字节串囗解包后的偏移量,词义字节串囗长度)) in ns.词汇各词字节偏移量囗差分表:
            词条字节串囗偏移量
            词条字节串囗字节数
            词义字节串囗解包后的偏移量
            词义字节串囗长度
    if 0b0:__()
    print(f'词汇量={ns.词汇量}')
    print(f'开启囗词汇={开启囗词汇}')
    print(f'开启囗词义={开启囗词义}')
    r'''[[[
    现代汉语词典:
        6342350 #果然是 解包后的整体字节数！
        2859527 #0x2ba207
        57507
        57507
    ]]]'''#'''

    def 输出词汇(fout, ns, /):
        for 词条 in ns.词汇:
            print(词条, file=fout)

    def 输出词汇囗依词义序(fout, ns, /):
        for (词义字节串囗解包后的偏移量,词义字节串囗长度,词条) in ns.词汇囗依词义序囗附词义字节串信息:
            print(f'0x{词义字节串囗解包后的偏移量:X}:{词义字节串囗长度!s}:{词条!s}', file=fout)

    def 输出全文(fout, ns, /):
        fout.write(ns.包数组囗整合囗全文)

    def 输出词典(fout, ns, /):
        for 词条,词义 in zip(ns.词汇, ns.词义数组):
            assert not '\n' in 词义
            assert not '\r' in 词义
            print(f',{词条!s}', file=fout)
            print(f':{词义!s}', file=fout)

    def 输出杂项(fout, ns, ls4ex, /):
        # hex(addr), bytes.hex(' ', -2)
        for ((begin_addr,end_addr), (is_xname_exported, is_xname_refered), (xname, idx4xname), obj) in ls4ex:
            sz4bs = end_addr - begin_addr
            common = f'{idx4xname!r}:{xname!r}:@[{begin_addr!r}..<{end_addr!r}]:@[0x{begin_addr:X}..<0x{end_addr:X}]:={sz4bs!r}:=0x{sz4bs:X}'
            if not 判别杂项名输出与否囗(xname):
                if type(obj) is int:
                    addr_or_sz = obj
                    print(f'#:{common!s}:{addr_or_sz!r}:0x{addr_or_sz:X}', file=fout)
                continue
            assert type(obj) in (bytes, str)
            if type(obj) is bytes:
                bs = obj
                assert sz4bs == len(bs)
                hex4bs = bs.hex(' ')
                print(f'-:{common!s}:{hex4bs!r}', file=fout)
            elif type(obj) is str:
                txt = obj
                sz4txt = len(txt)
                print(f'+:{common!s}:{sz4txt!r}:{txt!r}', file=fout)
            else:
                raise Exception(((begin_addr,end_addr), (is_xname_exported, is_xname_refered), (xname, idx4xname), type(obj)))

    def 判别杂项名输出与否囗(nm, /):
        #简介, xml, 名含『未知』
        return nm == '简介' or nm == 'xml' or '未知' in nm


    if 输出文件囗词汇:
        with open4w(输出文件囗词汇, force=force, xencoding=oencoding) as fout:
            输出词汇(fout, ns)

    if 输出文件囗词汇囗依词义序:
        with open4w(输出文件囗词汇囗依词义序, force=force, xencoding=oencoding) as fout:
            输出词汇囗依词义序(fout, ns)

    if 输出文件囗全文:
        with open4w(输出文件囗全文, force=force, xencoding=oencoding) as fout:
            输出全文(fout, ns)
    if 输出文件囗词典:
        with open4w(输出文件囗词典, force=force, xencoding=oencoding) as fout:
            输出词典(fout, ns)
    if 输出文件囗杂项:
        with open4w(输出文件囗杂项, force=force, xencoding=oencoding) as fout:
            输出杂项(fout, ns, ls4ex)
#e ../../python3_src/nn_ns/codec/DecodeUtils.py
from seed.types.MakeDict import MakeOrderedDict, ListOrderedItems
#class d(MakeOrderedDict):
#class ps(ListOrderedItems):




