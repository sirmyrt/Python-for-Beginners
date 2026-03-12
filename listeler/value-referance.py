#  -- Value Types (Değer Tipleri)  --  # cntrl + K + C hepsini yorum satiri yapmak icin
# x = 10 
# y = 20 

# x = y # x'in değeri y'nin değerine eşitlenir. Bu, x'in değerini 20 yapar. Ancak, bu işlem sadece x'in değerini değiştirir, y'nin değeri değişmez.

# y = 30 # y'nin değeri 30 olarak güncellenir. Bu, y'nin değerini 30 yapar, ancak x'in değeri hala 20'dir.

# print(x,y)

# -- Reference Types (Referans Tipleri) -- 

a = [ "elma", "armut", "muz" ]
b = [ "elma", "armut", "muz" ]

a = b # a'nın değeri b'nin değerine eşitlenir. Bu, a'nın değerini b'nin değeriyle aynı yapar. Ancak, bu işlem sadece a'nın değerini değiştirir, b'nin değeri değişmez.
a[0] = "çilek" # a'nın ilk elemanı "çilek" olarak güncellenir. Bu, a'nın ilk elemanını "çilek" yapar, ancak b'nin ilk elemanı hala "elma"dır.
print(a,b) 


# -- Liste kopyalama -- 

listeA = [10,20]
listeB = listeA.copy()  # 1.yontem // listeB, listeA'nın referansını tutar. Bu, listeB'nin değerini listeA'nın değeriyle aynı yapar. Ancak, bu işlem sadece listeB'nin değerini değiştirir, listeA'nın değeri değişmez.
listeB= list(listeA)    # 2.yontem // listeB, listeA'nın referansını tutar. Bu, listeB'nin değerini listeA'nın değeriyle aynı yapar. Ancak, bu işlem sadece listeB'nin değerini değiştirir, listeA'nın değeri değişmez.

listeB[0] = 100 # listeB'nin ilk elemanı 100 olarak güncellenir. Bu, listeB'nin ilk elemanını 100 yapar, ancak listeA'nın ilk elemanı hala 10'dur.

print(listeA,listeB) # listeA ve listeB'nin değerlerini yazdırır. Bu, listeA'nın değeri [10, 20] ve listeB'nin değeri [100, 20] olarak yazdırır. Ancak, bu işlem sadece listeB'nin değerini değiştirir, listeA'nın değeri değişmez.