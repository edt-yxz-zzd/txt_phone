e others/app/termux/grep/grep-regex-pattern-README.txt

view others/app/termux/grep/example4grep.txt
    grep_G_E_P__supports:goto
      各种特殊符合用法

view others/app/termux/grep/grep-regex-pattern-fmt.txt
    C++.regexp.grep...

view others/app/termux/grep/man_grep__4regex.txt
    -F  字符串
    -G  基本正则表达式
    -E  扩展正则表达式
    -P  Perl正则表达式
    "basic" (BRE), "extended" (ERE) and "perl" (PCRE).
        Perl-compatible regular expressions give additional functionality, and are documented in pcresyntax(3) and pcrepattern(3), but work only if PCRE is available in the system.
    Basic vs Extended Regular Expressions
        In basic regular expressions the meta-characters ?, +, {, |, (, and ) lose their special meaning; instead use the backslashed versions \?, \+, \{, \|, \(, and \).

view others/app/termux/help/grep.man.BREvsERE.txt
  对比:BRE vs ERE
  语法功能9部件:
[[
BRE vs ERE:语法不同:
  meta-characters:
    BRE:basic regular expression: \?, \+, \{, \|, \(, \)
    ERE:extended regular expression: ?, +, {, |, (, )

  GNU => [BRE =[功能]= ERE]
    In GNU grep there is no difference in available functionality between basic and extended syntaxes.

===
正则表达式的部件:
1. single_char:digit,letter,『.』,『\{<meta-character>}』
2. Bracket:『[...]』『[^...]』『[...{<char>}-{<char>}...]』『[...[:{<nm4cls>}:]...]』[# 补偿:[ #]『[]...^...-]』[#某些特殊字符的平凡化#]
  [:alnum:], [:alpha:], [:blank:], [:cntrl:], [:digit:], [:graph:], [:lower:], [:print:], [:punct:], [:space:], [:upper:], [:xdigit:]
3. Anchoring:『^』行首，『$』行尾，『\<』词首，『\>』词尾，『\b』词端，『\B』非词端
4. Backslash:『\w』==『[_[:alnum:]]』，『\w』==『[^_[:alnum:]]』
5. Repetition:『?』『*』『+』『{n}』『{,m}』『{n,}』『{n,m}』 #但BRE: \?, \+, \{
6. Concatenation
7. Alternation:『|』 #但BRE: \|
8. Back-reference:『\n』
9. Subexpression: 『(...)』 #但BRE: \(, \)
]]



[[
man pcresyntax
  语法 概述
man pcrepattern
  语法+语义 细节
man pcrematching
  匹配算法
man -c pcresyntax | col -b -x > others/app/termux/grep/grep-perl-regexp.man-pcresyntax.txt
man -c pcrepattern | col -b -x > others/app/termux/grep/grep-perl-regexp.man-pcrepattern.txt
man -c pcrematching | col -b -x > others/app/termux/grep/grep-perl-regexp.man-pcrematching.txt

view others/app/termux/grep/grep-perl-regexp.man-pcresyntax.txt
view others/app/termux/grep/grep-perl-regexp.man-pcrepattern.txt
view others/app/termux/grep/grep-perl-regexp.man-pcrematching.txt

]]




