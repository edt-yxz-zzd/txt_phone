#__all__:goto
r'''[[[
e script/clean_w3schools_pages.py
view script/clean_w3schools_html_TAGs.py
view ../lots/NOTE/html/术语.txt
    markup_element
    start_tag
    end_tag
    startend_tag
view ../lots/NOTE/html/httpd-confs/httpd.conf-sdcard_0my_files-unzip-py_doc-python_3_12_4_docs_html

script.clean_w3schools_pages
py -m nn_ns.app.debug_cmd   script.clean_w3schools_pages -x # -off_defs
py -m nn_ns.app.doctest_cmd script.clean_w3schools_pages:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %script.clean_w3schools_pages:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'script.clean_w3schools_pages:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
已下载 待整理:
  html-graphics html(含:svg html)
  bash html
  SQL html
      ls /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/
      view /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/index.html
      view /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/index.html
      view /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/index.html
      view /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/svg_intro.asp
        必须清除垃圾信息
          view ../lots/NOTE/html/tag/\[20240613]clean_w3schools_html_TAGs.py
      view script/clean_w3schools_html_TAGs.py
    view /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/tag_a.asp

<!DOCTYPE html>
<html lang="en-US">
<head>
<title>HTML a tag</title>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="../browserref.css">
</head>
<body>
    ... 内容
</body>
</html>


    view /sdcard/0my_files/tmp/wget_/www.w3schools.com/browserref.css
      view /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/svg_rect.asp
        内容区:8893行..9106行:搜索h1『\<Previous\>』or『class="w3-clear nextprev"』
          #主页 选择性保留 导航栏

<h1>SVG <span class="color_h1">&lt;rect&gt;</span></h1>
<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="svg_inhtml.asp">&#10094; Previous</a>
<a class="w3-right w3-btn" href="svg_circle.asp">Next &#10095;</a>
</div>
    ... ...
<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="svg_inhtml.asp">&#10094; Previous</a>
<a class="w3-right w3-btn" href="svg_circle.asp">Next &#10095;</a>
</div>
以上是body应该保留的内容
head含css:
<link rel="stylesheet" href="../plus/plans/main.css">
<style>
#nav_tutorials,#nav_references,#nav_certified,#nav_services,#nav_exercises {display:none;letter-spacing:0;position:absolute;width:100%;background-color:#282A35;color:white;padding-bottom:40px;z-index: 5 !important;font-family: 'Source Sans Pro Topnav', sans-serif!important;}
</style>


主页:default.asp === index.html
    !diff -s /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/default.asp /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/index.html
        ... are identical


主页:导航栏
    #body之内，h1之前
<div class='w3-sidebar w3-collapse' id='sidenav'>
  <div id='leftmenuinner'>
    <div id='leftmenuinnerinner'>
    ...可能 包含<div>
    </div>
  </div>
</div>

主页:乙型主页:
<h1>HTML Graphics</h1>
<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="https://www.w3schools.com/default.asp">&#10094; Previous</a>
  <a class="w3-right w3-btn" href="svg_intro.asp">Next &#10095;</a>
</div>
    ... ...
<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="https://www.w3schools.com/default.asp">&#10094; Previous</a>
  <a class="w3-right w3-btn" href="svg_intro.asp">Next &#10095;</a>
</div>


主页:甲型主页:Home而非Previous
<h1>HTML <span class="color_h1">Element Reference</span></h1>

<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="att_style_scoped.asp">&#10094; Home</a>
<a class="w3-right w3-btn" href="ref_byfunc.asp">Next &#10095;</a>
</div>
    ... ...
<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="att_style_scoped.asp">&#10094; Home</a>
<a class="w3-right w3-btn" href="ref_byfunc.asp">Next &#10095;</a>
</div>


]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose +dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/
    +dry_run
view script/clean_w3schools_pages--py_adhoc_call.py

from script.clean_w3schools_pages import *
]]]'''#'''
__all__ = r'''
Fail
LogicError

clean_w3schools_page_
    fmt4output_page
    clean_w3schools_default_index_page_
    clean_w3schools_material_page_

main4clean_w3schools_page_dir_from_to_
    clean_w3schools_page_dir_from_to_
        clean_w3schools_page_from_to_
            clean_w3schools_page_at_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#import re
from pathlib import Path
from seed.tiny_.check import check_type_is, check_int_ge
from seed.str_tools.Errors import BaseError, Fail, ParamError

#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.debug.print_err import print_err
    from seed.tiny_.check_path import check_dir_path_, check_not_same_path_
    from seed.filesys.fnmatch_ import list_filter_paths_via_patterns4fname__
    from seed.helper.xforce import check_xforce_, mk_xforce_, b_skip5xforce_opath4file_
    #bug:when 『except Fail as e:』lazy_obj not cls:from seed.str_tools.find_interval import Fail, ParamError
    from seed.str_tools.find_interval import indexs_, index_trials_
    from seed.str_tools.find_interval import find_interval4the_containing_html_element_at__
    from seed.tiny_.containers import mk_tuple__split_first_if_str__sep_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


__all__


assert issubclass(Fail, Exception)
class LogicError(Exception):pass

fmt4output_page = r'''<!DOCTYPE html>
<html>
<head>
{title6head}
{css6head}
</head>
<body>
{side_navigation6body}
{content6body}
</body>
</html>'''#'''

def _part1_clean_w3schools_xxx_page_(page, /, *, kwds7patch):
    try:
        ((ihead, _), (_, jhead), (ibody, _), (_, jbody)) = indexs_(page, 0, len(page), '<head  </head>  <body  </body>'.split())
    except Fail:
        if kwds7patch.get('patch_when_missing_HEAD_tag') and not '<head' in page:
            ((ibody, _), (_, jbody)) = indexs_(page, 0, len(page), ' <body  </body>'.split())
            (ihead, jhead) = (0, ibody)
        else:
            raise
        (ihead, jhead), (ibody, jbody)
    (ihead, jhead), (ibody, jbody)
    ((ititle, _), (_, jtitle)) = indexs_(page, ihead, jhead, '<title  </title>'.split())
    (ititle, jtitle), (ibody, jbody)
    return ((ititle, jtitle), (ibody, jbody))
def clean_w3schools_default_index_page_(page, /, *, css6head, kwds7patch):
    ((ititle, jtitle), (ibody, jbody)) = _part1_clean_w3schools_xxx_page_(page, kwds7patch=kwds7patch)
    (j7inside_sidenav, _) = index_trials_(page, ibody, jbody, ("id='sidenav'", 'id="sidenav"'))
    (ielement, jelement) = find_interval4the_containing_html_element_at__('div', j7inside_sidenav, page, ibody, jbody)
    #.if not tag == 'div': raise Fail('fail:search side_navigation6body <div>', nm4element)
    side_navigation6body = page[ielement:jelement]
    ((ih1, _), _, _, (_, jdiv)) = indexs_(page, jelement, jbody, '<h1  Next  Next  </div>'.split())
    title6head = page[ititle:jtitle]
    content6body = page[ih1:jdiv]
    output_default_index_page = fmt4output_page.format(title6head=title6head, css6head=css6head, side_navigation6body=side_navigation6body, content6body=content6body)
    return output_default_index_page












def clean_w3schools_material_page_(page, /, *, css6head, kwds7patch):
    #.((ihead, _), (_, jhead), (ibody, _), (_, jbody)) = indexs_(page, 0, len(page), '<head  </head>  <body  </body>'.split())
    #.((ititle, _), (_, jtitle)) = indexs_(page, ihead, jhead, '<title  </title>'.split())
    #raise KeyError(kwds7patch)
    ((ititle, jtitle), (ibody, jbody)) = _part1_clean_w3schools_xxx_page_(page, kwds7patch=kwds7patch)
    try:
        ((ih1, _), _, _, (_, jdiv)) = indexs_(page, ibody, jbody, '<h1  Previous</a>  Previous</a>  </div>'.split())
    except Fail:
        if kwds7patch.get('patch_when_missing_Previous_via_nextprev') and not 'Previous</a>' in page:
            ((ih1, _), _, _, (_, jdiv)) = indexs_(page, ibody, jbody, '<h1  nextprev  nextprev  </div>'.split())
        else:
            raise
        (ih1, jdiv)
    (ih1, jdiv)

    title6head = page[ititle:jtitle]
    content6body = page[ih1:jdiv]
    output_material_page = fmt4output_page.format(title6head=title6head, css6head=css6head, side_navigation6body='', content6body=content6body)
    return output_material_page
    r'''[[[
    #但都有:nextprev
例外一:没有『Previous</a>』:
    view /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/sql_ref_add.asp

<h1>SQL <span class="color_h1">ADD Keyword</span></h1>

<div class="w3-clear w3-center nextprev">
<a class="w3-left w3-white w3-btn w3-border-grey" title="SQL Keywords Reference" href="sql_ref_keywords.asp">&#10094; SQL Keywords <span class="w3-hide-small">Reference</span></a>
<a class="w3-right w3-btn" href="sql_ref_add_constraint.asp"><span class="w3-hide-small">Next </span>&#10095;</a>
</div>
    #]]]'''#'''





def clean_w3schools_page_(page, /, *, index_vs_material, css6head, kwds7patch):
    check_type_is(bool, index_vs_material)
    clean_w3schools_xxx_page_ = clean_w3schools_default_index_page_ if not index_vs_material else clean_w3schools_material_page_
    return clean_w3schools_xxx_page_(page, css6head=css6head, kwds7patch=kwds7patch)


def clean_w3schools_page_at_(ipath4page, /, *, encoding, emay__index_vs_material:'(...|bool)', css6head, kwds7patch):
    ipath4page = Path(ipath4page)
    if emay__index_vs_material is ...:
        index_vs_material = not ipath4page.stem.lower() in 'default index'
    else:
        index_vs_material = emay__index_vs_material
    index_vs_material
    page = ipath4page.read_text(encoding=encoding)
    try:
        return clean_w3schools_page_(page, index_vs_material=index_vs_material, css6head=css6head, kwds7patch=kwds7patch)
    except Fail as e:
        raise Fail('clean_w3schools_page_at_()', ipath4page) from e


def clean_w3schools_page_from_to_(ipath4page, opath4page, /, *, verbose:bool, dry_run:bool, xforce:'(False/raise|True/overwrite|.../skip|None/interactive)', encoding, emay__index_vs_material:'(...|bool)', css6head, kwds7patch):
    check_type_is(bool, verbose)
    check_type_is(bool, dry_run)
    #check_xforce_(xforce)
    #check_type_is(bool, force)
    opath4page = Path(opath4page)
    b_skip = b_skip5xforce_opath4file_(xforce, opath4page, fmt4prompt='?overwrite: {!r} (y/n)?')
    if b_skip:
        print_err(f'skip: {ipath4page!r} --> {opath4page!r}')
        return


    smay_dry_run = '[dry_run]' if dry_run else ''
    if verbose: print_err(f'{smay_dry_run}clean: {ipath4page!r} --> {opath4page!r}:...', end='')

    try:
        cleaned_page = clean_w3schools_page_at_(ipath4page, encoding=encoding, emay__index_vs_material=emay__index_vs_material, css6head=css6head, kwds7patch=kwds7patch)

        if dry_run:
            #print_err(f'dry_run: {ipath4page!r} --> {opath4page!r}')
            pass
        else:
            #omode = 'wt' if force else 'xt'
            opath4page.write_text(cleaned_page, encoding=encoding)
                #force
    except:
        if verbose: print_err('fail!')
        raise
    if verbose: print_err('ok!')
    return


def clean_w3schools_page_dir_from_to_(ipath4page_dir, opath4page_dir, /, *, imay_max_num_files4clean, may_case_sensitive:'may bool', may_emay_smay_sep4str8patterns, patterns4fname4page, patterns4fname4excluded_page, patterns4fname4index_page, verbose:bool, dry_run:bool, xforce:'(False/raise|True/overwrite|.../skip|None/interactive)', encoding, css6head, kwds7patch):
    check_int_ge(-1, imay_max_num_files4clean)
    check_type_is(bool, verbose)
    check_type_is(bool, dry_run)
    check_xforce_(xforce)
    #check_type_is(bool, force)
    check_type_is(str, encoding)
    check_type_is(str, css6head)

    patterns4fname4page = mk_tuple__split_first_if_str__sep_(may_emay_smay_sep4str8patterns, patterns4fname4page)
    patterns4fname4excluded_page = mk_tuple__split_first_if_str__sep_(may_emay_smay_sep4str8patterns, patterns4fname4excluded_page)
    patterns4fname4index_page = mk_tuple__split_first_if_str__sep_(may_emay_smay_sep4str8patterns, patterns4fname4index_page)

    ipath4page_dir = Path(ipath4page_dir)
    opath4page_dir = Path(opath4page_dir)
    check_dir_path_(ipath4page_dir)
    check_dir_path_(opath4page_dir)
    check_not_same_path_(ipath4page_dir, opath4page_dir)

    ipaths = [*ipath4page_dir.iterdir()]
    ipaths.sort()
    (_, ipaths4page) = list_filter_paths_via_patterns4fname__(may_case_sensitive, patterns4fname4page, ipaths)
    (ipaths4page, _) = list_filter_paths_via_patterns4fname__(may_case_sensitive, patterns4fname4excluded_page, ipaths4page)
    (ipaths4material_page, ipaths4index_page) = list_filter_paths_via_patterns4fname__(may_case_sensitive, patterns4fname4index_page, ipaths4page)
    n = imay_max_num_files4clean
    for index_vs_material, ipaths4page in zip([False, True], [ipaths4index_page, ipaths4material_page]):
        kwds = dict(verbose=verbose, dry_run=dry_run, xforce=xforce, encoding=encoding, emay__index_vs_material=index_vs_material, css6head=css6head)
        for ipath4page in ipaths4page:
            if n == 0:break
            n -= 1 # neg ok
            opath4page = opath4page_dir/ipath4page.name
            clean_w3schools_page_from_to_(ipath4page, opath4page, **kwds, kwds7patch=kwds7patch)
        if n == 0:break


_ver2css6head = (
{'[<@css6head-ver1@>]': '<link rel="stylesheet" type="text/css" href="../browserref.css">'
,'[<@css6head-ver2@>]': '<link rel="stylesheet" href="../plus/plans/main.css">'
})
def main4clean_w3schools_page_dir_from_to_(ipath4page_dir, opath4page_dir, /, *, imay_max_num_files4clean=-1, may_case_sensitive:'may bool'=True, may_emay_smay_sep4str8patterns=None, patterns4fname4page='*.html *.asp *.php', patterns4fname4excluded_page=(), patterns4fname4index_page='default.* index.*', verbose:bool=False, dry_run:bool=False, interactive:bool=False, skip:bool=False, force:bool=False, encoding='utf8', css6head_or_its_version='[<@css6head-ver2@>]', kwds7patch={}):
    '不含 *.htm 因为 只是 小页面'
    check_type_is(str, css6head_or_its_version)
    xforce = mk_xforce_(b_interactive=interactive, b_skip=skip, b_force=force)
    css6head_or_its_version = css6head_or_its_version.strip()
    if css6head_or_its_version.startswith('[<@css6head-ver') and css6head_or_its_version.endswith('@>]'):
        ver4css6head = css6head_or_its_version
        css6head = _ver2css6head[ver4css6head]
    else:
        css6head = css6head_or_its_version
    css6head
    if css6head and not '<' == css6head[0]:raise ParamError('css6head_or_its_version:', css6head_or_its_version)
    return clean_w3schools_page_dir_from_to_(ipath4page_dir, opath4page_dir, imay_max_num_files4clean=imay_max_num_files4clean, may_case_sensitive=may_case_sensitive, may_emay_smay_sep4str8patterns=may_emay_smay_sep4str8patterns, patterns4fname4page=patterns4fname4page, patterns4fname4excluded_page=patterns4fname4excluded_page, patterns4fname4index_page=patterns4fname4index_page, verbose=verbose, dry_run=dry_run, xforce=xforce, encoding=encoding, css6head=css6head, kwds7patch=kwds7patch)

__all__
from script.clean_w3schools_pages import *
