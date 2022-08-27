from Adamasmaca import *

while True:

    print("""
            *******************************
            ADAM ASMACA OYUNUNA HOŞGELDİNİZ
            *******************************
            """)
    print("""
            1- Oyuna Başla
            2- Oyuncu Puan Listesi
            3- Oyun Kuralları
    
            0- Çıkış
            """)

    secenekler_secim = int(input("Seçiminiz: "))

    if secenekler_secim == 0:
        print("Çıkılıyor...")
        break

    elif secenekler_secim == 1:
        AdamAsmaca.adamasmaca(kelime)
        cevap = input("Anamenüye dönmek ister misiniz? (E/H): ").upper()
        if cevap == "E":
            continue
        elif cevap == "H":
            print("Çıkılıyor...")
            break
        else:
            print("Hatalı seçim!")

    elif secenekler_secim == 2:
        AdamAsmaca.puantablosu(kelime)
        cevap = input("Anamenüye dönmek ister misiniz? (E/H): ").upper()
        if cevap == "E":
            continue
        elif cevap == "H":
            print("Çıkılıyor...")
            break
        else:
            print("Hatalı seçim!")

    elif secenekler_secim == 3:
        print("""
            1- Adam asılana kadar harf tahmin etme hakkınız vardır.
            2- Kolay (4-5 harfli), orta (6-7 harfli) ve zor (8-9 harfli) olmak üzere üç adet kategoride kelimeler verilmektedir.
            3- Her bilinen kelime için oyuncuya kelimede bulunan harf sayısı kadar puan eklenir ve oyun bittiğinde (kaybettiğinde) toplam puanı hesaplanır.
            4- Verilen kelimede bir harften birden fazla olsa bile oyun size sadece birini gösterir. (Örn: Kelimede üç adet "E" harfi varsa üç kere tahmin etmelisin.) 
            """)
        cevap = input("Anamenüye dönmek ister misiniz? (E/H): ").upper()
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
