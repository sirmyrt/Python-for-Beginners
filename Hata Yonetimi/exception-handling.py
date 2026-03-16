while True:
   try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x / y)
   except (ZeroDivisionError, ValueError) as ex:
    print("Gecersiz islem: Sifira bolme veya gecersiz deger girisi")
    print(ex) 
   except Exception as ex:
    print("Bilinmeyen bir hata olustu")
    print(ex)
   else:
    break
   finally:
    print("Islem tamamlandi")
   