# Verilen bir cümlede bulunan toplam sesli harf (a, e, i, o, u) sayısını hesaplayan bir program yazın.

cumle = "Merhaba, nasılsınız?"
sesli_harfler = "aeiouAEIOU"
toplam_sesli_harf = 0
for harf in cumle:
    if harf in sesli_harfler:
        toplam_sesli_harf += 1
print("Toplam sesli harf sayısı:", toplam_sesli_harf)

