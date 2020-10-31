
r"""

e script/gb18030_move_out_PUA.py

some gb18030 chars encoded in unicode PUA
later unicode std encode them normally

BMP PUA = [E000, F900)

view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字Unicode编码范围.txt
view ../../python3_src/nn_ns/CJK/CJK_data/raw/Unicode私人使用区PUA.txt
    *Unicode私人使用区PUA
    *汉字Unicode编码范围
    *GB18030: PUA->unicode

#"""

gb = 'gb18030'
BMP_PUA = range(0xE0_00, 0xF9_00)

def find_out_gb18030_at_BMP_PUA():
    for i in BMP_PUA:
        c = chr(i)
        bs = c.encode(gb)
        s = bs.decode(gb)
        assert len(s)==1
        j = ord(s)
        if j != i:
            print(f"{i:0>4X}->{j:0>4X}:{bs!r}")

find_out_gb18030_at_BMP_PUA()
    #output nothing!!!!!



