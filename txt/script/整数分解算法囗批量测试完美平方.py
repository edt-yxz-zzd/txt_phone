#__all__:goto
r'''[[[
e script/整数分解算法囗批量测试完美平方.py
view others/数学/prime/primality_test.txt


script.整数分解算法囗批量测试完美平方
py -m nn_ns.app.debug_cmd   script.整数分解算法囗批量测试完美平方 -x
py -m nn_ns.app.doctest_cmd script.整数分解算法囗批量测试完美平方:__doc__ -ff -v
py_adhoc_call   script.整数分解算法囗批量测试完美平方   @f
from script.整数分解算法囗批量测试完美平方 import *


[[[
===
[m >= 3][m%2 == 1][m >= (2*B+1)*(2*B+1)][s,t >= B > 0][m == (2*s+1)*(2*t+1)]:
    [h := (m-1)///2]
    [m == 2*h +1]
    [m == 4*s*t +2*(s+t) +1]
    [h == 2*s*t +(s+t)]

    [(s-B)*(t-B) >= 0]
    [(s*t) >= B*(s+t) -B**2 == B*(s+t-B)]
    [(s*t) >= B*(s+t-B)]

    [m == 4*s*t +2*(s+t) +1
    >= 4*B*(s+t-B) +2*(s+t) +1
    == (2*B+1)*(2*(s+t-B)+1)
    ]
    [m >= (2*B+1)*(2*(s+t-B)+1)]
    [(s+t)
    <= (m/(2*B+1) -1)/2 +B
    == m/2/(2*B+1) -1/2 +B
    == (h +1/2)/(2*B+1) -1/2 +B
    == (h -B)/(2*B+1) +B
    ]
    [(s+t) <= floor_((h -B)/(2*B+1)) +B]

    [(q,r) := h %/ 2]
    [h == 2*q +r]
    [0 <= r < 2]
    !! [m == 2*h +1]
    [m == 2*(2*q +r) +1]
    [m == 4*q +2*r +1]
    [m/4 == q +r/2 +1/4]

    [v := (s*t)]
    [dqv := q-v]
    [s*t == v == q-dqv]
    !! [h == 2*s*t +(s+t)]
    [h == 2*v +(s+t)]
    !! [h == 2*q +r]
    [(s+t) == h -2*v == r +2*(q-v) == r +2*dqv]
    [B**2 <= s*t == v <= q]
    [q-B**2 >= dqv >= 0]

    [(s+t) == r +2*dqv]
    [s*t == q-dqv]
    [(s-t)**2
    == (s+t)**2 -4*s*t
    == (r +2*dqv)**2 -4*(q-dqv)
    ]
    [(s-t)**2 == ((r +2*dqv)**2 -4*(q-dqv))]
    [[(s,t) have integer solutions] <-> [sqrt((r +2*dqv)**2 -4*(q-dqv)) %1 == 0]]


    !! [(s+t)**2 >= 4*(s*t)]
    !! [(s+t) == r +2*dqv]
    !! [s*t == q-dqv]
    [(r +2*dqv)**2 >= 4*(q-dqv)]
    [(r**2 +4*r*dqv +4*dqv**2) >= (4*q-4*dqv)]
    [(r**2/4 -q) +(r+1)*dqv +dqv**2 >= 0]
        #对称轴: [dqv == -(r+1)/2 < 0]
    !! [dqv >= 0]
    [dqv >= max{0,ceil_(大根)}]
    [dqv
    >= (-(r+1) +sqrt((r+1)**2 -4*(r**2/4 -q)))/2
    == (-(r+1) +sqrt(2*r+1 +4*q))/2
    !! [h == 2*q +r]
    == (-(r+1) +sqrt(2*h+1))/2
    !! [m == 2*h +1]
    == (-(r+1) +sqrt(m))/2
    ]
    [dqv >= ceil_((-(r+1) +sqrt(m))/2)]
    [-1 < (-(r+1) +sqrt(m))/2]
        <==> [r-1 < sqrt(m)]
        !! [0 <= r < 2]
        # [-1 <= r-1 <= 0]
        !! [m > 0]
        <==> True
    [0 <= ceil_(-(r+1) +sqrt(m))/2]
    [dqv >= ceil_((-(r+1) +sqrt(m))/2) >= 0]

    !! [(s*t) >= B*(s+t-B)]
    !! [(s+t) == r +2*dqv]
    !! [s*t == q-dqv]
    [(q-dqv) >= B*(r +2*dqv-B)]
    [q -B*r +B*B >= (2*B+1)*dqv]
    [dqv <= floor_((q -B*r +B*B)/(2*B+1))]
    [dqv
    <= floor_((q -B*r +B*B)/(2*B+1))
    == floor_((q -B*(h-2*q) +B*B)/(2*B+1))
    == q +floor_((-B*h +B*B)/(2*B+1))
    == q -ceil_(B*(h-B)/(2*B+1))

    == q +floor_((-B*h +B*B)/(2*B+1))
    == q +floor_((-B*(m-1) +2*B*B)/2/(2*B+1))
    == q +floor_((-B*m +B +2*B*B)/2/(2*B+1))
    == q +floor_((-B*m)/2/(2*B+1) +B/2)
    == q +floor_((-(B+1/2)*m +m/2)/2/(2*B+1) +B/2)
    == q +floor_(m/16/(B/2+1/4) +(B/2+1/4) -1/4 -m/4)
    !! [m/4 == q +r/2 +1/4]
    == floor_(m/16/(B/2+1/4) +(B/2+1/4) -1/2 -r/2)
        * [m/16/(B/2+1/4) == (B/2+1/4)]:
            [(B/2+1/4) == sqrt(m)/4]
            min max ... >= q +floor_(sqrt(m)/2 -1/4 -m/4)
            == floor_(sqrt(m)/2 -1/2 -r/2)
    ]
    [dqv <= floor_((q -B*r +B*B)/(2*B+1))
    == floor_(m/16/(B/2+1/4) +(B/2+1/4) -1/2 -r/2)
    ]
    [dqv >= ceil_((-(r+1) +sqrt(m))/2) >= 0]
    目标:
        [dqv :<- [ceil_((-(r+1) +sqrt(m))/2)..=floor_((q -B*r +B*B)/(2*B+1))]:
            search dqv :=> [sqrt((r +2*dqv)**2 -4*(q-dqv)) %1 == 0]
            问题是，用 中国剩余定理 感觉 搜索还是很慢

    * [m%4 == 3]:
        [{2*s+1,2*t+1}%4 == {1,3}]
        [{2*s,2*t}%4 == {0,2}]
        [{s,t}%2 == {0,1}]
        [(s*t)%2 == 0]
        [(s+t)%2 == 1]
        [(q,r) := h %/ 2]
        [h == 2*q +r]
        [0 <= r < 2]
        [v := (s*t)///2]
        [s*t == 2*v]
        !! [h == 2*s*t +(s+t)]
        [h == 4*v +(s+t)]
    * [m%4 == 1]:
        * [{2*s+1,2*t+1}%4 == {3}]:
            [{2*s,2*t}%4 == {2}]
            [{s,t}%2 == {1}]
            [(s*t)%2 == 1]
            [(s+t)%2 == 0]
        * [{2*s+1,2*t+1}%4 == {1}]:
            [{2*s,2*t}%4 == {0}]
            [{s,t}%2 == {0}]
            [(s*t)%4 == 0]
            [(s+t)%2 == 0]
]]]



#]]]'''
__all__ = r'''
'''.split()#'''
__all__

def factor_odd_pint_via_batch_detect_perfect_squares_using_CRT_(odd, /):
    assert odd > 0
    assert odd&1 == 1
    if odd == 1:
        return {}


if __name__ == "__main__":
    pass
__all__


from script.整数分解算法囗批量测试完美平方 import *
