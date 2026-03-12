# Mantıksal Operatörler
# 1- And
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# 2- Or
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# 3- Not
# not True = False
# not False = True

x = 9 

sonuc1= (x > 5) and (x < 10) # x'in 5'ten büyük ve 10'dan küçük olup olmadığını kontrol eder.

sonuc2= (x > 0) and (x % 2 == 0) # x'in pozitif ve çift olup olmadığını kontrol eder.
sonuc3= (x > 0) or (x % 2 == 0) # x'in pozitif veya çift olup olmadığını kontrol eder.
sonuc4= not (x > 0) # x'in pozitif olmadığını kontrol eder

print(sonuc1) # True
print(sonuc2) # False   
print(sonuc3) # True
print(sonuc4) # False