# Bir dizeden 0'dan n'ye kadar olan karakterleri silen ve yeni bir dize döndüren bir fonksiyon yazın.

def karakter_sil(dize, n):
    yeni_dize = ""
    for i in range(len(dize)):
        if i >= n:
            yeni_dize += dize[i]
    return yeni_dize    
# Örnek kullanım
dize = "Merhaba Dünya!"
n = 5
sonuc = karakter_sil(dize, n)   
print(sonuc)