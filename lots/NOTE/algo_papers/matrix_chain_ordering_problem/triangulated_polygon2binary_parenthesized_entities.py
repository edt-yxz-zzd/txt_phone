


r'''

n-gon
    n >= 3
    vertices of n-gon = [0..n-1]
    edges/sides of n-gon = {(i-1,i) | i <- [1..n-1]} \-/ {(n-1,0)}

    triangulated n-gon :: [(Vertex, Vertex)]
        (n-3) diagonals which not cross each other

(n-1) entities
    entities = [0..n-2]
    binary parenthesized (n-1) entities :: [(num_closes::UInt, num_opens::UInt)]
        len = n
        (n-2) parentheses
            -- (n-3) diagonals
            -- and (n-1,0)
            (n-2) opens
            (n-2) closes

parentheses_tree:
    parentheses_tree = tuple<parentheses_tree>
    leaf: ()
binary_tree
    (n-2) parentheses   -- inner nodes
    (n-1) entities      -- outer nodes
    binary_tree = (binary_tree, binary_tree) | (entity :: UInt)
'''

__all__ = '''
    triangulated_polygon2binary_parenthesized_entities
    binary_parenthesized_entities2binary_tree
    parenthesized_entities2parentheses_tree
    '''.split()

from itertools import chain

def triangulated_polygon2binary_parenthesized_entities(triangulated_polygon):
    # triangulated_polygon :: [(Vertex, Vertex)]
    # type Vertex = int
    # input: triangulated n-gon
    #       i.e. (n-3) diagonals :: [(Vertex, Vertex)]
    # output: binary parenthesized (n-1) entities / (n-2) parentheses
    #       i.e. n num_pairs :: [(num_closes, num_opens)]

    n_3 = len(triangulated_polygon)
    n = n_3+3
    close_idx = 0
    open_idx = 1

    # side: (n-1,0)
    global_side = (n-1,0)
    diagonals = triangulated_polygon
    it = chain([global_side], diagonals)
    parenthesized_entities = [[0,0] for _ in range(n)]
    for (v,u) in it:
        v,u = min(v,u), max(v,u)
        assert 0 <= v < u < n
        parenthesized_entities[v][open_idx] += 1
        parenthesized_entities[u][close_idx] += 1
    parenthesized_entities = [(num_closes, num_opens) for num_closes, num_opens in parenthesized_entities]
    return parenthesized_entities

assert triangulated_polygon2binary_parenthesized_entities([]) == [(0,1),(0,0),(1,0)]
assert triangulated_polygon2binary_parenthesized_entities([(0,2)]) == [(0,2),(0,0),(1,0),(1,0)]
assert triangulated_polygon2binary_parenthesized_entities([(1,3)]) == [(0,1),(0,1),(0,0),(2,0)]
assert triangulated_polygon2binary_parenthesized_entities([(0,2),(0,3)]) == [(0,3),(0,0),(1,0),(1,0),(1,0)]
assert triangulated_polygon2binary_parenthesized_entities([(0,2),(2,4)]) == [(0,2),(0,0),(1,1),(0,0),(2,0)]
assert triangulated_polygon2binary_parenthesized_entities([(1,3),(0,3)]) == [(0,2),(0,1),(0,0),(2,0),(1,0)]
assert triangulated_polygon2binary_parenthesized_entities([(1,4),(2,4)]) == [(0,1),(0,1),(0,1),(0,0),(3,0)]
assert triangulated_polygon2binary_parenthesized_entities([(1,3),(1,4)]) == [(0,1),(0,2),(0,0),(1,0),(2,0)]

def binary_parenthesized_entities2binary_tree(parenthesized_entities):
    # binary parenthesized_entities :: [(num_closes, num_opens)]
    # output: binary_tree = (binary_tree, binary_tree) | (entity :: UInt)
    tree = parenthesized_entities2parentheses_tree(parenthesized_entities)
    entity = -1
    def this_func(tree):
        nonlocal entity
        if not tree:
            entity += 1
            return entity
        if len(tree) != 2:
            raise ValueError('not binary_parenthesized_entities')
        L, R = tree # binary
        return (this_func(L), this_func(R))
    binary_tree = this_func(tree)
    n = len(parenthesized_entities)
    assert entity == n-2
    return binary_tree


def parenthesized_entities2parentheses_tree(parenthesized_entities):
    # parenthesized_entities :: [(num_closes, num_opens)] # may not binary
    # output: parentheses_tree = tuple<parentheses_tree>

    n = len(parenthesized_entities)
    assert n >= 2
    it = iter(parenthesized_entities)
    entities = []
    num_opens_tree_pairs = [] # [(num_opens, tree)]
    total_unclosed_opens = 0
    entity = ()
    for (num_closes, num_opens) in (parenthesized_entities):
        assert num_closes >= 0
        assert num_opens >= 0
        new_num_opens = num_opens

        total_unclosed_opens -= num_closes
        if total_unclosed_opens < 0: raise ValueError('mismatched closes')
        total_unclosed_opens += num_opens

        for _ in range(num_closes):
            reversed_nodes = []
            while True:
                num_opens, node = num_opens_tree_pairs.pop()
                reversed_nodes.append(node)
                if num_opens:
                    num_opens -= 1
                    node = tuple(reversed(reversed_nodes))
                    num_opens_tree_pairs.append((num_opens, node))
                    break
            pass
        pass

        num_opens_tree_pairs.append((new_num_opens, entity))
    if total_unclosed_opens > 0: raise ValueError('mismatched opens')
    if len(num_opens_tree_pairs) < 2: raise ValueError('too few input data')
    if len(num_opens_tree_pairs) > 2: raise ValueError('no global parenthesis')
    num_opens_tree_pairs.pop()
    [(_, tree)] = num_opens_tree_pairs

    return tree
assert parenthesized_entities2parentheses_tree([(0,1), (1,0)]) == ((),)
#                                                  ( () )

assert parenthesized_entities2parentheses_tree([(0,2),(2,0)]) == (((),),)
assert parenthesized_entities2parentheses_tree([(0,3),(3,0)]) == ((((),),),)
assert parenthesized_entities2parentheses_tree([(0,1),(0,0),(1,0)]) == ((),())

assert parenthesized_entities2parentheses_tree([(0,1), (0,0), (0,1), (2,0)]) == ((),(),((),))
#                                                  ( ()     ()   ( () ))
#                                                  1 ,,     ,,   1 ,, 22



assert binary_parenthesized_entities2binary_tree([(0,1),(0,0),(1,0)]) == (0,1)
assert binary_parenthesized_entities2binary_tree([(0,2),(0,0),(1,0),(1,0)]) == ((0,1),2)
assert binary_parenthesized_entities2binary_tree([(0,1),(0,1),(0,0),(2,0)]) == (0,(1,2))
assert binary_parenthesized_entities2binary_tree([(0,3),(0,0),(1,0),(1,0),(1,0)]) == (((0,1),2),3)
assert binary_parenthesized_entities2binary_tree([(0,2),(0,0),(1,1),(0,0),(2,0)]) == ((0,1),(2,3))
assert binary_parenthesized_entities2binary_tree([(0,2),(0,1),(0,0),(2,0),(1,0)]) == ((0,(1,2)),3)
assert binary_parenthesized_entities2binary_tree([(0,1),(0,1),(0,1),(0,0),(3,0)]) == (0,(1,(2,3)))
assert binary_parenthesized_entities2binary_tree([(0,1),(0,2),(0,0),(1,0),(2,0)]) == (0,((1,2),3))


