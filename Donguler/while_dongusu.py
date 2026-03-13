# for => list
sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#while --> koşul doğru olduğu sürece çalışır.

# while True:
#     print("Sonsuz döngü")  # Bu kod sonsuz döngü oluşturur, çünkü koşul her zaman True'dur. Programı durdurmak için Ctrl + C tuşlarına basabilirsiniz.

# i = 0 

# while i<10:
#     print(i)
#     i += 1  # i'yi 1 artırarak döngünün sonlanmasını sağlar. Bu şekilde i 10'a ulaştığında koşul False olur ve döngü sona erer.


i = 0

while ( i < len(sayilar)):
    print(sayilar[i])  # sayilar listesinin i'inci elemanını yazdırır.
    i += 1  # i'yi 1 artırarak döngünün sonlanmasını sağlar. Bu şekilde i, sayilar listesinin uzunluğuna ulaştığında koşul False olur ve döngü sona erer.

# for döngüsü, belirli bir koleksiyonun (örneğin bir liste) her bir elemanını sırayla işlemek için kullanılır. Bu durumda, sayilar listesindeki her bir sayıyı yazdırmak için for döngüsü kullanılabilir.

for sayi in sayilar:
    print(sayi)  # sayilar listesindeki her bir sayıyı sırayla yazdırır. Bu, while döngüsüne göre daha kısa ve okunabilir bir kod sağlar.