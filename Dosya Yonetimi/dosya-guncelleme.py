# with open("markalar.txt", "a") as file : # dosya ekleme modu ile acilir
#     file.write("6-BMW") # dosyaya yeni bir marka eklenir

# with open("markalar.txt", "r+") as file : # dosya okuma ve yazma modu ile acilir
#      markalar = file.read() # dosya okunur ve markalar degiskenine atanir
#      markalar = "1-Toyota\n" + markalar # markalar degiskeninin basina yeni bir marka eklenir
#      file.seek(0) # cursor konumu dosyanin basina getirilir
#      file.write(markalar) #  markalar degiskeni dosyaya yazilir

with open("markalar.txt", "r+") as file : # dosya okuma ve yazma modu ile acilir
     markalar = file.readlines()  # dosya okunur ve markalar degiskenine atanir. readlines() fonksiyonu dosyayi satir satir okur ve her satiri bir liste elemani olarak markalar degiskenine atar
     markalar.insert(2, "3-Honda\n") # markalar listesine 2. indexe yeni bir marka eklenir
     file.seek(0) # cursor konumu dosyanin basina getirilir
    #  for marka in markalar : # markalar listesi dongu ile donulur
    #      file.write(marka) # her bir marka dosyaya yazilir
    # bu ikisi yerine 
     file.writelines(markalar) # markalar listesi dosyaya yazilir. writelines() fonksiyonu bir liste alir ve her bir elemani dosyaya yazar
     

with open("markalar.txt", "r") as file : # dosya okuma modu ile acilir
    print(file.read()) # dosya okunur ve ekrana yazdirilir