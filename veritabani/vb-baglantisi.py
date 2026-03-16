import sqlite3

connection = sqlite3.connect("deneme.db")

# vb komutlari

sql = "INSERT INTO users (name, age) VALUES ('Ahmet', 30)" # users tablosuna bir veri eklemek icin SQL komutu

cursor = connection.cursor() # cursor nesnesi ile veritabanina komut gonderilir
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)") # users adinda bir tablo olusturulur, eger tablo zaten varsa olusturulmaz
cursor.execute(sql) # SQL komutunu calistir
result = cursor.fetchall() # execute() fonksiyonu ile gonderilen komutun sonucunu alir  

for customer in result:
    print(customer)


connection.close() # veritabanina baglanti kapatilir

print("Veritabanına bağlanıldı.")