@echo off
if "%1"=="" (
    echo Podaj katalog docelowy jako argument!
    goto koniec
)

if not exist "%1" mkdir "%1"
copy *.txt "%1"
echo Skopiowano pliki tekstowe do %1

:koniec
pause