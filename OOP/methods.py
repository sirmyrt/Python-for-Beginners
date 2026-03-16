# Class 
class Product:

    #attribute, property 
    def __init__(self, name, price, isActive):
     self.name = name
     self.price = price
     self.isActive = isActive 

     #instance method
    def intro(self):
       return f"Ürün Adı: {self.name} - Fiyat: {self.price} - Aktif mi? {self.isActive}"
       
    def kdv_price(self):
        return self.price * 1.18
   
# Instance , Nesne 
product1 = Product("Iphone", 1000, True) 
product2 = Product("Samsung", 800, True)
product3 = Product("Huawei", 600, True)

urunler = [product1, product2, product3]
 
for urun in urunler:
    if urun.isActive:
     print(f"Ürün Adı: {urun.name} - Fiyat: {urun.price} - Aktif mi? {urun.isActive}")
     print(urun.intro())
     print(f"KDV'li Fiyat: {urun.kdv_price()}")
