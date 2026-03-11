my_list = [1, 2, 3, 4, 5] #list
my_tuple = (1, 2, 3, 4, 5) #tuple değiştirilemez

print(type(my_list))   
print(type(my_tuple))

my_list[0] = 10 #listelerde elemanlar değiştirilebilir
# my_tuple[0] = 10 #tuple'larda elemanlar değiştirilemez, bu satır hata verecektir

sonuc1 = my_list[0] #listeden 0. indexteki elemanı döndürür
sonuc2 = my_tuple[0] #tuple'dan 0. indexteki elemanı döndürür

print(sonuc1)
print(sonuc2)

my_tuple2 = tuple([1, 2, 3, 4, 5]) #listeden tuple oluşturma
my_list2 = list((1, 2, 3, 4, 5)) #tuple'dan list oluşturma

print(type(my_tuple2))
print(type(my_list2))