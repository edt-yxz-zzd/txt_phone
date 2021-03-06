
r"""
enumerate Lyndon_word


ref:
	Enumerating all the Irreducible Polynomials over Finite Field

my algo for enumerate Lyndon_word

theorem:
	ff1
	ff2

	ff3_1
	ff3_2
	ff3_3
	ff3_4
	ff3_5
	ff3_6
	ff3_7

	ff5_1
	ff5_2
	ff5_3

	ff6_01
	ff6_02
	ff6_03
	ff6_04
	ff6_05
	ff6_06
	ff6_07

	ff6_1
	ff6_2
	ff6_3
	ff6_4
	ff6_5




[@a,w,i][a::Type][w::[a]][i::uint]:
	[left_rotate<i> w =[def]= w[i:]++w[:i]]

[m>=1][n>=1]:
	[word<m,n> =[def]= [uint%m]{n}]
	[offset_word<m,n> =[def]= {w::[uint%m]{n} | [@a<-w. [w[0] <= a]]}]
	[pp_word<m,n> = pseudo_periodic_word<m,n> =[def]= {w*(n//k)++w[:n%k] | @k<-[1..n-1]. @w. [w<-word<m,k>]}]

	[Lyndon_word<m,n> =[def]= {w::[uint%m]{n} | [@i<-[1..n-1]. [w < w[i:]++w[:i] == left_rotate<i> w]]}]

	#err [ppLyndon_word<m,n> = pseudo_periodic_Lyndon_word<m,n> =[def]= {w*(n//k)++w[:n%k] | @k<-[1..n-1]. @w. [w<-Lyndon_word<m,k>\-/ppLyndon_word<m,k>==dmLyndon_word<m,k>]}]
	[ppLyndon_word<m,n> = pseudo_periodic_Lyndon_word<m,n> =[def]= {w*(n//k)++w[:n%k] | @k<-[1..n-1]. @w. [w<-Lyndon_word<m,k>]}]
	[dmLyndon_word<m,n> =[def]= Lyndon_word<m,n>\-/ppLyndon_word<m,n>]
	#[dmLyndon_word<m,n> =[def]= {w*(n//k)++w[:n%k] | @k<-[1..n]. @w. [w<-Lyndon_word<m,k>]}]


[offset_word <= word]
[pp_word <= word]
[Lyndon_word <= offset_word]
[dmLyndon_word <= offset_word]
[ppLyndon_word <= offset_word]
[ppLyndon_word <= pp_word]

[w<-word][pw<-pp_word]
	[is_pp_word_of w pw =[def]= [k:=len w][n:=len pw][k<-[1..n-1]][pw == w*(n//k)++w[n%k]]]

[w<-word<m,n>][i<-[1..n-1]][w[:i]==w[n-i:]]:
	ff1:
	[w<-pp_word]
		proof:
			*[2*i<=n]:
				[wp:=w[:n-i]]
				[w == wp++wp[:i]]
				[w<-pp_word]
			*[2*i>n]:
				[wp:=w[:n-i]]
				[w == wp*(n//i)++wp[:n%i]]
				[w<-pp_word]
			[w<-pp_word]
			done
#[Lyndon_word/-\ppLyndon_word=={}]
ff2:[Lyndon_word/-\pp_word=={}]
	proof:
		[@pw][pw<-pp_word/-\Lyndon_word]:
			!![pw<-pp_word]
			[?w,m,n,k
			][pw<-pp_word<m,n>
			][w<-word<m,k>
			][pw == w*(n//k)++w[:n%k]
			][m>=1][1<=k<n]
			
			*[n%k==0]:
				!![1<=k<n]
				[n//k >=2]
				[pw == left_rotate<k> pw]
				[not pw<-Lyndon_word]
				_L
			*[n%k!=0]:
				[h:=w[:n%k]]
				[t:=w[n%k:]]
				[ht:=h++t]
				[th:=t++h]
				[w==ht]
				[hts:=ht*(n//k)]
				[ths:=th*(n//k)]
				[pw==hts++h==h++ths]
				!![n%k!=0]
				[0 < len(h) == n%k < n]
				!![1<=k<n]
				[0 < len(hts)==len(ths)==n-len(h) < n]
				!![pw<-Lyndon_word]
				[pw < left_rotate<len(hts)> pw]
				[hts++h < h++hts]
				[h++ths < h++hts]
				[ths < hts]
				[pw < left_rotate<len(h)> pw]
				[h++ths < ths++h]
				[hts++h < ths++h]
				[hts < ths]
				_L
		[Lyndon_word/-\pp_word=={}]
		done


[w<-word<m,n>][n>=1]:
	[w[:1]<-Lyndon_word]
	[max_sz_Lyndon_prefix w =[def]= max {k<-[1..n] | w[:k]<-Lyndon_word}]
	[w[n:]==w[:0]]
	[min_offset_proper_may_bifix w =[def]= min {j<-[1..n] | [w[j:]==w[:n-j]]}]

	ff3_1:
	[1
	<= max_sz_Lyndon_prefix w
	<= min_offset_proper_may_bifix w
	<= n
	]
		proof:
			[k:=max_sz_Lyndon_prefix w]
			[j:=min_offset_proper_may_bifix w]
			[1<=k<=n]
			[1<=j<=n]
			[w[:k]<-Lyndon_word]
			[w[j:]==w[:n-j]]
			[j<k]:
				[1<=j<k<=n]
				[w[:k-j]==w[j:k]]
				[k>len(w[:k-j])==k-j>0]
				!!ff1
				[w[:k] <- pp_word]
				!![w[:k]<-Lyndon_word]
				!!ff2
				_L
			[1<=k<=j<=n]
			done
	ff3_2:
	[@j<-[1..n]. @i<-[0..n-1]. [w[j:]==w[:n-j]]->[w[i]==w[i%j]]]
		proof:
			[@j][j<-[1..n]][w[j:]==w[:n-j]]:
				[j<=i<n]:
					!![w[j:]==w[:n-j]]
					[w[i] == w[i-j]]
				[@i][i<-[0..n-1]]:
					[w[i]==w[i%j]]
			done
	ff3_3:
	[j:=min_offset_proper_may_bifix w
	][@i<-[0..n-1]. [w[i]==w[i%j]]]
		proof:
			[@i][i<-[0..n-1]]:
				!!min_offset_proper_may_bifix def
				[w[j:]==w[:n-j]][1<=j<=n]
				!!ff3_2
				[w[i]==w[i%j]]
			done


	ff3_4:[[w<-dmLyndon_word] -->> [?wp,k][wp<-Lyndon_word<m,k>][0<k<=n][w==(cycle wp)[:n]]]
		proof:
			!![w<-dmLyndon_word]
			*[w<-Lyndon_word]:
				[wp:=w]
				[k:=n]
				[wp<-Lyndon_word<m,k>][0<k<=n][w==(cycle wp)[:n]]
			*[w<-ppLyndon_word]:
				[?wp,k][k<-[1..n-1]][wp<-Lyndon_word<m,k>][w==wp*(n//k)++wp[:n%k]]
				[wp<-Lyndon_word<m,k>][0<k<=n][w==(cycle wp)[:n]]
			done


	ff3_5:
	[
		[s:={wp<-Lyndon_word | [is_pp_word_of wp w]or[wp==w]}
		][k:=max_sz_Lyndon_prefix w
		][j:=min_offset_proper_may_bifix w
		] -->>
		[
			[j==k]
			<--> [w<-dmLyndon_word<m,n>]
			<--> [s!={}]
			<--> [s=={w[:j]}]
		]
	]
		proof:
			!!ff3_1
			[1<=k<=j<=n]
			[wk:=w[:k]]
			[@wp_][wp_ <- s][k_:=len wp_]:
				[wp_<-Lyndon_word]
				!!max_sz_Lyndon_prefix def
				[k_ <= k]
				!!min_offset_proper_may_bifix def
				[j <= k_]
				[j<=k_<=k]
				!![1<=k<=j<=n]
				[k_==k==j]
				[wp_==wk]
			[@wp_ <- s][wp_==wk]
			[s <= {wk}]
			[len s <= 1]
			[s != {}]:
				hh0:[s == {wk}][k==j]

			*[==>>]???[[w<-dmLyndon_word<m,n>] -->> [s!={}]]:
				!![w<-dmLyndon_word]
				!!ff3_4
				[?wp_,k_][k_<-[1..n]][wp_<-Lyndon_word<m,k_>][w==wp_*(n//k_)++wp_[:n%k_]]
				[wp_ <- s]
				[s != {}]

			*[==>>]???[[s!={}] -->> [s=={w[:j]}]]:
				!!hh0
				[s == {wk}][k==j]
				[s=={w[:j]}]

			*[==>>]???[[s=={w[:j]}] -->> [k==j]]:
				[s!={}]
				!!hh0
				[k==j]

			*[==>>]???[[k==j] -->> [w<-dmLyndon_word]]:
				!!ff3_3
				[@i<-[0..n-1]. [w[i]==w[i%j]]]
				!![k==j]
				[@i<-[0..n-1]. [w[i]==wk[i%k]]]
				!!max_sz_Lyndon_prefix def
				[wk<-Lyndon_word]
				*[k==n]:
					[w==wk<-Lyndon_word]
					[w<-dmLyndon_word]
				*[k<n]:
					[w<-ppLyndon_word]
					[w<-dmLyndon_word]
				[w<-dmLyndon_word]

			done








	ff3_6: [[w<-Lyndon_word] <--> [@i<-[1..n-1].[w[:i] < w[n-i:]]]]
		proof:
			*[==>>]:
				[@i][i<-[1..n-1]]:
					!![w<-Lyndon_word]
					[w < left_rotate<n-i> w]
					[w[:i] <= w[n-i:]]
					[w[:i] == w[n-i:]]:
						[w <- pp_word]
						!!ff2
						_L
					[w[:i] < w[n-i:]]
				[@i<-[1..n-1]. [w[:i] < w[n-i:]]]
			*[<<==]:
				!![@i<-[1..n-1]. [w[:i] < w[n-i:]]]
				[@i<-[1..n-1]. [w[:n-i] < w[i:]]]
				[@i][i<-[1..n-1]]:
					[w[:n-i] < w[i:]]
					[w < left_rotate<i> w]
				[w<-Lyndon_word]
			done

	ff3_7: [[w<-dmLyndon_word] <--> [@i<-[1..n-1].[w[:i] <= w[n-i:]]]]
		proof:
			*[==>>]:
				!![w<-dmLyndon_word]
				!!ff3_4
				[?wp,k][wp<-Lyndon_word<m,k>][0<k<=n][w==(cycle wp)[:n]]
				[wps:=cycle wp]
				[@j<-[0..]. [wps <= wps[j:]]]
				[@i][i<-[1..n-1]]:
					[wps <= wps[n-i:]]
					[wps[:i] <= wps[n-i:][:i]]
					[wps[:i] <= wps[n-i:n]]
					[w[:i] <= w[n-i:]]
				[@i<-[1..n-1].[w[:i] <= w[n-i:]]]
			*[<<==]:
				[k:=max_sz_Lyndon_prefix w]
				[j:=min_offset_proper_may_bifix w]
				!!ff3_1
				[1<=k<=j<=n]
				[wk:=w[:k]]
				[wj:=w[:j]]

				!!min_offset_proper_may_bifix
				[@i<-[1..j-1]. [w[:j-i] != w[i:]]]
				!![@i<-[1..n-1].[w[:i] <= w[n-i:]]]
				[@i<-[1..n-1].[w[:j-i] <= w[i:]]]
				[@i<-[1..j-1]. [w[:j-i] < w[i:]]]
				[@i<-[1..j-1]. [wj[:j-i] < wj[i:]]]
				!!ff3_6
				[wj<-Lyndon_word]
				!!max_sz_Lyndon_prefix def
				[k>=j]
				[k==j]
				!!ff3_5
				[w<-dmLyndon_word]
			done











[w <- Lyndon_word]:
	[i>=1]:
		#maynot [w[:i] <- Lyndon_word]
			#w=01011;w[:4]=0101

[w <- dmLyndon_word<m,n>]:
	ff5_1:[w[:1] <- dmLyndon_word]
	ff5_2:[[n>=2] -> [w[:n-1] <- dmLyndon_word]]
	ff5_3:[@i<-[1..n]. [w[:i] <- dmLyndon_word]]


	ff5_1:[w[:1] <- dmLyndon_word]
		proof:
			[w[:1] <- Lyndon_word]
			[w[:1] <- dmLyndon_word]
			done
	ff5_2:[[n>=2] -> [w[:n-1] <- dmLyndon_word]]
		proof:
			[w_:=w[:n-1]]
			[@i][i<-[2..n-1]]:
				!!ff3_7
				[w[:i] <= w[n-i:]]
				[w[:i][:i-1] <= w[n-i:][:i-1]]
				[w[:i-1] <= w[n-i:n-1]]
				[w_[:i-1] <= w_[n-i:]]
				[w_[:i-1] <= w_[(n-1)-(i-1):]]
			[@i<-[1..n-2].[w_[:i] <= w_[(n-1)-i:]]]
			!![n>=2]
			[n-1>=1]
			!!ff3_7
			[w_<-dmLyndon_word]
			done


	ff5_3:[@i<-[1..n]. [w[:i] <- dmLyndon_word]]
		proof:
			*[k==0]:
				!![w <- dmLyndon_word]
				[w[:n-k] <- dmLyndon_word]
			*[1<=k<=n-1][w[:n-(k-1)] <- dmLyndon_word]:
				[n-(k-1)>=2]
				!![w[:n-(k-1)] <- dmLyndon_word]
				!!ff5_2
				[w[:n-k] <- dmLyndon_word]
			[@k<-[0..n-1]. [w[:n-k] <- dmLyndon_word]]
			[@i<-[1..n]. [w[:i] <- dmLyndon_word]]
			done





[@m,n,w][m>=2][n>=2][END:=[m-1]*n][BEGIN:=[0]*n][LAST:=[m-2]++[m-1]*(n-1)]:
	[w <- dmLyndon_word<m,n>][w != END]:
		[rfind_notmax w =[def]= max {i<-[0..n-1] | w[i] != m-1}]

		[inc_prefix w =[def]= [i:=rfind_notmax w][prefix:= w[:i]++[w[i]+1]]:(prefix)]

		[inc w =[def]= [prefix:= w[:i]++[w[i]+1]][ww := (cycle $ inc_prefix w)[:n]]:(ww)]

		ff6_01:[{BEGIN,LAST,END} <= dmLyndon_word]
		ff6_02:[BEGIN<LAST<END]
		ff6_03:[inc LAST ==END]
		ff6_04:[w[:1]*n <= w]
		ff6_05:[0 <= w[0] < m-1]
		ff6_06:[BEGIN<=w<=LAST]
		ff6_07:[w < inc w]

		ff6_1:[inc_prefix w <- dmLyndon_word]
		ff6_2:[inc w <- dmLyndon_word<m,n>]
		ff6_3:[@wm<-word<m,n>. [w < wm < inc w] -> [not wm <- dmLyndon_word<m,n>]]
		ff6_4:[?i<-[1..]. [END == (inc^i) w]]
		ff6_5:[dmLyndon_word<m,n> == {(inc^i) BEGIN | i<-[0..len dmLyndon_word<m,n> -1]}]


		ff6_01:[{BEGIN,LAST,END} <= dmLyndon_word]
			proof:
				[@i][i<-[1..n-1]]:
					[BEGIN[:i] ==[0]*i== BEGIN[n-i:]]
					[END[:i] ==[m-1]*i== END[n-i:]]
					[LAST[0]==m-2<m-1==LAST[n-i:]]
					[LAST[:i] < LAST[n-i:]]
					!!ff3_7
					[{BEGIN,LAST,END} <= dmLyndon_word]
					done

		ff6_02:[BEGIN<LAST<END]
			proof:
				!![m>=2]
				[m-1>0]
				!![n>=2]
				[BEGIN[0]==0 <= m-2==LAST[0] < m-1==END[0]]
				[BEGIN[1]==0 < m-1==LAST[1]]
				[BEGIN<LAST<END]
				done

		ff6_03:[inc LAST ==END]
			proof:
				[inc_prefix LAST == [m-1]]
				[inc LAST ==END]
				done


		ff6_04:[w[:1]*n <= w]
			proof:
				!![w <- dmLyndon_word<m,n>]
				[w <- offset_word]
				[@u<-w. [u>=w[0]]]
				[w[:1]*n <= w]
				done

		ff6_05:[0 <= w[0] < m-1]
			proof:
				!![w <- dmLyndon_word<m,n>]
				[@u<-w. [u <- [0..m-1]]]
				!![n>0]
				[w[0] <- [0..m-1]]

				[w[0] == m-1]:
					!!ff6_04
					[END == w[:1]*n <= w]
					[w==END]
					_L
				[0 <= w[0] < m-1]
				done


		ff6_06:[BEGIN<=w<=LAST]
			proof:
				!!ff6_05
				[0 <= w[0] < m-1]
				[BEGIN[0] <= w[0] <= LAST[0]]
				[BEGIN[1:]==[0]*(n-1) <= w[1:] <= [m-1]*(n-1)==LAST[1:]]
				[BEGIN<=w<=LAST]
				done

		ff6_07:[w < inc w]
			proof:
				[pf:=inc_prefix w]
				[k:=len pf]
				[1<=k<=n]
				[w[:k] < pf==(inc w)[:k]]
				[w < inc w]
				done




		ff6_1:[inc_prefix w <- Lyndon_word]
			proof:
				[pf := inc_prefix w]
				[k:=len pf]
				[wk:=w[:k]]
				!![w<-dmLyndon_word]
				!!ff5_3
				[wk<-dmLyndon_word]
				[@i][i<-[1..k-1]]:
					!![pf[k-1]==wk[k-1]+1]
					!![pf[:k-1]==wk[:k-1]]
					[wk[n-i:] < pf[n-i:]]
					[wk[:i] == pf[:i]]
					!!ff3_7
					[wk[:i] <= wk[n-i:]]
					[pf[:i] < pf[n-i:]]
				[@i<-[1..k-1]. [pf[:i] < pf[n-i:]]]
				!!ff3_6
				[pf<-Lyndon_word]
				done



		ff6_2:[inc w <- dmLyndon_word<m,n>]
			proof:
				[pf := inc_prefix w]
				[k:=len pf]
				[1<=k<=n]
				!!ff6_1
				[pf <- Lyndon_word]
				[inc w == pf*(n//k)++pf[n%k]]
				*[k==n]:
					[inc w == pf <- Lyndon_word]
					[inc w <- dmLyndon_word]
				*[1<=k<n]:
					[inc w <- ppLyndon_word]
					[inc w <- dmLyndon_word]
				[inc w <- dmLyndon_word]
				done



		ff6_3:[@wm<-word<m,n>. [w < wm < inc w] -> [not wm <- dmLyndon_word<m,n>]]
			proof:
				[pf := inc_prefix w]
				[k:=len pf]
				[1<=k<=n]
				[u:=pf[k-1]]
				[cp:=pf[:k-1]]
				[w_ := inc w]
				[w==cp++[u-1]++[m-1]*(n-k)]
				[w_==cp++[u]++pf*((n-k)//k)++pf[n%k]]
				!![w < wm < w_]
				[wm[:k] == pf == w_[:k]]
				[wm[k:n] < w_[k:n]==w_[:n-k]]
				[?i][0<=i<n-k][wm[k:k+i] == w_[:i]][wm[k+i] < w_[i]]
				[wm[:k+i] == w_[:k+i]]
				[wm[:k+i+1] < w_[:k+i+1]]

				!![k>=1]
				[wm[:i+1] == w_[:i+1]]
				[wm[k:k+i+1] < w_[k:k+i+1] == w_[:i+1] == wm[:i+1]]

				!![i<n-k]
				[n-k>=i+1]
				[wm[:n-k] > wm[k:]]
				!!ff3_7
				[not wm <- dmLyndon_word]
				done

		ff6_4:[?i<-[1..]. [END == (inc^i) w]]
			proof:
				[f i := (inc^i) w]
				[@i<-[0..]. [f i != END]]:
					[s:={f i | i<-[0..m^n]}]
					[f i != END]:
						!!ff6_07
						[f i < f (i+1) <= END]
					[len s == m^n+1]
					[len(word<m,n>) == m^n]
					[s <= image f <= word<m,n>]
					[len s <= m^n]
					_L
				[?i<-[0..]. [f i == END]]

				!![w!=END]
				[END != f 0]
				[?i<-[1..]. [f i == END]]
				done

		ff6_5:[dmLyndon_word<m,n> == {(inc^i) BEGIN | i<-[0..len dmLyndon_word<m,n> -1]}]
			proof:
				[f i := (inc^i) BEGIN]
				!!ff6_4
				[?i][i<-[1..]. [f i == END]]
				[f 0 == BEGIN]
				[f i == END]
				[i>0]
				[s:={f j | j<-[0..i]}]

				[@wm][wm<-word<m,n>\\s]:
					[f 0 < wm < f i]
					!![i>0]
					[j:=max {j<-[0..i-1] | [wm > f j]}]
					[f j < wm < f (j+1)]
					!!ff6_3
					[not wm <- dmLyndon_word<m,n>]
				[{}==(word<m,n>\\s) /-\ dmLyndon_word<m,n>]
				!![dmLyndon_word<m,n> <= word<m,n>]
				[dmLyndon_word<m,n> <= s]

				!!ff6_2&ff6_01
				[s <= dmLyndon_word<m,n>]
				[s == dmLyndon_word<m,n>]
				done








$ python enumerate_Lyndon_word.py  2 4
(0, 0, 0, 1)
(0, 0, 1, 1)
(0, 1, 1, 1)

$ python enumerate_Lyndon_word.py  2 5
(0, 0, 0, 0, 1)
(0, 0, 0, 1, 1)
(0, 0, 1, 0, 1)
(0, 0, 1, 1, 1)
(0, 1, 0, 1, 1)
(0, 1, 1, 1, 1)

$ python enumerate_Lyndon_word.py  2 6
(0, 0, 0, 0, 0, 1)
(0, 0, 0, 0, 1, 1)
(0, 0, 0, 1, 0, 1)
(0, 0, 0, 1, 1, 1)
(0, 0, 1, 0, 1, 1)
(0, 0, 1, 1, 0, 1)
(0, 0, 1, 1, 1, 1)
(0, 1, 0, 1, 1, 1)
(0, 1, 1, 1, 1, 1)




normal basis
[num_irr_polys_over p n d
	= sum~ miu(d///i)*(p^n)^i {i\\\d} ///d
	= len enumerate_Lyndon_word(p^n,d)
]

[num_irr_polys_over 2 1 4
	= ((2^1)^4-(2^1)^2) ///4 = 3
	= len enumerate_Lyndon_word(2^1,4) = 3 #see above exec
]
[num_irr_polys_over 2 1 5
	= ((2^1)^5-(2^1)^1) ///5 = 6
	= len enumerate_Lyndon_word(2^1,5) = 6 #see above exec
]
[num_irr_polys_over 2 1 6
	= ((2^1)^6-(2^1)^3-(2^1)^2+(2^1)^1) ///6 = 9
	= len enumerate_Lyndon_word(2^1,6) = 9 #see above exec
]






"""






def enumerate_Lyndon_word(m, n):
	if n < 1:
		return
	if m < 1:
		return
	assert m>=1
	assert n>=1
	if n==1:
		for w0 in range(m):
			yield (w0,)
		return
	if m==1:
		return

	assert m>=2
	assert n>=2
	m_ = m-1
	max_w0 = m-2
	w = [None]*n
	i2sz = [None]*n
		#wi:=w[:i]
		#sz:=i2sz[i-1]
		#[0<=sz<=i-1]
		#[i-sz == min_offset_proper_may_bifix wi]
	i2m1sz = [None]*n
		#wi:=w[:i]
		#m1sz:=i2m1sz[i-1]
		#[0<=m1sz<=i-1] #w[0]<m_
		#wi[i-m1sz:] == [m-1]*m1sz
	def inc():
		begin1 = begin0 = 0
		end = n
		m1sz = i2m1sz[end-1]
		end1 = end0 = end-m1sz
		for i in range(end1, n):
			w[i] = None
			i2m1sz[i] = None
		while 1:
			assert 0 <= m1sz < end <= n
			i = n-m1sz-1
			assert 0 <= i < n
			assert i == end1-1
			if not i:
				return False
			assert 0 < i < n

			try:
				assert w[i] < m_
			except:
				print(f"w={w}; w[{i}]={w[i]}; m-1={m_}")
				print(f"i2m1sz={i2m1sz}; m1sz={m1sz}; n={n}")
				raise
			w[i] += 1
			i2sz[i] = 0
			if w[i] == m_:
				#bug:i2m1sz[i] += 1
				i2m1sz[i] = i2m1sz[i-1] + 1
			if not m1sz:
				break
			assert 0 < m1sz < end <= n
			assert 0 < i < n-1
			begin1 = i+1
			assert 2 <= begin1 == end1 < n
			assert w[begin1] is None
			assert w[begin1-1] is not None
			end = m1sz
			assert 1 <= end < n
			#bug: m1sz = i2m1sz[end-1]
			#bug: m1sz = i2m1sz[end%begin1-1]
			m1sz = i2m1sz[(end-1)%begin1]
			try:
				assert m1sz is not None
			except:
				print(f"w={w}")
				print(f"i2m1sz={i2m1sz}")
				print(f"m1sz={m1sz}")
				print(f"begin1={begin1}")
				print(f"end={end}")
				print(f"end%begin1={end%begin1}")
				raise

			assert 0 <= m1sz <= (end-1)%begin1 < end
			end0 = end-m1sz
			assert 0 == begin0 < end0 <= end
			assert (end0-1)%begin1 == (end-1)%begin1-m1sz
			assert not m1sz or w[end0%begin1] == m_
			assert w[(end0-1)%begin1] < m_
			#donot: w[begin1:begin1+(end0-begin0)]=w[begin0:end0]
			assert i2m1sz[begin0] == 0
			end1 = begin1+(end0-begin0)
			for i1, i0 in enumerate(range(begin0, end0), begin1):
				w[i1] = w[i0]
				i2m1sz[i1] = i2m1sz[i0]
			i2sz[begin1:begin1+(end0-begin0)] = range(1,1+(end0-begin0))
		return True


	for w0 in range(max_w0+1):
		for i in range(n):
			w[i] = w0
			i2sz[i] = i
			i2m1sz[i] = 0
		while 1:
			if not inc():
				break
			assert not i2sz[-1]
			yield (*w,)

































def main(args=None):
	import argparse

	parser = argparse.ArgumentParser(
		description="enumerate_Lyndon_word for irr poly"
		, epilog=""
		, formatter_class=argparse.RawDescriptionHelpFormatter
		)
	parser.add_argument('m', type=int
						, help='radix')
	parser.add_argument('n', type=int
						, help='word length')

	args = parser.parse_args(args)
	m = args.m
	n = args.n
	it = enumerate_Lyndon_word(m,n)
	for i, w in enumerate(it):
		print(f"{i}: {w}")


if __name__ == "__main__":
	main()



