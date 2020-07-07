echo %1 
echo %2
echo %*
pause
exit


rem The first item passed is always %1 the second item is always %2 and so on
rem %* in a batch script refers to all the arguments (e.g. %1 %2 %3 %4 %5 ...%255)
rem SHIFT [/n] If Command Extensions are enabled the SHIFT command supports the /n switch that tells the command to start shifting at the nth argument, where n may be between zero and eight. For example:
rem SHIFT /2 would shift %3 to %2, %4 to %3, etc. and leave %0 and %1 unaffected.


:loop
if "%1" == "" goto end
"C:\\Program Files\\7-Zip\\7zG.exe\" a -t7z "%1.7z" "%1"
shift
pause

:end