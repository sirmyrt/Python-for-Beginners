# Fonksiyonlar :
# Bir işlemi gerçekleştirmek için bir araya getirilmiş kod bloklarıdır.
# Fonksiyonlar, kodun tekrar kullanılabilirliğini sağlar ve programın daha düzenli olmasına yardımcı olur.  
# Fonksiyon Tanımlama :
# Python'da bir fonksiyon tanımlamak için "def" anahtar kelimesi kullanılır. Fonksiyon adı, parantezler ve iki nokta (:) ile tanımlanır. Fonksiyonun içindeki kod bloğu, girintili olarak yazılır.      

# Örnek 1 : Basit bir fonksiyon tanımlama ve çağırma

# def selamla():
#     print("Merhaba, nasılsın?")
# selamla()         # Fonksiyonu çağırma

def selamla():
    print("Merhaba, nasılsın?")

for i in range(3):
    selamla()         # Fonksiyonu çağırma 

# yada 

# def selamla():
#     for i in range(3):
#         print("Merhaba, nasılsın?")
# selamla()         # Fonksiyonu çağırma

def toplama():
    print(2 + 3)

toplama()         # Fonksiyonu çağırma


