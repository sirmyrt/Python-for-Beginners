# enumerate ve zip metotları iterable nesneler üzerinde döngü kurarken bize yardımcı olan metotlardır.
# enumerate --> bir iterable nesnenin elemanlarını ve indekslerini birlikte döndürür. Genellikle for döngülerinde kullanılır.
# zip --> birden fazla iterable nesneyi aynı anda döndürür. Her bir iterable nesnenin aynı indeksindeki elemanları birleştirerek bir tuple oluşturur. Genellikle for döngülerinde kullanılır.

markalar = ["BMW", "Mercedes", "Audi"]

# index = 1
# for markka in markalar:
#     print(f"{index}-{markka}")
#     index += 1


obj1 = enumerate(markalar)  # enumerate nesnesi oluşturur ve markalar listesinin elemanlarını ve indekslerini birlikte döndürür.

print(type(obj1))  # <class 'enumerate'> sonucunu verir.
print(list(obj1))  # enumerate nesnesini listeye dönüştürür ve [(0, 'BMW'), (1, 'Mercedes'), (2, 'Audi')] sonucunu verir.   

for index,marka in enumerate(markalar):
    print(f"{index}-{marka}")  # 0-BMW, 1-Mercedes, 2-Audi sonucunu verir.
    
    # print(marka)  # (0, 'BMW'), (1, 'Mercedes'), (2, 'Audi') sonucunu verir.


# -- zip metodu --

numara = [250, 450, 350]
ogrenci = ["Mert", "Onur", "Yılmaz"]

print(list(zip(numara, ogrenci)))  # zip nesnesi oluşturur ve numara ve ogrenci listelerinin aynı indeksindeki elemanları birleştirerek bir tuple oluşturur.

for no,isim in zip(numara, ogrenci):
    print(no,isim)  # (250, 'Mert'), (450, 'Onur'), (350, 'Yılmaz') sonucunu verir.