

r"""
py script/py_repr2json.py -i ~/tmp/ids_all_2.txt -o ~/tmp/ids_all_2.json.txt
#"""

from seed.helper.safe_eval import safe_eval
import json

def py_repr2json(txt, *, fout=None, locals=None, **json_dumps_kwargs):
    obj = safe_eval(txt, locals=locals)
    return py_obj2json(obj, fout=fout, **json_dumps_kwargs)

def py_obj2json(obj, fout=None, **json_dumps_kwargs):
    if fout is None:
        return json.dumps(obj, **json_dumps_kwargs)
    return json.dump(obj, fout, **json_dumps_kwargs)




def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description="py obj repr txt file to json file"
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
        py_repr2json(txt, fout=fout, sort_keys=True, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()


