# mail = input("Mail: ")
# password = input("Password: ")

# login = (mail == "admin" and password == "1234")

# if(login):
#     print("Login successful")
# else:  
#      print("Login failed")


#  -- tersi --

# if(not(login)):
#     print("Login failed")
# else:  
#      print("Login successful") 


# -- tek satırda -- 
# if (mail == "admin" and password == "1234"):
#     print("Login successful")


# -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

x = 10
y = 20

if(x > y):
    print("x y den kucuk")
elif(x == y):
    print("x y ye esittir")
else:
    print("x y den buyuk")



yas = 20

if yas < 18:
    print("Çocuk")
elif yas < 65:  # "Eğer yukarıdaki yanlışsa ama bu doğruysa"
    print("Erişkin")
else:
    print("Yaşlı")