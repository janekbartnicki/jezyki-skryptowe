@echo off
if "%1"=="" goto brak_argumentow
set /p n="Podaj liczbe n: "

for /l %%i in (1,1,%n%) do (
    echo %%i>> "%1"
)
echo Zapisano liczby do %1
goto koniec

:brak_argumentow
echo Blad argumentu.
:koniec
pause