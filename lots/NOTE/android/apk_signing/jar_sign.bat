

::: jar_sign.bat .\keystore\my-release-key.keystore password alias_name password xx.ap_ xx.apk



set "keystore_file=%~1"
set "store_password=%~2"
set "key_alias_name=%~3"
set "key_password=%~4"
set "unsigned_apk=%~5"
set "output_apk=%~6"


if "%keystore_file%"=="" goto error1
if "%unsigned_apk%"=="" goto error2
if "%output_apk%"=="" goto error3


set "JDK_BIN=%JAVA_HOME%\bin"
:: %JDK_BIN%\keytool  -genkey -v -keystore  my-release-key.keystore -alias alias_name  -keyalg RSA -keysize 2048  -validity 10000
:: -keypass <密钥口令> -storepass <密钥库口令> -alias <要处理的条目的别名> -validity <有效天数>

set APP_SIGNER="%JDK_BIN%\jarsigner"  -digestalg SHA1 -sigalg MD5withRSA -tsa http://timestamp.comodoca.com/authenticode
call %APP_SIGNER% -keystore "%keystore_file%" -storepass "%store_password%" -keypass "%key_password%" -signedjar "%output_apk%" "%unsigned_apk%" "%key_alias_name%" || goto sign_error
goto end

:error1
    echo:keystore_file should not be ''
    goto end
:error2
    echo:unsigned_apk should not be ''
    goto end
:error3
    echo:output_apk should not be ''
    goto end
:sign_error
    echo:fail to sign
    goto end

:end
