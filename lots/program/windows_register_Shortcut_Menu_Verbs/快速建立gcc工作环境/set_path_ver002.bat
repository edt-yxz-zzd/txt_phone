@echo off


REM ##############################################################################
REM #CMD�����ָ�����:
REM #chcp 936
REM ##############################################################################



REM set path=%path%;D:\software\programming\gcc\mingw32\bin
set path=D:\software\programming\gcc\mingw32\bin;%path%
set path=%path%;D:\software\programming\gcc\tool\boost_build\bin

set path=%path%;D:\software\programming\gcc\mingw32\msys\1.0\bin
set path=%path%;D:\software\programming\gcc\tool\moreLinuxCmd
set path=%path%;D:\software\programming\gcc\tool\UnxUtils\usr\local\wbin
set path=%path%;D:\software\programming\gcc\mingw32\msys\1.0

set path=%path%;C:\Python32
set path=%path%;C:\Program Files\gs\gs9.06\bin
set path=%path%;D:\software\cmdline_tool_link


set src_py=E:\my_data\program_source\python3_src
set 7z=python %src_py%\zip_by_7z.py
set boost=D:\software\programming\library\boost\boost_1_51_0


REM pause



@echo on