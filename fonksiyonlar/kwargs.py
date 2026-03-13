#Keyword argumanlar ve argumanlar farki

# def display_user(*args):        #*args ile argumanlar kullanilir. Argumanlar sirali olarak gonderilir.
#     print(type(args))
#     print(args)

# display_user()

# def display_user(**kwargs):      #**kwargs ile keyword argumanlar kullanilir. Keyword argumanlar anahtar-deger seklinde gonderilir.
#     print(type(kwargs))
#     print(kwargs)

# display_user()    

def display_user(**kwargs):
#     print(type(kwargs))
#     print(kwargs)


  for key,value in kwargs.items():     #kwargs ile gonderilen keyword argumanlar dict seklinde gonderilir. Bu nedenle items() metodu ile key-value ciftlerine erisebiliriz.
    print(f"{key}: {value}")
print("\n")

display_user(username="mert")  
display_user(username="mert",email="info@mert.com")
display_user(username="mert",email="info@mert.com",country="Turkey")

def myFunc(a,b,c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(1,2,3,4,5,6,7,8,9,key1="value1",key2="value2")    

