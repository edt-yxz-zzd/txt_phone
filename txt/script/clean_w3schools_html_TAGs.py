#__all__:goto
#__section__:goto
#[:def__kwds4clean]:goto
#clean-steps:
#[:section2__step1]:goto
#[:section2__step2]:goto
#[:section2__step3]:goto
#[:section2__step4]:goto
r"""[[[
e script/clean_w3schools_html_TAGs.py
    view  /sdcard/0my_files/book/lang/html/w3schools_TAGs.txz
    view others/app/termux/web_server.txt
    view ../lots/NOTE/html/tag/README-show-html.txt


py -m script.clean_w3schools_html_TAGs
py -m nn_ns.app.debug_cmd   script.clean_w3schools_html_TAGs -x
py -m nn_ns.app.doctest_cmd script.clean_w3schools_html_TAGs:__doc__ -ht
from script.clean_w3schools_html_TAGs import *

[[[[[
# [:__section__:2]:
now:
httpd -f /sdcard/0my_files/git_repos/txt_phone/lots/NOTE/html/httpd.conf-sdcard_0my_files
===
[[
TODO:
    #fixed:#fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp')
    #页面内容是别的页面！:fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp')
    #fixed[++to_turnon__common_sidenav/basenames4keep_sidenav]:fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp')
    #fixed:fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp')
]]
[[
DONE:TODO:ref_pxtoemconversion.asp
===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp
===
16:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp | grep '^[^<>]'
5,8c5
---
156,210c153
---
7638c7581
---
7640,7641c7583,7584
---
7643a7587,7588
7645,7677c7590
---
7679,7685c7592,7827
---
7688,7758d7829
7761,7762c7832,7833
---
===
19:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_httpmessages.asp | grep '^[^<>]'
5,8c5
---
156,210c153
---
7638c7581
---
7640,7641c7583,7584
---
7645,7664c7588,7696
---
7666,7677c7698,7700
---
7679,7685c7702,7703
---
7686a7705
7688,7757c7707,7840
---
7761,7762c7844,7845
---
===
17:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_country_codes.asp | grep '^[^<>]'
5,8c5
---
156,208c153
---
7638c7583
---
7640,7641c7585,7586
---
7643a7589,7603
7645,7664d7604
7666,7757d7605
7758a7607,9501
7761,7762c9504,9505
---
8674c10417
\ No newline at end of file
---
===
38:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_colornames.asp | grep '^[^<>]'
5,8c5
---
156,208d152
7638c7582
---
7640,7641c7584,7585
---
7643a7588,7668
7645,7667d7669
7668a7671,7685
7670,7685d7686
7686a7688,7689
7688,7711c7691,7694
---
7713c7696,7697
---
7715,7718c7699,7702
---
7720,7723c7704,7706
---
7725,7728c7708,7711
---
7729a7713,7714
7731,7734c7716,7719
---
7735a7721,7723
7737,7741c7725,7728
---
7742a7730,7731
7744,7748c7733,7736
---
7750,7756c7738,10206
---
7758a10209
7761,7762c10212,10213
---
8673c11124,11125
---
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_colornames.asp | grep '^[^<>]' -A3
5,8c5
< <title>PX to EM Conversion</title>
< <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
< <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
--
---
> <title>HTML Color Names</title>
156,208d152
< <link rel="stylesheet" href="../bootstrap/w3-fix.css">
< <style>
< table.notranslate tr:hover td{
--
7638c7582
< <h1>Pixels to Ems <span class="color_h1">Conversion</span></h1>
---
> <h1>HTML Color Names</h1>
7640,7641c7584,7585
< <a class="w3-left w3-btn" href="ref_httpmethods.asp">&#10094; Previous</a>
< <a class="w3-right w3-btn" href="ref_keyboardshortcuts.asp">Next &#10095;</a>
---
> <a class="w3-left w3-btn" href="ref_eventattributes.asp">&#10094; Previous</a>
> <a class="w3-right w3-btn" href="ref_canvas.asp">Next &#10095;</a>
7643a7588,7668
> <h2>Color Names Supported by All Browsers</h2>
> <p>All modern browsers support the following 140 color names (click on a color name, or a hex value, to view the color as the background-color along with different text colors):</p>
> <p><a href="https://www.w3schools.com/colors/default.asp">For a full overview of HTML colors, visit our
--
7645,7667d7669
< <h2>Pixel to Em Converter</h2>
< <p>The tool below allows you to work out the em sizes from pixels (or vice versa).</p>
< <ul>
--
7668a7671,7685
>     </div>
>   </div>
>
--
7670,7685d7686
< <h2>Body Font Size</h2>
< <p>In the table below, select a body font size in pixels (px) to display a
< complete &quot;px to em and percent&quot; conversion table.</p>
--
7686a7688,7689
>     </div>
>   </div>
7688,7711c7691,7694
< <script>
< function fillTable(x) {
< var t = "";
--
---
>   <div class="w3-col l4 m6 w3-center colorbox">
>     <div class="innerbox" id="box3" onmouseover="color_mouseover(this, 3)" onmouseout="color_mouseout(this, 3)">
>       <span class="colornamespan"><a target="_blank" href="https://www.w3schools.com/colors/color_tryit.asp?color=Aqua">Aqua</a></span><br>
--
7713c7696,7697
< fillTable(16);
---
> <div class="w3-row colorlinkcontainer" id="colorlinkcontainer3">
> <div style="float:left;width:50%"><div class="linktocolormixerdiv" id="linktomixer3"><a href="https://www.w3schools.com/colors/colors_mixer.asp?colorbottom=00FFFF&amp;colortop=FFFFFF">Color Mixer</a></div></div>
7715,7718c7699,7702
< function wrong() {
<  document.getElementById("myInput2").disabled = true;
<  document.getElementById("myInput2").value = "";
--
---
> <div style="float:left;width:50%"><div class="linktocolorpickerdiv" id="linktopicker3"><a href="https://www.w3schools.com/colors/colors_picker.asp?colorhex=00FFFF">Color Picker</a></div></div>
>
>
--
7720,7723c7704,7706
< function wrong2() {
<  document.getElementById("myInput").disabled = true;
<  document.getElementById("myInput").value = "";
--
---
> </div>
>     </div>
>   </div>
7725,7728c7708,7711
< function works() {
<  document.getElementById("myInput2").disabled = false;
<  document.getElementById("myInput2").value = "";
--
---
>   <div class="w3-col l4 m6 w3-center colorbox">
>     <div class="innerbox" id="box4" onmouseover="color_mouseover(this, 4)" onmouseout="color_mouseout(this, 4)">
>       <span class="colornamespan"><a target="_blank" href="https://www.w3schools.com/colors/color_tryit.asp?color=Aquamarine">Aquamarine</a></span><br>
--
7729a7713,7714
> <div class="w3-row colorlinkcontainer" id="colorlinkcontainer4">
> <div style="float:left;width:50%"><div class="linktocolormixerdiv" id="linktomixer4"><a href="https://www.w3schools.com/colors/colors_mixer.asp?colorbottom=7FFFD4&amp;colortop=FFFFFF">Color Mixer</a></div></div>
7731,7734c7716,7719
< function works2() {
<  document.getElementById("myInput").disabled = false;
<  document.getElementById("myInput").value = "";
--
---
> <div style="float:left;width:50%"><div class="linktocolorpickerdiv" id="linktopicker4"><a href="https://www.w3schools.com/colors/colors_picker.asp?colorhex=7FFFD4">Color Picker</a></div></div>
>
>
--
7735a7721,7723
> </div>
>     </div>
>   </div>
7737,7741c7725,7728
< function myFunction() {
<     var x = document.getElementById("myInput").value;
<     var z = document.getElementById("myInput2").value;
--
---
>   <div class="w3-col l4 m6 w3-center colorbox">
>     <div class="innerbox" id="box5" onmouseover="color_mouseover(this, 5)" onmouseout="color_mouseout(this, 5)">
>       <span class="colornamespan"><a target="_blank" href="https://www.w3schools.com/colors/color_tryit.asp?color=Azure">Azure</a></span><br>
--
7742a7730,7731
> <div class="w3-row colorlinkcontainer" id="colorlinkcontainer5">
> <div style="float:left;width:50%"><div class="linktocolormixerdiv" id="linktomixer5"><a href="https://www.w3schools.com/colors/colors_mixer.asp?colorbottom=F0FFFF&amp;colortop=FFFFFF">Color Mixer</a></div></div>
7744,7748c7733,7736
<     if (x) {
<         res.innerHTML = x/y + "em";
<     } else {
--
---
> <div style="float:left;width:50%"><div class="linktocolorpickerdiv" id="linktopicker5"><a href="https://www.w3schools.com/colors/colors_picker.asp?colorhex=F0FFFF">Color Picker</a></div></div>
>
>
--
7750,7756c7738,10206
<     if (isNaN (x) || isNaN (z) || isNaN (y)) {
<         res.innerHTML = "Wrong input! Use numbers";
<         res.style.color = "red";
--
---
> </div>
>     </div>
>   </div>
--
7758a10209
>
7761,7762c10212,10213
< <a class="w3-left w3-btn" href="ref_httpmethods.asp">&#10094; Previous</a>
< <a class="w3-right w3-btn" href="ref_keyboardshortcuts.asp">Next &#10095;</a>
---
> <a class="w3-left w3-btn" href="ref_eventattributes.asp">&#10094; Previous</a>
> <a class="w3-right w3-btn" href="ref_canvas.asp">Next &#10095;</a>
8673c11124,11125
< <![endif]--></body>
---
> <![endif]-->
> </body>
===
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp | grep '^[^<>]' -A3
5,8c5
< <title>PX to EM Conversion</title>
< <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
< <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
--
---
> <title>HTML Character Sets</title>
156,210c153
< <link rel="stylesheet" href="../bootstrap/w3-fix.css">
< <style>
< table.notranslate tr:hover td{
--
---
> </head><body>
7638c7581
< <h1>Pixels to Ems <span class="color_h1">Conversion</span></h1>
---
> <h1>HTML <span class="color_h1">Character Sets</span></h1>
7640,7641c7583,7584
< <a class="w3-left w3-btn" href="ref_httpmethods.asp">&#10094; Previous</a>
< <a class="w3-right w3-btn" href="ref_keyboardshortcuts.asp">Next &#10095;</a>
---
> <a class="w3-left w3-btn" href="ref_av_dom.asp">&#10094; Previous</a>
> <a class="w3-right w3-btn" href="ref_html_dtd.asp">Next &#10095;</a>
7643a7587,7588
> <h2>Common HTML Character Sets</h2>
> <p>The default character set in HTML5 is UTF-8.</p>
7645,7677c7590
< <h2>Pixel to Em Converter</h2>
< <p>The tool below allows you to work out the em sizes from pixels (or vice versa).</p>
< <ul>
--
---
> <p>For a closer look, visit our <a href="https://www.w3schools.com/charsets/default.asp">Complete HTML Character Set Reference</a>.</p>
7679,7685c7592,7827
< <div class="w3-panel w3-note">
< <p><strong>What is the difference between PX, EM and Percent?</strong></p><p>Pixel
< is a static measurement, while percent and EM are relative
--
---
> <div class="w3-responsive">
> <table class="ws-table-all">
> <tr>
--
7688,7758d7829
< <script>
< function fillTable(x) {
< var t = "";
--
7761,7762c7832,7833
< <a class="w3-left w3-btn" href="ref_httpmethods.asp">&#10094; Previous</a>
< <a class="w3-right w3-btn" href="ref_keyboardshortcuts.asp">Next &#10095;</a>
---
> <a class="w3-left w3-btn" href="ref_av_dom.asp">&#10094; Previous</a>
> <a class="w3-right w3-btn" href="ref_html_dtd.asp">Next &#10095;</a>
===
===
!cp -iv /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]' -A3 -B3
e /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html
===
===
del <title>
del <h1>

</head><body>
-->:
</head>
<body>

del prev/next:两处:
<div class="w3-clear nextprev">
<a class="w3-left w3-btn" href="ref_av_dom.asp">&#10094; Previous</a>
<a class="w3-right w3-btn" href="ref_html_dtd.asp">Next &#10095;</a>
</div>

del main-body
==>>:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]'
5,8d4
156,208d151
7637,7763d7579
8674c8490
\ No newline at end of file
---

===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]'
5d4
153c152,153
---
7580,7834d7579
8745c8490
\ No newline at end of file
---
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]' -A3 -B3
5d4
< <title>HTML Character Sets</title>
153c152,153
< </head><body>
---
> </head>
> <body>
7580,7834d7579
<
< <h1>HTML <span class="color_h1">Character Sets</span></h1>
< <div class="w3-clear nextprev">
--
< <a class="w3-left w3-btn" href="ref_av_dom.asp">&#10094; Previous</a>
< <a class="w3-right w3-btn" href="ref_html_dtd.asp">Next &#10095;</a>
< </div>
8745c8490
< </html>
\ No newline at end of file
---
> </html>
===
===
<head>
... ...
... ...
<script src="https://www.w3schools.com/lib/my-learning/main.js?v=1.0.26"></script>
... 额外冫样式辻脚本
</head>

===
py_adhoc_call   script.clean_w3schools_html_TAGs   @str.clean_w3schools_html_TAGs__ipath_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp > /sdcard/0my_files/tmp/wget_/w3schools-html-TAGs-ref_pxtoemconversion.clean.html
view /sdcard/0my_files/tmp/wget_/w3schools-html-TAGs-ref_pxtoemconversion.clean.html
http://127.0.0.1:8080/tmp/wget_/w3schools-html-TAGs-ref_pxtoemconversion.clean.html
===
===
]]
[[
DONE:TODO:default.asp
===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp
http://127.0.0.1:8080/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp
===
20:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp | grep '^[^<>]'
0a1
4,5c5
---
153,237c153
---
7665,7666c7581
---
7668,7669c7583,7584
---
7671a7587,7588
7673,7676c7590
---
7678c7592,7593
---
7680c7595,7599
---
7683,8176c7602,7826
---
8182,8183c7832,7833
---
===
7:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]'
0a1
4,5d4
153,235d151
7664,8184d7579
9095c8490
\ No newline at end of file
---
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp | grep '^[^<>]' -A3 -B3
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]' -A3 -B3
===
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
===
===
old:before:to_turnon__common_sidenav@kwds4clean
py_adhoc_call   script.clean_w3schools_html_TAGs   @str.clean_w3schools_html_TAGs__ipath_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp > /sdcard/0my_files/tmp/wget_/w3schools-html-TAGs-default.clean.html
view /sdcard/0my_files/tmp/wget_/w3schools-html-TAGs-default.clean.html
http://127.0.0.1:8080/tmp/wget_/w3schools-html-TAGs-default.clean.html

===
++:
<div class='w3-sidebar w3-collapse' id='sidenav'>
  <div id='leftmenuinner'>
    <div id='leftmenuinnerinner'>
<!--  <a href='javascript:void(0)' onclick='close_menu()' class='w3-button w3-hide-large w3-large w3-display-topright' style='right:16px;padding:3px 12px;font-weight:bold;'>&times;</a>-->
<h2 class="left"><span class="left_h2">HTML</span> References</h2>
<a target="_top" class="no-checkmark" href="default.asp">HTML by Alphabet</a>
<a target="_top" class="no-checkmark" href="ref_byfunc.asp">HTML by Category</a>
<a target="_top" class="no-checkmark" href="ref_html_browsersupport.asp">HTML Browser Support</a>
<a target="_top" class="no-checkmark" href="ref_attributes.asp">HTML Attributes</a>
<a target="_top" class="no-checkmark" href="att_global_dropzone.asp">HTML Global Attributes</a>
<a target="_top" class="no-checkmark" href="ref_eventattributes.asp">HTML Events</a>
<a target="_top" class="no-checkmark" href="ref_colornames.asp">HTML Colors</a>
<a target="_top" class="no-checkmark" href="ref_canvas.asp">HTML Canvas</a>
<a target="_top" class="no-checkmark" href="ref_av_dom.asp">HTML Audio/Video</a>
<a target="_top" class="no-checkmark" href="ref_charactersets.asp">HTML Character Sets</a>
<a target="_top" class="no-checkmark" href="ref_html_dtd.asp">HTML Doctypes</a>
<a target="_top" class="no-checkmark" href="ref_urlencode.asp">HTML URL Encode</a>
<a target="_top" class="no-checkmark" href="ref_language_codes.asp">HTML Language Codes</a>
<a target="_top" class="no-checkmark" href="ref_country_codes.asp">HTML Country Codes</a>
<a target="_top" class="no-checkmark" href="ref_httpmessages.asp">HTTP Messages</a>
<a target="_top" class="no-checkmark" href="ref_httpmethods.asp">HTTP Methods</a>
<a target="_top" class="no-checkmark" href="ref_pxtoemconversion.asp">PX to EM Converter</a>
<a target="_top" class="no-checkmark" href="ref_keyboardshortcuts.asp">Keyboard Shortcuts</a>
<br>
<div class="notranslate">
<h2 class="left"><span class="left_h2">HTML</span> Tags</h2>
<a target="_top" class="no-checkmark" href="tag_comment.asp">&lt;!--&gt;</a>
<a target="_top" class="no-checkmark" href="tag_doctype.asp">&lt;!DOCTYPE&gt;</a>
<a target="_top" class="no-checkmark" href="tag_a.asp">&lt;a&gt;</a>
<a target="_top" class="no-checkmark" href="tag_abbr.asp">&lt;abbr&gt;</a>
<a target="_top" class="no-checkmark" href="tag_acronym.asp">&lt;acronym&gt;</a>
<a target="_top" class="no-checkmark" href="tag_address.asp">&lt;address&gt;</a>
<a target="_top" class="no-checkmark" href="tag_applet.asp">&lt;applet&gt;</a>
<a target="_top" class="no-checkmark" href="tag_area.asp">&lt;area&gt;</a>
<a target="_top" class="no-checkmark" href="tag_article.asp">&lt;article&gt;</a>
<a target="_top" class="no-checkmark" href="tag_aside.asp">&lt;aside&gt;</a>
<a target="_top" class="no-checkmark" href="tag_audio.asp">&lt;audio&gt;</a>
<a target="_top" class="no-checkmark" href="tag_b.asp">&lt;b&gt;</a>
<a target="_top" class="no-checkmark" href="tag_base.asp">&lt;base&gt;</a>
<a target="_top" class="no-checkmark" href="tag_basefont.asp">&lt;basefont&gt;</a>
<a target="_top" class="no-checkmark" href="tag_bdi.asp">&lt;bdi&gt;</a>
<a target="_top" class="no-checkmark" href="tag_bdo.asp">&lt;bdo&gt;</a>
<a target="_top" class="no-checkmark" href="tag_big.asp">&lt;big&gt;</a>
<a target="_top" class="no-checkmark" href="tag_blockquote.asp">&lt;blockquote&gt;</a>
<a target="_top" class="no-checkmark" href="tag_body.asp">&lt;body&gt;</a>
<a target="_top" class="no-checkmark" href="tag_br.asp">&lt;br&gt;</a>
<a target="_top" class="no-checkmark" href="tag_button.asp">&lt;button&gt;</a>
<a target="_top" class="no-checkmark" href="tag_canvas.asp">&lt;canvas&gt;</a>
<a target="_top" class="no-checkmark" href="tag_caption.asp">&lt;caption&gt;</a>
<a target="_top" class="no-checkmark" href="tag_center.asp">&lt;center&gt;</a>
<a target="_top" class="no-checkmark" href="tag_cite.asp">&lt;cite&gt;</a>
<a target="_top" class="no-checkmark" href="tag_code.asp">&lt;code&gt;</a>
<a target="_top" class="no-checkmark" href="tag_col.asp">&lt;col&gt;</a>
<a target="_top" class="no-checkmark" href="tag_colgroup.asp">&lt;colgroup&gt;</a>
<a target="_top" class="no-checkmark" href="tag_data.asp">&lt;data&gt;</a>
<a target="_top" class="no-checkmark" href="tag_datalist.asp">&lt;datalist&gt;</a>
<a target="_top" class="no-checkmark" href="tag_dd.asp">&lt;dd&gt;</a>
<a target="_top" class="no-checkmark" href="tag_del.asp">&lt;del&gt;</a>
<a target="_top" class="no-checkmark" href="tag_details.asp">&lt;details&gt;</a>
<a target="_top" class="no-checkmark" href="tag_dfn.asp">&lt;dfn&gt;</a>
<a target="_top" class="no-checkmark" href="tag_dialog.asp">&lt;dialog&gt;</a>
<a target="_top" class="no-checkmark" href="tag_dir.asp">&lt;dir&gt;</a>
<a target="_top" class="no-checkmark" href="tag_div.asp">&lt;div&gt;</a>
<a target="_top" class="no-checkmark" href="tag_dl.asp">&lt;dl&gt;</a>
<a target="_top" class="no-checkmark" href="tag_dt.asp">&lt;dt&gt;</a>
<a target="_top" class="no-checkmark" href="tag_em.asp">&lt;em&gt;</a>
<a target="_top" class="no-checkmark" href="tag_embed.asp">&lt;embed&gt;</a>
<a target="_top" class="no-checkmark" href="tag_fieldset.asp">&lt;fieldset&gt;</a>
<a target="_top" class="no-checkmark" href="tag_figcaption.asp">&lt;figcaption&gt;</a>
<a target="_top" class="no-checkmark" href="tag_figure.asp">&lt;figure&gt;</a>
<a target="_top" class="no-checkmark" href="tag_font.asp">&lt;font&gt;</a>
<a target="_top" class="no-checkmark" href="tag_footer.asp">&lt;footer&gt;</a>
<a target="_top" class="no-checkmark" href="tag_form.asp">&lt;form&gt;</a>
<a target="_top" class="no-checkmark" href="tag_frame.asp">&lt;frame&gt;</a>
<a target="_top" class="no-checkmark" href="tag_frameset.asp">&lt;frameset&gt;</a>
<a target="_top" class="no-checkmark" href="tag_hn.asp">&lt;h1&gt; - &lt;h6&gt;</a>
<a target="_top" class="no-checkmark" href="tag_head.asp">&lt;head&gt;</a>
<a target="_top" class="no-checkmark" href="tag_header.asp">&lt;header&gt;</a>
<a target="_top" class="no-checkmark" href="tag_hgroup.asp">&lt;hgroup&gt;</a>
<a target="_top" class="no-checkmark" href="tag_hr.asp">&lt;hr&gt;</a>
<a target="_top" class="no-checkmark" href="tag_html.asp">&lt;html&gt;</a>
<a target="_top" class="no-checkmark" href="tag_i.asp">&lt;i&gt;</a>
<a target="_top" class="no-checkmark" href="tag_iframe.asp">&lt;iframe&gt;</a>
<a target="_top" class="no-checkmark" href="tag_img.asp">&lt;img&gt;</a>
<a target="_top" class="no-checkmark" href="tag_input.asp">&lt;input&gt;</a>
<a target="_top" class="no-checkmark" href="tag_ins.asp">&lt;ins&gt;</a>
<a target="_top" class="no-checkmark" href="tag_kbd.asp">&lt;kbd&gt;</a>
<a target="_top" class="no-checkmark" href="tag_label.asp">&lt;label&gt;</a>
<a target="_top" class="no-checkmark" href="tag_legend.asp">&lt;legend&gt;</a>
<a target="_top" class="no-checkmark" href="tag_li.asp">&lt;li&gt;</a>
<a target="_top" class="no-checkmark" href="tag_link.asp">&lt;link&gt;</a>
<a target="_top" class="no-checkmark" href="tag_main.asp">&lt;main&gt;</a>
<a target="_top" class="no-checkmark" href="tag_map.asp">&lt;map&gt;</a>
<a target="_top" class="no-checkmark" href="tag_mark.asp">&lt;mark&gt;</a>
<a target="_top" class="no-checkmark" href="tag_menu.asp">&lt;menu&gt;</a>
<a target="_top" class="no-checkmark" href="tag_meta.asp">&lt;meta&gt;</a>
<a target="_top" class="no-checkmark" href="tag_meter.asp">&lt;meter&gt;</a>
<a target="_top" class="no-checkmark" href="tag_nav.asp">&lt;nav&gt;</a>
<a target="_top" class="no-checkmark" href="tag_noframes.asp">&lt;noframes&gt;</a>
<a target="_top" class="no-checkmark" href="tag_noscript.asp">&lt;noscript&gt;</a>
<a target="_top" class="no-checkmark" href="tag_object.asp">&lt;object&gt;</a>
<a target="_top" class="no-checkmark" href="tag_ol.asp">&lt;ol&gt;</a>
<a target="_top" class="no-checkmark" href="tag_optgroup.asp">&lt;optgroup&gt;</a>
<a target="_top" class="no-checkmark" href="tag_option.asp">&lt;option&gt;</a>
<a target="_top" class="no-checkmark" href="tag_output.asp">&lt;output&gt;</a>
<a target="_top" class="no-checkmark" href="tag_p.asp">&lt;p&gt;</a>
<a target="_top" class="no-checkmark" href="tag_param.asp">&lt;param&gt;</a>
<a target="_top" class="no-checkmark" href="tag_picture.asp">&lt;picture&gt;</a>
<a target="_top" class="no-checkmark" href="tag_pre.asp">&lt;pre&gt;</a>
<a target="_top" class="no-checkmark" href="tag_progress.asp">&lt;progress&gt;</a>
<a target="_top" class="no-checkmark" href="tag_q.asp">&lt;q&gt;</a>
<a target="_top" class="no-checkmark" href="tag_rp.asp">&lt;rp&gt;</a>
<a target="_top" class="no-checkmark" href="tag_rt.asp">&lt;rt&gt;</a>
<a target="_top" class="no-checkmark" href="tag_ruby.asp">&lt;ruby&gt;</a>
<a target="_top" class="no-checkmark" href="tag_s.asp">&lt;s&gt;</a>
<a target="_top" class="no-checkmark" href="tag_samp.asp">&lt;samp&gt;</a>
<a target="_top" class="no-checkmark" href="tag_script.asp">&lt;script&gt;</a>
<a target="_top" class="no-checkmark" href="tag_search.asp">&lt;search&gt;</a>
<a target="_top" class="no-checkmark" href="tag_section.asp">&lt;section&gt;</a>
<a target="_top" class="no-checkmark" href="tag_select.asp">&lt;select&gt;</a>
<a target="_top" class="no-checkmark" href="tag_small.asp">&lt;small&gt;</a>
<a target="_top" class="no-checkmark" href="tag_source.asp">&lt;source&gt;</a>
<a target="_top" class="no-checkmark" href="tag_span.asp">&lt;span&gt;</a>
<a target="_top" class="no-checkmark" href="tag_strike.asp">&lt;strike&gt;</a>
<a target="_top" class="no-checkmark" href="tag_strong.asp">&lt;strong&gt;</a>
<a target="_top" class="no-checkmark" href="tag_style.asp">&lt;style&gt;</a>
<a target="_top" class="no-checkmark" href="tag_sub.asp">&lt;sub&gt;</a>
<a target="_top" class="no-checkmark" href="tag_summary.asp">&lt;summary&gt;</a>
<a target="_top" class="no-checkmark" href="tag_sup.asp">&lt;sup&gt;</a>
<a target="_top" class="no-checkmark" href="tag_svg.asp">&lt;svg&gt;</a>
<a target="_top" class="no-checkmark" href="tag_table.asp">&lt;table&gt;</a>
<a target="_top" class="no-checkmark" href="tag_tbody.asp">&lt;tbody&gt;</a>
<a target="_top" class="no-checkmark" href="tag_td.asp">&lt;td&gt;</a>
<a target="_top" class="no-checkmark" href="tag_template.asp">&lt;template&gt;</a>
<a target="_top" class="no-checkmark" href="tag_textarea.asp">&lt;textarea&gt;</a>
<a target="_top" class="no-checkmark" href="tag_tfoot.asp">&lt;tfoot&gt;</a>
<a target="_top" class="no-checkmark" href="tag_th.asp">&lt;th&gt;</a>
<a target="_top" class="no-checkmark" href="tag_thead.asp">&lt;thead&gt;</a>
<a target="_top" class="no-checkmark" href="tag_time.asp">&lt;time&gt;</a>
<a target="_top" class="no-checkmark" href="tag_title.asp">&lt;title&gt;</a>
<a target="_top" class="no-checkmark" href="tag_tr.asp">&lt;tr&gt;</a>
<a target="_top" class="no-checkmark" href="tag_track.asp">&lt;track&gt;</a>
<a target="_top" class="no-checkmark" href="tag_tt.asp">&lt;tt&gt;</a>
<a target="_top" class="no-checkmark" href="tag_u.asp">&lt;u&gt;</a>
<a target="_top" class="no-checkmark" href="tag_ul.asp">&lt;ul&gt;</a>
<a target="_top" class="no-checkmark" href="tag_var.asp">&lt;var&gt;</a>
<a target="_top" class="no-checkmark" href="tag_video.asp">&lt;video&gt;</a>
<a target="_top" class="no-checkmark" href="tag_wbr.asp">&lt;wbr&gt;</a>
</div>
      <br><br>
    </div>
  </div>
</div>
<div class='w3-main w3-light-grey' id='belowtopnav' style='margin-left:250px;'>
===
#[:def__kwds4clean]:goto
===
new:after:to_turnon__common_sidenav@kwds4clean
py_adhoc_call   script.clean_w3schools_html_TAGs   @str.clean_w3schools_html_TAGs__ipath_   --encoding:utf8  +to_turnon__common_sidenav :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp > /sdcard/0my_files/tmp/wget_/w3schools-html-TAGs-default.clean.html
view /sdcard/0my_files/tmp/wget_/w3schools-html-TAGs-default.clean.html
http://127.0.0.1:8080/tmp/wget_/w3schools-html-TAGs-default.clean.html

===
===
]]
[[
DONE[页面内容是别的页面:w3schools-bug!]:TODO:att_style_scoped.asp
===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp
http://127.0.0.1:8080/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp
===
36:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_charactersets.asp | grep '^[^<>]'
5c5
---
153,885c153
---
7901a7170,7175
8052c7326
---
8108c7382
---
8140,8221c7414,7561
---
8223,8244c7563
---
8246,8268d7564
8270,8271d7565
8272a7567
8274,8706c7569
---
8708,8827c7571,7577
---
8829,8861d7578
8864,8873c7581,7833
---
8875,9253d7834
9357a7939,7946
9358a7948,7987
9359a7989,8243
9361,9362c8245,8307
---
9364c8309
---
9367a8313,8332
9519c8484,8537
---
9726,9727c8744
---
===
35:
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]'
5d4
153,883d151
885c153
---
7901a7170,7175
8052c7326
---
8108c7382
---
8140,8197c7414,7561
---
8199,8244c7563
---
8246,8247d7564
8249,8250d7565
8251a7567
8253,8706c7569
---
8708,8717c7571,7577
---
8719,8734d7578
8736,9253d7579
9357a7684,7691
9358a7693,7732
9359a7734,7988
9361,9362c7990,8052
---
9364c8054
---
9367a8058,8077
9519c8229,8282
---
9726,9728c8489,8490
\ No newline at end of file
---
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]' -A3 -B3
5d4
< <title>W3Schools Online Web Tutorials</title>
153,883d151
< <style>
< /* Customize w3schools23.css */
< #nav_tutorials,
--
<   font-family: Verdana,sans-serif;
< }
< </style>
885c153
< <body style="font-family: 'Source Sans Pro', sans-serif;">
---
> <body>
7901a7170,7175
> @media screen and (max-width: 992px){
>   #subtopnav a.subtopnav_firstitem {
>     margin-left:50px!important;
>   }
> }
>
8052c7326
<         <a href='javascript:void(0);' class='topnav-icons fa fa-menu w3-hide-large w3-hide-medium w3-hide-small w3-left w3-bar-item w3-button ga-nav' style="line-height:1.1;padding-top:3px!important;" onclick='open_menu()' title='Menu'></a>
---
>         <a href='javascript:void(0);' class='topnav-icons fa fa-menu w3-hide-large w3-left w3-bar-item w3-button ga-nav' style="line-height:1.1;padding-top:8px!important;padding-bottom:8px!important;" onclick='open_menu()' title='Menu'></a>
8108c7382
<       <a href='javascript:void(0);' class='topnav-icons fa fa-menu w3-hide-large w3-hide-medium w3-hide-small w3-left w3-bar-item w3-button ga-nav' style="line-height:1.1;padding-top:8px!important;padding-bottom:7px!important;" onclick='open_menu()' title='Menu'></a>
---
>       <a href='javascript:void(0);' class='topnav-icons fa fa-menu w3-hide-large w3-left w3-bar-item w3-button ga-nav' style="line-height:1.1;padding-top:8px!important;padding-bottom:7px!important;" onclick='open_menu()' title='Menu'></a>
8140,8197c7414,7561
< <div class='w3-main w3-light-grey' id='belowtopnav'>
<
<   <div class='w3-row w3-white'>
--
<   </div>
<  </div>
<  </div>
---
> <div class='w3-sidebar w3-collapse' id='sidenav'>
>   <div id='leftmenuinner'>
>     <div id='leftmenuinnerinner'>
--
> <a target="_top" class="no-checkmark" href="tag_var.asp">&lt;var&gt;</a>
> <a target="_top" class="no-checkmark" href="tag_video.asp">&lt;video&gt;</a>
> <a target="_top" class="no-checkmark" href="tag_wbr.asp">&lt;wbr&gt;</a>
8199,8244c7563
<
< <div class="w3-row w3-padding-32 ws-yellow">
< <div class="w3-content" style="xmax-width:1400px">
--
< &nbsp; x.style.fontSize = &quot;25px&quot;; <br>
< &nbsp; x.style.color = &quot;red&quot;; <br>}<br>
< &lt;/script&gt;
---
>       <br><br>
8246,8247d7564
<    </div>
<    <a href="https://www.w3schools.com/js/tryit.asp?filename=tryjs_default" target="_blank" class="w3-button ga-fp tryit-button">Try it Yourself</a>
8249,8250d7565
<  </div>
<  </div>
8251a7567
> <div class='w3-main w3-light-grey' id='belowtopnav' style='margin-left:250px;'>
8253,8706c7569
< <div class="w3-row w3-padding-32 ws-light-pink">
< <div class="w3-content" style="xmax-width:1400px">
<  <div class="w3-col l6 w3-center" style="padding:3%">
--
<         </div>
<       </a>
<     </div>
---
>   <div class='w3-row w3-white'>
8708,8717c7571,7577
<     <div class="w3-col l6 s12 w3-center" style="padding:2% 3%;height:auto;">
<       <a href="https://www.w3schools.com/ai/default.asp" title="Artificial Intelligence Tutorial" class="ga-fp">
<         <div class="w3-card-2 w3-round ws-light-pink" style="padding:24px">
--
<
<   </div>
< </div>
---
>     <div class='w3-col l10 m12' id='main'>
>       <div id='mainLeaderboard' style='overflow:hidden;'>
>         <!-- MainLeaderboard-->
--
>         <!--<pre>main_leaderboard, all: [728,90][970,90][320,50][468,60]</pre>-->
>         <div id="adngin-main_leaderboard-0"></div>
>         <!-- adspace leaderboard -->
8719,8734d7578
< <div class="ws-black" style="padding:30px 3px 85px 3px">
<   <div class="w3-content w3-padding" style="max-width:974px;padding-top:78px;padding-bottom:125px">
<     <h1 style="font-size:65px;font-weight:700;text-align:center">Code Editor</h1>
--
<         <div class="codeeditorbr-column codeeditorbr-middle">
<           <input type="text" disabled class="codeeditorbr-input" value="www.w3schools.com/tryit/">
<         </div>
8736,9253d7579
<         <div class="w3-bar" style="background-color:#f1f1f1">
<     <button class="w3-bar-item w3-button ga-fp codeeditorbr-tablink ws-grey" style="color:black" onclick="openLangTab(event,'Frontend')">Frontend</button>
<     <button class="w3-bar-item w3-button ga-fp codeeditorbr-tablink" style="color:black" onclick="openLangTab(event,'Backend')">Backend</button>
--
< });
<
< </script>
9357a7684,7691
> <div class="w3-col l2 m12" id="right">
>
> <div class="sidesection">
--
>     <div id="adngin-sidebar_top-0"></div>
>
>   </div>
9358a7693,7732
>
> <style>
> .ribbon-vid {
--
>     <a href="https://www.facebook.com/w3schoolscom/" target="_blank" title="W3Schools on Facebook"><span class="fa fa-facebook-square fa-2x ga-right"></span></a>
>     <a href="https://www.instagram.com/w3schools.com_official/" target="_blank" title="W3Schools on Instagram"><span class="fa fa-instagram fa-2x ga-right"></span></a>
>   </div>
9359a7734,7988
>
>
> <script>
--
>
> <div id="vidpos" class="sidesection" style="text-align:center;margin-bottom:0;height:0;">
> <div id="adngin-outstream-0"></div>
9361,9362c7990,8052
< <div id="footer" class="footer w3-container w3-white" style="border-top:0">
< <div class="w3-col l2 m12" id="right" style="display: none;">&nbsp;</div>
---
>
>
> <div id="stickypos" class="sidesection" style="text-align:center;position:sticky;top:50px;">
--
>   </div>
> </div>
>
9364c8054
< function secondSnigel() {};
---
> uic_r_c()
9367a8058,8077
> </div>
> <div id="footer" class="footer w3-container w3-white">
>
--
> <!--<hr>-->
>
> </div>
9519c8229,8282
< <div id="spacemyfooter" style="margin:auto;">
---
> <style>
> @media screen and (max-width: 1440px) {
>   .footerlinks_1 {
--
> }
> </style>
> <div id="spacemyfooter">
9726,9728c8489,8490
< <![endif]-->
< </body>
< </html>
\ No newline at end of file
---
> <![endif]--></body>
> </html>
===
===
<script>
subtopnav_intoview();
</script>


<div class='w3-main w3-light-grey' id='belowtopnav'>

  <div class='w3-row w3-white'>
    
    <div class='w3-col l12 m12' id='main'>      

<div class="ws-black w3-center herosection">
... ...
... ...
... ...
<!-- END MAIN -->

<script src="https://www.w3schools.com/lib/w3codecolor.js"></script>

===
grep '<div\|</div>' /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp > /sdcard/0my_files/tmp/out4grep/att_style_scoped.asp..div.out.txt
e /sdcard/0my_files/tmp/out4grep/att_style_scoped.asp..div.out.txt
%s/<div/(\0/g
%s/<\/div>/\0)/g
==>>:
<div class='w3-main w3-light-grey' id='belowtopnav'>
...？？？
</div>#belowtopnav
</div>#无匹配??
<div id="footer" class="footer w3-container w3-white" style="border-top:0">
===
fgrep 'att_style_scoped.asp' -r /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ -l
index.html
default.asp
att_scoped.asp
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/index.html
    same!
    应当是 访问www.w3schools.com/TAGs/ [===default.asp] 保存为index.html
===
http://127.0.0.1:8080/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp
http://127.0.0.1:8080/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_scoped.asp
http://127.0.0.1:8080/tmp/wget_/www.w3schools.com/TAGs/att_scoped.asp

===
fgrep 'scoped' /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp
    没有？？
    att_scoped.asp::<style scoped>att_style_scoped.asp
    default.asp::Home --> att_style_scoped.asp
    看来真的有毛病:内容是web::home而非attr::scoped
===
===
]]
[[
===
!mv /sdcard/0my_files/tmp/wget_/www.w3schools.com/ /sdcard/0my_files/tmp/wget_/www.w3schools.com-ver1/
!mkdir /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/ -p
py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__idir_odir_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/   --basenames4skip:att_style_scoped.asp   --basenames4keep_sidenav:default.asp
fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp')
skip:basenames4skip:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp')
fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_li.asp')
fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_ol.asp')
fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_s.asp')
fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_u.asp')
===
att_form_target.asp
tag_li.asp
tag_ol.asp
tag_s.asp
tag_u.asp
===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_u.asp
    区别:<head>含function NewWindow(text)
    相同:
    <title> 不含『<>』
    <h1> 含『<>』
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_ul.asp
    区别:<head>不含function NewWindow(text)
    相同:
    <title> 不含『<>』
    <h1> 含『<>』
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]'
5,11d4
159d151
7588,7674d7579
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp  /sdcard/0my_files/tmp/wget_/w3schools-TAGs.base-tpl.html | grep '^[^<>]' -A3 -B3
5,11d4
< <script>
< function NewWindow(text)
< {
--
< }
< </script>
< <title>HTML form target Attribute</title>
159d151
< <link rel="stylesheet" type="text/css" href="../browserref.css">
7588,7674d7579
<
<
< <h1>HTML &lt;form&gt; <span class="color_h1">target</span> Attribute</h1>
===
py_adhoc_call   script.clean_w3schools_html_TAGs   @str.clean_w3schools_html_TAGs__ipath_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp -to_turnon__common_sidenav
===
#fix-bug:『(?# <title>()</title>)』『function NewWindow(text){()}』
1. 标题也有tag:
    <title>(?P<title>[^<>]*(</title>
    -->
    <title>(?P<title>.*?)</title>
2. 注释中不能含『()』
    <title>(?P<title>[^<>]*(</title>
    -->bug:
    (?# <title>(?P<title>[^<>]*(</title> ?#)
    -->fix-bug:
    (?# <title>（?P<title>[^<>]*）</title> ?#)
    同理:分离出来:
    (r'''
    ...
    (?#
    function NewWindow(text)
    ...(...)...
    ?#)
    ...
    '''#'''
    )
    -->fix-bug:
    (r'''
    ...
    '''#'''
    ## (?#
    ## ...
    ## function NewWindow(text)
    ## ...(...)...
    ## ...
    ## ?#)
    r'''
    ...
    '''#'''
    )

===
===
[:section2__step1]:here
py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__idir_odir_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/   --basenames4skip:att_style_scoped.asp   --basenames4keep_sidenav:default.asp 2>&1 | grep skip -v
    ok:全是skip

ls /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/att_form_target.asp
    存在
ls /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/att_style_scoped.asp
    不存在
===
http://127.0.0.1:8080/tmp/wget_/www.w3schools.com/TAGs/default.asp
    存在
http://127.0.0.1:8080/tmp/wget_/www.w3schools.com/TAGs/att_style_scoped.asp
    不存在
===
[:section2__step2]:here
echo '
<!DOCTYPE html>
<html lang="en-US">
<head>
<title>bug-page@20240612:www.w3schools.com/TAGs/att_style_scoped.asp</title>
</head>
<body>
<pre>
att_style_scoped.asp come from:
    <a href="default.asp">default.asp :: Home<a>
    <a href="att_scoped.asp">att_scoped.asp :: &lt;style scoped&gt;<a>
</pre>
</body>

' > /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/att_style_scoped.asp
===
http://127.0.0.1:8080/tmp/wget_/www.w3schools.com/TAGs/att_style_scoped.asp
    不存在-->存在
===
===
]]
[[
非『.asp』文件 以及 其他文件夹
basename -a /sdcard/0my_files/tmp/wget_/w3schools/html/*
===
17:
basename -a /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/* | fgrep '.asp' -v
ls -1 /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ | fgrep '.asp' -v
img_arc.gif
img_beziercurve.gif
img_enterkeyhint_go.jpg
img_enterkeyhint_search.jpg
img_inputmode_email.jpg
img_inputmode_numeric.jpg
img_lamp.jpg
img_miterlimitBevelFig.gif
img_miterlimitFig.gif
img_quadraticcurve.gif
img_textbaseline.gif
img_the_scream.jpg
img_translate.gif
index.html
mov_bbb.mp4
mov_bbb.ogg
mov_bbb.webm
===
[index.html := default.asp]
===
ls -hsS /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ | fgrep '.asp' -v
total 261M
772K mov_bbb.mp4
604K mov_bbb.ogg
472K mov_bbb.webm
368K index.html
144K img_enterkeyhint_search.jpg
136K img_enterkeyhint_go.jpg
136K img_inputmode_email.jpg
108K img_inputmode_numeric.jpg
32K img_the_scream.jpg
8.0K img_textbaseline.gif
4.0K img_beziercurve.gif
4.0K img_translate.gif
4.0K img_arc.gif
4.0K img_quadraticcurve.gif
4.0K img_miterlimitFig.gif
4.0K img_miterlimitBevelFig.gif
4.0K img_lamp.jpg
===
du -hs /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/.
    4.4M <<== all-clean-asp-files
===
grep 'img_arc.gif\|img_beziercurve.gif\|img_enterkeyhint_go.jpg\|img_enterkeyhint_search.jpg\|img_inputmode_email.jpg\|img_inputmode_numeric.jpg\|img_lamp.jpg\|img_miterlimitBevelFig.gif\|img_miterlimitFig.gif\|img_quadraticcurve.gif\|img_textbaseline.gif\|img_the_scream.jpg\|img_translate.gif\|mov_bbb.mp4\|mov_bbb.ogg\|mov_bbb.webm'  -r  /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/  -l
att_enterkeyhint.asp
att_global_enterkeyhint.asp
att_global_inputmode.asp
att_inputmode.asp
canvas_fillstyle.asp
canvas_arc.asp
canvas_createpattern.asp
canvas_drawimage.asp
canvas_miterlimit.asp
canvas_textbaseline.asp
canvas_translate.asp
canvas_beziercurveto.asp
canvas_getimagedata.asp
canvas_quadraticcurveto.asp

===
fgrep 'mov_bbb.mp4' -l  /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/{att_enterkeyhint.asp,att_global_enterkeyhint.asp,att_global_inputmode.asp,att_inputmode.asp,canvas_fillstyle.asp,canvas_arc.asp,canvas_createpattern.asp,canvas_drawimage.asp,canvas_miterlimit.asp,canvas_textbaseline.asp,canvas_translate.asp,canvas_beziercurveto.asp,canvas_getimagedata.asp,canvas_quadraticcurveto.asp}
canvas_drawimage.asp
===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/canvas_drawimage.asp
===
[:section2__step3]:here
view ../lots/NOTE/tools/ffmpeg/howto/useful-ffmpeg-commands.txt
!mkdir /sdcard/0my_files/tmp/wget_/out4ffmpeg/
#ffmpeg -i /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/input.mp4 -ss 00:00:50.0 -codec copy -t 20 /sdcard/0my_files/tmp/wget_/out4ffmpeg/output.mp4
ffmpeg -loop 1 -i /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/mov_bbb.mp4 -ss 00:00:05 -codec copy -t 1 /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.mp4
    『Option loop not found.』
ffmpeg -i /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/mov_bbb.mp4 -ss 00:00:05 -codec copy -t 1 /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.mp4
du -h  /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.mp4
    24K/second
    0.5s==>>12K
    1s==>>24K
mov_bbb.webm
    320x176(0.1MP)
mov_bbb.mp4
    320x176(0.1MP)
    (20x11)*16
    (60x33)*16/3
mov_bbb.ogg
    ???
#ffmpeg -i input.mp4 -s 480x320 -c:a copy output.mp4
ffmpeg -i /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/mov_bbb.mp4   -s 80x44 -c:a copy   /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.mp4
    20x11,60x33 无效，宽高必须是偶数！？
    40x22,80x44 有效，但浏览器无法显示？！
    80x44 其余播放器(VLC,mpv)播放异常
ffmpeg -i  ../lots/NOTE/html/tag/star.gif   -c:v libx264    /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.mp4
du -h /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.mp4
    4K

ffmpeg -i  ../lots/NOTE/html/tag/star.gif   -c:v libtheora    /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.ogg
    libtheora-小毛病:VLC无法播放,mpv正常播放
    ffmpeg -encoders | grep '^ V'
du -h /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.ogg
    16K

ffmpeg -i  ../lots/NOTE/html/tag/star.gif   -c:v libvpx-vp9    /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.webm
du -h /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.webm
    8K


mv  -iv  /sdcard/0my_files/tmp/wget_/out4ffmpeg/mov_bbb.{mp4,ogg,webm}   /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/
http://127.0.0.1:8080/tmp/wget_/www.w3schools.com/TAGs/canvas_drawimage.asp
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/mov_bbb.mp4
===
img_enterkeyhint_search.jpg
    1125x699(0.8MP)
img_enterkeyhint_go.jpg
    1125x699(0.8MP)
img_inputmode_email.jpg
    1125x682(0.8MP)
img_inputmode_numeric.jpg
    1125x682(0.8MP)
ffmpeg -i /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/img_enterkeyhint_search.jpg   -s 113x70 -c:a copy   /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/img_enterkeyhint_search.jpg
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/img_enterkeyhint_search.jpg
    4K

ffmpeg -i /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/img_enterkeyhint_go.jpg   -s 113x70 -c:a copy   /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/img_enterkeyhint_go.jpg
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/img_enterkeyhint_go.jpg
    4K

fgrep 'img_enterkeyhint_search.jpg' -l  /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/{att_enterkeyhint.asp,att_global_enterkeyhint.asp,att_global_inputmode.asp,att_inputmode.asp,canvas_fillstyle.asp,canvas_arc.asp,canvas_createpattern.asp,canvas_drawimage.asp,canvas_miterlimit.asp,canvas_textbaseline.asp,canvas_translate.asp,canvas_beziercurveto.asp,canvas_getimagedata.asp,canvas_quadraticcurveto.asp}
att_enterkeyhint.asp
att_global_enterkeyhint.asp

http://127.0.0.1:8080/tmp/wget_/www.w3schools.com/TAGs/att_enterkeyhint.asp
view /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/att_enterkeyhint.asp
===
ffmpeg -i /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/img_inputmode_email.jpg   -s 113x68 -c:a copy   /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/img_inputmode_email.jpg
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/img_inputmode_email.jpg
    4K
ffmpeg -i /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/img_inputmode_numeric.jpg   -s 113x68 -c:a copy   /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/img_inputmode_numeric.jpg
du -h /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/img_inputmode_numeric.jpg
    4K
http://127.0.0.1:8080/tmp/wget_/www.w3schools.com/TAGs/att_inputmode.asp
===
===
cp -iv /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/{img_the_scream.jpg,img_textbaseline.gif,img_beziercurve.gif,img_translate.gif,img_arc.gif,img_quadraticcurve.gif,img_miterlimitFig.gif,img_miterlimitBevelFig.gif,img_lamp.jpg} /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/
xxx:diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/
===
不需要:index.html
    !! [index.html := default.asp]
16:
ls -hsS /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/ | fgrep '.asp' -v
total 4.5M
 32K img_the_scream.jpg
 16K mov_bbb.ogg
8.0K img_textbaseline.gif
8.0K mov_bbb.webm
4.0K mov_bbb.mp4
4.0K img_enterkeyhint_search.jpg
4.0K img_beziercurve.gif
4.0K img_enterkeyhint_go.jpg
4.0K img_inputmode_email.jpg
4.0K img_translate.gif
4.0K img_arc.gif
4.0K img_quadraticcurve.gif
4.0K img_inputmode_numeric.jpg
4.0K img_miterlimitFig.gif
4.0K img_miterlimitBevelFig.gif
4.0K img_lamp.jpg
===
]]
[[
[:section2__step4]:here
打包:
===
du -hs /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/
    261M
du -hs /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/   --exclude='**/www.w3schools.com/TAGs/**'
    291K
ls -1 /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/
TAGs
bootstrap
browserref.css
css
favicon-16x16.png
favicon-32x32.png
favicon.ico
lib
plus
robots.txt
signup

cp -ivr /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/{bootstrap,browserref.css,css,favicon-16x16.png,favicon-32x32.png,favicon.ico,lib,plus,robots.txt,signup}  /sdcard/0my_files/tmp/wget_/www.w3schools.com/
    4.5M-->4.8M
du -hs /sdcard/0my_files/tmp/wget_/www.w3schools.com/
    4.8M

cd /sdcard/0my_files/tmp/wget_/ ; tar -cJvf w3schools_TAGs.txz  www.w3schools.com/
    4.8M-->348K
du -h w3schools_TAGs.txz
    348K
cp -iv /sdcard/0my_files/tmp/wget_/w3schools_TAGs.txz  /sdcard/0my_files/book/lang/html/
rm /sdcard/0my_files/book/lang/html/w3schools_TAGs.tgz
    output{ver1}:with some .asp files unclean, big-pic, big-video; without other toplayer folders

===
view /sdcard/0my_files/book/lang/html/w3schools_TAGs.txz
    ver2<<==section2
cp -iv /sdcard/0my_files/book/lang/html/w3schools_TAGs.txz ../lots/NOTE/html/tag/
view ../lots/NOTE/html/tag/w3schools_TAGs.txz

du -h script/clean_w3schools_html_TAGs.py
    68K
cp -iv script/clean_w3schools_html_TAGs.py '../lots/NOTE/html/tag/[20240613]clean_w3schools_html_TAGs.py'

===
===
===
]]

]]]]]



[[[[[
# [:__section__:1]:
===
[[[
cmds:
===
py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__ipath_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_a_download.asp

===
!mkdir /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/ -p
py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__idir_odir_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/



===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp
py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__ipath_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp

py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__idir_odir_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/   --basename4begin:att_form_target.asp


===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp
py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__idir_odir_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/   --basename4begin:att_style_scoped.asp   --basenames4skip:att_style_scoped.asp


===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp
py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__idir_odir_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/   --basename4begin:default.asp   --basenames4skip:att_style_scoped.asp:default.asp


===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp
py_adhoc_call   script.clean_w3schools_html_TAGs   @clean_w3schools_html_TAGs__idir_odir_   --encoding:utf8  :/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/  :/sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/   --basename4begin:ref_pxtoemconversion.asp   --basenames4skip:att_style_scoped.asp:default.asp:ref_pxtoemconversion.asp


===
ls -1 /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ | fgrep '.asp' -v | grep '[.].*' -o  |  sort -u
.gif
.html
.jpg
.mp4
.ogg
.webm
ls -1 /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/*.html
/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/index.html
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/index.html

cp -iv /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/{*.{gif,html,jpg,mp4,ogg,webm},att_style_scoped.asp,default.asp,ref_pxtoemconversion.asp}     /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/
du -hs  /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/
    8.2MB
ls -hsS  /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/
total 8.1M
772K mov_bbb.mp4
604K mov_bbb.ogg
472K mov_bbb.webm
392K att_style_scoped.asp
368K default.asp
368K index.html
356K ref_pxtoemconversion.asp
152K ref_colornames.asp
144K img_enterkeyhint_search.jpg
136K img_enterkeyhint_go.jpg
136K img_inputmode_email.jpg
116K ref_html_browsersupport.asp
108K img_inputmode_numeric.jpg
40K ref_attributes.asp
32K img_the_scream.jpg
28K ref_charactersets.asp
24K ref_urlencode.asp
20K att_input_type.asp
20K ref_byfunc.asp
... ...
... ...
4.0K img_miterlimitFig.gif
4.0K tag_frame.asp
4.0K img_miterlimitBevelFig.gif
4.0K tag_acronym.asp
4.0K tag_frameset.asp
4.0K att_onemptied.asp
4.0K img_lamp.jpg

===
cd /sdcard/0my_files/tmp/wget_/ ; tar -czvf w3schools_TAGs.tgz  www.w3schools.com/
    8.1M-->2.8M

du -h w3schools_TAGs.tgz
    2.8M

!mkdir /sdcard/0my_files/book/lang/html/
!cp -iv /sdcard/0my_files/tmp/wget_/w3schools_TAGs.tgz  /sdcard/0my_files/book/lang/html/w3schools_TAGs.tgz
===
e others/app/termux/web_server.txt
  apache2::httpd

httpd -f /sdcard/0my_files/tmp/wget_/httpd-conf4wget_
lynx http://127.0.0.1:8080/www.w3schools.com/TAGs/index.html
  /sdcard/0my_files/tmp/wget_/www.w3schools.com/TAGs/index.html
httpd -k stop
===
===
]]]
]]]]]






[[[[[
# [:__section__:0]:
===
[[[

===
https://www.w3schools.com/TAGs/
https://www.w3schools.com/TAGs/tag_table.asp
!mkdir /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/ -p
cd /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/ ; wget_web_under__nolimit  https://www.w3schools.com/TAGs/
... ...
... ...
Converting links in www.w3schools.com/TAGs/canvas_scale.asp... 611.
152-459
Converting links in www.w3schools.com/TAGs/att_onmouseup.asp... 614.
158-456
Converting links in www.w3schools.com/bootstrap/w3-fix.css... nothing to do.
Converted links in 750 files in 812 seconds.
===
cd /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/
du www.w3schools.com/ -hs
  261MB
du www.w3schools.com/TAGs/ -hs
  261MB

ls www.w3schools.com/TAGs/ -hsS
  # !! *.asp:76K,352K~472K,500K 基本是300多KB
total 261M
772K mov_bbb.mp4
604K mov_bbb.ogg
500K ref_colornames.asp
472K mov_bbb.webm
464K ref_html_browsersupport.asp
... ...
... ...
352K tag_frameset.asp
352K att_onemptied.asp
144K img_enterkeyhint_search.jpg
... ...
76K canvas_clip.asp
... ...
4.0K img_miterlimitBevelFig.gif
4.0K img_lamp.jpg

===
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_onemptied.asp
view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/canvas_clip.asp
===
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/canvas_clip.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_onemptied.asp | less
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_frameset.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_onemptied.asp | less
  太多重复代码...
diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_frameset.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_a.asp | less

diff /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/tag_a.asp /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp | less
===
<!DOCTYPE html>
<html lang="en-US">
<head>
<title>HTML a tag</title>
<meta charset="utf-8">
... ...
... ...
</head>
<body>
... ...
... ...
        <!-- adspace leaderboard -->

      </div>

<h1>HTML <span class="color_h1">&lt;a&gt;</span> Tag</h1>

<div class="w3-clear w3-center nextprev">
<a class="w3-left w3-btn" href="tag_doctype.asp">&#10094;<span class="w3-hide-small"> Previous</span></a>
<a class="w3-btn" href="default.asp"><span class="w3-hide-small">Complete HTML </span>Reference</a>
... ...
... ...主要区域
... ...
<a class="w3-right w3-btn" href="tag_abbr.asp"><span class="w3-hide-small">Next </span>&#10095;</a>
</div>
<div
  id="user-profile-bottom-wrapper"
  class="user-profile-bottom-wrapper"
>
... ...
... ...
<![endif]--></body>
</html>
===
]]]
]]]]]
#]]]"""
__all__ = r'''
regex4w3schools_html_TAG
    html4test
    regex4w3schools_html_TAG__prefix
fmt4clean_html
    clean_w3schools_html_TAGs__idir_odir_
    clean_w3schools_html_TAGs__ipath_
    clean_w3schools_html_TAGs__txt_
'''.split()#'''
__all__

from pathlib import Path
import re
from seed.tiny import print_err










# 注意: DOTALL<<==『.*?』
# 注意: 『 』-->『[ ]』<<==VERBOSE
# 注意: 『.』-->『[.]』
# 注意: 『?』-->『[?]』
# 注意: 『\n』-->『\n\s*』
# 注意: 『(?# () )』-->『(?# （） )』 #fix-bug:『(?# <title>()</title>)』『function NewWindow(text){()}』
#
if 0:
    #bug:
    assert (re.compile('(?#())').fullmatch(''))
        # re.error: unbalanced parenthesis at position 5
    #
else:
    assert (re.compile('(?#()').fullmatch('')) #)

regex4w3schools_html_TAG = re.compile(
r'''(?xs)
(?#vim:
s/[ .*?+]/[\0]/g
s/\n/\r\s*/g
?#)

\s*
<!DOCTYPE[ ]html>
\s*
<html[ ]lang="en-US">
\s*
<head>
\s*
(?:
(?#att_form_target.asp)
'''#'''
## (?#
## <script>
## function NewWindow(text)
## {
##   win=window.open(text,'','top=0,left=0,width=400,height=350');
## }
## </script>
## ?#)
r'''
<script>
.*?
</script>
\s*
)?
(?# <title>（?P<title>[^<>]*）</title> ?#)
<title>(?P<title>.*?)</title>
\s*
(?:
(?#ref_pxtoemconversion.asp)
(?#
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
?#)
<link[ ]rel="stylesheet"[ ]href="https://maxcdn[.]bootstrapcdn[.]com/bootstrap/3[.]3[.]5/css/bootstrap[.]min[.]css">
\s*
<script[ ]src="https://ajax[.]googleapis[.]com/ajax/libs/jquery/1[.]11[.]3/jquery[.]min[.]js"></script>
\s*
<script[ ]src="https://maxcdn[.]bootstrapcdn[.]com/bootstrap/3[.]3[.]5/js/bootstrap[.]min[.]js"></script>
\s*
)?
(?:
(?#default.asp)
(?#
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
?#)
<link[ ]rel="stylesheet"[ ]href="https://cdnjs[.]cloudflare[.]com/ajax/libs/font-awesome/4[.]7[.]0/css/font-awesome[.]min[.]css">
\s*
)?
<meta[ ]charset="utf-8">
.*?
(?#
<script src="https://www.w3schools.com/lib/my-learning/main.js?v=1.0.26"></script>
?#)
<script[ ]src="https://www[.]w3schools[.]com/lib/my-learning/main[.]js[?]v=1[.]0[.]26"></script>
(?:
(?#ref_pxtoemconversion.asp)
(?P<extra_style_script>.*?)
)
</head>
\s*
<body>
.*?
(?P<common_sidenav__optional>
<div[ ]class='w3-sidebar[ ]w3-collapse'[ ]id='sidenav'>
\s*
  <div[ ]id='leftmenuinner'>
\s*
    <div[ ]id='leftmenuinnerinner'>
.*?
<div[ ]class="notranslate">
.*?
</div>
\s*
      <br><br>
\s*
    </div>
\s*
  </div>
\s*
</div>
(?#common_sidenav__optional)
)
\s*
<div[ ]class='w3-main[ ]w3-light-grey'[ ]id='belowtopnav'[ ]style='margin-left:250px;'>
.*?
        <!--[ ]adspace[ ]leaderboard[ ]-->
\s*
      </div>
\s*
<h1>(?P<tagged_title>.*?)</h1>
(?P<main_area>.*?)
<div
\s*
  id="user-profile-bottom-wrapper"
\s*
  class="user-profile-bottom-wrapper"
\s*
>
.*?
</body>
\s*
</html>
\s*
'''#'''
,re.VERBOSE | re.DOTALL
)

html4test = (r'''
<!DOCTYPE html>
<html lang="en-US">
<head>
<title>HTML a tag</title>
<meta charset="utf-8">
... ...
... ...
<script src="https://www.w3schools.com/lib/my-learning/main.js?v=1.0.26"></script>
... ...
... ...额外冫样式辻脚本
... ...
</head>
<body>
... ...
... ...
<div class='w3-sidebar w3-collapse' id='sidenav'>
  <div id='leftmenuinner'>
    <div id='leftmenuinnerinner'>
... ...
... ...共同部分牜选择性保留
... ...
<div class="notranslate">
... ...
... ...共同部分牜选择性保留
... ...
</div>
      <br><br>
    </div>
  </div>
</div>
<div class='w3-main w3-light-grey' id='belowtopnav' style='margin-left:250px;'>
... ...
... ...
        <!-- adspace leaderboard -->

      </div>

<h1>HTML <span class="color_h1">&lt;a&gt;</span> Tag</h1>

<div class="w3-clear w3-center nextprev">
<a class="w3-left w3-btn" href="tag_doctype.asp">&#10094;<span class="w3-hide-small"> Previous</span></a>
<a class="w3-btn" href="default.asp"><span class="w3-hide-small">Complete HTML </span>Reference</a>
... ...
... ...主要区域
... ...
<a class="w3-right w3-btn" href="tag_abbr.asp"><span class="w3-hide-small">Next </span>&#10095;</a>
</div>
<div
  id="user-profile-bottom-wrapper"
  class="user-profile-bottom-wrapper"
>
... ...
... ...
<![endif]--></body>
</html>
'''#'''
)


regex4w3schools_html_TAG__prefix = re.compile(
r'''(?xs)
\s*
<!DOCTYPE[ ]html>
\s*
<html[ ]lang="en-US">
\s*
<head>
\s*
<title>(?P<title>[^<>]*)</title>
\s*
<meta[ ]charset="utf-8">
(?:(?!</head>).)*
</head>
'''#'''
)

assert regex4w3schools_html_TAG__prefix.match(html4test)
assert regex4w3schools_html_TAG.fullmatch(html4test)
    #fixed:bug: '(?x) ' --> '(?x)[ ]' #VERBOSE
    #fixed:bug: '(?x).*?' --> '(?xs).*?' #DOTALL

def __():
    #view /sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp
    ipath = '/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp'
    ipath = Path(ipath)
    txt = ipath.read_text('utf8')
    txt.index('</head>')
    whole_ptn = regex4w3schools_html_TAG.pattern
    if 0:
        end = whole_ptn.index('<body>')
    if 0:
        end = whole_ptn.index('main[.]js')
            #fail-->ok
    if 0:
        end = whole_ptn.index('<meta')
            #fail-->ok
    if 0:
        end = whole_ptn.index('<title>')
            #ok
    if 1:
        end = len(whole_ptn)
            #ok<<==fix-bug:『(?# <title>()</title>)』『function NewWindow(text){()}』
    ptn = whole_ptn[:end]
    _regex4w3schools_html_TAG__prefix = re.compile(ptn, re.VERBOSE | re.DOTALL)

    assert _regex4w3schools_html_TAG__prefix.match(txt)
__()


fmt4clean_html = r'''
<!DOCTYPE html>
<html lang="en-US">
<head>
<title>{title}</title>
<meta charset="utf-8">
{extra_style_script}
</head>
<body>
{common_sidenav__optional}
<h1>{tagged_title}</h1>
{main_area}
</body>
</html>
'''#'''

def basename_set5may_str(may_basenames__str, /):
    basenames = may_basenames__str.split(':') if may_basenames__str else []
    basenames = frozenset(basenames)
    return basenames
def clean_w3schools_html_TAGs__idir_odir_(idir, odir, /, *, encoding, glob_pattern='*.asp', basename4begin=None, basenames4skip=None, basenames4keep_sidenav):
    idir = Path(idir)
    odir = Path(odir)
    basenames4skip = basename_set5may_str(basenames4skip)
    basenames4keep_sidenav = basename_set5may_str(basenames4keep_sidenav)
        #kwds4clean

    ipaths = sorted(idir.glob(glob_pattern))
    if basename4begin:
        for i, ipath in enumerate(ipaths):
            if ipath.name == basename4begin:
                break
        else:
            raise IndexError(basename4begin)
        del ipaths[:i]
    for ipath in ipaths:
        basename = ipath.name
        if basename in basenames4skip:
            print_err(f'skip:basenames4skip:ipath:{ipath!r}')
            continue
        opath = odir / basename
        if opath.exists():
            print_err(f'skip:exists:opath:{opath!r}')
            continue
        kwds4clean = dict(to_turnon__common_sidenav=basename in basenames4keep_sidenav)
            #[:def__kwds4clean]:goto
        may_clean_html = clean_w3schools_html_TAGs__ipath_(ipath, encoding=encoding, **kwds4clean)
        if may_clean_html is None:
            print_err(f'fail:ipath:{ipath!r}')
            #fixed:#fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_form_target.asp')
            #fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/att_style_scoped.asp')
            #fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/default.asp')
            #fixed:fail:ipath:PosixPath('/sdcard/0my_files/tmp/wget_/w3schools/html/TAGs/www.w3schools.com/TAGs/ref_pxtoemconversion.asp')
            #raise 000
            continue
        clean_html = may_clean_html
        with open(opath, 'xt', encoding=encoding) as ofile:
            ofile.write(clean_html)
    return
def clean_w3schools_html_TAGs__ipath_(ipath, /, *, encoding, **kwds4clean):
    ipath = Path(ipath)
    #txt = ipath.read_text('utf8')
    txt = ipath.read_text(encoding)
    may_clean_html = clean_w3schools_html_TAGs__txt_(txt, **kwds4clean)
    return may_clean_html
def clean_w3schools_html_TAGs__txt_(txt, /, *, to_turnon__common_sidenav):
    '-> may clean_html'
    #[:def__kwds4clean]:here
    #kwds4clean == {to_turnon__common_sidenav}
    #

    #txt.index('\n  id="user-profile-bottom-wrapper"\n')
    m = regex4w3schools_html_TAG.fullmatch(txt)
    if m is None:
        return None
    d = (dict
    (title = m['title']
    ,extra_style_script = m['extra_style_script']
    ,common_sidenav__optional = m['common_sidenav__optional'] if to_turnon__common_sidenav else ''
    ,tagged_title = m['tagged_title']
    ,main_area = m['main_area']
    ))
    clean_html = fmt4clean_html.format(**d)
    return clean_html


if 0b000:print(clean_w3schools_html_TAGs__txt_(html4test, to_turnon__common_sidenav=True))
__all__
from script.clean_w3schools_html_TAGs import *
