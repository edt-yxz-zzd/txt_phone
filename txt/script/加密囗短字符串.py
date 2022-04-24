r'''

[[[
加密网页 第二版？
e script/加密囗短字符串.py

[[以前:
加密网页 第一版？
  == 呜呼哀哉尚飨加密 第二版


呜呼哀哉尚飨加密 第二版摘要:
  view ./others/数学/编程/呜呼哀哉尚飨加密/呜呜呼哀哉尚飨v2.txt
加密页面:
  view html_js/呜呼哀哉尚飨加密.html
    20220424 <==> view html_js/呜呼哀哉尚飨加密v2_1.html
加密脚本:
  view ./script/whazsx.py

加密脚本不同语言实现的网页展示:
  view ./others/数学/编程/呜呼哀哉尚飨加密/呜呼哀哉尚飨加密.js[v2_1].html
  view ./others/数学/编程/呜呼哀哉尚飨加密/呜呼哀哉尚飨加密.py[v2_2].html
    $ python whazsx.py a/b/c -d -i abc -m 1 -n 10 -k0 'abc' | python whazsx.py a/b/c -m 0 -n 10 -k0 'abc'


===
!mkdir ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/
!mkdir ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/首两版囗收集于20220424/
!mkdir ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/首两版囗收集于20220424/phone_txt__others__数学__编程/
!mkdir ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/首两版囗收集于20220424/phone_txt__script/
!mkdir ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/首两版囗收集于20220424/phone_txt__html_js/

!cp -r ./others/数学/编程/呜呼哀哉尚飨加密/   ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/首两版囗收集于20220424/phone_txt__others__数学__编程/
!cp ./script/whazsx.py       ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/首两版囗收集于20220424/phone_txt__script/
!cp ./html_js/呜呼*      ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/首两版囗收集于20220424/phone_txt__html_js/

e ../../python3_src/nn_ns/app/呜呼哀哉尚飨加密/首两版囗收集于20220424/ReadMe__呜呼哀哉尚飨加密_首两版囗收集于20220424.txt
]]

[[TODO:
加密网页 第二版？
加密网页 新版
  可参考 呜呜呼哀哉尚飨v2:『费力指数』『密码提示』
    『费力指数』:增加计算『里密钥』的运算量
    『密码提示』:格式『提示前缀/源密码本体/提示后缀』，提示双缀 会直接(?似乎可浅变换)出现在『表密文』中

  项目需求源于: 保存 ghp_/PAT #github 私人授权令牌
    #不同于以往:
    #   『用户口令』为用户自选，可自行设定『提示』，自定义统一生成函数::提示->版本->用户口令
    #   『ghp_/PAT』为网站所选，用户只能加密保存
    #

  加解密共有输入:
    源密钥
      =用户口令::[str]
      +源明文前后缀::(str, str)
      +源明文必含片段::{str}
      +源明文高频片段::{str}
      +其他密钥相关信息(网址,用户名,密码有效期起讫,...) ::{str:str}

  加密专有输入:
    * 以下 近乎出现在『表密文』
      字节串加解密算法名称及版本
      密文字符集名称及版本
      费力指数::uint
      用户口令提示前后缀及中间关键字::(str, [str], str)
      其他密钥相关信息关键字::[str]

    * 以下 不出现在『表密文』，即经过『源密钥』处理
      源明文::str
  加密输出:
    Either 出错信息 表密文::str
  解密专有输入:
    表密文::str
  解密输出:
    Either 出错信息 源明文::str
  解密预处理囗提示:
    输入:
      表密文::str
    输出:
      用户口令提示前后缀及中间关键字::(str, [str], str)
      其他密钥相关信息关键字::[str]


  加密流程:
    检查输入
    出错:未知加解密算法|未知字符集

    密钥盐=生成随机字节串()
      #近乎出现在『表密文』
    密文盐=生成随机字节串()
      #不出现在『表密文』，即经过『源密钥』处理

    实心明文囗甲=去掉前后缀(源密钥.源明文前后缀，源明文)
    出错:双缀不匹配

    (实心明文囗转义序列囗乙，已替换片段)=换下片段(实心明文囗甲，源密钥.源明文必含片段\-/源密钥.源明文高频片段)
    出错:源明文必含片段未出现

    实心明文=实心明文囗转义序列囗乙

    实心明文囗字节串=字节串化囗统一码(实心明文)
    压实明文囗字节串=拟压缩囗字节串(实心明文囗字节串)

    里明文囗字节串=弱加密囗字节串(密文盐，压实明文囗字节串)
    咸里明文囗字节串=组合囗盐(密文盐，里明文囗字节串)
    污咸里明文囗字节串=随机加入可识别噪声(咸里明文囗字节串)
      #『实心明文』在此被随机粗加密/加盐
      #     以保证不同加密实例使用不同『里明文』
      #     难为『同一未知「里明文」=>(密钥甲，密文甲，密文乙)->密钥乙』
      #

    里密钥=构造里密钥(源密钥，密钥盐，费力指数)
      #『源密钥』在此被随机变换/加盐
      #     以保证不同加密实例使用不同『里密钥』
      #     难为『同一未知「里密钥」=>(明文甲，密文甲，密文乙)->明文乙』
      #

    里密文囗字节串=强加密囗字节串<字节串加解密算法名称及版本>(里密钥，污咸里明文囗字节串)
      #『密文盐』在此被『里密钥』加密
      #     以保证『实心明文』的加盐操作受『源密钥』保护
      #     是『实心明文』的加盐操作的组成部分
      #
    里密文=字符串化囗指定字符集(密文字符集名称及版本，里密文囗字节串)

    表密文=组合表密文(字节串加解密算法名称及版本，密文字符集名称及版本，费力指数，用户口令提示前后缀及中间关键字，其他密钥相关信息关键字，密钥盐，里密文)

  解密流程:
    (字节串加解密算法名称及版本，密文字符集名称及版本，费力指数，用户口令提示前后缀及中间关键字，其他密钥相关信息关键字，密钥盐，里密文)=拆分表密文(表密文)
    出错:拆分元组失败|未知加解密算法|未知字符集

    提示囗当用户进行交互式输入时:
      显示『用户口令提示前后缀及中间关键字』:
          格式:『用户口令:{前缀}({输入框}){关键字}({输入框}){关键字}({输入框})...{关键字}({输入框}){后缀}』

      显示『其他密钥相关信息关键字』:
          格式:『其他密钥相关信息:{关键字}({输入框}){关键字}({输入框})...{关键字}({输入框})』

      并要求用户填空。

    里密文囗字节串=字节串化囗指定字符集(密文字符集名称及版本，里密文)
    出错:编码失败囗非法字符

    里密钥=构造里密钥(源密钥，密钥盐，费力指数)
    污咸里明文囗字节串=强解密囗字节串<字节串加解密算法名称及版本>(里密钥，里密文囗字节串)
    出错:强解密失败

    咸里明文囗字节串=消除可识别噪声(污咸里明文囗字节串)
    出错:噪声分离失败囗噪声格式错误

    (密文盐，里明文囗字节串)=拆分囗盐(咸里明文囗字节串)
    出错:拆分有序对失败

    压实明文囗字节串=弱解密囗字节串(密文盐，里明文囗字节串)
    出错:弱解密失败

    实心明文囗字节串=拟解压囗字节串(压实明文囗字节串)

    实心明文=字符串化囗统一码(实心明文囗字节串)
    出错:解码失败囗非法字节序列

    实心明文囗转义序列囗乙=实心明文

    (实心明文囗甲，已替换片段)=换上片段(实心明文囗转义序列囗乙，源密钥.源明文必含片段\-/源密钥.源明文高频片段)
    出错:源明文必含片段未出现

    源明文=添加前后缀(源密钥.源明文前后缀，实心明文囗甲)

]]


[[
TODO:简易 短字符串 压缩算法
  本来就不需要压缩！
[
https://www.vldb.org/pvldb/vol13/p2649-boncz.pdf
  Fast Static Symbol Table (FSST) compression,a light weight encoding scheme for strings.
  不是 压缩<短字符串>
  而是 压缩<数组 短字符串> #数据库之一列，同领域数组
  不是 我的目标
]
[
https://zhuanlan.zhihu.com/p/28035800

压缩=建模+去除冗余+转换+编码
最典型的建模方法是基于字符的概率统计，而基于上下文的建模方法(Context Modeling)则是从文本内容出发，它们追求的目标都是让字符的出现概率越不平均越好。
  比如动态马尔可夫压缩(DMC, dynamic Markov coding)。
  可行的算法只需要基于一部分内容的上下文进行预测，这就是PPM（部分匹配预测，prediction by partial match）以及各种演进版本。
转换方法是最具代表性的是基于词典的转换，比如庞大的LZ族系。
Huffman和算术编码则是常见的编码方法。
  ANS是前两类编码算法战争的终结者。
  它在2014年被提出来，随后很快就得到了大量应用。本质上属于算术编码，但它成功地找到了一个用近似概率表示的表格，将原来的概率计算转换为查表。所以它是一个达到Huffman编码效率的算术编码方法。FSE(Finite State Entropy)是ANS最为著名的实现。有兴趣进一步了解，可以看这里。
    https://github.com/Cyan4973/FiniteStateEntropy
    http://www.ezcodesample.com/abs/abs_article.html
      http://www.ezcodesample.com/abs/ANSCoder.txt
      ANS-Asymmetric Numeral System
      https://arxiv.org/abs/0902.0271
        https://arxiv.org/pdf/0902.0271
  !mkdir /sdcard/0my_files/tmp/wget_/Asymmetric_Numeral_System-ANS/
  cd /sdcard/0my_files/tmp/wget_/Asymmetric_Numeral_System-ANS/
  wget http://www.ezcodesample.com/abs/abs_article.html http://www.ezcodesample.com/abs/ANSCoder.txt https://arxiv.org/pdf/0902.0271

    https://link.zhihu.com/?target=https%3A//github.com/Cyan4973/FiniteStateEntropy
    https://link.zhihu.com/?target=http%3A//www.ezcodesample.com/abs/abs_article.html
]
]]

]]]
#'''



from seed.mapping_tools.dict_op import inv__k2v_to_v2k#, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks
import re
import unicodedata as U
from seed.func_tools.fmapT.checkT__tiny import (dot
,icheckT
,checkT__pattern_tuple
,checkT__pattern_list
,checkT__pattern_dict
,checkT__pattern_dictKV
,checkT__pattern_tmay
,checkT__5pred
,checkT__AND
,checkT__type_is
,checkT__type_le
,checkT__type_is__AND
,checkT__type_le__AND
,check__pass
,check__fail
,checkT__ifelse
,checkT__if
,checkT__if_not
,checkT__is
,checkT__eq
,checkT__ne
,checkT__lt
,checkT__gt
,checkT__le
,checkT__ge
,checkT__ge_lt
,check_bool
,check_int
,check_float
,check_complex
,check_bytes
,check_str
,check_tuple
,check_list
,check_frozenset
,check_set
,check_dict
,check__is_None
,checkT__tmay
,checkT__smay
,checkT__may
,checkT__imay
,checkT__tuple
,checkT__list
,checkT__frozenset
,checkT__set
,checkT__dict
,checkT__dictKV
)
from seed.func_tools.fmapT.predT__tiny import (dot
,not_
,is_True
,is_False
,is_None
,is_Ellipsis
,is_NotImplemented
,is_not_True
,is_not_False
,is_not_None
,is_not_Ellipsis
,is_not_NotImplemented
,fix_predicator
,allT__pattern_tuple
,anyT__pattern_tuple
,anyT__pattern_list
,allT__pattern_list
,anyT__pattern_dict
,allT__pattern_dict
,type_isT
,type_leT
,isinstanceT
,issubclassT
,isT
,is_notT
,eqT
,neT
,ltT
,gtT
,leT
,geT
,ge_ltT
,pred__True
,pred__False
,not_dotT
,predT__NOT
,predT__bool_op_
,predT__AND
,predT__NOT_AND
,predT__AND_NOT
,predT__NOT_AND_NOT
,predT__OR
,predT__NOT_OR
,predT__OR_NOT
,predT__NOT_OR_NOT
,predT__XOR
,predT__NOT_XOR
,predT__XOR_NOT
,predT__NOT_XOR_NOT
,is_frozenset
,is_set
,is_dict
,is_bool
,is_int
,is_float
,is_complex
,is_bytes
,is_str
,is_tuple
,is_list
,predT__tuple
,predT__list
,predT__frozenset
,predT__set
,predT__dict
,predT_on_property
,len_eqT
,len_ltT
,len_geT
,len_ge_ltT
,is_empty
)



def check_sorted(ls, /):
    s = sorted(ls)
    ls = [*ls]
    if not s == ls: raise TypeError

#bug:check_str_tuple = checkT__tuple(check_str)
check_str_tuple = checkT__AND(check_tuple, checkT__pattern_list(check_str))
check_sorted_str_tuple = checkT__AND(check_str_tuple, check_sorted)

check_str_pair_tuple = checkT__AND(check_tuple, checkT__pattern_list(checkT__tuple(check_str, check_str)))
check_sorted_str_pair_tuple = checkT__AND(check_str_pair_tuple, check_sorted)

check_用户口令提示前后缀及中间关键字 = checkT__tuple(check_str, check_str_tuple, check_str)
check_其他密钥相关信息关键字 = check_sorted_str_tuple
check_其他密钥相关信息 = check_sorted_str_pair_tuple

def 去掉前后缀(源明文前后缀, 源明文, /):
    前缀, 后缀 = 源明文前后缀
    #出错:双缀不匹配
    if not 源明文.startswith(前缀): raise TypeError
    if not 源明文.endswith(后缀): raise TypeError
    return 源明文[len(前缀):len(源明文)-len(后缀)]

def 换下片段(旧文本, 待替换片段, /):
    check_tuple(待替换片段)
    i2s = 待替换片段
    s2i = inv__k2v_to_v2k(dict(enumerate(i2s)))

    pattern = '|'.join(map(re.escape, 待替换片段))
    regex = re.compile(f'({pattern})')
    ls = regex.split(旧文本)
    if 0:
        L = len(ls)
        idc4old = range(0, L, 2)
        idc4new = range(1, L, 2)
    已替换片段 = tuple(sorted({*ls[1::2]}))

    def f4old(s, /):
        return s.replace('\0', '\0\1')
    def f4new(s, /):
        i = s2i[s]
        return f'\0{i:X}\1'

    ls[0::2] = map(f4old, ls[0::2])
    ls[1::2] = map(f4new, ls[1::2])
    转义序列 = ''.join(ls)
    return (转义序列, 已替换片段)

def 字节串化囗统一码(s, /):
    return s.encode('utf8')





class 囗加密类囗短字符串:
  加解密共有输入:
    源密钥
      =用户口令::[str]
      +源明文前后缀::(str, str)
      +源明文必含片段::{str}
      +源明文高频片段::{str}
      +其他密钥相关信息(网址,用户名,密码有效期起讫,...) ::{str:str}

  加密专有输入:
    * 以下 近乎出现在『表密文』
      字节串加解密算法名称及版本
      密文字符集名称及版本
      费力指数::uint
      用户口令提示前后缀及中间关键字::(str, [str], str)
      其他密钥相关信息关键字::[str]

    * 以下 不出现在『表密文』，即经过『源密钥』处理
      源明文::str
  加密输出:
    Either 出错信息 表密文::str
  解密专有输入:
    表密文::str
  解密输出:
    Either 出错信息 源明文::str
  解密预处理囗提示:
    输入:
      表密文::str
    输出:
      用户口令提示前后缀及中间关键字::(str, [str], str)
      其他密钥相关信息关键字::[str]


    def check_源密钥(用户口令数目, 其他密钥相关信息关键字, 源密钥, /):
        check_tuple(源密钥)
        checkT__5pred(len_eqT(5))(源密钥)
        (用户口令, 源明文前后缀, 源明文必含片段, 源明文高频片段, 其他密钥相关信息) = 源密钥

        check_str_tuple(用户口令)
        checkT__5pred(len_eqT(用户口令数目))(用户口令)

        check_str_tuple(源明文前后缀)
        checkT__5pred(len_eqT(2))(源明文前后缀)

        check_sorted_str_tuple(源明文必含片段)
        check_sorted_str_tuple(源明文高频片段)
        if not len({*源明文必含片段, *源明文高频片段}) == len(源明文必含片段) + len(源明文高频片段):raise TypeError

        check_其他密钥相关信息(其他密钥相关信息)
        其他密钥相关信息关键字数目 = len(其他密钥相关信息关键字)
        checkT__5pred(len_eqT(其他密钥相关信息关键字数目))(其他密钥相关信息)
        if not 其他密钥相关信息关键字 == tuple(map(fst, 其他密钥相关信息)):raise TypeError

        return

    def 拟压缩囗字节串化正整数序列(sf, Ls, /):
        ???有点麻烦
            sort suffixes
                siffix tree?
            radix=3
            3 .join
            to uint??
        算了，还是 继续用 呜呼哀哉尚飨加密 第二版
    def 拟压缩囗字节串(sf, old_bs, /):
        u = int.from_bytes(fb'\1{old_bs}\xff', order='big')
        s01 = f'{u:b}'
        ls = re.split(r'(0+)', s01)
        assert ls
        assert len(ls)%2 == 1
        assert all(ls)
        assert {*ls[0]} == {'1'}
        assert {*ls[-1]} == {'1'}
        assert len(ls[-1]) >= 7

        Ls = [*map(len, ls)]
            #[num_1s, num_0s, ...]

        assert (Ls[-1]) >= 7
        Ls[-1] -= 7
        if not Ls[-1]:
            Ls.pop()
        assert Ls
        assert all(Ls)
        new_bs = sf.拟压缩囗字节串化正整数序列(Ls)
        return new_bs

    def 加密(sf, /, *, 源明文, 源密钥, 字节串加解密算法名称及版本, 密文字符集名称及版本, 费力指数, 用户口令提示前后缀及中间关键字, 其他密钥相关信息关键字):
        check_str(源明文)
        check_str(字节串加解密算法名称及版本)
        check_str(密文字符集名称及版本)
        check_uint(费力指数)
        check_用户口令提示前后缀及中间关键字(用户口令提示前后缀及中间关键字)
        check_其他密钥相关信息关键字(其他密钥相关信息关键字)
        用户口令数目 = 1+len(*用户口令提示前后缀及中间关键字[1:-1])
        sf.check_源密钥(用户口令数目, 其他密钥相关信息关键字, 源密钥)

        强加密囗字节串 = sf.取方法囗强加密囗字节串(字节串加解密算法名称及版本)
        密文字符集囗字符数组 = sf.取属性值囗密文字符集囗字符数组(密文字符集名称及版本)


        密钥盐 = sf.生成随机字节串(hint=len(源明文))
          #近乎出现在『表密文』
        密文盐 = sf.生成随机字节串(hint=len(源明文))
          #不出现在『表密文』，即经过『源密钥』处理

        (用户口令, 源明文前后缀, 源明文必含片段, 源明文高频片段, 其他密钥相关信息) = 源密钥

        实心明文囗甲 = 去掉前后缀(源明文前后缀, 源明文)
            #出错:双缀不匹配

        待替换片段 = 源明文必含片段 + 源明文高频片段
        (实心明文囗转义序列囗乙, 已替换片段) = 换下片段(实心明文囗甲, 待替换片段)
            #出错:源明文必含片段未出现
        if not {*源明文必含片段} <= {*已替换片段}: raise Exception('源明文必含片段未出现')

        实心明文=实心明文囗转义序列囗乙

        实心明文囗字节串 = 字节串化囗统一码(实心明文)
        压实明文囗字节串 = sf.拟压缩囗字节串(实心明文囗字节串)

        里明文囗字节串=弱加密囗字节串(密文盐，压实明文囗字节串)
        咸里明文囗字节串=组合囗盐(密文盐，里明文囗字节串)
        污咸里明文囗字节串=随机加入可识别噪声(咸里明文囗字节串)
          #『实心明文』在此被随机粗加密/加盐
          #     以保证不同加密实例使用不同『里明文』
          #     难为『同一未知「里明文」=>(密钥甲，密文甲，密文乙)->密钥乙』
          #

        里密钥=构造里密钥(源密钥，密钥盐，费力指数)
          #『源密钥』在此被随机变换/加盐
          #     以保证不同加密实例使用不同『里密钥』
          #     难为『同一未知「里密钥」=>(明文甲，密文甲，密文乙)->明文乙』
          #

        里密文囗字节串=强加密囗字节串<字节串加解密算法名称及版本>(里密钥，污咸里明文囗字节串)
          #『密文盐』在此被『里密钥』加密
          #     以保证『实心明文』的加盐操作受『源密钥』保护
          #     是『实心明文』的加盐操作的组成部分
          #
        里密文=字符串化囗指定字符集(密文字符集名称及版本，里密文囗字节串)

        表密文=组合表密文(字节串加解密算法名称及版本，密文字符集名称及版本，费力指数，用户口令提示前后缀及中间关键字，其他密钥相关信息关键字，密钥盐，里密文)

      解密流程:
        (字节串加解密算法名称及版本，密文字符集名称及版本，费力指数，用户口令提示前后缀及中间关键字，其他密钥相关信息关键字，密钥盐，里密文)=拆分表密文(表密文)
        出错:拆分元组失败|未知加解密算法|未知字符集

        提示囗当用户进行交互式输入时:
          显示『用户口令提示前后缀及中间关键字』:
              格式:『用户口令:{前缀}({输入框}){关键字}({输入框}){关键字}({输入框})...{关键字}({输入框}){后缀}』

          显示『其他密钥相关信息关键字』:
              格式:『其他密钥相关信息:{关键字}({输入框}){关键字}({输入框})...{关键字}({输入框})』

          并要求用户填空。

        里密文囗字节串=字节串化囗指定字符集(密文字符集名称及版本，里密文)
        出错:编码失败囗非法字符

        里密钥=构造里密钥(源密钥，密钥盐，费力指数)
        污咸里明文囗字节串=强解密囗字节串<字节串加解密算法名称及版本>(里密钥，里密文囗字节串)
        出错:强解密失败

        咸里明文囗字节串=消除可识别噪声(污咸里明文囗字节串)
        出错:噪声分离失败囗噪声格式错误

        (密文盐，里明文囗字节串)=拆分囗盐(咸里明文囗字节串)
        出错:拆分有序对失败

        压实明文囗字节串=弱解密囗字节串(密文盐，里明文囗字节串)
        出错:弱解密失败

        实心明文囗字节串=拟解压囗字节串(压实明文囗字节串)

        实心明文=字符串化囗统一码(实心明文囗字节串)
        出错:解码失败囗非法字节序列

        实心明文囗转义序列囗乙=实心明文

        (实心明文囗甲，已替换片段)=换上片段(实心明文囗转义序列囗乙，源密钥.源明文必含片段\-/源密钥.源明文高频片段)
        出错:源明文必含片段未出现

        源明文=添加前后缀(源密钥.源明文前后缀，实心明文囗甲)


