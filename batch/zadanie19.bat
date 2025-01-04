@echo off
if not exist "wczesniej_niz_4_mies" (
    echo Nie mozna odnalezc pliku wczesniej_niz_4_mies
    exit
)
cd wczesniej_niz_4_mies
echo Czy na pewno chcesz usunac wszystkie pliki .txt? (T/N)
set /p wybor=
if /i "%wybor%"=="T" (
    del *.txt
    echo Usunieto wszystkie pliki .txt
) else (
    echo Operacja anulowana
)
pause