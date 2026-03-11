title = "Python ile Programlama Dersleri"

# 1- 'title'degiskeni icerisindeki karakter sayisi nedir

adet = len(title) 
print(adet)


# 2- 'title'icerisindeki 'Python'kelimesini alin

print(title[0:6])

# 3- 'title'degiskeninin ilk 5 ve son 5 karakterini alin

print(title[0:5])
print(title[-5:])

# 4- 'title' degiskenini tersten yazdirin

print(title[::-1])  


# 5- Klavyeden girilen ogrenci bilgisine gore ornek verilen cumleyi yazdiriniz.
#   Ornek : Mert Onur isimli ogrencinin 1. notu 60, 2.notu 60 ve not ortalamasi 60 olarak hesaplanmistir.

ad = input("Ogrencinin adini giriniz: ")
soyad = input("Ogrencinin soyadini giriniz: ")

not1= input("1.Not; ")
not2= input("2.Not; ")
ortalama = (int(not1) + int(not2)) / 2

sonuc = f"{ad} {soyad} isimli ogrencinin 1. notu {not1}, 2.notu {not2} ve not ortalamasi {ortalama} olarak hesaplanmistir."
print(sonuc) 