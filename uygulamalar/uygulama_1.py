""""
 Asagidaki musterinin bilgilerini ve satin aldigi urun bilgilerini degiskenler icerisinde saklayiniz.
 Toplam odenen ucret nedir? 
 Odenen miktarin kdv orani nedir? (18% kdv orani kullaniniz

 Sadik Turan 
 0536 123 45 67
info@sadikturan.com 
 Kocaeli

 Satin Aldigi urunler
 Urun Adi : Kablosuz Mouse
 Fiyati : 550 TL

 Satin Aldigi urunler
 Urun Adi :  Kablosuz Klavye
 Fiyati : 650 TL

 Satin Aldigi urunler
 Urun Adi : Dizustu Bilgisayar
 Fiyati : 56.000 TL

"""
ad = "Sadik"
soyad = "Turan"
telNo = "0536 123 45 67"
email = "info@sadikturan.com"
sehir = "Kocaeli"

urun1 = "Kablosuz Mouse"
fiyat1 = 550

urun2 = "Kablosuz Klavye"
fiyat2 = 650    

urun3 = "Dizustu Bilgisayar"
fiyat3 = 56000

print(f"=== Musteri Bilgileri ===\nAdi: {ad}\nSoyadi: {soyad}\nTelefon: {telNo}\nEmail: {email}\nSehir: {sehir}")
toplamOdenen = fiyat1 + fiyat2 + fiyat3
print ("Toplam Odenen Ucret: "+str(toplamOdenen))

print ( "Toplam Odenen Ucret Kdv Dahil: "+str(toplamOdenen * 1.18))