@echo off
:menu
cls
echo 1. Opcja pierwsza
echo 2. Opcja druga
echo 3. Wyjscie
set /p wybor="Wybierz opcje: "

if "%wybor%"=="1" goto opcja1
if "%wybor%"=="2" goto opcja2
if "%wybor%"=="3" goto koniec
goto menu

:opcja1
echo Wykonano opcje 1
pause
goto menu

:opcja2
echo Wykonano opcje 2
pause
goto menu

:koniec
echo Do widzenia!
pause