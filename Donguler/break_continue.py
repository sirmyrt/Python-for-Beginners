# continue --> döngünün o anki adımını atlar ve bir sonraki adıma geçer.
# break --> döngüyü tamamen sonlandırır.

# isim = "Mert Onur"

# for harf in isim:
#     if (harf == "o" or harf == "O"):
#        break 
#     print(harf) 


# i = 0

# while i < 10:
#    i += 1
#    if (i == 5):
#         continue
#    print(i)

i = 0
toplam = 0

while (i <= 100):
   i += 1
   if (i % 2 == 0):
        continue
   toplam += i

print(toplam)        

      

