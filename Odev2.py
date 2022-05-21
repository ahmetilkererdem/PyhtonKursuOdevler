## Kullanıcıdan 1.vize ve 2.vize  final not girilmesi istensin not aralığı 0 ile 100 arasında olmalıdır.
## vize ve finalin ortalaması alınsın.
## 0-44 : Kaldınız
## 45-69: Geçtiniz
## 70-84: İyi
## 85-100: Pekiyi

vize1 = int(input("Lütfen 1. Vize Notunuzu Giriniz: "))

vize2 = int(input("Lütfen 2. Vize Notunuzu Giriniz: "))

final = int(input("Lütfen Final Notunuzu Giriniz: "))

ortalama = float(((vize1 + vize2)/2)*0.4 + final*0.6)

if final < 35:
    print("Sonuç: Kaldınız")
elif final >= 35:
    if (ortalama >= 0 and ortalama < 45):
        print("Ortalamanız:", ortalama )
        print("Sonuç: Kaldınız")
    elif (ortalama >= 45 and ortalama < 70):
        print("Ortalamanız:", ortalama )
        print("Sonuç: Geçtiniz")
    elif (ortalama >= 70 and ortalama < 85):
        print("Ortalamanız:", ortalama )
        print("Sonuç: İyi")
    elif (ortalama >= 85 and ortalama <= 100):
        print("Ortalamanız:", ortalama )
        print("Sonuç: Pekiyi")
    else:
        print("Hatalı Sonuç!")

# ÖDEV: Kullanıcıdan isim,yaş,maaş ve çocuk sayısı alalım
# """
#     Eğer kullanıcının yaşı 45'in altındaysa;
#         çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺, değilse çocuk başına 200₺ maaşa eklenecek
#     Eğer kullanıcının yaşı 45 ve üzerinde ise:
#         çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.
#
#     Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak.
# """

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = int(input("Yaşınız: "))
maas = int(input("Maaşınız: "))
cocuk_sayisi = int(input("Çocuk Sayısı: "))

if yas < 45:
    if cocuk_sayisi < 3:
        maas += (cocuk_sayisi*250)
    else:
        maas += (cocuk_sayisi*200)
elif yas >= 45:
    maas += 500

print( ad + " " + soyad, "Maaşınız:", maas,"₺")

# ÖDEV: Kullanıcı Gİriş Paneli Tasarlayınız.
# """
#     Kullanıcıadı/Email ve şifre ile giriş sağlanacak
#         Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
#         Değilse
#             Kullanıcıya kayıt olmak ister misiniz?
#                 Hayır ise PEKİ!!!
#                 Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
#                     şifre ve şifretekrarın aynı olması
# """
# """
kullanici_adi = "ilkererdem"
sifre = "1234"
cevap1 = "Evet"
cevap2 = "Hayır"
kullanici_adi_sor = input("Kullanıcı Adı: ")
sifre_sor = input("Şifre: ")

if (kullanici_adi_sor == kullanici_adi and sifre_sor == sifre):
    print("Giriş Başarılı!")
elif (kullanici_adi_sor == kullanici_adi and sifre_sor != sifre):
    print("Hatalı Şifre! Giriş Başarısız!")
elif (kullanici_adi_sor != kullanici_adi):
    print(input("Kullanıcı Bulunamadı! Kayıt olmak ister misiniz? "))
    if cevap1 == ("Evet"):
        kullanici_adi_gir = input("Kullanıcı Adı: ")
        kullanici_ad = input("Adı: ")
        kullanici_soyad = input("Soyadı: ")
        email = input("Email: ")
        sifre = input("Şifre: ")
        sifre_tekrar = input("Şifre Tekrar: ")
        if (sifre == sifre_tekrar):
            print("Kayıt başarılı!")
        elif (sifre != sifre_tekrar):
            print("Şifreler aynı olmalı!")
elif cevap2 == ("Hayır"):
    print("Peki")






