@echo off
echo WYMAGANY JEST PROGRAM IMAGEMAGICK!

for %%a in (%*) do (
    for %%f in (*.jpg *.png) do (
        echo Konwertowanie %%f...
        magick "%%f" "%%~nf.eps"
    )
)
echo Zakonczono konwersje.
pause