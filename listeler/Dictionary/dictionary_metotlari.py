# clear() tum elemanları siler
# copy() bir sözlüğün kopyasını oluşturur
# get() belirtilen anahtara karşılık gelen değeri döndürür, eğer anahtar bulunmazsa varsayılan değeri döndürebilir
# items() sözlüğün anahtar-değer çiftlerini içeren bir görünüm döndür
# keys() sözlüğün anahtarlarını içeren bir görünüm döndürür
# pop() belirtilen anahtara karşılık gelen değeri kaldırır ve döndürür
# popitem() sözlüğün son eklenen anahtar-değer çiftini kaldırır ve döndürür
# setdefault() belirtilen anahtarın değerini döndürür, eğer anahtar bulunmazsa belirtilen değeri ekler ve döndürür
# update() bir sözlüğü başka bir sözlükle günceller
# values() sözlüğün değerlerini içeren bir görünüm döndürür

yemekTarifi = {
    'yemek': 'mercimek köftesi',
    'malzemeler': ['mercimek', 'bulgur', 'soğan', 'domates salçası', 'biber salçası', 'maydanoz', 'tuz', 'karabiber'],
    'hazırlanışı': 'Mercimekleri haşlayın, suyunu süzün ve bir kaba alın. Üzerine bulguru ekleyin ve karıştırarak bulgurun şişmesini sağlayın. Soğanı ince ince doğrayın ve mercimek-bulgur karışımına ekleyin. Domates salçası, biber salçası, tuz, karabiber ve ince kıyılmış maydanozu da ekleyerek iyice karıştırın. Karışımı avuç içinde şekillendirerek köfte haline getirin.'
}

 # acces items

sonuc = yemekTarifi["yemek"]
sonuc = yemekTarifi.get("yemek") # get() metodu ile de ayni sonucu alabiliriz. get() metodu, belirtilen anahtarın değerini döndürür, eğer anahtar bulunmazsa None döndürür.
sonuc = yemekTarifi.keys() # keys() metodu ile sözlüğün anahtarlarını alabiliriz.
sonuc = yemekTarifi.values() # values() metodu ile sözlüğün değerlerini alabiliriz.
sonuc = yemekTarifi.items() # items() metodu ile sözlüğün anahtar-değer çiftlerini alabiliriz. Bu, her bir anahtar-değer çiftini içeren bir görünüm döndürür.

# uptade items

# yemekTarifi["yemek"] = "Manti"

yemekTarifi.update({"yemek": "Manti"}) # update() metodu ile sözlüğün değerlerini güncelleyebiliriz. Bu, belirtilen anahtarın değerini günceller veya yeni bir anahtar-değer çifti ekler.

sonuc = yemekTarifi 
 

# delete items

yemekTarifi.pop("hazırlanışı") # pop() metodu ile belirtilen anahtara karşılık gelen değeri kaldırabiliriz. Bu, belirtilen anahtarın değerini döndürür.
yemekTarifi.popitem() # popitem() metodu ile sözlüğün son eklenen anahtar-değer çiftini kaldırabiliriz. Bu, kaldırılan anahtar-değer çiftini döndürür.
yemekTarifi.clear() # clear() metodu ile sözlüğün tüm elemanlarını silebiliriz. Bu, sözlüğü boş bir sözlük haline getirir.


print(sonuc)
