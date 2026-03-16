liste = ["1", "3", "5", "20b", "abc", "10a", "60"]

# 1: Liste elemanlari icindeki sayisal degerleri bulunuz.

# for x in liste:
#   try:
#     sonuc = int(x)
#     print(sonuc)
#   except ValueError:
#     continue 


# 2: Kullanici quit (q) degerini girmedikce aldiginiz ger inputun sayi olduguna emin olunuz aksi halde hata mesaji veriniz.

# while True:
#   sayi = input("sayi:  ")
#   if (sayi == "q"):
#     print("program sonlandirildi")
#     break
  
#   try:
#    sonuc = float(sayi)
#    print(f"girilen sayi: {sonuc}")
#    break 
#   except ValueError:
#     print("gecersiz sayi")
#     continue 

# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict,key) fonksiyonu hazorlayiniz

urun = {"urun_adi": "samsung s20"}

def get(liste, key):
  try:
     return liste[key]
  except KeyError:
    return None
  
sonuc = get(urun, "urun_adi")
print(sonuc)