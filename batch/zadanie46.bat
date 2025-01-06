@echo off
if "%1"=="" goto brak_argumentow

set /p n="Podaj liczbe n: "
set licznik=1

:petla
if %licznik% gtr %n% goto koniec
echo %licznik%>> "%1"
set /a licznik+=1
goto petla

:koniec
echo Zapisano liczby do %1
goto end

:brak_argumentow
echo Blad argumentu.
:end
pause