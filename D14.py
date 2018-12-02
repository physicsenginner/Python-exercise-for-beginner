##mevcut = int(input("Öğrenci Sayısını Giriniz"))
##liste = []
##for i in range(0,mevcut):
##    liste.append(int(input("Öğrenci notu giriniz")))
##print(liste)
##toplam = 0
##for ogrenci in liste:
##    toplam+=ogrenci
##ortalama = toplam/len(liste)
##print(toplam/len(liste))
mevcut = int(input("Öğrenci Sayısını Giriniz"))
toplam = 0
for i in range(0,mevcut):
    toplam += int(input("Öğrenci notu giriniz"))
print(toplam/mevcut)
    

