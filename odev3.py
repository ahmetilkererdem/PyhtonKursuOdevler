"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak. 3 defa giriş hakkı vardır.
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması


"""
# giris_hakki = 1
#
# kullanici_adi = "İlker"
# sifre = "1234"
# email = "ilker.erdem@gmail.com"
#
# kullanici_adi_sor = input( "Kullanıcı/Email Giriniz: " )
# sifre_sor = input( "Şifre: " )
#
# while (giris_hakki <= 3):
#     if ((kullanici_adi == kullanici_adi_sor) or (email == kullanici_adi_sor)) and (sifre == sifre_sor):
#         print( "Giriş başarılı!" )
#         break
#     elif ((kullanici_adi == kullanici_adi_sor) or (email == kullanici_adi_sor)) and (sifre != sifre_sor):
#         giris_kontrol = input("Hatalı şifre! Tekrar deneyiniz: ")
#         if giris_kontrol == sifre:
#             print("Giriş başarılı!")
#             break
#         else:
#             giris_hakki += 1
#             if giris_hakki == 3:
#                 print("Hesabınız bloke edilmiştir! Lütfen doğrulayınız.")
#                 break
#     else:
#         control = input( "Kullanıcı bulunamadı! Kayıt olmak ister misiniz? 'Evet' veya 'Hayır': " )
#         if control == "Hayır":
#             print( "Peki" )
#             break
#         elif control == "Evet":
#             ad = input( "Adı: " )
#             soyad = input( "Soyadı: " )
#             email = input( "Email: " )
#             yeni_kullanici_adi = input( "Kullanıcı Adı: " )
#             yeni_sifre = input( "Şifre: " )
#             sifre_tekrar = input( "Şifre Tekrar: " )
#             if sifre_tekrar == yeni_sifre:
#                 print( "Hesap oluşturma başarılı!" )
#             else:
#                 print( "Şifreler uyuşmamaktadır! Tekrar deneyiniz" )
#         break

#########################################################################################

#SORU: Kullanıcıdan personel sayısını alınız.
# Personelin kaç çocuğu olduğunu isteyelim.
# Program her çocuk için "Çocuğunuz adına 1 ağaç dikilmiştir" yazsın
# Toplam dikilen ağaç sayısınıda ekrana yazdıralım.

# isim = input("Adı: ")
# soyisim = input("Soyadı: ")
# cocuk_sayisi = int(input("Çocuk Sayısı: "))
#
# print("Çocuğunuz adına 1 adet ağaç dikilecektir.")
#
# for agac_sayisi in range(cocuk_sayisi):
#     agac = cocuk_sayisi*1
#     print("Toplam dikilecek ağaç sayısı: ", int(agac))

#########################################################################################

# SORU 10 ile 100 arasındaki tek sayıları bir listeye atın.

# tekler = list()
# for tek_sayilar in range( 11, 101, 2 ):
#     tekler.append(tek_sayilar)
# print(tekler)

#########################################################################################

# SORU: 1-200 arasında 20 adet rasgele sayi üretip sayilar isimli bir listeye atayınız.
# NOT: Sayının listede tekrar eklenmesini engelleyiniz.

# import random
#
# sayilar = list()
# for i in range(20):
#     sayi = random.randint(1,200)
#     if sayi not in sayilar:
#         sayilar.append(sayi)
#         continue
#
#
# sayilar.sort()
# print(sayilar)
# print(len(sayilar))