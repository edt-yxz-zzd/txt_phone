r'''[[[[[
see:
    view others/www.txt
        http://www.jjj.de/mathdata/
          Tables of mathematical data
        下载的压缩包(mathdata+src+dox)
            wget https://www.jjj.de/fxt/fxt-2022.04.13.tar.gz
                2MB -> 13MB

##e script/primitive_irreducible_polynomial.py
e script/gf__enumerate_primitive_irreducible_polynomials.py


[[最简模乘法囗公式:
[t>=0][degree f <= degree g <= 2*degree f -(t+1)][m==degree f]:
  [degree f >= (t+1)]
  [(q,r) := g/%f]
  [g == q*f + r]
  [degree r < degree f][degree f + degree q == degree g]
  [degree q = degree g % degree f = degree g - degree f <= degree f -(t+1)]
  [let ft(x) := f(x)%x**(t+1)]
  [degree ft <= t]
  [g == q*f + r == q*(f-ft) + (r+q*ft)]
  [degree (q*ft) = degree q + degree ft <= (degree f -(t+1)) +t == degree f -1]
  [degree (r + q*ft) <= max{degree r, degree(q*ft)} == degree f -1]
  [g%/(f-ft) == (q, r+q*ft)]
  [let (q_,r_) := g%/(f-ft)]
  [g%/f = (q,r) == (q_, r_ - q_*ft)]
  #注意:上面[t>=0]，下面[t>=1]
  [monic trinomial f][degree ft == t >= 1]:
    [f(x) == x**m + h0*x + f0]
    [m == degree f >= (t+1)]
    [g%/(f-ft) == g/%x**m == (high(m,g), low(m,g))]
    [g%/f == (q, r) == (q_, r_ - q_*ft) == (high(m,g), low(m,g) - high(m,g)*ft)]
      #完美！
      #最简模乘法囗公式
  模乘法 中 [g(x) = a(x)*b(x)，求g(x)%f(x)][degree a < m-1][degree b <= m-1][degree g <= 2*m-2]:
    #其实[t>1]也行，先高位折叠至[degree g <= 2*m -(t+1)]，最多折叠(t-1)位，串行耗时长
    [choose t==1]
    ==>>最佳模版: [m,1,0]
    [%2]情形:
      #https://www.jjj.de/mathdata/all-trinomial-irredpoly-short.txt
      #or:view /sdcard/Download/wget_/fxt/data/all-lowblock-irredpoly-short.txt
      #view /sdcard/Download/wget_/fxt/data/all-trinomial-irredpoly-short.txt
      # [m <= 399]:只有17个m相应 的 三项式 不可约
      #     不可约17:[2,3,4,  6,7,  9,15,22,28,30,46,60,63,127,153,172,303]
      #
      #view /sdcard/Download/wget_/fxt/data/all-trinomial-primpoly-short.txt
      # [m <= 399]:只有11个m相应 的 三项式 本原不可约
      #     [2,3,4,  6,7,  -9,15,22,-28,-30,-46,60,63,127,153,-172,-303]
      #     本原不可约11:[2,3,4,  6,7,  15,22,60,63,127,153]
      #     非本原不可约6:[9,28,30,46,172,303]
      #
]]

[[
ZZ[x]%p
  分解 (x**(p**m) - x)
  bug:???[(x**(p**(m+1)) - x)%(x**(p**m) - x) == 0]???
    #bug:???[(x**(p**(m+1)-1) - 1)%(x**(p**m-1) - 1) == 0]
    [(x**2**3-x)%(x**2**2-x) =!= 0] ==>> bug!!!

  [(x**(p**(m*n)) - x)%(x**(p**m) - x) == 0]
    <<== @x. [x**(p**m) = x] -> [x**(p**(m*n)) == (x**(p**m))**(p**(m*(n-1))) = (x)**(p**(m*(n-1))) == ... = (x)**(p**(m*1)) = x]
    即 所有 解 被包含 #两者 首项系数皆为1
    [m%n==0] <==> [GF(p**n) <= GF(p**m)]

  [all_primes =[def]= {p <- [1..] | [is_prime p]}]

  定义:[all_prime_factors_of :: pint -> 2**all_primes]
    [all_prime_factors_of i =[def]= {p <- [1..=i] | [is_prime p]}]

  定义:[all_divisors_of :: pint -> {pint}]
    [all_divisors_of i =[def]= {d <- [1..=i] | [i%d==0]}]

  定义:[max_height_of_prime_tower_ :: @[p <- all_primes] -> uint -> Either +oo uint]
    [max_height_of_prime_tower_ p i =[def]= if i==0 then +oo else
      max{e <- [0..] | [i%p**e==0]}
      ]

  定义:[mu :: pint -> {-1,0,+1}]
    [mu i =[def]= let ps := (all_prime_factors_of i) in
      if [i =!= II ps]/或/[?[p<-all_primes] -> [i%p**2==0]] then 0 else
      #squarefree
      if len ps %2 == 0
      then +1 else -1
      ]

  定义:[phi :: pint -> uint]
    [phi i =[def]= len {d <- [1..=i] | [gcd(d,i)==1]}]
    [phi i == i*II~ (1-1/p) ~{p<-all_prime_factors_of i}]

  下面的主要公式有：[
    #首项系数为一的多项式总数囗公式
        #多项式一根求根所在不可约因子的根集的公式
        #根集求多项式囗公式
    #首项系数为一的不可约多项式总数囗公式
        # 不可约多项式一根求根集囗公式
    #首项系数为一的本原不可约多项式总数囗公式
        # 本原不可约多项式一根求同次其他本原不可约多项式根集囗公式
            # 本原不可约多项式求同次其他本原不可约多项式囗公式 <<== 本原不可约多项式一根求同次其他本原不可约多项式根集囗公式+根集求多项式囗公式
        # 本原不可约多项式一根求同次非本原不可约多项式根集囗公式
            # 本原不可约多项式求同次非本原不可约多项式囗公式 <<== 本原不可约多项式一根求同次非本原不可约多项式根集囗公式+根集求多项式囗公式
  ]

  [%p][m::pint]:
    [GF(p**m) == roots_of (x**p**m - x)]

    [(可约+不可约)多项式 g][degree g==m]:
      [所有degree为m的 首项系数为一的 (可约+不可约)多项式 的 总数 == p**m]
          #首项系数为一的多项式总数囗公式

      !![(a+b)**p == a**p + b**p]
      [g(x)**p == g(x**p)]
      [@a. [g(a)==0] -> @[i<-[0..]] -> [g(a**p**i)==0]]
        #多项式一根求根所在不可约因子的根集的公式

      [let rs := roots_of g]
      [@[rs <- 2**GF(p**m)] -> [let g(z) == II {z-r | [r <- rs]}] -> [roots_of g == rs]]
        #根集求多项式囗公式



    [(本原+非本原)不可约多项式 h][degree h==m]:
      [GF(p**m) ~=~ ZZ[x]%p%h(x)]
        #the degree-m field generating irreducible polynomial
        #   ?次数为m的 域生成用的 不可约多项式?
        #
      [所有degree为m的 (本原+非本原)不可约多项式 的 根 的集合
        == {a <- GF(p**m) | [@[n <- [1..<m]] -> [m%n==0] -> [not$ a <- GF(p**n)]]}
        == {a <- GF(p**m) | [@[n <- [1..<m]] -> [m%n==0] -> [is_prime (m/n)] -> [not$ a <- GF(p**n)]]}
        == {a <- GF(p**m) | [@[n <- [1..<m]] -> [m%n==0] -> [is_prime (m/n)] -> [a**(p**n) =!= a]]}
        == {a <- GF(p**m) | [@[n <- [1..<m]] -> [a**(p**n) =!= a]]}
        ]
      [所有degree为m的 首项系数为一的 (本原+非本原)不可约多项式 的 总数
        == 所有degree为m的 首项系数为一的 (本原+非本原)不可约多项式 的 根 的集合 的规模/m
        # == p**m - sum~ p**n ~{...} + 补上重复删除的...
        == sum~ mu(m/d)* p**d ~{d <- all_divisors_of m}/m
          #首项系数为一的不可约多项式总数囗公式
        ]

      [@a. [h(a)==0]]:
        [@[n <- [1..<m]] -> [a**(p**n) =!= a]]
        [let rs := {a**(p**n) | [@n <- [0..<m]]}]
        [len rs == m]
          #???why???
          #!!非零元素 构成 乘法群
          #根的阶 整除 (p**m-1)
          #假设 根的阶 整除 (p**d-1)，d为m真因子
          #则 根**p**d=根，即 degree(gcd(h(x), x**p**d-x) <- [1..=d]
          #     h可约，矛盾
          #
        [roots_of h == rs]
      [@a. [h(a)==0] -> [roots_of h == {a**(p**n) | [@n <- [0..<m]]}]]
        # 不可约多项式一根求根集囗公式

    [本原不可约多项式 f][degree f==m]:
      # 定义: 本原不可约多项式 f <==> (f 根 为 非零乘法群 的 生成子)
      大前提[m>=1]
        [m==1]:
          [GF(p**m) ~=~ ZZ%p]
          [f x = x - i]where[i 是 ZZ%p\-\0 的 本原根/生成子]
          与[m>=2]的处理方式完全相同

      定义:[本原不可约多项式 f]
        <==> [@[a <- GF(p**m)] -> [f(a)==0] -> [GF(p**m)\-\{0} == {a**i | [@i <- [1..<p**m]]}]]
        <==> [@[d <- all_divisors_of(p**m-1)] -> [d=!=(p**m-1)] -> [x**d % f(x) =!= 1]]
        <==> [@[pd <- all_prime_factors_of(p**m-1)] -> [x**((p**m-1)/pd) % f(x) =!= 1]]

      [所有degree为m的 首项系数为一的 本原不可约多项式 的 总数
        == 所有degree为m的 首项系数为一的 本原不可约多项式 的 根 的集合 的规模/m
        == GF(p**m)非零元素 构成的 乘法群 的生成子 的规模/m
        == phi(p**m-1)/m
          #首项系数为一的本原不可约多项式总数囗公式
        ]

      [@[a <- GF(p**m)] -> [f(a)==0] -> @[u <- [1..<p**m-1]] -> [not$ all_prime_factors_of(u) <= {p}]{#避开f的根集#} -> [gcd(u,p**m-1)==1]{#生成子#} -> [{(a**u)**(p**i) | [@i <- [0..<m]]} 是 其他 degree为m的 不等于f的 本原不可约多项式 的 根集]]
        # 本原不可约多项式一根求同次其他本原不可约多项式根集囗公式
        #
        # 本原不可约多项式求同次其他本原不可约多项式囗公式 <<== 本原不可约多项式一根求同次其他本原不可约多项式根集囗公式+根集求多项式囗公式
        #   ?对称多项式的基 之间的 转换
        #   ?如何由 根 求出 相应 对称多项式的基
        #       归纳法:
        #       m=1 -> 2    -> 3 ->...
        #       [n=1]:a0 -> a0+a1 -> a0+a1+a2 -> ...
        #       [n=2]:0 -> a0*a1 -> a0*a1 +(a0+a1)*a2 -> a0*a1 +(a0+a1)*a2 + (a0+a1+a2)*a3 -> ...
        #       [n=3]:0 -> 0 -> a0*a1*a2 -> a0*a1*a2 + (a0*a1 +(a0+a1)*a2)*a3 -> ...
        #   [sp(m,n) =[def]= sum~ II~ a[k] ~{k<-ks} ~{ks <- 2**{0..<m} | [len ks == n]}]
        #   [[not$ 0<=n<=m] -> [sp(m,n) == 0]]
        #   [0<=n<=m]:
        #       [[0==n<=m] -> [sp(m,n) == 1]]
        #       [[0<=n==m] -> [sp(m,n) == II~ a[k] ~{k<-[0..<m]}]]
        # [sp(m+1,n+1) == sp(m,n+1) + sp(m,n)*a[m]]
        #   这计算轨迹 等同于 直接展开 II (z-a[i] {i<-[0..<m]} 有什么意思？！
        #
      [@[a <- GF(p**m)] -> [f(a)==0] -> @[u <- [1..<p**m-1]] -> [gcd(u,p**m-1)=!=1]{#避开-生成子->非本原#} -> [@[pd <- all_prime_factors_of m] -> [(a**u)**(p**(m/pd)) =!= (a**u)]]{#不可约#} -> [{(a**u)**(p**i) | [@i <- [0..<m]]} 是 其他 degree为m的 非本原不可约多项式 的 根集]]
        # 本原不可约多项式一根求同次非本原不可约多项式根集囗公式
        #
        # 本原不可约多项式求同次非本原不可约多项式囗公式 <<== 本原不可约多项式一根求同次非本原不可约多项式根集囗公式+根集求多项式囗公式

  根的阶ro:
    [gcd(ro, p**m)==1]
    [本原不可约] <==> [ro==p**m-1]
    [非本原不可约] <==> [[ro<p**m-1][@[d<-all_divisors_of m] -> [(p**d-1)%ro==0] -> [d==m]]] <==> [[ro<p**m-1][@[pd<-all_prime_factors_of m] -> [(p**(m/pd)-1)%ro=!=0]]]
    [可约] <==> [???]



  [%2]:
    x**2-x = (x-0)(x-1)
    x**2**2-x = (x-0)(x-1)(x**2+x+1)
    x**2**3-x = (x-0)(x-1)(x**6+x**5+x**4+x**3+x**2+x+1)
      #GF(p**m) ~=~ ZZ[x]%f(m,x) ==>> 本原不可约多项式 次数 为 m
      # 非零乘法群 规模 == p**m-1 #除了0
      # 生成子 总数 = phi(非零乘法群 规模) = phi(p**m-1)
      # monic本原不可约多项式 总数 = 生成子 总数 / 本原不可约多项式 次数 = phi(p**m-1)/m
      #     monic #多项式首项系数为一
      #     ???[p=2]梅森素数[m=3] phi(2**3-1)=7-1=6没有影响
      #GF(2**3) ==>> phi(2**3-1)/3 = 2 个 次数为3的 monic本原不可约多项式
      = (x-0)(x-1)(x**3+x+1)(x**3+x**2+1)
  ==>> [(x**2**3-x)%(x**2**2-x) =!= 0]
    #即 GF(2**3)不包含GF(2**2)

  [%3]:
    x**3-x = (x-0)(x-1)(x-2)

GF(2**8)
  degree(f(x))==e
  f(x) is irreducible polynomials over ZZ%p
  GF(p**e) ~=~ ZZ[x]%p%f(x)
  primitive irreducible polynomials
    f(a)==0, 根a刚好是 ZZ[a]%p 的 生成子
    ZZ[a]%p ~=~ ZZ[x]%p%f(x)
  GF(2**8)总数:phi(2**8-1)/8 = phi(17*5*3)/8=(17-1)(5-1)(3-1)/8=16

CLASS OF IRREDUCIBLE POLYNOMIALS
]]

#]]]]]'''


import sympy
from sympy import x






