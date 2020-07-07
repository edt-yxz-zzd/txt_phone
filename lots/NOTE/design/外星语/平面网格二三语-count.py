#-*-coding:utf8;-*-
#qpy:3
#qpy:console

print("This is console module")
#网格文字，编码整数在“蚕”中。-<oooo>-
#1:隔+选
#2:face>=4
#证明c3连接同面不同的两边仍是c3

#1:2n:up vtx u:curr i
#    f n u = [n>0][u>=0]sum: CC (u+i) i * f (n-1-i) i {i}
#    f 0 u = [u>=0]

import math as M
#print(dir(M))
FF  = M.factorial
#CC = M.choose
def CC(n, i):
    if not 0 <= i <= n: return 0
    return FF(n)//FF(i)//FF(n-i)

fd = {}
def f(n, u):
    if u < 0: return 0
    if n == 0: return 1
    if n < 0: return 0
    k = n, u
    m = fd.get(k)
    if m is not None: return m

    r = sum(CC(u+i, i) * f( n-1-i, i) for i in range(0, n))
    fd[k] = r
    return r
def ft(n):
    for j in range(n):
        print(j, f(j, 0))

ft(10)
#print([f(j, 0) for j in range(10)])
assert [f(j, 0) for j in range(10)] == [1, 1, 2, 4, 9, 22, 57, 154, 430, 1234]
#http://oeis.org/A287709



#2:2n:external face o
#    up left face i
#    first edge must be splitted or not, s
#    g n o s | o<3 = 0
#    g n o s | n<0 = 0
#    #bug: g n o s | n==0 = 1
#    g n o s | n==0 = [o>3][not s]
#    #bug:g n o s = sum: g (n-1) (o-i+4) (not 3<i<o-i+4) * (1 if s else i-2) {3<=i<=o+1}
#    g n o s = sum: g (n-1) (o-i+4) (i==3) * (1 if s else i-2) {3<=i<=o+1}
F = False
T = True
gd = {}
def g(n, o, s):
    if n < 0 or o < 3: return 0
    if n == 0: return int(o > 3 and not s)
    s = bool(s)
    k = n, o, s
    m = gd.get(k)
    if m is not None: return m

    r = sum(g(n-1, o-i+4, i==3) * (1 if s else i-2)
             for i in range(3, o+2)
             )
    gd[k] = r
    return r
def gt(n):
    for j in range(n):
        print(j, g(j, 4, F))

gt(10)
#print([g(j, 4, F) for j in range(10)])
assert [g(j, 4, F) for j in range(10)] == [1, 2, 6, 25, 114, 532, 2516, 12044, 58303, 285076]


def eval_util(max=0x11_0000, n=1000):
    for j in range(n):
        x = f(j, 0)
        print(j, x)
        if x > max:break
    print(j, [f(i,0) for i in range(j+1)], max)

    for j in range(n):
        x = g(j, 4, F)
        print(j, x)
        if x > max:break
    print(j, [g(i,4,F) for i in range(j+1)], max)
eval_util()




