@echo off
if exist "wczesniej_niz_4_mies" ( 
    cd wczesniej_niz_4_mies
) else (
    echo Nie mozna znalezc pliku wczesniej_niz_4_mies.
    exit
)
dir /b > lista_plikow.txt
for /f "tokens=*" %%a in (lista_plikow.txt) do (
    for /f "tokens=*" %%b in (lista_plikow.txt) do (
        if not "%%a"=="%%b" (
            echo Porownuje %%a z %%b:
            fc "%%a" "%%b"
            echo =====================================
        )
    )
)
del lista_plikow.txt
cd ..
pause