# Metot       /   Açıklama
# append()      /   Listenin sonuna bir eleman ekler.
# insert()      /   Belirtilen indexe bir eleman ekler.
# pop()         /   Belirtilen indexdeki elemanı siler ve silinen elemanı döndürür. (index belirtilmezse son elemanı siler)
# remove()      /   Belirtilen değere sahip ilk elemanı siler.
# clear()       /   Listenin tüm elemanlarını siler.
# index()        /   Belirtilen değere sahip ilk elemanın indexini döndürür.
# count()        /   Belirtilen değere sahip elemanların sayısını döndürür.
# sort()         /   Listenin elemanlarını sıralar.
# reverse()      /   Listenin elemanlarının sırasını tersine çevirir.
# copy()         /   Listenin bir kopyasını oluşturur.
# extend()       /   Bir listenin elemanlarını başka bir listeye ekler.
# len()           /   Listenin uzunluğunu döndürür.
# in               /   Bir elemanın listede olup olmadığını kontrol eder.
# not in            /   Bir elemanın listede olup olmadığını kontrol eder.


numbers = [2,5,6,13,15,22,47,123,658,790,903]
names = ["Ali", "Veli", "Ayşe", "Fatma", "Ahmet", "Mehmet"]

sonuc = min(numbers) # Listenin en küçük elemanını döndürür
sonuc = max(numbers) # Listenin en büyük elemanını döndürür
sonuc = sum(numbers) # Listenin elemanlarının toplamını döndürür
sonuc = len(numbers) # Listenin uzunluğunu döndürür

sonuc = min(names) # Listenin alfabetik olarak en küçük elemanını döndürür
sonuc = max(names) # Listenin alfabetik olarak en büyük elemanını döndürürür
sonuc = len(names) # Listenin uzunluğunu döndürür

# Ekleme 

numbers.append(1000) # Listenin sonuna 1000 elemanını ekler
names.append("Zeynep") # Listenin sonuna "Zeynep" elemanını ekler

numbers.insert(0, 1) # Listenin 0. indexine 1 elemanını ekler
names.insert(2, "Can") # Listenin 2. indexine "Can" elemanını ekler

# Silme

numbers.pop() # Listenin son elemanını siler ve silinen elemanı döndürür
names.pop(1) # Listenin 1. indexindeki elemanı siler ve silinen elemanı döndürür
numbers.remove(13) # Listenin ilk 13 elemanını siler
names.remove("Ahmet") # Listenin ilk "Ahmet" elemanını siler

# Sıralama

numbers.sort() # Listenin elemanlarını küçükten büyüğe sıralar
names.sort() # Listenin elemanlarını alfabetik olarak sıralar
numbers.reverse() # Listenin elemanlarının sırasını tersine çevirir
names.reverse() # Listenin elemanlarının sırasını tersine çevirir

# Arama 

sonuc = numbers.index(22) # Listenin elemanlarından 22'nin indexini döndürür
sonuc = names.index("Fatma") # Listenin elemanlarından "Fatma"

# in ve not in operatörleri

sonuc = 22 in numbers # Listenin elemanlarından 22'nin olup olmadığını kontrol eder
sonuc = "Ali" in names # Listenin elemanlarından "Ali"nin olup
sonuc = 100 in numbers # Listenin elemanlarından 100'ün olup olmadığını kontrol eder
sonuc = "Zeynep" not in names # Listenin elemanlarından "Zeynep"in olup olmadığını kontrol eder
sonuc = 30 not in numbers # Listenin elemanlarından 30'un olup olmadığını kontrol eder

# .count => Belirtilen değere sahip elemanların sayısını döndürür.

sonuc = numbers.count(6) # Listenin elemanlarından 6'nın kaç tane olduğunu döndürür
sonuc = names.count("Ali") # Listenin elemanlarından "Ali"nin kaç tane olduğunu döndürür 


print(sonuc)

