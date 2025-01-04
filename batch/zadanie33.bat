@echo off
if "%1"=="" goto brak_argumentow
title %1
tree %1
goto koniec

:brak_argumentow
echo Wystapil blad.
:koniec
pause