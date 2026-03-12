# Identity ve Membership Operatörleri
# Identity Operatörleri
# is: İki nesnenin aynı nesne olup olmadığını kontrol eder.
# is not: İki nesnenin aynı nesne olmadığını kontrol eder.

x = [1, 2, 3]
y = [1, 2, 5]

z = y 

print (x is y) # False  . x ve y farklı nesneler olduğu için False döner.
print (y is z) # True   . y ve z aynı nesne olduğu için True döner.
print (x is not y) # True  . x ve y farklı nesneler olduğu için True döner.
print (y is not z) # False  . y ve z aynı nesne olduğu için False döner.

# Membership Operatörleri
# in: Bir değerin bir dizide veya koleksiyonda bulunup bulunmadığını kontrol eder.
# not in: Bir değerin bir dizide veya koleksiyonda bulunmadığını kontrol eder.

liste = [1, 2, 3, 4, 5]

print(3 in liste) # True  . 3, liste içinde bulunduğu için True döner.
print(6 in liste) # False  . 6, liste içinde bulunmadığı için False döner.
print(3 not in liste) # False  . 3, liste içinde bulunduğu için False döner.
print(6 not in liste) # True  . 6, liste içinde bulunmadığı için True döner.    
