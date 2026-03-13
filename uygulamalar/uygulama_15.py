#  Klavyeden girilen n sayidaki ogrenci bilgisini liste icerisinde saklayiniz
#   ** dictionary listesi yapisi (ogrenciNo, ogrenciAdi, ogrenciSoyad) seklinde olsun
#   ** urun ekleme islemi bittiginde ogrencileri listeleyiniz

devammi = "e"
ogrenciler = []


while (devammi != "h"):
    ogrenciNo = input("Ogrenci No: ")
    ogrenciAdi = input("Ogrenci Adi: ")
    ogrenciSoyad = input("Ogrenci Soyadi: ")
    
    ogrenciler.append({
        "ogrenciNo": ogrenciNo,
        "ogrenciAdi": ogrenciAdi,
        "ogrenciSoyad": ogrenciSoyad
    })
    
    devammi = input("devam mi? (e/h):  ")


for ogrenci in ogrenciler:
    print(f"Ogrenci No: {ogrenci['ogrenciNo']}, Ogrenci Adi: {ogrenci['ogrenciAdi']}, Ogrenci Soyadi: {ogrenci['ogrenciSoyad']}")

