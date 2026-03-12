a, b, c = 4, 8, (12, 2)

# 1- Kullannicidan aldiginiz 2 sayinin carpimi ile a,b,c toplaminin farki nedir?

sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))
carpim = sayi1 * sayi2
toplam = a + b + (c[0] + c[1])  # c'nin elemanlarini topluyoruz
sonuc = carpim - toplam 

print("Sonuc:", sonuc)



# 2- c'nin b'ye kalansiz bolumunu hesaplayiiz

bolum = (c[0] + c[1]) // b  # c'nin elemanlarini topluyoruz ve b'ye kalansiz boluyoruz
print("Bolum:", bolum)

# 3- (a,b,c) toplaminin mod 7 si nedir?

toplam = a + b + (c[0] + c[1])    # yada  sonuc = (a + b + (c[0] + c[1])) % 7 
sonuc2 = toplam % 7
print("Sonuc2:", sonuc2) 

# 4- b'nin a. kuvvetini hesapla

kuvvet = b ** a
print("Kuvvet:", kuvvet) 

# 5- a, *b, c = (2,4,6,8,13) islemine gore c'nin kupu nedir?

a, *b, c = (2, 4, 6, 8, 13)  # a=2, b=[4,6,8], c=13
kup = c ** 3
print("C'nin kupu:", kup)


# 6- a, b, *c = (2,4,6,8,13) islemine gore c'nin degerleri toplami nedir?

a , b, *c = (2, 4, 6, 8, 13)  # a=2, b=4, c=[6,8,13]

print(c[0] + c[1] + c[2])  # c'nin elemanlarini topluyoruz

