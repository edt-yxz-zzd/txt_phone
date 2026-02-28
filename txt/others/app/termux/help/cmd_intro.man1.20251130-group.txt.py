
r'''[[[
e others/app/termux/help/cmd_intro.man1.20251130-group.txt.py
py others/app/termux/help/cmd_intro.man1.20251130-group.txt.py # 2>/dev/null # >> others/app/termux/help/cmd_intro.man1.20251130-group.txt
    stderr:show old/known (dup|bad) nm
    stdout:show new/unknown (dup|bad) nm



#]]]'''#'''


path7orginal = 'others/app/termux/help/cmd_intro.man1.txt'
path7grouping = 'others/app/termux/help/cmd_intro.man1.20251130-group.txt'
from pathlib import Path
from collections import Counter
from sys import stderr

def read(path, /, dup_ok=False):
    lines = Path(path).read_text('utf8').split('\n')
    try:
        j = lines.index(':::start:::')
    except ValueError:
        pass
    else:
        del lines[:j+1]
    lines = [s for s in lines if s[:1].isalnum()]
    #
    #.sz = len(lines)
    #.lines = sorted(set(lines))
    #.dup = not sz == len(lines)
    #.if dup and not dup_ok:
    #.    raise ValueError('dup')
    s2n = Counter(lines)
    lines = sorted(s2n.keys())
    if not dup_ok:
        for s in lines:
            n = s2n[s]
            if n > 1:
                print('dup line:', s)
    return lines

dup_nms7known = 'gst-doc,osage,patchwork'.split(',')
bad_nms7known = 'Termux,LFortran,persistent memory gawk,Smalltalk,brotli(1),gvmap.sh,Wget'.split(',')
def verify(path7orginal, path7grouping, /):
    lines7orginal = read(path7orginal, dup_ok=True)
    lines7grouping = read(path7grouping)
    missings = set(lines7orginal) -set(lines7grouping)
    if missings:
        for s in sorted(missings):
            print('missing line:', s)
    nms = set()
    dups = []
    for s in lines7grouping:
        if ' -- ' in s:
            j = s.index(' -- ')
        elif ' - ' in s:
            j = s.index(' - ')
        else:
            print('bad line:', s)
            continue
        s = s[:j]
        _nms = {t.strip() for t in s.split(',')}
        for nm in _nms:
            if nm in nms:
                dups.append(nm)
            nms.add(nm)
    dups = sorted(set(dups))
    for nm in dups:
        if nm in dup_nms7known:
            print('# known dup nm:', nm, file=stderr)
        else:
            print('dup nm:', nm)
    for nm in nms:
        _nm = f'a{nm}'.replace('-', '_')
        if not (nm == nm.lower() and _nm.isidentifier()):
            if nm in bad_nms7known:
                print('# known bad nm:', nm, file=stderr)
            else:
                print('bad nm:', nm)

verify(path7orginal, path7grouping)



