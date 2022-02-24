
r'''
e script/简繁对称字.py
e script/简繁对称字-middle-parse.py

DONE:简繁 伪对称字
  风雨雷 电?
  行，彳亍成行
  水？
  白？玄？黄黑赤青
  帝王皇
  天土大人
  日月？光
  田园风光
  登？祭？
  变量
  只需用于某个
  类
  背景音乐？
  子？女？
  草木本末
  井田
  亮丽风景
  杀 同 面？回 从 穴
  空穴来风
  心意？
  我？余
  卐卍
  鼎立
  至？于
  支
  view script/简繁对称字.py
    view ../../python3_src/nn_ns/CJK/CJK_pinyin__ucd/chars_3980.py
    view  script/简繁对称字.py.out.completed_chars_3980.txt



pwd/root-directory:
    /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/
    /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/简繁伪对称字/script/
    ----
    cp -t /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/简繁伪对称字/script/  /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/简繁对称字*
    ----
    简繁对称字-middle-parse.py
    简繁对称字-middle-parse.py.from_completed_chars_3980.out.txt
    简繁对称字.py
    简繁对称字.py.final.list_print.completed_chars_3980.txt
    简繁对称字.py.modify.list_print.completed_chars_3980.txt
    简繁对称字.py.out.list_print.completed_chars_3980.txt
    简繁对称字.py.out.store.completed_chars_3980.txt

py /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/简繁对称字.py -ps list_print -mk completed_chars_3980 -o /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/简繁对称字.py.out.list_print.completed_chars_3980.txt
    ===
    view /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/简繁对称字.py.out.list_print.completed_chars_3980.txt
    /.\{20,}
        找到有明显毛病的部分: □  # \u25A1
    ===
    !cp  script/简繁对称字.py.out.list_print.completed_chars_3980.txt  script/简繁对称字.py.modify.list_print.completed_chars_3980.txt
    e script/简繁对称字.py.modify.list_print.completed_chars_3980.txt
    !cp   script/简繁对称字.py.modify.list_print.completed_chars_3980.txt  script/简繁对称字.py.final.list_print.completed_chars_3980.txt
    view script/简繁对称字.py.final.list_print.completed_chars_3980.txt
        total 1197 hz 伪对称字
        =======================
        e script/简繁对称字-middle-parse.py
        view  script/简繁对称字-middle-parse.py.from_completed_chars_3980.out.txt
        =======================
        see:below pseudo_symmetric_hz_from_completed_chars_3980__total_1197
        =======================

py /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/简繁对称字.py -ps store -mk completed_chars_3980 -o /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/简繁对称字.py.out.store.completed_chars_3980.txt
    ===
    view /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/简繁对称字.py.out.store.completed_chars_3980.txt
    ===

e /storage/emulated/0/0my_files/git_repos/python3_src/

view ../../python3_src/nn_ns/CJK/CJK_data/汉字繁简.py
  view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字繁简.py
view ../../python3_src/nn_ns/CJK/CJK_data/chars_3980.py
  view ../../python3_src/nn_ns/CJK/CJK_pinyin__ucd/chars_3980.py


=============
=============
伪对称字:
    丝系玄
    了子
    女丈
    今令
    五
    瓜云去至卿县叁?虫禹愚心?万方?习習寥比乡少亥?各备夏夕多夢？[xxx豕?]?勿易
    亦刀力寡免鱼
    儿几风
    东车
    白百皇
    登
    竹
    又
    兴学
    人入
    千夭
    衣哀农
    宛祭留癸
    我羽
    樂嶽
    幺
    弱
    太
    奴如
    丑
    我
    戈
    母
    卦
    更
    澎
    久
    少乏
    鼠
    官
    耳
    舜
    茎
    赢
    食
    骨


#'''

from nn_ns.CJK.CJK_data.chars_3980 import chars_3980
from nn_ns.CJK.CJK_data.汉字繁简 import (
    简繁字对集
        ,繁体字到简体字串
        ,简体字到繁体字串
    )

_problematic_chars = '□'
_problematic_chars = ''.join(sorted(_problematic_chars))
#print(*map('{:X}'.format, map(ord, _problematic_chars)))

assert '\u25A1' == '□'
assert '\u25A1' in _problematic_chars

def _f1__fill_complete(s, /):
    done = {original for original, simplified, traditional in _iter__fill_complete(s)}
    return ''.join(sorted(done))
def _list_print__fill_complete(s, /, *, fout):
    it = _iter__fill_complete(s)
    ls = sorted(it)
    it = iter(ls)
    for i, (original, simplified, traditional) in enumerate(it):
        h = ord(original)
        print(fr'i{i:0>4}th:u{h:X}h:{original}:{simplified}:{traditional}', file=fout)
def _iter__fill_complete(s, /):
    to_do = set(s)
    done = set()
    while to_do:
        hz = to_do.pop()
        if hz in done: continue
        if hz in _problematic_chars: continue
        done.add(hz)
        xs = 繁体字到简体字串.get(hz, '')
        ys = 简体字到繁体字串.get(hz, '')
        yield hz, xs, ys #original, simplified, traditional
        to_do.update(xs)
        to_do.update(ys)
completed_chars_3980 = _f1__fill_complete(chars_3980)
#print(completed_chars_3980)
_list_print4completed_chars_3980 = lambda *, fout:_list_print__fill_complete(chars_3980, fout=fout)
_stored_form4completed_chars_3980 = (len(completed_chars_3980), completed_chars_3980)

###parser4pseudo_symmetric_hz_from_completed_chars_3980:total=1197###
pseudo_symmetric_hz_from_completed_chars_3980__total_1197 = r'''
一丁万丈三不与丑且丙业丛东丝丞丟
丢两並个丫中丰串丹主丽举久义乎乐
乔乖乗乘乙习乡买了二于云互五井亚
亜亞亢交亥亦亨亩享京亭亮亲人仆今
介从仑仝令众会伞余來侖傘儿允元兄
充兆兇光兊克兌免兑兒党兜兢入內全
兩八公六兰共关兴其具典兹养兽冀内
円冈冉冊册再冑冒冕冗军农冥冰冲况
几凡凤凰凳凶凸凹出击函凿刀刁分券
力办劣劳労勞募勺勻勾勿匀匆匈匕北
匡匪区十千卉半华卒单卖南卜卡卦卧
卫卯卵卿厂去县叁叄又叉双发受变叠
口古另叩只召叭可台史右叶合吉吊同
吏向吕吝吞否含吴吾呂呆呈呑呕员周
呸呻命咀咒咖咪咷哀品哄哑員唖唱唾
商問啞啡啬善喆喜喦喬單営嗇噩嚣嚻
囂囊囚四回因囡囬园囯困囲図围固图
圆圍園圓圖土圣圭坐垂垒基堂堃堯塞
墓墨壘士壬売壳壶壷壹壺壽夀备変夏
夕多夢大天太夫夭央夯夹夾奈奉奋奏
奔奕奠奥奧女奴如妥委姜姦娄婁婴嬰
子字孟季学學宁宇安宋完宗官宙宛宜
实実审客宣室宪宫宮宰害宴宵容宽寀
寅富寒寓寕寛寜寞察寡寥實寧寨審寬
小少尔尖尘尙尚尝尧尭尺尽山岁岂岔
岗岚岡峦峩崇崑崗崙崩嵐嵒嶽巒川州
巢巣工巨巫己巾币市帘帛帝带帶常幕
干平并幸幺幽开弃弄引张弱張彊归心
志忠忧念忽忿态怂怒思怠怨总恆恋恒
恙恩恭息恵恶恿悉患悪悬悲悶惠惡惫
意愚愛慈慕憂憲戀戈我手才扑扒扛扣
扫扭找承抠抻拇拑拒拜拝拳拿挑挙挛
捧捶掇掌排掛掰摹擧攀攣支文斉斋斎
斑斗方旁无日旦旧早旬旱旺昆昌易昔
昙春昼显晃晉晋晕普景晶暈暮暴曇曡
曰曲更曹曼曾替會月朋木未末本朵杀
杂李杏束条来杰東杳林果枣某查柬栄
栗栾案桑梦棄棗棘棠森業楽榮樂樊欒
欠止歹母毒比毕水永汁汇汞江汪沖沮
泉泛泪泰浅淡淵淺淼渊澎火灭灸災灾
炎烹焚熏熒燕營爪爭爱父爷爹爽爾片
犇犭狂狱猖獄玄玆率王珪班琴琵瓜瓣
瓦瓮甘甞用甭甯田由甲申男甸画畄界
留畜畢畦番異畱當疊癸発登白百皆皇
皿盂盃盅盆益盎盒盖目直省真眨眯眶
眷眺眾睡睦矗示祟票祭禀禁禹离禽禾
禿秃秦稟穴究穷空窒窜窝窦窩窯窰竄
竇立竝竞竟章童競竹竿笑笛笤笨笺筍
筒答策签简箇箋箕算管箩箫篓篙篡篦
篱簍簑簘簡簧簫簽籥米类粗粛粟粥粪
糞系紊素索累絮絲繭纍网罕罗罢罣罪
置羊美羔義羴羹羽翁翌習翠翼而耍耑
耳耸聂聞聶肃肅肉肖育胃胄背脅脊膏
臣臥自至臺臼舀舅舆與興舉舌舍舜舞
舟艾节芋芍芙芜芥芬芯芳芸芾苏苑苔
苗苟苦苯英苹茁茉茍茎茧茲茴茵茶茸
茹荅草荔荚荜荞荠荣荤荧药荳荸莖莢
莫莱获菊菌菓菜菩華菱菲萊萎萕萝萤
营萧萬葘董葱葵葷蒂蒜蒸蒿蓄蓉蓋蓑
蓖蓽蔓蔘蔡蔥蔷蕊蕎蕓蕭蕾薑薔薫薬
薰薺藥蘭虫虽蚕蚤蛍蛮蜀螢蟲蠢蠶蠺
蠻血行衍衒衔衕街衙衛衝衞衡衣表衰
衷袁裏裔裳裹西要見覓覔覚覺见觅觉
角言誉誊譽變讎讐谷豆豈豐貝負貢貧
貪貫責貴買貿賈賓賛賞賣質賽贊贏贝
负贡责质贪贫贯贵贸贾赏赛赞赢赤車
軍輩輿轟车轰辈辛辜辦辨辩辫辮辯邦
邯郵鄒酉釁采里重量金釜长門閃閆開
閏閑閒間閔閘閙閡関閣閤閧閨閩閱閲
閻闆闇闗關闡门闪闫问闰闲间闵闷闸
闹闺闻闽阁阂阅阎阐阱阳阵阻陈陣陳
陸隙雙雠雨雪雲零雷雾需霄霎霓霛霤
靈靑青非面靣革韋韓韭音頁页風风食
養首香骨高鬥鬧鬨魚魯鱻鱼鲁麤麥麦
黃黄黍黑黒黨鼎鼠鼡鼻齊齋齐
#'''

def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    def mk_func_name4list_print(target_name, /):
        return f'_list_print4{target_name}'
    def mk_var_name4store(target_name, /):
        return f'_stored_form4{target_name}'

    valid_cases4post_process = '''
        store
        list_print
        '''.split()
    class case2post_process:
        #@staticmethod
        def store(nm, stored_form4target, /, fout):
            print(fr'##action=store; target_name:{nm!s}##', file=fout)
            print(stored_form4target, file=fout)

        #@staticmethod
        def list_print(nm, f, /, fout):
            print(fr'##action=list_print; target_name:{nm!s}##', file=fout)
            f(fout=fout)
    case2post_process = case2post_process.__dict__
    case2post_process = {case:case2post_process[case] for case in valid_cases4post_process}

    valid_names4target = '''
        completed_chars_3980
        '''.split()
    _d = globals()
    name2stored_form = {nm: _d[mk_var_name4store(nm)] for nm in valid_names4target}
    name2list_print_func = {nm: _d[mk_func_name4list_print(nm)] for nm in valid_names4target}
    del _d
    case2name2xxx = dict(
        store = name2stored_form
        ,list_print = name2list_print_func
        )
    #case2name2xxx = case2name2xxx.__dict__
    assert case2post_process.keys() == case2name2xxx.keys()
    #print(sorted(case2post_process))
    #['__dict__', '__doc__', '__module__', '__weakref__', 'list_print', 'store']
    #assert len(case2post_process.keys()) == len(valid_cases4post_process)
    assert (case2post_process.keys()) == set(valid_cases4post_process)

    parser = argparse.ArgumentParser(
        description='简繁对称字'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-ps', '--post_process', type=str, required=True, choices=sorted(valid_cases4post_process)
                        , help='post_process for target')
    parser.add_argument('-mk', '--name4target', type=str, required=True, choices=sorted(valid_names4target)
                        , help='name of target to be handle')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-oe', '--output_encoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    oencoding = args.output_encoding
    omode = 'wt' if args.force else 'xt'

    nm = args.name4target
    case = args.post_process
    post_process = case2post_process[case]
    xxx = case2name2xxx[case][nm]


    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        post_process(nm, xxx, fout=fout)

if __name__ == "__main__":
    main()





