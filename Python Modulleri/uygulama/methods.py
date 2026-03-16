import db

def urun_ekle(isim, fiyat): 
    db.urunler.append({
        "id": len(db.urunler) + 1,
        "isim": isim,
        "fiyat": fiyat
    })

def guncelle(id,isim,fiyat):
    for urun in db.urunler:
        if urun["id"] == id:
            urun["isim"] = isim
            urun["fiyat"] = fiyat
            break

def urunBilgileri_getir():
   return db.urunler        