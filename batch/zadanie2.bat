@echo off

:input
set /p sciezka="Podaj sciezke do analizy (np. C:\Users): "

if not exist "%sciezka%" (
    echo Blad: Podana sciezka nie istnieje.
    goto input
)

echo Struktura katalogow dla: %sciezka%
tree "%sciezka%" /F
pause