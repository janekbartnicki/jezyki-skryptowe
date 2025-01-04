@echo off
if "%1"=="" (
    echo Nie wprowadzono imienia jako argument!
    goto koniec
)
title %1
echo Twoje imie jest teraz w tytule okna

:koniec
pause