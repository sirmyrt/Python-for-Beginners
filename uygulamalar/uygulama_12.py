sayilar = [1, 5, 17, 45, 98]

# 1-  "sayilar" listesinde bulunan her bir sayıyı ekrana yazdırır.

# for sayi in sayilar:
#     print(sayi)

# 2-  "sayilar" listesinde hangi sayilar 3un katidir

# for sayi in sayilar:
#     if sayi % 3 == 0:
#         print(sayi)

# 3- "sayilar" listesinde tum sayilarin toplami

toplam = 0
for sayi in sayilar:
    toplam += sayi  
print(toplam) # sayilar listesindeki tüm sayıların toplamını ekrana yazdırır.

# ---------------------------------------------------------------------- # 

urunler = ["samsung s240", "samsung s22", "iphone 15", "iphone 16s"]

# 4-  "urunler" listesindeki tum iphone marka urunleri listeleyiniz

# for urun in urunler:
#     if "iphone" in urun:
#         print(urun) # urunler listesindeki her bir ürünü kontrol eder ve içinde "iphone" geçen ürünleri ekrana yazdırır.

# 5- "urunler" listesinde kac adet samsung urun vardir

adet = 0
for urun in urunler:
   index = urun.find("samsung")
   if index != -1:
       adet += 1
print(adet) # urunler listesindeki her bir ürünü kontrol eder ve içinde "samsung" geçen ürünlerin sayısını ekrana yazdırır.