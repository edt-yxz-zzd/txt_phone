" e others/app/termux/setup4realme/vim.vimrc
"
"
" ===@termux:
"   cp /sdcard/0my_files/git_repos/txt_phone/txt/others/app/termux/setup4realme/vim.vimrc ~/.vimrc
" ===@droidvim:
"   :!cp /sdcard/0my_files/git_repos/txt_phone/txt/others/app/termux/setup4realme/vim.vimrc ~/.vimrc
"
"
"
" vim 2个 配置
"     ===
"     view /sdcard/0my_files/git_repos/txt_phone/txt/others/app/gvim/droidvim.txt
"     ===@droidvim:
"     call ATETermVimVimrc()
"     <==>
"     e ~/.vimrc
"     ===@termux:
"     vim ~/.vimrc
"
"
"
"

set history=1000

set hlsearch
set list
set listchars=tab:>-,trail:~,eol:$,extends:@,precedes:*,nbsp:%

filetype plugin indent on
set ts=2 sw=2
set tabstop=2      " show hard-tab
set shiftwidth=2   " indent by ">"
set softtabstop=0  " Number of spaces a <Tab> counts for. When 0, featuer is off
set noexpandtab
set et ts=4 sw=4 sts=4 " override above
" set expandtab tabstop=4 shiftwidth=4 softtabstop=4
set smarttab
set autoindent

set wrap               " soft-wrap lines
" If you like line numbers, you may want this instead:
set number
set showbreak=------>\  " line up soft-wrap prefix with the line numbers
set cpoptions+=n        " start soft-wrap lines (and any prefix) in the line-number area










""""
scriptencoding utf-8
" DroidVim default settings

set fileformats=unix,dos,mac

set hidden
set nowritebackup
set nobackup

set virtualedit=block
set whichwrap=b,s,[,],<,>

set autoindent
"set smartindent
set ignorecase
set smartcase
set formatoptions+=mMj

set noerrorbells
set novisualbell
set visualbell t_vb=
set number
set noshowcmd
set notitle
" We recommend to display tab and trailing whitespace.
" set list
" set listchars=tab:^\ ,trail:~
set omnifunc=syntaxcomplete#Complete

set mouse=a

" ================
" Appendix
" ================
" Help:
" Type `K` to see the help for the option under the cursor. (`:q` to close help)
"
" Text Input Mode:
" (Especially important for non-English languages.)
" If you want to use a language other than English in Insert mode, please refer to the "DroidVim help" -> "Text input mode".
"
" Colorscheme:
" You can use a 256 terminal color scheme (E.g. term256).
" :colorscheme term256

" INTERNAL_STORAGE:
" You can access internal storage with $INTERNAL_STORAGE.
" (e.g.) :cd $INTERNAL_STORAGE
" * If you are using Android 6 or later, restart this application after granting the storage access permission.
" * If you are using Android 10 or later, it is "Private Storage Area".
"
" Startup:
" When you start Vim, you may want to always edit the file in a specific directory.
" In that case, add the following to .vimrc
"   cd $INTERNAL_STORAGE/path/to/directory
"
" Vimfiles:
" Files in the home directory ($HOME) will be deleted during uninstallation.
" So we recommended that create `.vimrc` and `vimfiles (.vim)` in internal storage. (It can be accessed with filer app)
"
" If you created `.vimrc` or `vimfiles (.vim)` in internal storage, create a symbolic link with the following command via Vim
"  1. :cd $HOME
"  2. :!rm .vimrc
"     (Delete $HOME/.vimrc)
"  3. :!ln -s $INTERNAL_STORAGE/path/to/.vimrc .vimrc
"  4. :!rm -rf .vim
"     (Delete $HOME/.vim)
"  5. :!ln -s $INTERNAL_STORAGE/path/to/.vim .vim


set ts=2 sw=2
