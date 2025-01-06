@echo off
title Sprawdzanie i kasowanie plików
set /p typ="Podaj rozszerzenie plikow do usuniecia (bez kropki): "

dir *.%typ% >nul 2>nul
if errorlevel 1 (
    echo Nie znaleziono plokow typu .%typ%
) else (
    del *.%typ%
    echo Pliki zostaly usuniete.
)
pause