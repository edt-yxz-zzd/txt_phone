r'''[[[
e script/clean_w3schools_pages--py_adhoc_call.py
e script/clean_w3schools_pages--httpd.conf--w3schools-tmp-output

httpd -f /sdcard/0my_files/git_repos/txt_phone/txt/script/clean_w3schools_pages--httpd.conf--w3schools-tmp-output -k start
    http://127.0.0.1:8080/graphics/default.asp
    http://127.0.0.1:8080/bash/index.php
    http://127.0.0.1:8080/sql/default.asp

目录:
    [:区段牜服务器牜配置文件丶启动命令丶网址]:goto
    [:区段牜清理网页牜图像相关]:goto
    [:区段牜清理网页牜命令行]:goto
    [:区段牜清理网页牜数据库牜结构式查询语言]:goto
    [:区段牜复制附件]:goto









[[
[:区段牜清理网页牜图像相关]:here

@20251111
!mkdir /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/
!mkdir /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/
py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose +dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/
    +dry_run
py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose -dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/
    -dry_run
py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose -dry_run  +force --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/
    -dry_run +force
py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_  --imay_max_num_files4clean=3 +verbose -dry_run  +force --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/
    --imay_max_num_files4clean=3 -dry_run +force

view /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/default.asp
view /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/svg_intro.asp

view /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/canvas_circles.asp

view /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/trycanvas_coordinates.htm



[:区段牜复制附件]:goto

]]
[[
[:区段牜服务器牜配置文件丶启动命令丶网址]:here

@20251111
httpd -f /sdcard/0my_files/git_repos/txt_phone/txt/script/clean_w3schools_pages--httpd.conf--w3schools-tmp-output -k stop
    关闭服务器
httpd -f /sdcard/0my_files/git_repos/txt_phone/txt/script/clean_w3schools_pages--httpd.conf--w3schools-tmp-output -k start
    启动服务器:
        http://127.0.0.1:8080/graphics/default.asp
        http://127.0.0.1:8080/bash/index.php
    ######################
    #『-f』 必须 绝对路径
    #失败:httpd -f script/clean_w3schools_pages--httpd.conf--w3schools-tmp-output -k start
        #httpd: Could not open configuration file /data/data/com.termux/files/usr/script/clean_w3schools_pages--httpd.conf--w3schools-tmp-output: No such file or directory
        #因为 『httpd [ -d serverroot ] [ -f config ] ...』当命令行没有指定serverroot时，使用全局缺省值，而相对路径 是基于serverroot的。
    ######################
    ######################
    #对比:httpd -f /sdcard/0my_files/git_repos/txt_phone/lots/NOTE/html/httpd-confs/httpd.conf-sdcard_0my_files-unzip-py_doc-python_3_12_4_docs_html  -k start
    #view ../lots/NOTE/html/httpd-confs/httpd.conf-sdcard_0my_files-unzip-py_doc-python_3_12_4_docs_html
    #过气:view /sdcard/0my_files/unzip/png_specification/www.w3.org/Daemon/User/Config/httpd.conf.txt
    #       Pass,Port之类 都过气
    ######################
]]
<<==:
    配置文件全文如下:
@20251111
[[
#e script/clean_w3schools_pages--httpd.conf--w3schools-tmp-output
#   网址: http://127.0.0.1:8080/graphics/default.asp
    #view script/clean_w3schools_pages--py_adhoc_call.py

ServerRoot "/data/data/com.termux/files/usr"
LoadModule mpm_worker_module libexec/apache2/mod_mpm_worker.so
  #AH00534: httpd: Configuration error: No MPM loaded.
  #必要
LoadModule unixd_module libexec/apache2/mod_unixd.so
  # -k stop : httpd (no pid file) not running
  # 进程启动
LoadModule authz_core_module libexec/apache2/mod_authz_core.so
  #Invalid command 'Require', perhaps misspelled or defined by a module not included in the server configuration
  #见下面:『Require』指令:没有该指令，浏览器没有访问权限，打不开网页
ErrorLog "var/log/apache2/error_log"
  #(2)No such file or directory: AH02291: Cannot access directory '/data/data/com.termux/files/usr/logs/' for main error log
  #AH00014: Configuration check failed
ServerName localhost
  #AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1. Set the 'ServerName' directive globally to suppress this message

Listen 127.0.0.1:8080
  # 『80』fail, 『8080』ok!
#Listen 127.0.0.1:80
  #(13)Permission denied: AH00072: make_sock: could not bind to address 127.0.0.1:80
  #no listening sockets available, shutting down
  #AH00015: Unable to open logs
  #不知道为啥，反正端口『80』就是绑定不了

#######################
#这部分虽然可省略，但安全起见，还是保留吧。
<Directory / >
    AllowOverride none
    Require all denied
</Directory>
<Files ".ht*">
    Require all denied
</Files>
#######################


<VirtualHost *:8080>
    ServerName "localhost-w3schools.com-tmp-output"
    DocumentRoot "/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output"
</VirtualHost>
<Directory "/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output">
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>
#

#cp -iv /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/index.html /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/
#rm -iv /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/index.html
#.LoadModule dir_module libexec/apache2/mod_dir.so
#.<IfModule dir_module>
#.    DirectoryIndex index.html
#.</IfModule>

]]


[[
[:区段牜清理网页牜命令行]:here

@20251112
ls /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/
!mkdir /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/bash/
py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose +dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/bash/   --patterns4fname4excluded_page:'bash_exercises.php  bash_quiz.php  bash_exam.php'
    +dry_run
    部分网页:没有 <head>以及</head>
        view /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/bash_exercises.php
        bash_quiz.php
        bash_exam.php
py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose +dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/bash/   --kwds7patch='{"patch_when_missing_HEAD_tag":True}'
    +dry_run

py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose -dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/bash/   --kwds7patch='{"patch_when_missing_HEAD_tag":True}'
    -dry_run


[:区段牜复制附件]:goto
]]
[[
[:区段牜清理网页牜数据库牜结构式查询语言]:here

@20251112
ls /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/
!mkdir /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/sql/
py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose +dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/sql/    --patterns4fname4excluded_page:'sql_ref_add.asp  sql_ref_add_constraint.asp  sql_ref_all.asp  func_msaccess_abs.asp  func_msaccess_asc.asp'
    +dry_run
    估计很多网页:没有 'Previous</a>'
        view /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/sql_ref_add.asp
        sql_ref_add_constraint.asp
        sql_ref_all.asp
        func_msaccess_abs.asp
        func_msaccess_asc.asp
        ... ...
py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose +dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/sql/   --kwds7patch='{"patch_when_missing_Previous_via_nextprev":True}'
    +dry_run

py_adhoc_call   script.clean_w3schools_pages   @main4clean_w3schools_page_dir_from_to_ +verbose -dry_run  +skip --css6head_or_its_version:'[<@css6head-ver2@>]'   :/sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/sql/   --kwds7patch='{"patch_when_missing_Previous_via_nextprev":True}'
    -dry_run


[:区段牜复制附件]:goto
]]



[[
[:区段牜复制附件]:here


@20251112

#graphics:
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/
    880K #全是网页，尚未复制其余附件
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/
    32M

#bash:
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/bash/
    376K #全是网页，尚未复制其余附件
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/
    21M

#sql:
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/sql/
    2.5M #全是网页，尚未复制其余附件
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/
    180M
        3.3M images/
            images/* 都是 PPT封面，垃圾！



ls /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/*.{htm,gif}

#.find /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/ \! \( -name '*.html' -or -name '*.htm'  -or -name '*.asp'  -or -name '*.php' \)
    *.htm 似乎都是 测试小页

#output_dir:
find /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' \) -a -name '*.*'

#input_dir:
find /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' \) -a -name '*.*'
find /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' \) -a -name '*.*'
find /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' \) -a -name '*.*'




du -h  $(find /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' \) -a -name '*.*' )
    4.0K    trycanvas_coordinates.htm
    4.0K    img_arc.gif
    32K     pic_the_scream.jpg
    4.0K    clock.js
    4.0K    trygame_coordinates.htm
    4.0K    smiley.gif
    4.0K    angry.gif
    8.0K    trygame_gravity_game.htm
    8.0K    rotate1.png
    4.0K    game_movement1.png
    8.0K    game_movement2.png
    8.0K    game_movement3.png
    4.0K    game_movement4.png
    4.0K    trygame_movement_keyboard.htm

du -h  $(find /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' \) -a -name '*.*' )
    8.0K    prism_coy.css
    16K     prism_coy.js
    96K  xx img_cert_bash.png

du -h  $(find /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' \) -a -name '*.*' )
    images/* 都是 PPT封面，垃圾！
12K     img_inner_join.png
12K     img_full_outer_join.png
12K     img_left_join.png
12K     img_right_join.png
340K xx syllabus-exam.png
4.0K xx images/yt_logo_rgb_dark.webp
8.0K xx images/yt_logo_rgb_dark.png
108K xx images/img_sql_intro.webp
264K xx images/img_sql_intro.png
96K  xx images/img_sql_select.webp
252K xx images/img_sql_select.png
44K  xx images/img_sql_select_distinct.webp
436K xx images/img_sql_select_distinct.png
40K  xx images/img_sql_where.webp
420K xx images/img_sql_where.png
32K  xx images/img_sql_order_by.webp
260K xx images/img_sql_order_by.png
36K  xx images/img_sql_and.webp
268K xx images/img_sql_and.png
36K  xx images/img_sql_not.webp
272K xx images/img_sql_not.png
36K  xx images/img_sql_insert_into.webp
264K xx images/img_sql_insert_into.png
32K  xx images/img_sql_null.webp
264K xx images/img_sql_null.png
24K  xx images/sql_certificate.png
76K  xx images/sql_academy_class.png
60K  xx images/sql_challenge.png
792K xx sql_study_plan.png
56K  xx img_cert_sql.jpg


du -h  $(find /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' -or -name 'images' -prune -or -name syllabus-exam.png  -or -name sql_study_plan.png -or -name img_cert_sql.jpg \) -a -name '*.*' )
    12K     img_left_join.png
    12K     img_right_join.png
    12K     img_inner_join.png
    12K     img_full_outer_join.png

cp -iv -t /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/sql/   $(find /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' -or -name 'images' -prune -or -name syllabus-exam.png  -or -name sql_study_plan.png -or -name img_cert_sql.jpg \) -a -name '*.*' )


du -h  $(find /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' -or -name img_cert_bash.png \) -a -name '*.*' )
    8.0K    prism_coy.css
    16K     prism_coy.js

cp -iv -t /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/bash/   $(find /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' -or -name img_cert_bash.png \) -a -name '*.*' )


cp -iv -t /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/   $(find /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/ \! \( -name '*.html' -or -name '*.asp'  -or -name '*.php' \) -a -name '*.*' )


#复制附件后:
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/graphics/
    980K
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/bash/
    400K
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/sql/
    2.5M

#打包{附件已复制}
tar cJvf /sdcard/0my_files/book/lang/html/w3schools_graphics.txz -C /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/  graphics/
tar cJvf /sdcard/0my_files/book/lang/html/w3schools_bash.txz -C /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/  bash/
tar cJvf /sdcard/0my_files/book/lang/html/w3schools_sql.txz -C /sdcard/0my_files/tmp/wget_/www.w3schools.com-tmp-output/  sql/

@20251112
du -h /sdcard/0my_files/book/lang/html/w3schools_graphics.txz
    124K
du -h /sdcard/0my_files/book/lang/html/w3schools_bash.txz
    48K
du -h /sdcard/0my_files/book/lang/html/w3schools_sql.txz
    168K

vs:
    du -h /sdcard/0my_files/book/lang/html/w3schools_TAGs.txz
        348K
ls /sdcard/0my_files/book/lang/html/ -1
    w3schools_TAGs.txz
    w3schools_bash.txz
    w3schools_graphics.txz
    w3schools_sql.txz

rm -v -r /sdcard/0my_files/tmp/wget_/www.w3schools.com/bash/
rm -v -r /sdcard/0my_files/tmp/wget_/www.w3schools.com/graphics/
rm -v -r /sdcard/0my_files/tmp/wget_/www.w3schools.com/sql/

]]

#]]]'''#'''
