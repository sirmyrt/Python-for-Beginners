#  meyveden oluşan bir liste oluşturun. Listeye yeni bir meyve ekleyin, ardından ikinci meyveyi (1. indeksteki) listeden çıkarın.

meyveler = ["elma", "armut", "muz", "çilek"]
meyveler.append("portakal")  # Yeni bir meyve ekleyelim
print("Meyve listesi:", meyveler)
# İkinci meyveyi (1. indeksteki) listeden çıkaralım
meyveler.pop(1)
print("Güncellenmiş meyve listesi:", meyveler)  