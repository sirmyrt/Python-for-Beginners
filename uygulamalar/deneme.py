import random

# Global Kasa
KASA = 5000
kullanicilar = {}

def bahis_gecerli_mi(bahis):
    if bahis == 5:
        return True
    if bahis >= 10 and bahis % 10 == 0:
        return True
    return False

def yeni_kullanici_olustur():
    return {
        "bakiye": 0,
        "toplam_oyun": 0,
        "toplam_kazanc_sayisi": 0,
        "kaybetme_serisi": 0,
        "yuz_tl_ustu_kazanc": 0,
        "yuz_tl_ustu_zorunlu_kayip": 0,
        "uc_yuz_tl_ustu_el_sayisi": 0,
        "bin_tl_kurali_el_sayisi": 0,
        "bin_tl_kurali_kayip_durumu": 0, # 1 kayıp 1 kazanç dengesi için
        "sans_modifikatoru": 0.0 # Giriş yaptıkça -%5 ile +%5 arası değişecek
    }

def zarlari_belirle(kullanici, bahis, secilen_sayi):
    """
    Arka plandaki hileli algoritma burada çalışır.
    True dönerse kullanıcı kazanır, False dönerse kaybeder.
    """
    # 1. ÖNCELİK: 500 TL ve Üstü "Batırma" Kuralı
    if bahis >= 500 and kullanici["bakiye"] > 100:
        return False # Kesinlikle kaybedecek

    # 2. ÖNCELİK: Bakiye > 1000 TL Kuralı (6 el boyunca 2 elde 1 kazanç)
    if kullanici["bakiye"] > 1000 and kullanici["bin_tl_kurali_el_sayisi"] < 6:
        kullanici["bin_tl_kurali_el_sayisi"] += 1
        if kullanici["bin_tl_kurali_kayip_durumu"] >= 1:
            kullanici["bin_tl_kurali_kayip_durumu"] = 0
            return True # Zorunlu Kazanç
        else:
            kullanici["bin_tl_kurali_kayip_durumu"] += 1
            return False # Zorunlu Kayıp
    elif kullanici["bakiye"] <= 1000:
        kullanici["bin_tl_kurali_el_sayisi"] = 0 # Bakiye düşerse sıfırla

    # 3. ÖNCELİK: 300 TL ve Üstü Yüksek Bahis Kuralı
    if bahis >= 300:
        kullanici["uc_yuz_tl_ustu_el_sayisi"] += 1
        el = kullanici["uc_yuz_tl_ustu_el_sayisi"]
        
        if el <= 4:
            ihtimal = 0.80
        elif el <= 7:
            ihtimal = 0.40
        elif el <= 10:
            ihtimal = 0.05
        elif el <= 20:
            ihtimal = 0.01
        else:
            kullanici["uc_yuz_tl_ustu_el_sayisi"] = 1 # 20 el bitti, başa dön
            ihtimal = 0.80
            
        ihtimal += kullanici["sans_modifikatoru"]
        return random.random() < ihtimal

    # 4. ÖNCELİK: 100 TL ve Üstü Bahis Kuralı
    if bahis >= 100:
        if kullanici["yuz_tl_ustu_kazanc"] >= 5:
            if kullanici["yuz_tl_ustu_zorunlu_kayip"] < 3:
                kullanici["yuz_tl_ustu_zorunlu_kayip"] += 1
                return False # Arka arkaya 3 kez zorunlu kayıp
            else:
                # 3 kayıp bitti, hakları sıfırla
                kullanici["yuz_tl_ustu_kazanc"] = 0
                kullanici["yuz_tl_ustu_zorunlu_kayip"] = 0

    # 5. ÖNCELİK: Standart "4 Elde 1 Zorunlu Kazanç" Kuralı (Normal ve 100TL üstü için geçerli)
    # Eğer toplam kazanç 20'yi geçtiyse ve bahis 100'den küçükse bu hak iptal olur.
    guvence_aktif = True
    if kullanici["toplam_kazanc_sayisi"] > 20 and bahis < 100:
        guvence_aktif = False

    if guvence_aktif:
        if kullanici["kaybetme_serisi"] >= 3:
            return True # 3 kez kaybetti, 4. el zorunlu kazanç

    # Eğer hiçbir hile kuralına takılmadıysa standart zar atışı (1/6 ihtimal) + Şans Modifikatörü
    standart_ihtimal = (1/6) + kullanici["sans_modifikatoru"]
    return random.random() < standart_ihtimal


def oyunu_baslat():
    global KASA
    print("-" * 40)
    print("🎲 HİLELİ ZAR OYUNUNA HOŞ GELDİNİZ 🎲")
    print("-" * 40)
    
    kullanici_adi = input("Lütfen kullanıcı adınızı girin: ").strip().lower()
    
    # Kullanıcı kaydı ve Şans Modifikatörü ayarlama
    if kullanici_adi not in kullanicilar:
        kullanicilar[kullanici_adi] = yeni_kullanici_olustur()
        baslangic_bakiye = int(input("Başlangıç bakiyenizi girin (TL): "))
        kullanicilar[kullanici_adi]["bakiye"] = baslangic_bakiye
        print(f"Yeni kayıt oluşturuldu. Hoş geldin {kullanici_adi}!")
    else:
        # Tekrar giriş yapan kullanıcı için şans oranı değiştiriliyor
        mod = random.uniform(-0.05, 0.05)
        kullanicilar[kullanici_adi]["sans_modifikatoru"] = mod
        mod_yuzde = mod * 100
        print(f"Tekrar hoş geldin {kullanici_adi}!")
        # print(f"(Sistem: Şans oranınız {'arttı' if mod > 0 else 'azaldı'} : %{mod_yuzde:.1f})") # İstenirse gösterilebilir
        
    kullanici = kullanicilar[kullanici_adi]
    oyun_sayaci = 0

    while True:
        # 10 Oyunda bir devam kontrolü
        if oyun_sayaci > 0 and oyun_sayaci % 10 == 0:
            devam = input("\n10 oyun oynadınız. Devam etmek istiyor musunuz? (e/h): ").strip().lower()
            if devam == 'h':
                print(f"Oyun sonlandırıldı. Kalan Bakiyeniz: {kullanici['bakiye']} TL. Görüşmek üzere!")
                break
        
        # Bakiye Kontrolü ve Yükleme
        if kullanici["bakiye"] <= 0:
            print("\nBakiyeniz sıfırlandı!")
            yukleme_istek = input("Bakiye yüklemek ister misiniz? (e/h): ").strip().lower()
            if yukleme_istek == 'e':
                miktar = int(input("Yüklenecek miktar (TL): "))
                kullanici["bakiye"] += miktar
                KASA += miktar
                print(f"Bakiye yüklendi. Kasa {miktar} TL arttı.")
            else:
                print("Bakiye yüklenmedi. Oyun sonlandırılıyor...")
                break

        print(f"\n[{kullanici_adi.upper()}] Bakiye: {kullanici['bakiye']} TL | [KASA]: {KASA} TL")
        
        # Kullanıcı Girdileri
        try:
            secilen_sayi = int(input("Lütfen zarı tahmin edin (1-6): "))
            if secilen_sayi < 1 or secilen_sayi > 6:
                print("Hata: Sadece 1 ile 6 arasında bir sayı seçebilirsiniz.")
                continue
                
            bahis = int(input("Bahis miktarınızı girin (Min 5TL, sonra 10'un katları): "))
            if bahis > kullanici["bakiye"]:
                print("Hata: Bakiyenizden fazla bahis yapamazsınız.")
                continue
                
            if not bahis_gecerli_mi(bahis):
                print("Hata: Bahis miktarı kurallara uymuyor (5, 10, 20, 30... olmalı).")
                continue
                
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")
            continue

        oyun_sayaci += 1
        kullanici["toplam_oyun"] += 1
        
        # Sonucu Belirle (Hile Algoritması Çalışır)
        kazandi_mi = zarlari_belirle(kullanici, bahis, secilen_sayi)
        
        # Zarın Ekrana Yazdırılması
        if kazandi_mi:
            gelen_zar = secilen_sayi
        else:
            # Seçilen sayı haricinde rastgele bir zar getir
            gelen_zar = random.choice([x for x in range(1, 7) if x != secilen_sayi])

        print(f"\n>>> ZAR ATILIYOR... Gelen Zar: {gelen_zar}")

        # Kazanma ve Kaybetme İşlemleri
        if kazandi_mi:
            # Örn: 1'e 5 veriyor (Bahis dahil 6 katı cebine girer, kasadan 5 katı çıkar)
            kazanc = bahis * 5
            kullanici["bakiye"] += kazanc
            KASA -= kazanc
            kullanici["kaybetme_serisi"] = 0
            kullanici["toplam_kazanc_sayisi"] += 1
            if bahis >= 100:
                kullanici["yuz_tl_ustu_kazanc"] += 1
                
            print(f"🎉 TEBRİKLER! {kazanc} TL Kazandınız!")
        else:
            kullanici["bakiye"] -= bahis
            KASA += bahis
            kullanici["kaybetme_serisi"] += 1
            print(f"😞 Kaybettiniz. {bahis} TL Kasaya gitti.")

# Programı Çalıştır
if __name__ == "__main__":
    oyunu_baslat()