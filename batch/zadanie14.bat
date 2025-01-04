@echo off
echo Lista procesow:
tasklist
echo.
echo Liczba procesow:
tasklist | find /c /v ""
pause