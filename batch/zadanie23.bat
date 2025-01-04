@echo off
if "%1"=="" (
    echo Użycie: %0 plik_wejsciowy
    goto koniec
)

set plik_wejsciowy=%1

if not exist "%plik_wejsciowy%" (
    echo Podany plik wejściowy "%plik_wejsciowy%" nie istnieje.
    goto koniec
)

for /f "usebackq delims=" %%a in ("%plik_wejsciowy%") do (
    echo Wykonywanie: %%a
    call "%%a"
)

:koniec
pause
