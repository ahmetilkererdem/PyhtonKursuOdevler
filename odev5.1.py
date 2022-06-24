# Kullanıcıdan personel sayı bilgisini al: Her personel için;
# Ad,Soyad,DogumYılı bilgilerini alarak PersonelKayitlari.txt dosyasına yazdırınız.

import datetime
import os
import random

zaman =  datetime.date.today()
klasor_adi = str(zaman)
dosyaYolu =  "C:\\ilker\\"+ klasor_adi

if ( os.path.exists("C:\\ilker") == False):
    os.mkdir("C:\\ilker")

if (os.path.exists(dosyaYolu) == False):
    os.mkdir(dosyaYolu)
os.chdir(dosyaYolu)

dosya =  open(dosyaYolu+"\\PersonelKayitlari.txt", "a+")

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

dosya.close()






