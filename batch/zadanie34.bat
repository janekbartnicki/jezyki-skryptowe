@echo off
set /p tytul="Podaj tytul okna: "
title %tytul%

set /p katalog="Podaj sciezke katalogu: "
if not exist "%katalog%" (
    echo Katalog nie istnieje!
    goto koniec
)

set /p plik_wyjscia="Podaj nazwe pliku wejsciowego: "
dir "%katalog%" > "%plik_wyjscia%"

:koniec
pause