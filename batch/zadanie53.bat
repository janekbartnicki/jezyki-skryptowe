@echo off
set /p hex="Podaj liczbe w systemie szesnastkowym: "
set /a dec=0x%hex%
echo Liczba %hex% w systemie dziesietnym to: %dec%
pause