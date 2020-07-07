r'''
mk_windows_spec_lnk

#how find spec addr? 打开它，右击地址，“复制地址(C)”，在桌面右击新建快捷方式并ctrl+v，将粘贴的地址复制出来。
控制面板\网络和 Internet\网络连接
控制面板\网络和 Internet\网络连接"::{26EE0668-A00A-44D7-9371-BEB064C98683}\3\::{7007ACC7-3202-11D1-AAD2-00805FC1270E}"

控制面板\系统和安全\Windows 防火墙
控制面板\系统和安全\Windows 防火墙"::{26EE0668-A00A-44D7-9371-BEB064C98683}\5\::{4026492F-2F69-46B8-B9BF-5654FC07E423}"

"Windows 防火墙.lnk" # 469 bytes
    －－－－－－－－－－－
    4C0000000114020000000000C0000000
    00000046810008000000000000000000
    00000000000000000000000000000000
    00000000000000000000000001000000
    00000000000000000000000040001400
    1F706806EE260AA0D7449371BEB064C9
    86830C0001008421DE39050000001E00
    7180000000000000000000002F492640
    692FB846B9BF5654FC07E42300004301
    0000090000A0620000003153505330F1
    25B7EF471A10A5F102608C9EEBAC2900
    00000A000000001F0000000C00000057
    0069006E0064006F0077007300200032
    966B70995800001D0000000400000000
    1F00000006000000FB7CDF7E8765F64E
    3959000000000000D500000031535053
    A66A63283D95D211B5D600C04FD918D0
    B90000001E000000001F000000540000
    003A003A007B00320036004500450030
    003600360038002D0041003000300041
    002D0034003400440037002D00390033
    00370031002D00420045004200300036
    0034004300390038003600380033007D
    005C0035005C003A003A007B00340030
    003200360034003900320046002D0032
    004600360039002D0034003600420038
    002D0042003900420046002D00350036
    00350034004600430030003700450034
    00320033007D00000000000000000000
    0000000000
    －－－－－－－－－－－ gvim: ctrl+v; blockwise copy+paste
    4C 00 00 00   01 14 02 00   00 00 00 00   C0 00 00 00
    00 00 00 46   81 00 08 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   01 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   40 00 14 00
    1F 70 68 06   EE 26 0A A0   D7 44 93 71   BE B0 64 C9
    86 83 0C 00   01 00 84 21   DE 39 05 00   00 00 1E 00
    71 80 00 00   00 00 00 00   00 00 00 00   2F 49 26 40
    69 2F B8 46   B9 BF 56 54   FC 07 E4 23   00 00 43 01
    00 00 09 00   00 A0 62 00   00 00 31 53   50 53 30 F1
    25 B7 EF 47   1A 10 A5 F1   02 60 8C 9E   EB AC 29 00
    00 00 0A 00   00 00 00 1F   00 00 00 0C   00 00 00 57
    00 69 00 6E   00 64 00 6F   00 77 00 73   00 20 00 32
    96 6B 70 99   58 00 00 1D   00 00 00 04   00 00 00 00
    1F 00 00 00   06 00 00 00   FB 7C DF 7E   87 65 F6 4E
    39 59 00 00   00 00 00 00   D5 00 00 00   31 53 50 53
    A6 6A 63 28   3D 95 D2 11   B5 D6 00 C0   4F D9 18 D0
    B9 00 00 00   1E 00 00 00   00 1F 00 00   00 54 00 00
    00 3A 00 3A   00 7B 00 32   00 36 00 45   00 45 00 30
    00 36 00 36   00 38 00 2D   00 41 00 30   00 30 00 41
    00 2D 00 34   00 34 00 44   00 37 00 2D   00 39 00 33
    00 37 00 31   00 2D 00 42   00 45 00 42   00 30 00 36
    00 34 00 43   00 39 00 38   00 36 00 38   00 33 00 7D
    00 5C 00 35   00 5C 00 3A   00 3A 00 7B   00 34 00 30
    00 32 00 36   00 34 00 39   00 32 00 46   00 2D 00 32
    00 46 00 36   00 39 00 2D   00 34 00 36   00 42 00 38
    00 2D 00 42   00 39 00 42   00 46 00 2D   00 35 00 36
    00 35 00 34   00 46 00 43   00 30 00 37   00 45 00 34
    00 32 00 33   00 7D 00 00   00 00 00 00   00 00 00 00
    00 00 00 00   00
    －－－－－－－－－－－
    4C 00 00 00   01 14 02 00   00 00 00 00   C0 00 00 00
    00 00 00 46   81 00 08 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   01 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   40 00 14 00
    1F 70 68 06   EE 26 0A A0   D7 44 93 71   BE B0 64 C9
          ^^^^^^^^^^^^^ ~~~~~   ^^^^^ ~~~~~   ^^^^^^^^^^^
    86 83 0C 00   01 00 84 21   DE 39 05 00   00 00 1E 00
    ^^^^^
    71 80 00 00   00 00 00 00   00 00 00 00   2F 49 26 40
                                              ^^^^^^^^^^^
    69 2F B8 46   B9 BF 56 54   FC 07 E4 23   00 00 43 01
    ~~~~~ ^^^^^   ~~~~~ ^^^^^^^^^^^^^^^^^^^
    00 00 09 00   00 A0 62 00   00 00 31 53   50 53 30 F1
    25 B7 EF 47   1A 10 A5 F1   02 60 8C 9E   EB AC 29 00
    00 00 0A 00   00 00 00 1F   00 00 00 0C   00 00 00 57
    00 69 00 6E   00 64 00 6F   00 77 00 73   00 20 00 32
    96 6B 70 99   58 00 00 1D   00 00 00 04   00 00 00 00
    1F 00 00 00   06 00 00 00   FB 7C DF 7E   87 65 F6 4E
    39 59 00 00   00 00 00 00   D5 00 00 00   31 53 50 53
    A6 6A 63 28   3D 95 D2 11   B5 D6 00 C0   4F D9 18 D0
    B9 00 00 00   1E 00 00 00   00 1F 00 00   00 54 00 00
    00 3A 00 3A   00 7B 00 32   00 36 00 45   00 45 00 30#: : { 2 6 E E 0
    00 36 00 36   00 38 00 2D   00 41 00 30   00 30 00 41#6 6 8 - A 0 0 A
    00 2D 00 34   00 34 00 44   00 37 00 2D   00 39 00 33#- 4 4 D 7 - 9 3
    00 37 00 31   00 2D 00 42   00 45 00 42   00 30 00 36#7 1 - B E B 0 6
    00 34 00 43   00 39 00 38   00 36 00 38   00 33 00 7D#4 C 9 8 6 8 3 }
    00 5C 00 35   00 5C 00 3A   00 3A 00 7B   00 34 00 30#\ 5 \ : : { 4 0
    00 32 00 36   00 34 00 39   00 32 00 46   00 2D 00 32#2 6 4 9 2 F - 2
    00 46 00 36   00 39 00 2D   00 34 00 36   00 42 00 38#F 6 9 - 4 6 B 8
    00 2D 00 42   00 39 00 42   00 46 00 2D   00 35 00 36#- B 9 B F - 5 6
    00 35 00 34   00 46 00 43   00 30 00 37   00 45 00 34#5 4 F C 0 7 E 4
    00 32 00 33   00 7D 00 00   00 00 00 00   00 00 00 00#2 3 }
    00 00 00 00   00


－－－－－－－－－－－－－
#how?
#   在"控制面板\系统和安全\网络连接"，右击"本地连接"，"创建快捷方式"
#   在桌面，看其属性，得"{BA126ADB-2166-11D1-B1D0-00805FC1270E}"
#DB6A12BA6621D111B1D000805FC1270E
"本地连接.lnk" # 402 bytes
    －－－－－－－
    4C0000000114020000000000C0000000
    00000046810008000000000000000000
    00000000000000000000000000000000
    00000000000000000000000001000000
    00000000000000000000000040011400
    1F802020EC21EA3A6910A2DD08002B30
    309D1E00718000000000000000000000
    C7AC07700232D111AAD200805FC1270E
    0C01FF4E03000000FF5E0000DB6A12BA
    6621D111B1D000805FC1270E1FD4377C
    27AB90439F05253C3BC0096F09100000
    03000000070000008400000010000000
    000000000A0000000A0000007A000000
    01000000940000000200000000000000
    00000000000000009600000002000000
    2C673057DE8FA5630000410074006800
    650072006F0073002000410052003800
    31003500310020005000430049002D00
    45002000470069006700610062006900
    74002000450074006800650072006E00
    65007400200043006F006E0074007200
    6F006C006C0065007200200028004E00
    440049005300200036002E0032003000
    290000001FD4377C27AB90439F05253C
    3BC0096F000000000000000000000000
    0000
    －－－－－－－－－－－ gvim: ctrl+v; blockwise copy+paste
    4C 00 00 00   01 14 02 00   00 00 00 00   C0 00 00 00
    00 00 00 46   81 00 08 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   01 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   40 01 14 00
    1F 80 20 20   EC 21 EA 3A   69 10 A2 DD   08 00 2B 30
    30 9D 1E 00   71 80 00 00   00 00 00 00   00 00 00 00
    C7 AC 07 70   02 32 D1 11   AA D2 00 80   5F C1 27 0E
    0C 01 FF 4E   03 00 00 00   FF 5E 00 00   DB 6A 12 BA
    66 21 D1 11   B1 D0 00 80   5F C1 27 0E   1F D4 37 7C
    27 AB 90 43   9F 05 25 3C   3B C0 09 6F   09 10 00 00
    03 00 00 00   07 00 00 00   84 00 00 00   10 00 00 00
    00 00 00 00   0A 00 00 00   0A 00 00 00   7A 00 00 00
    01 00 00 00   94 00 00 00   02 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   96 00 00 00   02 00 00 00
    2C 67 30 57   DE 8F A5 63   00 00 41 00   74 00 68 00
    65 00 72 00   6F 00 73 00   20 00 41 00   52 00 38 00
    31 00 35 00   31 00 20 00   50 00 43 00   49 00 2D 00
    45 00 20 00   47 00 69 00   67 00 61 00   62 00 69 00
    74 00 20 00   45 00 74 00   68 00 65 00   72 00 6E 00
    65 00 74 00   20 00 43 00   6F 00 6E 00   74 00 72 00
    6F 00 6C 00   6C 00 65 00   72 00 20 00   28 00 4E 00
    44 00 49 00   53 00 20 00   36 00 2E 00   32 00 30 00
    29 00 00 00   1F D4 37 7C   27 AB 90 43   9F 05 25 3C
    3B C0 09 6F   00 00 00 00   00 00 00 00   00 00 00 00
    00 00
    －－－－－－－－－－－
    4C 00 00 00   01 14 02 00   00 00 00 00   C0 00 00 00
    00 00 00 46   81 00 08 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   01 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   40 01 14 00
    1F 80 20 20   EC 21 EA 3A   69 10 A2 DD   08 00 2B 30
    30 9D 1E 00   71 80 00 00   00 00 00 00   00 00 00 00
         ?(^^^^^^^^^^^^ ~~~~~   ^^^^^ ~~~~~   ^^^^^^^^^^)
    C7 AC 07 70   02 32 D1 11   AA D2 00 80   5F C1 27 0E
    (^^^)?
    0C 01 FF 4E   03 00 00 00   FF 5E 00 00   DB 6A 12 BA
                                              ^^^^^^^^^^^
    66 21 D1 11   B1 D0 00 80   5F C1 27 0E   1F D4 37 7C
    ~~~~~ ^^^^^   ~~~~~ ^^^^^^^^^^^^^^^^^^^
    27 AB 90 43   9F 05 25 3C   3B C0 09 6F   09 10 00 00
    03 00 00 00   07 00 00 00   84 00 00 00   10 00 00 00
    00 00 00 00   0A 00 00 00   0A 00 00 00   7A 00 00 00
    01 00 00 00   94 00 00 00   02 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   96 00 00 00   02 00 00 00
    2C 67 30 57   DE 8F A5 63   00 00 41 00   74 00 68 00
    65 00 72 00   6F 00 73 00   20 00 41 00   52 00 38 00
    31 00 35 00   31 00 20 00   50 00 43 00   49 00 2D 00
    45 00 20 00   47 00 69 00   67 00 61 00   62 00 69 00
    74 00 20 00   45 00 74 00   68 00 65 00   72 00 6E 00
    65 00 74 00   20 00 43 00   6F 00 6E 00   74 00 72 00
    6F 00 6C 00   6C 00 65 00   72 00 20 00   28 00 4E 00
    44 00 49 00   53 00 20 00   36 00 2E 00   32 00 30 00
    29 00 00 00   1F D4 37 7C   27 AB 90 43   9F 05 25 3C
    3B C0 09 6F   00 00 00 00   00 00 00 00   00 00 00 00
    00 00

'''





__all__ = '''
    mk_windows_spec_lnk
    _mk_windows_spec_lnk
    main

    windows_firewall_spec_addr__str
    web_connection_spec_addr__str
    local_connection_spec_addr__str

    windows_firewall_lnk_file__human
    windows_firewall_lnk_file__hex
    windows_firewall_lnk_file__bytes

    local_connection_lnk_file__human
    local_connection_lnk_file__hex
    local_connection_lnk_file__bytes
    '''.split()

import binascii # unhexlify
import re




def data_human2hex(data_human):
    return ''.join(data_human.split()).upper()
def data_hex2bytes(data_hex):
    return binascii.unhexlify(data_hex)
def data_human2bytes(data_human):
    return data_hex2bytes(data_human2hex(data_human))
def data_human2hex_and_bytes(data_human):
    data_hex = data_human2hex(data_human)
    data_bytes = data_hex2bytes(data_hex)
    return (data_hex, data_bytes)
def ascii_str2bytes(ascii_str):
    return ascii_str.encode('ascii')
def bytes_join_00(data_bytes):
    #bug:return b'\0'.join(data_bytes)
    #   iter(data_bytes)::Iter int # not (Iter bytes)
    def mk_iter():
        for i in data_bytes:
            yield i
            yield 0
    return bytes(mk_iter())


def spec_addr_str_to_00bytes(spec_addr__str):
    return bytes_join_00(ascii_str2bytes(spec_addr__str))





windows_firewall_lnk_file__human = '''
    4C 00 00 00   01 14 02 00   00 00 00 00   C0 00 00 00
    00 00 00 46   81 00 08 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   01 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   40 00 14 00
    1F 70 68 06   EE 26 0A A0   D7 44 93 71   BE B0 64 C9
    86 83 0C 00   01 00 84 21   DE 39 05 00   00 00 1E 00
    71 80 00 00   00 00 00 00   00 00 00 00   2F 49 26 40
    69 2F B8 46   B9 BF 56 54   FC 07 E4 23   00 00 43 01
    00 00 09 00   00 A0 62 00   00 00 31 53   50 53 30 F1
    25 B7 EF 47   1A 10 A5 F1   02 60 8C 9E   EB AC 29 00
    00 00 0A 00   00 00 00 1F   00 00 00 0C   00 00 00 57
    00 69 00 6E   00 64 00 6F   00 77 00 73   00 20 00 32
    96 6B 70 99   58 00 00 1D   00 00 00 04   00 00 00 00
    1F 00 00 00   06 00 00 00   FB 7C DF 7E   87 65 F6 4E
    39 59 00 00   00 00 00 00   D5 00 00 00   31 53 50 53
    A6 6A 63 28   3D 95 D2 11   B5 D6 00 C0   4F D9 18 D0
    B9 00 00 00   1E 00 00 00   00 1F 00 00   00 54 00 00
    00 3A 00 3A   00 7B 00 32   00 36 00 45   00 45 00 30
    00 36 00 36   00 38 00 2D   00 41 00 30   00 30 00 41
    00 2D 00 34   00 34 00 44   00 37 00 2D   00 39 00 33
    00 37 00 31   00 2D 00 42   00 45 00 42   00 30 00 36
    00 34 00 43   00 39 00 38   00 36 00 38   00 33 00 7D
    00 5C 00 35   00 5C 00 3A   00 3A 00 7B   00 34 00 30
    00 32 00 36   00 34 00 39   00 32 00 46   00 2D 00 32
    00 46 00 36   00 39 00 2D   00 34 00 36   00 42 00 38
    00 2D 00 42   00 39 00 42   00 46 00 2D   00 35 00 36
    00 35 00 34   00 46 00 43   00 30 00 37   00 45 00 34
    00 32 00 33   00 7D 00 00   00 00 00 00   00 00 00 00
    00 00 00 00   00
'''

local_connection_lnk_file__human = r'''
    4C 00 00 00   01 14 02 00   00 00 00 00   C0 00 00 00
    00 00 00 46   81 00 08 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   01 00 00 00
    00 00 00 00   00 00 00 00   00 00 00 00   40 01 14 00
    1F 80 20 20   EC 21 EA 3A   69 10 A2 DD   08 00 2B 30
    30 9D 1E 00   71 80 00 00   00 00 00 00   00 00 00 00
    C7 AC 07 70   02 32 D1 11   AA D2 00 80   5F C1 27 0E
    0C 01 FF 4E   03 00 00 00   FF 5E 00 00   DB 6A 12 BA
    66 21 D1 11   B1 D0 00 80   5F C1 27 0E   1F D4 37 7C
    27 AB 90 43   9F 05 25 3C   3B C0 09 6F   09 10 00 00
    03 00 00 00   07 00 00 00   84 00 00 00   10 00 00 00
    00 00 00 00   0A 00 00 00   0A 00 00 00   7A 00 00 00
    01 00 00 00   94 00 00 00   02 00 00 00   00 00 00 00
    00 00 00 00   00 00 00 00   96 00 00 00   02 00 00 00
    2C 67 30 57   DE 8F A5 63   00 00 41 00   74 00 68 00
    65 00 72 00   6F 00 73 00   20 00 41 00   52 00 38 00
    31 00 35 00   31 00 20 00   50 00 43 00   49 00 2D 00
    45 00 20 00   47 00 69 00   67 00 61 00   62 00 69 00
    74 00 20 00   45 00 74 00   68 00 65 00   72 00 6E 00
    65 00 74 00   20 00 43 00   6F 00 6E 00   74 00 72 00
    6F 00 6C 00   6C 00 65 00   72 00 20 00   28 00 4E 00
    44 00 49 00   53 00 20 00   36 00 2E 00   32 00 30 00
    29 00 00 00   1F D4 37 7C   27 AB 90 43   9F 05 25 3C
    3B C0 09 6F   00 00 00 00   00 00 00 00   00 00 00 00
    00 00


'''





(windows_firewall_lnk_file__hex
,windows_firewall_lnk_file__bytes
) = data_human2hex_and_bytes(windows_firewall_lnk_file__human)
(local_connection_lnk_file__hex
,local_connection_lnk_file__bytes
) = data_human2hex_and_bytes(local_connection_lnk_file__human)


windows_firewall_spec_addr_part0__str = '{26EE0668-A00A-44D7-9371-BEB064C98683}'
windows_firewall_spec_addr_part2__str = '{4026492F-2F69-46B8-B9BF-5654FC07E423}'
windows_firewall_spec_addr_part0__bytes = data_human2bytes('68 06   EE 26 0A A0   D7 44 93 71   BE B0 64 C9   86 83')
windows_firewall_spec_addr_part2__bytes = data_human2bytes('2F 49 26 40   69 2F B8 46   B9 BF 56 54   FC 07 E4 23')
windows_firewall_spec_addr__str = r'::{26EE0668-A00A-44D7-9371-BEB064C98683}\5\::{4026492F-2F69-46B8-B9BF-5654FC07E423}'
windows_firewall_bottom_spec_addr__bytes = spec_addr_str_to_00bytes(windows_firewall_spec_addr__str)

web_connection_spec_addr__str = r'::{26EE0668-A00A-44D7-9371-BEB064C98683}\3\::{7007ACC7-3202-11D1-AAD2-00805FC1270E}'

local_connection_spec_addr__bytes = data_human2bytes('DB 6A 12 BA   66 21 D1 11   B1 D0 00 80   5F C1 27 0E')
    #'DB6A12BA6621D111B1D000805FC1270E'
local_connection_spec_addr__str = r'{BA126ADB-2166-11D1-B1D0-00805FC1270E}'

assert 469 == len(windows_firewall_lnk_file__bytes)
assert 1 == windows_firewall_lnk_file__bytes.count(windows_firewall_spec_addr_part0__bytes)
assert 1 == windows_firewall_lnk_file__bytes.count(windows_firewall_spec_addr_part2__bytes)
assert 1 == windows_firewall_lnk_file__bytes.count(windows_firewall_bottom_spec_addr__bytes)

assert 402 == len(local_connection_lnk_file__bytes)
assert 1 == local_connection_lnk_file__bytes.count(local_connection_spec_addr__bytes)

xdigit_ptn = r'[0-9A-Fa-f]'
spec_addr_part_ptn = fr'(?:\{{{xdigit_ptn}{{8}}-{xdigit_ptn}{{4}}-{xdigit_ptn}{{4}}-{xdigit_ptn}{{4}}-{xdigit_ptn}{{12}}\}})'
    # reverse8 reverse4 reverse4  same4 same12
spec_addr_ptn = fr'(?:::(?P<spec_addr_part0>{spec_addr_part_ptn})\\(?P<part1>\d)\\::(?P<spec_addr_part2>{spec_addr_part_ptn}))'
spec_addr_part_regex = re.compile(spec_addr_part_ptn)
spec_addr_regex = re.compile(spec_addr_ptn)


def parse_spec_addr(spec_addr__str):
    # -> (spec_addr_part0__str, n, spec_addr_part2__str)
    m = spec_addr_regex.fullmatch(spec_addr__str)
    if not m:
        spec_addr_example = windows_firewall_spec_addr__str
        raise ValueError(f'not spec_addr, which should look like {spec_addr_example!r} not {spec_addr__str!r}')
    spec_addr_part0__str = m['spec_addr_part0']
    n = int(m['part1'])
    spec_addr_part2__str = m['spec_addr_part2']
    return spec_addr_part0__str, n, spec_addr_part2__str

def parse_spec_addr_part(spec_addr_part__str):
    m = spec_addr_part_regex.fullmatch(spec_addr_part__str)
    if not m:
        spec_addr_part_example = windows_firewall_spec_addr_part0__str
        raise ValueError(f'not spec_addr_part, which should look like {spec_addr_part_example!r} not {spec_addr_part__str!r}')
    data_hex_ls = spec_addr_part__str[1:-1].split('-')
    assert len(data_hex_ls) == 5
    data_bytes_ls = list(map(data_hex2bytes, data_hex_ls))
    for i in range(3):
        bs = data_bytes_ls[i]
        bs = bytes(reversed(bs))
        data_bytes_ls[i] = bs
    data_bytes = b''.join(data_bytes_ls)
    assert len(data_bytes) == 16
    return data_bytes
assert windows_firewall_spec_addr_part0__bytes == parse_spec_addr_part(windows_firewall_spec_addr_part0__str)
assert windows_firewall_spec_addr_part2__bytes == parse_spec_addr_part(windows_firewall_spec_addr_part2__str)


def mk_windows_spec_lnk(spec_addr__str):
    #spec_addr__str like windows_firewall_spec_addr__str
    return mk_windows_spec_lnk__long(spec_addr__str)
def mk_windows_spec_lnk__short(spec_addr__str):
    #spec_addr__str like local_connection_spec_addr__str
    raise NotImplementedError
def mk_windows_spec_lnk__long(spec_addr__str):
    #spec_addr__str like windows_firewall_spec_addr__str
    (spec_addr_part0__str, n, spec_addr_part2__str
    ) = parse_spec_addr(spec_addr__str)
    lnk_file_bytes = _mk_windows_spec_lnk(spec_addr_part0__str, n, spec_addr_part2__str)
    #### TODO: n and bottom addr str
    bottom_bytes = spec_addr_str_to_00bytes(spec_addr__str)
    lnk_file_bytes = lnk_file_bytes.replace(windows_firewall_bottom_spec_addr__bytes, bottom_bytes)
    #### TODO: n
    return lnk_file_bytes

def _mk_windows_spec_lnk(spec_addr_part0__str, n, spec_addr_part2__str):
    assert 0 <= n <= 9
    spec_addr_part0__bytes = parse_spec_addr_part(spec_addr_part0__str)
    spec_addr_part2__bytes = parse_spec_addr_part(spec_addr_part2__str)
    bs = windows_firewall_lnk_file__bytes
    bs = bs.replace(windows_firewall_spec_addr_part0__bytes, spec_addr_part0__bytes)
    bs = bs.replace(windows_firewall_spec_addr_part2__bytes, spec_addr_part2__bytes)
    #### TODO: n and bottom addr str
    lnk_file_bytes = bs
    return lnk_file_bytes

assert windows_firewall_lnk_file__bytes == mk_windows_spec_lnk(windows_firewall_spec_addr__str)

def _t():
    web_connect_lnk_file__bytes = _mk_windows_spec_lnk('{26EE0668-A00A-44D7-9371-BEB064C98683}', 3, '{7007ACC7-3202-11D1-AAD2-00805FC1270E}')
    with open('web_connect.lnk', 'wb') as ofile:
        ofile.write(web_connect_lnk_file__bytes)
def _t2():
    web_connect_lnk_file__bytes = mk_windows_spec_lnk(web_connection_spec_addr__str)
    with open('web_connect2.lnk', 'wb') as ofile:
        ofile.write(web_connect_lnk_file__bytes)


def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='make Windows special address link file'
        , epilog=f'spec_addr example: {windows_firewall_spec_addr__str!r}'
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-a', '--spec_addr', type=str, required=True
                        , help='spec_addr; for example, see epilog')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    omode = 'wb' if args.force else 'xb'

    lnk_file_bytes = mk_windows_spec_lnk(args.spec_addr)
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=None) as fout:
        fout.write(lnk_file_bytes)

if __name__ == "__main__":
    main()





