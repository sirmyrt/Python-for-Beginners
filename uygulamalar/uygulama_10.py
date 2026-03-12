# 1- Yasi 18'den buyuk yada veli izni varsa bir iste calisabilir durmunu kontrol ediniz

yas = int(input("Yasinizi giriniz: "))
veli_izni = input("Veli izniniz var mi? (Evet/Hayir): ").lower()
calisabilir = (yas > 18) or (veli_izni == "evet")

print("Calisabilir misiniz?", calisabilir)


# 2- Ders notu 50-100 arasindaysa gecti degilse kaldi durmunu kontrol ediniz

notu = int(input("Ders notunuzu giriniz: "))
gecti = (notu >= 50) and (notu <= 100)
print("Dersi gectiniz mi?", gecti)

# 3- Not ortalamasi en az 70 puan ve zayifi yoksa tesekkur belgesi alabilme durumunu kontrol ediniz

ortalama = float(input("Not ortalamanizi giriniz: "))
zayif_var = input("Zayif notunuz var mi? (Evet/Hayir): ").lower()
tesekkur_belgesi = (ortalama >= 70) and (zayif_var == "hayir")
print("Tesekkur belgesi alabilir misiniz?", tesekkur_belgesi)

# 4- Ise girmek icin en az onlisan yada lisans mezunu olma durmunu  kontrol ediniz. Sigara kullanmama kosulu

mezuniyet = input("Mezuniyet durumunuz nedir? (Onlisans/Lisans): ").lower()
sigara_kullanimi = input("Sigara kullaniyor musunuz? (Evet/Hayir): ").lower()
ise_girebilir = ((mezuniyet == "onlisans") or (mezuniyet == "lisans")) and (sigara_kullanimi == "hayir")
print("Ise girebilir misiniz?", ise_girebilir)

# 5- Uygulama girisi kontrolu "username yada email" ve "parola"icin yapalim 

username = input("Kullanici adinizi giriniz: ")
email = input("Email adresinizi giriniz: ")
parola = input("Parolanizi giriniz: ")
giris_kontrolu = ((username == "admin") or (email == "ornek@email.com")) and (parola == "123456")
print("Uygulamaya giris yapabilir misiniz?", giris_kontrolu)