
import datetime
import random
from Kelimeler import *
import os


zaman = datetime.date.today()
klasor_adi = "Oyuncu Puan Tablosu"
dosyaYolu = "C:\\ADAM ASMACA\\" + klasor_adi

if (os.path.exists("C:\\ADAM ASMACA") == False):
    os.mkdir("C:\\ADAM ASMACA")

if (os.path.exists(dosyaYolu) == False):
    os.mkdir(dosyaYolu)
os.chdir(dosyaYolu)

kelime = list()

class AdamAsmaca():

    @classmethod
    def adamasmaca(cls, kelime):
        toplam_puan = 0
        yanlis = 0

        oyuncu_adi = input("Oyuncu Adı: ")
        print("""
                SEVİYE:

                1- Kolay
                2- Orta
                3- Zor
                """)

        secenekler_secim = int(input("Seçiminiz: "))

        while True:
            asilma = ["",
                      "__________      ",
                      "         |      ",
                      "         0      ",
                      "        /|\     ",
                      "        / \     ",
                      ]
            if secenekler_secim == 1:
                tahmin_kelime = random.choice(kolay)
                harf_okuma = list(tahmin_kelime)
                board = ["_"] * len(tahmin_kelime)
                kazanma = False
                if tahmin_kelime in kolay_esya:
                    print("Kategori: Eşya")
                elif tahmin_kelime in kolay_giysi:
                    print("Kategori: Giysi")
                elif tahmin_kelime in kolay_hayvan:
                    print("Kategori: Hayvan")
                elif tahmin_kelime in kolay_meyve:
                    print("Kategori: Meyve")
                elif tahmin_kelime in kolay_sebze:
                    print("Kategori: Sebze")
                print("_ " * len(tahmin_kelime))
                while yanlis < len(asilma) - 1:
                    print("\n")
                    harf = input("Bir harf tahmin et: ")
                    if harf in harf_okuma:
                        cind = harf_okuma \
                            .index(harf)
                        board[cind] = harf
                        harf_okuma[cind] = '$'
                    else:
                        yanlis += 1
                    print((" ".join(board)))
                    e = yanlis + 1
                    print("\n"
                          .join(asilma[0: e]))
                    if "_" not in board:
                        print(f"Tebrikler {oyuncu_adi}! Bildiniz.")
                        print("Sorulan kelime:",tahmin_kelime)
                        kazanma = True
                        toplam_puan += (len(tahmin_kelime))
                        print("Toplam Puan: ",toplam_puan)
                        del tahmin_kelime
                        break
                if not kazanma:
                    print(f"Maalesef kaybettin {oyuncu_adi}! Sorulan kelime:",tahmin_kelime)
                    print("Toplam Puan: ",toplam_puan)
                    if toplam_puan > 0:
                        dosya = open(dosyaYolu + "\\Oyuncu Puan Tablosu.txt", "a+")
                        dosya.write(f"""
Oyuncu adı: {str(oyuncu_adi)}           Puan: {str(toplam_puan)}            Tarih: {str(zaman)}
""")
                        dosya.close()
                    break

            elif secenekler_secim ==2:
                tahmin_kelime = random.choice(orta)
                harf_okuma = list(tahmin_kelime)
                board = ["_"] * len(tahmin_kelime)
                kazanma = False
                if tahmin_kelime in orta_esya:
                    print("Kategori: Eşya")
                elif tahmin_kelime in orta_giysi:
                    print("Kategori: Giysi")
                elif tahmin_kelime in orta_hayvan:
                    print("Kategori: Hayvan")
                elif tahmin_kelime in orta_meyve:
                    print("Kategori: Meyve")
                elif tahmin_kelime in orta_sebze:
                    print("Kategori: Sebze")
                print("_ " * len(tahmin_kelime))
                while yanlis < len(asilma) - 1:
                    print("\n")
                    harf = input("Bir harf tahmin et: ")
                    if harf in harf_okuma:
                        cind = harf_okuma \
                            .index(harf)
                        board[cind] = harf
                        harf_okuma[cind] = '$'
                    else:
                        yanlis += 1
                    print((" ".join(board)))
                    e = yanlis + 1
                    print("\n"
                          .join(asilma[0: e]))
                    if "_" not in board:
                        print(f"Tebrikler {oyuncu_adi}! Bildiniz.")
                        print("Sorulan kelime:",tahmin_kelime)
                        kazanma = True
                        toplam_puan += (len(tahmin_kelime))
                        print("Toplam Puan: ",toplam_puan)
                        del tahmin_kelime
                        break
                if not kazanma:
                    print(f"Maalesef kaybettin {oyuncu_adi}! Sorulan kelime:",tahmin_kelime)
                    print("Toplam Puan: ",toplam_puan)
                    if toplam_puan > 0:
                        dosya = open(dosyaYolu + "\\Oyuncu Puan Tablosu.txt", "a+")
                        dosya.write(f"""
Oyuncu adı: {str(oyuncu_adi)}           Puan: {str(toplam_puan)}            Tarih: {str(zaman)}
""")
                        dosya.close()
                    break

            elif secenekler_secim ==3:
                tahmin_kelime = random.choice(zor)
                harf_okuma = list(tahmin_kelime)
                board = ["_"] * len(tahmin_kelime)
                kazanma = False
                if tahmin_kelime in zor_esya:
                    print("Kategori: Eşya")
                elif tahmin_kelime in zor_giysi:
                    print("Kategori: Giysi")
                elif tahmin_kelime in zor_hayvan:
                    print("Kategori: Hayvan")
                elif tahmin_kelime in zor_meyve:
                    print("Kategori: Meyve")
                elif tahmin_kelime in zor_sebze:
                    print("Kategori: Sebze")
                print("_ " * len(tahmin_kelime))
                while yanlis < len(asilma) - 1:
                    print("\n")
                    harf = input("Bir harf tahmin et: ")
                    if harf in harf_okuma:
                        cind = harf_okuma \
                            .index(harf)
                        board[cind] = harf
                        harf_okuma[cind] = '$'
                    else:
                        yanlis += 1
                    print((" ".join(board)))
                    e = yanlis + 1
                    print("\n"
                          .join(asilma[0: e]))
                    if "_" not in board:
                        print(f"Tebrikler {oyuncu_adi}! Bildiniz.")
                        print("Sorulan kelime:",tahmin_kelime)
                        kazanma = True
                        toplam_puan += (len(tahmin_kelime))
                        print("Toplam Puan: ",toplam_puan)
                        del tahmin_kelime
                        break
                if not kazanma:
                    print(f"Maalesef kaybettin {oyuncu_adi}! Sorulan kelime:",tahmin_kelime)
                    print("Toplam Puan: ",toplam_puan)
                    if toplam_puan > 0:
                        dosya = open(dosyaYolu + "\\Oyuncu Puan Tablosu.txt", "a+")
                        dosya.write(f"""
Oyuncu adı: {str(oyuncu_adi)}           Puan: {str(toplam_puan)}            Tarih: {str(zaman)}
""")
                        dosya.close()
                    break


    @classmethod
    def puantablosu (cls, kelime):
        dosya = open(dosyaYolu + "\\Oyuncu Puan Tablosu.txt", "r")
        dosya.seek(0)
        print("\n*********************** PUAN TABLOSU ***********************\n", dosya.read())
