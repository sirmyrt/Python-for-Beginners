# Verilen dizede yalnızca çift indeks numarasında bulunan karakterleri görüntüleyin.

def cift_indeks_karakterleri(dize):
    cift_karakterler = ""
    for i in range(len(dize)):
        if i % 2 == 0:
            cift_karakterler += dize[i]
    return cift_karakterler
# Örnek kullanım
dize = "Merhaba Dünya!"
sonuc = cift_indeks_karakterleri(dize)
print(sonuc)