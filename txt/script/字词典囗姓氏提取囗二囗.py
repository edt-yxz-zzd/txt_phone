#__all__:goto
r'''[[[
e script/字词典囗姓氏提取囗二囗.py
view ../../../unzip/e_book/字词典/\[Chinese-English\ dictionary]cedict_1_0_ts.u8

grep surname -i '../../../unzip/e_book/字词典/[Chinese-English dictionary]cedict_1_0_ts.u8' >  /sdcard/0my_files/tmp/out4grep/grep.surname.-i..cedict_1_0_ts.out.txt
view /sdcard/0my_files/tmp/out4grep/grep.surname.-i..cedict_1_0_ts.out.txt
    926行
    格式不同:中国姓vs外国姓
和 和 [He2] /surname He/Japanese (food, clothes etc)/
    !!!
阿多諾 阿多诺 [A1 duo1 nuo4] /surname Adorno/Theodor Ludwig Wiesengrund Adorno 狄奧多·阿多諾|狄奥多·阿多诺[Di2 ao4 duo1 · A1 duo1 nuo4] (1903-1969), German sociologist, philosopher, musicologist, and composer/
    !!!
万俟 万俟 [Mo4 qi2] /polysyllabic surname Moqi/
司 司 [Si1] /surname Si/
吳 吴 [Wu2] /surname Wu/area comprising southern Jiangsu, northern Zhejiang and Shanghai/name of states in Southern China at different historical periods/
寧 宁 [Ning2] /abbr. for Ningxia Hui Autonomous Region 寧夏回族自治區|宁夏回族自治区[Ning2 xia4 Hui2 zu2 Zi4 zhi4 qu1]/abbr. for Nanjing 南京[Nan2 jing1]/surname Ning/
司寇 司寇 [Si1 kou4] /two-character surname Sikou/
宇文 宇文 [Yu3 wen2] /a branch of the Xianbei 鮮卑|鲜卑[Xian1 bei1] nomadic people/two-character surname Yuwen/

五百年前是一家 五百年前是一家 [wu3 bai3 nian2 qian2 shi4 yi1 jia1] /five hundred years ago we were the same family (idiom) (said of persons with the same surname)/
姓 姓 [xing4] /family name/surname/CL:個|个[ge4]/to be surnamed/
姓名 姓名 [xing4 ming2] /name and surname/CL:個|个[ge4]/
某人 某人 [mou3 ren2] /someone/a certain person/some people/I (self-address after one's surname)/

今井 今井 [Jin1 jing3] /Imai (Japanese surname)/
佛洛斯特 佛洛斯特 [Fu2 luo4 si1 te4] /Frost (surname)/


script.字词典囗姓氏提取囗二囗
py -m nn_ns.app.debug_cmd   script.字词典囗姓氏提取囗二囗 -x
py -m nn_ns.app.doctest_cmd script.字词典囗姓氏提取囗二囗:__doc__ -ff -v
from script.字词典囗姓氏提取囗二囗 import *


py_adhoc_call   script.字词典囗姓氏提取囗二囗   ,囗提取囗 =1
py_adhoc_call   script.字词典囗姓氏提取囗二囗   @str.囗提取囗 =2
    765行

py_adhoc_call   script.字词典囗姓氏提取囗二囗   @str.囗提取囗 =2 > script/字词典囗姓氏提取囗二囗.py.outs/script.字词典囗姓氏提取囗二囗..grep.surname.-i..cedict_1_0_ts..中英词典囗姓氏囗繁简对照囗带拼音囗囗文本.out.txt
view script/字词典囗姓氏提取囗二囗.py.outs/script.字词典囗姓氏提取囗二囗..grep.surname.-i..cedict_1_0_ts..中英词典囗姓氏囗繁简对照囗带拼音囗囗文本.out.txt
cp -t script/字词典囗姓氏提取囗二囗.py.outs/ /sdcard/0my_files/tmp/out4grep/grep.surname.-i..cedict_1_0_ts.out.txt
view script/字词典囗姓氏提取囗二囗.py.outs/grep.surname.-i..cedict_1_0_ts.out.txt
du -h script/字词典囗姓氏提取囗二囗.py.outs/*
48K     script/字词典囗姓氏提取囗二囗.py.outs/grep.surname.-i..cedict_1_0_ts.out.txt
12K     script/字词典囗姓氏提取囗二囗.py.outs/script.字词典囗姓氏提取囗二囗..grep.surname.-i..cedict_1_0_ts..中英词典囗姓氏囗繁简对照囗带拼音囗囗文本.out.txt



中英词典囗姓氏囗繁简对照囗带拼音囗囗文本:copy to:
cp -t ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/ script/字词典囗姓氏提取囗二囗.py.outs/script.字词典囗姓氏提取囗二囗..grep.surname.-i..cedict_1_0_ts..中英词典囗姓氏囗繁简对照囗带拼音囗囗文本.out.txt
view ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/script.字词典囗姓氏提取囗二囗..grep.surname.-i..cedict_1_0_ts..中英词典囗姓氏囗繁简对照囗带拼音囗囗文本.out.txt

#]]]'''
__all__ = r'''
囗行变换囗
    囗提取囗
囗待进一步处理文本囗人工编辑结果
    中英词典囗姓氏囗繁简对照囗带拼音囗囗文本
        囗中英词典囗姓氏囗繁简对照囗带拼音囗囗文本囗
'''.split()#'''
__all__




囗待进一步处理文本囗人工编辑结果 = r'''[[[
grep surname -i '../../../unzip/e_book/字词典/[Chinese-English dictionary]cedict_1_0_ts.u8' >  /sdcard/0my_files/tmp/out4grep/grep.surname.-i..cedict_1_0_ts.out.txt
then:

:.,$sort i/Japanese/
和 和 [He2] /surname He/Japanese (food, clothes etc)/


:.,$sort i/\/surname/
万俟 万俟 [Mo4 qi2] /polysyllabic surname Moqi/
上官 上官 [Shang4 guan1] /two-character surname Shangguan/



:.,$sort /(surname)/
里 里 [Li3] /Li (surname)/
:.,$sort /surname [A-Z]/
烏梁海 乌梁海 [Wu1 liang2 hai3] /Mongol surname/
烏良哈 乌良哈 [Wu1 liang2 ha3] /Mongol surname/
鄂 鄂 [E4] /abbr. for Hubei Province 湖北省[Hu2 bei3 Sheng3] in central China/surname E/
阿多諾 阿多诺 [A1 duo1 nuo4] /surname Adorno/Theodor Ludwig Wiesengrund Adorno 狄奧多·阿多諾|狄奥多·阿多诺[Di2 ao4 duo1 · A1 duo1 nuo4] (1903-1969), German sociologist, philosopher, musicologist, and composer/
萊佛士 莱佛士 [Lai2 fo2 shi4] /Stamford Raffles (1781-1826), British statesman and founder of the city of Singapore/surname Raffles/
拉青格 拉青格 [La1 qing1 ge2] /Ratzinger (German surname of Pope Benedict XVI)/





:.,$sort /surname/
阿多諾 阿多诺 [A1 duo1 nuo4] /surname Adorno/Theodor Ludwig Wiesengrund Adorno 狄奧多·阿多諾|狄奥多·阿多诺[Di2 ao4 duo1 · A1 duo1 nuo4] (1903-1969), German sociologist, philosopher, musicologist, and composer/
艾 艾 [Ai4] /surname Ai/
... ...
左 左 [Zuo3] /surname Zuo/
#上移5个姓氏:
喬答摩 乔答摩 [Qiao2 da1 mo2] /Gautama, surname of the Siddhartha, the historical Buddha/
瞿曇 瞿昙 [Qu2 tan2] /Gautama, surname of the Siddhartha, the historical Buddha/
里 里 [Li3] /Li (surname)/
烏梁海 乌梁海 [Wu1 liang2 hai3] /Mongol surname/
烏良哈 乌良哈 [Wu1 liang2 ha3] /Mongol surname/
#下移14个外国姓氏:阿多諾..川普
    ^\S\S
#下移『赐姓』



===共926行，765个中国姓氏
===begin:
艾 艾 [Ai4] /surname Ai/
安 安 [An1] /surname An/
卬 卬 [Ang2] /surname Ang/
敖 敖 [Ao2] /surname Ao/
仈 仈 [Ba1] /surname Ba/
巴 巴 [Ba1] /Ba state during Zhou dynasty (in east of modern Sichuan)/abbr. for east Sichuan or Chongqing/surname Ba/abbr. for Palestine or Palestinian/abbr. for Pakistan/
白 白 [Bai2] /surname Bai/
百 百 [Bai3] /surname Bai/
柏 柏 [Bai3] /surname Bai/Taiwan pr. [Bo2]/
百里 百里 [Bai3 li3] /two-character surname Baili/
班 班 [Ban1] /surname Ban/
包 包 [Bao1] /surname Bao/
暴 暴 [Bao4] /surname Bao/
鮑 鲍 [Bao4] /surname Bao/
貝 贝 [Bei4] /surname Bei/
賁 贲 [Ben1] /surname Ben/
畢 毕 [Bi4] /surname Bi/
邲 邲 [Bi4] /surname Bi/ancient place name/
卞 卞 [Bian4] /surname Bian/
別 别 [Bie2] /surname Bie/
秉 秉 [Bing3] /surname Bing/
邴 邴 [Bing3] /surname Bing/
薄 薄 [Bo2] /surname Bo/
卜 卜 [Bu3] /surname Bu/
步 步 [Bu4] /surname Bu/
蔡 蔡 [Cai4] /surname Cai/
蒼 苍 [Cang1] /surname Cang/
曹 曹 [Cao2] /surname Cao/Zhou Dynasty vassal state/
策 策 [Ce4] /surname Ce/
岑 岑 [Cen2] /surname Cen/
柴 柴 [Chai2] /surname Chai/
常 常 [Chang2] /surname Chang/
昌 昌 [Chang1] /surname Chang/
萇 苌 [Chang2] /surname Chang/
巢 巢 [Chao2] /surname Chao/
晁 晁 [Chao2] /surname Chao/
鼂 鼂 [Chao2] /surname Chao/
車 车 [Che1] /surname Che/
臣 臣 [Chen2] /surname Chen/
諶 谌 [Chen2] /surname Chen/
陳 陈 [Chen2] /surname Chen/vassal state during the Spring and Autumn Period 770-475 BC/Chen of the Southern dynasties (557-589)/
乘 乘 [Cheng2] /surname Cheng/
成 成 [Cheng2] /surname Cheng/
晟 晟 [Cheng2] /surname Cheng/
澄 澄 [Cheng2] /surname Cheng/
程 程 [Cheng2] /surname Cheng/
承 承 [Cheng2] /surname Cheng/Cheng (c. 2000 BC), third of the legendary Flame Emperors 炎帝[Yan2 di4] descended from Shennong 神農|神农[Shen2 nong2] Farmer God/
郕 郕 [Cheng2] /surname Cheng/Zhou Dynasty (1046-256 BCE) vassal state/
庱 庱 [Cheng3] /surname Cheng/ancient area of modern day Danyang City, Jiangsu Province/
池 池 [Chi2] /surname Chi/
蚩 蚩 [Chi1] /surname Chi/
遲 迟 [Chi2] /surname Chi/
郗 郗 [Chi1] /surname Chi/name of an ancient city/
崇 崇 [Chong2] /surname Chong/
丑 丑 [Chou3] /surname Chou/
褚 褚 [Chu3] /surname Chu/
鄐 鄐 [Chu4] /surname Chu/
儲 储 [Chu3] /surname Chu/Taiwan pr. [Chu2]/
楚 楚 [Chu3] /surname Chu/abbr. for Hubei 湖北省[Hu2 bei3 Sheng3] and Hunan 湖南省[Hu2 nan2 Sheng3] provinces together/Chinese kingdom during the Spring and Autumn and Warring States Periods (722-221 BC)/
釧 钏 [Chuan4] /surname Chuan/
淳于 淳于 [Chun2 yu2] /two-character surname Chun'yu/
春 春 [Chun1] /surname Chun/
佽 佽 [Ci4] /surname Ci/
從 从 [Cong2] /surname Cong/
琮 琮 [Cong2] /surname Cong/
爨 爨 [Cuan4] /surname Cuan/
崔 崔 [Cui1] /surname Cui/
錯 错 [Cuo4] /surname Cuo/
笪 笪 [Da2] /surname Da/
達 达 [Da2] /surname Da/
戴 戴 [Dai4] /surname Dai/
亶 亶 [Dan3] /surname Dan/
黨 党 [Dang3] /surname Dang/
刀 刀 [Dao1] /surname Dao/
鄧 邓 [Deng4] /surname Deng/
邸 邸 [Di3] /surname Di/
鞮 鞮 [Di1] /surname Di/
狄 狄 [Di2] /surname Di/generic name for northern ethnic minorities during the Qin and Han Dynasties (221 BC-220 AD)/
翟 翟 [Di2] /surname Di/variant of 狄[Di2], generic name for northern ethnic minorities during the Qin and Han Dynasties (221 BC-220 AD)/
甸 甸 [Dian4] /surname Dian/
刁 刁 [Diao1] /surname Diao/
丁 丁 [Ding1] /surname Ding/
東 东 [Dong1] /surname Dong/
董 董 [Dong3] /surname Dong/
鼕 冬 [Dong1] /surname Dong/
東方 东方 [Dong1 fang1] /the East/the Orient/two-character surname Dongfang/
東郭 东郭 [Dong1 guo1] /two-character surname Dongguo/
竇 窦 [Dou4] /surname Dou/
杜 杜 [Du4] /surname Du/
都 都 [Du1] /surname Du/
段 段 [Duan4] /surname Duan/
端木 端木 [Duan1 mu4] /two-character surname Duanmu/
兌 兑 [Dui4] /surname Dui/
鈬 鈬 [Duo2] /surname Duo/
鐸 铎 [Duo2] /surname Duo/
鄂 鄂 [E4] /abbr. for Hubei Province 湖北省[Hu2 bei3 Sheng3] in central China/surname E/
耏 耏 [Er2] /surname Er/
樊 樊 [Fan2] /surname Fan/
范 范 [Fan4] /surname Fan/
坊 坊 [Fang1] /surname Fang/
房 房 [Fang2] /surname Fang/
方 方 [Fang1] /surname Fang/
斐 斐 [Fei3] /surname Fei/
費 费 [Fei4] /surname Fei/
封 封 [Feng1] /surname Feng/
豐 丰 [Feng1] /surname Feng/
酆 酆 [Feng1] /Zhou Dynasty capital/surname Feng/
馮 冯 [Feng2] /surname Feng/
鳳 凤 [Feng4] /surname Feng/
付 付 [Fu4] /surname Fu/
伏 伏 [Fu2] /surname Fu/
傅 傅 [Fu4] /surname Fu/
富 富 [Fu4] /surname Fu/
符 符 [Fu2] /surname Fu/
福 福 [Fu2] /surname Fu/abbr. for Fujian province 福建省[Fu2 jian4 sheng3]/
賅 赅 [Gai1] /surname Gai/
乾 干 [Gan1] /surname Gan/
甘 甘 [Gan1] /surname Gan/abbr. for Gansu Province 甘肅省|甘肃省[Gan1 su4 Sheng3]/
港 港 [Gang3] /Hong Kong, abbr. for 香港[Xiang1 gang3]/surname Gang/
高 高 [Gao1] /surname Gao/
郜 郜 [Gao4] /surname Gao/name of a feudal state/
戈 戈 [Ge1] /surname Ge/
葛 葛 [Ge3] /surname Ge/
蓋 盖 [Ge3] /surname Ge/
鬲 鬲 [Ge2] /surname Ge/
耿 耿 [Geng3] /surname Geng/
宮 宫 [Gong1] /surname Gong/
弓 弓 [Gong1] /surname Gong/
貢 贡 [Gong4] /surname Gong/
龔 龚 [Gong1] /surname Gong/
公孫 公孙 [Gong1 sun1] /two-character surname Gongsun/
勾 勾 [Gou1] /surname Gou/
緱 缑 [Gou1] /surname Gou/
苟 苟 [Gou3] /surname Gou/
古 古 [Gu3] /surname Gu/
谷 谷 [Gu3] /surname Gu/
辜 辜 [Gu1] /surname Gu/
顧 顾 [Gu4] /surname Gu/
冠 冠 [Guan4] /surname Guan/
官 官 [Guan1] /surname Guan/
筦 筦 [Guan3] /surname Guan/
管 管 [Guan3] /surname Guan/
觀 观 [Guan4] /surname Guan/
關 关 [Guan1] /surname Guan/
廣 广 [Guang3] /surname Guang/
歸 归 [Gui1] /surname Gui/
炅 炅 [Gui4] /surname Gui/
炔 炔 [Gui4] /surname Gui/
桂 桂 [Gui4] /surname Gui/abbr. for Guangxi Autonomous Region 廣西壯族自治區|广西壮族自治区[Guang3 xi1 Zhuang4 zu2 Zi4 zhi4 qu1]/
邽 邽 [Gui1] /surname Gui/ancient place name/
媯 妫 [Gui1] /surname Gui/name of a river/
穀梁 谷梁 [Gu3 liang2] /surname Guliang/abbr. for 穀梁傳|谷梁传[Gu3 liang2 Zhuan4], Guliang Annals/
咼 呙 [Guo1] /surname Guo/
國 国 [Guo2] /surname Guo/
虢 虢 [Guo2] /Guo, a kinship group whose members held dukedoms within the Zhou Dynasty realm, including Western Guo 西虢國|西虢国 and Eastern Guo 東虢國|东虢国/surname Guo/
過 过 [Guo4] /surname Guo/
郭 郭 [Guo1] /surname Guo/
海 海 [Hai3] /surname Hai/
翰 翰 [Han4] /surname Han/
韓 韩 [Han2] /Han, one of the Seven Hero States of the Warring States 戰國七雄|战国七雄/Korea from the fall of the Joseon dynasty in 1897/Korea, esp. South Korea 大韓民國|大韩民国/surname Han/
杭 杭 [Hang2] /surname Hang/Hangzhou/
昊 昊 [Hao4] /surname Hao/
郝 郝 [Hao3] /ancient place name/surname Hao/
何 何 [He2] /surname He/
佫 佫 [He4] /surname He/
賀 贺 [He4] /surname He/
和 和 [He2] /surname He/Japanese (food, clothes etc)/
赫 赫 [He4] /surname He/abbr. for Herz Hz 赫茲|赫兹[He4 zi1]/
恆 恒 [Heng2] /surname Heng/
洪 洪 [Hong2] /surname Hong/
紅 红 [Hong2] /surname Hong/
訇 訇 [Hong1] /surname Hong/
閎 闳 [Hong2] /surname Hong/
侯 侯 [Hou2] /surname Hou/
后 后 [Hou4] /surname Hou/
郈 郈 [Hou4] /surname Hou/place name/
忽 忽 [Hu1] /surname Hu/
扈 扈 [Hu4] /surname Hu/
胡 胡 [Hu2] /surname Hu/
滹 滹 [Hu1] /surname Hu/name of a river/
滑 滑 [Hua2] /surname Hua/
花 花 [Hua1] /surname Hua/
華 华 [Hua4] /Mt Hua 華山|华山 in Shaanxi/surname Hua/
懷 怀 [Huai2] /surname Huai/
奐 奂 [Huan4] /surname Huan/
宦 宦 [Huan4] /surname Huan/
桓 桓 [Huan2] /surname Huan/
環 环 [Huan2] /surname Huan/
還 还 [Huan2] /surname Huan/
黃 黄 [Huang2] /surname Huang or Hwang/
皇 皇 [Huang2] /surname Huang/
皇甫 皇甫 [Huang2 fu3] /two-character surname Huangfu/
惠 惠 [Hui4] /surname Hui/
火 火 [Huo3] /surname Huo/
霍 霍 [Huo4] /surname Huo/
丌 丌 [Ji1] /surname Ji/
冀 冀 [Ji4] /short name for Hebei 河北 province/surname Ji/
姞 姞 [Ji2] /surname Ji/
季 季 [Ji4] /surname Ji/
戢 戢 [Ji2] /surname Ji/
機 机 [Ji1] /surname Ji/
汲 汲 [Ji2] /surname Ji/
稽 稽 [Ji1] /surname Ji/
籍 籍 [Ji2] /surname Ji/
藉 藉 [Ji2] /surname Ji/
計 计 [Ji4] /surname Ji/
吉 吉 [Ji2] /surname Ji/abbr. for Jilin Province 吉林省[Ji2 lin2 Sheng3]/
紀 纪 [Ji3] /surname Ji/also pr. [Ji4]/
薊 蓟 [Ji4] /surname Ji/ancient Chinese city state near modern day Beijing/
姬 姬 [Ji1] /surname Ji/family name of the Zhou Dynasty 周代[Zhou1 dai4] (1046-256 BC)/
嵇 嵇 [Ji1] /surname Ji/name of a mountain/
佳 佳 [Jia1] /surname Jia/
加 加 [Jia1] /abbr. for Canada 加拿大[Jia1 na2 da4]/surname Jia/
嘉 嘉 [Jia1] /surname Jia/
家 家 [Jia1] /surname Jia/
賈 贾 [Jia3] /surname Jia/
駕 驾 [Jia4] /surname Jia/
剪 剪 [Jian3] /surname Jian/
籛 篯 [Jian1] /surname Jian/
翦 翦 [Jian3] /surname Jian/
蕑 蕑 [Jian1] /surname Jian/
諫 谏 [Jian4] /surname Jian/
蹇 蹇 [Jian3] /surname Jian/
姜 姜 [Jiang1] /surname Jiang/
江 江 [Jiang1] /surname Jiang/
薑 姜 [Jiang1] /surname Jiang/
蔣 蒋 [Jiang3] /surname Jiang/refers to Chiang Kai-shek 蔣介石|蒋介石/
姣 姣 [Jiao1] /surname Jiao/
教 教 [Jiao4] /surname Jiao/
焦 焦 [Jiao1] /surname Jiao/
皦 皦 [Jiao3] /surname Jiao/
矯 矫 [Jiao3] /surname Jiao/
蟜 蟜 [Jiao3] /surname Jiao/
郊 郊 [Jiao1] /surname Jiao/
靳 靳 [Jin4] /surname Jin/
金 金 [Jin1] /surname Jin/surname Kim (Korean)/Jurchen Jin dynasty (1115-1234)/
晉 晋 [Jin4] /surname Jin/the Jin Dynasties (265-420)/Western Jin 西晉|西晋[Xi1 Jin4] (265-316), Eastern Jin 東晉|东晋[Dong1 Jin4] (317-420) and Later Jin Dynasty (936-946)/short name for Shanxi province 山西[Shan1 xi1]/
井 井 [Jing3] /Jing, one of the 28 constellations of Chinese astronomy/surname Jing/
景 景 [Jing3] /surname Jing/
經 经 [Jing1] /surname Jing/
靖 靖 [Jing4] /surname Jing/
京 京 [Jing1] /abbr. for Beijing/surname Jing/Jing ethnic minority/
樛 樛 [Jiu1] /surname Jiu/
居 居 [Ju1] /surname Ju/
苴 苴 [Ju1] /surname Ju/
鞠 鞠 [Ju1] /surname Ju/
涓 涓 [Juan1] /surname Juan/
雋 隽 [Juan4] /surname Juan/
傕 傕 [Jue2] /surname Jue/
矍 矍 [Jue2] /surname Jue/
角 角 [Jue2] /surname Jue/
凱 凯 [Kai3] /surname Kai/
闞 阚 [Kan4] /surname Kan/
康 康 [Kang1] /surname Kang/
亢 亢 [Kang4] /surname Kang/Kang, one of the 28 constellations/
恪 恪 [Ke4] /surname Ke/
柯 柯 [Ke1] /surname Ke/
孔 孔 [Kong3] /surname Kong/
噲 哙 [Kuai4] /surname Kuai/
鄶 郐 [Kuai4] /surname Kuai/name of a feudal state/
寬 宽 [Kuan1] /surname Kuan/
匡 匡 [Kuang1] /surname Kuang/
鄺 邝 [Kuang4] /surname Kuang/
匱 匮 [Kui4] /surname Kui/
夔 夔 [Kui2] /one-legged mountain demon of Chinese mythology/Chinese mythical figure who invented music and dancing/Chinese rain god/surname Kui/
蕢 蒉 [Kui4] /surname Kui/
隗 隗 [Kui2] /surname Kui/Zhou Dynasty vassal state/
賴 赖 [Lai4] /surname Lai/
藍 蓝 [Lan2] /surname Lan/
蘭 兰 [Lan2] /surname Lan/abbr. for Lanzhou 蘭州|兰州[Lan2 zhou1], Gansu/
郎 郎 [Lang2] /surname Lang/
郞 郞 [Lang2] /variant of 郎[Lang2]/surname Lang/
嫪 嫪 [Lao4] /surname Lao/
樂 乐 [Le4] /surname Le/
嫘 嫘 [Lei2] /surname Lei/
纍 累 [Lei2] /surname Lei/
雷 雷 [Lei2] /surname Lei/
冷 冷 [Leng3] /surname Leng/
利 利 [Li4] /surname Li/
力 力 [Li4] /surname Li/
勵 励 [Li4] /surname Li/
厲 厉 [Li4] /surname Li/
李 李 [Li3] /surname Li/
栗 栗 [Li4] /surname Li/
澧 澧 [Li3] /Lishui River in north Hunan, flowing into Lake Dongting 洞庭湖/surname Li/
立 立 [Li4] /surname Li/
離 离 [Li2] /surname Li/
黎 黎 [Li2] /Li ethnic group of Hainan Province/surname Li/abbr. for Lebanon 黎巴嫩[Li2 ba1 nen4]/
禮 礼 [Li3] /surname Li/abbr. for 禮記|礼记[Li3 ji4], Classic of Rites/
酈 郦 [Li4] /surname Li/ancient place name/
廉 廉 [Lian2] /surname Lian/
連 连 [Lian2] /surname Lian/
梁 梁 [Liang2] /name of Kingdoms and Dynasties at different periods/surname Liang/
僚 僚 [Liao2] /surname Liao/
廖 廖 [Liao4] /surname Liao/
藺 蔺 [Lin4] /surname Lin/
遴 遴 [Lin2] /surname Lin/
林 林 [Lin2] /surname Lin/Japanese surname Hayashi/
凌 凌 [Ling2] /surname Ling/
泠 泠 [Ling2] /surname Ling/
令狐 令狐 [Ling2 hu2] /old place name (in modern Linyi county 臨猗縣|临猗县, Shanxi)/two-character surname Linghu/
劉 刘 [Liu2] /surname Liu/
柳 柳 [Liu3] /surname Liu/
龍 龙 [Long2] /surname Long/
隆 隆 [Long2] /surname Long/short for 吉隆坡[Ji2 long2 po1], Kuala Lumpur/
樓 楼 [Lou2] /surname Lou/
婁 娄 [Lou2] /surname Lou/one of the 28 lunar mansions in Chinese astronomy/
潞 潞 [Lu4] /name of a river/surname Lu/
路 路 [Lu4] /surname Lu/
逯 逯 [Lu4] /surname Lu/
錄 录 [Lu4] /surname Lu/
陸 陆 [Lu4] /surname Lu/
露 露 [Lu4] /surname Lu/
魯 鲁 [Lu3] /surname Lu/Shandong Province 山東省|山东省[Shan1 dong1 Sheng3]/vassal state during the Zhou Dynasty (1066-221 BC) in modern day Shandong Province/
盧 卢 [Lu2] /surname Lu/abbr. for Luxembourg 盧森堡|卢森堡[Lu2 sen1 bao3]/
甪 甪 [Lu4] /surname Lu/place name/
欒 栾 [Luan2] /surname Luan/
羅 罗 [Luo2] /surname Luo/
駱 骆 [Luo4] /surname Luo/
洛 洛 [Luo4] /surname Luo/old name of several rivers (in Henan, Shaanxi, Sichuan and Anhui)/
呂 吕 [Lu:3] /surname Lü/
律 律 [Lu:4] /surname Lü/
鑢 鑢 [Lu:4] /surname Lü/
麻 麻 [Ma2] /surname Ma/
馬 马 [Ma3] /surname Ma/abbr. for Malaysia 馬來西亞|马来西亚[Ma3 lai2 xi1 ya4]/
麥 麦 [Mai4] /surname Mai/
嫚 嫚 [Man4] /surname Man/
冒 冒 [Mao4] /surname Mao/
毛 毛 [Mao2] /surname Mao/
茅 茅 [Mao2] /surname Mao/
枚 枚 [Mei2] /surname Mei/
梅 梅 [Mei2] /surname Mei/
門 门 [Men2] /surname Men/
孟 孟 [Meng4] /surname Meng/
蒙 蒙 [Meng2] /surname Meng/
宓 宓 [Mi4] /surname Mi/
禰 祢 [Mi2] /surname Mi/
米 米 [Mi3] /surname Mi/
糜 糜 [Mi2] /surname Mi/
羋 芈 [Mi3] /surname Mi/
麋 麋 [Mi2] /surname Mi/
密 密 [Mi4] /surname Mi/name of an ancient state/
繆 缪 [Miao4] /surname Miao/
苗 苗 [Miao2] /Hmong or Miao ethnic group of southwest China/surname Miao/
民 民 [Min2] /surname Min/
閔 闵 [Min3] /surname Min/
明 明 [Ming2] /Ming Dynasty (1368-1644)/surname Ming/Ming (c. 2000 BC), fourth of the legendary Flame Emperors, 炎帝[Yan2 di4] descended from Shennong 神農|神农[Shen2 nong2] Farmer God/
莫 莫 [Mo4] /surname Mo/
鄚 鄚 [Mo4] /surname Mo/
墨 墨 [Mo4] /surname Mo/abbr. for 墨西哥[Mo4 xi1 ge1], Mexico/
万俟 万俟 [Mo4 qi2] /polysyllabic surname Moqi/
牟 牟 [Mou2] /surname Mou/
木 木 [Mu4] /surname Mu/
牧 牧 [Mu4] /surname Mu/
穆 穆 [Mu4] /surname Mu/
慕容 慕容 [Mu4 rong2] /a branch of the Xianbei 鮮卑|鲜卑 nomadic people/two-character surname Murong/
納 纳 [Na4] /surname Na/
那 那 [Na1] /surname Na/
南 南 [Nan2] /surname Nan/
南郭 南郭 [Nan2 guo1] /surname Nanguo/
淖 淖 [Nao4] /surname Nao/
能 能 [Neng2] /surname Neng/
倪 倪 [Ni2] /surname Ni/
年 年 [Nian2] /surname Nian/
聶 聂 [Nie4] /surname Nie/
齧 齧 [Nie4] /surname Nie/
寧 宁 [Ning2] /abbr. for Ningxia Hui Autonomous Region 寧夏回族自治區|宁夏回族自治区[Ning2 xia4 Hui2 zu2 Zi4 zhi4 qu1]/abbr. for Nanjing 南京[Nan2 jing1]/surname Ning/
牛 牛 [Niu2] /surname Niu/
鈕 钮 [Niu3] /surname Niu/
農 农 [Nong2] /surname Nong/
那 那 [Nuo2] /surname Nuo/
區 区 [Ou1] /surname Ou/
歐 欧 [Ou1] /Europe/abbr. for 歐洲|欧洲[Ou1 zhou1]/surname Ou/
毆 殴 [Ou1] /surname Ou/
歐陽 欧阳 [Ou1 yang2] /two-character surname Ouyang/
怕 怕 [Pa4] /surname Pa/
番 番 [Pan1] /surname Pan/
潘 潘 [Pan1] /surname Pan/Pan, faun in Greek mythology, son of Hermes/
尨 尨 [Pang2] /surname Pang/
逄 逄 [Pang2] /surname Pang/
龐 庞 [Pang2] /surname Pang/
裴 裴 [Pei2] /surname Pei/
彭 彭 [Peng2] /surname Peng/
蓬 蓬 [Peng2] /surname Peng/
皮 皮 [Pi2] /surname Pi/
裨 裨 [Pi2] /surname Pi/
邳 邳 [Pi1] /surname Pi/Han dynasty county in modern Jiangsu/also pr. [Pei2]/
扁 扁 [Pian1] /surname Pian/
駢 骈 [Pian2] /surname Pian/
朴 朴 [Piao2] /surname Piao/Korean surname (Park, Pak, or Bak)/also pr. [Pu2]/
平 平 [Ping2] /surname Ping/
頗 颇 [Po1] /surname Po/Taiwan pr. [Po3]/
浦 浦 [Pu3] /surname Pu/
溥 溥 [Pu3] /surname Pu/
濮 濮 [Pu2] /name of a river/surname Pu/
蒲 蒲 [Pu2] /surname Pu/old place name/
亓 亓 [Qi2] /surname Qi/
戚 戚 [Qi1] /surname Qi/
盵 盵 [Qi4] /surname Qi/
祁 祁 [Qi2] /surname Qi/
齊 齐 [Qi2] /(name of states and dynasties at several different periods)/surname Qi/
杞 杞 [Qi3] /surname Qi/Zhou Dynasty vassal state/
岐 岐 [Qi2] /surname Qi/also used in place names/
乾 乾 [Qian2] /surname Qian/
錢 钱 [Qian2] /surname Qian/
強 强 [Qiang2] /surname Qiang/
槍 枪 [Qiang1] /surname Qiang/
羌 羌 [Qiang1] /Qiang ethnic group of northwestern Sichuan/surname Qiang/
喬 乔 [Qiao2] /surname Qiao/
譙 谯 [Qiao2] /surname Qiao/
郄 郄 [Qie4] /surname Qie/
欽 钦 [Qin1] /surname Qin/
覃 覃 [Qin2] /surname Qin/
秦 秦 [Qin2] /surname Qin/Qin dynasty (221-207 BC) of the first emperor 秦始皇[Qin2 Shi3 huang2]/abbr. for 陝西|陕西[Shan3 xi1]/
清 清 [Qing1] /Qing or Ch'ing dynasty of Imperial China (1644-1911)/surname Qing/
黥 黥 [Qing2] /surname Qing/
丘 丘 [Qiu1] /surname Qiu/
仇 仇 [Qiu2] /surname Qiu/
盚 盚 [Qiu2] /surname Qiu/
秋 秋 [Qiu1] /surname Qiu/
糗 糗 [Qiu3] /surname Qiu/
裘 裘 [Qiu2] /surname Qiu/
邱 邱 [Qiu1] /surname Qiu/
佉 佉 [Qu1] /surname Qu/
屈 屈 [Qu1] /surname Qu/
曲 曲 [Qu1] /surname Qu/
朐 朐 [Qu2] /surname Qu/
渠 渠 [Qu2] /surname Qu/
璩 璩 [Qu2] /surname Qu/
瞿 瞿 [Qu2] /surname Qu/
蘧 蘧 [Qu2] /surname Qu/
麯 麯 [Qu1] /surname Qu/
麴 麴 [Qu1] /surname Qu/
全 全 [Quan2] /surname Quan/
權 权 [Quan2] /surname Quan/
闕 阙 [Que1] /surname Que/
冉 冉 [Ran3] /surname Ran/
穰 穰 [Rang2] /surname Rang/
饒 饶 [Rao2] /surname Rao/
任 任 [Ren4] /surname Ren/
容 容 [Rong2] /surname Rong/
戎 戎 [Rong2] /surname Rong/
榮 荣 [Rong2] /surname Rong/
肜 肜 [Rong2] /surname Rong/
孺 孺 [Ru2] /surname Ru/
茹 茹 [Ru2] /surname Ru/
阮 阮 [Ruan3] /surname Ruan/small state during the Shang Dynasty (1600-1046 BC) located in the southeast of modern-day Gansu Province/
芮 芮 [Rui4] /surname Rui/
薩 萨 [Sa4] /Bodhisattva/surname Sa/
三 三 [San1] /surname San/
桑 桑 [Sang1] /surname Sang/
沙 沙 [Sha1] /surname Sha/
單 单 [Shan4] /surname Shan/
山 山 [Shan1] /surname Shan/
閃 闪 [Shan3] /surname Shan/
商 商 [Shang1] /Shang Dynasty (c. 1600-1046 BC)/surname Shang/
尚 尚 [Shang4] /surname Shang/
上官 上官 [Shang4 guan1] /two-character surname Shangguan/
劭 劭 [Shao4] /surname Shao/
卲 卲 [Shao4] /surname Shao/
紹 绍 [Shao4] /surname Shao/
韶 韶 [Shao2] /surname Shao/
召 召 [Shao4] /surname Shao/name of an ancient state that existed in what is now Shaanxi Province/
邵 邵 [Shao4] /surname Shao/place name/
佘 佘 [She2] /surname She/
厙 厍 [She4] /surname She/
舍 舍 [She4] /surname She/
申 申 [Shen1] /old name for Shanghai 上海[Shang4 hai3]/surname Shen/
瞫 瞫 [Shen3] /surname Shen/
莘 莘 [Shen1] /surname Shen/
沈 沈 [Shen3] /surname Shen/place name/
盛 盛 [Sheng4] /surname Sheng/
申屠 申屠 [Shen1 tu2] /two-character surname Shentu/
世 世 [Shi4] /surname Shi/
史 史 [Shi3] /surname Shi/
士 士 [Shi4] /surname Shi/
奭 奭 [Shi4] /surname Shi/
室 室 [Shi4] /surname Shi/
師 师 [Shi1] /surname Shi/
施 施 [Shi1] /surname Shi/
時 时 [Shi2] /surname Shi/
石 石 [Shi2] /surname Shi/
適 适 [Shi4] /surname Shi/
壽 寿 [Shou4] /surname Shou/
束 束 [Shu4] /surname Shu/
殳 殳 [Shu1] /surname Shu/
疏 疏 [Shu1] /surname Shu/
舒 舒 [Shu1] /surname Shu/
耍 耍 [Shua3] /surname Shua/
帥 帅 [Shuai4] /surname Shuai/
雙 双 [Shuang1] /surname Shuang/
水 水 [Shui3] /surname Shui/
司 司 [Si1] /surname Si/
姒 姒 [Si4] /surname Si/
司寇 司寇 [Si1 kou4] /two-character surname Sikou/
司馬 司马 [Si1 ma3] /Minister of War (official title in pre-Han Chinese states)/two-character surname Sima/
司徒 司徒 [Si1 tu2] /minister of education (history)/two-character surname Situ/
松 松 [Song1] /surname Song/
宋 宋 [Song4] /surname Song/the Song dynasty (960-1279)/also Song of the Southern dynasties 南朝宋 (420-479)/
宿 宿 [Su4] /surname Su/
粟 粟 [Su4] /surname Su/
肅 肃 [Su4] /surname Su/
蔌 蔌 [Su4] /surname Su/
蘇 苏 [Su1] /surname Su/abbr. for Soviet Union 蘇維埃|苏维埃 or 蘇聯|苏联/abbr. for Jiangsu province 江蘇|江苏/abbr. for Suzhou city 蘇州|苏州/
眭 眭 [Sui1] /surname Sui/
睢 睢 [Sui1] /surname Sui/
隋 隋 [Sui2] /the Sui dynasty (581-617 AD)/surname Sui/
隨 随 [Sui2] /surname Sui/
孫 孙 [Sun1] /surname Sun/
妁 妁 [Shuo4] /surname Suo/
索 索 [Suo3] /surname Suo/abbr. for 索馬里|索马里[Suo3 ma3 li3], Somalia/
沓 沓 [Ta4] /surname Ta/
禢 禢 [Ta4] /surname Ta/see also 褟[ta1]/
台 台 [Tai2] /Taiwan (abbr.)/surname Tai/
邰 邰 [Tai2] /surname Tai/name of a feudal state/
檀 檀 [Tan2] /surname Tan/
潭 潭 [Tan2] /surname Tan/
澹 澹 [Tan2] /surname Tan/
覃 覃 [Tan2] /surname Tan/
談 谈 [Tan2] /surname Tan/
譚 谭 [Tan2] /surname Tan/
鐔 镡 [Tan2] /surname Tan/
郯 郯 [Tan2] /surname Tan/name of an ancient city/
唐 唐 [Tang2] /Tang dynasty (618-907)/surname Tang/
湯 汤 [Tang1] /surname Tang/
陶 陶 [Tao2] /surname Tao/
滕 滕 [Teng2] /vassal state of Zhou in Shandong/Teng county in Shandong/surname Teng/
題 题 [Ti2] /surname Ti/
田 田 [Tian2] /surname Tian/
鐵 铁 [Tie3] /surname Tie/
佟 佟 [Tong2] /surname Tong/
彤 彤 [Tong2] /surname Tong/
童 童 [Tong2] /surname Tong/
鈄 钭 [Tou3] /surname Tou/
土 土 [Tu3] /Tu (ethnic group)/surname Tu/
屠 屠 [Tu2] /surname Tu/
徒 徒 [Tu2] /surname Tu/
涂 涂 [Tu2] /surname Tu/
拓 拓 [Tuo4] /surname Tuo/
媧 娲 [Wa1] /surname Wa/sister of legendary emperor Fu Xi 伏羲/
宛 宛 [Wan3] /surname Wan/
萬 万 [Wan4] /surname Wan/
汪 汪 [Wang1] /surname Wang/
王 王 [Wang2] /surname Wang/
危 危 [Wei1] /surname Wei/
圍 围 [Wei2] /surname Wei/
委 委 [Wei3] /surname Wei/
寪 寪 [Wei3] /surname Wei/
尉 尉 [Wei4] /surname Wei/
維 维 [Wei2] /abbr. for Uighur 維吾爾|维吾尔[Wei2 wu2 er3]/surname Wei/
薳 薳 [Wei3] /surname Wei/
謂 谓 [Wei4] /surname Wei/
隗 隗 [Wei3] /surname Wei/
韋 韦 [Wei2] /surname Wei/
微 微 [Wei1] /surname Wei/ancient Chinese state near present day Chongqing/Taiwan pr. [Wei2]/
魏 魏 [Wei4] /surname Wei/name of vassal state of Zhou dynasty from 661 BC in Shanxi, one of the Seven Hero Warring States/Wei state, founded by Cao Cao 曹操, one of the Three Kingdoms from the fall of the Han/the Wei dynasty 221-265/Wei prefecture and Wei county at different historical periods/
衛 卫 [Wei4] /surname Wei/vassal state during the Zhou Dynasty (1066-221 BC), located in present day Henan and Hebei Provinces/
文 文 [Wen2] /surname Wen/
溫 温 [Wen1] /surname Wen/
聞 闻 [Wen2] /surname Wen/
甕 瓮 [Weng4] /surname Weng/
翁 翁 [Weng1] /surname Weng/
仵 仵 [Wu3] /surname Wu/
伍 伍 [Wu3] /surname Wu/
兀 兀 [Wu4] /surname Wu/
吾 吾 [Wu2] /surname Wu/
武 武 [Wu3] /surname Wu/
毋 毋 [Wu2] /surname Wu/
烏 乌 [Wu1] /abbr. for Ukraine 烏克蘭|乌克兰[Wu1 ke4 lan2]/surname Wu/
巫 巫 [Wu1] /surname Wu/also pr. [Wu2]/
鄔 邬 [Wu1] /surname Wu/ancient place name/
吳 吴 [Wu2] /surname Wu/area comprising southern Jiangsu, northern Zhejiang and Shanghai/name of states in Southern China at different historical periods/
郄 郄 [Xi4] /variant of 郤, surname Xi/
僖 僖 [Xi1] /surname Xi/
奚 奚 [Xi1] /surname Xi/
席 席 [Xi2] /surname Xi/
昔 昔 [Xi1] /surname Xi/
羲 羲 [Xi1] /same as Fuxi 伏羲[Fu2 Xi1], a mythical emperor/surname Xi/
習 习 [Xi2] /surname Xi/
郤 郤 [Xi4] /surname Xi/
隰 隰 [Xi2] /surname Xi/
夏 夏 [Xia4] /the Xia or Hsia dynasty c. 2000 BC/Xia of the Sixteen Kingdoms (407-432)/surname Xia/
冼 冼 [Xian3] /surname Xian/
咸 咸 [Xian2] /surname Xian/
向 向 [Xiang4] /surname Xiang/
相 相 [Xiang1] /surname Xiang/
襄 襄 [Xiang1] /surname Xiang/
項 项 [Xiang4] /surname Xiang/
蕭 萧 [Xiao1] /surname Xiao/
肖 肖 [Xiao1] /surname Xiao/Taiwan pr. [Xiao4]/
渫 渫 [Xie4] /surname Xie/
燮 燮 [Xie4] /surname Xie/
解 解 [Xie4] /surname Xie/
謝 谢 [Xie4] /surname Xie/
頡 颉 [Xie2] /surname Xie/
西門 西门 [Xi1 men2] /surname Ximen/
新 新 [Xin1] /abbr. for Xinjiang 新疆[Xin1 jiang1] or Singapore 新加坡[Xin1 jia1 po1]/surname Xin/
辛 辛 [Xin1] /surname Xin/
鄩 鄩 [Xin2] /surname Xin/place name/
刑 刑 [Xing2] /surname Xing/
幸 幸 [Xing4] /surname Xing/
興 兴 [Xing1] /surname Xing/
邢 邢 [Xing2] /surname Xing/place name/
敻 敻 [Xiong4] /surname Xiong/
熊 熊 [Xiong2] /surname Xiong/
休 休 [Xiu1] /surname Xiu/
修 修 [Xiu1] /surname Xiu/
徐 徐 [Xu2] /surname Xu/
盱 盱 [Xu1] /surname Xu/
胥 胥 [Xu1] /surname Xu/
藇 藇 [Xu4] /surname Xu/
許 许 [Xu3] /surname Xu/
鄦 鄦 [Xu3] /surname Xu/vassal state during the Zhou Dynasty (1046-221 BC)/
宣 宣 [Xuan1] /surname Xuan/
禤 禤 [Xuan1] /surname Xuan/
軒 轩 [Xuan1] /surname Xuan/
軒轅 轩辕 [Xuan1 yuan2] /two-character surname Xuanyuan/
雪 雪 [Xue3] /surname Xue/
薛 薛 [Xue1] /surname Xue/vassal state during the Zhou Dynasty (1046-256 BC)/
荀 荀 [Xun2] /surname Xun/
衙 衙 [Ya2] /surname Ya/
軋 轧 [Ya4] /surname Ya/
偃 偃 [Yan3] /surname Yan/
傿 傿 [Yan1] /name of an immortal/ancient place name/surname Yan/
嚴 严 [Yan2] /surname Yan/
奄 奄 [Yan3] /surname Yan/
延 延 [Yan2] /surname Yan/
晏 晏 [Yan4] /surname Yan/
沇 沇 [Yan3] /surname Yan/
燕 燕 [Yan1] /Yan, a vassal state of Zhou in modern Hebei and Liaoning/north Hebei/the four Yan kingdoms of the Sixteen Kingdoms, namely: Former Yan 前燕 (337-370), Later Yan 後燕|后燕 (384-409), Southern Yan 南燕 (398-410), Northern Yan 北燕 (409-436)/surname Yan/
閆 闫 [Yan2] /variant of 閻|阎[Yan2]/surname Yan/
閻 阎 [Yan2] /Yama/gate of village/surname Yan/
顏 颜 [Yan2] /surname Yan/
鄢 鄢 [Yan1] /surname Yan/name of a district in Henan/
仰 仰 [Yang3] /surname Yang/
揚 扬 [Yang2] /abbr. for 揚州|扬州[Yang2 zhou1]/surname Yang/
楊 杨 [Yang2] /surname Yang/
羊 羊 [Yang2] /surname Yang/
么 幺 [Yao1] /surname Yao/
姚 姚 [Yao2] /surname Yao/
搖 摇 [Yao2] /surname Yao/
瑤 瑶 [Yao2] /Yao ethnic group of southwest China and southeast Asia/surname Yao/
銚 铫 [Yao2] /surname Yao/
堯 尧 [Yao2] /surname Yao/Yao or Tang Yao (c. 2200 BC), one of Five legendary Emperors 五帝[wu3 di4], second son of Di Ku 帝嚳|帝喾[Di4 Ku4]/
也 也 [Ye3] /surname Ye/
業 业 [Ye4] /surname Ye/
葉 叶 [Ye4] /surname Ye/
鄴 邺 [Ye4] /surname Ye/ancient district in modern day Hebei Province 河北省[He2 bei3 Sheng3]/
佚 佚 [Yi4] /surname Yi/
宜 宜 [Yi2] /surname Yi/
扆 扆 [Yi3] /surname Yi/
益 益 [Yi4] /surname Yi/
齮 齮 [Yi3] /surname Yi/
義 义 [Yi4] /surname Yi/(Tw) abbr. for 義大利|义大利[Yi4 da4 li4], Italy/
伊 伊 [Yi1] /surname Yi/abbr. for 伊拉克[Yi1 la1 ke4], Iraq/abbr. for 伊朗[Yi1 lang3], Iran/
易 易 [Yi4] /surname Yi/abbr. for 易經|易经[Yi4 jing1], the Book of Changes/
翼 翼 [Yi4] /surname Yi/alternative name for 絳|绛[Jiang4] capital of the Jin State during the Spring and Autumn Period (770-475 BC)/
羿 羿 [Yi4] /surname Yi/name of legendary archer/also written 后羿[Hou4 Yi4]/
尹 尹 [Yin3] /surname Yin/
誾 訚 [Yin2] /surname Yin/
闉 闉 [Yin1] /surname Yin/
陰 阴 [Yin1] /surname Yin/
印 印 [Yin4] /surname Yin/abbr. for 印度[Yin4 du4]/
殷 殷 [Yin1] /surname Yin/dynasty name at the end the Shang dynasty, after their move to Yinxu 殷墟 in modern Henan province/
嬴 嬴 [Ying2] /surname Ying/
應 应 [Ying4] /surname Ying/
穎 颖 [Ying3] /surname Ying/
雍 雍 [Yong1] /surname Yong/
鄘 鄘 [Yong1] /surname Yong/name of a feudal state/
尤 尤 [You2] /surname You/
游 游 [You2] /surname You/
于 于 [Yu2] /surname Yu/
余 余 [Yu2] /surname Yu/
俞 俞 [Yu2] /surname Yu/
喻 喻 [Yu4] /surname Yu/
禹 禹 [Yu3] /Yu the Great (c. 21st century BC), mythical leader who tamed the floods/surname Yu/
紆 纡 [Yu1] /surname Yu/
臾 臾 [Yu2] /surname Yu/
虞 虞 [Yu2] /surname Yu/
遇 遇 [Yu4] /surname Yu/
遹 遹 [Yu4] /surname Yu/
邘 邘 [Yu2] /surname Yu/
郁 郁 [Yu4] /surname Yu/
餘 馀 [Yu2] /surname Yu/
鬱 郁 [Yu4] /surname Yu/
魚 鱼 [Yu2] /surname Yu/
楀 楀 [Yu3] /surname Yu/(arch. name of tree)/
於 於 [Yu1] /surname Yu/Taiwan pr. [Yu2]/
庾 庾 [Yu3] /surname Yu/name of a mountain/
蔚 蔚 [Yu4] /surname Yu/place name/
園 园 [Yuan2] /surname Yuan/
爰 爰 [Yuan2] /surname Yuan/
苑 苑 [Yuan4] /surname Yuan/
蜎 蜎 [Yuan1] /surname Yuan/
袁 袁 [Yuan2] /surname Yuan/
元 元 [Yuan2] /surname Yuan/the Yuan or Mongol dynasty (1279-1368)/
尉遲 尉迟 [Yu4 chi2] /surname Yuchi/
岳 岳 [Yue4] /surname Yue/
嶽 岳 [Yue4] /surname Yue/
樂 乐 [Yue4] /surname Yue/
惲 恽 [Yun4] /surname Yun/
雲 云 [Yun2] /surname Yun/abbr. for Yunnan Province 雲南省|云南省[Yun2 nan2 Sheng3]/
宇文 宇文 [Yu3 wen2] /a branch of the Xianbei 鮮卑|鲜卑[Xian1 bei1] nomadic people/two-character surname Yuwen/
昝 昝 [Zan3] /surname Zan/
臧 臧 [Zang1] /surname Zang/
曾 曾 [Zeng1] /surname Zeng/
繒 缯 [Zeng1] /surname Zeng/
鄫 鄫 [Zeng2] /surname Zeng/Zhou vassal state/
查 查 [Zha1] /surname Zha/
霅 霅 [Zha2] /surname Zha/
祭 祭 [Zhai4] /surname Zhai/
翟 翟 [Zhai2] /surname Zhai/
展 展 [Zhan3] /surname Zhan/
湛 湛 [Zhan4] /surname Zhan/
詹 詹 [Zhan1] /surname Zhan/
仉 仉 [Zhang3] /surname Zhang/
張 张 [Zhang1] /surname Zhang/
章 章 [Zhang1] /surname Zhang/
長孫 长孙 [Zhang3 sun1] /two-character surname Zhangsun/
兆 兆 [Zhao4] /surname Zhao/
炤 炤 [Zhao4] /surname Zhao/
趙 赵 [Zhao4] /surname Zhao/one of the seven states during the Warring States Period (476-220 BC)/the Former Zhao 前趙 (304-329) and Later Zhao 後趙 (319-350), states of the Sixteen Kingdoms/
甄 甄 [Zhen1] /surname Zhen/
鄭 郑 [Zheng4] /Zheng state during the Warring States period/surname Zheng/abbr. for 鄭州|郑州[Zheng4 zhou1]/
帙 帙 [Zhi4] /surname Zhi/
摯 挚 [Zhi4] /surname Zhi/
支 支 [Zhi1] /surname Zhi/
袟 袟 [Zhi4] /surname Zhi/
郅 郅 [Zhi4] /surname Zhi/
直 直 [Zhi2] /surname Zhi/Zhi (c. 2000 BC), fifth of the legendary Flame Emperors 炎帝[Yan2 di4] descended from Shennong 神農|神农[Shen2 nong2] Farmer God/
中 中 [Zhong1] /China/Chinese/surname Zhong/
仲 仲 [Zhong4] /surname Zhong/
鍾 钟 [Zhong1] /surname Zhong/
籀 籀 [Zhou4] /surname Zhou/
周 周 [Zhou1] /surname Zhou/Zhou Dynasty (1046-256 BC)/
壴 壴 [Zhu4] /surname Zhu/
朱 朱 [Zhu1] /surname Zhu/
洙 洙 [Zhu1] /surname Zhu/
祝 祝 [Zhu4] /surname Zhu/
諸 诸 [Zhu1] /surname Zhu/
邾 邾 [Zhu1] /surname Zhu/
竺 竺 [Zhu2] /surname Zhu/abbr. for 天竺[Tian1 zhu2] India (esp. in Tang or Buddhist context)/Buddhism (archaic)/
顓 颛 [Zhuan1] /surname Zhuan/
鱄 鱄 [Zhuan1] /surname Zhuan/
莊 庄 [Zhuang1] /surname Zhuang/
諸葛 诸葛 [Zhu1 ge3] /two-character surname Zhuge/
騅 骓 [Zhui1] /surname Zhui/
卓 卓 [Zhuo2] /surname Zhuo/
菑 菑 [Zi1] /field recently opened for cultivation/surname Zi/
訾 訾 [Zi1] /surname Zi/
宗 宗 [Zong1] /surname Zong/
棸 棸 [Zou1] /surname Zou/
鄹 鄹 [Zou1] /name of a state/surname Zou/
騶 驺 [Zou1] /surname Zou/
鯫 鲰 [Zou1] /surname Zou/
鄒 邹 [Zou1] /surname Zou/vassal state during the Zhou Dynasty (1046-256 BC) in the southeast of Shandong Province/
祖 祖 [Zu3] /surname Zu/
組 组 [Zu3] /surname Zu/
坐 坐 [Zuo4] /surname Zuo/
左 左 [Zuo3] /surname Zuo/
里 里 [Li3] /Li (surname)/
烏梁海 乌梁海 [Wu1 liang2 hai3] /Mongol surname/
烏良哈 乌良哈 [Wu1 liang2 ha3] /Mongol surname/
喬答摩 乔答摩 [Qiao2 da1 mo2] /Gautama, surname of the Siddhartha, the historical Buddha/
瞿曇 瞿昙 [Qu2 tan2] /Gautama, surname of the Siddhartha, the historical Buddha/
賜姓 赐姓 [ci4 xing4] /to bestow a surname (of emperor conferring favor on ethnic group)/
阿多諾 阿多诺 [A1 duo1 nuo4] /surname Adorno/Theodor Ludwig Wiesengrund Adorno 狄奧多·阿多諾|狄奥多·阿多诺[Di2 ao4 duo1 · A1 duo1 nuo4] (1903-1969), German sociologist, philosopher, musicologist, and composer/
阿拉塔斯 阿拉塔斯 [A1 la1 ta3 si1] /surname Alatas/Ali Alatas (1932-2008), Indonesian foreign minister (1988-1999)/
阿爾都塞 阿尔都塞 [A1 er3 dou1 sai1] /surname Althusser/Louis Pierre Althusser 路易·皮埃爾·阿爾都塞|路易·皮埃尔·阿尔都塞[Lu4 yi4 · Pi2 ai1 er3 · A1 er3 dou1 sai1] (1918-1990), Marxist philosopher/
阿奎納 阿奎纳 [A1 kui2 na4] /surname Aquinas/Thomas Aquinas 托馬斯·阿奎納|托马斯·阿奎纳[Tuo1 ma3 si1 · A1 kui2 na4] (1225-1274)/
阿姆斯特朗 阿姆斯特朗 [A1 mu3 si1 te4 lang3] /surname Armstrong/
阿羅約 阿罗约 [A1 luo2 yue1] /surname Arroyo/
阿什拉維 阿什拉维 [A1 shen2 la1 wei2] /surname Ashrawi/Hanan Daoud Khalil Ashrawi (1946-), Palestinian scholar and political activist/
邱吉爾 邱吉尔 [Qiu1 ji2 er3] /Winston Churchill (1874-1965), UK politican and prime minister 1940-1945 and 1951-1955/surname Churchill/
富蘭克林 富兰克林 [Fu4 lan2 ke4 lin2] /Franklin/Benjamin Franklin (1706-1790), US Founding Father, scientist and author/surname Franklin/
福祿貝爾 福禄贝尔 [Fu2 lu4 bei4 er3] /surname Fröbel or Froebel/Friedrich Wilhelm August Fröbel (1782-1852), German pedagogue/
尼克松 尼克松 [Ni2 ke4 song1] /Richard Nixon (1913-1994), US politician, President 1969-1974/surname Nixon/
波羅 波罗 [Bo1 luo2] /Polo (car made by Volkswagen)/surname Polo/
萊佛士 莱佛士 [Lai2 fo2 shi4] /Stamford Raffles (1781-1826), British statesman and founder of the city of Singapore/surname Raffles/
川普 川普 [Chuan1 pu3] /Sichuanese pidgin (the mix of Standard Mandarin and Sichuanese dialect)/(Tw) surname Trump/
大久保 大久保 [Da4 jiu3 bao3] /Japanese surname and place name Oukubo/
三浦 三浦 [San1 pu3] /Miura (Japanese surname and place name)/
上田 上田 [Shang4 tian2] /Ueda (Japanese surname and place name)/
中島 中岛 [Zhong1 dao3] /Nakajima or Nakashima (Japanese surname and place name)/
中川 中川 [Zhong1 chuan1] /Nakagawa (Japanese surname and place name)/
中野 中野 [Zhong1 ye3] /Nakano (Japanese surname and place name)/
丸山 丸山 [Wan2 shan1] /Maruyama (Japanese surname and place name)/
佐野 佐野 [Zuo3 ye3] /Sano (Japanese surname and place name)/
千葉 千叶 [Qian1 ye4] /Chiba (Japanese surname and place name)/
吉田 吉田 [Ji2 tian2] /Yoshida (Japanese surname and place name)/
吉野 吉野 [Ji2 ye3] /Yoshino (Japanese surname and place name)/
和田 和田 [He2 tian2] /Hoten or Khotan city and prefecture in Xinjiang/Wada (Japanese surname and place name)/
坂井 坂井 [Ban3 jing3] /Sakai (Japanese surname and place name)/
大野 大野 [Da4 ye3] /Ōno (Japanese surname and place name)/
宮崎 宫崎 [Gong1 qi2] /Miyazaki (Japanese surname and place name)/
小島 小岛 [Xiao3 dao3] /Kojima (Japanese surname and place name)/
小野 小野 [Xiao3 ye3] /Ono (Japanese surname and place name)/
岡本 冈本 [Gang1 ben3] /Okamoto (Japanese surname and place name)/
成田 成田 [Cheng2 tian2] /Narita (Japanese surname and place name)/
松尾 松尾 [Song1 wei3] /Matsuo (Japanese surname and place name)/
松本 松本 [Song1 ben3] /Matsumoto (Japanese surname and place name)/
柴田 柴田 [Chai2 tian2] /Shibata (Japanese surname and place name)/
植田 植田 [Zhi2 tian2] /Ueda (Japanese surname and place name)/
橋本 桥本 [Qiao2 ben3] /Hashimoto (Japanese surname and place name)/
櫻井 樱井 [Ying1 jing3] /Sakurai (Japanese surname and place name)/
清水 清水 [Qing1 shui3] /Qingshui (place name)/Shimizu (Japanese surname and place name)/
田村 田村 [Tian2 cun1] /Tamura (Japanese surname and place name)/
石川 石川 [Shi2 chuan1] /Ishikawa (Japanese surname and place name)/
石田 石田 [Shi2 tian2] /Ishida (Japanese surname and place name)/
福島 福岛 [Fu2 dao3] /Fukushima (Japanese surname and place name)/
菊池 菊池 [Ju2 chi2] /Kikuchi (Japanese surname and place name)/
藤澤 藤泽 [Teng2 ze2] /Fujisawa (Japanese surname and place name)/
山口 山口 [Shan1 kou3] /Yamaguchi (Japanese surname and place name)/Yamaguchi prefecture in southwest of Japan's main island Honshū 本州[Ben3 zhou1]/
巴爾的摩 巴尔的摩 [Ba1 er3 di4 mo2] /Baltimore (place name, surname etc)/
拉青格 拉青格 [La1 qing1 ge2] /Ratzinger (German surname of Pope Benedict XVI)/
老 老 [lao3] /prefix used before the surname of a person or a numeral indicating the order of birth of the children in a family or to indicate affection or familiarity/old (of people)/venerable (person)/experienced/of long standing/always/all the time/of the past/very/outdated/(of meat etc) tough/
前橋 前桥 [Qian2 qiao2] /Maebashi (surname or place name)/
三田 三田 [San1 tian2] /Mita, Sanda, Mitsuda etc (Japanese surname or place name)/
複姓 复姓 [fu4 xing4] /two-character surname such as 司馬|司马 or 諸葛|诸葛/
五百年前是一家 五百年前是一家 [wu3 bai3 nian2 qian2 shi4 yi1 jia1] /five hundred years ago we were the same family (idiom) (said of persons with the same surname)/
列治文 列治文 [Lie4 zhi4 wen2] /Richmond (place name or surname)/
某人 某人 [mou3 ren2] /someone/a certain person/some people/I (self-address after one's surname)/
里奇蒙 里奇蒙 [Li3 qi2 meng2] /Richmond (place name or surname)/
上野 上野 [Shang4 ye3] /Ueno, district in Taitō Ward, Tokyo/Ueno (Japanese surname)/
中山 中山 [Zhong1 shan1] /refers to Dr Sun Yat-sen/Zhongshan, prefecture-level city in Guangdong, close to Sun Yat-sen's birthplace/Nakayama (Japanese surname)/
中村 中村 [Zhong1 cun1] /Nakamura (Japanese surname)/
久保 久保 [Jiu3 bao3] /Kubo (Japanese surname)/
今井 今井 [Jin1 jing3] /Imai (Japanese surname)/
佐佐木 佐佐木 [Zuo3 zuo3 mu4] /Sasaki (Japanese surname)/
佐藤 佐藤 [Zuo3 teng2] /Satō (Japanese surname)/
內田 内田 [Nei4 tian2] /Uchida (Japanese surname)/
前田 前田 [Qian2 tian2] /Maeda (Japanese surname)/
加藤 加藤 [Jia1 teng2] /Katō (Japanese surname)/
原 原 [Yuan2] /Hara (Japanese surname)/
原田 原田 [Yuan2 tian2] /Harada (Japanese surname)/
坂本 坂本 [Ban3 ben3] /Sakamoto (Japanese surname)/
增田 增田 [Zeng1 tian2] /Masuda (Japanese surname)/
大塚 大冢 [Da4 zhong3] /Ōtsuka (Japanese surname)/
大西 大西 [Da4 xi1] /Ōnishi (Japanese surname)/
太田 太田 [Tai4 tian2] /Ohta or Ōta (Japanese surname)/
安倍 安倍 [An1 bei4] /Abe (Japanese surname)/
安藤 安藤 [An1 teng2] /Andō (Japanese surname)/
宮本 宫本 [Gong1 ben3] /Miyamoto (Japanese surname)/
小川 小川 [Xiao3 chuan1] /Ogawa (Japanese surname)/
小林 小林 [Xiao3 lin2] /Kobayashi (Japanese surname)/
小淵 小渊 [Xiao3 yuan1] /Obuchi (Japanese surname)/
山下 山下 [Shan1 xia4] /Yamashita (Japanese surname)/
山崎 山崎 [Shan1 qi2] /Yamazaki or Yamasaki (Japanese surname)/
山本 山本 [Shan1 ben3] /Yamamoto (Japanese surname)/
山田 山田 [Shan1 tian2] /Yamada (Japanese surname)/
岡田 冈田 [Gang1 tian2] /Okada (Japanese surname)/
岩崎 岩崎 [Yan2 qi2] /Iwasaki (Japanese surname)/
工藤 工藤 [Gong1 teng2] /Kudō (Japanese surname)/
平野 平野 [Ping2 ye3] /Hirano (Japanese surname)/
後藤 后藤 [Hou4 teng2] /Gotō (Japanese surname)/
新井 新井 [Xin1 jing3] /Arai (Japanese surname)/
木下 木下 [Mu4 xia4] /Kinoshita (Japanese surname)/
木村 木村 [Mu4 cun1] /Kimura (Japanese surname)/
杉山 杉山 [Shan1 shan1] /Sugiyama (Japanese surname)/
杉本 杉本 [Shan1 ben3] /Sugimoto (Japanese surname)/
村上 村上 [Cun1 shang4] /Murakami (Japanese surname)/
村田 村田 [Cun1 tian2] /Murata (Japanese surname)/
松井 松井 [Song1 jing3] /Matsui (Japanese surname)/
松田 松田 [Song1 tian2] /Matsuda (Japanese surname)/
森 森 [Sen1] /Mori (Japanese surname)/
森田 森田 [Sen1 tian2] /Morita (Japanese surname)/
橫山 横山 [Heng2 shan1] /Hengshan County in Yulin 榆林[Yu2 lin2], Shaanxi/Hengshan township in Hsinchu County 新竹縣|新竹县[Xin1 zhu2 Xian4], northwest Taiwan/Yokoyama (Japanese surname)/
武田 武田 [Wu3 tian2] /Takeda (Japanese surname)/
池田 池田 [Chi2 tian2] /Ikeda (Japanese surname)/
渡邊 渡边 [Du4 bian1] /Watanabe (Japanese surname)/
田中 田中 [Tian2 zhong1] /Tienchung town in Changhua county 彰化縣|彰化县[Zhang1 hua4 xian4], Taiwan/Tanaka (Japanese surname)/
石井 石井 [Shi2 jing3] /Ishii (Japanese surname)/
福田 福田 [Fu2 tian2] /Futian district of Shenzhen City 深圳市, Guangdong/Fukuda (Japanese surname)/
竹內 竹内 [Zhu2 nei4] /Takeuchi (Japanese surname)/
荒井 荒井 [Huang1 jing3] /Arai (Japanese surname)/
菅原 菅原 [Jian1 yuan2] /Sugawara (Japanese surname)/
藤井 藤井 [Teng2 jing3] /Fujii (Japanese surname)/
藤原 藤原 [Teng2 yuan2] /Fujiwara (Japanese surname)/
藤本 藤本 [Teng2 ben3] /Fujimoto (Japanese surname)/
藤田 藤田 [Teng2 tian2] /Fujita (Japanese surname)/
藤野 藤野 [Teng2 ye3] /Fujino (Japanese surname)/
西村 西村 [Xi1 cun1] /Nishimura (Japanese surname)/
谷口 谷口 [Gu3 kou3] /Taniguchi (Japanese surname)/
近藤 近藤 [Jin4 teng2] /Kondō (Japanese surname)/
遠藤 远藤 [Yuan3 teng2] /Endō (Japanese surname)/
酒井 酒井 [Jiu3 jing3] /Sakai (Japanese surname)/
野口 野口 [Ye3 kou3] /Noguchi (Japanese surname)/
野村 野村 [Ye3 cun1] /Nomura (Japanese surname)/
金子 金子 [Jin1 zi3] /Kaneko (Japanese surname)/
鈴木 铃木 [Ling2 mu4] /Suzuki (Japanese surname)/
長谷川 长谷川 [Chang2 gu3 chuan1] /Hasegawa (Japanese surname)/
青木 青木 [Qing1 mu4] /Aoki (Japanese surname)/
高木 高木 [Gao1 mu4] /Takagi (Japanese surname)/
高橋 高桥 [Gao1 qiao2] /Takahashi (Japanese surname)/
高田 高田 [Gao1 tian2] /Takada (Japanese surname)/
齋藤 斋藤 [Zhai1 teng2] /Saitō (Japanese surname)/
佛洛斯特 佛洛斯特 [Fu2 luo4 si1 te4] /Frost (surname)/
哈蒙德 哈蒙德 [Ha1 meng2 de2] /Hammond (surname)/
布坎南 布坎南 [Bu4 kan3 nan2] /Buchanan (surname)/
弗格森 弗格森 [Fu2 ge2 sen1] /Ferguson (surname)/
弗里曼 弗里曼 [Fu2 li3 man4] /Freeman (surname)/
斯佩羅 斯佩罗 [Si1 pei4 luo2] /Spero (surname)/
普羅迪 普罗迪 [Pu3 luo2 di2] /Prodi (surname)/
本內特 本内特 [Ben3 nei4 te4] /Bennett (surname)/
波特 波特 [Bo1 te4] /Potter or Porter (surname)/
海德 海德 [Hai3 de2] /Hyde (surname)/
納什 纳什 [Na4 shi2] /Nash (surname)/
考克斯 考克斯 [Kao3 ke4 si1] /Cox (surname)/
萊特 莱特 [Lai2 te4] /Wright (surname)/
蒙哥馬利 蒙哥马利 [Meng2 ge1 ma3 li4] /Bernard Montgomery (Montie) (1887-1976), Second World War British field marshal/Montgomery or Montgomerie (surname)/
貝內特 贝内特 [Bei4 nei4 te4] /Bennett (surname)/
馬斯洛 马斯洛 [Ma3 si1 luo4] /Maslow (surname)/Abraham Maslow (1908-1970), US psychologist/
藤森 藤森 [Teng2 sen1] /Fujimori (Japanese surname)/Alberto Ken'ya Fujimori (1938-), president of Peru 1990-2000/
班克斯 班克斯 [Ban1 ke4 si1] /Banks (surname)/Banksy (UK artist)/
諾伊曼 诺伊曼 [Nuo4 yi1 man4] /Neumann (surname)/John von Neumann (1903-1957), Hungarian-born American mathematician and polymath/
強生 强生 [Qiang2 sheng1] /Johnson (surname)/Johnson & Johnson (company)/
柏崎 柏崎 [Bai3 qi2] /Kashiwazaki (Japanese surname)/Kashiwazaki, town in Niigata prefecture, Japan/Kashiwazaki, title of a Noh play/
迪士尼 迪士尼 [Di2 shi4 ni2] /Disney (company name, surname)/Walt Disney (1901-1966), American animator and film producer/
惠特曼 惠特曼 [Hui4 te4 man4] /Whitman (surname)/Walt Whitman (1819-1892), American poet and journalist/
迪斯尼 迪斯尼 [Di2 si1 ni2] /Disney (company name, surname)/also written 迪士尼[Di2 shi4 ni2]/
井上 井上 [Jing3 shang4] /Inoue (Japanese surname, pr. "ee-no-oo-ay")/
伊藤 伊藤 [Yi1 teng2] /Itō or Itoh, Japanese surname/
姓名 姓名 [xing4 ming2] /name and surname/CL:個|个[ge4]/
姓 姓 [xing4] /family name/surname/CL:個|个[ge4]/to be surnamed/
漢姓 汉姓 [Han4 xing4] /Han surname/Chinese surname/
百家姓 百家姓 [Bai3 jia1 xing4] /The Book of Family Names, anonymous Song dynasty reading primer listing 438 surnames/
#]]]'''#'''
import re
_line_regex = re.compile(r'^(?P<繁体>\S+) (?P<简体>\S+) \[(?P<拼音>[^][]*)\] /.*/$')
def 囗行变换囗(s, /):
    m = _line_regex.fullmatch(s)
    if m is None:raise 000
    繁体 = m['繁体']
    简体 = m['简体']
    拼音 = m['拼音']
    if 简体==繁体:
        简体 = ''
    assert not 'v' in 拼音
    assert not 'V' in 拼音
    拼音 = 拼音.lower().replace(' ', '-').replace('u:', 'v')
    x = ':'.join([繁体, 简体, 拼音])
    return x
def 囗提取囗(case, /):
    txt = 囗待进一步处理文本囗人工编辑结果
    _, body = txt.split('===begin:\n')
    data, _ = body.split('\n賜姓 赐姓')
    ls = data.split('\n')
    assert len(ls) == 765
    xs = [*map(囗行变换囗, ls)]
    if case == 1:
        return xs
    new = '\n'.join(xs)
    if case == 2:
        return new
    if case == 3:
        return new, xs
中英词典囗姓氏囗繁简对照囗带拼音囗囗文本 = 囗提取囗(2)
囗中英词典囗姓氏囗繁简对照囗带拼音囗囗文本囗 = r'''
艾::ai4
安::an1
卬::ang2
敖::ao2
仈::ba1
巴::ba1
白::bai2
百::bai3
柏::bai3
百里::bai3-li3
班::ban1
包::bao1
暴::bao4
鮑:鲍:bao4
貝:贝:bei4
賁:贲:ben1
畢:毕:bi4
邲::bi4
卞::bian4
別:别:bie2
秉::bing3
邴::bing3
薄::bo2
卜::bu3
步::bu4
蔡::cai4
蒼:苍:cang1
曹::cao2
策::ce4
岑::cen2
柴::chai2
常::chang2
昌::chang1
萇:苌:chang2
巢::chao2
晁::chao2
鼂::chao2
車:车:che1
臣::chen2
諶:谌:chen2
陳:陈:chen2
乘::cheng2
成::cheng2
晟::cheng2
澄::cheng2
程::cheng2
承::cheng2
郕::cheng2
庱::cheng3
池::chi2
蚩::chi1
遲:迟:chi2
郗::chi1
崇::chong2
丑::chou3
褚::chu3
鄐::chu4
儲:储:chu3
楚::chu3
釧:钏:chuan4
淳于::chun2-yu2
春::chun1
佽::ci4
從:从:cong2
琮::cong2
爨::cuan4
崔::cui1
錯:错:cuo4
笪::da2
達:达:da2
戴::dai4
亶::dan3
黨:党:dang3
刀::dao1
鄧:邓:deng4
邸::di3
鞮::di1
狄::di2
翟::di2
甸::dian4
刁::diao1
丁::ding1
東:东:dong1
董::dong3
鼕:冬:dong1
東方:东方:dong1-fang1
東郭:东郭:dong1-guo1
竇:窦:dou4
杜::du4
都::du1
段::duan4
端木::duan1-mu4
兌:兑:dui4
鈬::duo2
鐸:铎:duo2
鄂::e4
耏::er2
樊::fan2
范::fan4
坊::fang1
房::fang2
方::fang1
斐::fei3
費:费:fei4
封::feng1
豐:丰:feng1
酆::feng1
馮:冯:feng2
鳳:凤:feng4
付::fu4
伏::fu2
傅::fu4
富::fu4
符::fu2
福::fu2
賅:赅:gai1
乾:干:gan1
甘::gan1
港::gang3
高::gao1
郜::gao4
戈::ge1
葛::ge3
蓋:盖:ge3
鬲::ge2
耿::geng3
宮:宫:gong1
弓::gong1
貢:贡:gong4
龔:龚:gong1
公孫:公孙:gong1-sun1
勾::gou1
緱:缑:gou1
苟::gou3
古::gu3
谷::gu3
辜::gu1
顧:顾:gu4
冠::guan4
官::guan1
筦::guan3
管::guan3
觀:观:guan4
關:关:guan1
廣:广:guang3
歸:归:gui1
炅::gui4
炔::gui4
桂::gui4
邽::gui1
媯:妫:gui1
穀梁:谷梁:gu3-liang2
咼:呙:guo1
國:国:guo2
虢::guo2
過:过:guo4
郭::guo1
海::hai3
翰::han4
韓:韩:han2
杭::hang2
昊::hao4
郝::hao3
何::he2
佫::he4
賀:贺:he4
和::he2
赫::he4
恆:恒:heng2
洪::hong2
紅:红:hong2
訇::hong1
閎:闳:hong2
侯::hou2
后::hou4
郈::hou4
忽::hu1
扈::hu4
胡::hu2
滹::hu1
滑::hua2
花::hua1
華:华:hua4
懷:怀:huai2
奐:奂:huan4
宦::huan4
桓::huan2
環:环:huan2
還:还:huan2
黃:黄:huang2
皇::huang2
皇甫::huang2-fu3
惠::hui4
火::huo3
霍::huo4
丌::ji1
冀::ji4
姞::ji2
季::ji4
戢::ji2
機:机:ji1
汲::ji2
稽::ji1
籍::ji2
藉::ji2
計:计:ji4
吉::ji2
紀:纪:ji3
薊:蓟:ji4
姬::ji1
嵇::ji1
佳::jia1
加::jia1
嘉::jia1
家::jia1
賈:贾:jia3
駕:驾:jia4
剪::jian3
籛:篯:jian1
翦::jian3
蕑::jian1
諫:谏:jian4
蹇::jian3
姜::jiang1
江::jiang1
薑:姜:jiang1
蔣:蒋:jiang3
姣::jiao1
教::jiao4
焦::jiao1
皦::jiao3
矯:矫:jiao3
蟜::jiao3
郊::jiao1
靳::jin4
金::jin1
晉:晋:jin4
井::jing3
景::jing3
經:经:jing1
靖::jing4
京::jing1
樛::jiu1
居::ju1
苴::ju1
鞠::ju1
涓::juan1
雋:隽:juan4
傕::jue2
矍::jue2
角::jue2
凱:凯:kai3
闞:阚:kan4
康::kang1
亢::kang4
恪::ke4
柯::ke1
孔::kong3
噲:哙:kuai4
鄶:郐:kuai4
寬:宽:kuan1
匡::kuang1
鄺:邝:kuang4
匱:匮:kui4
夔::kui2
蕢:蒉:kui4
隗::kui2
賴:赖:lai4
藍:蓝:lan2
蘭:兰:lan2
郎::lang2
郞::lang2
嫪::lao4
樂:乐:le4
嫘::lei2
纍:累:lei2
雷::lei2
冷::leng3
利::li4
力::li4
勵:励:li4
厲:厉:li4
李::li3
栗::li4
澧::li3
立::li4
離:离:li2
黎::li2
禮:礼:li3
酈:郦:li4
廉::lian2
連:连:lian2
梁::liang2
僚::liao2
廖::liao4
藺:蔺:lin4
遴::lin2
林::lin2
凌::ling2
泠::ling2
令狐::ling2-hu2
劉:刘:liu2
柳::liu3
龍:龙:long2
隆::long2
樓:楼:lou2
婁:娄:lou2
潞::lu4
路::lu4
逯::lu4
錄:录:lu4
陸:陆:lu4
露::lu4
魯:鲁:lu3
盧:卢:lu2
甪::lu4
欒:栾:luan2
羅:罗:luo2
駱:骆:luo4
洛::luo4
呂:吕:lv3
律::lv4
鑢::lv4
麻::ma2
馬:马:ma3
麥:麦:mai4
嫚::man4
冒::mao4
毛::mao2
茅::mao2
枚::mei2
梅::mei2
門:门:men2
孟::meng4
蒙::meng2
宓::mi4
禰:祢:mi2
米::mi3
糜::mi2
羋:芈:mi3
麋::mi2
密::mi4
繆:缪:miao4
苗::miao2
民::min2
閔:闵:min3
明::ming2
莫::mo4
鄚::mo4
墨::mo4
万俟::mo4-qi2
牟::mou2
木::mu4
牧::mu4
穆::mu4
慕容::mu4-rong2
納:纳:na4
那::na1
南::nan2
南郭::nan2-guo1
淖::nao4
能::neng2
倪::ni2
年::nian2
聶:聂:nie4
齧::nie4
寧:宁:ning2
牛::niu2
鈕:钮:niu3
農:农:nong2
那::nuo2
區:区:ou1
歐:欧:ou1
毆:殴:ou1
歐陽:欧阳:ou1-yang2
怕::pa4
番::pan1
潘::pan1
尨::pang2
逄::pang2
龐:庞:pang2
裴::pei2
彭::peng2
蓬::peng2
皮::pi2
裨::pi2
邳::pi1
扁::pian1
駢:骈:pian2
朴::piao2
平::ping2
頗:颇:po1
浦::pu3
溥::pu3
濮::pu2
蒲::pu2
亓::qi2
戚::qi1
盵::qi4
祁::qi2
齊:齐:qi2
杞::qi3
岐::qi2
乾::qian2
錢:钱:qian2
強:强:qiang2
槍:枪:qiang1
羌::qiang1
喬:乔:qiao2
譙:谯:qiao2
郄::qie4
欽:钦:qin1
覃::qin2
秦::qin2
清::qing1
黥::qing2
丘::qiu1
仇::qiu2
盚::qiu2
秋::qiu1
糗::qiu3
裘::qiu2
邱::qiu1
佉::qu1
屈::qu1
曲::qu1
朐::qu2
渠::qu2
璩::qu2
瞿::qu2
蘧::qu2
麯::qu1
麴::qu1
全::quan2
權:权:quan2
闕:阙:que1
冉::ran3
穰::rang2
饒:饶:rao2
任::ren4
容::rong2
戎::rong2
榮:荣:rong2
肜::rong2
孺::ru2
茹::ru2
阮::ruan3
芮::rui4
薩:萨:sa4
三::san1
桑::sang1
沙::sha1
單:单:shan4
山::shan1
閃:闪:shan3
商::shang1
尚::shang4
上官::shang4-guan1
劭::shao4
卲::shao4
紹:绍:shao4
韶::shao2
召::shao4
邵::shao4
佘::she2
厙:厍:she4
舍::she4
申::shen1
瞫::shen3
莘::shen1
沈::shen3
盛::sheng4
申屠::shen1-tu2
世::shi4
史::shi3
士::shi4
奭::shi4
室::shi4
師:师:shi1
施::shi1
時:时:shi2
石::shi2
適:适:shi4
壽:寿:shou4
束::shu4
殳::shu1
疏::shu1
舒::shu1
耍::shua3
帥:帅:shuai4
雙:双:shuang1
水::shui3
司::si1
姒::si4
司寇::si1-kou4
司馬:司马:si1-ma3
司徒::si1-tu2
松::song1
宋::song4
宿::su4
粟::su4
肅:肃:su4
蔌::su4
蘇:苏:su1
眭::sui1
睢::sui1
隋::sui2
隨:随:sui2
孫:孙:sun1
妁::shuo4
索::suo3
沓::ta4
禢::ta4
台::tai2
邰::tai2
檀::tan2
潭::tan2
澹::tan2
覃::tan2
談:谈:tan2
譚:谭:tan2
鐔:镡:tan2
郯::tan2
唐::tang2
湯:汤:tang1
陶::tao2
滕::teng2
題:题:ti2
田::tian2
鐵:铁:tie3
佟::tong2
彤::tong2
童::tong2
鈄:钭:tou3
土::tu3
屠::tu2
徒::tu2
涂::tu2
拓::tuo4
媧:娲:wa1
宛::wan3
萬:万:wan4
汪::wang1
王::wang2
危::wei1
圍:围:wei2
委::wei3
寪::wei3
尉::wei4
維:维:wei2
薳::wei3
謂:谓:wei4
隗::wei3
韋:韦:wei2
微::wei1
魏::wei4
衛:卫:wei4
文::wen2
溫:温:wen1
聞:闻:wen2
甕:瓮:weng4
翁::weng1
仵::wu3
伍::wu3
兀::wu4
吾::wu2
武::wu3
毋::wu2
烏:乌:wu1
巫::wu1
鄔:邬:wu1
吳:吴:wu2
郄::xi4
僖::xi1
奚::xi1
席::xi2
昔::xi1
羲::xi1
習:习:xi2
郤::xi4
隰::xi2
夏::xia4
冼::xian3
咸::xian2
向::xiang4
相::xiang1
襄::xiang1
項:项:xiang4
蕭:萧:xiao1
肖::xiao1
渫::xie4
燮::xie4
解::xie4
謝:谢:xie4
頡:颉:xie2
西門:西门:xi1-men2
新::xin1
辛::xin1
鄩::xin2
刑::xing2
幸::xing4
興:兴:xing1
邢::xing2
敻::xiong4
熊::xiong2
休::xiu1
修::xiu1
徐::xu2
盱::xu1
胥::xu1
藇::xu4
許:许:xu3
鄦::xu3
宣::xuan1
禤::xuan1
軒:轩:xuan1
軒轅:轩辕:xuan1-yuan2
雪::xue3
薛::xue1
荀::xun2
衙::ya2
軋:轧:ya4
偃::yan3
傿::yan1
嚴:严:yan2
奄::yan3
延::yan2
晏::yan4
沇::yan3
燕::yan1
閆:闫:yan2
閻:阎:yan2
顏:颜:yan2
鄢::yan1
仰::yang3
揚:扬:yang2
楊:杨:yang2
羊::yang2
么:幺:yao1
姚::yao2
搖:摇:yao2
瑤:瑶:yao2
銚:铫:yao2
堯:尧:yao2
也::ye3
業:业:ye4
葉:叶:ye4
鄴:邺:ye4
佚::yi4
宜::yi2
扆::yi3
益::yi4
齮::yi3
義:义:yi4
伊::yi1
易::yi4
翼::yi4
羿::yi4
尹::yin3
誾:訚:yin2
闉::yin1
陰:阴:yin1
印::yin4
殷::yin1
嬴::ying2
應:应:ying4
穎:颖:ying3
雍::yong1
鄘::yong1
尤::you2
游::you2
于::yu2
余::yu2
俞::yu2
喻::yu4
禹::yu3
紆:纡:yu1
臾::yu2
虞::yu2
遇::yu4
遹::yu4
邘::yu2
郁::yu4
餘:馀:yu2
鬱:郁:yu4
魚:鱼:yu2
楀::yu3
於::yu1
庾::yu3
蔚::yu4
園:园:yuan2
爰::yuan2
苑::yuan4
蜎::yuan1
袁::yuan2
元::yuan2
尉遲:尉迟:yu4-chi2
岳::yue4
嶽:岳:yue4
樂:乐:yue4
惲:恽:yun4
雲:云:yun2
宇文::yu3-wen2
昝::zan3
臧::zang1
曾::zeng1
繒:缯:zeng1
鄫::zeng2
查::zha1
霅::zha2
祭::zhai4
翟::zhai2
展::zhan3
湛::zhan4
詹::zhan1
仉::zhang3
張:张:zhang1
章::zhang1
長孫:长孙:zhang3-sun1
兆::zhao4
炤::zhao4
趙:赵:zhao4
甄::zhen1
鄭:郑:zheng4
帙::zhi4
摯:挚:zhi4
支::zhi1
袟::zhi4
郅::zhi4
直::zhi2
中::zhong1
仲::zhong4
鍾:钟:zhong1
籀::zhou4
周::zhou1
壴::zhu4
朱::zhu1
洙::zhu1
祝::zhu4
諸:诸:zhu1
邾::zhu1
竺::zhu2
顓:颛:zhuan1
鱄::zhuan1
莊:庄:zhuang1
諸葛:诸葛:zhu1-ge3
騅:骓:zhui1
卓::zhuo2
菑::zi1
訾::zi1
宗::zong1
棸::zou1
鄹::zou1
騶:驺:zou1
鯫:鲰:zou1
鄒:邹:zou1
祖::zu3
組:组:zu3
坐::zuo4
左::zuo3
里::li3
烏梁海:乌梁海:wu1-liang2-hai3
烏良哈:乌良哈:wu1-liang2-ha3
喬答摩:乔答摩:qiao2-da1-mo2
瞿曇:瞿昙:qu2-tan2
'''.strip()#end:囗中英词典囗姓氏囗繁简对照囗带拼音囗囗文本囗'''
assert 中英词典囗姓氏囗繁简对照囗带拼音囗囗文本 == 囗中英词典囗姓氏囗繁简对照囗带拼音囗囗文本囗

if __name__ == "__main__":
    pass
__all__


from script.字词典囗姓氏提取囗二囗 import *


