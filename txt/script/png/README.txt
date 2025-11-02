
e script/png/README.txt

png specification:
  view ../lots/NOTE/image/png/www-png.txt
    view /sdcard/0my_files/unzip/png_specification/www.libpng.org/pub/png/spec/1.2/PNG-Contents.html
    view /sdcard/0my_files/unzip/png_specification/www.w3.org/TR/png-3/index.html

  view ../lots/NOTE/image/png/png_3-w3_org-note.txt
    view /sdcard/0my_files/unzip/png_specification/www.w3.org/TR/png-3/index.html
    view /sdcard/0my_files/tmp/out4py/html2text/w3_org-png_3-index.html.txt

[[

[png_file == (png_file_signature, chunks/[chunk])]

[png_file_signature == b'\x89PNG\r\n\x1a\n']
    #bytes([137,80,78,71,13,10,26,10])

[chunks[0].chunk_type == 'IHDR']
[chunks[-1].chunk_type == 'IEND']

[chunk == (len4data, chunk_type, data, crc4typ_dat)]

[data :: bytes{len==len4data}]
[len4data :: bytes{len==4}{big_endian_32bit_uint}{uint%2**31}]
    32bit但最高爻元置零
[crc4typ_dat :: bytes{len==4}{big_endian_32bit_uint}]
[chunk_type :: bytes{len==4}]
    每一字节的(1<<5)爻元 是 超类型:
      + 欤补助/欤非紧要
      + 欤私用
      + <保留{当下置零}>欤扩展
      + 欤安全复制/欤不依赖其他类型块/欤独列类型
    大写字母:A-Z:0x41..0x5A
    小写字母:a-z:0x61..0x7A
    两者:同:
        第七爻元:0#最高爻元
        第六爻元:1#次高爻元
    两者:异:
        第五爻元:0#大写字母
        第五爻元:1#小写字母
    >>> bin(ord('Z'))
    '0b1011010'
    >>> bin(ord('A'))
    '0b1000001'
    >>> bin(ord('z'))
    '0b1111010'
    >>> bin(ord('a'))
    '0b1100001'
    ...6543210


#from:w3_org-png_3:
PNG four-byte unsigned integer
  a four-byte unsigned integer limited to the range 0 to 2^31-1.
    Note:The restriction is imposed in order to accommodate languages that have difficulty with unsigned four-byte values.
]]
