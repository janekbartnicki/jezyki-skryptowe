@echo off
if "%1"=="" goto brak_args

del /s /q "%1\*.tmp"
echo Usunieto pliki tymczasowe z folderu %1
goto koniec

:brak_args
echo Blad argumentow.
:koniec
pause