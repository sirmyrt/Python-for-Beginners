customers = ["ayberkpancar","mertonur","demiryilmaz","selimpolat"]
order_totals = [13000 , 18000 , 7000 , 15000]

# 1- 'ayberkpancar' adiyla yapilan 7000 liralik  siparisi listeye ekleyiniz.

customers.append("ayberkpancar")
order_totals.append(7000)

# 2- Son eklenen siparisi siliniz.

customers.pop()
order_totals.pop()  

# 3- Tum musteriler icin asagidaki ozet cumleyi yazdiriniz: 
# '<username> 'isimli musterinin siparis toplami <10000> TL'dir. 

sonuc = f"{customers[0]} isimli musterinin siparis toplami {order_totals[0] + order_totals[4]} TL'dir."
sonuc = f"{customers[1]} isimli musterinin siparis toplami {order_totals[1]} TL'dir."
           # -- yada --
            #for i in range(len(customers)):
                # print(f"{customers[i]} isimli musterinin siparis toplami {order_totals[i]} TL'dir.")

# 4- Musterileri alfabetik siraya gore yazdiriniz.

customers.sort()

# 5- Siparis toplamlarini azalan siraya gore yazdiriniz.

order_totals.sort(reverse=True) # yada order_totals.sort() ve order_totals.reverse() kullanilabilir

# 6- En dusuk siparis hangisidir?

order_totals.sort()                                  # yada  sonuc = min(order_totals) kullanilabilir / sonuc = max(order_totals) kullanilabilir
en_dusuk_siparis = order_totals[0]
print(f"En dusuk siparis: {en_dusuk_siparis} TL") 

# 7- 'mertonur' adli kullanicinin kac siparisi oldugunu yazdiriniz.

mertonur_index = customers.index("mertonur")                                    # yada  sonuc = customers.count("mertonur") kullanilabilir
mertonur_siparisi = order_totals[mertonur_index]
print(f"mertonur adli kullanicinin siparis toplami: {mertonur_siparisi} TL")

# 8- customers listesinde demiryilmaz isimli kullaniciyi siliniz

customers.remove("demiryilmaz")

# 9- Listelerdeki tum icerikleri siliniz
 
customers.clear()
order_totals.clear()

# 10- Kullanicidan aldiginiz kullanici adi ve siparis toplami bilgilerini listelere ekleyiniz.

kullanici_adi = input("Kullanici adi: ")
siparis_toplami = float(input("Siparis toplami: ")) 
customers.append(kullanici_adi)
order_totals.append(siparis_toplami)        
print(f"{kullanici_adi} isimli kullanicinin siparis toplami {siparis_toplami} TL'dir.")

# -- yada -- 
# username = input("Kullanici adi: ")
# toplam = input("Siparis toplami: ")
# customers.append(username)
# order_totals.append(toplam)

print(customers)
print(order_totals) 
