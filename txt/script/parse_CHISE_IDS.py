
# https://glyphwiki.org/wiki/cdp-8bf5
# http://www.chise.org/ids/
# ;; -*- coding: utf-8-mcs-er -*-
# U+51FB	击	⿱&CDP-8BF1;凵
# '⿸&U-i003+76D1;𫩏'
# 'U+5175\t兵\t⿱斤&GT-K00264;\t?'
# 'U-0002F800\t丽\t⿰⿱一𠔼⿱一𠔼'
# 'U-0002F803\t&C6-2566;\t⿳一&AJ1-04220;一'
#
# ⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻
#


__all__ = '''
    parse_CHISE_IDS__payload
    iter_parse_CHISE_IDS__payload
    maybe_parse_CHISE_IDS__line
    parse_CHISE_IDS__files
    parse_CHISE_IDS__file
    iter_parse_CHISE_IDS__file

    ops
    op2num_args__str
    op2num_args

    PATTERNS
    line_rex
    split_payload_rex
    '''.split()


import re
from seed.tiny import print_err

_skipped_buggy_fnames = [
    'IDS-UCS-Compat.txt'
    ]
_bugs = {
    #'U+5DE4\t巤\t⿱巛囚&CDP-8D46;': 'U+5DE4\t巤\t⿳巛囚&CDP-8D46;'
    'U+5DE4\t巤\t⿱巛囚&CDP-8D46;': 'U+5DE4\t巤\t⿱𡿺&CDP-8D46;'
    ,'U+F901\t更\t⿰曰': 'U+F901\t更\t更'
    # 更 U+66F4 vs U+F901: F901 is kZVariant of 66F4
    #   http://www.unicode.org/cgi-bin/GetUnihanData.pl?codepoint=66f4
    #   https://www.compart.com/en/unicode/U+F901
    ,'U+F903\t賈\t⿰貝': 'U+F903\t賈\t賈'
    # ==>> finally, I simply skip "IDS-UCS-Compat.txt"
    #,'U+38A4\t㢤\t弋?': 'U+38A4\t㢤\t⿱十成\t?'
    #   U+8F7D	载	⿹𢦏车
    # http://www.chise.org/ids-find?components=%E3%A2%A4
    # http://www.chise.org/ids-find?components=㢤
    ,'U+38A4\t㢤\t弋?': 'U+38A4\t㢤\t⿹⿱十弋&CDP-8B6C;\t?'
    ,'U-000200A6\t𠂦\t⿻&CDP-8BF5;上十'
        : 'U-000200A6\t𠂦\t⿻&CDP-8BF5;⿱上十'
    # https://glyphwiki.org/wiki/cdp-8bf5 ==>> &CDP-8BF5;
    ,'U-000200B5\t𠂵\t⿻&CDP-8BF5;土&CDP-8BF1;'
        : 'U-000200B5\t𠂵\t⿻&CDP-8BF5;⿱土&CDP-8BF1;'
    ,'U-00020176\t𠅶\t⿰⿱𠅘丸': 'U-00020176\t𠅶\t⿰𠅘丸'
    }

class PATTERNS:
    hex_char = r'[0-9A-F]'
    name_char = r'[0-9A-Za-z+-]'
    #cjk_char = r'(?:(?![\x00-\xff])\w)' #bad
    cjk_char = r'(?:(?![\x00-\xff])\S)'
    op = r'[⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻]'
    ref = fr'(?:[&]{name_char}+[;])'
    key = fr'(?:[@]{name_char}+[=])'
    #payload_char = fr'(?:{op}|{ref}|\S)'
    payload_char = fr'(?:{op}|{ref}|{cjk_char})'
    payload = fr'(?:{payload_char}+)'
    may_keyed_payload = fr'(?:{key}?{payload})'
    may_keyed_payload__nm = fr'(?P<key>{key}?)(?P<payload>{payload})'
    payloads = fr'(?P<payloads>(?:\t{payload_char}+)+)'

    #line = fr'(?P<unicode>U[+-]{hex_char}+)\t(?P<char_repr>{ref}|\S)\t(?P<payload>{payload_char}+)(?P<problem>(?:\t[?])?)'
    #line = fr'(?P<unicode>(?:U[+]{hex_char}{{4,5}}|U[-]{hex_char}{{8}}))\t(?P<char_repr>{ref}|\S)\t(?P<payload>{payload_char}+)(?P<problem>(?:\t[?])?)'
    #line = fr'(?P<unicode>(?:U[+]{hex_char}{{4,5}}|U[-]{hex_char}{{8}}))\t(?P<char_repr>{ref}|\S)(?P<payloads>(?:\t{payload_char}+)+)(?P<problem>(?:\t[?])?)'
    line__nm = fr'(?P<unicode>(?:U[+]{hex_char}{{4,5}}|U[-]{hex_char}{{8}}))\t(?P<char_repr>{ref}|\S)(?P<payloads>(?:\t{may_keyed_payload})+)(?P<problem>(?:\t[?])?)'
    split_payload = fr'({payload_char})'

class Globals:
    line_rex = re.compile(PATTERNS.line__nm)
    may_keyed_payload_rex = re.compile(PATTERNS.may_keyed_payload__nm)
    split_payload_rex = re.compile(PATTERNS.split_payload)
    ops = set(PATTERNS.op[1:-1])
    assert len(ops) == 12
    op2num_args__str = r'⿰2⿱2⿲3⿳3⿴2⿵2⿶2⿷2⿸2⿹2⿺2⿻2'
    ####################        ^^^^^
    op2num_args = dict(zip(op2num_args__str[::2], map(int, op2num_args__str[1::2])))
    assert len(op2num_args) == len(ops)
    assert set(op2num_args) == ops
    bugs = _bugs
    skipped_buggy_fnames = _skipped_buggy_fnames
del _bugs
del _skipped_buggy_fnames

def parse_CHISE_IDS__payload(payload):
    # -> tree
    # tree = (op, [arg]) | ('hz', char) | ('ref', ref_entity)
    it = iter_parse_CHISE_IDS__payload(payload)
    ls = list(it)
    it = reversed(ls)
    right_stack = []
    #left_stack = []
    for case, data in it:
        if case == 'op':
            op = data
            num_args = Globals.op2num_args[op]
            if not 0 < num_args <= len(right_stack): raise Exception(f'bad format: too few args after {op} : {payload!r} ==>> {ls!r}')
            ####
            #for _ in range(num_args): left_stack.append(right_stack.pop())
            args = right_stack[-num_args:]
            del right_stack[-num_args:]
            ####
            tree = nonleaf = (op, args)
        else:
            tree = leaf = (case, data)
        right_stack.append(tree)
    if 1 != len(right_stack): raise Exception(f'bad format: non-single top-level op : {payload!r} ==>> {ls!r}')
    [tree] = right_stack
    return tree

def iter_parse_CHISE_IDS__payload(payload):
    # -> Iter (('op', op:char) | ('hz', char:char) | ('ref', ref:str))
    ls = Globals.split_payload_rex.split(payload)
    if not len(ls) >= 3: raise Exception(f'bad format: {payload!r} ==>> {ls!r}')
    if not all(ls[1::2]): raise Exception(f'bad format: {payload!r} ==>> {ls!r}')
    if any(ls[::2]): raise Exception(f'bad format: {payload!r} ==>> {ls!r}')

    ls = ls[1::2]
    for x in ls:
        if len(x) > 1:
            assert x[0] == '&'
            assert x[-1] == ';'
            ref = x
            yield ('ref', ref)
        else:
            assert x
            #if x == '⿱': print(x, repr(x), ops, x in ops)
            if x in Globals.ops:
                op = x
                yield ('op', op)
            else:
                char = x
                yield ('hz', char)

def maybe_parse_CHISE_IDS__line(line):
    # -> None|(char, may_char_ref, {key:[tree]})
    # tree = (op, [arg]) | ('hz', char:char) | ('ref', ref_entity:str)
    # may_char_ref:None|str
    line = line.strip()
    if not line or line.startswith(';'):
        return None
    line = Globals.bugs.get(line, line)

    m = Globals.line_rex.fullmatch(line)

    if not m:
        raise Exception(f'unknown format: {line!r}')
    unicode = m['unicode']
    assert unicode[0] == 'U'
    assert unicode[1] in '+-'
    order = int(unicode[2:], base=16)
    char_repr = m['char_repr']
    #payload = m['payload']
    [_, *payloads] = m['payloads'].split('\t')
    problem = m['problem']

    #if order==0x216A7: print_err(f'0x216A7: {line!r}')
    char = chr(order)
    assert order == ord(char)
    if len(char_repr) == 1:
        may_char_ref = None
        if char != char_repr: raise Exception(f'bad format: unicode not match hz-char: {line!r}')
    else:
        char_ref = char_repr
        may_char_ref = char_ref

    try:
        #tree = parse_CHISE_IDS__payload(payload)
        #forest = []
        key2forest = {}
        for may_keyed_payload in payloads:
            _m = Globals.may_keyed_payload_rex.fullmatch(may_keyed_payload)
            key = _m['key']
            payload = _m['payload']
            tree = parse_CHISE_IDS__payload(payload)
            #forest.append(tree)
            _add(key2forest, key, tree)
    except Exception as e:
      if _Globals.howto_handle_err is _Globals.Skip:
        print_err(f'{line!r}: {e!r}')
        return None
      raise Exception(e, line)
    if problem: print_err(f'problem?: {line!r}')
    assert len(char) == 1
    #return (char, may_char_ref, tree)
    #return (char, may_char_ref, forest)
    return (char, may_char_ref, key2forest)


def post_handle_result(result):
    hz2key2forest = {}
    ref2hz = {}
    for k,v in result.items():
        if len(k) == 1:
            assert type(v) is dict
            hz = k
            key2forest = v
            hz2key2forest[hz] = key2forest
        else:
            assert type(v) is tuple
            assert len(v) == 2
            assert v[0] == 'hz'
            char_ref = k
            _, hz = v
            ref2hz[char_ref] = hz
    return hz2key2forest, ref2hz
def parse_CHISE_IDS__files(ifiles, *, output:'mapping'=None):
    # -> {char:{key:[tree]} | char_ref:('hz", char)}
    if output is None: output = {}
    for ifile in ifiles:
        parse_CHISE_IDS__file(ifile, output=output)
    return output
def parse_CHISE_IDS__file(ifile, *, output:'mapping'=None):
    if output is None: output = {}
    d = output
    it = iter_parse_CHISE_IDS__file(ifile)
    i = len(output)
    #for (char, may_char_ref, tree) in it:
    #    d[char] = tree
    #for (char, may_char_ref, forest) in it:
    #    d[char] = forest
    for (char, may_char_ref, key2forest) in it:
        #assert char not in d
        d[char] = key2forest
        i += 1
        if len(d) != i: raise Exception(f'bad format: duplicated: U+{ord(char):0>8X} {char!r}')
        if may_char_ref is not None:
            char_ref = may_char_ref
            d[char_ref] = ('hz', char)
            i += 1
            if len(d) != i: raise Exception(f'bad format: duplicated: {char_ref!r}->{char!r}')
    return d
def iter_parse_CHISE_IDS__file(ifile):
    for line in ifile:
        try:
            may_result = maybe_parse_CHISE_IDS__line(line)
        except Exception as e:
          if _Globals.howto_handle_err is _Globals.Skip:
            print_err(f'{line!r}: {e!r}')
            may_result = None
          else:
            raise
        if may_result is None:
            continue
        result = may_result
        #(char, may_char_ref, tree) = result
        #yield char, may_char_ref, tree
        #(char, may_char_ref, forest) = result
        #yield char, may_char_ref, forest
        (char, may_char_ref, key2forest) = result
        yield char, may_char_ref, key2forest


'''
if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals())
'''

def _add(d, k, v):
    vs = d.setdefault(k, [])
    vs.append(v)

class _Globals:
    class Skip:pass
    class Raise:pass
    howto_handle_err = Skip

def main(args=None):
    import argparse
    import glob
    import os.path
    #from pathlib import Path
    from pprint import pprint
    from seed.io.may_open import may_open_stdout

    parser = argparse.ArgumentParser(
        description='parse CHISE-IDS into a python-dict'
        , epilog=f'''
* CHISE-IDS from: http://www.chise.org/ids/
ref entity:
    &CDP-8BF5; ==>> https://glyphwiki.org/wiki/cdp-8bf5
skip: {Globals.skipped_buggy_fnames!r}
bugs: {Globals.bugs!r}
'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('inputs', type=str, default=[], nargs='*'
                        , help='glob patterns of input file paths')
    parser.add_argument('-r', '--recursive', action='store_true'
                        , default = False
                        , help='enable "**" in glob patterns')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-se', '--skip_err', action='store_true'
                        , default = False
                        , help='skip error instead of raise')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'
    _Globals.howto_handle_err = _Globals.Skip if args.skip_err else _Globals.Raise

    glob_patterns = args.inputs
    recursive = args.recursive
    #glob = Path('.').glob # no iglob
    skipped_buggy_fname_set = set(map(str.lower, Globals.skipped_buggy_fnames))
    def iter_ifiles():
        for glob_pattern in glob_patterns:
            for path in glob.iglob(glob_pattern, recursive=recursive):
                print_err(f'glob_pattern: {glob_pattern!r} ==>> path:{path!r}')
                fname = os.path.basename(path)
                if fname.lower() in skipped_buggy_fname_set:
                    print_err(f'\tskip:{fname!r}')
                    continue
                else:
                    with open(path, 'rt', encoding=encoding) as ifile:
                        yield ifile

    d = parse_CHISE_IDS__files(iter_ifiles())
    hz2key2forest, ref2hz = post_handle_result(d)
    r = dict(hz2key2forest=hz2key2forest
            ,ref2hz=ref2hz
            )

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        #print(d, file=fout)
        pprint(r, stream=fout)

if __name__ == "__main__":
    main()



