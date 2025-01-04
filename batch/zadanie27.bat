@echo off
setlocal EnableDelayedExpansion

echo 1. Wyswietl zawartosc
echo 2. Utworz folder
echo 3. Usun folder
set /p opcja="Wybierz opcje (1-3): "
set /p sciezka="Podaj sciezke lokalna: "

if not exist "%sciezka%" (
    echo Podana sciezka nie istnieje.
    goto koniec
)

cd "%sciezka%"

if "%opcja%"=="1" (
    dir .
) else if "%opcja%"=="2" (
    set /p nazwa="Podaj nazwe folderu: "
    if exist "!nazwa!" (
        echo Folder !nazwa! juz istnieje.
    ) else (
        mkdir "!nazwa!"
        echo Folder "!sciezka!\!nazwa!" zostal utworzony.
    )
) else if "%opcja%"=="3" (
    set /p nazwa="Podaj nazwe folderu: "
    if not exist "!nazwa!" (
        echo Folder !nazwa! nie istnieje.
    ) else (
        rmdir /s /q "!nazwa!"
        echo Folder "!sciezka!\!nazwa!" zostal usuniety.
    )
) else (
    echo Niepoprawna opcja.
)

:koniec
pause
