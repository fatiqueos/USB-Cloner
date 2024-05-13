# USB Sürücüsünden Gizlice Dosya Kopyalama Betiği

Bu Python betiği, bir USB sürücüsündeki dosyaları belirli bir gizli klasöre kopyalayan ve yedekleyen bir araçtır.
Araç, belirli aralıklarla USB sürücüsündeki verileri yedeklemek için kullanılabilir. Ancak, bu betiğin kötü amaçlı kullanımı izinsiz veri kopyalamaya yöneliktir ve yasadışı etkinliklerde kullanılması kesinlikle önerilmez.
Kullanıcılar, yalnızca yasal ve etik amaçlar için bu aracı kullanmalıdır. Verilerin gizliliğini ve güvenliğini sağlamak için lütfen yalnızca kendi USB sürücülerinizde ve yasal izinlerle kullanın.

## Gereksinimler

Bu betiğin çalışması için aşağıdaki gereksinimlerin karşılanması gerekmektedir:
- Python 3
- psutil kütüphanesi

psutil kütüphanesini yüklemek için terminal veya komut istemcisinde aşağıdaki komutu çalıştırabilirsiniz:

pip install psutil

markdown


## Kullanım

1. **Gereksinimleri Kontrol Edin:** Betiği çalıştırmadan önce `psutil` kütüphanesini yüklediğinizden emin olun.

2. **Betiği Çalıştırın:** Betiği çalıştırdığınızda, USB sürücüsü bağlı değilse veya erişilemezse uygun bir mesaj alacaksınız.

3. **USB Sürücüsü Bağlandığında:** USB sürücüsü bağlandığında, betik sürücüdeki dosyaları belirlenen hedef klasöre kopyalayacaktır.

4. **Kopyalama İşlemi:** Kopyalama işlemi belirli aralıklarla (varsayılan olarak 5 saniye) tekrarlanacaktır.

## Önemli Notlar

- **İzinler:** Betiği çalıştırmak için yüksek izinlere (root yetkileri) ihtiyacınız olabilir, özellikle de işletim sisteminizde dosya sistemlerine erişim kısıtlamaları varsa.

- **Dosya Erişimi:** USB sürücüsünün bağlı olduğundan ve dosyaların kopyalanabilir olduğundan emin olun.

- **Betiği Durdurma:** Betiği durdurmak için klavyeden `Ctrl + C` tuşlarına basabilirsiniz.

## İletişim Bilgileri

- Telegram: [t.me/fatiqueos](https://t.me/fatiqueos)
- Discord: fatiqueos#0
