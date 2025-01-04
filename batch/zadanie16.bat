@echo off
title Chat
set /p komputer="Podaj nazwe lub IP komputera do polaczenia: "
msg /server:%komputer% * /time:99999
pause