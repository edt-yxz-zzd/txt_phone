from common_short_hand import *


from html import escape
def main(argv=None):
    import argparse
    import os.path
    from seed.io.may_open import may_open_stdin, may_open_stdout


    parser = argparse.ArgumentParser(
        description='simple encape text to html'
        , epilog=r'''only "<>&" and "\"\'" if quote=True will be escaped.'''
        #, formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-e', '--encoding', type=str, default='utf8', help='input/output file encoding')
    parser.add_argument('-t', '--title', type=str, default = None
                        , required=True
                        , help='title of html')
    parser.add_argument('-i', '--input', type=str, default = None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default = None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('-q', '--quote', action='store_true'
                        , default = False
                        , help=r'''escape "\"\'" too; otherwise only "<>&" be escaped''')



    args = parser.parse_args(argv)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        input_text = ''.join(fin)

    escaped_text = escape(input_text, args.quote)
    output_text = (
f'''{args.title!s}

<pre>
{escaped_text!s}
</pre>
''')

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        fout.write(output_text)

    parser.exit(0)
    return 0



if __name__ == "__main__":
    main()

