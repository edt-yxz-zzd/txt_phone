goto :start
exit /b
:set_ERRORLEVEL
    exit /b %1

:start

rem if defined ERRORLEVEL always be TRUE

rem delete %%ERRORLEVEL%%
set ERRORLEVEL=
call :set_ERRORLEVEL 1
if not defined ERRORLEVEL echo %ERRORLEVEL%
if defined ERRORLEVEL echo %ERRORLEVEL%

call :set_ERRORLEVEL 0
if not defined ERRORLEVEL echo %ERRORLEVEL%
if defined ERRORLEVEL echo %ERRORLEVEL%

