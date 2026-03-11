# 1 --  "Toyota , Bmw , Renault , Mercedes , Opel" elemanlarına sahip bir liste oluşturunuz.

arabalar = ["Toyota", "Bmw", "Renault", "Mercedes", "Opel"]


# 2 --  Liste kaç elemanlıdır ?

sonuc = len(arabalar)

# 3 --  Listenin ilk ve son elemanı nedir ?

ilk_eleman = arabalar[0]
son_eleman = arabalar[-1]

# 4 --  "Mercedes" ifadesi listede var mı ?

var_mi = "Mercedes" in arabalar # yada sonuc = "Mercedes" in arabalar 
                                #              "Mercedes" not in arabalar  # "Mercedes" ifadesinin listede olmadığını kontrol eder

print(f"Mercedes listede var mı? {var_mi}")

# 5 --  Listenin ilk 2 elemanını yazdırınız.

ilk_2_eleman = arabalar[:2]

print(ilk_2_eleman)

# 6 -- "Reanult" markasini "Togg" olarak güncelleyiniz.

arabalar[2] = "Togg"

# 7 --  Listenin sonuna "Audi" ve "Ford" markasını ekleyiniz.

arabalar.append("Audi")
arabalar.append("Ford")

print(arabalar)

# 8 -- Listenin son elemanını siliniz.

del arabalar[-1]  # veya arabalar.pop() kullanabilirsiniz
print(arabalar)

# 9 -- Asagidaki verileri bir liste içerisinde saklayınız.
#     studentA: Yiğit Bilgi 2010, (70,60,70)
#     studentB: Sena Turan 1999, (80,80,70)
#     studentC: Ahmet Yılmaz 2000, (85,75,80)

studentA = ["Yiğit Bilgi", 2010, (70, 60, 70)]
studentB = ["Sena Turan", 1999, (80, 80, 70)]
studentC = ["Ahmet Yılmaz", 2000, (85, 75, 80)]

students = [studentA, studentB, studentC]


# 10 -- Öğrencilerin yaşlarını hesaplayınız.

from datetime import datetime
current_year = datetime.now().year
studentA_age = current_year - studentA[1]
studentB_age = current_year - studentB[1]
studentC_age = current_year - studentC[1]

print(f"{studentA[0]}: {studentA_age} yaşında")
print(f"{studentB[0]}: {studentB_age} yaşında")     
print(f"{studentC[0]}: {studentC_age} yaşında")

# 11 -- Öğrencilerin ortalama notlarını hesaplayınız.

studentA_average = sum(studentA[2]) / len(studentA[2])
studentB_average = sum(studentB[2]) / len(studentB[2])
studentC_average = sum(studentC[2]) / len(studentC[2])

print(f"{studentA[0]}: Ortalama Not = {studentA_average}")
print(f"{studentB[0]}: Ortalama Not = {studentB_average}")  
print(f"{studentC[0]}: Ortalama Not = {studentC_average}")  