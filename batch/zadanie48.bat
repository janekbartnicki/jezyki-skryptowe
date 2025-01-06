@echo off
title Szukanie pliku
if "%1"=="" goto brak_argumentow

echo Szukanie pliku %1...
for %%d in (C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    if exist %%d:\ (
        echo Przeszukiwanie dysku %%d:
        dir /s /b "%%d:\%1" 2>nul
    )
)
goto koniec

:brak_argumentow
echo Blad argumentow.
:koniec
pause