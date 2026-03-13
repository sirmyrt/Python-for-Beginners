# 1- Kendisine gonderilen bir kelimeyi belirtilen kez ekranda gosteren bir fonksiyon yaziniz.

def yazdir(text, adet):
    return text * adet

print(yazdir("Merhaba ", 3))


# 2- Dikdortgenin alan ve cevresini hesaplayan bir fonksiyon yaziniz.

def dikdortgen_hesapla(kenar1, kenar2):
    alan = kenar1 * kenar2
    cevre = 2 * (kenar1 + kenar2)
    return alan, cevre

print(dikdortgen_hesapla(5, 3))

# 3- Yazi tura uygulamasini fonksiyon kullanarak yapiniz.

import random
def yazi_tura():
    return random.choice(["Yazi", "Tura"])
print(yazi_tura())


# 4- Kendisine gonderilen 2 sayi arasindaki tum asal sayilari bulan fonksiyonu yazin

def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1,sayi2+1):
        if(sayi > 1):
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalSayilariBul(10, 50)                


# 5- Kendisine gonderilen bir sayinin tam bolenlerini bir liste seklinde donduren fonksiyonu yaziniz.

def tamBolenleriBul(sayi):
   tamBolenler = []

   for i in range(2, sayi):
       if(sayi % i == 0):
           tamBolenler.append(i)
                              
       return tamBolenler
print(tamBolenleriBul(28))
                       

