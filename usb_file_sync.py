import os
import shutil
from datetime import datetime
import time
import subprocess
import sys

try:
    import psutil
except ImportError:
    print("psutil kütüphanesi yüklenemedi. Yükleniyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil

def find_usb_drives():
    drives = psutil.disk_partitions(all=True)
    usb_drives = []
    for drive in drives:
        if 'removable' in drive.opts:
            usb_drives.append(drive.mountpoint)
    return usb_drives

def create_backup_folder(backup_date):
    backup_folder_name = backup_date.strftime('%Y-%m-%d')
    target_folder = os.path.join(os.path.expanduser('~'), '.distorted', backup_folder_name)
    os.makedirs(target_folder, exist_ok=True)
    return target_folder

def copy_files(src, dest):
    try:
        for item in os.listdir(src):
            file_path = os.path.join(src, item)
            if os.path.isfile(file_path):
                try:
                    shutil.copy(file_path, dest)
                except Exception as e:
                    print(f"{file_path} dosyası kopyalanırken hata oluştu: {e}")
            elif os.path.isdir(file_path):
                new_dest = os.path.join(dest, item)
                os.makedirs(new_dest, exist_ok=True)
                copy_files(file_path, new_dest)
    except Exception as e:
        print(f"Hata oluştu: {e}")

def main():
    interval_seconds = 5  # Kopyalama işleminin tekrarlanma aralığı (saniye cinsinden)
    while True:
        try:
            current_date = datetime.now()
            usb_drives = find_usb_drives()
            if usb_drives:
                backup_folder = create_backup_folder(current_date)
                for usb_drive in usb_drives:
                    print(f"[{current_date.strftime('%Y-%m-%d %H:%M:%S')}] Kopyalama işlemi başladı...")
                    copy_files(usb_drive, backup_folder)
                    print(f"[{current_date.strftime('%Y-%m-%d %H:%M:%S')}] Kopyalama işlemi tamamlandı.")
            else:
                print("USB sürücüsü bulunamadı.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}. Tekrar denenecek.")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Kapatma talebi alındı. Çıkılıyor...")
            break
        except Exception as e:
            print(f"Bir hata oluştu: {e}. Yeniden başlatılıyor...")
