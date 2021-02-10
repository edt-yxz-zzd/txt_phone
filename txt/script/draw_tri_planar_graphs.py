
r"""


=========ver2
=====
py script/draw_tri_planar_graphs.py -f --exe networkx-planar_layout -m '/sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3/-adc3m3[4, 6, 8].txt' -od '/sdcard/0my_files/tmp/dot/many/'


view /sdcard/0my_files/tmp/dot/many/[0000000]4 bcd,adc,abd,acb.dot
view ../../python3_src/nn_ns/graph/adc3m3_from4to18d.txt
    [4,6..16]
for i in {4..16..2} ; do ./plantri -adc3m3 ${i}d ; done > ~/tmp/-adc3m3[4d-16d].txt
view ~/tmp/-adc3m3[4d-16d].txt
diff ~/tmp/-adc3m3[4d-16d].txt /sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3_from4to18d.txt

mkdir /sdcard/0my_files/tmp/dot/plantri-adc3m3-[4-16]d--dot-svg-png/
py script/draw_tri_planar_graphs.py -f --exe networkx-planar_layout -m '/sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3_from4to18d.txt' -od '/sdcard/0my_files/tmp/dot/plantri-adc3m3-[4-16]d--dot-svg-png/'

cd /sdcard/0my_files/tmp/dot/
du -h ./plantri-adc3m3-[4-16]d--dot-svg-png/
    32 MB
    #.zip ==>> 22.4 MB
7z a  ./plantri-adc3m3-[4-16]d--dot-svg-png.7z  ./plantri-adc3m3-[4-16]d--dot-svg-png/
    #.7z ==>> 18 MB
mkdir ./plantri-adc3m3-[4-16]d--dot-svg/
cp -t ./plantri-adc3m3-[4-16]d--dot-svg/   ./plantri-adc3m3-\[4-16\]d--dot-svg-png/*.dot
cp -t ./plantri-adc3m3-[4-16]d--dot-svg/   ./plantri-adc3m3-\[4-16\]d--dot-svg-png/*.svg
du -h ./plantri-adc3m3-[4-16]d--dot-svg/
    4.8 MB
7z a  ./plantri-adc3m3-[4-16]d--dot-svg.7z  ./plantri-adc3m3-[4-16]d--dot-svg/
    #.7z ==>> 368 KB without png




=====
graphviz donot support drawing of planar graph
    ==>> turn to networkx.drawing.layout.planar_layout

import networkx as nx
pos = nx.planar_layout(G)
nx.draw_planar(G)


https://graphviz.org/doc/info/lang.html
https://stackoverflow.com/questions/49040633/converting-network-graph-to-graphviz
https://stackoverflow.com/questions/5343899/how-to-force-node-position-x-and-y-in-graphviz

py.networkx:
    import networkx as nx
    G.add_node(v,x=100,y=100)
    for v in G:
        G.node[v]['pos'] = "{},{}!".format(G.node[v]['x'], G.node[n]['y'])
    nx.drawing.write_dot(G, "test.dot")
    ===
    import pydot
    p = nx.nx_pydot.to_pydot(G)
graphviz.dot:
    #should call neato with pos
    #neato xxx.dot -n2 -Tpng -o xxx.png
    v [pos=100,50!];
        #设置 点v 的 位置
        #point 的 格式：f"{},{}!"
    u [pos="100,50"];
        #???
    w [pos="100,50!"];
        #???
    v -> u  [pos="e,27,324.1 27,359.7 27,351.98 27,342.71 27,334.11"];

man dot
    -n[1|2] (no-op)
        If set, neato assumes nodes have already been positioned and all nodes have a pos attribute giving the positions.
        It then performs an optional adjustment to remove node-node overlap
          , depending on the value of the overlap attribute
          , computes the edge layouts
          , depending on the value of the splines attribute
          , and emits the graph in the appropriate format.
        If num is supplied, the following actions occur:
           num = 1
               Equivalent to -n.
               # -n1 === -n
           num > 1
               # -n2 不调整 点的位置 哪怕重叠
               Use node positions as specified, with no adjustment to remove node-node overlaps
                 , and use any edge layouts already specified by the pos attribute.
               neato computes an edge layout for any edge that does not have a pos attribute.
               As usual, edge layout is guided by the splines attribute.





=========ver1
=====
py script/draw_tri_planar_graphs.py -f --exe twopi -m '/sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3/-adc3m3[4, 6, 8].txt' -od '/sdcard/0my_files/tmp/dot/many/'
=====
e script/draw_tri_planar_graphs.py
graphviz.dot + tri-plane
  nauty::plantri
man dot
  dot -> neato twopi circo fdp sfdp
/*
dot ab.dot -Tsvg -o ab.svg -Tpng -o ab.png
*/
graph ab {
    label="ab";
    a; b;
    a -- b;
}



plantri45.exe -adc3m3 4d > -adc3m3[4].txt
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
    ,18:1249
    ,20:7595
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
#"""





__all__ = '''
    output_dot_png_svg__many__ipath
    output_dot_png_svg__many
    output_dot_png_svg__1
    '''.split()

import networkx as nx
from nn_ns.graph.graph_format_ascii_embedding import str2embedding as _tri_planar_str2embedding
from seed.tiny import fprint
from pathlib import Path
import re
import subprocess



SCALE = 50
dot_exes_str = 'dot neato twopi circo fdp sfdp'
dot_exes = dot_exes_str.split()

def tri_planar_str2embedding(tri_planar_str):
    #print(f'{tri_planar_str!r}')
    tri_planar_str = tri_planar_str.strip()
    return _tri_planar_str2embedding(tri_planar_str)

def _t0():
    s = '4 bcd,adc,abd,acb'
    em = tri_planar_str2embedding(s)
    #print(em)
    assert em == ((1, 2, 3), (0, 3, 2), (0, 1, 3), (0, 2, 1))

def _t1(*, exe, force=False):
    ifname = '/sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3/-adc3m3[4, 6, 8].txt'
    output_dir = '/sdcard/0my_files/tmp/dot/many/'
    output_dot_png_svg__many__ipath(ifname, output_dir=output_dir, exe=exe, force=force)


def vtx_num2name(n):
    assert type(n) is int
    assert 0 <= n < 26
    c = chr(ord('A') + n)
    return f'{c}{n:0>2}'


def c_quote(s):
    #if not max(s, default='0') < '\u0100': raise NotImplementedError
    if not re.fullmatch(r'[\[\]0-9 a-z,]*', s): NotImplementedError
    return s

def output_dot_png_svg__many__ipath(ipath, *, output_dir, exe, force):
    output_dir = Path(output_dir)
    with open(ipath, 'rt', encoding='ascii') as fin:
        output_dot_png_svg__many(iter(fin), output_dir=output_dir, exe=exe, force=force)
def output_dot_png_svg__many(tri_planar_strs, *, output_dir, exe, force):
    output_dir = Path(output_dir)
    for nth, tri_planar_str in enumerate(tri_planar_strs):
        output_dot_png_svg__1(nth, tri_planar_str, output_dir=output_dir, exe=exe, force=force)

def output_dot_png_svg__1(nth, tri_planar_str, *, output_dir, exe, force):
    output_dir = Path(output_dir)
    tri_planar_str = tri_planar_str.strip()

    if exe in ['networkx-planar_layout', 'nn_ns-straight_line']:
        #pos are set
        layout = exe
    else:
        assert exe in dot_exes
        layout = 'dot_layout'

    title = output_graphviz_dot_file(nth, tri_planar_str, output_dir=output_dir, force=force, layout=layout)
    prefix = output_dir / title
    common_args = [f'{prefix!s}.dot', '-Tsvg', '-o', f'{prefix!s}.svg', '-Tpng', '-o', f'{prefix!s}.png']
    if layout == 'dot_layout':
        cmd = [exe, *common_args]
    else:
        cmd = ['neato', '-n2', *common_args]
    subprocess.run(cmd, check=True)

def output_graphviz_dot_file(nth, tri_planar_str, *, output_dir, force, layout):
    output_dir = Path(output_dir)
    title = nth_tri_planar_str2file_base_name(nth, tri_planar_str)
    ofname = output_dir / f'{title}.dot'
    tri_planar_embedding = tri_planar_str2embedding(tri_planar_str)
    omode = 'wt' if force else 'xt'
    with open(ofname, omode, encoding='ascii') as fout:
        print_graphviz_dot_file(tri_planar_embedding, file=fout, title=title, layout=layout)
    return title

def embedding2networkx_graph(embedding):
    nv = len(embedding)
    g = nx.Graph()
    for v, neighbour_vtc in enumerate(embedding):
        for u in neighbour_vtc:
            g.add_edge(v, u)
    assert len(g) == g.order() == g.number_of_nodes() == nv
    return g
def planar_embedding2networkx_planar_layout(planar_embedding, *, scale):
    g = embedding2networkx_graph(planar_embedding)
    pos = nx.planar_layout(g) #{vtx:(x,y)}
    assert type(pos) is dict

    if not scale:
        scale = 1
    if 1:
        d = {}
        for u, (x,y) in pos.items():
            x *= scale
            y *= scale
            d[u] = x,y
    scaled_pos = d
    return scaled_pos

def nth_tri_planar_str2file_base_name(nth, tri_planar_str):
    return f'[{nth:0>7}]{tri_planar_str}'
def print_graphviz_dot_file(tri_planar_embedding, *, file, title, layout):
    assert layout in 'dot_layout networkx-planar_layout nn_ns-straight_line'.split()

    nv = len(tri_planar_embedding)
    if layout == 'nn_ns-straight_line':
        raise NotImplementedError(f'case: layout={layout}')
    elif layout == 'networkx-planar_layout':
        scaled_pos = planar_embedding2networkx_planar_layout(tri_planar_embedding, scale = SCALE*nv)
    else:
        assert layout == 'dot_layout'
        scaled_pos = None
    if scaled_pos is None:
        ls_scaled_pos = None
    else:
        #ls_scaled_pos = [None]*nv
        ls_scaled_pos = ', '.join("{u}: ({x},{y})".format(u=u,x=x,y=y) for u, (x,y) in sorted(scaled_pos.items()))
        ls_scaled_pos = f"{{{ls_scaled_pos}}}"

    indent = '  '

    # {title}=[{nth}]{tri_planar_str}
    # {tri_planar_embedding}
    # {ls_scaled_pos}
    if ls_scaled_pos:
        header = f"""/*
title={title!r}
embedding={tri_planar_embedding!r}
layout={ls_scaled_pos!s}
$ neato -n2 ...
*/"""
    else:
        header = f"""/*
title={title!r}
embedding={tri_planar_embedding!r}
*/"""
    fprint(header, file=file)
    fprint('graph {', file=file)

    if title:
        fprint(f'{indent}label = "{c_quote(title)!s}";', file=file)
    ###
    fprint(f'{indent}overlap = false;', file=file)
    r'''
    overlap = false;
        #no-affects
        http://graphviz.org/doc/info/attrs.html
        overlap
            Determines if and how node overlaps should be removed.
            ###not about edge!!! WTF
    #'''

    if nv:
        vtc_decl = '; '.join(map(vtx_num2name, range(nv)))
        fprint(f'{indent}{vtc_decl};', file=file)

    if scaled_pos:
        for u, (x,y) in scaled_pos.items():
            u_name = vtx_num2name(u)
            fprint(f'{indent}{u_name} [ pos = "{x},{y}!" ];', file=file)


    if 1:
        for u, neighbour_vtc in enumerate(tri_planar_embedding):
            #避免 边 出现两次
            neighbour_vtc = [v for v in neighbour_vtc if v > u]
            if neighbour_vtc:
                neighbour_vtc_str = ', '.join(map(vtx_num2name, neighbour_vtc))
                u_name = vtx_num2name(u)
                fprint(f'{indent}{u_name} -- {{{neighbour_vtc_str!s}}};', file=file)

    fprint('}', file=file)


def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='generate image for given tri_planar_graph'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-s', '--single', type=str, default=None
                        , help='input single "{tri_planar_str}@{nth}". eg. "4 bcd,adc,abd,acb@0"')
    parser.add_argument('-m', '--inputfile_for_many', type=str, default=None
                        , help='input file of which each line is tri_planar_str and lineno is nth.')

    parser.add_argument('-od', '--output_dir', type=str, default='.'
                        , help='output directory')
    parser.add_argument('--exe', type=str, default='twopi', required=True
                        , help=f'executable like "dot", "twopi"(=default). see "man dot"; special [networkx-planar_layout nn_ns-straight_line], dot [{dot_exes_str}]')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    if args.inputfile_for_many:
        output_dot_png_svg__many__ipath(args.inputfile_for_many, output_dir=args.output_dir, exe=args.exe, force=args.force)
    if args.single:
        tri_planar_str, nth = args.single.split('@')
        nth = int(nth)
        assert nth >= 0
        output_dot_png_svg__1(nth, tri_planar_str, output_dir=args.output_dir, exe=args.exe, force=args.force)
if __name__ == "__main__":
    main()



if __name__ == '__main__':
    _t0()
    #_t1(exe='circo')#相交
    #_t1(exe='neato')#相交
    #_t1(exe='twopi')#相交#较佳
    #_t1(exe='fdp')#相交
    #_t1(exe='sfdp')#fail to run!
    #_t1(exe='dot')#相交









