#__all__:goto
r'''[[[
e script/整数分解囗平方差囗中国剩余定理.py
py script/整数分解囗平方差囗中国剩余定理.py


猜想已被证明:
    [M > 0][gcd(M,N)==1]:
        [len(求平方差分解囗模囗暴力(M, N)) == phi(M)*2**[M%2==0] == phi(2*M)]
    [@[M,N::int] -> [M > 0] -> [gcd(M,N)==1] -> [len{(x,y) | [x,y:<- [0..<M]][(x**2-y**2-N) %M ==0]} == phi(2*M)]]
    --> e others/数学/我的猜想.txt

[[
不断提升M，最终分解N
factorint(N)

[x**2-y**2 =[%M]= N]
M[j] = II p[i]**e<p[i]> {i<-[0..=j]}
  = M[j-1] * p[j]**e<p[j]>
  p[i] -> p[i]**2 -> ... -> p[i]**e<p[i]>

XY_exact(N) := {(x,y) | [x,y<-[0..<N]][x**2-y**2 == N]}
  == {(x,y) | [x<-[ceil_sqrt(N)..<N]][y<-[0..<x]][y==floor_sqrt(x**2-N)][x**2-y**2 == N]}
XY(N;M) := {(x,y) | [x,y<-[0..<M]][x**2-y**2 =[%M]= N]}
求XY(N;M[j-1])，XY(N;p[j]**e<p[j]>)
再用CRT中国剩余定理求XY(N;M[j])
[@[N<-[2..]] -> @[J<-[1..]] -> [M[J] > N] -> [XY_exact(N) |<=| XY(N;M[J])]]


# %p**i --> %p**(i+1)
[is_prime p][i <- [1..]][N%p =!= 0]:
    [ni := N%p**i]
    [ni1 := N%p**(i+1)]

    [x,y <- [0..<p**i]]
    [x**2-y**2 =[%p**i]= N]
    [(x**2-y**2) %p**i == ni]

    [x1,y1 <- [0..<p**(i+1)]]
    [x1**2-y1**2 =[%p**(i+1)]= N]
    [(x1**2-y1**2) %p**(i+1) == ni1]
    [x1%p**i == x][y1%p**i == y]

    [u,v,s,t <- [0..<p]]
    [x1 == x+u*p**i][y1 == y+v*p**i]
    [(x**2-y**2) %p**(i+1) == ni+s*p**i]
    [(x1**2-y1**2) %p**(i+1) == ni+t*p**i]
    [ni1 == ni+t*p**i]
    [t == N//p**i %p]
    [s == (x**2-y**2)//p**i %p]

    [x1**2-y1**2
        == (x**2-y**2) + 2*p**i*(u*x-v*y) + p**(2*i)*(u**2-v**2)
        =[%p**(i+1)]= (x**2-y**2) + 2*p**i*(u*x-v*y)
        =[%p**(i+1)]= (ni+s*p**i) + 2*p**i*(u*x-v*y)
        =[%p**(i+1)]= ni + p**i*(2*u*x-2*v*y +s)
        =[%p**(i+1)]= ni+t*p**i
        ]
    [(2*u*x-2*v*y +s)%p == t]
    [(2*u*x-2*v*y)%p == (t-s)%p]
    * [p=!=2]:
        (u,v)有p对解
        (x1,y1)有p对解
        提升i，可行解数量指数性增长，没有意义
    * [p==2]:
        [0 == (2*u*x-2*v*y)%p == (t-s)%p]
        [t%2 == s%2]
        [t == s]
        * [t%2 =!= s%2]:
            1解%p**i 变 0解%p**(i+1)
            可能 导致 非指数性增长
        * [t%2 == s%2]:
            uv组合为4
            1解%p**i 变 4解%p**(i+1)
                见下面:若[e>=i+2]则1解%p**i 变 2解%p**(i+1)
            但 s 依赖于1解%p**i，所有 可行解数量 未必就是 指数性增长
            # %p**(i+1) --> %p**(i+2)
            [x1 == x+u*2**i][y1 == y+v*2**i]
            !![t == N//p**i %p]
            !![s == (x**2-y**2)//p**i %p]
            [t1 := N//p**(i+1) %p]
            [s1 := (x1**2-y1**2)//p**(i+1) %p]
            [i>=2]:
                [s1 == (x1**2-y1**2)//2**(i+1) %2
                == (x1**2-y1**2) %2**(i+2) //2**(i+1) %2
                == ((x+u*2**i)**2-(y+v*2**i)**2) %2**(i+2) //2**(i+1) %2
                == ((x**2+2*x*u*2**i)-(y**2+2*y*v*2**i)) %2**(i+2) //2**(i+1) %2
                == (x**2-y**2 + (u*x-v*y)*2**(i+1))//2**(i+1) %2
                == ((x**2-y**2)//2**(i+1) %2 + (u*x-v*y)*2**(i+1)//2**(i+1) %2) %2
                == ((x**2-y**2)//2**(i+1) %2 + (u*x-v*y)%2) %2
                == ((x**2-y**2)//2**(i+1) + (u*x-v*y)) %2
                == t1
                ]
                [(u*x-v*y)
                =[%2]= t1-(x**2-y**2)//2**(i+1)
                =[%2]= t1+(x**2-y**2)//2**(i+1)
                =[%2]= (x**2-y**2)//2**(i+1) + N//2**(i+1) %2
                =[%2]= (x**2-y**2 + N)//2**(i+1)
                ]
                !![N%p =!= 0]
                [N%2 == 1]
                [(x**2-y**2)%2==N%2 == 1]
                [x%2=!=y%2]
                [r := (u*x-v*y)%2]
                * [x%2==0][y%2==1]:
                    [(u*0-v*1)%2==r]
                    [v==r]
                    [u<-{0,1}]
                    [uv解数量 == 2]
                * [x%2==1][y%2==0]:
                    [(u*1-v*0)%2==r]
                    [u==r]
                    [v<-{0,1}]
                    [uv解数量 == 2]


[M<-[3,5..]][M%2==1][a,b <- [0..<M]][a*b =[%M]= N][gcd(N,M)==1]:
    [gcd(a*b,M)==1]
    [gcd(a,M)==1]
    [gcd(b,M)==1]
    #[M%2==1]
    [inv_2 := 2**-1 %M]
    [inv_2 == (M+1)///2]
    [(x+y)==a]
    [(x-y)==b]
    [x == (a+b)*inv_2 %M]
    [y == (a-b)*inv_2 %M]

    [inv_a := a**-1 %M]
    [b == N*inv_a %M]
    [x == (a+N*inv_a)*inv_2 %M]

    [c <- [0..<M]][gcd(c,M)==1][inv_c := c**-1 %M][(c+N*inv_c)*inv_2 =[%M]= (a+N*inv_a)*inv_2]:
        !![(c+N*inv_c)*inv_2 =[%M]= (a+N*inv_a)*inv_2]
        [2*a*c*(c+N*inv_c)*inv_2 =[%M]= 2*a*c*(a+N*inv_a)*inv_2]
        [(a*c*c+a*N) =[%M]= (a*c*a+c*N)]
        [a*c*(c-a) =[%M]= (c-a)*N]
        [(a*c-N)*(c-a) %M == 0]
        [(a*c-a*b)*(c-a) %M == 0]
        [a*(c-b)*(c-a) %M == 0]
        [(c-b)*(c-a) %M == 0]
        [[
        [is_prime M][p:=M]:
            [[(a*c-N)%p == 0]or[(c-a)%p == 0]]
            * [(a*c-N)%p == 0]:
                [c == N*inv_a %p == b]
            * [(c-a)%p == 0]:
                [c==a]
            [c <- {a,b}]


            [ab_pairs := {(a,b) | [a:<-[1..<p]][b:=N*inv_mod_(p;a)%p]}]
            [len ab_pairs == p-1]
            [ab_pairs__eq := {(a,b) <- ab_pairs | [a==b]}]
            [ab_pairs__ne := {(a,b) <- ab_pairs | [a=!=b]}]

            [ab_pairs == ab_pairs__eq \-/ ab_pairs__ne]
            [{} == ab_pairs__eq /-\ ab_pairs__ne]
            [len ab_pairs == len ab_pairs__eq + len ab_pairs__ne]
            [2 \\\ (len ab_pairs__ne)]
            !![p%2==1]
            [2 \\\ (p-1)==(len ab_pairs)]
            [2 \\\ (len ab_pairs__eq)]
            [xs := {x | [(a,b) <- ab_pairs][x:=(a+b)*inv_2]}]
            [len xs == len ab_pairs__eq + (len ab_pairs__ne)///2
                == (len ab_pairs__eq)///2 + (len ab_pairs__eq + len ab_pairs__ne)///2
                == (len ab_pairs__eq)///2 + (len ab_pairs)///2
                == (len ab_pairs__eq)///2 + (p-1)///2
            ]

            [ab_pairs__eq == {(a,b) <- ab_pairs | [a==b]}
                == {(a,b) <- ab_pairs | [a==N*inv_mod_(p;a)%p]}
                == {(a,b) <- ab_pairs | [a**2%p=N%p]}
                == {(a,a) | [a:<-[1..<p]][a**2%p=N%p]}
            ]

            !!p奇素数
            !![N%p=!=0]
            * [Jacobi_symbol(p;N)==+1]:
                ?[r<-[1..=p//2]] -> [r**2%p==N%p]
                [p-r > p//2 >= r]
                [{r,p-r} == {a<-[0..<p] | [a**2%p==N%p]}]
                [ab_pairs__eq == {(r,r), (p-r,p-r)}]
                [len ab_pairs__eq == 2]
                [len xs == (len ab_pairs__eq)///2 + (p-1)///2 == (p+1)///2]

            * [Jacobi_symbol(p;N)==-1]:
                [{} == {r<-[0..<p] | [r**2%p==N%p]}]
                [len ab_pairs__eq == 0]
                [len xs == (len ab_pairs__eq)///2 + (p-1)///2 == (p-1)///2]
            [len xs == (p+Jacobi_symbol(p;N))///2]
            [xys_(p;N) =[def]= {(x,y) | [x,y:<-[0..<p]][x**2-y**2=[%p]=N]}]
            [len_xys_(p;N) =[def]= len xys_(p;N)]
            [len_xys_(p;N) == len ab_pairs<p;N> == p-1 == phi(p) == phi(2*p**1)]
                #猜想-特例证明: %奇素数

            [xs_(p;N) =[def]= {x | [(x,y) :<- xys_(p;N)]}]
            [ys_(p;N) =[def]= {y | [(x,y) :<- xys_(p;N)]}]
            [len_xs_(p;N) =[def]= len xs_(p;N)]
            [len_ys_(p;N) =[def]= len ys_(p;N)]
            [len_ys_(p;+N) == len_xs_(p;-N)]
            [len_xs_(p;+N) == (p+Jacobi_symbol(p;+N))///2]
            [len_ys_(p;+N) == len_xs_(p;-N) == (p+Jacobi_symbol(p;-N))///2]
            [@[x<-xs_(p;+N)] -> [(p-x)<-xs_(p;+N)]]
            [[len_xs_(p;+N)%2==1] <-> [0<-xs_(p;+N)] <-> [Jacobi_symbol(p;-N)==+1]]

            [xxs_(p;N) =[def]= {x**2%p | [x:<-xs_(p;N)]}]
            [yys_(p;N) =[def]= {y**2%p | [y:<-ys_(p;N)]}]
            [len_xxs_(p;N) =[def]= len xxs_(p;N)]
            [len_yys_(p;N) =[def]= len yys_(p;N)]
            [len_yys_(p;+N) == len_xxs_(p;+N)]
                # [xx=[%p]=N+yy]
            [len_yys_(p;+N) == len_xxs_(p;-N)]
                # [ww=[%p]=(+N)+zz]
                #   zz play as yy
                # [zz=[%p]=(-N)+ww]
                #   zz play as xx
            [len_yys_(p;+N) == len_xxs_(p;+N) == len_xxs_(p;-N) == len_yys_(p;-N)]
            [len_xxs_(p;N) == (len_xs_(p;N)+1)//2]
                # +x,-x; 0
                # [gcd(p,x)=!=1]==>>[x==0]
            [len_xxs_(p;+N) == (len_xs_(p;+N)+1)//2 == ((p+Jacobi_symbol(p;+N))///2+1)//2]
            [len_xxs_(p;+N) == len_xxs_(p;-N) == ((p+Jacobi_symbol(p;-N))///2+1)//2]
            [((p+Jacobi_symbol(p;+N))///2+1)//2 == ((p+Jacobi_symbol(p;-N))///2+1)//2]
            [Jacobi_symbol(p;-1)==-1]:
                ###下面证明 <==> [p%4==3]
                <==> [Jacobi_symbol(p;+N) =!= Jacobi_symbol(p;-N)]
                !![((p+Jacobi_symbol(p;+N))///2+1)//2 == ((p+Jacobi_symbol(p;-N))///2+1)//2]
                [((p-1)///2+1)//2 == ((p+1)///2+1)//2 == ((p-1)///2+1+1)//2]
                [2 \\\ ((p-1)///2+1)]
                [(p-1)///2 %2 == 1]
                [(p-1)%4 ///2 == 1]
                [(p-1)%4 == 2]
                [p%4 == 3]
                    #233，原来可以这样证明:[Jacobi_symbol(p;-1)==+1] <==> [p%4==1]
                ...
        ]]
        [[
        @[p,e::int][is_prime p][p%2==1][e>=1][p**e==M]:
            [xys_ex_(p**e;N) =[def]= {(x,y) | [x,y:<-[0..<p**e]][x**2-y**2=[%p**e]=N]}]
            [len_xys_ex_(p**e;N) =[def]= len xys_ex_(p**e;N)]

            [xs_ex_(p**e;N) =[def]= {x | [(x,y) :<- xys_ex_(p**e;N)]}]
            [ys_ex_(p**e;N) =[def]= {y | [(x,y) :<- xys_ex_(p**e;N)]}]
            [len_xs_ex_(p**e;N) =[def]= len xs_ex_(p**e;N)]
            [len_ys_ex_(p**e;N) =[def]= len ys_ex_(p**e;N)]

            [(c-b)*(c-a) %M == 0]
            [(c-b)*(c-a) %p**e == 0]
            [e_cb := max_power_of_base_as_factor_of_(p;(c-b)%p**e +p**e)]
            [e_ca := max_power_of_base_as_factor_of_(p;(c-a)%p**e +p**e)]
            [e_ba := max_power_of_base_as_factor_of_(p;(b-a)%p**e +p**e)]
                #避免0导致结果+oo
                #即用e替代 两个等价输出{e,+oo}
            [[
            [(c-a)%p**e =!= 0][(c-b)%p**e =!= 0]:
                [e_cb < e][e_ca < e]
                [e_cb + e_ca >= e]
                [1 <= e_cb < e][1 <= e_ca < e]
                [e>=2]
                [e_ba >= min(e_cb, e_ca)]
                [e_ba > min(e_cb, e_ca)]:
                    [e_cb == e_ca]
                    #may be [a==b][e_ba==e]
                [e_cb =!= e_ca]:
                    [e_ba == min(e_cb, e_ca)]

                [e_cb >= min(e_ba, e_ca)]
                [e_ca >= min(e_cb, e_ba)]
                [e_ba >= min(e_cb, e_ca)]

                [e_cba := min(e_cb,e_ca,e_ba)]
                [e_cba >= 1]
                [(c-a)%p**e_ca == 0][(c-b)%p**e_cb == 0]
                [(c-a)%p**e_cba == 0][(c-b)%p**e_cba == 0]
                [c =[%p**e_cba]= b =[%p**e_cba]= a]
                [c =[%p]= b =[%p]= a]
                !![a*b =[%M]= N]
                [a*b =[%p**e]= N]
                [a*b =[%p]= N]
                [a**2 =[%p]= N]
                [Jacobi_symbol(p;N) == +1]
                [is_square_residual_mod(p;N)]
                [is_square_residual_mod(p**e;N)]

                [eh := (e+1)//2]
                !![e>=2]
                [1 <= eh < e]
                * [2*e_ba >= e]:
                    <==> [e_ba >= eh]
                    * [e_ba == min(e_cb, e_ca)]:
                        [e_cba == e_ba >= eh]
                    * [e_ba > min(e_cb, e_ca)]:
                        [e_cb == e_ca]
                        !![e_cb + e_ca >= e]
                        [2*e_cb >= e]
                        [e_cba == e_cb >= eh]
                    [e_cba >= eh]
                    [c%p**eh == a%p**eh == b%p**eh]
                    [c//p**eh =!= a//p**eh][c//p**eh =!= b//p**eh]
                    [len {c<{a,b}>|...[[c=!=b][c=!=a]]} == (p**(e-eh) - 2 + [a==b])]
                    [len ({a,b} \-/ {c<{a,b}>|...[[c=!=b][c=!=a]]}) == 2-[a==b] + (p**(e-eh) - 2 + [a==b]) == p**(e-eh)]

                * [2*e_ba < e]:
                    <==> [e_ba < eh]
                    [e_cba == e_ba]
                    [e_cba == e_ba]
                    [min(e_cb,e_ca) == e_ba < eh]
                    !![e_cb + e_ca >= e]
                    [max(e_cb,e_ca) + min(e_cb,e_ca) >= e]
                    [max(e_cb,e_ca) >= e - min(e_cb,e_ca) == e - e_ba >= e-(eh-1) == e-((e+1)//2-1) == e-(e-1)//2 == e//2+1 >= eh > e_ba]
                    [e - e_ba > e_ba]
                    [b%p**(e-e_ba) =!= a%p**(e-e_ba)]
                    [[[c%p**(e-e_ba) == a%p**(e-e_ba)][c//p**(e-e_ba) =!= a//p**(e-e_ba)]]or[[c%p**(e-e_ba) == b%p**(e-e_ba)][c//p**(e-e_ba) =!= b//p**(e-e_ba)]]]
                    [len {c<{a,b}>|...[[c=!=b][c=!=a]]} == 2*(p**(e-(e-e_ba))-1) == 2*(p**e_ba-1)]
                    [len ({a,b} \-/ {c<{a,b}>|...[[c=!=b][c=!=a]]}) == 2 + 2*(p**e_ba-1) == 2*p**e_ba]
                #####
                [len ({a,b} \-/ {c<{a,b}>|...[[c=!=b][c=!=a]]}) == if e_ba >= eh then p**(e-eh) else 2*p**e_ba]
                !![is_square_residual_mod(p**e;N)]
                :?[d<-[0..p**e//2]] -> [[d%p=!=0][{d,p**e-d} == {z <- [0..<p**e] | [z**2%p**e==N]}]]
                [dn := p**e-d]
                [ds := {d,dn}]
                [e_ba < eh] <==> [ds /-\ ({a,b} \-/ {c<{a,b}>|...[[c=!=b][c=!=a]]}) == {}]
            ]]

            [abs_ex_(p**e;N) =[def]= {(a,b) | [a:<-[0..<p**e]][a%p=!=0][b:=N*inv_mod_(p**e;a)%p**e]}]
            [len_abs_ex_(p**e;N) =[def]= len abs_ex_(p**e;N)]

            !!abs_ex_(p**e;N)定义中a的取值 a<->b
            [len_abs_ex_(p**e;N) == phi(p**e)]
            !![p**e%2==1]
            # (x,y) <-> (a,b)
            #   前面c用于表达 x 一对多 a
            #   但(x,y)与(a,b)是一一对应的！！
            [len_xys_ex_(p**e;N) == len_abs_ex_(p**e;N) == phi(p**e) == phi(2*p**e)]
                #猜想-特例证明: %奇素数幂

            !![[(c-a)%p**e =!= 0][(c-b)%p**e =!= 0]] ==>> [is_square_residual_mod(p;N)]
            * [not$ is_square_residual_mod(p;N)]:
                # [not$ [(c-a)%p**e =!= 0][(c-b)%p**e =!= 0]]
                # [[(c-a)%p**e == 0]or[(c-b)%p**e == 0]]
                [len_xys_ex_(p**e;N) == len_abs_ex_(p**e;N) == phi(p**e)]
            * [is_square_residual_mod(p;N)]:
                !![e_ba < eh] <==> [ds /-\ ({a,b} \-/ {c<{a,b}>|...[[c=!=b][c=!=a]]}) == {}]
                [len_abs_ex_(p**e;N)
                    == (p-1-(len ds<p**1;N>))*p**(e-1) + (len ds<p**eh;N>)*p**(e-eh) + sum (len ds<p**e_ba;N>)*(p-1)*p**(e-1-e_ba)///(2*p**e_ba) *(2*p**e_ba) {e_ba <-[1..<eh]}
                    == (p-3)*p**(e-1) + 2*p**(e-eh) + sum 2*(p-1)*p**(e-1-e_ba) {e_ba <-[1..<eh]}
                    == (p-3)*p**(e-1) + 2*p**(e-eh) + 2*(p-1)*p**(e-eh)*sum p**(eh-1-e_ba) {e_ba <-[1..<eh]}
                    # [k:=(eh-1-e_ba)]
                    == (p-3)*p**(e-1) + 2*p**(e-eh) + 2*(p-1)*p**(e-eh)*sum p**k {k <-[0..<eh-1]}
                    == 2*p**(e-eh) + 2*(p-1)*p**(e-eh)*(p**(eh-1) -1)///(p-1)
                    == (p-3)*p**(e-1) + 2*p**(e-1)
                    == (p-1)*p**(e-1)
                    == phi(2*p**e)
                    ]

            [xxs_ex_(p**e;N) =[def]= {x**2%p**e | [(x,y) :<- xys_ex_(p**e;N)]}]
            [yys_ex_(p**e;N) =[def]= {y**2%p**e | [(x,y) :<- xys_ex_(p**e;N)]}]
            [len_xxs_ex_(p**e;N) =[def]= len xxs_ex_(p**e;N)]
            [len_yys_ex_(p**e;N) =[def]= len yys_ex_(p**e;N)]
            [[
            #is_square_residual_mod
            !![is_prime p][p%2==1]
            !![N%p =!= 0]这里是关键
            !![e>=1]
            [is_square_residual_mod(p**e;N)
            == is_square_residual_mod(p;N)
            == [Jacobi_symbol(p;N)==+1]
            ]
            [[bug:
            #len_xs_ex_/len_xxs_ex_版本的等式错了
            @[k::int]:
                [is_square_residual_mod(p**e;x+k*p) == is_square_residual_mod(p;x%p)]
                    bug:缺了条件[x%p=!=0]
                [is_square_residual_mod(p**e;(x+k*p)**2-N) == is_square_residual_mod(p;(x**2-N)%p)]
                    bug:缺了条件[(x**2-N)%p=!=0]
                [[x<-xs_(p;N)] -> [(x+k*p)%p**e<-xs_ex_(p**e;N)]]
                [len_xs_ex_(p**e;N) == len_xs_(p;N)*p**(e-1)]
                #No:[len_xxs_ex_(p**e;N) == (len_xs_ex_(p**e;N)+1)//2]
                    # +(x+k*p),-(x+k*p); 0; +k_*p**e_,-k_*p**e_
                    # [gcd(p**e,x+k*p)=!=1]==>>[x==0][(x+k*p == k_*p**e_][[k_%p=!=0][1<=e_<e]or[k_==0][e_==+oo]]
                [is_square_residual_mod(p**e;(x**2+k*p)) == is_square_residual_mod(p;(x**2)%p)]
                [is_square_residual_mod(p**e;(x**2+k*p)-N) == is_square_residual_mod(p;(x**2-N)%p)]
                [[xx<-xxs_(p;N)] -> [(xx+k*p)%p**e<-xxs_ex_(p**e;N)]]
                [len_xxs_ex_(p**e;N) == len_xxs_(p;N)*p**(e-1)]

            !![len_xs_(p;+N) == (p+Jacobi_symbol(p;+N))///2]
            !![len_xs_ex_(p**e;N) == len_xs_(p;N)*p**(e-1)]
            !![len_xxs_(p;+N) == ((p+Jacobi_symbol(p;+N))///2+1)//2]
            !![len_xxs_ex_(p**e;N) == len_xxs_(p;N)*p**(e-1)]
            [len_xs_ex_(p**e;N) == (p+Jacobi_symbol(p;+N))///2 *p**(e-1)]
            [len_xxs_ex_(p**e;N) == ((p+Jacobi_symbol(p;+N))///2+1)//2 *p**(e-1)]
                #〖上下对比囗似乎有毛病〗
            :bug]]
            ]]

        ]]

        [g := gcd(c-a,M)]
        [ca_g := (c-a)///g]
        [M_g := M///g]
        [gcd(ca_g,M_g)==1]

        [(a*c-N)*ca_g*g %(M_g*g) == 0]
        [(a*c-N)*ca_g %M_g == 0]
        [(a*c-N) %M_g == 0]
        [a*c =[%M_g]= N]

        !![a*inv_a %M ==1]
        [a*inv_a %M_g == 1%M_g] # M_g may be 1
        [inv_a*a*c =[%M_g]= inv_a*N]
        [c =[%M_g]= inv_a*N]
        [c0 := inv_a*N %M_g]
        [c <- {c0+k*M_g | [k <- [0..<g]]}]
        [k <- [0..<g]][c == c0+k*M_g]:
            !![g := gcd(c-a,M)]
            !![c0 := inv_a*N %M_g]
            !![M_g := M///g]
            [g == gcd(c-a,M)
                == gcd(c0+k*M_g-a,M)
                == gcd(inv_a*N %M_g + k*M_g -a,M_g*g)
                ]
]]


view others/数学/二次互反律.txt
    is_square_residual_mod
        平方剩余判定整体算法

[[
@[M,N::int][M =!= 0][gcd(M,N)==1]:
    [num_solutions_of_square_diff_mod(M;N) =[def]= len{(x,y) | [x,y:<- [0..<abs(M)]][(x**2-y**2-N) %M ==0]}]
    #####
    [num_part1_square_of_solutions_of_square_diff_mod(M;N) =[def]= len{x**2%M | [x,y:<- [0..<abs(M)]][(x**2-y**2-N) %M ==0]}]
        #比num_part1_of_solutions_of_square_diff_mod(M;N)少一半(p==2时剩1/4)，再少[x**2=[%M]=z][gcd(z,M)=!=1]的根(每组根计一)
    [num_part2_square_of_solutions_of_square_diff_mod(M;N) =[def]= len{y**2%M | [x,y:<- [0..<abs(M)]][(x**2-y**2-N) %M ==0]}]
    #####
    [num_part1_of_solutions_of_square_diff_mod(M;N) =[def]= len{x | [x,y:<- [0..<abs(M)]][(x**2-y**2-N) %M ==0]}]
    [num_part2_of_solutions_of_square_diff_mod(M;N) =[def]= len{y | [x,y:<- [0..<abs(M)]][(x**2-y**2-N) %M ==0]}]
    #####
    [num_solutions_of_square_diff_mod(M;+N) == num_solutions_of_square_diff_mod(M;-N)]
    [num_part2_square_of_solutions_of_square_diff_mod(M;+N) == num_part1_square_of_solutions_of_square_diff_mod(M;-N)]
    [num_part2_of_solutions_of_square_diff_mod(M;+N) == num_part1_of_solutions_of_square_diff_mod(M;-N)]
        #搜索x还是y？哪个更少？
        # [ceil_sqrt(N) <= x <= (N+1)//2]
        # [0 <= y <= (N-1)//2]
        # 差不多...都是O(N)，x更少
    #####
    # odd_prime:[sz_xx == sz_yy == (sz_x + sz_y - sz_xy///2)///2]
    # even_prime:[sz_xx == sz_yy == (sz_x + sz_y - sz_xy///4)///4]
    [@[p,e,N::int] -> [[is_prime p][p%2==1][e>=1][N%p =!= 0]] -> [num_part1_square_of_solutions_of_square_diff_mod(p**e;+N) == num_part1_square_of_solutions_of_square_diff_mod(p**e;-N) == (num_part1_of_solutions_of_square_diff_mod(p**e;+N) + num_part1_of_solutions_of_square_diff_mod(p**e;-N) - num_solutions_of_square_diff_mod(p**e;N)///2)///2]]
    [@[e,N::int] -> [[e>=3][N%2==1]] -> [num_part1_square_of_solutions_of_square_diff_mod(2**e;+N) == num_part1_square_of_solutions_of_square_diff_mod(2**e;-N) == (num_part1_of_solutions_of_square_diff_mod(2**e;+N) + num_part1_of_solutions_of_square_diff_mod(2**e;-N) - num_solutions_of_square_diff_mod(2**e;N)///4)///4]]
    #####
    [[
    @[x,y::int][(x**2-y**2)==N>0][x>y>=0]:
        # y增 <==> x增 <==> (x+y)增 <==> (x-y)减
        # min (x-y) <==> max y <==> max x
        [d := x-y]
        [x == y+d]
        !![x>y]
        [d >= 1]
        [N == x**2-y**2 == (y+d)**2-y**2 == 2*y*d + d**2]
        [y == (N-d**2)///(2*d) <= (N-1**2)/(2*1) == (N-1)/2]
        [0 <= y <= (N-1)//2]
        [h := (N-1)//2]
        [0 <= y <= h]
        [N == 2*h+2-N%2]
        [x**2 == N+y**2 <= N+h**2 == 2*h+2-N%2 + h**2 == (h+1)**2 + 1-N%2 <= (h+1)**2 + 1]
        [x <= floor_sqrt((h+1)**2 + 1) == h+1 = (N+1)//2]
        [x**2 == N+y**2 >= N]
        [x >= ceil_sqrt(N)]
        [ceil_sqrt(N) <= x <= (N+1)//2]
        [0 <= y <= (N-1)//2]

        [u := h+1-x]
        [v := h-y]
        [x == h+1-u]
        [y == h-v]
        [0 <= u <= h+1-ceil_sqrt(N)]
        [0 <= v <= h]
        [x**2-y**2==(x-y)*(x+y)
            ==(1+v-u)*(2*h+1-u-v)
            ==(1-(u-v))*((2*h+1)-(u+v))
            ==(2*h+1) -(2*h+1)*(u-v) -(u+v) +(u+v)*(u-v)
            ==(2*h+1) -2*(h+1)*u +2*h*v +(u**2-v**2)
            !![N == 2*h+2-N%2]
            ==((N+N%2-2)+1) -((N+N%2-2)+2)*u +(N+N%2-2)*v +(u**2-v**2)
            ==(N+N%2-1) -(N+N%2)*u +(N+N%2-2)*v +(u**2-v**2)
            ]
        [0 == x**2-y**2-N ==(N%2-1) -(N+N%2)*u +(N+N%2-2)*v +(u**2-v**2)]
    ]]
    #####
]]



TODO:
    ===
    证明:[@[M,N::int] -> [M > 0] -> [gcd(M,N)==1] -> [len{(x,y) | [x,y:<- [0..<M]][(x**2-y**2-N) %M ==0]} == phi(2*M)]]
        证明:[@[M,N::int] -> [M > 0] -> [gcd(M,N)==1] -> [num_solutions_of_square_diff_mod(M;N) == phi(2*M)]]

    ===
    求num_part1_of_solutions_of_square_diff_mod(M;N)
    ===
    ===
    ===

证明:[@[M,N::int] -> [M > 0] -> [gcd(M,N)==1] -> [num_solutions_of_square_diff_mod(M;N) == phi(2*M)]]
[[[
@[p,e,N,x,y,a,b::int][is_prime p][p%2==1][e>=1][N%p=!=0][x**2-y**2 =[%p**e]= N][a==(x+y)%p**e][b==(x-y)%p**e][x,y,a,b <- [0..<p**e]]:
见上面: 猜想-特例证明: %奇素数幂
    [proof:其实很简单 [x+y=[%p**e]=a][x-y=[%p**e]=b] ==>> [a*b=[%p**e]=N][a%p=!=0] ==>> [b==N*inv_mod_(p**e;a)]
        (x,y)与(a,b)一一对应
        (a,b)与a一一对应
        a的数量是phi(p**e)
    ]

[[
@[p,e,N,x,y,a,b::int][p==2][e>=1][N%2==1][x**2-y**2 =[%2**e]= N][a==(x+y)%2**e][b==(x-y)%2**e][x,y,a,b <- [0..<2**e]]:
    [N =[%2**e]= x**2-y**2 =[%2**e]= (x+y)*(x-y) =[%2**e]= a*b]
    !![N%2==1]
    [a%2==1]
    [b%2==1]
    !![a==(x+y)%2**e]
    [(x+y)%2 == a%2 == 1]
    [x%2 == 1-y%2]
    [x%2 =!= y%2]

    [a+b =[%2**e]= (x+y)+(x-y) == 2*x]
    [(a+b)///2 =[%2**(e-1)]= x]
    [u := x%2**e //2**(e-1)]
    [x == u*2**(e-1) + (a+b)///2 %2**(e-1)]

    [a-b =[%2**e]= (x+y)-(x-y) == 2*y]
    [(a-b)///2 =[%2**(e-1)]= y]
    [v := y%2**e //2**(e-1)]
    [y == v*2**(e-1) + (a-b)///2 %2**(e-1)]

    [[无用:
    !![N =[%2**e]= a*b]
    !![a%2 ==1]
    [b == N*inv_mod_(2**e;a)%2**e]
    @[c <- [0..<2**e]][c%2==1][c+N*inv_mod_(2**e;c) =[%2**e]= a+N*inv_mod_(2**e;a)]:
        [a*c*(c+N*inv_mod_(2**e;c)) =[%2**e]= a*c*(a+N*inv_mod_(2**e;a))]
        [a*c*c+a*N =[%2**e]= a*c*a+c*N]
        [a*c*(c-a) =[%2**e]= (c-a)*N]
        [(a*c-N)*(c-a) =[%2**e]= 0]
        #没用！关键是(x,y)与(a,b)的对应关系
    ]]

    @[c,d <- [0..<2**e]][c%2==1][d%2==1][c+d =[%2**e]= a+b][c-d =[%2**e]= a-b]:
        [(c+d)+(c-d) =[%2**e]= (a+b)+(a-b)]
        [2*c =[%2**e]= 2*a]
        [c =[%2**(e-1)]= a]
        [d =[%2**e]= a+b-c]
        # 一(x,y)对应2对(a,b)



    * [e>=2]:
        [((a+b)///2 %2**(e-1))**2 - ((a-b)///2 %2**(e-1))**2
            == (x-u*2**(e-1))**2 - (y-v*2**(e-1))**2
            == (x**2-y**2) - (u*x-v*y)*2**e + (u**2-v**2)*2**(2*e-2)
            !! [e>=2]:
            =[%2**e]= (x**2-y**2)
            =[%2**e]= N
            ]
        [((a+b)///2 %2**(e-1),(a-b)///2 %2**(e-1)) <- xys_ex_(2**e;N)]
        @[u,v <- {0,1}]:
            [(u*2**(e-1)+(a+b)///2 %2**(e-1),v*2**(e-1)+(a-b)///2 %2**(e-1)) <- xys_ex_(2**e;N)]
            # 一(a,b)对应4对(x,y)
        # 一(a,b)对应4对(x,y)
        # 一(x,y)对应2对(a,b)
        [len_xys_ex_(2**e;N) == len_abs_ex_(2**e;N)///2 *4 == phi(2**e)///2 *4 == 2**e == phi(2*2**e)]
        # 2**2: N=1: {(xx,yy)}=={(1,0)}, xys=={(1,0),(3,0),(1,2),(3,2)}, abs=={(1,1),(3,3)}
    * [e==1]:
        !![N%2==1]
        [N%2**e ==1]
        * [N%2**e ==0]:
            [xys_ex_(2**e;N) == {(0,0),(1,1)}]
        * [N%2**e ==1]:
            [xys_ex_(2**e;N) == {(0,1),(1,0)}]
        [len_xys_ex_(2**e;N) == 2 == 2**e == phi(2*2**e)]
    [len_xys_ex_(2**e;N) == phi(2*2**e)]
        #猜想-特例证明: %偶素数幂
]]


@[M,N::int][M==1]:
    [N%M==0]
    [gcd(M,N)==gcd(M,N%M)==gcd(M,0)==1]
    @[x,y::int][x,y <- [0..<M]]:
        [x==y==0]
        [0**2-0**2==0]
        [x**2-y**2 =[%M]= N]
    [num_solutions_of_square_diff_mod(M;N) == len{(0,0)} == 1 == phi(2) == phi(2*M)]

证明:[@[M,N::int] -> [M > 0] -> [gcd(M,N)==1] -> [num_solutions_of_square_diff_mod(M;N) == phi(2*M)]]
    proof:由 中国剩余定理 组合 上面特例(%奇素数幂，%偶素数幂) 可得证
]]]



[[[[
求num_part1_of_solutions_of_square_diff_mod(M;N)
[[bug: 见下面p**e与2**e，替代M
[M =!= 0][gcd(M,N)==1][(x**2-y**2-N)%M==0]:
    [np := len(all_prime_factors_of(M))]
    [mt := if M%2==1 then 2**np else if M%4==2 then 2**(np-1) else if M%8==4 then 2**np else 2**(np+1)]
    [(z**2-1)%M==0]的z的解的数量为mt
        # 6:1,5
        # 12:1,5,7,11
        # 24:1,5,7,11,13,17,19,23
    @a.[gcd(a,M)==1]:
        [(z**2-a)%M==0]的z的解的数量为0或mt
    [sz_xy := num_solutions_of_square_diff_mod(M;N)]
    [sz_x := num_part1_of_solutions_of_square_diff_mod(M;N)]

    ???若[gcd(y,M) > 1]即[gcd(x**2-N,M) > 1]??? #而非[y==0]
        y<x>的数量 不是 mt
    太难，还是看特例:[M==p**e]
]]



[[
求num_part1_of_solutions_of_square_diff_mod(p**e;N)
    求num_part2_of_solutions_of_square_diff_mod(p**e;N)
    求num_part1_square_of_solutions_of_square_diff_mod(p**e;N)
[is_prime p][p%2==1][e>=1][N%p =!= 0][(x**2-y**2-N)%p**e==0]:
    !![N%p =!= 0]
    [is_square_residual_mod(p**e;N)
        == is_square_residual_mod(p;N)
        == [Jacobi_symbol(p;N)==+1]
        ]
    [is_square_residual_mod(p**e;-1)
        == [Jacobi_symbol(p;-1)==+1]
        == [p%4==1]
        ]
    [is_square_residual_mod(p**e;-N)
        == [Jacobi_symbol(p;-1)*Jacobi_symbol(p;N)==+1]
        == [[p%4==1] == [Jacobi_symbol(p;N)==+1]]
        ]

    [@[z0<-[1..<p**e]] -> [z0%p=!=0] -> [len{z<-[0..<p**e] | [(z**2-z0**2)%p**e==0]} == 2]]
    [@[z0<-[1..<p**e]] -> [z0%p=!=0] -> [+z0 =![%p**e]!= -z0]]

    [@[z0<-[0..<p**e]] -> [ez0:=max_power_of_base_as_factor_of_(p,z0)] -> [len{z<-[0..<p**e] | [(z**2-z0**2)%p**e==0]} == num_sqrts_mod_odd_prime_power(p,e,ez0)]]
    [num_sqrts_mod_odd_prime_power(p,e,ez0) =[def]= (if 2*ez0 >= e then p**(e//2) else 2*p**ez0)]
        # [2*ez0 >= e] <==> [ez0 >= (e+1)//2]

    [ex := max_power_of_base_as_factor_of_(p,x)]
    [ey := max_power_of_base_as_factor_of_(p,y)]
    * [ex=!=0][ey=!=0]:
        [N%p==(x**2-y**2)%p=0]
        !![N%p =!= 0]
        _L
    * [ex==0][ey=!=0]:
        [x**2 =[%p**e]= N+y**2]
        [is_square_residual_mod(p**e;N+y**2)]
        [Jacobi_symbol(p;N)==+1]
        #解结构:{+x,-x} *** {z | [z**2 =[%p**e]= y**2]}
        #解数量: [Jacobi_symbol(p;N)==+1]*2*num_sqrts_mod_odd_prime_power(p,e,ey)
        #   2==num_sqrts_mod_odd_prime_power(p,e,ex)
    * [ex=!=0][ey==0]:
        [y**2 =[%p**e]= -N+x**2]
        [is_square_residual_mod(p**e;-N+x**2)]
        [Jacobi_symbol(p;-N)==+1]
        [[p%4==1] == [Jacobi_symbol(p;N)==+1]]
        #解结构:{z | [z**2 =[%p**e]= x**2]} *** {+y,-y}
        #解数量: [[p%4==1] == [Jacobi_symbol(p;N)==+1]]*2*num_sqrts_mod_odd_prime_power(p,e,ex)
        #   2==num_sqrts_mod_odd_prime_power(p,e,ey)
    * [ex==0][ey==0]:
        #解结构: {+x,-x} *** {+y,-y}
        #解数量: 2*2 == 4
        #   2==num_sqrts_mod_odd_prime_power(p,e,ex)==num_sqrts_mod_odd_prime_power(p,e,ey)


    # 可能有复杂的[x*y%p==0]而不止[[x%p**e==0]or[y%p**e==0]]

    #####
    [sz_xy := num_solutions_of_square_diff_mod(p**e;N)]
        # 猜想已被证明[sz_xy==phi(2*p**e) == phi(p**e)]
    [sz_x := num_part1_of_solutions_of_square_diff_mod(p**e;N)]
    [sz_x == let sp := [is_square_residual_mod(p**e;+N)] in
        #bug:ey 不得超过(e+1)//2
        #   所有ey<-[(e+1)//2..<e]++[+oo] 生成同一组解 即 [y**2==0]，不得拆成多个ey
        #[ey==0]时 总是{+y,-y}，无需特殊处理
        #bug:没有 考虑 组数
        #bug:(sz_xy -sp*sum 2*num_sqrts_mod_odd_prime_power(p,e,ey) {ey<-[1..<e]++[+oo]} -t*sum 2*num_sqrts_mod_odd_prime_power(p,e,ex) {ex<-[1..<e]++[+oo]})///2 + sp*sum 2 {ey<-[1..<e]++[+oo]} +t*sum num_sqrts_mod_odd_prime_power(p,e,ex) {ex<-[1..<e]++[+oo]}
        #####
        (sz_xy -sp*sum 2*num_sqrts_mod_odd_prime_power(p,e,ey) *(phi(p**(e-ey))///num_sqrts_mod_odd_prime_power(p,e,ey)) {ey<-[1..<(e+1)//2]} -sp*sum 2*num_sqrts_mod_odd_prime_power(p,e,ey)*1 {ey<-[(e+1)//2]})///2 + sp*sum 2*(phi(p**(e-ey))///num_sqrts_mod_odd_prime_power(p,e,ey)) {ey<-[1..<(e+1)//2]} + sp*sum 2*1 {ey<-[(e+1)//2]}
        == sz_xy///2 -sp*sum phi(p**(e-ey)) {ey<-[1..<(e+1)//2]} -sp*p**(e//2) + sp*sum 2*(phi(p**(e-ey))///num_sqrts_mod_odd_prime_power(p,e,ey)) {ey<-[1..<(e+1)//2]} + sp*2
        #####见下面:部分-过程
        == sz_xy///2 -sp*p**(e//2) + sp*2 -sp*p**(e//2)*(p**((e-1)//2)-1) + sp*p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1)
        == sz_xy///2 + sp*2 -sp*p**(e//2)*(p**((e-1)//2)) + sp*p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1)
        == sz_xy///2 + sp*2 -sp*p**(e-1) + sp*p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1)
        == sz_xy///2 - sp*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
        [[
        #####部分:
        [sum phi(p**(e-ey)) {ey<-[1..<(e+1)//2]}
        ==p**(e//2)*(p**((e-1)//2)-1)
        ]
        [sum 2*(phi(p**(e-ey))///num_sqrts_mod_odd_prime_power(p,e,ey)) {ey<-[1..<(e+1)//2]}
        ==p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1)
        ]
        #####过程:
        [sum phi(p**(e-ey)) {ey<-[1..<(e+1)//2]}
        ==(p-1)*sum p**(e-1-ey) {ey<-[1..<(e+1)//2]}
        ==(p-1)*sum p**(e-(e+1)//2+(e+1)//2-1-ey) {ey<-[1..<(e+1)//2]}
        ==(p-1)*p**(e-(e+1)//2)*sum p**((e+1)//2-1-ey) {ey<-[1..<(e+1)//2]}
        ==(p-1)*p**(e-(e+1)//2)*sum p**(ey-1) {ey<-[1..<(e+1)//2]}
        ==(p-1)*p**(e-(e+1)//2)*sum p**ey {ey<-[0..<(e-1)//2]}
        ==(p-1)*p**(e-(e+1)//2)*(p**((e-1)//2)-1)//(p-1)
        ==p**(e-(e+1)//2)*(p**((e-1)//2)-1)
        ==p**(e//2)*(p**((e-1)//2)-1)
        ]
        [sum 2*(phi(p**(e-ey))///num_sqrts_mod_odd_prime_power(p,e,ey)) {ey<-[1..<(e+1)//2]}
        ==sum 2*(phi(p**(e-ey))///(2*p**ey)) {ey<-[1..<(e+1)//2]}
        ==sum 2*((p-1)*p**(e-ey-1)///(2*p**ey)) {ey<-[1..<(e+1)//2]}
        ==(p-1)*sum p**(e-2*ey-1) {ey<-[1..<(e+1)//2]}
        # [z:=(e-2*ey-1) >= e-2*((e+1)//2-1)-1 == e+1-(e+1)//2*2 == (e+1)%2]
        ==(p-1)*sum p**z {z<-[(e+1)%2,(e+1)%2+2..<e-2]}
        ==(p-1)*p**((e+1)%2)*sum p**k {k<-[0,2..<e-2-(e+1)%2]}
        ==(p-1)*p**(1-e%2)*sum p**k {k<-[0,2..<e-2-(1-e%2)]}
        ==(p-1)*p**(1-e%2)*sum p**k {k<-[0,2..<e+e%2-3]}
        ==(p-1)*p**(1-e%2)*sum p**k {k<-[0,2..<e+e%2-3+1]} #步长为2，结尾凑成偶数
        # [i:=k///2]
        ==(p-1)*p**(1-e%2)*sum (p**2)**i {i<-[0,1..<(e+e%2-2)///2]}
        ==(p-1)*p**(1-e%2)*(p**((e+e%2-2)///2 *2)-1)///(p**2-1)
        ==p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1)
        ]
        ]]
        == sz_xy///2 - [Jacobi_symbol(p;N)==+1]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
        =[猜想已被证明]= p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
            #？大约phi(p**e)一半？
        =[简化]= p**(e-1)*(p-1)///2 -sp*((p**e -(1+e%2)*p-(2-e%2))///(p+1))
        =[简化补充]= [e==0]*1 + [e>=1]*(p**(e-1)*(p-1)///2 -sp*((p**e -(1+e%2)*p-(2-e%2))///(p+1)))
    ]

    [sz_y := num_part2_of_solutions_of_square_diff_mod(p**e;N)]
    !![num_part2_of_solutions_of_square_diff_mod(M;N) == num_part1_of_solutions_of_square_diff_mod(M;-N)]
    [sz_y == num_part2_of_solutions_of_square_diff_mod(p**e;-N)
        == sz_xy///2 - [Jacobi_symbol(p;-N)==+1]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
        == sz_xy///2 - [[p%4==1]==[Jacobi_symbol(p;N)==+1]]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
        =[猜想已被证明]= p**(e-1)*(p-1)///2 -[[p%4==1]==[Jacobi_symbol(p;N)==+1]]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
        =[简化]= p**(e-1)*(p-1)///2 -[sp==p41]*((p**e -(1+e%2)*p-(2-e%2))///(p+1))
          where:
            [sp := [Jacobi_symbol(p;N)==+1]]
            [p41 := [p%4==1]]
        =[简化补充]= [e==0]*1 + [e>=1]*(p**(e-1)*(p-1)///2 -[sp==p41]*((p**e -(1+e%2)*p-(2-e%2))///(p+1)))
    ]

    [sz_xx := num_part1_square_of_solutions_of_square_diff_mod(p**e;N)]
    [sz_xx == let[
        #[sp := [is_square_residual_mod(p**e;+N)]]
        #[sn := [is_square_residual_mod(p**e;-N)]]
        [sp := [Jacobi_symbol(p;N)==+1]]
        [sn := [Jacobi_symbol(p;N)==+1]]
        [p41 := [p%4==1]]
        #[sn == [sp==p41]]
        [jpN := Jacobi_symbol(p;N)]
        #[jpN == (2*sp-1)]
        ]in
        (sz_xy -sp*sum 2*num_sqrts_mod_odd_prime_power(p,e,ey) *(phi(p**(e-ey))///num_sqrts_mod_odd_prime_power(p,e,ey)) {ey<-[1..<(e+1)//2]} -sp*sum 2*num_sqrts_mod_odd_prime_power(p,e,ey)*1 {ey<-[(e+1)//2]} -sn*sum 2*num_sqrts_mod_odd_prime_power(p,e,ex) *(phi(p**(e-ex))///num_sqrts_mod_odd_prime_power(p,e,ex)) {ex<-[1..<(e+1)//2]} -sn*sum 2*num_sqrts_mod_odd_prime_power(p,e,ex)*1 {ex<-[(e+1)//2]})///4 + sp*sum (phi(p**(e-ey))///num_sqrts_mod_odd_prime_power(p,e,ey)) {ey<-[1..<(e+1)//2]} + sp*sum 1 {ey<-[(e+1)//2]} + sn*sum (phi(p**(e-ex))///num_sqrts_mod_odd_prime_power(p,e,ex)) {ex<-[1..<(e+1)//2]} + sn*sum 1 {ex<-[(e+1)//2]}
        == sz_x/2 + sz_y/2 - sz_xy/4
        == (sz_x + sz_y - sz_xy///2)///2
        == ((sz_xy///2 - sp*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)) + (sz_xy///2 - sn*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)) - sz_xy///2)///2
        == (sz_xy///2 - (sp+sn)*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2))///2
        =[猜想已被证明]= (p**(e-1)*(p-1)///2 - ([Jacobi_symbol(p;+N)]+[Jacobi_symbol(p;-N)])*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2))///2
        =[简化]= (p**(e-1)*(p-1)///2 - (sp+[sp==p41])*((p**e -(1+e%2)*p-(2-e%2))///(p+1)))///2
        # ([Jacobi_symbol(p;+N)]+[Jacobi_symbol(p;-N)])
        # == ([Jacobi_symbol(p;+N)]+[[Jacobi_symbol(p;+N)]==[p%4==1]])
        # (1,1) --> 2
        # (0,0) --> 1
        # (1,0) --> 1
        # (0,1) --> 0
        # sp*u+p41*v+w==?
        # 1*u+1*v+w==2
        # 0*u+0*v+w==1 ==>> [w==1]
        # 1*u+0*v+w==1 ==>> [u==0]
        # 0*u+1*v+w==0 ==>> [v==-1]
        # sp*0+p41*(-1)+1==?
        # 1*u+1*v+w==1*0+1*(-1)+1==0=!=2
        #   线性方程组无解
        #####
        [(sp+[sp==p41])
        == (sp+(sp+p41+1)%2)
        == (2*sp*p41 + 1-p41)
        == ((2*sp-1)*p41 + 1)
        == (jpN*p41 + 1)
        ]
        #####
        =[简化]= (p**(e-1)*(p-1)///2 - (jpN*p41 + 1)*((p**e -(1+e%2)*p-(2-e%2))///(p+1)))///2
        =[简化补充]= [e==0]*1 + [e>=1]*((p**(e-1)*(p-1)///2 - (jpN*p41 + 1)*((p**e -(1+e%2)*p-(2-e%2))///(p+1)))///2)
    ]
    [[debug:
        结果:最后发现是len_xs_ex_/len_xxs_ex_版本的等式错了
    =======
    但！见上面:〖上下对比囗似乎有毛病〗:
        [len_xs_ex_(p**e;N) == (p+Jacobi_symbol(p;+N))///2 *p**(e-1)]
        [len_xxs_ex_(p**e;N) == ((p+Jacobi_symbol(p;+N))///2+1)//2 *p**(e-1)]
        [sz_x<p**e;N> == p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)]
        [sz_xx<p**e;N> == (p**(e-1)*(p-1)///2 - ([Jacobi_symbol(p;+N)]+[Jacobi_symbol(p;-N)])*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2))///2]
    应有:
        # sz_x == len_xs_ex_
        [sz_x<p**e;N> == len_xs_ex_(p**e;N)]

        # sz_xx == len_xxs_ex_
        [sz_xx<p**e;N> == len_xxs_ex_(p**e;N)]

    * [e==1]:[
        # sz_x == len_xs_ex_
        [len_xs_ex_(p**e;N) == (p+Jacobi_symbol(p;+N))///2]
        [sz_x<p**e;N> == (p-1)///2 -[Jacobi_symbol(p;N)==+1]*(-1)
            == (p-1+2*[Jacobi_symbol(p;N)==+1])///2
            == if [Jacobi_symbol(p;N)==+1] then (p+1)///2 else (p-1+2*0)///2
            == (p+Jacobi_symbol(p;+N))///2
            == len_xs_ex_(p**e;N)
        ]
        # sz_xx == len_xxs_ex_
        [sp := [Jacobi_symbol(p;+N)]]
        [p41 := [p%4==1]]
        [len_xxs_ex_(p**e;N) == ((p+Jacobi_symbol(p;+N))///2+1)//2
            == ((p+2*sp-1)///2+1)//2
            == ((p-1)///2+sp+1)//2
            * [sp==0][p==4*k+1]:
                ... == (2k+0+1)//2 == k
            * [sp==0][p==4*k+3]:
                ... == (2k+1 +0+1)//2 == k+1
            * [sp==1][p==4*k+1]:
                ... == (2k+1+1)//2 == k+1
            * [sp==1][p==4*k+3]:
                ... == (2k+1 +1+1)//2 == k+1
            == p//2 + 1-(1-sp)*p41
        ]
        [sz_xx<p**e;N> == ((p-1)///2 - ([Jacobi_symbol(p;+N)]+[Jacobi_symbol(p;-N)])*(-1))///2
            == ((p-1)///2 + ([Jacobi_symbol(p;+N)]+[[Jacobi_symbol(p;+N)]==[p%4==1]]))///2
            == ((p-1)///2 + (sp+[sp==p41]))///2
            * [sp==0][p==4*k+1]:
                ... == (2*k + 0)///2 == k
            * [sp==0][p==4*k+3]:
                ... == (2*k+1 + 1)///2 == k+1
            * [sp==1][p==4*k+1]:
                ... == (2*k + 2)///2 == k+1
            * [sp==1][p==4*k+3]:
                ... == (2*k+1 + 1)///2 == k+1
            == p//2 + 1-(1-sp)*p41
            == len_xxs_ex_(p**e;N)
        ]
    ]
    * [e>=1]:[
        # sz_x == len_xs_ex_
        [len_xs_ex_(p**e;N) == (p+Jacobi_symbol(p;+N))///2 *p**(e-1)]
        [len_xs_ex_(p**(e+1);N) == p*len_xs_ex_(p**e;N)]
            #翻p倍
        [sz_x<p**e;N> == p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
            == p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*(p**(e-1) - (p**(e-1)-p**(1-e%2))///(p+1) -2)
            == p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*((p**e+p**(e-1) - p**(e-1)+p**(1-e%2))///(p+1) -2)
            == p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*((p**e+p**(1-e%2))///(p+1) -2)
            [[
            * [e==2*k]:
                [(p**e+p**(1-e%2))
                == (p**(2*k)+p)
                == p*(p**(2*k-1)+1)
                ]
            * [e==2*k+1]:
                [(p**e+p**(1-e%2))
                == (p**(2*k+1)+1)
                ]
            * [e==2*(k+1)]:
                [(p**e+p**(1-e%2))
                == p*(p**(2*(k+1)-1)+1)
                == p*(p**(2*k+1)+1)
                #没能 翻p倍，因为 外面带个尾巴『-2』
                # 『-2*p-2』
                # 真的对不上！！
                最后发现是len_xs_ex_/len_xxs_ex_版本的等式错了

                ]
            ]]
        ]

    ]
    :debug]]
    [[分支简化:
    简化下面两式:
        [sz_x<p**e;N> == p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)]
        [sz_xx<p**e;N> == (p**(e-1)*(p-1)///2 - ([Jacobi_symbol(p;+N)]+[Jacobi_symbol(p;-N)])*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2))///2]

    [sp := [Jacobi_symbol(p;N)==+1]]
    [sn := [Jacobi_symbol(p;N)==+1]]
    [p41 := [p%4==1]]
    [jpN := Jacobi_symbol(p;N)]

    [sn == [sp==p41]]
    [jpN == (2*sp-1)]

    [sz_x<p**e;N> == p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
        == p**(e-1)*(p-1)///2 -sp*(p**(e-1) - (p**(e-1)-p**(1-e%2))///(p+1) -2)
        == p**(e-1)*(p-1)///2 -sp*((p**e+p**(1-e%2))///(p+1) -2)
        == p**(e-1)*(p-1)///2 -sp*((p**e+p**(1-e%2) -2*p-2)///(p+1))
        ###
            [(p**e+p**(1-e%2) -2*p-2) ==:
            * [e==2*i+1]:
                ... == (p**e+p**0 -2*p-2) == (p**e -2*p-1)
            * [e==2*i+0]:
                ... == (p**e+p**1 -2*p-2) == (p**e -p-2)
            == (p**e -(1+e%2)*p-(2-e%2))
            ]
        ###
        == p**(e-1)*(p-1)///2 -sp*((p**e -(1+e%2)*p-(2-e%2))///(p+1))
        ]

    [sz_xx<p**e;N> == (p**(e-1)*(p-1)///2 - ([Jacobi_symbol(p;+N)]+[Jacobi_symbol(p;-N)])*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2))///2
        == (p**(e-1)*(p-1)///2 - (sp+[sp==p41])*((p**e -(1+e%2)*p-(2-e%2))///(p+1)))///2
        == (p**(e-1)*(p-1)///2 - (jpN*p41 + 1)*((p**e -(1+e%2)*p-(2-e%2))///(p+1)))///2
        ]

    :分支简化]]

]]



[[
求num_part1_of_solutions_of_square_diff_mod(2**e;N)
    求num_part2_of_solutions_of_square_diff_mod(2**e;N)
    求num_part1_square_of_solutions_of_square_diff_mod(2**e;N)
[e>=3][N%2==1][(x**2-y**2-N)%2**e==0]:
    [is_square_residual_mod(2**e;N)
        == is_square_residual_mod(2**3;N)
        == [N%8==1]
        ]
    [[is_square_residual_mod(2**e;N)] -> [not$ is_square_residual_mod(2**e;-N)]]
    [not$ [[is_square_residual_mod(2**e;N)][is_square_residual_mod(2**e;-N)]]]
        # ==>> 下面无(T,T)分支

    !![e>=3]
    [@[z0<-[1..<2**e]] -> [z0%2=!=0] -> [len{z<-[0..<2**e] | [(z**2-z0**2)%2**e==0]} == 2**min(2,e-1) == 4]]
    !![e>=3]
    [@[z0<-[1..<2**e]] -> [z0%2=!=0] -> [+z0 =![%2**e]!= -z0]]

    [@[z0<-[0..<2**e]] -> [ez0 := max_power_of_base_as_factor_of_(2,z0)] -> [len{z<-[0..<2**e] | [(z**2-z0**2)%2**e==0]} == num_sqrts_mod_two_power(e,ez0)]]

    [num_sqrts_mod_two_power(e,ez0) =[def]= (if 2*ez0 >= e then 2**(e//2) else 2**ez0 * 2**min(2,e-2*ez0-1))]
        # 2**min(2,e-2*ez0-1) == (if e-2*ez0 >= 3 then 4 else (e-2*ez0))

    # 可能有复杂的[x*y%2==0]而不止[[x%2**e==0]or[y%2**e==0]]

    注意:与上面不同:
    * [ex==0][ey=!=0]:
        [x**2 =[%2**e]= N+y**2]
        [is_square_residual_mod(2**e;N+y**2)] 不等于 [is_square_residual_mod(2**e;N)]
        [N%8==1] 应该为 [(N+y**2)%8==1]
        [ey==1]时，需要特殊处理
        [y%8 <- {2,6}]
        [y**2%8 == 4]
        [(N+y**2)%8==(N+4)%8==1]
        [N%8==5]
    * [ex=!=0][ey==0]:
        [y**2 =[%p**e]= -N+x**2]
        [is_square_residual_mod(p**e;-N+x**2)]
        [(-N)%8==1] 应该为 [(-N+x**2)%8==1]
        [ex==1]时，需要特殊处理
        [x%8 <- {2,6}]
        [x**2%8 == 4]
        [(-N+x**2)%8==(-N+4)%8==1]
        [N%8==3]
    #####
    [sz_xy := num_solutions_of_square_diff_mod(2**e;N)]
        # 猜想已被证明[sz_xy==phi(2*2**e) == (2**e)]
    [sz_x := num_part1_of_solutions_of_square_diff_mod(2**e;N)]
    [sz_x == let[
        [s5 := [N%8==5]]
        [s1 := [N%8==1]]
        #[p41 := [p%4==1]]
        #bug:[p41 == s5+s1]
        #[N41 := [p%4==1]]
        #bug:[N41 == s5+s1]
        ]in
        # [p:=2]
        !![e>=3] #[(e+1)//2 >=2 >1]
        (sz_xy -s5*sum 4*num_sqrts_mod_two_power(e,ey)*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[1]} -s1*sum 4*num_sqrts_mod_two_power(e,ey) *(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[2..<(e+1)//2]} -s1*sum 4*num_sqrts_mod_two_power(e,ey)*1 {ey<-[(e+1)//2]})///4 + s5*sum 4*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[1]} + s1*sum 4*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[2..<(e+1)//2]} + s1*sum 4*1 {ey<-[(e+1)//2]}
        == (sz_xy///4 -s5*sum phi(p**(e-ey)) {ey<-[1]} -s1*sum phi(p**(e-ey)) {ey<-[2..<(e+1)//2]} -s1*sum num_sqrts_mod_two_power(e,ey) {ey<-[(e+1)//2]}) + s5*sum 4*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[1]} + s1*sum 4*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[2..<(e+1)//2]} + s1*4
        !! [num_sqrts_mod_two_power(e,ez0) =[def]= (if 2*ez0 >= e then 2**(e//2) else 2**ez0 * 2**min(2,e-2*ez0-1))]
        #####见下面:部分-过程
        == sz_xy///4 -s5*p**(e-2) -s1*p**(e//2)*(p**(e//2+e%2-2) -1) -s1*2**(e//2) + s5*2**max(2,e-3) + s1*[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) + s1*4
        == sz_xy///4 -s5*(2**(e-2)-2**max(2,e-3)) -s1*(2**(e-2) -[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) -4)
        [[
        #####部分:
        [sum phi(p**(e-ey)) {ey<-[2..<(e+1)//2]}
        ==p**(e//2)*(p**(e//2+e%2-2) -1)
        ]
        [sum 4*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[1]}
        ==2**max(2,e-3)
        ]
        [sum 4*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[2..<(e+1)//2]}
        ==[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3)
        ]
        #####过程:
        [sum phi(p**(e-ey)) {ey<-[2..<(e+1)//2]}
        ==sum p**(e-ey-1) {ey<-[2..<(e+1)//2]}
        # [z:=(e-ey-1)==e-(ey+1)>=e-(e+1)//2==e//2]
        # [z<=e-2-1==e-3<e-2]
        ==sum p**z {z<-[e//2..<e-2]}
        # [k:=z-e//2]
        # [k<e-2-e//2==e//2+e%2-2]
        ==p**(e//2)*sum p**k {k<-[0..<e//2+e%2-2]}
        ==p**(e//2)*(p**(e//2+e%2-2) -1)///(p-1)
        ==p**(e//2)*(p**(e//2+e%2-2) -1)
        ]
        [sum 4*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[1]}
        ==(p**(e-2)///(2**1 * 2**min(2,e-2*1-1)))*4
        ==(p**(e-3)///2**min(2,e-3))*4
        ==2**max(0,e-5)*4
        ==2**max(2,e-3)
        ]
        [sum 4*(phi(p**(e-ey))///num_sqrts_mod_two_power(e,ey)) {ey<-[2..<(e+1)//2]}
        ==4*sum (p**(e-ey-1)///(2**ey * 2**min(2,e-2*ey-1))) {ey<-[2..<(e+1)//2]}
        ==4*sum (p**(e-2*ey-1)///(2**min(2,e-2*ey-1))) {ey<-[2..<(e+1)//2]}
        ==4*sum 2**max(0,e-2*ey-3) {ey<-[2..<(e+1)//2]}
        ==sum 2**max(2,e-2*ey-1) {ey<-[2..<(e+1)//2]}
        [[分支:
        # [e-2*ey-1 <= 1] <==> [ey >= (e-2)/2] <==> [ey >= (e-1)//2]
        # [(e-1)//2 >= 2] <==> [e>=5]
        * [3<=e<5]:
            [2==(e+1)//2]
            ...==sum 2**max(2,e-2*ey-1) {ey<-[2..<2]}
                == 0
        * [e>=5]:
            [2 <= (e-1)//2 < (e+1)//2]
            ...==sum 2**max(2,e-2*ey-1) {ey<-[2..<(e-1)//2]++[(e-1)//2..<(e+1)//2]}
                ==sum 2**(e-2*ey-1) {ey<-[2..<(e-1)//2]} + sum 2**2 {ey<-[(e-1)//2..<(e+1)//2]}
                ==sum 2**(e-2*ey-1) {ey<-[2..<(e-1)//2]} + 4
                # [z:=(e-2*ey-1)=(e+1-2*(ey+1))>=e+1-(e-1)//2 *2==e+1-(e-1-(e-1)%2)==2+(e-1)%2==3-e%2 <- {2,3}]
                # [z <= e-2*2-1 == e-5]
                ==4+sum 2**z {z<-[(3-e%2),(3-e%2)+2..<e-5+2]}
                ==4+2**(3-e%2)*sum 2**k {k<-[0,2..<e-5+2-(3-e%2)==e+e%2-6]}
                ==4+2**(3-e%2)*(2**(e+e%2-6) -1)///(2**2-1)
                ==4+2**(3-e%2)*(2**(e+e%2-6) -1)///3
        ]]
        ==sum 2**max(2,e-2*ey-1) {ey<-[2..<(e+1)//2]}
        ==[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3)
        ]
        ]]
        == sz_xy///4 -[N%8==5]*(2**(e-2)-2**max(2,e-3)) -[N%8==1]*(2**(e-2) -[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) -4)
        =[猜想已被证明]= 2**(e-2) -[N%8==5]*(2**(e-2)-2**max(2,e-3)) -[N%8==1]*(2**(e-2) -[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) -4)
            #？大约phi(2**e)一半？
            #！！[N%8==1]时大约只有phi(2**e)的1/4
            #！！[N%8==5]时只有phi(2**e)的1/4
            #   1*5%8 == 3*7%8 == 5
            #   3*3%8 == 7*7%8 == 1
            #   即可:
            #     [N%8==3][N'==3*N] # =[%8]=1
            #     [N%8==7][N'==3*N] # =[%8]=5
            #       但 N->N' 比特数增加log2(3)超过1，不划算
        #####
        [(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3)
        == ((2**(e-3) -2**(3-e%2) +12)///3)
        == (4*(2**(e-5) -2**(1-e%2) +3)///3)
        ]
        #####
        =[简化]= 2**(e-2) -s5*(2**(e-2)-2**max(2,e-3)) -s1*(2**(e-2) -[e>=5]*(4*(2**(e-5) -2**(1-e%2) +3)///3) -4)
        #####
        [[
        * [3<=e<5]:
            ... == 2**(e-2) -s5*(2**(e-2)-2**2) -s1*(2**(e-2) -4)
                == 2**(e-2) -(s5+s1)*(2**(e-2)-4)
                == 2**(e-2) +(s5+s1)*(4-2**(e-2))
                # [2**(e-2) == (4-2*[e==3])]
                == (4-2*[e==3]) +2*[e==3]*(s5+s1)
                == (4-2*[e==3]) +2*[e==3]*N41
                == 4-2*[e==3]*(1-N41)
                == 4-2*[e==3][N%4==3]
        * [e>=5]:
            ... == 2**(e-2) -s5*(2**(e-2)-2**(e-3)) -s1*(2**(e-2) -(4*(2**(e-5) -2**(1-e%2) +3)///3) -4)
                == 2**(e-2) -s5*(2**(e-3)) -s1*(2**(e-2) -4*(2**(e-5) -2**(1-e%2) +6)///3)
                == 2**(e-2) -s5*(2**(e-3)) -s1*(4*(3*2**(e-4) -2**(e-5) +2**(1-e%2) -6)///3)
                == 2**(e-2) -s5*(2**(e-3)) -s1*(4*(5*2**(e-5) +(2 - e%2) -6)///3)
                == 2**(e-2) -s5*(2**(e-3)) -s1*(4*(5*2**(e-5) -(4 +e%2))///3)
                == (1-s5-s1)*2**(e-2) +s5*(2**(e-2)-2**(e-3)) +s1*(2**(e-2) -4*(5*2**(e-5) -(4 +e%2))///3)
                == [N%4==3]*2**(e-2) +s5*(2**(e-3)) +s1*(4*(3*2**(e-4) -5*2**(e-5) +(4 +e%2))///3)
                == [N%4==3]*2**(e-2) +[N%8==5]*(2**(e-3)) +[N%8==1]*(4*(2**(e-5) +(4 +e%2))///3)
        ]]
        #####
        =[简化]= [3<=e<5]*(4-2*[e==3][N%4==3]) + [e>=5]*([N%4==3]*2**(e-2) +[N%8==5]*(2**(e-3)) +[N%8==1]*(4*(2**(e-5) +(4 +e%2))///3))
        #####
        [[
        * [e==1]:
            [N%2**e==1]
            [1 =[%2**e]= 0**2-1**2]
            [1 =[%2**e]= 1**2-0**2]
            [sz_x<2**e;N> == sz_y<2**e;N> == len{0,1} == 2]
            [sz_xx<2**e;N> == sz_yy<2**e;N> == len{0,1} == 2 == 3-e]
        * [e==2]:
            [N%2**e<-{1,3}]
            [1 =[%2**e]= 1**2 =[%2**e]= 3**2]
            [0 =[%2**e]= 0**2 =[%2**e]= 2**2]
            * [N%2**e==1]:
                [1 =[%2**e]= 1-0]
                [sz_xx<2**e;N> == len{1} == 1]
                [sz_yy<2**e;N> == len{0} == 1]
                [sz_x<2**e;N> == len{1,3} == 2]
                [sz_y<2**e;N> == len{0,2} == 2]
            * [N%2**e==1]:
                [3 =[%2**e]= 0-1]
                [sz_xx<2**e;N> == len{0} == 1]
                [sz_yy<2**e;N> == len{1} == 1]
                [sz_x<2**e;N> == len{0,2} == 2]
                [sz_y<2**e;N> == len{1,3} == 2]
            [sz_x<2**e;N> == sz_y<2**e;N> == 2]
            [sz_xx<2**e;N> == sz_yy<2**e;N> == 1 == 3-e]
        ###
        [1<=e<3]:
            [sz_xx<2**e;N> == sz_yy<2**e;N> == 3-e]
            [sz_x<2**e;N> == sz_y<2**e;N> == 2]
        ]]
        #####
        =[简化补充]= [1<=e<3]*2 + [3<=e<5]*(4-2*[e==3][N%4==3]) + [e>=5]*([N%4==3]*2**(e-2) +[N%8==5]*(2**(e-3)) +[N%8==1]*(4*(2**(e-5) +(4 +e%2))///3))
        =[简化补充]= [e==0]*1 + [1<=e<3]*2 + [e==3]*(2+2*[N%4==1]) + [e==4]*4 + [e>=5]*([N%4==3]*2**(e-2) +[N%8==5]*(2**(e-3)) +[N%8==1]*(4*(2**(e-5) +(4 +e%2))///3))
    ]
    [sz_y := num_part2_of_solutions_of_square_diff_mod(2**e;N)]
    !![num_part2_of_solutions_of_square_diff_mod(M;N) == num_part1_of_solutions_of_square_diff_mod(M;-N)]
    [sz_y == num_part2_of_solutions_of_square_diff_mod(2**e;-N)
        == sz_xy///4 -[(-N)%8==5]*(2**(e-2)-2**max(2,e-3)) -[(-N)%8==1]*(2**(e-2) -[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) -4)
        == sz_xy///4 -[N%8==3]*(2**(e-2)-2**max(2,e-3)) -[N%8==7]*(2**(e-2) -[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) -4)
        =[猜想已被证明]= 2**(e-2) -[N%8==3]*(2**(e-2)-2**max(2,e-3)) -[N%8==7]*(2**(e-2) -[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) -4)
        =[简化]= [3<=e<5]*(4-2*[e==3][N%4==1]) + [e>=5]*([N%4==1]*2**(e-2) +[N%8==3]*(2**(e-3)) +[N%8==7]*(4*(2**(e-5) +(4 +e%2))///3))
        =[简化补充]= [1<=e<3]*2 + [3<=e<5]*(4-2*[e==3][N%4==1]) + [e>=5]*([N%4==1]*2**(e-2) +[N%8==3]*(2**(e-3)) +[N%8==7]*(4*(2**(e-5) +(4 +e%2))///3))
        =[简化补充]= [e==0]*1 + [1<=e<3]*2 + [e==3]*(2+2*[N%4==1]) + [e==4]*4 + [e>=5]*([N%4==1]*2**(e-2) +[N%8==3]*(2**(e-3)) +[N%8==7]*(4*(2**(e-5) +(4 +e%2))///3))
    ]
    [sz_xx := num_part1_square_of_solutions_of_square_diff_mod(2**e;N)]
    [sz_xx == let[
        [s5 := [N%8==5]]
        [s1 := [N%8==1]]
        [s3 := [N%8==3]]
        [s7 := [N%8==7]]
        ]in
        sz_x/4 + sz_y/4 - sz_xy/16
        == (sz_x + sz_y - sz_xy///4)///4
        == (sz_xy///4 -(s5+s3)*(2**(e-2)-2**max(2,e-3)) -(s1+s7)*(2**(e-2) -[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) -4))///4
        #####
        [sz_x + sz_y
        == [3<=e<5]*(4-2*[e==3][N%4==3]) + [e>=5]*([N%4==3]*2**(e-2) +[N%8==5]*(2**(e-3)) +[N%8==1]*(4*(2**(e-5) +(4 +e%2))///3))
        +  [3<=e<5]*(4-2*[e==3][N%4==1]) + [e>=5]*([N%4==1]*2**(e-2) +[N%8==3]*(2**(e-3)) +[N%8==7]*(4*(2**(e-5) +(4 +e%2))///3))
        == [3<=e<5]*(8-2*[e==3]) + [e>=5]*(2**(e-2) +(s3+s5)*(2**(e-3)) +(s1+s7)*(4*(2**(e-5) +(4 +e%2))///3))
        ]
        #####
        == ([3<=e<5]*(8-2*[e==3]) + [e>=5]*(2**(e-2) +(s3+s5)*(2**(e-3)) +(s1+s7)*(4*(2**(e-5) +(4 +e%2))///3)) - 2**(e-2))///4
        == ([3<=e<5]*4 + [e>=5]*((s3+s5)*(2**(e-3)) +(s1+s7)*(4*(2**(e-5) +(4 +e%2))///3)))///4
        =[简化]= [3<=e<5]*1 + [e>=5]*((s3+s5)*(2**(e-5)) +(s1+s7)*((2**(e-5) +(4 +e%2))///3))
        =[简化补充]= [1<=e<3]*(3-e) + [3<=e<5]*1 + [e>=5]*((s3+s5)*(2**(e-5)) +(s1+s7)*((2**(e-5) +(4 +e%2))///3))
        =[简化补充]= [e==1]*2 + [2<=e<5]*1 + [e>=5]*((s3+s5)*(2**(e-5)) +(s1+s7)*((2**(e-5) +(4 +e%2))///3))
        =[简化补充]= [0<=e<5]*(1+[e==1]) + [e>=5]*((s3+s5)*(2**(e-5)) +(s1+s7)*((2**(e-5) +(4 +e%2))///3))
    ]
]]
]]]]

#]]]'''
__all__ = '''

    '''.split()
from seed.math.Jacobi_symbol import Jacobi_symbol
from seed.math.gcd import gcd
from seed.math.II import II
from nn_ns.math_nn.Chinese_Remainder_Theorem import CRT, ECRT, mk_CRT, apply_CRT, apply_CRT__pairs, check_CRT_ans, CRT_Answer_Error
from nn_ns.math_nn.prime2 import primes_lt
from seed.math.floor_ceil import floor_log2
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer


def 求平方差分解囗模囗暴力(M, N, /):
    assert M >= 1
    assert gcd(M,N) == 1
    n = N%M
    d = {} # {x**2:[x]}
    for x in range(M):
        x2 = x**2%M
        xs = d.setdefault(x2,[])
        xs.append(x)
    XY_N_M = {(x,y) for x2 in d for y2 in [(x2-n)%M] if y2 in d for x in d[x2] for y in d[y2]}
    return XY_N_M

def 求平方差分解囗模素数(p, N, /):
    #[is_prime p]
    d = {x**2 %p : x for x in range(0, p//2+1)}
    n = N%p
    XY_N_p__core = {(d[x2],d[y2]) for x2 in d for y2 in [(x2-n)%p] if y2 in d}
    XY_N_p = {(x,y) for a,b in XY_N_p__core for na, nb in [((-a)%p, (-b)%p)] for (x,y) in [(a,b), (na,b), (a,nb), (na,nb)]}
    return XY_N_p

def 求平方差分解囗模素数幂(p, e, N, may_XY_N_p, /):
    if not (p == 2 or e==1): raise ValueError
    if e == 1:
        if may_XY_N_p is None:
            XY_N_p = 求平方差分解囗模素数(p, N)
        else:
            XY_N_p = may_XY_N_p
        return XY_N_p
    return 求平方差分解囗模二幂(e, N, may_XY_N_p)
def 求平方差分解囗模二幂(e, N, may_XY_N_p, /):
    p = 2
    if not e >= 1: raise ValueError
    if not N&1: raise ValueError
    pe = 1<<e
    N %= pe
        # N > 0
    if may_XY_N_p is None:
        XY_N_p = 求平方差分解囗模素数(p, N)
    else:
        XY_N_p = may_XY_N_p
    XY_N_p_i = XY_N_p # [i==1]
    sN = bin(N)[2:]
    assert sN[0] == '1'
    L = len(sN)
    def iter_lifted_xy_pairs(x,y, i):
        #[t == N//p**i %p]
        #[s == (x**2-y**2)//p**i %p]
        assert i >= 1
        assert (x**2-y**2 -N)%2**i == 0
        #bug:wrap:t = 1 if sN[L-1-i] == '1' else 0
        t = (1 if sN[L-1-i] == '1' else 0) if i < L else 0
        #bug?:neg?:
        s = ((x**2-y**2)>>i)&1
        #bug?:neg?:s = ((x**2-y**2)//2**i)&1
        # (-1)//2==-1
        #s = (((x**2-y**2)%2**(i+1))>>i)&1
        if t == s:
            assert (x**2-y**2 -N)%2**(i+1) == 0, ((x,y,i),N,(t,s),((x**2-y**2)//2**i,(x**2-y**2)))
            h = 1<<i
            xh = x + h
            yh = y + h
            yield (x,y)
            yield (xh,y)
            yield (x,yh)
            yield (xh,yh)
        else:
            pass
        return
    for i in range(1, e):
        XY_N_p_i1 = {(x1,y1) for x,y in XY_N_p_i for x1,y1 in iter_lifted_xy_pairs(x,y,i)}
        XY_N_p_i = XY_N_p_i1 #[i:=i+1]
    XY_N_p_e = XY_N_p_i #[i==e]
    return XY_N_p_e

def _t求平方差分解囗模素数幂(P, E, /):
    d = {}
    for p in primes_lt(P):
        es = range(1, E) if p == 2 else [1]
        for e in es:
            M = pe = p**e
            phi_pe = pe//p *(p-1)
            for N in range(pe):
                if not N%p ==0:
                    XY_N_p_e = 求平方差分解囗模素数幂(p,e,N,None)
                    XY_N_M = 求平方差分解囗模囗暴力(M,N)
                    assert XY_N_p_e == XY_N_M, (p,e,pe,N,XY_N_p_e,XY_N_M,XY_N_p_e-XY_N_M,XY_N_M-XY_N_p_e)
                    sz = len(XY_N_p_e)
                    d[(p,e,N)] = ((sz, phi_pe, sz/phi_pe), XY_N_p_e)
                    if 1:
                        ##猜想已被证明:
                        ratio = 2 if p== 2 else 1
                        assert sz == phi_pe*ratio
    return d
#print(stable_repr__expand_top_layer(_t求平方差分解囗模素数幂(10, 8)))

def _find_upperbound4primes_lt__ver1():
    ps = primes_lt(1000)
    M = 1
    nprimes_nbits_pairs = []
    p_nbits_pairs = []
    for num_primes, p in enumerate(ps, 1):
        M *= p
        num_bits = floor_log2(M)
        nprimes_nbits_pairs.append((num_primes, num_bits))
        p_nbits_pairs.append((p, num_bits))
    def key(p_nbits, /):
        (p, num_bits) = p_nbits
        p1 = p+1
        return p1/num_bits
    #sorted_p_nbits_pairs = sorted(p_nbits_pairs, key=key)
    #print(p_nbits_pairs)
    #print(sorted_p_nbits_pairs)
    ratio_p_nbits_triples = [((p+1)/num_bits, p, num_bits) for p, num_bits in p_nbits_pairs]
    sorted_ratio_p_nbits_triples = sorted(ratio_p_nbits_triples)
    #print(ratio_p_nbits_triples)
    print(sorted_ratio_p_nbits_triples)
    [(0.7155519742143432, 887, 1241), (0.7172264355362947, 661, 923), (0.7181153533712429, 883, 1231), (0.7184873949579832, 683, 952), (0.7194004995836802, 863, 1201), (0.7197452229299363, 677, 942), (0.7198612315698178, 829, 1153), (0.72, 773, 1075), (0.7200832466181062, 691, 961), (0.7214765100671141, 859, 1192), (0.7215909090909091, 761, 1056)
    , ..., (0.84375, 53, 64), (0.8571428571428571, 59, 70), (0.8648648648648649, 31, 37), (0.8695652173913043, 19, 23), (0.875, 41, 48), (0.8888888888888888, 23, 27), (0.9047619047619048, 37, 42), (0.9375, 29, 32), (1.0, 13, 14), (1.0, 17, 18), (1.0909090909090908, 11, 11), (1.1428571428571428, 7, 7), (1.5, 5, 4), (2.0, 3, 2), (3.0, 2, 1)]



    # floor_log2(N)+1 <= floor_log2(M) == (p+1)/ratio<p>
    # [p>17]: [ratio<p> < 1][... > p+1]
    # num_primes_lt(u) ~ u/ln(u)
    # num_primes_lt**-1(num_primes) = ???
    # N < 2**(floor_log2(N)+1) <= II(primes[:(floor_log2(N)+1)]) ~ II(primes_lt(uN))
    #   where [num_bits == (floor_log2(N)+1) < uN/ln(uN)]
    # [uN0 := num_bits**2]
    # [uN0/ln(uN0) == num_bits/2 * num_bits/ln(num_bits)]
    # [uN1 := num_bits*ln(num_bits)**2]
    # [uN1/ln(uN1) == num_bits*ln(num_bits)**2/(ln(num_bits)+2*lnln(num_bits))]
    if 0:
        ratio_p_uN_nbits_tpls = [((p+1)/uN, p, uN, num_bits) for p, num_bits in p_nbits_pairs for uN in [num_bits*floor_log2(num_bits)**2]]
        sorted_ratio_p_uN_nbits_tpls = sorted(ratio_p_uN_nbits_tpls)
        #print(ratio_p_uN_nbits_tpls)
        print(sorted_ratio_p_uN_nbits_tpls)
#_find_upperbound4primes_lt__ver1()

def _debug__find_upperbound4primes_lt__ver1():
    if 1:
        N = 102377
        assert floor_log2(N) == 16
        assert 2**16 < N < 2**17
        #print(II(primes_lt(17)), N, II(primes_lt(17+1)))
        assert II(primes_lt(17)) == 30030 < N < 510510 == II(primes_lt(17+1))
_debug__find_upperbound4primes_lt__ver1()
assert 1001 == 7*11*13 == 91*11
def _find_upperbound4primes_lt__ver2():
    ps = primes_lt(1000)
    M = 1
    p_nbits_pairs = []
    for num_primes, p in enumerate(ps, 1):
        prev_num_bits = floor_log2(M)
        p_nbits_pairs.append((p, prev_num_bits))
        M *= p
    ratio_p_nbits_triples = [((p+1)/(prev_num_bits+1), p, prev_num_bits) for p, prev_num_bits in p_nbits_pairs]
    sorted_ratio_p_nbits_triples = sorted(ratio_p_nbits_triples)
    print(sorted_ratio_p_nbits_triples)
    [(0.7207792207792207, 887, 1231), (0.723404255319149, 883, 1221), (0.7234972677595628, 661, 914), (0.7242246437552389, 863, 1192), (0.7253446447507953, 683, 942), (0.725398313027179, 773, 1066), (0.7255244755244755, 829, 1143), (0.7259100642398287, 677, 933), (0.7261280167890871, 691, 952)
    , ..., (0.9, 53, 59), (0.9230769230769231, 59, 64), (0.9696969696969697, 31, 32), (0.9767441860465116, 41, 42), (1.0, 23, 23), (1.0, 37, 37), (1.0526315789473684, 19, 18), (1.0714285714285714, 29, 27), (1.1666666666666667, 13, 11), (1.2, 17, 14), (1.5, 11, 7), (1.6, 7, 4), (2.0, 3, 1), (2.0, 5, 2), (3.0, 2, 0)]
#_find_upperbound4primes_lt__ver2()


def _N2upperbound4primes_lt(N, /):
    assert N >= 1
    #bug:@[N==102377]:upperbound4primes_lt = max(floor_log2(N)+1, 11+1)
    #   bug in _find_upperbound4primes_lt__ver1
    upperbound4primes_lt = max(floor_log2(N)+2, 37+1)
        # using _find_upperbound4primes_lt__ver2
    return upperbound4primes_lt
def _N2primes(N, /):
    assert N >= 1
    upperbound4primes_lt = _N2upperbound4primes_lt(N)
    primes = primes_lt(upperbound4primes_lt)
    assert II(primes) >= N, (N, upperbound4primes_lt, primes)
    if not II(primes) >= N: raise logic-err
    M = 1
    if N <= M:
        num_primes = 0
    else:
        for num_primes, p in enumerate(primes, 1):
            M *= p
            if N <= M:break
        else:
            raise logic-err
        assert N > II(primes[:num_primes-1])
    assert N <= II(primes[:num_primes])
    primes = primes[:num_primes]
    return primes

def _test__N2primes():
    p = 2
    _N2primes(1) # [e==0]
    for e in range(1, 100):
        pe = 1<<e # >= 2
        pe_n1 = pe-1 # >= 1
        _N2primes(pe)
        _N2primes(pe_n1)
_test__N2primes()


def 求整数分解囗平方差囗中国剩余定理(p_e_pairs, N, /, *, verbose=False):
    M = 1
    XY_N_M = {(0,0)}
    for p,e in p_e_pairs:
        pe = p**e
        crt = mk_CRT([M, pe], extended=False)
        XY_N_p_e = 求平方差分解囗模素数幂(p, e, N, None)
        sz_M0 = len(XY_N_M)
        sz_pe = len(XY_N_p_e)
        M = crt.get_whole_modulus()
        n = N%M
        XY_N_M = {(x,y)
            for xR,yR in XY_N_p_e
            for xL,yL in XY_N_M
            for x,y in [(crt([xL,xR]), crt([yL,yR]))]
            if (x**2-y**2)%M == n
                #无用？
                #见下面:assert sz == sz_M0*sz_pe
                #见上面 猜想已被证明 [sz==phi(M)*2**[M%2==0]]
            }
        sz = len(XY_N_M)
        if verbose:
            print(M, sz, f'{sz*100/M}%')
        assert sz == sz_M0*sz_pe
    return XY_N_M


class _G:
    psp = 222268187453619875640733914738520122510113

def _t():
    ps_lt18 = primes_lt(18)
    M = II(ps_lt18)

    N = 102377
    for N in range(102377, M, 2):
        if all(N%p for p in ps_lt18):break
    else:
        raise logic-err
    print(N)
    ps = _N2primes(N)
    print(ps)
    p_e_pairs = [(p, (4 if p==2 else 1)) for p in ps]
    print(p_e_pairs)
    XY_N_M = 求整数分解囗平方差囗中国剩余定理(p_e_pairs, N, verbose=True)
    r'''
[[N%7==0
102377
(2, 3, 5, 7, 11, 13, 17)
[(2, 4), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1)]
16 16 100.0%
48 32 66.66666666666667%
240 128 53.333333333333336%
1680 768 45.714285714285715%
18480 16128 87.27272727272727%
240240 193536 80.55944055944056%
#... #long long time...
4084080 3096576 75.820649938297%

可行解太多了...毫无意义...
16 = 2*phi(16)
32 = 16*(3-1)
128 = 32*(5-1)
768 = 128*(7-1)
16128 = 768*21 ???
    [102377 == 9307*11]
193536 = 16128*(13-1)
3096576 = 193536*(17-1)
]]
[[gcd(N, II([2, 3, 5, 7, 11, 13, 17]))==1
102379
(2, 3, 5, 7, 11, 13, 17)
[(2, 4), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1)]
16 16 100.0%
48 32 66.66666666666667%
240 128 53.333333333333336%
1680 768 45.714285714285715%
18480 7680 41.55844155844156%
240240 92160 38.36163836163836%
4084080 1474560 36.10507139918904%

16 = 2*phi(16)
32 = 16*(3-1)
128 = 32*(5-1)
768 = 128*(7-1)
7680 = 768*(11-1)
92160 = 7680*(13-1)
1474560 = 92160*(17-1)
sz = 2*phi(M)

]]
    #'''
#xxx assert len(求平方差分解囗模囗暴力(11, 102377)) == 11-1
assert 102377 == 9307*11
assert len(求平方差分解囗模囗暴力(11**1, 9)) == (11-1)*11**(1-1)
assert len(求平方差分解囗模囗暴力(11**2, 9)) == (11-1)*11**(2-1)
assert len(求平方差分解囗模囗暴力(11**3, 9)) == (11-1)*11**(3-1)

if __name__ == "__main__":
    #_t()
    pass

def num_part1_of_solutions_of_square_diff_mod__ex(M, N, /):
    XY_N_M = 求平方差分解囗模囗暴力(M,N)
    xs = {x for x,y in XY_N_M}
    return len(xs), xs, XY_N_M
def num_part1_of_solutions_of_square_diff_mod(M, N, /):
    len_xs, xs, XY_N_M = num_part1_of_solutions_of_square_diff_mod__ex(M,N)
    return len_xs
def num_part1_square_of_solutions_of_square_diff_mod__ex(M, N, /):
    len_xs, xs, XY_N_M = num_part1_of_solutions_of_square_diff_mod__ex(M,N)
    xxs = {x**2%M for x in xs}
    return len(xxs), xxs, len_xs, xs, XY_N_M
    XY_N_M = 求平方差分解囗模囗暴力(M,N)
    xxs = {x**2%M for x,y in XY_N_M}
    return len(xxs), xxs, XY_N_M
def num_part1_square_of_solutions_of_square_diff_mod(M, N, /):
    len_xxs, xxs, len_xs, xs, XY_N_M = num_part1_square_of_solutions_of_square_diff_mod__ex(M,N)
    return len_xxs

def _t__num_part1_of_solutions_of_square_diff_mod(P, E, /):
    assert E >= 1
    assert P >= 3
    for p in primes_lt(P+1):
      #e = max(3 if p==2 else 1,E)
      e0 = (3 if p==2 else 1)
      for e in range(e0, E+1):
        pe = p**e
        if p==2:
            basic = 2**(e-2)
            ex5 = (2**(e-2)-2**max(2,e-3))
            #ex1 = (2**(e-2) -(e>=5)*(4+2**(3-e%2)*(2**(e+e%2-6) -1)//3) -4)
            #   bug:出现 浮点数:因为((e>=5)*...)并非 短路运算
            #print(2**(e+e%2-6))
            ex1 = (2**(e-2) -(e>=5)*(4+(2**(e-3) -2**(3-e%2))//3) -4)
            exs = [ex5,ex1]
        else:
            basic = p**(e-1)*(p-1)//2
            ex = (p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)//(p+1) -2)
            exs = [ex]
        for N in range(pe):
            if not N%p ==0:
                #sz_x, xs, XY_N_pe = num_part1_of_solutions_of_square_diff_mod__ex(pe, N)
                sz_xx, xxs, sz_x, xs, XY_N_pe = num_part1_square_of_solutions_of_square_diff_mod__ex(pe,N)
                if p==2:
                    # =[猜想已被证明]= 2**(e-2) -[N%8==5]*(2**(e-2)-2**max(2,e-3)) -[N%8==1]*(2**(e-2) -[e>=5]*(4+2**(3-e%2)*(2**(e+e%2-6) -1)///3) -4)
                    s1 = N%8==1
                    s5 = N%8==5
                    sz_x_guess = basic-s5*ex5-s1*ex1
                    s3 = N%8==3
                    s7 = N%8==7
                    ss = [s5,s1,s3,s7]
                    sz_xx_guess = (basic-(s5+s3)*ex5-(s1+s7)*ex1)//4
                else:
                    # =[猜想已被证明]= p**(e-1)*(p-1)///2 -[Jacobi_symbol(p;N)==+1]*(p**(e-1) - p**(1-e%2)*(p**(e+e%2-2)-1)///(p+1) -2)
                    sp = Jacobi_symbol(p,N)==+1
                    sz_x_guess = basic-sp*ex
                    sn = sp==(p%4==1)
                    sz_xx_guess = (basic-(sp+sn)*ex)//2
                    ss = [sp,sn]
                assert sz_x_guess == sz_x, ((p,e,N), (sz_x_guess,sz_x), (basic, ss, exs), sorted(xs), len(XY_N_pe), sorted(XY_N_pe))
                assert sz_xx_guess == sz_xx, ((p,e,N), (sz_xx_guess,sz_xx), (basic, ss, exs), sorted(xxs), len(XY_N_pe), sorted(XY_N_pe))
    r'''
assert sz_x_guess == sz_x, ((p,e,N), (sz_x_guess,sz_x), (basic, b, ex), sorted(xs), len(XY_N_pe), sorted(XY_N_pe))
bug 已修复！AssertionError: ((3, 4, 1), (2, 8), (27, True, 25)
, [1, 8, 19, 35, 46, 62, 73, 80]
, 54, [(1, 0), (1, 9), (1, 18), (1, 27), (1, 36), (1, 45), (1, 54), (1, 63), (1, 72), (8, 12), (8, 15), (8, 39), (8, 42), (8, 66), (8, 69), (19, 6), (19, 21), (19, 33), (19, 48), (19, 60), (19, 75), (35, 3), (35, 24), (35, 30), (35, 51), (35, 57), (35, 78), (46, 3), (46, 24), (46, 30), (46, 51), (46, 57), (46, 78), (62, 6), (62, 21), (62, 33), (62, 48), (62, 60), (62, 75), (73, 12), (73, 15), (73, 39), (73, 42), (73, 66), (73, 69), (80, 0), (80, 9), (80, 18), (80, 27), (80, 36), (80, 45), (80, 54), (80, 63), (80, 72)])

[(1, 0), (1, 9), (1, 18), (1, 27), (1, 36), (1, 45), (1, 54), (1, 63), (1, 72)
, (80, 0), (80, 9), (80, 18), (80, 27), (80, 36), (80, 45), (80, 54), (80, 63), (80, 72)]
    ey>=(e+1)//2
    sz==p**(e//2)=3**(4//2)==9
, (8, 12), (8, 15), (8, 39), (8, 42), (8, 66), (8, 69)
, (73, 12), (73, 15), (73, 39), (73, 42), (73, 66), (73, 69)
    ey==1
    sz==2*p**ey==2*3**1==6
        //3 => 4,5,13,14,22,23
        //3 %9 => 4,5,4,5,4,5
        //3 //9 => 0,0,1,1,2,2
, (19, 6), (19, 21), (19, 33), (19, 48), (19, 60), (19, 75)
, (62, 6), (62, 21), (62, 33), (62, 48), (62, 60), (62, 75)

, (35, 3), (35, 24), (35, 30), (35, 51), (35, 57), (35, 78)
, (46, 3), (46, 24), (46, 30), (46, 51), (46, 57), (46, 78)

e=4
    ey=1
    3组:(2*6)*3 = 2*(3-1)*3**2 = 2*phi(3**(e-ey)) == 36
    3组=phi(3**(e-ey))/2*p**ey

    ey>=2
    2*ey>=e
    1组:(2*p**(e//2))*1==18

    sz_xy = 54 = 18+36
    sz_x = 2*1 + 2*3 = 8

    #'''

if 1:
    _t__num_part1_of_solutions_of_square_diff_mod(4, 7)
    #_t__num_part1_of_solutions_of_square_diff_mod(6, 4)
    #_t__num_part1_of_solutions_of_square_diff_mod(10, 5)

def _II_primes__vs__2_pow_num_primes(P,/):
    ps = primes_lt(P+1)
    M = 1
    for num_primes, p in enumerate(ps,1):
        if p==2:
            p = 2**3
        M *= p
        L = (M-1).bit_length()
        print(p, (L, num_primes), L/num_primes, L-num_primes)

#_II_primes__vs__2_pow_num_primes(10**2)


if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main, adhoc_argparse
    #adhoc_argparser__main(globals(), None)
