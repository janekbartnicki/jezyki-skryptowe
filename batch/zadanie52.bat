@echo off
if "%1"=="" goto brak_argumentow
set /a dec=0x%1
echo Liczba %1 w systemie dziesietnym to: %dec%
goto koniec

:brak_argumentow
echo Blad argumentu.

:koniec
pause