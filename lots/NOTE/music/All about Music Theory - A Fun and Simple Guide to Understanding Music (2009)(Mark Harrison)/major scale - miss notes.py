

'''
WWHWWWH
'''

from pprint import pprint
from itertools import combinations

steps = (1,2,2,1,2,2,2) # 0==7; step[i] = pitch(i+1)-pitch(i)

def miss_N_notes(num_misses, steps=steps):
    # 0 < N < D = len(steps)
    # D == 7; N = num_misses
    # @yield : steps'::tuple, miss_notes::frozenset
    #       where len(steps') == D-N, len(miss_notes)=N
    D = len(steps)
    N = num_misses
    assert 0 < N < D
    for misses in combinations(range(D), N):
        will_drops = [False]*D
        for x in misses:
            will_drops[x]=True
        steps_ = [0]
        # steps'[0] to wrap the list
        for will_drop, step, note in zip(will_drops, steps, range(D)):
            # current: step'[-1] === step{prev(note)-[skip_miss]->note}
            # input: step = steps[note] = step{note->note+1}
            if will_drop:
                # drop note;
                steps_[-1] += step
                # step'[-1] === step{prev(note)-[skip_miss]->note->note+1}
                # drop note ==>> prev(note+1) == prev(note)
                # next round begins with:
                #   step'[-1] === step{prev(note+1)-[skip_miss]->note+1}
            else:
                # not drop note
                steps_.append(step)
                # step'[-1] === step{note->note+1}
                # not drop note ==>> prev(note+1) == note
                # next round begins with:
                #   step'[-1] === step{prev(note+1)-[skip_miss]->note+1}

        last = steps_.pop()
        steps_[0] += last
        steps_ = tuple(steps_)
        assert len(steps_) == D-N
        assert sum(steps_) == sum(steps)
        misses = frozenset(misses)
        assert len(misses) == N
        yield steps_, misses
def iter_find(x, array, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(array)
    for i in range(begin, end):
        if x == array[i]:
            yield i
def std_steps(steps):
    # min{rotate steps}
    m = min(steps)
    steps_ = steps
    for i in iter_find(m, steps):
        steps_2 = steps[i:] + steps[:i]
        steps_ = min(steps_, steps_2)
    assert steps_[0] == m
    return steps_


def find_nondetermine_major_scale_if_miss_N_notes(N, steps=steps):
    steps2missess = {}
    for steps_, misses in miss_N_notes(N, steps=steps):
        steps_2 = std_steps(steps_)
        if steps_2 not in steps2missess:
            steps2missess[steps_2] = []
        misses = tuple(sorted(misses))
        steps2missess[steps_2].append(misses)
    steps2missess = {k:sorted(ls)
        for k, ls in steps2missess.items() if len(ls)>1}
    return steps2missess

def steps2missess__tuple2str(steps2missess):
    # assume D == 7
    def tuple2str(t):
        return ''.join(map('{:x}'.format, t))
    f = tuple2str
    return {f(k):list(map(f,ls)) for k,ls in steps2missess.items()}
def _t(MaxN=6):
    for N in range(1,MaxN+1):
        steps2missess = find_nondetermine_major_scale_if_miss_N_notes(N)
        steps2missess = steps2missess__tuple2str(steps2missess)
        pprint(steps2missess)

'''
{'122322': ['0', '4']}
{'12234': ['02', '46'],
 '12252': ['01', '45'],
 '12522': ['06', '34'],
 '14322': ['05', '24'],
 '22323': ['03', '04', '14']}
{'1227': ['012', '456'],
 '1254': ['026', '346'],
 '1272': ['016', '345'],
 '1434': ['025', '246'],
 '1452': ['015', '245'],
 '1722': ['056', '234'],
 '2235': ['023', '046', '134'],
 '2253': ['013', '045', '124'],
 '2325': ['014', '034', '036', '145'],
 '2343': ['024', '035', '146']}
{'129': ['0126', '3456'],
 '147': ['0125', '2456'],
 '174': ['0256', '2346'],
 '192': ['0156', '2345'],
 '228': ['0123', '0456', '1234'],
 '237': ['0146', '0234', '0356', '1345'],
 '255': ['0134', '0145', '0236', '0346', '1245'],
 '273': ['0124', '0136', '0345', '1456'],
 '345': ['0135', '0245', '1246'],
 '354': ['0235', '0246', '1346']}
{'1b': ['01256', '23456'],
 '2a': ['01234', '01236', '01456', '03456', '12345'],
 '39': ['01246', '01356', '02345', '13456'],
 '48': ['01235', '02456', '12346'],
 '57': ['01245', '01345', '01346', '02346', '02356', '12456']}
{'c': ['012345', '012346', '012356', '012456', '013456', '023456', '123456']}

'''
if __name__ == "__main__":
    _t()

