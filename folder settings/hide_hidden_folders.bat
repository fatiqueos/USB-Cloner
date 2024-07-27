@echo off
REM This script disables the option to show hidden folders in Windows.

REM Registry key for the hidden folders setting
set RegKey=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
set RegValue=Hidden

REM Check the current setting in the registry
reg query "%RegKey%" /v "%RegValue%" | findstr "0x1" >nul
if %errorlevel% equ 0 (
    REM If the setting is on, turn it off
    reg add "%RegKey%" /v "%RegValue%" /t REG_DWORD /d 0 /f >nul
)

echo Hidden folders setting has been turned off.
