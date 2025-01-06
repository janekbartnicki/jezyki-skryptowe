@echo off
if "%1"=="create" (
    echo Test > test.txt
    echo Utworzono plik test.txt
) else if "%1"=="delete" (
    del test.txt
    echo Usunieto plik test.txt
) else (
    echo Blad.
)
pause