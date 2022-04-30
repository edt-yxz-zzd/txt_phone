r'''[[[[[
e script/20220427_fix_termux.py
py script/20220427_fix_termux.py

[[
ok:cd,pwd,diff
alias rm="py -m nn_ns.app.rm"
alias cp="py -m nn_ns.app.cp"
alias mv="py -m nn_ns.app.mv"
alias ls="py -m nn_ns.app.ls"
alias cat="py -m nn_ns.app.cat"
]]


[[[
termux-repositories-legacy-24.12.2019.tar
https://pt.osdn.net/projects/termux-old/storage/termux-packages/

Archive of Termux’s packages for Android 5/6
  https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar

Archive of apps, packages and sources compatible with Android 5:
  https://archive.org/details/termux-repositories-legacy
https://pt.osdn.net/projects/termux-old/storage/termux-packages/dists/stable/
https://pt.osdn.net/projects/termux-old/storage/termux-packages/dists/stable/main/binary-arm/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/Release
  <-- 跳转自 https://pt.osdn.net/projects/termux-old/storage/termux-packages/ 下的文件列表中的『Release』
  https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/
    似乎可以用来替换 https://packages-cf.termux.org/apt/termux-main
      因为同样有文件夹『dists/』
        确实行，不过本地动态链接库一致性已遭到破坏，apt/dpkg无法正常工作(rm失败)，需要手动修复。
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/
[ ]	Packages.xz	2022-03-13 00:31 	80K	 
[ ]	libandroid-glob-static_0.6-1_arm.deb	2022-03-13 00:52 	4.3K	 
[ ]	libandroid-glob_0.6-1_arm.deb	2022-03-13 00:52 	6.5K	 
[ ]	libandroid-shmem-static_0.2.1-1_arm.deb	2022-03-13 00:52 	5.4K	 
[ ]	libandroid-shmem_0.2.1-1_arm.deb	2022-03-13 00:52 	8.7K	 
[ ]	libandroid-support-static_24-6_arm.deb	2022-03-13 00:52 	103K	 
[ ]	libandroid-support_24-6_arm.deb	2022-03-13 00:52 	102K	 

cd /sdcard/Download/
wget https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/ -o binary-arm.html
file:///sdcard/Download/binary-arm.html
file:///sdcard/Download/index.html
    重命名 --> file:///sdcard/Download/binary-arm-index.html
  下载全部？
下载 https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/Packages.xz
解压 /sdcard/Download/Packages.xz
view /sdcard/Download/Packages/Packages
下载 https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/binutils_2.33.1-1_arm.deb
dpkg -I /sdcard/Download/binutils_2.33.1-1_arm.deb
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x18a
  搜libandroid-support.so
  install old version: dpkg -i ./libandroid-support_22-1_arm.deb; restart the app; And then avoid apt upgrade for a while (or use apt-mark hold libandroid-support) 
dpkg -I /sdcard/Download/libandroid-support_24-6_arm.deb
    Pre-Depends: dpkg (>= 1.19.4-3)
    Essential: yes
$ dpkg --version
    Debian 'dpkg' package management program version 1.19.7 (arm).

dpkg-deb -c /sdcard/Download/libandroid-support_24-6_arm.deb
./data/data/com.termux/files/usr/lib/libandroid-support.so
./data/data/com.termux/files/usr/share/doc/libandroid-support/LICENSE -> ../../LICENSES/Apache-2.0.txt
view /data/data/com.termux/files/usr/share/doc/libandroid-support/
cp /data/data/com.termux/files/usr/lib/libandroid-support.so '/data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427]'
    fail to exec
    e script/20220427_fix_termux.py
py $my_txt/script/20220427_fix_termux.py 'cp("/data/data/com.termux/files/usr/lib/libandroid-support.so", "/data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427]")'
du '/data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427]'
    fail to exec
diff /data/data/com.termux/files/usr/lib/libandroid-support.so '/data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427]'
    ok
py $my_txt/script/20220427_fix_termux.py 'cp("/data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427]", "/data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427]another")'
apt install  /sdcard/Download/libandroid-support_24-6_arm.deb
    fail to exec
    ?
unzip termux.apk --> libandroid-support.so
  view /sdcard/0my_files/unzip/apk/termux/
  view /sdcard/0my_files/unzip/apk/termux/lib/armeabi-v7a/libtermux.so
  diff -q /data/data/com.termux/files/usr/lib/libandroid-support.so /sdcard/0my_files/unzip/apk/termux/lib/armeabi-v7a/libtermux.so
    Files /data/data/com.termux/files/usr/lib/libandroid-support.so and /sdcard/0my_files/unzip/apk/termux/lib/armeabi-v7a/libtermux.so differ
  diff -q /data/data/com.termux/files/usr/lib/libtermux.so /sdcard/0my_files/unzip/apk/termux/lib/armeabi-v7a/libtermux.so
    diff: /data/data/com.termux/files/usr/lib/libtermux.so: No such file or directory
  cd /data/data/com.termux/
  find . -name 'libtermux.so'
    ??没找到？但确实有！
  diff -q /data/data/com.termux/lib/libtermux.so /sdcard/0my_files/unzip/apk/termux/lib/armeabi-v7a/libtermux.so
    相同！从未更新过！
  ls /data/data/com.termux/files/usr/lib/
  apt install /sdcard/Download/libandroid-support_24-6_arm.deb
    fail to exec
    E: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
  dpkg-deb --extract /sdcard/Download/libandroid-support_24-6_arm.deb /sdcard/Download/libandroid-support_24-6_arm/
    [[
    tar: .: Cannot utime: Operation not permitted
    tar: .: Cannot change mode to rwxr-xr-x: Operation not permitted
    tar: Exiting with failure status due to previous errors
    dpkg-deb: error: tar subprocess returned error exit status 2
    ]]
  dpkg-deb --extract /sdcard/Download/libandroid-support_24-6_arm.deb ~/1tmp/libandroid-support_24-6_arm/
    ok!
  tree ~/1tmp/libandroid-support_24-6_arm/
  cp ~/1tmp/libandroid-support_24-6_arm/data/data/com.termux/files/usr/lib/libandroid-support.so /data/data/com.termux/files/usr/lib/libandroid-support.so[24-6_arm][from_www_tw]
  cp /data/data/com.termux/files/usr/lib/libandroid-support.so[24-6_arm][from_www_tw] /data/data/com.termux/files/usr/lib/libandroid-support.so
    !!!修改系统!!!
  diff -q /data/data/com.termux/files/usr/lib/libandroid-support.so /data/data/com.termux/files/usr/lib/libandroid-support.so[24-6_arm][from_www_tw]
    相同
  diff -q /data/data/com.termux/files/usr/lib/libandroid-support.so /data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427]
    Files /data/data/com.termux/files/usr/lib/libandroid-support.so and /data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427] differ
    [[
    $ ls
    WARNING: linker: ls: unused DT entry: type 0x1d arg 0xc5b
    WARNING: linker: /data/data/com.termux/files/usr/lib/libgmp.so: unused DT entry: type 0x1d arg 0x2900
    CANNOT LINK EXECUTABLE: cannot locate symbol "__fwrite_chk" referenced by "ls"...
    page record for 0xb6e3e00c was not found (block_size=64)
    ]]

dpkg -I /sdcard/Download/binutils_2.33.1-1_arm.deb
    Depends: libc++, zlib

download all from:
    view /sdcard/Download/binary-arm-index.html
      下载全部？
    view /sdcard/Download/binary-arm-index.html.txt
    view /sdcard/Download/binary-arm-index.html.ls-3.txt
    view /sdcard/Download/binary-arm-index.html.ls-1.txt
        https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/*
    view /sdcard/Download/binary-arm-index.html.urls.txt

    main4calc_total_size('/sdcard/Download/binary-arm-index.html.ls-3.txt')
        --> 1.111G
        可以下载全部！
        892个文件，890个deb+Packages(所有库的信息)+Packages.xz(Packages的压缩包)
        下载完，还要下载 Release/InRelease
        /dists/stable/Release
        /dists/stable/InRelease
        /dists/stable/main/binary-arm/index.html
        /dists/stable/main/binary-arm/* #892
        其他？
            自己当服务器？TODO
                deb https://127.0.0.0/localhost/.../dists

    mkdir /sdcard/Download/curl-deb4termux/
    cd /sdcard/Download/curl-deb4termux/
    ###xargs -n 1 curl -O < urls-to-download.txt
    xargs -n 1 curl -O < /sdcard/Download/downs4termux/binary-arm-index.html.urls.txt
        !!!下载全部!!!
        重新开始继续下载 要修改 urls.txt!!!避免重复下载
        ===
        暂时将许多之前此次下载新建的文件 从『/sdcard/Download/』移至『/sdcard/Download/downs4termux/』
            view /sdcard/Download/downs4termux/Packages/Packages
        将deb尽快移至『/mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/』
            view /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/
            view /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/all-deb_pkgs4termux/
            view /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/
            TODO

    alias ls="py -m nn_ns.app.ls"
    ls /sdcard/Download/curl-deb4termux/
        golang-doc_2:1.13.3-1_arm.deb
        golang_2:1.13.3-1_arm.deb
        mariadb-static_1:10.4.6-1_arm.deb
        mariadb_1:10.4.6-1_arm.deb
        #名字含『:』，文件管理器 移动不了
        #更名『:』-->『--』，再用 文件管理器 移动
    使用SManager:
        cd /sdcard/Download/curl-deb4termux/
        cp golang-doc_2:1.13.3-1_arm.deb       golang-doc_2--1.13.3-1_arm.deb
        cp golang_2:1.13.3-1_arm.deb           golang_2--1.13.3-1_arm.deb
        cp mariadb-static_1:10.4.6-1_arm.deb   mariadb-static_1--10.4.6-1_arm.deb
        cp mariadb_1:10.4.6-1_arm.deb          mariadb_1--10.4.6-1_arm.deb

DOING:
    e /sdcard/Download/downs4termux/other-urls.txt
        main4calc_total_size('/sdcard/Download/downs4termux/binary-all-index.html.ls-3.txt')
            --> 949M

    dpkg-deb --extract /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/coreutils_8.31-5_arm.deb ~/1tmp/coreutils_8.31-5_arm/
    tree ~/1tmp/coreutils_8.31-5_arm/

        可执行文件 主要两个，其余都是文档/箭头(软链接):
            /data/data/com.termux/files/home/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so
            /data/data/com.termux/files/home/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/bin/coreutils
    diff -q /data/data/com.termux/files/home/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/bin/coreutils  /data/data/com.termux/files/usr/bin/coreutils
        不同
    diff -q /data/data/com.termux/files/home/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so  /data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so
        不同
    #备份
    alias cp="py -m nn_ns.app.cp"
    cp ~/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so  /data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so[8.31-5_arm][from_www_tw]
    cp ~/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/bin/coreutils  /data/data/com.termux/files/usr/bin/coreutils[8.31-5_arm][from_www_tw]
    cp /data/data/com.termux/files/home/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/bin/coreutils  /data/data/com.termux/files/home/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/bin/coreutils[save20220427]
    cp /data/data/com.termux/files/home/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/bin/coreutils  /data/data/com.termux/files/home/1tmp/coreutils_8.31-5_arm/data/data/com.termux/files/usr/bin/coreutils[save20220427]another
    cp /data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so  /data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so[save20220427]
    cp /data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so  /data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so[save20220427]another
    ====
    !!!修改系统!!!
    cp /data/data/com.termux/files/usr/bin/coreutils[8.31-5_arm][from_www_tw] /data/data/com.termux/files/usr/bin/coreutils
    cp /data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so[8.31-5_arm][from_www_tw]  /data/data/com.termux/files/usr/libexec/coreutils/libstdbuf.so
        ls/cp恢复正常工作！
    ====

    TODO 等下载完bootstrap+science??


[[
view /sdcard/Download/downs4termux/binary-arm-index.html.ls-3.txt

\d\{3,}\(\.\d*\)\?M$
rust_1.38.0-4_arm.deb	2022-03-13 01:06 	188M

\d\{2,}\(\.\d*\)\?M$
dart_2.4.1-1_arm.deb	2022-03-13 00:36 	35M
emacs_26.3-2_arm.deb	2022-03-13 00:38 	33M
erlang_21.3.8-2_arm.deb	2022-03-13 00:39 	32M
geth-utils_1.9.6-1_arm.deb	2022-03-13 00:43 	25M
ghostscript_9.27-3_arm.deb	2022-03-13 00:43 	13M
gitea_1.9.5-1_arm.deb	2022-03-13 00:44 	23M
golang_2:1.13.3-1_arm.deb	2022-03-13 00:45 	50M
keybase_4.7.2-1_arm.deb	2022-03-13 00:51 	29M
ldc_1.18.0-6_arm.deb	2022-03-13 00:51 	18M
libllvm-static_9.0.0-1_arm.deb	2022-03-13 00:57 	31M
libllvm_9.0.0-1_arm.deb	2022-03-13 00:57 	24M
lldb_9.0.0-1_arm.deb	2022-03-13 00:59 	11M
lnd_0.8.2-beta-0_arm.deb	2022-03-13 01:00 	12M
mariadb_1:10.4.6-1_arm.deb	2022-03-13 01:00 	16M
mupdf-static_1.16.1-1_arm.deb	2022-03-13 01:01 	23M
mupdf-tools_1.16.1-1_arm.deb	2022-03-13 01:01 	39M
perl_5.30.0-2_arm.deb	2022-03-13 01:03 	13M


rust 188M
    Description: Systems programming language focused on safety, speed and concurrency
erlang 32M
    Description: General-purpose concurrent functional programming language
gitea 23M
    Description: Git with a cup of tea, painless self-hosted git service
keybase 29M
    Description: Key directory that maps social media identities to encryption keys

geth-utils 25M
    Description: Additional utilities for Geth (like abigen, bootnode, evm, puppeth)
    Depends: geth (= 1.9.6-1)
        geth
            Description: Go implementation of the Ethereum protocol

dart 35M
    Description: Dart is a general-purpose programming language

Package: python
    3.8 才8M？

]]
[[
view /sdcard/Download/downs4termux/Packages/Packages
    binutils
meaning Breaks Conflicts Depends Replaces Essential Recommends Suggests Pre-Depends

搜索『\<Package\>:.*dev』，只找到一个:
    Package: icu-devtools
coreutils #被apt/dpkg依赖，重装之？
    busybox #coreutils轻量子集#单文件
    chroot#没有此包#需要root？
        proot #拟chroot

Package: apt
Depends: coreutils, dpkg, findutils, gpgv, grep, libc++, libcurl, liblzma, sed, termux-licenses, zlib

Package: coreutils
Depends: libandroid-support, libiconv

Package: dpkg
Depends: bzip2, coreutils, diffutils, gzip, less, libbz2, liblzma, tar, xz-utils, zlib

Package: libc++
    没有依赖需求

Package: libiconv-static
Depends: libiconv (= 1.16-4)
Description: Static libraries for libiconv

Package: libiconv
Breaks: libandroid-support (<= 24), libiconv-dev, libandroid-support-dev
Replaces: libandroid-support (<= 24), libiconv-dev, libandroid-support-dev
Description: An implementation of iconv()
    没有依赖需求

Package: iconv
Depends: libiconv (= 1.16-4)
Description: Utility converting between different character encodings
    运行之，连控制台都推出了，问题很严重

libandroid-support 已经手动替换
    解决了 启动新对话时的警告
    但 ls/rm/... 依然有问题，看来还得手动安装coreutils, libandroid-support-static, ?? libiconv

Package: libandroid-support-static
Depends: libandroid-support (= 24-6)
Description: Static libraries for libandroid-support

Package: libandroid-support
Version: 24-6
Pre-Depends: dpkg (>= 1.19.4-3)
Essential: yes
Description: Library extending the Android C library (Bionic) for additional multibyte, locale and math support

]]

dpkg -I /sdcard/Download/
dpkg-deb -c /sdcard/Download/

https://linuxhint.com/manual_install_deb_package_cli_ubuntu/#:~:text=How%20to%20Manually%20Install%20a%20Deb%20Package%20Using,Install%20a%20Deb%20Package.%20...%207%20Conclusion.%20
[[
$ dpkg -I /path/to/file.deb
  show info+dependencies
$ dpkg-deb -c /path/to/file.deb
  show file+destination path
$ dpkg-deb --extract /path/to/file.deb
$ sudo dpkg -i /path/to/file.deb
  install without any dependencies
$ sudo apt -f install
  fix the unmet dependency issue
$ sudo apt install /path/to/file.deb
$ sudo apt install ./file.deb
  automatically install all the required dependencies
===

Debian
How to Manually Install a Deb Package Using Command Line in Ubuntu
2 years ago
by Nitesh Kumar
This article will list a few command line methods that can be used to install standalone “.deb” installers that are not available in official repositories of Ubuntu. Some other useful commands helpful for handling “.deb” packages will also be covered. So let’s jump in.

List All Dependencies of a Deb File


To view information about a “.deb” file and all of its dependencies, run the command below:

$ dpkg -I /path/to/file.deb

The example below shows information about persepolis download manager “.deb” file.

This command is specially useful if you want to check what is being installed beforehand.
List All Files That will be Installed From a Deb Package

To see all files that a “.deb” package will install on your system along with their destination paths, run the command below:
$ dpkg-deb -c /path/to/file.deb

The example below shows files that will be installed on the system if you manually install persepolis download manager “.deb” package. Note that Ubuntu’s apt package manager also lists included files but requires you to install the package first. However, this method doesn’t require you to install the “.deb” package and it is really useful if you want to analyze which file goes where.

Extract All Files from a Deb Package

Sometimes you may want to extract a deb package to check a piece of code or use some of its included files for debugging and other purposes. To extract all files from a deb package, you can run a command in following format:
$ dpkg-deb --extract /path/to/file.deb

Note that extracting files is not the same as installation of a deb package. You will just get extracted contents of a “.deb” package in a local folder.
Install a Deb File Using Dpkg

Dpkg is a package management utility for managing “.deb” (debian) packages. To install a “.deb” package using dpkg, run the command below:
$ sudo dpkg -i /path/to/file.deb

The above command will install the standalone deb package only, without any dependencies. To fix this, you will have to run a command to auto-install required dependencies. Otherwise your system may be left in a broken state. To fix the unmet dependency issue, run the command below:
$ sudo apt -f install
Install a Deb File Using Gdebi

Gdebi is a nice command line and graphical application solely dedicated for installing standalone “.deb” packages stored on your local drive. It automatically resolves dependencies as well, as long as they are available in official Ubuntu repositories (requires network connection).

To install gdebi in Ubuntu, run the command below:
$ sudo apt install gdebi

To install a “.deb” package using Gdebi, run the command below:
$ sudo gdebi /path/to/file.deb

Since gdebi will take care of installation of dependencies, you don’t have to manually run another command to fix broken packages. However, if you want to check if there are broken packages or not and fix them automatically, you can run the command mentioned above again:
$ sudo apt -f install
Using Apt to Install a Deb Package

You can also use Ubuntu’s default “apt” package manager to install standalone “.deb” files. To do so, run the following command:
$ sudo apt install /path/to/file.deb

If you launched terminal inside the directory of “.deb” file, run following command instead:
$ sudo apt install ./file.deb

Like gdebi, apt will automatically install all the required dependencies. To confirm, run the command below:
$ sudo apt -f install
Conclusion

These are a few commands you can use to install “.deb” files without using any graphical interface. They are useful if you are running and managing Ubuntu server edition or using Ubuntu without any desktop environment.
About the author
Nitesh Kumar

I am a freelancer software developer and content writer who loves Linux, open source software and the free software community.

Linux Hint LLC, editor@linuxhint.com
1210 Kelly Park Cir, Morgan Hill, CA 95037
An Elite CafeMedia Publisher
]]
]]]
#]]]]]'''





#shutil.copy2(src, dst, *, follow_symlinks=True)

#shutil.move(src, dst, copy_function=shutil.copy2)

#shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
#shutil.rmtree(path, ignore_errors=False, onerror=None)
#shutil.disk_usage(path)
#shutil.chown(path, user=None, group=None)
#shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None)




import sys
import shutil
from pathlib import Path
import math
def main():
    #print(dir(sys))
    [sf, *args] = sys.argv
    print(args)
    #my_txt
    if 0:
        main4calc_total_size('/sdcard/Download/downs4termux/binary-arm-index.html.ls-3.txt')
        # 1.1111050071194768G
    if 1:
        main4calc_total_size('/sdcard/Download/downs4termux/binary-all-index.html.ls-3.txt')
        #948.941668510437M
        #400多MB是texlive字体

def main4calc_total_size(ipath4ls3, /):
    total_sz = calc_total_size(ipath4ls3)
    print(ipath4ls3)
    print(sz_unit5sz(total_sz))
def calc_total_size(ipath4ls3, /):
    ipath4ls3 = Path(ipath4ls3)
    txt = ipath4ls3.read_text('ascii')
    fieldss = [line.split('\t') for line in txt.strip().split('\n')]
    acc = 0
    for nm, datetime, sz_unit in fieldss:
        sz_unit = sz_unit.strip()
        if '0' <= sz_unit[-1] <='9':
            sz_unit += 'B'
        sz = sz_unit2sz(sz_unit)
        acc += sz
    total_sz = acc
    return total_sz

unit2scale = dict(G=2**30, M=2**20, K=2**10, B=1)
def sz_unit5sz(sz, /):
    ps = sorted(unit2scale.items(), key=lambda x:x[1], reverse=True)
    for unit, scale in ps:
        if sz >= scale:
            break
    else:
        raise logic-err

    sz__float = sz/scale
    return f'{sz__float}{unit}'
def sz_unit2sz(sz_unit, /):
    unit = sz_unit[-1]
    scale = unit2scale[unit]
    sz__float = float(sz_unit[:-1])
    sz__float1000 = math.floor(sz__float*1000)
    sz = sz__float1000*scale//1000
    return sz


r'''
e others/app/termux/apt_update__fail/apt_update_fail__solved_ver2.txt
    <<==
        [[
        e /sdcard/Download/downs4termux/other-urls.txt
        e TODO.txt
        e others/app/termux/apt_pkg.txt
        e script/20220427_fix_termux.py
            本文件
        view others/app/termux/apt_update__fail/bug---apt_update_fail__solved_ver1---bug.txt
            e others/app/termux/apt_update_fail__solved.txt
            !mv others/app/termux/apt_update_fail__solved.txt    others/app/termux/apt_update__fail/bug---apt_update_fail__solved_ver1---bug.txt

        ]]


#'''

r'''
[[[[[@20220428
e /sdcard/Download/downs4termux/other-urls.txt
TODO:
  move to:
    e script/20220427_fix_termux.py

https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/

非平凡/非独子
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/Release
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/InRelease

https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-all/Packages

!mkdir -p /sdcard/Download/downs4termux/other4curl/termux-old/termux-packages/dists/stable/main/binary-arm/
!mkdir /sdcard/Download/downs4termux/other4curl/termux-old/termux-packages/dists/stable/main/binary-all/

cd /sdcard/Download/downs4termux/other4curl/
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/Release -o ./termux-old/termux-packages/dists/stable/Release
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/InRelease -o ./termux-old/termux-packages/dists/stable/InRelease
view /sdcard/Download/downs4termux/other4curl/termux-old/termux-packages/dists/stable/Release
  Architectures: all arm i686 aarch64 x86_64
view /sdcard/Download/downs4termux/other4curl/termux-old/termux-packages/dists/stable/InRelease

curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-all/Packages -o ./termux-old/termux-packages/dists/stable/main/binary-all/Packages
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-all/ -o ./termux-old/termux-packages/dists/stable/main/binary-all/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/Packages -o ./termux-old/termux-packages/dists/stable/main/binary-arm/Packages
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/ -o ./termux-old/termux-packages/dists/stable/main/binary-arm/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/ -o ./termux-old/termux-packages/dists/stable/main/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/ -o ./termux-old/termux-packages/dists/stable/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/ -o ./termux-old/termux-packages/dists/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/ -o ./termux-old/termux-packages/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/ -o ./termux-old/index.html


view /sdcard/Download/downs4termux/binary-arm-index.html.ls-3.txt
e /sdcard/Download/downs4termux/binary-all-index.html.txt
^\[ ]\t
%s///
\t $
%s///
w /sdcard/Download/downs4termux/binary-all-index.html.ls-3.txt
\t.*
%s///
w /sdcard/Download/downs4termux/binary-all-index.html.ls-1.txt

view /sdcard/Download/downs4termux/binary-all-index.html.txt
view /sdcard/Download/downs4termux/binary-all-index.html.ls-3.txt
view /sdcard/Download/downs4termux/binary-all-index.html.ls-1.txt
view /sdcard/Download/downs4termux/binary-all-index.html.urls.txt
  https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-all/

    !mkdir /sdcard/Download/curl-all-deb4termux/
    cd /sdcard/Download/curl-all-deb4termux/
    xargs -n 1 curl -O < /sdcard/Download/downs4termux/binary-all-index.html.urls.txt
      共99个文件
    ls /sdcard/Download/curl-all-deb4termux/
      ecj_1:4.6.2-1_all.deb
      改名『:』-->『--』
    使用SManager:
      cp /sdcard/Download/curl-all-deb4termux/ecj_1:4.6.2-1_all.deb /sdcard/Download/curl-all-deb4termux/ecj_1--4.6.2-1_all.deb


https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/bootstrap/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/game-packages-21/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/science-packages-21/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-root-packages-21/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/unstable-packages-21/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/x11-packages-21/
  TODO


]]]]@20220428
#'''



r'''
[[[[[@20220430
move from:
    e TODO.txt

pkg in unstable-repo

termux-upgrade-repo
$ termux-upgrade-repo
Checking Android version... This device is not running Android 7.0 or later.

mkdir /sdcard/0my_files/tmp/curl_/termux/
cd /sdcard/0my_files/tmp/curl_/termux/
curl  -Lf -O https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar
curl  --continue-at - -sSLf -O https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar
curl: (28) Failed to connect to archive.org port 443: Connection timed out




Failed to connect to +"archive.org"

[[ubuntu apt rollback
https://superuser.com/questions/38717/how-can-i-undo-or-rollback-an-apt-get-upgrade-command-on-ubuntu
  awk
  aptitude

    Log in
    Sign up

Super User
Sponsored by
Sponsored logo
How can I undo or rollback an "apt-get upgrade" command on Ubuntu?
Ask Question
Asked 12 years, 7 months ago
Modified 1 year, 3 months ago
Viewed 112k times
31

Is there a way in Ubuntu to rollback or undo the last upgrade after doing an apt-get upgrade if you don't like the results?
ubuntu
restore
package-management
aptitude
undo
Share
Improve this question
edited Jun 14, 2012 at 20:34
user avatar
slhck
211k6363 gold badges572572 silver badges566566 bronze badges
asked Sep 9, 2009 at 22:21
user avatar
jjclarkson
44311 gold badge44 silver badges66 bronze badges

    Not with out a lot of work, that wouldn't be worth it. Can you save your /home and start over? What didn't you like? – 
    user10547
    Sep 9, 2009 at 22:31
    I haven't done it yet, but this is a production server and I need to be sure there's no incompatibilities with our custom PHP/MySQL/Apache2 setup, and get back quickly if there is. I'd like to upgrade because I think it will fix another problem I'm having. – 
    jjclarkson
    Sep 9, 2009 at 22:45
    Unless you did dist-upgrade, I don't see what results there are not to like, since those are most likely security updates. – 
    LiraNuna
    Sep 9, 2009 at 22:48
    If you have a custom install, it's your responsibility to save patches and apply them against the current version. – 
    LiraNuna
    Sep 9, 2009 at 22:51
    2
    If it's a server, try a dev server before upgrading the production one – 
    solarc
    Oct 3, 2009 at 2:27

Show 2 more comments
12 Answers
Sorted by:
9

I had to do this today on my Debian system. First, I identified the time range when the offending upgrade happened, and retrieved the log entries giving the old and new version numbers of the upgraded packages:

$ awk '$1=="2016-03-20" && $3=="upgrade"' /var/log/dpkg.log
2016-03-20 16:58:22 upgrade libwebkitgtk-3.0-0:amd64 2.4.9-3 2.4.10-1
2016-03-20 16:58:24 upgrade libjavascriptcoregtk-3.0-0:amd64 2.4.9-3 2.4.10-1
2016-03-20 16:58:26 upgrade traceroute:amd64 1:2.0.22-1 1:2.1.0-1
2016-03-20 16:58:33 upgrade ethtool:amd64 1:4.2-1 1:4.5-1
2016-03-20 16:58:34 upgrade libsdl1.2debian:amd64 1.2.15+dfsg1-3 1.2.15+dfsg1-4
2016-03-20 16:58:34 upgrade subversion:amd64 1.9.3-2+b1 1.9.3-3
2016-03-20 16:58:36 upgrade libsvn1:amd64 1.9.3-2+b1 1.9.3-3
2016-03-20 16:58:56 upgrade linux-image-amd64:amd64 4.3+70 4.4+71
2016-03-20 16:58:56 upgrade linux-libc-dev:amd64 4.3.5-1 4.4.6-1
2016-03-20 16:59:03 upgrade amd64-microcode:amd64 2.20141028.1 2.20160316.1

Next, I tried to find the still-cached package files on disk (luckily for me I hadn't run autoclean):

$ awk '$1=="2016-03-20" && $3=="upgrade" {gsub(/:/, "%3a", $5); split($4, f, ":"); print "/var/cache/apt/archives/" f[1] "_" $5 "_" f[2] ".deb"}' /var/log/dpkg.log | xargs -r ls -ld
ls: cannot access '/var/cache/apt/archives/ethtool_1%3a4.2-1_amd64.deb': No such file or directory
-rw-r--r-- 1 root root   28820 Dec 18  2014 /var/cache/apt/archives/amd64-microcode_2.20141028.1_amd64.deb
-rw-r--r-- 1 root root 1978874 Dec 10 18:22 /var/cache/apt/archives/libjavascriptcoregtk-3.0-0_2.4.9-3_amd64.deb
-rw-r--r-- 1 root root  185006 Mar 12 00:41 /var/cache/apt/archives/libsdl1.2debian_1.2.15+dfsg1-3_amd64.deb
-rw-r--r-- 1 root root 1317644 Mar  3 11:30 /var/cache/apt/archives/libsvn1_1.9.3-2+b1_amd64.deb
-rw-r--r-- 1 root root 7679400 Dec 10 18:22 /var/cache/apt/archives/libwebkitgtk-3.0-0_2.4.9-3_amd64.deb
-rw-r--r-- 1 root root    6108 Dec 14 06:59 /var/cache/apt/archives/linux-image-amd64_4.3+70_amd64.deb
-rw-r--r-- 1 root root 1075506 Feb  7 21:36 /var/cache/apt/archives/linux-libc-dev_4.3.5-1_amd64.deb
-rw-r--r-- 1 root root  983174 Mar  3 11:30 /var/cache/apt/archives/subversion_1.9.3-2+b1_amd64.deb
-rw-r--r-- 1 root root   53376 Feb 28 18:35 /var/cache/apt/archives/traceroute_1%3a2.0.22-1_amd64.deb

It looks like I don't have the older ethtool package for some reason. Still, let's carry on by force-installing the older package files:

$ sudo dpkg -i /var/cache/apt/archives/amd64-microcode_2.20141028.1_amd64.deb /var/cache/apt/archives/libjavascriptcoregtk-3.0-0_2.4.9-3_amd64.deb /var/cache/apt/archives/libsdl1.2debian_1.2.15+dfsg1-3_amd64.deb /var/cache/apt/archives/libsvn1_1.9.3-2+b1_amd64.deb /var/cache/apt/archives/libwebkitgtk-3.0-0_2.4.9-3_amd64.deb /var/cache/apt/archives/linux-image-amd64_4.3+70_amd64.deb /var/cache/apt/archives/linux-libc-dev_4.3.5-1_amd64.deb /var/cache/apt/archives/subversion_1.9.3-2+b1_amd64.deb /var/cache/apt/archives/traceroute_1%3a2.0.22-1_amd64.deb
dpkg: warning: downgrading amd64-microcode from 2.20160316.1 to 2.20141028.1
(Reading database ... 139632 files and directories currently installed.)
Preparing to unpack .../amd64-microcode_2.20141028.1_amd64.deb ...
Unpacking amd64-microcode (2.20141028.1) over (2.20160316.1) ...
dpkg: warning: downgrading libjavascriptcoregtk-3.0-0:amd64 from 2.4.10-1 to 2.4.9-3
Preparing to unpack .../libjavascriptcoregtk-3.0-0_2.4.9-3_amd64.deb ...
Unpacking libjavascriptcoregtk-3.0-0:amd64 (2.4.9-3) over (2.4.10-1) ...
dpkg: warning: downgrading libsdl1.2debian:amd64 from 1.2.15+dfsg1-4 to 1.2.15+dfsg1-3
Preparing to unpack .../libsdl1.2debian_1.2.15+dfsg1-3_amd64.deb ...
Unpacking libsdl1.2debian:amd64 (1.2.15+dfsg1-3) over (1.2.15+dfsg1-4) ...
dpkg: warning: downgrading libsvn1:amd64 from 1.9.3-3 to 1.9.3-2+b1
Preparing to unpack .../libsvn1_1.9.3-2+b1_amd64.deb ...
Unpacking libsvn1:amd64 (1.9.3-2+b1) over (1.9.3-3) ...
Preparing to unpack .../libwebkitgtk-3.0-0_2.4.9-3_amd64.deb ...
Unpacking libwebkitgtk-3.0-0:amd64 (2.4.9-3) over (2.4.9-3) ...
dpkg: warning: downgrading linux-image-amd64 from 4.4+71 to 4.3+70
Preparing to unpack .../linux-image-amd64_4.3+70_amd64.deb ...
Unpacking linux-image-amd64 (4.3+70) over (4.4+71) ...
dpkg: warning: downgrading linux-libc-dev:amd64 from 4.4.6-1 to 4.3.5-1
Preparing to unpack .../linux-libc-dev_4.3.5-1_amd64.deb ...
Unpacking linux-libc-dev:amd64 (4.3.5-1) over (4.4.6-1) ...
dpkg: warning: downgrading subversion from 1.9.3-3 to 1.9.3-2+b1
Preparing to unpack .../subversion_1.9.3-2+b1_amd64.deb ...
Unpacking subversion (1.9.3-2+b1) over (1.9.3-3) ...
dpkg: warning: downgrading traceroute from 1:2.1.0-1 to 1:2.0.22-1
Preparing to unpack .../traceroute_1%3a2.0.22-1_amd64.deb ...
Unpacking traceroute (1:2.0.22-1) over (1:2.1.0-1) ...
Setting up amd64-microcode (2.20141028.1) ...
update-initramfs: deferring update (trigger activated)
amd64-microcode: microcode will be updated at next boot
Setting up libjavascriptcoregtk-3.0-0:amd64 (2.4.9-3) ...
Setting up libsdl1.2debian:amd64 (1.2.15+dfsg1-3) ...
Setting up libsvn1:amd64 (1.9.3-2+b1) ...
dpkg: dependency problems prevent configuration of libwebkitgtk-3.0-0:amd64:
 libwebkitgtk-3.0-0:amd64 depends on libwebkitgtk-3.0-common (>= 2.4.9); however:
  Package libwebkitgtk-3.0-common is not installed.

dpkg: error processing package libwebkitgtk-3.0-0:amd64 (--install):
 dependency problems - leaving unconfigured
Setting up linux-image-amd64 (4.3+70) ...
Setting up linux-libc-dev:amd64 (4.3.5-1) ...
Setting up subversion (1.9.3-2+b1) ...
Setting up traceroute (1:2.0.22-1) ...
update-alternatives: using /usr/bin/traceroute.db to provide /usr/bin/traceroute (traceroute) in auto mode
update-alternatives: using /usr/bin/lft.db to provide /usr/bin/lft (lft) in auto mode
update-alternatives: using /usr/bin/traceproto.db to provide /usr/bin/traceproto (traceproto) in auto mode
update-alternatives: using /usr/sbin/tcptraceroute.db to provide /usr/sbin/tcptraceroute (tcptraceroute) in auto mode
Processing triggers for libc-bin (2.22-3) ...
Processing triggers for man-db (2.7.5-1) ...
Processing triggers for initramfs-tools (0.123) ...
update-initramfs: Generating /boot/initrd.img-4.4.0-1-amd64
Errors were encountered while processing:
 libwebkitgtk-3.0-0:amd64

As the error message said, one of my packages depended on a -common package just before the upgrade, but the upgrade removed it (and apt-get can't find it any more). Luckily, its package file is still in /var/cache/apt so I can just add it to the list and try again:

$ ls -ld /var/cache/apt/archives/libwebkitgtk-3.0-common*
-rw-r--r-- 1 root root 452278 Dec 10 18:22 /var/cache/apt/archives/libwebkitgtk-3.0-common_2.4.9-3_all.deb
$ sudo dpkg -i /var/cache/apt/archives/amd64-microcode_2.20141028.1_amd64.deb /var/cache/apt/archives/libjavascriptcoregtk-3.0-0_2.4.9-3_amd64.deb /var/cache/apt/archives/libsdl1.2debian_1.2.15+dfsg1-3_amd64.deb /var/cache/apt/archives/libsvn1_1.9.3-2+b1_amd64.deb /var/cache/apt/archives/libwebkitgtk-3.0-0_2.4.9-3_amd64.deb /var/cache/apt/archives/linux-image-amd64_4.3+70_amd64.deb /var/cache/apt/archives/linux-libc-dev_4.3.5-1_amd64.deb /var/cache/apt/archives/subversion_1.9.3-2+b1_amd64.deb /var/cache/apt/archives/traceroute_1%3a2.0.22-1_amd64.deb /var/cache/apt/archives/libwebkitgtk-3.0-common_2.4.9-3_all.deb
(Reading database ... 139632 files and directories currently installed.)
Preparing to unpack .../amd64-microcode_2.20141028.1_amd64.deb ...
Unpacking amd64-microcode (2.20141028.1) over (2.20141028.1) ...
Preparing to unpack .../libjavascriptcoregtk-3.0-0_2.4.9-3_amd64.deb ...
Unpacking libjavascriptcoregtk-3.0-0:amd64 (2.4.9-3) over (2.4.9-3) ...
Preparing to unpack .../libsdl1.2debian_1.2.15+dfsg1-3_amd64.deb ...
Unpacking libsdl1.2debian:amd64 (1.2.15+dfsg1-3) over (1.2.15+dfsg1-3) ...
Preparing to unpack .../libsvn1_1.9.3-2+b1_amd64.deb ...
Unpacking libsvn1:amd64 (1.9.3-2+b1) over (1.9.3-2+b1) ...
Preparing to unpack .../libwebkitgtk-3.0-0_2.4.9-3_amd64.deb ...
Unpacking libwebkitgtk-3.0-0:amd64 (2.4.9-3) over (2.4.9-3) ...
Preparing to unpack .../linux-image-amd64_4.3+70_amd64.deb ...
Unpacking linux-image-amd64 (4.3+70) over (4.3+70) ...
Preparing to unpack .../linux-libc-dev_4.3.5-1_amd64.deb ...
Unpacking linux-libc-dev:amd64 (4.3.5-1) over (4.3.5-1) ...
Preparing to unpack .../subversion_1.9.3-2+b1_amd64.deb ...
Unpacking subversion (1.9.3-2+b1) over (1.9.3-2+b1) ...
Preparing to unpack .../traceroute_1%3a2.0.22-1_amd64.deb ...
Unpacking traceroute (1:2.0.22-1) over (1:2.0.22-1) ...
Selecting previously unselected package libwebkitgtk-3.0-common.
Preparing to unpack .../libwebkitgtk-3.0-common_2.4.9-3_all.deb ...
Unpacking libwebkitgtk-3.0-common (2.4.9-3) ...
Setting up amd64-microcode (2.20141028.1) ...
update-initramfs: deferring update (trigger activated)
amd64-microcode: microcode will be updated at next boot
Setting up libjavascriptcoregtk-3.0-0:amd64 (2.4.9-3) ...
Setting up libsdl1.2debian:amd64 (1.2.15+dfsg1-3) ...
Setting up libsvn1:amd64 (1.9.3-2+b1) ...
Setting up linux-image-amd64 (4.3+70) ...
Setting up linux-libc-dev:amd64 (4.3.5-1) ...
Setting up subversion (1.9.3-2+b1) ...
Setting up traceroute (1:2.0.22-1) ...
update-alternatives: using /usr/bin/traceroute.db to provide /usr/bin/traceroute (traceroute) in auto mode
update-alternatives: using /usr/bin/lft.db to provide /usr/bin/lft (lft) in auto mode
update-alternatives: using /usr/bin/traceproto.db to provide /usr/bin/traceproto (traceproto) in auto mode
update-alternatives: using /usr/sbin/tcptraceroute.db to provide /usr/sbin/tcptraceroute (tcptraceroute) in auto mode
Setting up libwebkitgtk-3.0-common (2.4.9-3) ...
Setting up libwebkitgtk-3.0-0:amd64 (2.4.9-3) ...
Processing triggers for libc-bin (2.22-3) ...
Processing triggers for man-db (2.7.5-1) ...
Processing triggers for initramfs-tools (0.123) ...
update-initramfs: Generating /boot/initrd.img-4.4.0-1-amd64

Success! Actually this didn't solve my problem. But it successfully downgraded the packages, QED.
Share
Improve this answer
answered Mar 21, 2016 at 22:35
user avatar
aecolley
40233 silver badges44 bronze badges
Add a comment
5

aptitude gives you access to all versions of a package if available according to Debian package management.
Share
Improve this answer
edited Jun 14, 2012 at 20:34
user avatar
slhck
211k6363 gold badges572572 silver badges566566 bronze badges
answered Feb 18, 2010 at 21:58
user avatar
user28725
5111 silver badge11 bronze badge

    2.7.3 might help you downgrade to stable. 2.7.16 explains saving and restoring dpkg state. dpkg-repack allows you to "compress" a single package. – 
    joeytwiddle
    Nov 2, 2012 at 20:50

Add a comment
5

I came across Hartman's Blogstatic Blog: How to Undo an Update in Ubuntu Lucid

    The first step to undoing the offending update was to find out what updates it was exactly. After searching some forums I came across a way to see my update history: Open synaptic package manager ("sudo synaptic" in the terminal). From the menu bar, click File -> History and you will see all your updates sorted by date.

    Unfortunately I had installed about 20 updates today, and I didn't know which one had caused the problem. By searching through each of the packages named in the History list, I was able to downgrade a few at a time until the problem was solved and I had identified the offending update. To do this:

    Use the search bar to find the package you want to downgrade. Once you've found what you're looking for, click on the package to select it. From the menu bar, click Package -> Force Version and select the previous version of the package from the drop down menu. Click the "Apply" button to apply the downgrade.

Share
Improve this answer
edited Jun 15, 2012 at 7:14
user avatar
slhck
211k6363 gold badges572572 silver badges566566 bronze badges
answered Jun 14, 2012 at 20:31
user avatar
Manav Brar
5111 silver badge22 bronze badges

    1
    I am expecting everyone here to know the basics on how to look up the last offending update: – 
    Manav Brar
    Jun 14, 2012 at 20:56
    2
    What was that edit about? Do you have another question? Do you want us to play a guessing game? – 
    slhck
    Jun 15, 2012 at 7:15

Add a comment
5

I also had to undo an package upgrade today on a couple of Debian servers. I successfully reverted the packages to the last version by using aptitude, whereas the following awk command was very helpful.

(In the below command replace the date string with the date of the day from which on you want to revert the upgrades)

awk 'BEGIN{ start="0" } { if($0 ~ /Log started: 2017-06-20/) { start="1"} if ( start == "1" && $0 ~ /Unpacking.*over/) {gsub(/[\s\t)( ]+/,"",$5); printf("%s=%s ", $2 , $5)}}' /var/log/apt/term.log

review the output to verify that these are the packages and versions to be reverted. Then use apt or aptitude to do the downgrade of the listed packages:

apt-get install [paste output here]

or

aptitude install [paste output here]

I hope that this is also a useful time saver for others.
Share
Improve this answer
edited Jan 19, 2021 at 6:39
answered Jun 20, 2017 at 14:21
user avatar
Andreas Kohlbecker
5111 silver badge33 bronze badges

    Thanks. It gives me Unable to find a version "5.4.0.60.63" for the package "linux-generic", is there any way to resolve that? aptitude update does not help. – 
    jangorecki
    Jan 18, 2021 at 16:35
    I suspect that linux-generic=5.4.0.60.63 is no longer available in the official package sources, and that you have cleaned your local apt package cache. The solution for this dilemma depends on your specific linux distribution. If you are using Debian you could try using the snapshot archive which provides a kind of wayback-machine to old packages which are no longer available otherwise: snapshot.debian.org – 
    Andreas Kohlbecker
    Jan 19, 2021 at 6:52

Add a comment
2

I believe not, aside from taking a full backup of the relevant filesystems (those that contain /, /bin, /lib, /sbin, /usr, /var, /etc and /boot (which may all be on on filesystem) and your boot record) so you can roll the machine back afterwards.
Share
Improve this answer
answered Sep 9, 2009 at 22:34
user avatar
David Spillett
23.2k4747 silver badges6767 bronze badges

    I could (and probably will) take a bare metal backup, but I wanted a software option that would let me undo the upgrade in a faster time frame. Restoring from the bare metal backup could take several hours. – 
    jjclarkson
    Sep 9, 2009 at 22:47
    1
    You could make sure you have copies of all the packages you are about to upgrade in their previous versions (they are probably still sat in your apt cache somewhere in /var) and any relevant config files stored away. You could then try force a roll back by explicitly telling dpkg to install those versions. You might have some work to do afterwards when you want the normal upgrades to happen, so it isn't something I'd recommend. – 
    David Spillett
    Sep 9, 2009 at 23:20
    A backup made with rsync (timestamping enabled) can be restored quite quickly, compared to a backup made with tar. – 
    joeytwiddle
    Oct 6, 2012 at 10:48

Add a comment
2

I run my linux servers in a virtualized environment and run a shapshot just before an apt-get upgrade, or any major 3rd party updates/upgrades for that matter.

Then if something goes wrong, I simply revert and life goes on until I can find out more information.

This came in very handle when I upgraded my Ubuntu box to 12.04, and somehow MySQL was completely non-functional after the upgrade. I rolled back, found the answer later, reran the upgrade, fixed MySQL, and life was good.
Share
Improve this answer
answered May 31, 2013 at 19:00
user avatar
Brain2000
38422 silver badges66 bronze badges
Add a comment
1

You could try checkinstall

    After you ./configure; make your program, CheckInstall will run make install (or whatever you tell it to run) and keep track of every file modified by this installation, using the excelent installwatch ...

So maybe you could tell it to run aptitude safe-upgrade and it would keep track of every modification made by the upgrade.
Share
Improve this answer
answered Oct 3, 2009 at 2:26
user avatar
solarc
49522 gold badges55 silver badges1717 bronze badges
Add a comment
1

There's a project called Nexenta that combines the OpenSolaris kernel with the Ubuntu userspace. It provides a tool to integrate Solaris's ZFS and Debian's apt in order to provide an undo button for upgrades. See here: http://www.nexenta.org/os/TransactionalZFSUpgrades

More generally, what you need is a versioning file system. Btrfs for Linux is in development.
Share
Improve this answer
answered Oct 5, 2009 at 2:28
user avatar
Ryan C. Thompson
11.2k99 gold badges4444 silver badges6868 bronze badges
Add a comment
1

Using Apt-Undo is a possible option, but it can only work if you are using it to installed and uninstall packages. It won't help if you've already uninstalled software the normal way.

http://www.ubuntugeek.com/apt-undo-a-simple-way-of-undoing-apt-actions.html http://lkubuntu.wordpress.com/2011/07/27/apt-undo-a-simple-way-of-undoing-apt-actions/
Share
Improve this answer
answered Aug 10, 2013 at 14:37
user avatar
Rucent88
69288 silver badges1111 bronze badges
Add a comment
1
DPkg::Pre-Install-Pkgs and ZFS on Linux snapshots

If you installed your operating system on a ZFS file system (e.g., ZFS on Linux), you can configure apt-get to run zfs snapshot before it installs or upgrades anything, which will back up your file system instantaneously. It may work with backup mechanisms other than ZFS snapshots, but I'll leave that testing to others.
The Script

Create a file like

/etc/apt/apt.conf.d/71backup

with contents

// Tell `apt-get' to take a ZFS snapshot before installing or upgrading a
// set of packages:
DPkg::Pre-Install-Pkgs {"/sbin/zfs snapshot rpool/ROOT/debian@apt-get_$(date '+%Y-%m-%d-%H%M')";};

where rpool/ROOT/debian should be replaced by the name of the ZFS file system to which your operating system is mounted. You gave it that name when you first installed your OS, and it can be found under attribute NAME with the command

# zfs list -t filesystem
NAME ...
...
rpool/ROOT/debian ...
...

But does it work?

You'd better take a snapshot before following the configuration advice of some random internet person:

# zfs snapshot rpool/ROOT/debian@$(date '+%Y-%m-%d-%H%M%S')_test
# zfs list -t snapshot | grep rpool
...
rpool/ROOT/debian@2018-08-01-230001_test

There it is. Should error: fn_borked soon occur, you may return your system to its blissful current state with

# zfs rollback rpool/ROOT/debian@2018-08-01-230001_test

Now try it out by installing two tiny games that are likely available in your repo:

# apt-get install tanglet sudoku
...
# zfs list -t snapshot | grep apt\-get
rpool/ROOT/debian@apt-get_2018-08-02-033614

That snapshot contains your file system as it was before the two games were installed.

# exit
$ sudoku

Fun times for grandma, but you hate sudoku.

$ sudo -i
# zfs rollback rpool/ROOT/debian@apt-get_2018-08-02-033614
# exit
$ sudoku
-bash: /usr/games/sudoku: No such file or directory
$ tanglet
-bash: tanglet: command not found

After multiple snapshots have been taken, you may roll back to any earlier one by adding the -r flag. In our case, for instance, try

# zfs -r rollback rpool/ROOT/debian@2018-08-01-230001_test

Be warned, however, that not only will this return your file system to the state it was in when rpool/ROOT/debian@2018-08-01-230001_test was taken, but it will also delete irretrievably all later snapshots. If you followed along with this post, the snapshot rpool/ROOT/debian@apt-get_2018-08-02-033614 would now be gone.

I tested apt-get upgrade on a Debian GNU/Linux with

# apt-get -t=oldstable install tanglet sudoku
...
# apt-get upgrade
...
# zfs list -t snapshot | grep apt\-get

It works. One snapshot was created for the install command, another for the upgrade command.

Caveat: I tested this for the first time today and know very little about apt's inner workings. Should this break something for you or entail risks my benewbed mind hasn't considered, please comment about it below.
Share
Improve this answer
edited Aug 22, 2018 at 11:21
answered Aug 14, 2018 at 1:42
user avatar
LaTeX2enub1336
11133 bronze badges
Add a comment
0

I have successfully done that few times but I won't recommended it. This is what I did (if I recall correctly):

1) Remove any non-official software which are not included in the default ubuntu repositories (it may not be required, but I suggest it as they may get in your way).

2) Change your /etc/apt/sources.list (and sources.list.d/*) to the previous version (comment all non-official repositories).

3) apt-get update / aptitude update

4) Using aptitude, downgrade core packages (like X11, libraries, etc). It will start firing a lot of broken packages... so you will need to solve each case (you need to know how to do that in aptitude). The way you downgrade it is by going to the description panel and installing the version (by pressing +) at the bottom.

5) Repeat #4 until all software belongs to your target version (check on version column in aptitude).

These are the reason why I don't recommend this method:

    It takes a lot of time (its a painfully process)
    Some application may not work properly (as they may still have the most recent configuration). In that case you will need to "purge" and reinstall.
    There are system-related updates that won't work after downgrade
    Its highly risky as you may end-up with an unusable system

I would highly recommend to do a clean install and move your configuration little by little. It also takes time, but at the end you have a stable version.

The reason I did it was mainly as experimentation and as a result of desperation.
Share
Improve this answer
answered Sep 7, 2015 at 7:31
user avatar
lepe
46677 silver badges1313 bronze badges
Add a comment
0

When using Debian there is a tool apt-revert where you have a CLI to select which apt call should be reverted.

This can, of course, only work in general, if all old package versions are still available, even if already deleted locally. This is possible for Debian with snapshots.debian.org which apt-revert uses.

If something like this exists for Ubuntu, too, it probably wouldn't be a lot of work to adapt apt-revert to also work on Ubuntu.
Share
Improve this answer
answered Jun 10, 2020 at 19:12
user avatar
Patrick Häcker
10111 bronze badge
Add a comment
Your Answer

By clicking “Post Your Answer”, you agree to our terms of service, privacy policy and cookie policy
Not the answer you're looking for? Browse other questions tagged ubuntu restore package-management aptitude undo or ask your own question.

    The Overflow Blog

Empathy for the Dev: Avoiding common pitfalls when communicating with developers

    Episode 436: Meet the design system that lets us customize and theme Stack...
    Featured on Meta
    How might the Staging Ground & the new Ask Wizard work on the Stack Exchange...

Linked
1
Karmic erased my desktop
Related
7
How to ReUse Ubuntu APT
1
How can I upgrade Ubuntu from 9.10 to 10.04 on a netbook with a 4GB root partition?
4
How can I get apt-get to install python packages for a different version of python?
4
Fear of apt-get upgrade: Will it break my website?
4
Postgresql has broken apt-get on Ubuntu
5
Upgrade from 10.04 to 12.04: apt/aptitude debug information
4
Ubuntu can't apt-get upgrade
0
apt-get upgrade fails, unmet dependencies
Hot Network Questions

    How to set animation to move an object by a distance and not from one place to another
    Can I put my rental in a trust and have the trust sell it?
    Can Alarm be used to detect hidden creatures?
    Rotation direction of Pulsars
    How are fonts "stored" on LaTeX?

more hot questions
Question feed

Super User

    Tour
    Help
    Chat
    Contact
    Feedback

Company

    Stack Overflow
    Teams
    Advertising
    Collectives
    Talent
    About
    Press
    Legal
    Privacy Policy
    Terms of Service
    Cookie Settings
    Cookie Policy

Stack Exchange Network

    Technology
    Culture & recreation
    Life & arts
    Science
    Professional
    Business
    API
    Data

    Blog
    Facebook
    Twitter
    LinkedIn
    Instagram

Site design / logo © 2022 Stack Exchange Inc; user contributions licensed under cc by-sa. rev 2022.4.21.42004

Your privacy

By clicking “Accept all cookies”, you agree Stack Exchange can store cookies on your device and disclose information in accordance with our Cookie Policy.
Super User requires external JavaScript from another domain, which is blocked or failed to load. Retry using another source.
]]

termux-repositories-legacy-24.12.2019.tar
https://pt.osdn.net/projects/termux-old/storage/termux-packages/

Archive of Termux’s packages for Android 5/6
  https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar

Archive of apps, packages and sources compatible with Android 5:
  https://archive.org/details/termux-repositories-legacy
https://pt.osdn.net/projects/termux-old/storage/termux-packages/dists/stable/
https://pt.osdn.net/projects/termux-old/storage/termux-packages/dists/stable/main/binary-arm/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/Release
  <-- 跳转自 https://pt.osdn.net/projects/termux-old/storage/termux-packages/ 下的文件列表中的『Release』
  https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/
    似乎可以用来替换 https://packages-cf.termux.org/apt/termux-main
      因为同样有文件夹『dists/』
        确实行，不过本地动态链接库一致性以遭到破坏，
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/
[ ]	Packages.xz	2022-03-13 00:31 	80K	 
[ ]	libandroid-glob-static_0.6-1_arm.deb	2022-03-13 00:52 	4.3K	 
[ ]	libandroid-glob_0.6-1_arm.deb	2022-03-13 00:52 	6.5K	 
[ ]	libandroid-shmem-static_0.2.1-1_arm.deb	2022-03-13 00:52 	5.4K	 
[ ]	libandroid-shmem_0.2.1-1_arm.deb	2022-03-13 00:52 	8.7K	 
[ ]	libandroid-support-static_24-6_arm.deb	2022-03-13 00:52 	103K	 
[ ]	libandroid-support_24-6_arm.deb	2022-03-13 00:52 	102K	 

cd /sdcard/Download/
wget https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/ -o binary-arm.html
file:///sdcard/Download/binary-arm.html
file:///sdcard/Download/index.html
  下载所有？
下载 https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/Packages.xz
解压 /sdcard/Download/Packages.xz
view /sdcard/Download/Packages/Packages
下载 https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/binutils_2.33.1-1_arm.deb
dpkg -I /sdcard/Download/binutils_2.33.1-1_arm.deb
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x18a
  搜libandroid-support.so
  install old version: dpkg -i ./libandroid-support_22-1_arm.deb; restart the app; And then avoid apt upgrade for a while (or use apt-mark hold libandroid-support)
dpkg -I /sdcard/Download/libandroid-support_24-6_arm.deb
dpkg-deb -c /sdcard/Download/libandroid-support_24-6_arm.deb
./data/data/com.termux/files/usr/lib/libandroid-support.so
./data/data/com.termux/files/usr/share/doc/libandroid-support/LICENSE -> ../../LICENSES/Apache-2.0.txt
view /data/data/com.termux/files/usr/share/doc/libandroid-support/
cp /data/data/com.termux/files/usr/lib/libandroid-support.so '/data/data/com.termux/files/usr/lib/libandroid-support.so[save20220427]'
e script/20220427_fix_termux.py
  DOING
不要在此处写步骤，转至20220427_fix_termux.py
[[
ok:cd,pwd,diff
alias rm="py -m nn_ns.app.rm"
alias cp="py -m nn_ns.app.cp"
alias mv="py -m nn_ns.app.mv"
alias ls="py -m nn_ns.app.ls"
alias cat="py -m nn_ns.app.cat"
]]

dpkg -I /sdcard/Download/
dpkg-deb -c /sdcard/Download/

https://linuxhint.com/manual_install_deb_package_cli_ubuntu/#:~:text=How%20to%20Manually%20Install%20a%20Deb%20Package%20Using,Install%20a%20Deb%20Package.%20...%207%20Conclusion.%20
[[
$ dpkg -I /path/to/file.deb
  show info+dependencies
$ dpkg-deb -c /path/to/file.deb
  show file+destination path
$ dpkg-deb --extract /path/to/file.deb
$ sudo dpkg -i /path/to/file.deb
  install without any dependencies
$ sudo apt -f install
  fix the unmet dependency issue
$ sudo apt install /path/to/file.deb
$ sudo apt install ./file.deb
  automatically install all the required dependencies
===

Debian
How to Manually Install a Deb Package Using Command Line in Ubuntu
2 years ago
by Nitesh Kumar
This article will list a few command line methods that can be used to install standalone “.deb” installers that are not available in official repositories of Ubuntu. Some other useful commands helpful for handling “.deb” packages will also be covered. So let’s jump in.

List All Dependencies of a Deb File


To view information about a “.deb” file and all of its dependencies, run the command below:

$ dpkg -I /path/to/file.deb

The example below shows information about persepolis download manager “.deb” file.

This command is specially useful if you want to check what is being installed beforehand.
List All Files That will be Installed From a Deb Package

To see all files that a “.deb” package will install on your system along with their destination paths, run the command below:
$ dpkg-deb -c /path/to/file.deb

The example below shows files that will be installed on the system if you manually install persepolis download manager “.deb” package. Note that Ubuntu’s apt package manager also lists included files but requires you to install the package first. However, this method doesn’t require you to install the “.deb” package and it is really useful if you want to analyze which file goes where.

Extract All Files from a Deb Package

Sometimes you may want to extract a deb package to check a piece of code or use some of its included files for debugging and other purposes. To extract all files from a deb package, you can run a command in following format:
$ dpkg-deb --extract /path/to/file.deb

Note that extracting files is not the same as installation of a deb package. You will just get extracted contents of a “.deb” package in a local folder.
Install a Deb File Using Dpkg

Dpkg is a package management utility for managing “.deb” (debian) packages. To install a “.deb” package using dpkg, run the command below:
$ sudo dpkg -i /path/to/file.deb

The above command will install the standalone deb package only, without any dependencies. To fix this, you will have to run a command to auto-install required dependencies. Otherwise your system may be left in a broken state. To fix the unmet dependency issue, run the command below:
$ sudo apt -f install
Install a Deb File Using Gdebi

Gdebi is a nice command line and graphical application solely dedicated for installing standalone “.deb” packages stored on your local drive. It automatically resolves dependencies as well, as long as they are available in official Ubuntu repositories (requires network connection).

To install gdebi in Ubuntu, run the command below:
$ sudo apt install gdebi

To install a “.deb” package using Gdebi, run the command below:
$ sudo gdebi /path/to/file.deb

Since gdebi will take care of installation of dependencies, you don’t have to manually run another command to fix broken packages. However, if you want to check if there are broken packages or not and fix them automatically, you can run the command mentioned above again:
$ sudo apt -f install
Using Apt to Install a Deb Package

You can also use Ubuntu’s default “apt” package manager to install standalone “.deb” files. To do so, run the following command:
$ sudo apt install /path/to/file.deb

If you launched terminal inside the directory of “.deb” file, run following command instead:
$ sudo apt install ./file.deb

Like gdebi, apt will automatically install all the required dependencies. To confirm, run the command below:
$ sudo apt -f install
Conclusion

These are a few commands you can use to install “.deb” files without using any graphical interface. They are useful if you are running and managing Ubuntu server edition or using Ubuntu without any desktop environment.
About the author
Nitesh Kumar

I am a freelancer software developer and content writer who loves Linux, open source software and the free software community.

Linux Hint LLC, editor@linuxhint.com
1210 Kelly Park Cir, Morgan Hill, CA 95037
An Elite CafeMedia Publisher
]]

]]]]@20220430
#'''



r'''
[[[[[@20220430
move from:
    e others/app/termux/apt_pkg.txt

[[[[[[[[[
===========================================
@20220426 刚刚解决故障，开始更新
view others/app/termux/apt_update_fail__solved.txt
  解决安装更新时仓库链接失效故障
apt update
apt-get update
apt list
apt list | grep 'termux.*upgradable'
  [[
WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

termux-am/stable 0.4 all [upgradable from: 0.3-1]
termux-auth/stable 1.4-2 arm [upgradable from: 1.1-2]
termux-exec/stable 1:1.0 arm [upgradable from: 0.4-2]
termux-keyring/stable 3.3 all [upgradable from: 1.1-1]
termux-licenses/stable 2.0-2 all [upgradable from: 1.0-1]
termux-tools/stable 0.175 all [upgradable from: 0.75]
  ]]
$
apt upgrade termux-am
apt upgrade termux-auth
apt upgrade termux-exec
apt upgrade termux-keyring
apt upgrade termux-licenses
apt upgrade termux-tools

[[[[[
[[[
$ apt upgrade termux-am
Reading package lists... Done
Building dependency tree
Reading state information... Done
Calculating upgrade... Done
The following packages were automatically installed and are no longer required:
  binutils libcairo-gobject libtool libutil
Use 'apt autoremove' to remove them.
The following NEW packages will be installed:
  dialog game-music-emu giflib
  libandroid-posix-semaphore libaom libbluray
  libcap-ng libcompiler-rt libdav1d libevent liblz4
  librav1e libresolv-wrapper libssh2 libudfread
  libvidstab lld llvm openjpeg-tools
  openssh-sftp-server openssl-1.1 pkg-config
  termux-am-socket ttf-dejavu unbound xxhash zstd
The following packages have been kept back:
  libcairo pango texlive-bin
The following packages will be upgraded:
  apt autoconf automake bash bash-completion binutils
  busybox bzip2 ca-certificates clang cmake
  command-not-found coreutils curl dash diffutils
  dpkg dx ecj ffmpeg findutils fontconfig freetype
  fribidi gawk gdbm gdk-pixbuf gettext git glib gnupg
  gpgv graphviz grep gzip harfbuzz harfbuzz-icu
  hexedit hub jsoncpp krb5 ldns less lftp
  libandroid-glob libandroid-support libarchive
  libass libassuan libbz2 libc++ libcroco libcrypt
  libcurl libdb libedit libexpat libffi libgcrypt
  libgd libgmp libgnutls libgpg-error libgraphite
  libicu libidn2 libjpeg-turbo libksba libllvm
  libltdl liblzma libmp3lame libmpfr libnettle
  libnghttp2 libogg libopus libpixman libpng librsvg
  libsoxr libsqlite libtiff libtool libunistring
  libuuid libuv libvorbis libvpx libwebp libx264
  libx265 libxml2 libxslt littlecms m4 make man
  ncurses ncurses-ui-libs ndk-sysroot openjpeg
  openssh openssl openssl-tool p7zip pacman4console
  pcre pcre2 perl pinentry poppler procps psmisc
  pure-ftpd python python-static readline resolv-conf
  rhash sed sharutils tar tcl teckit termux-am
  termux-auth termux-exec termux-keyring
  termux-licenses termux-tools tree tsu unrar
  util-linux vim-python vim-runtime wget xvidcore
  xz-utils zlib
141 upgraded, 27 newly installed, 0 to remove and 3 not upgraded.
Need to get 179 MB of archives.
After this operation, 198 MB of additional disk space will be used.
Do you want to continue? [Y/n] n
Abort.

#先去push故障解决方案到github，再来更新termux，大动作
Do you want to continue? [Y/n] y
  #又有故障！
  [[
Preparing to unpack .../archives/coreutils_9.1_arm.deb ...
Unpacking coreutils (9.1) over (8.31-5) ...
WARNING: linker: rm: unused DT entry: type 0x1d arg 0xc5b
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x18a
WARNING: linker: /data/data/com.termux/files/usr/lib/libgmp.so: unused DT entry: type 0x1d arg 0x2900
CANNOT LINK EXECUTABLE: cannot locate symbol "__fwrite_chk" referenced by "rm"...
page record for 0xb6e5f00c was not found (block_size=64)
dpkg: error while cleaning up:
 rm command for cleanup subprocess returned error exit status 1
Setting up coreutils (9.1) ...
WARNING: linker: rm: unused DT entry: type 0x1d arg 0xc5b
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x18a
WARNING: linker: /data/data/com.termux/files/usr/lib/libgmp.so: unused DT entry: type 0x1d arg 0x2900
CANNOT LINK EXECUTABLE: cannot locate symbol "__fwrite_chk" referenced by "rm"...
page record for 0xb6e0a00c was not found (block_size=64)
dpkg: error processing archive /data/data/com.termux/files/usr/var/cache/apt/archives/libbz2_1.0.8-6_arm.deb (--unpack):
 rm command for cleanup subprocess returned error exit status 1
Errors were encountered while processing:
 /data/data/com.termux/files/usr/var/cache/apt/archives/libbz2_1.0.8-6_arm.deb
E: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
  ]]
see:
  e script/20220427_fix_termux.py
  e /sdcard/Download/downs4termux/other-urls.txt
]]]


[[[
$ apt update
Err:1 https://packages-cf.termux.org/apt/termux-main stable InRelease
  At least one invalid signature was encountered.
Reading package lists... Done
Building dependency tree
Reading state information... Done
140 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://packages-cf.termux.org/apt/termux-main stable InRelease: At least one invalid signature was encountered.
W: Failed to fetch https://packages-cf.termux.org/apt/termux-main/dists/stable/InRelease  At least one invalid signature was encountered.
W: Some index files failed to download. They have been ignored, or old ones used instead.
]]]
[[[
$ apt-get update
Get:1 https://packages-cf.termux.org/apt/termux-main stable InRelease [14.0 kB]
Err:1 https://packages-cf.termux.org/apt/termux-main stable InRelease
  At least one invalid signature was encountered.
Fetched 14.0 kB in 9s (1491 B/s)
Reading package lists... Done
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://packages-cf.termux.org/apt/termux-main stable InRelease: At least one invalid signature was encountered.
W: Failed to fetch https://packages-cf.termux.org/apt/termux-main/dists/stable/InRelease  At least one invalid signature was encountered.
W: Some index files failed to download. They have been ignored, or old ones used instead.
]]]




apt list --upgradable

]]]]]


pkg help
pkg list-all
pkg install termux-tools
pkg install termux-auth
[[[
$ pkg install termux-tools
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x18a
Err:1 https://packages-cf.termux.org/apt/termux-main stable InRelease
  At least one invalid signature was encountered.
Reading package lists... Done
Building dependency tree
Reading state information... Done
140 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://packages-cf.termux.org/apt/termux-main stable InRelease: At least one invalid signature was encountered.
W: Failed to fetch https://packages-cf.termux.org/apt/termux-main/dists/stable/InRelease  At least one invalid signature was encountered.
W: Some index files failed to download. They have been ignored, or old ones used instead.
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  liblz4 xxhash
Use 'apt autoremove' to remove them.
The following additional packages will be installed:
  dialog termux-am-socket termux-keyring
Suggested packages:
  termux-api
Recommended packages:
  ed dos2unix inetutils net-tools unzip
The following NEW packages will be installed:
  dialog termux-am-socket
The following packages will be upgraded:
  termux-keyring termux-tools
2 upgraded, 2 newly installed, 0 to remove and 138 not upgraded.                                              Need to get 0 B/145 kB of archives.
After this operation, 348 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
WARNING: linker: rm: unused DT entry: type 0x1d arg 0xc5b
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x18a
WARNING: linker: /data/data/com.termux/files/usr/lib/libgmp.so: unused DT entry: type 0x1d arg 0x2900
CANNOT LINK EXECUTABLE: cannot locate symbol "__fwrite_chk" referenced by "rm"...
page record for 0xb6de000c was not found (block_size=64)
dpkg: error processing archive /data/data/com.termux/files/usr/var/cache/apt/archives/termux-keyring_3.3_all.deb (--unpack):
 rm command for cleanup subprocess returned error exit status 1
E: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
]]]


[[[[[
E: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
dpkg --configure -a
$ dpkg --configure -a  [[
Processing triggers for man (1.14.5-2) ...
]]

apt install --fix-broken
$ apt install --fix-broken  [[
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  liblz4 xxhash
Use 'apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 140 not upgraded.
]]



apt update
pkg install termux-tools
pkg install termux-auth
===
[[[
https://www.tecmint.com/sub-process-usr-bin-dpkg-returned-an-error-in-ubuntu/


Learn Linux in One Week and Go From Zero to Hero - Get This Book
Tecmint: Linux Howtos, Tutorials & Guides
How to Solve “Sub-process /usr/bin/dpkg returned an error code (1)” In Ubuntu
James KiarieNovember 1, 2021 Categories Questions, Ubuntu 11 Comments
freestar

It’s not uncommon to run into an issue of broken packages in Ubuntu and other Debian-based distributions. Sometimes, when you upgrade the system or install a software package, you may encounter the ‘Sub-process /usr/bin/dpkg returned an error code’ error.

For example, a while back, I tried to upgrade Ubuntu 18.04 and I bumped into the dpkg error as shown below.

Errors were encountered while processing:
google-chrome-stable
E: Sub-process /usr/bin/dpkg returned an error code (1)

This indicates that the google-chrome-stable package is either broken or corrupt. There are a few workarounds to this problem, so don’t throw in the towel yet or discard your system.
Solution 1: Reconfiguring the dpkg Package

One of the triggers of this error is a corrupted dpkg database. This can be caused by the sudden interruption of the installation of a software package. Reconfiguring the database is one way to resolve this issue.

To do this, simply execute the command:

$ sudo dpkg --configure -a

freestar

This reconfigures the unpacked packages that were not installed during the installation process.
Solution 2: Force Install the Troublesome Package

Sometimes, errors can occur during the installation of software packages. When such happens, you can force install the package using the -f option as shown.

$ sudo apt install -f
OR
$ sudo apt install --fix-broken

The -f option & --fix-broken can be interchangeably used to fix broken dependencies resulting from an interrupted package or cached package download.
Solution 3: Purge the Bad or Corrupted Software Package

If the first two solutions did not fix the problem, you can remove or purge the problematic software package as shown.

$ sudo apt remove --purge package_name

For example, in my case, purging the Google chrome package fixed the issue.

$ sudo apt remove --purge google-chrome-stable

Then invoke the commands below to remove all the old, unused, and unnecessary packages which also frees up space on your hard drive.

$ sudo apt clean
$ sudo apt autoremove

Solution 4: Remove all the Files Associated with the Package

Lastly, you can manually remove all the associated with the troublesome package. First, you need to find these files which are located in the /var/lib/dpkg/info directory as shown.

$ sudo ls -l /var/lib/dpkg/info | grep -i package_name

After listing the files, you can move them to the /tmp directory as shown

$ sudo mv /var/lib/dpkg/info/package-name.* /tmp

Alternatively, you can use the rm command to manually remove the files.

$ sudo rm -r /var/lib/dpkg/info/package-name.*

Finally, update the package lists as shown:

$ sudo apt update

You can thereafter give it another shot in reinstalling the software package.
Conclusion

This type of dpkg error points to an issue with the package installer usually caused by the interruption of an installation process or a corrupt dpkg database.

Any of the above-mentioned solutions should fix this error. If you have come this far, then it’s our hope that the issue has been successfully resolved and that you were able to reinstall your software package.



====
11 thoughts on “How to Solve “Sub-process /usr/bin/dpkg returned an error code (1)” In Ubuntu”

    Manish	
    March 16, 2022 at 6:26 pm

    I typed: sudo apt-get install -f

    I got:

    dpkg: error processing package libx11-doc (--configure):
     package is in a very bad inconsistent state; you should
     reinstall it before attempting configuration
    Errors were encountered while processing:
     libx11-doc
    E: Sub-process /usr/bin/dpkg returned an error code (1)

    Help?
    Reply	
    Ipsita	
    March 5, 2022 at 6:11 pm

    Hello,

    After typing the 1st command line I got this

    $ sudo dpkg --configure -a

    dpkg: error processing package python3-pip (--configure):
     package is in a very bad inconsistent state; you should
     reinstall it before attempting configuration
    Errors were encountered while processing:
     python3-pip

    How to solve this?
    Reply	
        Ravi Saive	
        March 7, 2022 at 11:14 am

        @Ipsita,

        Remove the broken package and re-install again to fix it as shown…

        $ sudo dpkg --remove --force-remove-reinstreq python3-pip
        $ sudo apt-get install python3-pip

        Reply	
    David Crawford	
    October 31, 2021 at 6:46 pm

    Hi, many thanks for all your hard work. I’m not an IT expert by any means, so am grateful to you nerds for all your expertise. However, in solution 2, the second suggestion, a ‘space’ has been omitted after ‘install‘…

    $ sudo apt install --fix-broken

    Maybe handy for those who ‘copy’n’paste’. Not trying to be clever, but if I’m wrong, I apologise.

    Thanks, DC.
    Reply	
        Ravi Saive	
        November 1, 2021 at 10:52 am

        @David,

        Thanks for pointing out the error, I’ve corrected the command in the article…
        Reply	
    Chowdhury Kamruzzaman	
    September 10, 2021 at 12:58 am

    How to know which package is causing the problem or how else I would know which package to download?
    Reply	
    Hugo gonzalez	
    September 6, 2021 at 4:30 am

    calcurse-caldav
    E: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)

    ~ sudo dpkg --configure

    su executable not found
    sudo requires su.
    Help, please
    Reply	
    Carlos Escalona	
    July 13, 2021 at 8:04 pm

    I did make all processes to deinstall, in my case, VirtualBox.

    But, to a total surprise, the program yet is in my Linux Mint system.

    I have a Linux Mint 20.2 Uma

    I tried to eliminate the software because I had the error “sub-process /usr/bin/dpkg returned an error code (1)“.

    I don’t know what happened.
    Reply	
        Ravi Saive	
        July 14, 2021 at 10:44 am

        @Carlos,

        Check this article to fix that error – How to Solve “Sub-process /usr/bin/dpkg returned an error code (1)” In Ubuntu
        Reply	
    Aadish Saini	
    July 13, 2021 at 7:29 pm

    Thanks a lot

    After the whole 1 day!!!!
    Reply	
    Igor Evgen	
    June 3, 2021 at 6:55 pm

    Hello,

    I have Ubuntu release 21.04 (Hirsute Hippo) 64-bit with Kernel Linux 5.11.0-18-generic x86_64 and MATE 1.24.1.

    My Software Updater failed.

    I tried:

    <sudo apt autoremove && sudo apt clean && sudo apt update && sudo apt 

    and got

    Reading package lists... Done
    Building dependency tree... Done
    Reading state information... Done
    0 to upgrade, 0 to newly install, 0 to remove and 0 not to upgrade.
    2 not fully installed or removed.
    After this operation, 0 B of additional disk space will be used.
    Setting up usrmerge (24ubuntu3) ...

    FATAL ERROR:
    Both /bin/usb_printerid and /usr/bin/usb_printerid exist.

    You can try correcting the errors reported and running again
    /usr/lib/usrmerge/convert-usrmerge until it will complete without errors.
    Do not install or update other Debian packages until the program
    has been run successfully.

    dpkg: error processing package usrmerge (--configure):
     installed usrmerge package post-installation script subprocess 
    returned error exit status 1
    Setting up postfix (3.5.6-1) ...

    Postfix (main.cf) configuration was not changed.  If you need to make changes,
     
    edit /etc/postfix/main.cf (and others) as needed.  To view Postfix 
    configuration values, see postconf(1).

    After modifying main.cf, be sure to run 'systemctl reload postfix'.

    Running newaliases
    newaliases: warning: valid_hostname: misplaced delimiter: igor-System-Product-
    Name..
    newaliases: fatal: file /etc/postfix/main.cf: parameter myhostname: bad parame
    ter value: igor-System-Product-Name..
    dpkg: error processing package postfix (--configure):
     installed postfix package post-installation script subprocess returned error 
    exit status 75
    Processing triggers for libc-bin (2.33-0ubuntu5) ...
    Errors were encountered while processing:
     usrmerge
     postfix
    E: Sub-process /usr/bin/dpkg returned an error code (1)

    Please advise.
    Thank you.
    Igor
    Reply	

]]]
[[[
https://blog.csdn.net/u013832707/article/details/113104006#:~:text=Sub-process%20%2Fusr%2Fbin%2Fdpkg%20returned%20an%20error%20code%20%281%29,%E8%AF%B4%E6%98%8Edpkg%E8%BF%99%E4%B8%80package%20installers%20%E5%87%BA%E7%8E%B0%E4%BA%86%E9%97%AE%E9%A2%98%E3%80%82%20%E8%BF%99%E4%B8%80%E9%94%99%E8%AF%AF%E4%B8%80%E8%88%AC%E6%98%AF%E4%BD%BF%E7%94%A8dpkg%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%A4%B1%E8%B4%A5%E6%88%96%E8%80%85%E8%A2%AB%E4%B8%AD%E6%96%AD%E5%90%8E%E5%87%BA%E7%8E%B0%E7%9A%84%E3%80%82%20%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%B8%AD%20%2Fuse%2Fbin%2Fdpkg%20%E8%BF%99%E4%B8%80%E5%85%B3%E9%94%AE%E4%BF%A1%E6%81%AF%E8%AF%B4%E6%98%8E%E4%BA%86%E7%B3%BB%E7%BB%9F%E7%9A%84dpkg%E8%BD%AF%E4%BB%B6%E5%87%BA%E9%94%99%E4%BA%86%E3%80%82

解决 dpkg 安装出错后的 Sub-process /usr/bin/dpkg returned an error code (1) 错误 原创
2021-01-25 10:25:26 1点赞

    持久决心

    码龄8年
关注

前言

在使用 dpkg -i 安装.deb软件包的过程中，会出现安装失败的可能。之后无论用sudo apt install -f or sud apt autoremove 等常见的修复命令都是无效的。网络上很多解决方案都直接给出需要运行的命令，不分析原因也不说明理由。我从来不尝试这样的解决方案，除非我自己知道或是只能死马当活马医。

不过针对Sub-process /usr/bin/dpkg returned an error code (1)的问题，很简单的就能找到原因。参考博客：https://phoenixnap.com/kb/fix-sub-process-usr-bin-dpkg-returned-error-code-1
错误的原因

Sub-process /usr/bin/dpkg returned an error code (1)说明dpkg这一package installers 出现了问题。这一错误一般是使用dpkg安装软件失败或者被中断后出现的。

命令行中/use/bin/dpkg这一关键信息说明了系统的dpkg软件出错了。任意一次新的安装都会报这样的错误。

针对这一问题有很多解决方案，有简单的也有复杂的。接下来就告诉大家如何修复这一问题。
解决方法
方案一：重新配置 dpkg database（推荐）

重新配置 package database，直接运行一下命令即可：
sudo dpkg --configure -a
这一命令把那些已经解压但是没有被安装的package进行重新配置。在特定的时间中断安装可能会造成这一错误。这一命令尤其适用于安装进程被中断的情况。

方案二：强制安装该软件

如果方案一不行，你可以尝试自动解决依赖问题，安装该软件。执行以下命令：
sudo apt-get install -f

-f选项意味着修复问题。它会尝试修复损坏的依赖信息。这常常适用于解决因为网络问题而导致的安装失败。

方案三：卸载存在问题的软件

如果你知道是哪个软件导致了这个问题，你可以卸载它。运行如下命令：
sudo apt-get remove --purge package_name

这一命令会卸载相关软件的所有痕迹。

方案四：清除所有无用的软件

如果是旧的、过时的、无用的软件造成的错误，运行如下命令
sudo apt autoremove

卸载无用的软件

方案五：删除 post file

如果你知道导致这一错误的软件，你可以手动删除相关的文件。这些文件通常在/var/lib/dpkg/info文件夹下。执行如下命令
sudo ls –l /var/lib/dpkg/info | grep –i package_name

这一命令会将你安装的软件的所有引用列出来，之后通过如下命令删除它们：
sudo mv /var/lib/dpkg/info/package_name.* /tmp

这一命令将相关文件移动到/tmp文件夹下，之后运行如下命令进行更新
sudo apt-get update

方案六：重写package file

执行以下命令：
sudo dpkg –i ––force–overwrite /var/cache/apt/archives/full_name_of_package

如果你不知道实际的package name，可以执行以下命令进行搜索：
ls /var/cache/apt/archies/*package_name*


======================
]]]



]]]]]
[[[[[
W: Failed to fetch https://packages-cf.termux.org/apt/termux-main/dists/stable/InRelease  At least one invalid signature was encountered.
dpkg --print-foreign-architectures
dpkg --remove-architecture <architecture name>
apt-get update

===
[[[
https://askubuntu.com/questions/298177/a-failed-to-fetch-error-occurs-when-apt-get-update-is-run-how-do-i-fix-this


Ask Ubuntu
A "failed to fetch" error occurs when apt-get update is run. How do I fix this?
Ask Question
Asked 8 years, 11 months ago
Modified 1 month ago
Viewed 445k times
55

Contrary to the note above, I haven't found the answer to my problem.

I have read almost a dozen apt-get update questions, most from askubuntu.com, with "failed to fetch" errors and tried the solutions answered there. Unfortunately, none worked. I just recently installed Ubuntu 12.04 on my laptop, dual booting it alongside Windows 7. When i tried

sudo apt-get update

on the terminal, the following kept occuring:

Err http://ph.archive.ubuntu.com precise InRelease
Err http://ph.archive.ubuntu.com precise-updates InRelease                     
Err http://ph.archive.ubuntu.com precise-backports InRelease                   
Err http://ph.archive.ubuntu.com precise Release.gpg                           
  Unable to connect to ph.archive.ubuntu.com:http: [IP: 91.189.92.177 80]
Err http://ph.archive.ubuntu.com precise-updates Release.gpg            
  Unable to connect to ph.archive.ubuntu.com:http: [IP: 91.189.92.177 80]
Err http://ph.archive.ubuntu.com precise-backports Release.gpg          
  Unable to connect to ph.archive.ubuntu.com:http: [IP: 91.189.92.177 80]
Err http://extras.ubuntu.com precise InRelease                          
Err http://extras.ubuntu.com precise Release.gpg                        
  Unable to connect to extras.ubuntu.com:http:
Err http://security.ubuntu.com precise-security InRelease
Err http://security.ubuntu.com precise-security Release.gpg
  Unable to connect to security.ubuntu.com:http: [IP: 91.189.92.190 80]
Reading package lists... Done
W: Failed to fetch http://ph.archive.ubuntu.com/ubuntu/dists/precise/InRelease  
W: Failed to fetch http://ph.archive.ubuntu.com/ubuntu/dists/precise-updates/InRelease  
W: Failed to fetch http://ph.archive.ubuntu.com/ubuntu/dists/precise-backports/InRelease  
W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/precise-security/InRelease  
W: Failed to fetch http://extras.ubuntu.com/ubuntu/dists/precise/InRelease  
W: Failed to fetch http://ph.archive.ubuntu.com/ubuntu/dists/precise/Release.gpg      Unable to connect to ph.archive.ubuntu.com:http: [IP: 91.189.92.177 80]
W: Failed to fetch http://ph.archive.ubuntu.com/ubuntu/dists/precise-updates/Release.gpg  Unable to connect to ph.archive.ubuntu.com:http: [IP: 91.189.92.177 80]
W: Failed to fetch http://ph.archive.ubuntu.com/ubuntu/dists/precise-backports/Release.gpg  Unable to connect to ph.archive.ubuntu.com:http: [IP: 91.189.92.177 80]
W: Failed to fetch http://extras.ubuntu.com/ubuntu/dists/precise/Release.gpg  Unable to connect to extras.ubuntu.com:http:
W: Failed to fetch http://security.ubuntu.com/ubuntu/dists/precise-security/Release.gpg  Unable to connect to security.ubuntu.com:http: [IP: 91.189.92.190 80]
W: Some index files failed to download. They have been ignored, or old ones used instead.

Note:

This happened immediately after I installed Ubuntu 12.04. I am very new to the Linux/Ubuntu world and a noob when it comes to these kind of stuff.

The Sources list in the Update Manager (and Software Center) settings was short. It only contained 2 lines with "Canonical" in it, 2 lines with "Independent" in it, and 2 other lines. I think the list was short because it was a freshly installed Ubuntu.

Connection to the internet seems fine and my friend whose laptop had just been installed with Ubuntu 12.04 around the same time as mine, seems to have no problem with his update. We share the same connection so I think internet connection issues couldn't have been the reason for the error.

Attempted Solutions:

From here, I explored around /etc/resolvconf/resolv.conf.d and added in the /etc/resolvconf/resolv.conf.d/head the following:

nameserver 8.8.8.8
nameserver 8.8.4.4

Error still occured.

From here and here, I repeatedly changed which Mirror server to use in the Update manager and Software sources settings. Again, error still occured.

I also tried editing my sources list, unchecking the lines with "independent" on it(as suggested). According to here, I tried removing the derb-src lines in the sources list. Still, to no avail.

Lastly, this site suggests running the following:

echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
or, for a permanent solution,
echo "nameserver 8.8.8.8" | sudo tee /etc/resolvconf/resolv.conf.d/base > /dev/null

Sadly, nothing worked for me. In all forums that I have been to, the answer related to nameserver 8.8.8.8 seems to come up most often. Take note also that I really did not understand the solutions, what they meant or how are they done. I just simply followed them.

This is the output for cat /etc/apt/sources.list:

# deb cdrom:[Ubuntu 12.04 LTS _Precise Pangolin_ - Release amd64 (20120425)]/ dists/precise/main/binary-i386/

# deb cdrom:[Ubuntu 12.04 LTS _Precise Pangolin_ - Release amd64 (20120425)]/ dists/precise/restricted/binary-i386/
# deb cdrom:[Ubuntu 12.04 LTS _Precise Pangolin_ - Release amd64 (20120425)]/ precise main restricted

# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://archive.ubuntu.com/ubuntu precise main restricted
deb-src http://archive.ubuntu.com/ubuntu precise main restricted

## Major bug fix updates produced after the final release of the
## distribution.
deb http://archive.ubuntu.com/ubuntu precise-updates main restricted
deb-src http://archive.ubuntu.com/ubuntu precise-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://archive.ubuntu.com/ubuntu precise universe
deb-src http://archive.ubuntu.com/ubuntu precise universe
deb http://archive.ubuntu.com/ubuntu precise-updates universe
deb-src http://archive.ubuntu.com/ubuntu precise-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu 
## team, and may not be under a free licence. Please satisfy yourself as to 
## your rights to use the software. Also, please note that software in 
## multiverse WILL NOT receive any review or updates from the Ubuntu
## security team.
deb http://archive.ubuntu.com/ubuntu precise multiverse
deb-src http://archive.ubuntu.com/ubuntu precise multiverse
deb http://archive.ubuntu.com/ubuntu precise-updates multiverse
deb-src http://archive.ubuntu.com/ubuntu precise-updates multiverse

## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
## Also, please note that software in backports WILL NOT receive any review
## or updates from the Ubuntu security team.
deb http://archive.ubuntu.com/ubuntu precise-backports main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu precise-backports main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu precise-security main restricted
deb-src http://archive.ubuntu.com/ubuntu precise-security main restricted
deb http://archive.ubuntu.com/ubuntu precise-security universe
deb-src http://archive.ubuntu.com/ubuntu precise-security universe
deb http://archive.ubuntu.com/ubuntu precise-security multiverse
deb-src http://archive.ubuntu.com/ubuntu precise-security multiverse

## Uncomment the following two lines to add software from Canonical's
## 'partner' repository.
## This software is not part of Ubuntu, but is offered by Canonical and the
## respective vendors as a service to Ubuntu users.
# deb http://archive.canonical.com/ubuntu precise partner
# deb-src http://archive.canonical.com/ubuntu precise partner

## This software is not part of Ubuntu, but is offered by third-party
## developers who want to ship their latest software.
deb http://extras.ubuntu.com/ubuntu precise main
deb-src http://extras.ubuntu.com/ubuntu precise main

And the following is for cat /etc/resolv.conf:

# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
nameserver 127.0.0.1
search nip.upd.edu.ph

It has been pointed out that the answer is here but unfortunately that didn't work either. I tried choosing different servers but the "choose server" was never available. Searching for the best server yielded a "No suitable server" result. I think the mirror servers are fine and again, there seems to be no issue with internet connection.

Using ping -c3 archive.ubuntu.com and ping -c3 8.8.8.8 both yielded 0% packet loss. The ping for 8.8.8.8 sometimes yielded 33% packet loss but mostly 0%.

Typing nslookup google.com yields

Server:     127.0.0.1
Address:    127.0.0.1#53

Output of ps aux | grep dns:

nobody    1761  0.0  0.0  33012  1284 ?        S    17:04   0:00 /usr/sbin/dnsmasq
 --no-resolv --keep-in-foreground --no-hosts --bind-interfaces --pid-file=/var
/run/sendsigs.omit.d/network-manager.dnsmasq.pid --listen-address=127.0.0.1 --conf-
file=/var/run/nm-dns-dnsmasq.conf --cache-size=0 --proxy-dnssec
joa       2197  0.0  0.0  13576   928 pts/0    S+   17:10   0:00 grep --color=auto dns

12.04
updates
software-sources
ping
Share
Improve this question
edited Apr 13, 2017 at 12:23
community wiki

17 revs, 2 users 96%
jowayow

    Okay, let's just start from scratch. First, can you copy the exact output of the terminal when you type sudo apt-get update? Also, can you include the output of cat /etc/apt/sources.list and cat /etc/resolv.conf? And you confirm that you can browse websites on the internet normally? – 
    Alaa Ali
    May 21, 2013 at 13:45
    @Alaa In response to your inquiry, I have edited the question and posted everything you needed to know. And yes, I was able to browse websites on the internet normally. – 
    jowabels
    May 21, 2013 at 14:27
    0% packet loss? So you can ping and browse, but you can't resolve in apt-get updates...hmm. Is there some kind of DNS setting that only works with apt-get? Anyways, can you post the first two lines from nslookup google.com, and post the output of ps aux | grep dns? Also, are you using a static IP? – 
    Alaa Ali
    May 22, 2013 at 8:16 

    @Alaa I have edited the question and posted the outputs. The output for ps aux | grep dns is supposed to be a single line but I edited it to make it easier to view. Initially, I would say that I use a dynamic IP because I haven't paid anything for it, but I use university internet connections so its hard to know if the IP I use is static or dynamic. – 
    jowabels
    May 22, 2013 at 9:27
    @Alaa I just verified that I use a dynamic IP. – 
    jowabels
    May 22, 2013 at 9:40

Show 8 more comments
5 Answers
Sorted by:
34

Edit /etc/resolv.conf. In a Terminal window run

sudo gedit /etc/resolv.conf

and add the line

nameserver 8.8.8.8

and save. Then do

ping www.google.com

If this succeeds then run the following commands

sudo apt-get --download-only --reinstall install resolvconf
sudo dpkg --purge --force-depends resolvconf
sudo apt-get install resolvconf

If resolving now fails then right-click on the network indicator in the bar at the top of the desktop, click Edit Connections, select your connection, Click Edit | IPv4 Settings. Change Method from Automatic (DHCP) to Automatic (DHCP) addresses only and enter 8.8.8.8 in the Additional DNS servers field. Click Save.... Verify that /etc/resolv.conf now contains a line nameserver 8.8.8.8 and that you can still ping www.google.com.
Share
Improve this answer
edited Apr 3, 2015 at 14:50
user avatar
Kalle Richter
5,4751818 gold badges6161 silver badges9696 bronze badges
answered May 21, 2013 at 15:15
user avatar
jdthood
11.9k22 gold badges4747 silver badges6565 bronze badges

    6
    @guntbert Umm. You are talking to the author of the resolvconf package. I think that he knows what he is talking about. ;-) – 
    Kevin Bowen
    May 22, 2013 at 9:17
    @jdthood Previously, I was able to ping 8.8.8.8 (as stated in the question) but after adding the line nameserver 8.8.8.8, it didn't resolve and this line appeared From nat1.up.edu.ph (10.16.1.2) icmp_seq=1 Destination Host Unreachable – 
    jowabels
    May 22, 2013 at 9:53 

    1
    @maggotbrain thx for helping me pull my foot out of my mouth again :-) – 
    guntbert
    May 22, 2013 at 10:29
    1
    @guntbert It's all good, man. Been there, myself. If there are any dns/resolveconf issues, jdthood is the goto man to solve them! – 
    Kevin Bowen
    May 22, 2013 at 10:52
    3
    When I follow these steps, I get this error after I run the first command: Err http://us.archive.ubuntu.com/ubuntu/ wily/main resolvconf all 1.77ubuntu1   404  Not Found [IP: 91.189.91.23 80] E: Failed to fetch http://us.archive.ubuntu.com/ubuntu/pool/main/r/resolvconf/resolvconf_1.77ubuntu1_all.deb  404  Not Found [IP: 91.189.91.23 80] – 
    MadPhysicist
    Sep 30, 2017 at 1:55

Show 3 more comments
32

I was facing the same problem and figured the easiest solution is to reset the sources of /etc/apt/sources.list. To do so, follow these steps:

    Obtain the release of your Ubuntu version, type into the console:

    lsb_release -r

    Go to http://repogen.simplylinux.ch/ to generate a new sources.list
    Select your country & release

    Check the first 12 boxes:

    All Ubuntu Brances + Security & Updates
    Generate and copy your new list

    Backup the old file to sources.list.old

    mv /etc/apt/sources.list /etc/apt/sources.list.old

    You can now either open vi to save the new list by doing:

    vi /etc/apt/sources.list
    (Paste and save using `:wq`)

    Or by copying and pasting into your terminal the "curl" command (including a unique URI for your updated source list) as it is presented under "Sources List" on the repogen output page.

    G2G, retry running apt-get update

Share
Improve this answer
edited Feb 12, 2018 at 14:58
community wiki

3 revs, 3 users 81%
RienNeVaPlus

    2
    I decided to answer this, even though the authors problem was solved differently. His question is the top result to a lot of problems related to a corrupted source.list file (stumbled upon it 3 times) and felt to leave my solution here, since it would have saved me a lot of time. – 
    RienNeVaPlus
    Jun 6, 2014 at 19:59
    I downloaded a ubuntu 12 virtual machine, and no repos where valid (italian ones). I did this and worked like a charm! thanks! – 
    Feida Kila
    Oct 1, 2014 at 15:06
    Before pasting in vim, you'll need to edit insert mode by hitting the letter 'i' after you open it – 
    s g
    Jan 27, 2016 at 20:15
    This is what worked for me. – 
    Rick
    Mar 28, 2016 at 6:04
    There isn't 14.10 in the release list :( – 
    JoeTidee
    Sep 9, 2016 at 22:51

Show 1 more comment
7

sudo apt-get update finally worked! I just realized that the problem was not on the system but instead how the system connects and retrieves data from the internet. I just configured my Network settings and changed the proxy detection to Manual and filled in the HTTP, HTTPS, FTP, and Socks Host blanks the proxy that I use. When I updated again, this error output happened at first:

E: Could not get lock /var/lib/dpkg/lock - open (11 Resource temporarily unavailable)
E: Unable to lock the administration directory (/var/lib/dpkg/)

Well, not exactly like the same but similar to it (I copied above from here). But when I tried updating again, it finally worked(the reason I posted the error output above and not the exact output I saw) and I can now choose a different mirror server. If the Network proxy configuration was really the reason for my woes, well, I kinda felt stupid for such basic mistake.

Anyway, thanks everybody for your help! :)
Share
Improve this answer
edited Apr 13, 2017 at 12:24
community wiki

2 revs
jowayow
Add a comment
1

Do this

sudo bash -c 'echo "nameserver 127.0.0.1" >> /etc/resolv.conf'

Then do sudo apt-get update to see if it works.
Share
Improve this answer
answered May 22, 2013 at 9:45
user avatar
Alaa Ali
29.4k1010 gold badges9191 silver badges104104 bronze badges

    Nope, sudo apt-get update still doesn't work. Do I have to remove the line nameserver 127.0.01 or it's ok to leave it there? – 
    jowabels
    May 22, 2013 at 10:19
    Did you try to do this after reverting from jdthood's answer? So just make sure that you can ping 8.8.8.8, then add the line nameserver 127.0.0.1 to /etc/resolv.conf, it has to be the only line (after the comments of course). – 
    Alaa Ali
    May 22, 2013 at 10:43 

    Yes, I did this after reverting and there was no issue with ping 8.8.8.8 (Of course, after reverting). Basically, nameserver 127.0.0.1 was the only line added to /etc/resolv.conf. – 
    jowabels
    May 22, 2013 at 10:59
    I just wondered, the original /etc/resolv.conf` file already contained nameserver 127.0.0.1 before adding it. When I followed your answer, the edited file now contained to lines of nameserver 127.0.0.1. Is there any reason for this? – 
    jowabels
    May 23, 2013 at 2:26
    The command in my answer added the line nameserver 127.0.0.1 regardless of whatever was already in the file. The original file (after a fresh install) should most likely contain that line already, although the output that you had in your question did not have that. But, after you followed the last commands in jdthood's answer, I think the file was reset and the line nameserver 127.0.0.1 was added. So when you followed my answer, another line was added. Anyways, if you have two lines, it's safe to remove one of them. – 
    Alaa Ali
    May 23, 2013 at 5:27

Show 2 more comments
0

I had the same error and found out it was because I had added the armhf architecture.
Run this-
sudo dpkg --print-foreign-architectures
Its better to remove any new architectures as not all repositories have index files for them and cause this error.
Run-
sudo dpkg --remove-architecture <architecture name>
and then-
sudo apt-get update
This solved the issue for me.
Hope it helps... :)
Share
Improve this answer
answered Mar 19 at 6:20
community wiki

Savio
Add a comment

]]]
]]]]]
[[[[[
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x18a

使用 Android 6.0 SDK-API 23 的主仓库
  termux repository for API23 Android6
[[
https://github.com/termux/termux-packages/issues/4658
Note that the last working version of Termux for android 5/6 is Termux 0.75. This is available in Fdroid by enabling the 'F-Droid Archive' repo in settings.
  https://archive.org/
  https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar
  https://linx.li/termux-v079-offline-bootstraps.apk
I have edited /data/data/com.termux/files/usr/etc/apt/sources.list to http
Yes - that works! Thanks a lot!
备份？
  cd $PREFIX/../
  tar zcvf /sdcard/termux-prefix.tar.gz usr

https://github.com/SDRausty/TermuxArch
  [
https://sdrausty.github.io/TermuxArch/docs/install
    [
Prerequisites: minimum of about 1GB free in userspace on device, if you want to have some fun on your device and working knowledge of vimtutor is recommended. There are many ways to run this setup script on device. Please use the bash shell for installation and execution of setupTermuxArch.sh. Here are some methods:
    ...
    ]

This Termux bash setup shell script will attempt to set Arch Linux up in your Termux environment. Please see install for options how to run setupTermuxArch on device. You can use bash setupTermuxArch to install Arch Linux in a Termux PRoot container on your Android smartphone and tablet, and Chromebook too. When successfully completed, you will be experiencing the pleasure of the Linux command prompt in Arch Linux in Termux PRoot on Android, Chromebook and Fire OS on smartphone, tablet and wearable.
  ]



x11-repo is no longer available for Android 5/6. I provide only packages compiled for "current" Android API level, i.e. 24 or Android 7.0.

If want packages working on Android 5, get them from https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar.


https://github.com/termux/termux-packages/issues/4658
  [[


Skip to content
termux /
termux-packages
Public

    Code
    Issues 339
    Pull requests 21
    Discussions
    Actions
    Projects
    Wiki
    Security
    Insights

Jump to bottom
Mirror Termux packages for Android 5.x/6.x on IBiblio #4658
Open
1 task
Symbian9 opened this issue on 16 Dec 2019 · 10 comments
Labels
enhancement
help wanted
not stale
Comments
@Symbian9 Symbian9 commented on 16 Dec 2019 •

    UPDATE NOTE: The last working Termux packaged for Android 5.x

        https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar

Problem description

End of android-5/6 support on 2020-01-01
Actual behavior

    From that date there will no longer be any updates to the package repositories' android-5 branches.

    An android-5 branch has also been created for termux-app, and the latest tagged version of the app (0.76) requires android 7.

    If you are using android 5 or android 6 on your device then the only way to continue to get updates after 2020-01-01 would be to upgrade to android 7 or newer (if possible).

        Q: What will happen to the android-5 branch? Will it be archived or completely removed?
            A: Branch will be available but packages may not.

According this note its not clear what would happen with packages repo for Android 5.x/6.x (removed, archived with read-only, or something else)
Expected behavior

Mirror latest available Termux APKs & its packages for Android 5.x/6.x on IBiblio

    http://distro.ibiblio.org/termux/

Additional information

Closes #4467
REFERENCES

    https://en.wikipedia.org/wiki/Ibiblio
    http://distro.ibiblio.org

@ghost ghost added the enhancement label on 17 Dec 2019
@Symbian9 Symbian9 commented on 31 Dec 2019

Any news? Please, make it happen! (only 1 day left)

Backup all packages that, as for now, targeted to Android 5.x/6.x too (termux/unstable-packages, termux/x11-packages, etc.)
@sudomain sudomain commented on 19 Jan 2020

Packages are available via the link in this comment. Note that the last working version of Termux for android 5/6 is Termux 0.75. This is available in Fdroid by enabling the 'F-Droid Archive' repo in settings.

If the archived packages are hosted elsewhere, I'm guessing that users will have to manually edit $PREFIX/etc/apt/sources.list to contain the url to the archived packages?

It's worth mentioning that as long as A5/6 users have a working version of proot, they can install TermuxArch and recieve updated versions of packages like git, openssh, etc. from Arch Linux ARM. That'll be the main thing I use Termux for on my A5/6 devices.
@Symbian9 Symbian9 commented on 19 Jan 2020 •

    Packages are available

This not look like normal repo, instead it is just single large archive file — "mirror" on Archive.org is unusable because it's impossible to enable it as 3rd-party repo in Termux.

So, as for now, this issue/feature request not solved yet.
@sudomain sudomain commented on 28 Jan 2020

    This not look like normal repo

I didn't mean to imply this, but the tar file contains .deb files which can be manually installed (though painfully) with dpkg -i .

Questions for devs: Are Termux repos just standard debian repos? Is there a tool on this list that is used for packaging?
@ghost ghost commented on 28 Jan 2020

    Are Termux repos just standard debian repos?

Yes, it is a standard Debian repository. Otherwise apt would just not work.

    Is there a tool on this list that is used for packaging?

We don't use utilities from this list.

Packages are created manually with script in https://github.com/termux/termux-packages/blob/master/scripts/build/termux_step_create_debfile.sh. Repository structure is constructed by https://bintray.com/.
@sudomain sudomain commented on 28 Jan 2020 •

So ibiblio.org hosts over 100 Linux distros and software projects on distro.ibiblio.org, so it may be worthwhile. The application process seems rather straight forward. @xeffyr would it be ok if I applied for hosting of the Termux packages (for Android 5/6) on ibiblio on behalf of the Termux packages project?
@ghost ghost commented on 29 Jan 2020 •

Yes, it will be ok.

I should note that such mirroring is only useful for packages. Bootstrap environment is fetched from hardcoded URL which can't be changed without rebuilding application, so failure of termux.net will have serious effect anyway.

Reminding that termux.net is continuing to be available as there no plans to disable it.
@sudomain sudomain commented on 29 Jan 2020 •

    Reminding that termux.net is continuing to be available as there no plans to disable it.

This is welcome news and pretty hilarious because I spent last night wrestling with dpkg to install packages from the archive, not realizing that pkg install still works. #4467 lead me to believe that the packages were being removed. I can't speak for @Symbian9 , but for me this issue is resolved since termux.net still has the proot package for TermuxArch
@Symbian9 Symbian9 commented on 29 Jan 2020 •

Many packages which targeted to Android 5/6 already removed from actual termux.net repo.

So, I still keep this issue as un-resolved.
@ghost ghost added the help wanted label on 7 May 2020
@Zxce3 Zxce3 commented on 26 Jul 2021

any new news?
@stale stale bot added wontfix and removed wontfix labels on 18 Nov 2021
@stale stale bot added the wontfix label on 6 Jan
@Grimler91 Grimler91 added the not stale label on 6 Jan
@stale stale bot removed the wontfix label on 6 Jan
@termux termux deleted a comment from stale bot on 7 Jan
@termux termux deleted a comment from spz2020 on 7 Jan
@termux termux deleted a comment from stale bot on 7 Jan
@termux termux deleted a comment from Symbian9 on 7 Jan
Remember, contributions to this repository should follow its contributing guidelines.
Assignees
No one assigned
Labels
enhancement
help wanted
not stale
Projects
None yet
Milestone
No milestone
Development

No branches or pull requests
Notifications
Customize

You’re not receiving notifications from this thread.
4 participants
@Symbian9
@Grimler91
@sudomain
@Zxce3

    © 2022 GitHub, Inc.

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About
  ]]
]]
[[
https://github.com/termux/termux-packages/issues/4467



Skip to content
termux /
termux-packages
Public

    Code
    Issues 339
    Pull requests 21
    Discussions
    Actions
    Projects
    Wiki
    Security
    Insights

Jump to bottom
End of android-5/6 (termux.net) support on 2020-01-01 #4467
Closed
Grimler91 opened this issue on 28 Oct 2019 · 57 comments
Labels
android-5.x
android-6.x
information
Comments
@Grimler91 Grimler91 commented on 28 Oct 2019 •

Hi,

Following discussion in the latest development meeting it has been decided to drop android-5 support from 2020-01-01.
From that date there will no longer be any updates to the package repositories' android-5 branches.
An android-5 branch has also been created for termux-app, and the latest tagged version of the app (0.76) requires android 7.

Supporting the android-5 branches takes some time and effort from the maintainers. This time and effort would, arguably, be better spent making termux ready for android Q (and later). Some big changes are required to make termux usable for the latest android versions, as discussed in termux/termux-app#1072.

If you are using android 5 or android 6 on your device then the only way to continue to get updates after 2020-01-01 would be to upgrade to android 7 or newer (if possible).

See also the discussion in #2874 from when we first separated the repos into an android-5 branch and a master branch.

Archive of apps, packages and sources compatible with Android 5:
https://archive.org/details/termux-repositories-legacy
@Grimler91 Grimler91 added information android-5.x android-6.x labels on 28 Oct 2019
@Grimler91 Grimler91 pinned this issue on 28 Oct 2019
@Grimler91 Grimler91 changed the title End of android-5 support on 2020-01-01 End of android-5/6 support on 2020-01-01 on 28 Oct 2019
@ghost ghost commented on 28 Oct 2019 •

I also should note that unstable and x11 repositories will be disabled at this point and packages will not be downloadable for Android 5.

Edit:
I have removed unstable-repo & x11-repo on Nov 28, so new users will not be able to use repositories which are going to be deleted soon. Everyone else who has these packages already installed (or backed up) will be able to use x11/unstable repositories until their EOL.
@ghost ghost commented on 28 Oct 2019 •

A to-do list of things that highly advisable to do before dropping Android 5 support completely:

Fix
Clang can't link readline program on Android 5 #4287
Fix
[LDC] Dub doesn't work properly #4189 (in version 1.18.0)
Fix
Weechat can't load python plugin #4633.
command-not-found utility needs update

    Update bootstrap archives (package & motd updates)

List (probably incomplete) of issues that will not be fixed for Android 5-6:

pkg seafile-client don't work #4699 (seafile-client depends on python2 + requires shebang fix)
pass does not include autocompletion files #4628 ([termux.net] pass does not have completion files)
Pulseaudio is not working on Android 5 #4594 (Pulseaudio autospawn is not working)
php date() prints time in UTC #4565 (php date() prints date in UTC)
Dialog text entry inconsistent: emacs and gpg on terminal #4545 (inconsistent pinentry dialog in emacs)
gnupg dependency: dirmngr #4524 (gnupg & dirmngr should be unsplitted)
Radare2 segfault #4511 (radare2 segfault)
Package yasm is broken #4497 (incorrect code generation in yasm compiled for ARM)
calcurse: visual glitches when editing a note #4378 (visual glitches in calcurse due to broken threading)
lighttpd mod_webdav.so dlopen failed #3968 (lighttpd mod_webdav.so dlopen failed)
Apache2 service won't stop #3268 (pid file corruption in apache2)

    Wrong timezone in Go #2622 (golang always fallback to UTC timezone)

Issues likely related to OS bugs/features:

'mv' command doesn't work on text files starting with 'LG' on LG brand devices #4217 (mv does not work properly)
mv from coreutils #2869 (mv does not work properly, different from
'mv' command doesn't work on text files starting with 'LG' on LG brand devices #4217 )
mv doesnt work #4630 (duplicate of 'mv' command doesn't work on text files starting with 'LG' on LG brand devices #4217 and

    mv from coreutils #2869 ?)

@dickyharper dickyharper commented on 29 Oct 2019

Will I still be able to use youtube-dl and ffmpeg after 1.1.2020? If no, is there any other way you recommend? Thanks. Best Wishes. 😶
@ghost ghost commented on 29 Oct 2019

    Will I still be able to use youtube-dl and ffmpeg after 1.1.2020?

Will be able as soon as you have backup of $PREFIX with necessary things installed or termux.net is not down.
@dickyharper dickyharper commented on 30 Oct 2019

How do I get the backup myself? Some course videos can only download with youtube-dl. 😓
@ghost ghost commented on 30 Oct 2019 •

cd $PREFIX/../
tar zcvf /sdcard/termux-prefix.tar.gz usr

https://wiki.termux.com/wiki/Backing_up_Termux
@zorro zorro commented on 30 Oct 2019

What will happen to the android-5 branch? Will it be archived or completely removed?
@ghost ghost commented on 30 Oct 2019

Branch will be available but packages may not.
@samoht0 samoht0 commented on 31 Oct 2019

Wound be fine to remove those bintray.com/grimler/ repos from android-5 official repo list before EOS. They aren't used anyway.

Why isn't there a stable option to continue providing bootstrap and android-5 main repo? Maybe on bintray, if hosting using termux.net is an issue?
@Grimler91 Grimler91 commented on 31 Oct 2019

    Wound be fine to remove those bintray.com/grimler/ repos from android-5 official repo list before EOS. They aren't used anyway.

? The android-5 branches haven't been updated in a while but the packages work as far as I know. I don't see why removing the repos and decrease the amount of available packages would help anyone.

    Why isn't there a stable option to continue providing bootstrap and android-5 main repo? Maybe on bintray, if hosting using termux.net is an issue?

Last month we hit the data traffic cap and the main repository was suspended. Moving the android-5 repo there as well would make the situation worse.
Anyways, I believe Fornwall will continue hosting the android-5 repo and bootstraps on termux.net, at least for a considerable time, but not update it.
@ghost ghost commented on 31 Oct 2019 •

    if hosting using termux.net is an issue?

Nowhere was mentioned that hosting of termux.net is an issue. But support apparently it is.
Android 5 is old and I don't want to keep device on this OS version just for testing android-5 packages.
@samoht0 samoht0 commented on 31 Oct 2019

    I don't see why removing the repos and decrease the amount of available packages would help anyone.
    Last month we hit the data traffic cap and the main repository was suspended. Moving the android-5 repo there as well would make the situation worse.
    [xeffyr] I also should note that unstable and x11 repositories will be disabled at this point and packages will not be downloadable for Android 5.

Consistent statement considering the two others? Not for me, honestly. But maybe I'm just not getting it.

    Nowhere was mentioned that hosting of termux.net is an issue. But support apparently it is.
    Branch will be available but packages may not.

The second statement is related to, what? I assumed termux.net. A clarification by Fredrik would help here greatly, I guess.
@ghost ghost commented on 31 Oct 2019 •

    Consistent statement considering the two others?

Statement is consistent enough.

X11 and unstable repositories are not related to termux.net even though they provide packages for legacy Android. Removing them does not affect termux.net and they are not necessary for main Termux functionality.

These packages are hosted on my (non Termux org) account in order to make all resources available to main repo which is essential. Removing the X11 & unstable for legacy Android will be necessary to have stable hosting of these ones for Android 7+ and have room for some new packages.

For those who disagree with that, I will provide APT repository archives via https://archive.org/.

Sources will not disappear and will be available. Those who want to continue support Android 5 can use them and keep up to date. Though, last 3000 commits tell that not so many people are interested in supporting Android 5:
android-5 last 3000 commits stats (click to expand)

    The second statement is related to, what?

It is an answer to #4467 (comment).

    A clarification by Fredrik would help here greatly, I guess.

Yes, termux.net is hosted by @fornwall so clarification will be nice on this topic.
@dickyharper dickyharper commented on 31 Oct 2019 •

    cd $PREFIX/../
    tar zcvf /sdcard/termux-prefix.tar.gz usr

    https://wiki.termux.com/wiki/Backing_up_Termux

Yes I did. Thank you. Will the version you're talking about here still be, or has it been canceled? Termux is a really handy app.

https://reddit.com/r/termux/comments/dlpv1i/app_cannt_run_after_updating_to_version_076/f4uovos?context=3
😶
@ghost ghost commented on 31 Oct 2019

Still be, just wait until @fornwall will release it.
@dickyharper dickyharper commented on 31 Oct 2019

Thank you very much for your hard work. 😊
ghost pushed a commit to termux/termux-x11 that referenced this issue on 10 Nov 2019
set minimal sdk version to 24
1caea5f
@termux termux deleted a comment from alireza5830 on 10 Nov 2019
@ghost ghost mentioned this issue on 16 Nov 2019
F-Droid version is showing incompatible termux/termux-app#1349
Closed
@ghost ghost mentioned this issue on 5 Dec 2019
Bad System call with screen in package version 4.7.0-1 #4627
Closed
@ghost ghost mentioned this issue on 12 Dec 2019
Unstable and x11 repo not working termux/termux-app#1370
Closed
@Symbian9 Symbian9 mentioned this issue on 16 Dec 2019
Mirror Termux packages for Android 5.x/6.x on IBiblio #4658
Open
1 task
@ghost ghost mentioned this issue on 20 Dec 2019
bitcoin: bump version to 0.19.0.1 (patch from master) #4670
Merged
@ghost ghost mentioned this issue on 20 Dec 2019
lnd: bump version to 0.8.2 #4672
Merged
@ghost ghost commented on 22 Dec 2019 •

Last git versions for Termux and addons available for Android 5/6 devices:

Termux app: termux-app.apk.gz

API: termux-api.apk.gz

Boot: termux-boot.apk.gz

Float: termux-float.apk.gz

Styling: termux-styling.apk.gz

Task: termux-task.apk.gz

Widget: termux-widget.apk.gz

gunzip downloaded APKs before installation.
@karstengit karstengit commented on 6 Jan 2020 •

    Embedded bootstraps are not supported on Android 5. It downloads them from http://termux.net/bootstrap/new/ instead.

        There is no chance to continue !?

    Depends on your device, network/isp, etc...

No - sorry - the sources are not existant any more:

404 Not Found
nginx/1.14.0 (Ubuntu)
@ghost ghost commented on 6 Jan 2020 •

Really ?
Are you sure that URL is https://termux.net/bootstrap/new/ ? I just checked, everything here.

Screenshot_2020-01-05_19-37-58
@karstengit karstengit commented on 6 Jan 2020 •

    Really ?
    Are you sure that URL is https://termux.net/bootstrap/new/ ? I just checked, everything here.
    ...bootstrap exists but bootstraps not ;-)

bootstraps without the s is correct.

So what is the reason that the download fails?
I can only say that the internet connections works for every other app.

Calling the Link in a browser on the mobile works.
So the Termux-App must use an other URL.
@ghost ghost commented on 6 Jan 2020

    So what is the reason that the download fails?

If you think your internet is ok (& not tampered), then only:

    Android forces app to be installed on external storage on some devices (known issue btw).
    You messed up permissions in /data/data/* and Android failed to recover them.

@ghost ghost commented on 6 Jan 2020

App uses correct URL, https://github.com/termux/termux-app/blob/android-5/app/src/main/java/com/termux/app/TermuxInstaller.java#L173. Last git versions for Android 5 (posted in #4467 (comment)) are tested and work well.
@karstengit karstengit commented on 6 Jan 2020 •

I believe that the code is well and correct.

I never did something manually in /data/data*

Hmm - can i extract the archive manually to the correct place?
(zip could be downloaded in browser on the mobile.)
The mobile is rooted.
/data/data/com.termux has only folders that are empty.

On the SD there seems no directory for termux in /storage/.../Android/data
@ghost ghost commented on 6 Jan 2020 •

First go to android settings and check if application is installed to internal storage.

I.e. ensure that you are not running into:

java.lang.RuntimeException: Unable to create directory: /data/data/com.termux/files/usr-staging/share when installing the app on an adopted SD termux-app#1023

    Termux won't load binaries. termux-app#761

@karstengit karstengit commented on 6 Jan 2020 •

    First go to android settings and check if application is installed to internal storage.

    I.e. ensure that you are not running into:

    * [termux/termux-app#1023](https://github.com/termux/termux-app/issues/1023)

    * [termux/termux-app#761](https://github.com/termux/termux-app/issues/761)

It is installed internal with 4.71 MB.
I give manually access to the memory without success.

Maybe some special SELinux or something else?
@ghost ghost commented on 6 Jan 2020

Last thing you can try is Termux app v0.79 with embedded bootstraps (git debug version).
https://linx.li/termux-v079-offline-bootstraps.apk
@karstengit karstengit commented on 6 Jan 2020

O.K.
I deinstalled the App, downloaded and installed this one with offline bootstraps.
This one works!
Thank you for your time and help!

Google has really done everything to make the usage of Linux nearly unpossible in Android.
@karstengit karstengit commented on 6 Jan 2020 •

I am trying to install https://github.com/EXALAB/AnLinux-App (it is basing on Termux)

Now i get the Error
E: The repository 'https://termux.net stable Release' does not have a Release file.

But it is there http://termux.net/dists/stable/Release
@ghost ghost commented on 6 Jan 2020 •

Something tampers your internet connection. For same reason it have failed to download bootstraps before.

Can you try to execute

curl -L https://termux.net/dists/stable/Release

- it should print text starting with

Codename: stable
Version: 1
Architectures: all arm i686 aarch64 x86_64
Description: Main repository
Suite: stable
Date: Mon, 23 Dec 2019 22:46:08 UTC

@karstengit karstengit commented on 6 Jan 2020 •

Yes - download with curl works complete.

But there was an additional line after the Error message as i see now:
N: Updating from such a repository can't be done securely, and is therefore disabled by default.

This is the (not understandable) reason in this case.
@ghost ghost commented on 6 Jan 2020

    N: Updating from such a repository can't be done securely, and is therefore disabled by default.

This is not a reason, apt just failed to download release file and verify it.

Few more things you can try:

    Edit $PREFIX/etc/sources.list and change https to http.
    Try VPN.

@karstengit karstengit commented on 7 Jan 2020 •

I have edited /data/data/com.termux/files/usr/etc/apt/sources.list to http
Yes - that works! Thanks a lot!

The AnLinux install process could be started and finished too.
But at least Termux seems to be all i need.
Is there maybe an alternate way to get Termux direct installed with root privileges?
I think i must have a closer look at https://github.com/termux/termux-root-packages
and https://proot-me.github.io/

Is it possible to connect over WLAN with an Linux-PC to an Termux-Shell?
(When i use SSHelper i get remote an shell on the mobile, but not within the Termux environment.)

Besides - this is the Android running:
https://forum.xda-developers.com/galaxy-s5/development/rom-ane4-kitkat-4-4-2-multi-csc-t2813628
Maybe you have an idea what have been modified that causes the problems.
I can only say that this ROM is working good for all other cases of normal use with the S5.
@ghost ghost commented on 7 Jan 2020

    Is it possible to connect over WLAN with an Linux-PC to an Termux-Shell?

SSH or Telnet, pick what is the best for you.
@karstengit karstengit commented on 7 Jan 2020 •

        Is it possible to connect over WLAN with an Linux-PC to an Termux-Shell?

    SSH or Telnet, pick what is the best for you.

So i have to install and configure an SSH-Server under Termux?

Where can i find some basic concepts ?
For example the use of X11 is not really clear.

The usage of the archived packages is now clear.
https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar
Unpack to an own Webserver and edit the path in sources.list to it. Correct?

But the bootstrap-archives cannot be used, because the URL in the APP is fix. Correct?
https://archive.org/download/termux-repositories-legacy/bootstrap-archives-legacy-24.12.2019.tar
@ghost ghost commented on 7 Jan 2020

    So i have to install and configure an SSH-Server under Termux?
    Where can i find some basic concepts ?
    For example the use of X11 is not really clear.

Why not to check Termux Wiki ?

    Unpack to an own Webserver and edit the path in sources.list to it. Correct?
    But the bootstrap-archives cannot be used, because the URL in the APP is fix. Correct?

Both are correct.
@karstengit karstengit commented on 7 Jan 2020 •

        For example the use of X11 is not really clear.

    Why not to check Termux Wiki ?

Found it now:

    https://wiki.termux.com/wiki/Graphical_Environment
    https://wiki.termux.com/wiki/Remote_Access#Using_the_SSH_server

It seems that the Wiki is not editable. So i can't add something.
@karstengit karstengit commented on 8 Jan 2020 •

With the current installation "pkg install x11-repo" does not work.
How can this be added manually?
(I could get X11 running within Debian in AnLinux, but this cost really many additional internal Flash).

Can you tell me which script / executable is called by the main App to launch the Termux shell / environment ?

And a really wicked question: Is there an old version of Termux for Android 4 ?
@Grimler91 Grimler91 commented on 8 Jan 2020

    It seems that the Wiki is not editable. So i can't add something.

You need to make an account first, we've had problems with spam.

    With the current installation "pkg install x11-repo" does not work.
    How can this be added manually?

Have a look at the previous x11-repo script and mimic what it did:

termux-packages/packages/x11-repo/build.sh

Line 12 in f6e6add
 echo "deb https://dl.bintray.com/xeffyr/x11-packages-21 x11 main" > $TERMUX_PREFIX/etc/apt/sources.list.d/x11.list 

    Can you tell me which script / executable is called by the main App to launch the Termux shell / environment ?

Not sure what you mean? bash is launched for a bash shell.

    And a really wicked question: Is there an old version of Termux for Android 4 ?

No. Packages for android 4 is incompatible with android >= 5 (search the github issues for more information as this has been asked/requested many times)
@ghost ghost commented on 8 Jan 2020

    With the current installation "pkg install x11-repo" does not work.
    How can this be added manually?

x11-repo is no longer available for Android 5/6. I provide only packages compiled for "current" Android API level, i.e. 24 or Android 7.0.

If want packages working on Android 5, get them from https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar.
@karstengit karstengit commented on 8 Jan 2020 •

        Can you tell me which script / executable is called by the main App to launch the Termux shell / environment ?

    Not sure what you mean? bash is launched for a bash shell.

Yes - the idea is that the Termux-App is (of course) calling the bash.
But how it is called that the environment of Termux can be used in the shell?
I am asking because this call can be done within an other bash.

    No. Packages for android 4 is incompatible with android >= 5 (search the github issues for more information as this has been asked/requested many times)

I didn't know if there is an backup of Termux for Android 4.0 too ?
That was the idea behind this question.

    If want packages working on Android 5, get them from https://archive.org/download/termux-repositories-legacy/termux-repositories-legacy-24.12.2019.tar.

O.K. It's not so easy to use older Android's. The versions differ really hard.
@ghost ghost commented on 8 Jan 2020 •

    But how it is called that the environment of Termux can be used in the shell?
    I am asking because this call can be done within an other bash.

Linux has a system call execve which allows to execute binaries :)
Termux is only calls it and then just redirects stdin/stdout/stderr. Basically how all terminal emulators work.

    I didn't know if there is an backup of Termux for Android 4.0 too ?

Termux packages never were compiled for Android 4.0. There a much more patches needed than for Android 5.
@ghost ghost mentioned this issue on 9 Jan 2020
screen throws "Bad system call" on Android Pie #4414
Closed
@ghost ghost changed the title End of android-5/6 support on 2020-01-01 End of android-5/6 (termux.net) support on 2020-01-01 on 9 Jan 2020
@karstengit karstengit commented on 9 Jan 2020 •

    Linux has a system call execve which allows to execute binaries :)
    Termux is only calls it and then just redirects stdin/stdout/stderr. Basically how all terminal emulators work.

Yes - and how the bash is called with what kind of parameters?

    Termux packages never were compiled for Android 4.0. There a much more patches needed than for Android 5.

O.K. Thanks for the info.
@ghost ghost commented on 9 Jan 2020

    how the bash is called with what kind of parameters?

Why not to just check the source code...

    https://github.com/termux/termux-packages/blob/3eeb70674681e484b207933e8a466bbedae67165/packages/termux-tools/login
    https://github.com/termux/termux-app/blob/90e6260d5e05211ec3e6dfeb9e6e631b56062281/app/src/main/java/com/termux/app/TermuxService.java#L282
    https://github.com/termux/termux-app/blob/90e6260d5e05211ec3e6dfeb9e6e631b56062281/app/src/main/java/com/termux/app/BackgroundJob.java#L134
    https://github.com/termux/termux-app/blob/90e6260d5e05211ec3e6dfeb9e6e631b56062281/terminal-emulator/src/main/java/com/termux/terminal/TerminalSession.java#L180
    https://github.com/termux/termux-app/blob/90e6260d5e05211ec3e6dfeb9e6e631b56062281/terminal-emulator/src/main/jni/termux.c#L25

And finally - http://man7.org/linux/man-pages/man2/execve.2.html.
@ghost ghost commented on 9 Jan 2020

I'm locking this issue due to much offtopic.
@termux termux locked and limited conversation to collaborators on 9 Jan 2020
This issue was closed.
Write Preview

This conversation has been locked and limited to collaborators.
Assignees
No one assigned
Labels
android-5.x
android-6.x
information
Projects
None yet
Milestone
No milestone
Development

No branches or pull requests
Notifications
Customize

You’re not receiving notifications from this thread.
7 participants
@wbsch
@karstengit
@Grimler91
@hy-l
@samoht0
@dickyharper
@zorro

    © 2022 GitHub, Inc.

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About
]]
view others/app/termux/downloaded_scripts/termux-change-repo
        ===
        MAIN="https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main"
        ROOT="https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-root"
        X11="https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-x11"
        ===
        MAIN="https://mirror.bardia.tech/termux/termux-packages-24/"
        ROOT="https://mirror.bardia.tech/termux/termux-root-packages-24/"
        X11="https://mirror.bardia.tech/termux/x11-packages/"
        ===
        MAIN="https://grimler.se/termux-packages-24"
        ROOT="https://grimler.se/termux-root-packages-24"
        X11="https://grimler.se/x11-packages"
        ===
        MAIN="https://mirrors.aliyun.com/termux/termux-packages-24"
        ROOT="https://mirrors.aliyun.com/termux/termux-root-packages-24"
        X11="https://mirrors.aliyun.com/termux/x11-packages"
        ===
view others/app/termux/apt_update_fail__solved.txt
    mv /data/data/com.termux/files/usr/etc/apt/sources.list '/data/data/com.termux/files/usr/etc/apt/sources.list[old]'
    echo $'# The main termux repository:\ndeb https://packages-cf.termux.org/apt/termux-main stable main\n' > /data/data/com.termux/files/usr/etc/apt/sources.list
cat /data/data/com.termux/files/usr/etc/apt/sources.list
vim /data/data/com.termux/files/usr/etc/apt/sources.list
deb https://termux.net stable main
改为：deb http://termux.net stable main
改为：deb https://termux.com stable main


legacy environments termux repository mirrors
  https://github.com/termux/termux-app/issues/1393
  $ termux-upgrade-repo

legacy termux repository mirrors
[[
https://github.com/termux/termux-packages/wiki/Mirrors



Skip to content
termux /
termux-packages
Public

    Code
    Issues 339
    Pull requests 22
    Discussions
    Actions
    Projects
    Wiki
    Security
    Insights

Mirrors
Jump to bottom
Henrik Grimler edited this page 21 days ago · 92 revisions
Pages 15

Home
Auto updating packages
Build environment
Building packages
Coding guideline
Common porting problems
Creating new package
Donate
For maintainers
Haskell package guidelines
How to mirror the official repositories
Mirrors

    Info for mirror maintainers
    Repositories and Mirrors
    How to use
    Primary host
    Mirrors
    Mirrors that are part of mirror rotation in pkg
    Mirrors by a1batross
    Mirrors by Astra ISP
    Mirrors by Grimler
    Mirrors by Librehat
    Mirrors by mwt
    Mirrors by Purdue University Linux Users Group
    Mirrors by Sahilister
    Mirrors hosted in Iran
    Mirrors by Bardia Moshiri
    Mirrors hosted in China
    Mirrors by Beijing Foreign Studies University
    Mirrors by Chongqing University of Posts and Telecommunications
    Mirrors by Dongguan University of Technology
    Mirrors by Harbin Institute of Technology
    Mirrors by eScience Center, Nanjing University
    Mirrors by Tsinghua University TUNA Association
    Mirrors by University of Science and Technology of China, Linux User Group
    Mirrors by Alibaba Open Source Mirror Site

Package Management
Termux and Android 10

    Termux file system layout

Clone this wiki locally
Info for mirror maintainers

unstable-packages, game-packages and science-packages have been merged into the main (termux-packages) repository and no longer have to be synced.

Mirroring termux-packages, termux-root-packages and x11-packages can be done with several tools like rsync, apt-mirror or aptly. Steps are outlined in the page How to mirror the official repositories.
Repositories and Mirrors

Termux packages, except bootstrap environment, are served via external web services. There is a primary package server (seed) and number or mirrors, which replicate the content from it to reduce load and provide a some level of redundancy. Mirrors are running either on behalf of maintainers, community members or unaffiliated third parties and are not guaranteed to be always available.

Packages require Termux running on Android 7.0 or higher. Do not try to use repositories listed there on legacy environments.

Service availability may vary depending on your device, Internet connection quality, and censorship events in your country. If we detect serious issue on our side, we will post announce on GitHub and our community pages. Other issues, like introduced on client side or somewhere between endpoints, would be ignored.
How to use

Run apt edit-sources, comment out existing URLs and add line for picked repository, or use the termux-change-repo script that is part of the termux-tools package.
Primary host

A default Termux packages repository and content seeder for available mirrors. Server is provided for free by FossHost - a hosting provider for open source communities.

Server is IPv6-only and uses IPv6-to-IPv4 proxy, also provided by FossHost. It is quite slow but we don't have anything better at the moment. Hopefully you understand what's going on. If slow download speed bothers you, please use mirror instead.
Repository 	sources.list entry
Main 	deb https://packages.termux.org/apt/termux-main stable main
Root 	deb https://packages.termux.org/apt/termux-root root stable
X11 	deb https://packages.termux.org/apt/termux-x11 x11 main

CloudFlare CDN endpoint. Fast and stable, but has limits on uploads (100MB max per POST in "free" plan) which makes impossible to use it for submitting packages via GitHub Actions + Aptly REST API.
Repository 	sources.list entry
Main 	deb https://packages-cf.termux.org/apt/termux-main stable main
Root 	deb https://packages-cf.termux.org/apt/termux-root root stable
X11 	deb https://packages-cf.termux.org/apt/termux-x11 x11 main

Please don't use our host in your forks. Set up your own repository. Otherwise consider to contribute to our project instead of maintaining the custom fork.
Mirrors

There are listed all known Termux mirrors. If you host a one but didn't find it in the list, please open the issue in https://github.com/termux/termux-packages/issues.
Mirrors that are part of mirror rotation in pkg

These mirrors (listed alphabetically) might be picked, on random, when pkg checks available mirrors and picks one.
Mirrors by a1batross

Updated four times per day.
Repository 	sources.list entry
Main 	deb https://termux.mentality.rip/termux-main stable main
Root 	deb https://termux.mentality.rip/termux-root root stable
X11 	deb https://termux.mentality.rip/termux-x11 x11 main
Mirrors by Astra ISP

Updated once per 4 hours.
Repository 	sources.list entry
Main 	deb https://termux.astra.in.ua/apt/termux-main stable main
Root 	deb https://termux.astra.in.ua/apt/termux-root root stable
X11 	deb https://termux.astra.in.ua/apt/termux-x11 x11 main
Mirrors by Grimler

Mirrored from the main node, updated hourly during "office hours" (requires a gpg hardware key to be accessible for repo signing to work).
Repository 	sources.list entry
Main 	deb https://grimler.se/termux/termux-main stable main
Root 	deb https://grimler.se/termux/termux-root root stable
X11 	deb https://grimler.se/termux/termux-x11 x11 main
Mirrors by Librehat

Updated four times per day.
Repository 	sources.list entry
Main 	deb https://termux.librehat.com/apt/termux-main stable main
Root 	deb https://termux.librehat.com/apt/termux-root root stable
X11 	deb https://termux.librehat.com/apt/termux-x11 x11 main
Mirrors by mwt

Hosted in New Jersey, USA. Updated four times per day.
Repository 	sources.list entry
Main 	deb https://mirror.mwt.me/termux/main stable main
Root 	deb https://mirror.mwt.me/termux/root root stable
X11 	deb https://mirror.mwt.me/termux/x11 x11 main
Mirrors by Purdue University Linux Users Group

Hosted in Indiana, USA. Updated four times per day.
Repository 	sources.list entry
Main 	deb https://plug-mirror.rcac.purdue.edu/termux/termux-main stable main
Root 	deb https://plug-mirror.rcac.purdue.edu/termux/termux-root root stable
X11 	deb https://plug-mirror.rcac.purdue.edu/termux/termux-x11 x11 main
Mirrors by Sahilister

Updated four times per day.
Repository 	sources.list entry
Main 	deb https://termux.sahilister.in/apt/termux-main stable main
Root 	deb https://termux.sahilister.in/apt/termux-root root stable
X11 	deb https://termux.sahilister.in/apt/termux-x11 x11 main
Mirrors hosted in Iran

Mirrors for users in Iran for better ping and download speed.
Mirrors by Bardia Moshiri

This mirror is hosted in Iran. Updated four times per day.

Rsync: rsync://mirror.bardia.tech/termux

Contact: fakeshell@bardia.tech
Repository 	sources.list entry
Main 	deb https://mirror.bardia.tech/termux/termux-packages-24 stable main
Root 	deb https://mirror.bardia.tech/termux/termux-root-packages-24 root stable
X11 	deb https://mirror.bardia.tech/termux/x11-packages x11 main
Mirrors hosted in China

Mirrors for users in China for better ping and download speed.
Mirrors by Beijing Foreign Studies University
Repository 	sources.list entry
Main 	deb https://mirrors.bfsu.edu.cn/termux/apt/termux-main stable main
Root 	deb https://mirrors.bfsu.edu.cn/termux/apt/termux-root root stable
X11 	deb https://mirrors.bfsu.edu.cn/termux/apt/termux-x11 x11 main
Mirrors by Chongqing University of Posts and Telecommunications

More info at https://mirrors.cqupt.edu.cn/.
Repository 	sources.list entry
Main 	deb https://mirrors.cqupt.edu.cn/termux/apt/termux-main stable main
Root 	deb https://mirrors.cqupt.edu.cn/termux/apt/termux-root root stable
X11 	deb https://mirrors.cqupt.edu.cn/termux/apt/termux-x11 x11 main
Mirrors by Dongguan University of Technology
Repository 	sources.list entry
Main 	deb https://mirrors.dgut.edu.cn/termux/apt/termux-main stable main
Root 	deb https://mirrors.dgut.edu.cn/termux/apt/termux-root root stable
X11 	deb https://mirrors.dgut.edu.cn/termux/apt/termux-x11 x11 main
Mirrors by Harbin Institute of Technology
Repository 	sources.list entry
Main 	deb https://mirrors.hit.edu.cn/termux/apt/termux-main stable main
Root 	deb https://mirrors.hit.edu.cn/termux/apt/termux-root root stable
X11 	deb https://mirrors.hit.edu.cn/termux/apt/termux-x11 x11 main
Mirrors by eScience Center, Nanjing University
Repository 	sources.list entry
Main 	deb https://mirror.nju.edu.cn/termux/apt/termux-main stable main
Root 	deb https://mirror.nju.edu.cn/termux/apt/termux-root root stable
X11 	deb https://mirror.nju.edu.cn/termux/apt/termux-x11 x11 main
Mirrors by Tsinghua University TUNA Association
Repository 	sources.list entry
Main 	deb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main
Root 	deb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-root root stable
X11 	deb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-x11 x11 main
Mirrors by University of Science and Technology of China, Linux User Group
Repository 	sources.list entry
Main 	deb https://mirrors.ustc.edu.cn/termux/apt/termux-main/ stable main
Root 	deb https://mirrors.ustc.edu.cn/termux/apt/termux-root/ root stable
X11 	deb https://mirrors.ustc.edu.cn/termux/apt/termux-x11/ x11 main
Mirrors by Alibaba Open Source Mirror Site

More info at https://mirrors.aliyun.com/about.
Repository 	sources.list entry
Main 	deb https://mirrors.aliyun.com/termux/termux-packages-24 stable main
Root 	deb https://mirrors.aliyun.com/termux/termux-root-packages-24 root stable
X11 	deb https://mirrors.aliyun.com/termux/x11-packages x11 main

    © 2022 GitHub, Inc.

    Terms
    Privacy
    Security
    Status
    Docs
    Contact GitHub
    Pricing
    API
    Training
    Blog
    About
]]
legacy termux repository
[[不对，这是当前的版本
https://github.com/orgs/termux/repositories

]]
[[不对，这是高版本模拟低版本
https://github.com/farhansadik/legacy-termux

README.md
Legacy Termux

Repository support for old version of termux
Support

Minimum Supported Android Version Android 7 and above
Minimum Termux Version 95
Installation

Copy and paste those commands one by one...

pkg install git
git clone https://github.com/farhansadik/legacy-termux.git
bash legacy-termux/install

===

mkdir /sdcard/0my_files/tmp/git_/termux
cd /sdcard/0my_files/tmp/git_/termux
git clone https://github.com/farhansadik/legacy-termux.git
bash legacy-termux/install
]]
[[不知啥版本
https://packages-cf.termux.org/


Termux Packages
About Termux

Termux is a terminal emulator application for Android OS which can be extended by packages of ported common GNU/Linux utilities.

Home page: https://termux.com

Github: https://github.com/termux
What is available there?

There are hosted apt repositories for the Termux project. See table below for details.
Repository 	sources.list entry
Main 	deb https://packages.termux.org/apt/termux-main/ stable main
Games 	deb https://packages.termux.org/apt/termux-games/ games stable
Root 	deb https://packages.termux.org/apt/termux-root/ root stable
Science 	deb https://packages.termux.org/apt/termux-science/ science stable
X11 	deb https://packages.termux.org/apt/termux-x11/ x11 main


===
https://packages-cf.termux.org/apt/

Index of /apt/

../
termux-games/                                      06-Jul-2021 18:03                   -
termux-main/                                       07-Mar-2022 11:01                   -
termux-root/                                       07-Mar-2022 10:52                   -
termux-science/                                    06-Jul-2021 18:04                   -
termux-unstable/                                   24-Oct-2021 18:26                   -
termux-x11/                                        07-Mar-2022 10:55                   -


===
https://packages-cf.termux.org/apt/termux-main/

Index of /apt/termux-main/

../
dists/                                             07-Mar-2022 11:01                   -
pool/                                              07-Mar-2022 11:01                   -
]]
[[24>23 不行，没有23
https://mirror.bardia.tech/termux/
 [PARENTDIR]	Parent Directory	 	- 	 
[DIR]	game-packages-24/	2022-02-15 20:47 	- 	 
[DIR]	science-packages-24/	2022-02-15 20:47 	- 	 
[DIR]	termux-packages-24/	2022-02-15 20:47 	- 	 
[DIR]	termux-root-packages-24/	2022-02-15 20:47 	- 	 
[DIR]	unstable-packages/	2022-02-15 20:47 	- 	 
[DIR]	x11-packages/	2022-02-15 20:47 	- 	 
]]

===
[[[
https://groups.io/g/termux/topic/83337945#590


Groups.io

    Topics when pkg upgrade killed { ls, mv, cp, head, ... }, PHP becomes file-manager. 

Date
when pkg upgrade killed { ls, mv, cp, head, ... }, PHP becomes file-manager.
Ahmed Ferzan/Ferzen R <zelqarneyn@...>
6/06/21  

After updating the list of repositories, pkg finally seemed to be able to do upgrade, as it used to. However, after downloading the packages, the trouble(s) surfaced, & upgrades were not doable.

Worse, some of the existing commands started not to work. For example,

$ ls
WARNING: linker: ls: unused DT entry: type 0x1d arg 0xcdd
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x178
WARNING: linker: /data/data/com.termux/files/usr/lib/libgmp.so: unused DT entry: type 0x1d arg 0x2981
CANNOT LINK EXECUTABLE: cannot locate symbol "__write_chk" referenced by "ls"...
page record for 0x7fa20d3010 was not found (block_size=16)


A good news is, {apache/httpd, bash, clang, kill, php, ...} keep working (hopefully, a further attempt with pkg won't take them away, too). Therefore,  cgi scripts & programmatic alternatives to the lost facilties is still possible. For example, getting to PHP shell (with "php -a"),
----
function ls($dirname) { $dir=scandir($dirname); $count = count($dir); for ($i = 0; $i < count($dir) ; $i++) {echo $dir[$i] . " \n";} return $count; }
$px = '/data/data/com.termux/files/usr';
ls($px);
ls($px . '/etc');
----

If the PHP has ncurses, a file-manager is thinkable with that, too.

BTW, a request-for-feature I already had before this happened, was having a short description (one-liner, or so) for each package that pkg lists (that is, not having to firstly install (to read man/info) and/or find through internet), for example, if there is a text-mode file-manager in the list, then I would like to know that, instead of programming the wheel from scratch.



More
Henrik Grimler
6/06/21  

lör 2021-06-05 klockan 16:25 +0000 skrev Ahmed Ferzan/Ferzen R:

    After updating the list of repositories, pkg finally seemed to be
    able to do upgrade, as it used to. However, after downloading the
    packages, the trouble(s) surfaced, & upgrades were not doable.

What repositories were you using before? 
What repositories are you using now?


    $ ls
    WARNING: linker: ls: unused DT entry: type 0x1d arg 0xcdd
    WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-
    support.so: unused DT entry: type 0x1d arg 0x178
    WARNING: linker: /data/data/com.termux/files/usr/lib/libgmp.so:
    unused DT entry: type 0x1d arg 0x2981
    CANNOT LINK EXECUTABLE: cannot locate symbol "__write_chk" referenced
    by "ls"...
    page record for 0x7fa20d3010 was not found (block_size=16)


What android version are you using?

Best regards,
Henrik Grimler

More
Ahmed Ferzan/Ferzen R <zelqarneyn@...>
6/08/21  

Dear Mr. Grimler,

As concerns your questions after my previous mail,

(1) The first question is presumably not the issue (other than perhaps my needing the older version(s) of some package(s)) because it mainly replaced bintray repositories. Previously, I was using the default repositories that Termux (from playstore, in 2020) had installed, namely,
----
# The main termux repository:
#  deb https://termux.net stable main
deb https://grimler.se/termux-packages-24 stable main
deb https://grimler.se/game-packages-24 games stable
deb https://grimler.se/termux-root-packages-24 root stable
deb https://grimler.se/science-packages-24 science stable
deb https://grimler.se/unstable-packages unstable main
deb https://grimler.se/x11-packages x11 main
----
# https://dl.bintray.com/grimler/game-packages-21 games stabledeb
https://grimler.se/game-packages-24 games stable
----
# This had been corrected/updated in April2021, already,
#    w.r.t. your response to my question. No problem with it.
deb https://its-pointless.github.io/files/21  termux extras
----
# deb https://dl.bintray.com/grimler/science-packages-21 science stable
deb https://grimler.se/science-packages-24 science stable


(2) The second question may be a problem in your view, as your documents/responses suggest android versions 7-to-9 mostly, while mine is 6 (& termux is from playstore, not F-droid, for making do with what works, as far as it works, & I presume that your F-droid version installs the same app id, & therefore the two cannot co-exist). If the trouble is some library that presumes at least version7, then may I find the older version of that library (or, if it is optional, then I may un-install that library entirely)? BTW, I'm sorry for taking your attention-&-time because of my sticking with the older stuff you suggest leaving (I can make things somehow work, anyway, & may have fun as that is diversion even when not big challenge, but causing you also attend to it, starts to feel weird/sorry).






More
Henrik Grimler
6/08/21  

Hi Ahmed,

On Mon, 2021-06-07 at 16:01 +0000, Ahmed Ferzan/Ferzen R wrote:

    Dear Mr. Grimler,

    # https://dl.bintray.com/grimler/game-packages-21 games stabledeb
    https://grimler.se/game-packages-24 games stable
    ----
    # deb https://dl.bintray.com/grimler/science-packages-21 science stable
    deb https://grimler.se/science-packages-24 science stable

You can't use repositories targeting API level 24 (corresponding to
android 7) on android 6. Doing so will give the type of error that you
are experiencing as well as other issues.

    (2) The second question may be a problem in your view, as your
    documents/responses suggest android versions 7-to-9 mostly, while mine
    is 6 (& termux is from playstore, not F-droid, for making do with what
    works, as far as it works, & I presume that your F-droid version
    installs the same app id, & therefore the two cannot co-exist). If the
    trouble is some library that presumes at least version7, then may I
    find the older version of that library (or, if it is optional, then I
    may un-install that library entirely)? 

To get back to a working termux you basically need to re-install the
app to remove all the installed packages targeting android 7. 

Instead of switching to the *-24 repositories you should use termux.net
for the main repo (this is default in the android <7 app so no need to
change anything) and then https://termux.com/science-packages-21-bin
for the science repo and https://termux.com/game-packages-21-bin for
the game repo (see readmes [1], [2]).

Best regards,
Henrik Grimler

[1] https://github.com/termux/science-packages-21-bin
[2] https://github.com/termux/game-packages-21-bin

More
Henrik Grimler
6/08/21  

What steps have you taken from the previous email? Have you re-
installed the app fully to get rid of all the broken packages?

The repos are fine, in your case it looks like apt/gpg, or apt's trust
database, is broken for some reason.
toggle quoted messageShow quoted text

More
Henrik Grimler
6/09/21  

Hi Ahmed,

On Tue, Jun 08, 2021 at 04:14:55PM +0000, Ahmed Ferzan/Ferzen R wrote:

    I did not do anything extra.  With 24 packages, pkg had done downloads, & then broke something that caused ls/mv/cp/head/mkdir/rmdir not to work (& other apps warn that android.support.so & something else) have problems, but then those apps continue to work). So, there isn't any app I know as the problem here. I cannot un-install shell facilities, & they are not the cause, they are victims of their dependency[ies] on whatever library causes this.

    BTW, now attempting it, it turns out that uninstalling the package libandroid-support causes uninstalling lots of packages (such as apache2 that actually keeps working). Attempt to reinstall'ing causes refusal that reports non-downloadability of the package: "Reinstallation of libandroid-support is not possible, it cannot be downloaded."

I am confused, have you, or have you not, reinstalled termux to restore all packages to the -21 variants? Lots of packages depend on libandroid-support, so makes sense that you cannot remove it.

More
Ahmed Ferzan/Ferzen R <zelqarneyn@...>
6/09/21  

Thanks for that extra information, however, now pkg/apt again refuses to upgrade.
--------
    $ pkg upgrade
Get:1 https://termux.net stable InRelease [1720 B]
Ign:2 https://termux.com/game-packages-21-bin games InRelease
Hit:3 https://its-pointless.github.io/files/21 termux InRelease
Ign:4 https://termux.com/science-packages-21-bin science InRelease
Err:1 https://termux.net stable InRelease
  At least one invalid signature was encountered.
Get:5 https://termux.com/game-packages-21-bin games Release [5344 B]
Get:6 https://termux.com/science-packages-21-bin science Release [5348 B]
Err:3 https://its-pointless.github.io/files/21 termux InRelease
  At least one invalid signature was encountered.
Get:7 https://termux.com/game-packages-21-bin games Release.gpg [475 B]
Get:8 https://termux.com/science-packages-21-bin science Release.gpg [475 B]
Ign:7 https://termux.com/game-packages-21-bin games Release.gpg
Ign:8 https://termux.com/science-packages-21-bin science Release.gpg
Reading package lists... Done
W: GPG error: https://termux.net stable InRelease: At least one invalid signature was encountered.
E: The repository 'https://termux.net stable InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://its-pointless.github.io/files/21 termux InRelease: At least one invalid signature was encountered.
W: GPG error: https://termux.com/game-packages-21-bin games Release: At least one invalid signature was encountered.
E: The repository 'https://termux.com/game-packages-21-bin games Release' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
W: GPG error: https://termux.com/science-packages-21-bin science Release: At least one invalid signature was encountered.
E: The repository 'https://termux.com/science-packages-21-bin science Release' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
--------

Presumably, somethings have changed in those repositories, that is, not working like how pkg/apt used to work in mid-2020.



Scarica Outlook per Android
toggle quoted messageShow quoted text

More
Ahmed Ferzan/Ferzen R <zelqarneyn@...>
6/09/21  

I did not do anything extra.  With 24 packages, pkg had done downloads, & then broke something that caused ls/mv/cp/head/mkdir/rmdir not to work (& other apps warn that android.support.so & something else) have problems, but then those apps continue to work). So, there isn't any app I know as the problem here. I cannot un-install shell facilities, & they are not the cause, they are victims of their dependency[ies] on whatever library causes this.

BTW, now attempting it, it turns out that uninstalling the package libandroid-support causes uninstalling lots of packages (such as apache2 that actually keeps working). Attempt to reinstall'ing causes refusal that reports non-downloadability of the package: "Reinstallation of libandroid-support is not possible, it cannot be downloaded."




Scarica Outlook per Android

toggle quoted messageShow quoted text

More
1 - 8 of 8 	  	

    previous page
    1
    next page

]]]

]]]]]
[[[[[
At least one invalid signature was encountered.
/data/data/com.termux/files/usr/var/lib/apt/lists/

===
https://stackoverflow.com/questions/62473932/atleast-one-invalid-signature-was-encountered#:~:text=The%20error%20suggests%20that%20one%20of%20the%20files,the%20whole%20file%2C%20so%20it%20can%20be%20recreated.

docker - Atleast one invalid signature was …

The error suggests that one of the files in /var/lib/apt/lists consist at least one invalid/corrupted signature (could be the result of apt-key misuse or something else). Edit the file, find and remove the corrupted parts, or remove the whole file, so it can be recreated.

]]]]]

[[[[[
连ls/rm都无法使用了...
CANNOT LINK EXECUTABLE: cannot locate symbol "__fwrite_chk" referenced by "ls"...


===
https://blog.csdn.net/qwaszx523/article/details/52778558
adb 查看Android版本号和SDK版本号

获取系统版本：
  adb shell getp ro p ro.build.version.release
获取系统api版本：
  adb shell getp ro p ro.build.version.sdk.

===
e others/app/termux/Android_system_properties.txt

avdmanager: command not found
$ android list target
android: command not found
$ getprop ro.build.version.release
6.0
$ getprop ro.build.version.codename
REL

$ getprop --help
usage: getprop [NAME [DEFAULT]]

Gets an Android system property, or lists them all.



$ echo $my_tmp
/sdcard/0my_files/tmp/
getprop > /sdcard/0my_files/tmp/getprop.txt
view  /sdcard/0my_files/tmp/getprop.txt
[[摘要 Android 6.0 SDK-API 23
[ro.build.version.all_codenames]: [REL]
[ro.build.version.base_os]: []
[ro.build.version.codename]: [REL]
[ro.build.version.freemeos]: [6.2]
[ro.build.version.incremental]: [1558425897]
[ro.build.version.preview_sdk]: [0]
[ro.build.version.release]: [6.0]
[ro.build.version.sdk]: [23]
[ro.build.version.security_patch]: [2017-06-05]

]]
[[全部
[af.music.outputid]: [3]
[af.rf_info]: [273]
[bgw.current3gband]: [0]
[camera.appguide.enable]: [0]
[camera.disable_zsl_mode]: [1]
[cdma.icc.operator.mcc]: [460]
[cdma.operator.ltmoffset]: [32]
[cdma.operator.mcc]: [460]
[cdma.operator.sid]: [13828]
[cdma.ril.eboot]: [0]
[cdma.ril.ecclist]: [110,119,120,112]
[cdma.version.baseband]: [SIXTH.CBP.MD.MP2.V41_P19, 2020/08/24 17:03]
[dalvik.vm.dex2oat-Xms]: [64m]
[dalvik.vm.dex2oat-Xmx]: [512m]
[dalvik.vm.heapgrowthlimit]: [128m]
[dalvik.vm.heapsize]: [256m]
[dalvik.vm.image-dex2oat-Xms]: [64m]
[dalvik.vm.image-dex2oat-Xmx]: [64m]
[dalvik.vm.isa.arm.features]: [default]
[dalvik.vm.isa.arm.variant]: [cortex-a53]
[dalvik.vm.mtk-stack-trace-file]: [/data/anr/mtk_traces.txt]
[dalvik.vm.stack-trace-file]: [/data/anr/traces.txt]
[debug.MB.running]: [0]
[debug.atrace.tags.enableflags]: [0]
[debug.force_rtl]: [0]
[debug.hwc.bq_count]: [4]
[debug.hwc.compose_level]: [0]
[debug.hwui.render_dirty_regions]: [false]
[debug.mdlogger.Running]: [0]
[debug.mdlogger.log2sd.path]: [internal_sd]
[debug.mtklog.netlog.Running]: [0]
[debug.program_binary.enable]: [1]
[dev.bootcomplete]: [1]
[drm.service.enabled]: [true]
[fmradio.driver.enable]: [1]
[gsm.baseband.capability]: [503]
[gsm.current.phone-type]: [2,1,,,,,,,,,1,2]
[gsm.defaultpdpcontext.active]: [true]
[gsm.gcf.testmode]: [0]
[gsm.network.type]: [LTE]
[gsm.nitz.time]: [1651010295126]
[gsm.operator.alpha]: [中国电信]
[gsm.operator.alpha.2]: []
[gsm.operator.idpstring]: [00]
[gsm.operator.iso-country]: [cn,,,,,,,,,,cn]
[gsm.operator.isroaming]: [false]
[gsm.operator.numeric]: [46003,,,,,,,,,,46011]
[gsm.project.baseband]: [DROI6737M_65_M0_HW(DEFAULT)]
[gsm.project.baseband.2]: [DROI6737M_65_M0_HW(DEFAULT)]
[gsm.ril.cardtypeset]: [1]
[gsm.ril.cardtypeset.2]: [1]
[gsm.ril.ct3g]: [0]
[gsm.ril.ct3g.2]: [0]
[gsm.ril.eboot]: [-1]
[gsm.ril.fulluicctype]: [USIM,UIM,CSIM]
[gsm.ril.fulluicctype.2]: []
[gsm.ril.init]: [0]
[gsm.ril.sst.mccmnc]: [46011]
[gsm.ril.uicctype]: [CSIM]
[gsm.ril.uicctype.2]: []
[gsm.serial]: [Y8A031000020                                               P10 ]
[gsm.sim.operator.alpha]: [中国电信]
[gsm.sim.operator.default-name]: [中国电信]
[gsm.sim.operator.imsi]: [460115035193340]
[gsm.sim.operator.iso-country]: [cn]
[gsm.sim.operator.numeric]: [46003]
[gsm.sim.retry.pin1]: [3]
[gsm.sim.retry.pin1.2]: []
[gsm.sim.retry.pin2]: [3]
[gsm.sim.retry.pin2.2]: []
[gsm.sim.retry.puk1]: [10]
[gsm.sim.retry.puk1.2]: []
[gsm.sim.retry.puk2]: [10]
[gsm.sim.retry.puk2.2]: []
[gsm.sim.ril.mcc.mnc]: []
[gsm.sim.ril.mcc.mnc.2]: []
[gsm.sim.ril.phbready]: [true]
[gsm.sim.ril.phbready.2]: []
[gsm.sim.ril.testsim]: [0]
[gsm.sim.state]: [READY,ABSENT]
[gsm.simswitch.offmd1]: [0]
[gsm.version.baseband]: [MOLY.LR9.W1444.MD.LWTG.MP.V88.P124, 2019/05/21 16:02]
[gsm.version.baseband1]: [MOLY.LR9.W1444.MD.LWTG.MP.V88.P124, 2019/05/21 16:02]
[gsm.version.ril-impl]: [mtk gemini ril 1.0]
[init.svc.MtkCodecService]: [running]
[init.svc.NativeMisc]: [running]
[init.svc.NvRAMAgent]: [running]
[init.svc.NvRAMBackup]: [running]
[init.svc.PPLAgent]: [running]
[init.svc.adbd]: [running]
[init.svc.agpsd]: [running]
[init.svc.batterywarning]: [running]
[init.svc.bootanim]: [stopped]
[init.svc.bootlogoupdater]: [stopped]
[init.svc.ccci_fsd]: [running]
[init.svc.ccci_mdinit]: [running]
[init.svc.cmddumper]: [running]
[init.svc.conn_launcher]: [running]
[init.svc.console]: [running]
[init.svc.cus_attr_service]: [stopped]
[init.svc.debuggerd]: [running]
[init.svc.drm]: [running]
[init.svc.efused_loader]: [stopped]
[init.svc.emdlogger1]: [running]
[init.svc.emsvr_user]: [running]
[init.svc.enableswap]: [stopped]
[init.svc.epdg_wod]: [running]
[init.svc.fingerprintd]: [running]
[init.svc.flash_recovery]: [stopped]
[init.svc.fuelgauged]: [running]
[init.svc.gas_srv]: [running]
[init.svc.gatekeeperd]: [running]
[init.svc.ged_srv]: [running]
[init.svc.gsm0710muxd]: [running]
[init.svc.guiext-server]: [running]
[init.svc.healthd]: [running]
[init.svc.installd]: [running]
[init.svc.ipsec_mon]: [running]
[init.svc.keystore]: [running]
[init.svc.lmkd]: [running]
[init.svc.logd]: [running]
[init.svc.logd-reinit]: [stopped]
[init.svc.mal-daemon]: [running]
[init.svc.media]: [running]
[init.svc.memsicp]: [running]
[init.svc.mnld]: [running]
[init.svc.mobile_log_d]: [running]
[init.svc.msensord]: [stopped]
[init.svc.netd]: [running]
[init.svc.netdiag]: [running]
[init.svc.nvram_daemon]: [stopped]
[init.svc.pq]: [running]
[init.svc.program_binary]: [running]
[init.svc.ril-daemon]: [stopped]
[init.svc.ril-daemon-mtk]: [running]
[init.svc.servicemanager]: [running]
[init.svc.slpd]: [running]
[init.svc.sn]: [stopped]
[init.svc.statusd]: [running]
[init.svc.surfaceflinger]: [running]
[init.svc.terservice]: [stopped]
[init.svc.thermal]: [running]
[init.svc.thermal_manager]: [stopped]
[init.svc.thermald]: [running]
[init.svc.ueventd]: [running]
[init.svc.vold]: [running]
[init.svc.volte_imcb]: [stopped]
[init.svc.volte_stack]: [stopped]
[init.svc.volte_ua]: [stopped]
[init.svc.vtservice]: [running]
[init.svc.wfca]: [running]
[init.svc.wifi2agps]: [running]
[init.svc.wmtLoader]: [stopped]
[init.svc.xlogboot]: [stopped]
[init.svc.xlogdebugchanged]: [stopped]
[init.svc.zygote]: [running]
[media.wfd.portrait]: [0]
[media.wfd.video-format]: [5]
[mediatek.wlan.chip]: [CONSYS_MT6735]
[mediatek.wlan.ctia]: [0]
[mediatek.wlan.module.postfix]: [_consys_mt6735]
[mtk.md1.starttime]: [0s Wed Apr 27 05:57:53 2022
]
[mtk.md1.status]: [ready]
[mtk.md3.status]: [ready]
[mtk.vdec.waitkeyframeforplay]: [1]
[net.bt.name]: [Android]
[net.cdma.boottimes]: [2]
[net.cdma.mdmstat]: [ready]
[net.cdma.poker]: [red.joker]
[net.cdma.via.card.state]: [valid]
[net.cdma.via.service.state]: [in service]
[net.change]: [net.cdma.via.service.state]
[net.dns1]: [202.96.134.33]
[net.dns2]: [240e:1f:1::1]
[net.dns3]: [202.96.128.166]
[net.dns4]: [240e:1f:1::33]
[net.hostname]: [android-e7107983c7b8e75f]
[net.ims.ipsec.version]: [2.0]
[net.ipv6.ccmni0.plen]: [64]
[net.ipv6.ccmni0.prefix]: [240e:47d:c0e:b5e0::]
[net.nsiot_pending]: [false]
[net.perf.cpu.core]: [4,4,0,0]
[net.perf.cpu.freq]: [1144000,1144000,0,0]
[net.perf.rps]: [ff]
[net.qtaguid_enabled]: [1]
[net.tcp.default_init_rwnd]: [60]
[persist.datashaping.alarmgroup]: [1]
[persist.freeme.product.model]: []
[persist.gemini.sim_num]: [2]
[persist.main.attach.state]: [1]
[persist.meta.dumpdata]: [0]
[persist.mtk.datashaping.support]: [1]
[persist.mtk.ims.video.enable]: [0]
[persist.mtk.volte.enable]: [0]
[persist.mtk.wcn.combo.chipid]: [0x0321]
[persist.mtk_dynamic_ims_switch]: [1]
[persist.radio.actual.svlte_slot]: [3,2]
[persist.radio.capability.iccid]: [89860321750207267777]
[persist.radio.cdma.msgid]: [9]
[persist.radio.cdma_slot]: [1]
[persist.radio.cfu.change.0]: [0]
[persist.radio.cfu.change.1]: [1]
[persist.radio.cfu.iccid.0]: [89860321750207267777]
[persist.radio.cfu.iccid.1]: [89860121801128693542]
[persist.radio.cfu.timeslot.0]: []
[persist.radio.cfu.timeslot.1]: []
[persist.radio.data.iccid]: [89860321750207267777]
[persist.radio.default.sim]: [0]
[persist.radio.fd.counter]: [15]
[persist.radio.fd.off.counter]: [5]
[persist.radio.fd.off.r8.counter]: [5]
[persist.radio.fd.r8.counter]: [15]
[persist.radio.flashless.fsm]: [0]
[persist.radio.flashless.fsm_cst]: [0]
[persist.radio.flashless.fsm_rw]: [0]
[persist.radio.gemini_support]: [1]
[persist.radio.ia]: [89860321750207267777,IPV4V6,3,,0]
[persist.radio.ia-apn]: [ctlte]
[persist.radio.ia-pwd-flag]: [0]
[persist.radio.mobile.data]: [89860321750207267777,0]
[persist.radio.mtk_dsbp_support]: [1]
[persist.radio.multisim.config]: [dsds]
[persist.radio.new.sim.slot]: []
[persist.radio.re.ia-apn]: []
[persist.radio.re.ia.flag]: [0]
[persist.radio.reset_on_switch]: [true]
[persist.radio.sim.sbp]: [9]
[persist.radio.sim.status]: []
[persist.radio.simswitch]: [1]
[persist.radio.simswitch.iccid]: [89860321750207267777]
[persist.radio.svlte.mode]: [svlte]
[persist.radio.svlte_slot]: [3,2]
[persist.radio.terminal-based.cw]: [disabled_tbcw]
[persist.radio.unlock]: [false]
[persist.radio.ut.cfu.mode]: [disabled_ut_cfu_mode]
[persist.ril.bip.disabled]: [0]
[persist.service.acm.enable]: [0]
[persist.service.bdroid.bdaddr]: [22:22:da:ba:bb:85]
[persist.service.stk.shutdown]: [0]
[persist.sys.ams.recover]: [false]
[persist.sys.bootpackage]: [1]
[persist.sys.cus_attr.brand]: [Changhong]
[persist.sys.cus_attr.bt]: [ChanghongS16]
[persist.sys.cus_attr.cpu]: [030]
[persist.sys.cus_attr.hotwlan]: [ChanghongS16]
[persist.sys.cus_attr.init]: [0]
[persist.sys.cus_attr.lcm]: [0]
[persist.sys.cus_attr.model]: [ChanghongS16]
[persist.sys.cus_attr.ram]: [33]
[persist.sys.cus_attr.rom]: [32]
[persist.sys.cus_attr.rom_free]: [1.0]
[persist.sys.cus_attr.runrom]: [32:3]
[persist.sys.dLVEBAKwf.JEBWMgfV]: [mhEGGZEaTcGZcaj]
[persist.sys.dLVEBdLLKV.EeWstLB]: [mhEGGZEaaimjaEE]
[persist.sys.dLVECBWysLWyEeMMEV]: [mhEGGZEahiiEZEm]
[persist.sys.dLVEceBsgEu.etdzcL]: [mhEGGZEaZEiEZci]
[persist.sys.dLVEeWstLBsEwKuzes]: [mhEGGZEahhmaihZ]
[persist.sys.dLVEegfLWeRBEVBWBV]: [mhEGGZEaZihcTjZ]
[persist.sys.dLVEf.Wd.WfESBABVe]: [mhEGGZEaGZaiEhc]
[persist.sys.dLVEgV.EctLSu.t]: [mhEGGZEacjZcGjc]
[persist.sys.dLVEueWJgeBEV.Bfge]: [mhEGGZEaGEccmiG]
[persist.sys.dLVEuuEeWstLBsEetf]: [mhEGGZEahaGcmhT]
[persist.sys.dWE.fLgdzE.deK.Wse]: [mhEGGZEaajZciTa]
[persist.sys.dWEJgSLEMKew.t]: [mhEGGZEajjaTaZG]
[persist.sys.dalvik.vm.lib.2]: [libart.so]
[persist.sys.display_tasks]: [5]
[persist.sys.first_time_boot]: [false]
[persist.sys.main.interpolation]: [800]
[persist.sys.mdLVEBAKwf.JEBWMgf]: [aSYfUaUUNSfB]
[persist.sys.mdLVEBdLLKV.EeWstL]: [aSYfUaaOOJUJ]
[persist.sys.mdLVECBWysLWyEeMME]: [aSYfUaKJNJKO]
[persist.sys.mdLVEceBsgEu.etdzc]: [aSYfUaEbbBBU]
[persist.sys.mdLVEeWstLBsEwKuze]: [aSYfUaZZKNZY]
[persist.sys.mdLVEegfLWeRBEVBWB]: [aSYfUaYOURBS]
[persist.sys.mdLVEf.Wd.WfEDDKBR]: [aSYfUaESFYZE]
[persist.sys.mdLVEf.Wd.WfESBABV]: [aSYfUaZFJBfj]
[persist.sys.mdLVEgV.EctLSu.t]: [aSYfUaNZSKff]
[persist.sys.mdLVEueWJgeBEV.Bfg]: [aSYfUaNSUYRR]
[persist.sys.mdLVEuuEeWstLBsEet]: [aSYfUaBBSBBB]
[persist.sys.mdWE.fLgdzE.deK.Ws]: [aSYfUaKRjBYa]
[persist.sys.mdWEJgSLEMKew.t]: [aSYfUaYaSFBN]
[persist.sys.mute.state]: [2]
[persist.sys.pq.adl.idx]: [0]
[persist.sys.pq.shp.idx]: [2]
[persist.sys.profiler_ms]: [0]
[persist.sys.sd.defaultpath]: [/storage/emulated/0]
[persist.sys.sub.interpolation]: [200]
[persist.sys.timezone]: [Asia/Shanghai]
[persist.sys.usb.config]: [mtp,adb]
[qemu.hw.mainkeys]: [0]
[ril.active.md]: [5]
[ril.cardtype.cache]: [8]
[ril.cdma.emdstatus.send]: [1]
[ril.cdma.meid]: [a100005d97092f]
[ril.cdma.report]: [0]
[ril.cdma.report.case]: [0]
[ril.cdma.switching]: [0]
[ril.current.share_modem]: [2]
[ril.data.allow]: [0]
[ril.data.mal]: [0]
[ril.ecc.service.category.list]: [;119,4;110,1;120,2;122,8;12119,16]
[ril.ecc.service.category.list.1]: []
[ril.ecc.service.category.mcc]: [460]
[ril.ecclist]: [;112,0;911,0]
[ril.ecclist1]: []
[ril.external.md]: [1]
[ril.fd.mode]: [1]
[ril.first.md]: [1]
[ril.flightmode.poweroffMD]: [1]
[ril.getccci.response]: [1]
[ril.ia.network]: [ctlte.MNC011.MCC460.GPRS]
[ril.iccid.sim1]: [89860321750207267777]
[ril.iccid.sim1_c2k]: [89860321750207267777]
[ril.iccid.sim2]: [N/A]
[ril.imei.sim1]: [860224034672753]
[ril.imei.sim2]: [860224034672761]
[ril.imsi.status.sim1]: [1]
[ril.imsi.status.sim2]: [0]
[ril.ipo.radiooff]: [0]
[ril.ipo.radiooff.2]: [0]
[ril.mal.flag]: [0]
[ril.mux.ee.md1]: [0]
[ril.mux.report.case]: [0]
[ril.pdn.reuse]: [1]
[ril.pid.1]: [5281]
[ril.radiooff.poweroffMD]: [0]
[ril.read.imsi]: [1]
[ril.ready.sim]: [true]
[ril.specific.sm_cause]: [0]
[ril.switch.modem.cause.type]: [255]
[ril.switch.modem.delay.info]: ["FFFFFF",255,0]
[ril.telephony.mode]: [0]
[ril.volte.mal.latency]: [65535]
[ril.volte.mal.opkey]: [0x0001]
[ril.volte.mal.pkterrth]: [99]
[ril.volte.mal.rb_hoddc_t]: [3]
[ril.volte.mal.rb_hol2w_t]: [10]
[ril.volte.mal.rb_how2l_t]: [150]
[ril.volte.mal.retranth]: [99]
[ril.volte.mal.throupt]: [65535]
[ril.volte.mal.vijit]: [3]
[ril.volte.mal.vojit]: [26]
[rild.libargs]: [-d /dev/ttyC0]
[rild.libpath]: [mtk-ril.so]
[rild.mark_switchuser]: [0]
[ro.adb.secure]: [1]
[ro.allow.mock.location]: [0]
[ro.audio.silent]: [0]
[ro.baseband]: [unknown]
[ro.board.platform]: [mt6737t]
[ro.board.vplatform]: [n41acl_37tlf]
[ro.boot.bootreason]: [power_key]
[ro.boot.hardware]: [mt6735]
[ro.boot.mode]: [normal]
[ro.boot.name]: [android]
[ro.boot.serialno]: [MNMFZ5VOFM8TN7JF]
[ro.bootimage.build.date]: [Tue May 21 16:23:26 CST 2019]
[ro.bootimage.build.date.utc]: [1558427006]
[ro.bootimage.build.fingerprint]: [alps/full_n41acl_37tlf/n41acl_37tlf:6.0/MRA58K/1558425897:user/test-keys]
[ro.bootloader]: [unknown]
[ro.bootmode]: [normal]
[ro.build.characteristics]: [default]
[ro.build.date]: [Tue May 21 16:15:26 CST 2019]
[ro.build.date.utc]: [1558426526]
[ro.build.description]: [full_n41acl_37tlf-user 6.0 MRA58K 1558425897 test-keys]
[ro.build.display.id]: [ChanghongS16_201905211600]
[ro.build.fingerprint]: [alps/full_n41acl_37tlf/n41acl_37tlf:6.0/MRA58K/1558425897:user/test-keys]
[ro.build.flavor]: [mt6737atvdroi_n41acl_s16j_changhong_cc_256gbitp24d3_m_lte_6m-cs]
[ro.build.freemeos_brand_no]: [CHANGHONG]
[ro.build.freemeos_channel_no]: [CHANGHONG_FANZHUO]
[ro.build.freemeos_customer_br]: [Droi_S16]
[ro.build.freemeos_customer_no]: [CHANGHONG]
[ro.build.freemeos_label]: [FreemeOS]
[ro.build.host]: [v99]
[ro.build.id]: [MRA58K]
[ro.build.ota.product]: [CHANGHONG_S16_zh_vanzo]
[ro.build.product]: [ChanghongS16]
[ro.build.tags]: [test-keys]
[ro.build.tyd.custom.hw_version]: []
[ro.build.tyd.production]: [1]
[ro.build.type]: [user]
[ro.build.user]: [scm]
[ro.build.version.all_codenames]: [REL]
[ro.build.version.base_os]: []
[ro.build.version.codename]: [REL]
[ro.build.version.freemeos]: [6.2]
[ro.build.version.incremental]: [1558425897]
[ro.build.version.preview_sdk]: [0]
[ro.build.version.release]: [6.0]
[ro.build.version.sdk]: [23]
[ro.build.version.security_patch]: [2017-06-05]
[ro.c2k.irat.support]: [1]
[ro.camera.sound.forced]: [0]
[ro.carrier]: [unknown]
[ro.cdma.cfall.disable]: [*730]
[ro.cdma.cfb.disable]: [*900]
[ro.cdma.cfb.enable]: [*90]
[ro.cdma.cfdf.disable]: [*680]
[ro.cdma.cfdf.enable]: [*68]
[ro.cdma.cfnr.disable]: [*920]
[ro.cdma.cfnr.enable]: [*92]
[ro.cdma.cfu.disable]: [*720]
[ro.cdma.cfu.enable]: [*72]
[ro.cdma.cw.disable]: [*740]
[ro.cdma.cw.enable]: [*74]
[ro.com.android.mobiledata]: [false]
[ro.com.google.clientidbase]: [android-{country}]
[ro.com.google.clientidbase.am]: [android-{country}]
[ro.com.google.clientidbase.gmm]: [android-{country}]
[ro.com.google.clientidbase.ms]: [android-{country}]
[ro.com.google.clientidbase.yt]: [android-{country}]
[ro.compatible.accelerometer]: [mxc400x-new@qma6981-new@mc3xxx_auto]
[ro.compatible.alsps]: [stk3x1x@epl259x-new@epl8854]
[ro.compatible.fingerprint]: [@]
[ro.compatible.flashlight]: [constant_flashlight]
[ro.compatible.gyroscope]: [@]
[ro.compatible.hall]: [@]
[ro.compatible.irda]: [abov]
[ro.compatible.lcm]: [ili9881d_hsd50_kyd_hd@ili9881d_hsd50_hongzhan_hd]
[ro.compatible.leds]: [mt65xx]
[ro.compatible.lens]: [dummy_lens@fm50af@dw9714af@dw9761af]
[ro.compatible.magnetometer]: [@]
[ro.compatible.mainimgsensor]: [ov13853_mipi_raw@s5k3l8_mipi_raw]
[ro.compatible.memory]: [KMR21000BM_B809@KMRX1000BM_B614@MT29TZZZ7D7EKKBT_107W_97V@H9TQ26ADFTACUR_KUM@KMR31000BM_B6]
[ro.compatible.subimgsensor]: [gc8024mipi_raw]
[ro.compatible.touchpanel]: [msg2836a@gslx68x_37pre_ali@GT1X]
[ro.compatible.vibrator]: [vibrator]
[ro.config.alarm_alert]: [Alarm_Lights.ogg]
[ro.config.default.fake_value]: [32:3;ChanghongS16;Changhong;3;32;ChanghongS16;ChanghongS16;800;200;0;030;1.0;]
[ro.config.message_sound]: [sms-received3.ogg]
[ro.config.notification_sound]: [Proxima.ogg]
[ro.config.real.ram]: [3]
[ro.config.real.rom]: [32]
[ro.config.ringtone]: [happy.ogg]
[ro.config.ringtone_sim2]: [happy.ogg]
[ro.config.switch.fake_model]: [false]
[ro.config.switch.fake_ram]: [true]
[ro.config.switch.fake_rom]: [true]
[ro.crypto.state]: [unencrypted]
[ro.custom.build.version]: [1558425897]
[ro.dalvik.vm.native.bridge]: [0]
[ro.debuggable]: [1]
[ro.droi_mmi_theme_font]: [1]
[ro.droi_smart_sms_support]: [1]
[ro.efused]: [no]
[ro.expect.recovery_id]: [0xac5751f3beceae9b61db59da51abcce07b690c33000000000000000000000000]
[ro.fo_fmode_fcamera]: [1]
[ro.fo_fmode_gps]: [1]
[ro.fo_fmode_gsensor]: [1]
[ro.fo_fmode_lsensor]: [1]
[ro.fo_fmode_strobe_back]: [1]
[ro.fo_fmode_wifi]: [1]
[ro.fo_sc_permission_control]: [1]
[ro.fo_sc_permission_permium]: [1]
[ro.fo_sc_shutdown_clear]: [1]
[ro.fo_sc_static_uninstall]: [1]
[ro.fo_security_bpm]: [1]
[ro.fo_security_hi]: [1]
[ro.fo_security_mreceiver]: [1]
[ro.fo_security_notifi]: [1]
[ro.fo_security_number_markers]: [1]
[ro.freeme.auto_generate_mac]: [1]
[ro.freeme.biglauncher]: [1]
[ro.freeme.channel_info_support]: [1]
[ro.freeme.extreme_lk_trim]: [1]
[ro.freeme.hw_camera_back]: [1]
[ro.freeme.hw_sensor_proximity]: [1]
[ro.freeme.navigationbar_min]: [1]
[ro.freeme.nyx_version]: [1]
[ro.freeme.reverse_dial_silent]: [1]
[ro.freeme.sc_home]: [1]
[ro.freeme.security_as]: [1]
[ro.freeme.smart_dial_answer]: [1]
[ro.freeme.ss_applist]: [1]
[ro.freeme.ss_filter]: [1]
[ro.freeme.ss_float]: [1]
[ro.freeme.ss_hide]: [1]
[ro.freeme.ss_install]: [1]
[ro.freeme.ss_troi]: [1]
[ro.freeme.vib_tuner_support]: [1]
[ro.freeme.wifi_enhancement]: [1]
[ro.freeme_legalnotices]: [1]
[ro.frp.pst]: [/dev/block/platform/mtk-msdc.0/11230000.msdc0/by-name/frp]
[ro.gemini.smart_sim_switch]: [false]
[ro.hardware]: [mt6735]
[ro.have_aacencode_feature]: [1]
[ro.have_aee_feature]: [1]
[ro.kernel.zio]: [38,108,105,16]
[ro.mediatek.chip_ver]: [S01]
[ro.mediatek.gemini_support]: [true]
[ro.mediatek.platform]: [MT6737T]
[ro.mediatek.project.path]: [device/droi/n41acl_37tlf]
[ro.mediatek.version.branch]: [alps-mp-m0.mp1]
[ro.mediatek.version.release]: [alps-mp-m0.mp1-V2.84_droi6737t.36.m0_P219]
[ro.mediatek.version.sdk]: [4]
[ro.mediatek.wlan.p2p]: [1]
[ro.mediatek.wlan.wsc]: [1]
[ro.mount.fs]: [EXT4]
[ro.mtk.c2k.slot2.support]: [1]
[ro.mtk_2sdcard_swap]: [1]
[ro.mtk_agps_app]: [1]
[ro.mtk_antibricking_level]: [2]
[ro.mtk_audenh_support]: [1]
[ro.mtk_audio_ape_support]: [1]
[ro.mtk_audio_profiles]: [1]
[ro.mtk_audio_tuning_tool_ver]: [V1]
[ro.mtk_beam_plus_support]: [1]
[ro.mtk_besloudness_support]: [1]
[ro.mtk_bessurround_support]: [1]
[ro.mtk_bg_power_saving_support]: [1]
[ro.mtk_bg_power_saving_ui]: [1]
[ro.mtk_bip_scws]: [1]
[ro.mtk_bt_support]: [1]
[ro.mtk_c2k_support]: [1]
[ro.mtk_cam_lomo_support]: [1]
[ro.mtk_cam_mfb_support]: [3]
[ro.mtk_cam_vfb]: [1]
[ro.mtk_dhcpv6c_wifi]: [1]
[ro.mtk_dialer_search_support]: [1]
[ro.mtk_dual_mic_support]: [1]
[ro.mtk_eap_sim_aka]: [1]
[ro.mtk_emmc_support]: [1]
[ro.mtk_enable_md1]: [1]
[ro.mtk_enable_md3]: [1]
[ro.mtk_epdg_support]: [1]
[ro.mtk_fd_support]: [1]
[ro.mtk_flight_mode_power_off_md]: [1]
[ro.mtk_flv_playback_support]: [1]
[ro.mtk_fm_recording_support]: [1]
[ro.mtk_gemini_support]: [1]
[ro.mtk_gps_support]: [1]
[ro.mtk_hetcomm_support]: [1]
[ro.mtk_ims_support]: [1]
[ro.mtk_is_tablet]: [0]
[ro.mtk_lte_support]: [1]
[ro.mtk_md_sbp_custom_value]: [0]
[ro.mtk_md_world_mode_support]: [0]
[ro.mtk_miravision_image_dc]: [1]
[ro.mtk_miravision_support]: [1]
[ro.mtk_mobile_management]: [1]
[ro.mtk_network_type_always_on]: [1]
[ro.mtk_oma_drm_support]: [1]
[ro.mtk_omacp_support]: [1]
[ro.mtk_perf_response_time]: [1]
[ro.mtk_perf_simple_start_win]: [1]
[ro.mtk_perfservice_support]: [1]
[ro.mtk_pq_support]: [2]
[ro.mtk_rild_read_imsi]: [1]
[ro.mtk_search_db_support]: [1]
[ro.mtk_send_rr_support]: [1]
[ro.mtk_shared_sdcard]: [1]
[ro.mtk_slow_motion_support]: [1]
[ro.mtk_svlte_support]: [1]
[ro.mtk_tetheringipv6_support]: [1]
[ro.mtk_thumbnail_play_support]: [1]
[ro.mtk_vilte_support]: [1]
[ro.mtk_voice_contact_support]: [1]
[ro.mtk_voice_extension_support]: [1]
[ro.mtk_voice_unlock_support]: [1]
[ro.mtk_volte_support]: [1]
[ro.mtk_wapi_support]: [1]
[ro.mtk_wappush_support]: [1]
[ro.mtk_wfc_support]: [1]
[ro.mtk_wfd_sink_support]: [1]
[ro.mtk_wfd_sink_uibc_support]: [1]
[ro.mtk_wfd_support]: [1]
[ro.mtk_widevine_drm_l3_support]: [1]
[ro.mtk_wifi_mcc_support]: [1]
[ro.mtk_wlan_support]: [1]
[ro.mtk_wmv_playback_support]: [1]
[ro.mtk_world_phone]: [1]
[ro.mtk_world_phone_policy]: [0]
[ro.nid.productinfo]: [60]
[ro.nid.wifi_mac_address]: [54]
[ro.opengles.version]: [196608]
[ro.product.board]: []
[ro.product.brand]: [Changhong]
[ro.product.cpu.abi]: [armeabi-v7a]
[ro.product.cpu.abi2]: [armeabi]
[ro.product.cpu.abilist]: [armeabi-v7a,armeabi]
[ro.product.cpu.abilist32]: [armeabi-v7a,armeabi]
[ro.product.cpu.abilist64]: []
[ro.product.device]: [ChanghongS16]
[ro.product.locale]: [zh-CN]
[ro.product.manufacturer]: [Changhong]
[ro.product.model]: [ChanghongS16]
[ro.product.name]: [ChanghongS16]
[ro.product.project_name]: [mt6737atvdroi_n41acl_s16j_changhong_cc_256gbitp24d3_m_lte_6m-cs]
[ro.recovery_id]: [0xac5751f3beceae9b61db59da51abcce07b690c33000000000000000000000000]
[ro.revision]: [0]
[ro.ril.ecclist]: [112,911]
[ro.runtime.firstboot]: [1651009698792]
[ro.secure]: [1]
[ro.serialno]: [MNMFZ5VOFM8TN7JF]
[ro.sf.hwrotation]: [0]
[ro.sf.lcd_density]: [320]
[ro.sim_me_lock_mode]: [0]
[ro.sim_refresh_reset_by_modem]: [1]
[ro.sys.default.lockscreen]: [com.freeme.lockscreen.halo]
[ro.sys.license]: [3e84e518f295e6bfa38188a597f3a840]
[ro.sys.usb.bicr]: [yes]
[ro.sys.usb.charging.only]: [yes]
[ro.sys.usb.mtp.whql.enable]: [0]
[ro.sys.usb.storage.type]: [mtp,mass_storage]
[ro.telephony.default_network]: [4,0]
[ro.telephony.sim.count]: [2]
[ro.tyd_extreme_lk_support]: [1]
[ro.tyd_freeme_multi_sim]: [1]
[ro.tyd_fullscreen_incoming]: [1]
[ro.wifi.channels]: []
[ro.wlan.mtk.wifi.5g]: [1]
[ro.zygote]: [zygote32]
[ro.zygote.preload.enable]: [0]
[security.perf_harden]: [1]
[selinux.reload_policy]: [1]
[service.bootanim.exit]: [1]
[service.cat.install.on]: [0]
[service.cat.install.on.2]: [0]
[service.cat.install.on.3]: [0]
[service.cat.install.on.4]: [0]
[service.nvram_init]: [Ready]
[service.wcn.coredump.mode]: [0]
[service.wcn.driver.ready]: [yes]
[sys.boot.reason]: [0]
[sys.boot_completed]: [1]
[sys.ipo.pwrdncap]: [2]
[sys.ipowin.done]: [1]
[sys.oem_unlock_allowed]: [0]
[sys.power_off_alarm]: [1651013340]
[sys.settings_global_version]: [2]
[sys.settings_secure_version]: [3]
[sys.settings_system_version]: [6]
[sys.sysctl.extra_free_kbytes]: [12150]
[sys.sysctl.tcp_def_init_rwnd]: [60]
[sys.usb.config]: [mtp,adb]
[sys.usb.ffs.ready]: [1]
[sys.usb.state]: [mtp,adb]
[sys.usb.vid]: [0E8D]
[viatel.device.asci]: [uart.4.ttyMT]
[viatel.device.at]: [sdio.4.ttySDIO]
[viatel.device.at2]: [sdio.6.ttySDIO]
[viatel.device.at3]: [sdio.7.ttySDIO]
[viatel.device.data]: [sdio.1.ttySDIO]
[viatel.device.ets]: [sdio.2.ttySDIO]
[viatel.device.excp.data]: [sdio.12.ttySDIO]
[viatel.device.excp.msg]: [sdio.11.ttySDIO]
[viatel.device.fls]: [sdio.3.ttySDIO]
[viatel.device.gps]: [sdio.5.ttySDIO]
[viatel.device.pcv]: [sdio.0.ttySDIO]
[vold.has_adoptable]: [1]
[vold.path.external_sd]: [/storage/72A2-151D]
[vold.path.internal_storage]: [/storage/emulated/0]
[vold.post_fs_data_done]: [1]
[vold.support_external_sd]: [1]
[wfd.dummy.enable]: [1]
[wifi.direct.interface]: [p2p0]
[wifi.interface]: [wlan0]
[wifi.tethering.interface]: [ap0]
[wlan.driver.status]: [unloaded]
[wlan.wfd.security.image]: [1]
]]


===
https://github.com/cundong/SmartAppUpdates/issues/24
我遇到的是因为手机没有给app开启读写sd卡的权限导致的，开启权限就好了

===

apt-get --download-only --reinstall install rm
$ apt-get --download-only --reinstall install rm
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package rm
$ r
No command r found, did you mean:
 Command ar in package binutils
 Command rm in package busybox
 Command pr in package coreutils
 Command k in package kona
 Command mr in package myrepos
 Command r2 in package radare2
 Command rg in package ripgrep
 Command ri in package ruby-ri

apt-get --download-only --reinstall install busybox
$ apt-get --download-only --reinstall install busybox
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  liblz4 xxhash
Use 'apt autoremove' to remove them.
The following packages will be upgraded:
  busybox
1 upgraded, 0 newly installed, 0 to remove and 139 not upgraded.
Need to get 0 B/425 kB of archives.
After this operation, 8192 B disk space will be freed.
Download complete and in download only mode
$ ls
WARNING: linker: ls: unused DT entry: type 0x1d arg 0xc5b
WARNING: linker: /data/data/com.termux/files/usr/lib/libandroid-support.so: unused DT entry: type 0x1d arg 0x18a
WARNING: linker: /data/data/com.termux/files/usr/lib/libgmp.so: unused DT entry: type 0x1d arg 0x2900
CANNOT LINK EXECUTABLE: cannot locate symbol "__fwrite_chk" referenced by "ls"...
page record for 0xb6ddb00c was not found (block_size=64)
$ l
No command l found, did you mean:
 Command ld in package binutils
 Command ln in package coreutils
 Command k in package kona
 Command lz in package mtools
 Command sl in package sl
 Command ul in package util-linux

apt-get --reinstall install busybox

]]]]]
see:
  e script/20220427_fix_termux.py
  e /sdcard/Download/downs4termux/other-urls.txt
]]]]]]]]]
]]]]@20220430
#'''

r'''
[[[[[@20220430
copy from:
    e /sdcard/Download/downs4termux/other-urls.txt

[[[[[
e /sdcard/Download/downs4termux/other-urls.txt
TODO:
  move to:
    e script/20220427_fix_termux.py

https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/

非平凡/非独子
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/Release
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/InRelease

https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-all/Packages

!mkdir -p /sdcard/Download/downs4termux/other4curl/termux-old/termux-packages/dists/stable/main/binary-arm/
!mkdir /sdcard/Download/downs4termux/other4curl/termux-old/termux-packages/dists/stable/main/binary-all/

cd /sdcard/Download/downs4termux/other4curl/
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/Release -o ./termux-old/termux-packages/dists/stable/Release
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/InRelease -o ./termux-old/termux-packages/dists/stable/InRelease
view /sdcard/Download/downs4termux/other4curl/termux-old/termux-packages/dists/stable/Release
  Architectures: all arm i686 aarch64 x86_64
view /sdcard/Download/downs4termux/other4curl/termux-old/termux-packages/dists/stable/InRelease

curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-all/Packages -o ./termux-old/termux-packages/dists/stable/main/binary-all/Packages
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-all/ -o ./termux-old/termux-packages/dists/stable/main/binary-all/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/Packages -o ./termux-old/termux-packages/dists/stable/main/binary-arm/Packages
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-arm/ -o ./termux-old/termux-packages/dists/stable/main/binary-arm/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/ -o ./termux-old/termux-packages/dists/stable/main/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/ -o ./termux-old/termux-packages/dists/stable/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/ -o ./termux-old/termux-packages/dists/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/ -o ./termux-old/termux-packages/index.html
curl https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/ -o ./termux-old/index.html


view /sdcard/Download/downs4termux/binary-arm-index.html.ls-3.txt
e /sdcard/Download/downs4termux/binary-all-index.html.txt
^\[ ]\t
%s///
\t $
%s///
w /sdcard/Download/downs4termux/binary-all-index.html.ls-3.txt
\t.*
%s///
w /sdcard/Download/downs4termux/binary-all-index.html.ls-1.txt

view /sdcard/Download/downs4termux/binary-all-index.html.txt
view /sdcard/Download/downs4termux/binary-all-index.html.ls-3.txt
view /sdcard/Download/downs4termux/binary-all-index.html.ls-1.txt
view /sdcard/Download/downs4termux/binary-all-index.html.urls.txt
  https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-packages/dists/stable/main/binary-all/

    !mkdir /sdcard/Download/curl-all-deb4termux/
    cd /sdcard/Download/curl-all-deb4termux/
    xargs -n 1 curl -O < /sdcard/Download/downs4termux/binary-all-index.html.urls.txt
      共99个文件
    ls /sdcard/Download/curl-all-deb4termux/
      ecj_1:4.6.2-1_all.deb
      改名『:』-->『--』
    使用SManager:
      cp /sdcard/Download/curl-all-deb4termux/ecj_1:4.6.2-1_all.deb /sdcard/Download/curl-all-deb4termux/ecj_1--4.6.2-1_all.deb






######################
######################
######################
######################
######################
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/bootstrap/
    mkdir /sdcard/Download/curl-top-deb4termux/
    mkdir /sdcard/Download/curl-top-deb4termux/bootstrap/
    cd /sdcard/Download/curl-top-deb4termux/bootstrap/
    curl -O https://free.nchc.org.tw/osdn/storage/g/t/te/termux-old/bootstrap/bootstrap-arm.zip

https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-root-packages-21/

https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/science-packages-21/
  https://free.nchc.org.tw/osdn/storage/g/t/te/termux-old/science-packages-21/dists/science/stable/
    [DIR]	binary-aarch64/
    [DIR]	binary-arm/
    [DIR]	binary-i686/
    [DIR]	binary-x86_64/
    没关系，都是文本文档

https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/game-packages-21/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/unstable-packages-21/
https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/x11-packages-21/
  TODO


cd /sdcard/Download/curl-top-deb4termux/
tpl: wget -r -l inf --no-remove-listing --no-parent -p -k -nc -N --no-use-server-timestamps -c --random-wait --wait=8 --tries=30 --limit-rate=200K --compression=auto -U "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1"    https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/zzzzzzzzzzzz-packages-21/ --reject-regex='[^?]*[?].*|(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/zzzzzzzzzzzz-packages-21/|)(aarch64|i686|x86_64)(/.*)?' --accept-regex='(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/zzzzzzzzzzzz-packages-21/|)(all|arm|dists)(/.*)?'
  --reject-regex=REGEX
    regex matching rejected URLs
  --accept-regex=REGEX
    regex matching accepted URLs

wget -r -l inf --no-remove-listing --no-parent -p -k -nc -N --no-use-server-timestamps -c --random-wait --wait=8 --tries=30 --limit-rate=200K --compression=auto -U "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1"    https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-root-packages-21/ --reject-regex='[^?]*[?].*|(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-root-packages-21/|)(aarch64|i686|x86_64)(/.*)?' --accept-regex='(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/termux-root-packages-21/|)(all|arm|dists)(/.*)?'


wget -r -l inf --no-remove-listing --no-parent -p -k -nc -N --no-use-server-timestamps -c --random-wait --wait=8 --tries=30 --limit-rate=200K --compression=auto -U "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1"    https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/science-packages-21/ --reject-regex='[^?]*[?].*|(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/science-packages-21/|)(aarch64|i686|x86_64)(/.*)?' --accept-regex='(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/science-packages-21/|)(all|arm|dists)(/.*)?'



wget -r -l inf --no-remove-listing --no-parent -p -k -nc -N --no-use-server-timestamps -c --random-wait --wait=8 --tries=30 --limit-rate=200K --compression=auto -U "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1"    https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/game-packages-21/ --reject-regex='[^?]*[?].*|(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/game-packages-21/|)(aarch64|i686|x86_64)(/.*)?' --accept-regex='(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/game-packages-21/|)(all|arm|dists)(/.*)?'



wget -r -l inf --no-remove-listing --no-parent -p -k -nc -N --no-use-server-timestamps -c --random-wait --wait=8 --tries=30 --limit-rate=200K --compression=auto -U "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1"    https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/x11-packages-21/ --reject-regex='[^?]*[?].*|(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/x11-packages-21/|)(aarch64|i686|x86_64)(/.*)?' --accept-regex='(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/x11-packages-21/|)(all|arm|dists)(/.*)?'


wget -r -l inf --no-remove-listing --no-parent -p -k -nc -N --no-use-server-timestamps -c --random-wait --wait=8 --tries=30 --limit-rate=200K --compression=auto -U "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1"    https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/unstable-packages-21/ --reject-regex='[^?]*[?].*|(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/unstable-packages-21/|)(aarch64|i686|x86_64)(/.*)?' --accept-regex='(https://free.nchc.org.tw/osdn//storage/g/t/te/termux-old/unstable-packages-21/|)(all|arm|dists)(/.*)?'


]]]]]



e others/app/termux/apt_update__fail/apt_update_fail__solved_ver2.txt
搜 dpkg ... log
  [[
  e /sdcard/Download/downs4termux/other-urls.txt
  e script/20220427_fix_termux.py
  e others/app/termux/apt_pkg.txt
  e others/app/termux/apt_update_fail__solved.txt
            !mv others/app/termux/apt_update_fail__solved.txt    others/app/termux/apt_update__fail/bug---apt_update_fail__solved_ver1---bug.txt
  e TODO.txt
  ]]==>> /var/log/dpkg.log
    termux下没找到对应的

  $ ls ~/../usr/var/log/ -1
    alternatives.log
    apt
  view ~/../usr/var/log/alternatives.log
    没什么东西
  ls ~/../usr/var/log/apt/ -1
    eipp.log.xz
    history.log
    term.log
  view ~/../usr/var/log/apt/history.log
    命令执行结果？
  view ~/../usr/var/log/apt/term.log
    终端输出的全部历史？
  mkdir /sdcard/0my_files/tmp/var_log_apt__20220429/
  cp -r ~/../usr/var/log/apt/  /sdcard/0my_files/tmp/var_log_apt__20220429/
  e /sdcard/0my_files/tmp/var_log_apt__20220429/README.txt
  view others/app/termux/apt_update__fail/var_log_apt__20220429.zip
    打包保存
  view /sdcard/0my_files/tmp/var_log_apt__20220429/apt/
  view /sdcard/0my_files/tmp/var_log_apt__20220429/apt/history.log
  [[~/../usr/var/log/apt/history.log::202204:
... ...
... ...
Start-Date: 2021-05-27  20:37:31
Commandline: apt install patch
Install: patch:arm (2.7.6-4)
End-Date: 2021-05-27  20:37:42

Start-Date: 2022-04-26  18:48:11
Commandline: apt remove game-repo
Remove: game-repo:arm (1.0-1)
End-Date: 2022-04-26  18:48:12

Start-Date: 2022-04-26  18:48:29
Commandline: apt remove science-repo
Remove: science-repo:arm (1.0-1)
End-Date: 2022-04-26  18:48:30

######################
######################
######################error below
######################
######################
Start-Date: 2022-04-26  22:56:44
Commandline: apt upgrade termux-am
Install: libaom:arm (3.3.0, automatic), dialog:arm (1.3-20220117-0, automatic), llvm:arm (14.0.1, automatic), librav1e:arm (0.5.1, automatic), zstd:arm (1.5.2-1, automatic), openjpeg-tools:arm (2.4.0-1, automatic), liblz4:arm (1.9.3, automatic), openssh-sftp-server:arm (9.0p1-1, automatic), libssh2:arm (1.10.0-2, automatic), libvidstab:arm (1.1.0-2, automatic), libcompiler-rt:arm (14.0.1, automatic), libcap-ng:arm (2:0.8.3, automatic), giflib:arm (5.2.1-2, automatic), libdav1d:arm (1.0.0, automatic), lld:arm (14.0.1, automatic), termux-am-socket:arm (1.02, automatic), libandroid-posix-semaphore:arm (0.1-3, automatic), libevent:arm (2.1.12-1, automatic), xxhash:arm (0.8.1, automatic), pkg-config:arm (0.29.2-1, automatic), libresolv-wrapper:arm (1.1.7-2, automatic), unbound:arm (1.15.0-1, automatic), libudfread:arm (1.1.2, automatic), game-music-emu:arm (0.6.3, automatic), libbluray:arm (1.3.1, automatic), ttf-dejavu:arm (2.37-8, automatic), openssl-1.1:arm (1.1.1n, automatic)
Upgrade: libcurl:arm (7.67.0-1, 7.82.0-1), libmpfr:arm (4.0.2-2, 4.1.0-1), libvorbis:arm (1.3.6-3, 1.3.7-1), python-static:arm (3.8.0-1, 3.10.4), libgcrypt:arm (1.8.5-1, 1.10.1), libedit:arm (20191025-3.1-1, 20210910-3.1-0), libc++:arm (20-3, 23b-3), zlib:arm (1.2.11-2, 1.2.12), diffutils:arm (3.7-3, 3.8), termux-auth:arm (1.1-2, 1.4-2), libass:arm (0.14.0-2, 0.15.2-4), clang:arm (9.0.0-1, 14.0.1), libbz2:arm (1.0.8-3, 1.0.8-6), ffmpeg:arm (4.2.1-3, 5.0.1-1), dx:arm (29.0.2-1, 1:1.16-6), m4:arm (1.4.18-4, 1.4.19-3), openssh:arm (8.1p1-2, 9.0p1-1), openssl:arm (1.1.1d-2, 3.0.2), libcrypt:arm (0.2-3, 0.2-5), libsqlite:arm (3.30.1-1, 3.38.2), libpixman:arm (0.38.4-3, 0.40.0-2), libexpat:arm (2.2.9-1, 2.4.8), p7zip:arm (16.02-5, 17.04-1), libffi:arm (3.2.1-5, 3.4.2), dash:arm (0.5.10.2-3, 0.5.11.5-1), apt:arm (1.4.9-12, 2.4.5), libgmp:arm (6.1.2-5, 6.2.1-1), libgraphite:arm (1.3.13-4, 1.3.14-1), libllvm:arm (9.0.0-1, 14.0.1), libmp3lame:arm (3.100-2, 3.100-3), binutils:arm (2.33.1-1, 2.38), libicu:arm (65.1-1, 71.1), ndk-sysroot:arm (20-3, 23b-7), libunistring:arm (0.9.10-4, 1.0), ecj:arm (1:4.6.2-1, 1:4.12-4), libsoxr:arm (0.1.3-3, 0.1.3-3), libdb:arm (18.1.32-3, 18.1.40-3), resolv-conf:arm (1.2-1, 1.3), libgd:arm (2.2.5-6, 1:2.3.3), pcre2:arm (10.33-2, 10.40), util-linux:arm (2.34-3, 2.38), automake:arm (1.16.1-1, 1.16.5), libuv:arm (1.33.1-1, 1.44.1), ncurses-ui-libs:arm (6.1.20190511-8, 6.3), coreutils:arm (8.31-5, 9.1), git:arm (2.23.0-1, 2.35.3), gawk:arm (5.0.1-5, 5.1.1-1), hub:arm (2.12.8-1, 2.14.2-1), procps:arm (3.3.15-7, 3.3.17-1), teckit:arm (2.5.9-4, 2.5.11), libogg:arm (1.3.4-1, 1.3.5), gdbm:arm (1.18.1-3, 1.22), littlecms:arm (2.9-2, 2.13.1-1), termux-licenses:arm (1.0-1, 2.0-2), libltdl:arm (2.4.6-7, 2.4.6-8), libgnutls:arm (3.6.9-2, 3.7.3), termux-am:arm (0.3-1, 0.4), libpng:arm (1.6.37-3, 1.6.37-3), python:arm (3.8.0-1, 3.10.4), hexedit:arm (1.4.2-1, 1.5), jsoncpp:arm (1.9.1-2, 1.9.5), man:arm (1.14.5-2, 1.14.5-3), libopus:arm (1.3.1-4, 1.3.1-5), libjpeg-turbo:arm (2.0.3-1, 2.1.3), libx264:arm (20190215-2, 1:0.161.3049-1), libx265:arm (3.2.1-1, 3.5-3), rhash:arm (1.3.8-3, 1.4.2-2), autoconf:arm (2.69-1, 2.71-2), pacman4console:arm (1.3-1, 1.3-3), freetype:arm (2.10.1-2, 2.12.0), dpkg:arm (1.19.7-5, 1.21.1-1), fontconfig:arm (2.13.1-4, 2.14.0), liblzma:arm (5.2.4-3, 5.2.5-1), krb5:arm (1.17-2, 1.19.3), libvpx:arm (1.8.1-2, 1.11.0), termux-keyring:arm (1.1-1, 3.3), openjpeg:arm (2.3.1-2, 2.4.0-1), unrar:arm (5.8.3-1, 6.1.6), psmisc:arm (23.2-2, 23.4), glib:arm (2.62.2-1, 2.72.1), readline:arm (8.0.1-1, 8.1.1), sed:arm (4.7-2, 4.8-2), libandroid-support:arm (24-6, 28-2), make:arm (4.2.1-4, 4.3-2), tar:arm (1.32-4, 1.34), tcl:arm (8.6.9-7, 8.6.11-1), termux-tools:arm (0.75, 0.175), fribidi:arm (1.0.7-1, 1.0.12), tsu:arm (2.3-1, 8.6.0), xvidcore:arm (1.3.5-2, 1.3.7), pinentry:arm (1.1.0-5, 1.2.0), vim-runtime:arm (8.1.2200-1, 8.2.4650), gpgv:arm (2.2.17-2, 2.3.5), librsvg:arm (2.46.3-1, 2.54.0), libksba:arm (1.3.5-3, 1.6.0), xz-utils:arm (5.2.4-3, 5.2.5-1), sharutils:arm (4.15.2-2, 4.15.2-2), grep:arm (3.3-3, 3.7-2), libarchive:arm (3.4.0-2, 3.6.1), libnettle:arm (3.5.1-3, 3.7.3), ncurses:arm (6.1.20190511-8, 6.3), bzip2:arm (1.0.8-3, 1.0.8-6), bash:arm (5.0.11-1, 5.1.16-1), pcre:arm (8.43-4, 8.45-1), pure-ftpd:arm (1.0.49-1, 1.0.50-2), busybox:arm (1.31.1-1, 1.35.0), findutils:arm (4.7.0-1, 4.9.0-1), libxml2:arm (2.9.10-1, 2.9.13), cmake:arm (3.15.5-1, 3.23.1), ca-certificates:arm (20191129, 1:2022.03.29), perl:arm (5.30.0-2, 5.34.1-1), libuuid:arm (1.0.3-4, 1.0.3-5), command-not-found:arm (1.42.1, 1.75), wget:arm (1.20.3-3, 1.21.3-2), libtiff:arm (4.0.10-9, 4.3.0-2), gzip:arm (1.10-3, 1.12), vim-python:arm (8.1.2200-3, 8.2.4650), gnupg:arm (2.2.17-2, 2.3.5), openssl-tool:arm (1.1.1d-2, 3.0.2), libwebp:arm (1.0.3-2, 1.2.2), gettext:arm (0.20.1-3, 0.21-5), poppler:arm (0.79.0-2, 21.08.0-5), curl:arm (7.67.0-1, 7.82.0-1), libxslt:arm (1.1.34-1, 1.1.35), libidn2:arm (2.2.0-2, 2.3.2), gdk-pixbuf:arm (2.40.0-1, 2.42.8-1), libcroco:arm (0.6.13-2, 0.6.13-7), libassuan:arm (2.5.3-2, 2.5.5), harfbuzz-icu:arm (2.6.4-1, 4.2.1), graphviz:arm (2.40.1-10, 2.50.0), tree:arm (1.8.0-2, 2.0.2), ldns:arm (1.7.1-2, 1.8.1-1), libgpg-error:arm (1.36-2, 1.45), less:arm (551-2, 590), harfbuzz:arm (2.6.4-1, 4.2.1), libnghttp2:arm (1.39.2-1, 1.47.0), libtool:arm (2.4.6-7, 2.4.6-8), termux-exec:arm (0.4-2, 1:1.0), lftp:arm (4.8.4-7, 4.9.2-4), bash-completion:arm (2.9-1, 2.11-2), libandroid-glob:arm (0.6-1, 0.6-2)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-26  22:56:47

Start-Date: 2022-04-26  23:14:33
Commandline: apt install termux-tools
Install: dialog:arm (1.3-20220117-0, automatic), termux-am-socket:arm (1.02, automatic)
Upgrade: termux-keyring:arm (1.1-1, 3.3), termux-tools:arm (0.75, 0.175)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-26  23:14:33

Start-Date: 2022-04-26  23:17:36
Commandline: apt install termux-auth
Upgrade: termux-auth:arm (1.1-2, 1.4-2)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-26  23:17:36

Start-Date: 2022-04-26  23:40:20
Commandline: apt install termux-tools
Install: dialog:arm (1.3-20220117-0, automatic), termux-am-socket:arm (1.02, automatic)
Upgrade: termux-keyring:arm (1.1-1, 3.3), termux-tools:arm (0.75, 0.175)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-26  23:40:21

Start-Date: 2022-04-27  00:48:13
Commandline: apt-get --reinstall install busybox
Upgrade: busybox:arm (1.31.1-1, 1.35.0)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-27  00:48:13

Start-Date: 2022-04-27  11:26:54
Commandline: apt install unstable-repo
Upgrade: apt:arm (1.4.9-12, 2.4.5)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-27  11:26:54

Start-Date: 2022-04-27  18:30:52
Commandline: apt install /sdcard/Download/libandroid-support_24-6_arm.deb
Downgrade: libandroid-support:arm (28-2, 24-6)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-27  18:30:52

Start-Date: 2022-04-27  18:31:05
Commandline: apt install /sdcard/Download/libandroid-support_24-6_arm.deb
Downgrade: libandroid-support:arm (28-2, 24-6)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-27  18:31:05

Start-Date: 2022-04-27  22:41:36
Commandline: apt install /sdcard/Download/libandroid-support_24-6_arm.deb
Downgrade: libandroid-support:arm (28-2, 24-6)
Error: Sub-process /data/data/com.termux/files/usr/bin/dpkg returned an error code (1)
End-Date: 2022-04-27  22:41:36
  ]]
  view /sdcard/0my_files/tmp/var_log_apt__20220429/apt/term.log
  grep Unpacking /sdcard/0my_files/tmp/var_log_apt__20220429/apt/term.log
  [[grep Unpacking ~/../usr/var/log/apt/term.log
... ...
... ...
Unpacking patch (2.7.6-4) ...
######################
######################
######################error below
######################
######################
Unpacking libandroid-support (28-2) over (24-6) ...
Unpacking liblz4 (1.9.3) ...
Unpacking xxhash (0.8.1) ...
Unpacking libc++ (23b-3) over (20-3) ...
Unpacking libgmp (6.2.1-1) over (6.1.2-5) ...
Unpacking coreutils (9.1) over (8.31-5) ...
  ]] ==>> 全部重装！libandroid-support liblz4 xxhash libc++ libgmp coreutils
  [[
  虽然 libandroid-support 与 coreutils 已手动重装，但文档之类没有还原，还要用apt重装
    #手动重装coreutils之后，『rm』『mv』『cp』才能用，apt依赖于dpkg依赖于rm...依赖于coreutils
    #
apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/xxxx.deb
[[
view /sdcard/Download/downs4termux/binary-arm-index.html.ls-3.txt
libandroid-glob-static_0.6-1_arm.deb	2022-03-13 00:52 	4.3K
libandroid-glob_0.6-1_arm.deb	2022-03-13 00:52 	6.5K
libandroid-shmem-static_0.2.1-1_arm.deb	2022-03-13 00:52 	5.4K
libandroid-shmem_0.2.1-1_arm.deb	2022-03-13 00:52 	8.7K
libandroid-support-static_24-6_arm.deb	2022-03-13 00:52 	103K
libandroid-support_24-6_arm.deb	2022-03-13 00:52 	102K


liblz4-static_1.9.2-1_arm.deb	2022-03-13 00:57 	53K
liblz4_1.9.2-1_arm.deb	2022-03-13 00:57 	75K

没有xxhash的deb

libc++_20-3_arm.deb	2022-03-13 00:53 	161K

libgmp-static_6.1.2-5_arm.deb	2022-03-13 00:55 	203K
libgmp_6.1.2-5_arm.deb	2022-03-13 00:55 	293K

coreutils_8.31-5_arm.deb	2022-03-13 00:35 	689K
]]

$ pkg list-installed
  并没有 static

!!!重装!!!
apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libandroid-support_24-6_arm.deb
apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/liblz4_1.9.2-1_arm.deb
apt autoremove xxhash

apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libc++_20-3_arm.deb
apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libgmp_6.1.2-5_arm.deb

apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/coreutils_8.31-5_arm.deb
  ]]==>>输出 [[[
[[
$ apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libandroid-support_24-6_arm.deb
Reading package lists... Done
Building dependency tree
Reading state information... Done
Note, selecting 'libandroid-support' instead of '/mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libandroid-support_24-6_arm.deb'
The following packages were automatically installed and are no longer required:
  liblz4 xxhash
Use 'apt autoremove' to remove them.
The following packages will be DOWNGRADED:
  libandroid-support
0 upgraded, 0 newly installed, 1 downgraded, 0 to remove and 0 not upgraded.
Need to get 0 B/104 kB of archives.
After this operation, 115 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
dpkg: warning: downgrading libandroid-support from 28-2 to 24-6
(Reading database ... 30696 files and directories currently installed.)
Preparing to unpack .../libandroid-support_24-6_arm.deb ...
Unpacking libandroid-support (24-6) over (28-2) ...
Setting up libandroid-support (24-6) ...
]]
[[
$ apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/liblz4_1.9.2-1_arm.deb
Reading package lists... Done
Building dependency tree
Reading state information... Done
Note, selecting 'liblz4' instead of '/mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/liblz4_1.9.2-1_arm.deb'
The following package was automatically installed and is no longer required:
  xxhash
Use 'apt autoremove' to remove it.
The following packages will be DOWNGRADED:
  liblz4
0 upgraded, 0 newly installed, 1 downgraded, 0 to remove and 0 not upgraded.
Need to get 0 B/76.3 kB of archives.
After this operation, 12.3 kB disk space will be freed.
Do you want to continue? [Y/n] y
Get:1 /storage/72A2-151D/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/liblz4_1.9.2-1_arm.deb liblz4 arm 1.9.2-1 [76.3 kB]
dpkg: warning: downgrading liblz4 from 1.9.3 to 1.9.2-1
(Reading database ... 30695 files and directories currently installed.)
Preparing to unpack .../liblz4_1.9.2-1_arm.deb ...
Unpacking liblz4 (1.9.2-1) over (1.9.3) ...
Setting up liblz4 (1.9.2-1) ...
]]
[[
$ apt autoremove xxhash
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages will be REMOVED:
  xxhash
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 344 kB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 30695 files and directories currently installed.)
Removing xxhash (0.8.1) ...
Processing triggers for man (1.14.5-2) ...
]]
[[
$ apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libc++_20-3_arm.deb
Reading package lists... Done
Building dependency tree
Reading state information... Done
Note, selecting 'libc++' instead of '/mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libc++_20-3_arm.deb'
The following packages will be DOWNGRADED:
  libc++
0 upgraded, 0 newly installed, 1 downgraded, 0 to remove and 0 not upgraded.
Need to get 0 B/164 kB of archives.
After this operation, 45.1 kB disk space will be freed.
Do you want to continue? [Y/n] y
dpkg: warning: downgrading libc++ from 23b-3 to 20-3
(Reading database ... 30678 files and directories currently installed.)
Preparing to unpack .../archives/libc++_20-3_arm.deb ...
Unpacking libc++ (20-3) over (23b-3) ...
Setting up libc++ (20-3) ...
]]
[[
$ apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libgmp_6.1.2-5_arm.deb
Reading package lists... Done
Building dependency tree
Reading state information... Done
Note, selecting 'libgmp' instead of '/mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/libgmp_6.1.2-5_arm.deb'
The following packages will be DOWNGRADED:
  libgmp
0 upgraded, 0 newly installed, 1 downgraded, 0 to remove and 0 not upgraded.
Need to get 0 B/300 kB of archives.
After this operation, 20.5 kB disk space will be freed.
Do you want to continue? [Y/n] y
dpkg: warning: downgrading libgmp from 6.2.1-1 to 6.1.2-5
(Reading database ... 30678 files and directories currently installed.)
Preparing to unpack .../libgmp_6.1.2-5_arm.deb ...
Unpacking libgmp (6.1.2-5) over (6.2.1-1) ...
Setting up libgmp (6.1.2-5) ...
]]
[[
$ apt install /mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/coreutils_8.31-5_arm.deb
Reading package lists... Done
Building dependency tree
Reading state information... Done
Note, selecting 'coreutils' instead of '/mnt/m_external_sd/000edt/0my_files/apk/deb_pkgs4termux/arm-deb_pkgs4termux/coreutils_8.31-5_arm.deb'
The following packages will be DOWNGRADED:
  coreutils
0 upgraded, 0 newly installed, 1 downgraded, 0 to remove and 0 not upgraded.
Need to get 0 B/706 kB of archives.
After this operation, 69.6 kB disk space will be freed.
Do you want to continue? [Y/n] y
dpkg: warning: downgrading coreutils from 9.1 to 8.31-5
(Reading database ... 30676 files and directories currently installed.)
Preparing to unpack .../coreutils_8.31-5_arm.deb ...
Unpacking coreutils (8.31-5) over (9.1) ...
Setting up coreutils (8.31-5) ...
Processing triggers for man (1.14.5-2) ...
]]
]]]

更新 我的步骤
  终结之




]]]]@20220430
#'''

r'''
[[[[[@20220430
move from:
]]]]@20220430
#'''
r'''
[[[[[@20220430
move from:
]]]]@20220430
#'''
main()
