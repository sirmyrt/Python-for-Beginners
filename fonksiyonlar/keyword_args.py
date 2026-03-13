# Keyword Arguments (Anahtar Kelime Argümanları)
# Fonksiyonlara argümanları sırayla vermek yerine, hangi argümanın hangi değere sahip olduğunu belirterek fonksiyonu çağırabiliriz. Bu, kodun okunabilirliğini artırır ve argümanların sırasını önemsememizi sağlar.
# Keyword arguments kullanarak fonksiyon çağırmak için, argümanları anahtar kelime olarak belirtiriz. Örneğin:


def full_name(firstname: str, lastname: str, age: int) -> str:
    return f"Your name is {firstname} {lastname} and you are {age} years old"

sonuc = full_name("Mert","Onur", 25)
sonuc = full_name(lastname="Onur", firstname="Mert", age=25)


print(sonuc)

