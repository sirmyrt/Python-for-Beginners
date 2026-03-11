kurum = "Istanbul Sanayi Odasi".split() #str to list

print(type(kurum))
print(kurum)
print(kurum[0])
print(kurum[1])

sayilar = [1, 2, 3, 4, 5] #list
isimler = ["Ali", "Veli", "Ayse"] #list

print(type(sayilar))
print(type(sayilar[0]))

print(type(isimler))
print(type(isimler[0])) 

ogrenci = ["Selim","Yilmaz",60,50,80]

print(ogrenci[0] + " " + ogrenci[1] ) 

ortalama = (ogrenci[2] + ogrenci[3] + ogrenci[4]) / 3
print(ortalama)

ogrenciler = [["Selim","Yilmaz",60,50,80], ["Ali","Yilmaz",90,70,80]]

print(ogrenciler[0][2]) #Soldaki sayi hangi ogrenci oldugunu sagdaki sayi ise o ogrencinin hangi notunu gosterdigini gosterir

print(ogrenciler[1])
