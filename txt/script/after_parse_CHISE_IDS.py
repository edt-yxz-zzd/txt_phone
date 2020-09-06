
r"""
ParsedResult = Map hz {key:[ParsedIDS]}
ParsedIDS
    = ('hz', hz)
    | ('ref', ref)
    | (op, *args)

op = ⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻




#"""

r"""
parse_CHISE_IDS.py
after_parse_CHISE_IDS.py
===============

cd /sdcard/0my_files/unzip/e_book/汉字分解/CHISE_IDS[67b94ff]/ids-67b94ff
py ~/txt/script/parse_CHISE_IDS.py -o ~/tmp/ids_all_1.txt ./IDS-UCS-*.txt -se -f 2>~/tmp/ids_all_1_err.txt

cd /sdcard/0my_files/unzip/e_book/汉字分解/chise-ids-ea97c5d[20200812]/ids-ea97c5d
py ~/txt/script/parse_CHISE_IDS.py -o ~/tmp/ids_all_2.txt ./IDS-UCS-*.txt -se -f 2>~/tmp/ids_all_2_err.txt

diff  ~/tmp/ids_all_1_err.txt ~/tmp/ids_all_2_err.txt

less  ~/tmp/ids_all_1_err.txt
less  ~/tmp/ids_all_2_err.txt


cd ~/txt
py script/after_parse_CHISE_IDS.py -e utf8 -o ~/tmp/after_ids_pp_1.txt -i ~/tmp/ids_all_1.txt -f
py script/after_parse_CHISE_IDS.py -e utf8 -o ~/tmp/after_ids_pp_2.txt -i ~/tmp/ids_all_2.txt -f
diff  ~/tmp/after_ids_pp_1.txt ~/tmp/after_ids_pp_2.txt

less  ~/tmp/after_ids_pp_1.txt
less  ~/tmp/after_ids_pp_2.txt

#"""




from pathlib import Path
import ast
from pprint import pprint
import re
from seed.tiny import print_err


class Recur:pass
class Stop:pass

class HandleParsedResult:
    def __init__(sf, hz2HandleParsedIDS):
        sf.hz2HandleParsedIDS = hz2HandleParsedIDS
    def feed(sf, hz2key2ParsedIDSs:'ParsedResult'):
        for hz, key2idss in hz2key2ParsedIDSs.items():
            hnd = sf.hz2HandleParsedIDS(hz)
            if type(key2idss) is not dict:
                print(f'{hz!r}')
                print(f'{key2idss!r}')
                print(hz, repr(hz), hex(ord(hz)))
                print(key2idss)
            for idss in key2idss.values():
                for ids in idss:
                    hnd.main(ids)
class HandleParsedIDS:
    def main(sf, ids):
        ls = [ids]
        while ls:
            ids = ls.pop()
            case = ids[0]
            if case == 'hz':
                _, hz = ids
                sf.handle_hz(hz, ids=ids)
            elif case == 'ref':
                _, ref = ids
                sf.handle_ref(ref, ids=ids)
            else:
                op, *args = ids
                r = sf.handle_op(op, *args, ids=ids)
                if r is Stop:
                    pass
                elif r is Recur:
                    ls.extend(reversed(args))

    def handle_op(sf, op, *args, ids):
        return Recur
    def handle_hz(sf, hz, *, ids):
        return Recur
    def handle_ref(sf, ref, *, ids):
        return Recur


def _add(d, k, hz):
    hz_ls = d.setdefault(k, [])
    hz_ls.append(hz)
r"""
class HandleParsedIDS__apply_ref2hz(HandleParsedIDS):
    def __init__(sf, ref2hz, key2forest):
        sf.ref2hz= ref2hz
        sf.key2forest = key2forest
    def handle_hz(sf, hz, *, ids):
        _add(sf.key2forest, hz, sf.hz)
        return Recur
    def handle_ref(sf, ref, *, ids):
        _add(sf.key2forest, ref, sf.hz)
        return Recur
    def handle_op(sf, op, *args, ids):
        if op == '⿻':
            k = repr(ids)
            _add(sf.key2forest, k, sf.hz)
            return Stop
        return Recur
#"""

class HandleParsedIDS__all_hz_ref(HandleParsedIDS):
    def __init__(sf, hz, hz_ref_to_hz_ls:dict):
        sf.hz = hz
        sf.hz_ref_to_hz_ls = hz_ref_to_hz_ls
    def handle_hz(sf, hz, *, ids):
        _add(sf.hz_ref_to_hz_ls, hz, sf.hz)
        return Recur
    def handle_ref(sf, ref, *, ids):
        _add(sf.hz_ref_to_hz_ls, ref, sf.hz)
        return Recur
class HandleParsedIDS__all_hz_ref_overlap(HandleParsedIDS):
    def __init__(sf, hz, hz_ref_overlap_to_hz_ls:dict):
        sf.hz = hz
        sf.hz_ref_overlap_to_hz_ls = hz_ref_overlap_to_hz_ls
    def handle_hz(sf, hz, *, ids):
        _add(sf.hz_ref_overlap_to_hz_ls, hz, sf.hz)
        return Recur
    def handle_ref(sf, ref, *, ids):
        _add(sf.hz_ref_overlap_to_hz_ls, ref, sf.hz)
        return Recur
    def handle_op(sf, op, *args, ids):
        if op == '⿻':
            k = repr(ids)
            _add(sf.hz_ref_overlap_to_hz_ls, k, sf.hz)
            return Stop
        return Recur

class HandleParsedIDS__all_component(HandleParsedIDS):
    def __init__(sf, hz, component_to_hz_ls:dict):
        sf.hz = hz
        sf.component_to_hz_ls = component_to_hz_ls
    def handle_hz(sf, hz, *, ids):
        _add(sf.component_to_hz_ls, hz, sf.hz)
        return Recur
    def handle_ref(sf, ref, *, ids):
        _add(sf.component_to_hz_ls, ref, sf.hz)
        return Recur
    def handle_op(sf, op, *args, ids):
        k = repr(ids)
        _add(sf.component_to_hz_ls, k, sf.hz)
        return Recur
        if op == '⿻':
            return Stop


def _main__d(hz2key2ParsedIDSs, *, fout):
    #print(f'total_hz = {len(hz2key2ParsedIDSs)}', file=fout)
    total_hz = len(hz2key2ParsedIDSs)
    clss = [
            HandleParsedIDS__all_hz_ref
            ,HandleParsedIDS__all_hz_ref_overlap
            ,HandleParsedIDS__all_component
            ]
    cls_nm2info_n_cmpnt2hz_ls = {}
    for cls in clss:
        #print(cls.__name__, file=fout)
        cls_nm = cls.__name__
        cmpnt2hz_ls = {}
        def hz2HandleParsedIDS(hz):
            sf = cls(hz, cmpnt2hz_ls)
            return sf
        hnd = HandleParsedResult(hz2HandleParsedIDS)
        hnd.feed(hz2key2ParsedIDSs)
        n = len(cmpnt2hz_ls)
        n_ge2 = (sum(len(ls) >= 2 for ls in cmpnt2hz_ls.values()))
        #print(f'total_cmpnts = {len(cmpnt2hz_ls)}', file=fout)
        #print(f'total_cmpnts__ge2 = {n_ge2}', file=fout)
        #pprint(cmpnt2hz_ls, stream=fout)
        info = dict(total_cmpnts=n
                , total_cmpnts__ge2=n_ge2
                )
        cls_nm2info_n_cmpnt2hz_ls[cls_nm] = (info, cmpnt2hz_ls)
    output = (dict(total_hz=total_hz)
            ,cls_nm2info_n_cmpnt2hz_ls
            )
    pprint(output, stream=fout)
    #return output
def _main__t(txt, *, fout):
    d = ast.literal_eval(txt)
    ref2hz = d['ref2hz']
    unfound_refs = set()
    found_refs = set()
    def m2s(m):
        ref = m.group(0)
        may_hz = ref2hz.get(ref)
        if may_hz is None:
            unfound_refs.add(ref)
            s = ref
        else:
            found_refs.add(ref)
            hz = may_hz
            s = hz
        return s
    new_txt = re.sub(r'&[^;&]*;', m2s, txt)
    print_err(f'len(found_refs)={len(found_refs)}; len(unfound_refs)={len(unfound_refs)};')
    new_d = ast.literal_eval(new_txt)
    hz2key2forest = new_d['hz2key2forest']
    hz2key2ParsedIDSs = hz2key2forest
    _main__d(hz2key2ParsedIDSs, fout=fout)

def _main__p(path, *, fout, encoding):
    #path = '~/tmp/ids_basic.txt'
    #path = Path.home() / 'tmp/ids_basic.txt'
    path = Path(path)
    txt = path.read_text(encoding=encoding)
    _main__t(txt, fout=fout)
#_main__p(Path.home() / 'tmp/ids_all.txt', encoding='utf8', fout=None)

def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description="handle result dict generated by parse_CHISE_IDS.py"
        , epilog=""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        txt = fin.read()

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        _main__t(txt, fout=fout)
if __name__ == "__main__":
    main()






