# x = 10

# if x > 5:
#     raise ValueError("x değeri 5'ten büyük olamaz.")
# # yada 
# if x > 5:
#     raise Exception("x değeri 5'ten büyük olamaz.")

def renklendir(text, renk):
    renkler = ("kırmızı", "mavi", "yeşil", "sarı", "sarı", "sarı")
   
    if type(text) is not str:
        raise TypeError("text parametresi bir string olmalıdır.")

    if type(renk) is not str:
        raise TypeError("renk parametresi bir string olmalıdır.")

    if renk not in renkler:
        raise ValueError(f"renk parametresi şu renklerden biri olmalıdır:")    

    print(f"{text} {renk} renkte yazdırıldı.")
try:
 renklendir("Dünya", "mavi")
 renklendir("Python", "yeşil")                             
except (TypeError, ValueError) as e:
    print(f"Hata: {e}")



# renklendir("10", "kırmızı")     # text parametresi string olduğu için hata vermez
# renklendir(10, "kırmızı")       # text parametresi string olmadığı için TypeError hatası verir

