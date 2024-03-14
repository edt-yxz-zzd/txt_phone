#__all__:goto
r'''[[[
e ./script/找出冫高位面汉字.py


script.找出冫高位面汉字
py -m nn_ns.app.debug_cmd   script.找出冫高位面汉字 -x
py -m nn_ns.app.doctest_cmd script.找出冫高位面汉字:__doc__
py_adhoc_call   script.找出冫高位面汉字   @找出冫高位面字符或私用区字符巛鬽输入路径扌   :../../python3_src/useful__cjk_naming.txt
py_adhoc_call   script.找出冫高位面汉字   @str.找出冫高位面字符或私用区字符巛鬽输入路径扌   :../../python3_src/useful__cjk_naming.txt

#]]]'''
__all__ = r'''
欤高位面字符扌
欤基本位面私用区字符扌
欤高位面字符或私用区字符扌
欤基本位面非私用区字符扌
找出冫高位面字符或私用区字符巛文件对象扌
找出冫高位面字符或私用区字符巛鬽输入路径扌
'''.split()#'''
__all__

def 欤高位面字符扌(ch, /):
    return not ord(ch) < 0x1_00_00
def 欤基本位面私用区字符扌(ch, /):
    # Private Use Area (PUA): U+E000..U+F8FF
    return 0xE0_00 <= ord(ch) < 0xF9_00
def 欤高位面字符或私用区字符扌(ch, /):
    return (欤高位面字符扌(ch) or 欤基本位面私用区字符扌(ch))
def 欤基本位面非私用区字符扌(ch, /):
    return not 欤高位面字符或私用区字符扌(ch)

def 找出冫高位面字符或私用区字符巛文件对象扌(ifile, /):
    cs = (ch for line in ifile for ch in line)
    cs = filter(欤高位面字符或私用区字符扌, cs)
    cs = map(chr, sorted(set(map(ord, cs))))
    return ''.join(cs)
def 找出冫高位面字符或私用区字符巛鬽输入路径扌(may_ipath, iencoding='utf8', /):
    from seed.io.may_open import may_open_stdin, may_open_stdout
    with may_open_stdin(may_ipath, 'rt', encoding=iencoding) as ifile:
        s = 找出冫高位面字符或私用区字符巛文件对象扌(ifile)
    return s



__all__


from script.找出冫高位面汉字 import *
