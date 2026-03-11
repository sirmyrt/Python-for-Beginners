#string concat
ad = "Mert"
soyad = "Onur"
yas = 22

# msj = "Benim adim " + ad + " soyadim " + soyad + " ve yasim " + str(yas)

#string format
#msj = "Benim adim {} soyadim {} ve yasim {}".format(ad,soyad,yas)
#msj = "Benim adim {1} soyadim {0} ve yasim {2}".format(ad,soyad,yas)
#msj = "Benim adim {ad} soyadim {soyad} ve yasim {yas}".format(ad=ad,soyad=soyad,yas=yas)

#f-string
msj = f"Benim adim {ad} soyadim {soyad} ve yasim {yas}"
print(msj)