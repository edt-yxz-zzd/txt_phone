
#from common_short_hand import *

def main(args=None):
    import argparse
    from pathlib import Path
    #from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description=""
        , epilog=""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-id', '--input_dir', type=str, default=None
                        , required=True
                        , help='input dir path')
    parser.add_argument('-od', '--output_dir', type=str, default=None
                        , required=True
                        , help='output dir path')
    parser.add_argument('-ie', '--input_encoding', type=str
                        , default='gb18030'
                        , required=True
                        , help='input file encoding')
    parser.add_argument('-oe', '--output_encoding', type=str
                        , default='utf8'
                        , required=True
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    iencoding = args.input_encoding
    oencoding = args.output_encoding
    omode = 'wt' if args.force else 'xt'

    ifolder = Path(args.input_dir)
    ofolder = Path(args.output_dir)
    print(f"iencoding={iencoding!r}")
    print(f"oencoding={oencoding!r}")
    print(f"ifolder={ifolder!r}")
    print(f"ofolder={ofolder!r}")
    print("="*60)
    for p in ifolder.iterdir():
      if p.is_file():
        ifname = p
        print(f"ifname={ifname!r}")
        txt = ifname.read_text(encoding=iencoding)
        ofname = ofolder.joinpath(ifname.name)
        print(f"==>>ofname={ofname!r}")
        with ofname.open(omode, encoding=oencoding) as fout:
          fout.write(txt)


if __name__ == "__main__":
    main()
