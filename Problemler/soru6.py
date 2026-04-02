# Verilen bir sayının (örneğin, 5!) faktöriyelini bir fordöngü kullanarak hesaplayan bir program yazın.

sayi = int(input("Sayi Gir:")) 
faktoriyel = 1 

for i in range(1, sayi + 1):
    faktoriyel = faktoriyel * i 
print(f"Faktoriyel: {sayi}! = {faktoriyel}")
