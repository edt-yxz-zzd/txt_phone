r'''[[[
e script/max_term_of_init_terms_of_continued_fraction_of_pi.py





[[
view /sdcard/0my_files/unzip/e_book/连分数/continued_fraction_pi/Continued fraction expansion of Pi.txt
view /sdcard/0my_files/unzip/e_book/连分数/continued_fraction_pi/continued_fraction_pi_100term_per_line_omit_zeroth_term.txt
    不包含首项『3』


3;[7,15,1,292,1,1,1,2,1,3,1,14,2,1,1,2,2,2,2,1,84,
 2,1,1,15,3,13,1,4,2,6,6,99,1,2,2,6,3,5,1,1,6,8,1,
 7,1,2,3,7,1,2,1,1,12,1,1,1,3,1,1,8,1,1,2,1,6,1,1,
 5,2,2,3,1,2,4,4,16,1,161,45,1,22,1,2,2,1,4,1,2,24,
 1,2,1,3,1,2,1]
(0, 7)
(1, 15)
(3, 292)
(306, 436)
(430, 20776)
(28420, 78629)
(156380, 179136)
(267312, 528210)
(453292, 12996958)
(11504929, 878783625)
...
Line 4533: 6, 1, 1, 9, 1, 8, 3, 1, 4, 1, 1, 1, 2, 4, 22, 1, 3, 40, 1, 1, 1, 2, 1, 3, 2, 38, 1, 2, 1, 1, 2, 2, 2, 1, 1, 20, 2, 15, 2, 5, 4, 1, 1, 10, 1, 10, 12, 1, 1, 1, 1, 2, 1, 2, 14, 2, 1, 2, 1, 1, 5, 2, 1, 2, 1, 2, 1, 2, 4, 1, 2, 1, 4, 1, 3, 1, 4, 1, 3, 4, 5, 1, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 12996958, 14, 1, 2, 2, 1, 4, 1, 


#ValueError: invalid literal for int() with base 10: b' 1; \r4'
#Line100_0000: 1, 62, 1, 32, 1, 5, 1, 1, 95, 1, 2, 3, 1, 5, 1, 76, 1, 1, 2, 2, 8, 1, 6, 9, 2, 6, 1, 1, 3, 1, 1, 4, 2, 1, 73, 5, 1, 1, 4, 1, 5, 1, 10, 1, 1, 1, 2, 2, 2, 3, 1, 1, 1, 7, 1, 2, 3, 5, 3, 9, 9, 44, 1, 9, 1, 376, 1, 5, 1, 3, 6, 6, 1, 2, 4, 2, 35, 2, 1, 2, 2, 1, 4, 1, 20, 2, 1, 4, 1, 1, 1, 1, 7, 26, 1, 3, 1, 1, 3, 1; 
    有『;』替代『,』
#Line180_0000: 352, 2, 6, 69, 1, 1, 3, 2, 1, 1, 1, 2, 6, 1, 11, 3, 2, 1, 2, 1, 1, 1, 5, 6, 1, 1, 1, 1, 1, 3, 2, 5, 2, 2, 11, 2, 5, 1, 23, 5, 1, 1, 1, 5, 1, 38, 1, 2, 2, 1, 1, 3, 1, 4, 1, 1, 2, 1, 2, 2, 1, 23, 1, 1, 3, 1, 3, 1, 1, 1, 1, 2, 3, 12, 1, 11, 2, 2, 9, 1, 57, 5, 4, 1, 1, 1, 3, 2, 1, 1, 5, 1, 224, 5, 1, 1, 2, 3, 1, 2, 
    最后一行:后面还有『,』
]]
[[
py script/max_term_of_init_terms_of_continued_fraction_of_pi.py show_min_idx_max_term_pairs5ipath :'/sdcard/0my_files/unzip/e_book/连分数/continued_fraction_pi/continued_fraction_pi_100term_per_line_omit_zeroth_term.txt' =5
(0, 7)
(1, 15)
(3, 292)
(306, 436)
(430, 20776)
[(0, 7), (1, 15), (3, 292), (306, 436), (430, 20776)]
last= (430, 20776)



py script/max_term_of_init_terms_of_continued_fraction_of_pi.py show_min_idx_max_term_pairs5ipath :'/sdcard/0my_files/unzip/e_book/连分数/continued_fraction_pi/continued_fraction_pi_100term_per_line_omit_zeroth_term.txt' > ~/my_tmp/out4py/script.max_term_of_init_terms_of_continued_fraction_of_pi.py.out.txt
view /sdcard/0my_files/tmp/out4py/script.max_term_of_init_terms_of_continued_fraction_of_pi.py.out.txt
(0, 7)
(1, 15)
(3, 292)
(306, 436)
(430, 20776)
(28420, 78629)
(156380, 179136)
(267312, 528210)
(453292, 12996958)
(11504929, 878783625)
[(0, 7), (1, 15), (3, 292), (306, 436), (430, 20776), (28420, 78629), (156380, 179136), (267312, 528210), (453292, 12996958), (11504929, 878783625)]
last= (179999999, 2)
曾经:
    last= (11504929, 878783625)
    逻辑有毛病:应当显示:『last= (179999999, 2)』其中(1_7999_9999==180_0000*100-1, 2)，见上面『Line180_0000』
    已更正！
]]


help(str.isspace)
help(bytes.isspace)
isspace(...)
    B.isspace() -> bool

    Return True if all characters in B are whitespace and there is at least one character in B, False otherwise.

help(bytes.split)
split(self, /, sep=None, maxsplit=-1)
    Return a list of the sections in the bytes, using sep as the delimiter.

    sep
        The delimiter according which to split the bytes.
        None (the default value) means split on ASCII whitespace characters (space, tab, return, newline, formfeed, vertical tab).
    maxsplit
        Maximum number of splits to do.
        -1 (the default value) means no limit.

help(bytes.replace)
replace(self, old, new, count=-1, /)
    Return a copy with all occurrences of substring old replaced by new.

      count
        Maximum number of occurrences to replace.
        -1 (the default value) means replace all occurrences.

    If the optional argument count is given, only the first count occurrences are replaced.


#]]]'''
__all__ = '''
    show_min_idx_max_term_pairs5ipath
    iter_min_idx_max_term_pairs5ipath
    iter_min_idx_max_term_pairs5ibfile
    iter_ints5ibfile

    '''.split()
from itertools import islice

class Globals:
    ifpath = '/sdcard/0my_files/unzip/e_book/连分数/continued_fraction_pi/continued_fraction_pi_100term_per_line_omit_zeroth_term.txt'

    first_5000_terms_of_continued_fraction_of_pi_omit_zeroth_term = [
7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1, 4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1, 1, 10, 2, 
5, 4, 1, 2, 2, 8, 1, 5, 2, 2, 26, 1, 4, 1, 1, 8, 2, 42, 2, 1, 7, 3, 3, 1, 1, 7, 2, 4, 9, 7, 2, 3, 1, 57, 1, 18, 1, 9, 19, 1, 2, 18, 1, 3, 7, 30, 1, 1, 1, 3, 3, 3, 1, 2, 8, 1, 1, 2, 1, 15, 1, 2, 13, 1, 2, 1, 4, 1, 12, 1, 1, 3, 3, 28, 1, 10, 3, 2, 20, 1, 1, 1, 1, 4, 1, 1, 1, 5, 3, 2, 1, 6, 1, 4, 1, 120, 2, 1, 1, 3, 
1, 23, 1, 15, 1, 3, 7, 1, 16, 1, 2, 1, 21, 2, 1, 1, 2, 9, 1, 6, 4, 127, 14, 5, 1, 3, 13, 7, 9, 1, 1, 1, 1, 1, 5, 4, 1, 1, 3, 1, 1, 29, 3, 1, 1, 2, 2, 1, 3, 1, 1, 1, 3, 1, 1, 10, 3, 1, 3, 1, 2, 1, 12, 1, 4, 1, 1, 1, 1, 7, 1, 1, 2, 1, 11, 3, 1, 7, 1, 4, 1, 48, 16, 1, 4, 5, 2, 1, 1, 4, 3, 1, 2, 3, 1, 2, 2, 1, 2, 5, 
20, 1, 1, 5, 4, 1, 436, 8, 1, 2, 2, 1, 1, 1, 1, 1, 5, 1, 2, 1, 3, 6, 11, 4, 3, 1, 1, 1, 2, 5, 4, 6, 9, 1, 5, 1, 5, 15, 1, 11, 24, 4, 4, 5, 2, 1, 4, 1, 6, 1, 1, 1, 4, 3, 2, 2, 1, 1, 2, 1, 58, 5, 1, 2, 1, 2, 1, 1, 2, 2, 7, 1, 15, 1, 4, 8, 1, 1, 4, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 9, 1, 4, 3, 15, 1, 2, 
1, 13, 1, 1, 1, 3, 24, 1, 2, 4, 10, 5, 12, 3, 3, 21, 1, 2, 1, 34, 1, 1, 1, 4, 15, 1, 4, 44, 1, 4, 20776, 1, 1, 1, 1, 1, 1, 1, 23, 1, 7, 2, 1, 94, 55, 1, 1, 2, 1, 1, 3, 1, 1, 32, 5, 1, 14, 1, 1, 1, 1, 1, 3, 50, 2, 16, 5, 1, 2, 1, 4, 6, 3, 1, 3, 3, 1, 2, 2, 2, 5, 2, 2, 2, 28, 1, 1, 13, 1, 5, 43, 1, 4, 3, 5, 3, 1, 4, 1, 1, 
2, 2, 1, 1, 19, 2, 7, 1, 72, 3, 1, 2, 3, 7, 11, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 33, 7, 19, 1, 19, 3, 1, 4, 1, 1, 1, 1, 2, 3, 1, 3, 2, 2, 2, 2, 4, 1, 1, 1, 4, 2, 3, 1, 1, 1, 1, 11, 1, 1, 2, 1, 2, 1, 2, 2, 1, 7, 2, 27, 1, 1, 6, 2, 1, 9, 6, 26, 1, 1, 3, 2, 1, 1, 1, 1, 1, 15, 1, 36, 4, 2, 2, 1, 22, 2, 1, 
106, 2, 2, 1, 3, 1, 12, 10, 7, 1, 2, 1, 1, 1, 1, 8, 2, 4, 5, 3, 2, 1, 4, 23, 1, 18, 2, 10, 3, 1, 6, 6, 13, 8, 6, 2, 2, 2, 2, 1, 1, 1, 3, 1, 7, 17, 1, 1, 1, 2, 5, 5, 1, 1, 2, 11, 1, 6, 1, 6, 1, 29, 4, 29, 3, 5, 3, 1, 141, 1, 2, 7, 7, 2, 2, 7, 1, 1, 7, 1, 7, 1, 2, 4, 1, 1, 1, 30, 1, 12, 4, 18, 10, 2, 8, 1, 2, 2, 2, 4, 
13, 1, 5, 4, 1, 6, 1, 1, 11, 2, 4, 2, 1, 1, 3, 3, 12, 1, 1, 39, 5, 1, 1, 16, 125, 1, 4, 1, 2, 1, 19, 1, 4, 1, 1, 2, 1, 4, 1, 10, 1, 4, 2, 1, 1, 1, 5, 10, 4, 14, 1, 13, 41, 1, 4, 1, 8, 1, 1, 2, 1, 3, 1, 6, 1, 3, 2, 2, 2, 1, 4, 1, 14, 1, 2, 8, 1, 8, 3, 3, 3, 1, 37, 4, 2, 4, 1, 3, 4, 25, 4, 27, 2, 7, 1, 1, 2, 6, 1, 1, 
1, 12, 1, 2, 2, 2, 13, 12, 1, 3, 1, 6, 1, 1, 33, 1, 5, 3, 1, 5, 15, 8, 8, 47, 1, 3, 2, 12, 2, 12, 1, 12, 1, 2, 5, 3, 1, 1, 1, 1, 2, 3, 5, 4, 2, 1, 1, 5, 1, 9, 14, 1, 1, 3, 2, 1, 9, 3, 22, 13, 1, 1, 3, 20, 1, 1, 61, 1, 376, 2, 107, 1, 10, 3, 2, 2, 31, 1, 2, 10, 2, 2, 62, 2, 2, 7, 4, 5, 6, 1, 1, 1, 1, 2, 8, 2, 73, 3, 5, 42, 
1, 3, 2, 1, 1, 59, 6, 1, 1, 1, 5, 1, 6, 1, 2, 6, 1, 1, 1, 1, 3, 2, 1, 3, 1, 8, 1, 4, 2, 5, 4, 7, 1, 4, 2, 2, 6, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 5, 1, 2, 1, 1, 10, 1, 6, 1, 129, 1, 4, 65, 2, 4, 4, 3, 2, 3, 1, 1, 5, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 3, 1, 2, 1, 2, 4, 2, 1, 2, 27, 6, 2, 1, 
193, 1, 3, 9, 1, 3, 35, 2, 1, 8, 1, 1, 1, 1, 9, 3, 56, 1, 6, 6, 2, 8, 1, 8, 1, 2, 3, 6, 3, 1, 3, 1, 1, 1, 2, 13, 1, 1, 1, 1, 13, 2, 1, 3, 1, 3, 15, 2, 1, 1, 2, 4, 1, 4, 5, 2, 2, 1, 2, 1, 6, 1, 4, 12, 1, 1, 1, 1, 13, 1, 3, 4, 1, 1, 1, 2, 9, 1, 7, 1, 1, 1, 1, 4, 1, 3, 4, 1, 1, 4, 3, 1, 39, 2, 1, 1, 1, 1, 1, 4, 
7, 2, 2, 2, 1, 1, 1, 1, 2, 114, 12, 4, 1, 3, 2, 1, 19, 1, 1, 2, 1, 1, 3, 4, 1, 60, 3, 72, 2, 1, 1, 1, 50, 1, 1, 1, 1, 3, 1, 1, 2, 2, 1, 4, 1, 7, 3, 1, 2, 1, 5, 1, 1, 1, 2, 6, 2, 21, 2, 6, 1, 6, 1, 1, 2, 1, 7, 1, 8, 1, 1, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 11, 2, 4, 10, 2, 1, 1, 13, 1, 1, 7, 15, 1, 1, 1, 2, 3, 
15, 8, 8, 2, 1, 13, 3, 5, 1, 2, 1, 6, 1, 10, 123, 3, 1, 4, 59, 4, 156, 88, 1, 5, 4, 1, 3, 1, 4, 2, 9, 1, 7, 4, 2, 1, 2, 3, 2, 1, 2, 11, 1, 13, 7, 7, 1, 63, 37, 12, 86, 1, 1, 1, 1, 2, 2, 4, 2, 18, 1, 1, 1, 41, 2, 1, 1, 12, 1, 2, 1, 1, 2, 10, 1, 1, 1, 5, 1, 1, 3, 1, 7, 5, 1, 9, 1, 2, 2, 7, 1, 1, 5, 2, 1, 3, 3, 5, 2, 1, 
11, 3, 1, 3, 2, 1, 1, 2, 1, 14, 5, 2, 2, 1, 1, 1, 1, 3, 1, 3, 3, 2, 2, 1, 3, 2, 1, 2, 1, 4, 1, 14, 1, 1, 58, 7, 1, 2, 1, 1, 5, 1, 2, 1, 5, 18, 1, 4, 3, 1, 1, 1, 4, 1, 1, 2, 5, 1, 148, 1, 9, 2, 1, 2, 1, 5, 4, 93, 1, 1, 2, 4, 1, 2, 73, 1, 1, 3, 1, 1, 1, 1, 2, 1, 34, 1, 5, 6, 1, 2, 1, 3, 4, 1, 16, 28, 17, 2, 5, 5, 
26, 1, 1, 4, 12, 1, 3, 2, 1, 5, 1, 2, 9, 3, 2, 41, 1, 16, 2, 2, 20, 1, 17, 1, 6, 16, 3, 3, 2, 2, 2, 18, 15, 1, 1, 51, 4, 9, 5, 2, 2, 1, 2, 1, 45, 3, 1, 1, 3, 1, 2, 1, 3, 1, 1, 3, 5, 1, 2, 3, 8, 2, 47, 2, 3, 1, 1, 1, 15, 9, 1, 8, 2, 1, 4, 2, 4, 14, 1, 12, 2, 1, 161, 1, 26, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 18, 528, 12, 4, 1, 
5, 16, 3, 1, 1, 1, 1, 1, 5, 1, 2, 1, 63, 1, 97, 1, 4, 4, 10, 5, 9, 5, 2, 3, 2, 5, 7, 1, 32, 13, 1, 5, 4, 1, 7, 1, 3, 12, 1, 3, 9, 1, 7, 1, 102, 53, 1, 1, 1, 3, 4, 2, 15, 2, 8, 2, 2, 3, 1, 2, 4, 1, 1, 3, 2, 3, 1, 1, 2, 3, 1, 1, 6, 1, 1, 14, 1, 80, 11, 1, 1, 1, 1, 22, 1, 2, 3, 1, 3, 26, 2, 24, 2, 2, 4, 3, 1, 1, 1, 1, 
3, 1, 63, 1, 1, 1, 25, 1, 1, 1, 8, 1, 3, 3, 1, 10, 5, 6, 2, 1, 1, 3, 1, 1, 1, 1, 2, 2, 1, 2, 8, 12, 1, 53, 1, 2, 1, 1, 5, 1, 1, 3, 1, 39, 1, 12, 1, 3, 14, 18, 9, 3, 2, 2, 2, 1, 1, 3, 1, 4, 4, 7, 1, 17, 1, 14, 1, 1, 1, 1, 3, 1, 1, 10, 1, 2, 2, 3, 1, 2, 1, 2, 2, 2, 12, 1, 3, 44, 2, 10, 1, 14, 1, 2, 1, 43, 4, 1, 7, 3, 
4, 1, 1, 2, 2, 1, 34, 1, 2, 5, 8, 3, 2, 1, 2, 13, 4, 3, 2, 1, 1, 1, 1, 25, 1, 5, 1, 94, 2, 4, 3, 4, 5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 41, 1, 5, 1, 4, 4, 1, 155, 1, 8, 1, 1, 1, 1, 4, 1, 1, 2, 9, 2, 1, 2, 1, 1, 1, 6, 23, 1, 2, 3, 5, 2, 1, 1, 1, 1, 7, 67, 5, 7, 1, 23, 3, 3, 1, 6, 1, 11, 1, 57, 
1, 4, 1, 5, 1, 1, 8, 1, 1, 2, 5, 2, 10, 1, 1, 2, 1, 1, 3, 1, 2, 1, 3, 1, 11, 2, 10, 1, 4, 18, 1, 2, 3, 1, 1, 6, 3, 6, 4, 31, 3, 4, 1, 18, 3, 9, 7, 5, 1, 2, 2, 1, 7, 1, 23, 2, 217, 1, 2, 1, 4, 1, 54, 2, 196, 10, 3, 1, 32, 1, 40, 55, 1, 5, 1, 3, 3, 1, 2, 2, 1, 3, 6, 3, 16, 1, 31, 1, 5, 6, 1, 4, 42, 4, 1, 10, 1, 3, 1, 3, 
3, 1, 2, 1, 1, 1, 4, 1, 13, 1, 88, 1, 1, 1, 14, 3, 27, 3, 1, 1, 16, 4, 1, 2, 4, 1, 4, 1, 1, 17, 2, 4, 1, 1, 9, 2, 1, 1, 3, 1, 1, 30, 1, 1, 3, 2, 2, 1, 1, 4, 10, 1, 7, 1, 6, 1, 35, 1, 1, 2, 3, 6, 1, 1, 2, 4, 4, 24, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1, 2, 1, 6, 6, 2, 1, 1, 10, 6, 4, 2, 1, 3, 9, 1, 2, 16, 1, 5, 1, 1, 
1, 1, 6, 5, 1, 13, 5, 4, 1, 2, 3, 1, 1, 1, 3, 1, 30, 2, 5, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 6, 5, 3, 65, 48, 3, 3, 6, 1, 9, 2, 1, 5, 6, 2, 1, 1, 1, 1, 620, 8, 1, 1, 4, 8, 1, 6, 1, 5, 8, 1, 5, 1, 4, 9, 47, 3, 1, 6, 1, 25, 1, 3, 425, 2, 3, 3, 17, 1, 2, 3, 2, 3, 1, 1, 1, 5, 2, 1, 41, 1, 1, 1, 1, 3, 1, 5, 
1, 1, 6, 256, 17, 1, 14, 1, 2, 3, 1, 2, 2, 2, 4, 9, 7, 3, 3, 18, 1, 33, 1, 5, 2, 4, 25, 1, 2, 1, 6, 1, 3, 4, 16, 4, 2, 2, 7, 3, 1, 14, 2, 1, 2, 1, 3, 3, 1, 4, 1, 59, 1, 121, 9, 1, 2, 1, 11, 1, 20, 1, 9, 2, 1, 3, 391, 1, 2, 8, 3, 4, 1, 1, 3, 13, 1, 95, 2, 2, 4, 21, 1, 21, 2, 8, 13, 3, 1, 1, 1, 5, 1, 8, 1, 15, 1, 252, 3, 4, 
2, 15, 1, 1, 1, 5, 2, 6, 11, 1, 10, 41, 1, 4, 2, 2, 1, 1, 1, 5, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 24, 8, 21, 3, 3, 9, 14, 9, 1, 9, 3, 1, 2, 3, 2, 2, 2, 9, 1, 5, 3, 7, 1, 2, 1, 6, 1, 1, 3, 6, 1, 1, 1, 1, 1, 1, 1, 15, 2, 4, 1, 1, 7, 1, 2, 1, 1, 15, 2, 1, 5, 1, 1, 13, 1, 2, 1, 1, 1, 5, 2, 21, 1, 1, 
1, 1, 13, 1, 1, 10, 1, 6, 2, 11, 1, 2, 7, 1, 7, 1, 16, 1, 4, 3, 1, 2, 1, 7, 1, 3, 1, 4, 9, 2, 1, 1, 1, 1, 23, 1, 1, 4, 1, 4, 3, 1, 2, 2, 2, 1, 3, 1, 1, 5, 1, 1, 1, 6, 106, 1, 1, 1, 7, 2, 18, 1, 1, 1, 4, 1, 2, 4, 20, 2, 1, 3, 1, 5, 1, 3, 1, 50, 1, 2, 14, 2, 1, 1, 2, 1, 2, 2, 1, 1, 3, 3, 1, 1, 4, 1, 1, 1, 13, 8, 
3, 2, 1, 8, 5, 1, 6, 1, 50, 1, 2, 3, 8, 1, 3, 5, 2, 1, 8, 8, 1, 1, 10, 2, 1, 1, 1, 2, 13, 1, 4, 10, 1, 1, 1, 1, 26, 2, 22, 3, 7, 6, 1, 2, 3, 28, 3, 17, 3, 1, 1, 1, 4, 1, 5, 2, 4, 5, 1, 2, 1, 1, 1, 4, 1, 2, 5, 1, 1, 1, 4, 1, 2, 5, 2, 193, 2, 1, 47, 1, 4, 1, 6, 1, 4, 1, 6, 23, 4, 1, 20, 2, 3, 32, 1, 6, 1, 4, 1, 3, 
1, 10, 1, 3, 1, 1, 2, 5, 2, 1, 1, 1, 93, 1, 1, 11, 8, 1, 1, 1, 1, 2, 15, 4, 1, 7, 1, 3, 2, 1, 1, 1, 9, 10, 1, 6, 1, 4, 5, 3, 1, 11, 1, 6, 5, 1, 1, 1, 1, 3, 1, 152, 3, 1, 4, 3, 7, 1, 473, 1, 1, 1, 3, 108, 2, 1, 3, 3, 3, 6, 1, 1, 1, 18, 1, 51, 2, 2, 5, 2, 2, 1, 1, 15, 6, 10, 1, 6, 1, 1, 6, 8, 2, 33, 1, 6, 2, 5, 3, 1, 
13, 1, 2, 1, 2, 3, 2, 1, 5, 1, 2, 1, 2, 1, 10, 4, 2, 1, 2, 6, 23, 4, 1, 3, 1, 5, 1, 3, 5, 3, 1, 3, 2, 5, 8, 1, 4, 5, 1, 1, 18, 6, 1, 1, 43, 1, 8, 1, 22, 1, 9, 5, 1, 2, 1, 15, 16, 1, 1, 5, 4, 3, 7, 1, 1, 1, 4, 1, 1, 3, 3, 1, 2, 16, 2, 7, 1, 17, 3, 28, 5, 15, 5, 1, 8, 3, 1, 141, 1, 9, 7, 2, 5, 1, 1, 7, 5, 30, 1, 6, 
2, 2, 6, 1, 4, 3, 3, 10, 22, 14, 1, 2, 3, 21, 4, 1, 1, 1, 12, 1, 9, 4, 2, 1, 7, 1, 1, 1, 10, 1, 3, 1, 1, 1, 1, 1, 1, 6, 1, 10, 1, 7, 8, 2, 1, 1, 1, 5, 8, 5, 9, 37, 4, 1, 17, 1, 2, 1, 3, 1, 5, 2, 1, 4, 15, 2, 2, 5, 1, 1, 1, 6, 1, 1, 20, 48, 1, 5, 17, 2, 7, 7, 1, 16, 1, 37, 3, 2, 1, 2, 5, 1, 1, 1, 4, 3, 2, 3, 16, 1, 
2, 18, 2, 1, 1, 1, 1, 1, 4, 1, 3, 5, 1, 2, 23, 2, 3, 1, 4, 13, 7, 1, 5, 1, 2, 1, 1, 30, 1, 7, 4, 1, 1, 1, 15, 1, 17, 1, 4, 1, 1, 1, 2, 188, 1, 5, 2, 2, 19, 2, 1, 2, 1, 70, 1, 2, 1, 2, 3, 1, 4, 1, 1, 1, 4, 1, 3, 1, 1, 2, 1, 1, 5, 5, 2, 1, 2, 7, 2, 2, 1, 1, 2, 2, 1, 31, 8, 1, 1, 3, 1, 1, 1, 1, 3, 15, 2, 1, 3, 1, 
1, 3, 24, 4, 1, 1, 7, 2, 12, 4, 2, 2, 1, 15, 1, 1, 1, 1, 2, 1, 9, 1, 2, 2, 3, 1, 2, 9, 1, 1, 3, 1, 1, 7, 1, 12, 1, 3, 1, 2, 1, 3, 6, 6, 1, 1, 1, 1, 10, 2, 10, 1, 2, 2, 2, 5, 12, 1, 2, 3, 4, 10, 1, 1, 3, 2, 4, 1, 37, 1, 4, 2, 1, 1, 67, 1, 1, 6, 2, 1, 2, 2, 3, 1, 2, 2, 1, 5, 2, 2, 1, 1, 6, 2, 1, 1, 47, 57, 1, 1, 
1, 1, 2, 2, 7, 5, 2, 2, 2, 3, 7, 1, 4, 1, 1, 6, 1, 4, 1, 3, 1, 1, 1, 4, 16, 49, 1, 1, 1, 1, 2, 1, 2, 1, 3, 1, 2, 1, 1, 38, 2, 3, 2, 3, 25, 6, 1, 1, 12, 3, 5, 3, 4, 7, 1, 1, 2, 7, 1, 9, 1, 5, 2, 1, 1, 1, 33, 2, 6, 3, 1, 10, 1, 1, 2, 43, 2, 1, 1, 2, 3, 1, 4, 310, 2, 7, 2, 53, 211, 2, 2, 2, 1, 1, 3, 7, 1, 1, 8, 2, 
3, 2, 2, 1, 2, 1, 2, 1, 9, 3, 11, 1, 2, 1, 2, 4, 1, 1, 1, 1, 5, 2, 2, 1, 17, 1, 1, 1, 2, 1, 1, 1, 1, 1, 6, 4, 3, 3, 11, 23, 2, 1, 5, 12, 21, 2, 1, 2, 3, 6, 5, 1, 1, 1, 1, 1, 210, 15, 1, 1, 16, 3, 1, 2, 4, 1, 2, 20, 3, 3, 3, 3, 3, 1, 23, 29, 1, 23, 24, 1, 2, 3, 1, 2, 7, 1, 5, 80, 1, 2, 4, 2, 2, 32, 2, 4, 16, 3, 46, 2, 
5, 1, 113, 4, 1, 6, 1, 1, 2, 1, 1, 1, 16, 1, 2, 1, 5, 4, 7, 1, 1, 5, 1, 31, 1, 2, 1, 3, 1, 14, 3, 1, 2, 5, 1, 1, 17, 3, 2, 3, 1, 2, 10, 2, 2, 1, 1, 325, 1, 85, 3, 1, 4, 55, 3, 1, 3, 14, 1, 5, 1, 6, 4, 6, 30, 3, 1, 11, 1, 1, 1, 1, 1722, 1, 87, 24, 5, 1, 1, 16, 1, 15, 23, 8, 3, 3, 15, 1, 1, 292, 2, 6, 2, 1, 98, 3, 1, 2, 4, 1, 
5, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 8, 1, 2, 33, 3, 3, 2, 3, 9, 6, 4, 4, 5, 7, 1, 13, 7, 1, 2, 2, 21, 4, 1, 8, 3, 19, 7, 1, 1, 50, 1, 3, 1, 1, 17, 1, 4, 5, 2, 3, 1, 2, 2, 1, 18, 4, 38, 1, 33, 4, 2, 1, 57, 1, 1, 6, 1, 1, 4, 1, 2, 104, 3, 5, 8, 1, 1, 7, 1, 4, 1, 52, 1, 5, 1, 5, 1, 4, 84, 1, 2, 8, 8, 2, 1, 1, 1, 1, 2, 
1, 111, 1, 12, 1, 1, 18, 4, 2, 3, 1, 9, 2, 1, 40, 1, 1, 1, 1, 2, 1, 1, 1, 9, 1, 5, 1, 3, 2, 2, 2, 1, 1, 204, 36, 1, 1, 4, 118, 1, 8, 3, 2, 1, 12, 1, 1, 1, 2, 1, 31, 1, 4, 5, 1, 11, 2, 55, 1, 17, 1, 1, 1, 6, 6, 1, 4, 5, 8, 1, 5, 1, 14, 1, 1, 3, 2, 5, 1, 1, 1, 3, 1, 1, 2, 1, 2, 5, 1, 1, 5, 20, 11, 1, 1, 2, 1, 1, 2, 1, 
3, 4, 46, 2, 4, 1, 1, 1, 10, 2, 1, 5, 1, 2, 4, 22, 2, 7, 1, 1, 1, 10, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 10, 11, 7, 3, 1, 1, 1, 7, 1, 1, 8, 1, 8, 1, 2, 2, 3, 6, 2, 36, 1, 2, 1, 4, 3, 1, 1, 1, 1, 1, 4, 2, 3, 1, 7, 3, 4, 4, 1, 1, 1, 2, 54, 16, 1, 7, 19, 2, 4, 1, 1, 1, 2, 7, 1, 1, 5, 3, 4, 1, 4, 18, 1, 1, 1, 1, 1, 8, 
3, 1, 8, 1, 2, 1, 1, 4, 1, 1, 1, 2, 3, 7, 6, 1, 1, 8, 2, 3, 2, 13, 1, 1, 1, 1, 7, 1, 3, 1, 10, 2, 1, 3, 2, 5, 1, 1, 1, 2, 142, 2, 1, 1, 1, 3, 7, 1, 16, 4, 1, 84, 1, 14, 1, 39, 1, 1, 33, 1, 1, 1, 1, 5, 1, 2, 2, 6, 1, 1, 5, 1, 1, 1, 4, 2, 2, 1, 4, 5, 1, 2, 1, 3, 1, 1, 1, 10, 3, 2, 1, 9, 2, 10, 1, 6, 1, 1, 1, 1, 
2, 2, 14, 3, 1, 5, 2, 4, 1, 3, 29, 2, 2, 2, 4, 1, 18, 1, 4, 1, 1, 2, 3, 3, 4, 1, 3, 2, 1, 1, 1, 2, 4, 1, 1, 1, 1, 46, 1, 1, 3, 4, 3, 212, 3, 1, 2, 1, 1, 4, 8, 1, 74, 1, 2, 1, 5, 1, 1, 9, 1, 1, 1, 1, 3, 80, 2, 1, 3, 1, 1, 2, 2, 4, 4, 1, 2159, 5, 8, 4, 1, 1, 4, 2, 2, 5, 1, 5, 2, 2, 2, 44, 1, 1, 1, 23, 2, 1, 6, 1, 
1, 1, 13, 46, 2, 2, 7, 3, 18, 1, 8277, 35, 29, 2, 1, 2, 2, 6, 1, 5, 2, 1, 5, 2, 242, 4, 1, 4, 1, 1, 4, 1, 7, 1, 1, 2, 3, 1, 1, 1, 7, 1, 28, 1, 50, 10, 2, 37, 13, 1, 1, 1, 2, 2, 2, 3, 1, 1, 1, 5, 2, 1, 4, 1, 1, 520, 10, 2, 8, 1, 4, 1, 39, 3, 1, 1, 6, 1, 1, 1, 9, 1, 1, 7, 10, 1, 1, 5, 1, 1, 2, 6, 2, 5, 5, 4, 1, 12, 1, 6, 
2, 4, 3, 1, 1, 9, 1, 1, 1, 1, 1, 3, 5, 1, 588, 1, 3, 1, 6, 1, 8, 8, 1, 2, 1, 2, 1, 1, 7, 4, 1, 13, 1, 58, 1, 4, 1, 6, 5, 1, 17, 1, 1, 1, 63, 1, 4, 2, 1, 2, 14, 1, 3, 5, 1, 1, 61, 1, 1, 3, 5, 2, 3, 1, 2, 11, 1, 2, 3, 1, 1, 2, 7, 2, 1, 2, 4, 1, 10, 1, 5, 1, 2, 2, 1, 5, 1, 1, 5, 1, 1, 7, 1, 1, 4, 11, 1, 1, 1, 3, 
2, 6, 1, 3, 2, 1, 4, 6, 2, 1, 7, 1, 17, 12, 1, 1, 7, 7, 1431, 5, 1, 10, 2, 4, 9, 1, 7, 2, 2, 5, 1, 1, 1, 3, 1, 8, 1, 1, 1, 1, 17, 1, 1, 1, 1, 1, 3, 1, 1, 2, 3, 73, 7, 4, 1, 2, 1, 5, 1, 2, 1, 1, 1, 2, 3, 4, 6, 1, 1, 1, 3, 1, 2, 10, 21, 9, 3, 1, 5, 1, 1, 7, 6, 3, 4, 19, 11, 1, 1, 1, 6, 5, 3, 1, 8, 4, 2, 1, 1, 1, 
1, 2, 1, 2, 4, 12, 3, 6, 1, 1, 5, 1, 1, 1, 1, 1, 1, 3, 9, 1, 1, 92, 3, 26, 1, 212, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 2, 5, 6, 1, 1, 41, 1, 7, 4, 1, 8, 1, 5, 2, 1, 1, 2, 4, 2, 15, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 10, 8, 1, 12, 2, 1, 1, 1, 10, 1, 12, 5, 1, 3, 1, 1, 1, 1, 3, 1, 1, 1, 5, 331, 1, 1, 1, 22, 3, 1, 3, 3, 
2, 2, 1, 1, 21, 2, 1, 1, 57, 2, 2, 1, 5, 1, 117, 21, 7, 19, 1, 3, 1, 1, 1, 5, 4, 4, 7, 3, 2, 3, 1, 3, 4, 2, 21, 1, 5, 1, 2, 1, 143, 1, 1, 4, 1, 1, 2, 6, 2, 1, 1, 2, 3, 49, 1, 3, 2, 31, 2, 1, 32, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 5, 1, 7, 1, 1, 1, 7, 1, 2, 5, 1, 2, 1, 1, 1, 12, 5, 5, 1, 2, 2, 27, 1, 1, 1, 2, 1, 
21, 1, 4, 1, 4, 1, 6, 7, 1, 1, 1, 1, 2, 4, 2, 21, 2, 3, 1, 4, 1, 501, 1, 1, 11, 7, 3, 1, 2, 6, 9, 1, 1, 15, 3, 1, 3, 1, 3, 1, 4, 1, 40, 1, 1, 22, 154, 1, 5, 7, 1, 2, 3, 8, 1, 5, 1, 3, 1, 4, 1, 5, 8, 1, 1, 2, 1, 1, 1, 1, 5, 10, 1, 1, 2, 2, 1, 1, 5, 1, 2, 4, 5, 1, 1, 23, 1, 47, 1, 17, 9, 4, 2, 1, 3, 20, 1, 1, 2, 180, 
1, 1, 2, 6, 1, 9, 1, 2, 1, 1, 2, 5, 1, 7, 1, 4, 1, 1, 2, 1, 21, 2, 1, 3, 1, 2, 6, 1, 15, 2, 3, 3, 1, 1, 18, 27, 1, 9, 19, 1, 6, 1, 2, 1, 1, 12, 3, 23, 1, 1, 1, 42, 1, 3, 1, 6, 1, 7, 1, 4, 1, 7, 4, 1, 1, 3, 3, 46, 8, 1, 3, 10, 6, 1, 2, 3, 1, 42, 1, 4, 1, 2, 6, 3, 1, 1, 1, 6, 1, 5, 1, 2, 9, 1, 2, 9, 37, 4, 2, 4, 
2, 9, 1, 5, 2, 4, 1, 2, 1, 18, 5, 2, 3, 2, 3, 4, 1, 27, 11, 1, 3, 1, 3, 1, 7, 1, 13, 2, 1, 1, 1, 1, 1, 9, 4, 2, 1, 1, 9, 1, 1, 15, 8, 1, 3, 4, 2, 7, 1, 4, 134, 5, 1, 57, 2, 18, 2, 9, 1, 1, 3, 1, 4, 2, 3, 1, 1, 2, 1, 8, 2, 2, 1, 1, 1, 2, 35, 2, 1, 3, 2, 1, 7, 1, 11, 1, 1, 1, 1, 7, 1, 1, 3, 7, 1, 1, 4, 1, 1, 63, 
1, 1, 1, 14, 527, 3, 1, 1, 3, 1, 19, 1, 3, 2, 1, 1, 44, 1, 2, 1, 1, 3, 17, 3, 1, 3, 1, 3, 2, 3, 9, 1, 75, 5, 34, 3, 3, 3, 1, 55, 2, 1, 1, 1, 29, 5, 15, 1, 3, 1, 1, 8, 1, 82, 2, 1, 1, 2, 1, 4, 13, 1, 2, 2, 172, 3, 12, 6, 2, 1, 19, 1, 1, 27, 2, 2, 1, 1, 2, 1, 1, 6, 1, 2, 1, 6, 2, 1, 4, 2, 1, 4, 1, 3, 2, 2, 2, 4, 1, 1282, 
1, 2, 1, 2, 1, 17, 1, 14, 2, 2, 2, 4, 2, 1, 1, 3, 2, 1, 2, 1, 1, 4, 1, 4, 1, 1, 1, 2, 4, 1, 3, 3, 1, 1, 1, 1, 1, 204, 1, 2, 3, 2, 1, 3, 4, 1, 1, 3, 1, 5, 4, 18, 4, 1, 1, 12, 1, 2, 3, 1, 1, 1, 5, 1, 5, 3, 5, 2, 1, 9, 1, 2, 1, 1, 4, 3, 1, 1, 4, 3, 29, 8, 3, 5, 2, 1, 1, 1, 9, 1, 1, 4, 3, 1, 1, 2, 4, 5, 2, 3, 
2, 1, 1, 4, 1, 1, 16, 1, 12, 4, 1, 1, 2, 1, 1, 36, 3, 5, 6, 1, 1, 6, 1, 1, 1, 2, 2, 89, 3, 2, 3, 2, 1, 3, 1, 1, 6, 1, 15, 15, 1, 5, 5, 9, 4, 3, 1, 1, 16, 1, 1, 2, 1, 4, 4, 1, 1, 11, 8, 1, 1, 1, 1, 52, 4, 4, 2, 1, 1, 2, 3, 1, 2, 1, 8, 1, 1, 3, 1, 1, 2, 5, 1, 2, 1, 2, 2, 3, 2, 18, 9, 1, 4, 8, 2, 31, 1, 1, 164, 4, 
3, 2, 1, 8, 12, 2, 78, 6, 3, 3, 14, 10, 1, 26, 2, 6, 34, 1, 7, 12, 1, 1, 2, 2, 1, 1, 4, 1, 12, 2, 19, 2, 1, 20, 1, 38, 1, 4, 1, 2, 8, 1, 9, 3, 3, 11, 1, 2, 1, 1, 1, 8, 1, 2, 2, 1, 1, 1, 1, 1, 3, 2, 1, 2, 14, 1, 2, 8, 3, 1, 1, 3, 7, 1, 1, 13, 1, 5, 1, 2, 1, 58, 1, 1, 1, 14, 2, 1, 3, 19, 1, 13, 7, 1, 4, 5, 1, 2, 1, 2, 
    ]
assert len(Globals.first_5000_terms_of_continued_fraction_of_pi_omit_zeroth_term) == 5000


def _get_return_value_of_null_generator_iterator(it0, /):
    try:
        next(it0)
    except StopIteration as exc:
        r = exc.value
    else:
        raise logic-err
    return r

def _t():
    def f():
        return 1; yield
    it = f()
    print(_get_return_value_of_null_generator_iterator(it))
        # => 1
    print(_get_return_value_of_null_generator_iterator(it))
        # => None
    #不可重复取值！

    def f():
        while 1:
            return 1
        yield
    it = f()
    print(_get_return_value_of_null_generator_iterator(it))
        # => 1
    print(_get_return_value_of_null_generator_iterator(it))
        # => None

#_t();raise


def show_min_idx_max_term_pairs5ipath(ipath, /, *args4islice):
    def put_last_idx_int_pair(i, u, /):
        tmay_i_u_pair.append((i,u))
    tmay_i_u_pair = []
    ls = []
    it = iter_min_idx_max_term_pairs5ipath(ipath, *args4islice, put_last_idx_int_pair=put_last_idx_int_pair)
    i_u = (-1,-1)
    for i_u in it:
        print(i_u, flush=True)
        ls.append(i_u)
    print(ls, flush=True)
    if not args4islice:
        [i_u] = tmay_i_u_pair
    if 0:
        if not args4islice:
            i_u = _get_return_value_of_null_generator_iterator(it)
    print('last=', i_u, flush=True)
    return
    ls = [*iter_min_idx_max_term_pairs5ipath(ipath, *args4islice)]
    print(ls)

def iter_min_idx_max_term_pairs5ipath(ipath, /, *args4islice, put_last_idx_int_pair):
    with open(ipath, 'rb') as ibfile:
        if 0b00:
            #testing
            import io
            ibfile = io.BytesIO(b'2, 3, 1, ')
        it = it0 = iter_min_idx_max_term_pairs5ibfile(ibfile, put_last_idx_int_pair=put_last_idx_int_pair)
        if args4islice:
            it = islice(it, *args4islice)
        yield from it
        if 0:
            if not args4islice:
                i_u = _get_return_value_of_null_generator_iterator(it0)
                #bug:i_u 永远为None，因为 不可重复取值
                return i_u
            else:
                return ()

def iter_min_idx_max_term_pairs5ibfile(ibfile, /, *, put_last_idx_int_pair):
    prev_max = -1
    (i, u) = (-1, -1)
    for i, u in enumerate(iter_ints5ibfile(ibfile)):
        if prev_max < u:
            yield (i, u)
            prev_max = u
    put_last_idx_int_pair(i, u)
    return (i, u)

def iter_ints5ibfile(ibfile, /):
    r'regex_b"(\d+\s*[,;]\s*)*" -> Iter int'
    L = 1<<16
    prev_tail = b''
    while 1:
        _bs = ibfile.read(L)
        bs = prev_tail + _bs
        bs = bs.replace(b';', b',')
        bss = bs.split(b',')
        prev_tail = bss.pop()
        for u in map(int, bss):
            yield u
        if not _bs:
            if not (prev_tail.isspace() or not prev_tail): raise Exception([prev_tail])#logic-err
            return
            break

if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main, adhoc_argparse, AdhocArgParserError
    adhoc_argparser__main(globals(), None)
        #main()


