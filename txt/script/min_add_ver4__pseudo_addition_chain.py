#__all__:goto
r'''[[[
e script/min_add_ver4__pseudo_addition_chain.py
view others/数学/最短加链牜简并态.txt
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_min_and_max_if_revered.py
    le12021
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_max_one.py
    le4333
view script/搜索冫最短加链长度.py


失败:『真·最短加链牜简并态算法』@20250208
只能有=>『伪最短加链牜简并态算法/最短短程加链牜简并态算法』@20250208


script.min_add_ver4__pseudo_addition_chain
py -m nn_ns.app.debug_cmd   script.min_add_ver4__pseudo_addition_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd script.min_add_ver4__pseudo_addition_chain:__doc__ -ht # -ff -df

[[
定义:短程加链
    短程:相邻=>差存在链中
    短程加链的所有前缀都是短程加链
    最短短程加链的所有前缀都是最短短程加链
        即:允许递归搜索
<<==:
伪最短加链 重命名为:最短短程加链
<<==:
伪最短加链
    伪最短加链的所有前缀都是伪最短加链
    即:允许递归搜索

pseudo_shortest_addition_chain
all prefix are pseudo_shortest_addition_chain
]]


py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,50:枚举冫长度下限估计相关信息纟最短加链牜简并态算法扌

[[[
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,3000:枚举冫长度下限估计相关信息纟最短加链牜简并态算法扌    >  /sdcard/0my_files/tmp/0tmp  2>/sdcard/0my_files/tmp/0tmp2
view /sdcard/0my_files/tmp/0tmp
du -h /sdcard/0my_files/tmp/0tmp
    11M
view /sdcard/0my_files/tmp/0tmp2
    [2..=3001] ==>> 332*-1
    即:下限估计误差332个-1，没有更大误差
===
71
139
141
142
191
263
267
269
275
277
278
282
284
379
383
407
519
523
525
526
531
533
534
537
538
547
549
550
554
556
564
568
607
635
671
695
701
703
727
733
743
751
753
755
758
766
789
791
797
799
807
814
821
831
1031
1035
1037
1038
1043
1045
1046
1049
1050
1052
1059
1061
1062
1065
1066
1068
1074
1076
1087
1091
1093
1094
1098
1100
1108
1111
1112
1128
1136
1149
1151
1183
1195
1199
1211
1214
1243
1247
1259
1267
1270
1271
1277
1319
1327
1339
1342
1343
1367
1373
1375
1383
1389
1390
1391
1397
1403
1406
1425
1427
1447
1453
1454
1457
1466
1479
1487
1489
1502
1506
1507
1510
1516
1532
1557
1559
1565
1567
1573
1575
1577
1578
1581
1582
1583
1589
1594
1598
1599
1607
1611
1614
1628
1637
1642
1647
1662
1903
1979
2047
2055
2059
2061
2062
2067
2069
2070
2073
2074
2076
2083
2085
2086
2089
2090
2092
2097
2098
2100
2103
2104
2109
2111
2115
2117
2118
2121
2122
2124
2130
2132
2136
2141
2143
2148
2152
2157
2159
2167
2171
2173
2174
2179
2181
2182
2186
2188
2196
2199
2200
2207
2215
2216
2224
2233
2237
2239
2256
2263
2269
2271
2272
2279
2283
2287
2289
2291
2293
2297
2298
2299
2301
2302
2335
2347
2351
2357
2359
2363
2365
2366
2367
2375
2383
2390
2395
2398
2399
2407
2411
2419
2421
2422
2423
2428
2429
2455
2459
2463
2471
2477
2479
2485
2486
2487
2489
2491
2494
2518
2519
2521
2531
2534
2540
2542
2545
2554
2591
2599
2615
2621
2623
2631
2635
2638
2639
2651
2653
2654
2655
2663
2667
2669
2671
2675
2677
2678
2679
2681
2683
2684
2685
2686
2707
2727
2733
2734
2735
2745
2746
2750
2759
2766
2767
2779
2780
2782
2794
2806
2812
2833
2835
2850
2854
2887
2893
2894
2897
2906
2908
2913
2914
2932
2951
2959
2961
2974
2978
===
]]]


[[[

py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,10:枚举冫相关信息纟最短短程加链牜简并态算法扌
#py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,10:枚举冫相关信息纟最短短程加链牜简并态算法扌 -rename_NonTouchRanges | gawk $'{ gsub("NonTouchRanges", "RT") ; print $0 }'
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,10:枚举冫相关信息纟最短短程加链牜简并态算法扌 +rename_NonTouchRanges > /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,10:枚举冫相关信息纟最短短程加链牜简并态算法扌 +rename_NonTouchRanges --path:/sdcard/0my_files/tmp/0tmp

py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,100:枚举冫相关信息纟最短短程加链牜简并态算法扌 -rename_NonTouchRanges > /sdcard/0my_files/tmp/0tmp
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain  @_rename_NonTouchRanges  --ipath:/sdcard/0my_files/tmp/0tmp --opath:/sdcard/0my_files/tmp/0tmp4
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,100:枚举冫相关信息纟最短短程加链牜简并态算法扌 +rename_NonTouchRanges --path:/sdcard/0my_files/tmp/0tmp4

[2..=10025]之后:考虑重头再来:+尝试补充缺失=>无缺版:goto


<<==:


py_adhoc_call   script.min_add_ver4__pseudo_addition_chain  @_rename_NonTouchRanges  --ipath:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt  --opath:/sdcard/0my_files/tmp/0tmp4
du -h /sdcard/0my_files/tmp/0tmp4
    34M-->23M
mv -iv /sdcard/0my_files/tmp/0tmp4 script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
more script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt

==>>:
py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield +to_show_timedelta --may_args4PeriodicToilLeisureTime='(60,60)' --may_prompt_string6resting:$'\n\n    resting...\n\n' }  script.min_add_ver4__pseudo_addition_chain   ,3001:枚举冫相关信息纟最短短程加链牜简并态算法扌  +rename_NonTouchRanges --path:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
    在几分钟内完成[2..<3000]-323缺失
    注意:这里的定义稍有不同:『长度纟最短短程加链』包含『1』也就是说，计算加链中出现的所有正整数，而非加法发生次数
    由于『尝试校验最短=True』，所以若未报错，则前10_0000的最短短程加链其实就是最短加链。
    由于并非所有整数的最短短程加链都是最短加链，所以存在数据缺失。
    唯一的毛病是，由于中间数据缺失，所谓『水平反转后词典序最小/水平反转后词典序最大』可能有误
        求冫魊最短短程加链牜水平反转后词典序最小扌
        求冫魊最短短程加链牜水平反转后词典序最大扌
view script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt
#cancel:gawk $'{ gsub("NonTouchRanges", "RT") ; print $0 }' < script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt  > script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌-rename-RT.out.txt

===
@20250208
此时:[2..=10024]-缺失1756
grep '[0-9]*, None' -o script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt | lineno1
也就是说 [9002..=10025] 这1024个之中缺失319，缺太多了，就此打住。
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
    27M
tar -cvf script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.le10025.out.txt.tar.lzma  --lzma script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.le10025.out.txt.tar.lzma
    2.2M @20250208

===
此时:[2..=9001]-缺失1437
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
    23M
tar -cvf script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.le9001.out.txt.tar.lzma  --lzma script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.le9001.out.txt.tar.lzma
    1.9M

===
此时:[2..=9000]-缺失1437
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt
    34M
    _rename_NonTouchRanges:
        34M-->23M
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt.tar.lzma
    2.2M
    _rename_NonTouchRanges:
        2.2M-->1.9M
mv -iv  script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt  script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.preRT.out.txt
mv -iv script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt.tar.lzma script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.preRT.out.txt.tar.lzma
===
此时:[2..<6000]-缺失824
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt
    18M
tar -cvf script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt.tar.lzma  --lzma script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt.tar.lzma
    1.2M
===
此时:[2..<3000]-323缺失
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt
    6M
grep '[0-9]*, None' -o script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.out.txt | lineno1
    计算缺失数量
===
1:71, None
2:139, None
3:141, None
4:142, None
5:191, None
6:263, None
7:267, None
8:269, None
9:275, None
10:277, None
11:278, None
12:282, None
13:284, None
14:383, None
15:407, None
16:519, None
17:523, None
18:525, None
19:526, None
20:531, None
21:533, None
22:534, None
23:537, None
24:538, None
25:547, None
26:549, None
27:550, None
28:554, None
29:556, None
30:564, None
31:568, None
32:607, None
33:635, None
34:671, None
35:695, None
36:701, None
37:703, None
38:727, None
39:733, None
40:743, None
41:751, None
42:753, None
43:755, None
44:766, None
45:789, None
46:791, None
47:797, None
48:799, None
49:807, None
50:814, None
51:821, None
52:831, None
53:1031, None
54:1035, None
55:1037, None
56:1038, None
57:1043, None
58:1045, None
59:1046, None
60:1049, None
61:1050, None
62:1052, None
63:1059, None
64:1061, None
65:1062, None
66:1065, None
67:1066, None
68:1068, None
69:1074, None
70:1076, None
71:1087, None
72:1091, None
73:1093, None
74:1094, None
75:1098, None
76:1100, None
77:1108, None
78:1111, None
79:1112, None
80:1128, None
81:1136, None
82:1149, None
83:1151, None
84:1183, None
85:1195, None
86:1199, None
87:1211, None
88:1214, None
89:1243, None
90:1247, None
91:1259, None
92:1267, None
93:1270, None
94:1271, None
95:1277, None
96:1319, None
97:1327, None
98:1339, None
99:1342, None
100:1343, None
101:1367, None
102:1373, None
103:1375, None
104:1383, None
105:1389, None
106:1390, None
107:1391, None
108:1403, None
109:1406, None
110:1425, None
111:1447, None
112:1453, None
113:1454, None
114:1457, None
115:1466, None
116:1479, None
117:1487, None
118:1489, None
119:1502, None
120:1506, None
121:1507, None
122:1510, None
123:1532, None
124:1557, None
125:1559, None
126:1565, None
127:1567, None
128:1573, None
129:1575, None
130:1577, None
131:1578, None
132:1581, None
133:1582, None
134:1583, None
135:1589, None
136:1594, None
137:1598, None
138:1599, None
139:1607, None
140:1611, None
141:1614, None
142:1628, None
143:1637, None
144:1642, None
145:1647, None
146:1662, None
147:1903, None
148:1979, None
149:2047, None
150:2055, None
151:2059, None
152:2061, None
153:2062, None
154:2067, None
155:2069, None
156:2070, None
157:2073, None
158:2074, None
159:2076, None
160:2083, None
161:2085, None
162:2086, None
163:2089, None
164:2090, None
165:2092, None
166:2097, None
167:2098, None
168:2100, None
169:2103, None
170:2104, None
171:2109, None
172:2111, None
173:2115, None
174:2117, None
175:2118, None
176:2121, None
177:2122, None
178:2124, None
179:2130, None
180:2132, None
181:2136, None
182:2141, None
183:2143, None
184:2148, None
185:2152, None
186:2157, None
187:2159, None
188:2167, None
189:2171, None
190:2173, None
191:2174, None
192:2179, None
193:2181, None
194:2182, None
195:2186, None
196:2188, None
197:2196, None
198:2199, None
199:2200, None
200:2207, None
201:2215, None
202:2216, None
203:2224, None
204:2233, None
205:2237, None
206:2239, None
207:2256, None
208:2263, None
209:2269, None
210:2271, None
211:2272, None
212:2279, None
213:2283, None
214:2287, None
215:2289, None
216:2291, None
217:2293, None
218:2297, None
219:2298, None
220:2299, None
221:2301, None
222:2302, None
223:2335, None
224:2347, None
225:2351, None
226:2357, None
227:2359, None
228:2363, None
229:2365, None
230:2366, None
231:2367, None
232:2375, None
233:2383, None
234:2390, None
235:2395, None
236:2398, None
237:2399, None
238:2407, None
239:2411, None
240:2419, None
241:2421, None
242:2422, None
243:2423, None
244:2428, None
245:2429, None
246:2455, None
247:2459, None
248:2463, None
249:2471, None
250:2477, None
251:2479, None
252:2485, None
253:2486, None
254:2487, None
255:2489, None
256:2491, None
257:2494, None
258:2518, None
259:2519, None
260:2521, None
261:2531, None
262:2534, None
263:2540, None
264:2542, None
265:2545, None
266:2554, None
267:2591, None
268:2599, None
269:2615, None
270:2621, None
271:2623, None
272:2631, None
273:2635, None
274:2638, None
275:2639, None
276:2651, None
277:2653, None
278:2654, None
279:2655, None
280:2663, None
281:2667, None
282:2669, None
283:2671, None
284:2675, None
285:2678, None
286:2679, None
287:2681, None
288:2683, None
289:2684, None
290:2685, None
291:2686, None
292:2707, None
293:2727, None
294:2733, None
295:2734, None
296:2735, None
297:2745, None
298:2746, None
299:2750, None
300:2759, None
301:2766, None
302:2767, None
303:2779, None
304:2780, None
305:2782, None
306:2806, None
307:2812, None
308:2833, None
309:2850, None
310:2887, None
311:2893, None
312:2894, None
313:2897, None
314:2906, None
315:2908, None
316:2913, None
317:2914, None
318:2932, None
319:2951, None
320:2959, None
321:2961, None
322:2974, None
323:2978, None
    此时:[2..<3000]-323缺失
===
]]]


[[
无缺版:here
[2..=10025]之后:考虑重头再来:+尝试补充缺失
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,100:枚举冫相关信息纟最短短程加链牜简并态算法扌 +rename_NonTouchRanges +尝试补充缺失
py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield +to_show_timedelta --may_args4PeriodicToilLeisureTime='(30,30)' --may_prompt_string6resting:$'\n\n    resting...\n\n' }  script.min_add_ver4__pseudo_addition_chain   ,5001:枚举冫相关信息纟最短短程加链牜简并态算法扌  +rename_NonTouchRanges +尝试补充缺失 --path:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt
view script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt
    [2..=8239]
        此后:++iter_half_n2info_()
    [2..=12021] 52M
        就此打住@20250209
tar -cvf script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt.tar.lzma  --lzma script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt
du -h script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt.tar.lzma
    4.6M@20250209
mv -iv script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt.tar.lzma script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.le12021.out.txt.tar.lzma

TODO:
提取:加链:另档
    _提取另档冫加链扌()
对比:缺失版vs无缺版
    _对比冫缺失版丷无缺版扌()
ls script/min_add_ver4__pseudo_addition_chain.py.*

py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,str.10:_提取另档冫加链扌 --路径纟无缺版:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,str._提取另档冫加链扌 --路径纟无缺版:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt  > script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt
du -h script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt
    1.7M
view script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt
tar -cvf script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt.tar.lzma  --lzma script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt
du -h script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt.tar.lzma
    124K




def _对比冫缺失版丷无缺版扌(*, 路径纟缺失版, 路径纟无缺版):
py_adhoc_call   script.min_add_ver4__pseudo_addition_chain   ,_对比冫缺失版丷无缺版扌 --路径纟缺失版:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt --路径纟无缺版:script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt  > script/min_add_ver4__pseudo_addition_chain.py.._对比冫缺失版丷无缺版扌.le10025-vs-le12021.out.txt
du -h script/min_add_ver4__pseudo_addition_chain.py.._对比冫缺失版丷无缺版扌.le10025-vs-le12021.out.txt
    49M
view script/min_add_ver4__pseudo_addition_chain.py.._对比冫缺失版丷无缺版扌.le10025-vs-le12021.out.txt
    17493line=>17493/3==5831行记录 不同
    超过半数不同，相当严重
rm script/min_add_ver4__pseudo_addition_chain.py.._对比冫缺失版丷无缺版扌.le10025-vs-le12021.out.txt
DONE@20250209
===
前七行:
71
'(71, None, 0, 0, 0, 0, 0, 0)\n'
'(71, 10, 11, 70, [53, 55, 57, 58, 59, 61, 62, 63, 67, 69, 70], RT({1: 46, 48: 24}), [1, 2, 4, 5, 9, 18, 22, 31, 53, 71], [1, 2, 4, 8, 16, 32, 64, 68, 70, 71])\n'
127
'(127, 11, 25, 123, [79, 87, 89, 91, 93, 101, 103, 105, 106, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 125, 126], RT({1: 70, 72: 22, 96: 11, 108: 20}), [1, 2, 3, 6, 12, 24, 48, 49, 55, 79, 127], [1, 2, 4, 6, 12, 24, 48, 96, 120, 126, 127])\n'
'(127, 11, 26, 124, [71, 79, 87, 89, 91, 93, 101, 103, 105, 106, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 125, 126], RT({1: 93, 96: 11, 108: 20}), [1, 2, 3, 5, 7, 14, 28, 56, 57, 71, 127], [1, 2, 4, 6, 12, 24, 48, 96, 120, 126, 127])\n'
139
===

删除大文件:
ls script/min_add_ver4__pseudo_addition_chain.py.*
script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt
script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt.tar.lzma
script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.le10025.out.txt.tar.lzma
script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.le12021.out.txt.tar.lzma
script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt


du -h script/min_add_ver4__pseudo_addition_chain.py.*
124K script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt.tar.lzma
1.7M script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt

2.2M script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.le10025.out.txt.tar.lzma
4.6M script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.le12021.out.txt.tar.lzma

27M script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
52M script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt


rm -iv script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.out.txt
rm -iv script/min_add_ver4__pseudo_addition_chain.py..枚举冫相关信息纟最短短程加链牜简并态算法扌.RT.无缺.out.txt
ls_sSh_1F script/

使用于:
cp -iv script/min_add_ver4__pseudo_addition_chain.py.._提取另档冫加链扌.无缺.le12021.out.txt.tar.lzma   ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_min_and_max_if_revered.py..data.le12021.tar.lzma
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_min_and_max_if_revered.py

]]

from script.min_add_ver4__pseudo_addition_chain import 枚举冫长度下限估计相关信息纟最短加链牜简并态算法扌
]]]'''#'''
__all__ = r'''
枚举冫长度下限估计相关信息纟最短加链牜简并态算法扌
校验冫短程加链扌
求冫魊最短短程加链牜水平反转后词典序最小扌
求冫魊最短短程加链牜水平反转后词典序最大扌
枚举冫相关信息纟最短短程加链牜简并态算法扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...


#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...



#不能重构，因为事实上不存在
#.def mk_one_pseudo_shortest_addition_chain_(n2info, n, /):
#.    ls = [n]
#.    m = n
#.    (n, sz4chain, may_overrun, num_submaxs, num_nodes, submaxs, nodes, node2submaxs) = n2info[n]
#.    while submaxs:
#.        m
#.        n = submaxs[-1]
#.        ls.append(n)
#.        (n, sz4chain, may_overrun, num_submaxs, num_nodes, submaxs, nodes, node2submaxs) = n2info[n]
#.        #assert (m-n) in nodes
#.        submaxs = node2submaxs[m-n]
#.        m = n
#.    ls.reverse()
#.    return ls



def 枚举冫长度下限估计相关信息纟最短加链牜简并态算法扌():
    '简并态:下限估计冫最短加链长度[#比 真·最短加链 还短 因为可能不存在#]'
    ######################
    from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length__first_100000_terms
    from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length
    from seed.tiny import print_err
    ######################
    n2min_sz = pint2shortest_addition_chain_length
    L = len(n2min_sz)
    n2info = [(0, 0, 0, 0, 0, [], set()), (1, 1, 0, 0, 1, [], {1})]
        # [(n, sz4chain, may_underrun, num_submaxs, num_nodes, submaxs, all_possible_nodes)]
    #n2info = [(0, 0, 0, 0, 0, [], set(), {}), (1, 1, 0, 0, 1, [], {1}, {1:[]})]
        #xxx# [(n, sz4chain, may_overrun, num_submaxs, num_nodes, submaxs, all_possible_nodes, node2submaxs)]
    sz2ns = [[0], [1]]
    while 1:
        m = len(n2info)
        _sz4chain = min(sz4chain for (n, sz4chain, may_underrun, num_submaxs, num_nodes, submaxs, nodes) in n2info if (m-n) in nodes)
        submaxs4m = []
        nodes4m = {m}
        # node2submaxs4m = {m:submaxs4m}
        for (n, sz4chain, may_underrun, num_submaxs, num_nodes, submaxs, nodes) in n2info:
            if sz4chain==_sz4chain and (m-n) in nodes:
                submaxs4m.append(n)
                nodes4m |= nodes
                #for node in nodes: node2submaxs4m.setdefault(node, []).append(n)
        if len(nodes4m) == 1:raise Exception(m)
        if len(submaxs4m) == 0:raise Exception(m)
        submaxs4m
        nodes4m
        #node2submaxs4m

        sz4chain4m = 1+_sz4chain
        if m >= L:
            may_underrun4m = None
        else:
            min_sz4m = (1+n2min_sz[m])
                #n2min_sz exclude "1"
            underrun4m = sz4chain4m - min_sz4m
            may_underrun4m = underrun4m
        infos4m = (m, sz4chain4m, may_underrun4m, num_submaxs:=len(submaxs4m), num_nodes:=len(nodes4m), submaxs4m, nodes4m) #, node2submaxs4m
        n2info.append(infos4m)
        if sz4chain4m == len(sz2ns):
            sz2ns.append([])
        sz2ns[sz4chain4m].append(m)
        if may_underrun4m:
            assert underrun4m <= 0, (min_sz4m, infos4m)#mk_one_pseudo_shortest_addition_chain_(n2info, m)
            if underrun4m < 0:
                if 0b0001:print_err(m)
        yield infos4m





######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
######################
def _mkrs4rngs_():
    global _mkrs4rngs_
    old = _mkrs4rngs_
    ######################
    from seed.data_funcs.rngs import make_Ranges, sorted_rngs_to_iter_nontouch_ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
        #TouchRangeBasedIntMapping.from_value2begin2sz/.from_rng_value_pairs/.from_clone_of_rngs_with_default
    from seed.data_funcs.rngs import IRanges
        #for:.from_hexXhexszpair_list/.from_hex_repr_pair_list/.from_len_rng2hexbegins/.from_len_rng2begin_chars/.from_char_pairs__str/.from_hex_sz_pair_list/.from_hex2sz
        #for:.from_touch_rngs/.from_sorted_rngs/.from_unsorted_rngs/.from_sorted_ints/.from_unsorted_ints/.from_sorted_chars/.from_unsorted_chars
    from seed.data_funcs.rngs import NonTouchRanges, TouchRanges, make_NonTouchRanges, make_TouchRanges
    ######################
    from seed.helper.repr_input import repr_helper
    from seed.helper.stable_repr import stable_repr
    class RT:
        def __init__(sf, ranges, ):
            check_type_is(NonTouchRanges, ranges)
            sf._rs = ranges
        def __repr__(sf, /):
            s = stable_repr({int(u):sz for u, sz in sf._rs.to_hex_sz_pair_list()})
                #from_hex2sz
                #from_hex_sz_pair_list
            return f'RT({s})'
            return repr_helper(sf, sf._rs.ranges)
    ######################
    Mk = IRanges.from_sorted_ints
    _mkrs4rngs = (Mk, NonTouchRanges, RT)
    def _mkrs4rngs_():
        return _mkrs4rngs
    new = _mkrs4rngs_
    assert not new is old
    return _mkrs4rngs_()

def _n2sz_():
    global _n2sz_
    old = _n2sz_
    from nn_ns.math_nn.numbers.shortest_addition_chain_length import pint2shortest_addition_chain_length as _n2sz
    def _n2sz_():
        return _n2sz
    new = _n2sz_
    assert not new is old
    return _n2sz_()
def 校验冫短程加链扌(短程加链, 尝试校验最短):
    ls = 短程加链
    sz = len(ls)
    if sz == 0: return
    assert ls[0] == 1
    if sz == 1: return
    if 尝试校验最短:
        n = ls[-1]
        _n2sz = _n2sz_()
        if n < len(_n2sz):
            assert sz-1 == _n2sz[n], (_n2sz[n], sz, ls)
    s = set(ls)
    for i in range(1, sz):
        m = ls[i]
        n = ls[i-1]
        #短程:相邻=>差存在链中
        assert (m-n) in s

def 求冫魊最短短程加链牜水平反转后词典序最小扌(n2info, n, xs=(), /):
    '-> tmay 最短短程加链牜水平反转后词典序最小 # [唯一的毛病是，由于中间数据缺失，所谓『水平反转后词典序最小/水平反转后词典序最大』可能有误]'
    return 求冫魊最短短程加链牜水平反转后词典序最大扌(n2info, n, xs, min_vs_max=False)
def 求冫魊最短短程加链牜水平反转后词典序最大扌(n2info, n, xs=(), /, *, min_vs_max=True):
    '-> tmay 最短短程加链牜水平反转后词典序最大 # [唯一的毛病是，由于中间数据缺失，所谓『水平反转后词典序最小/水平反转后词典序最大』可能有误]'
    from bisect import bisect_left, bisect_right
    def left_(a, b, /):
        return a
    def right_(a, b, /):
        return b
    def forward_(max_x, submaxs4n):
        i = bisect_left(submaxs4n, max_x)
        for i in range(i, len(submaxs4n)):
            yield submaxs4n[i]
    def backward_(max_x, submaxs4n):
        for t in reversed(submaxs4n):
            if t < max_x:break
            yield t
    f = right_ if min_vs_max else left_
    #g = reversed if min_vs_max else iter
    g = backward_ if min_vs_max else forward_
    xs = set(xs)
    xs.discard(n)
    assert not xs or max(xs) < n
    #if 0b0001:from seed.tiny import print_err
    def recur(n, xs, /, *, _xs=xs, n2info=n2info, f=f):
        '-> tmay copy(ls)'
        #if 0b0001:print_err(n, xs)
        assert xs is _xs
        (n, sz4chain, num_submaxs, num_nodes, submaxs4n, nodes4n, ls0, ls1) = n2info[n]
        if not (ls1 or ls0):
            # creating info4n
            raise 000
            max_x = 0
        elif not xs:
            ls = f(ls0, ls1)
            # copy <<== append
            return (list(ls),)
        else:
            # [len(xs) > 0]
            max_x = max(xs)
        # [creating info4n]or[len(xs) > 0]
        assert max_x < n, (n, xs, max_x, n2info[n-1:n+1])
        # [max(xs) < n]
        # [creating info4n]or[len(xs) > 0]
        if not all(x in nodes4n for x in xs):
            return ()
        if len(xs) == 1:
            [x] = xs
            ls = f(ls0, ls1)
            if x in ls:
                # copy <<== append
                return (list(ls),)
        sz4xs = len(xs)
        for t in g(max_x, submaxs4n):
            #(_t, _, _, _, _, nodes4t, _, _) = n2info[t]
            #if not if all(x in nodes4t for x in xs): continue
            #if t < max_x:break
            if t < max_x:raise 000
            #if 0b0001:print_err(n, t, xs)
            diff = n-t
            assert diff > 0
            del4t = t in xs
            add4d = not (diff == t or diff in xs)
            if add4d:
                xs.add(diff)
            assert len(xs) == sz4xs+add4d
            if del4t:
                xs.remove(t)
            assert len(xs) == sz4xs+add4d-del4t
            #if 0b0001:print_err(n, t, diff, del4t, add4d, xs)
            tmay_ls = [*recur(t, xs)]
            #if 0b0001:print_err(n, t, xs)
            assert len(xs) == sz4xs+add4d-del4t
            if del4t:
                xs.add(t)
            assert len(xs) == sz4xs+add4d
            if add4d:
                xs.remove(diff)
            assert len(xs) == sz4xs
            if tmay_ls:
                [ls] = tmay_ls
                assert t == ls[-1]
                ls.append(n)
                # copy <<== append
                return (ls,)
        return ()
    return recur(n, xs)

#.def 求冫定点简并态纟最短短程加链扌(n2info, n, xs, /):
#.    xs = {*xs}
#.    m = max(xs)
#.    if m == n:
#.        xs.remove(n)
#.    elif m > n:
#.        raise Exception(n, xs)
#.    # [[len(xs) > 0] -> [max(xs) < n]]
#.    #check_type_is(list, xs)
#.    #len(xs)
#.    (n, sz4chain, num_submaxs, num_nodes, submaxs, nodes4n, submax2nodes, _, _) = n2info[n]
#.    if not xs:return nodes4n
#.    # [len(xs) > 0]
#.    # [max(xs) < n]
#.    if not all(x in nodes4n for x in xs):raise Exception(n, xs)#return set()
#.    ts = [t for t, nodes4t in submax2nodes.items() if all(x in nodes4t for x in xs)]
#.    nodes9xs = set()
#.    sz4xs = len(xs)
#.    for t in ts:
#.        diff = n-t
#.        xs.add(diff)
#.        s = 求冫定点简并态纟最短短程加链扌(n2info, t, xs)
#.        if not len(xs) == sz4xs:
#.            xs.remove(diff)
#.        assert len(xs) == sz4xs
#.        if s:
#.            assert t in s
#.            nodes9xs |= t
#.    if nodes9xs:
#.        nodes9xs.add(n)
#.    return nodes9xs


def _提取另档冫加链扌(*, 路径纟无缺版):
    import re
    rgx = re.compile('\[[^\[\]]*\]')
    with open(路径纟无缺版, 'rt', encoding='utf8') as 文件纟无缺版:
        for line in 文件纟无缺版:
            (submaxs, ls0, ls1) = [m.group(0) for m in rgx.finditer(line)]
            yield ls0
            yield ls1

def _对比冫缺失版丷无缺版扌(*, 路径纟缺失版, 路径纟无缺版):
    with open(路径纟缺失版, 'rt', encoding='utf8') as 文件纟缺失版, open(路径纟无缺版, 'rt', encoding='utf8') as 文件纟无缺版:
        for lineno, (line0, line1) in enumerate(zip(文件纟缺失版,文件纟无缺版)):
            if line0 == line1:continue
            #t = (lineno, line0, line1)
            i = line0.index(',')
            assert line0[:i+1] == line1[:i+1], (lineno, line0, line1)
            #if 'None' in line0:
            yield from (lineno, line0, line1)
def _rename_NonTouchRanges(*, ipath, opath):
    're-format output of 枚举冫相关信息纟最短短程加链牜简并态算法扌 as if [rename_NonTouchRanges=True]'
    (Mk, NonTouchRanges, RT) = _mkrs4rngs_()
    d = {'NonTouchRanges':NonTouchRanges}

    shower4NonTouchRanges = RT
    def apply_shower4NonTouchRanges(it, /, *, f=shower4NonTouchRanges):
        for info in it:
            yield (*info[:-3], f(info[-3]), *info[-2:]) if not info[1] is None else info
    def apply_shower(info, /, *, f=shower4NonTouchRanges):
        return (*info[:-3], f(info[-3]), *info[-2:]) if not info[1] is None else info
    with open(ipath, 'rt', encoding='utf8') as ifile, open(opath, 'xt', encoding='utf8') as ofile:
        def oprint(x, /):
            print(x, file=ofile)
            return x
        ifile.seek(0)
        for i, line in enumerate(ifile, 0):
            #if 0b0001:print_err(line)
            row = eval(line, d)
            check_type_is(tuple, row)
            assert row[0] == i
            new = apply_shower(row)
            oprint(new)
            #yield new

def 枚举冫相关信息纟最短短程加链牜简并态算法扌(*, path=None, 尝试校验最短=True, 尝试补充缺失=False, rename_NonTouchRanges=False):
    r'''[[[
    简并态:最短短程加链
    ===
    :: -> Iter (相关信息|缺失)
    [缺失 :: (uint, None, 0...)]
    [相关信息 :: (自然数, 长度纟最短短程加链, 规模纟次大点集纟所有最短短程加链, 规模纟点集纟所有最短短程加链, 次大点集纟所有最短短程加链, 简并态/点集纟所有最短短程加链, 最短短程加链牜水平反转后词典序最小,最短短程加链牜水平反转后词典序最大)]
    ===
    注意:这里的定义稍有不同:『长度纟最短短程加链』包含『1』也就是说，计算加链中出现的所有正整数，而非加法发生次数
    ===
    注意:存在数据缺失，导致所谓『水平反转后词典序最小/水平反转后词典序最大』可能有误
    ===
    在几分钟内完成[2..<3000]-323缺失
    ===
    [由于『尝试校验最短=True』，所以若未报错，则前10_0000的最短短程加链其实就是最短加链。]
    [由于并非所有整数的最短短程加链都是最短加链，所以存在数据缺失。]
    注意:[唯一的毛病是，由于中间数据缺失，所谓『水平反转后词典序最小/水平反转后词典序最大』可能有误]
        求冫魊最短短程加链牜水平反转后词典序最小扌
        求冫魊最短短程加链牜水平反转后词典序最大扌
    ===
    定义:短程加链
        短程:相邻=>差存在链中
        短程加链的所有前缀都是短程加链
        最短短程加链的所有前缀都是最短短程加链
            即:允许递归搜索
    ===
    #]]]'''#'''
    (Mk, NonTouchRanges, RT) = _mkrs4rngs_()
    if rename_NonTouchRanges:
        shower4NonTouchRanges = RT
        nm4mkr4NonTouchRanges = 'RT'
        NonTouchRanges = NonTouchRanges.from_hex2sz #from_hex_sz_pair_list
        def apply_shower4NonTouchRanges(it, /, *, f=shower4NonTouchRanges):
            for info in it:
                yield (*info[:-3], f(info[-3]), *info[-2:]) if not info[1] is None else info
    else:
        from seed.tiny_.funcs import echo
        shower4NonTouchRanges = echo
        nm4mkr4NonTouchRanges = 'NonTouchRanges'
        apply_shower4NonTouchRanges = echo
    shower4NonTouchRanges
    nm4mkr4NonTouchRanges
    apply_shower4NonTouchRanges
    run_ = lambda rows:apply_shower4NonTouchRanges(_罓枚举冫相关信息纟最短短程加链牜简并态算法扌(rows, 尝试校验最短=尝试校验最短, 尝试补充缺失=尝试补充缺失))

    rows = []
    if not path:
        oprint = print
        def oprint(x, /):
            pass
            return x
        yield from run_(rows)
    else:
        #from seed.tiny import print_err
        d = {nm4mkr4NonTouchRanges:NonTouchRanges}#dict(RT=NonTouchRanges, set=set)
        with open(path, 'at+', encoding='utf8') as ifile:
            ifile.seek(0)
            for i, line in enumerate(ifile, 0):
                #if 0b0001:print_err(line)
                row = eval(line, d)
                check_type_is(tuple, row)
                assert row[0] == i
                rows.append(row)
            rows
            def oprint(x, /):
                print(x, file=ifile)
                return x
            yield from map(oprint, run_(rows))
def _罓枚举冫相关信息纟最短短程加链牜简并态算法扌(saved_rows, /, *, 尝试校验最短, 尝试补充缺失):
    '简并态:最短短程加链'
    ######################
    if 尝试补充缺失:_n2sz = _n2sz_()
    from seed.tiny import print_err
    ######################
    #L = len(_n2sz)
    #n2info = [(0, 0, 0, 0, [], set(), {}, [], []), (1, 1, 0, 1, [], {1}, {1:[1]}, [1], [1])]
        # [(n, sz4chain, num_submaxs, num_nodes, 次大点/submaxs/NonTouchRanges, 简并态/nodes/all_possible_nodes, 次大点讠简并态牜含差/submax2nodes/{(n|submax):NonTouchRanges{include (n-submax)}}, 最短短程加链牜水平反转后词典序最小,最短短程加链牜水平反转后词典序最大)]
    #_n2info = [(0, 0, 0, 0, [], IRanges.from_sorted_ints([]), [], []), (1, 1, 0, 1, [], IRanges.from_sorted_ints([1]), [1], [1])]
    #Mk = IRanges.from_sorted_ints
    (Mk, NonTouchRanges, RT) = _mkrs4rngs_()
    _n2info = [(0, 0, 0, 0, [], Mk([]), [], []), (1, 1, 0, 1, [], Mk([1]), [1], [1])]
        # [(n, sz4chain, num_submaxs, num_nodes, 次大点/submaxs/NonTouchRanges, 简并态/nodes/all_possible_nodes, 最短短程加链牜水平反转后词典序最小,最短短程加链牜水平反转后词典序最大)]
    #sz2ns = [[0], [1]]
    #node2ns = [[], [1]]
    m = len(saved_rows)
    n2info = saved_rows
    if m < len(_n2info):
        infos = _n2info[m:]
        n2info += infos
        yield from infos
        del infos
    m = len(n2info)
    assert m >= 2
    m -= 1
    b_reset_sz = False
    get = n2info.__getitem__
    iter_half_n2info_ = lambda:map(get, range((m+1)//2, m))
    while 1:
        if b_reset_sz:
            b_reset_sz = False
            if not _sz4chain < _n2sz[m]:raise Exception('not found:@', 1+_sz4chain, _n2sz[m])
            #_sz4chain = _n2sz[m]
            _sz4chain += 1
            assert m == len(n2info)
        else:
            m += 1
            assert m == len(n2info)
            #_sz4chain = min(sz4chain for (n, sz4chain, num_submaxs, num_nodes, submaxs, nodes, _, _) in n2info if sz4chain and (m-n) in nodes)
            _sz4chain = min(sz4chain for (n, sz4chain, num_submaxs, num_nodes, submaxs, nodes, _, _) in iter_half_n2info_() if sz4chain and (m-n) in nodes)
        _sz4chain #has be reset
        assert m == len(n2info)
        submaxs4m = []
        nodes4m = Mk([m])
        #submax2nodes4m = {}
        lss = []
        #for (n, sz4chain, num_submaxs, num_nodes, submaxs, nodes, _, _) in n2info:
        for (n, sz4chain, num_submaxs, num_nodes, submaxs, nodes, _, _) in iter_half_n2info_():
            #if sz4chain==_sz4chain and (diff:=m-n) in nodes and (nodes6diff:=求冫定点简并态纟最短短程加链扌(n2info, n, [diff])):
            if sz4chain==_sz4chain and (diff:=m-n) in nodes and (tmay_ls:=求冫魊最短短程加链牜水平反转后词典序最大扌(n2info, n, [diff])):
                submax = n
                submaxs4m.append(submax)
                nodes4m |= nodes
                #submax2nodes4m[submax] = nodes6diff
                [ls] = tmay_ls
                lss.append(ls)
        num_nodes4m = nodes4m.len_ints()
        if num_nodes4m == 1:
            if 尝试补充缺失:
                b_reset_sz = True
                continue
            infos4m = (m, None, *[0]*6)
            n2info.append(infos4m)
            yield infos4m
            continue
            raise Exception(m)
            #first:71
        if len(submaxs4m) == 0:raise Exception(m)
        submaxs4m
        nodes4m
        #submax2nodes4m
        ls1 = lss[-1]
        ls1.append(m)
        if submaxs4m[0] == submaxs4m[-1]:
            ls0 = ls1
        else:
            #if 0b0001:print(m, ls1, submaxs4m)
            [ls0] = 求冫魊最短短程加链牜水平反转后词典序最小扌(n2info, submaxs4m[0], [m-submaxs4m[0]])
            ls0.append(m)

        sz4chain4m = 1+_sz4chain
        if 1:
            infos4m = (m, sz4chain4m, num_submaxs:=len(submaxs4m), num_nodes:=num_nodes4m, submaxs4m, nodes4m, ls0, ls1)
            n2info.append(infos4m)
        #.else:
        #.    infos4m = (m, sz4chain4m, num_submaxs:=len(submaxs4m), num_nodes:=num_nodes4m, submaxs4m, nodes4m, ls0:=[], ls1:=[])
        #.    n2info.append(infos4m)
        #.    [_ls0] = 求冫魊最短短程加链牜水平反转后词典序最小扌(n2info, m)
        #.    [_ls1] = 求冫魊最短短程加链牜水平反转后词典序最大扌(n2info, m)
        #.    ls0[:] = _ls0
        #.    ls1[:] = _ls1
        assert ls0[-1] == m, (m, ls0)
        assert ls1[-1] == m
        校验冫短程加链扌(ls0, 尝试校验最短)
        校验冫短程加链扌(ls1, 尝试校验最短)
        infos4m
        #.if 0:
        #.    if sz4chain4m == len(sz2ns):
        #.        sz2ns.append([])
        #.    sz2ns[sz4chain4m].append(m)
        #.if m <L:
        #.    min_sz4m = (1+_n2sz[m])
        #.        #_n2sz exclude "1"
        #.     if not sz4chain4m == min_sz4m:
        #.         raise Exception(min_sz4m, infos4m)
        yield (infos4m)




__all__
from script.min_add_ver4__pseudo_addition_chain import *
