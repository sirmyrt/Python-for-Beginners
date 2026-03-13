# for - - while döngüsünün aksine belirli bir sayıda tekrarlanması gereken durumlarda kullanılır.
# for --> list

sayilar = [1, 5, 17, 45, 98]
isimler = ["Mert", "Ahmet", "Ayşe", "Fatma"]
adSoyad = "Mert Onur"


# for x in sayilar:
#     print(x)

# for x in sayilar:
#     print("Merhaba Ben Mert") # 5 kez yazdırır.

# for x in sayilar:
#     print(x * 2) # listedeki her bir sayıyı 2 ile çarparak yazdırır.

# for isim in isimler:
#     print(isim) # listedeki her bir ismi yazdırır. 

# for i in adSoyad:
#     print(i) # adSoyad stringindeki her bir karakteri yazdırır.

my_tuple = [(1, 2), (3, 4), (5, 6)]

# for a,b in my_tuple:
#     print(a,b) # listede bulunan her bir tuple'ı a ve b değişkenlerine atayarak yazdırır.

my_dict = { "41": "Kocaeli", "34": "İstanbul" ,"35": "İzmir"}

# for x in my_dict:
#     print(x) # my_dict sözlüğündeki her bir anahtarı yazdırır.


# for x in my_dict:
#     print(my_dict[x]) # my_dict sözlüğündeki her bir değeri yazdırır.

for x in my_dict.values():
    print(x) # my_dict sözlüğündeki her bir değeri yazdırır.

for x in my_dict.keys():
    print(x) # my_dict sözlüğündeki her bir anahtarı yazdırır.

for x in my_dict.items():
    print(x) # my_dict sözlüğündeki her bir anahtar-değer çiftini yazdırır.











