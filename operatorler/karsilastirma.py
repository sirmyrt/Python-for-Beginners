# Karsilastirma operatorleri kullanim amaci 
# bir degerin digerine esit olup olmadigini kontrol
# etmek ve sonucunu boolean (True/False) olarak dondurmektir.

# Operatörler:
# == : Esittir operatoru, iki degerin birbirine esit olup olmadigini kontrol eder.
# != : Esit degildir operatoru, iki degerin birbirine esit olmadigini kontrol eder.
# >  : Buyuktur operatoru, sol tarafin sag tarafindan buyuk olup olmadigini kontrol eder.
# <  : Kucuktur operatoru, sol tarafin sag tarafindan kucuk olup olmadigini kontrol eder.
# >= : Buyuk esittir operatoru, sol tarafin sag tarafindan buyuk veya esit olup olmadigini kontrol eder.
# <= : Kucuk esittir operatoru, sol tarafin sag tarafindan kucuk veya esit olup olmadigini kontrol eder.    

a,b,c,d= 2,2,10,5


eposta = "user@example.com"
parola = "password123"

e_sonuc= (eposta == input('eposta:') and parola == input('parola:'))  # Kullanıcıdan eposta ve parola girmesini istiyoruz ve girilen degerlerin dogru olup olmadigini kontrol ediyoruz
if e_sonuc:
    print("Giris basarili!")
else:
    print("Giris basarisiz!")

# print("Eposta ve parola dogru mu?", e_sonuc)

sonuc1 = (a == b)  # True, cunku a ve b birbirine esittir
sonuc2 = (a != c)  # True, cunku a ve c birbirine esit degildir
sonuc3 = (a != b)  # False, cunku a ve b birbirine esittir

print(f'sonuc1: {sonuc1}, sonuc2: {sonuc2}, sonuc3: {sonuc3}')