@echo off
set /p liczba="Podaj liczbę: "
set /p operacja="Podaj operację (+,-,*,/): "
set /p liczba2="Podaj drugą liczbę: "

set /a wynik=0

if "%operacja%"=="+" set /a wynik=%liczba%+%liczba2%
if "%operacja%"=="-" set /a wynik=%liczba%-%liczba2%
if "%operacja%"=="*" set /a wynik=%liczba%*%liczba2%
if "%operacja%"=="/" set /a wynik=%liczba%/%liczba2%

echo Wynik: %wynik%
pause