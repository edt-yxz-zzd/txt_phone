#__all__:goto
r'''[[[
e script/搜索冫最短加链牜除模降解牜查表.py
view script/搜索冫首个特例纟最短加链牜查表.py
TODO:考虑使用 平方根策略:dichotomic_strategy
    view others/数学/最短加链/次优加链-论文-连分数-批量处理.txt
      直接求加靶链:cf_chain__many_(靶集:=({N}\-/τ(N)), γ_:=σ) #使用:γ_{dichotomic_strategy}


script.搜索冫最短加链牜除模降解牜查表
py -m nn_ns.app.debug_cmd   script.搜索冫最短加链牜除模降解牜查表 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.搜索冫最短加链牜除模降解牜查表:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   script.搜索冫最短加链牜除模降解牜查表   ,str.200:甄别冫靶值牜二进制拆分给出最短加链牜查表扌
+1:1
+2:2
+3:3
+4:4
+5:5
+6:6
+7:7
+8:8
+9:9
+10:10
+11:11
+12:12
+13:13
+14:14
-15:1
+16:15
+17:16
+18:17
+19:18
+20:19
+21:20
+22:21
-23:2
+24:22
+25:23
+26:24
-27:3
+28:25
+29:26
-30:4
-31:5
+32:27
+33:28
+34:29
+35:30
+36:31
+37:32
+38:33
-39:6
+40:34
+41:35
+42:36
-43:7
+44:37
-45:8
-46:9
-47:10
+48:38
+49:39
+50:40
-51:11
+52:41
+53:42
-54:12
-55:13
+56:43
+57:44
+58:45
-59:14
-60:15
-61:16
-62:17
-63:18
+64:46
+65:47
+66:48
+67:49
+68:50
+69:51
+70:52
+71:53
+72:54
+73:55
+74:56
-75:19
+76:57
-77:20
-78:21
-79:22
+80:58
+81:59
+82:60
-83:23
+84:61
-85:24
-86:25
-87:26
+88:62
+89:63
-90:27
-91:28
-92:29
-93:30
-94:31
-95:32
+96:64
+97:65
+98:66
-99:33
+100:67
+101:68
-102:34
-103:35
+104:69
+105:70
+106:71
-107:36
-108:37
-109:38
-110:39
-111:40
+112:72
+113:73
+114:74
-115:41
+116:75
-117:42
-118:43
-119:44
-120:45
-121:46
-122:47
-123:48
-124:49
-125:50
-126:51
-127:52
+128:76
+129:77
+130:78
+131:79
+132:80
+133:81
+134:82
-135:53
+136:83
+137:84
+138:85
+139:86
+140:87
+141:88
+142:89
-143:54
+144:90
+145:91
+146:92
-147:55
+148:93
-149:56
-150:57
-151:58
+152:94
-153:59
-154:60
-155:61
-156:62
-157:63
-158:64
-159:65
+160:95
+161:96
+162:97
-163:66
+164:98
-165:67
-166:68
-167:69
+168:99
+169:100
-170:70
-171:71
-172:72
-173:73
-174:74
-175:75
+176:101
+177:102
+178:103
-179:76
-180:77
-181:78
-182:79
-183:80
-184:81
-185:82
-186:83
-187:84
-188:85
-189:86
-190:87
-191:88
+192:104
+193:105
+194:106
-195:89
+196:107
+197:108
-198:90
-199:91
+200:109
]]


py_adhoc_call   script.搜索冫最短加链牜除模降解牜查表   ,200:搜索冫最短加链牜除模降解牜查表扌
    效果糟糕，成功的 都是 二进制拆分

from script.搜索冫最短加链牜除模降解牜查表 import *
]]]'''#'''
__all__ = r'''
甄别冫靶值牜二进制拆分给出最短加链牜查表扌


搜索冫最短加链牜除模降解牜查表扌
    NotOK
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...


def 甄别冫靶值牜二进制拆分给出最短加链牜查表扌(may_pint2shortest_addition_chain_length=None, /):
    (u2szmm, floor_log2, 上界相关纟) = _init(may_pint2shortest_addition_chain_length)
    it = enumerate(u2szmm)
    next(it, None)
        # 0:None
    num_goods = 0
    num_bads = 0
    for 靶值, 显链长 in it:
        #if 0b0001:print(靶值, 显链长)
        (阳爻数纟靶值, 上界纟显链长牜二进制) = 上界相关纟(靶值)
        if 显链长 == 上界纟显链长牜二进制:
            num_goods += 1
            yield f'+{靶值}:{num_goods}'
        else:
            assert 显链长 < 上界纟显链长牜二进制
            num_bads += 1
            yield f'-{靶值}:{num_bads}'

class NotOK(Exception):pass

def _init(may_pint2shortest_addition_chain_length, /):
    from seed.math.floor_ceil import floor_log2
    if not may_pint2shortest_addition_chain_length is None:
        pint2shortest_addition_chain_length = may_pint2shortest_addition_chain_length
    else:
        from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length
    u2szmm = pint2shortest_addition_chain_length
    def 上界相关纟(靶值, /):
        阳爻数纟靶值 = 靶值.bit_count()
        上界纟显链长牜二进制 = floor_log2(靶值) +阳爻数纟靶值 -1
        return (阳爻数纟靶值, 上界纟显链长牜二进制)
    return (u2szmm, floor_log2, 上界相关纟)

def 搜索冫最短加链牜除模降解牜查表扌(may_pint2shortest_addition_chain_length=None, /):
    (u2szmm, floor_log2, 上界相关纟) = _init(may_pint2shortest_addition_chain_length)
    #N = -1+len(u2szmm)
    it = enumerate(u2szmm)
    next(it, None)
        # 0:None
    next(it, None)
        # 1:0
    next(it, None)
        # 2:1
        # 初始手动处理『靶值1,2』<<==『put_ok_(2, -1, [1])』<<== 『for d in us4ok:』
    u2xs = [None]
    us4ok = []
    def 显链长纟(u, /):
        return u2szmm[u]
    def u2ok_(u, /):
        return u2xs[u][0]
    def u2chain_(u, /):
        if not u2ok_(u):
            raise NotOK
        return u2xs[u][-1]
    def put_bad_(u, /):
        ok = False
        xs = (ok, u)
        u2xs.append(xs)
        return xs
    def put_ok_(u, d, chain, /):
        ok = True
        if u > 1:us4ok.append(u)
        xs = (ok, u, d, chain)
        u2xs.append(xs)
        return xs
    def mul_chain_(q, d, /):
        ls4q = u2chain_(q)
        ls4d = u2chain_(d)
        ls4qd = (*ls4d[:-1], *(d*v for v in ls4q))
        return ls4qd
    def mul_add_chain_(q, d, r, /):
        ls4qd = mul_chain_(q, d)
        u = ls4qd[-1]+r
        if r > 0:
            if r in ls4qd:
                ls4qdr = (*ls4qd, u)
            else:
                ls4r = u2chain_(r)
                ls4qdr = tuple(sorted({*ls4r, *ls4qd, u}))
            ls4qdr
        else:
            assert r == 0
            ls4qdr = ls4qd
        ls4qdr
        return ls4qdr
    def mk_chain_(u, d, /):
        q, r = divmod(u, d)
        return mul_add_chain_(q, d, r)
    put_ok_(1, -1, (1,))
    put_ok_(2, -1, (1, 2))
    for 靶值, 显链长 in it:
        #if 0b0001:print(靶值, 显链长)
        (阳爻数纟靶值, 上界纟显链长牜二进制) = 上界相关纟(靶值)
        if 显链长 == 上界纟显链长牜二进制:
            yield put_ok_(靶值, 2, mk_chain_(靶值,2))
            continue
        #for d in range(2, 靶值):
        for d in us4ok:
            #if 0b0001:print(靶值, 显链长, d)
            try:
                ls4tgt = mk_chain_(靶值, d)
            except NotOK:
                continue
            if len(ls4tgt) > 显链长:
                continue
            assert len(ls4tgt) == 显链长, (靶值, 显链长, len(ls4tgt))
            yield put_ok_(靶值, d, ls4tgt)
            break
            #q, r = divmod(靶值, d)
        else:
            yield put_bad_(靶值)


__all__
from script.搜索冫最短加链牜除模降解牜查表 import *
