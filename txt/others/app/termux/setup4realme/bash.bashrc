


#e /sdcard/0my_files/git_repos/txt_phone/txt/others/app/termux/setup4realme/bash.bashrc
#   snippet from: view /sdcard/0my_files/git_repos/txt_phone/txt/others/app/termux/apt_pkg.txt
#
#vim ~/../usr/etc/bash.bashrc
#xxx NOT cp ?? ~/../usr/etc/bash.bashrc
#cat /sdcard/0my_files/git_repos/txt_phone/txt/others/app/termux/setup4realme/bash.bashrc >> ~/../usr/etc/bash.bashrc
#vim $etc_sh
#   append
alias py=python
export PYTHONPATH="/sdcard/0my_files/unzip/python3_src-master:$PYTHONPATH"


export my_home="/sdcard/0my_files/"
export my_tmp="/sdcard/0my_files/tmp/"
export my_repos="$my_home/git_repos/"
export my_git_txt="$my_repos/txt_phone/"
export my_git_py="$my_repos/python3_src/"

export my_txt="$my_git_txt/txt/"


export my_git_sh="$my_git_py/bash_script/"
#PREFIX=/data/data/com.termux/files/usr
export my_sh="$PREFIX/bin/my_sh/"
export PATH="$my_sh:$PATH"
export PYTHONPATH="$my_git_py:$PYTHONPATH"
echo $PATH
echo $PYTHONPATH

#bug: export etc="~/../usr/etc/"
#export etc=~/../usr/etc/
export etc="$PREFIX/etc/"
export etc_sh="$etc/bash.bashrc"


cd $my_tmp/
cd $my_git_sh/
cd $my_sh/
cd $my_txt/


