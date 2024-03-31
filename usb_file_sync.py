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

def find_usb_drive():
    drives = psutil.disk_partitions(all=True)
    for drive in drives:
        if 'removable' in drive.opts:
            return drive.device
    return None

def create_users_document_folder():
    documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
    target_folder = os.path.join(documents_path, 'Users Library')
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
    target_folder = create_users_document_folder()
    interval_seconds = 5  # Kopyalama işleminin tekrarlanma aralığı (saniye cinsinden)
    while True:
        try:
            usb_drive_letter = find_usb_drive()
            if usb_drive_letter:
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Kopyalama işlemi başladı...")
                copy_files(usb_drive_letter, target_folder)
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Kopyalama işlemi tamamlandı.")
            else:
                print("USB sürücü bulunamadı.")
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
