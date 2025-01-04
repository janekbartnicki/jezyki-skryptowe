@echo off
if exist "wczesniej_niz_4_mies" (
    cd wczesniej_niz_4_mies
    attrib +a *.txt
    echo Zmieniono atrybut
)
pause
