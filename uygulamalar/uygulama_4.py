kursAdi = "Btk Akademi ile Programlama Dersleri"
website = "www.btkakademi.gov.tr"

# 1- 'Btk Akademi' karakter dizisinin bas ve sondaki bosluk karaktelerini silin

kursadi = kursAdi.strip()
print(kursadi)

# 2- kursAdi degiskeninin tum karakterleri kucuk harfe cevir

kursadi = kursAdi.lower()
print(kursadi)

# 3- website degiskeninde kac tane '.' karakteri vardir

sonuc = website.count('.')
print(sonuc)

# 4- website degiskeni https ile mi baslamaktadir

sonuc = website.startswith('https')
print(sonuc)

# 5- websitesi tr ile mi bitiyor

sonuc = website.endswith('tr')
print(sonuc)

# 6- kursadi icerisindeki tum karakterler harflerden mi olusuyor

sonuc = kursAdi.isalpha()
print(sonuc)

# 7- kursAdi degiskenindeki tum bosluklari '-'ile degistir

sonuc = kursAdi.replace(' ', '-')
print(sonuc)

# 8- kursAdi degiskenindeki Python kelimesini ReactJs ile degistiriniz

sonuc = kursAdi.replace('Programlama', 'ReactJs')
print(sonuc)

# 9- website degiskeni 'wwww'iceriyormu 

sonuc = website.find('www') 
print(sonuc)

# 10- kursAdi degiskenini listeye ceviriniz

sonuc = kursAdi.split()
print(sonuc)