@echo off
if "%1"=="/h" (
    echo Użycie: %0 [/a]
    echo /a - usuń wszystkie wpisy bez pytania
    echo /h - wyświetl pomoc
    goto koniec
)

if "%1"=="/a" (
    reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /f
    reg delete HKLM\Software\Microsoft\Windows\CurrentVersion\Run /f
    del /q "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\*.*"
) else (
    echo Czy chcesz usunąć wpisy autostartu? (T/N)
    choice /c tn /n
    if errorlevel 2 goto koniec
    
    reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /f
    reg delete HKLM\Software\Microsoft\Windows\CurrentVersion\Run /f
    del /q "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\*.*"
)

:koniec
pause