"""
    module1 (db)         : urunler
    module2 (methods)    : urun_ekle, urun_sil, urun_guncelle, urun_listele
    module3 (app)        : kullanıcı arayüzü, menü, kullanıcı girişi

                yeni urun ekleme => urun_ekle
                urun silme => urun_sil
                urun guncelleme => urun_guncelle
                urun listeleme => urun_listele
"""

from methods import*

sonuc = urunBilgileri_getir()

urun_ekle("Masa", 12000)

for i in urunBilgileri_getir():
    print(f"ID: {i['id']} - İsim: {i['isim']} - Fiyat: {i['fiyat']}")

guncelle(1,"Laptop Pro", 7000)

for i in urunBilgileri_getir():
    print(f"ID: {i['id']} - İsim: {i['isim']} - Fiyat: {i['fiyat']}")


# for i in sonuc:
#     print(f"ID: {i['id']} - İsim: {i['isim']} - Fiyat: {i['fiyat']}")

