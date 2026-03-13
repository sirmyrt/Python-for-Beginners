#local scope
#global scope 
#scope nedir = değişkenlerin erişilebilir olduğu alanlara scope denir

# x = "global scope"

# def my_func():
#     x = "local scope"
#     print(x)

# my_func()
# print(x)


# name = "Mert"

# def change_name(new_name):
#     global name               # global anahtar kelimesi ile global değişkeni fonksiyon içinde değiştirebiliriz
#     name = new_name
#     print(name)

# change_name("Ali")
# print(name)


def greeting():
    name = "Mert"
    

    def hello():
        name = "Ali"
        print("Hello " + name)

    hello()

greeting()   


x = 50 

def test():
   global x
   print(f"x: {x}")
   
   x = 100
   print(f"changed x to {x}")

test()
print(x)    