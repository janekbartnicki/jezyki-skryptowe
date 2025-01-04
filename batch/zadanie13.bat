@echo off
echo Testowanie połączenia z internetem...
ping 8.8.8.8 -n 4
ping google.com -n 4
echo.
echo Trasa do google.com:
tracert google.com
pause