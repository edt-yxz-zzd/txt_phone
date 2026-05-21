#__all__:goto
r'''[[[
e script/设计冫乘法群牜不可交换.py

script.设计冫乘法群牜不可交换
py -m nn_ns.app.debug_cmd   script.设计冫乘法群牜不可交换 -x # -off_defs
py -m nn_ns.app.doctest_cmd script.设计冫乘法群牜不可交换:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %script.设计冫乘法群牜不可交换:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######

[[
加法群:additive group
乘法群:multiplicative group

循环群:cyclic group
交换群:commutative group(亦称Abelian group)
非可换环:non-commutative ring #noncommutative ring
]]
[[
源起: view others/数学/p_adic_integer_ring.txt
===
[(1+B*x)*(1+B*y) == 1+B*(x+y)+B**2*x*y]
[gcd(B,(1+B*x)) == 1]
[gcd(A*B,a*b) == 1]:
  [(a+A*x)*(b+B*y) == a*b+(b*A*x+a*B*y)+A*B*x*y]
  [gcd(A,(a+A*x)) == 1]
  [gcd(B,(b+B*y)) == 1]
===
[e,k,C::int][e,k>=1][C>=2][C**e==A==B][gcd(C,a*b) == 1]:
  [gcd(A*B,a*b) == 1]
  [gcd(C**(e+k),(a+A*x)*(b+B*y)) == 1]
  [vb:=pow((b+B*y),-1,C**(e+k))]
  [(b+B*y)*vb =[%C**(e+k)]= 1]
  [(a+A*x)*(b+B*y)*vb =[%C**(e+k)]= (a+A*x)]
  [(a+A*x)*(b+B*y)*vb -a =[%C**(e+k)]= (A*x)]
  [((a+A*x)*(b+B*y)*vb -a)///A =[%C**k]= x]
  [x =[%C**k]= (((a+A*x)*(b+B*y)*vb -a)///A)]
  [(a+A*x)*(b+B*y) %C**e == a*b%C**e]
===
[e,k,C::int][e,k>=1][C>=2][B:=A:=C**e][a,b::uint%C**(k+e)][gcd(C,a*b) == 1][x,y::uint%C**k]:
  [mul7nc_{e,k,C;a,b}(x,y) =[def]= (a+A*x)*(b+B*y) %C**(e+k) //C**e]
    #乘法牜不可交换
    #未必支持结合律
===
[B,D::int][B,D>=2][a,b::uint%(B*D)][gcd(B,a*b) == 1][x,y::uint%D]:
  !! [gcd(B,a*b) == 1]
  [gcd(B,(a+B*x)*(b+B*y)) == gcd(B,a*b) == 1]
  [gcd((B*D),(a+B*x)*(b+B*y)) == 1]
    <==> [gcd(D,(a+B*x)*(b+B*y)) == 1]
  how? [gcd(D,(a+B*x)*(b+B*y)) == 1]
  [p::prime][D%p==0][B%p=!=0]:
    [(a+B*x)%p==0]
      !! [B%p=!=0]
      <==>[x=[%p]=(-a)*pow(B,-1,p)]
    !! [D%p==0]
    [D>=p]
    !! [x::uint%D]
    [max x == D-1 >= p-1]
    [x:=(-a)*pow(B,-1,p)%p]:
      [(a+B*x)%p==0]
      [gcd(D,(a+B*x)) %p == 0]
      [gcd(D,(a+B*x)*(b+B*y)) =!= 1]
  [gcd(D,(a+B*x)*(b+B*y)) == 1]
    <==> [@[p::prime][D%p==0] -> [B%p==0]]
===
[B,D::int][B,D>=2][@[p::prime][D%p==0] -> [B%p==0]][a,b::uint%(B*D)][gcd(B,a*b) == 1][x,y::uint%D]:
  [p::prime][gcd(D,a+B*x)%p==0]:
    !! [gcd(D,a+B*x)%p==0]
    [D%p==0]
    !! [@[p::prime][D%p==0] -> [B%p==0]]
    [B%p==0]
    [gcd(p,a+B*x)
    !! [B%p==0]
    <= gcd(B,a+B*x)
    == gcd(B,a)
    <= gcd(B,a*b)
    !! [gcd(B,a*b) == 1]
    == 1
    ]
    [gcd(p,a+B*x) == 1]

    !! [gcd(D,a+B*x)%p==0]
    [(a+B*x)%p==0]
    [gcd(p,a+B*x) == p]
    !! [gcd(p,a+B*x) == 1]
    _L
  #==>>:
  [gcd(D,a+B*x) == 1]
  #同理:
  [gcd(D,b+B*y) == 1]
  [gcd(D,(a+B*x)*(b+B*y)) == 1]

  !! [gcd(B,a*b) == 1]
  [gcd(B,(a+B*x)*(b+B*y)) == gcd(B,a*b) == 1]
  [gcd((B*D),(a+B*x)*(b+B*y)) == 1]
  [M:=(B*D)]
  [gcd(M,(a+B*x)*(b+B*y)) == 1]
  [vb:=pow((b+B*y),-1,M)]
  [(a+B*x) =[%M]= (a+B*x)*(b+B*y)*vb]
  [B*x =[%M]= ((a+B*x)*(b+B*y)*vb -a)]
  [x =[%D]= ((a+B*x)*(b+B*y)*vb -a)%M ///B]
  !! [x::uint%D]
  [x == ((a+B*x)*(b+B*y)*vb -a)%M ///B]
    #乘法可逆:都是 可逆元素/单位元素
===
[B,D::int][B,D>=2][@[p::prime][D%p==0] -> [B%p==0]][a,b,c::uint%(B*D)][gcd(B,a*b*c) == 1][d,x,y::uint%D]:
  [mul7nc_{B,D;a,b,c,d}(x,y) =[def]= ((c*(a+B*x)*(b+B*y) -c*a*b +B*d) %(B*D) ///B)]
    #乘法牜不可交换
    #未必支持结合律
  [M:=(B*D)]
  !! [gcd(B,a*b*c) == 1]
  !! [@[p::prime][D%p==0] -> [B%p==0]]
  [gcd(M,a*b*c) == 1]
  [vc:=pow(c,-1,M)]
  !! [gcd(M,(a+B*x)*(b+B*y)) == 1]
  [va:=pow((a+B*x),-1,M)]

  [mul7nc_{B,D;a,b,c,d}(x,y) == x]:
    [x == (c*(a+B*x)*(b+B*y) -c*a*b +B*d) %(B*D) ///B]
    [B*x == (c*(a+B*x)*(b+B*y) -c*a*b +B*d) %(B*D)]
    [B*x =[%M]= (c*(a+B*x)*(b+B*y) -c*a*b +B*d)]
    [vc*va*(B*x-B*d+c*a*b) =[%M]= (b+B*y)]
    [y =[%D]= (vc*va*(B*x-B*d+c*a*b) -b)%M ///B]
    [y == (vc*va*(B*x-B*d+c*a*b) -b)%M ///B]
        [y 是 x 的 右侧幺元] #oneR{x}
  #最大麻烦是:结合律
  # [(x*y)*z == x*(y*z)]
  [mul7nc_(mul7nc_(x,y),z) == ???]
  [mul7nc_(x,mul7nc_(y,z)) == ???]

  [mul7nc_(mul7nc_(x,y),z)
  == ((c*(a+B*mul7nc_(x,y))*(b+B*z) -c*a*b +B*d) %(B*D) ///B)
  == ((c*(a+B*((c*(a+B*x)*(b+B*y) -c*a*b +B*d) %(B*D) ///B))*(b+B*z) -c*a*b +B*d) %(B*D) ///B)
  ]
  [mul7nc_(x,mul7nc_(y,z))
  == ((c*(a+B*x)*(b+B*mul7nc_(y,z)) -c*a*b +B*d) %(B*D) ///B)
  == ((c*(a+B*x)*(b+B*((c*(a+B*y)*(b+B*z) -c*a*b +B*d) %(B*D) ///B)) -c*a*b +B*d) %(B*D) ///B)
  ]
  [mul7nc_(mul7nc_(x,y),z) == mul7nc_(x,mul7nc_(y,z))]
    <==>:
    [((c*(a+B*((c*(a+B*x)*(b+B*y) -c*a*b +B*d) %(B*D) ///B))*(b+B*z) -c*a*b +B*d) %(B*D) ///B) == ((c*(a+B*x)*(b+B*((c*(a+B*y)*(b+B*z) -c*a*b +B*d) %(B*D) ///B)) -c*a*b +B*d) %(B*D) ///B)]
    <==>:
    [((a+B*((c*(a+B*x)*(b+B*y) -c*a*b +B*d) %(B*D) ///B))*(b+B*z)) =[%M]= ((a+B*x)*(b+B*((c*(a+B*y)*(b+B*z) -c*a*b +B*d) %(B*D) ///B)))]
    <==>:
    [((a+((c*(a+B*x)*(b+B*y) -c*a*b +B*d) %(B*D)))*(b+B*z)) =[%M]= ((a+B*x)*(b+((c*(a+B*y)*(b+B*z) -c*a*b +B*d) %(B*D))))]
    <==>:
    [((a+(c*(a+B*x)*(b+B*y) -c*a*b +B*d))*(b+B*z)) =[%M]= ((a+B*x)*(b+(c*(a+B*y)*(b+B*z) -c*a*b +B*d)))]

    #####
    1111:
    [((a+(c*(a+B*x)*(b+B*y) -c*a*b +B*d))*(b+B*z)) =[%M]= ((a+B*x)*(b+(c*(a+B*y)*(b+B*z) -c*a*b +B*d)))]
    ==>>:
    [LHS.z.coeff
    == (a+(c*(a+B*x)*(b+B*y) -c*a*b +B*d))*B
    ]
    [RHS.z.coeff
    == (a+B*x)*c*(a+B*y)*B
    ]
    ==>>:
    [(a+(c*(a+B*x)*(b+B*y) -c*a*b +B*d))*B =[%M]= (a+B*x)*c*(a+B*y)*B]
        <==>:
        [(a+(c*(a+B*x)*(b+B*y) -c*a*b +B*d)) =[%D]= (a+B*x)*c*(a+B*y)]
        <==>:
        [(a+(-c*a*b +B*d)) =[%D]= (a+B*x)*c*(a+B*y) -c*(a+B*x)*(b+B*y)]
        <==>:
        [(a -c*a*b +B*d) =[%D]= c*(a+B*x)*(a-b)]
        <==>:
        [(a -c*a*b +B*d) =[%D]= (a-b) =[%D]= 0]
        <==>:
        [b =[%D]= a][B*d =[%D]= a*(c*a-1)]

    #####
    2222:
    [((a+(c*(a+B*x)*(b+B*y) -c*a*b +B*d))*(b+B*z)) =[%M]= ((a+B*x)*(b+(c*(a+B*y)*(b+B*z) -c*a*b +B*d)))]
    ==>>:
    [LHS.x.coeff
    == (c*B*(b+B*y)*(b+B*z))
    ]
    [RHS.x.coeff
    == B*(b+(c*(a+B*y)*(b+B*z) -c*a*b +B*d))
    ]
    ==>>:
    [(c*B*(b+B*y)*(b+B*z)) =[%M]= B*(b+(c*(a+B*y)*(b+B*z) -c*a*b +B*d))]
        <==>:
        [(c*(b+B*y)*(b+B*z)) =[%D]= (b+(c*(a+B*y)*(b+B*z) -c*a*b +B*d))]
        <==>:
        [(c*(b+B*y)*(b+B*z) -c*(a+B*y)*(b+B*z)) =[%D]= (b -c*a*b +B*d)]
        [c*(b-a)*(b+B*z) =[%D]= (b -c*a*b +B*d)]
        <==>:
        [(b -c*a*b +B*d) =[%D]= (b-a) =[%D]= 0]
        <==>:
        [b =[%D]= a][B*d =[%D]= a*(c*a-1)]
        #与前面相同

    #####
    3333:
    [((a+(c*(a+B*x)*(b+B*y) -c*a*b +B*d))*(b+B*z)) =[%M]= ((a+B*x)*(b+(c*(a+B*y)*(b+B*z) -c*a*b +B*d)))]
    ==>>:
    [LHS.y.coeff
    == (c*(a+B*x)*B*(b+B*z))
    ]
    [RHS.y.coeff
    == ((a+B*x)*c*B*(b+B*z))
    ]
    ==>>:
    [(c*(a+B*x)*B*(b+B*z)) =[%M]= ((a+B*x)*c*B*(b+B*z))]
        <==>:
        True
        useless


    #####
    4444:
    [((a+(c*(a+B*x)*(b+B*y) -c*a*b +B*d))*(b+B*z)) =[%M]= ((a+B*x)*(b+(c*(a+B*y)*(b+B*z) -c*a*b +B*d)))]
    ==>>:
    [LHS.常项
    == ((a+(c*(a)*(b) -c*a*b +B*d))*(b))
    == ((a+B*d)*b)
    == (a*b+B*d*b)
    ]
    [RHS.常项
    == ((a)*(b+(c*(a)*(b) -c*a*b +B*d)))
    == (a*(b+B*d))
    == (a*b+B*d*a)
    ]
    ==>>:
    [(a*b+B*d*b) =[%M]= (a*b+B*d*a)]
        <==>:
        [B*d*b =[%M]= B*d*a]
        [B*d*(b-a) =[%M]= 0]
        !! 上面: [b =[%D]= a][B*d =[%D]= a*(c*a-1)]
        <==>:
        True
        useless

    #####
  #==>>:
  [mul7nc_(mul7nc_(x,y),z) == mul7nc_(x,mul7nc_(y,z))]
    <==>:
    [b =[%D]= a][B*d =[%D]= a*(c*a-1)]

  [g:=gcd(D,B*d)]
  [Bdg := (B*d)///g]
  [Dg := D///g]
  [gcd(Dg,Bdg) == 1]

  [B*d =[%D]= a*(c*a-1)]:
    !! [gcd(D,a) == 1]
    [(c*a-1)%gcd(D,B*d) == 0]
    [(c*a-1)%g == 0]
    [ca1g := (c*a-1)///g]

    !! [B*d =[%D]= a*(c*a-1)]
    [Bdg =[%Dg]= a*ca1g]
    !! [gcd(Dg,Bdg) == 1]
    [gcd(Dg,a*ca1g) == 1]
    [gcd(Dg,ca1g) == 1]
    [gcd(D,c*a-1)==g==gcd(D,B*d)]
    [gcd(D,c*a-1) == gcd(D,B*d)]
    [gcd(D,c*a-1) %gcd(D,B) == 0]
    [(c*a-1) %gcd(D,B) == 0] #EQ__1:here
  [[B*d =[%D]= a*(c*a-1)] -> [gcd(D,c*a-1) == gcd(D,B*d)]]
  [[B*d =[%D]= a*(c*a-1)] -> [(c*a-1) %gcd(D,B) == 0]]

  [B*d =[%D]= a*(c*a-1)]:
    # 先设定d，再求a
    !! [gcd(D,c*a-1) == gcd(D,B*d)]
    !! [ca1g := (c*a-1)///g]
    [c*a == (1+g*ca1g)]
    [a == (1+g*ca1g)///c]
    ....
    ???
    失败:先设定d，再求a

  [gDB:=gcd(D,B)]
  [gDB > 1]
  [B*d =[%D]= a*(c*a-1)]:
    [gcd(B*d,D)
    !! [B*d =[%D]= a*(c*a-1)]
    == gcd(a*(c*a-1),D)
    !! [gcd(D,a) == 1]
    == gcd((c*a-1),D)
    ]
    [gcd(B*d,D) == gcd((c*a-1),D)]
    !! [gDB:=gcd(D,B)]
    [gcd(B*d,D) %gDB == 0]
    [gcd((c*a-1),D) %gDB == 0]
    [(c*a-1) %gDB == 0] # EQ__2:here

  [B*d =[%D]= a*(c*a-1)]:
    # 先设定a，再求d
    !! [(c*a-1) %gDB == 0] # EQ__2:goto
    [ka:=(c*a-1)///gDB]:
        [c*a==(1+ka*gDB)]
        [(1+ka*gDB)%c == 0]
        [ka*gDB =[%c]= -1]
        !! [gcd(B*D,c) == 1]
        [ka =[%c]= pow(-gDB,-1,c)]
        !! [a,c::uint%M]
        [0 <= c*a <= c*(M-1)]
            #[0 <= c*a <= (M-1)**2]
        !! [c*a==(1+ka*gDB)]
        [0 <= (1+ka*gDB) <= c*(M-1)]
        [-1 <= ka*gDB <= c*(M-1) -1]
        !! [gDB > 1]
        [0 <= ka <= (c*(M-1) -1)//gDB]
    [begin4ka:=pow(-gDB,-1,c)]
    [step4ka:=c]
    [end4ka:=1+(c*(M-1) -1)//gDB]
    [ka:<-range(begin4ka,end4ka,step4ka)]
        #range4ka
        # missing:[gcd(B,(1+ka*gDB)) == 1]
    [a:=(1+ka*gDB)///c]
    [c*a==(1+ka*gDB)]
    !! [gcd(B,c*a) == 1]
    [gcd(B,(1+ka*gDB)) == 1]

    [gcd(D,B*d)
    !! [gcd(D,c*a-1) == gcd(D,B*d)]
    == gcd(D,c*a-1)
    !! [c*a==1+ka*gDB]
    == gcd(D,ka*gDB)
    !! [gDB:=gcd(D,B)]
    == gcd(D///gDB,ka)*gDB
    ]
    [gcd(D,B*d) == gcd(D///gDB,ka)*gDB]
    [gcd(D///gDB,ka)*gDB
    == gcd(D,B*d)
    !! [gDB:=gcd(D,B)]
    => [gcd(D///gDB,(B///gDB)) == 1]
    == gcd(D///gDB,d)*gDB
    ]
    [gcd(D///gDB,ka)*gDB == gcd(D///gDB,d)*gDB]
    [gcd(D///gDB,ka) == gcd(D///gDB,d)]
    [gcd(D///gDB,d) == gcd(D///gDB,ka)]
    [gka := gcd(D///gDB,ka)]
    [gcd(D///gDB,d) == gka]
    [d%gka == 0]
    [(D///gDB)%gka == 0]
    [gcd(D///gDB///gka,d///gka) == 1]
    [coprime4kd := D///gDB///gka]
    [gcd(coprime4kd,d///gka) == 1]

    [kd:=d///gka]:
        !! [gcd(coprime4kd,d///gka) == 1]
        [gcd(coprime4kd,kd) == 1]
        [d==kd*gka]
        !! [d::uint%D]
        [0 <= d < D]
        [0 <= d <= D-1]
        [0 <= d///gka <= (D-1)//gka]
        [0 <= kd <= (D-1)//gka]
    初版有毛病:
        [kd:<-[0..=(D-1)//gka]][1 == gcd(kd,coprime4kd)]
        [d:=kd*gka]
            # ka随便取
            # [d:=kd{ka,随机}*gka{ka}]
    修正:
        !! [B*d =[%D]= a*(c*a-1)]
        [(B///gDB) * (d///gka) =[%(D///gDB///gka)]= a*((c*a-1)///gDB///gka)]
        [(B///gDB) * kd =[%coprime4kd]= a*(ka///gka)]

        !! [gcd(D///gDB,(B///gDB)) == 1]
        [gcd(coprime4kd,(B///gDB)) == 1]
        !! [gcd(coprime4kd,kd) == 1]
        [gcd(coprime4kd,(B///gDB)*kd) == 1]

        !! [gka := gcd(D///gDB,ka)]
        [gcd(D///gDB///gka,ka///gka) == 1]
        [gcd(coprime4kd,(ka///gka)) == 1]
        !! [gcd(D,a) == 1]
        [gcd(coprime4kd,a) == 1]
        [gcd(coprime4kd,a*(ka///gka)) == 1]

        !! [(B///gDB) * kd =[%coprime4kd]= a*(ka///gka)]
        !! [gcd(coprime4kd,(B///gDB)*kd) == 1]
        !! [gcd(coprime4kd,a*(ka///gka)) == 1]
        [kd =[%coprime4kd]= a*(ka///gka) * pow((B///gDB),-1,coprime4kd)]
        !! [0 <= kd <= (D-1)//gka]
        [end4kd := 1+(D-1)//gka]
        [begin4kd := a*(ka///gka) * pow((B///gDB),-1,coprime4kd) %coprime4kd]
        [step4kd := coprime4kd]
        [kd:<-range(begin4kd,end4kd,step4kd)]
            #range4kd

    #成功:先设定a，再求d
    ###########################
    # ^TypeError: (60, 81, 1, 31, 1)
    #       not [B*d =[%D]= a*(c*a-1)]
    debug:
    [B:=60][D:=81][a:=1][c:=31] =?=> [d:=1]
        [gDB==3]
        [ka==(c*a-1)///gDB==30/3==10]
        [gka == gcd(D///gDB,ka) == gcd(81/3,10) == 1]
        [coprime4kd == D///gDB///gka == 81/3/1 == 27]
        [d==1]:
            ??: [B*d =[%D]= a*(c*a-1)]
            ??: [60*1 =[%81]= 1*(31*1-1)]
            ??: [60 =[%81]= 30]
                毛病在于上述过程只确保:gcd 3
            ??: [20 =[%27]= 10]
            _L
    ###########################


[B,D::int][B,D>=2][@[p::prime][D%p==0] -> [B%p==0]][a,c::uint%(B*D)][gcd(B,a*c) == 1][d,x,y::uint%D][B*d =[%D]= a*(c*a-1)]:
  [mul7cm_{B,D;a,c,d}(x,y) =[def]= ((c*(a+B*x)*(a+B*y) -c*a*a +B*d) %(B*D) ///B)]
    #乘法牜可交换 <<== [a==b]
    #支持结合律
  [M:=(B*D)]
  !! [B*d =[%D]= a*(c*a-1)]
  [B*d +a =[%D]= c*a*a]
  [B*d -c*a*a =[%D]= -a]
  [T:=(B*d -c*a*a)%M]
  [T =[%D]= -a]
  [T =[%B]= -c*a*a]
  [mul7cm_(x,y) == ((c*(a+B*x)*(a+B*y) +T) %M ///B)]
  #.[mul7cm_(x,y)
  #.== ((c*(a+B*x)*(a+B*y) -c*a*a +B*d) %(B*D) ///B)
  #.== ((c*(a+B*x)*(a+B*y) -c*a*a%B -c*a*a//B*B +B*d) %(B*D) ///B)
  #.]
  [x::Group{mul7cm_}]:
    !! [mul7cm_(x,oneR) == x]
    [x == ((c*(a+B*x)*(a+B*oneR) +T) %M ///B)]
    [B*x =[%M]= (c*(a+B*x)*(a+B*oneR) +T)]
  @x. [B*x =[%M]= (c*(a+B*x)*(a+B*oneR) +T)]
    <==>:
        [
        [B =[%M]= c*B*(a+B*oneR)] # x.coeff
        [0 =[%M]= (c*a*(a+B*oneR) +T)] #常项
        ]
    <==>:
        [vaM := pow(a,-1,M)]
        [1 =[%D]= c*(a+B*oneR)]
        [-T*vaM =[%M]= c*(a+B*oneR)]
            !! [T =[%D]= -a]
            [-T*vaM =[%D]= 1]
            [1 =[%D]= c*(a+B*oneR)]
                即:前一式是冗余的
    <==>:
        [-T*vaM =[%M]= c*(a+B*oneR)]
    ==>>:
        [vcM := pow(c,-1,M)]
        [-T*vaM*vcM-a =[%M]= B*oneR]
        [B*oneR
        =[%M]= -T*vaM*vcM-a
        !! [T:=(B*d -c*a*a)%M]
        =[%M]= -(B*d -c*a*a)*vaM*vcM-a
        =[%M]= -B*d*vaM*vcM +c*a*a*vaM*vcM -a
        =[%M]= -B*d*vaM*vcM +a -a
        =[%M]= -B*d*vaM*vcM
        ]
        [B*oneR =[%M]= -B*d*vaM*vcM]
        [oneR =[%D]= -d*vaM*vcM]
        [oneR == (-d*vaM*vcM) %D]
  [oneR == (-d*vaM*vcM) %D]
  !! 乘法牜可交换
  [one == (-d*vaM*vcM) %D]
  !! [vaM := pow(a,-1,M)]
  !! [vcM := pow(c,-1,M)]
  [one == (-d*pow(a*c,-1,D)) %D]



  [x,y::Group{mul7cm_}][mul7cm_(x,y) == xy]:
    [xy == ((c*(a+B*x)*(a+B*y) +T) %M ///B)]
    [B*xy =[%M]= (c*(a+B*x)*(a+B*y) +T)]
    [(B*xy-T) =[%M]= (c*(a+B*x))*(a+B*y)]
    [(B*xy-T)*pow((c*(a+B*x)),-1,M) =[%M]= (a+B*y)]
    [(-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) =[%M]= (B*y)]

    [(-a +(B*xy-T)*pow((c*(a+B*x)),-1,M))
    =[%B]= (-a +(-T)*pow(c*a,-1,B))
    !! [T =[%B]= -c*a*a]
    =[%B]= (-a +(c*a*a)*pow(c*a,-1,B))
    =[%B]= (-a +a)
    =[%B]= 0
    ]
    [(-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) =[%B]= 0]
    !! [(-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) =[%M]= (B*y)]
    [y =[%D]= (-a +(B*xy-T)*pow((c*(a+B*x)),-1,M))///B]
    [y == (-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) %M ///B]
  [@[x,y::Group{mul7cm_}][mul7cm_(x,y) == xy] -> [y == (-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) %M ///B]]
  [div7cm_(xy,x) =[def]= (-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) %M ///B]
===
]]

'#'; __doc__ = r'#'

(5040, 480, 131, 11, 18)
#.>>> ops = Ops4mul7cm([2,3,5,7], (2**4*3**2*5*7, 2**5*3*5, 131, 11, 18))
#.>>> ops
#.Ops4mul7cm([2, 3, 5, 7], (5040, 480, 131, 11, 18))
>>> ops = Ops4mul7cm((2**4*3**2*5*7, 2**5*3*5, 131, 11, 18))
>>> ops
Ops4mul7cm((5040, 480, 131, 11, 18))
>>> ops.one
462
>>> ops._D_
480
>>> x = ops.std_arg_(1+2**16)
>>> y = ops.std_arg_(-1+2**61)
>>> z = ops.std_arg_(2567)
>>> xy = ops.mul7cm_(x, y)
>>> yz = ops.mul7cm_(y, z)
>>> xy_z = ops.mul7cm_(xy, z)
>>> x_yz = ops.mul7cm_(x, yz)
>>> vy = ops.inv7cm_(y)
>>> x
257
>>> y
31
>>> z
167
>>> xy
66
>>> yz
456
>>> xy_z
251
>>> x_yz
251
>>> vy
173
>>> xy_z == x_yz #结合律
True
>>> ops.one == ops.mul7cm_(ops.one, ops.one)
True
>>> x == ops.mul7cm_(x, ops.one)
True
>>> y == ops.mul7cm_(ops.one, y)
True
>>> xy == ops.mul7cm_(y, x) #交换律
True
>>> ops.one == ops.mul7cm_(vy, y)
True
>>> x == ops.mul7cm_(xy, vy)
True
>>> y == ops.div7cm_(xy, x)
True
>>> ops.one == ops.div7cm_(ops.one, ops.one)
True
>>> ops.one == ops.inv7cm_(ops.one)
True
>>> y == ops.inv7cm_(vy)
True

mul_order_of_
>>> from collections import Counter


#.>>> _ps4D_ = [2,3,5]
#>>> for x in range(ops._D_):
#...     print(x, ops.mul_order_of_(_ps4D_, x), sep=':')

>>> _ps4D_ = [2,3,5]
>>> j2ord = [ops.mul_order_of_(_ps4D_, x) for x in range(ops._D_)]
>>> c = Counter(j2ord)

#>>> c.most_common()
[(480, 128), (160, 64), (240, 64), (80, 32), (96, 32), (120, 32), (40, 16), (32, 16), (48, 16), (60, 16), (24, 8), (20, 8), (16, 8), (15, 8), (30, 8), (12, 4), (10, 4), (8, 4), (5, 4), (6, 2), (4, 2), (3, 2), (2, 1), (1, 1)]
>>> xo_pairs1 = sorted(c.items())
>>> xo_pairs1
[(1, 1), (2, 1), (3, 2), (4, 2), (5, 4), (6, 2), (8, 4), (10, 4), (12, 4), (15, 8), (16, 8), (20, 8), (24, 8), (30, 8), (32, 16), (40, 16), (48, 16), (60, 16), (80, 32), (96, 32), (120, 32), (160, 64), (240, 64), (480, 128)]
>>> from itertools import islice, accumulate, repeat
>>> group_order = ops._D_
>>> g = j2ord.index(group_order)
>>> g #本原根
1
>>> gs = list(accumulate(repeat(g, group_order), ops.mul7cm_))
>>> gs[0] == g
True
>>> gs[-1] == ops.one
True
>>> sorted(gs) == list(range(group_order))
True
>>> gs
[1, 260, 279, 58, 77, 336, 355, 134, 153, 412, 431, 210, 229, 8, 27, 286, 305, 84, 103, 362, 381, 160, 179, 438, 457, 236, 255, 34, 53, 312, 331, 110, 129, 388, 407, 186, 205, 464, 3, 262, 281, 60, 79, 338, 357, 136, 155, 414, 433, 212, 231, 10, 29, 288, 307, 86, 105, 364, 383, 162, 181, 440, 459, 238, 257, 36, 55, 314, 333, 112, 131, 390, 409, 188, 207, 466, 5, 264, 283, 62, 81, 340, 359, 138, 157, 416, 435, 214, 233, 12, 31, 290, 309, 88, 107, 366, 385, 164, 183, 442, 461, 240, 259, 38, 57, 316, 335, 114, 133, 392, 411, 190, 209, 468, 7, 266, 285, 64, 83, 342, 361, 140, 159, 418, 437, 216, 235, 14, 33, 292, 311, 90, 109, 368, 387, 166, 185, 444, 463, 242, 261, 40, 59, 318, 337, 116, 135, 394, 413, 192, 211, 470, 9, 268, 287, 66, 85, 344, 363, 142, 161, 420, 439, 218, 237, 16, 35, 294, 313, 92, 111, 370, 389, 168, 187, 446, 465, 244, 263, 42, 61, 320, 339, 118, 137, 396, 415, 194, 213, 472, 11, 270, 289, 68, 87, 346, 365, 144, 163, 422, 441, 220, 239, 18, 37, 296, 315, 94, 113, 372, 391, 170, 189, 448, 467, 246, 265, 44, 63, 322, 341, 120, 139, 398, 417, 196, 215, 474, 13, 272, 291, 70, 89, 348, 367, 146, 165, 424, 443, 222, 241, 20, 39, 298, 317, 96, 115, 374, 393, 172, 191, 450, 469, 248, 267, 46, 65, 324, 343, 122, 141, 400, 419, 198, 217, 476, 15, 274, 293, 72, 91, 350, 369, 148, 167, 426, 445, 224, 243, 22, 41, 300, 319, 98, 117, 376, 395, 174, 193, 452, 471, 250, 269, 48, 67, 326, 345, 124, 143, 402, 421, 200, 219, 478, 17, 276, 295, 74, 93, 352, 371, 150, 169, 428, 447, 226, 245, 24, 43, 302, 321, 100, 119, 378, 397, 176, 195, 454, 473, 252, 271, 50, 69, 328, 347, 126, 145, 404, 423, 202, 221, 0, 19, 278, 297, 76, 95, 354, 373, 152, 171, 430, 449, 228, 247, 26, 45, 304, 323, 102, 121, 380, 399, 178, 197, 456, 475, 254, 273, 52, 71, 330, 349, 128, 147, 406, 425, 204, 223, 2, 21, 280, 299, 78, 97, 356, 375, 154, 173, 432, 451, 230, 249, 28, 47, 306, 325, 104, 123, 382, 401, 180, 199, 458, 477, 256, 275, 54, 73, 332, 351, 130, 149, 408, 427, 206, 225, 4, 23, 282, 301, 80, 99, 358, 377, 156, 175, 434, 453, 232, 251, 30, 49, 308, 327, 106, 125, 384, 403, 182, 201, 460, 479, 258, 277, 56, 75, 334, 353, 132, 151, 410, 429, 208, 227, 6, 25, 284, 303, 82, 101, 360, 379, 158, 177, 436, 455, 234, 253, 32, 51, 310, 329, 108, 127, 386, 405, 184, 203, 462]


!! 有限交换群同构于循环群的直积
!! (2, 1) 即 只有一个元素满足[x=!=one][x**2==one]
=> 分解后只有一个偶阶循环群
!! [480 == 2**5*3*5]
=> 该偶阶循环群分量的阶%32==0


!! (480, 128) 即 存在本原根
=> 构造出来的乘法群是一个循环群
    这是碰巧还是必然？
    是碰巧:见:iter_find_noncyclic_group_opss5BDc_ -> Ops4mul7cm((30, 60, 1, 1, 0))
>>> group_order = 480
>>> ps4group_order = [2,3,5]
>>> info4group_order = prepare4mul_order_of_(group_order, ps4group_order)
>>> _mul_order_of_ = lambda x:mul_order_of_(info4group_order, is_one_, __rpow__, x)

[group:=ZZ%480] #加法群
>>> __rpow__ = lambda e,x:e*x%group_order
>>> is_one_ = (0).__eq__
>>> j2ord = [_mul_order_of_(x) for x in range(group_order)]
>>> c = Counter(j2ord)
>>> xo_pairs2 = sorted(c.items())
>>> xo_pairs2
[(1, 1), (2, 1), (3, 2), (4, 2), (5, 4), (6, 2), (8, 4), (10, 4), (12, 4), (15, 8), (16, 8), (20, 8), (24, 8), (30, 8), (32, 16), (40, 16), (48, 16), (60, 16), (80, 32), (96, 32), (120, 32), (160, 64), (240, 64), (480, 128)]
>>> xo_pairs2 == xo_pairs1
True

>>> ops = Ops4mul7cm((30, 60, 1, 1, 0))
>>> _ps4D_ = [2,3,5]
>>> j2ord = [ops.mul_order_of_(_ps4D_, x) for x in range(ops._D_)]
>>> c = Counter(j2ord)
>>> xo_pairs3 = sorted(c.items())
>>> xo_pairs3
[(1, 1), (2, 3), (3, 2), (5, 4), (6, 6), (10, 12), (15, 8), (30, 24)]

(30, 24) => 含 ZZ%30分量
=> 同构于 (ZZ%2, ZZ%30)
>>> group_order = 60
>>> ps4group_order = [2,3,5]
>>> info4group_order = prepare4mul_order_of_(group_order, ps4group_order)
>>> _mul_order_of_ = lambda x:mul_order_of_(info4group_order, is_one_, __rpow__, x)

[modulus:=31*3 = 93]
[phi(modulus) == 60 == 2**2*3*5]
[group:=ZZ%modulus]
>>> modulus = 93
>>> ps4modulus = [3,31]
>>> __rpow__ = lambda e,x:pow(x,e,modulus)
>>> is_one_ = (1).__eq__
>>> j2ord = [_mul_order_of_(x) for x in range(modulus) if not any(0 == x%p for p in ps4modulus)]
>>> c = Counter(j2ord)
>>> xo_pairs4 = sorted(c.items())
>>> xo_pairs4 == xo_pairs3
True
>>> xo_pairs4
[(1, 1), (2, 3), (3, 2), (5, 4), (6, 6), (10, 12), (15, 8), (30, 24)]




[phi(modulus) == 480 == 2**5*3*5]
    '/sdcard/0my_files/book/math/factorint/snd/The new book of prime number records(3ed)(1996)(Ribenboim).djvu'
    page41[66/567]
    [37 == len{n | [n:<-[1..]][phi(n) == 480]}]
    480 => 37个
    12 => 6个
    8 => 5个
    4 => 4个
    2 => 3个
    1 => 2个

[phi(modulus) == 480 == 2**5*3*5]
    手动计算:
    #8 => 5个
    [11*7*2**4 == 1232]
    [11*7*3*2**3 == 1848]
    [11*7*5*2**2 == 1540]
    [11*7*5*3 == 1155]
    [11*7*5*3*2 == 2310]

    12 => 6个
    [41*7*2**2 == 1148]
    [41*7*3 == 1148]
    [41*7*3*2 == 1148]
    [41*13 == 533]
    [41*13*2 == 1066]
    ... ...
    ==>>:
    view ../../python3_src/seed/math/valence_of_Euler_function.py

==>>:
>>> group_order = 480
>>> ps4group_order = [2,3,5]
>>> info4group_order = prepare4mul_order_of_(group_order, ps4group_order)
>>> _mul_order_of_ = lambda x:mul_order_of_(info4group_order, is_one_, __rpow__, x)

[modulus:=31*17 = 527]
[phi(modulus) == 480 == 2**5*3*5]
[group:=ZZ%modulus]
>>> modulus = 527
>>> ps4modulus = [17,31]
>>> __rpow__ = lambda e,x:pow(x,e,modulus)
>>> is_one_ = (1).__eq__
>>> j2ord = [_mul_order_of_(x) for x in range(modulus) if not any(0 == x%p for p in ps4modulus)]
>>> c = Counter(j2ord)
>>> sorted(c.items())
[(1, 1), (2, 3), (3, 2), (4, 4), (5, 4), (6, 6), (8, 8), (10, 12), (12, 8), (15, 8), (16, 16), (20, 16), (24, 16), (30, 24), (40, 32), (48, 32), (60, 32), (80, 64), (120, 64), (240, 128)]




[[
xxx:py_adhoc_call   script.设计冫乘法群牜不可交换   ,10:iter_paramss5BDc_  ='2**4*3**2*5*7'  ='2**5*3*5' =11 ='[2,3,5,7]'
py_adhoc_call   script.设计冫乘法群牜不可交换   ,10:iter_paramss5BDc_  ='2**4*3**2*5*7'  ='2**5*3*5' =11
    (5040, 480, 131, 11, 0)
    (5040, 480, 131, 11, 2)
    (5040, 480, 131, 11, 4)
    (5040, 480, 131, 11, 6)
    (5040, 480, 131, 11, 8)
    (5040, 480, 131, 11, 10)
    (5040, 480, 131, 11, 12)
    (5040, 480, 131, 11, 14)
    (5040, 480, 131, 11, 16)
    (5040, 480, 131, 11, 18)
]]
[[
py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(2,3)'  =6 =6 =1
    <NONE>
py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(2,3)'  =6 =6 =5
    <NONE>

py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(2,3)'  =12 =12 =1
    <NONE>

py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(3,)'  =3 =9 =1
    <NONE>

py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(2,3,5)'  =30 =30 =1
    <NONE>
py_adhoc_call   script.设计冫乘法群牜不可交换   ,4:iter_find_noncyclic_group_opss5BDc_  ='(2,3,5)'  =30 =60 =1
    Ops4mul7cm((30, 60, 1, 1, 0))
    Ops4mul7cm((30, 60, 1, 1, 2))
    Ops4mul7cm((30, 60, 1, 1, 4))
    Ops4mul7cm((30, 60, 1, 1, 6))
    ... ...
    ... ...

有限交换群可分解成循环群的直积
循环群的直积仍为循环群的充要条件是各分量循环群的阶两两互素
阶不含平方因子的有限交换群必然是循环群
非循环群的有限交换群的阶必然含平方因子

尝试素幂阶:
py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(3,)'  =3 =27 =1
    <NONE>
py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(3,)'  =3 =81 =1
    <NONE>
py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(2,3)'  =6 =81 =1
    <NONE>
py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BDc_  ='(2,3,5)'  =60 =81 =1
    <NONE>
py_adhoc_call   script.设计冫乘法群牜不可交换   ,4:iter_find_noncyclic_group_opss5BDc_  ='(2,3,5)'  =60 =81 =31
    <NONE>

    已修正:初版有毛病:
        # ^TypeError: (60, 81, 1, 31, 1)
        #       not [B*d =[%D]= a*(c*a-1)]

py_adhoc_call   script.设计冫乘法群牜不可交换   ,iter_find_noncyclic_group_opss5BD_  ='(3,)'  =3 =27
    <NONE>


尝试多素幂阶之积:
py_adhoc_call   script.设计冫乘法群牜不可交换   ,4:iter_find_noncyclic_group_opss5BDc_  ='(2,3)'  =6 =72 =1
    Ops4mul7cm((6, 72, 1, 1, 0))
    Ops4mul7cm((6, 72, 1, 1, 12))
    Ops4mul7cm((6, 72, 1, 1, 24))
    Ops4mul7cm((6, 72, 1, 1, 36))
    ... ...

py_adhoc_call   script.设计冫乘法群牜不可交换   ,4:iter_find_noncyclic_group_opss5BDc_  ='(2,3)'  =6 =12 =1
    Ops4mul7cm((6, 12, 1, 1, 0))
    Ops4mul7cm((6, 12, 1, 1, 2))
    Ops4mul7cm((6, 12, 1, 1, 4))
    Ops4mul7cm((6, 12, 1, 1, 6))
    ... ...


]]


py_adhoc_call   script.设计冫乘法群牜不可交换   @f
from script.设计冫乘法群牜不可交换 import *
]]]'''#'''
__all__ = r'''
IOps4mul7cm
    check_params__BDacd_
    Ops4mul7cm

prepare_range4ka_ex5BDc_
prepare_a_ex5BDc_gDB_ka_
iter_paramss5BDc_
iter_find_noncyclic_group_opss5BDc_

iter_cs5BD_
iter_paramss5BD_
iter_find_noncyclic_group_opss5BD_
'''.split()#'''
#iter_kds5coprime4kd_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge, check_uint_lt, check_tuple__len_eq
    from seed.math.II import II__p2e_ # II_mod, II, II__ft2e_, II__ft_e_pairs_, factorial_mod_
    from seed.math.gcd import gcd, gcd_many, are_coprime
    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
    from seed.helper.repr_input import repr_helper
    from seed.tiny_.containers import mk_tuple
    #from seed.types.FrozenDict import mk_FrozenDict
    #from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
    from seed.math.power.power_ import power_
    #def power_(mul_, may_inv_, may_is_zero_, is_one_, one, imay_group_order, e, x0, /):
    #    'mul_/(x->x->x) -> may inv_/(x->x) -> may is_zero_/(x->bool) -> is_one_/(x->bool) -> one/x -> imay_group_order/imay uint{>=1} -> e/int -> x0/x -> y/x # [y==x**e] # [zero**0 == 1]'
    from seed.math.mul_order_of_ import mul_order_of_, prepare4mul_order_of_
    from seed.math.perfect_div import perfect_div
    from seed.math.iter_coprime_uints_to__lt_ import iter_coprime_uints_to__lt_, iter_coprimes_mod_

#.    from itertools import islice
#.    from functools import cached_property
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

__all__

def iter_cs5BD_(B, D, /):
    'B -> D -> Iter c'
    # [B,D >= 2]
    # [B**D.bit_length()%D == 0]
    yield from iter_coprime_uints_to__lt_(B*D, B)
    return
    ##################
    # [0 <= c < B*D]
    # [gcd(B,c) == 1]
    ##################


def prepare_range4ka_ex5BDc_(B, D, c, /):
    'B -> D -> c -> (gDB, coprime4ca, range4ka)'
        #old:'B -> D -> c -> (gDB, range4ka)'
    #_check_params__BDc_(_params__BDc_:=(B,D,c))

    # [B,D >= 2]
    # [0 <= c < B*D]
    # [B**D.bit_length()%D == 0]
    # [gcd(B,c) == 1]

    gDB = gcd(D,B)
    # [gDB == gcd(D,B)]
    assert gDB > 1
    #bug:coprime4ca = perfect_div(B, pow(gDB, B.bit_length(), B))
    coprime4ca = perfect_div(B, gcd(B, pow(gDB, B.bit_length(), B)))

    M = B*D
    begin4ka = pow(-gDB,-1,c)
    step4ka = c
    end4ka = 1+(c*(M-1) -1)//gDB
    range4ka = range(begin4ka,end4ka,step4ka)
    #return (gDB, range4ka)
    return (gDB, coprime4ca, range4ka)
    # [ka =[%step4ka]= begin4ka]
    # [ka =[%c]= (-gDB)**-1%c]
    # [ka*gDB =[%c]= -1]
    # [(1+ka*gDB)%c == 0]

    # [0 <= ka <= (c*(M-1) -1)//gDB]
    # [0 <= ka*gDB <= (c*(M-1) -1)//gDB *gDB <= (c*(M-1) -1)]
    # [1 <= 1+ka*gDB <= c*(M-1)]
    # [c*a == 1+ka*gDB]:
    #   [1 <= c*a <= c*(M-1)]
    #   [c*a =!= 0]
    #   [c =!= 0]
    #   !! [0 <= c < B*D]
    #   [1 <= c < M]
    #   !! [1 <= c*a <= c*(M-1)]
    #   [1 <= a <= (M-1)]
    #   [1 <= a < M]
    # [c*a == 1+ka*gDB] => [1 <= a < M][1 <= c < M]


    # [coprime4ca == B///gcd(B, gDB**B.bit_length()%B)]

    # [gcd(gDB, (1+ka*gDB)) == 1]
    # [gcd(B, (1+ka*gDB)) == gcd(B///gDB, (1+ka*gDB)) == gcd(B///gcd(B, gDB**B.bit_length()%B), (1+ka*gDB)) == gcd(coprime4ca, (1+ka*gDB))]
    # [gcd(B, (1+ka*gDB)) == gcd(coprime4ca, (1+ka*gDB))]



    ##################
    # [(1+ka*gDB)%c == 0]
    # [c*a == 1+ka*gDB] => [1 <= a < M][1 <= c < M]  #<<==range4ka
    # [gcd(B, (1+ka*gDB)) == gcd(coprime4ca, (1+ka*gDB))]
    # missing:[gcd(B,(1+ka*gDB)) == 1]
    ##################
def prepare_a_ex5BDc_gDB_ka_(B, D, c, gDB, ka, /):
    'B -> D -> c -> gDB -> ka -> (a, gka, range4kd)'
        #old:'B -> D -> c -> gDB -> ka -> (a, gka, coprime4kd, range4kd)'
    # [B,D >= 2]
    # [0 <= c < B*D]
    # [B**D.bit_length()%D == 0]
    # [gcd(B,c) == 1]
    # [gDB == gcd(D,B)]
    # [(1+ka*gDB)%c == 0]
    # [c*a == 1+ka*gDB] => [1 <= a < M][1 <= c < M]  #<<==range4ka
    # [gcd(B,(1+ka*gDB)) == 1] #!!!!

    #gDB = gcd(D,B)
    assert gDB > 1

    # !! [(1+ka*gDB)%c == 0]
    #a = perfect_div((1+ka*gDB), c)
    a = (1+ka*gDB)//c
    assert c*a == (1+ka*gDB), ((B,D,c,gDB,ka), (a, c*a, (1+ka*gDB)))
        # ^AssertionError: ((5040, 480, 11, 240, 5), (109, 1199, 1201))
    # [c*a == 1+ka*gDB]
    # !! [c*a == 1+ka*gDB] => [1 <= a < M][1 <= c < M]  #<<==range4ka
    # [1 <= a < M]
    # [1 <= c < M]

    # !! [c*a == 1+ka*gDB]
    # !! [gcd(B,(1+ka*gDB)) == 1]
    # [gcd(B,c*a) == 1]
    # [gcd(B,a) == 1]
    # [gcd(D,a) == 1]


    #gka = gcd(tmp:=perfect_div(D,gDB), ka)
    #coprime4kd = perfect_div(tmp,gka)
    gka = gcd(tmp:=D//gDB, ka)
    coprime4kd = tmp//gka
    assert D == coprime4kd * gka * gDB
    # [D == coprime4kd * gka * gDB]
    # [gka == gcd(D///gDB, ka) == gcd(coprime4kd * gka, ka)]
    # [1 == gcd(coprime4kd, ka///gka)]

    # !! [gcd(D,a) == 1]
    # [1 == gcd(coprime4kd, a)]


    # !! [gDB == gcd(D,B)]
    # [1 == gcd(D///gDB, B///gDB)]
    # [1 == gcd(D///gDB///gka, B///gDB)]
    # [1 == gcd(coprime4kd, B///gDB)]
    begin4kd = a*perfect_div(ka,gka) * pow(perfect_div(B,gDB),-1,coprime4kd) %coprime4kd
    end4kd = 1+(D-1)//gka
    step4kd = coprime4kd
    #bug:初版:range4kd = range(0, 1+(D-1)//gka)
    range4kd = range(begin4kd,end4kd,step4kd)
    #return (a, gka, coprime4kd, range4kd)
    return (a, gka, range4kd)
    # [kd %coprime4kd == begin4kd]
    # [kd =[%coprime4kd]= a * (ka///gka) * (B///gDB)**-1]
    # !! [1 == gcd(coprime4kd, a)]
    # !! [1 == gcd(coprime4kd, ka///gka)]
    # !! [1 == gcd(coprime4kd, B///gDB)]
    # [1 == gcd(coprime4kd, kd)]

    # !! [kd =[%coprime4kd]= a * (ka///gka) * (B///gDB)**-1]
    # [kd*(B///gDB) =[%coprime4kd]= a * (ka///gka)]
    # [kd*(B///gDB)*gka*gDB =[%(coprime4kd*gka*gDB)]= a * (ka///gka)*gka*gDB]
    # !! [D == coprime4kd * gka * gDB]
    # [B*(kd*gka) =[%D]= a * (ka*gDB)]
    # !! [c*a == 1+ka*gDB]
    # [B*(kd*gka) =[%D]= a*(c*a-1)]
    # [d==kd*gka] => [B*d =[%D]= a*(c*a-1)]


    # [0 <= kd <= (D-1)//gka]
    # [0 <= kd*gka <= (D-1)//gka *gka <= D-1]
    # [d==kd*gka] => [0 <= d < D]

    ##################
    # [1 <= a < M]
    # [gcd(B,c*a) == 1]
    # [d==kd*gka] => [0 <= d < D][B*d =[%D]= a*(c*a-1)]
    ##################
def __():
  def iter_kds5coprime4kd_(coprime4kd, range4kd, /):
    'coprime4kd -> range4kd -> Iter kd'
    for kd in range4kd:
        if are_coprime(kd, coprime4kd):
            #d = kd*gka
            yield kd



def iter_paramss5BD_(B, D, /, *, params_vs_ops=False):
    for c in iter_cs5BD_(B, D):
        yield from iter_paramss5BDc_(B, D, c, params_vs_ops=params_vs_ops)
def iter_paramss5BDc_(B, D, c, /, *, params_vs_ops=False):
    #def iter_paramss5BDc_(B, D, c, _ps4B_=None, /):
    'B -> D -> c -> Iter _params__BDacd_/(B,D,a,c,d)'
    # [B,D >= 2]
    # [0 <= c < B*D]
    # [B**D.bit_length()%D == 0]
    # [gcd(B,c) == 1]



    #.to_check = not _ps4B_ is None
    #.if to_check:
    #.    _ps4B_ = mk_tuple(_ps4B_)

    (gDB, coprime4ca, range4ka) = prepare_range4ka_ex5BDc_(B, D, c)
    ##################
    # [(1+ka*gDB)%c == 0]
    # [c*a == 1+ka*gDB] => [1 <= a < M][1 <= c < M]  #<<==range4ka
    # [gcd(B, (1+ka*gDB)) == gcd(coprime4ca, (1+ka*gDB))]
    # missing:[gcd(B,(1+ka*gDB)) == 1]
    ##################


    for ka in range4ka:
        if not are_coprime(coprime4ca, 1+ka*gDB):continue
            #if not are_coprime(B, 1+ka*gDB):continue
        # [gcd(coprime4ca,(1+ka*gDB)) == 1]
        # !! [gcd(B, (1+ka*gDB)) == gcd(coprime4ca, (1+ka*gDB))]
        # [gcd(B,(1+ka*gDB)) == 1]

        (a, gka, range4kd) = prepare_a_ex5BDc_gDB_ka_(B, D, c, gDB, ka)
        ##################
        # [1 <= a < M]
        # [gcd(B,c*a) == 1]
        # [d==kd*gka] => [0 <= d < D][B*d =[%D]= a*(c*a-1)]
        ##################
        for kd in range4kd:
            #for kd in iter_kds5coprime4kd_(coprime4kd, range4kd):
            d = kd*gka
            # [d == kd*gka]
            # !! [d==kd*gka] => [0 <= d < D][B*d =[%D]= a*(c*a-1)]
            # [0 <= d < D][B*d =[%D]= a*(c*a-1)]
            # [1 <= a < M]
            # [gcd(B,c*a) == 1]
            # [B,D >= 2]
            # [0 <= c < B*D]
            # [B**D.bit_length()%D == 0]
            _params__BDacd_ = (B,D,a,c,d)
            #.if to_check:
            #.    ops = Ops4mul7cm(_ps4B_, _params__BDacd_)
            #.    _ps4B_ = ops.___ps4B___
            if params_vs_ops:
                ops = Ops4mul7cm(_params__BDacd_)
                yield ops
            else:
                check_params__BDacd_(_params__BDacd_)
                yield _params__BDacd_

            # ^TypeError: (60, 81, 1, 31, 1)
            #       not [B*d =[%D]= a*(c*a-1)]

def iter_find_noncyclic_group_opss5BD_(_ps4D_, B, D, /):
    for c in iter_cs5BD_(B, D):
        yield from iter_find_noncyclic_group_opss5BDc_(_ps4D_, B, D, c)
#xxx:def iter_find_noncommutative_group_opss5BDc_(_ps4D_, B, D, c, /):
def iter_find_noncyclic_group_opss5BDc_(_ps4D_, B, D, c, /):
    # acyclic vs noncyclic
    '-> Iter Ops4mul7cm #eg:Ops4mul7cm((30, 60, 1, 1, 0))'
    group_order = D
    ps4group_order = _ps4D_
    for ops in iter_paramss5BDc_(B, D, c, params_vs_ops=True):
        ops.mul_order_of_
        if not any(group_order==ops.mul_order_of_(ps4group_order, x) for x in range(group_order)):
            yield ops

def __():
  def check_params__BDacd_(_p2e4B_, _p2e4D_, _params__BDacd_, /):
    check_tuple__len_eq(5, _params__BDacd_)
    (B,D,a,c,d) = _params__BDacd_
    check_int_ge(2, B)
    check_int_ge(2, D)
    if not all(e > 0 for e in _p2e4B_.values()):raise TypeError
    if not all(e > 0 for e in _p2e4D_.values()):raise TypeError
    if not II__p2e_(_p2e4B_) == B:raise TypeError
    if not II__p2e_(_p2e4D_) == D:raise TypeError
    if not _p2e4D_.keys() <= _p2e4B_.keys():raise TypeError
    # [@[p::prime][D%p==0] -> [B%p==0]]

    M = B*D
    check_uint_lt(M, a)
    check_uint_lt(M, c)
    check_uint_lt(D, d)
    if not are_coprime(B, a*c):raise TypeError

    if not (B*d -a*(c*a-1)) %D == 0:raise TypeError
    # [B*d =[%D]= a*(c*a-1)]

def check_params__BDacd_(_params__BDacd_, /):
    check_tuple__len_eq(5, _params__BDacd_)
    (B,D,a,c,d) = _params__BDacd_
    check_int_ge(2, B)
    check_int_ge(2, D)
    if not 0 == pow(B, 1<<D.bit_length(), D):raise TypeError
    # [@[p::prime][D%p==0] -> [B%p==0]]

    M = B*D
    check_uint_lt(M, a)
    check_uint_lt(M, c)
    check_uint_lt(D, d)
    if not are_coprime(B, a*c):raise TypeError

    if not (B*d -a*(c*a-1)) %D == 0:raise TypeError(_params__BDacd_)
    # [B*d =[%D]= a*(c*a-1)]

def _check_params__BDc_(_params__BDc_, /):
    check_tuple__len_eq(3, _params__BDc_)
    (B,D,c) = _params__BDc_
    check_int_ge(2, B)
    check_int_ge(2, D)
    if not 0 == pow(B, 1<<D.bit_length(), D):raise TypeError
    # [@[p::prime][D%p==0] -> [B%p==0]]

    M = B*D
    check_uint_lt(M, c)
    if not are_coprime(B, c):raise TypeError



class IOps4mul7cm(ABC):
    r'''[[[
[B,D::int][B,D>=2][@[p::prime][D%p==0] -> [B%p==0]][a,c::uint%(B*D)][gcd(B,a*c) == 1][d,x,y::uint%D][B*d =[%D]= a*(c*a-1)]:
  [mul7cm_{B,D;a,c,d}(x,y) =[def]= ((c*(a+B*x)*(a+B*y) -c*a*a +B*d) %(B*D) ///B)]
    #乘法牜可交换
    #支持结合律
  [M:=(B*D)]
  [T:=(B*d -c*a*a)%M]
  [one == (-d*pow(a*c,-1,D)) %D]
  [div7cm_(xy,x) =[def]= (-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) %M ///B]
  [mul7cm_(x,y) == ((c*(a+B*x)*(a+B*y) +T) %M ///B)]
    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def _params__BDacd_(sf, /):
        '-> (B,D,a,c,d)'
    #.@property
    #.@abstractmethod
    #.def _p2e4B_(sf, /):
    #.    '-> {prime:exp{>=2}} # [II__p2e_(_p2e4B_) == B]'
    #.@property
    #.@abstractmethod
    #.def _p2e4D_(sf, /):
    #.    '-> {prime:exp{>=2}} # [II__p2e_(_p2e4D_) == D]'
    @CachedProperty
    def one(sf, /):
        '-> uint%D{@x. [x*1==x]}'
        # [one == (-d*pow(a*c,-1,D)) %D]
        (B,D,a,c,d) = sf._params__BDacd_
        one = (-d*pow(a*c,-1,D)) %D
        return one
    @CachedProperty
    def _params__MT_(sf, /):
        '-> (M,T)'
        (B,D,a,c,d) = sf._params__BDacd_
        M = B*D
        T = (B*d -c*a*a)%M
        return (M,T)
    @CachedProperty
    def _D_(sf, /):
        '-> D/uint'
        (B,D,a,c,d) = sf._params__BDacd_
        return D
    def std_arg_(sf, i, /):
        'i/int -> x/uint%D'
        return i%sf._D_
    def mul7cm_(sf, x, y, /):
        'x/uint%D -> y/uint%D -> (x*y)/uint%D'
        # [mul7cm_(x,y) == ((c*(a+B*x)*(a+B*y) +T) %M ///B)]
        (B,D,a,c,d) = sf._params__BDacd_
        (M,T) = sf._params__MT_
        check_uint_lt(D, x)
        check_uint_lt(D, y)
        xy = ((c*(a+B*x)*(a+B*y) +T) %M //B)
        assert 0 <= xy < D
        return xy
    def div7cm_(sf, xy, x, /):
        'xy/uint%D -> x/uint%D -> y/uint%D{[x*y==xy]}'
        # [div7cm_(xy,x) =[def]= (-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) %M ///B]
        (B,D,a,c,d) = sf._params__BDacd_
        (M,T) = sf._params__MT_
        check_uint_lt(D, xy)
        check_uint_lt(D, x)
        y = (-a +(B*xy-T)*pow((c*(a+B*x)),-1,M)) %M //B
        assert 0 <= y < D
        return y
    def inv7cm_(sf, x, /):
        'x/uint%D -> y/uint%D{[x*y==one]}'
        return sf.div7cm_(sf.one, x)

    def is_one_(sf, x, /):
        'x/uint%D -> bool'
        return x == sf.one
        return sf.std_arg_(x) == sf.one
    def rpow7cm_(sf, exp, x, /):
        'exp/int -> x/uint%D -> y/uint%D # [x**exp == y]'
        check_type_is(int, exp)
        #def power_(mul_, may_inv_, may_is_zero_, is_one_, one, imay_group_order, e, x0, /):
        return power_(sf.mul7cm_, sf.inv7cm_, None, sf.is_one_, sf.one, sf._D_, exp, x)

    def mul_order_of_(sf, _ps4D_, x, /):
        '_ps4D_/[prime] -> x/uint%D -> k/uint%D # [II(_ps4D_)**+oo%D == 0][k == min{k | [x**k==one]}]'
        #def mul_order_of_(sf, _p2e4D_, x, /):
        #    '_p2e4D_/{prime:exp{>=2}} -> x/uint%D -> k/uint%D # [II__p2e_(_p2e4D_) == D][k == min{k | [x**k==one]}]'
        #_ps4D_ = _p2e4D_.keys()
        group_order = sf._D_
        ps4group_order = _ps4D_
        info4group_order = prepare4mul_order_of_(group_order, ps4group_order)
        __rpow__ = sf.rpow7cm_
        return mul_order_of_(info4group_order, sf.is_one_, __rpow__, x)


class Ops4mul7cm(IOps4mul7cm):
    'Ops4mul7cm(_ps4B_, _params__BDacd_)'
    ___no_slots_ok___ = True
    def __init__(sf, _params__BDacd_, /):
        #.def __init__(sf, _ps4B_, _params__BDacd_, /):
        #._ps4B_ = mk_tuple(_ps4B_)
        _params__BDacd_ = mk_tuple(_params__BDacd_)
        check_params__BDacd_(_params__BDacd_)
        #_params__BDacd_ = (B,D,a,c,d)
        #.(B,D,a,c,d) = _params__BDacd_
        #._p2e4B_ = mk_FrozenDict(complete_factor_pint_via_trial_division(_ps4B_, B))
        #._p2e4D_ = mk_FrozenDict(complete_factor_pint_via_trial_division(_ps4B_, D))
        #.check_params__BDacd_(_p2e4B_, _p2e4D_, _params__BDacd_)

        #.ps4B = mk_tuple(sorted(_p2e4B_))
        #.if not _ps4B_ in [ps4B]:
        #.    _ps4B_ = ps4B

        #.sf.__ps4B = _ps4B_
        #.sf.__p2e4B = _p2e4B_
        #.sf.__p2e4D = _p2e4D_
        sf.__params__BDacd = _params__BDacd_
    def __repr__(sf, /):
        #._ps4B_ = sf.__ps4B
        #.return repr_helper(sf, [*_ps4B_], sf._params__BDacd_)
        return repr_helper(sf, sf._params__BDacd_)
    #.@property
    #.def ___ps4B___(sf, /):
    #.    '-> [prime]'
    #.    return sf.__ps4B

    #.@property
    #.@override
    #.def _p2e4B_(sf, /):
    #.    '-> {prime:exp{>=2}} # [II__p2e_(_p2e4B_) == B]'
    #.    return sf.__p2e4B
    #.@property
    #.@override
    #.def _p2e4D_(sf, /):
    #.    '-> {prime:exp{>=2}} # [II__p2e_(_p2e4D_) == D]'
    #.    return sf.__p2e4D


    @property
    @override
    def _params__BDacd_(sf, /):
        '-> (B,D,a,c,d)'
        return sf.__params__BDacd












__all__
from script.设计冫乘法群牜不可交换 import *
