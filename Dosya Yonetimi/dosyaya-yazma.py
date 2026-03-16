# "w" : write (yazma) modu, dosya yoksa oluşturur, varsa içeriğini siler ve yeni içeriği yazar
#  ** Dosyayi konumda olusturur
#  ** Eger konumda ayni isimde bir dosya varsa, o dosyanin icerigini siler ve yeni icerigi yazar

with open("dosya.txt", "w") as file: # dosya yazma modu ile acilir
    file.write("Merhaba, bu bir deneme dosyasidir.\n") # dosyaya yazi yazilir
    file.write("Bu dosya Python ile yazilmistir.\n") # dosyaya yazi yazilir 
    file.write("Dosya islemleri cok kolaydir.\n") # dosyaya yazi yazilir        
# file.close() # dosya kapatilir (with blogu kullanildigi icin gerekli degil)

with open("dosya.txt", "r") as file: # dosya okuma modu ile acilir
    for i in file: # dosya satir satir okunur
        print(i) # her satir ekrana yazdirilir