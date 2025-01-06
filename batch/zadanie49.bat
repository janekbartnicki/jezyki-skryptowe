@echo off
set /p folder="Podaj sciezke folderu: "

if not exist "%folder%" (
    echo Folder nie istnieje!
    goto koniec
)

echo Usuwanie plikow tymczasowych...
del /s /q "%folder%\*.tmp"
del /s /q "%folder%\~*.*"
del /s /q "%folder%\*.temp"
echo Zakonczono czyszczenie.

:koniec
pause