@echo off
setlocal enabledelayedexpansion

if "%~1"=="" (
    echo Blad: Nie podano pliku wejsciowego.
    exit /b
)

if "%~2"=="" (
    echo Blad: Nie podano slowa do usuniecia.
    exit /b
)

if not exist "%~1" (
    echo Blad: Plik %~1 nie istnieje.
    exit /b
)

set "content="
for /f "usebackq delims=" %%a in ("%~1") do (
    if not defined content (
        set "content=%%a"
    ) else (
        set "content=!content! %%a"
    )
)

set "word_to_remove=%~2"

set "content=!content:%word_to_remove%=!"

echo.
echo Oryginalny tekst z pliku:
type "%~1"
echo.
echo Tekst po usunieciu slowa "%word_to_remove%":
echo !content!
pause