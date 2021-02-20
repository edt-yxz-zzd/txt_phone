
r"""
e script/info_tri_planar_graphs.py
view script/draw_tri_planar_graphs.py
===
py script/info_tri_planar_graphs.py -i '/sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3/-adc3m3[4, 6, 8].txt'
py script/info_tri_planar_graphs.py -i /sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3_from4to18d.txt


cd /data/data/com.termux/files/home/src/plantri50/plantri50@termux@armv7l-unknown-linux-gnueabi/
for i in {4..20..2} ; do ./plantri -adc3m3 ${i}d ; done > ~/tmp/plantri~-adc3m3~4d-20d.txt
    726 KB
cd /sdcard/0my_files/git_repos/txt_phone/txt/
py script/info_tri_planar_graphs.py -i ~/tmp/plantri~-adc3m3~4d-20d.txt -o ~/tmp/info_tri_planar_graphs_4-20.txt
    ? MB
7z a ~/tmp/info_tri_planar_graphs_4-20.7z   script/info_tri_planar_graphs.py  ~/tmp/plantri~-adc3m3~4d-20d.txt  ~/tmp/info_tri_planar_graphs_4-20.txt


TODO: --continue_output
    read output, get nth, nv2canon2id
    DONE
TODO: stable_repr
    DONE

# recover from broken
py script/info_tri_planar_graphs.py -i /sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3_from4to18d.txt  -c ~/tmp/info_tri_planar_graphs_4-20.txt  -o ~/tmp/info_tri_planar_graphs_4-20_recover_ver2.txt

# continue to 20
py script/info_tri_planar_graphs.py -i ~/tmp/plantri~-adc3m3~4d-20d.txt   -c -o ~/tmp/info_tri_planar_graphs_4-20_recover_ver2.txt
    46.6 MB

mv -T ~/tmp/info_tri_planar_graphs_4-20_recover_ver2.txt   ~/tmp/info_tri_planar_graphs_4_20_ver2.txt
7z a ~/tmp/info_tri_planar_graphs_4_20_ver2.7z   script/info_tri_planar_graphs.py  ~/tmp/plantri~-adc3m3~4d-20d.txt  ~/tmp/info_tri_planar_graphs_4_20_ver2.txt
    2.3 MB
    #total=9150


py script/info_tri_planar_graphs.py -i ~/tmp/plantri~-adc3m3~4d-16d.txt -o ~/tmp/info_tri_planar_graphs_4_16_ver2.txt
    992 KB
7z a ~/tmp/info_tri_planar_graphs_4_16_ver2.7z   script/info_tri_planar_graphs.py  ~/tmp/plantri~-adc3m3~4d-16d.txt  ~/tmp/info_tri_planar_graphs_4_16_ver2.txt
    71 KB
    #total=306


grep '^# '  ~/tmp/info_tri_planar_graphs_4_16_ver2.txt  > ~/tmp/info_tri_planar_graphs_4_16_ver2.simplified.txt
    207 KB <- 992 KB
grep '^# '  ~/tmp/info_tri_planar_graphs_4_20_ver2.txt  > ~/tmp/info_tri_planar_graphs_4_20_ver2.simplified.txt
    11.3 MB <- 46.6 MB
7z a ~/tmp/info_tri_planar_graphs_4_16_ver2.simplified.7z   ~/tmp/info_tri_planar_graphs_4_16_ver2.simplified.txt
    16 KB <- 207 KB <- 992 KB
7z a ~/tmp/info_tri_planar_graphs_4_20_ver2.simplified.7z   ~/tmp/info_tri_planar_graphs_4_20_ver2.simplified.txt   ~/tmp/info_tri_planar_graphs_4_16_ver2.simplified.txt
    662 KB <- 11.3 MB <- 46.6 MB

moveto: mv -t /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/info_tri_planar_graphs.py.data/
    info_tri_planar_graphs_4_16_ver2.7z
    info_tri_planar_graphs_4_16_ver2.simplified.7z
    info_tri_planar_graphs_4_16_ver2.simplified.txt
    info_tri_planar_graphs_4_20_ver2.7z
    info_tri_planar_graphs_4_20_ver2.simplified.7z
    plantri~-adc3m3~4d-16d.txt
    plantri~-adc3m3~4d-20d.7z










TODO: using:
    seed.io.savefile.SaveFile::aSaveFile__TuplePerBlock
        ver3 replace infofile ver1/ver2 format
            {info}\n# {simplified_info}\n
        ver3:
            assert  ',' < '0'
            assert  ')' < '0'
            assert  '_' > '0'
            (tid=(nv, local_nth, global_nth), tri_planar_ename, tri_planar_embedding, canon=new_min_dfs, dedge_orbits::sorted_set<sorted_tuple<pair<vtx>>>, vtx_orbits::sorted_set<sorted_tuple<vtx>>, may_low_xename2miss_curr_dedge_orbit_mins::sorted_dict{(None|xename):sorted_set<min_dedge_per_orbit>})
    seed.mapping_tools.fdefault::set_fdefault,add_new_item
        replace:
            if nv not in nv2canon2id:
                nv2canon2id[nv] = {}
        by:
            set_fdefault(nv2canon2id, nv, dict)
        replace:
            canon2id[canon] = id
        by:
            add_new_item(canon2id, canon, id)
    ???
TODO: subcmd
    argparse::add_subparsers(parser_class=lambda *args, **args: ArgumentParser(*args, parents=..., **args))




===





embedding :: tuple<tuple<vtx>>
    not support multiedge ==>> simple
#embedding maynot be planar_embedding
#   planar_embedding is on plane/sphere
#embedding maynot be undirected_embedding
tri_planar_embedding = triconnected_simple_undirected_planar_embedding
    no multiedge
tri_embedding = 3-degree-simple-undirected_embedding
    no self-loop

target:
    1. order & vtx_orbits & edge_orbits & label(min_dfs) of tri_planar_graph automorphism permutation group
    2. downgrade of tri_planar_graph, i.e. remove one edge (two end_vtc disappear) and lookup whether there is isomorphism tri_planar_graph


dfs_tree str version
label_dfs_grammar:
    dfs_tree_str = dfs_sub_tree_str
    dfs_sub_tree_str = "(" dfs_sub_root (dfs_sub_tree_str|dfs_back_or_rbackedge_str)* ")"
    dfs_back_or_rbackedge_str = "[" ancestor_or_descendant_vtx "]"
    dfs_sub_root = vtx
    ancestor_or_descendant_vtx = vtx
    vtx = regex"\d"+
dfs_tree data version
    dfs_tree = dfs_sub_tree
    dfs_sub_tree = tuple<dfs_sub_root, (dfs_sub_tree|ancestor_or_descendant_vtx)*>
    ancestor_or_descendant_vtx = uint

=========
view /sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3/'-adc3m3[4, 6, 8].txt'

4 bcd,adc,abd,acb
6 bcd,aef,afd,ace,bdf,bec
8 bcd,aef,afg,agh,bhf,bec,chd,dge
8 bcd,aef,afg,age,bdh,bhc,chd,egf

num_edges = num_vertices *3/2
    # 39 = 26 *3/2
num_vertices2num_graphs = \
    {4:1
    ,6:1
    ,8:2
    ,10:5
    ,12:14
    ,14:50
    ,16:233
    #total=306
    ,18:1249
    ,20:7595
    #total=9150
    ,22:49566
    ,24:339722
    #total=398438
    ,26:2406841
    #total=2805279
    }
$ echo $[398438+2406841]
2805279

# unicode total: 0x11_0000 == 1114112
    -adc3m3[26].txt
        247 MB (259,938,828 bytes)
        2406841 cubic graphs
    -adc3m3[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24].txt
        37.4 MB (39,285,084 bytes)
        398438 cubic graphs
#
#"""


__all__ = '''
    canon_label_tri_planar_embedding__min_dfs
    mk_edge_orbits_from_all_old2canon
    mk_vtx_orbits_from_edge_orbits
    mk_vtx_orbits_from_all_old2canon
    downgrade_tri_planar_embedding
        tri_remove_edge
    tri_planar_strs2iter_info_pairs

    read_infofile_write_to_newfile
    write_infofile

    write_infofile__tri_planar_strs
    continue_infofile_with
    continue_on_new_infofile_with
    '''.split()

from nn_ns.graph.graph_format_ascii_embedding import str2embedding as _tri_planar_str2embedding
from seed.helper.safe_eval import safe_eval
from seed.helper.stable_repr import stable_repr
from seed.tiny import fst, snd
from seed.tiny import fprint
from seed.debug.diff_str import assert_seq_eq
from functools import reduce, cmp_to_key
import operator as opss
from pathlib import Path
from itertools import islice
r"""
import networkx as nx
from seed.text.escape_as_c_string import escape_as_c_string__narrow
import re
import subprocess
#"""


#========[copy from draw_tri_planar_graphs.py
def nth_tri_planar_str2file_base_name(nth, tri_planar_str):
    return f'[{nth:0>7}]{tri_planar_str}'
def tri_planar_str2embedding(tri_planar_str):
    #print(f'{tri_planar_str!r}')
    tri_planar_str = tri_planar_str.strip()
    return _tri_planar_str2embedding(tri_planar_str)
#========]copy from draw_tri_planar_graphs.py


def tri_planar_str2ename(tri_planar_str):
    r'''->tri_planar_ename
    ename = embedding str as name
    vs:
        tri_planar_str2ename
        tri_planar_str2embedding
        nth_tri_planar_str2file_base_name
        ns_tri_planar_ename2xename
    #'''
    str_nv, str_mx = tri_planar_str.split()
    tri_planar_ename = str_mx.replace(',', '_')
    assert tri_planar_str == tri_planar_ename2str(tri_planar_ename)
    return tri_planar_ename
def tri_planar_ename2nv(tri_planar_ename):
    nv = 1 + tri_planar_ename.count('_')
    return nv
def tri_planar_ename2str(tri_planar_ename):
    str_mx = tri_planar_ename.replace('_', ',')
    nv = tri_planar_ename2nv(tri_planar_ename)
    tri_planar_str = f'{nv} {str_mx}'
    return tri_planar_str

def ns_tri_planar_ename2xename(nv, local_nth, global_nth, tri_planar_ename):
    r'''->tri_planar_xename
    xename = extened ename
    #'''
    assert nv == tri_planar_ename2nv(tri_planar_ename)
    assert 0 <= local_nth <= global_nth
    tri_planar_xename = f'{nv}_{local_nth}_{global_nth}_{tri_planar_ename}'
    assert (nv, local_nth, global_nth, tri_planar_ename) == tri_planar_xename2ns_ename(tri_planar_xename)
    return tri_planar_xename

def tri_planar_xename2ns_ename(tri_planar_xename):
    r'''->(nv, local_nth, global_nth, tri_planar_ename)
    #'''
    (nv, local_nth, global_nth, tri_planar_ename) = tri_planar_xename.split('_', 3)
    (nv, local_nth, global_nth) = map(int, (nv, local_nth, global_nth))
    return (nv, local_nth, global_nth, tri_planar_ename)




def flip_planar_embedding(planar_embedding):
    'planar_embedding -> planar_embedding'
    return tuple(vtc[::-1] for vtc in planar_embedding)
def dfs_tree2str(dfs_tree):
    'dfs_tree -> dfs_tree_str'
    def f(dfs_sub_tree):
        it = iter(dfs_sub_tree)
        dfs_sub_root = next(it)
        ls.append(f'({dfs_sub_root}')
        for x in it:
            if type(x) is int:
                #back_edge|rback_edge
                ancestor_or_descendant_vtx = x
                ls.append(f'[{ancestor_or_descendant_vtx}]')
            else:
                dfs_sub_tree = x
                f(dfs_sub_tree)
        ls.append(')')
    ls = []
    f(dfs_tree)
    dfs_tree_str = ''.join(ls)
    return dfs_tree_str

def dfs_tree_to_old2new(dfs_tree):
    'dfs_tree -> old2new'
    def add(v):
        if v not in old2new:
            old2new[v] = new = len(old2new)
    def f(dfs_sub_tree):
        it = iter(dfs_sub_tree)
        dfs_sub_root = next(it)
        add(dfs_sub_root)
        for x in it:
            if type(x) is int:
                #back_edge|rback_edge
                ancestor_or_descendant_vtx = x
                pass
            else:
                dfs_sub_tree = x
                f(dfs_sub_tree)
    old2new = {}
    f(dfs_tree)
    old2new = tuple(old2new[v] for v in range(len(old2new)))
    return old2new

def relabel_dfs_tree(old2new, dfs_tree):
    '->dfs_tree'
    def f(dfs_sub_tree):
        it = iter(dfs_sub_tree)
        dfs_sub_root = next(it)
        ls = [old2new[dfs_sub_root]]
        for x in it:
            if type(x) is int:
                #back_edge|rback_edge
                ancestor_or_descendant_vtx = x
                ls.append(old2new[ancestor_or_descendant_vtx])
            else:
                dfs_sub_tree = x
                ls.append(f(dfs_sub_tree))
        return tuple(ls)
    new_dfs_tree = f(dfs_tree)

    assert tuple(range(len(old2new))) == dfs_tree_to_old2new(new_dfs_tree)
    return new_dfs_tree

def sign(x):
    if x < 0: return -1
    if x > 0: return +1
    return 0

def cmp_dfs_tree(lhs, rhs):
    #rint(f'lhs={lhs}\nrhs={rhs}')
    def cmp_tree(lhs, rhs):
        r = len(lhs) - len(rhs)
        if r: return sign(r)
        r = lhs[0] - rhs[0]
        if r: return sign(r)
        for x,y in zip(lhs, rhs):
            r = cmp_vtx_or_tree(x,y)
            if r: return r
        return 0
    def cmp_vtx_or_tree(lhs, rhs):
        a = type(lhs) is not int
        b = type(rhs) is not int
        #vtx:0 < tree:1
        r = a - b
        if r: return sign(r)
        if a:
            #tree
            return cmp_tree(lhs, rhs)
        else:
            #vtx
            r = lhs - rhs
            if r: return sign(r)
    return cmp_tree(lhs, rhs)

def canon_label_tri_planar_embedding__min_dfs(tri_planar_embedding, list_all=False):
    r"""tri_planar_embedding -> (old2new, min_new_dfs_tree)
    tri_planar_embedding -> (all_old2new, min_new_dfs_tree)

    tri_planar_graph has only two planar_embedding
        ==>> canon by min_dfs
    #"""

    embeddings = [tri_planar_embedding, flip_planar_embedding(tri_planar_embedding)]
    dfs_trees = (dfs_tree
            for embedding in embeddings
            for dfs_tree in iter_dfs_trees__simple_connected_undirected_planar_embedding(embedding)
            )

    #bug:min_dfs_tree = min(dfs_trees)
    def key(dfs_tree):
        old2new = dfs_tree_to_old2new(dfs_tree)
        new_dfs_tree = relabel_dfs_tree(old2new, dfs_tree)
        return (new_dfs_tree, old2new)

    if not list_all:
        (min_new_dfs_tree, old2new) = min(map(key, dfs_trees), key=lambda pair: cmp_to_key(cmp_dfs_tree)(pair[0]))
        return (old2new, min_new_dfs_tree)
    else:
        it = map(key, dfs_trees)
        (min_new_dfs_tree, old2new) = next(it)
        all_old2new = [old2new]
        for (new_dfs_tree, old2new) in it:
            r = cmp_dfs_tree(min_new_dfs_tree, new_dfs_tree)
            if r == 0:
                #min_new_dfs_tree == new_dfs_tree
                all_old2new.append(old2new)
            elif r < 0:
                #min_new_dfs_tree < new_dfs_tree
                pass
            else:
                #new_dfs_tree <.min_new_dfs_tree:
                min_new_dfs_tree = new_dfs_tree
                all_old2new = [old2new]

        old2new = all_old2new[0]
        return (all_old2new, min_new_dfs_tree)

def iter_dfs_trees__simple_connected_undirected_planar_embedding(simple_connected_undirected_planar_embedding):
    r"""simple_connected_undirected_planar_embedding -> dfs_tree
    #"""
    embedding = simple_connected_undirected_planar_embedding
    def mk(u, v):
        return mk_dfs_tree__simple_connected_undirected_planar_embedding(embedding, set(), u, v)
    for u, neighbour_vtc in enumerate(embedding):
        for v in neighbour_vtc:
            yield mk(u, v)

def mk_dfs_tree__simple_connected_undirected_planar_embedding(simple_connected_undirected_planar_embedding, visited_set, pseudo_parent, dfs_sub_root):
    r"""-> dfs_sub_tree
    neighbour_vtc.index(pseudo_parent)
        not support multiedge ==>> simple
    #"""
    recur = mk_dfs_tree__simple_connected_undirected_planar_embedding
    assert type(pseudo_parent) is int
    assert type(visited_set) is set

    assert not visited_set or pseudo_parent in visited_set
    exclude_parent = is_real_parent = bool(visited_set)

    embedding = simple_connected_undirected_planar_embedding
    neighbour_vtc = embedding[dfs_sub_root]
    i = neighbour_vtc.index(pseudo_parent)
    j = i+exclude_parent
    vtc = neighbour_vtc[j:] + neighbour_vtc[:i]

    ls = [dfs_sub_root]
    new_parent = dfs_sub_root
    visited_set.add(new_parent)
    for v in vtc:
        if v in visited_set:
            #back_edge|rback_edge
            x = ancestor_or_descendant_vtx = v
        else:
            #new sub_tree
            new_root = v
            x = dfs_sub_tree = recur(embedding, visited_set, new_parent, new_root)
        ls.append(x)
    #bug:visited_set.remove(new_parent)
    dfs_sub_tree = tuple(ls)
    return dfs_sub_tree




def embedding2uv_edges(embedding):
    'embedding -> [(vtx,vtx)]'
    return tuple(embedding2iter_uv_edges(embedding))
def embedding2iter_uv_edges(embedding):
    'embedding -> Iter<(vtx,vtx)>'
    for u, neighbour_vtc in enumerate(embedding):
        for v in neighbour_vtc:
            yield u,v
def mk_edge_orbits_from_all_old2canon(old_uv_edges, all_old2canon):
    '[old_uv_edge] -> [{old_vtx:canon_vtx}] -> {{old_uv_edge}}'
    len(old_uv_edges)
    len(all_old2canon)
    ne = len(old_uv_edges)
    old2canon = next(iter(all_old2canon))
    def mk_new_edge(old2new, old_edge):
        u, v = old_edge
        new_edge = old2new[u], old2new[v]
        return new_edge
    new_edge2old_edges = {mk_new_edge(old2canon, old_edge): set() for old_edge in old_uv_edges}
    del old2canon

    for old2new in all_old2canon:
        for old_edge in old_uv_edges:
            new_edge = mk_new_edge(old2new, old_edge)
            new_edge2old_edges[new_edge].add(old_edge)
    edge_orbits = frozenset(map(frozenset, new_edge2old_edges.values()))

    assert ne == sum(map(len, edge_orbits))
    assert not ne or reduce(opss.__or__, edge_orbits) == frozenset(old_uv_edges)
    return edge_orbits

def mk_vtx_orbits_from_edge_orbits(nv, edge_orbits):
    vtx_orbits = set()
    for edge_orbit in edge_orbits:
        s0 = frozenset(map(fst, edge_orbit))
        s1 = frozenset(map(snd, edge_orbit))
        vtx_orbits.add(s0)
        vtx_orbits.add(s1)
    isolated_vtc = frozenset(range(nv)).difference(*vtx_orbits)
    if isolated_vtc:
        vtx_orbits.add(isolated_vtc)
    vtx_orbits = frozenset(vtx_orbits)
    check_vtx_orbits(nv, vtx_orbits)
    return vtx_orbits


def mk_vtx_orbits_from_all_old2canon(all_old2canon):
    '[{old_vtx:canon_vtx}] -> {{old_vtx}}'
    len(all_old2canon)
    old2canon = next(iter(all_old2canon))
    nv = len(old2canon)
    del old2canon

    new2olds = [set() for _ in range(nv)]
    for old2new in all_old2canon:
        for old, new in enumerate(old2new):
            new2olds[new].add(old)
    vtx_orbits = frozenset(map(frozenset, new2olds))

    check_vtx_orbits(nv, vtx_orbits)
    return vtx_orbits
def check_vtx_orbits(nv, vtx_orbits):
    assert nv == sum(map(len, vtx_orbits))
    assert not nv or reduce(opss.__or__, vtx_orbits) == frozenset(range(nv))



def tri_remove_edge(tri_embedding, uv_edge):
    r'''tri_embedding -> uv_edge -> (old2may_new, new_tri_embedding)
    '''
    assert all(3 == len(vtc) for vtc in tri_embedding)
    u, v = sorted(uv_edge)
    nv = len(tri_embedding)
    old2may_new = [*range(u)]
    old2may_new.append(None)
    old2may_new.extend(old-1 for old in range(u+1, v))
    old2may_new.append(None)
    old2may_new.extend(old-2 for old in range(v+1, nv))
    assert nv == len(old2may_new)


    tmp_embedding = [*map(list, tri_embedding)]
    def on_uv(u,v):
        assert v not in tmp_embedding[v] #no self-loop
        vtc = tmp_embedding[v]
        i = vtc.index(u)
        vtc.pop(i)
        x,y = vtc
        for a,b in [(x,y),(y,x)]:
            ls = tmp_embedding[a]
            j = ls.index(v)
            ls[j] = b
    on_uv(u,v)
    #串行，非 并行，-v=u-，=v-u=
    on_uv(v,u)


    new_embedding = []
    for old in range(nv):
        may_new = old2may_new[old]
        if may_new is None: continue
        new = may_new
        assert new == len(new_embedding)

        old_vtc = tmp_embedding[old]
        new_vtc = tuple(old2may_new[old] for old in old_vtc)
        assert None not in new_vtc
        new_embedding.append(new_vtc)
    new_tri_embedding = tuple(new_embedding)
    return old2may_new, new_tri_embedding



def downgrade_tri_planar_embedding(tri_planar_embedding, edge_orbits, low_level_canon2id):
    '-> {id:{edge_orbit}}'
    low_id2miss_curr_edge_orbits = {}
    stable_edge_orbits = set()
    Nothing = object()
    for edge_orbit in edge_orbits:
        uv_edge = next(iter(edge_orbit))
        (old2may_mid, mid_tri_embedding) = tri_remove_edge(tri_planar_embedding, uv_edge)
        (mid2new, min_new_dfs_tree) = canon_label_tri_planar_embedding__min_dfs(mid_tri_embedding)
        may_id = low_level_canon2id.get(min_new_dfs_tree, Nothing)
        if may_id is not Nothing:
            low_id = may_id
            s = low_id2miss_curr_edge_orbits.setdefault(low_id, set())
        else:
            s = stable_edge_orbits
        s.add(edge_orbit)
    return low_id2miss_curr_edge_orbits, stable_edge_orbits





def tri_planar_strs2iter_info_pairs(tri_planar_strs_from_nth, *, continue_state):
    if continue_state is None:
        start_nth = 0
        nv2canon2id = {}
    else:
        start_nth, nv2canon2id = continue_state

    assert start_nth == sum(map(len, nv2canon2id.values()))
    assert set(nv2canon2id) == set(range(4, 4+2*len(nv2canon2id), 2))

    if 0 and __debug__:
        #rint(f'start_nth={start_nth}; nv2canon2id={nv2canon2id}')
        tri_planar_strs_from_nth = [*tri_planar_strs_from_nth]
        #rint(f'tri_planar_strs_from_nth={tri_planar_strs_from_nth}')
    for nth, tri_planar_str in enumerate(tri_planar_strs_from_nth, start_nth):
        tri_planar_str = tri_planar_str.strip()
        tri_planar_embedding = tri_planar_str2embedding(tri_planar_str)
        (all_old2new, min_new_dfs_tree) = canon_label_tri_planar_embedding__min_dfs(tri_planar_embedding, list_all=True)

        nv = len(tri_planar_embedding)
        canon = min_new_dfs_tree
        id = nth_tri_planar_str2file_base_name(nth, tri_planar_str)
        if nv not in nv2canon2id:
            nv2canon2id[nv] = {}
        canon2id = nv2canon2id[nv]
        canon2id[canon] = id

        old_uv_edges = embedding2uv_edges(tri_planar_embedding)
        edge_orbits = mk_edge_orbits_from_all_old2canon(old_uv_edges, all_old2new)
        vtx_orbits = mk_vtx_orbits_from_all_old2canon(all_old2new)
        assert vtx_orbits == mk_vtx_orbits_from_edge_orbits(nv, edge_orbits)
        if nv == 4:
            low_level_canon2id = {}
        else:
            try:
                low_level_canon2id = nv2canon2id[nv-2]
            except KeyError:
                #rint(set(nv2canon2id))
                raise
        low_id2miss_curr_edge_orbits, stable_edge_orbits = downgrade_tri_planar_embedding(tri_planar_embedding, edge_orbits, low_level_canon2id)

        info = (nv, nth, tri_planar_embedding, id, canon, edge_orbits, vtx_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits)
        simplified_info = mk_simplified_info(id, low_id2miss_curr_edge_orbits, stable_edge_orbits)

        yield info, simplified_info

def mk_simplified_info(id, low_id2miss_curr_edge_orbits, stable_edge_orbits):
    def edge_orbits2mins(edge_orbits):
        return set(map(min, edge_orbits))
    low_id2miss_curr_edge_orbit_mins = {low_id:edge_orbits2mins(edge_orbits) for low_id, edge_orbits in low_id2miss_curr_edge_orbits.items()}
    stable_edge_orbit_mins = edge_orbits2mins(stable_edge_orbits)
    simplified_info = (id, low_id2miss_curr_edge_orbit_mins, stable_edge_orbit_mins)
    return simplified_info


infofile_headers = (
    #8
    ('info-ver1 = (nv, nth, tri_planar_embedding, id, canon, edge_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits)'
    #9
    #+vtx_orbits
    ,'info-ver2 = (nv, nth, tri_planar_embedding, id, canon, edge_orbits, vtx_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits)'
    #3
    ,'simplified_info = (id, low_id2miss_curr_edge_orbit_mins, stable_edge_orbit_mins)'
    ))
def write_infofile__tri_planar_strs(fout, headers, tri_planar_strs_from_0th):
    info_pairs = tri_planar_strs2iter_info_pairs(tri_planar_strs_from_0th, continue_state=None)
    write_infofile(fout, headers, info_pairs)
def write_infofile(fout, headers, info_pairs):
    write_headers__infofile(fout, headers)
    write_info_pairs__infofile(fout, info_pairs)
def write_headers__infofile(fout, headers):
    for header in headers:
        fprint('##', header, file=fout)
def write_info_pairs__infofile(fout, info_pairs):
    for info, simplified_info in info_pairs:
        write_info_pair__infofile(fout, info, simplified_info)
def write_info_pair__infofile(fout, info, simplified_info):
    write_info__infofile(fout, info)
    write_simplified_info__infofile(fout, simplified_info)

if stable_repr:
    def write_info__infofile(fout, info):
        fprint(stable_repr(info), file=fout)
    def write_simplified_info__infofile(fout, simplified_info):
        fprint('#', stable_repr(simplified_info), file=fout)


def continue_on_new_infofile_with(fout, headers, fcontinue, tri_planar_strs_from_0th):
    (overwrite_pos, todo_list, start_nth, nv2canon2id, info_pairs) = read_infofile(fcontinue, with_info_pairs=True)
    continue_state = start_nth, nv2canon2id
    #rint(f'continue_state={continue_state}')

    write_infofile(fout, headers, info_pairs)
    _continue_infofile_with(fout, tri_planar_strs_from_0th, continue_state)
def continue_infofile_with(tri_planar_strs_from_0th, fio):
    (overwrite_pos, continue_state, _) = continue_infofile(fio, with_info_pairs=False)
    assert overwrite_pos == fio.tell()
    #rint(f'continue_state={continue_state}')
    _continue_infofile_with(fio, tri_planar_strs_from_0th, continue_state)

def _continue_infofile_with(fout, tri_planar_strs_from_0th, continue_state):
    start_nth, nv2canon2id = continue_state
    it = iter(tri_planar_strs_from_0th)
    #bug:limit should be before: for _ in zip(it, range(start_nth)):pass
    #for _ in zip(range(start_nth), it):pass
    it = islice(it, start_nth, None)
    tri_planar_strs_from_nth = it

    info_pairs = tri_planar_strs2iter_info_pairs(tri_planar_strs_from_nth, continue_state=continue_state)
    write_info_pairs__infofile(fout, info_pairs)
def continue_infofile(fio, *, with_info_pairs):
    '-> (overwrite_pos, continue_state, may_info_pairs)'
    (overwrite_pos, todo_list, start_nth, nv2canon2id, may_info_pairs) = read_infofile(fio, with_info_pairs=with_info_pairs)
    continue_state = start_nth, nv2canon2id
    #rint(f'continue_state={continue_state}')
    write_todo_list__infofile(fio, overwrite_pos, todo_list)
    overwrite_pos = fio.tell()
    return overwrite_pos, continue_state, may_info_pairs

def read_infofile(fin, *, with_info_pairs):
    '->(overwrite_pos, todo_list, start_nth, nv2canon2id, may_info_pairs)'
    nv2canon2id = {}
    if with_info_pairs:
        may_info_pairs = info_pairs = []
    else:
        may_info_pairs = None
    nth = -1
    it = iter_read_infofile__basic(fin)
    for case, data in it:
        #rint(f'nth={nth}')
        if case == 'info':
            (info_ver1, info_ver2, simplified_info) = data
            (nv, nth, tri_planar_embedding, id, canon, edge_orbits, vtx_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits) = info_ver2
            if nv not in nv2canon2id:
                nv2canon2id[nv] = {}
            canon2id = nv2canon2id[nv]
            canon2id[canon] = id

            if with_info_pairs:
                info_pairs.append((info_ver2, simplified_info))
        elif case == 'simplified_info':
            pass
        else:
            assert case == 'overwrite_pos'
            overwrite_pos = data
            break
    assert case == 'overwrite_pos'
    overwrite_pos
    nv2canon2id
    start_nth = nth + 1
    #rint(f'start_nth={start_nth}')
    #rint(f'nv2canon2id={nv2canon2id}')
    assert start_nth == sum(map(len, nv2canon2id.values()))
    assert set(nv2canon2id) == set(range(4, 4+2*len(nv2canon2id), 2))

    # n?s?
    todo_list = [*it]
    assert len(todo_list) < 3
    if len(todo_list) == 1:
        assert todo_list[0][0] in ('newline', 'simplified_info')
    elif len(todo_list) == 2:
        assert todo_list[0][0] == 'newline'
        assert todo_list[1][0] == 'simplified_info'

    continue_state = start_nth, nv2canon2id
    return (overwrite_pos, todo_list, start_nth, nv2canon2id, may_info_pairs)
def write_todo_list__infofile(fout, overwrite_pos, todo_list):
    fout.seek(overwrite_pos)
    for case, data in todo_list:
        if case == 'newline':
            fprint(file=fout)
        else:
            assert case == 'simplified_info'
            simplified_info = data
            write_simplified_info__infofile(fout, simplified_info)


def read_infofile_write_to_newfile(fout, headers, fin):
    #fin is not fout
    it = iter_read_infofile_as_info_pairs(fin)
    write_infofile(fout, headers, it)

def iter_read_infofile_as_info_pairs(fin):
    '-> Iter<(info, simplified_info)>'
    info = None
    for case, data in iter_read_infofile__basic(fin):
        if case == 'info':
            assert info is None
            (info_ver1, info_ver2, simplified_info) = data
            info = info_ver2
            assert info is not None
        elif case == 'simplified_info':
            simplified_info = data
            yield info, simplified_info
            info = None
    assert info is None

def iter_fin(fin):
    #for line in fin: fin.tell()
    #OSError: telling position disabled by next() call
    #but StringIO is ok
    while 1:
        s = fin.readline()
        if not s:
            break
        yield s
def iter_read_infofile__basic(fin):
    r'''-> super_regex"(is)*(ion?s|on?)"
        i = ('info', (info_ver1, info_ver2, simplified_info))
        s = ('simplified_info', simplified_info)
        o = ('overwrite_pos', overwrite_pos)
        n = ('newline', None)

    #'''
    #skip headers
    column0 = True
    pos = fin.tell()
    it = iter_fin(fin)
    for line in it:
        if line.startswith('('):
            break
        pos = fin.tell()
        #OSError: telling position disabled by next() call
        #but StringIO is ok
    fin.seek(pos)

    #read info+simplified_info
    READ_INFO = 0
    READ_SIMPLIFIED_INFO = 1
    case = READ_INFO
    pos = fin.tell()
    for line in it:
        if case == -1:
            raise Exception('file-format-error')
        #line = line.strip()
        #if not line: continue
        if line.startswith('(') or line.startswith('# ('):
            pass
        else:
            pos = fin.tell()
            continue

        if case == READ_INFO:
            case = READ_SIMPLIFIED_INFO
            if not line.startswith('('):
                raise logic-error
            try:
                info = safe_eval(line)
            except SyntaxError:
                broken_info = line
                case = -1
                overwrite_pos = pos
                overwrite_case = READ_INFO
                continue #without pos = fin.tell()
            L = len(info)
            if L == 8:
                #ver1
                #calc vtx_orbits
                info_ver1 = info; del info
                (nv, nth, tri_planar_embedding, id, canon, edge_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits) = info_ver1
                vtx_orbits = mk_vtx_orbits_from_edge_orbits(nv, edge_orbits)
                info_ver2 = (nv, nth, tri_planar_embedding, id, canon, edge_orbits, vtx_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits)
            else:
                #ver2
                assert L == 9
                info_ver2 = info; del info
                (nv, nth, tri_planar_embedding, id, canon, edge_orbits, vtx_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits) = info_ver2
                info_ver1 = (nv, nth, tri_planar_embedding, id, canon, edge_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits)
            simplified_info = mk_simplified_info(id, low_id2miss_curr_edge_orbits, stable_edge_orbits)
            info_ver1
            info_ver2
            simplified_info
            yield 'info', (info_ver1, info_ver2, simplified_info)
        else:
            assert case == READ_SIMPLIFIED_INFO
            case = READ_INFO
            if not line.startswith('# ('):
                raise logic-error
            try:
                _simplified_info = safe_eval(line[2:])
            except SyntaxError:
                broken_simplified_info = line
                case = -1
                overwrite_pos = pos
                overwrite_case = READ_SIMPLIFIED_INFO
                continue #without pos = fin.tell()
            assert 3 == len(simplified_info)
            (id, low_id2miss_curr_edge_orbit_mins, stable_edge_orbit_mins) = _simplified_info
            assert simplified_info == _simplified_info
            yield 'simplified_info', simplified_info
        pos = fin.tell()

    last_line = line
    if case != -1:
        #last line not broken
        assert pos == fin.tell()
        overwrite_pos = pos
    yield 'overwrite_pos', overwrite_pos

    if case == -1:
        #last line broken
        if overwrite_case == READ_INFO:
            broken_info
            pass
        else:
            assert overwrite_case == READ_SIMPLIFIED_INFO
            broken_simplified_info
            #overwrite: simplified_info
            yield 'simplified_info', simplified_info
    else:
        #last line not broken
        if last_line.endswith('\n'):
            #last line complete
            pass
        else:
            #last line miss newline
            yield 'newline', None
        if case == READ_SIMPLIFIED_INFO:
            yield 'simplified_info', simplified_info
        else:
            pass











def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    Nothing = object()
    parser = argparse.ArgumentParser(
        description='generate downgrade info for tri_planar_graph seq'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-c', '--continue_output', type=str, default=Nothing, nargs='?'
                        , help='prev output file; if given "." or not given then read curr output file as prev output file')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = 'ascii'
    omode = 'wt' if args.force else 'xt'
    continue_output = args.continue_output
    if 0:
        #rint(f'continue_output={continue_output!r}')
        r"""
$ py script/info_tri_planar_graphs.py -c 4
continue_output='4'
$ py script/info_tri_planar_graphs.py -c
continue_output=None
$ py script/info_tri_planar_graphs.py
continue_output=<object object at 0xb69767f8>
        #"""
        return

    continue_infofile_with
    #read_infofile_write_to_newfile
    read_infofile_continue_on_new_infofile = continue_on_new_infofile_with
    mk_new_infofile = write_infofile__tri_planar_strs

    may_ifname = args.input
    may_ofname = args.output
    if may_ofname is None:
        may_opath = None
    else:
        ofname = may_ofname
        may_opath = opath = Path(ofname)

    if continue_output is Nothing:
        case = mk_new_infofile
    elif continue_output is None or continue_output == '.':
        # try continue_infofile_with else mk_new_infofile
        if may_opath is not None and opath.exists():
            case = continue_infofile_with
        else:
            case = mk_new_infofile
    else:
        cpath = Path(continue_output)
        if not cpath.exists():
            raise FileNotFoundError(cpath)
        if may_opath is not None:
            #bug:if opath.samefile(cpath):
            #   existing_path.samefile(another_existing_path)
            if opath.exists() and cpath.samefile(opath):
                case = continue_infofile_with
            else:
                case = read_infofile_continue_on_new_infofile
        else:
            case = read_infofile_continue_on_new_infofile
    case


    if case is mk_new_infofile:
        assert continue_output is Nothing or ((may_opath is None or not opath.exists()) and (continue_output is None or continue_output == '.'))
    elif case is continue_infofile_with:
        assert continue_output is not Nothing
        assert not (may_opath is None or not opath.exists())
        opath
        assert (continue_output is None or continue_output == '.') or (cpath.exists() and opath.exists() and cpath.samefile(opath))
    else:
        assert case is read_infofile_continue_on_new_infofile
        assert continue_output is not Nothing
        assert not (continue_output is None or continue_output == '.')
        cpath
        assert cpath.exists()
        assert (may_opath is None or not opath.exists()) or not opath.exists() or not cpath.samefile(opath)


    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        tri_planar_strs_from_0th = iter(fin)
        if case is mk_new_infofile:
            with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
                write_infofile__tri_planar_strs(fout, infofile_headers, tri_planar_strs_from_0th)
        elif case is continue_infofile_with:
            with open(opath, 'r+t', encoding=encoding) as fio:
                continue_infofile_with(tri_planar_strs_from_0th, fio)
        elif case is read_infofile_continue_on_new_infofile:
            with may_open_stdout(may_ofname, omode, encoding=encoding) as fout, open(cpath, 'rt', encoding=encoding) as fcontinue:
                continue_on_new_infofile_with(fout, infofile_headers, fcontinue, tri_planar_strs_from_0th)
        else:
            raise logic-error





def _t():
    from io import StringIO
    input_txt = r'''4 bcd,adc,abd,acb
6 bcd,aef,afd,ace,bdf,bec
8 bcd,aef,afg,agh,bhf,bec,chd,dge
8 bcd,aef,afg,age,bdh,bhc,chd,egf
'''

    ok_ver1 = r'''info = (nv, nth, tri_planar_embedding, id, canon, edge_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits)
simplified_info = (id, low_id2miss_curr_edge_orbit_mins, stable_edge_orbit_mins)
(4, 0, ((1, 2, 3), (0, 3, 2), (0, 1, 3), (0, 2, 1)), '[0000000]4 bcd,adc,abd,acb', (0, (1, (2, 0, (3, 0, 1)), 3), 3, 2), frozenset({frozenset({(3, 2), (3, 1), (1, 0), (2, 3), (0, 3), (0, 2), (1, 3), (2, 0), (1, 2), (3, 0), (2, 1), (0, 1)})}), {}, {frozenset({(3, 2), (3, 1), (1, 0), (2, 3), (0, 3), (0, 2), (1, 3), (2, 0), (1, 2), (3, 0), (2, 1), (0, 1)})})
# ('[0000000]4 bcd,adc,abd,acb', {}, {(0, 1)})
(6, 1, ((1, 2, 3), (0, 4, 5), (0, 5, 3), (0, 2, 4), (1, 3, 5), (1, 4, 2)), '[0000001]6 bcd,aef,afd,ace,bdf,bec', (0, (1, (2, 0, (3, (4, 0, (5, 1, 3)), 5)), 5), 4, 2), frozenset({frozenset({(5, 1), (3, 2), (4, 1), (2, 3), (0, 3), (5, 4), (0, 2), (2, 0), (4, 5), (3, 0), (1, 5), (1, 4)}), frozenset({(5, 2), (4, 3), (1, 0), (2, 5), (3, 4), (0, 1)})}), {'[0000000]4 bcd,adc,abd,acb': {frozenset({(5, 1), (3, 2), (4, 1), (2, 3), (0, 3), (5, 4), (0, 2), (2, 0), (4, 5), (3, 0), (1, 5), (1, 4)})}}, {frozenset({(5, 2), (4, 3), (1, 0), (2, 5), (3, 4), (0, 1)})})
# ('[0000001]6 bcd,aef,afd,ace,bdf,bec', {'[0000000]4 bcd,adc,abd,acb': {(0, 2)}}, {(0, 1)})
'''

    ok_ver2 = r'''## info-ver1 = (nv, nth, tri_planar_embedding, id, canon, edge_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits)
## info-ver2 = (nv, nth, tri_planar_embedding, id, canon, edge_orbits, vtx_orbits, low_id2miss_curr_edge_orbits, stable_edge_orbits)
## simplified_info = (id, low_id2miss_curr_edge_orbit_mins, stable_edge_orbit_mins)
(4, 0, ((1, 2, 3), (0, 3, 2), (0, 1, 3), (0, 2, 1)), '[0000000]4 bcd,adc,abd,acb', (0, (1, (2, 0, (3, 0, 1)), 3), 3, 2), frozenset({frozenset({(0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (1, 3), (2, 0), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2)})}), frozenset({frozenset({0, 1, 2, 3})}), {}, {frozenset({(0, 1), (0, 2), (0, 3), (1, 0), (1, 2), (1, 3), (2, 0), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2)})})
# ('[0000000]4 bcd,adc,abd,acb', {}, {(0, 1)})
(6, 1, ((1, 2, 3), (0, 4, 5), (0, 5, 3), (0, 2, 4), (1, 3, 5), (1, 4, 2)), '[0000001]6 bcd,aef,afd,ace,bdf,bec', (0, (1, (2, 0, (3, (4, 0, (5, 1, 3)), 5)), 5), 4, 2), frozenset({frozenset({(0, 1), (1, 0), (2, 5), (3, 4), (4, 3), (5, 2)}), frozenset({(0, 2), (0, 3), (1, 4), (1, 5), (2, 0), (2, 3), (3, 0), (3, 2), (4, 1), (4, 5), (5, 1), (5, 4)})}), frozenset({frozenset({0, 1, 2, 3, 4, 5})}), {'[0000000]4 bcd,adc,abd,acb': {frozenset({(0, 2), (0, 3), (1, 4), (1, 5), (2, 0), (2, 3), (3, 0), (3, 2), (4, 1), (4, 5), (5, 1), (5, 4)})}}, {frozenset({(0, 1), (1, 0), (2, 5), (3, 4), (4, 3), (5, 2)})})
# ('[0000001]6 bcd,aef,afd,ace,bdf,bec', {'[0000000]4 bcd,adc,abd,acb': {(0, 2)}}, {(0, 1)})
'''


    newline = '\n'
    fcontinue_txtss = []
    for ok in [ok_ver1, ok_ver2]:
        assert ok.endswith(newline)
        miss_newline = ok[:-1]
        broken_simplified_info = miss_newline[:-8]
        i = broken_simplified_info.rindex(newline)
        miss_simplified_info = broken_simplified_info[:i+1]
        assert miss_simplified_info.endswith(newline)
        miss_newline_simplified_info = miss_simplified_info[:-1]
        broken_info = miss_newline_simplified_info[:-8]


        fcontinue_txts = [ok
            , miss_newline
            , broken_simplified_info
            , miss_simplified_info
            , miss_newline_simplified_info
            , broken_info
            ]
        fcontinue_txtss.append(fcontinue_txts)


    r'''
    mk_new_infofile
        write_infofile__tri_planar_strs(fout, infofile_headers, tri_planar_strs_from_0th)
    continue_infofile_with
        continue_infofile_with(tri_planar_strs_from_0th, fio)
    read_infofile_continue_on_new_infofile
        continue_on_new_infofile_with(fout, infofile_headers, fcontinue, tri_planar_strs_from_0th)
    #'''
    fin = StringIO(input_txt)
    fin_pos0 = fin.tell()

    for ver, fcontinue_txts in enumerate(fcontinue_txtss, 1):
      if 1:
        fin.seek(fin_pos0)
        tri_planar_strs_from_0th = iter(fin)
        fout = StringIO()
        write_infofile__tri_planar_strs(fout, infofile_headers, tri_planar_strs_from_0th)
        output_txt = fout.getvalue()
        assert input_txt == fin.getvalue()
        assert output_txt == fout.getvalue()
        #rint(output_txt); return

      for fcontinue_txt in fcontinue_txts:
        if 1:
            fin.seek(fin_pos0)
            tri_planar_strs_from_0th = iter(fin)
            fcontinue = StringIO(fcontinue_txt)
            fout = StringIO()
            continue_on_new_infofile_with(fout, infofile_headers, fcontinue, tri_planar_strs_from_0th)
            assert input_txt == fin.getvalue()
            assert_seq_eq(output_txt, fout.getvalue())

        if ver == 2:
            # ver diff ==>> header & init section diff
            #should use stable_repr, too
            fin.seek(fin_pos0)
            tri_planar_strs_from_0th = iter(fin)
            fio = fout = fcontinue = StringIO(fcontinue_txt)
            continue_infofile_with(tri_planar_strs_from_0th, fio)
            assert input_txt == fin.getvalue()
            assert_seq_eq(output_txt, fout.getvalue())



if __name__ == "__main__":
    #_t()
    main()

