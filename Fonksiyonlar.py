klasor_adi = "Öğrenciler"
dosyaYolu = "C:\\PİRİ REİS ÜNİVERSİTESİ\\" + klasor_adi

liste = list()

class Ogrenci():

    ad = []
    soyad = []
    cinsiyet = []
    tc_no = []
    dogum_tarihi = []
    numara = []

    @classmethod
    def kaydet(cls, liste):
        while True:
            dosya = open(dosyaYolu + "\\Ogrenci Listesi.txt", "a+")
            print("***** ÖĞRENCİ KAYIT *****")
            a = Ogrenci()
            a.ad = input("Adı: ")
            a.soyad = input("Soyadı: ")
            a.cinsiyet = input("Cinsiyet (E/K): ")
            a.tc_no = input("TC Kimlik No: ")
            a.dogum_tarihi = input("Doğum Tarihi: ")
            a.numara = int(input("Numara: "))
            try:
                if (a.ad == []) or (a.soyad == []) or (a.cinsiyet == []) or (a.tc_no == []) or (a.dogum_tarihi == []) or ((a.numara == [])):
                    raise RuntimeError()
                print(f"Adı: {a.ad}\nSoyadı: {a.soyad}\nCinsiyet: {a.cinsiyet}\nTC Kimlik No: {a.tc_no}\nDoğum Tarihi: {a.dogum_tarihi}\nNumara: {str(a.numara)}")
                liste.append(a)
                dosya.write(a.ad + "        " + a.soyad + "     " + a.cinsiyet + "     " + a.tc_no + "      " + a.dogum_tarihi + "     " + str(a.numara) + "\n")
                dosya.close()
                cevap = input("Devam etmek ister misin?(E/H): ").upper()
                if cevap == "E":
                    continue
                elif cevap == "H":
                    print("Kaydetme işlemi tamamlandı.")
                    break
                else:
                    print("Hatalı seçim!")
            except RuntimeError:
                print("Eksik bilgi var! Yeniden deneyiniz.")
                del a

    @classmethod
    def sil(cls, liste):
        dosya = open(dosyaYolu + "\\Ogrenci Listesi.txt", "r+")
        ogrenci_listesi = dosya.readlines()
        dosya.seek(0)
        print("********************* ÖĞRENCİ LİSTESİ *********************\n", dosya.read())
        silinecek_personel = int(input("Silinecek personelin sıra numarasını girin: "))
        del ogrenci_listesi[silinecek_personel - 1]
        dosya.close()
        yeni_ogrenci_listesi = open(dosyaYolu + "\\Ogrenci Listesi.txt", "w+")
        yeni_ogrenci_listesi.writelines(ogrenci_listesi)
        print("Silme işlemi tamamlandı.")
        yeni_ogrenci_listesi.close()

    @classmethod
    def guncelle(cls, liste):
        dosya = open(dosyaYolu + "\\Ogrenci Listesi.txt", "r+")
        ogrenci_listesi = dosya.readlines()
        dosya.seek(0)
        print("********************* ÖĞRENCİ LİSTESİ *********************\n", dosya.read())
        guncellenecek_ogrenci = int(input("Güncellenecek öğrencinin sıra numarasını girin: "))
        dosya.close()
        print(ogrenci_listesi[guncellenecek_ogrenci-1])
        del ogrenci_listesi[guncellenecek_ogrenci - 1]
        ad = input("Adı: ")
        soyad = input("Soyadı: ")
        cinsiyet = input("Cinsiyet (E/K): ")
        tc_no = input("TC Kimlik No: ")
        dogum_tarihi = input("Doğum Tarihi: ")
        numara = int(input("Numara: "))
        ogrenci_listesi.insert(guncellenecek_ogrenci - 1, ad + "        " + soyad + "     " + cinsiyet + "     " + tc_no + "      " + dogum_tarihi + "     " + str(numara) + "\n")
        yeni_dosya = open(dosyaYolu + "\\Ogrenci Listesi.txt", "w+")
        yeni_dosya.writelines(ogrenci_listesi)
        print("Güncelleme işlemi tamamlandı.\nGüncel hali: ", ogrenci_listesi[guncellenecek_ogrenci - 1])
        yeni_dosya.close()
