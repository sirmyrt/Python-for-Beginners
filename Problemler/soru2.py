#İlk 10 sayıyı (0-9) sırayla dolaşın. Her yinelemede, geçerli sayıyı, önceki sayıyı ve bunların toplamını yazdırın.

onceki_sayi = 0

for sayi in range(10):
    toplam = onceki_sayi + sayi
    print(f"Geçerli sayı: {sayi}, Önceki sayı: {onceki_sayi}, Toplam: {toplam}")
    onceki_sayi = sayi
    