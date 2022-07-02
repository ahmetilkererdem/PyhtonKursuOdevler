# ÖDEV :

#   +    1- Class yapısında olacak
#   +    2- En az 2 tane class metod olacak
#   +    3- dosya ve klasör yok kontrolü eklenecek
#   +    4- try except kullanılacak
#   +    5- raise kullanımı olacak
#       6- filter kullanımı olacak, yani ad soyad vs. bilgilerine göre arama yapabileceğim

# Öğrenci kayıt otomasyonu tasarlayınb, ogrenciler dosyaya kayıt edilecek, silinecek ve güncellenecek

####################################################################################################################

import os
from Fonksiyonlar import *

klasor_adi = "Öğrenciler"
dosyaYolu =  "C:\\PİRİ REİS ÜNİVERSİTESİ\\"+ klasor_adi

if ( os.path.exists("C:\\PİRİ REİS ÜNİVERSİTESİ") == False):
    os.mkdir("C:\\PİRİ REİS ÜNİVERSİTESİ")

if (os.path.exists(dosyaYolu) == False):
    os.mkdir(dosyaYolu)
os.chdir(dosyaYolu)

while True:
    print("******** PİRİ REİS ÜNİVERSİTESİ ********")
    print("""
        SEÇENEKLER:
        
        1- Öğrenci Kayıt Etme
        2- Öğrenci Kayıt Silme
        3- Öğrenci Kayıt Güncelleme
        
        0- Çıkış
        """)

    secenekler_secim = int(input("Seçiminiz: "))

    # try:
    #     if (secenekler_secim != (0 or 1 or 2 or 3)):
    #         raise ValueError()
    #
    # except ValueError:
    #     print("Geçersiz tuşlama! Lütfen yukarıdaki menüde verilen rakamlardan birini tuşlayınız.")

    if secenekler_secim == 0:
        print("Çıkılıyor...")
        break

    elif secenekler_secim == 1:
        Ogrenci.kaydet(liste)
        cevap = input("Anamenüye geçmek ister misin?(E/H): ").upper()
        if cevap == "E":
            continue
        elif cevap == "H":
            print("Çıkılıyor...")
            break
        else:
            print("Hatalı seçim!")

    elif secenekler_secim == 2:
        Ogrenci.sil(liste)
        cevap = input("Anamenüye geçmek ister misin?(E/H): ").upper()
        if cevap == "E":
            continue
        elif cevap == "H":
            print("Çıkılıyor...")
            break
        else:
            print("Hatalı seçim!")

    elif secenekler_secim == 3:
        Ogrenci.guncelle(liste)
        cevap = input("Anamenüye geçmek ister misin?(E/H): ").upper()
        if cevap == "E":
            continue
        elif cevap == "H":
            print("Çıkılıyor...")
            break
        else:
            print("Hatalı seçim!")

    else:
        cevap = input("Tekrar denemek ister misiniz? (E/H): ").upper()
        if cevap == "E":
            continue
        elif cevap == "H":
            print("Çıkılıyor...")
            break
        else:
            print("Hatalı seçim!")