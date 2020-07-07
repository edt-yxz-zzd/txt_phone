
r'''
校验字符系统
from https://www.jianshu.com/p/ead5b08e9839
校验字符系统
关于校验字符系统，其国际标准ISO 7064有2个版本，分别是ISO 7064:1983和ISO/IEC 7064:2003，从内容上来说，除了表面的调整，本质上没有区别，我想可以理解为是IEC成立后对其工作范围主权的宣示。那么，对应的国家标准，也有了2个版本，分别是GB/T 17710-1999和GB/T 17710-2008，基本上保证了对国际标准的高水准翻译水平，使英文阅读能力欠佳的读者可以通过国家标准来体会国际标准制定的严谨，并从中受益。
标准中，提供了如下几个校验字符系统，基本涵盖日常所需。身份证号码校验使用的ISO 7064, MOD 11-2，便是其中之一。在实际项目中，可按需选用。



系统类型
系统名称
适用范围
校验码数目及类型
数字表示法




纯系统
ISO 7064, MOD 11-2
数字
1位数字或附加符X
1


纯系统
ISO 7064, MOD 37-2
字母数字
1位数字或字母或附加符*
2


纯系统
ISO 7064, MOD 97-10
数字
2位数字
3


纯系统
ISO 7064, MOD 661-26
字母
2位字母
4


纯系统
ISO 7064, MOD 1271-36
字母数字
2位数字或字母
5


混合系统
ISO 7064, MOD 11,10
数字
1位数字
6


混合系统
ISO 7064, MOD 27,26
字母
1位字母
7


混合系统
ISO 7064, MOD 37,36
字母数字
1位数字或字母
8



表格中可见，校验字符系统，包括纯系统和混合系统。使用一个模数的称为纯系统，系统名称中MOD后第1个数字是模数，第2个数字是基数；使用两个模数的称为混合系统，系统名称中MOD后的2个数字都是模数。

作者：godson_ds
链接：https://www.jianshu.com/p/ead5b08e9839
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。


######################################################
######################################################
######################################################
######################################################
第二代身份证号码的编码规则及校验
https://www.jianshu.com/p/ead5b08e9839

二代身份证号码的编码规则
    身份证号码共18位，由17位本体码和1位校验码组成。

    前6位是地址码，表示登记户口时所在地的行政区划代码，依照《中华人民共和国行政区划代码》国家标准（GB/T2260）的规定执行；
    7到14位是出生年月日，采用YYYYMMDD格式；
    15到17位是顺序码，表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编订的顺序号，顺序码的奇数分配给男性，偶数分配给女性，即第17位奇数表示男性，偶数表示女性；
    第18位是校验码，采用ISO 7064:1983, MOD 11-2校验字符系统，计算规则下一章节说明。

一代身份证与二代身份证的区别在于：
    一代身份证是15位，二代身份证是18位；
    一代身份证出生年月日采用YYMMDD格式，二代身份证出生年月日采用YYYYMMDD格式；
    一代身份证无校验码，二代身份证有校验码。
'''


__all__ = '''
    第二代身份证号码
    ISO7064s
        ISO7064_1_m11_r2
        ISO7064_1_m37_r2
        ISO7064_2_m97_r10
        ISO7064_2_m661_r26
        ISO7064_2_m1271_r36
        ISO7064_1_m11_m10
        ISO7064_1_m27_m26
        ISO7064_1_m37_m36

    字符变数字ABC
        字符变数字
            char2num__10
            char2num__11
            char2num__26
            char2num__36
            char2num__37

    字符串校验系统ABC
        ISO_7064_字符串校验系统ABC
            ISO_7064_字符串校验系统ABC__init
            ISO_7064_字符串校验系统_纯系统ABC
                ISO_7064_字符串校验系统_纯系统      纯系统
                    纯系统两位
            ISO_7064_字符串校验系统_混合系统ABC
                ISO_7064_字符串校验系统_混合系统    混合系统
                    混合系统一位
    '''.split()

from abc import ABC, abstractmethod
import re
from datetime import date

def override(f):
    return f
class 字符变数字ABC(ABC):
    @abstractmethod
    def __get_size__(self):
        raise NotImplementedError
    @abstractmethod
    def __字符变数字__(self, 字符):
        raise NotImplementedError
    def get_size(self):
        f = type(self).__get_size__
        return f(self)
    def 字符串变数字串(self, 字符串):
        f = type(self).__字符变数字__
        g = lambda x: f(self, x)
        it = map(g, 字符串)
        return tuple(it)

class 字符变数字(字符变数字ABC):
    @override
    def __get_size__(self):
        return self._size
    @override
    def __字符变数字__(self, 字符):
        return self._char2num[字符]
    def __init__(self, ordered_upper_chars):
        if ordered_upper_chars != ordered_upper_chars.upper(): raise ValueError
        if len(set(ordered_upper_chars)) != len(ordered_upper_chars): raise ValueError

        d = {}
        for num, char in enumerate(ordered_upper_chars.upper()):
            d[char] = num
            d[char.lower()] = num
        self._char2num = d
        self._size = len(ordered_upper_chars)
        self.ordered_upper_chars = ordered_upper_chars

char2num__10 = 字符变数字('0123456789')
char2num__11 = 字符变数字('0123456789X')
char2num__26 = 字符变数字('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
char2num__36 = 字符变数字('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
char2num__37 = 字符变数字('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ*')

class 字符串校验系统ABC(ABC):pass
class ISO_7064_字符串校验系统ABC(字符串校验系统ABC):
    @abstractmethod
    def __取校验码数目__(self):
        raise NotImplementedError
    @abstractmethod
    def __取校验码字符变数字__(self):
        raise NotImplementedError
    @abstractmethod
    def __取非校验码字符变数字__(self):
        raise NotImplementedError
    def 字符串变反向数字串(self, 字符串):
        cls = type(self)
        L = cls.__取校验码数目__(self)
        assert L > 0
        非校验码字符串 = 字符串[:-L]
        校验码字符串 = 字符串[-L:]
        非校验码字符变数字 = cls.__取非校验码字符变数字__(self)
        校验码字符变数字 = cls.__取校验码字符变数字__(self)
        非校验码数字串 = 非校验码字符变数字.字符串变数字串(非校验码字符串)
        校验码数字串 = 校验码字符变数字.字符串变数字串(校验码字符串)
        反向数字串 = (*reversed(校验码数字串), *reversed(非校验码数字串))
        return 反向数字串



class ISO_7064_字符串校验系统_纯系统ABC(ISO_7064_字符串校验系统ABC):
    @abstractmethod
    def __取模数__(self):
        raise NotImplementedError
    @abstractmethod
    def __取基数__(self):
        raise NotImplementedError
    def verify(self, 字符串):
        模数 = type(self).__取模数__(self)
        基数 = type(self).__取基数__(self)
        反向数字串 = self.字符串变反向数字串(字符串)
        r = 0
        for x in reversed(反向数字串):
            r = (r*基数 + x)%模数
        return (r == 1)

class ISO_7064_字符串校验系统_混合系统ABC(ISO_7064_字符串校验系统ABC):
    @abstractmethod
    def __取小模数__(self):
        raise NotImplementedError
    def verify(self, 字符串):
        小模数 = type(self).__取小模数__(self)
        大模数 = 小模数 + 1
        assert 小模数%2 == 0 # even
        反向数字串 = self.字符串变反向数字串(字符串)
        r = 0
        for x in reversed(反向数字串):
            r = (r*2 %大模数 + x - 1)%小模数 + 1
        return (r == 1)


#####################################################
class ISO_7064_字符串校验系统ABC__init(ISO_7064_字符串校验系统ABC):
    def __init__(self, 校验码数目, 非校验码字符变数字, 校验码字符变数字):
        assert type(校验码数目) is int
        assert 校验码数目 > 0
        assert isinstance(非校验码字符变数字, 字符变数字ABC)
        assert isinstance(校验码字符变数字, 字符变数字ABC)

        self.校验码数目 = 校验码数目
        self.非校验码字符变数字 = 非校验码字符变数字
        self.校验码字符变数字 = 校验码字符变数字

    @override
    def __取校验码数目__(self):
        return self.校验码数目
    @override
    def __取非校验码字符变数字__(self):
        return self.非校验码字符变数字
    @override
    def __取校验码字符变数字__(self):
        return self.校验码字符变数字

class ISO_7064_字符串校验系统_纯系统(
    ISO_7064_字符串校验系统ABC__init
    ,ISO_7064_字符串校验系统_纯系统ABC
    ):
    name_regex = re.compile(r'ISO 7064, MOD (?P<模数>\d+)-(?P<基数>\d+)')
    assert name_regex.fullmatch('ISO 7064, MOD 11-2')

    def __取模数__(self):
        return self.M
    def __取基数__(self):
        return self.R
    def __init__(self, name, 校验码数目, 非校验码字符变数字, 校验码字符变数字):
        super().__init__(校验码数目, 非校验码字符变数字, 校验码字符变数字)

        m = type(self).name_regex.fullmatch(name)
        if m is None: raise ValueError('the ISO name is wrong')
        模数 = int(m['模数'])
        基数 = int(m['基数'])
        if 校验码数目 == 1:
            if 模数 != 校验码字符变数字.get_size(): raise ValueError
        else:
            if 模数 > 校验码字符变数字.get_size()**校验码数目: raise ValueError

        self.name = name
        self.M = 模数
        self.R = 基数


class ISO_7064_字符串校验系统_混合系统(
    ISO_7064_字符串校验系统ABC__init
    ,ISO_7064_字符串校验系统_混合系统ABC
    ):
    name_regex = re.compile(r'ISO 7064, MOD (?P<大模数>\d+),(?P<小模数>\d+)')
    assert name_regex.fullmatch('ISO 7064, MOD 11,10')

    def __取小模数__(self):
        return self.M
    def __init__(self, name, 校验码数目, 非校验码字符变数字, 校验码字符变数字):
        super().__init__(校验码数目, 非校验码字符变数字, 校验码字符变数字)

        m = type(self).name_regex.fullmatch(name)
        if m is None: raise ValueError('the ISO name is wrong')
        小模数 = int(m['小模数'])
        大模数 = int(m['大模数'])
        if 小模数%2 != 0:  raise ValueError # SHOULD BE even
        if 小模数 + 1 != 大模数: raise ValueError('the ISO name is wrong')
        if 校验码数目 == 1:
            if 小模数 != 校验码字符变数字.get_size(): raise ValueError
        else:
            if 小模数 > 校验码字符变数字.get_size()**校验码数目: raise ValueError

        self.name = name
        self.M = 小模数


纯系统 = ISO_7064_字符串校验系统_纯系统
混合系统 = ISO_7064_字符串校验系统_混合系统
def 纯系统两位(name, 字符变数字):
    return 纯系统(name, 2, 字符变数字, 字符变数字)
def 混合系统一位(name, 字符变数字):
    return 混合系统(name, 1, 字符变数字, 字符变数字)

'''
纯系统
ISO 7064, MOD 11-2
数字
1位数字或附加符X
1
'''
ISO7064_1_m11_r2 = _1 = 纯系统(
    'ISO 7064, MOD 11-2', 1, char2num__10, char2num__11)


'''
纯系统
ISO 7064, MOD 37-2
字母数字
1位数字或字母或附加符*
2
'''
ISO7064_1_m37_r2 = _2 = 纯系统(
    'ISO 7064, MOD 37-2', 1, char2num__36, char2num__37)


'''
纯系统
ISO 7064, MOD 97-10
数字
2位数字
3
'''
ISO7064_2_m97_r10 = _3 = 纯系统两位(
    'ISO 7064, MOD 97-10', char2num__10)


'''
纯系统
ISO 7064, MOD 661-26
字母
2位字母
4
'''
ISO7064_2_m661_r26 = _4 = 纯系统两位(
    'ISO 7064, MOD 661-26', char2num__26)


'''
纯系统
ISO 7064, MOD 1271-36
字母数字
2位数字或字母
5
'''
ISO7064_2_m1271_r36 = _5 = 纯系统两位(
    'ISO 7064, MOD 1271-36', char2num__36)


'''
混合系统
ISO 7064, MOD 11,10
数字
1位数字
6
'''
ISO7064_1_m11_m10 = _6 = 混合系统一位(
    'ISO 7064, MOD 11,10', char2num__10)


'''
混合系统
ISO 7064, MOD 27,26
字母
1位字母
7
'''
ISO7064_1_m27_m26 = _7 = 混合系统一位(
    'ISO 7064, MOD 27,26', char2num__26)


'''
混合系统
ISO 7064, MOD 37,36
字母数字
1位数字或字母
8
'''
ISO7064_1_m37_m36 = _8 = 混合系统一位(
    'ISO 7064, MOD 37,36', char2num__36)

ISO7064s = (
    _1, _2, _3, _4, _5, _6, _7, _8
    )
assert len(ISO7064s) == 8


assert ISO7064_1_m11_r2.verify('370683198901117657')

class 第二代身份证号码:
    第二代身份证号码fmt = r'{address_code:0>6}{YYYYMMDD}{double_gender_order:0>3}{check_code}'
    第二代身份证号码regex = re.compile(r'(?P<address_code>\d{6})(?P<YYYYMMDD>(?P<YYYY>\d{4})(?P<MM>\d{2})(?P<DD>\d{2}))(?P<double_gender_order>\d{3})(?P<check_code>[X\d])')
    def __init__(self
        , 中国行政区划代码, 出生日期, 是否男性
        , 同地同日同性出生顺序号):
        is_UInt = lambda XX: type(XX) is int and XX >= 0
        if not is_UInt(中国行政区划代码): raise TypeError
        if type(出生日期) is not date: raise TypeError
        if type(是否男性) is not bool: raise TypeError
        if not is_UInt(同地同日同性出生顺序号): raise TypeError

        self.address_code = 中国行政区划代码
        self.birthday = 出生日期
        self.is_male = 是否男性
        self.single_gender_order = 同地同日同性出生顺序号
        s = self.to_第二代身份证号码字符串()
        if len(s) != 18: raise ValueError

    def to_第二代身份证号码字符串(self, *, excluded_check_code=False):
        s = type(self).第二代身份证号码fmt.format(
            address_code=self.address_code
            ,YYYYMMDD=self.birthday.strftime('%Y%m%d')
            ,double_gender_order=self.single_gender_order*2+self.is_male
            ,check_code=''
            )
        if len(s) != 17: raise ValueError
        if excluded_check_code:
            t = s
            if len(t) != 17: raise ValueError
        else:
            for check_code in char2num__11.ordered_upper_chars:
                t = s+check_code
                if ISO7064_1_m11_r2.verify(t):
                    break
            else:
                raise logic-error
            if len(t) != 18: raise ValueError
        第二代身份证号码字符串 = t
        return 第二代身份证号码字符串

    @classmethod
    def from_第二代身份证号码字符串(cls, 第二代身份证号码字符串, *, excluded_check_code=False):
        t = 第二代身份证号码字符串
        excluded_check_code = bool(excluded_check_code)
        if excluded_check_code:
            s = t + 'X'
        else:
            s = t

        if len(s) != 18: raise ValueError
        m = cls.第二代身份证号码regex.fullmatch(s)
        if m is None: raise ValueError
        if not excluded_check_code:
            if not ISO7064_1_m11_r2.verify(s): raise ValueError
        address_code = int(m['address_code'])
        YYYY = int(m['YYYY'])
        MM = int(m['MM'])
        DD = int(m['DD'])
        birthday = date(YYYY, MM, DD)
        double_gender_order = int(m['double_gender_order'])
        is_male = double_gender_order%2 != 0
        single_gender_order = double_gender_order // 2
        self = cls(address_code, birthday, is_male, single_gender_order)
        if self.to_第二代身份证号码字符串(excluded_check_code=excluded_check_code) != t: raise logic-error
        return self

def _t():
    self = 第二代身份证号码.from_第二代身份证号码字符串('370683198901117657')
    assert self.to_第二代身份证号码字符串() == '370683198901117657'
    self = 第二代身份证号码.from_第二代身份证号码字符串('37068319890111765', excluded_check_code=True)
    assert self.to_第二代身份证号码字符串() == '370683198901117657'
_t()


def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='第二代身份证号码'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('identity_card_number', type=str
                        , help='identity_card_number; e.g. 370683198901117657 or 37068319890111765 (excluded_check_code "7")')

    args = parser.parse_args(args)
    ID = args.identity_card_number
    if not 17 <= len(ID) <= 18: raise ValueError
    self = 第二代身份证号码.from_第二代身份证号码字符串(ID[:17], excluded_check_code=True)
    ID_ = self.to_第二代身份证号码字符串()
    ISO7064_1_m11_r2.verify(ID_)
    if ID != ID_:
        print(ID_)
    return
    ###############################
    excluded_check_code = len(ID) == 17

    self = 第二代身份证号码.from_第二代身份证号码字符串(ID, excluded_check_code=excluded_check_code)
    ID_ = self.to_第二代身份证号码字符串()
    if excluded_check_code:
        print(ID_)
    else:
        assert ID == ID_
        ISO7064_1_m11_r2.verify(ID)

if __name__ == "__main__":
    main()


