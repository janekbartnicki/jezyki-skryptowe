@echo off
wmic diskdrive get status,caption,size
wmic logicaldisk get name,freespace,size
pause