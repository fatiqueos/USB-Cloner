import winreg

def prevent_pin_to_quick_access():
    try:
        # Kayıt defterini aç
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE)
        
        # Hızlı erişim sabitlemelerini engelle
        winreg.SetValueEx(reg_key, "DoNotUseQuickAccess", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(reg_key, "ShowRecentFiles", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(reg_key, "ShowRecentFolders", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(reg_key)

        print("Hızlı erişime klasör sabitlemeleri engellendi. Değişikliklerin etkili olması için bilgisayarınızı yeniden başlatmanız gerekebilir.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

prevent_pin_to_quick_access()
