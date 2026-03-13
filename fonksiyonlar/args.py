# args --> bir fonksiyona istediğimiz kadar parametre gönderebilmemizi sağlar. Gönderilen parametreler bir tuple olarak saklanır.


# sayilar = (10,20,30,40)

# def toplam(liste):
#     sonuc = 0
#     for i in liste:
#         sonuc += i
#     return sonuc

def toplam(*args):
    print(args)
    print(type(args))
    sonuc = 0
    for i in args:
        sonuc += i
    return args 

sonuc =toplam(10,20)
sonuc = toplam(10,20,30,40)
sonuc = toplam(10,20,30,40,50,60)

print(sonuc)