
r'''
苏宁易购_液体单价计算类
e.g.
    麻油
    https://search.suning.com/%E9%BA%BB%E6%B2%B9/#second-filter

苏宁易购_重量单价计算类
e.g.
    挂面
    https://search.suning.com/%E6%8C%82%E9%9D%A2/#second-filter

usage:
    >>> 苏宁易购_麻油体积价格_examples = [
    ...    '香油芝麻油麻油 纯正小磨香油 白芝麻月子油5斤 171.90Y'
    ...    ,'金龙鱼 芝麻油 400ml 调味品 27.9Y'
    ...    ]
    >>> 苏宁易购_挂面重量价格_examples = [
    ...    '厨大妈蛋香挂面1000g 6.6Y'
    ...    ,'金沙河原味鸡蛋挂面900g 5.8Y'
    ...    ]
    >>> 苏宁易购_食用油单价计算.show_sorted_examples(苏宁易购_麻油体积价格_examples)
    香油芝麻油麻油 纯正小磨香油 白芝麻月子油5斤 171.90Y
        # 68.76Y/L 14.543339150668993ml/Y
    金龙鱼 芝麻油 400ml 调味品 27.9Y
        # 69.75Y/L 14.336917562724015ml/Y
    >>> 苏宁易购_重量单价计算.show_sorted_examples(苏宁易购_挂面重量价格_examples)
    金沙河原味鸡蛋挂面900g 5.8Y
        # 6.444444444444445Y/kg 155.17241379310346g/Y
    厨大妈蛋香挂面1000g 6.6Y
        # 6.6Y/kg 151.5151515151515g/Y

'''


__all__ = '''
    苏宁易购_单价类
        苏宁易购_液体单价计算类
            苏宁易购_液体体积价格_ptn
            苏宁易购_液体体积价格_rex
            苏宁易购_食用油单价计算
                食用油密度KG_per_L

        苏宁易购_重量单价计算类
            苏宁易购_商品重量价格_ptn
            苏宁易购_商品重量价格_rex
            苏宁易购_重量单价计算

    examples_str2examples
        苏宁易购_麻油体积价格_examples_str
        苏宁易购_麻油体积价格_examples
        苏宁易购_挂面重量价格_examples_str
        苏宁易购_挂面重量价格_examples

    '''.split()
#######################
r'''
    UnitPattern
        uint_ptn
        real_number_ptn
        volume_unit_ptn
        weight_unit_ptn
        money_unit_ptn
        volume_ptn
        weight_ptn
        count_ptn
        price_ptn

    half
    three_fourth
    one
    tenth
    hundredth
    thousandth

    are_spaces
    str2iter_non_space_lines
    str2non_space_lines
    '''.split()

import re
import sys
from abc import ABC, abstractmethod
from fractions import Fraction
assert Fraction('1.1') == Fraction(11, 10)

def override(f):
    return f
def are_spaces(s:str):
    return not s or s.isspace()
def str2iter_non_space_lines(s):
    return (s for s in s.split('\n') if not are_spaces(s))
def str2non_space_lines(s):
    return tuple(str2iter_non_space_lines(s))


half = Fraction(1, 2)
three_fourth = Fraction(3, 4)
one = Fraction(1)
tenth = Fraction(1, 10)
hundredth = tenth**2
thousandth = tenth**3

uint_ptn = r'(?:(?<=[^\d\.])\d+|^\d+)'
#compile fail: uint_ptn = r'(?:(?<=^|\D)\d+)'
re.compile(uint_ptn)
real_number_ptn = fr'(?:{uint_ptn}(?:\.\d+)?)'
class UnitPattern:
    volume_unit_ptn = r'(?:[mM]?[lL])'
    if 1:
        std_volume_unit2L = {'ML':thousandth, 'L':one}

    weight_unit_ptn = r'(?:[斤克gG]|公斤|千克|[kK][gG])'
    if 1:
        upper_weight_unit2std = dict(zip(
            '斤 克 G 公斤 千克 KG'.split()
            ,'斤 G G KG KG KG'.split()
            ))
        std_weight_unit2KG = {'G':thousandth, '斤':half, 'KG':one}

    money_unit_ptn = r'(?:[yYjJfF元角分])'
    if 1:
        upper_money_unit2std = dict(zip('YJF元角分', 'YJFYJF'))
        std_money_unit2Y = {'Y':one, 'J':tenth, 'F':hundredth}

    @classmethod
    def volume_unit2L(cls, volume_unit:str):
        # volume_unit s.t. volume_unit_ptn
        # volume_unit -> Fraction
        std_volume_unit = volume_unit.upper()
        return cls.std_volume_unit2L[std_volume_unit]
    @classmethod
    def weight_unit2KG(cls, weight_unit:str):
        # weight_unit s.t. weight_unit_ptn
        # weight_unit -> Fraction
        upper_weight_unit = weight_unit.upper()
        std_weight_unit = cls.upper_weight_unit2std[upper_weight_unit]
        return cls.std_weight_unit2KG[std_weight_unit]
    @classmethod
    def money_unit2Y(cls, money_unit:str):
        # money_unit s.t. money_unit_ptn
        # money_unit -> Fraction
        assert len(money_unit) == 1
        upper_money_unit = money_unit.upper()
        std_money_unit = cls.upper_money_unit2std[upper_money_unit]
        return cls.std_money_unit2Y[std_money_unit]



volume_unit_ptn = UnitPattern.volume_unit_ptn
weight_unit_ptn = UnitPattern.weight_unit_ptn
money_unit_ptn = UnitPattern.money_unit_ptn
volume_ptn = fr'(?P<VOLUME>{real_number_ptn})(?P<VOLUME_UNIT>{volume_unit_ptn})'
weight_ptn = fr'(?P<WEIGHT>{real_number_ptn})(?P<WEIGHT_UNIT>(?:[斤克gG]|公斤|[kK][gG]))'
count_ptn = fr'(?:\*(?P<COUNT>{uint_ptn}))'
price_ptn = fr'(?P<PRICE>{real_number_ptn})(?P<PRICE_UNIT>{money_unit_ptn})'
class 苏宁易购_单价类(ABC):
    @abstractmethod
    def maybe_parse_str(self, s):
        '-> None|unit_price_Y_per_XXX :: Fraction (unit: Y/XXX)'
        raise NotImplementedError
    @abstractmethod
    def format_unit_price(self, unit_price_Y_per_XXX):
        raise NotImplementedError
    def show_sorted_examples(self, 苏宁易购_商品价格_examples):
        pairs = []
        for example in 苏宁易购_商品价格_examples:
            try:
                maybe_unit_price_Y_per_XXX = self.maybe_parse_str(example)
            except:
                print(f'fail to parse {example!r}', file=sys.stderr)
                raise
            if maybe_unit_price_Y_per_XXX is None:
                print(f'fail to parse {example!r}', file=sys.stderr)
            else:
                unit_price_Y_per_XXX = maybe_unit_price_Y_per_XXX
                pairs.append((unit_price_Y_per_XXX, example))

        # sorted
        pairs = sorted(pairs)
        for unit_price_Y_per_XXX, example in pairs:
            price_str = self.format_unit_price(unit_price_Y_per_XXX)
            print(example)
            print(f'    # {price_str}')


苏宁易购_液体体积价格_ptn = fr'(?P<SND_HALF_PRICE>【第[2二]份半价】)?.*(?:{volume_ptn}|{weight_ptn}){count_ptn}?.*\s{price_ptn}\s*'
苏宁易购_液体体积价格_rex = re.compile(苏宁易购_液体体积价格_ptn)
class 苏宁易购_液体单价计算类(苏宁易购_单价类):
    def __init__(self, 密度KG_per_L:Fraction):
        '密度KG_per_L :: Fraction (unit: KG/L)'
        assert type(密度KG_per_L) is Fraction
        self.密度KG_per_L = 密度KG_per_L
    @override
    def maybe_parse_str(self, s):
        '-> None|unit_price_Y_per_L :: Fraction (unit: Y/L)'
        m = 苏宁易购_液体体积价格_rex.fullmatch(s)
        if not m:
            return None
            print(f'fail to parse {s!r}', file=sys.stderr)

        d = m.groupdict()
        may_SND_HALF_PRICE = d.get('SND_HALF_PRICE')
        if may_SND_HALF_PRICE is None:
            discount = one
        else:
            discount = three_fourth
        discount
        assert type(discount) is Fraction

        may_VOLUME = d.get('VOLUME')
        may_WEIGHT = d.get('WEIGHT')
        if may_VOLUME is None:
            if may_WEIGHT is None: raise logic-error
            WEIGHT = may_WEIGHT
            WEIGHT = Fraction(m['WEIGHT'])
            WEIGHT_UNIT = m['WEIGHT_UNIT']
            WEIGHT_KG = WEIGHT * UnitPattern.weight_unit2KG(WEIGHT_UNIT)
            VOLUME_L = WEIGHT_KG / self.密度KG_per_L
        else:
            VOLUME = may_VOLUME
            VOLUME = Fraction(m['VOLUME'])
            VOLUME_UNIT = m['VOLUME_UNIT']
            VOLUME_L = VOLUME * UnitPattern.volume_unit2L(VOLUME_UNIT)
        VOLUME_L
        assert type(VOLUME_L) is Fraction

        may_COUNT = d.get('COUNT')
        if may_COUNT is None:
            COUNT = one
        else:
            COUNT = may_COUNT
            COUNT = Fraction(COUNT)
        COUNT
        assert type(COUNT) is Fraction
        VOLUME_L *= COUNT
        assert type(VOLUME_L) is Fraction

        PRICE = Fraction(m['PRICE'])
        PRICE_UNIT = m['PRICE_UNIT']
        PRICE_Y = PRICE * UnitPattern.money_unit2Y(PRICE_UNIT)
        assert type(PRICE_Y) is Fraction
        PRICE_Y *= discount
        PRICE_Y
        assert type(PRICE_Y) is Fraction

        unit_price_Y_per_L = PRICE_Y / VOLUME_L
        assert type(unit_price_Y_per_L) is Fraction
        return unit_price_Y_per_L

    @override
    def format_unit_price(self, unit_price_Y_per_XXX):
        unit_price_Y_per_L = unit_price_Y_per_XXX
        Y_per_L__float = float(unit_price_Y_per_L)
        ml_per_Y__float = float(1000 / unit_price_Y_per_L)
        return f'{Y_per_L__float}Y/L {ml_per_Y__float}ml/Y'



苏宁易购_商品重量价格_ptn = fr'(?P<SND_HALF_PRICE>【第[2二]份半价】)?.*{weight_ptn}{count_ptn}?.*\s{price_ptn}\s*'
苏宁易购_商品重量价格_rex = re.compile(苏宁易购_商品重量价格_ptn)
class 苏宁易购_重量单价计算类(苏宁易购_单价类):
    @override
    def maybe_parse_str(self, s):
        '-> None|unit_price_Y_per_KG :: Fraction (unit: Y/KG)'
        m = 苏宁易购_商品重量价格_rex.fullmatch(s)
        if not m:
            return None
            print(f'fail to parse {s!r}', file=sys.stderr)

        d = m.groupdict()
        may_SND_HALF_PRICE = d.get('SND_HALF_PRICE')
        if may_SND_HALF_PRICE is None:
            discount = one
        else:
            discount = three_fourth
        discount
        assert type(discount) is Fraction

        WEIGHT = Fraction(m['WEIGHT'])
        WEIGHT_UNIT = m['WEIGHT_UNIT']
        WEIGHT_KG = WEIGHT * UnitPattern.weight_unit2KG(WEIGHT_UNIT)
        WEIGHT_KG
        assert type(WEIGHT_KG) is Fraction

        may_COUNT = d.get('COUNT')
        if may_COUNT is None:
            COUNT = one
        else:
            COUNT = may_COUNT
            COUNT = Fraction(COUNT)
        COUNT
        assert type(COUNT) is Fraction
        WEIGHT_KG *= COUNT
        assert type(WEIGHT_KG) is Fraction

        PRICE = Fraction(m['PRICE'])
        PRICE_UNIT = m['PRICE_UNIT']
        PRICE_Y = PRICE * UnitPattern.money_unit2Y(PRICE_UNIT)
        assert type(PRICE_Y) is Fraction
        PRICE_Y *= discount
        PRICE_Y
        assert type(PRICE_Y) is Fraction

        unit_price_Y_per_KG = PRICE_Y / WEIGHT_KG
        assert type(unit_price_Y_per_KG) is Fraction
        return unit_price_Y_per_KG

    @override
    def format_unit_price(self, unit_price_Y_per_XXX):
        unit_price_Y_per_KG = unit_price_Y_per_XXX
        Y_per_KG__float = float(unit_price_Y_per_KG)
        g_per_Y__float = float(1000 / unit_price_Y_per_KG)
        return f'{Y_per_KG__float}Y/kg {g_per_Y__float}g/Y'






r'''
# 约 1kg/L
https://zhidao.baidu.com/question/554523566308216692.html
    花生油密度：0.9110至0.9180
    豆油的密度：0.9150至0.9375
    芝麻油常温下的密度在0.920克/毫升~0.926克/毫升之间，可以用0.923乘以相应的毫升数.得到相应的数据！
https://baike.baidu.com/item/%E8%93%96%E9%BA%BB%E6%B2%B9/1755249
    蓖麻油 相对密度（d20℃4℃）　0.9550-0.9700
'''
食用油密度KG_per_L = one
苏宁易购_食用油单价计算 = 苏宁易购_液体单价计算类(食用油密度KG_per_L)
苏宁易购_重量单价计算 = 苏宁易购_重量单价计算类()


苏宁易购_麻油体积价格_examples_str = (r'''
香油芝麻油麻油 纯正小磨香油 白芝麻月子油5斤 171.90Y
金龙鱼 芝麻油 400ml 调味品 27.9Y
金龙鱼食用油芝麻香油220ml*2瓶家用烹饪小磨香油凉拌油纯芝麻小磨香油火锅凉 25.90Y
乡王花椒油142ml 8.00Y
李锦记 纯香芝麻油 410ml 100% 苏宁易购 调味品 芝麻油 厨房调味 21.90Y
九斗碗特麻花椒油400ml 瓶装汉源花椒油 国产四川麻椒油 香油麻油调和油 凉拌菜 19.80Y
银京 食用油 凉拌调味烹饪火锅 纯芝麻 香油 200ML 9.00Y
红井源内蒙古胡麻油1L装 食用油 亚麻籽油 38.00Y
红井源压榨一级亚麻籽油5L/胡麻油/食用油/麻油 179.00Y
红井源压榨一级亚麻籽油2.5L/胡麻油/食用油/麻油 89.00Y
【第2份半价】蜀滋蜀味红花椒油400ml 瓶装香油 麻油调和油 国产麻椒油调味品 16.80Y
九斗碗特麻花椒油2.5L 汉源花椒油 香油 麻油 瓶装藤椒油 火锅蘸料调料油碟 凉拌 74.50Y
红井源 胡麻油 5L 亚麻籽油 食用油 胡麻油 家庭经济装 160.00Y
怡升纯麻油400ml*1瓶 芝麻油 火锅凉拌蘸料 粮油调味 香油 15.90Y
红井源压榨一级亚麻籽油1L/胡麻油/食用油/麻油 44.00Y
蜀滋蜀味藤椒油400ml 四川花椒油 麻油调和油 麻椒油凉拌菜调料 凉面条酸辣粉 16.80Y
红井源内蒙古胡麻油2.5L 食用油 食用亚麻籽油 79.00Y
九斗碗特麻花椒油400ml*2瓶装 香油 麻油调和油 国产麻椒油 凉拌菜调料 酸辣粉 34.80Y
【中华特色】张家口馆 雅阁天娇 soundstar 亚麻籽油5L食用油调和油压榨 胡麻油 190.00Y
5L家庭装纯胡麻油亚麻籽油 山老汉热榨胡麻油食用油 传统工艺压榨 128.80Y
蜀滋蜀味红花椒油400ml*2瓶装 厨房调味品香油 麻油调和油 国产麻椒油 酸辣粉凉 26.80Y
红井源胡麻油1.8L 食用亚麻籽油 亚麻油 胡麻油 食用油 65.00Y
【中华特色】乌兰察布馆 亚麻籽油 非转基因初榨浓香纯亚麻子油食用油胡麻油5L 140.00Y
红井源压榨一级亚麻籽油1.8L/胡麻油/食用油/麻油 69.00Y
华建诚鑫 纯香胡麻油3L 亚麻籽油 73.80Y
胡麻油5L清香冷榨亚麻籽油婴儿宝宝食用油月子油甘肃庆阳特产 99.00Y
华建诚鑫 纯香胡麻油5L 亚麻籽油 125.00Y
蜀滋蜀味特麻型红花椒油2.5L 餐饮瓶装香油 麻油调和油 国产麻椒油 凉拌菜调料 酸 69.90Y
【中华特色】乌兰察布馆 亚麻籽油 非转基因浓香纯亚麻子油食用油胡麻油2.5L 华 75.00Y
【中华特色】 山东馆 崔字牌 小磨香油 2.5L纯芝麻香油 火锅调料 蘸料 麻油2500 132.00Y
华建诚鑫 纯香胡麻油2.5L 亚麻籽油 65.00Y
顿可芝麻香油410ml 麻油 香油 芝麻油 火锅油碟蘸料 凉粉米线凉拌菜调料 酸辣粉 19.90Y
内蒙古红井源压榨一级纯香亚麻籽油4.456L食用油胡麻油儿童食用油 135.00Y
华建诚鑫 纯香胡麻油1.8L 亚麻籽油 52.00Y
【中华特色】泰安馆 富世康 亚麻籽油1.8L 初冷榨 胡麻油 食用油 月子油 华东 79.00Y
益善园胡麻籽油亚麻籽油 热榨初榨纯香烙饼胡麻油1.25L内蒙特产420ml*3 45.00Y
华建诚鑫 压榨一级亚麻籽油1.8L 胡麻油 66.00Y
华建诚鑫纯香胡麻油4.5L 山西特产 健康食用油 129.90Y
胡麻油5L压榨冷榨亚麻籽油天然食用油婴儿宝宝食用油无任何添加甘肃庆阳特产 158.00Y
川宝的厨房红花椒油5L 量贩餐饮桶装 厨房香油 麻油调和油 国产麻椒油 凉拌菜调 118.00Y
顿可芝麻调和油2.5L 芝麻油 麻油 凉粉米线凉拌菜调料 火锅香油碟蘸料 厨房烹饪 38.80Y
压榨香油火锅伴侣麻油串串香蘸料芝麻油，410ml顿可芝麻香油*1瓶 25.80Y
【会宁扶贫馆】赐亿胡麻油5L 158.00Y
【会宁扶贫馆】赐亿2.5L胡麻油 88.00Y
【中华特色】平罗馆 周福乐 熟榨 非转基因小磨胡麻油500ml 炒菜凉拌食用油压榨 13.00Y
华建诚鑫 纯香胡麻油1L 亚麻籽油 31.60Y
重庆火锅油碟罐装65mL*60罐老火锅麻油芝麻香油碟蘸料调和油 127.50Y
【中华特色】静宁扶贫馆 曹务老味道 胡麻油10斤装 5L 食用油免邮 传统工艺压榨 269.00Y
【会宁扶贫馆】香泰乐胡麻油2.5L瓶装 88.00Y
【中华特色】石家庄馆 特产石门峪胡麻油4L瓶装 古法压榨 口味醇厚 华北 95.00Y
中粮福临门一级小磨芝麻香油250mL/小磨工艺/凉拌调味烹饪火锅 16.50Y
红井源古法压榨醇香胡麻油 1L 38.50Y
红井源古法压榨纯香胡麻油 2.5L 95.00Y
''')

苏宁易购_挂面重量价格_examples_str = (r'''
厨大妈蛋香挂面1000g 6.6Y
金沙河原味鸡蛋挂面900g 5.8Y
金沙河龙须挂面 细面条 凉面 拌面 炸酱面 热干面900g 5.8Y
金龙鱼鸡蛋面 家常面系列挂面面条800g 4.5Y
福临门家宴细圆挂面900g 4.5Y
''')




examples_str2examples = str2non_space_lines
苏宁易购_麻油体积价格_examples = examples_str2examples(苏宁易购_麻油体积价格_examples_str)
苏宁易购_挂面重量价格_examples = examples_str2examples(苏宁易购_挂面重量价格_examples_str)

################################################################
########################## main ################################
################################################################
'''
if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals())
'''

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


if __name__ == '__main__':
    print('\n'*3);print('='*60);print('\n'*3)
    苏宁易购_重量单价计算.show_sorted_examples(苏宁易购_挂面重量价格_examples)
    print('\n'*3);print('='*60);print('\n'*3)
    苏宁易购_食用油单价计算.show_sorted_examples(苏宁易购_麻油体积价格_examples)

    ###############################
    ###############################
    ###############################
    (
    (r'''
福临门家宴细圆挂面900g 4.5Y
    # 5.0Y/kg 200.0g/Y
金龙鱼鸡蛋面 家常面系列挂面面条800g 4.5Y
    # 5.625Y/kg 177.77777777777777g/Y
金沙河原味鸡蛋挂面900g 5.8Y
    # 6.444444444444445Y/kg 155.17241379310346g/Y
金沙河龙须挂面 细面条 凉面 拌面 炸酱面 热干面900g 5.8Y
    # 6.444444444444445Y/kg 155.17241379310346g/Y
厨大妈蛋香挂面1000g 6.6Y
    # 6.6Y/kg 151.5151515151515g/Y
    ''')
    ,######################################
    (r'''
顿可芝麻调和油2.5L 芝麻油 麻油 凉粉米线凉拌菜调料 火锅香油碟蘸料 厨房烹饪 38.80Y
    # 15.52Y/L 64.43298969072166ml/Y
胡麻油5L清香冷榨亚麻籽油婴儿宝宝食用油月子油甘肃庆阳特产 99.00Y
    # 19.8Y/L 50.505050505050505ml/Y
川宝的厨房红花椒油5L 量贩餐饮桶装 厨房香油 麻油调和油 国产麻椒油 凉拌菜调 118.00Y
    # 23.6Y/L 42.3728813559322ml/Y
【中华特色】石家庄馆 特产石门峪胡麻油4L瓶装 古法压榨 口味醇厚 华北 95.00Y
    # 23.75Y/L 42.10526315789474ml/Y
华建诚鑫 纯香胡麻油3L 亚麻籽油 73.80Y
    # 24.6Y/L 40.65040650406504ml/Y
华建诚鑫 纯香胡麻油5L 亚麻籽油 125.00Y
    # 25.0Y/L 40.0ml/Y
5L家庭装纯胡麻油亚麻籽油 山老汉热榨胡麻油食用油 传统工艺压榨 128.80Y
    # 25.76Y/L 38.81987577639752ml/Y
【中华特色】平罗馆 周福乐 熟榨 非转基因小磨胡麻油500ml 炒菜凉拌食用油压榨 13.00Y
    # 26.0Y/L 38.46153846153846ml/Y
华建诚鑫 纯香胡麻油2.5L 亚麻籽油 65.00Y
    # 26.0Y/L 38.46153846153846ml/Y
蜀滋蜀味特麻型红花椒油2.5L 餐饮瓶装香油 麻油调和油 国产麻椒油 凉拌菜调料 酸 69.90Y
    # 27.96Y/L 35.7653791130186ml/Y
【中华特色】乌兰察布馆 亚麻籽油 非转基因初榨浓香纯亚麻子油食用油胡麻油5L 140.00Y
    # 28.0Y/L 35.714285714285715ml/Y
华建诚鑫纯香胡麻油4.5L 山西特产 健康食用油 129.90Y
    # 28.866666666666667Y/L 34.64203233256351ml/Y
华建诚鑫 纯香胡麻油1.8L 亚麻籽油 52.00Y
    # 28.88888888888889Y/L 34.61538461538461ml/Y
九斗碗特麻花椒油2.5L 汉源花椒油 香油 麻油 瓶装藤椒油 火锅蘸料调料油碟 凉拌 74.50Y
    # 29.8Y/L 33.557046979865774ml/Y
【中华特色】乌兰察布馆 亚麻籽油 非转基因浓香纯亚麻子油食用油胡麻油2.5L 华 75.00Y
    # 30.0Y/L 33.333333333333336ml/Y
内蒙古红井源压榨一级纯香亚麻籽油4.456L食用油胡麻油儿童食用油 135.00Y
    # 30.296229802513466Y/L 33.007407407407406ml/Y
【第2份半价】蜀滋蜀味红花椒油400ml 瓶装香油 麻油调和油 国产麻椒油调味品 16.80Y
    # 31.5Y/L 31.746031746031747ml/Y
【会宁扶贫馆】赐亿胡麻油5L 158.00Y
    # 31.6Y/L 31.645569620253166ml/Y
华建诚鑫 纯香胡麻油1L 亚麻籽油 31.60Y
    # 31.6Y/L 31.645569620253166ml/Y
红井源内蒙古胡麻油2.5L 食用油 食用亚麻籽油 79.00Y
    # 31.6Y/L 31.645569620253166ml/Y
胡麻油5L压榨冷榨亚麻籽油天然食用油婴儿宝宝食用油无任何添加甘肃庆阳特产 158.00Y
    # 31.6Y/L 31.645569620253166ml/Y
红井源 胡麻油 5L 亚麻籽油 食用油 胡麻油 家庭经济装 160.00Y
    # 32.0Y/L 31.25ml/Y
重庆火锅油碟罐装65mL*60罐老火锅麻油芝麻香油碟蘸料调和油 127.50Y
    # 32.69230769230769Y/L 30.58823529411765ml/Y
蜀滋蜀味红花椒油400ml*2瓶装 厨房调味品香油 麻油调和油 国产麻椒油 酸辣粉凉 26.80Y
    # 33.5Y/L 29.850746268656717ml/Y
【会宁扶贫馆】赐亿2.5L胡麻油 88.00Y
    # 35.2Y/L 28.40909090909091ml/Y
【会宁扶贫馆】香泰乐胡麻油2.5L瓶装 88.00Y
    # 35.2Y/L 28.40909090909091ml/Y
红井源压榨一级亚麻籽油2.5L/胡麻油/食用油/麻油 89.00Y
    # 35.6Y/L 28.089887640449437ml/Y
益善园胡麻籽油亚麻籽油 热榨初榨纯香烙饼胡麻油1.25L内蒙特产420ml*3 45.00Y
    # 35.714285714285715Y/L 28.0ml/Y
红井源压榨一级亚麻籽油5L/胡麻油/食用油/麻油 179.00Y
    # 35.8Y/L 27.932960893854748ml/Y
红井源胡麻油1.8L 食用亚麻籽油 亚麻油 胡麻油 食用油 65.00Y
    # 36.111111111111114Y/L 27.692307692307693ml/Y
华建诚鑫 压榨一级亚麻籽油1.8L 胡麻油 66.00Y
    # 36.666666666666664Y/L 27.272727272727273ml/Y
【中华特色】张家口馆 雅阁天娇 soundstar 亚麻籽油5L食用油调和油压榨 胡麻油 190.00Y
    # 38.0Y/L 26.31578947368421ml/Y
红井源内蒙古胡麻油1L装 食用油 亚麻籽油 38.00Y
    # 38.0Y/L 26.31578947368421ml/Y
红井源古法压榨纯香胡麻油 2.5L 95.00Y
    # 38.0Y/L 26.31578947368421ml/Y
红井源压榨一级亚麻籽油1.8L/胡麻油/食用油/麻油 69.00Y
    # 38.333333333333336Y/L 26.08695652173913ml/Y
红井源古法压榨醇香胡麻油 1L 38.50Y
    # 38.5Y/L 25.974025974025974ml/Y
怡升纯麻油400ml*1瓶 芝麻油 火锅凉拌蘸料 粮油调味 香油 15.90Y
    # 39.75Y/L 25.157232704402517ml/Y
蜀滋蜀味藤椒油400ml 四川花椒油 麻油调和油 麻椒油凉拌菜调料 凉面条酸辣粉 16.80Y
    # 42.0Y/L 23.80952380952381ml/Y
九斗碗特麻花椒油400ml*2瓶装 香油 麻油调和油 国产麻椒油 凉拌菜调料 酸辣粉 34.80Y
    # 43.5Y/L 22.988505747126435ml/Y
【中华特色】泰安馆 富世康 亚麻籽油1.8L 初冷榨 胡麻油 食用油 月子油 华东 79.00Y
    # 43.888888888888886Y/L 22.78481012658228ml/Y
红井源压榨一级亚麻籽油1L/胡麻油/食用油/麻油 44.00Y
    # 44.0Y/L 22.727272727272727ml/Y
银京 食用油 凉拌调味烹饪火锅 纯芝麻 香油 200ML 9.00Y
    # 45.0Y/L 22.22222222222222ml/Y
顿可芝麻香油410ml 麻油 香油 芝麻油 火锅油碟蘸料 凉粉米线凉拌菜调料 酸辣粉 19.90Y
    # 48.53658536585366Y/L 20.603015075376884ml/Y
九斗碗特麻花椒油400ml 瓶装汉源花椒油 国产四川麻椒油 香油麻油调和油 凉拌菜 19.80Y
    # 49.5Y/L 20.2020202020202ml/Y
【中华特色】 山东馆 崔字牌 小磨香油 2.5L纯芝麻香油 火锅调料 蘸料 麻油2500 132.00Y
    # 52.8Y/L 18.939393939393938ml/Y
李锦记 纯香芝麻油 410ml 100% 苏宁易购 调味品 芝麻油 厨房调味 21.90Y
    # 53.41463414634146Y/L 18.72146118721461ml/Y
【中华特色】静宁扶贫馆 曹务老味道 胡麻油10斤装 5L 食用油免邮 传统工艺压榨 269.00Y
    # 53.8Y/L 18.587360594795538ml/Y
乡王花椒油142ml 8.00Y
    # 56.33802816901409Y/L 17.75ml/Y
金龙鱼食用油芝麻香油220ml*2瓶家用烹饪小磨香油凉拌油纯芝麻小磨香油火锅凉 25.90Y
    # 58.86363636363637Y/L 16.98841698841699ml/Y
压榨香油火锅伴侣麻油串串香蘸料芝麻油，410ml顿可芝麻香油*1瓶 25.80Y
    # 62.926829268292686Y/L 15.891472868217054ml/Y
中粮福临门一级小磨芝麻香油250mL/小磨工艺/凉拌调味烹饪火锅 16.50Y
    # 66.0Y/L 15.151515151515152ml/Y
香油芝麻油麻油 纯正小磨香油 白芝麻月子油5斤 171.90Y
    # 68.76Y/L 14.543339150668993ml/Y
金龙鱼 芝麻油 400ml 调味品 27.9Y
    # 69.75Y/L 14.336917562724015ml/Y
    ''')
    ,######################################
    )
