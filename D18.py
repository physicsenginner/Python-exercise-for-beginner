## ilk değişken gönderimi
def ilkFonk(var1,var2):
    print(var1 + var2)

ilkFonk(2,5)
## Farklı Sırada Değişken Gönderimi
ilkFonk(var2=6,var1=3)

## Fonksiyon içindeki parametreye varsayılan değer atama
def Fonk2(var1=0,var2=0):
    print(var1 + var2)

## Bu sayede parametresiz fonksiyon çalıştırabiliyoruz
Fonk2()

## Sayısını bilmediğimiz birden fazla değeri bir parametre adı
## altında göndermek için
def Fonk3(*args):
    toplam = 0
    for item in args:
        toplam += item
    print(toplam)

Fonk3(3,4,5,6,9,8,7,10)

def Fonk3_1(*args,islem):
    toplam = 0
    if islem == 1:
        for item in args:
            toplam += item
    print(toplam)

Fonk3_1(3,4,5,6,9,8,7,10,islem=1)

## eğer parametrenin sayını ve her bir parametreye gönderilecek
## değer sayısının bilinmemesi durumunda

def Fonk4(**kwargs):
    for key,value in kwargs.items():
        print("Gelen {}: Değer {}".format(key,value))
Fonk4(Param1 = "Bir",Param2 = "İki",deger = ["2332",["asdasd"],123123])


    












