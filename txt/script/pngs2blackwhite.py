
r'''

py script/pngs2blackwhite.py   -i '/sdcard/0my_files/tmp/graph/hand_draw-plantri-adc3m3-4d16d~sz306~[not_blackwhite]/'  -o  '/sdcard/0my_files/tmp/graph/tmp_out/'
====
png二值化
  由于实际操作中的种种原因，png白色真白，但黑色不黑，用python::purepng库 使png颜色 二值化
  由于 Pixly 不支持 bitdepth=1, 这里 只用 bitdepth=8
  由于 Pixly 将 greyscale=True 保存的图 读作 alpha 通道，这里 只用 greyscale=False





====
view script/draw_tri_planar_graphs.py.data/hand_draw-readme.txt

view script/pngs2blackwhite.py
  png二值化
  view others/app/termux/py_pip/purepng.txt



====
pip install purepng
import png

====



=======copy from purepng.txt
import png

idir = '/sdcard/0my_files/git_repos/txt_phone/draw-plantri-adc3m3/.'
odir = '/sdcard/0my_files/tmp/graph/png/.'

path_sq = f'{idir}/32_32_sq.png'
path_035 = f'{idir}/035.png'
opng35_fmt = '/sdcard/0my_files/tmp/tmp035_{}.png'

r = png.Reader(path_sq).read()
  (32, 32, <map object at 0xb66d8c10>, {'greyscale': False, 'alpha': True, 'planes': 4, 'bitdepth': 8, 'interlace': 0, 'size': (32, 32), 'text': {}})
m = [*r[2]]
len(m)
  32
len(m[0])
  128 == 32*4 bytes

r35 = png.Reader(path_035).read()
  #(x-width-col, y-height-row)
  (64, 32, <map object at 0xb66d8df0>, {'greyscale': False, 'alpha': True, 'planes': 4, 'bitdepth': 8, 'interlace': 0, 'size': (64, 32), 'text': {}})
m35 = [*r35[2]]
len(m35)
  32 rows
len(m35[0])
  256 == 64*4  bytes cols*RGBA #0xff - 最饱和、最透明



...
...
...


m35_bit = rgba_to_bit(m35, input_alpha=True)
m35_byte = rgba_to_byte(m35, input_alpha=True)
m35_rgb_bw = rgba_to_rgb_bw(m35, input_alpha=True)


#png.Writer(width:num_columns, height:num_rows, greyscale=True, bitdepth=bbb,palette=[[int%2**bbb]{3|4}]).write(fout, [[int%2**bbb]{width}]{height})
  "bitdepth < 8 only permitted with greyscale or palette"
  "alpha and palette not compatible
  "greyscale and palette not compatible"
  palette=None|len<-[1..256]&&len(self[0])<)[3..4]

with open(opng35_fmt.format('byte_grey'), 'xb') as fout:
  png.Writer(64, 32, greyscale=True, bitdepth=8,palette=None,alpha=False).write(fout, m35_byte)
  # => 172 B

with open(opng35_fmt.format('bit_grey'), 'xb') as fout:
  png.Writer(64, 32, greyscale=True, bitdepth=1,palette=None,alpha=False).write(fout, m35_bit)
  # => 146 B

with open(opng35_fmt.format('bit_palette'), 'xb') as fout:
  png.Writer(64, 32, greyscale=False, bitdepth=1,palette=[(0,0,0), (0xff,0xff,0xff)],alpha=False).write(fout, m35_bit)
    #竟然不是(1,1,1) !!! 而是 (0xff,0xff,0xff)
  # => 164 B

with open(opng35_fmt.format('bw_palette'), 'xb') as fout:
  png.Writer(64, 32, greyscale=False, bitdepth=8,palette=[(0,0,0), (0xff,0xff,0xff)],alpha=False).write(fout, m35_bit)
  # => 190 B

with open(opng35_fmt.format('rgb_bw'), 'xb') as fout:
  png.Writer(64, 32, greyscale=False, bitdepth=8,palette=None,alpha=False).write(fout, m35_rgb_bw)
  # => 228 B



hand_draw_rgba_pngs_to_rgb_bw(odir, idir)



#'''

try:
    from seed.for_libs.for_logging import disable_logging
except ImportError:
    import logging
    logging.disable()
    try:
        import png
    finally:
        logging.disable(logging.NOTSET)
    #rint('here')
else:
    with disable_logging():
        import png

if 1:
    import logging
    assert logging.getLogger() is logging.getLogger('')
    assert logging.getLogger() is not logging.getLogger('root')
    logging.disable()
    logging.disable(logging.NOTSET)


from pathlib import Path

#updated: add force
def hand_draw_rgba_pngs_to_rgb_bw(odir, idir, *, force):
  idir = Path(idir)
  odir = Path(odir)
  omode = 'wb' if force else 'xb'

  for ipng in idir.glob('*.png'):
    opng = odir / ipng.name
    (width, height, mx_rgba, attrs) = png.Reader(str(ipng)).read()
    #(32, 32, <map object at 0xb66d8c10>, {'greyscale': False, 'alpha': True, 'planes': 4, 'bitdepth': 8, 'interlace': 0, 'size': (32, 32), 'text': {}})
    if attrs['bitdepth'] == 8 and not attrs['greyscale']:pass
    else:
      raise NotImplementedError
    input_alpha = attrs['alpha']
    mx_rgb_bw = rgba_to_rgb_bw(mx_rgba, input_alpha=input_alpha)
    with open(opng, omode) as fout:
      png.Writer(width, height, greyscale=False, bitdepth=8,palette=None,alpha=False).write(fout, mx_rgb_bw)


def rgba_to_bit(m, *, input_alpha):
  def f(r,g,b,a):
    return (r,g,b) == (0xff,0xff,0xff)
  return rgba_to_xxx(f, m, input_alpha=input_alpha)

def rgba_to_byte(m, *, input_alpha):
  def f(r,g,b,a):
    x = (r,g,b) == (0xff,0xff,0xff)
    return 0xff * x
  return rgba_to_xxx(f, m, input_alpha=input_alpha)

def rgba_to_rgb_bw(m, *, input_alpha):
  def f(r,g,b,a):
    black = (0x00,0x00,0x00)
    white = (0xff,0xff,0xff)
    is_white = (r,g,b) == white
    return white if is_white else black
  return rgba_to_xxx(f, m, input_alpha=input_alpha)

def rgba_to_xxx(f, m, *, input_alpha):
  step = 4 if input_alpha else 3
  xss = []
  for row in m:
    w = len(row)//step
    assert w*step == len(row)
    xs = []
    for i in range(w):
      rgbx = row[step*i:step*i+step]
      if step == 4:
        r,g,b,a = rgbx
      else:
        r,g,b = rgbx
        a = None
      x = f(r,g,b,a)
      try:
        it = iter(x)
      except TypeError:
        xs.append(x)
      else:
        xs.extend(it)
    xss.append(xs)
  return xss











def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='convert png color to black/white only'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None, required=True
                        , help='input folder')
    parser.add_argument('-o', '--output', type=str, default=None, required=True
                        , help='output folder')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    hand_draw_rgba_pngs_to_rgb_bw(
        odir=args.output
        ,idir=args.input
        ,force = args.force
        )
if __name__ == "__main__":
    main()


