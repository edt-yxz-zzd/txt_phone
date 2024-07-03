e others/app/termux/help/README.txt
view ../../python3_src/bash_script/app/man__save_to_file
view ../../python3_src/bash_script/app/help__save_to_file


[[what is "quote"??
    # /sdcard/0my_files//git_repos//python3_src//bash_script//app/h: line 22: quote: command not found
but usable shell! why?
  [[
$ a=' x z'
$ echo   "$a"
 x z
$ echo   '$a'
$a
$ quote
''$ quote $a
'x'$ quote   "$a"
' x z'$ help quote
bash: help: no help topics match `quote'.  Try `help help' or `man -k quote' or `info quote'.
$ man quote
man: No entry for quote in the manual.
$ quote  --help
'--help'$ info quote
info: No menu item 'quote' in node '(dir)Top'
$ which quote
$ set quote
$ export quote
$ quote $a
'x'$ quote   "$a"
' x z'$
  ]]

『quote』is local name:
$ declare -f quote
quote ()
{
    local quoted=${1//\'/\'\\\'\'};
    printf "'%s'" "$quoted"
}
$ declare -f _quote_readline_by_ref
quote_readline ()
{
    local ret;
    _quote_readline_by_ref "$1" ret;
    printf %s "$ret"
}
dequote ()
{
    eval printf %s "$1" 2> /dev/null
}
_quote_readline_by_ref ()
{
    if [[ $1 == \'* ]]; then
        printf -v $2 %s "${1:1}";
    else
        printf -v $2 %q "$1";
    fi;
    [[ ${!2} == \$* ]] && eval $2=${!2}
}

]]


man set
  --> tcl::set
    !!!not env!!!
    set - Read and write variables
info set
  --> tcl::set
    !!!not env!!!
    set - Read and write variables
help set
  --> bash::set
    !!!not env!!!
    Set or unset values of shell options and positional parameters.
man export
  --> '' #fail
    man: No entry for export in the manual.
info export
  --> '' #fail
    info: No menu item 'export' in node '(dir)Top'
help export
  --> bash::export
    !!!env!!!
    Set export attribute for shell variables.
help declare


view ../../python3_src/bash_script/app/man__save_to_file
view ../../python3_src/bash_script/app/help__save_to_file

[[hexdump:
man__save_to_file hexdump
help__save_to_file hexdump
    man -c hexdump | col -b -x > others/app/termux/help/hexdump.man.txt
    hexdump --help > others/app/termux/help/hexdump.help.txt
e others/app/termux/help/hexdump.example.txt

view others/app/termux/help/hexdump.man.txt
view others/app/termux/help/hexdump.help.txt
view others/app/termux/help/hexdump.example.txt
]]
[[bash:
man__save_to_file bash
help__save_to_file bash
    man -c bash | col -b -x > others/app/termux/help/bash.man.txt
    bash --help > others/app/termux/help/bash.help.txt
e others/app/termux/help/bash.example.txt

view others/app/termux/help/bash.man.txt
view others/app/termux/help/bash.help.txt
##view others/app/termux/help/bash.example.txt


/^\S
/^   \S
grep '^ \? \? \?\S' others/app/termux/help/bash.man.txt > others/app/termux/help/bash.man.outlines.txt
view others/app/termux/help/bash.man.outlines.txt
[some:
DEFINITIONS
RESERVED WORDS
SHELL GRAMMAR
COMMENTS
QUOTING
PARAMETERS
EXPANSION
]

metacharacter
  A character that, when unquoted, separates words.  One of the following:
      |  & ; ( ) < > space tab newline
control operator
  A token that performs a control function.  It is one of the following symbols:
      || & && ; ;; ;& ;;& ( ) | |& <newline>

RESERVED WORDS
   Reserved words are words that have a special meaning to the shell.
   The following words are recognized as reserved
      when unquoted and
          either the first word of a command (see SHELL GRAMMAR below)
          , the third word of a case or select command (only in is valid)
          , or the third word of a for command (only in and do are valid):

       ! case  coproc  do done elif else esac fi for function if in select then until while { } time [[ ]]


if which which ; then { echo ok ; } else { echo bad ; } fi ;
if which xxxxx ; then { echo ok ; } else { echo bad ; } fi ;



exe, *args == "$0" "$1" ...
len(args) == $#
return/exit_status == $?

『$1』在命令中可能是多个词
『"$1"』在命令中是单个词
『$@』:= $1 $2 ...
『"$@"』:= "$1" "$2" ...
xxx 『$*』:= $1 $2 ...
xxx 『"$*"』:= "$1" "$2" ...
$ args "$*"
['.../args.py', '']
$ args "$@"
['.../args.py']

bash -c 'args "$@" ; args "$*" ; args "$0" ;' xxx 'y "y' -333 -ab
  [[
['.../args.py', 'y "y', '-333', '-ab']
['.../args.py', 'y "y -333 -ab']
['.../args.py', 'xxx']
  ]]

bash -c 'echo "$@" ; echo "$*" ; echo "$0" ;' xxx yyy -333 -ab
[[
yyy -333 -ab
yyy -333 -ab
xxx
]]
bash -c 'echo "$-" ; echo "$$" ; echo '"\'"'"$!"'"\'"' ;' xxx yyy -333 -ab
[[
hBc
9746
''
]]
py -m nn_ns.app.args 'echo "$-" ; echo "$$" ; echo '"\'"'"$!"'"\'"' ;' xxx yyy -333 -ab
xxx py -m nn_ns.app.args "$1" 'echo "$-" ; echo "$$" ; echo '"'"'"$!"'"'"' ;' xxx yyy -333 -ab

help shift
a1="$1"
a2="$2"
if ! shift 2 ; then { echo bad >&2 ; exit 1 ; } ; fi
  #输入不足2个


help if
  if: if COMMANDS; then COMMANDS; [ elif COMMANDS; then COMMANDS; ]... [ else COMMANDS; ] fi

help for
  for: for NAME [in WORDS ... ] ; do COMMANDS; done

bash -c 'for x ; do echo $x ; done;' xxx yyy -333 -ab
  [[
yyy
-333
-ab
  ]]

]]

add:script.sh:
  e ../../python3_src/bash_script/app/h
  [[
quote ()
{
    local quoted=${1//\'/\'\\\'\'};
    printf "'%s'" "$quoted"
} ;


for nm ; do {
    if which "$nm" ; then {
        if man -c "$nm" | col -b -x > others/app/termux/help/"$nm".man.txt ; then {
            echo ok: man -c "$nm" ;
            grep '^ \? \? \?\S' others/app/termux/help/"$nm".man.txt > others/app/termux/help/"$nm".man.outlines.txt ;
        } else {
            echo fail: man -c "$nm" ;
        } fi ;

        #bug:if "$nm" --help 2>&1  1>others/app/termux/help/"$nm".help.txt ; then {
        #   as-if: fs[2] := fs[1]; f[1] := fs[?]
        #   xxx as-if: (fs[2], fs[1]) := (f[1], fs[?])
        if "$nm" --help  1>others/app/termux/help/"$nm".help.txt   2>&1 ; then {
            echo ok: "$nm" --help ;
        } else {
            echo fail: "$nm" --help ;
        } fi ;
    } else {
        #py -m nn_ns.app.args "$nm"
        #   use 『"$nm"』 instead of 『$nm』
        #echo not found:  \'"$nm"\' ;
        echo not found:  $(quote "$nm") ;
        # /sdcard/0my_files//git_repos//python3_src//bash_script//app/h: line 22: quote: command not found
    } fi ;
} done ;

  ]]



