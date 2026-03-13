# Bankamatik Uygulamasi

# Hesap bilgileri tutulacak. (dict)
# menu , paraCekme, bakiyeSorgula, paraYatirma fonksiyonlari tanimlanacak.
# cekilmek istenen tutar hesapta yoksa ek hesabin kullanilmak istengigi sorgulanacak.


hesaplar = [
    {
        "ad":"Mert Onur",
        "hesapNo":"123456789",
        "bakiye":1000,
        "ekHesap":500,
        "username":"mertonur",
        "password":"1234",
    },
    {
        "ad":"Ayse Yilmaz",
        "hesapNo":"987654321",
        "bakiye":2000,
        "ekHesap":1000,
        "username":"ayseyilmaz",
        "password":"5678",
    },
    {
        "ad":"Ahmet Demir",
        "hesapNo":"456789123",
        "bakiye":1500,
        "ekHesap":700,
        "username":"ahmetdemir",
        "password":"9012",
    }
]

def menu(hesap):
    print("\n")

    print("1. Bakiye Sorgula")
    print("2. Para Cekme")
    print("3. Para Yatirma")
   

    islem = input("Yapmak istediginiz islemi seciniz: ")

    if islem == "1":
        bakiyeSorgula(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    else:
        print("Gecersiz islem. Tekrar deneyiniz.")
        
    menu(hesap)

def bakiyeSorgula(hesap):
    print(f"Hesabinizda {hesap['bakiye']} TL bulunmaktadir.")
    print(f"Ek hesabinizda {hesap['ekHesap']} TL bulunmaktadir.")

def paraCekme(hesap):
    miktar = float(input("Cekmek istediginiz tutari giriniz: "))

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print(f"{miktar} TL basariyla cekildi. Kalan bakiye: {hesap['bakiye']} TL")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ekKullanimi = input("Bakiye yetersiz. Ek hesabi kullanmak istiyor musunuz? (E/H): ")
            if ekKullanimi.lower() == "e":
                ekKullanilacak = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekKullanilacak
                print(f"{miktar} TL basariyla cekildi. Kalan bakiye: {hesap['bakiye']} TL, Kalan ek hesap: {hesap['ekHesap']} TL")
            else:
                print("Islem iptal edildi.")
                


def paraYatirma(hesap):
    pass


def login():
    username = input("Kullanici adinizi giriniz: ")
    password = input("Sifrenizi giriniz: ")

    isLoggedIn = False

    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn = True
            menu(hesap)
            break

    if not (isLoggedIn):
        print("Kullanici adi veya sifre hatali. Tekrar deneyiniz.")


login()            
