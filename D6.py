##yaricap = int(input("Dairenin yarıçapını giriniz :"))
##pi = 22/7
##print(pi*yaricap*yaricap)

adi = input("Adınızı Giriniz")
soyadi = input("Soyadınızı Giriniz")
telefon = input("Telefon :")
yas = input("Yaşınızı Giriniz")

# format metodunu kullanarak ortadaki standart
# metine değişkenlerimi dağıttım
print("="*30+"""
       \n Adı: {1}
       \n Soyadı: {0}
       \n Telefonu:{3}
       \n Yaş: {2}
       \n""".format(adi,soyadi,telefon,yas)
     +"="*30)
