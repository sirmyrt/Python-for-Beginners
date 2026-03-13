# Bir aracin yakit tipine gore (benzin,dizel,lpg) belirtilen bir mesafeyi kac litre yakit masrafi oldugunu hesaplayan programi yaziniz.
#benzin  : 39.35
#dizel   : 41.71
#lpg     : 20.28

benzinFiyat = 39.35
dizelFiyat = 41.71
lpgFiyat = 20.28

yakitTipi = input("Yakit tipini giriniz (benzin,dizel,lpg): ")
yakitTipi2 = input("Ikinci yakit tipini giriniz (benzin,dizel,lpg): ")

mesafe = float(input("Gidilecek mesafeyi km cinsinden giriniz: "))  

# Ilk yakit tipi icin hesaplama
if yakitTipi == "benzin":
    yakitMiktari = mesafe / 100 * 7.5  
    toplamMaliyet = yakitMiktari * benzinFiyat
elif yakitTipi == "dizel":
    yakitMiktari = mesafe / 100 * 6.0  
    toplamMaliyet = yakitMiktari * dizelFiyat
elif yakitTipi == "lpg":
    yakitMiktari = mesafe / 100 * 8.0  
    toplamMaliyet = yakitMiktari * lpgFiyat 
else:
    print("Gecersiz yakit tipi girdiniz.")
    toplamMaliyet = None

# Ikinci yakit tipi icin hesaplama
if yakitTipi2 == "benzin":
    yakitMiktari2 = mesafe / 100 * 7.5  
    toplamMaliyet2 = yakitMiktari2 * benzinFiyat
elif yakitTipi2 == "dizel":
    yakitMiktari2 = mesafe / 100 * 6.0  
    toplamMaliyet2 = yakitMiktari2 * dizelFiyat
elif yakitTipi2 == "lpg":
    yakitMiktari2 = mesafe / 100 * 8.0  
    toplamMaliyet2 = yakitMiktari2 * lpgFiyat 
else:
    print("Gecersiz yakit tipi girdiniz.")
    toplamMaliyet2 = None

# Fiyat farki hesaplama
if toplamMaliyet is not None and toplamMaliyet2 is not None:
    fiyatFarki = abs(toplamMaliyet - toplamMaliyet2)
    pahaliBirOlan = yakitTipi if toplamMaliyet > toplamMaliyet2 else yakitTipi2
    
    print(f"\n=== YAKIT TIPI KARSILASTIRMASI ===")
    print(f"{yakitTipi.upper()}: {toplamMaliyet:.2f} TL")
    print(f"{yakitTipi2.upper()}: {toplamMaliyet2:.2f} TL")
    print(f"Fiyat Farki: {fiyatFarki:.2f} TL")
    print(f"Daha pahali olan: {pahaliBirOlan.upper()}")    




# Bir ogrencinin 2 yazili bir sozlu notunu alarak ortalama hesaplayiniz ve hesaplanan ortalamaya gore not araligina karsilik gelen degerlendirmeyi yaziniz

# 0-24     : 0
# 25-44    : 1
# 45-54    : 2
# 55-69    : 3
# 70-84    : 4
# 85-100   : 5

not1 = float(input("1. yazili notunu giriniz: "))
not2 = float(input("2. yazili notunu giriniz: "))
sozluNot = float(input("Sozlu notunu giriniz: "))
ortalama = (not1 + not2 + sozluNot) / 3 

if 0 <= ortalama < 25:
    degerlendirme = 0
elif 25 <= ortalama < 45:
    degerlendirme = 1   
elif 45 <= ortalama < 55:
    degerlendirme = 2
elif 55 <= ortalama < 70:   
    degerlendirme = 3
elif 70 <= ortalama < 85:
    degerlendirme = 4
elif 85 <= ortalama <= 100:
    degerlendirme = 5
else:
    degerlendirme = "Gecersiz ortalama"

print(f"Ogrencinin ortalamasi: {ortalama:.2f}, degerlendirme: {degerlendirme}")

