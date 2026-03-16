# Class 
class Product:
    

    #method
    #attribute, property 
  def __init__(self, name, price, isActive):
    self.name = name
    self.price = price
    self.isActive = isActive 
   
# Instance , Nesne 
product1 = Product("Iphone", 1000, True) 
product2 = Product("Samsung", 800, True)
product3 = Product("Huawei", 600, True)

urunler = [product1, product2, product3]
 
for urun in urunler:
    if urun.isActive:
     print(f"Ürün Adı: {urun.name} - Fiyat: {urun.price} - Aktif mi? {urun.isActive}")
