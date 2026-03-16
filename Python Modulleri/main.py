import module 

sonuc = module.sayi 
sonuc = module.sayilar
sonuc = module.urun
sonuc = module.toplama(5, 10)

import module as m

sonuc = m.sayi
sonuc = m.sayilar   
sonuc = m.urun
sonuc = m.toplama(5, 10)

from module import sayi, sayilar, urun

sonuc = sayi
sonuc = sayilar
sonuc = urun

from module import *

sonuc = sayi
sonuc = sayilar
sonuc = urun
sonuc = toplama(5, 10)

print(sonuc)