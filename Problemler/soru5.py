#Üçüncü bir geçici değişken kullanmadan , a ve b olmak üzere iki değişkenin değerlerini değiştiren bir program yazın.

a = 5
b = 10
print(f"Before Swap: a = {a}, b = {b}")

# Simultaneous assignment (Tuple Unpacking)
a, b = b, a

print(f"After Swap: a = {a}, b = {b}")
