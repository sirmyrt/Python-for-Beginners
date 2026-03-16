# 1- Faktoriyel fonksiyonu olusturun ve fonksiyona gelen deger icin hata mesajlari veriniz

# def faktoriyel(x):
#     x = int(x)

#     if x < 0:
#         raise ValueError("Negatif sayilarin faktoriyeli tanimlanmaz.")
    
#     sonuc = 1

#     for i in range(1, x + 1):
#        sonuc *= i

#     return sonuc

# for i in [3,6,7,'2a',-1,-7,9]:
#     try:
#         x = faktoriyel(i)
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         print(x)


# 2- Girilen parola icinde turkce karakter hatasi veriniz.

def parola_kontrol(parola):
    turkce_karakterler = "çÇğĞıİöÖşŞüÜ"

    for karakter in parola:
        if karakter in turkce_karakterler:
            raise ValueError("Parola turkce karakter icermemelidir.")
    
    print("Parola gecerli.")

parola = input("parola: ")

try:
    parola_kontrol(parola)
except ValueError as e:
    print(e)

