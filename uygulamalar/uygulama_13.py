urunler = [
    {"ad": "Laptop", "fiyat": 22000},
    {"ad": "Telefon", "fiyat": 15000},
    {"ad": "Tablet", "fiyat": 3000},
    {"ad": "Kulaklık", "fiyat": 800},
    {"ad": "Monitör", "fiyat": 4000}
]

# 1- Asagidaki ornek cumleyi yazdiriniz 
# "Laptop ürününün fiyatı 22000 TL'dir."

for urun in urunler:
    print(f"{urun['ad']} ürününün fiyatı {urun['fiyat']} TL'dir.")


# 2- Urunlerin fiyatlarinin toplamini yazdiriniz

toplam_fiyat = 0
for urun in urunler:
    toplam_fiyat += urun['fiyat']
print(f"Urunlerin toplam fiyatı: {toplam_fiyat} TL'dir.")

# 3- 3000 ile 20000 arasindaki urunleri listeleyiniz

for urun in urunler:
    if 3000 <= urun['fiyat'] <= 20000:
        print(f"{urun['ad']} - {urun['fiyat']} TL")

# 4- Kullanicidan alinan anahtar kelimeye gore urunleri filtreleyiniz. (Ornegin: "Lap" --> Laptop)

aranan_kelime = input("Aramak istediğiniz ürünün anahtar kelimesini giriniz: ")
for urun in urunler:
    if aranan_kelime.lower() in urun['ad'].lower():
        print(f"{urun['ad']} - {urun['fiyat']} TL")
