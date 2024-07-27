import winreg

def prevent_pin_to_quick_access():
    try:
        # Open the registry
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced"
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE)
        
        # Prevent pinning to Quick Access
        winreg.SetValueEx(reg_key, "DoNotUseQuickAccess", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(reg_key, "ShowRecentFiles", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(reg_key, "ShowRecentFolders", 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(reg_key)

        print("Pinned folders to Quick Access have been disabled. You may need to restart your computer for the changes to take effect.")
    except Exception as e:
        print(f"An error occurred: {e}")

prevent_pin_to_quick_access()
