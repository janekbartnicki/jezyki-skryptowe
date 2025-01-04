@echo off
dir /b > temp.txt
for /f "tokens=*" %%a in (temp.txt) do (
    for /f "tokens=*" %%b in (temp.txt) do (
        if not "%%a"=="%%b" (
            echo Porownuje %%a z %%b:
            fc "%%a" "%%b"
            echo =====================================
        )
    )
)
del temp.txt
pause