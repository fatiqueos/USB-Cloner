import os
import shutil
from datetime import datetime
import time
import subprocess
import sys
import logging
import psutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(SCRIPT_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

TEMP_DIR = os.getenv('TEMP', os.path.expanduser('~\\AppData\\Local\\Temp'))
BASE_DIR = os.path.join(TEMP_DIR, '.soǝnbᴉʇɐɟ')
os.makedirs(BASE_DIR, exist_ok=True)

def setup_logging():
    log_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '_yedek.log'
    log_filepath = os.path.join(LOG_DIR, log_filename)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename=log_filepath, filemode='w')
    return log_filepath

def find_usb_drives():
    drives = psutil.disk_partitions(all=True)
    usb_drives = []
    for drive in drives:
        if 'removable' in drive.opts:
            usb_drives.append(drive.mountpoint)
    return usb_drives

def create_backup_folder(backup_date):
    backup_folder_name = backup_date.strftime('%Y-%m-%d')
    target_folder = os.path.join(BASE_DIR, backup_folder_name)
    os.makedirs(target_folder, exist_ok=True)
    return target_folder

def copy_files(src, dest):
    try:
        for item in os.listdir(src):
            file_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)
            if os.path.isfile(file_path):
                try:
                    shutil.copy(file_path, dest_path)
                except PermissionError:
                    logging.warning(f"{file_path} icin izin reddedildi. Atlanıyor.")
                except Exception as e:
                    logging.error(f"{file_path} dosyasini kopyalarken hata: {e}")
            elif os.path.isdir(file_path):
                try:
                    os.makedirs(dest_path, exist_ok=True)
                    copy_files(file_path, dest_path)
                except PermissionError:
                    logging.warning(f"{file_path} dizini icin izin reddedildi. Atlanıyor.")
                except Exception as e:
                    logging.error(f"{file_path} dizinini kopyalarken hata: {e}")
    except Exception as e:
        logging.error(f"Kopyalama islemi sirasinda hata: {e}")

def backup_usb_drives():
    current_date = datetime.now()
    usb_drives = find_usb_drives()
    if usb_drives:
        backup_folder = create_backup_folder(current_date)
        for usb_drive in usb_drives:
            logging.info(f"{usb_drive} icin yedekleme islemi baslatiliyor...")
            try:
                copy_files(usb_drive, backup_folder)
            except Exception as e:
                logging.error(f"{usb_drive} yedekleme sirasinda hata: {e}")
            else:
                logging.info(f"{usb_drive} icin yedekleme tamamlandi.")
    else:
        logging.info("Hicbir USB surucusu bulunamadi.")

def countdown(seconds):
    time.sleep(seconds)

def main():
    setup_logging()
    
    countdown(10)
    interval_seconds = 5
    while True:
        try:
            backup_usb_drives()
        except Exception as e:
            logging.error(f"Bir hata olustu: {e}. Yeniden deniyor.")
        time.sleep(interval_seconds)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Kapatma istegi alindi. Cikiliyor...")
    except Exception as e:
        logging.error(f"Bir hata olustu: {e}. Yeniden baslatiliyor...")
