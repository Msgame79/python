@chcp 65001>nul
@echo off

if "%1"=="" (
    echo no arguments
    pause
    exit
) else (
    rem
)
if "%2"=="" (
    rem
) else (
    echo 2 or more arguments
    pause
    exit
)

pyinstaller -F %1 > nul 2>&1

explorer .\dist

pause

exit