@echo off
setlocal enabledelayedexpansion

set "input="
set /p "input=Wprowadz ciag znakow: "

set "start="
set /p "start=Wprowadz pozycje startowa (liczba, zaczyna sie od 0): "
set "length="
set /p "length=Wprowadz liczbe znakow do wybrania: "

set "substring="
if %start% lss 0 (
    echo Pozycja startowa nie moze byc mniejsza od 0.
    exit /b
)

if %start% geq %length% (
    echo Pozycja startowa nie moze byc wieksza niz dlugosc ciagu.
    exit /b
)

if %length% leq 0 (
    echo Liczba znakow do wybrania musi byc wieksza niz 0.
    exit /b
)

set "substring=!input:~%start%,%length%!"

echo Wybrany podciag: !substring!
pause
