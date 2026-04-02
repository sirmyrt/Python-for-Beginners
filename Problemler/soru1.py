# İki tamsayıyı kabul eden bir Python fonksiyonu yazın. 
# İki sayının çarpımı 1000'den küçük veya eşitse, çarpımlarını döndürün; aksi takdirde, toplamlarını döndürün.

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

carpim = sayi1 * sayi2
toplam = sayi1 + sayi2

if carpim <= 1000:
    print("Çarpım:", carpim)    
else:  
    print("Toplam:", toplam)
    
