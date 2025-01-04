@echo off
title Sprawdzanie i kasowanie plików
set /p typ="Podaj rozszerzenie plików do sprawdzenia (bez kropki): "

dir *.%typ% >nul 2>nul
if errorlevel 1 (
    echo Nie znaleziono plików typu .%typ%
) else (
    set /p wybor="Znaleziono pliki .%typ%. Czy chcesz je usunąć? (T/N): "
    if /i "%wybor%"=="T" (
        del *.%typ%
        echo Pliki zostały usunięte.
    ) else (
        echo Operacja anulowana.
    )
)
pause