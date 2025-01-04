@echo off
echo Nazwa komputera:
hostname
echo.

echo Woluminy:
wmic logicaldisk get caption,volumename,size

echo.
echo Karty sieciowe i adresy MAC:
getmac

echo.
echo Adresacja IP:
ipconfig /all

pause