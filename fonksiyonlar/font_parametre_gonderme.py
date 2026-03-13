def selamla(isim):
    return "Merhaba, " + isim 

print(selamla("Ahmet"))   # fonksiyonun sonucunu ekrana yazdırdık


def toplam(say1, say2):
    return say1 + say2

print(toplam(5, 10))   
print(toplam(3, 7))   

def yasHesapla(dogumYili):
    return 2024 - dogumYili

print(yasHesapla(1983))   


def emekliligeKacYilKaldi(dogumYili):
    yas = yasHesapla(dogumYili)
    emeklilikYasi = 65
    kalanYil = emeklilikYasi - yas
    return kalanYil

print(emekliligeKacYilKaldi(2004))

def emeklilik(dgYili, isim):
    yas = yasHesapla(dgYili)

    kalanSure = 65 - yas

    if kalanSure > 0:
        return f"{isim}, emekliliğine {kalanSure} yıl kaldı."
    else:
        return f"{isim}, zaten {abs(kalanSure)} emekli olmuşsunuz."
    
print(emeklilik(1983, "Ahmet"))
print(emeklilik(1950, "Ayşe"))
print(emeklilik(2000, "Mehmet"))
    