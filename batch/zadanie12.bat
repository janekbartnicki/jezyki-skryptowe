@echo off
set count=0
for %%d in (C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    if exist %%d:\ (
        echo Przeszukiwanie dysku %%d:
        for /r %%d:\ %%G in (*.exe) do (
            set /a count+=1
            echo %%G
        )
        echo Zakonczono przeszukiwanie dysku %%d:
        echo ---------------------------------------
    )
)

echo.
echo Znaleziono %count% plików wykonywalnych w systemie
pause