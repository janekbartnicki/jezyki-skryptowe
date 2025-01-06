@echo off
if "%1"=="" goto brak_argumentow

if not exist "%1" (
    echo Plik %1 nie istnieje!
    goto koniec
)

for /f "tokens=*" %%a in (%1) do (
    set miesiac=%%a
    if /i "%%a"=="styczen" echo 1
    if /i "%%a"=="luty" echo 2
    if /i "%%a"=="marzec" echo 3
    if /i "%%a"=="kwiecien" echo 4
    if /i "%%a"=="maj" echo 5
    if /i "%%a"=="czerwiec" echo 6
    if /i "%%a"=="lipiec" echo 7
    if /i "%%a"=="sierpien" echo 8
    if /i "%%a"=="wrzesien" echo 9
    if /i "%%a"=="pazdziernik" echo 10
    if /i "%%a"=="listopad" echo 11
    if /i "%%a"=="grudzien" echo 12
)
goto koniec

:brak_argumentow
echo Podaj nazwę pliku jako argument
:koniec
pause