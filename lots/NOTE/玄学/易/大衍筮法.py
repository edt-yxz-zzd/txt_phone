
#大衍筮法
#先数１，２，……，１０共５５策
#６策用于记第几爻
#４９策用于“三变”
import random
import math
def choose(n, k):
    return math.factorial(n)//math.factorial(k)//math.factorial(n-k)
def 揲之以四(策数):
    奇 = 策数%4
    return 奇 if 奇 else 4
def 变(策数):
    卦一 = 1
    策数 -= 卦一
    #分而为二
    #左 = random.randrange(1,策数); 右 = 策数 - 左
    total = 2**策数 - 2
    accumulates = [0]
    for i in range(1, 策数):
        num = choose(策数, i)
        acc = accumulates[-1] + num
        accumulates.append(acc)
    assert accumulates[-1] == total
    x = random.randrange(total)
    for i, upper in enumerate(accumulates):
        if x < upper:
            break
    else:
        raise logic-error
    assert 1 <= i <= 策数 - 1
    左 = i; 右 = 策数 - 左

    扐 = 揲之以四(左) + 揲之以四(右) # 已减 卦一
    策数 -= 扐
    return 策数
def 三变成一爻(用数):
    策数 = 用数
    for _ in range(3):
        策数 = 变(策数)
        #rint(策数)
    营数 = 策数//4
    #rint(营数, 策数, 用数)
    assert 营数 in (6,7,8,9)
    return 营数

大衍之数 = sum(range(1, 10+1))  # 55
爻数 = 6                        # 6
用数 = 大衍之数 - 爻数          # 49
def 大衍筮法():
    六爻营数 = [三变成一爻(用数) for i in range(爻数)] # [(6|7|8|9)]
    本卦六爻 = []
    之卦六爻 = []
    T, F = 阳,阴 = True, False
    营数２阴阳 = dict(zip(range(6,9+1), [阴,阳,阴,阳]))
    营数２变否 = dict(zip(range(6,9+1), [T,F,F,T]))
    for 营数 in 六爻营数:
        本爻 = 营数２阴阳[营数]
        之爻 = not 本爻 if 营数２变否[营数] else 本爻
        本卦六爻.append(本爻)
        之卦六爻.append(之爻)
    def str阴阳(阴阳):
        return '阴阳'[阴阳]
    本卦六爻 = ''.join(map(str阴阳, 本卦六爻))
    之卦六爻 = ''.join(map(str阴阳, 之卦六爻))
    return 本卦六爻, 之卦六爻   # 初二三四五上

def 大衍筮法营数概率分布(n):
    概率分布 = {i:0 for i in range(6,9+1)}
    for i in range(n):
        营数 = 三变成一爻(用数) # [(6|7|8|9)]
        概率分布[营数] += 1
    return 概率分布

if __name__ == '__main__':
    print(大衍筮法())
    print(大衍筮法())
    print(大衍筮法())
    print(大衍筮法())
    print(大衍筮法())
    #
    n = 4096
    概率分布 = 大衍筮法营数概率分布(n)
    print(概率分布)
    for k, v in sorted(概率分布.items()):
        f = float(v)/n
        print(f'\tp({k}) = {f}')

    # 大约是 1573, see:大衍筮法爻变概率分布.py
    '''
    ('阴阳阴阴阴阴', '阴阴阴阳阴阴')
    ('阴阴阴阳阳阳', '阴阴阳阴阳阴')
    ('阳阳阴阴阳阴', '阳阴阴阴阳阴')
    ('阳阳阳阴阳阴', '阳阳阳阳阳阴')
    ('阳阳阳阳阳阳', '阳阳阳阳阳阴')
    {6: 239, 7: 1247, 8: 1844, 9: 766}
            p(6) = 0.058349609375
            p(7) = 0.304443359375
            p(8) = 0.4501953125
            p(9) = 0.18701171875
    '''
