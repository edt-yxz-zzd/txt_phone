
e others/app/termux/help/README-cmds.txt
[[
每行宽度调整至1000
  view others/app/termux/help/mandoc.man.txt
  view others/app/termux/help/cmd_intro.README.txt
  ... | mandoc -c -T utf8 -O indent=1 -O width=1000 | col -b -x | head -n 20
  ==>>:
  man -c -T utf8 -O indent=1 -O width=1000    bash    | col -b -x | head -n 20
  man -c -T utf8 -O indent=1 -O width=1000    bash    | col -b -x > others/app/termux/help/bash.man.width-1000.txt
    见下面:更新版牜缩进减半
view others/app/termux/help/bash.man.width-1000.txt
  最大缩进30空格
grep '^  *' others/app/termux/help/bash.man.width-1000.txt -o | sort -u | sed 's/ /+/g' | sed 's/++/-_/g' | sed 's/-_-/#_-/g'
  -_+
  #_-_-_+
  #_-_#_-_
  #_-_#_-_#_-_
  #_-_#_-_#_-_-_
  #_-_#_-_#_-_-_+
  #_-_#_-_#_-_#_-_+
  #_-_#_-_#_-_#_-_#_-_+
  #_-_#_-_#_-_#_-_#_-_-_
  #_-_#_-_#_-_#_-_#_-_#_-_#_-_-_
  123456789012345678901234567890
grep '^  *' others/app/termux/help/bash.man.width-1000.txt -o | sort -u | sed 's/ /+/g' | sed 's/++/-_/g' | sed 's/-_-/#_-/g' | gawk -- '{ print length($0) }'
  3
  7
  8
  12
  14
  15
  17
  21
  22
  30

^\( \{1,}\)\S.*\n\+\(\1 \{1,3}\)\S
  找不到，至少缩进4空格
3:2
7:4
8:4
12:6
14:6
15:8
17:8
21:10
22:10
30:12

:s/^\(  *\)\1/\1
echo 'a       b' | sed 's/a\(  *\)\1/a\1/'
  a    b
echo 'a       b' | sed 's/ \{4,\}/  /g'
  a  b

更新版牜缩进减半:
  man -c -T utf8 -O indent=1 -O width=1000    bash    | col -b -x | sed 's/^\(  *\)\1/\1/' | sed 's/ \{30,\}/                             /g' > others/app/termux/help/bash.man.width-1000.txt
发现:有误:『Theextglob』
发现:这是2022年版 比 之前2020年多了些内容
view others/app/termux/help/bash.man.txt
  2020年版
view others/app/termux/help/bash.man.width-1000.txt
  2022年版; 行宽1000字符 #更多内容


view others/app/termux/help/bash.man.outlines.txt
view others/app/termux/help/bash.man.width-1000.outlines.txt
xxx:grep -n -T -E -- '^ *[A-Z0-9]\w*( [A-Z0-9]\w*)*$' others/app/termux/help/bash.man.width-1000.txt | head
nl -d '' -p -b a -h a -f a -i 1 -l 1 -n rz -s : -w 4 -v 1  others/app/termux/help/bash.man.width-1000.txt | grep -E -- $'^ *[0-9]+: *[A-Z0-9]\w*( [A-Z0-9]\w*)*$' > others/app/termux/help/bash.man.width-1000.outlines.txt


e others/app/termux/help/sed-workflow.txt
e others/app/termux/help/文本处理-grep-sed-gawk.txt

]]
[[
提取大纲
view others/app/termux/help/bash.man.outlines.txt
view others/app/termux/help/gawk.man.txt
grep -E '^ *[A-Z0-9]\w*( [A-Z0-9]\w*)*$' others/app/termux/help/gawk.man.txt > others/app/termux/help/gawk.man.outlines.txt
view others/app/termux/help/gawk.man.outlines.txt
some:
   Arrays
   Namespaces
   Variable Typing And Conversion

e others/app/termux/help/awk-see-gawk.txt
]]



