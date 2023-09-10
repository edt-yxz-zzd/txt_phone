#__all__:goto
r'''[[[
now move to:
e ../../python3_src/seed/math/continued_fraction/iter_continued_fraction_of_log__truncated_.py
===
e script/log_b_y.py
view others/数学/continued-fraction/continued_fraction_of_logB_Y.txt

[[[
我的算法，对原论文算法进行修改:连分数 奇偶位 切换 floor/ceil，得到 真正的上下限，可以确定 哪些是有效位，而原文只是 估计...
===
see:
    dfloor_log_ex_
    ufloor_log_ex_
    lcf  # 原连分数cf的下限
    gcf  # 原连分数cf的上限
    [lcf <= cf <= gcf]
===
[1 < b < y]:
    [x == log_(b;y)]
    [b**x == y]
    [1 < b < b**x]
    [cf := cf_(x)]
    [x == t0 == cf0 + t1]
    [b**cf0 <= b**(cf0+t1) < b**(cf0+1)]
    [1 <= b**t1 == y/b**cf0 < b]
    [1 == b**t1 < b]:
        #stop
        [x == cf0]
    [1 < b**t1 < b]:
        #recur
        [1 < b < b**(1/t1)]
        [t1 == 1/(cf1+t2)]
        [1 < b < b**(cf1+t2)]

===

[1 < b < y]:
    [y[0] := y]
    [b[0] := b]
    [1 < b[0] < y[0]]
    [cf[i] := floor_log_(b[i];y[i])]
    [b[i]**cf[i] <= y[i] < b[i]**(cf[i]+1)]
    * [b[i]**cf[i] == y[i]]:
        #stop
        [cf[i+1:] = [+oo]*inf]
    * [b[i]**cf[i] < y[i]]:
        #recur
        [b[i]**cf[i] < y[i] < b[i]**(cf[i]+1)]
        [1 < y[i]/b[i]**cf[i] < b[i]]
        [b[i+1] := y[i]/b[i]**cf[i]]
        [y[i+1] := b[i]]

===
[1 < b < y]:
    [y[0] := y]
    [b[0] := b]
    [1 < b[0] < y[0]]
    [1 <= b[i] < y[i]]
    * [b[i] == 1]:
        #stop
        [cf[i:] = [+oo]*inf]
    * [b[i] > 1]:
        [cf[i] := floor_log_(b[i];y[i])]
        [b[i]**cf[i] <= y[i] < b[i]**(cf[i]+1)]
        [1 <= y[i]/b[i]**cf[i] < b[i]]
        [b[i+1] := y[i]/b[i]**cf[i]]
        [y[i+1] := b[i]]
        [1 <= b[i+1] < y[i+1]]


===

######################
######################
######################
[b > 1][y >= 1]:
    [floor_log_(b;y) =[def]= if y < b then 0 else 1+floor_log_(b;y/b)]
    [floor_log_ex_(b;y) =[def]= if y < b then (y,0) else fmap (1+) floor_log_ex_(b;y/b)]
[kb > k][ky >= k][k >= 1]:
    [dfloor_log_(k;kb;ky) =[def]= if ky < kb then 0 else 1+dfloor_log_(k;kb;floor(k*ky/kb))]
    [ufloor_log_(k;kb;ky) =[def]= if ky < kb then 0 else 1+ufloor_log_(k;kb;ceil(k*ky/kb))]

    [dfloor_log_ex_(k;kb;ky) =[def]= if ky < kb then (ky,0) else fmap (1+) dfloor_log_ex_(k;kb;floor(k*ky/kb))]
    [ufloor_log_ex_(k;kb;ky) =[def]= if ky < kb then (ky,0) else fmap (1+) ufloor_log_ex_(k;kb;ceil(k*ky/kb))]
######################
proof_termination_of_dfloor_log_
proof termination of dfloor_log_
    [k >= 1]
    [kb > k]
    [ky >= k]
    * [1 <= k <= ky < kb]:
        stop
    * [1 <= k < kb <= ky][new_ky := floor(k*ky/kb)]:
        [kb <= ky]
        [k*kb <= k*ky]
        [k <= k*ky/kb]
        [k <= floor(k*ky/kb) == new_ky]
        [1 <= k <= new_ky]
        ####################
        [old_ky := ky]
        [old_ky >= kb > k >= 1]
        [old_ky >= 2]
        !! [k < kb]
        [k/kb < 1]
        [old_ky*(k/kb) < old_ky]
        [new_ky <= k*old_ky/kb < old_ky]
        !! [1 <= k <= new_ky]
        !! [new_ky < old_ky]
        !! [new_ky, old_ky :: int]
        [will terminate]
        ######################

######################
proof_termination_of_ufloor_log_
proof termination of ufloor_log_
    [k >= 1]
    [kb > k]
    [ky >= k]
    * [1 <= k <= ky < kb]:
        stop
    * [1 <= k < kb <= ky][new_ky := ceil(k*ky/kb)]:
        [kb <= ky]
        [k*kb <= k*ky]
        [k <= k*ky/kb]
        [k <= ceil(k*ky/kb) == new_ky]
        [1 <= k <= new_ky]
        ####################
        [old_ky := ky]
        [old_ky >= kb > k >= 1]
        !! [new_ky := ceil(k*ky/kb)]
        [new_ky == ceil(k*old_ky/kb) == floor((k*old_ky-1)/kb) +1]
        [new_ky >= old_ky]:
            [floor((k*old_ky-1)/kb) +1 >= old_ky]
            [(k*old_ky-1)/kb >= old_ky-1]
            [(k*old_ky-1) >= old_ky*kb -kb]
            [(kb-1) >= old_ky*(kb-k) >= old_ky*1]
            [kb > old_ky]
            !! [old_ky >= kb]
            _L
        [new_ky < old_ky]

        !! [1 <= k <= new_ky]
        !! [new_ky < old_ky]
        !! [new_ky, old_ky :: int]
        [will terminate]
        ####################
######################
######################
######################
# vs:
#   floor_log_(b;y)
#   dfloor_log_(k;k*b;k*y)
#   ufloor_log_(k;k*b;k*y)
######################
[floor_log_(b;y) <= floor_log_(b;y+1)]
[dfloor_log_(k;kb;ky) <= dfloor_log_(k;kb;ky+1)]
[ufloor_log_(k;kb;ky) <= ufloor_log_(k;kb;ky+1)]
######################
[floor_log_(b+1;y) <= floor_log_(b;y)]
[dfloor_log_(k;kb+1;ky) <= dfloor_log_(k;kb;ky)]
[ufloor_log_(k;kb+1;ky) <= ufloor_log_(k;kb;ky)]
######################
[dfloor_log_(k;k*b;k*y) <= floor_log_(b;y)]
    # induction:
    [dfloor_log_(k;k*b;floor(k*k*y/kb)) <= floor_log_(b;floor(k*k*y/kb)/k) <= floor_log_(b;(k*k*y/kb)/k) == floor_log_(b;y/b)]
######################
[ufloor_log_(k;k*b;k*y) >= floor_log_(b;y)]
    # induction:
    [ufloor_log_(k;k*b;ceil(k*k*y/kb)) >= floor_log_(b;ceil(k*k*y/kb)/k) >= floor_log_(b;(k*k*y/kb)/k) == floor_log_(b;y/b)]
######################
######################
######################
[snd floor_log_ex_(b;y) == floor_log_(b;y)]
[snd dfloor_log_ex_(k;kb;ky) == dfloor_log_(k;kb;ky)]
[snd ufloor_log_ex_(k;kb;ky) == ufloor_log_(k;kb;ky)]
######################
[1 <= fst floor_log_ex_(b;y) < b]
    『1 <= ...』<<==:
    [y >= b]:
        [(y/b) >= 1]
[k <= fst dfloor_log_ex_(k;kb;ky) < kb]
[k <= fst ufloor_log_ex_(k;kb;ky) < kb]
    『k <= ...』<<==:
    [ky >= kb]:
        [floor(k*ky/kb) >= floor(k*kb/kb) == k]
        [ceil(k*ky/kb) >= ceil(k*kb/kb) == k]
######################
######################
[[kb >= k*b] -> [ky <= k*y] -> [dfloor_log_(k;kb;ky) <= floor_log_(b;y)]]
    !! [dfloor_log_(k;kb+1;ky) <= dfloor_log_(k;kb;ky)]
    !! [dfloor_log_(k;kb;ky) <= dfloor_log_(k;kb;ky+1)]
    !! [dfloor_log_(k;k*b;k*y) <= floor_log_(b;y)]
######################
[[kb <= k*b] -> [ky >= k*y] -> [ufloor_log_(k;kb;ky) >= floor_log_(b;y)]]
    !! [ufloor_log_(k;kb+1;ky) <= ufloor_log_(k;kb;ky)]
    !! [ufloor_log_(k;kb;ky) <= ufloor_log_(k;kb;ky+1)]
    !! [ufloor_log_(k;k*b;k*y) >= floor_log_(b;y)]
######################
[[(lb_,le) := dfloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb >= k*b] -> [ky <= k*y] -> [le <= e]]
    !!v[[kb >= k*b] -> [ky <= k*y] -> [dfloor_log_(k;kb;ky) <= floor_log_(b;y)]]
######################
[[(gb_,ge) := ufloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb <= k*b] -> [ky >= k*y] -> [ge >= e]]
    !! [[kb <= k*b] -> [ky >= k*y] -> [ufloor_log_(k;kb;ky) >= floor_log_(b;y)]]
######################
[[(lb_,le) := dfloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb >= k*b] -> [ky <= k*y] -> [le == e] -> [lb_ <= k*b_]]
    [[proof:
    !! [floor_log_ex_(b;y) =[def]= if y < b then (y,0) else fmap (1+) floor_log_ex_(b;y/b)]
    !! [dfloor_log_ex_(k;kb;ky) =[def]= if ky < kb then (ky,0) else fmap (1+) dfloor_log_ex_(k;kb;floor(k*ky/kb))]
    #induction:
    * [le == e == 0]:
        [lb_ == ky <= k*y == k*b_]
    * [le == e >= 1]:
        [y >= b]
        [ky >= kb]
        !! [kb >= k*b][ky <= k*y]
        [ky*k*b <= k*y*kb]
        [ky/kb <= y/b]
        [(k*ky/kb) <= k*(y/b)]
        [floor(k*ky/kb) <= k*(y/b)]
        ...recur apply induction...
    DONE
    ]]

######################
[[(gb_,ge) := ufloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb <= k*b] -> [ky >= k*y] -> [ge == e] -> [gb_ >= k*b_]]
    [[proof:
    !! [floor_log_ex_(b;y) =[def]= if y < b then (y,0) else fmap (1+) floor_log_ex_(b;y/b)]
    !! [ufloor_log_ex_(k;kb;ky) =[def]= if ky < kb then (ky,0) else fmap (1+) ufloor_log_ex_(k;kb;ceil(k*ky/kb))]
    #induction:
    * [ge == e == 0]:
        [gb_ == ky >= k*y == k*b_]
    * [ge == e >= 1]:
        [y >= b]
        [ky >= kb]
        !! [kb <= k*b][ky >= k*y]
        [ky*k*b >= k*y*kb]
        [ky/kb >= y/b]
        [(k*ky/kb) >= k*(y/b)]
        [ceil(k*ky/kb) >= k*(y/b)]
        ...recur apply induction...
    DONE
    ]]

######################
######################
######################
######################

===

[1 < b < y]:
    [y[0] := y]
    [b[0] := b]
    [1 < b[0] < y[0]]
    [1 <= b[i] < y[i]]
    * [b[i] == 1]:
        #stop
        [cf[i:] = [+oo]*inf]
    * [b[i] > 1]:
        [(b[i+1], cf[i]) := floor_log_ex_(b[i];y[i])]
        [1 <= b[i+1] < b[i]]
        [y[i+1] := b[i]]
        [1 <= b[i+1] < y[i+1]]


===


[1 < b < y][k >= 1]:
    ############
    [y[0] := y]
    [b[0] := b]
    [1 < b[0] < y[0]]
    [1 <= b[2*i] < y[2*i]]

    ############
    #le
    [lky[0] := k*y]
    [lkb[0] := k*b]
    [lkb[0] >= k*b[0]]
    [lky[0] <= k*y[0]]
    [k < lkb[0] < lky[0]]
    [k <= lkb[2*i] < lky[2*i]]

    ############
    #ge
    [gky[0] := k*y]
    [gkb[0] := k*b]
    [gkb[0] <= k*b[0]]
    [gky[0] >= k*y[0]]
    [k < gkb[0] < gky[0]]
    [k <= gkb[2*i] < gky[2*i]]










    ############
    ############
    [lcf[2*i] := dfloor_log_(k;lkb[2*i];lky[2*i])]
    [gcf[2*i] := ufloor_log_(k;gkb[2*i];gky[2*i])]

    # swith d/u --> u/d
    [lcf[2*i+1] := ufloor_log_(k;lkb[2*i+1];lky[2*i+1])]
    [gcf[2*i+1] := dfloor_log_(k;gkb[2*i+1];gky[2*i+1])]



    ############
    ############
    [1 <= b[2*i] < y[2*i]]
    * [b[2*i] == 1]:
        #stop
        [cf[2*i:] = [+oo]*inf]
    * [b[2*i] > 1]:
        [(b[2*i+1], cf[2*i]) := floor_log_ex_(b[2*i];y[2*i])]
        [1 <= b[2*i+1] < b[2*i]]
        [y[2*i+1] := b[2*i]]
        [1 <= b[2*i+1] < y[2*i+1]]

    ############
    [k <= lkb[2*i] < lky[2*i]]
    * [lkb[2*i] == k]:
        #stop
        [lcf[2*i:] = [+oo]*inf]
    * [lkb[2*i] > k]:
        [(lkb[2*i+1], lcf[2*i]) := dfloor_log_ex_(k;lkb[2*i];lky[2*i])]
        [k <= lkb[2*i+1] < lkb[2*i]]
        [lky[2*i+1] := lkb[2*i]]
        [k <= lkb[2*i+1] < lky[2*i+1]]

    ############
    [k <= gkb[2*i] < gky[2*i]]
    * [gkb[2*i] == k]:
        #stop
        [gcf[2*i:] = [+oo]*inf]
    * [gkb[2*i] > k]:
        [(gkb[2*i+1], gcf[2*i]) := ufloor_log_ex_(k;gkb[2*i];gky[2*i])]
        [k <= gkb[2*i+1] < gkb[2*i]]
        [gky[2*i+1] := gkb[2*i]]
        [k <= gkb[2*i+1] < gky[2*i+1]]





    ############
    ############
    [1 <= b[2*i+1] < y[2*i+1]]
    * [b[2*i+1] == 1]:
        #stop
        [cf[2*i+1:] = [+oo]*inf]
    * [b[2*i+1] > 1]:
        [(b[2*(i+1)], cf[2*i+1]) := floor_log_ex_(b[2*i+1];y[2*i+1])]
        [1 <= b[2*(i+1)] < b[2*i+1]]
        [y[2*(i+1)] := b[2*i+1]]
        [1 <= b[2*(i+1)] < y[2*(i+1)]]

    ############
    [k <= lkb[2*i+1] < lky[2*i+1]]
    * [lkb[2*i+1] == k]:
        #stop
        [lcf[2*i+1:] = [+oo]*inf]
    * [lkb[2*i+1] > k]:
        [(lkb[2*(i+1)], lcf[2*i+1]) := ufloor_log_ex_(k;lkb[2*i+1];lky[2*i+1])]
            # d --> u
        [k <= lkb[2*(i+1)] < lkb[2*i+1]]
        [lky[2*(i+1)] := lkb[2*i+1]]
        [k <= lkb[2*(i+1)] < lky[2*(i+1)]]

    ############
    [k <= gkb[2*i+1] < gky[2*i+1]]
    * [gkb[2*i+1] == k]:
        #stop
        [gcf[2*i+1:] = [+oo]*inf]
    * [gkb[2*i+1] > k]:
        [(gkb[2*(i+1)], gcf[2*i+1]) := dfloor_log_ex_(k;gkb[2*i+1];gky[2*i+1])]
            # u --> d
        [k <= gkb[2*(i+1)] < gkb[2*i+1]]
        [gky[2*(i+1)] := gkb[2*i+1]]
        [k <= gkb[2*(i+1)] < gky[2*(i+1)]]


    ############
    ############
===
#vs: cf, lcf, gcf

[[lcf[:2*i] == cf[:2*i]] -> [[lkb[2*i] >= k*b[2*i]][lky[2*i] <= k*y[2*i]][lcf[2*i] <= cf[2*i]]]]
[[lcf[:2*i+1] == cf[:2*i+1]] -> [[lkb[2*i+1] <= k*b[2*i+1]][lky[2*i+1] >= k*y[2*i+1]][lcf[2*i+1] >= cf[2*i+1]]]]
    [[proof:the above 2:
    by induction:
    ######################
    * [n==2*i][i==0]:
        [lkb[0] >= k*b[0]]
        [lky[0] <= k*y[0]]
        !! [dfloor_log_(k;kb;ky) <= dfloor_log_(k;kb;ky+1)]
        !! [dfloor_log_(k;kb+1;ky) <= dfloor_log_(k;kb;ky)]
        [dfloor_log_(k;lkb[0];lky[0]) <= dfloor_log_(k;k*b[0];k*y[0])]

        !! [dfloor_log_(k;k*b;k*y) <= floor_log_(b;y)]
        [dfloor_log_(k;lkb[0];lky[0]) <= dfloor_log_(k;k*b[0];k*y[0]) <= floor_log_(b[0];y[0])]

        !! [(b[2*i+1], cf[2*i]) := floor_log_ex_(b[2*i];y[2*i])]
        !! [(lkb[2*i+1], lcf[2*i]) := dfloor_log_ex_(k;lkb[2*i];lky[2*i])]
        [lcf[0] <= cf[0]]

        ==>> [[lkb[0] >= k*b[0]][lky[0] <= k*y[0]][lcf[0] <= cf[0]]]
        ==>> [[lkb[2*i] >= k*b[2*i]][lky[2*i] <= k*y[2*i]][lcf[2*i] <= cf[2*i]]]

    ######################
    ######################
    * [n==2*i+1][i>=0][[lkb[2*i] >= k*b[2*i]][lky[2*i] <= k*y[2*i]][lcf[2*i] <= cf[2*i]]][lcf[:2*i+1] == cf[:2*i+1]]:
        !! [lcf[:2*i+1] == cf[:2*i+1]]
        [lcf[2*i] == cf[2*i]]

        !! [[(lb_,le) := dfloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb >= k*b] -> [ky <= k*y] -> [le == e] -> [lb_ <= k*b_]]
        !! [(b[2*i+1], cf[2*i]) := floor_log_ex_(b[2*i];y[2*i])]
        !! [(lkb[2*i+1], lcf[2*i]) := dfloor_log_ex_(k;lkb[2*i];lky[2*i])]
        !! [lkb[2*i] >= k*b[2*i]]
        !! [lky[2*i] <= k*y[2*i]]
        !! [lcf[2*i] == cf[2*i]]
        [lkb[2*i+1] <= k*b[2*i+1]]



        !! [lkb[2*i] >= k*b[2*i]]
        !! [y[2*i+1] := b[2*i]]
        !! [lky[2*i+1] := lkb[2*i]]
        [lky[2*i+1] >= k*y[2*i+1]]



        !! [[(gb_,ge) := ufloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb <= k*b] -> [ky >= k*y] -> [ge >= e]]
        !! [(b[2*(i+1)], cf[2*i+1]) := floor_log_ex_(b[2*i+1];y[2*i+1])]
        !! [(lkb[2*(i+1)], lcf[2*i+1]) := ufloor_log_ex_(k;lkb[2*i+1];lky[2*i+1])]
        !! [lkb[2*i+1] <= k*b[2*i+1]]
        !! [lky[2*i+1] >= k*y[2*i+1]]
        [lcf[2*i+1] >= cf[2*i+1]]


        ==>> [[lkb[2*i+1] <= k*b[2*i+1]][lky[2*i+1] >= k*y[2*i+1]][lcf[2*i+1] >= cf[2*i+1]]]

    ######################
    ######################
    * [n==2*(i+1)][i>=0][[lkb[2*i+1] <= k*b[2*i+1]][lky[2*i+1] >= k*y[2*i+1]][lcf[2*i+1] >= cf[2*i+1]]][lcf[:2*(i+1)] == cf[:2*(i+1)]]:
        !! [lcf[:2*(i+1)] == cf[:2*(i+1)]]
        [lcf[:2*i+1] == cf[:2*i+1]]

        !! [[(gb_,ge) := ufloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb <= k*b] -> [ky >= k*y] -> [ge == e] -> [gb_ >= k*b_]]
        !! [(b[2*(i+1)], cf[2*i+1]) := floor_log_ex_(b[2*i+1];y[2*i+1])]
        !! [(lkb[2*(i+1)], lcf[2*i+1]) := ufloor_log_ex_(k;lkb[2*i+1];lky[2*i+1])]
        !! [lkb[2*i+1] <= k*b[2*i+1]]
        !! [lky[2*i+1] >= k*y[2*i+1]]
        [lkb[2*(i+1)] >= k*b[2*(i+1)]]


        !! [lkb[2*i+1] <= k*b[2*i+1]]
        !! [y[2*(i+1)] := b[2*i+1]]
        !! [lky[2*(i+1)] := lkb[2*i+1]]
        [lky[2*(i+1)] <= y[2*(i+1)]]



        !! [[(lb_,le) := dfloor_log_ex_(k;kb;ky)] -> [(b_,e) := floor_log_ex_(b;y)] -> [kb >= k*b] -> [ky <= k*y] -> [le <= e]]
        !! [(b[2*i+1], cf[2*i]) := floor_log_ex_(b[2*i];y[2*i])]
        !! [(lkb[2*i+1], lcf[2*i]) := dfloor_log_ex_(k;lkb[2*i];lky[2*i])]
        !! [lkb[2*(i+1)] >= k*b[2*(i+1)]]
        !! [lky[2*(i+1)] <= k*y[2*(i+1)]]
        [lcf[2*(i+1)] <= cf[2*(i+1)]]


        ==>> [[lkb[2*(i+1)] >= k*b[2*(i+1)]][lky[2*(i+1)] <= k*y[2*(i+1)]][lcf[2*(i+1)] <= cf[2*(i+1)]]]
        ==>> [[lkb[2*i] >= k*b[2*i]][lky[2*i] <= k*y[2*i]][lcf[2*i] <= cf[2*i]]]
    ######################
    ######################

    DONE
    ]]
==>>:
[[lcf[:2*i] == cf[:2*i]] -> [lcf[2*i] <= cf[2*i]]]
[[lcf[:2*i+1] == cf[:2*i+1]] -> [lcf[2*i+1] >= cf[2*i+1]]]


===

[[gcf[:2*i] == cf[:2*i]] -> [[gkb[2*i] <= k*b[2*i]][gky[2*i] >= k*y[2*i]][gcf[2*i] >= cf[2*i]]]]
[[gcf[:2*i+1] == cf[:2*i+1]] -> [[gkb[2*i+1] >= k*b[2*i+1]][gky[2*i+1] <= k*y[2*i+1]][gcf[2*i+1] <= cf[2*i+1]]]]
    proof:vivi-above
==>>:
[[gcf[:2*i] == cf[:2*i]] -> [gcf[2*i] >= cf[2*i]]]
[[gcf[:2*i+1] == cf[:2*i+1]] -> [gcf[2*i+1] <= cf[2*i+1]]]

===
===
[lcf <= cf]
    !! [[lcf[:2*i] == cf[:2*i]] -> [lcf[2*i] <= cf[2*i]]]
    !! [[lcf[:2*i+1] == cf[:2*i+1]] -> [lcf[2*i+1] >= cf[2*i+1]]]
===
[gcf >= cf]
    !! [[gcf[:2*i] == cf[:2*i]] -> [gcf[2*i] >= cf[2*i]]]
    !! [[gcf[:2*i+1] == cf[:2*i+1]] -> [gcf[2*i+1] <= cf[2*i+1]]]
===
[lcf <= cf <= gcf]
    !! [lcf <= cf]
    !! [gcf >= cf]
===
]]]

[[[
view others/数学/continued-fraction/continued_fraction_of_log2_X.txt

/sdcard/0my_files/book/math/continued_fraction/On Shanks algorithm for computing the continued fraction of log_b_a(2002)(Terence).pdf
===
https://cs.uwaterloo.ca/journals/JIS/VOL5/Jackson/matthews3.html
  wget_U 'https://cs.uwaterloo.ca/journals/JIS/VOL5/Jackson/matthews3.pdf' -O 'On Shanks algorithm for computing the continued fraction of log_b_a(2002)(Terence).pdf'
  Abstract: We give a more practical variant of Shanks' 1954 algorithm for computing the continued fraction of log_b a, for integers a > b > 1, using the floor and ceiling functions and an integer parameter c > 1. The variant, when repeated for a few values of c = 10^r, enables one to guess if log_b a is rational and to find approximately r partial quotients.


]]]












script.log_b_y
py -m nn_ns.app.debug_cmd   script.log_b_y -x
py -m nn_ns.app.doctest_cmd script.log_b_y:__doc__ -ff -v
py_adhoc_call   script.log_b_y   ,iter_continued_fraction_of_log__truncated_ =100  =2  =3
py_adhoc_call   script.log_b_y   ,iter_continued_fraction_of_log__truncated_ ='1<<10000'  =2  =3 > /sdcard/0my_files/tmp/out4py/script.log_b_y..1p10000-2-3.out.txt
view  /sdcard/0my_files/tmp/out4py/script.log_b_y..1p10000-2-3.out.txt
[[total 2943:cf_log_(2;3)[2938-1]==19
1
1
1
2
2
3
1
5
2
23
2
2
1
1
55
1
... ...
... ...
3
3
25
1
19
1
2
1
2
1
]]


#]]]'''
__all__ = r'''
    dfloor_log_ex_
    ufloor_log_ex_
    iter_xbound_continued_fraction_of_log_
    iter_continued_fraction_of_log__truncated_
'''.split()#'''


def dfloor_log_ex_(k, kb, ky, /):
    assert 1 <= k
    assert k < kb
    assert k <= ky
    # [k < kb]
    # [k <= ky]
    e = 0
    while not ky < kb:
        # [k < kb <= ky]
        # [k < k*kb <= k*ky]
        # [k <= k*ky/kb]
        # [k <= k*ky//kb]
        ky = (k*ky)//kb
        # [k <= ky]
        ######################
        # proof_termination_of_dfloor_log_
        # [old_ky >= kb > k >= 1]
        # [old_ky >= 2]
        # !! [k < kb]
        # [k/kb < 1]
        # [old_ky*(k/kb) < old_ky]
        # [new_ky <= k*old_ky/kb < old_ky] --> [not dead loop]
        # termination
        ######################
        e += 1
    # [k <= ky < kb]
    assert k <= ky < kb
    return ky, e


def ufloor_log_ex_(k, kb, ky, /):
    assert 1 <= k
    assert k < kb
    assert k <= ky
    # [k < kb]
    # [k <= ky]
    e = 0
    while not ky < kb:
        # [k < kb <= ky]
        # [k < k*kb <= k*ky]
        # [k <= k*ky/kb]
        # [k <= ceil(k*ky/kb) == (k*ky-1)//kb +1]
        ky = (k*ky-1)//kb +1
        # [k <= ky]
        ######################
        # proof_termination_of_ufloor_log_
        # [old_ky >= kb > k >= 1]
        # !! [new_ky := ceil(k*ky/kb)]
        # [new_ky == ceil(k*old_ky/kb) == floor((k*old_ky-1)/kb) +1]
        # [new_ky >= old_ky]:
        #   [floor((k*old_ky-1)/kb) +1 >= old_ky]
        #   [(k*old_ky-1)/kb >= old_ky-1]
        #   [(k*old_ky-1) >= old_ky*kb -kb]
        #   [(kb-1) >= old_ky*(kb-k) >= old_ky*1]
        #   [kb > old_ky]
        #   !! [old_ky >= kb]
        #   _L
        # [new_ky < old_ky]
        # [new_ky < old_ky] --> [not dead loop]
        # termination
        ######################
        e += 1
    # [k <= ky < kb]
    assert k <= ky < kb
    return ky, e

_fs = dfloor_log_ex_, ufloor_log_ex_
def iter_xbound_continued_fraction_of_log_(lower_vs_upper, k, kb, ky, /):
    assert type(lower_vs_upper) is bool
    assert 1 <= k
    assert k <= kb
    assert k <= ky
    fs = _fs
    while k < kb:
        _kb, cf_digit = fs[lower_vs_upper](k, kb, ky)
        yield cf_digit
        kb, ky = _kb, kb
        lower_vs_upper = not lower_vs_upper
def iter_continued_fraction_of_log__truncated_(param4memory_consume, base, y, /):
    r'''[[[
    param4memory_consume -> base/int{>=1} -> y/int{>=1} -> cf/iter continued_fraction_of_log_(base; y)[:?]

    [[base==1] -> [cf == []/+oo]]

    #]]]'''#'''
    assert 1 <= param4memory_consume
    assert 1 <= base
    assert 1 <= y
    if 0:
        if base == 1:
            return

    k = param4memory_consume
    kb = k*base
    ky = k*y
    assert 1 <= k
    assert k <= kb
    assert k <= ky

    lcf = iter_xbound_continued_fraction_of_log_(False, k, kb, ky)
    gcf = iter_xbound_continued_fraction_of_log_(True, k, kb, ky)

    for a, b in zip(lcf, gcf):
        if a == b:
            yield a
        else:
            #truncate
            break

#null_iter = iter('')









__all__


from script.log_b_y import dfloor_log_ex_, ufloor_log_ex_, iter_xbound_continued_fraction_of_log_, iter_continued_fraction_of_log__truncated_
from script.log_b_y import *
