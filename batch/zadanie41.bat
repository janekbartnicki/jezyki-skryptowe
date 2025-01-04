@echo off
title Lista katalogów do pliku
if "%1"=="" goto brak_argumentow

dir /ad /b > "%1"
echo Lista katalogow zostala zapisana do %1
goto koniec

:brak_argumentow
echo Podaj plik wyjsciowy!
:koniec
pause