@echo off
REM Bu betik, Windows'ta varsayılan gizli klasörleri gösterme ayarını kontrol eder.
REM Eğer ayar açıksa, kapatır; kapalıysa, değiştirir.

REM Gizli klasörleri gösterme ayarının bulunduğu kayıt defteri anahtarı
set RegKey=HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
set RegValue=Hidden

REM Kayıt defterindeki mevcut ayarı kontrol etme
reg query "%RegKey%" /v "%RegValue%" | findstr "0x1" >nul
if %errorlevel% equ 0 (
    REM Ayar açıksa, kapatma işlemi
    reg add "%RegKey%" /v "%RegValue%" /t REG_DWORD /d 0 /f >nul
) else (
    REM Ayar kapalıysa, açma işlemi
    reg add "%RegKey%" /v "%RegValue%" /t REG_DWORD /d 1 /f >nul
)
