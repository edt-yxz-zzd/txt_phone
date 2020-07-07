@echo off


REM ##############################################################################
REM #CMD环境恢复中文:
REM #chcp 936
REM ##############################################################################


REM set path=%path%;D:\software\programming\gcc\mingw32\bin
set path=D:\software\programming\gcc\mingw32\bin;%path%
set path=C:\mingw64\x64-4.8.1-posix-seh-rev5\mingw64\bin;%path%
set path=%path%;D:\software\programming\gcc\tool\boost_build\bin

set path=%path%;D:\software\programming\gcc\mingw32\msys\1.0\bin
set path=%path%;D:\software\programming\gcc\tool\moreLinuxCmd
set path=%path%;D:\software\programming\gcc\tool\UnxUtils\usr\local\wbin
set path=%path%;D:\software\programming\gcc\mingw32\msys\1.0

rem set path=%path%;C:\Python32
rem set path=%path%;C:\Program Files\gs\gs9.06\bin
set path=%path%;D:\software\cmdline_tool_link


set src_py=E:\my_data\program_source\python3_src
set 7z=python %src_py%\zip_by_7z.py
set boost=D:\software\programming\library\boost\boost_1_51_0


REM pause


rem C:\Windows\System32\cmd.exe /E:ON /V:ON /T:0E /K "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd"

set DISTUTILS_USE_SDK=1
rem C:\Windows\System32\cmd.exe /E:ON /V:ON              "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd  x64 release"

"C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd"  /x64 /release

@echo on