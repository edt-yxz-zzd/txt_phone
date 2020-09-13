
r"""
script/ids_basic_component2strokes.py



/storage/emulated/0/0my_files/tmp/after_ids_pp_2.txt
   'HandleParsedIDS__all_hz_ref':
      ({'total_cmpnts': 5077, 'total_cmpnts__ge2': 2791}
      ,{'&A-CDP-8D60;': ['薨', '蘉'], ...}
      )

    #结合 ucs-strokes.txt, ids_all_2.json.txt, 对5077个部件按笔画数排序并给出笔画顺序(校验或计算笔画数，辅助搜索部件)

#"""

import ast
from seed.tiny import snd, print_err

class Globals:
    ucs_strokes_txt__path = r"/sdcard/0my_files/unzip/e_book/汉字分解/cjkvi-ids[202008]/cjkvi-ids-master/ucs-strokes.txt"
    after_ids_pp_2_txt__path = r"/storage/emulated/0/0my_files/tmp/after_ids_pp_2.txt"
    ids_all_2_json_txt__path = r"/storage/emulated/0/0my_files/tmp/ids_all_2.json.txt"


def read_after_ids_txt__path(after_ids_txt__path):
    with open(after_ids_txt__path, "rt", encoding="utf8") as fin:
        return read_after_ids_txt__file(fin)
def read_after_ids_txt__file(after_ids_txt__file):
    return read_after_ids_txt__str(after_ids_txt__file.read())
def read_after_ids_txt__str(after_ids_txt__str):
    main_info, d = ast.literal_eval(after_ids_txt__str)
    info, ddd = d["HandleParsedIDS__all_hz_ref"]
    nonprimes = set()
    for hz_or_ref, hz_or_ref_ls in ddd.items():
        s = set(hz_or_ref_ls)
        s.discard(hz_or_ref)
        nonprimes |= s
    ddd = {k:v for k,v in ddd.items() if k not in nonprimes}
    #print_err(len(ddd)) #==1743
    return ddd
def parse_ucs_strokes_txt__path(ucs_strokes_txt__path):
    with open(ucs_strokes_txt__path, "rt", encoding="utf8") as fin:
        return dict(iter_parse_ucs_strokes_txt__file(fin))
def iter_parse_ucs_strokes_txt__file(ucs_strokes_txt__file):
    for line in ucs_strokes_txt__file:
        _, hz_or_ref_or_spec_char, num_strokes_ls_str = line.split("\t")
        num_strokes_ls = tuple(map(int, num_strokes_ls_str.split(",")))
        assert num_strokes_ls
        yield hz_or_ref_or_spec_char, num_strokes_ls


def mk_prime_hz_or_ref_to_num_strokes_ls_ex(prime_hz_or_ref_to_hz_or_ref_ls, hz_or_ref_or_spec_char_to_num_strokes_ls):
    def f(ls):
        ls = sorted(ls, key=lambda s: (len(s), s))
        chars = ";".join(ls)
        assert len(chars.split()) == 1
        #no spaces
        return chars
    prime_hz_or_ref_to_num_strokes_ls_ex = {prime_hz_or_ref: (hz_or_ref_or_spec_char_to_num_strokes_ls.get(prime_hz_or_ref, ()), f(hz_or_ref_ls)) for prime_hz_or_ref, hz_or_ref_ls in prime_hz_or_ref_to_hz_or_ref_ls.items()}
    return prime_hz_or_ref_to_num_strokes_ls_ex

def combine_two_files(after_ids_txt__path, ucs_strokes_txt__path):
    prime_hz_or_ref_to_hz_or_ref_ls = read_after_ids_txt__path(after_ids_txt__path)
    hz_or_ref_or_spec_char_to_num_strokes_ls = parse_ucs_strokes_txt__path(ucs_strokes_txt__path)
    prime_hz_or_ref_to_num_strokes_ls_ex = mk_prime_hz_or_ref_to_num_strokes_ls_ex(prime_hz_or_ref_to_hz_or_ref_ls, hz_or_ref_or_spec_char_to_num_strokes_ls)
    prime_hz_or_ref_AND_num_strokes_ls_PAIRs_ex = sorted(prime_hz_or_ref_to_num_strokes_ls_ex.items(), key=lambda x_yz:x_yz[1][0])
    return prime_hz_or_ref_AND_num_strokes_ls_PAIRs_ex
def show_prime_hz_or_ref_AND_num_strokes_ls_PAIRs_ex(prime_hz_or_ref_AND_num_strokes_ls_PAIRs_ex, *, fout):
    for prime_hz_or_ref, (num_strokes_ls, chars) in prime_hz_or_ref_AND_num_strokes_ls_PAIRs_ex:
        print(fr"{prime_hz_or_ref!s}:{num_strokes_ls!r}#{chars!s}", file=fout)

def _f(*, fout=None):
    prime_hz_or_ref_AND_num_strokes_ls_PAIRs_ex = combine_two_files(Globals.after_ids_pp_2_txt__path, Globals.ucs_strokes_txt__path)
    show_prime_hz_or_ref_AND_num_strokes_ls_PAIRs_ex(prime_hz_or_ref_AND_num_strokes_ls_PAIRs_ex, fout=fout)




if __name__ == "__main__":
    _f()


