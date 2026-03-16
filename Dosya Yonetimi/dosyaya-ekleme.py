#open(dosya_adi, dosya_erisme_modu) fonksiyonu ile dosya acilir ve dosya nesnesi olusturulur
#dosya_erisme_modu : dosyayi hangi amacla actigimizi belirtir
#"r" okuma modu    : okuma modu . belirtilen konumda dosya olmalidir
#"a" ekleme modu  : (append)ekleme modu . belirtilen konumda dosya varsa içeriğine ekler, yoksa oluşturur       
#r+ : okuma ve yazma modu . belirtilen konumda dosya olmalidir  

with open("dosya.txt", "a") as f: # dosya ekleme modu ile acilir
    # f.seek(0) # cursor konumu dosyanin basina getirilir 
    f.read() # dosya okunur ve cursor konumu dosyanin sonuna gelir
    f.write("Bu bir ekleme satiridir.\n") # dosyaya ekleme yapilir