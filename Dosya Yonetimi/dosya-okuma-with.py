# file = open("log.txt")
# print(file.read())

# file.close() 

try:
      with open("log.txt", "r") as f: # with blogu kullanarak dosya acilir 
          for i in f: # dosya satir satir okunur
               print(i) # her satir ekrana yazdirilir
except FileNotFoundError as e: # dosya bulunamazsa hata yakalanir               
    print("Dosya bulunamadi:", e)