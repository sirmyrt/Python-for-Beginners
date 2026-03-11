"""
Uygulama 1 : Yari capi verilen bir dairenin alan ve cevresini hesapla
Alan = pi * r * r
Cevre = 2 * pi * r

Uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesapla
mil = km * 0.621371

"""

# ----Uygulama 1 ----------------
#pi = 3.14
#r = float(input("Yari capi giriniz: "))
#alan = pi * r * r 
#cevre = 2 * pi * r
#print( "Alan : " + str(alan))
#print( "Cevre : " + str(cevre)) 

# ----Uygulama 2 --------------

# km = float(input("Km bilgisini giriniz: "))
# mil = km * 0.621371
# print ("Mil cinsinden degeri: " + str(mil))

# veya ------

mesafeKm = input("km : ")
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2)

print (mesafeKm + "km: " + str(mesafeMil) + " mil ")

