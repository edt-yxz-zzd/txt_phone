
'''
<src>/xxx.svg
==>>
    <dst>/svg_as_png/xxx.svg_as.png
    <dst>/svg_to_png/xxx.svg_to.png
'''

#from glob import iglob
from pathlib import Path
import filecmp # cmp
import shutil # copy2
import cairosvg # svg2png

assert bool(...) is True
def is_older_than(file1:Path, file2:Path):
    if not file1.is_file(): raise Exception('{file1!r} is not a file')
    if not file2.is_file(): raise Exception('{file2!r} is not a file')

    #return filecmp.cmp(file1, file2)
    stat1 = file1.stat()
    stat2 = file2.stat()
    return stat1.st_mtime < stat2.st_mtime

def is_same_file__careless(file1:Path, file2:Path):
    '''

return:
    ... - (size, last_modified_time) be the same
    True - content be the same
    False - content be different
'''
    if not file1.is_file(): raise Exception('{file1!r} is not a file')
    if not file2.is_file(): raise Exception('{file2!r} is not a file')

    #return filecmp.cmp(file1, file2)
    stat1 = file1.stat()
    stat2 = file2.stat()
    if stat1.st_size != stat2.st_size:
        return False
    if stat1.st_mtime != stat2.st_mtime:
        # careless
        return ...
    return bool(filecmp.cmp(file1, file2))

def main1(src, **kwargs):
    src = dst = Path(src)
    return main2(src, dst, **kwargs)
def main2(src, dst, **kwargs):
    src = Path(src)
    dst = Path(dst)

    svg_folder = src
    svg_as_png_folder = dst / 'svg_as_png'
    svg_to_png_folder =  dst / 'svg_to_png'
    return main3(svg_folder, svg_as_png_folder, svg_to_png_folder, **kwargs)
def main3(svg_folder, svg_as_png_folder, svg_to_png_folder, *, verbose:bool):
    svg_folder = Path(svg_folder)
    svg_as_png_folder = Path(svg_as_png_folder)
    svg_to_png_folder = Path(svg_to_png_folder)
    verbose = bool(verbose)
    assert not verbose
    main__svg_as_png(svg_folder, svg_as_png_folder)
    main__svg_to_png(svg_folder, svg_to_png_folder)

def main__svg_to_png(svg_folder, svg_to_png_folder):
    svg_folder = Path(svg_folder)
    svg_to_png_folder = Path(svg_to_png_folder)
    for svg_path in svg_folder.glob('*.svg'):
        if not svg_path.is_file(): continue

        stem = svg_path.stem
        svg_to_png_path = svg_to_png_folder / (stem+'.svg_to.png')

        str_svg_to_png_path = str(svg_to_png_path)
        str_svg_path = str(svg_path)
        if svg_to_png_path.exists():
            if not svg_to_png_path.is_file():
                eprint(f'convert {str_svg_path!r} to {str_svg_to_png_path!r}: dst is an existing directory!')
            #elif not filecmp.cmp(svg_path, svg_to_png_path):
            elif not is_older_than(svg_path, svg_to_png_path):
                eprint(f'convert {str_svg_path!r} to {str_svg_to_png_path!r}: dst - existing and older!')
            else:
                # existing but new
                pass
        else:
            # not existing
            #xxx:cairosvg.svg2png(url=svg_path, write_to=svg_to_png_path)
            #xxx:cairosvg.svg2png(file_obj=str_svg_path, write_to=str_svg_to_png_path)
            cairosvg.svg2png(svg_path.read_bytes(), write_to=str_svg_to_png_path)


def main__svg_as_png(svg_folder, svg_as_png_folder):
    svg_folder = Path(svg_folder)
    svg_as_png_folder = Path(svg_as_png_folder)
    #svg_folder.glob('*.svg')
    #for svg_path in iglob(str(svg_folder / '*.svg'), recursive=False):
    for svg_path in svg_folder.glob('*.svg'):
        if not svg_path.is_file(): continue

        stem = svg_path.stem
        svg_as_png_path = svg_as_png_folder / (stem+'.svg_as.png')
        if svg_as_png_path.exists():
            str_svg_as_png_path = str(svg_as_png_path)
            str_svg_path = str(svg_path)
            if not svg_as_png_path.is_file():
                eprint(f'copy {str_svg_path!r} to {str_svg_as_png_path!r}: dst is an existing directory!')
            #elif not filecmp.cmp(svg_path, svg_as_png_path):
            elif not is_same_file__careless(svg_path, svg_as_png_path):
                eprint(f'copy {str_svg_path!r} to {str_svg_as_png_path!r}: dst - existing and diff!')
            else:
                # existing but same
                pass
        else:
            # not existing
            shutil.copy2(svg_path, svg_as_png_path)

if __name__ == '__main__':
    src = '.'
    src = Path(__file__).parent
    main1(src, verbose=False)

