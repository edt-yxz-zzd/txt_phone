r'''
?@ - 美
7
5
9

e - e
s - s
t - t


/ eI; e/ [ei; ə]

/ 7eI eI 5eI; 9e e `e/ [ˌeɪ eɪ ˈeɪ]

/ E5bAk; E`bAk/ [ə'bæk]                       ']
E - ə
A - æ
b - b
k - k
` - ˈ
I - ɪ - i??


/ 5AbEkEs; `AbEkEs/ 英 [ˈæbəkəs]  美 [ˈæbəkəs]
/ E5bB:ft; ?@ E5bAft; E`bAft/ 英 [əˈbɑ:ft]  美 [əˈbæft]

B: - ɑ:

/ E5bAFt; E`bAFt/ [əˈbæʃt]
F - ʃ


/ 5AbEtwB:(r); ?@ 7AbE5twB:r; 9AbE`twBr/ 英 [ˈæbətwɑ:(r)]  美 [ˈæbəˌtwɑr]
() - optional
r - r
w - w
B - ɑ
: - :

/ 5Abes; `AbZs/ 英 [ˈæbes]  美 [ˈæbɪs] 
Z - ɪ????????? wrong


/ E5bri:vIeIt; E`brivI9et/ 英 [əˈbri:vieɪt]  美 [əˈbriviˌet] 
i: - i:
9 - ˌ
/ E9bri:vI5eIFn; E9brivI`eFEn/ 英 [əˌbri:viˈeɪʃn]  美 [əˌbriviˈeʃən]
v - v
n - n
5 - ˈ
/ Ab5dCmInl; Ab`dBmEnl/ 英 [æbˈdɒmɪnl]  美 [æbˈdɑ:mɪnl] 
d - d
C - ɒ
m - m
l - l

/ Eb5dQkt, Ab-; Eb`dQkt, Ab-/ 英 [æbˈdʌkt]  美 [æbˈdʌkt] 
Q - ʌ

/ 5AberEnt; Ab`ZrEnt/ 英 [æˈberənt]  美 [æˈbɛrənt, ˈæbə-] 
Z - ɛ ????

/ E5bet; E`bZt/ 英 [əˈbet]  美 [əˈbɛt] 
Z - ɛ

/ Eb5hR:(r); Eb`hRr/ 英 [əbˈhɔ:(r)]  美 [æbˈhɔr] 
h - h
R - ɔ
/ E5baId; E`baId/ 英 [əˈbaɪd]  美 [əˈbaɪd] 
a - a

/ Eb5dVUE(r); Eb`dVJr/ 英 [əbˈdʒʊə(r)]  美 [əbˈdʒʊr] 
V - ʒ
U - ʊ
J - u???


'''

import os.path

path = r'E:\book\数据\英汉词典\牛津英汉双解(第4版)TXT\0001A'

encoding = 'utf_16_be' if 0 else 'gb18030'
s = set()
N = len(s)
for (dirpath, dirnames, filenames) in os.walk(path):
    for basename in filenames:
        fname = os.path.join(dirpath, basename)
        try:
            with open(fname, encoding=encoding, errors='replace') as fin:
                pre_line = ''
                for line in fin:
                    if 'strong form 强读式' in line or '罕读作' in line:
                        pass
                    elif '缩写' in line:
                        pass
                    elif line[:1] == '/':
                        try:
                            j = line.index('/', 1)
                        except:
                            print(basename)
                            print(line)
                        else:
                            s.update(line[1:j])
                            if len(s) != N:
                                print(pre_line[:-1])
                                print(line[:j+1])
                                print(''.join(sorted(s)))
                                N = len(s)
                    pre_line = line
        except:
            print(basename)
            raise
ss = ''.join(sorted(s))
print(ss)
                

















