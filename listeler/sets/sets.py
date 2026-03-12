#  -- sets -- 

# Indekslenemez # Sırasız # Değiştirilemez # Tekrarsız  -- Elemanlar tekrarlanamaz -- Eleman silebilir veya eklenebilir -- Guncellenemez 

mySet = {"elma", "armut", "muz", "çilek"}

 # mySet.add("kivi") # add() metodu ile sete yeni bir eleman ekleyebiliriz. Eğer eklemek istediğimiz eleman zaten sette varsa, set değişmez.
 # mySet.update(["portakal", "mandalina"]) # update() metodu ile sete birden fazla eleman ekleyebiliriz. Bu, belirtilen iterable'ın her bir elemanını sete ekler.
 # mySet.remove("armut") # remove() metodu ile setten belirtilen elemanı kaldırabiliriz. Eğer kaldırmak istediğimiz eleman sette yoksa, KeyError hatası verir.
 # mySet.discard("armut") # discard() metodu ile setten belirtilen elemanı kaldırabiliriz. Eğer kaldırmak istediğimiz eleman sette yoksa, hata vermez ve set değişmez.
 # mySet.pop() # pop() metodu ile setten rastgele bir elemanı kaldırabiliriz ve döndürebiliriz. Setler sırasız olduğu için hangi elemanın kaldırılacağını tahmin edemeyiz.
 # mySet.clear() # clear() metodu ile setin tüm elemanlarını silebiliriz. Bu, seti boş bir set haline getirir.         

for x in mySet:
    print(x) # for döngüsü ile setin elemanlarını tek tek yazdırabiliriz. Setler sırasız olduğu için elemanların sırası tahmin edilemez.

sonuc = mySet
print(sonuc) 