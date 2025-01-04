@echo off
if "%1"=="" (
    echo Użycie: %0 folder_wejsciowy plik_wyjsciowy
    goto koniec
)
if "%2"=="" (
    echo Użycie: %0 folder_wejsciowy plik_wyjsciowy
    goto koniec
)

set folder_wejsciowy=%1
set plik_wyjsciowy=%2

if not exist "%folder_wejsciowy%" (
    echo Podany folder wejściowy "%folder_wejsciowy%" nie istnieje.
    goto koniec
)

dir /b /a-d "%folder_wejsciowy%\*.txt" "%folder_wejsciowy%\*.log" > "%plik_wyjsciowy%"

if exist "%plik_wyjsciowy%" (
    echo Lista wybranych elementow zapisana w pliku "%plik_wyjsciowy%".
) else (
    echo Nie udalo się zapisac listy w pliku "%plik_wyjsciowy%".
)

:koniec
pause
