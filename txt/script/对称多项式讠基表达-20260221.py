#__all__:goto
r'''[[[
e script/对称多项式讠基表达.py
cp -iv script/对称多项式讠基表达.py ../../python3_src/seed/math/polynomial/
mv -iv script/对称多项式讠基表达.py script/对称多项式讠基表达-20260221.py


script.对称多项式讠基表达
py -m nn_ns.app.debug_cmd   script.对称多项式讠基表达 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.对称多项式讠基表达:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %script.对称多项式讠基表达:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'script.对称多项式讠基表达:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
view script/对称多项式讠基表达-old.py
    #mv -iv script/对称多项式讠基表达.py script/对称多项式讠基表达-old.py
]]
[[
view ../../python3_src/seed/math/combination.py
    #combinations(iterable, r)
    #permutations(iterable, r=None)

[础称平式=基础对称多项式(变量数) =[def]= let [sf.变量数:=变量数][k:=sf.变量数] in (\vars -> let [n:=len(vars)] in if [n < k] then 0 else (sum[II(sorted_vars) | [sorted_vars:<-combinations(vars,k)]]))]
    #combinations(iterable, r)

[础称乘式=基础对称多项式乘式(础称平式讠幂次) =[def]= let [sf.变量数:=max(础称平式.变量数 for 础称平式 in 础称平式讠幂次.keys())][k:=sf.变量数][k2e:=础称平式讠幂次] in (\vars -> let [n:=len(vars)] in if [n < k] then 0 else (II[础称平式(k;vars)**e | [(k,e):<-k2e.items()]]))]

[础称组式=基础对称多项式积和组合式(础称乘式讠系数) =[def]= let [(sf.最小变量数,sf.最大变量数):=minmax(础称乘式.变量数 for 础称乘式 in 础称乘式讠系数.keys())][k:=sf.最小变量数][k2eZc:=础称乘式讠系数] in (\vars -> let [n:=len(vars)] in if [n < k] then 0 else (sum[础称乘式(k2e;vars)*c | [(k2e,c):<-k2eZc.items()]]))]

#########
加乘
迦逫
十米
辻迷
瓧毩

grep '[加乘十米乂]' /sdcard/0my_files/tmp/out4py/script.hz.部件拆分..提取基本面编码空间里的汉字囗.out.txt | sort -t : -k 2
匊:a,勹,米,
籵:a,米,十,
毩:a,毛,米,
瓧:a,瓦,十,

,瓧:20923:瓦:6:155412:gnyf:shiwa:shíwǎ:瓧/shíwǎ//电功率“十瓦”的旧书写形式。
,毩:9709:毛:10:3115431234:tfno:ju:jū:毩jū/古同“鞠”，古时一种游戏用的皮球。
#########
加型vs乘型
    瓧/加型对称化:(3*a^2*b + 7*a) --> SUM{(3*X^2*Y + 7*X)}
        最大次数之和固化
    毩/乘型对称化:(3*a^2*b + 7*a) --> II{(3*X^2*Y + 7*X)}
        最大次数之和-->+oo
        只能先固化输入变量数n==len(vars)
#########
[瓧称重式=单项式耂加型对称化多项式(幂次讠重数) =[def]= let [sf.变量数:=sum(幂次讠重数.values())][k:=sf.变量数][e2r:=幂次讠重数][e_r_pairs:=sorted(e2r.items())] in (\vars -> let [n:=len(vars)] in if [n < k] then 0 else (1/(II[factorial(r) | [r:<-e2r.values()]]) * sum[II[II(_ordered_vars)**e | [(e,_ordered_vars):<-zip(map fst e_r_pairs,_ordered_varss)]] | [ordered_vars:<-permutations(vars,k)][_ordered_varss:=cut(map snd e_r_pairs;ordered_vars)]]))]
    #permutations(iterable, r=None)
    #(a^2*b) --> (a^2*b+b^2*a + a^2*c+b^2*c+c^2*a+c^2*b + ...)

[瓧称组式=多项式耂加型对称化多项式(瓧称重式讠系数) =[def]= let [(sf.最小变量数,sf.最大变量数):=minmax(瓧称重式.变量数 for 瓧称重式 in 瓧称重式讠系数.keys())][k:=sf.最小变量数][e2rZc:=瓧称重式讠系数] in (\vars -> let [n:=len(vars)] in if [n < k] then 0 else (sum[瓧称重式(e2r;vars)*c | [(e2r,c):<-e2rZc.items()]]))]
    #(3*a^2*b + 7*a) --> 3*(a^2*b+b^2*a + a^2*c+b^2*c+c^2*a+c^2*b + ...) + 7*(a+b+c+...)

#########
[础称组式({}) == 瓧称组式({}) == 0]
[础称组式({础称乘式({}):1}) == 瓧称组式({瓧称重式({}):1}) == 1]
[础称组式({础称乘式({础称平式(k):1}):1}) == 瓧称组式({瓧称重式({1:k}):1}) == 加型对称化(II(vars[:k]))]

#########
#########

[k2eZc :: {{num_vars{>=1}:exp{>=1}}:coeff{=!=0}}]
[e2rZc :: {{exp{>=1}:num_repeat{>=1}}:coeff{=!=0}}]
[瓧称组式讠础称组式扌 :: 瓧称组式{e2rZc} -> 础称组式{k2eZc}]

]]
[[
_瓧称重式讠础称组式扌
_拆分冫瓧称重式扌
降低幂次算法:
    [瓧称重式(幂次讠重数:={3:1,2:2,1:1})
    == (a^3*b^2*c^2*d + ...{加型对称化})
    == (a^2*b*c + ...{加型对称化})*(a*b*c*d + ...{加型对称化}) - 残差
    == 瓧称重式(幂次讠重数:={2:1,1:2})*础称平式(变量数:=4) - 残差
    == (recur...) - 残差
    == (recur...) - ((a^2*b*c*e*f*g*h     + a^3*b*c*e*f*g + a^2*b^2*c*e*f*g + a^2*b*c^2*e*f*g + a^2*b*c*d*e*f*g      + a^3*b^2*c*e*f + a^3*b*c^2*e*f + a^3*b*c*d*e*f + a^2*b^2*c^2*e*f + a^2*b^2*c*d*e*f + a^2*b*c^2*d*e*f     + a^3*b^2*c^2*e + a^3*b^2*c*d*e + a^3*b*c^2*d*e + a^2*b^2*c^2*d*e) + ...{加型对称化})
    ]
]]
[[
文本化:
表述冫础称平式讠文本表达扌
表述冫础称乘式讠文本表达扌
表述冫础称组式讠文本表达扌
表述冫瓧称重式讠文本表达扌
表述冫瓧称组式讠文本表达扌

NNN:正整数=([1-9][0-9]*)
FFF:非零有理数:[dp]{NNN}?(J{NNN})?

础称平式:I|wNNN
础称乘式:I|(wNNN(vNNNN)?)(XwNNN(vNNNN)?)*
础称组式:O|(kFFF{础称乘式}?)+

瓧称重式:I|(eNNN(rNNNN)?)(XeNNN(rNNNN)?)*
瓧称组式:O|(kFFF{瓧称重式}?)+
]]
[[
整数拆分:
view ../../python3_src/seed/math/uint_partition.py

]]





'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   script.对称多项式讠基表达   @解读冫瓧称重式巛文本表达扌  :e2e1r2    =0  =6  #miss:『X』
    (乸瓧称重式({2: 1}), 2)

py_adhoc_call   script.对称多项式讠基表达   @解读冫瓧称重式巛文本表达扌  :e2Xe1r2    =0  =6 # < 7
    (乸瓧称重式({2: 1, 1: 1}), 5)

py_adhoc_call   script.对称多项式讠基表达   @解读冫瓧称重式巛文本表达扌  :e2Xe1r2    =0  =7
    (乸瓧称重式({2: 1, 1: 2}), 7)
]]
[[
py_adhoc_call   script.对称多项式讠基表达   @解读冫瓧称组式巛文本表达扌  :kd  =0  =2
    (乸瓧称组式({乸瓧称重式({}): -1}), 2)

py_adhoc_call   script.对称多项式讠基表达   @解读冫瓧称组式巛文本表达扌  :kd3J5  =0  =5
    (乸瓧称组式({乸瓧称重式({}): Fraction(-3, 5)}), 5)

py_adhoc_call   script.对称多项式讠基表达   @解读冫瓧称组式巛文本表达扌  :kpJ5e3r2Xe5Xe4r2  =0  =16
    (乸瓧称组式({乸瓧称重式({3: 2, 5: 1, 4: 2}): Fraction(1, 5)}), 16)

]]
[[
py_adhoc_call   script.对称多项式讠基表达   @瓧称重式讠础称组式牜文本版扌  ='{}'  :e2
    'kpw1v2kd2w2'
    <==>:
    [(x^2+...) == (x+...)^2 -2*(x*y+...)]

py_adhoc_call   script.对称多项式讠基表达   @瓧称重式讠础称组式牜文本版扌  ='{}'  :e3
    'kd3w1Xw2kpw1v3kp3w3'
    <==>:
    [(x^3+...) == -3*(x+...)(x*y+...)  +(x+...)^3  +3*(x*y*z+...)]

]]
[[
++kw:欤随机数值校验丨随机数值串生成器
++__str__
py_adhoc_call   script.对称多项式讠基表达   @瓧称重式讠础称组式牜文本版扌  +欤随机数值校验丨随机数值串生成器  ='{}'  :e3
    'kd3w1Xw2kpw1v3kp3w3'
py_adhoc_call   script.对称多项式讠基表达   @瓧称重式讠础称组式牜文本版扌  +欤随机数值校验丨随机数值串生成器  ='{}'  :e1
    'kpw1'
]]
[[
py_adhoc_call   script.对称多项式讠基表达   ,str.枚举冫瓧称重式巛自然数牜整数拆分扌 =5
    e5
    e1Xe4
    e2Xe3
    e1r2Xe3
    e1Xe2r2
    e1r3Xe2
    e1r5
]]
[[
py_adhoc_call   script.对称多项式讠基表达   ,str.枚举冫瓧称重式辻础称组式巛自然数牜整数拆分扌 +欤文本版 ='{}' =5
e5:kp5w1Xw2v2kd5w1Xw4kp5w1v2Xw3kd5w1v3Xw2kpw1v5kd5w2Xw3kp5w5
e1Xe4:kd3w1Xw2v2kpw1Xw4kdw1v2Xw3kpw1v3Xw2kp5w2Xw3kd5w5
e2Xe3:kpw1Xw2v2kp5w1Xw4kd2w1v2Xw3kdw2Xw3kd5w5
e1r2Xe3:kdw1Xw4kpw1v2Xw3kd2w2Xw3kp5w5
e1Xe2r2:kd3w1Xw4kpw2Xw3kp5w5
e1r3Xe2:kpw1Xw4kd5w5
e1r5:kpw5

]]
[[
py_adhoc_call   script.对称多项式讠基表达   ,str.枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分扌 +欤文本版 +欤随机数值校验丨随机数值串生成器  ='{}'  ='range(10)'
    #total:97:1+1+2+3+5+7+11+15+22+30
I:kp
e1:kpw1
e2:kpw1v2kd2w2
e1r2:kpw2
e3:kd3w1Xw2kpw1v3kp3w3
e1Xe2:kpw1Xw2kd3w3
e1r3:kpw3
e4:kp4w1Xw3kd4w1v2Xw2kpw1v4kp2w2v2kd4w4
e1Xe3:kdw1Xw3kpw1v2Xw2kd2w2v2kp4w4
e2r2:kd2w1Xw3kpw2v2kp2w4
e1r2Xe2:kpw1Xw3kd4w4
e1r4:kpw4
e5:kp5w1Xw2v2kd5w1Xw4kp5w1v2Xw3kd5w1v3Xw2kpw1v5kd5w2Xw3kp5w5
e1Xe4:kd3w1Xw2v2kpw1Xw4kdw1v2Xw3kpw1v3Xw2kp5w2Xw3kd5w5
e2Xe3:kpw1Xw2v2kp5w1Xw4kd2w1v2Xw3kdw2Xw3kd5w5
e1r2Xe3:kdw1Xw4kpw1v2Xw3kd2w2Xw3kp5w5
e1Xe2r2:kd3w1Xw4kpw2Xw3kp5w5
e1r3Xe2:kpw1Xw4kd5w5
e1r5:kpw5
e6:kd12w1Xw2Xw3kp6w1Xw5kp9w1v2Xw2v2kd6w1v2Xw4kp6w1v3Xw3kd6w1v4Xw2kpw1v6kp6w2Xw4kd2w2v3kp3w3v2kd6w6
e1Xe5:kp7w1Xw2Xw3kdw1Xw5kd4w1v2Xw2v2kpw1v2Xw4kdw1v3Xw3kpw1v4Xw2kd6w2Xw4kp2w2v3kd3w3v2kp6w6
e2Xe4:kp4w1Xw2Xw3kd6w1Xw5kpw1v2Xw2v2kp2w1v2Xw4kd2w1v3Xw3kp2w2Xw4kd2w2v3kd3w3v2kp6w6
e1r2Xe4:kd3w1Xw2Xw3kpw1Xw5kdw1v2Xw4kpw1v3Xw3kp2w2Xw4kp3w3v2kd6w6
e3r2:kd3w1Xw2Xw3kd3w1Xw5kp3w1v2Xw4kd3w2Xw4kpw2v3kp3w3v2kp3w6
e1Xe2Xe3:kpw1Xw2Xw3kp7w1Xw5kd3w1v2Xw4kp4w2Xw4kd3w3v2kd12w6
e1r3Xe3:kdw1Xw5kpw1v2Xw4kd2w2Xw4kp6w6
e2r3:kp2w1Xw5kd2w2Xw4kpw3v2kd2w6
e1r2Xe2r2:kd4w1Xw5kpw2Xw4kp9w6
e1r4Xe2:kpw1Xw5kd6w6
e1r6:kpw6
e7:kp14w1Xw2Xw4kd7w1Xw2v3kp7w1Xw3v2kd7w1Xw6kd21w1v2Xw2Xw3kp7w1v2Xw5kp14w1v3Xw2v2kd7w1v3Xw4kp7w1v4Xw3kd7w1v5Xw2kpw1v7kd7w2Xw5kp7w2v2Xw3kd7w3Xw4kp7w7
e1Xe6:kd8w1Xw2Xw4kp5w1Xw2v3kd4w1Xw3v2kpw1Xw6kp9w1v2Xw2Xw3kdw1v2Xw5kd5w1v3Xw2v2kpw1v3Xw4kdw1v4Xw3kpw1v5Xw2kp7w2Xw5kd7w2v2Xw3kp7w3Xw4kd7w7
e2Xe5:kd4w1Xw2Xw4kd3w1Xw2v3kd7w1Xw3v2kp7w1Xw6kp6w1v2Xw2Xw3kd2w1v2Xw5kpw1v3Xw2v2kp2w1v3Xw4kd2w1v4Xw3kd3w2Xw5kp3w2v2Xw3kp7w3Xw4kd7w7
e1r2Xe5:kp3w1Xw2Xw4kp4w1Xw3v2kdw1Xw6kd4w1v2Xw2Xw3kpw1v2Xw5kdw1v3Xw4kpw1v4Xw3kd2w2Xw5kp2w2v2Xw3kd7w3Xw4kp7w7
e3Xe4:kd2w1Xw2Xw4kpw1Xw2v3kp5w1Xw3v2kp7w1Xw6kd3w1v2Xw2Xw3kd7w1v2Xw5kp3w1v3Xw4kp7w2Xw5kdw2v2Xw3kd5w3Xw4kd7w7
e1Xe2Xe4:kp8w1Xw2Xw4kdw1Xw3v2kd8w1Xw6kpw1v2Xw2Xw3kp3w1v2Xw5kd3w1v3Xw4kd4w2Xw5kd2w2v2Xw3kd2w3Xw4kp14w7
e1r3Xe4:kd3w1Xw2Xw4kpw1Xw6kdw1v2Xw5kpw1v3Xw4kp2w2Xw5kp3w3Xw4kd7w7
e1Xe3r2:kdw1Xw2Xw4kd2w1Xw3v2kd4w1Xw6kp4w1v2Xw5kd7w2Xw5kpw2v2Xw3kp5w3Xw4kp7w7
e2r2Xe3:kd2w1Xw2Xw4kpw1Xw3v2kd7w1Xw6kp2w1v2Xw5kp3w2Xw5kdw3Xw4kp7w7
e1r2Xe2Xe3:kpw1Xw2Xw4kp9w1Xw6kd4w1v2Xw5kp6w2Xw5kd3w3Xw4kd21w7
e1r4Xe3:kdw1Xw6kpw1v2Xw5kd2w2Xw5kp7w7
e1Xe2r3:kp5w1Xw6kd3w2Xw5kpw3Xw4kd7w7
e1r3Xe2r2:kd5w1Xw6kpw2Xw5kp14w7
e1r5Xe2:kpw1Xw6kd7w7
e1r7:kpw7
e8:kd16w1Xw2Xw5kp24w1Xw2v2Xw3kd16w1Xw3Xw4kp8w1Xw7kp24w1v2Xw2Xw4kd16w1v2Xw2v3kp12w1v2Xw3v2kd8w1v2Xw6kd32w1v3Xw2Xw3kp8w1v3Xw5kp20w1v4Xw2v2kd8w1v4Xw4kp8w1v5Xw3kd8w1v6Xw2kpw1v8kd8w2Xw3v2kp8w2Xw6kd8w2v2Xw4kp2w2v4kp8w3Xw5kp4w4v2kd8w8
e1Xe7:kp9w1Xw2Xw5kd17w1Xw2v2Xw3kp9w1Xw3Xw4kdw1Xw7kd10w1v2Xw2Xw4kp9w1v2Xw2v3kd5w1v2Xw3v2kpw1v2Xw6kp11w1v3Xw2Xw3kdw1v3Xw5kd6w1v4Xw2v2kpw1v4Xw4kdw1v5Xw3kpw1v6Xw2kp8w2Xw3v2kd8w2Xw6kp8w2v2Xw4kd2w2v4kd8w3Xw5kd4w4v2kp8w8
e2Xe6:kp4w1Xw2Xw5kp16w1Xw3Xw4kd8w1Xw7kd6w1v2Xw2Xw4kd4w1v2Xw2v3kd9w1v2Xw3v2kp2w1v2Xw6kp8w1v3Xw2Xw3kd2w1v3Xw5kpw1v4Xw2v2kp2w1v4Xw4kd2w1v5Xw3kp2w2Xw3v2kp4w2Xw6kd4w2v2Xw4kp2w2v4kd8w3Xw5kd4w4v2kp8w8
e1r2Xe6:kd3w1Xw2Xw5kp5w1Xw2v2Xw3kd9w1Xw3Xw4kpw1Xw7kp4w1v2Xw2Xw4kp5w1v2Xw3v2kdw1v2Xw6kd5w1v3Xw2Xw3kpw1v3Xw5kdw1v4Xw4kpw1v5Xw3kd5w2Xw3v2kp2w2Xw6kd2w2v2Xw4kp8w3Xw5kp4w4v2kd8w8
e3Xe5:kpw1Xw2Xw5kp6w1Xw2v2Xw3kpw1Xw3Xw4kd8w1Xw7kd9w1v2Xw2Xw4kpw1v2Xw2v3kp3w1v2Xw3v2kp8w1v2Xw6kd3w1v3Xw2Xw3kd3w1v3Xw5kp3w1v4Xw4kd7w2Xw3v2kd8w2Xw6kp8w2v2Xw4kd2w2v4kp7w3Xw5kd4w4v2kp8w8
e1Xe2Xe5:kd8w1Xw2Xw5kd3w1Xw2v2Xw3kd10w1Xw3Xw4kp9w1Xw7kp11w1v2Xw2Xw4kdw1v2Xw3v2kd3w1v2Xw6kpw1v3Xw2Xw3kp3w1v3Xw5kd3w1v4Xw4kp5w2Xw3v2kp4w2Xw6kd4w2v2Xw4kpw3Xw5kp8w4v2kd16w8
e1r3Xe5:kp3w1Xw2Xw5kp4w1Xw3Xw4kdw1Xw7kd4w1v2Xw2Xw4kpw1v2Xw6kdw1v3Xw5kpw1v4Xw4kd2w2Xw6kp2w2v2Xw4kd3w3Xw5kd4w4v2kp8w8
e4r2:kp8w1Xw2Xw5kd4w1Xw2v2Xw3kd8w1Xw3Xw4kd4w1Xw7kp4w1v2Xw2Xw4kp2w1v2Xw3v2kp4w1v2Xw6kd4w1v3Xw5kp4w2Xw3v2kd4w2Xw6kd4w2v2Xw4kpw2v4kd4w3Xw5kp6w4v2kp4w8
e1Xe3Xe4:kd10w1Xw2Xw5kpw1Xw2v2Xw3kp10w1Xw3Xw4kp9w1Xw7kdw1v2Xw2Xw4kd2w1v2Xw3v2kd9w1v2Xw6kp4w1v3Xw5kdw2Xw3v2kp16w2Xw6kpw3Xw5kd8w4v2kd16w8
e2r2Xe4:kd4w1Xw2Xw5kp8w1Xw7kd2w1v2Xw2Xw4kpw1v2Xw3v2kd2w1v2Xw6kp2w1v3Xw5kd2w2Xw3v2kd4w2Xw6kp4w2v2Xw4kp8w3Xw5kd4w4v2kd8w8
e1r2Xe2Xe4:kp11w1Xw2Xw5kdw1Xw3Xw4kd10w1Xw7kpw1v2Xw2Xw4kp4w1v2Xw6kd4w1v3Xw5kd6w2Xw6kd2w2v2Xw4kd9w3Xw5kp4w4v2kp24w8
e1r4Xe4:kd3w1Xw2Xw5kpw1Xw7kdw1v2Xw6kpw1v3Xw5kp2w2Xw6kp3w3Xw5kd8w8
e2Xe3r2:kp5w1Xw2Xw5kdw1Xw3Xw4kp8w1Xw7kd5w1v2Xw6kpw2Xw3v2kp2w2Xw6kd2w2v2Xw4kd7w3Xw5kp4w4v2kd8w8
e1r2Xe3r2:kdw1Xw2Xw5kd2w1Xw3Xw4kd5w1Xw7kp5w1v2Xw6kd9w2Xw6kpw2v2Xw4kp3w3Xw5kp2w4v2kp12w8
e1Xe2r2Xe3:kd3w1Xw2Xw5kpw1Xw3Xw4kd17w1Xw7kp5w1v2Xw6kp6w3Xw5kd4w4v2kp24w8
e1r3Xe2Xe3:kpw1Xw2Xw5kp11w1Xw7kd5w1v2Xw6kp8w2Xw6kd3w3Xw5kd32w8
e1r5Xe3:kdw1Xw7kpw1v2Xw6kd2w2Xw6kp8w8
e2r4:kd2w1Xw7kp2w2Xw6kd2w3Xw5kpw4v2kp2w8
e1r2Xe2r3:kp9w1Xw7kd4w2Xw6kpw3Xw5kd16w8
e1r4Xe2r2:kd6w1Xw7kpw2Xw6kp20w8
e1r6Xe2:kpw1Xw7kd8w8
e1r8:kpw8
e9:kd27w1Xw2Xw3v2kp18w1Xw2Xw6kd27w1Xw2v2Xw4kp9w1Xw2v4kp18w1Xw3Xw5kp9w1Xw4v2kd9w1Xw8kd27w1v2Xw2Xw5kp54w1v2Xw2v2Xw3kd27w1v2Xw3Xw4kp9w1v2Xw7kp36w1v3Xw2Xw4kd30w1v3Xw2v3kp18w1v3Xw3v2kd9w1v3Xw6kd45w1v4Xw2Xw3kp9w1v4Xw5kp27w1v5Xw2v2kd9w1v5Xw4kp9w1v6Xw3kd9w1v7Xw2kpw1v9kp18w2Xw3Xw4kd9w2Xw7kp9w2v2Xw5kd9w2v3Xw3kd9w3Xw6kp3w3v3kd9w4Xw5kp9w9
e1Xe8:kp19w1Xw2Xw3v2kd10w1Xw2Xw6kp19w1Xw2v2Xw4kd7w1Xw2v4kd10w1Xw3Xw5kd5w1Xw4v2kpw1Xw8kp11w1v2Xw2Xw5kd30w1v2Xw2v2Xw3kp11w1v2Xw3Xw4kdw1v2Xw7kd12w1v3Xw2Xw4kp14w1v3Xw2v3kd6w1v3Xw3v2kpw1v3Xw6kp13w1v4Xw2Xw3kdw1v4Xw5kd7w1v5Xw2v2kpw1v5Xw4kdw1v6Xw3kpw1v7Xw2kd18w2Xw3Xw4kp9w2Xw7kd9w2v2Xw5kp9w2v3Xw3kp9w3Xw6kd3w3v3kp9w4Xw5kd9w9
e2Xe7:kp13w1Xw2Xw3v2kd4w1Xw2Xw6kdw1Xw2v2Xw4kp5w1Xw2v4kd18w1Xw3Xw5kd9w1Xw4v2kp9w1Xw8kp6w1v2Xw2Xw5kd5w1v2Xw2v2Xw3kp20w1v2Xw3Xw4kd2w1v2Xw7kd8w1v3Xw2Xw4kd5w1v3Xw2v3kd11w1v3Xw3v2kp2w1v3Xw6kp10w1v4Xw2Xw3kd2w1v4Xw5kpw1v5Xw2v2kp2w1v5Xw4kd2w1v6Xw3kd4w2Xw3Xw4kd5w2Xw7kp5w2v2Xw5kd5w2v3Xw3kp9w3Xw6kd3w3v3kp9w4Xw5kd9w9
e1r2Xe7:kd12w1Xw2Xw3v2kp3w1Xw2Xw6kd5w1Xw2v2Xw4kp10w1Xw3Xw5kp5w1Xw4v2kdw1Xw8kd4w1v2Xw2Xw5kp9w1v2Xw2v2Xw3kd11w1v2Xw3Xw4kpw1v2Xw7kp5w1v3Xw2Xw4kp6w1v3Xw3v2kdw1v3Xw6kd6w1v4Xw2Xw3kpw1v4Xw5kdw1v5Xw4kpw1v6Xw3kp11w2Xw3Xw4kd2w2Xw7kp2w2v2Xw5kd2w2v3Xw3kd9w3Xw6kp3w3v3kd9w4Xw5kp9w9
e3Xe6:kd18w1Xw2Xw3v2kp9w1Xw2v2Xw4kd3w1Xw2v4kd9w1Xw4v2kp9w1Xw8kp9w1v2Xw2Xw5kp9w1v2Xw2v2Xw3kp9w1v2Xw3Xw4kd9w1v2Xw7kd12w1v3Xw2Xw4kpw1v3Xw2v3kp3w1v3Xw3v2kp3w1v3Xw6kd3w1v4Xw2Xw3kd3w1v4Xw5kp3w1v5Xw4kp9w2Xw7kd9w2v2Xw5kp3w2v3Xw3kd9w3Xw6kp6w3v3kp9w4Xw5kd9w9
e1Xe2Xe6:kp7w1Xw2Xw3v2kp8w1Xw2Xw6kd12w1Xw2v2Xw4kp10w1Xw3Xw5kp14w1Xw4v2kd10w1Xw8kd11w1v2Xw2Xw5kd4w1v2Xw2v2Xw3kd13w1v2Xw3Xw4kp3w1v2Xw7kp14w1v3Xw2Xw4kdw1v3Xw3v2kd3w1v3Xw6kpw1v4Xw2Xw3kp3w1v4Xw5kd3w1v5Xw4kp4w2Xw3Xw4kd4w2Xw7kp4w2v2Xw5kp2w2v3Xw3kd3w3v3kd18w4Xw5kp18w9
e1r3Xe6:kd3w1Xw2Xw6kp5w1Xw2v2Xw4kd4w1Xw3Xw5kd5w1Xw4v2kpw1Xw8kp4w1v2Xw2Xw5kp5w1v2Xw3Xw4kdw1v2Xw7kd5w1v3Xw2Xw4kpw1v3Xw6kdw1v4Xw5kpw1v5Xw4kd5w2Xw3Xw4kp2w2Xw7kd2w2v2Xw5kp3w3Xw6kp9w4Xw5kd9w9
e4Xe5:kp7w1Xw2Xw3v2kd18w1Xw2Xw6kd3w1Xw2v2Xw4kpw1Xw2v4kp2w1Xw3Xw5kp11w1Xw4v2kp9w1Xw8kp7w1v2Xw2Xw5kd4w1v2Xw2v2Xw3kd13w1v2Xw3Xw4kd9w1v2Xw7kp4w1v3Xw2Xw4kp2w1v3Xw3v2kp9w1v3Xw6kd4w1v4Xw5kp2w2Xw3Xw4kp9w2Xw7kpw2v2Xw5kdw2v3Xw3kp9w3Xw6kd3w3v3kd11w4Xw5kd9w9
e1Xe3Xe5:kp4w1Xw2Xw3v2kp10w1Xw2Xw6kp2w1Xw2v2Xw4kp5w1Xw3Xw5kd6w1Xw4v2kd10w1Xw8kd15w1v2Xw2Xw5kpw1v2Xw2v2Xw3kp5w1v2Xw3Xw4kp10w1v2Xw7kdw1v3Xw2Xw4kd2w1v3Xw3v2kd4w1v3Xw6kp4w1v4Xw5kd2w2Xw3Xw4kd18w2Xw7kp8w2v2Xw5kd2w2v3Xw3kd3w3v3kp2w4Xw5kp18w9
e2r2Xe5:kd3w1Xw2Xw3v2kp4w1Xw2Xw6kp6w1Xw2v2Xw4kp8w1Xw3Xw5kdw1Xw4v2kd9w1Xw8kd6w1v2Xw2Xw5kp2w1v2Xw7kd2w1v3Xw2Xw4kpw1v3Xw3v2kd2w1v3Xw6kp2w1v4Xw5kd6w2Xw3Xw4kp5w2Xw7kd9w3Xw6kp3w3v3kpw4Xw5kp9w9
e1r2Xe2Xe5:kd11w1Xw2Xw6kd3w1Xw2v2Xw4kd15w1Xw3Xw5kpw1Xw4v2kp11w1Xw8kp15w1v2Xw2Xw5kdw1v2Xw3Xw4kd4w1v2Xw7kpw1v3Xw2Xw4kp4w1v3Xw6kd4w1v4Xw5kp5w2Xw3Xw4kp6w2Xw7kd6w2v2Xw5kp9w3Xw6kp7w4Xw5kd27w9
e1r4Xe5:kp3w1Xw2Xw6kp4w1Xw3Xw5kdw1Xw8kd4w1v2Xw2Xw5kpw1v2Xw7kdw1v3Xw6kpw1v4Xw5kd2w2Xw7kp2w2v2Xw5kd3w3Xw6kd4w4Xw5kp9w9
e1Xe4r2:kd3w1Xw2Xw3v2kp14w1Xw2Xw6kdw1Xw2v2Xw4kd6w1Xw3Xw5kd5w1Xw4v2kd5w1Xw8kpw1v2Xw2Xw5kp5w1v2Xw3Xw4kp5w1v2Xw7kd5w1v3Xw6kd2w2Xw3Xw4kd9w2Xw7kdw2v2Xw5kpw2v3Xw3kd9w3Xw6kp3w3v3kp11w4Xw5kp9w9
e2Xe3Xe4:kpw1Xw2Xw3v2kp4w1Xw2Xw6kd2w1Xw2v2Xw4kd2w1Xw3Xw5kd2w1Xw4v2kd18w1Xw8kp5w1v2Xw2Xw5kdw1v2Xw3Xw4kp11w1v2Xw7kd5w1v3Xw6kp8w2Xw3Xw4kd4w2Xw7kd6w2v2Xw5kd3w3v3kp2w4Xw5kp18w9
e1r2Xe3Xe4:kd13w1Xw2Xw6kpw1Xw2v2Xw4kp5w1Xw3Xw5kp5w1Xw4v2kp11w1Xw8kdw1v2Xw2Xw5kd2w1v2Xw3Xw4kd11w1v2Xw7kp5w1v3Xw6kdw2Xw3Xw4kp20w2Xw7kp9w3Xw6kd13w4Xw5kd27w9
e1Xe2r2Xe4:kd12w1Xw2Xw6kp2w1Xw3Xw5kdw1Xw4v2kp19w1Xw8kd3w1v2Xw2Xw5kpw1v2Xw3Xw4kd5w1v2Xw7kp5w1v3Xw6kd2w2Xw3Xw4kdw2Xw7kp6w2v2Xw5kp9w3Xw6kd3w4Xw5kd27w9
e1r3Xe2Xe4:kp14w1Xw2Xw6kdw1Xw3Xw5kd12w1Xw8kpw1v2Xw2Xw5kp5w1v2Xw7kd5w1v3Xw6kd8w2Xw7kd2w2v2Xw5kd12w3Xw6kp4w4Xw5kp36w9
e1r5Xe4:kd3w1Xw2Xw6kpw1Xw8kdw1v2Xw7kpw1v3Xw6kp2w2Xw7kp3w3Xw6kd9w9
e3r3:kd3w1Xw2Xw6kd3w1Xw3Xw5kp3w1Xw4v2kd3w1Xw8kp3w1v2Xw7kd3w2Xw3Xw4kd3w2Xw7kp3w2v2Xw5kp6w3Xw6kpw3v3kd3w4Xw5kp3w9
e1Xe2Xe3r2:kp7w1Xw2Xw6kp4w1Xw3Xw5kd3w1Xw4v2kp19w1Xw8kd12w1v2Xw7kpw2Xw3Xw4kp13w2Xw7kd3w2v2Xw5kd18w3Xw6kp7w4Xw5kd27w9
e1r3Xe3r2:kdw1Xw2Xw6kd2w1Xw3Xw5kd6w1Xw8kp6w1v2Xw7kd11w2Xw7kpw2v2Xw5kp3w3Xw6kp2w4Xw5kp18w9
e2r3Xe3:kp2w1Xw2Xw6kd2w1Xw3Xw5kpw1Xw4v2kp9w1Xw8kd2w1v2Xw7kd5w2Xw7kp3w3Xw6kdw4Xw5kd9w9
e1r2Xe2r2Xe3:kd4w1Xw2Xw6kpw1Xw3Xw5kd30w1Xw8kp9w1v2Xw7kd5w2Xw7kp9w3Xw6kd4w4Xw5kp54w9
e1r4Xe2Xe3:kpw1Xw2Xw6kp13w1Xw8kd6w1v2Xw7kp10w2Xw7kd3w3Xw6kd45w9
e1r6Xe3:kdw1Xw8kpw1v2Xw7kd2w2Xw7kp9w9
e1Xe2r4:kd7w1Xw8kp5w2Xw7kd3w3Xw6kpw4Xw5kp9w9
e1r3Xe2r3:kp14w1Xw8kd5w2Xw7kpw3Xw6kd30w9
e1r5Xe2r2:kd7w1Xw8kpw2Xw7kp27w9
e1r7Xe2:kpw1Xw8kd9w9
e1r9:kpw9

]]
[[
py_adhoc_call   seed.math.uint_partition   @list.20:iter_uint_and_num_uint_partitions_pairs_ --cache=... +without_uint
py_adhoc_call   seed.math.uint_partition   @sum.10:iter_uint_and_num_uint_partitions_pairs_ --cache=... +without_uint
    97
py_adhoc_call   seed.math.uint_partition   @sum.20:iter_uint_and_num_uint_partitions_pairs_ --cache=... +without_uint
    2087
py_adhoc_call   seed.math.uint_partition   @sum.21:iter_uint_and_num_uint_partitions_pairs_ --cache=... +without_uint
    2714
py_adhoc_call   seed.math.uint_partition   @sum.26:iter_uint_and_num_uint_partitions_pairs_ --cache=... +without_uint
    9296
py_adhoc_call   seed.math.uint_partition   @sum.30:iter_uint_and_num_uint_partitions_pairs_ --cache=... +without_uint
    23025

def 枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌(文件路径冃缓存冃瓧称重式讠础称组式, 序列纟自然数, /, *, 欤随机数值校验丨随机数值串生成器=False, 欤文本版=False):
感觉 数值校验 很费时，取消...

#py_adhoc_call   script.对称多项式讠基表达   ,str.枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌   -欤随机数值校验丨随机数值串生成器  +欤文本版  :script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.out.txt  ='range(10)'
#py_adhoc_call   script.对称多项式讠基表达   ,str.枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌   -欤随机数值校验丨随机数值串生成器  +欤文本版  :script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.out.txt  ='range(10,21)'
view script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.out.txt
du -bh script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.out.txt
    8.9K #@lt10 #le9 #total:97
    5.7M #@lt21 #le20#total:2714

mv -iv script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.out.txt script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.le20.未曾数值校验.out.txt
tar -cvf script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.le20.未曾数值校验.out.txt.tar.lzma --lzma -C script/ 对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.le20.未曾数值校验.out.txt
tar -tf script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.le20.未曾数值校验.out.txt.tar.lzma
tar -xf script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.le20.未曾数值校验.out.txt.tar.lzma -O | more
du -bh script/对称多项式讠基表达.py..枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌.le20.未曾数值校验.out.txt.tar.lzma
    785K #<--5.7M #le20#total:2714

]]




py_adhoc_call   script.对称多项式讠基表达   @f
from script.对称多项式讠基表达 import *
]]]'''#'''
__all__ = r'''
枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌

瓧称组式讠础称组式扌
瓧称重式讠础称组式扌

瓧称组式讠础称组式牜文本版扌
瓧称重式讠础称组式牜文本版扌
    表述冫础称组式讠文本表达扌
    解读冫瓧称重式巛文本表达扌
    解读冫瓧称组式巛文本表达扌





乸础称平式
乸础称乘式
乸础称组式

乸瓧称重式
乸瓧称组式

检查冫系数扌



表述冫础称平式讠文本表达扌
表述冫础称乘式讠文本表达扌
表述冫础称组式讠文本表达扌
表述冫非零系数讠文本表达扌
表述冫瓧称重式讠文本表达扌
表述冫瓧称组式讠文本表达扌

解读冫础称平式巛文本表达扌
解读冫础称乘式巛文本表达扌
解读冫础称组式巛文本表达扌
解读冫非零系数巛文本表达扌
解读冫瓧称重式巛文本表达扌
解读冫瓧称组式巛文本表达扌

FormatError
取冫彣首字符巛文本扌
取冫首字符巛文本扌
取查冫首字符巛文本扌
解读冫正整数巛文本表达扌
解读冫非零有理数巛文本表达扌



ValidateFail
随机数值校验牜瓧称囜式扌
    随机数值校验牜瓧称重式扌
    随机数值校验牜瓧称组式扌


乸文件冃缓存冃瓧称重式讠础称组式
    加载冫缓存冃瓧称重式讠础称组式巛文件扌
枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌
    枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分扌
        枚举冫瓧称重式辻础称组式巛自然数牜整数拆分扌
            枚举冫瓧称重式巛自然数牜整数拆分扌


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
import re
from collections.abc import MutableMapping
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
#.from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
with mk_ctx4lazy_import4funcs_(__name__):
    from random import randint
    from itertools import accumulate#islice
    from functools import cached_property
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.tiny_.containers import mk_tuple
    from seed.tiny_.types5py import mk_MapView#MapView
    from seed.tiny_.funcs import snd #echo,fst,snd
    from seed.math.II import II
    from seed.math.combination import combinations, product, C
    from fractions import Fraction

    from seed.iters.flatten_recur import flatten_recur
    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
    from seed.tiny_.dict__add_fmap_filter import dict_add__new #fmap4dict_value, filter4dict_value, dict_add__is, dict_add__eq, dict_add__new, group4dict_value
    from seed.math.power.addition_chain.short.cf_chain import 构造冫加靶链牜加辗链构造式扌
        # :: 靶值集 -> 加靶链
    from seed.math.power.addition_chain.common.indices import 松序加链讠址引减一讠最大最小加数址引扌
    #########
    # view ../../python3_src/seed/math/combination__parts.py
    from seed.math.combination__parts import 排列组合牜泛型牜树状遍历扌, LEAF, ENTER, EXIT, 排列组合牜指定次序牜树状遍历扌, 预备冫参数纟排列组合牜泛型牜树状遍历扌
    #[(LEAF, ENTER, EXIT) == (0, +1, -1)]
    #def 排列组合牜泛型牜树状遍历扌(候选数, 入选数, 未规范泛型拆分表纟入选数, /, *, 鬽起始已入选名单=None):
    #    '候选数/uint -> 入选数/uint -> 拆分表{入选数} -> Iter (单步况态, 已入选名单/SeqView[uint%候选数]{len<=入选数}) # [单步况态 :: (+1/ENTER|-1/EXIT|0/LEAF)]'
    #def 预备冫参数纟排列组合牜泛型牜树状遍历扌(入选数, 未规范泛型拆分表纟入选数, /):
    #    '入选数 -> 未规范泛型拆分表纟入选数 -> 位置讠毝更小位置纟更小入选值'
    #def 排列组合牜指定次序牜树状遍历扌(候选数, 入选数, 位置讠毝更小位置纟更小入选值, /, *, 鬽起始已入选名单=None):
    #    '候选数/uint -> 入选数/uint -> 位置讠毝更小位置纟更小入选值/次序表{入选数}/[imay uint%入选数]{len==入选数} -> Iter (单步况态, 已入选名单/SeqView[uint%候选数]{len<=入选数}) # [单步况态 :: (+1/ENTER|-1/EXIT|0/LEAF)] # [all(-1 <= imay_i < j for j, imay_i in enumerate(位置讠毝更小位置纟更小入选值))]'
    #########



    from seed.math.uint_partition import uint2iter_uint_partitions_
    #:def uint2iter_uint_partitions_(u, /, *, to_expand=True, max4part=None, max4num_parts=None):
    #:    'u/uint -> (kw:to_expand/bool) -> Iter ([part] if to_expand else [(part, count)]) # in decreasing order'



___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__




class _乸全序:
    def __ne__(sf, ot, /):
        return not ot == sf
    def __lt__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return not ot <= sf
    def __gt__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return not sf <= ot
    def __ge__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return ot <= sf
class _乸含属性变量数:
    @property
    def 最小变量数(sf, /):
        return sf.变量数
    @property
    def 最大变量数(sf, /):
        return sf.变量数
class 乸础称平式(_乸全序, _乸含属性变量数):
    '础称平式=基础对称多项式(变量数)'
    def __init__(sf, 变量数, /):
        #check_int_ge(0, 变量数)
        check_int_ge(1, 变量数)
        sf._k = 变量数
    @property
    def 变量数(sf, /):
        return sf._k
    @classmethod
    def 巛文本扌(cls, 文本冃础称平式, /):
        return _巛文本扌(cls, 解读冫础称平式巛文本表达扌, 文本冃础称平式)
    def __str__(sf, /):
        文本冃础称平式 = 表述冫础称平式讠文本表达扌(础称平式:=sf, 欤校验=True)
        return 文本冃础称平式
    def __repr__(sf, /):
        k = sf.变量数
        return f'乸础称平式({k})'
    def __hash__(sf, /):
        return sf._k
    def __eq__(sf, ot, /):
        if sf is ot:return True
        return type(sf) is type(ot) and sf._k == ot._k
    def __le__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return sf._k <= ot._k

    def eval(sf, 序列纟变量值, /, *, 鬽缓存冃变量数讠幂次讠幂方=None):
        变量号讠变量值 = mk_tuple(序列纟变量值)
        777;del 序列纟变量值
        if len(变量号讠变量值) < sf.变量数:
            return 0
        #return sum(map(II, combinations(变量号讠变量值, sf.变量数)))
        变量数讠幂次讠幂方 = _缓存巛鬽缓存冃变量数讠幂次讠幂方扌(鬽缓存冃变量数讠幂次讠幂方)
        幂次讠幂方 = 变量数讠幂次讠幂方.setdefault(sf.变量数, {})
        if not 幂次讠幂方:
            幂次讠幂方[1] = sum(II(中选变量值集) for 中选变量值集 in combinations(变量号讠变量值, sf.变量数))
        return 幂次讠幂方[1]

class 乸础称乘式(_乸全序, _乸含属性变量数):
    '础称乘式=基础对称多项式乘式(础称平式讠幂次)'
    def __init__(sf, 础称平式讠幂次, /):
        k2e = 础称平式讠幂次 = {**础称平式讠幂次}
        for 础称平式 in 础称平式讠幂次.keys():
            check_type_is(乸础称平式, 础称平式)
            check_int_ge(1, 础称平式.变量数)
        for 幂次 in 础称平式讠幂次.values():
            check_int_ge(1, 幂次)
        sf._k2e = 础称平式讠幂次
        #sf._k_e_pairs = None#k_e_pairs = tuple(sorted(k2e.items()))
        #sf._h = None#hash(k_e_pairs)
    @property
    def 础称平式讠幂次(sf, /):
        return mk_MapView(sf._k2e)
    @cached_property
    def 变量数(sf, /):
        return max((础称平式.变量数 for 础称平式 in sf.础称平式讠幂次), default=0)
    @cached_property
    def _k_e_pairs(sf, /):
        k2e = sf.础称平式讠幂次
        return tuple(sorted(k2e.items()))
    @cached_property
    def _h(sf, /):
        k_e_pairs = sf._k_e_pairs
        return hash(k_e_pairs)
    @classmethod
    def 巛文本扌(cls, 文本冃础称乘式, /):
        return _巛文本扌(cls, 解读冫础称乘式巛文本表达扌, 文本冃础称乘式)
    def __str__(sf, /):
        文本冃础称乘式 = 表述冫础称乘式讠文本表达扌(础称乘式:=sf, 欤校验=True)
        return 文本冃础称乘式
    def __repr__(sf, /):
        k2e = sf._k2e
        return f'乸础称乘式({k2e})'
    def __hash__(sf, /):
        return sf._h
    def __eq__(sf, ot, /):
        if sf is ot:return True
        return type(sf) is type(ot) and sf._k_e_pairs == ot._k_e_pairs
    def __le__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return sf._k_e_pairs <= ot._k_e_pairs

    def eval(sf, 序列纟变量值, /, *, 鬽缓存冃变量数讠幂次讠幂方=None):
        变量号讠变量值 = mk_tuple(序列纟变量值)
        777;del 序列纟变量值
        if len(变量号讠变量值) < sf.变量数:
            return 0
        变量数讠幂次讠幂方 = _缓存巛鬽缓存冃变量数讠幂次讠幂方扌(鬽缓存冃变量数讠幂次讠幂方)
        #.return II(础称平式.eval(变量号讠变量值, 鬽缓存冃变量数讠幂次讠幂方=变量数讠幂次讠幂方)**幂次 for 础称平式, 幂次 in sf.础称平式讠幂次.items())
        return II(_pow(变量数讠幂次讠幂方, 变量号讠变量值, 幂次, 础称平式) for 础称平式, 幂次 in sf.础称平式讠幂次.items())

def _pow(变量数讠幂次讠幂方, 变量号讠变量值, 幂次, 础称平式):
    #.return 础称平式.eval(变量号讠变量值, 鬽缓存冃变量数讠幂次讠幂方=变量数讠幂次讠幂方)**幂次
    幂次讠幂方 = 变量数讠幂次讠幂方.setdefault(础称平式.变量数, {})
    if not 幂次讠幂方:
        础称平式.eval(变量号讠变量值, 鬽缓存冃变量数讠幂次讠幂方=变量数讠幂次讠幂方)
    if not 幂次 in 幂次讠幂方:
        幂次讠幂方[幂次] = 幂次讠幂方[1]**幂次
    return 幂次讠幂方[幂次]

class 乸础称组式(_乸全序):
    '础称组式=基础对称多项式积和组合式(础称乘式讠系数)'
    def __init__(sf, 础称乘式讠系数, /):
        k2eZc = 础称乘式讠系数 = {**础称乘式讠系数}
        for 础称乘式 in 础称乘式讠系数.keys():
            check_type_is(乸础称乘式, 础称乘式)
        for 系数 in 础称乘式讠系数.values():
            检查冫系数扌(系数)
        sf._k2eZc = 础称乘式讠系数
    @property
    def 础称乘式讠系数(sf, /):
        return mk_MapView(sf._k2eZc)
    @cached_property
    def 最小变量数(sf, /):
        return min((础称乘式.变量数 for 础称乘式 in sf.础称乘式讠系数), default=0)
    @cached_property
    def 最大变量数(sf, /):
        return max((础称乘式.变量数 for 础称乘式 in sf.础称乘式讠系数), default=0)
    @cached_property
    def _k2e_c_pairs(sf, /):
        k2eZc = sf.础称乘式讠系数
        return tuple(sorted(k2eZc.items()))
    @cached_property
    def _h(sf, /):
        k2e_c_pairs = sf._k2e_c_pairs
        return hash(k2e_c_pairs)
    @classmethod
    def 巛文本扌(cls, 文本冃础称组式, /):
        return _巛文本扌(cls, 解读冫础称组式巛文本表达扌, 文本冃础称组式)
    def __str__(sf, /):
        文本冃础称组式 = 表述冫础称组式讠文本表达扌(础称组式:=sf, 欤校验=True)
        return 文本冃础称组式
    def __repr__(sf, /):
        k2eZc = sf._k2eZc
        return f'乸础称组式({k2eZc})'
    def __hash__(sf, /):
        return sf._h
    def __eq__(sf, ot, /):
        if sf is ot:return True
        return type(sf) is type(ot) and sf._k2e_c_pairs == ot._k2e_c_pairs
    def __le__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return sf._k2e_c_pairs <= ot._k2e_c_pairs

    def eval(sf, 序列纟变量值, /, *, 鬽缓存冃变量数讠幂次讠幂方=None):
        变量号讠变量值 = mk_tuple(序列纟变量值)
        777;del 序列纟变量值
        if len(变量号讠变量值) < sf.最小变量数:
            return 0
        变量数讠幂次讠幂方 = _缓存巛鬽缓存冃变量数讠幂次讠幂方扌(鬽缓存冃变量数讠幂次讠幂方)
        return sum(础称乘式.eval(变量号讠变量值, 鬽缓存冃变量数讠幂次讠幂方=变量数讠幂次讠幂方)*系数 for 础称乘式, 系数 in sf.础称乘式讠系数.items())

def _缓存巛鬽缓存冃变量数讠幂次讠幂方扌(鬽缓存冃变量数讠幂次讠幂方, /):
    if None is 鬽缓存冃变量数讠幂次讠幂方:
        变量数讠幂次讠幂方 = {}
    else:
        变量数讠幂次讠幂方 = 鬽缓存冃变量数讠幂次讠幂方
    变量数讠幂次讠幂方
    变量数讠幂次讠幂方.items()
    return 变量数讠幂次讠幂方





class 乸瓧称重式(_乸全序, _乸含属性变量数):
    '瓧称重式=单项式耂加型对称化多项式(幂次讠重数)'
    def __init__(sf, 幂次讠重数, /):
        e2r = 幂次讠重数 = {**幂次讠重数}
        for 幂次 in 幂次讠重数.keys():
            check_int_ge(1, 幂次)
        for 重数 in 幂次讠重数.values():
            check_int_ge(1, 重数)
        sf._e2r = 幂次讠重数
    @property
    def 幂次讠重数(sf, /):
        return mk_MapView(sf._e2r)
    @cached_property
    def 变量数(sf, /):
        return sum(sf.幂次讠重数.values())
    @cached_property
    def _e_r_pairs(sf, /):
        e2r = sf.幂次讠重数
        return tuple(sorted(e2r.items()))
    @cached_property
    def _h(sf, /):
        e_r_pairs = sf._e_r_pairs
        return hash(e_r_pairs)
    @classmethod
    def 巛文本扌(cls, 文本冃瓧称重式, /):
        return _巛文本扌(cls, 解读冫瓧称重式巛文本表达扌, 文本冃瓧称重式)
    def __str__(sf, /):
        文本冃瓧称重式 = 表述冫瓧称重式讠文本表达扌(瓧称重式:=sf, 欤校验=True)
        return 文本冃瓧称重式
    def __repr__(sf, /):
        e2r = sf._e2r
        return f'乸瓧称重式({e2r})'
    def __hash__(sf, /):
        return sf._h
    def __eq__(sf, ot, /):
        if sf is ot:return True
        return type(sf) is type(ot) and sf._e_r_pairs == ot._e_r_pairs
    def __le__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return sf._e_r_pairs <= ot._e_r_pairs

    def eval(sf, 序列纟变量值, /, *, 鬽缓存冃变量号讠幂次讠幂方=None):
        变量号讠变量值 = mk_tuple(序列纟变量值)
        777;del 序列纟变量值
        if len(变量号讠变量值) < sf.变量数:
            return 0
        if len(变量号讠变量值) == 0:
            return 1
        #.acc = 1
        #.for 中选变量值集 in combinations(变量号讠变量值, sf.变量数):
        #.    for 幂次, 重数 in sf.幂次讠重数.items():
        #.        ... ...
        #########
        (严序加链纟幂次, kmm2ji) = sf._相关数据纟加链纟幂次
        加链 = 严序加链纟幂次
        def 填充冫幂次讠幂方巛变量值扌(幂次讠幂方, 变量值, /):
            if not 1 in 幂次讠幂方:
                幂次讠幂方[1] = 变量值
            else:
                if not 幂次讠幂方[1] == 变量值:raise ValueError
            for k, (j, i) in enumerate(kmm2ji, 1):
                if not 加链[k] in 幂次讠幂方:
                    幂次讠幂方[加链[k]] = 幂次讠幂方[加链[j]] * 幂次讠幂方[加链[i]]
            return
        #def 构造冫幂次讠幂方巛变量值扌(变量值, /):
        #    幂次讠幂方 = {1:变量值}
        #    for k, (j, i) in enumerate(kmm2ji, 1):
        #        幂次讠幂方[加链[k]] = 幂次讠幂方[加链[j]] * 幂次讠幂方[加链[i]]
        #    return 幂次讠幂方
        #变量号讠幂次讠幂方 = [*map(构造冫幂次讠幂方巛变量值扌, 变量号讠变量值)]
        变量号讠幂次讠幂方 = _缓存巛鬽缓存冃变量号讠幂次讠幂方扌(len(变量号讠变量值), 鬽缓存冃变量号讠幂次讠幂方)
        for _ in map(填充冫幂次讠幂方巛变量值扌, 变量号讠幂次讠幂方, 变量号讠变量值):pass
        #########
        def main():
            入选数 = sf.变量数
            候选数 = len(变量号讠变量值)
            位置讠幂次 = sf._位置讠幂次
            #.it = 排列组合牜泛型牜树状遍历扌(候选数, 入选数, sf._未规范泛型拆分表纟入选数)
            it = 排列组合牜指定次序牜树状遍历扌(候选数, 入选数, sf._位置讠毝更小位置纟更小入选值)
            栈纟累积值 = [1]
            累计值 = 0
            for (单步况态, 已入选名单) in it:
                match 单步况态:
                    case 0:
                        累计值 += 栈纟累积值[-1]

                    case 1:
                        当前位置 = -1+len(已入选名单)
                        变量号 = 已入选名单[当前位置]
                        幂次 = 位置讠幂次[当前位置]
                        幂方 = 变量号讠幂次讠幂方[变量号][幂次]
                        栈纟累积值.append(栈纟累积值[-1]*幂方)
                    case -1:
                        栈纟累积值.pop()
                    case _:
                        raise 000
                    #case
            assert 栈纟累积值 == [1]
            累计值
            return 累计值
        #end-def main():
        #########
        return main()
    @cached_property
    def _列表纟幂次辻重数(sf, /):
        列表纟幂次辻重数 = tuple(sorted(sf.幂次讠重数.items()))
        return 列表纟幂次辻重数
    @cached_property
    def _位置讠幂次(sf, /):
        列表纟幂次辻重数 = sf._列表纟幂次辻重数
        位置讠幂次 = tuple(幂次 for 幂次, 重数 in 列表纟幂次辻重数 for _ in range(重数))
        return 位置讠幂次
    @cached_property
    def _位置讠毝更小位置纟更小入选值(sf, /):
        入选数 = sf.变量数
        位置讠毝更小位置纟更小入选值 = 预备冫参数纟排列组合牜泛型牜树状遍历扌(入选数, sf._未规范泛型拆分表纟入选数)
        return 位置讠毝更小位置纟更小入选值
    @cached_property
    def _未规范泛型拆分表纟入选数(sf, /):
        列表纟幂次辻重数 = sf._列表纟幂次辻重数
        序列纟组合小块 = (重数 for 幂次, 重数 in 列表纟幂次辻重数)
        未规范泛型拆分表纟入选数 = 未规范排列大区 = (6.5, *序列纟组合小块)
        return 未规范泛型拆分表纟入选数
    @cached_property
    def _相关数据纟加链纟幂次(sf, /):
        #.最高幂次 = 位置讠幂次[-1] if 位置讠幂次 else 0
        幂次集 = sf.幂次讠重数.keys()
        严序加链纟幂次 = 构造冫加靶链牜加辗链构造式扌(幂次集)
        kmm2ji = 松序加链讠址引减一讠最大最小加数址引扌(严序加链纟幂次)
        return (严序加链纟幂次, kmm2ji)



class 乸瓧称组式(_乸全序):
    '瓧称组式=多项式耂加型对称化多项式(瓧称重式讠系数)'
    def __init__(sf, 瓧称重式讠系数, /):
        e2rZc = 瓧称重式讠系数 = {**瓧称重式讠系数}
        for 瓧称重式 in 瓧称重式讠系数.keys():
            check_type_is(乸瓧称重式, 瓧称重式)
        for 系数 in 瓧称重式讠系数.values():
            检查冫系数扌(系数)
        sf._e2rZc = 瓧称重式讠系数
    @property
    def 瓧称重式讠系数(sf, /):
        return mk_MapView(sf._e2rZc)
    @cached_property
    def 最小变量数(sf, /):
        return min((瓧称重式.变量数 for 瓧称重式 in sf.瓧称重式讠系数), default=0)
    @cached_property
    def 最大变量数(sf, /):
        return max((瓧称重式.变量数 for 瓧称重式 in sf.瓧称重式讠系数), default=0)
    @cached_property
    def _e2r_c_pairs(sf, /):
        e2rZc = sf.瓧称重式讠系数
        return tuple(sorted(e2rZc.items()))
    @cached_property
    def _h(sf, /):
        e2r_c_pairs = sf._e2r_c_pairs
        return hash(e2r_c_pairs)
    @classmethod
    def 巛文本扌(cls, 文本冃瓧称组式, /):
        return _巛文本扌(cls, 解读冫瓧称组式巛文本表达扌, 文本冃瓧称组式)
        #.check_type_is(str, 文本冃瓧称组式)
        #.(瓧称组式, 讫址) = 解读冫瓧称组式巛文本表达扌(文本冃瓧称组式, 0, len(文本冃瓧称组式))
        #.if not 讫址 == len(文本冃瓧称组式):raise FormatError('多余尾部:', 文本冃瓧称组式[讫址:讫址+100])
        #.check_type_is(cls, 瓧称组式)
        #.return 瓧称组式
    def __str__(sf, /):
        文本冃瓧称组式 = 表述冫瓧称组式讠文本表达扌(瓧称组式:=sf, 欤校验=True)
        return 文本冃瓧称组式
    def __repr__(sf, /):
        e2rZc = sf._e2rZc
        return f'乸瓧称组式({e2rZc})'
    def __hash__(sf, /):
        return sf._h
    def __eq__(sf, ot, /):
        if sf is ot:return True
        return type(sf) is type(ot) and sf._e2r_c_pairs == ot._e2r_c_pairs
    def __le__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return sf._e2r_c_pairs <= ot._e2r_c_pairs

    def eval(sf, 序列纟变量值, /, *, 鬽缓存冃变量号讠幂次讠幂方=None):
        变量号讠变量值 = mk_tuple(序列纟变量值)
        777;del 序列纟变量值
        if len(变量号讠变量值) < sf.最小变量数:
            return 0
        变量号讠幂次讠幂方 = _缓存巛鬽缓存冃变量号讠幂次讠幂方扌(len(变量号讠变量值), 鬽缓存冃变量号讠幂次讠幂方)
        return sum(瓧称重式.eval(变量号讠变量值, 鬽缓存冃变量号讠幂次讠幂方=变量号讠幂次讠幂方)*系数 for 瓧称重式, 系数 in sf.瓧称重式讠系数.items())

def _缓存巛鬽缓存冃变量号讠幂次讠幂方扌(候选数, 鬽缓存冃变量号讠幂次讠幂方, /):
    if None is 鬽缓存冃变量号讠幂次讠幂方:
        变量号讠幂次讠幂方 = [{} for _ in range(候选数)]
    else:
        变量号讠幂次讠幂方 = 鬽缓存冃变量号讠幂次讠幂方
    变量号讠幂次讠幂方
    assert len(变量号讠幂次讠幂方) == 候选数 #len(变量号讠变量值)
    return 变量号讠幂次讠幂方

def 检查冫系数扌(系数, /):
    if 系数 == 0:raise ValueError(系数)
    if not 0*系数 == 0:raise ValueError(系数)
    if not 1*系数 == 系数:raise ValueError(系数)
    if not -1*系数 == -系数:raise ValueError(系数)
    if not 系数:raise ValueError(系数)


def _巛文本扌(cls, 解读扌, 文本冃囜式, /):
    check_type_is(str, 文本冃囜式)
    (囜式, 讫址) = 解读扌(文本冃囜式, 0, len(文本冃囜式))
    if not 讫址 == len(文本冃囜式):raise FormatError('多余尾部:', 文本冃囜式[讫址:讫址+100])
    check_type_is(cls, 囜式)
    return 囜式
class 乸文件冃缓存冃瓧称重式讠础称组式(MutableMapping):
    'iobfile -> 缓存冃瓧称重式讠础称组式'
    def __init__(sf, iobfile, /):
        assert iobfile.tell() == 0
        #assert iobfile.read(0) == b''
        加载冫缓存冃瓧称重式讠础称组式巛文件扌(缓存冃瓧称重式讠础称组式:={}, iobfile)
        sf._d = 缓存冃瓧称重式讠础称组式
        sf._io = iobfile
    def __len__(sf, /):
        return len(sf._d)
    def __iter__(sf, /):
        return iter(sf._d)
    def __delitem__(sf, k, /):
        check_type_is(乸瓧称重式, k)
        raise NotImplementedError('乸文件冃缓存冃瓧称重式讠础称组式.__delitem__')
    def __getitem__(sf, k, /):
        check_type_is(乸瓧称重式, k)
        v = sf._d[k]
        #check_type_is(乸础称组式, v)
        return v
    def __setitem__(sf, k, v, /):
        check_type_is(乸瓧称重式, k)
        check_type_is(乸础称组式, v)
        d = sf._d
        if not None is (_v:=d.get(k)):
            if not _v == v:raise Exception('__setitem__:重复键不同靶', k, _v, v)
        else:
            s = f'{k!s}:{v!s}\n'
            bs = s.encode('ascii')
            obfile = sf._io
            obfile.write(bs)
            #obfile.flush()
            d[k] = v

def 加载冫缓存冃瓧称重式讠础称组式巛文件扌(缓存冃瓧称重式讠础称组式, ibfile, /):
    for line in ibfile:
        if not line[-1:] == b'\n':raise FormatError
        line = line.decode('ascii')
        line = line.strip()
        (文本冃瓧称重式, 文本冃础称组式) = line.split(':')
        瓧称重式 = 乸瓧称重式.巛文本扌(文本冃瓧称重式)
        础称组式 = 乸础称组式.巛文本扌(文本冃础称组式)
        _础称组式 = 缓存冃瓧称重式讠础称组式.setdefault(瓧称重式, 础称组式)
        if not _础称组式 == 础称组式:raise Exception('加载:重复键不同靶', 文本冃瓧称重式, _础称组式, 础称组式)
def 枚举冫瓧称重式巛自然数牜整数拆分扌(自然数, /):
    'uint -> Iter 瓧称重式'
    check_int_ge(0, 自然数)
    it = uint2iter_uint_partitions_(自然数, to_expand=False)
    for pairs in it:
        幂次讠重数 = dict(pairs)
        瓧称重式 = 乸瓧称重式(幂次讠重数)
        yield 瓧称重式
def 枚举冫瓧称重式辻础称组式巛自然数牜整数拆分扌(缓存冃瓧称重式讠础称组式, 自然数, /, *, 欤随机数值校验丨随机数值串生成器=False, 欤文本版=False):
    '缓存冃瓧称重式讠础称组式/{瓧称重式{e2r}:础称组式{k2eZc}} -> uint -> (Iter (瓧称重式, 础称组式)) if not 欤文本版 else (Iter str/f"{瓧称重式!s}:{础称组式!s}")'
    for 瓧称重式 in 枚举冫瓧称重式巛自然数牜整数拆分扌(自然数):
        础称组式 = 瓧称重式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称重式, 欤随机数值校验丨随机数值串生成器=欤随机数值校验丨随机数值串生成器)
        yield (瓧称重式, 础称组式) if not 欤文本版 else f'{瓧称重式!s}:{础称组式!s}'
def 枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分扌(缓存冃瓧称重式讠础称组式, 序列纟自然数, /, *, 欤随机数值校验丨随机数值串生成器=False, 欤文本版=False):
    '缓存冃瓧称重式讠础称组式/{瓧称重式{e2r}:础称组式{k2eZc}} -> Iter uint -> (Iter (瓧称重式, 础称组式)) if not 欤文本版 else (Iter str/f"{瓧称重式!s}:{础称组式!s}")'
    for 自然数 in 序列纟自然数:
        yield from 枚举冫瓧称重式辻础称组式巛自然数牜整数拆分扌(缓存冃瓧称重式讠础称组式, 自然数, 欤随机数值校验丨随机数值串生成器=欤随机数值校验丨随机数值串生成器, 欤文本版=欤文本版)
def 枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分牜缓存文件扌(文件路径冃缓存冃瓧称重式讠础称组式, 序列纟自然数, /, *, 欤随机数值校验丨随机数值串生成器=False, 欤文本版=False):
    'path -> Iter uint -> (Iter (瓧称重式, 础称组式)) if not 欤文本版 else (Iter str/f"{瓧称重式!s}:{础称组式!s}")'
    序列纟自然数 = iter(序列纟自然数)
    #with open(文件路径冃缓存冃瓧称重式讠础称组式, 'r+b') as iobfile:
        #FileNotFoundError:
    with open(文件路径冃缓存冃瓧称重式讠础称组式, 'a+b') as iobfile:
        end = iobfile.tell()
        iobfile.seek(0)
        缓存冃瓧称重式讠础称组式 = 乸文件冃缓存冃瓧称重式讠础称组式(iobfile)
        if not end == iobfile.tell():raise Exception(end, iobfile.tell())
        yield from 枚举冫瓧称重式辻础称组式巛序列纟自然数牜整数拆分扌(缓存冃瓧称重式讠础称组式, 序列纟自然数, 欤随机数值校验丨随机数值串生成器=欤随机数值校验丨随机数值串生成器, 欤文本版=欤文本版)



def 瓧称组式讠础称组式牜文本版扌(缓存冃瓧称重式讠础称组式, 文本冃瓧称组式, /, *, 欤随机数值校验丨随机数值串生成器=False):
    '缓存冃瓧称重式讠础称组式/{瓧称重式{e2r}:础称组式{k2eZc}} -> 文本{瓧称组式{e2rZc}} -> 文本{础称组式{k2eZc}}'
    #.check_type_is(str, 文本冃瓧称组式)
    #.(瓧称组式, 讫址) = 解读冫瓧称组式巛文本表达扌(文本冃瓧称组式, 0, len(文本冃瓧称组式))
    #.if not 讫址 == len(文本冃瓧称组式):raise FormatError('多余尾部:', 文本冃瓧称组式[讫址:讫址+100])
    瓧称组式 = 乸瓧称组式.巛文本扌(文本冃瓧称组式)
    础称组式 = 瓧称组式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称组式, 欤随机数值校验丨随机数值串生成器=欤随机数值校验丨随机数值串生成器)
    #文本冃础称组式 = 表述冫础称组式讠文本表达扌(础称组式, 欤校验=True)
    文本冃础称组式 = str(础称组式)
    return 文本冃础称组式

def 瓧称重式讠础称组式牜文本版扌(缓存冃瓧称重式讠础称组式, 文本冃瓧称重式, /, *, 欤随机数值校验丨随机数值串生成器=False):
    '缓存冃瓧称重式讠础称组式/{瓧称重式{e2r}:础称组式{k2eZc}} -> 文本{瓧称重式{e2r}} -> 文本{础称组式{k2eZc}}'
    #.check_type_is(str, 文本冃瓧称重式)
    #.(瓧称重式, 讫址) = 解读冫瓧称重式巛文本表达扌(文本冃瓧称重式, 0, len(文本冃瓧称重式))
    #.if not 讫址 == len(文本冃瓧称重式):raise FormatError('多余尾部:', 文本冃瓧称重式[讫址:讫址+100])
    瓧称重式 = 乸瓧称重式.巛文本扌(文本冃瓧称重式)
    础称组式 = 瓧称重式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称重式, 欤随机数值校验丨随机数值串生成器=欤随机数值校验丨随机数值串生成器)
    #文本冃础称组式 = 表述冫础称组式讠文本表达扌(础称组式, 欤校验=True)
    文本冃础称组式 = str(础称组式)
    return 文本冃础称组式


def 瓧称组式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称组式, /, *, 欤随机数值校验丨随机数值串生成器=False):
    '缓存冃瓧称重式讠础称组式/{瓧称重式{e2r}:础称组式{k2eZc}} -> 瓧称组式{e2rZc} -> 础称组式{k2eZc}'
    础称组式 = flatten_recur(_瓧称组式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称组式))
    随机数值校验牜瓧称组式扌(欤随机数值校验丨随机数值串生成器, 础称组式, 瓧称组式)
    return 础称组式
def 瓧称重式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称重式, /, *, 欤随机数值校验丨随机数值串生成器=False):
    '缓存冃瓧称重式讠础称组式/{瓧称重式{e2r}:础称组式{k2eZc}} -> 瓧称重式{e2r} -> 础称组式{k2eZc}'
    sz0 = len(缓存冃瓧称重式讠础称组式)
    础称组式 = flatten_recur(_瓧称重式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称重式))
    sz1 = len(缓存冃瓧称重式讠础称组式)
    if not sz1 == sz0:
        随机数值校验牜瓧称重式扌(欤随机数值校验丨随机数值串生成器, 础称组式, 瓧称重式)
    return 础称组式

class ValidateFail(Exception):pass
def 随机数值校验牜瓧称重式扌(欤随机数值校验丨随机数值串生成器, 础称组式, 瓧称重式, /):
    #最大变量数 = 瓧称重式.变量数
    随机数值校验牜瓧称囜式扌(欤随机数值校验丨随机数值串生成器, 础称组式, 瓧称重式)
def 随机数值校验牜瓧称组式扌(欤随机数值校验丨随机数值串生成器, 础称组式, 瓧称组式, /):
    #最大变量数 = 瓧称组式.最大变量数
    随机数值校验牜瓧称囜式扌(欤随机数值校验丨随机数值串生成器, 础称组式, 瓧称组式)
def 随机数值校验牜瓧称囜式扌(欤随机数值校验丨随机数值串生成器, 础称组式, 瓧称囜式, /):
    if not 础称组式.最小变量数 == 瓧称囜式.最小变量数:raise ValidateFail('数值校验失败:', 础称组式, 瓧称囜式, (础称组式.最小变量数, 瓧称囜式.最小变量数))

    if type(欤随机数值校验丨随机数值串生成器) is bool:
        欤随机数值校验 = 欤随机数值校验丨随机数值串生成器
        if not 欤随机数值校验:
            return
        趃生成冫随机数值串扌 = _趃生成冫随机数值串扌
    elif callable(欤随机数值校验丨随机数值串生成器):
        趃生成冫随机数值串扌 = 欤随机数值校验丨随机数值串生成器
    else:
        raise TypeError(type(欤随机数值校验丨随机数值串生成器), [bool, callable])
    趃生成冫随机数值串扌
    最小变量数 = min(础称组式.最小变量数, 瓧称囜式.最小变量数)
    最大变量数 = max(础称组式.最大变量数, 瓧称囜式.最大变量数)
    for 变量号讠变量值 in 趃生成冫随机数值串扌(最小变量数, 最大变量数):
        #鬽缓存冃变量号讠幂次讠幂方
        #鬽缓存冃变量数讠幂次讠幂方
        if not (r0:=础称组式.eval(变量号讠变量值)) == (r1:=瓧称囜式.eval(变量号讠变量值)):raise ValidateFail('数值校验失败:', 础称组式, 瓧称囜式, 变量号讠变量值, (r0, r1))
def _趃生成冫随机数值串扌(最小变量数, 最大变量数, /):
    '最小变量数 -> 最大变量数 -> Iter 变量号讠变量值/[(int|Fraction)]{len=变量数}'
    变量号讠变量值 = tuple(accumulate(randint(2, 100) for _ in range(3+最大变量数)))
    yield 变量号讠变量值
    return


def _累加冫础称组式扌(础称乘式讠系数, 系数, 础称组式, /):
    for 础称乘式, c in 础称组式.础称乘式讠系数.items():
        c *= 系数
        _累加扌(础称乘式讠系数, 础称乘式, c)
def _累加扌(d, k, v, /):
    if v == 0:
        return
    if not None is (_v:=d.get(k)):
        v += _v
        if v == 0:
            del d[k]
            return
        v
    else:
        v
    v
    d[k] = v

def _瓧称组式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称组式, /):
    础称乘式讠系数 = {}
    for 瓧称重式, 系数 in 瓧称组式.瓧称重式讠系数.items():
        础称组式 = yield _瓧称重式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称重式)
        _累加冫础称组式扌(础称乘式讠系数, 系数, 础称组式)
    础称组式 = 乸础称组式(础称乘式讠系数)
    return 础称组式

def _瓧称重式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称重式, /):
    if not None is (础称组式:=缓存冃瓧称重式讠础称组式.get(瓧称重式)):
        return 础称组式
    k = 瓧称重式.变量数
    e2r = 瓧称重式.幂次讠重数
    if not e2r:
        # == 1
        assert k == 0
        础称组式 = 乸础称组式({乸础称乘式({}):1})
    elif 1 == (max_e:=max(e2r)):
        match [*e2r.items()]:
            case [(1, r)]:
                assert k == r >= 1
            case _:
                raise 000
        础称组式 = 乸础称组式({乸础称乘式({乸础称平式(k):1}):1})
    else:
        assert max_e >= 2
        assert k >= 1
        (础称平式牜白噪声, 瓧称重式牜降一, 瓧称组式冃残差) = _拆分冫瓧称重式扌(k, e2r, 瓧称重式)
        础称组式 = yield _组合冫础称组式扌(缓存冃瓧称重式讠础称组式, 础称平式牜白噪声, 瓧称重式牜降一, 瓧称组式冃残差)
    础称组式
    777;check_type_is(乸础称组式, 础称组式)
    777;缓存冃瓧称重式讠础称组式[瓧称重式] = 础称组式
    础称组式 = yield _瓧称重式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称重式)
    return 础称组式


def _拆分冫瓧称重式扌(k, e2r, 瓧称重式, /):
    础称平式牜白噪声 = 乸础称平式(k)
    # [(?,?) := 瓧称重式/%础称平式牜白噪声]
    emm2r = {e-1:r for e, r in e2r.items() if not e == 1}
    瓧称重式牜降一 = 乸瓧称重式(emm2r)
    # [? := 瓧称重式 -础称平式牜白噪声*瓧称重式牜降一]
    # [r[e] == r0[e]/保高 + r1[e]/升一]
    # [r[e-1] == r0[e-1]/保高 + r1[e-1]/升一]
    #   r0[e] 已经处理过
    #   r1[e]+r0[e-1] 混合为 r'[e-1] => C(r'[e-1]; r1[e])
    #       [r1[e] := r[e] -r0[e]]
    #       [r0[e-1] := r'[e-1] -r1[e]]
    def put(_e_rs_pairs, e, r, /):
        if e == 0 or r == 0:
            return
        if _e_rs_pairs and e == _e_rs_pairs[-1][0]:
            _e_rs_pairs[-1][1].append(r)
            return
        _e_rs_pairs.append((e, [r]))
        return
    k
    emm_r_pairs = 瓧称重式牜降一._e_r_pairs
        #emm2r
    _rs4emm = tuple(map(snd, emm_r_pairs))
    _k = 瓧称重式牜降一.变量数
    assert _k == sum(_rs4emm) # 变量数
    diff4k = e2r.get(1, 0) #降一时沉没数
    assert k == _k + diff4k # 变量数
    瓧称重式讠系数 = {}
        #应当看作 从emm2r选择性升一...
    for j2r0 in product(*[range(1+r) for r in _rs4emm]):
        sz4uncover = sum(j2r0)
        if sz4uncover == 0:
            #全升一
            #xxx:assert j2r0 == _rs4emm
            continue
        _e_rs_pairs = []
            #as残差
        put(_e_rs_pairs, 1, diff4k+sz4uncover)
            #not:(_k-k7used)
        for (emm, r), r0 in zip(emm_r_pairs, j2r0):
            #r0:保高
            #r1:升一
            r1 = r -r0
            e = emm+1
            put(_e_rs_pairs, emm, r0)
            put(_e_rs_pairs, e, r1)
        _e_rs_pairs
        _e_r_pairs = tuple((e, sum(rs)) for e, rs in _e_rs_pairs)
        _e2r = dict(_e_r_pairs)
        瓧称重式冃部分残差 = 乸瓧称重式(_e2r)
        coeff = -II(C(sum(rs), rs[0]) for e, rs in _e_rs_pairs)
        #if coeff == -1:
        _累加冫瓧称组式扌(瓧称重式讠系数, coeff, 瓧称重式冃部分残差)
    瓧称重式讠系数
    瓧称组式冃残差 = 乸瓧称组式(瓧称重式讠系数)
    return (础称平式牜白噪声, 瓧称重式牜降一, 瓧称组式冃残差)
def _累加冫瓧称组式扌(瓧称重式讠系数, 系数, 瓧称重式, /):
    dict_add__new(瓧称重式讠系数, 瓧称重式, 系数)

def _组合冫础称组式扌(缓存冃瓧称重式讠础称组式, 础称平式牜白噪声, 瓧称重式牜降一, 瓧称组式冃残差, /):
    础称组式牜降一 = yield _瓧称重式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称重式牜降一)
    础称组式冃残差 = yield _瓧称组式讠础称组式扌(缓存冃瓧称重式讠础称组式, 瓧称组式冃残差)
    # [? := 础称平式牜白噪声*础称组式牜降一 + 础称组式冃残差]
    础称乘式讠系数 = _乘冫础称平式丶础称组式扌(础称平式牜白噪声,础称组式牜降一)
    _累加冫础称组式扌(础称乘式讠系数, 系数:=1, 础称组式冃残差)
    础称组式 = 乸础称组式(础称乘式讠系数)
    return 础称组式
    777;yield


def _乘冫础称平式丶础称乘式扌(础称平式, 础称乘式, /):
    础称平式讠幂次 = {**础称乘式.础称平式讠幂次}
    _累加扌(础称平式讠幂次, 础称平式, 1)
    础称乘式 = 乸础称乘式(础称平式讠幂次)
    return 础称乘式
def _乘冫础称平式丶础称组式扌(础称平式, 础称组式, /):
    础称乘式讠系数 = {_乘冫础称平式丶础称乘式扌(础称平式, 础称乘式):系数 for 础称乘式, 系数 in 础称组式.础称乘式讠系数.items()}
    return 础称乘式讠系数




################
#文本化:
def 表述冫础称平式讠文本表达扌(础称平式, /, *, 欤校验=False):
    return _表述牜校验扌(欤校验, _表述冫础称平式讠文本表达扌, 解读冫础称平式巛文本表达扌, 础称平式)
def _表述冫础称平式讠文本表达扌(础称平式, /):
    变量数 = 础称平式.变量数
    return 'I' if 变量数==0 else f'w{变量数}'

def 表述冫础称乘式讠文本表达扌(础称乘式, /, *, 欤校验=False):
    return _表述牜校验扌(欤校验, _表述冫础称乘式讠文本表达扌, 解读冫础称乘式巛文本表达扌, 础称乘式)
def _表述冫础称乘式讠文本表达扌(础称乘式, /):
    础称平式讠幂次 = 础称乘式.础称平式讠幂次
    if not 础称平式讠幂次:
        return 'I'
    def __():
        for 础称平式, 幂次 in sorted(础称平式讠幂次.items()):
            wNNN = 表述冫础称平式讠文本表达扌(础称平式)
            smay_vNNN = f'v{幂次}' if not 幂次 == 1 else ''
            yield wNNN + smay_vNNN
    return 'X'.join(__())

def 表述冫础称组式讠文本表达扌(础称组式, /, *, 欤校验=False):
    '础称组式 -> 文本冃础称组式/str'
    return _表述牜校验扌(欤校验, _表述冫础称组式讠文本表达扌, 解读冫础称组式巛文本表达扌, 础称组式)
    #.文本冃础称组式 = _表述冫础称组式讠文本表达扌(础称组式)
    #.if 欤校验:
    #.    (_础称组式, 讫址) = 解读冫础称组式巛文本表达扌(文本冃础称组式, 0, len(文本冃础称组式))
    #.    if not 讫址 == len(文本冃础称组式):raise Exception(础称组式, 文本冃础称组式, 文本冃础称组式[讫址:])
    #.    if not _础称组式 == 础称组式:raise Exception(础称组式, 文本冃础称组式, _础称组式)
    #.return 文本冃础称组式
def _表述牜校验扌(欤校验, _表述扌, 解读扌, 囜式, /):
    文本冃囜式 = _表述扌(囜式)
    if 欤校验:
        try:
            (_囜式, 讫址) = 解读扌(文本冃囜式, 0, len(文本冃囜式))
        except FormatError as exc:
            raise Exception(囜式, 文本冃囜式, exc)
        if not 讫址 == len(文本冃囜式):raise Exception(囜式, 文本冃囜式, 文本冃囜式[讫址:])
        if not _囜式 == 囜式:raise Exception(囜式, 文本冃囜式, _囜式)
    return 文本冃囜式
def _表述冫础称组式讠文本表达扌(础称组式, /):
    '础称组式 -> 文本冃础称组式/str'
    础称乘式讠系数 = 础称组式.础称乘式讠系数
    if not 础称乘式讠系数:
        return 'O'
    def __():
        for 础称乘式, 非零系数 in sorted(础称乘式讠系数.items()):
            sc = 表述冫非零系数讠文本表达扌(非零系数)
            sm = 表述冫础称乘式讠文本表达扌(础称乘式)
            if sm == 'I':
                sm = ''
            yield f'k{sc}{sm}'
    return ''.join(__())

def 表述冫非零系数讠文本表达扌(非零系数, /, *, 欤校验=False):
    return _表述牜校验扌(欤校验, _表述冫非零系数讠文本表达扌, 解读冫非零系数巛文本表达扌, 非零系数)
def _表述冫非零系数讠文本表达扌(非零系数, /):
    (分子, 分母) = 非零系数.as_integer_ratio()
    if 分子 == 0:raise TypeError
    sign = 'dp'[分子 > 0]
    分子 = abs(分子)
    sN = '' if 分子 == 1 else str(分子)
    sD = '' if 分母 == 1 else f'J{分母}'
    return f'{sign}{sN}{sD}'


def 表述冫瓧称重式讠文本表达扌(瓧称重式, /, *, 欤校验=False):
    return _表述牜校验扌(欤校验, _表述冫瓧称重式讠文本表达扌, 解读冫瓧称重式巛文本表达扌, 瓧称重式)
def _表述冫瓧称重式讠文本表达扌(瓧称重式, /):
    幂次讠重数 = 瓧称重式.幂次讠重数
    if not 幂次讠重数:
        return 'I'
    def __():
        for 幂次, 重数 in sorted(幂次讠重数.items()):
            eNNN = f'e{幂次}'
            smay_rNNN = f'r{重数}' if not 重数 == 1 else ''
            yield eNNN + smay_rNNN
    return 'X'.join(__())


def 表述冫瓧称组式讠文本表达扌(瓧称组式, /, *, 欤校验=False):
    return _表述牜校验扌(欤校验, _表述冫瓧称组式讠文本表达扌, 解读冫瓧称组式巛文本表达扌, 瓧称组式)
def _表述冫瓧称组式讠文本表达扌(瓧称组式, /):
    瓧称重式讠系数 = 瓧称组式.瓧称重式讠系数
    if not 瓧称重式讠系数:
        return 'O'
    def __():
        for 瓧称重式, 非零系数 in sorted(瓧称重式讠系数.items()):
            sc = 表述冫非零系数讠文本表达扌(非零系数)
            sm = 表述冫瓧称重式讠文本表达扌(瓧称重式)
            if sm == 'I':
                sm = ''
            yield f'k{sc}{sm}'
    return ''.join(__())


表述冫础称平式讠文本表达扌
表述冫础称乘式讠文本表达扌
表述冫础称组式讠文本表达扌
表述冫非零系数讠文本表达扌
表述冫瓧称重式讠文本表达扌
表述冫瓧称组式讠文本表达扌

################
_ptn4NNN = r'(?:[1-9][0-9]*)'
_ptn4wNNN = fr'(?:w{_ptn4NNN})'
_ptn4vNNN = fr'(?:v{_ptn4NNN})'
_ptn4eNNN = fr'(?:e{_ptn4NNN})'
_ptn4rNNN = fr'(?:r{_ptn4NNN})'
_ptn4kdpNNN = fr'(?:k[dp]{_ptn4NNN}?)'
_ptn4JNNN = fr'(?:J{_ptn4NNN})'

_ptn4wNNNvNNN = fr'(?:{_ptn4wNNN}{_ptn4vNNN}?)'
_ptn4eNNNrNNN = fr'(?:{_ptn4eNNN}{_ptn4rNNN}?)'
_ptn4kdpNNNJNNN = fr'(?:{_ptn4kdpNNN}{_ptn4JNNN}?)'

_ptn4wNNNvNNNX = fr'(?:{_ptn4wNNNvNNN}(?:X{_ptn4wNNNvNNN})*)'
_ptn4eNNNrNNNX = fr'(?:{_ptn4eNNNrNNN}(?:X{_ptn4eNNNrNNN})*)'
_ptn4I_wNNNvNNNX = fr'(?:I|{_ptn4wNNNvNNNX})'
_ptn4I_eNNNrNNNX = fr'(?:I|{_ptn4eNNNrNNNX})'
_ptn4kdpNNNJNNNwNNNvNNNX = fr'(?:{_ptn4kdpNNNJNNN}{_ptn4I_wNNNvNNNX}?)'
_ptn4kdpNNNJNNNeNNNrNNNX = fr'(?:{_ptn4kdpNNNJNNN}{_ptn4I_eNNNrNNNX}?)'
_ptn4O_kdpNNNJNNNwNNNvNNNXXkk = fr'(?:O|{_ptn4kdpNNNJNNNwNNNvNNNX}+)'
_ptn4O_kdpNNNJNNNeNNNrNNNXXkk = fr'(?:O|{_ptn4kdpNNNJNNNeNNNrNNNX}+)'

_rgx4wNNN = re.compile(_ptn4wNNN)
_rgx4I_wNNNvNNNX = re.compile(_ptn4I_wNNNvNNNX)
_rgx4I_eNNNrNNNX = re.compile(_ptn4I_eNNNrNNNX)
_rgx4O_kdpNNNJNNNwNNNvNNNXXkk = re.compile(_ptn4O_kdpNNNJNNNwNNNvNNNXXkk)
_rgx4O_kdpNNNJNNNeNNNrNNNXXkk = re.compile(_ptn4O_kdpNNNJNNNeNNNrNNNXXkk)

class FormatError(Exception):pass

def 取冫彣首字符巛文本扌(文本, 起址, 讫址, /):
    '-> 彣 首字符 # smay char'
    return 文本[起址:min(1+起址,讫址)]
def 取冫首字符巛文本扌(文本, 起址, 讫址, /):
    '-> 首字符 | ^EOFError'
    match 取冫彣首字符巛文本扌(文本, 起址, 讫址):
        case '':
            raise EOFError(起址, 讫址, 文本[-20+起址:+20+讫址])
        case 首字符:
            pass
        #case
    #检查冫首字符扌(首字符)
    return 首字符
def 取查冫首字符巛文本扌(合法字符集丨检查冫首字符扌, 文本, 起址, 讫址, /):
    '-> 首字符 | ^EOFError | ^FormatError{合法字符集} | ^Exception{检查冫首字符扌}'
    首字符 = 取冫首字符巛文本扌(文本, 起址, 讫址)
    if callable(合法字符集丨检查冫首字符扌):
        检查冫首字符扌 = 合法字符集丨检查冫首字符扌
        检查冫首字符扌(首字符)
            # ^Exception{检查冫首字符扌}
    else:
        合法字符集 = 合法字符集丨检查冫首字符扌
        if not 首字符 in 合法字符集:raise FormatError(合法字符集, 首字符)
    return 首字符

def 解读冫正整数巛文本表达扌(文本, 起址, 讫址, /, *, 欤返回零乊失败:bool):
    '-> (正整数|^Exception) if not 欤返回零乊失败 else (0/失败|正整数)/uint'
    if not 欤返回零乊失败:
        取查冫首字符巛文本扌('123456789', 文本, 起址, 讫址)
    else:
        彣首字符 = 取冫彣首字符巛文本扌(文本, 起址, 讫址)
        if not (彣首字符 and 彣首字符 in '123456789'):
            讫址 = 起址
            return (0, 讫址)

    for j in range(起址, 讫址):
        ch = 文本[j]
        if not ch.isdigit():
            讫址 = j
            break
    else:
        讫址 # len(文本)
    讫址
    s = 文本[起址:讫址]
    assert s
    #if not s: return (0, 讫址)
    u = int(s)
    assert u > 0
    return (u, 讫址)
def 解读冫非零有理数巛文本表达扌(文本, 起址, 讫址, /, *, 欤返回零乊失败:bool):
    '-> (非零有理数|^Exception) if not 欤返回零乊失败 else (0/失败|非零有理数)/uint'
    if not 欤返回零乊失败:
        取查冫首字符巛文本扌('dp', 文本, 起址, 讫址)
    else:
        彣首字符 = 取冫彣首字符巛文本扌(文本, 起址, 讫址)
        if not (彣首字符 and 彣首字符 in 'dp'):
            讫址 = 起址
            return (0, 讫址)


    dp = 文本[起址]
    777;起址 += 1
    正负号 = -1 if dp == 'd' else +1

    (分子, 起址) = 解读冫正整数巛文本表达扌(文本, 起址, 讫址, 欤返回零乊失败=True)
    if not 分子:
        分子 = 1
    分子 *= 正负号
    if 取冫彣首字符巛文本扌(文本, 起址, 讫址) == 'J':
        (分母, 起址) = 解读冫正整数巛文本表达扌(文本, 1+起址, 讫址, 欤返回零乊失败=False)
    else:
        分母 = 1
    非零有理数 = 分子 if 分母 == 1 else Fraction(分子,分母)
    讫址 = 起址
    return (非零有理数, 讫址)
#.class 乸非空解读器:
#.        失败处理{缺省值}？首字符？
#.    def 欤合法首字符扌(sf, 字符, /):
#.        '-> bool'
#.    def 解读扌(sf, 文本, 起址, 讫址, /):
#.        '[0 <= 起址 <= 讫址 <= len(文本)] => 文本 -> 起址 -> 讫址 -> (值, 讫址) | ^FormatError'
#.        if 起址 == 讫址: raise FormatError('eof')
#.        if not 欤合法首字符扌(文本[起址]):
#.            raise FormatError('')
#.        match sf.试解读扌(文本, 起址, 讫址):
#.            case (True, (值, 讫址)):
#.                return (值, 讫址)
#.            case (False, (错, 讫址)):
#.                raise FormatError((错, 讫址))
#.            case bad:
#.                raise TypeError(bad)
#.
#.
#.    def 试解读扌(sf, 文本, 起址, 讫址, /):
#.        '[0 <= 起址 <= 讫址 <= len(文本)] => 文本 -> 起址 -> 讫址 -> Either (错, 讫址) (值, 讫址)'
#.    def 罓试解读扌(sf, 文本, 起址, 讫址, /):
#.        '[0 <= 起址 < 讫址 <= len(文本)][欤合法首字符扌(文本[起址])] => 文本 -> 起址 -> 讫址 -> Either (错, 讫址) (值, 讫址)'
def 解读冫础称平式巛文本表达扌(文本, 起址, 讫址, /):
    match 取查冫首字符巛文本扌('wI', 文本, 起址, 讫址):
        case 'w':
            (变量数, 讫址) = 解读冫正整数巛文本表达扌(文本, 1+起址, 讫址, 欤返回零乊失败=False)
        case 'I':
            (变量数, 讫址) = (1, 1+起址)
        case _:
            raise 000
        #case
    础称平式 = 乸础称平式(变量数)
    return (础称平式, 讫址)

    #.if None is (m:=_rgx4I_wNNN.match(文本, 起址, 讫址)):raise FormatError(文本[起址:起址+100])
    #.assert 起址 == m.start()
    #.讫址 = m.end()
    #.wNNN = 文本[起址:讫址]
    #.变量数 = int(wNNN[1:])
    #.础称平式 = 乸础称平式(变量数)
    #.return (础称平式, 讫址)
def _4wNNNvNNN(wNNNvNNN, w, v, /):
    if v in wNNNvNNN:
        wNNN, _NNN = wNNNvNNN.split(v)
        幂次 = int(_NNN)
    else:
        wNNN = wNNNvNNN
        幂次 = 1
    assert wNNN[0] == w
    变量数 = int(wNNN[1:])
    return (变量数, 幂次)
def 解读冫础称乘式巛文本表达扌(文本, 起址, 讫址, /):
    (变量数讠幂次, 讫址) = _解读冫础称乘式巛文本表达扌(文本, 起址, 讫址, _rgx4I_wNNNvNNNX, 'w', 'v')
    础称平式讠幂次 = {乸础称平式(变量数): 幂次 for (变量数, 幂次) in 变量数讠幂次.items()}
    础称乘式 = 乸础称乘式(础称平式讠幂次)
    return (础称乘式, 讫址)
def _解读冫础称乘式巛文本表达扌(文本, 起址, 讫址, _rgx4I_wNNNvNNNX, w, v, /):
    if None is (m:=_rgx4I_wNNNvNNNX.match(文本, 起址, 讫址)):raise FormatError(文本[起址:起址+100])
    assert 起址 == m.start()
    讫址 = m.end()
    I_wNNNvNNNX = 文本[起址:讫址]
    match I_wNNNvNNNX:
        case 'I':
            变量数讠幂次 = {}
        case wNNNvNNNX:
            ls4wNNNvNNN = wNNNvNNNX.split('X')
            #(变量数, 幂次) = _4wNNNvNNN(wNNNvNNN)
            变量数讠幂次 = _mk_dict5uniq_items(_4wNNNvNNN(wNNNvNNN, w, v) for wNNNvNNN in ls4wNNNvNNN)
        #case
    变量数讠幂次
    return (变量数讠幂次, 讫址)
def _4dpNNNJNNNwNNNvNNNX(dpNNNJNNNwNNNvNNNX, 解读冫础称乘式巛文本表达扌, 乸础称乘式, /):
    L = len(dpNNNJNNNwNNNvNNNX)
    (非零系数, j) = 解读冫非零系数巛文本表达扌(dpNNNJNNNwNNNvNNNX, 0, L) #, 欤返回零乊失败=False
    if j < L:
        (础称乘式, j) = 解读冫础称乘式巛文本表达扌(dpNNNJNNNwNNNvNNNX, j, L)
    else:
        础称乘式 = 乸础称乘式({})
        j
    础称乘式
    assert j == L
    return (础称乘式, 非零系数)
def _mk_dict5uniq_items(items, /):
    d = {}
    for k, v in items:
        dict_add__new(d, k, v)
    return d
def 解读冫础称组式巛文本表达扌(文本, 起址, 讫址, /):
    (础称组式, 讫址) = _解读冫础称组式巛文本表达扌(文本, 起址, 讫址, _rgx4O_kdpNNNJNNNwNNNvNNNXXkk, 解读冫础称乘式巛文本表达扌, 乸础称乘式, 乸础称组式)
    return (础称组式, 讫址)
def _解读冫础称组式巛文本表达扌(文本, 起址, 讫址, _rgx4O_kdpNNNJNNNwNNNvNNNXXkk, 解读冫础称乘式巛文本表达扌, 乸础称乘式, 乸础称组式, /):
    if None is (m:=_rgx4O_kdpNNNJNNNwNNNvNNNXXkk.match(文本, 起址, 讫址)):raise FormatError(文本[起址:起址+100])
    assert 起址 == m.start()
    讫址 = m.end()
    O_kdpNNNJNNNwNNNvNNNXXkk = 文本[起址:讫址]
    match O_kdpNNNJNNNwNNNvNNNXXkk:
        case 'O':
            础称乘式讠系数 = {}
        case kdpNNNJNNNwNNNvNNNXXkk:
            [_null, *ls4dpNNNJNNNwNNNvNNNX] = kdpNNNJNNNwNNNvNNNXXkk.split('k')
            assert _null == ''
            础称乘式讠系数 = _mk_dict5uniq_items(_4dpNNNJNNNwNNNvNNNX(dpNNNJNNNwNNNvNNNX, 解读冫础称乘式巛文本表达扌, 乸础称乘式) for dpNNNJNNNwNNNvNNNX in ls4dpNNNJNNNwNNNvNNNX)

        #case
    础称乘式讠系数
    础称组式 = 乸础称组式(础称乘式讠系数)
    return (础称组式, 讫址)
def 解读冫非零系数巛文本表达扌(文本, 起址, 讫址, /):
    (非零系数, 讫址) = 解读冫非零有理数巛文本表达扌(文本, 起址, 讫址, 欤返回零乊失败=False)
    return (非零系数, 讫址)
def 解读冫瓧称重式巛文本表达扌(文本, 起址, 讫址, /):
    (幂次讠重数, 讫址) = _解读冫础称乘式巛文本表达扌(文本, 起址, 讫址, _rgx4I_eNNNrNNNX, 'e', 'r')
    瓧称重式 = 乸瓧称重式(幂次讠重数)
    return (瓧称重式, 讫址)
def 解读冫瓧称组式巛文本表达扌(文本, 起址, 讫址, /):
    (瓧称组式, 讫址) = _解读冫础称组式巛文本表达扌(文本, 起址, 讫址, _rgx4O_kdpNNNJNNNeNNNrNNNXXkk, 解读冫瓧称重式巛文本表达扌, 乸瓧称重式, 乸瓧称组式)
    return (瓧称组式, 讫址)



解读冫础称平式巛文本表达扌
解读冫础称乘式巛文本表达扌
解读冫础称组式巛文本表达扌
解读冫非零系数巛文本表达扌
解读冫瓧称重式巛文本表达扌
解读冫瓧称组式巛文本表达扌





################
__all__
from script.对称多项式讠基表达 import *
