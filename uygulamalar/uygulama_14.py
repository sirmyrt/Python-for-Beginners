# 1- Baslangic ve bitis degerlerini  kullanicidan aliniz ve bu degerler arasindaki tum cift sayilari yazdiriniz


# baslangic = int(input("baslangic"))
# bitis = int(input("bitis"))

# i = baslangic

# while i <= bitis:
#     if (i % 2 == 0):  # i'nin çift olup olmadığını kontrol eder. Eğer i çift ise, bu koşul True olur ve i yazdırılır.
        # print(i)
    # i += 1  # i'yi 1 artırarak döngünün sonlanmasını sağlar. Bu şekilde i, bitis değerine ulaştığında koşul False olur ve döngü sona erer.


# 2- (1-100) arasindaki sayilari azalan sekilde yazdiriniz.


# i = 100
# while (i > 0):
#     print(i)
#     i -= 1  # i'yi 1 azaltarak döngünün sonlanmasını sağlar. Bu şekilde i, 0'a ulaştığında koşul False olur ve döngü sona erer.


# 3- Kullanicidan alacaginiz 5 sayiyi ekrana sirali bir sekilde yazdiriniz


i = 0
sayilar = []

while (i < 5):
  sayi = int(input("Sayi giriniz: "))
  sayilar.append(sayi)  # Kullanıcının girdiği sayıyı sayilar listesine ekler.
  i += 1  # i'yi 1 artırarak döngünün sonlan

sayilar.sort()  # sayilar listesini küçükten büyüğe sıralar.
print("Girilen sayılar sıralı şekilde: ", sayilar)  # Sıralanmış sayilar listesini yazdırır.





# 4- Klavyeden girisi istenen username bilgisi icin bosluk girildigi surece tekrar username girisi isteyiniz

username = ""

while not username: # username değişkeni boş olmadığı sürece döngü devam eder. Eğer kullanıcı boş bir string girerse, bu koşul False olur ve döngü sona erer.
   username = input("Kullanıcı adı giriniz: ")  # Kullanıcıdan bir kullanıcı adı girmesini ister ve bu değeri username değişkenine atar.
print("Girilen kullanici adi: " + username)   