mesaj = "Merhabalar adim Mert , 22 yasindayim"

#sonuc = mesaj.title()
# sonuc= mesaj.capitalize()
#sonuc  = "merhabalar dostlar" .islower()
#sonuc = mesaj.strip()  #bas ve sondaki bosluklari siler
#sonuc = mesaj.split()  #mesajdaki kelimeleri ayirir ve listeye atar
#sonuc = mesaj.split(',') #virgule gore ayirir ve listeye atar
#sonuc = mesaj.index('adim') #index fonksiyonu verilen degerin mesaj icerisindeki indexini verir
#sonuc = mesaj.startswith("M") #mesaj M harfi ile basliyor mu?
#sonuc = mesaj.replace("22", "23") #mesaj icerisindeki 22 degerini 23 yapar

sonuc = mesaj.replace("Mert", "Ahmet").replace("22", "23") #birden fazla replace yapilabilir
print(sonuc)