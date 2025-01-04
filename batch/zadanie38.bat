@echo off
set /p lokalizacja="Podaj lokalizacje pliku wejsciowego: "
if "%1"=="" (
    echo Podaj maksymalną liczbę jako argument!
    goto koniec
)

for /l %%i in (0,1,%1) do (
    echo %%i>> "%lokalizacja%"
)
echo Zapisano liczby do %lokalizacja%

:koniec
pause