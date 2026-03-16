# Not Uygulamasi

# 1- Menu 
   # 1- Not Gir
   # 2- Ortalamalari  Goster (90-100 -> AA, 85-89 -> BA)
   # 3- Notlari Kayit Et
   # 4- Cikis


def not_hesapla(satir):
    satir = satir[:-1]  # \n karakterini sil
    liste = satir.split(":")  # Ad Soyad : Not1 , Not2 , Not3

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")  # Not1 , Not2 , Not3

    not1 = int(notlar[0])
    not2 = int(notlar[1])   
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harfNotu = "AA"
    elif ortalama >= 80 and ortalama < 90:
        harfNotu = "BA"
    elif ortalama >= 70 and ortalama < 80:
        harfNotu = "BB" 
    elif ortalama >= 60 and ortalama < 70:
        harfNotu = "CB"
    elif ortalama >= 50 and ortalama < 60:
        harfNotu = "CC"
    elif ortalama >= 40 and ortalama < 50:
        harfNotu = "DC"
    elif ortalama >= 30 and ortalama < 40:
        harfNotu = "DD"
    elif ortalama >= 20 and ortalama < 30:
        harfNotu = "FD"
    elif ortalama >= 0 and ortalama < 20:
        harfNotu = "FF"

    return f"{ogrenciAdi} : {harfNotu} ({ortalama})"




def not_gir():
    ad = input("Ogrenci Adi: ")
    soyad = input("Ogrenci Soyadi: ")
    not1 = input("Not 1: ")
    not2 = input("Not 2: ")
    not3 = input("Not 3: ")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as f:
        f.write(ad + ' ' + soyad + ' : ' + not1 + ' , ' + not2 + ' , ' + not3 + '\n')


def notlari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as f:
        for satir in f:
            print(not_hesapla(satir))

def notlari_kayit_et():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as f:
        liste = []
        for satir in f:
            liste.append(not_hesapla(satir))
        
        with open ("sonuclar.txt", "w", encoding="utf-8") as f2:
            for i in liste:
                f2.write(i + "\n")

    with open("sonuclar.txt", "w", encoding="utf-8") as f:
        for i in liste:
            f.write(i + "\n")


while True:
    islem = input("1- Not Gir\n2- Ortalamalari Goster\n3- Notlari Kayit Et\n4- Cikis\n")
                  
    if islem == "1":   
        not_gir()
    elif islem == "2":
        notlari_oku()     
    elif islem == "3":
        notlari_kayit_et()
    elif islem == "4":
        print("Cikis yapiliyor...")
        break
          