"""
** BankaHesabi isminde sinif tanimla
** Uretilen her bir nesne "hesapSahibi" isminde bir ozellige sahip olsun. BankaHesabi("Mert Onur")
** Uretilen her bir nesne "bakiye" isminde bir ozellige sahip olsun ve baslangic degeri 0 olsun.
** Uretilen her bir nesne "paraYatir" isminde bir metoda sahip olsun. Bu metod parametre olarak yatirilacak miktari alsin ve bakiyeye eklesin. ve bakiye miktarini geri dondurmeli
** Uretilen her bir nesne "paraCek" isminde bir metoda sahip olsun. Bu metod parametre olarak cekilecek miktari alsin ve eger cekilecek miktar bakiyeden kucuk veya esit ise bakiyeden ceksin ve bakiye miktarini geri dondurmeli. Eger cekilecek miktar bakiyeden buyuk ise "Yetersiz Bakiye" yazdirsin ve bakiye miktarini geri dondurmeli


hesap = BankaHesabi("Mert Onur")
hesap.hesapSahibi => "Mert Onur"
hesap.bakiye => 0
hesap.paraYatir(100) => 100
hesap.paraCek(30) => 70
"""


class BankaHesabi:
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye = 0

    def get_bakiye(self):
        return self.bakiye

    def paraYatir(self, miktar):
        self.bakiye += miktar
        return self.bakiye  

    def paraCek(self, miktar):
        if miktar <= self.bakiye:
            self.bakiye -= miktar
            return self.bakiye
        else:
            print("Yetersiz Bakiye")
            return self.bakiye    
        
hesap = BankaHesabi("Mert Onur")
hesap.paraYatir(100)
print(hesap.get_bakiye())
hesap.paraCek(30)
print(hesap.get_bakiye())
hesap.paraCek(100)
print(hesap.get_bakiye())
