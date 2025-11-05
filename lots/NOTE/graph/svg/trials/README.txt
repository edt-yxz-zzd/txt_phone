
e ../lots/NOTE/graph/svg/trials/README.txt

尝试一:无单位化宽高坐标
尝试二:嵌入文本
尝试三:几何图形
尝试四:路径
尝试五:组件
片段:标题丶描述
尝试六:裁剪显示区
猜测:有相当把握:线性变换矩阵

[[
@20251105
!mkdir ../lots/NOTE/graph/svg/trials/saved_svg/
cp -iv -t ../lots/NOTE/graph/svg/trials/saved_svg/  /sdcard/0my_files/tmp/graph/svg/trial_*.svg
ls ../lots/NOTE/graph/svg/trials/saved_svg/ -1
  trial_0.svg
  trial_1.svg
  trial_2.svg
  trial_3.svg
  trial_4.svg
  trial_5.svg

du -h ../lots/NOTE/graph/svg/trials/saved_svg/
  28K
du -h ../lots/NOTE/graph/svg/trials/README.txt
  16K
]]

[[
尝试一:无单位化宽高坐标
cp -iv ../lots/NOTE/graph/plantri45_adc3m3_hand_draw/6-10-1.svg /sdcard/0my_files/tmp/graph/svg/trial_0.svg
e /sdcard/0my_files/tmp/graph/svg/trial_0.svg
    del: standalone="no"
    精简:
    xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  version="1.2" baseProfile="tiny"
    -->:
    xmlns="http://www.w3.org/2000/svg"
        xmlns:这是必要的
            这大概就是standalone="no"的根源
        xlink:可能是因为本文件刚好没用到，在更复杂的svg里见到使用xlink@f0fba320057377a9c002eccd93a881d8.svg
          缺失报错:@PrivacyBrowser
              This page contains the following errors:
                  error on line 22 at column 52: Namespace prefix xlink for href on use is not defined
              Below is a rendering of the page up to the first error.

无单位宽高:

<?xml version="1.0" encoding="UTF-8"?>
<svg
width="200"
height="400"
viewBox="-100 -100 200 200"
    xmlns="http://www.w3.org/2000/svg" >
<!-- svg_tag.viewBox 定义 视窗的xy4topleft weight height 它们的单位 即是 内部 坐标的单位 ; 而svg_tag.weight,height 却是 对 viewBox.宽高 的 拉伸，比如:svg_tag.height=400 而viewBox.height=200 则 纵向拉伸为2倍 -->
<g stroke="#00FF00" stroke-width="10" >
  <polyline points="0,0 0,200 " />
</g>

<g stroke="#0000FF" stroke-width="10" >
  <polyline points="0,0 100,0 " />
</g>

</svg>

]]
[[
find /sdcard/Download/ -iname '*svg*'
ls /sdcard/Download/可能有用/*.svg
f0fba320057377a9c002eccd93a881d8.svg
  公式:log_(b;n+1)-log_(b;n)
GroupCycle_1000.svg
  ？箭头指来指去
CycleGraph_650.svg
  交换群元素的幂方轨迹
  带圈数字+弧线
NumberedEquation1.svg
  ？某种泛连分式？

grep '<\w\+' /sdcard/Download/可能有用/*.svg -o -h | sort -u
    <clipPath
    <defs
    <g
    <path
    <svg
    <symbol
    <use

du -h /sdcard/Download/可能有用/*.svg
132K    /sdcard/Download/可能有用/CycleGraph_650.svg
12K     /sdcard/Download/可能有用/GroupCycle_1000.svg
48K     /sdcard/Download/可能有用/NumberedEquation1.svg
4.0K    /sdcard/Download/可能有用/f0fba320057377a9c002eccd93a881d8.svg


tar -cJvf ../lots/NOTE/graph/svg/trials/some_svg5web-20251105.txz   -C  /sdcard/Download/可能有用/  CycleGraph_650.svg GroupCycle_1000.svg NumberedEquation1.svg f0fba320057377a9c002eccd93a881d8.svg
tar -tvf ../lots/NOTE/graph/svg/trials/some_svg5web-20251105.txz
du -h ../lots/NOTE/graph/svg/trials/some_svg5web-20251105.txz
  36K
tar -xvf ../lots/NOTE/graph/svg/trials/some_svg5web-20251105.txz -C /sdcard/0my_files/tmp/graph/svg/
ls /sdcard/0my_files/tmp/graph/svg/

view /sdcard/0my_files/tmp/graph/svg/CycleGraph_650.svg
view /sdcard/0my_files/tmp/graph/svg/GroupCycle_1000.svg
view /sdcard/0my_files/tmp/graph/svg/NumberedEquation1.svg
view /sdcard/0my_files/tmp/graph/svg/f0fba320057377a9c002eccd93a881d8.svg

发现:文本字形 直接 用path硬编码到svg里！神经病啊

#################################
# f0fba320057377a9c002eccd93a881d8.svg
#################################
#注意:没有 xml 声明
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="vertical-align:-.755ex" width="21.07ex" height="2.634ex" viewBox="0 -809.3 9071.8 1134.2">
<defs>
<path id="a" stroke-width="1" d="M42 46h14q39 0 47 14v64q0 19 1 43t0 50 0 55 0 57v213q0 26-1 44t0 17q-3 19-14 25t-45 9H26v23q0 23 2 23l10 1q10 1 29 2t37 2 37 2 30 3 11 1h3V379q0-317 1-319 4-8 12-11 21-3 49-3h16V0h-8l-23 1q-23 1-49 1t-38 1-38 0-50-2L34 0h-8v46h16z"/>
  #注意:『id="a"』
... ...
... ...
</defs>
<g fill="currentColor" stroke="currentColor" stroke-width="0" transform="scale(1 -1)">
<use xlink:href="#a"/>
<use x="278" xlink:href="#b"/>
<use x="779" xlink:href="#c"/>
<use x="1809" y="-343" transform="scale(.707)" xlink:href="#d"/>
<use x="1683" xlink:href="#e"/>
... ...
... ...
</g>
</svg>
#################################



#################################
# GroupCycle_1000.svg
#################################
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="159.19pt" height="159.19pt" viewBox="0 0 159.19 159.19" version="1.2">
<defs>
<g>
<symbol overflow="visible" id="glyph0-0">
<path style="stroke:none;" d=""/>
</symbol>
... ...
... ...
</g>
</defs>
<g id="surface1">
... ...
<path style=" stroke:none;fill-rule:nonzero;fill:rgb(0%,0%,0%);fill-opacity:1;" d="M 60.027344 31.953125 L 52.574219 46.019531 L 45.625 38.734375 "/>
... ...
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-1" x="73.952212" y="17.193515"/>
</g>
... ...
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-2" x="146.894562" y="86.70542"/>
</g>
... ...
... ...
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-4" x="74.040861" y="156.140825"/>
</g>
</g>
</svg>
#################################



#################################
# NumberedEquation1.svg
#################################
# 结构 类似于 GroupCycle_1000.svg
#################################


#################################
# CycleGraph_650.svg
#################################
定义区<defs>含 新见标签:
<clipPath id="clip1">
  <path d="M 450 188 L 503.960938 188 L 503.960938 242 L 450 242 Z M 450 188 "/>
</clipPath>


主体<g id="surface1">含 新见用法:
<g clip-path="url(#clip1)" clip-rule="nonzero">
  <path .../>
</g>
#################################

]]

[[
尝试二:嵌入文本
e /sdcard/0my_files/tmp/graph/svg/trial_1.svg

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
width="800"
height="1600"
viewBox="-400 -400 800 800"
    xmlns="http://www.w3.org/2000/svg" >
<!-- 尝试:文本 -->
<!--
view /sdcard/0my_files/tmp/out4py/py_src/site-packages/cairosvg/text.py
??? <textPath ...>
??? <text ...>
font-family="SimSun" font-size="9" font-weight="400" font-style="normal" 
font-family="sans-serif"
font-style="normal"
font-weight="400" or "bold" or "normal"
xlink:href= # f"#{id}"
letter-spacing
???x-bearing, y-bearing, width, height
x, y, dx, dy, rotate
text-anchor="middle" "end"
  baseline alignment tags
startOffset


grep 'vertical' -r /sdcard/0my_files/tmp/out4py/py_src/site-packages/cairosvg/ -i
  只能 单字符旋转，而非 字符串整行 旋转，也没有 竖排

文本无法换行？
  无效:<br/><p></p>
  无 或 无效:&newline; &FL; &FeedLine;
    有效:&#48; -> 『0』
    但 无效:&#13; &#10;

-->
<g stroke="#00FF00" stroke-width="10" >
  <polyline points="0,0 0,200 " />
</g>

<g stroke="#0000FF" stroke-width="10" >
  <polyline points="0,0 100,0 " />
</g>

<g stroke="red" stroke-width="3" fill="yellow"
  font-family="SimSun" font-size="80" font-weight="400" font-style="normal" >
  <text x="0" y="-100" dx="0" dy="0" rotate="90" text-anchor="middle" >xxxAAA</text>
  <text x="0" y="0" dx="0" dy="0" rotate="45" text-anchor="middle" >abc</text>
  <text x="0" y="0" dx="0" dy="100" rotate="0" text-anchor="middle" >dy=100</text>
  <text x="0" y="200" dx="0" dy="0" rotate="0" text-anchor="middle" >y=200</text>
  <text x="0" y="0" dx="300" dy="100" rotate="0" text-anchor="middle" >dx=300</text>
  <text x="300" y="0" dx="0" dy="0" rotate="0" text-anchor="middle" >x=300</text>
</g>
</svg>


]]
[[
尝试三:几何图形
e /sdcard/0my_files/tmp/graph/svg/trial_2.svg

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
width="800"
height="1600"
viewBox="-400 -400 800 800"
    xmlns="http://www.w3.org/2000/svg" >
<!-- 尝试:几何图形 -->
<!--
view ../lots/NOTE/graph/svg/shape_tags6svg.txt
  circle:r,cx,cy
  ellipse:rx,ry,cx,cy
  line:x1,y1,x2,y2
  polyline:points
  polygon: #polyline&&close_path
  rect:x,y,width,height,rx,ry

-->
<g stroke="#00FF00" stroke-width="10" >
  <polyline points="0,0 0,200 " />
</g>

<g stroke="#0000FF" stroke-width="10" >
  <polyline points="0,0 100,0 " />
</g>

<g stroke="red" stroke-width="3" fill="yellow" >
  <rect x="-400" y="-400" width="50" height="100" rx="0" ry="0" />
  <rect x="-300" y="-400" width="50" height="100" rx="10" ry="20" />

  <line x1="-200" y1="-400" x2="-150" y2="-300" />
  <polyline points="-100,-400 -50,-400 -50,-300 -75,-300" />
  <polygon points="0,-400 50,-400 50,-300 25,-300 " />

  <circle cx="125" cy="-350" r="25" />
  <ellipse cx="225" cy="-350" rx="25" ry="50" />

</g>
</svg>


]]

[[
尝试四:路径
e /sdcard/0my_files/tmp/graph/svg/trial_3.svg

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
width="400"
height="800"
viewBox="-200 -200 400 400"
    xmlns="http://www.w3.org/2000/svg" >
<!-- 尝试:路径 -->
<!--
e ../lots/NOTE/graph/svg/path6svg.txt

view /sdcard/0my_files/tmp/out4py/py_src/site-packages/cairosvg/path.py
  三角形:<path d="M 60 31 L 52 46 L 45 138 "/>

相对坐标:相对于 隐含的 当前坐标
  当前坐标 被更新为 最后一个坐标
M:move
  x y # 绝对坐标
m:relative move
  x y # 相对坐标

a A:arc# Elliptic curve
  #区分:相对坐标 绝对坐标
  rx ry rotation large sweep x3 y3
    large:regex"[01]"
    sweep:regex"[01]"
    # x1, y1 = current_point

C:Curve
  x1 y1 x2 y2 x3 y3 # 绝对坐标
c:Relative curve
  x1 y1 x2 y2 x3 y3 # 相对坐标
  应该就是 贝塞尔曲线？Bessel？

h:Relative horizontal line
  x # 相对坐标
H:Horizontal line
  x # 绝对坐标

l:Relative straight line
  x y # 相对坐标
L:Straight line
  x y # 绝对坐标

q:Relative quadratic curve
  x2 y2 x3 x3 # 相对坐标
  # x1 y1 := 0 0
Q:Quadratic curve
  x2 y2 x3 y3 # 绝对坐标
  # x1 y1 := 当前坐标

s:Relative smooth curve
  x2 y2 x3 x3 # 相对坐标
    x, y = current_point
    x1 = x3 - x2 if last_letter in 'csCS' else 0
    y1 = y3 - y2 if last_letter in 'csCS' else 0
S:Smooth curve
  x2 y2 x3 y3 # 绝对坐标
    x, y = current_point
    x1 = x3 + (x3 - x2) if last_letter in 'csCS' else x
    y1 = y3 + (y3 - y2) if last_letter in 'csCS' else y

t:Relative quadratic curve end
  x3 y3 # 相对坐标
    #其余点的计算分多种情形
T:Quadratic curve end
  x3 y3 # 绝对坐标

v:Relative vertical line
  y # 相对坐标
V:Vertical line
  y # 绝对坐标

z Z:End of path
  zZ并无差别？
  出现=>polygon 闭合多边形
  缺失=>polyline

见下面『t』:可见 连续同一操作符可省略
  <path d="M -200 150 t 100 -50 50 100"/>
  <path d="M 0 150 t 100 -50 t 50 100"/>

-->
<g stroke="#00FF00" stroke-width="10" >
  <polyline points="0,0 0,200 " />
</g>

<g stroke="#0000FF" stroke-width="10" >
  <polyline points="0,0 100,0 " />
</g>

<g stroke="red" stroke-width="3" fill="yellow" >
  <path d="M -200 -200 h 50 v 100 l -25 50  "/>
  <path d="M -100 -200 h 50 v 100 l -25 50 z "/>
  <path d="M 0 -200 h 50 v 100 l -25 50 Z "/>

  <path d="M -200 0 a 25 50 45 1 1 50 100"/>
  <path d="M -100 0 c 25 -25 100 -50 50 100"/>
  <path d="M 0 0 q 100 -50 50 100"/>
  <path d="M 100 0 s 100 -50 50 100"/>
  <path d="M -200 150 t 100 -50 50 100"/>
  <path d="M 0 150 t 100 -50 t 50 100"/>

</g>
</svg>


]]
[[
尝试五:组件
e /sdcard/0my_files/tmp/graph/svg/trial_4.svg

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
width="800"
height="1600"
viewBox="-400 -400 800 800"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    >
<!-- 尝试:组件 -->
<!--
"id" 作为 组件名
use: 不支持 scale rotate
  transform="matrix(1,2,3,4,5,6)"
  恒等变换？transform="matrix(1,0,0,1,0,0)"
    ??? [a,b;c,d]*[x;y] + [e;f]
    但是 坐标变换 很难预料 跑到哪里去
    !! 先 矩阵外部偏移，再 旋转缩放，最后 矩阵内部偏移
    => 矩阵外部偏移 xy 应当将 原组件中心 摆到 原点，矩阵内部偏移 将 靶组件 摆到 目的地
transform="matrix(a,b,c,d,e,f)"
点坐标:[x;y;1]
线性变换矩阵:[a,b,e;c,d,f;0,0,1]
-->
<defs>
  <path id="path_1__rect" stroke-width="1" d="M 0 0 h 100 v 100 h -100 z"/>
  <symbol id="component_1" overflow="visible" >
    <path stroke="green" stroke-width="10" fill="blue"  d="M -50 0 a 50 50   0 0 1   100 0 z"/>
    <path stroke="orange" stroke-width="10" fill="grey"  d="M -50 10 l 50 50   50 -50 z"/>
  </symbol>
</defs>
<g stroke="#00FF00" stroke-width="10" >
  <polyline points="0,0 0,200 " />
</g>

<g stroke="#0000FF" stroke-width="10" >
  <polyline points="0,0 100,0 " />
</g>

<g stroke="red" stroke-width="3" fill="yellow" >
  <use x="-300" y="-300" xlink:href="#path_1__rect"/>
  <use x="100" y="-300" xlink:href="#path_1__rect"/>
  <use x="100" y="100" xlink:href="#path_1__rect"/>
  <use x="-300" y="100" xlink:href="#component_1"/>
  <use x="-200" y="0" transform="matrix(1,0,0,1,0,0)" xlink:href="#component_1"/>
  <use x="-100" y="-100" transform="matrix(2,0,0,2,100,100)" xlink:href="#component_1"/>
  <use x="-100" y="100" transform="matrix(0,1,1,0,0,0)" xlink:href="#component_1"/>
  <use x="0" y="0" transform="matrix(0,0.5,2,0,-100,100)" xlink:href="#component_1"/>

</g>
</svg>



]]
[[
片段:标题丶描述
<title>Qt SVG Document</title>
<desc>Generated with Qt</desc>
<defs>
... ...
</defs>
... ...
]]
[[
尝试六:裁剪显示区
e /sdcard/0my_files/tmp/graph/svg/trial_5.svg

<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
width="800"
height="1600"
viewBox="-400 -400 800 800"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    >
<title>尝试:裁剪显示区</title>
<desc>
裁剪显示区 只需 抽象线条位置信息，无需其他 颜色、线宽 等 信息
</desc>
<defs>
  <clipPath id="clipped_view_area_1">
    <path fill="none" stroke="none" stroke-width="1000" d="M 0 0 h 100 v 100 h -100 "/>
  </clipPath>
  <clipPath id="clipped_view_area_2">
    <path fill="#000000" stroke="#000000" stroke-width="1000" d="M -100 0 h 100 v 100 h -100 "/>
  </clipPath>
  <clipPath id="clipped_view_area_3">
    <path d="M -200 0 h 100 v 100 h -100 "/>
  </clipPath>
</defs>
<g stroke="#00FF00" stroke-width="10" >
  <polyline points="0,0 0,200 " />
</g>

<g stroke="#0000FF" stroke-width="10" >
  <polyline points="0,0 100,0 " />
</g>

<g stroke="red" stroke-width="3" fill="yellow" >
  <g clip-path="url(#clipped_view_area_1)" clip-rule="nonzero">
    <path stroke="orange" stroke-width="10" fill="grey"  d="M 25 -25 h 50 v 200 h -50 z"/>
  </g>
  <g clip-path="url(#clipped_view_area_2)" clip-rule="nonzero">
    <path stroke="orange" stroke-width="10" fill="grey"  d="M -75 -25 h 50 v 200 h -50 z"/>
  </g>
  <g clip-path="url(#clipped_view_area_3)" clip-rule="nonzero">
    <path stroke="orange" stroke-width="10" fill="grey"  d="M -175 -25 h 50 v 200 h -50 z"/>
  </g>


</g>
</svg>


]]
[[
猜测:有相当把握:线性变换矩阵
transform="scale(1 -1)"
transform="scale(.5)"
transform="matrix(1,0,0,1,0,0)"

transform="matrix(a,b,c,d,e,f)"
点坐标:[x;y;1]
线性变换矩阵:[a,b,e;c,d,f;0,0,1]

]]

