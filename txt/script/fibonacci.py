r"""
fibonacci



f[0]=0


v[n]=[;f[n-1];f[n]]
v[0]=[;1;0]
mx = [;0,1;1,1]
v[n]=mx*v[n-1]=mx^n*v[0]






$ python fibonacci.py | more
0:0
1:1
2:1
3:2
4:3
5:5
6:8
7:13
8:21
9:34
10:55
11:89
12:144
13:233
14:377
15:610
16:987
17:1597
18:2584
19:4181
20:6765
21:10946
22:17711
23:28657
24:46368
25:75025
26:121393
27:196418
28:317811
29:514229
30:832040
31:1346269
32:2178309
33:3524578
34:5702887
35:9227465
36:14930352
37:24157817
38:39088169
39:63245986
40:102334155
41:165580141
42:267914296
43:433494437
44:701408733
45:1134903170
46:1836311903
47:2971215073
48:4807526976
49:7778742049
50:12586269025
51:20365011074
52:32951280099
53:53316291173
54:86267571272
55:139583862445
56:225851433717
57:365435296162
58:591286729879
59:956722026041
60:1548008755920
61:2504730781961
62:4052739537881
63:6557470319842
64:10610209857723
65:17167680177565
66:27777890035288
67:44945570212853
68:72723460248141
69:117669030460994
70:190392490709135
71:308061521170129
72:498454011879264
73:806515533049393
74:1304969544928657
75:2111485077978050
76:3416454622906707
77:5527939700884757
78:8944394323791464
79:14472334024676221
80:23416728348467685
81:37889062373143906
82:61305790721611591
83:99194853094755497
84:160500643816367088
85:259695496911122585
86:420196140727489673
87:679891637638612258
88:1100087778366101931
89:1779979416004714189
90:2880067194370816120
91:4660046610375530309
92:7540113804746346429
93:12200160415121876738
94:19740274219868223167
95:31940434634990099905
96:51680708854858323072
97:83621143489848422977
98:135301852344706746049
99:218922995834555169026
100:354224848179261915075
101:573147844013817084101
102:927372692193078999176
103:1500520536206896083277
104:2427893228399975082453
105:3928413764606871165730
106:6356306993006846248183
107:10284720757613717413913

"""

class Globals:
	v0 = (1,0)
	mx = (0,1,1,1)

def vec2_mul(lhs, rhs):
	return lhs[0]*rhs[0]+lhs[1]*rhs[1]
def mx22_mul(lhs, rhs):
	row0 = lhs[:2]
	row1 = lhs[2:]
	col0 = rhs[::2]
	col1 = rhs[1::2]
	rs = (row0,row0, row1,row1)
	cs = (col0,col1, col0,col1)
	mx = (*map(vec2_mul, rs,cs),)
	return mx
def mx22_vmul(lhs, rhs):
	row0 = lhs[:2]
	row1 = lhs[2:]
	col0 = rhs
	rs = (row0,row1)
	cs = (col0,col0)
	v = (*map(vec2_mul, rs,cs),)
	return v

def mx22_pow(mx, n):
	assert n >=0
	r = (1,0,0,1)
	while 1:
		if n&1:
			r = mx22_mul(r, mx)
		n >>= 1
		if not n: break
		mx = mx22_mul(mx, mx)
	return r

def calc_vn(n):
	mx = mx22_pow(Globals.mx, n)
	vn = mx22_vmul(mx, Globals.v0)
	#print(mx, vn)
	return vn

def iter_fibonacci(v):
	v0,v1 = v
	while 1:
		yield v1
		v0,v1 = v1, v0+v1

def iter_fibonacci_from(n):
	vn = calc_vn(n)
	#print(vn)
	it = iter_fibonacci(vn)
	yield from enumerate(it, n)




def main(args=None):
    import argparse, sys
    #from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description=r"show fibonacci"
        , epilog=r""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-n', "--from_n", type=int, default=0
                        , help='from fibonacci[n]')
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
    omode = 'at' if args.force else 'xt'

    n = args.from_n
    if n<0:raise Exception(f"n={n}<0")
    it = iter_fibonacci_from(n)
    def do(it, fout):
        for n, fn in it:
            print(f"{n}:{fn}", file=fout)

    may_ofname = args.output
    #with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
    if may_ofname is None:
        fout = sys.stdout
        do(it, fout)
    else:
        with open(may_ofname, omode, encoding=encoding) as fout:
            do(it, fout)
if __name__ == "__main__":
    main()




