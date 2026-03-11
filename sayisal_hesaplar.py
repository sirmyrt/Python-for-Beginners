# Degisken tanimlama

urunAfiyat = 2000
urunBfiyat = 3000
 
kdvOrani = 0.22

print (urunAfiyat * kdvOrani + urunAfiyat)
print (urunBfiyat * kdvOrani + urunBfiyat)

urunToplami = urunAfiyat + urunBfiyat
print ("Urun Fiyatlari Toplami: " + str(urunToplami))

urunToplamiKdvli = urunToplami * (1 + kdvOrani)
print ("Urun Fiyatlari Toplami Kdv Dahil: " + str(urunToplamiKdvli))