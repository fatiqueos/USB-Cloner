import os
import subprocess
import sys

def open_directory_in_explorer(directory_path):
    """Verilen dizini Windows Gezgini'nde açar."""
    try:
        subprocess.run(['explorer', directory_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Dizin açılırken bir hata oluştu: {e}")
        sys.exit(1)

def main():
    # TEMP dizinini ve `.soǝnbᴉʇɐɟ` klasörünü tanımla
    temp_dir = os.getenv('TEMP', os.path.expanduser('~\\AppData\\Local\\Temp'))
    target_dir = os.path.join(temp_dir, '.soǝnbᴉʇɐɟ')

    # `.soǝnbᴉʇɐɟ` klasörünün var olup olmadığını kontrol et
    if not os.path.exists(target_dir):
        print(f"{target_dir} klasörü bulunamadı.")
        sys.exit(1)

    # Klasörü Windows Gezgini'nde aç
    open_directory_in_explorer(target_dir)

if __name__ == "__main__":
    main()
