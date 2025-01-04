@echo off
if "%1"=="" goto brak_argumentow
cd "%1"
del *.tmp
echo Usunieto pliki .tmp z katalogu "%1"
goto koniec

:brak_argumentow
echo Podaj katalog jako argument
:koniec
pause