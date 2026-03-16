# """
#     Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.

#     Kullanimi         : open(dosya_adi, dosya_erisme_modu)
#     dosya_erisme_modu : dosyayi hangi amacla actigimizi belirtir
#     "r" okuma modu    : okuma modu . belirtilen konumda dosya olmalidir
#     seek              : cursor konumu 
# """ 



f = open("log.txt", "r") # dosya okuma modu ile acilir

print(f.read()) # dosya okunur ve ekrana yazdirilir 