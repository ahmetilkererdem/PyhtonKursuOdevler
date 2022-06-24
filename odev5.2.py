### ÖDEV: Bir Şirket Otomasyonu tasarlayınız. İnsan Kaynakları, Muhasebe ve Bilgi İşlem birimleri olsun.
# Her personeli kendi birim adıyla oluşturulan txt dosyasına isim soyisim doğumyılı başlıkları altında personel bilgileri tutulsun.
# Personel ekleme, Güncelleme, Silme, Birime göre personel listeleme işlemlerini yapan bir menü tasarlayarak işlemler bu  menü üzerinden ilerlesin.

import datetime
import os
import random

# zaman =  datetime.date.today()
klasor_adi = "Birimler"
dosyaYolu =  "C:\\İlker Pazarlama\\"+ klasor_adi

if ( os.path.exists("C:\\İlker Pazarlama") == False):
    os.mkdir("C:\\İlker Pazarlama")

if (os.path.exists(dosyaYolu) == False):
    os.mkdir(dosyaYolu)
os.chdir(dosyaYolu)

while True:
    print("******** İLKER PAZARLAMA ********")
    print("""
        SEÇENEKLER:

        1- Personel Ekleme
        2- Personel Güncelleme
        3- Personel Silme
        4- Personel Listeleme

            Çıkış için "0" 
        """)

    secenekler_secim = int(input("Seçiminiz: "))

    if secenekler_secim == 1:

        print("""
            BİRİMLER:
            
            1- İnsan Kaynakları
            2- Muhasebe
            3- Bilgi İşlem

            """)

        birimler_secim = int(input("Seçiminiz: "))

        if birimler_secim == 1:

            dosya =  open(dosyaYolu+"\\İnsan Kaynakları.txt", "a+")

            dosya.write("""
                    AD SOYAD                    DOGUM YILI
                    --------                    ----------
            """)

            personel = int(input("Kaç kişi: "))

            for i in range(1, personel+1):

                ad = input(f"{i}. Kişinin Adı: ")
                soyad = input(f"{i}. Kişinin Soyadı: ")
                ad_soyad = ad + " " + soyad
                dogum_yili =  int(input(f"{i}. Kişinin Doğum Yılı: "))
                dosya.write(f"""
                    {str(ad_soyad)}                 {str(dogum_yili)}
                """)
                print("Personel eklenmştir.")
            dosya.close()

        elif birimler_secim == 2:

            dosya = open(dosyaYolu + "\\Muhasebe.txt", "a+")

            dosya.write("""
                    AD SOYAD                    DOGUM YILI
                    --------                    ----------
            """)

            personel = int(input("Kaç kişi: "))

            for i in range(1, personel + 1):
                ad = input(f"{i}. Kişinin Adı: ")
                soyad = input(f"{i}. Kişinin Soyadı: ")
                ad_soyad = ad + " " + soyad
                dogum_yili = int(input(f"{i}. Kişinin Doğum Yılı: "))
                dosya.write(f"""
                    {str(ad_soyad)}                 {str(dogum_yili)}
                """)
                print("Personel eklenmştir.")
            dosya.close()

        elif birimler_secim == 3:

            dosya = open(dosyaYolu + "\\Bilgi İşlem.txt", "a+")

            dosya.write("""
                    AD SOYAD                    DOGUM YILI
                    --------                    ----------
            """)

            personel = int(input("Kaç kişi: "))

            for i in range(1, personel + 1):
                ad = input(f"{i}. Kişinin Adı: ")
                soyad = input(f"{i}. Kişinin Soyadı: ")
                ad_soyad = ad + " " + soyad
                dogum_yili = int(input(f"{i}. Kişinin Doğum Yılı: "))
                dosya.write(f"""
                    {str(ad_soyad)}                 {str(dogum_yili)}
                """)
                print("Personel eklenmştir.")
            dosya.close()

        else:
            print("Hatalı Seçim")

        break

    elif secenekler_secim == 2:
        break

    elif secenekler_secim == 3:

        print("""
            BİRİMLER:

            1- İnsan Kaynakları
            2- Muhasebe
            3- Bilgi İşlem

            """)

        birimler_secim = int(input("Seçiminiz: "))

        if birimler_secim == 1:
            dosya_ik = dosyaYolu+"\\İnsan Kaynakları.txt"
            os.remove(dosya_ik)
            break

        elif birimler_secim == 2:
            dosya_m = dosyaYolu+"\\Muhasebe.txt"
            os.remove(dosya_m)
            break

        elif birimler_secim == 3:
            dosya_bi = dosyaYolu+"\\Bilgi İşlem.txt"
            os.remove(dosya_bi)
            break

    elif secenekler_secim == 4:

        dosyaYolu = "C:\\İlker Pazarlama\\" + klasor_adi
        dosya = open(dosyaYolu + "\\İnsan Kaynakları.txt", "r+")

        personelListesi = dosya.readlines()
        dosya.close()

        ad_soyad = list()

        for i in personelListesi:
            ad_soyad.append(int(i.rstrip("\n")))

        yeni_dosya_yolu =  "C:\\İlker Pazarlama\\" + klasor_adi

        dosya = open(yeni_dosya_yolu, mode="a+")

        for i in ad_soyad:
            dosya.write(f"{i}\n")

        dosya.close()

    elif secenekler_secim == 0:
        print("Çıkılıyor...")
        break

    else:
        print("Hatalı seçim")
        break


