# 1- Girilen 2 sayidan hangisi büyüktür?

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

if sayi1 > sayi2:
    print(f"{sayi1} sayısı {sayi2} sayısından büyüktür.")
elif sayi1 < sayi2:
    print(f"{sayi2} sayısı {sayi1} sayısından büyüktür.") 
elif sayi1 == sayi2:
    print(f"{sayi1} sayısı {sayi2} sayısına eşittir.")

#  ----   yada ---->  sonuc (sayi1 > sayi2) ifadesi True ise sayi1'i, False ise sayi2'yi döndürür. 
#                     print(f"{sayi1} {sayi2} den buyuk {sonuc}")


# 2- Girilen bir sayinin tek mi çift mi olduğunu bulunuz.

gSayi = int(input("Bir sayı giriniz: "))
gSayi = gSayi % 2 
print(gSayi) # 0 ise çift, 1 ise tek sayı olduğunu gösterir.


# 3- Bir ogrencinin girilen 3 notuna gore basari durumunu kontrol ediniz. (ortalama 50 ve ustu ise geçti değilse kaldı)     

# not1 = int(input("Birinci notu giriniz: "))
# not2 = int(input("İkinci notu giriniz: "))
# not3 = int(input("Üçüncü notu giriniz: "))

# ortalama = (not1 + not2 + not3) / 3
# print(f"Ortalamasi: {ortalama},Durumu {ortalama >=50}") # 50 ve üstü ise True, değilse False döndürür.

# --- yada --

not1 = int(input("Birinci notu giriniz: "))
not2 = int(input("İkinci notu giriniz: "))
not3 = int(input("Üçüncü notu giriniz: "))

ortalama = (not1 + not2 + not3) / 3
if ortalama >= 50:
    print(f"Ortalaması: {ortalama}, Durumu: Geçti")
else:    print(f"Ortalaması: {ortalama}, Durumu: Kaldı")
