## Birden fazla değer gönderebilmek için return deyimi nasıl
## Kullanılır

def Fonk(*var1,var2):
    toplam = 0
    for item in var1:
        toplam += item
    return var1,toplam
sonuc = Fonk(12,32,43,23,12,var2=2)
print("{} sayılarının toplamı : {}".format(sonuc[0],sonuc[1]))
