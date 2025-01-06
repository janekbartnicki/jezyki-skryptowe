@echo off
if "%1"=="" goto brak_argumentow

set miesiac=%1
if /i "%miesiac%"=="styczen" echo 1
if /i "%miesiac%"=="luty" echo 2
if /i "%miesiac%"=="marzec" echo 3
if /i "%miesiac%"=="kwiecien" echo 4
if /i "%miesiac%"=="maj" echo 5
if /i "%miesiac%"=="czerwiec" echo 6
if /i "%miesiac%"=="lipiec" echo 7
if /i "%miesiac%"=="sierpien" echo 8
if /i "%miesiac%"=="wrzesien" echo 9
if /i "%miesiac%"=="pazdziernik" echo 10
if /i "%miesiac%"=="listopad" echo 11
if /i "%miesiac%"=="grudzien" echo 12
goto koniec

:brak_argumentow
echo Podaj nazwę miesiaca jako argument.
:koniec
pause