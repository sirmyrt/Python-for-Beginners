# key-value turunde bilgiler tutan veri yapisidir. Key degeri benzersizdir. Key'e karsilik gelen deger value olarak adlandirilir.
# Sözlükler, süslü parantezler {} kullanılarak oluşturulur ve her bir anahtar-değer çifti iki nokta (:) ile ayrılır. Anahtarlar virgülle ayrılarak belirtilir.
# Sözlükler, sırasızdır, yani elemanların belirli bir sırası yoktur. Ancak, Python 3.7 ve sonraki sürümlerde, sözlükler eklenme sırasını korur.
# Sözlükler, değiştirilebilir (mutable) veri yapılarıdır, yani bir sözlüğün içeriği oluşturulduktan sonra değiştirilebilir. Anahtarlar benzersiz olmalıdır, ancak değerler tekrarlanabilir.
#Siralanabilir - Guncellenebilir - Tekrarlanamaz 

sehirler = ['istanbul', 'ankara', 'izmir']
plakalar = [34, 6, 35]

# key-value yapisi ile sehirler ve plakalar bilgilerini tutmak istiyoruz.

print(plakalar[0]) # 34
print(plakalar[1]) # 6
print(plakalar[2]) # 35

print(f'{sehirler[0]} plaka kodu {plakalar[0]}') # istanbul plaka kodu 34
print(f'{sehirler[1]} plaka kodu {plakalar[1]}') # ankara plaka kodu 6
print(f'{sehirler[2]} plaka kodu {plakalar[2]}') # izmir plaka kodu 35

print(plakalar[sehirler.index('istanbul')]) # 34
print(plakalar[sehirler.index('ankara')]) # 6
print(plakalar[sehirler.index('izmir')]) # 35

# dictionary kullanarak sehirler ve plakalar bilgilerini tutmak istiyoruz.

plakalar = {
    'kocaeli': 41,
      'istanbul': 34,
        'ankara': 6, 
          'izmir': 35}

plakalar['edirne'] = 22 # yeni bir key-value ekleme


print(plakalar) 

