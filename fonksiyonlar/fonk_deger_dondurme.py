def toplam():
    return 10+20

sonuc = toplam()   # fonksiyonun sonucunu sonuc değişkenine atadık
print(sonuc)       # fonksiyonun sonucunu ekrana yazdırdık

def yil():
    import datetime
    return datetime.datetime.now().year

def saat():
    import datetime
    return datetime.datetime.now().hour

def dakika():
    import datetime
    return datetime.datetime.now().minute   

def yasHesapla():
    return yil() - 1983                       #return 2024 - 1980

print(yasHesapla())   # fonksiyonun sonucunu ekrana yazdırdık

def selamlama():
    if(saat() < 12):
        return "Günaydın"
    else:
        return "Merhaba"
    
print(selamlama())    