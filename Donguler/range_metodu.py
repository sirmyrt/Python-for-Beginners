# range --> range() fonksiyonu, belirli bir aralıkta sayılar üretmek için kullanılır. Genellikle döngülerde kullanılır ve üç farklı şekilde kullanılabilir:
# range(stop) --> 0'dan başlayarak stop değerine kadar olan sayıları üretir.
# range(start, stop) --> start değerinden başlayarak stop değerine kadar olan sayıları
# range(start, stop, step) --> start değerinden başlayarak stop değerine kadar olan sayıları step adımlarıyla üretir.



# for i in range(1,100,2):
#     print(i)               # 1'den başlayarak 100'e kadar olan tek sayıları yazdırır.


rng = range(10)     # 0'dan başlayarak 10'a kadar olan sayıları üretir.
rng = range(10, 20) # 10'dan başlayarak 20'ye kadar olan sayıları üretir.
rng = range(0, 10, 2) # 0'dan başlayarak 10'a kadar olan sayıları 2'şer adımlarla üretir (0, 2, 4, 6, 8).
rng = range(0,-20,-2) # 0'dan başlayarak -20'ye kadar olan sayıları 2'şer adımlarla üretir (0, -2, -4, -6, -8, -10, -12, -14, -16, -18).


sonuc = list(rng)  # range nesnesini listeye dönüştürür ve [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] sonucunu verir.
print(sonuc)

for i in range (50,250):
    if(i%2==0):
        print(i)       # 50'den başlayarak 250'ye kadar olan çift sayıları yazdırır.