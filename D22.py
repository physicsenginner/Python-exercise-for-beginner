##def kullanici_Giris(kullaniciAdi):
##    try:
##        int(kullaniciAdi)
##    except:
##        print("Hoşgeldiniz")
##
##kullanici_Giris("Ahmet")


##var1 = input("ilk sayı")
##var2 = input("ikinci sayı")
##try:
##    sayi1 = int(var1)
##    sayi2 = int(var2)
##    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
##except ZeroDivisionError:
##    print("Bir Sayıyı Sıfıra Bölemezsiniz")
##except ValueError:
##    print("Lütfen Sadece Sayı Giriniz")
    

##var1 = input("ilk sayı")
##var2 = input("ikinci sayı")
##try:
##    sayi1 = int(var1)
##    sayi2 = int(var2)
##    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
##except (ZeroDivisionError,ValueError):
##    print("Bir Hata Oluştu")

##adim = "0"
##var1 = input("ilk sayı")
##var2 = input("ikinci sayı")
##try:
##    sayi1 = int(var1)
##    adim = "1A"
##    sayi2 = int(var2)
##    adim = "2A"
##    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
##    adim = "3A"
##except ValueError as hata:
##    print(hata,"Hata Kodu:"+adim)



var1 = input("ilk sayı")
var2 = input("ikinci sayı")
try:
    sayi1 = int(var1)
    sayi2 = int(var2)
except:
    print("Bir Hata Oluştu",sayi1)
else:
    try:
        print(sayi1/sayi2)
    except ZeroDivisionError:
        print("Sıfıra Bölüm Hatası")


































    
































    
