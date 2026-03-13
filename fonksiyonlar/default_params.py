# def selamlama(isim,mesaj):
#     return f"{mesaj} {isim}"

# sonuc = selamlama("Ahmet","Merhaba")

# print (sonuc)

def selamlama (isim = "Ahmet", mesaj = "Merhaba"):
    return f"{mesaj} {isim}"

print(selamlama())


def usAlma(taban,us):
    return taban ** us

sonuc = usAlma(2,3)
print(sonuc)

def toplam(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def islem(a,b,fn = toplam):
    return fn(a,b)

sonuc = islem(10,20,cikarma)
sonuc = islem(10,20)
sonuc = islem(10,20,toplam)


print(sonuc)