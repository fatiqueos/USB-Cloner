@echo off
REM Bu betik, Windows'ta gizli klasorleri gostermek secenegini aciklar.

REM Gizli klasorler ayari icin kayit defteri anahtari
set RegKey=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
set RegValue=Hidden

REM Kayit defterindeki mevcut ayari kontrol et
reg query "%RegKey%" /v "%RegValue%" | findstr "0x0" >nul
if %errorlevel% equ 0 (
    REM Eger ayar kapaliysa, ac
    reg add "%RegKey%" /v "%RegValue%" /t REG_DWORD /d 1 /f >nul
)

echo Gizli klasorler ayari acildi.
