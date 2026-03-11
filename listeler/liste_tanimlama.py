programlama_dilleri = ["Python", "Java", "C++", "JavaScript"]

sonuc = programlama_dilleri 
sonuc = type(programlama_dilleri)
sonuc = programlama_dilleri[0:2] # 0. indexten 2. indexe kadar olan elemanları alır (2. index dahil değil)
sonuc = programlama_dilleri[:2] # Başlangıçtan 2. indexe kadar olan elemanları alır
sonuc = programlama_dilleri[2:4] # 2. indexten 4. indexe kadar olan elemanları alır (4. index dahil değil)
sonuc = programlama_dilleri[2:5] # 2. indexten 5. indexe kadar olan elemanları alır (5. index dahil değil)
sonuc = programlama_dilleri[:] # Tüm elemanları alır
sonuc = programlama_dilleri[-3:-1] # Başlangıçtan sonuna kadar 2'şer atlayarak elemanları alır
sonuc = programlama_dilleri[-3:] # Son 3 elemanı alır

# Guncelleme
programlama_dilleri[-1] = "Php" # Son elemanı "Php" olarak günceller

sonuc = programlama_dilleri
sonuc = len(programlama_dilleri) # Listenin uzunluğunu verir
sonuc = programlama_dilleri + ["C#", "Go"] # Listeye yeni elemanlar ekler

sonuc = "Python" in programlama_dilleri # "Python" elemanının listede olup olmadığını kontrol eder
sonuc = "React" in programlama_dilleri # "React" elemanının listede olup olmadığını kontrol eder

for dil in programlama_dilleri:
    print (dil)




print (sonuc)