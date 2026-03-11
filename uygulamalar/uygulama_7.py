# Asagidakki ogrenci bilgilerini dictionary listesinde saklayiniz
# 101 Ali Bilgi 2010 (40,80,90)
# 102 Veli Bilgi 2011 (50,60,70)
# 103 Ayse Yilmaz 2012 (60,70,80)

ogrenciler = {
    101: {
        'ad': 'Ali',        
        'soyad': 'Bilgi',
        'dogum_yili': 2010,
        'notlar': (40, 80, 90)
    },
    102: {
        'ad': 'Veli',       
        'soyad': 'Bilgi',
        'dogum_yili': 2011,
        'notlar': (50, 60, 70)
    },
    103: {
        'ad': 'Ayse',       
        'soyad': 'Yilmaz',
        'dogum_yili': 2012,
        'notlar': (60, 70, 80)
    }
}



#Klavyeden girilen ogrenci numarasina gore asagidaki cumleeyi yazdiriniz
# 101 numarali Ali Bilgi ismindeki ogrencinin yasi 14 ve not ortalamasi 70 


ogrenciNo = int(input('Ogrenci numarasini giriniz: '))  # Eger int yazilmazsa hata verir. Ogrenci numarasi 101, 102 veya 103 olmalidir. int olmazsa onu string olarak algilar ve hata verir.
ogrenci = ogrenciler[ogrenciNo]

print(f"{ogrenciNo} numarali {ogrenci['ad']} {ogrenci['soyad']} ismindeki ogrencinin yasi {2024 - ogrenci['dogum_yili']} ve not ortalamasi {sum(ogrenci['notlar']) / len(ogrenci['notlar'])}")