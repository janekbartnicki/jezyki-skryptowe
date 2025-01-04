@echo off
if "%1"=="" goto brak_args

xcopy "%1" "backup_%1" /d /e /i /y
echo Backup zostal utworzony w folderze backup_%1
goto koniec

:brak_args
echo Blad argumentow.
:koniec
pause