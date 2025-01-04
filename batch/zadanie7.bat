@echo off
if not exist "wczesniej_niz_4_mies" mkdir "wczesniej_niz_4_mies"
forfiles /D -4 /C "cmd /c if @isdir==FALSE copy @file ..\wczesniej_niz_4_mies"
pause